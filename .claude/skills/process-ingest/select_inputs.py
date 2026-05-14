#!/usr/bin/env python3
"""
Decide which files in inputs/ should be evaluated.

Walks inputs/ recursively. Groups files by (parent-directory, logical-name,
format-class) so two unrelated docs in different folders don't collide.

Rules (per project memory):
  1. Format preference: when both .docx and .pdf exist for the same logical
     document, evaluate only the .docx.
  2. Version selection: analyse only the highest version of each logical
     document. Versions are detected at the end of the stem in patterns like
     "name v1.0", "name_V2", "name (1.0)", "name - 2.1.3".
  3. Drawio renders (X.drawio.png) are dropped when the source X.drawio is
     present in the same directory; otherwise kept as a standalone image.
  4. Other formats (.vsdx, .drawio, .xml, raster images) are independent
     groups and don't compete with .docx / .pdf.

Output (JSON to stdout):
  {
    "selected":   [<absolute paths chosen>],
    "excluded":   [{"path": <abs>, "reason": "<why>"}, ...],
    "unsupported":[{"path": <abs>, "ext": "<.pptx|.xlsx|...>"}, ...]
  }

`unsupported` is reported separately from `excluded` so the orchestrator can
surface format gaps (e.g. a .pptx the team relies on but ingest can't read yet).

Usage:
  select_inputs.py [<input-dir>]   # defaults to ./inputs
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EVALUABLE_EXTS = {".docx", ".pdf", ".pptx", ".vsdx", ".drawio", ".xml", ".png", ".jpg", ".jpeg", ".svg"}
PROSE_EXTS = {".docx", ".pdf"}
KNOWN_UNSUPPORTED = {".ppt", ".xlsx", ".xls", ".csv", ".xmind", ".vsd", ".odt", ".odp", ".ods"}

VERSION_RE = re.compile(
    r"""
    [\s\-_(\[]*          # optional separators / opening bracket
    [Vv]?                # optional V prefix
    \s*
    (\d+(?:[\.\-_ ]\d+)*)  # version digits (group 1)
    \s*
    [)\]]?               # optional closing bracket
    \s*$                 # must end the stem
    """,
    re.VERBOSE,
)


def _normalize(s: str) -> str:
    return re.sub(r"[\s\-_]+", " ", s).strip().lower()


def parse_version(stem: str) -> tuple[str, tuple[int, ...] | None]:
    """Return (logical_name_normalized, version_tuple_or_None)."""
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
    """X.drawio.png — a PNG export of a drawio source."""
    return path.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg"} and path.stem.lower().endswith(".drawio")


def select(input_dir: Path) -> dict:
    files = sorted(p for p in input_dir.rglob("*") if p.is_file())
    selected: list[Path] = []
    excluded: list[dict] = []
    unsupported: list[dict] = []

    # Drop drawio renders when the source exists alongside.
    file_set = {p.resolve() for p in files}
    after_render_dedup: list[Path] = []
    for p in files:
        if _is_drawio_render(p):
            source = p.with_name(p.stem)  # X.drawio.png -> X.drawio
            if source.resolve() in file_set:
                excluded.append({
                    "path": str(p),
                    "reason": f"drawio render; source exists at {source.name}",
                })
                continue
        after_render_dedup.append(p)

    # Group key: (parent-dir-relative, logical_name, format-class)
    groups: dict[tuple[str, str, str], list[tuple[Path, str, tuple[int, ...] | None]]] = {}

    for p in after_render_dedup:
        ext = p.suffix.lower()
        if ext in KNOWN_UNSUPPORTED:
            unsupported.append({"path": str(p), "ext": ext})
            continue
        if ext not in EVALUABLE_EXTS:
            excluded.append({"path": str(p), "reason": f"unsupported extension '{ext or '<none>'}'"})
            continue
        logical, version = parse_version(p.stem)
        fmt_class = "prose" if ext in PROSE_EXTS else ext
        try:
            parent_rel = str(p.parent.relative_to(input_dir))
        except ValueError:
            parent_rel = str(p.parent)
        key = (parent_rel, logical, fmt_class)
        groups.setdefault(key, []).append((p, ext, version))

    for (parent_rel, logical, fmt_class), items in groups.items():
        # Format preference within the prose class: .docx wins over .pdf
        if fmt_class == "prose":
            docx_items = [x for x in items if x[1] == ".docx"]
            pdf_items = [x for x in items if x[1] == ".pdf"]
            if docx_items:
                pool = docx_items
                for p, _, _ in pdf_items:
                    excluded.append({
                        "path": str(p),
                        "reason": f".docx variant exists for logical doc \"{logical}\" in {parent_rel}",
                    })
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

        for p, _, _ in chosen:
            selected.append(p)

    selected_sorted = sorted({p.resolve() for p in selected}, key=lambda p: str(p).lower())
    return {
        "selected": [str(p) for p in selected_sorted],
        "excluded": sorted(excluded, key=lambda d: d["path"]),
        "unsupported": sorted(unsupported, key=lambda d: d["path"]),
    }


if __name__ == "__main__":
    in_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("inputs")
    if not in_dir.is_dir():
        print(json.dumps({"selected": [], "excluded": [], "unsupported": [], "error": f"not a directory: {in_dir}"}))
        sys.exit(1)
    print(json.dumps(select(in_dir), indent=2))
