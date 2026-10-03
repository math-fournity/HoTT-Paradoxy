#!/usr/bin/env python3
"""Capture the bare-Lean run for MP-ZFC-OBSERVATION-BOUNDARY-001.

This is intentionally self-contained: the proof imports no external library.
It writes a formal-proof-run/v1 receipt under HoTT/verification/runs and does
not update the canonical claim matrix; this detached worktree is a contributor
candidate until the canonical dev integrator reviews it.
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
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-01"
PROOF_ID = "MP-ZFC-OBSERVATION-BOUNDARY-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/ObservationBoundary.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/CLAIM.md")
LEAN = Path("/Users/aurolafly/.elan/bin/lean")


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
    if "/" in RUN_ID or not RUN_ID.startswith("20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-"):
        raise SystemExit("RUN_ID_INVALID")
    source = ROOT / SOURCE
    claim = ROOT / CLAIM
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not LEAN.is_file():
        raise SystemExit("LEAN_MISSING")

    argv = [str(LEAN), str(source)]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    completed = dt.datetime.now(dt.timezone.utc)
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [source_row(source), source_row(claim), source_row(Path(__file__))],
        "external_dependencies": [],
        "policy": "Bare Lean core only; no imports or external source tree."
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["ZFC-OBS-001", "ZFC-OBS-002", "ZFC-OBS-003", "ZFC-OBS-004", "ZFC-OBS-005", "ZFC-OBS-006"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 core propositional logic and inductive fixture; not a formalization of ZFC or real analysis.",
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Observation collision proves relative completion-observation incompleteness and blocks a Done classifier through the coarse observation; an explicit statewise CompletionBridge is the positive transport control; CompletionEquivalent formalizes the stronger same-task identity condition; enriched terminal-event observation is a second positive control.",
        "non_goals": [
            "No theorem about ZFC, real numbers, actual physical motion, or an actual source LiftClaim.",
            "No proof that every mathematical completion loses process data.",
            "No claim of a ZFC inconsistency or a completed Q0/Q1 verdict."
        ],
        "index_status": "CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"
    }
    run.mkdir(parents=True)
    for name, data in [
        ("stdout.txt", result.stdout),
        ("stderr.txt", result.stderr),
        ("environment.txt", (
            f"platform={platform.platform()}\nlean={version}\n"
            "imports=none\naxioms=printed-in-stdout\n"
        ).encode()),
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
