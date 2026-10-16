#!/usr/bin/env python3
"""Deterministic under-covered-owner sample of the understanding claims (N14b, batch 3).

Fixed rule (no result-dependence):

1. For every owner document compute the sampling ratio
   (claims already sampled in batches 1-2 / total claims of that owner).
2. Rank owners by ratio ascending (ties broken by owner path); take the 8
   lowest-ratio owners.
3. From each selected owner take up to 4 equal-spaced claims, excluding
   batch-1/2 claims.

Review verdicts are written by the current AI into the companion report.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = "audit/claim-evidence-ledger.jsonl"
BATCH1 = "audit/understanding-claim-sample-20260912.json"
BATCH2 = "audit/understanding-claim-sample-batch2-20260912.json"
OUTPUT = "audit/understanding-claim-sample-batch3-20260912.json"
OWNERS = 8
PER_OWNER = 4


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
    prior = set()
    for rel in (BATCH1, BATCH2):
        prior |= {e["claim_id"] for e in json.loads((root / rel).read_text(encoding="utf-8"))["entries"]}

    by_owner: dict[str, list[dict]] = {}
    for row in rows:
        by_owner.setdefault(row["claim_owner_document"], []).append(row)

    ranked = []
    for owner, claims in by_owner.items():
        sampled = sum(1 for c in claims if c["claim_id"] in prior)
        ranked.append((sampled / len(claims), owner, claims, sampled))
    ranked.sort(key=lambda item: (item[0], item[1]))

    entries, selection = [], []
    for ratio, owner, claims, sampled in ranked[:OWNERS]:
        pool = [c for c in claims if c["claim_id"] not in prior]
        picked = equidistant(pool, PER_OWNER)
        selection.append({"owner": owner, "total": len(claims), "prior_sampled": sampled,
                          "ratio": round(ratio, 4), "selected": len(picked)})
        for row in picked:
            entries.append({
                "claim_id": row["claim_id"],
                "owner_document": owner,
                "line": row.get("claim_line"),
                "claim_type": row.get("claim_type"),
                "text": (row.get("claim_text") or "")[:400],
                "review_verdict": None,
                "review_reason": None,
            })

    payload = {
        "schema_version": "understanding-claim-sample-batch3/v1",
        "sampling_rule": {
            "rank": "owners by prior sampling ratio ascending, ties by path",
            "owners_taken": OWNERS,
            "per_owner": PER_OWNER,
            "prior_sampled_ids": len(prior),
        },
        "selection": selection,
        "entries": entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "SAMPLED", "total": len(entries), "selection": selection,
                      "output": str(out_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
