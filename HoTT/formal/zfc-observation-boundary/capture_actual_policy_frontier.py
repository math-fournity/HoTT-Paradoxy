#!/usr/bin/env python3
"""Capture the bare-Lean M6 ActualPolicyEvidenceFrontier run."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "20261004-MP-ZFC-ACTUAL-POLICY-FRONTIER-001-"
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else PREFIX + "01"
PROOF_ID = "MP-ZFC-ACTUAL-POLICY-FRONTIER-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/ActualPolicyEvidenceFrontier.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/ActualPolicyEvidenceFrontier-CLAIM.md")
H107 = Path("audit/20261004-P-DAG-ZFC-QP-107-Terra-Max.md")
H108 = Path("audit/20261004-P-DAG-ZFC-QP-108-Terra-Max.md")
H109 = Path("audit/20261004-P-DAG-ZFC-QP-109-Terra-Max.md")
H110 = Path("audit/20261004-P-DAG-ZFC-QP-110-Terra-Max.md")
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
    source, claim, h107, h108, h109, h110 = (ROOT / SOURCE, ROOT / CLAIM, ROOT / H107, ROOT / H108, ROOT / H109, ROOT / H110)
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not all(path.is_file() for path in (source, claim, h107, h108, h109, h110, LEAN)):
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
        "files": [row(source), row(claim), row(h107), row(h108), row(h109), row(h110), row(Path(__file__))],
        "external_sources": [],
        "policy": "Bounded M6 source-ledger frontier; not a global negative conclusion about ZFC or mathematics.",
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["ZFC-FRONTIER-001", "ZFC-FRONTIER-002", "ZFC-FRONTIER-003", "ZFC-FRONTIER-004", "ZFC-FRONTIER-005", "ZFC-FRONTIER-006", "ZFC-FRONTIER-007"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 core finite evidence-frontier ledger; no actual ZFC/community/HoTT semantic conclusion.",
        "command_argv": [str(LEAN), str(source)],
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Frozen H107-H110 denominator has P mapped but lacks adoption, actual-Q, PBacktrace, and formal A/B incompatibility fields, so it cannot close ActualPolicyWitness.",
        "non_goals": [
            "No global absence theorem.",
            "No actual ZFC inconsistency.",
            "No actual community adoption or missing-Q conclusion.",
            "No actual HoTT PBacktrace or truth refutation.",
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
