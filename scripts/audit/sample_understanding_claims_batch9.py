#!/usr/bin/env python3
"""Deterministic proportion-matched sample of the understanding claims (N20, batch 9).

Fixed rule (no result-dependence), continuing batches 1-8:

1. Start from the frozen 2,396-row claim ledger.
2. Compute the sampled ratio of every owner document after batches 1-8.
3. Allocation walks the owners in ratio order (ties by path) and tops each
   owner up to the 5-claim cap before moving to the next, never giving an owner
   more than it has unsampled claims left. Owners whose frozen claims were all
   sampled by batches 1-8 are skipped (nothing left to take). The first eight
   owners in ratio order therefore absorb the full 40-claim budget at exactly
   5 each.
4. Within an owner, take equal-spaced claims, excluding batches 1-8.

Review verdicts are written by the current AI into the companion report.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = "audit/claim-evidence-ledger.jsonl"
PRIOR = (
    "audit/understanding-claim-sample-20260912.json",
    "audit/understanding-claim-sample-batch2-20260912.json",
    "audit/understanding-claim-sample-batch3-20260912.json",
    "audit/understanding-claim-sample-batch4-20260912.json",
    "audit/understanding-claim-sample-batch5-20260912.json",
    "audit/understanding-claim-sample-batch6-20260912.json",
    "audit/understanding-claim-sample-batch7-20260912.json",
    "audit/understanding-claim-sample-batch8-20260912.json",
)
OUTPUT = "audit/understanding-claim-sample-batch9-20260912.json"
BUDGET = 40
MAX_PER_OWNER = 5


def equidistant(rows: list[dict], k: int) -> list[dict]:
    if k >= len(rows):
        return rows
    step = len(rows) / k
    picked, seen = [], set()
    for i in range(k):
        row = rows[min(len(rows) - 1, int(i * step))]
        if row["claim_id"] not in seen:
            seen.add(row["claim_id"])
            picked.append(row)
    return picked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    root = args.project_root.resolve()
    out_path = args.output or (root / OUTPUT)

    rows = [json.loads(line) for line in (root / LEDGER).read_text(encoding="utf-8").splitlines() if line.strip()]
    rows.sort(key=lambda r: r["claim_id"])
    prior_ids: set[str] = set()
    for rel in PRIOR:
        prior_ids |= {e["claim_id"] for e in json.loads((root / rel).read_text(encoding="utf-8"))["entries"]}

    by_owner: dict[str, list[dict]] = {}
    for row in rows:
        by_owner.setdefault(row["claim_owner_document"], []).append(row)

    ranked = []
    for owner, claims in by_owner.items():
        sampled = sum(1 for c in claims if c["claim_id"] in prior_ids)
        remaining = len(claims) - sampled
        ranked.append({"owner": owner, "claims": claims, "total": len(claims),
                       "prior_sampled": sampled, "ratio": sampled / len(claims),
                       "remaining": remaining})
    ranked.sort(key=lambda item: (item["ratio"], item["owner"]))

    allocation: dict[str, int] = {}
    remaining_budget = BUDGET
    for item in ranked:
        if remaining_budget <= 0:
            break
        take = min(MAX_PER_OWNER, item["remaining"], remaining_budget)
        if take <= 0:
            continue
        allocation[item["owner"]] = take
        remaining_budget -= take

    entries, selection = [], []
    for item in ranked:
        want = allocation.get(item["owner"], 0)
        if not want:
            continue
        pool = [c for c in item["claims"] if c["claim_id"] not in prior_ids]
        picked = equidistant(pool, want)
        selection.append({
            "owner": item["owner"],
            "total": item["total"],
            "prior_sampled": item["prior_sampled"],
            "prior_ratio": round(item["ratio"], 4),
            "remaining": item["remaining"],
            "selected": len(picked),
        })
        for row in picked:
            entries.append({
                "claim_id": row["claim_id"],
                "owner_document": item["owner"],
                "line": row.get("claim_line"),
                "claim_type": row.get("claim_type"),
                "text": (row.get("claim_text") or "")[:400],
                "artifact_locators": row.get("artifact_locators"),
                "source_locators": row.get("source_locators"),
                "review_verdict": None,
                "review_reason": None,
            })

    entries.sort(key=lambda e: e["claim_id"])
    payload = {
        "schema_version": "understanding-claim-sample-batch9/v1",
        "sampling_rule": {
            "rank": "owners by prior sampling ratio ascending, ties by path",
            "budget": BUDGET,
            "max_per_owner": MAX_PER_OWNER,
            "allocation": allocation,
            "prior_sampled_ids": len(prior_ids),
            "fully_sampled_owners_skipped": [i["owner"] for i in ranked if i["remaining"] == 0],
        },
        "selection": selection,
        "entries": entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "SAMPLED", "total": len(entries), "allocation": allocation,
                      "selection": selection, "output": str(out_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
