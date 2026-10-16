#!/usr/bin/env python3
"""Verify ABX-0 source identities and the four existing Flash receipts.

No proof assistant is replayed here.  The verifier checks current source/hash
identity and persisted run qualification; historical --rerun evidence remains
separately located in audit/zcode-7cb03240-review-20260920/replays/.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SOURCE_MANIFEST = ROOT / "audit/zcode-7cb03240-review-20260920/SOURCE-MANIFEST.json"
IMPORT = HERE / "SOURCE-IMPORT.json"
OUT = HERE / "INTAKE-VERIFICATION.json"
RUNS = (
    "20260919-MP-G4-RING-ORIGIN-02",
    "20260919-MP-G4-BREAKPOINT-BRIDGE-03",
    "20260919-MP-G4-NO-BREAKOUT-02",
    "20260919-MP-G4-CUT-AS-SOURCE-01",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    source_rows = json.loads(SOURCE_MANIFEST.read_text())
    source_checks = []
    failures = []
    for row in source_rows:
        path = Path(row["path"])
        if not path.exists():
            source_checks.append({"path": row["path"], "status": "MISSING"})
            failures.append(row["path"])
            continue
        actual = sha(path)
        ok = actual == row["sha256"]
        source_checks.append({"path": row["path"], "expected_sha256": row["sha256"], "actual_sha256": actual, "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(row["path"])

    import_receipt = json.loads(IMPORT.read_text())
    snapshot = ROOT / import_receipt["repo_snapshot"]["path"]
    import_ok = snapshot.exists() and sha(snapshot) == import_receipt["repo_snapshot"]["sha256"]
    if not import_ok:
        failures.append("ABX_USER_SOURCE")

    run_checks = []
    for name in RUNS:
        command = [sys.executable, "-B", "scripts/audit/verify_formal_proof_run.py", "--run-dir", f"HoTT/verification/runs/{name}"]
        completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        try:
            result = json.loads(completed.stdout)
        except json.JSONDecodeError:
            result = {"status": "NON_JSON"}
        ok = completed.returncode == 0 and result.get("status") == "PASS_WITH_SCOPE" and result.get("kernel_status") == "KERNEL_ACCEPTED_WITH_SCOPE"
        run_checks.append({"run": name, "exit_code": completed.returncode, "status": result.get("status"), "kernel_status": result.get("kernel_status"), "index_status": result.get("index_status"), "replay": result.get("replay"), "verified_without_rerun": True})
        if not ok:
            failures.append(name)

    result = {
        "schema_version": "abx-intake-verification/v1",
        "status": "PASS" if not failures else "FAIL",
        "source_manifest_sha256": sha(SOURCE_MANIFEST),
        "source_checks": source_checks,
        "user_source_snapshot_ok": import_ok,
        "run_checks": run_checks,
        "failures": failures,
        "scope": "Current source/receipt identity only. Does not replay a kernel, prove ABX, or show a real K consumer.",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
