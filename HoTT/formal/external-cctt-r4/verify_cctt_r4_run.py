#!/usr/bin/env python3
"""Verify GZ-005 receipt integrity and optionally re-run its bounded controls."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path("HoTT/formal/external-cctt-r4")
RUN = Path("HoTT/verification/runs/20261005-CCTT-R4-INPUT-DOMAIN-002")
REQUIRED_ARTIFACTS = {
    "RUN.json", "environment.txt", "source-manifest.json", "build.stdout.txt", "build.stderr.txt",
    "fixtures/Positive.profile.stdout.txt", "fixtures/Positive.profile.stderr.txt",
    "fixtures/Positive.checker.stdout.txt", "fixtures/Positive.checker.stderr.txt",
    "fixtures/Hole.profile.stdout.txt", "fixtures/Hole.profile.stderr.txt",
    "fixtures/Hole.checker.stdout.txt", "fixtures/Hole.checker.stderr.txt",
    "fixtures/Recursive.profile.stdout.txt", "fixtures/Recursive.profile.stderr.txt",
    "fixtures/Recursive.checker.stdout.txt", "fixtures/Recursive.checker.stderr.txt",
    "fixtures/Recursive.normalization.stdout.txt", "fixtures/Recursive.normalization.stderr.txt",
    "fixtures/TypeError.profile.stdout.txt", "fixtures/TypeError.profile.stderr.txt",
    "fixtures/TypeError.checker.stdout.txt", "fixtures/TypeError.checker.stderr.txt",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(root: Path) -> dict[str, object]:
    run = root / RUN
    receipt = json.loads((run / "RUN.json").read_text(encoding="utf-8"))
    if receipt.get("schema_version") != "cctt-r4-checker-run/v1":
        raise ValueError("RUN_SCHEMA_INVALID")
    if receipt.get("run_id") != run.name or receipt.get("status") != "CHECKER_INPUT_DOMAIN_CONTROLS_PASS_WITH_SCOPE":
        raise ValueError("RUN_ID_OR_STATUS_INVALID")
    artifacts = receipt.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != REQUIRED_ARTIFACTS - {"RUN.json"}:
        raise ValueError("ARTIFACT_SET_INVALID")
    for relative, expected in artifacts.items():
        path = run / relative
        data = path.read_bytes()
        if expected != {"bytes": len(data), "sha256": sha(data)}:
            raise ValueError(f"ARTIFACT_HASH_MISMATCH:{relative}")
    manifest = json.loads((run / "source-manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "cctt-r4-source-manifest/v1":
        raise ValueError("SOURCE_MANIFEST_SCHEMA_INVALID")
    for row in manifest.get("package_files", []):
        path = root / row["path"]
        data = path.read_bytes()
        if row != {"path": row["path"], "bytes": len(data), "sha256": sha(data)}:
            raise ValueError(f"PACKAGE_SOURCE_DRIFT:{row['path']}")
    fixtures = receipt.get("fixtures")
    if not isinstance(fixtures, dict):
        raise ValueError("FIXTURE_RECORDS_INVALID")
    if fixtures["Positive"]["profile"]["accepted"] is not True:
        raise ValueError("POSITIVE_PROFILE_NOT_ACCEPTED")
    if fixtures["Positive"]["checker"]["diagnostic_accepted"] is not True:
        raise ValueError("POSITIVE_CHECKER_NOT_ACCEPTED")
    for name in ("Hole", "Recursive"):
        if fixtures[name]["checker"]["diagnostic_accepted"] is not True or fixtures[name]["profile"]["accepted"] is not False:
            raise ValueError(f"CONTROL_EXPECTATION_INVALID:{name}")
    if fixtures["TypeError"]["checker"]["diagnostic_accepted"] is not False:
        raise ValueError("TYPE_ERROR_NOT_REJECTED_BY_DIAGNOSTIC")
    return {"status": "PASS_WITH_SCOPE", "run": RUN.as_posix(), "fixture_names": sorted(fixtures)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()
    try:
        result = verify(args.root.resolve())
        if args.rerun:
            live = subprocess.run(
                [sys.executable, str(args.root / PACKAGE / "capture_cctt_r4_run.py"), "--verify"],
                cwd=args.root,
                capture_output=True,
                text=True,
                check=False,
            )
            if live.returncode:
                raise ValueError(f"LIVE_RERUN_FAILED:{live.stderr.strip()}")
            result["live_rerun"] = json.loads(live.stdout)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"GZ005_VERIFY_ERROR:{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
