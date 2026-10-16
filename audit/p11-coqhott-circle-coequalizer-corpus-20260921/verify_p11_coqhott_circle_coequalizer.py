#!/usr/bin/env python3
"""Verify the bounded P11 Coq-HoTT source-audit record."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md"
AUDIT = OUT / "P11-COQHOTT-SOURCE-AUDIT.json"
RECEIPT = OUT / "P11-COQHOTT-CIRCLE-COEQUALIZER-VERIFICATION.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = REPORT.read_text(encoding="utf-8")
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    required = [
        "NOT_A_CONSUMER",
        "DEFENSE_EXPLICIT_GLUING_AND_COHERENCE",
        "EXPLICIT_ADMITTED_TORUS_BOUNDARY",
        "P12_THIRD_SUCCESSOR_DISCOVERY_REQUIRED",
        "K-input",
        "K-output",
        "K-claim",
        "K-forgetting",
        "K-version",
        "Circle                   := Coeq Unit Unit idmap idmap",
        "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [token for token in required if token not in report]
    coverage = audit.get("read_coverage", {})
    coverage_ok = all(value == "FULL_READ" for value in coverage.values()) and len(coverage) == 5
    identity_ok = audit.get("repository") == "https://github.com/HoTT/Coq-HoTT" and audit.get("commit") == "e3deab71b9cb53a22c00ab39dea4699dd2c89a13"
    result = {
        "schema_version": "p11-coqhott-circle-coequalizer-verification/v1",
        "task_id": "P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-001",
        "status": "PASS_WITH_SCOPE" if not missing and coverage_ok and identity_ok else "FAIL",
        "verdict": "NOT_A_CONSUMER / DEFENSE_EXPLICIT_GLUING_AND_COHERENCE / EXPLICIT_ADMITTED_TORUS_BOUNDARY / P12_THIRD_SUCCESSOR_DISCOVERY_REQUIRED / NO_NEW_HOTT_DEFECT_CLAIM",
        "scope": "Checks the five-file source-audit report and fixed identity only. It does not compile Coq-HoTT, verify the admitted lemma, audit further consumers, establish K, or prove a HoTT defect.",
        "sources": {
            str(REPORT.relative_to(ROOT)): sha(REPORT),
            str(AUDIT.relative_to(ROOT)): sha(AUDIT),
            "audit/p10-second-successor-discovery-20260921/P10-COQHOTT-CANDIDATE-FREEZE.json": sha(ROOT / "audit/p10-second-successor-discovery-20260921/P10-COQHOTT-CANDIDATE-FREEZE.json"),
            "HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md": sha(ROOT / "HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md"),
            "HoTT后续研究总体方案/005 - 当前第一步与交接.md": sha(ROOT / "HoTT后续研究总体方案/005 - 当前第一步与交接.md"),
        },
        "missing_required_tokens": missing,
        "source_identity_ok": identity_ok,
        "full_read_coverage_ok": coverage_ok,
        "public_sources_checked": [
            "https://github.com/HoTT/Coq-HoTT/blob/master/theories/Spaces/Circle.v",
            "https://hott.github.io/Coq-HoTT/coqdoc-html/HoTT.Colimits.Coeq.html",
            "https://arxiv.org/abs/1610.04591",
        ],
    }
    if args.write:
        RECEIPT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
