#!/usr/bin/env python3
"""Deterministic proportion-matched sample of the understanding claims (N15b, batch 4).

Fixed rule (no result-dependence), continuing batches 1-3:

1. Start from the frozen 2,396-row claim ledger.
2. Compute the sampled ratio of every owner document after batches 1-3.
3. Allocate the batch as far as possible toward the lowest-ratio owners
   (ties broken by owner path), taking up to 5 claims per owner, then the
   remaining budget at 4/3/2/1 per owner in the same ranking order.
4. Within an owner, take equal-spaced claims, excluding batches 1-3.

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
)
OUTPUT = "audit/understanding-claim-sample-batch4-20260912.json"
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
        ranked.append((sampled / len(claims), owner, claims, sampled))
    ranked.sort(key=lambda item: (item[0], item[1]))

    allocation: dict[str, int] = {}
    remaining = BUDGET
    for cap in range(MAX_PER_OWNER, 0, -1):
        for ratio, owner, claims, sampled in ranked:
            if remaining <= 0:
                break
            pool_size = len(claims) - sampled
            room = min(cap, pool_size) - allocation.get(owner, 0)
            if room <= 0:
                continue
            take = min(room, remaining)
            allocation[owner] = allocation.get(owner, 0) + take
            remaining -= take
        if remaining <= 0:
            break

    entries, selection = [], []
    for ratio, owner, claims, sampled in ranked:
        want = allocation.get(owner, 0)
        if not want:
            continue
        pool = [c for c in claims if c["claim_id"] not in prior_ids]
        picked = equidistant(pool, want)
        selection.append({
            "owner": owner,
            "total": len(claims),
            "prior_sampled": sampled,
            "prior_ratio": round(ratio, 4),
            "selected": len(picked),
        })
        for row in picked:
            entries.append({
                "claim_id": row["claim_id"],
                "owner_document": owner,
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
        "schema_version": "understanding-claim-sample-batch4/v1",
        "sampling_rule": {
            "rank": "owners by prior sampling ratio ascending, ties by path",
            "budget": BUDGET,
            "max_per_owner": MAX_PER_OWNER,
            "allocation": allocation,
            "prior_sampled_ids": len(prior_ids),
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
