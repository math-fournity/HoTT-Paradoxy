#!/usr/bin/env python3
"""Read-only verification of the numeric/hash spot-checks cited by the batch-4 review.

Every check is a fixed claim from `audit/understanding-claim-sample-batch4-20260912.json`
that must be traceable to an authoritative artifact in this repo. Exit code is
non-zero if any check fails, so the audit report cannot silently claim a checked
number.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "audit/understanding-claim-batch4-spot-checks-20260912.json"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    root = args.project_root.resolve()
    out_path = args.output or (root / OUTPUT)

    manifest = json.loads((root / "sources/SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    manifest_text = json.dumps(manifest, ensure_ascii=False)
    store = json.loads((root / "archive/STORE.json").read_text(encoding="utf-8"))
    store_relatives = [f.get("relative", "") for f in store.get("files", [])]
    thought_rows = read_jsonl(root / "audit/gemini-thought-ledger.jsonl")
    execution_rows = read_jsonl(root / "audit/gemini-execution-ledger.jsonl")
    summary = json.loads((root / "audit/ledger-summary.json").read_text(encoding="utf-8"))
    b3 = (root / "理解章节/B3-网页GPT工作史-II.md").read_text(encoding="utf-8")
    a2 = (root / "理解章节/A2-参照悖论谱.md").read_text(encoding="utf-8")

    checks: list[dict] = []

    def check(claim_id: str, name: str, ok: bool, observed: str) -> None:
        checks.append({"claim_id": claim_id, "check": name, "ok": bool(ok), "observed": observed})

    check("CL-000849", "MinerU old-snapshot SHA registered",
          "62cef54875fbc0e654b71c9e17895381f4529cddde6ad3a3a7d96f31032affe2" in manifest_text,
          "sha present in sources/SOURCE_MANIFEST.json")
    check("CL-001619", "EARLY-GEMINI review assets in archive store",
          sum(1 for rel in store_relatives if "EARLY-GEMINI-001" in rel) == 3,
          f"{sum(1 for rel in store_relatives if 'EARLY-GEMINI-001' in rel)} assets")
    check("CL-001557", "B3 records 70/3 test result",
          "70 过 3 败" in b3, "phrase found in B3")
    check("CL-001433", "B3 records the all-zero-prefix break",
          "全零流的 0ⁿ 前缀被 0ⁿ1 破坏" in b3, "phrase found in B3")
    check("CL-001495", "B3 records Löb premise distinction",
          "Löb 前提区分" in b3, "phrase found in B3")
    check("CL-002133", "Gemini thought ledger count 21",
          len(thought_rows) == 21, f"{len(thought_rows)}")
    check("CL-002133", "Gemini execution ledger count 36",
          len(execution_rows) == 36, f"{len(execution_rows)}")
    check("CL-002133", "Gemini ordinary text count 24",
          summary["counts"].get("gemini_ordinary_text_responses") == 24,
          str(summary["counts"].get("gemini_ordinary_text_responses")))
    check("CL-002324", "LocalGPT primary lineage responses 220",
          summary["counts"].get("local_gpt_primary_lineage_assistant_responses") == 220,
          str(summary["counts"].get("local_gpt_primary_lineage_assistant_responses")))
    check("CL-002154", "WebGPT section ledger denominator 111",
          summary["counts"].get("webgpt_sections") == 111,
          str(summary["counts"].get("webgpt_sections")))
    check("CL-000324", "A2 states the user-reading principle",
          "按用户的读法展开，不用世界通行读法替代" in a2, "phrase found in A2")
    check("CL-002251", "读遍账本 records the HoTT-2 residual M state",
          "HoTT-2 主其余 ~30 条回复" in (root / "理解章节/读遍账本.md").read_text(encoding="utf-8"),
          "phrase found in 读遍账本")
    sample_path = root / "audit/understanding-claim-sample-batch4-20260912.json"
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    reviewed = [e for e in sample["entries"] if e.get("review_verdict")]
    check("batch4", "all 40 sampled claims carry a verdict",
          len(reviewed) == 40, f"{len(reviewed)}")
    check("batch4", "no UNSUPPORTED verdict without counter-evidence",
          not any(e["review_verdict"] == "UNSUPPORTED" for e in reviewed),
          "0 UNSUPPORTED")

    failed = [c for c in checks if not c["ok"]]
    payload = {
        "schema_version": "batch4-spot-checks/v1",
        "read_only": True,
        "checks": checks,
        "passed": len(checks) - len(failed),
        "failed": len(failed),
        "scope_note": (
            "Fixed spot-checks for numbers/hashes cited by batch-4 verdicts. "
            "The 497-line/32,478-byte byte-identity claim of CL-001619 is supported by the "
            "B3 owner text plus archive presence; the byte-level re-hash of the historical "
            "draft is NOT re-run here."
        ),
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS" if not failed else "FAIL", "passed": payload["passed"],
                      "failed": payload["failed"], "output": str(out_path)}, ensure_ascii=False))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
