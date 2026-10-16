#!/usr/bin/env python3
"""Verify P14's bounded actual-HoTT candidate selection."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-REPORT.md"
FREEZE = OUT / "P14-PRIETO-CUBIDES-CANDIDATE-FREEZE.json"
RECEIPT = OUT / "P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-VERIFICATION.json"
LOCAL = "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/DISCOVERY-CANDIDATES.json"
P13 = "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = REPORT.read_text(encoding="utf-8")
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    required = [
        "SUCCESSOR_SELECTED", "PRIETO_CUBIDES_SPHERICAL_MAPS_AGDA_CANDIDATE", "P15_NOT_STARTED",
        "P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-001", "K-input", "K-output", "K-claim",
        "K-forgetting", "K-version", "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [token for token in required if token not in report]
    published = freeze["published_source"]
    source_ok = (
        freeze.get("candidate_id") == "P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-001"
        and published.get("source_commit_short") == "57c278b4"
        and published.get("agda_version") == "2.6.2.2-442c76b"
        and len(freeze.get("candidate_modules", [])) == 5
    )
    local_text = (ROOT / LOCAL).read_text(encoding="utf-8")
    local_ok = "doi:10.1145/3497775.3503671" in local_text and "DISCOVERY_UNREVIEWED" in local_text
    p13_text = (ROOT / P13).read_text(encoding="utf-8")
    p13_ok = all(token in p13_text for token in ("H_intrinsic", "Done_ambient^fin", "Done_curve"))
    result = {
        "schema_version": "p14-ambient-operation-k-successor-discovery-verification/v1",
        "task_id": "P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-001",
        "status": "PASS_WITH_SCOPE" if not missing and source_ok and local_ok and p13_ok else "FAIL",
        "verdict": "SUCCESSOR_SELECTED / PRIETO_CUBIDES_SPHERICAL_MAPS_AGDA_CANDIDATE / P15_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "scope": "Checks the P14 selection card, the published-source version markers, local historical non-audit status, and P13 admission targets. It does not fetch/compile Agda, validate the published source's full contents, find K, or prove a HoTT defect.",
        "sources": {str(REPORT.relative_to(ROOT)): sha(REPORT), str(FREEZE.relative_to(ROOT)): sha(FREEZE), LOCAL: sha(ROOT / LOCAL), P13: sha(ROOT / P13)},
        "missing_required_tokens": missing,
        "source_identity_ok": source_ok,
        "local_predecessor_ok": local_ok,
        "p13_contract_ok": p13_ok,
        "published_sources_checked": list(published.values()),
    }
    if args.write:
        RECEIPT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
