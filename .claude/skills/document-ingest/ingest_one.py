#!/usr/bin/env python3
"""
Generic document ingest entrypoint.

Converts a single source artefact into a normalized representation under
workdir/<slug>/ and writes a domain-neutral meta.json. Domain-specific fields
are stored under meta["domain_hints"]. Compatibility top-level fields
(doc_type_guess / engagement_type_guess) are retained for existing process
analyzers.

Usage:
  ingest_one.py <path-to-artefact> [--domain generic|process|cv]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUTS_DIR = REPO_ROOT / "inputs"
DEFAULT_WORKDIR = REPO_ROOT / "workdir"
INGEST_DIR = Path(__file__).resolve().parent

TEXT_EXTS = {".md", ".markdown", ".txt"}
PROSE_EXTS = {".docx", ".pdf", *TEXT_EXTS}
SLIDE_EXTS = {".pptx"}
DIAGRAM_EXTS = {".drawio", ".xml", ".vsdx"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".svg"}
SUPPORTED_EXTS = PROSE_EXTS | SLIDE_EXTS | DIAGRAM_EXTS | IMAGE_EXTS

PROCESS_DOC_TYPES = {"methodology", "engagement-sop", "research-process", "diagram", "policy", "template", "unknown"}


def slugify(rel_path: str) -> str:
    s = rel_path.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "artefact"


def _safe_rel(input_path: Path, inputs_dir: Path) -> str:
    resolved = input_path.resolve()
    try:
        return str(resolved.relative_to(inputs_dir.resolve()))
    except ValueError:
        return input_path.name


def _read_sample(out_dir: Path, limit_chars: int = 20000) -> str:
    for name in ("content.md", "captions.md"):
        p = out_dir / name
        if p.exists():
            return p.read_text(encoding="utf-8", errors="replace")[:limit_chars]
    return ""


def classify_process(rel_path: str, ext: str, sample_text: str = "") -> tuple[str, str]:
    """Return (engagement_type_guess, process_doc_type_guess)."""
    rp = rel_path.lower()
    txt = sample_text.lower()
    combined = f"{rp}\n{txt[:5000]}"
    engagement = "unknown"
    doc_type = "unknown"

    if any(k in combined for k in ("threatscenario", "threat scenario", "threat-scenario", "threat_scenario", "0. threat scenarios")):
        engagement = "threat-scenario"
    elif any(k in combined for k in ("operations_process", "operations process", "1. operations", "red team operation")):
        engagement = "operation"
    elif any(k in combined for k in ("exercises_process", "exercises process", "2. exercises", "red team exercise")):
        engagement = "exercise"
    elif any(k in combined for k in ("physical", "social", "methodology", "research", "bloodhound", "redteaming", "apts")):
        engagement = "cross-cutting"

    if ext in DIAGRAM_EXTS or "diagram" in rp or any(k in rp for k in (
        "networkmap", "infra", "deconfliction", "perdigueiro",
        "redteamprocess", "soc-rt", "soc_rt",
    )):
        doc_type = "diagram"
    elif "questionnaire" in rp or "template" in rp:
        doc_type = "template"
    elif "policy" in rp:
        doc_type = "policy"
    elif "methodology" in rp or (ext == ".pptx" and "redteaming" in rp):
        doc_type = "methodology"
    elif "research" in rp or (ext == ".pptx" and "apts" in rp):
        doc_type = "research-process"
    elif "process" in rp or "sop" in rp:
        doc_type = "engagement-sop"
    elif "policy" in txt:
        doc_type = "policy"
    elif "standard operating procedure" in txt or re.search(r"^#+ .*process", sample_text, flags=re.I | re.M):
        doc_type = "engagement-sop"

    return engagement, doc_type


def classify_generic(rel_path: str, ext: str, sample_text: str, requested_domain: str) -> dict:
    rp = rel_path.lower()
    txt = sample_text.lower()
    combined = f"{rp}\n{txt[:8000]}"

    if ext in DIAGRAM_EXTS:
        document_kind = "diagram"
    elif ext in IMAGE_EXTS:
        document_kind = "image"
    elif ext in SLIDE_EXTS:
        document_kind = "slide-deck"
    elif ext in PROSE_EXTS:
        document_kind = "prose-document"
    else:
        document_kind = "unknown"

    doc_family = "unknown"
    doc_type = document_kind if document_kind != "unknown" else "unknown"

    # CV / recruiting bundle detection first, because filenames can be very short.
    cv_markers = ["curriculum vitae", "resume", "résumé", "cv", "work experience", "employment history"]
    cover_markers = ["cover letter", "motivation letter"]
    jd_markers = ["job description", "role description", "requirements", "responsibilities", "must have", "nice to have"]

    stem_tokens = re.split(r"[^a-z0-9]+", Path(rel_path).stem.lower())
    if requested_domain == "cv" or any(k in combined for k in cover_markers + jd_markers) or "resume" in stem_tokens or "cv" in stem_tokens:
        doc_family = "cv"
        if any(k in combined for k in cover_markers):
            doc_type = "cover-letter"
        elif any(k in combined for k in jd_markers) and not any(k in combined for k in cv_markers[:3]):
            doc_type = "job-description"
        else:
            doc_type = "cv"

    process_engagement, process_doc_type = classify_process(rel_path, ext, sample_text)
    if requested_domain == "process" or process_doc_type != "unknown" or process_engagement != "unknown":
        # Do not overwrite explicit CV classification unless process was requested.
        if requested_domain == "process" or doc_family == "unknown":
            doc_family = "process"
            doc_type = process_doc_type

    if doc_family == "unknown":
        if "policy" in combined:
            doc_family = "governance"
            doc_type = "policy"
        elif "template" in combined:
            doc_family = "template"
            doc_type = "template"
        elif document_kind in {"diagram", "image", "slide-deck"}:
            doc_family = document_kind
            doc_type = document_kind

    return {
        "requested_domain": requested_domain,
        "doc_family_guess": doc_family,
        "doc_type_guess": doc_type,
        "document_kind_guess": document_kind,
        "domain_hints": {
            "process": {
                "doc_type_guess": process_doc_type,
                "engagement_type_guess": process_engagement,
            }
        },
    }


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def run_capturing(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return proc.returncode, proc.stderr.decode(errors="replace").strip()


def ingest(input_path: Path, *, domain: str, inputs_dir: Path, workdir: Path) -> str:
    if not input_path.is_file():
        raise SystemExit(f"not a file: {input_path}")

    rel = _safe_rel(input_path, inputs_dir)
    slug = slugify(rel)
    out_dir = workdir / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    ext = input_path.suffix.lower()
    tooling: list[str] = []
    warnings: list[str] = []
    content_files: list[str] = []

    if ext == ".docx":
        run(["python3", str(INGEST_DIR / "docx_to_md.py"), str(input_path), str(out_dir)])
        tooling.append("docx_to_md.py")
        content_files.append("content.md")
    elif ext == ".pptx":
        rc, err = run_capturing(["python3", str(INGEST_DIR / "pptx_to_md.py"), str(input_path), str(out_dir)])
        if rc == 0:
            tooling.append("pptx_to_md.py")
            content_files.append("content.md")
        elif rc == 3:
            tooling.append("pptx_to_md.py (skipped)")
            warnings.append("legacy .ppt binary format with misleading .pptx extension; not supported. Convert to .pptx with PowerPoint/LibreOffice and re-ingest.")
        else:
            tooling.append("pptx_to_md.py (failed)")
            warnings.append(f"pptx_to_md.py failed (rc={rc}): {err[:300]}")
    elif ext in {".drawio", ".xml"}:
        run(["python3", str(INGEST_DIR / "drawio_to_graph.py"), str(input_path), str(out_dir)])
        tooling.append("drawio_to_graph.py")
        content_files.append("diagram.json")
    elif ext == ".vsdx":
        run(["python3", str(INGEST_DIR / "vsdx_to_graph.py"), str(input_path), str(out_dir)])
        tooling.append("vsdx_to_graph.py")
        content_files.append("diagram.json")
    elif ext == ".pdf":
        if shutil.which("pdftotext"):
            try:
                subprocess.run(
                    ["pdftotext", "-layout", str(input_path), str(out_dir / "content.md")],
                    check=True, stderr=subprocess.PIPE,
                )
                tooling.append("pdftotext")
                content_files.append("content.md")
            except subprocess.CalledProcessError as e:
                tooling.append("pdftotext (failed)")
                warnings.append(f"pdftotext failed: {e.stderr.decode(errors='replace')[:200]}")
        else:
            warnings.append("pdftotext not installed; pdf text not extracted")
    elif ext in TEXT_EXTS:
        text = input_path.read_text(encoding="utf-8", errors="replace")
        (out_dir / "content.md").write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        tooling.append("text-copy")
        content_files.append("content.md")
    elif ext in IMAGE_EXTS:
        (out_dir / "captions.md.todo").write_text("vision pass needed\n", encoding="utf-8")
        tooling.append("vision-pending")
        warnings.append("image artefact: requires vision/OCR pass to populate captions.md")
        content_files.append("captions.md.todo")
    else:
        warnings.append(f"unsupported extension {ext}")

    sample = _read_sample(out_dir)
    classification = classify_generic(rel, ext, sample, domain)
    process_hint = classification["domain_hints"]["process"]

    # Process compatibility: existing evaluators read these top-level fields.
    top_level_doc_type = classification["doc_type_guess"]
    top_level_engagement = None
    if classification["doc_family_guess"] == "process" or domain == "process":
        top_level_doc_type = process_hint["doc_type_guess"]
        top_level_engagement = process_hint["engagement_type_guess"]

    meta = {
        "source_path": str(input_path.resolve()),
        "rel_path": rel,
        "slug": slug,
        "file_name": input_path.name,
        "extension": ext,
        "content_files": content_files,
        "requested_domain": domain,
        "doc_family_guess": classification["doc_family_guess"],
        "document_kind_guess": classification["document_kind_guess"],
        "doc_type_guess": top_level_doc_type,
        "domain_hints": classification["domain_hints"],
        "engagement_type_guess": top_level_engagement,
        "tooling_used": ", ".join(tooling),
        "warnings": warnings,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return slug


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingest one artefact into workdir/<slug>.")
    parser.add_argument("input_path")
    parser.add_argument("--domain", default="generic", choices=["generic", "process", "cv"], help="Domain hint for classification only; conversion stays generic.")
    parser.add_argument("--inputs-dir", default=str(DEFAULT_INPUTS_DIR))
    parser.add_argument("--workdir", default=str(DEFAULT_WORKDIR))
    args = parser.parse_args(argv)

    slug = ingest(Path(args.input_path), domain=args.domain, inputs_dir=Path(args.inputs_dir), workdir=Path(args.workdir))
    print(slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
