#!/usr/bin/env python3
"""
Minimal .pptx -> markdown converter using only the standard library.

Usage: pptx_to_md.py <input.pptx> <workdir>

Produces <workdir>/content.md with one section per slide, in canonical
presentation order (read from ppt/presentation.xml -> sldIdLst, resolved via
ppt/_rels/presentation.xml.rels). Each slide section preserves:
  - title placeholder (rendered as ## "Slide N — <title>")
  - body text frames with bullet indent (lvl="..." -> indented "- " bullets)
  - tables as GitHub-flavored markdown tables
  - speaker notes (rendered as a blockquote at the end of the slide)

Images, charts, SmartArt, and embedded objects are not extracted; their
presence is noted as a `[image]` / `[chart]` placeholder so a downstream
evaluator can tell the slide isn't text-only.
"""
from __future__ import annotations

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PKG_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def _para_text(p_elem) -> str:
    """Concatenate all <a:t> runs in an <a:p>, joining tabs/breaks sensibly."""
    parts: list[str] = []
    for child in p_elem.iter():
        tag = child.tag
        if tag == f"{A}t" and child.text:
            parts.append(child.text)
        elif tag == f"{A}br":
            parts.append("\n")
        elif tag == f"{A}tab":
            parts.append("\t")
    return "".join(parts)


def _para_level(p_elem) -> int:
    pPr = p_elem.find(f"{A}pPr")
    if pPr is None:
        return 0
    lvl = pPr.get("lvl")
    try:
        return int(lvl) if lvl is not None else 0
    except ValueError:
        return 0


def _is_bullet(p_elem) -> bool:
    """A pPr without <a:buNone/> implies a bullet by default in pptx."""
    pPr = p_elem.find(f"{A}pPr")
    if pPr is None:
        return False
    if pPr.find(f"{A}buNone") is not None:
        return False
    return any(pPr.find(f"{A}{tag}") is not None for tag in ("buChar", "buAutoNum", "buFont")) or True


def _placeholder_type(sp_elem) -> str | None:
    ph = sp_elem.find(f".//{P}nvSpPr/{P}nvPr/{P}ph")
    if ph is None:
        return None
    return ph.get("type") or "body"


def _render_paragraphs(tx_body) -> list[str]:
    out: list[str] = []
    if tx_body is None:
        return out
    for p in tx_body.findall(f"{A}p"):
        txt = _para_text(p).strip()
        if not txt:
            continue
        lvl = _para_level(p)
        if _is_bullet(p) and lvl >= 0:
            out.append("  " * lvl + "- " + txt)
        else:
            out.append(txt)
    return out


def _render_table(tbl_elem) -> list[str]:
    rows: list[list[str]] = []
    for tr in tbl_elem.findall(f".//{A}tr"):
        cells: list[str] = []
        for tc in tr.findall(f"{A}tc"):
            txBody = tc.find(f"{A}txBody")
            cell_lines = _render_paragraphs(txBody)
            joined = " ".join(line.lstrip("- ").strip() for line in cell_lines).replace("|", "\\|")
            cells.append(joined or " ")
        if cells:
            rows.append(cells)
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [" "] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "|".join(["---"] * width) + "|"]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return lines


def _media_marker(sp_or_pic_tag: str) -> str | None:
    if sp_or_pic_tag == f"{P}pic":
        return "[image]"
    if sp_or_pic_tag == f"{P}graphicFrame":
        return None  # could be a table or chart; resolved at deeper level
    return None


def _iter_shapes_in_order(sp_tree):
    """Yield top-level shapes (sp / pic / graphicFrame / grpSp) in spTree order."""
    if sp_tree is None:
        return
    for child in list(sp_tree):
        tag = child.tag
        if tag in {f"{P}sp", f"{P}pic", f"{P}graphicFrame"}:
            yield child
        elif tag == f"{P}grpSp":
            # recurse into groups
            yield from _iter_shapes_in_order(child)


def _slide_title(sp_tree) -> str | None:
    for shape in _iter_shapes_in_order(sp_tree):
        if shape.tag != f"{P}sp":
            continue
        ph_type = _placeholder_type(shape)
        if ph_type in {"title", "ctrTitle"}:
            txBody = shape.find(f"{P}txBody")
            paras = _render_paragraphs(txBody)
            stripped = [p.lstrip("- ").strip() for p in paras]
            text = " ".join(filter(None, stripped)).strip()
            return text or None
    return None


