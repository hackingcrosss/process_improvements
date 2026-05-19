#!/usr/bin/env python3
"""Compatibility wrapper for document-ingest/vsdx_to_graph.py."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "document-ingest" / "vsdx_to_graph.py"
sys.argv = [str(SCRIPT), *sys.argv[1:]]
runpy.run_path(str(SCRIPT), run_name="__main__")
