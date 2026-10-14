#!/usr/bin/env python3
"""Capture one CG-008 round-19 run as an F-011 receipt (goal-local).

Same receipt format as the CG-008 round-13 receipt
(2026-10-12-CG001-CG008-IVE-ITR-CLOSED-01): formal-proof-run/v1 with
RUN.json, stdout.txt, stderr.txt, environment.txt, source-manifest.json,
so .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py
checks and replays it unchanged.

Reuses the SAME driver (zfc_lean_check.py) and pin set (make_z0_pins.py);
only the source list and the run metadata differ.

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-008-zfc-set-sigma1-completeness/tools/capture_cg008_round19.py
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path("HoTT/formal/claude-cg001/godel-q-zfc-z0-full")
DRIVER = Path(".claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py")
PINS_TOOL = Path(".claude/goals/CG-006-zfc-complete-formalization/tools/make_z0_pins.py")
SELF = Path(".claude/goals/CG-008-zfc-set-sigma1-completeness/tools/capture_cg008_round19.py")

RUN_ID = "2026-10-13-CG001-CG008-AXSTEP-SPLIT-01"
PROOF_ID = "MP-CG001-GODEL-Q-ZFC-Z0-CG008-014"
CLAIM_IDS = ["CG001-C-143", "CG001-C-144"]
RUN_DIR = ROOT / "HoTT/verification/runs" / RUN_ID

# 依赖序（闭包由导入图算出，最后一个 = 目标）
_PKG_PREFIX = PACKAGE.as_posix() + "/"
SOURCES_REPO = [line.strip() for line in
                (Path(".claude/goals/CG-008-zfc-set-sigma1-completeness/tools/"
                      "z0_r20_closure.txt").read_text().splitlines()) if line.strip()]
TARGET = "GodelQ/ZFC/CG008TargetShape.lean"

SCOPE = (
    "CG-008 P3 round 19: the gap is split, and both halves except the nonstandard one are paid; "
    "and the two narrowings (A: mine; B: 002-Step's single D3 instance) are composed and checked "
    "to be ORTHOGONAL, not additive. "
    "New sources: CG008FleetGap (the minimal gap, stated in the fleet's shared shape C: "
    "Provable ZFC (translate sigma) -> Provable ZFC (translate (zfcTr sigma)); plus a "
    "machine-checked correction: the N->V transfer EXISTS -- provable_iff_provable descends to "
    "the meta level and internalize_provability ascends to any V -- while V->N does NOT, since "
    "both lemmas hard-wire N; so the gap is not a universe mismatch), "
    "CG008MinimalGapSuffices (C alone suffices for hD3G: HBL3 is a statement INSIDE ISigma_1, "
    "verified model-by-model via complete ISigma_1, and models_zfcTr_iff is an iff whose two "
    "sides are both V-internal -- so the route never leaves V and never passes through "
    "zfcTr.D1), CG008AxStepSplit (Foundation's own mem_Delta1Class_iff splits "
    "p in ISigma_1.Delta_1Class into PA-minus or InductionR; PA-minus is finite, so nonstandard "
    "members are EXACTLY nonstandard instances of the induction scheme; the finite half is "
    "PROVED: mem_ofList_ch, mem_ofFinite_ch, mem_PAMinus_is_standard, axStep_finite_proved), "
    "CG008InductionBody (the body K is constrained by IsPrenexHierarchy Sigma 1; standard "
    "bodies bridge to the meta level via isPrenexHierarchy_quote_iff; the standard-code branch "
    "of AxStep_induction is discharged by axStep_standard_code, so the wall is entirely on "
    "NONSTANDARD codes; and Foundation has NO formalized relative interpretability -- "
    "grep for Interpretability across FirstOrder returns nothing), and CG008TargetShape "
    "(godel_is_standard: godel is a META-level def, so the G-code is STANDARD, hence B's single "
    "instance does NOT itself bypass the nonstandard wall; z0_of_finalTarget: FinalTarget "
    "implies the full Z0 via the single-instance theorem; finalTarget_of_minimalGap: "
    "MinimalGap implies FinalTarget, one-way.  The two narrowings act at different places: "
    "B reduces HOW MANY D3 instances are needed, A reduces WHAT IT TAKES to prove one)."
)

NON_GOALS = [
    "hD3G is NOT proved; MinimalGap (= C) is NOT proved; AxStep_induction is NOT proved; "
    "FinalTarget is NOT proved. "
    "Z0Blocked.lean still carries its precise unproved marker and is NOT a source of this run.",
    "No claim that Z0's unconditional form is established.",
    "The standard-code branch is discharged; the nonstandard branch is stated, not proved.",
    "The orthogonality result is a STATEMENT about the two narrowings, not a proof of either.",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def file_row(relative: Path) -> dict[str, object]:
    data = (ROOT / relative).read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def main() -> int:
    run_dir = RUN_DIR
    run_dir.mkdir(parents=True, exist_ok=True)

    # External dependency rows: same construction as capture_z0_run.py:84-100 —
    # the pinned Lean toolchain files, then every locally built Foundation/Mathlib
    # .olean in the closure.  The pins tool is still run first as a consistency
    # gate (its MATHLIB_CLOSURE.json aggregate is checked against the pinned one).
    toolchain = json.loads((ROOT / PACKAGE / "LEAN_TOOLCHAIN.json").read_text(encoding="utf-8"))
    closure = json.loads((ROOT / PACKAGE / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))
    live = json.loads(subprocess.run(
        [sys.executable, "-B", str(PINS_TOOL)],
        cwd=ROOT, capture_output=True, check=True).stdout)
    if live["aggregate_sha256"] != closure["aggregate_sha256"]:
        raise SystemExit("PINS_TOOL_AGGREGATE_MISMATCH")

    prefix = Path(toolchain["prefix"])
    externals: list[dict[str, object]] = []
    for row in toolchain["pinned_files"]:
        path = prefix / row["relative_path"]
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"LEAN_TOOLCHAIN_FILE_MISMATCH:{row['relative_path']}")
        externals.append({"label": f"lean-{row['relative_path']}", "local_path": str(path),
                          "bytes": len(data), "sha256": sha(data)})
    build_root = Path(closure["library_roots"]["foundation-build"])
    for row in closure["foundation_build"]["locally_built_files"]:
        if not row["path"].endswith((".olean", ".olean.private", ".olean.server")):
            continue
        path = build_root / row["path"]
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"FOUNDATION_BUILD_FILE_MISMATCH:{row['path']}")
        externals.append({"label": f"foundation-build-{row['path']}", "local_path": str(path),
                          "bytes": len(data), "sha256": sha(data)})

    sources_repo = [safe_relative(s) for s in SOURCES_REPO]
    sources_pkg = [safe_relative(s.as_posix()[len(_PKG_PREFIX):])
                   for s in sources_repo if s.as_posix().startswith(_PKG_PREFIX)]
    assert len(sources_pkg) == len(sources_repo), "non-package source in closure"
    assert sources_pkg[-1].as_posix() == TARGET, sources_pkg[-1]

    argv = [sys.executable, "-B", DRIVER.as_posix(), "--package", PACKAGE.as_posix()]
    argv += [s.as_posix() for s in sources_pkg]

    started = time.time()
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True)
    duration = time.time() - started

    (run_dir / "stdout.txt").write_bytes(proc.stdout)
    (run_dir / "stderr.txt").write_bytes(proc.stderr)

    env_lines = [
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={sys.version.split()[0]}",
        f"cwd={ROOT}",
    ]
    env_bytes = ("\n".join(env_lines) + "\n").encode("utf-8")
    (run_dir / "environment.txt").write_bytes(env_bytes)

    manifest = {
        "external_dependencies": externals,
        "files": [file_row(s) for s in sources_repo],
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "schema_version": "formal-proof-source-manifest/v1",
    }
    man_bytes = json_bytes(manifest)
    (run_dir / "source-manifest.json").write_bytes(man_bytes)

    now = datetime.now(timezone.utc)
    run = {
        "audit_notes": [],
        "audit_session": "Claude CG-008 line, worktree dev-ef7e5239, 2026-10-13 round 19",
        "claim_ids": CLAIM_IDS,
        "command_argv": argv,
        "completed_at_utc": now.isoformat(),
        "cwd": str(ROOT),
        "duration_seconds": duration,
        "environment": {"bytes": len(env_bytes), "path": "environment.txt",
                        "sha256": sha(env_bytes)},
        "exit_code": proc.returncode,
        "expected_outcome": "ACCEPT",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "non_goals": NON_GOALS,
        "outcome_matches_expectation": proc.returncode == 0,
        "proof_assistant": "Lean 4",
        "proof_assistant_version": "Lean (version 4.34.0, arm64-apple-darwin24.6.0)",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "schema_version": "formal-proof-run/v1",
        "scope": SCOPE,
        "source_manifest": {"bytes": len(man_bytes), "path": "source-manifest.json",
                            "sha256": sha(man_bytes)},
        "started_at_utc": datetime.fromtimestamp(started, timezone.utc).isoformat(),
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if proc.returncode == 0 else "REJECTED",
        "stderr": {"bytes": len(proc.stderr), "path": "stderr.txt",
                   "sha256": sha(proc.stderr)},
        "stdout": {"bytes": len(proc.stdout), "path": "stdout.txt",
                   "sha256": sha(proc.stdout)},
        "theory_variant": "Lean 4 kernel with Mathlib and FormalizedFormalLogic/Foundation (classical); first-order ZFC over \u2112\u209b\u2091\u209c, arithmetic, computability and abstract proof theory; never HoTT paths",
        "tool": SELF.as_posix(),
    }
    (run_dir / "RUN.json").write_bytes(json_bytes(run))

    print(f"run dir: {run_dir}")
    print(f"exit={proc.returncode} duration={duration:.1f}s sources={len(sources_pkg)}")
    return 0 if proc.returncode == 0 else 42


if __name__ == "__main__":
    raise SystemExit(main())