def _render_slide(slide_xml_bytes: bytes, notes_xml_bytes: bytes | None) -> tuple[str | None, list[str], bool]:
    """Return (title, body_lines, has_media)."""
    root = ET.fromstring(slide_xml_bytes)
    sp_tree = root.find(f"{P}cSld/{P}spTree")
    title = _slide_title(sp_tree)
    body_lines: list[str] = []
    has_media = False

    for shape in _iter_shapes_in_order(sp_tree):
        tag = shape.tag
        if tag == f"{P}sp":
            if _placeholder_type(shape) in {"title", "ctrTitle"}:
                continue
            txBody = shape.find(f"{P}txBody")
            paras = _render_paragraphs(txBody)
            if paras:
                body_lines.extend(paras)
                body_lines.append("")
        elif tag == f"{P}pic":
            has_media = True
            body_lines.append("[image]")
            body_lines.append("")
        elif tag == f"{P}graphicFrame":
            tbl = shape.find(f".//{A}tbl")
            if tbl is not None:
                table_lines = _render_table(tbl)
                if table_lines:
                    body_lines.extend(table_lines)
                    body_lines.append("")
            else:
                has_media = True
                body_lines.append("[chart-or-smartart]")
                body_lines.append("")

    if notes_xml_bytes:
        try:
            notes_root = ET.fromstring(notes_xml_bytes)
            notes_sp_tree = notes_root.find(f"{P}cSld/{P}spTree")
            notes_lines: list[str] = []
            for shape in _iter_shapes_in_order(notes_sp_tree):
                if shape.tag != f"{P}sp":
                    continue
                if _placeholder_type(shape) != "body":
                    continue
                txBody = shape.find(f"{P}txBody")
                paras = _render_paragraphs(txBody)
                for line in paras:
                    notes_lines.append(line.lstrip("- ").strip())
            notes_lines = [n for n in notes_lines if n]
            if notes_lines:
                body_lines.append("> **Notes:** " + " ".join(notes_lines))
                body_lines.append("")
        except ET.ParseError:
            pass

    while body_lines and body_lines[-1] == "":
        body_lines.pop()
    return title, body_lines, has_media


def _slide_order(z: zipfile.ZipFile) -> list[str]:
    """Return slide part names in canonical presentation order."""
    try:
        with z.open("ppt/presentation.xml") as f:
            pres = ET.parse(f).getroot()
        sld_id_lst = pres.find(f"{P}sldIdLst")
        if sld_id_lst is None:
            raise KeyError
        rids = [s.get(f"{R}id") for s in sld_id_lst.findall(f"{P}sldId")]
        with z.open("ppt/_rels/presentation.xml.rels") as f:
            rels = ET.parse(f).getroot()
        targets = {rel.get("Id"): rel.get("Target") for rel in rels.findall(f"{PKG_REL}Relationship")}
        ordered: list[str] = []
        for rid in rids:
            tgt = targets.get(rid)
            if not tgt:
                continue
            # Targets are like "slides/slide1.xml" — make absolute within the zip.
            part = tgt if tgt.startswith("/") else "ppt/" + tgt
            part = part.lstrip("/")
            ordered.append(part)
        return ordered
    except Exception:
        # Fallback: sort slide files by numeric suffix.
        slides = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        return sorted(slides, key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)))


def _notes_for(z: zipfile.ZipFile, slide_part: str) -> bytes | None:
    rels_name = slide_part.rsplit("/", 1)[0] + "/_rels/" + slide_part.rsplit("/", 1)[1] + ".rels"
    try:
        with z.open(rels_name) as f:
            rels = ET.parse(f).getroot()
    except KeyError:
        return None
    for rel in rels.findall(f"{PKG_REL}Relationship"):
        if rel.get("Type", "").endswith("/notesSlide"):
            tgt = rel.get("Target")
            base = slide_part.rsplit("/", 1)[0]
            notes_part = (base + "/" + tgt) if not tgt.startswith("/") else tgt.lstrip("/")
            # Normalize ../ segments
            parts: list[str] = []
            for seg in notes_part.split("/"):
                if seg == "..":
                    if parts:
                        parts.pop()
                elif seg and seg != ".":
                    parts.append(seg)
            notes_path = "/".join(parts)
            try:
                with z.open(notes_path) as f:
                    return f.read()
            except KeyError:
                return None
    return None


OLE_MAGIC = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"


def convert(input_path: Path, workdir: Path) -> None:
    workdir.mkdir(parents=True, exist_ok=True)
    out_md = workdir / "content.md"

    # Detect legacy .ppt (OLE compound document) misnamed with .pptx
    with input_path.open("rb") as f:
        head = f.read(8)
    if head == OLE_MAGIC:
        print(
            f"legacy-ppt-format: {input_path} is a binary .ppt (OLE compound) "
            "with a misleading .pptx extension; not supported by this ingest",
            file=sys.stderr,
        )
        sys.exit(3)

    lines: list[str] = []
    media_slide_count = 0
    with zipfile.ZipFile(input_path) as z:
        slides = _slide_order(z)
        for idx, slide_part in enumerate(slides, start=1):
            try:
                with z.open(slide_part) as f:
                    slide_bytes = f.read()
            except KeyError:
                continue
            notes_bytes = _notes_for(z, slide_part)
            title, body, has_media = _render_slide(slide_bytes, notes_bytes)
            if has_media:
                media_slide_count += 1
            header = f"## Slide {idx}" + (f" — {title}" if title else "")
            lines.append(header)
            lines.append("")
            if body:
                lines.extend(body)
                lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out_md} (slides={len(slides)}, media_slides={media_slide_count})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: pptx_to_md.py <input.pptx> <workdir>", file=sys.stderr)
        sys.exit(2)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
