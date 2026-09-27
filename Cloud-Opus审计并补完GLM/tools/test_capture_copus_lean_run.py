#!/usr/bin/env python3
"""Unit test for classify_failure in capture_copus_lean_run.py (Cloud-Opus audit, 2026-09-27).

Why: the first Lean replay attempt failed on a missing toolchain file
(lib/lean/Init.olean.server was not extracted), and the first version of the
capture tool recorded the negative control as "rejected as expected".  A
negative control must count only when Lean rejects the target file itself.
The first two cases below are the archived failed receipts of that attempt.
Later the same day the tool learned to tell a "(kernel)" error in the target
(the kernel itself refused a declaration) from an elaborator error; two cases
test that split.

Run from the repository root:  python3 -B Cloud-Opus审计并补完GLM/tools/test_capture_copus_lean_run.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "Cloud-Opus审计并补完GLM/tools/capture_copus_lean_run.py"
FAILED = ROOT / "Cloud-Opus审计并补完GLM/附件/失败捕获-20260927-Lean缺Init配套文件"
U = Path("HoTT/formal/claude-cg001/universe-set-lean")
K = Path("HoTT/formal/cloud-opus-glm-audit/lean-controls")


def load():
    spec = importlib.util.spec_from_file_location("capture_copus_lean_run", TOOL)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> int:
    m = load()
    cases = [
        ("archived failed positive (missing Init.olean.server)",
         (FAILED / "20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01/stdout.txt").read_text(encoding="utf-8"),
         [U / "UniverseIsSet.lean"], "TOOLCHAIN_OR_IO_FAILURE"),
        ("archived failed negative (missing Init.olean.server)",
         (FAILED / "20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-NEG-01/stdout.txt").read_text(encoding="utf-8"),
         [U / "UniverseIsSet.lean", U / "WrongCastFlips.lean"], "TOOLCHAIN_OR_IO_FAILURE"),
        ("Opus macOS negative control (genuine rejection)",
         (ROOT / "HoTT/verification/runs/20260926-CG001-UNIVERSE-SET-LEAN-NEG-01/stdout.txt").read_text(encoding="utf-8"),
         [U / "UniverseIsSet.lean", U / "WrongCastFlips.lean"], "ELABORATION_ERROR_IN_TARGET"),
        ("synthetic: the kernel itself refuses a declaration in the target",
         f"## lean {U / 'UniverseIsSet.lean'}\n## lean {K / 'KernelCastFlips.lean'}\n"
         f"{K / 'KernelCastFlips.lean'}:17:0: error: (kernel) declaration type mismatch, 'kernelCastFlips' has type\n## exit 1\n",
         [U / "UniverseIsSet.lean", K / "KernelCast.lean", K / "KernelCastFlips.lean"], "KERNEL_ERROR_IN_TARGET"),
        ("synthetic: a kernel error in an earlier source is not a rejection of the target",
         f"## lean {K / 'KernelCast.lean'}\n{K / 'KernelCast.lean'}:39:0: error: (kernel) declaration type mismatch\n## exit 1\n",
         [K / "KernelCast.lean", K / "KernelCastFlips.lean"], "ERROR_IN_EARLIER_SOURCE"),
        ("synthetic: error in an earlier source",
         f"## lean {U / 'UniverseIsSet.lean'}\n{U / 'UniverseIsSet.lean'}:3:0: error: unknown identifier 'x'\n## exit 1\n",
         [U / "UniverseIsSet.lean", U / "WrongCastFlips.lean"], "ERROR_IN_EARLIER_SOURCE"),
        ("synthetic: leanchecker failure",
         f"## lean {U / 'UniverseIsSet.lean'}\n## leanchecker --fresh UniverseIsSet\nuncaught exception\n## exit 1\n",
         [U / "UniverseIsSet.lean"], "LEANCHECKER_FAILURE"),
        ("synthetic: driver refused to run", "", [U / "UniverseIsSet.lean"], "DRIVER_OR_TOOL_FAILURE"),
    ]
    failures = 0
    for name, stdout, sources, expected in cases:
        got = m.classify_failure(stdout, sources)
        ok = got == expected
        failures += not ok
        print(f"{'OK ' if ok else 'BAD'} {name} -> {got}" + ("" if ok else f" (expected {expected})"))
    print("ALL PASS" if failures == 0 else f"{failures} FAILURE(S)")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
