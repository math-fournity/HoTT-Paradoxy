#!/usr/bin/env python3
"""Capture the bare-Lean ActualPolicyWitness interface run."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "20261004-MP-ZFC-ACTUAL-POLICY-WITNESS-001-"
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else PREFIX + "01"
PROOF_ID = "MP-ZFC-ACTUAL-POLICY-WITNESS-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/ActualPolicyWitness.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/ActualPolicyWitness-CLAIM.md")
USER_SOURCE = Path("sources/prompts/Codex-ZFC-Q-P-观察力数学幻觉与政策张力-用户原文-20261004.md")
M6_REPORT = Path("audit/20261004-ZFC-QP-M6-SEP-P-CANDIDATE.md")
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
    source, claim, user_source, m6 = (ROOT / SOURCE, ROOT / CLAIM, ROOT / USER_SOURCE, ROOT / M6_REPORT)
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not all(path.is_file() for path in (source, claim, user_source, m6, LEAN)):
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
        "files": [row(source), row(claim), row(user_source), row(m6), row(Path(__file__))],
        "external_sources": [],
        "policy": "Bare-Lean witness interface and negative adoption control; no actual ZFC/community/HoTT conclusion.",
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["ZFC-WITNESS-001", "ZFC-WITNESS-002", "ZFC-WITNESS-003", "ZFC-WITNESS-004", "ZFC-WITNESS-005", "ZFC-WITNESS-006", "ZFC-WITNESS-007"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 core conditional witness interface; no ZFC syntax/model, community behavior, physical motion, or HoTT provenance formalized.",
        "command_argv": [str(LEAN), str(source)],
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "A source P card alone does not imply policy adoption; a complete ActualPolicyWitness with explicit adoption, Q, backtrace, and incompatibility fields yields False.",
        "non_goals": [
            "No actual ZFC inconsistency.",
            "No actual community adoption or missing-Q conclusion.",
            "No actual P-to-HoTT-B provenance.",
            "No claim mathematical truth is formally refuted.",
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
