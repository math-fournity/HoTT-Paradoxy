#!/usr/bin/env python3
"""macOS cross-platform replay of the Linux-captured runs of CG001-C-77..C-80 (handoff W12).

Each Linux run 20260930-CG001-QUESTIONING-DELAY-* is re-captured on this Mac with the same proof id,
claim ids, sources and include roots, under a new run id with -MACOS-; the capture tools are the
Claude line's macOS tools (Agda: capture_cg001_agda_macos_run.py; Lean: capture_lean_proof_run.py,
pinned toolchain, never through elan).  Arguments are passed as a list (no shell word splitting).

Usage: replay_macos.py agda-a | agda-b | lean | compare
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/Volumes/D/HoTT_AI_HANDOFF_20260911")
RUNS = ROOT / "HoTT/verification/runs"
TOOLS = ".claude/goals/CG-001-targeted-overview/tools"
P = "HoTT/formal/claude-cg001"
QD = f"{P}/questioning-delay"
QDL = f"{P}/questioning-delay-lean"
INC = ["--include", f"{P}/pedometer-semantics", "--include", f"{P}/universe-questioning"]
DEPS = [f"{QD}/CLAIM.md", f"{P}/pedometer-semantics/PedometerSemantics.agda",
        f"{P}/pedometer-semantics/DelayMonad.agda", f"{P}/universe-questioning/UniverseHasNoLevel.agda"]

AGDA_A = [("01", None), ("NEG-01", "WrongUniverseAnswersEarly.agda"), ("NEG-02", "WrongNaturalsSilent.agda")]
AGDA_B = [("NEG-03", "WrongSetsStopAtOne.agda"), ("NEG-04", "WrongNeverByRefl.agda")]
LEAN = [("LEAN-01", None), ("LEAN-NEG-01", "WrongLeanUniverseSilent.lean")]


def linux_run(suffix: str) -> dict:
    return json.loads((RUNS / f"20260930-CG001-QUESTIONING-DELAY-{suffix}/RUN.json").read_text(encoding="utf-8"))


def mac_id(suffix: str) -> str:
    if suffix.startswith("LEAN"):
        rest = suffix[len("LEAN"):]  # "-01" or "-NEG-01"
        return f"20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS{rest}"
    return f"20260930-CG001-QUESTIONING-DELAY-MACOS-{suffix}"


def note(linux: dict) -> str:
    return (f"macOS cross-platform replay of the Linux run {linux['run_id']} (handoff W12): same proof id, claim ids, sources "
            "and include roots; captured with the Claude line's macOS tool and pinned toolchain.")


def capture_agda(batch) -> None:
    for suffix, neg in batch:
        linux = linux_run(suffix)
        source = f"{QD}/QuestioningDelay.agda" if neg is None else f"{QD}/{neg}"
        manifests = DEPS if neg is None else [f"{QD}/QuestioningDelay.agda", *DEPS]
        argv = [sys.executable, "-B", f"{TOOLS}/capture_cg001_agda_macos_run.py",
                "--run-id", mac_id(suffix), "--proof-id", linux["proof_id"]]
        for c in linux["claim_ids"]:
            argv += ["--claim-id", c]
        argv += ["--source", source, *INC]
        for m in manifests:
            argv += ["--manifest-file", m]
        argv += ["--expect", "ACCEPT" if neg is None else "REJECT",
                 "--scope", f"{linux['scope']} [{note(linux)}]"]
        for ng in linux.get("non_goals", []):
            argv += ["--non-goal", ng]
        argv += ["--non-goal", "A cross-platform replay adds no claim; it checks that the same sources give the same kernel verdict on a second platform."]
        r = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        print(mac_id(suffix), "exit", r.returncode, (r.stdout.strip().splitlines() or [""])[-1][:300], r.stderr.strip()[-300:])


def capture_lean() -> None:
    for suffix, neg in LEAN:
        linux = linux_run(suffix)
        sources = [f"{QDL}/QuestioningLean.lean"] if neg is None else [f"{QDL}/QuestioningLean.lean", f"{QDL}/{neg}"]
        argv = [sys.executable, "-B", f"{TOOLS}/capture_lean_proof_run.py",
                "--run-id", mac_id(suffix), "--proof-id", linux["proof_id"]]
        for c in linux["claim_ids"]:
            argv += ["--claim-id", c]
        for s in sources:
            argv += ["--source", s]
        if neg is None:
            argv += ["--leanchecker"]
        for m in [f"{QD}/CLAIM.md", f"{QD}/QuestioningDelay.agda"]:
            argv += ["--manifest-file", m]
        argv += ["--scope", f"{linux['scope']} [{note(linux)}]"]
        for ng in linux.get("non_goals", []):
            argv += ["--non-goal", ng]
        r = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        print(mac_id(suffix), "exit", r.returncode, (r.stdout.strip().splitlines() or [""])[-1][:300], r.stderr.strip()[-300:])


ROOT_MARKERS = [
    (re.compile(r"/home/user/HoTT-Paradoxy"), "<REPO>"),
    (re.compile(re.escape(str(ROOT))), "<REPO>"),
    (re.compile(r"/home/user/toolchain/[^\s)]*?/cubical(?=/)"), "<CUBICAL>"),
    (re.compile(r"/Volumes/D/HoTT-toolchain-cache/cubical-v0\.9/cubical(?=/)"), "<CUBICAL>"),
    (re.compile(r"/home/user/toolchain/[^\s)]*?/lib/lean"), "<LEANLIB>"),
    (re.compile(r"/Users/[^\s)]*?/\.elan/toolchains/[^\s)/]+/lib/lean"), "<LEANLIB>"),
]


def normalize(text: str) -> list[str]:
    out = []
    for line in text.splitlines():
        for pattern, repl in ROOT_MARKERS:
            line = pattern.sub(repl, line)
        out.append(line.rstrip())
    return out


def compare() -> int:
    bad = 0
    for suffix, _ in AGDA_A + AGDA_B + LEAN:
        lin = RUNS / f"20260930-CG001-QUESTIONING-DELAY-{suffix}"
        mac = RUNS / mac_id(suffix)
        lj, mj = (json.loads((d / "RUN.json").read_text(encoding="utf-8")) for d in (lin, mac))
        lo, mo = (normalize((d / "stdout.txt").read_text(encoding="utf-8", errors="replace")) for d in (lin, mac))
        le, me = ((d / "stderr.txt").read_bytes() for d in (lin, mac))
        same_exit = lj["exit_code"] == mj["exit_code"]
        same_status = lj["status"] == mj["status"]
        same_out = lo == mo
        diff_lines = [(i, a, b) for i, (a, b) in enumerate(zip(lo, mo)) if a != b][:3]
        print(json.dumps({"linux": lin.name, "macos": mac.name, "exit": [lj["exit_code"], mj["exit_code"]],
                          "status": [lj["status"], mj["status"]], "stdout_lines": [len(lo), len(mo)],
                          "normalized_stdout_equal": same_out, "stderr_bytes": [len(le), len(me)],
                          "first_diffs": diff_lines}, ensure_ascii=False))
        if not (same_exit and same_status and same_out):
            bad += 1
    print("MISMATCHES", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "agda-a":
        capture_agda(AGDA_A)
    elif mode == "agda-b":
        capture_agda(AGDA_B)
    elif mode == "lean":
        capture_lean()
    elif mode == "compare":
        raise SystemExit(compare())
    else:
        raise SystemExit(__doc__)
