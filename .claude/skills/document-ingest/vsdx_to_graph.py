#!/usr/bin/env python3
"""
Best-effort .vsdx -> node/edge JSON graph using only the standard library.

Usage: vsdx_to_graph.py <input.vsdx> <workdir>

A .vsdx is a zip containing visio/pages/page*.xml. We pull shape text and
connection records (visio/pages/page*.xml.rels for connector targets).
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    "v": "http://schemas.microsoft.com/office/visio/2012/main",
}


def collect_text(elem) -> str:
    parts: list[str] = []
    for t in elem.iter():
        if t.tag.endswith("}Text") or t.tag == "Text":
            for child in t.iter():
                if child.text:
                    parts.append(child.text)
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


def convert(input_path: Path, workdir: Path) -> None:
    workdir.mkdir(parents=True, exist_ok=True)
    nodes: list[dict] = []
    edges: list[dict] = []

    with zipfile.ZipFile(input_path) as z:
        page_xmls = [n for n in z.namelist() if re.match(r"visio/pages/page\d+\.xml$", n)]
        if not page_xmls:
            (workdir / "diagram.json").write_text(json.dumps({"nodes": [], "edges": [], "groups": []}, indent=2), encoding="utf-8")
            print("no pages found in vsdx")
            return

        for page in page_xmls:
            with z.open(page) as f:
                tree = ET.parse(f)
            root = tree.getroot()
            shapes_by_id: dict[str, dict] = {}
            for shape in root.iter():
                if not shape.tag.endswith("}Shape"):
                    continue
                sid = shape.get("ID")
                if not sid:
                    continue
                label = collect_text(shape)
                shapes_by_id[sid] = {"id": f"{page}:{sid}", "label": label}

            # Connections: <Connect FromSheet="..." ToSheet="..." FromCell="EndX|BeginX" .../>
            for connect in root.iter():
                if not connect.tag.endswith("}Connect"):
                    continue
                from_sheet = connect.get("FromSheet")
                to_sheet = connect.get("ToSheet")
                if from_sheet and to_sheet:
                    edges.append({
                        "from": f"{page}:{from_sheet}",
                        "to": f"{page}:{to_sheet}",
                        "label": None,
                    })

            nodes.extend(shapes_by_id.values())

    out = {"nodes": nodes, "edges": edges, "groups": []}
    out_path = workdir / "diagram.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"wrote {out_path} (nodes={len(nodes)}, edges={len(edges)})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: vsdx_to_graph.py <input.vsdx> <workdir>", file=sys.stderr)
        sys.exit(2)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
