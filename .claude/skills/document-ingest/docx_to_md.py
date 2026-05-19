#!/usr/bin/env python3
"""
Minimal .docx -> markdown converter using only the standard library.

Usage: docx_to_md.py <input.docx> <workdir>

Produces <workdir>/content.md preserving heading levels (Heading1..Heading9) and
bullet/numbered lists. Tables are rendered as GitHub-flavored markdown tables.
"""
from __future__ import annotations

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def text_of(elem) -> str:
    parts = []
    for t in elem.iter(f"{W}t"):
        parts.append(t.text or "")
    for _ in elem.iter(f"{W}tab"):
        parts.append("\t")
    for _ in elem.iter(f"{W}br"):
        parts.append("\n")
    return "".join(parts)


def heading_level(p) -> int | None:
    pStyle = p.find(f"{W}pPr/{W}pStyle")
    if pStyle is None:
        return None
    val = pStyle.get(f"{W}val", "")
    m = re.match(r"Heading(\d+)$", val)
    if m:
        return int(m.group(1))
    if val.lower() in {"title"}:
        return 1
    return None


def list_info(p):
    numPr = p.find(f"{W}pPr/{W}numPr")
    if numPr is None:
        return None
    ilvl = numPr.find(f"{W}ilvl")
    numId = numPr.find(f"{W}numId")
    return (
        int(ilvl.get(f"{W}val", "0")) if ilvl is not None else 0,
        int(numId.get(f"{W}val", "0")) if numId is not None else 0,
    )


def render_table(tbl) -> str:
    rows = []
    for tr in tbl.findall(f"{W}tr"):
        cells = []
        for tc in tr.findall(f"{W}tc"):
            cell_text = " ".join(
                text_of(p).strip() for p in tc.findall(f"{W}p")
            ).strip()
            cells.append(cell_text.replace("|", "\\|") or " ")
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [" "] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "|".join(["---"] * width) + "|"]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def convert(docx_path: Path, workdir: Path) -> None:
    workdir.mkdir(parents=True, exist_ok=True)
    out_md = workdir / "content.md"

    with zipfile.ZipFile(docx_path) as z:
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)

    body = tree.getroot().find(f"{W}body")
    lines: list[str] = []
    for child in list(body):
        tag = child.tag
        if tag == f"{W}p":
            txt = text_of(child).strip()
            lvl = heading_level(child)
            if lvl is not None and txt:
                lines.append("#" * min(lvl, 6) + " " + txt)
                lines.append("")
                continue
            li = list_info(child)
            if li is not None and txt:
                ilvl, _ = li
                lines.append("  " * ilvl + "- " + txt)
                continue
            if txt:
                lines.append(txt)
                lines.append("")
        elif tag == f"{W}tbl":
            md = render_table(child)
            if md:
                lines.append(md)
                lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out_md} ({len(lines)} lines)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: docx_to_md.py <input.docx> <workdir>", file=sys.stderr)
        sys.exit(2)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
