#!/usr/bin/env python3
"""Verify P32's bounded discovery record without promoting it to a global claim."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P32-HOTT-SPECIFIC-REFLECTION-CONSUMER-DISCOVERY-REPORT.md"
FREEZE = HERE / "P32-HOTT-SPECIFIC-REFLECTION-SOURCE-FREEZE.json"
OUT = HERE / "P32-HOTT-SPECIFIC-REFLECTION-CONSUMER-DISCOVERY-VERIFICATION.json"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    text = REPORT.read_text()
    needed = ["双条件", "Shulman", "2LTT", "HoTT-Agda", "Cubical", "h-propositional", "P33", "NO_NEW_HOTT_DEFECT_CLAIM"]
    missing = [token for token in needed if token not in text]
    mismatches = {path: {"expected": expected, "actual": sha256(ROOT / path)} for path, expected in freeze["local_source_sha256"].items() if sha256(ROOT / path) != expected}
    payload = {
        "schema_version": "p32-hott-specific-reflection-discovery-verification/v1",
        "task_id": "P32-HOTT-SPECIFIC-REFLECTION-CONSUMER-DISCOVERY-2026-001",
        "status": "PASS_WITH_SCOPE" if not missing and not mismatches else "FAIL",
        "verdict": freeze["verdict"],
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing,
        "local_source_hash_mismatches": mismatches,
        "scope": "Checks a bounded source-discovery report. It establishes neither source-code absence nor a HoTT theorem or defect.",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if payload["status"] != "PASS_WITH_SCOPE":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
