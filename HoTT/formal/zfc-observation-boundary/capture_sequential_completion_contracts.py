#!/usr/bin/env python3
"""Capture the bare-Lean sequential completion-contract control."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "20261004-MP-ZENO-SEQUENTIAL-COMPLETION-CONTRACTS-001-"
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else PREFIX + "01"
PROOF_ID = "MP-ZENO-SEQUENTIAL-COMPLETION-CONTRACTS-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/SequentialCompletionContracts.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/SequentialCompletionContracts-CLAIM.md")
LEAN = Path("/Users/aurolafly/.elan/bin/lean")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith(PREFIX):
        raise SystemExit("RUN_ID_INVALID")
    source, claim = ROOT / SOURCE, ROOT / CLAIM
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not all(path.is_file() for path in (source, claim, LEAN)):
        raise SystemExit("REQUIRED_INPUT_MISSING")

    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run([str(LEAN), str(source)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    completed = dt.datetime.now(dt.timezone.utc)
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(source), row(claim), row(Path(__file__))],
        "external_sources": [],
        "policy": "Bare-Lean indexed-trace contract control; not real time, convergence, physical motion, ZFC, or a source adoption claim.",
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["ZENO-CONTRACT-001", "ZENO-CONTRACT-002", "ZENO-CONTRACT-003", "ZENO-CONTRACT-004"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 core indexed-trace contract control; no formalization of real analysis, physical motion, ZFC, or source prose.",
        "command_argv": [str(LEAN), str(source)],
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Canonical natural-index trace satisfies every-step Done but not final-action Done; it is a contract distinction control.",
        "non_goals": [
            "No real limit theorem.",
            "No physical completion claim.",
            "No actual source or ZFC conclusion.",
            "No P-to-HoTT-B provenance.",
        ],
        "index_status": "CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    environment = f"platform={platform.platform()}\nlean={version}\nimports=none\naxioms=printed-in-stdout\n".encode()
    for name, data in [
        ("stdout.txt", result.stdout),
        ("stderr.txt", result.stderr),
        ("environment.txt", environment),
        ("source-manifest.json", (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()),
    ]:
        write_new(run / name, data)
        receipt[name.removesuffix(".txt").replace("-", "_")] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", (json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode, "duration_seconds": receipt["duration_seconds"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
