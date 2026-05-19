#!/usr/bin/env python3
"""
Domain-aware input selector for the generic document analyzer.

Usage:
  select_inputs.py [<input-dir>] [--domain generic|process|cv]

Output JSON:
  {
    "selected": [<absolute paths>],
    "excluded": [{"path": ..., "reason": ...}],
    "unsupported": [{"path": ..., "ext": ...}]
  }

Domain policies:
  - process: prefer .docx over .pdf and keep only the highest version of each
    logical prose document; diagrams/images are independent.
  - cv: keep all evaluable documents in the candidate bundle; do not collapse
    versions because older CVs, cover letters, or portfolios may be relevant.
  - generic: keep all evaluable documents except known render duplicates.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EVALUABLE_EXTS = {
    ".docx", ".pdf", ".pptx", ".vsdx", ".drawio", ".xml",
    ".png", ".jpg", ".jpeg", ".svg", ".md", ".markdown", ".txt",
}
PROSE_EXTS = {".docx", ".pdf", ".md", ".markdown", ".txt"}
KNOWN_UNSUPPORTED = {".ppt", ".xlsx", ".xls", ".csv", ".xmind", ".vsd", ".odt", ".odp", ".ods", ".rtf"}

VERSION_RE = re.compile(
    r"""
    [\s\-_(\[]*
    [Vv]?
    \s*
    (\d+(?:[\.\-_ ]\d+)*)
    \s*
    [)\]]?
    \s*$
    """,
    re.VERBOSE,
)


def _normalize(s: str) -> str:
    return re.sub(r"[\s\-_]+", " ", s).strip().lower()


def parse_version(stem: str) -> tuple[str, tuple[int, ...] | None]:
    m = VERSION_RE.search(stem)
    if not m:
        return _normalize(stem), None
    raw = m.group(1)
    parts = re.split(r"[\.\-_ ]+", raw)
    try:
        version = tuple(int(p) for p in parts if p != "")
    except ValueError:
        return _normalize(stem), None
    if not version:
        return _normalize(stem), None
    logical = stem[: m.start()]
    return _normalize(logical), version


def _is_drawio_render(path: Path) -> bool:
    return path.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg"} and path.stem.lower().endswith(".drawio")


def _drop_drawio_renders(files: list[Path]) -> tuple[list[Path], list[dict]]:
    file_set = {p.resolve() for p in files}
    kept: list[Path] = []
    excluded: list[dict] = []
    for p in files:
        if _is_drawio_render(p):
            source = p.with_name(p.stem)  # X.drawio.png -> X.drawio
            if source.resolve() in file_set:
                excluded.append({"path": str(p), "reason": f"drawio render; source exists at {source.name}"})
                continue
        kept.append(p)
    return kept, excluded


def _partition_supported(files: list[Path]) -> tuple[list[Path], list[dict], list[dict]]:
    supported: list[Path] = []
    excluded: list[dict] = []
    unsupported: list[dict] = []
    for p in files:
        ext = p.suffix.lower()
        if ext in KNOWN_UNSUPPORTED:
            unsupported.append({"path": str(p), "ext": ext})
        elif ext not in EVALUABLE_EXTS:
            excluded.append({"path": str(p), "reason": f"unsupported extension '{ext or '<none>'}'"})
        else:
            supported.append(p)
    return supported, excluded, unsupported


def _select_all(input_dir: Path, files: list[Path]) -> list[Path]:
    return sorted({p.resolve() for p in files}, key=lambda p: str(p).lower())


def _select_process(input_dir: Path, files: list[Path]) -> tuple[list[Path], list[dict]]:
    selected: list[Path] = []
    excluded: list[dict] = []

    groups: dict[tuple[str, str, str], list[tuple[Path, str, tuple[int, ...] | None]]] = {}
    for p in files:
        ext = p.suffix.lower()
        logical, version = parse_version(p.stem)
        fmt_class = "prose" if ext in {".docx", ".pdf"} else ext
        try:
            parent_rel = str(p.parent.relative_to(input_dir))
        except ValueError:
            parent_rel = str(p.parent)
        groups.setdefault((parent_rel, logical, fmt_class), []).append((p, ext, version))

    for (parent_rel, logical, fmt_class), items in groups.items():
        if fmt_class == "prose":
            docx_items = [x for x in items if x[1] == ".docx"]
            pdf_items = [x for x in items if x[1] == ".pdf"]
            if docx_items:
                pool = docx_items
                for p, _, _ in pdf_items:
                    excluded.append({"path": str(p), "reason": f".docx variant exists for logical doc \"{logical}\" in {parent_rel}"})
            else:
                pool = pdf_items
        else:
            pool = items

        versioned = [x for x in pool if x[2] is not None]
        if versioned:
            max_v = max(x[2] for x in versioned)
            chosen = [x for x in versioned if x[2] == max_v]
            for p, _, v in pool:
                if v != max_v:
                    excluded.append({
                        "path": str(p),
                        "reason": (
                            "older version "
                            f"{'.'.join(map(str, v)) if v else 'unversioned'} "
                            f"superseded by {'.'.join(map(str, max_v))}"
                        ),
                    })
        else:
            chosen = pool

        selected.extend(p for p, _, _ in chosen)

    return sorted({p.resolve() for p in selected}, key=lambda p: str(p).lower()), excluded


def select(input_dir: Path, domain: str) -> dict:
    files = sorted(p for p in input_dir.rglob("*") if p.is_file())
    after_render_dedup, render_excluded = _drop_drawio_renders(files)
    supported, ext_excluded, unsupported = _partition_supported(after_render_dedup)

    excluded = render_excluded + ext_excluded
    if domain == "process":
        selected, process_excluded = _select_process(input_dir, supported)
        excluded.extend(process_excluded)
    else:
        selected = _select_all(input_dir, supported)

    return {
        "selected": [str(p) for p in selected],
        "excluded": sorted(excluded, key=lambda d: d["path"]),
        "unsupported": sorted(unsupported, key=lambda d: d["path"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Select analyzable inputs for a domain.")
    parser.add_argument("input_dir", nargs="?", default="inputs")
    parser.add_argument("--domain", default="generic", choices=["generic", "process", "cv"])
    args = parser.parse_args()
    in_dir = Path(args.input_dir)
    if not in_dir.is_dir():
        print(json.dumps({"selected": [], "excluded": [], "unsupported": [], "error": f"not a directory: {in_dir}"}))
        return 1
    print(json.dumps(select(in_dir, args.domain), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
