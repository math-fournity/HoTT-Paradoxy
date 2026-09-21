#!/usr/bin/env python3
"""Verify the bounded P5 successor-selection receipt.

This verifier checks the declared scope and provenance anchors.  It does not
prove a topological theorem or certify the truth of any external paper.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json"

SOURCES = {
    "report": "audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md",
    "origin_interface": "ABX行动/003 - 原圆环对象、判据与正反控制.md",
    "open_obligations": "audit/abx-action-20260921/H-R-K查找思路整备/005 - 未覆盖义务、禁止重复与重新出发条件.md",
    "p1": "audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md",
    "p2": "audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md",
    "p3": "audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md",
    "source_contract": "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda",
    "task_integration": "HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda",
}

REQUIRED_REPORT_TOKENS = (
    "SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON",
    "P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001",
    "https://arxiv.org/abs/1908.01366",
    "https://arxiv.org/abs/1509.07584",
    "KNOWN_DEFENSE_OR_BOUNDARY",
    "NO_NEW_ADMISSIBLE_CONSUMER_SELECTED",
    "NOT_TRIGGERED",
    "OriginPresentation",
    "operation-spec",
    "Done_strong",
    "NO_NEW_HOTT_DEFECT_CLAIM",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    missing = [str(ROOT / rel) for rel in SOURCES.values() if not (ROOT / rel).is_file()]
    report = (ROOT / SOURCES["report"]).read_text(encoding="utf-8") if not missing else ""
    absent_tokens = [token for token in REQUIRED_REPORT_TOKENS if token not in report]
    payload = {
        "schema_version": "p5-successor-discovery-verification/v1",
        "task_id": "P5-SUCCESSOR-DISCOVERY-001",
        "status": "PASS_WITH_SCOPE" if not missing and not absent_tokens else "FAIL",
        "selected_successor": "P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001",
        "claim_scope": "A bounded successor-selection and source-provenance check; not a mathematical proof or a HoTT-defect claim.",
        "checked_sources": {name: {"path": rel, "sha256": digest(ROOT / rel)} for name, rel in SOURCES.items() if (ROOT / rel).is_file()},
        "missing_sources": missing,
        "missing_required_report_tokens": absent_tokens,
        "public_sources_checked": [
            "https://arxiv.org/abs/1908.01366",
            "https://arxiv.org/abs/1911.04921",
            "https://arxiv.org/abs/1509.07584",
            "https://homotopytypetheory.org/2015/09/25/realcohesion/",
        ],
        "not_verified": [
            "the full mathematical content of the cited papers",
            "a full OriginTop/R construction",
            "a HoTT rule bridge, actual K, implementation discrepancy, or HoTT defect",
        ],
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        OUT.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if payload["status"] == "PASS_WITH_SCOPE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
