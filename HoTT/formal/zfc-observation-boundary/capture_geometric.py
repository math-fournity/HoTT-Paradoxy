#!/usr/bin/env python3
"""Capture the Mathlib Lean run for MP-ZFC-GEOMETRIC-COMPLETION-001.

The run preserves the exact source, pinned local Mathlib path, full Lean output,
and the declared classical dependencies printed by Lean.  It creates a
contributor receipt only; it does not update a canonical claim matrix.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-01"
PROOF_ID = "MP-ZFC-GEOMETRIC-COMPLETION-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/GeometricCompletion.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/GeometricCompletion-CLAIM.md")
ENVIRONMENT_QUALIFICATION = Path(
    "audit/astra-real-geometry-20260919/environment-qualification/LEAN_PATH.txt"
)
LEAN = Path("/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def source_row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith("20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-"):
        raise SystemExit("RUN_ID_INVALID")
    source = ROOT / SOURCE
    claim = ROOT / CLAIM
    qualification = ROOT / ENVIRONMENT_QUALIFICATION
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not source.is_file() or not claim.is_file() or not qualification.is_file():
        raise SystemExit("REQUIRED_INPUT_MISSING")
    if not LEAN.is_file():
        raise SystemExit("LEAN_MISSING")

    lean_path = qualification.read_text(encoding="utf-8").strip()
    if not lean_path:
        raise SystemExit("LEAN_PATH_EMPTY")
    argv = [str(LEAN), str(source)]
    env = os.environ.copy()
    env["LEAN_PATH"] = lean_path
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    completed = dt.datetime.now(dt.timezone.utc)
    accepted = (
        result.returncode == 0
        and b"sorryAx" not in result.stdout
        and b"declaration uses 'sorry'" not in result.stderr
    )
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [
            source_row(source),
            source_row(claim),
            source_row(qualification),
            source_row(Path(__file__)),
        ],
        "external_dependencies": [
            {
                "kind": "pinned-local-mathlib-build",
                "lean_path": lean_path,
                "qualification_path": str(ENVIRONMENT_QUALIFICATION),
            }
        ],
        "policy": "Mathlib topology/real-analysis proof; Lean axiom report is retained verbatim."
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["ZFC-GEO-001", "ZFC-GEO-002", "ZFC-GEO-003", "ZFC-GEO-004", "ZFC-GEO-005", "ZFC-GEO-006", "ZFC-GEO-007", "ZFC-GEO-008"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4.34.1 plus pinned Mathlib real-analysis/topology; not a formalization of ZFC or a physical-motion theory.",
        "command_argv": argv,
        "cwd": str(ROOT),
        "lean_path": lean_path,
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_DECLARED_AXIOMS_AND_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "A concrete geometric real sequence tends to 1 while no finite natural-number stage equals 1; the named limit outcome does not imply, and is not equivalent to, finite-stage endpoint arrival. A separate closed-continuous-time model supplies an endpoint-arrival positive control.",
        "non_goals": [
            "No theorem that a limit settles or fails to settle any physical or philosophical completion condition.",
            "No theorem about all limit theories, all real-number constructions, or all ZFC models.",
            "No proof of a ZFC inconsistency, incompleteness theorem, or completed Q0/Q1 verdict."
        ],
        "axiom_policy": "Expected Mathlib/classical dependencies are preserved from Lean #print axioms; they must not be described as a no-axiom proof.",
        "index_status": "CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"
    }
    run.mkdir(parents=True)
    environment = (
        f"platform={platform.platform()}\nlean={version}\n"
        f"lean_path={lean_path}\nimports=Mathlib.Analysis.SpecificLimits.Normed\n"
        "axioms=printed-in-stdout; expected classical/Mathlib dependencies\n"
    ).encode()
    for name, data in [
        ("stdout.txt", result.stdout),
        ("stderr.txt", result.stderr),
        ("environment.txt", environment),
        ("source-manifest.json", json_bytes(manifest)),
    ]:
        write_new(run / name, data)
        receipt[name.removesuffix(".txt").replace("-", "_")] = {
            "path": name, "bytes": len(data), "sha256": sha(data)
        }
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({
        "status": receipt["status"],
        "run_id": RUN_ID,
        "exit": result.returncode,
        "duration_seconds": receipt["duration_seconds"],
        "stdout_sha256": sha(result.stdout),
        "stderr_sha256": sha(result.stderr)
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
