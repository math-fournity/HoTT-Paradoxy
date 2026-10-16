#!/usr/bin/env python3
"""Verify P27's bounded reflection-consumer selection."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P27-REFLECTION-CONSUMER-DISCOVERY-REPORT.md"
FREEZE = OUT / "P27-REFLECTION-CONSUMER-SOURCE-FREEZE.json"
RESULT = OUT / "P27-REFLECTION-CONSUMER-DISCOVERY-VERIFICATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    required = [
        "SUCCESSOR_SELECTED",
        "CFTT_STAGED_QUOTATION_SPLICE_AND_UNSTAGING_CONSUMER_CANDIDATE",
        "LOCAL_DISCOVERY_UNREVIEWED_ASSET_UPGRADED_TO_VERSION_PINNED_CANDIDATE",
        "P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-001",
        "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [token for token in required if token not in report]
    candidates = json.loads((ROOT / freeze["local_asset"]["paths"][0]).read_text(encoding="utf-8"))
    triage = json.loads((ROOT / freeze["local_asset"]["paths"][1]).read_text(encoding="utf-8"))
    def contains(tree):
        if isinstance(tree, dict):
            if tree.get("candidate_key") == "doi:10.1145/3674648":
                return True
            return any(contains(value) for value in tree.values())
        if isinstance(tree, list):
            return any(contains(value) for value in tree)
        return False
    local_asset_present = contains(candidates) and contains(triage)
    pin_ok = freeze["external_sources"]["staged_remote_head"] == "9c4e2017669086e2f77df5014f1c215a5a7e07a3"
    status = "PASS_WITH_SCOPE" if not missing and local_asset_present and pin_ok else "FAIL"
    result = {
        "schema_version": "p27-reflection-consumer-discovery-verification/v1",
        "task_id": freeze["task_id"],
        "status": status,
        "verdict": freeze["verdict"],
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing,
        "local_asset_present": local_asset_present,
        "remote_pin_ok": pin_ok,
        "scope": "Verifies source selection and local asset provenance only. It does not inspect the CFTT source supplement or establish a HoTT claim.",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
