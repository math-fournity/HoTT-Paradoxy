#!/usr/bin/env python3
"""Compatibility launcher for the single top-level cognition runtime.

The canonical implementation is `.codex/tools/cognition_runtime.py`.  Keeping
this path executable preserves the WebGPT skill's historical command shape
without creating a second state engine.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


CANONICAL = Path(__file__).resolve().parents[3] / "tools" / "cognition_runtime.py"
_spec = spec_from_file_location("top_level_cognition_runtime", CANONICAL)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"canonical cognition runtime unavailable: {CANONICAL}")
_runtime = module_from_spec(_spec)
_spec.loader.exec_module(_runtime)
globals().update({name: value for name, value in vars(_runtime).items() if not name.startswith("__")})

if __name__ == "__main__":
    _runtime.main()
