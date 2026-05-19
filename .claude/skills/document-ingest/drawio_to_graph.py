#!/usr/bin/env python3
"""
Convert a .drawio (or mxfile XML) diagram into a node/edge JSON graph.

Usage: drawio_to_graph.py <input.drawio|.xml> <workdir>

Handles both plain mxfile XML and the compressed form (mxfile/diagram contains
base64-encoded, deflate-compressed mxGraphModel XML).
"""
from __future__ import annotations

import base64
import json
import re
import sys
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path
from urllib.parse import unquote


def maybe_decompress(diagram_text: str) -> str:
    s = (diagram_text or "").strip()
    if s.startswith("<"):
        return s
    try:
        raw = base64.b64decode(s)
        try:
            inflated = zlib.decompress(raw, -zlib.MAX_WBITS)
        except zlib.error:
            inflated = zlib.decompress(raw)
        return unquote(inflated.decode("utf-8", errors="replace"))
    except Exception:
        return s


def extract_models(root: ET.Element) -> list[ET.Element]:
    models: list[ET.Element] = []
    for diagram in root.iter("diagram"):
        text = diagram.text or ""
        xml = maybe_decompress(text)
        try:
            inner = ET.fromstring(xml)
        except ET.ParseError:
            continue
        if inner.tag == "mxGraphModel":
            models.append(inner)
        else:
            for m in inner.iter("mxGraphModel"):
                models.append(m)
    if not models and root.tag == "mxGraphModel":
        models.append(root)
    if not models:
        for m in root.iter("mxGraphModel"):
            models.append(m)
    return models


def clean_label(s: str | None) -> str:
    if not s:
        return ""
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def kind_from_style(style: str | None) -> str | None:
    if not style:
        return None
    style_l = style.lower()
    if "shape=mxgraph.flowchart.decision" in style_l or "rhombus" in style_l:
        return "decision"
    if "swimlane" in style_l:
        return "swimlane"
    if "ellipse" in style_l:
        return "actor"
    if "shape=cylinder" in style_l or "cylinder" in style_l:
        return "datastore"
    return None


def convert(input_path: Path, workdir: Path) -> None:
    workdir.mkdir(parents=True, exist_ok=True)
    text = input_path.read_text(encoding="utf-8", errors="replace")
    root = ET.fromstring(text)
    models = extract_models(root)

    nodes: list[dict] = []
    edges: list[dict] = []
    groups: list[dict] = []
    children_by_parent: dict[str, list[str]] = {}

    seen_node_ids: set[str] = set()
    for model in models:
        for cell in model.iter("mxCell"):
            cid = cell.get("id")
            if not cid:
                continue
            parent = cell.get("parent")
            style = cell.get("style") or ""
            label = clean_label(cell.get("value"))
            if cell.get("edge") == "1":
                edges.append({
                    "id": cid,
                    "from": cell.get("source"),
                    "to": cell.get("target"),
                    "label": label or None,
                })
            elif cell.get("vertex") == "1":
                if cid in seen_node_ids:
                    continue
                seen_node_ids.add(cid)
                node = {"id": cid, "label": label}
                k = kind_from_style(style)
                if k:
                    node["kind"] = k
                nodes.append(node)
                if parent:
                    children_by_parent.setdefault(parent, []).append(cid)
                if "swimlane" in (style or "").lower():
                    groups.append({"id": cid, "label": label, "members": []})

    members_index = {g["id"]: g for g in groups}
    for parent_id, kids in children_by_parent.items():
        if parent_id in members_index:
            members_index[parent_id]["members"].extend(kids)

    out = {"nodes": nodes, "edges": edges, "groups": groups}
    out_path = workdir / "diagram.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"wrote {out_path} (nodes={len(nodes)}, edges={len(edges)}, groups={len(groups)})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: drawio_to_graph.py <input> <workdir>", file=sys.stderr)
        sys.exit(2)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
