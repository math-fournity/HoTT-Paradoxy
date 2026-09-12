#!/usr/bin/env python3
"""Compatibility entrypoint for the single top-level cognition runtime.

The canonical implementation is ``.codex/tools/cognition_runtime.py``.  This
historical Skill path remains executable so existing callers do not break, but
it no longer carries an independently editable runtime copy.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

CANONICAL = Path(__file__).resolve().parents[3] / "tools" / "cognition_runtime.py"
SPEC = importlib.util.spec_from_file_location("hott_top_level_cognition_runtime", CANONICAL)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load canonical cognition runtime: {CANONICAL}")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

for NAME in dir(MODULE):
    if not NAME.startswith("__"):
        globals()[NAME] = getattr(MODULE, NAME)

if __name__ == "__main__":
    raise SystemExit(MODULE.main())
