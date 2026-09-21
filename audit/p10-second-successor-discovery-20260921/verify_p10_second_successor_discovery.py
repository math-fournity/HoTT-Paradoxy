#!/usr/bin/env python3
"""Verify the bounded P10 successor-selection artifact."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md"
FREEZE = OUT / "P10-COQHOTT-CANDIDATE-FREEZE.json"
RESULT = OUT / "P10-SECOND-SUCCESSOR-DISCOVERY-VERIFICATION.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = REPORT.read_text(encoding="utf-8")
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    required = [
        "SUCCESSOR_SELECTED",
        "COQHOTT_CIRCLE_COEQUALIZER_CORPUS_CANDIDATE",
        "P11_NOT_STARTED",
        "P10-SECOND-SUCCESSOR-DISCOVERY-001",
        "Circle := Coeq Unit Unit idmap idmap",
        "K-input",
        "K-output",
        "K-claim",
        "K-forgetting",
        "K-version",
        "NEARBY_NOT_SAME_TASK",
        "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [token for token in required if token not in report]
    identity_ok = freeze["repository"] == "https://github.com/HoTT/Coq-HoTT" and freeze["commit"] == "e3deab71b9cb53a22c00ab39dea4699dd2c89a13" and len(freeze["files"]) == 5
    result = {
        "schema_version": "p10-second-successor-discovery-verification/v1",
        "task_id": "P10-SECOND-SUCCESSOR-DISCOVERY-001",
        "status": "PASS_WITH_SCOPE" if not missing and identity_ok else "FAIL",
        "verdict": "SUCCESSOR_SELECTED / COQHOTT_CIRCLE_COEQUALIZER_CORPUS_CANDIDATE / P11_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "scope": "Checks only the bounded discovery comparison and candidate identity. It does not inspect the remote checkout, typecheck Coq-HoTT, audit P11, find K, or prove a HoTT defect.",
        "sources": {
            str(REPORT.relative_to(ROOT)): digest(REPORT),
            str(FREEZE.relative_to(ROOT)): digest(FREEZE),
            "HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md": digest(ROOT / "HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md"),
            "HoTT后续研究总体方案/005 - 当前第一步与交接.md": digest(ROOT / "HoTT后续研究总体方案/005 - 当前第一步与交接.md"),
            "ABX行动/005 - 状态、停止条件与未来交接.md": digest(ROOT / "ABX行动/005 - 状态、停止条件与未来交接.md"),
        },
        "missing_required_tokens": missing,
        "candidate_identity_ok": identity_ok,
        "public_sources_checked": [
            "https://github.com/HoTT/Coq-HoTT/blob/master/theories/Spaces/Circle.v",
            "https://hott.github.io/Coq-HoTT/coqdoc-html/HoTT.Colimits.Coeq.html",
            "https://arxiv.org/abs/1610.04591",
            "https://martinescardo.github.io/papers/universe-indiscrete.pdf",
        ],
    }
    if args.write:
        RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
