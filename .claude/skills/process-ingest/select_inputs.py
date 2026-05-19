#!/usr/bin/env python3
"""Compatibility wrapper: process selection now delegates to document-ingest."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "document-ingest" / "select_inputs.py"

if __name__ == "__main__":
    if "--domain" not in sys.argv:
        sys.argv = [str(SCRIPT), *sys.argv[1:], "--domain", "process"]
    else:
        sys.argv = [str(SCRIPT), *sys.argv[1:]]
    runpy.run_path(str(SCRIPT), run_name="__main__")
