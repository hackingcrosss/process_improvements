#!/usr/bin/env python3
"""
Ingest a single artefact: dispatch to the right converter, classify, write
workdir/<slug>/meta.json. Slug derived from path relative to inputs/, so two
files with the same basename in different subdirs do not collide.

Usage: ingest_one.py <absolute-path-to-artefact>

Prints the slug to stdout.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
INPUTS_DIR = REPO_ROOT / "inputs"
WORKDIR = REPO_ROOT / "workdir"
INGEST_DIR = REPO_ROOT / ".claude" / "skills" / "process-ingest"


def slugify(rel_path: str) -> str:
    s = rel_path.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def classify(rel_path: str, ext: str) -> tuple[str, str]:
    rp = rel_path.lower()
    engagement = "unknown"
    doc_type = "unknown"

    if "threatscenario" in rp or "threat-scenario" in rp or "threat_scenario" in rp or "0. threat scenarios" in rp:
        engagement = "threat-scenario"
    elif "operations" in rp or "1. operations" in rp:
        engagement = "operation"
    elif "exercise" in rp or "2. exercises" in rp:
        engagement = "exercise"
    elif "physical" in rp or "social" in rp:
        engagement = "cross-cutting"
    elif "methodology" in rp or "research" in rp or "bloodhound" in rp or "redteaming" in rp or "apts" in rp:
        engagement = "cross-cutting"

    if ext == ".drawio" or "diagram" in rp or any(k in rp for k in (
        "networkmap", "infra", "deconfliction", "perdigueiro",
        "redteamprocess", "soc-rt", "soc_rt",
    )):
        doc_type = "diagram"
    elif "questionnaire" in rp or "template" in rp:
        doc_type = "template"
    elif ext == ".pptx" and "redteaming" in rp:
        doc_type = "methodology"
    elif ext == ".pptx" and "apts" in rp:
        doc_type = "research-process"
    elif "methodology" in rp:
        doc_type = "methodology"
    elif "research" in rp:
        doc_type = "research-process"
    elif "process" in rp or "sop" in rp:
        doc_type = "engagement-sop"

    return engagement, doc_type


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def run_capturing(cmd: list[str]) -> tuple[int, str]:
    """Run a command and return (returncode, stderr_text). Does not raise."""
    proc = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return proc.returncode, proc.stderr.decode(errors="replace").strip()


def ingest(input_path: Path) -> str:
    if not input_path.is_file():
        raise SystemExit(f"not a file: {input_path}")

    rel = input_path.resolve().relative_to(INPUTS_DIR.resolve())
    slug = slugify(str(rel))
    out_dir = WORKDIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    ext = input_path.suffix.lower()
    tooling = ""
    warnings: list[str] = []

    if ext == ".docx":
        run(["python3", str(INGEST_DIR / "docx_to_md.py"), str(input_path), str(out_dir)])
        tooling = "docx_to_md.py"
    elif ext == ".pptx":
        rc, err = run_capturing(["python3", str(INGEST_DIR / "pptx_to_md.py"), str(input_path), str(out_dir)])
        if rc == 0:
            tooling = "pptx_to_md.py"
        elif rc == 3:
            tooling = "pptx_to_md.py (skipped)"
            warnings.append("legacy .ppt binary format with misleading .pptx extension; not supported. Convert to .pptx with PowerPoint/LibreOffice and re-ingest.")
        else:
            tooling = "pptx_to_md.py (failed)"
            warnings.append(f"pptx_to_md.py failed (rc={rc}): {err[:300]}")
    elif ext in {".drawio", ".xml"}:
        run(["python3", str(INGEST_DIR / "drawio_to_graph.py"), str(input_path), str(out_dir)])
        tooling = "drawio_to_graph.py"
    elif ext == ".vsdx":
        run(["python3", str(INGEST_DIR / "vsdx_to_graph.py"), str(input_path), str(out_dir)])
        tooling = "vsdx_to_graph.py"
    elif ext == ".pdf":
        if shutil.which("pdftotext"):
            try:
                subprocess.run(
                    ["pdftotext", "-layout", str(input_path), str(out_dir / "content.md")],
                    check=True, stderr=subprocess.PIPE,
                )
                tooling = "pdftotext"
            except subprocess.CalledProcessError as e:
                warnings.append(f"pdftotext failed: {e.stderr.decode(errors='replace')[:200]}")
        else:
            warnings.append("pdftotext not installed; pdf text not extracted")
    elif ext in {".png", ".jpg", ".jpeg", ".svg"}:
        # Vision pass deferred to the calling agent.
        (out_dir / "captions.md.todo").write_text("vision pass needed\n", encoding="utf-8")
        tooling = "vision-pending"
        warnings.append("image artefact: requires vision pass to populate captions.md")
    else:
        warnings.append(f"unsupported extension {ext}")

    engagement, doc_type = classify(str(rel), ext)
    meta = {
        "source_path": str(input_path),
        "rel_path": str(rel),
        "slug": slug,
        "doc_type_guess": doc_type,
        "engagement_type_guess": engagement,
        "tooling_used": tooling,
        "warnings": warnings,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return slug


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: ingest_one.py <path>", file=sys.stderr)
        sys.exit(2)
    print(ingest(Path(sys.argv[1])))
