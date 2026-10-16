#!/usr/bin/env python3
"""Deterministic stratified sample of the understanding claims (N13, batch 2).

Fixed rule (no result-dependence):

1. Strata by owner document class:
   - C-series (current syntheses): 理解章节/C*.md
   - meta class: 读遍账本.md / 全量精读工作方案.md / 升级方案-v2.md / README.md / 审计锚点-AI侧.md
   - A-series: 理解章节/A*.md
   - B-series: 理解章节/B*.md
2. Sample sizes: C=10, meta=10, A=15, B=15 (total 50).
3. Within each stratum: drop claims already sampled in batch 1, order by claim_id,
   and take an equal-spaced subsample of the target size.

Review verdicts are written by the current AI into the companion report.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = "audit/claim-evidence-ledger.jsonl"
BATCH1 = "audit/understanding-claim-sample-20260912.json"
OUTPUT = "audit/understanding-claim-sample-batch2-20260912.json"
SIZES = {"C": 10, "meta": 10, "A": 15, "B": 15}
META_NAMES = {"读遍账本.md", "全量精读工作方案.md", "升级方案-v2.md", "README.md", "审计锚点-AI侧.md"}


def stratum_of(owner: str) -> str:
    name = (owner or "").split("/")[-1]
    if name.startswith("C"):
        return "C"
    if name in META_NAMES:
        return "meta"
    if name.startswith("A"):
        return "A"
    if name.startswith("B"):
        return "B"
    return "meta"


def equidistant(rows: list[dict], k: int) -> list[dict]:
    if k >= len(rows):
        return rows
    step = len(rows) / k
    picked = [rows[min(len(rows) - 1, int(i * step))] for i in range(k)]
    seen, out = set(), []
    for row in picked:
        if row["claim_id"] not in seen:
            seen.add(row["claim_id"])
            out.append(row)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    root = args.project_root.resolve()
    out_path = args.output or (root / OUTPUT)

    rows = [json.loads(line) for line in (root / LEDGER).read_text(encoding="utf-8").splitlines() if line.strip()]
    rows.sort(key=lambda r: r["claim_id"])
    batch1 = {e["claim_id"] for e in json.loads((root / BATCH1).read_text(encoding="utf-8"))["entries"]}

    strata: dict[str, list[dict]] = {"A": [], "B": [], "C": [], "meta": []}
    for row in rows:
        strata[stratum_of(row.get("claim_owner_document", ""))].append(row)

    entries, counts = [], {}
    for key in ("C", "meta", "A", "B"):
        pool = [r for r in strata[key] if r["claim_id"] not in batch1]
        picked = equidistant(pool, SIZES[key])
        counts[key] = {"stratum_size": len(strata[key]), "pool_after_batch1": len(pool), "selected": len(picked)}
        for row in picked:
            entries.append({
                "claim_id": row["claim_id"],
                "stratum": key,
                "owner_document": row.get("claim_owner_document"),
                "line": row.get("claim_line"),
                "claim_type": row.get("claim_type"),
                "text": (row.get("claim_text") or "")[:400],
                "review_verdict": None,
                "review_reason": None,
            })

    payload = {
        "schema_version": "understanding-claim-sample-batch2/v1",
        "sampling_rule": {
            "strata": ["C-series", "meta class", "A-series", "B-series"],
            "sizes": SIZES,
            "within_stratum": "drop batch-1 claims; order by claim_id; equal-spaced subsample",
            "batch1_excluded": len(batch1),
        },
        "counts": counts,
        "entries": entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "SAMPLED", "counts": counts, "total": len(entries), "output": str(out_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
