#!/usr/bin/env python3
"""Deterministic bounded sample of the understanding claims (N12).

Fixed sampling rule (no result-dependence):

1. Keyword inclusion: every claim whose text mentions at least one of the
   keywords below (English, case-insensitive; Chinese, substring) is included.
2. Equal-spacing fill: from the remaining claims (ordered by claim_id), take
   every k-th claim so that the total sample reaches SAMPLE_SIZE.

The output records the rule, the counts and the sampled claims; review
verdicts are written by the current AI into the companion audit document, not
by this script.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = "audit/claim-evidence-ledger.jsonl"
RECON = "audit/cross-source-reconciliation.json"
OUTPUT = "audit/understanding-claim-sample-20260912.json"
SAMPLE_SIZE = 40
KEYWORD_CAP = 30
KEYWORDS_EN = ["univalence", "ua", "hit", "truncation", "cauchy", "sip", "cost", "quotient"]
KEYWORDS_ZH = ["单价", "高阶归纳", "截断", "柯西", "商", "成本", "表示", "资格"]


def load_ledger(root: Path) -> list[dict]:
    rows = []
    for line in (root / LEDGER).read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    rows.sort(key=lambda r: r["claim_id"])
    return rows


def load_recon_index(root: Path) -> dict[str, dict]:
    data = json.loads((root / RECON).read_text(encoding="utf-8"))
    index = {}
    for row in data.get("entries", []):
        if row.get("source_class") == "understanding_claim":
            index[row["source_id"]] = row
    return index


def matched_keywords(text: str) -> list[str]:
    low = text.lower()
    hits = [k for k in KEYWORDS_EN if k in low]
    hits += [k for k in KEYWORDS_ZH if k in text]
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    root = args.project_root.resolve()
    out_path = args.output or (root / OUTPUT)

    rows = load_ledger(root)
    recon = load_recon_index(root)
    keyword_selected = []
    rest = []
    for row in rows:
        hits = matched_keywords(row.get("claim_text", ""))
        if hits:
            keyword_selected.append((row, hits))
        else:
            rest.append(row)

    if len(keyword_selected) > KEYWORD_CAP:
        step = max(1, len(keyword_selected) // KEYWORD_CAP)
        keyword_selected = keyword_selected[::step][:KEYWORD_CAP]

    fill_needed = max(0, SAMPLE_SIZE - len(keyword_selected))
    fill = []
    if fill_needed and rest:
        step = max(1, len(rest) // fill_needed)
        fill = rest[::step][:fill_needed]

    sample = []
    for row, hits in keyword_selected:
        sample.append((row, hits, "KEYWORD"))
    for row in fill:
        sample.append((row, [], "EQUAL_SPACING_FILL"))
    sample.sort(key=lambda item: item[0]["claim_id"])

    entries = []
    for row, hits, mode in sample:
        rec = recon.get(row["claim_id"], {})
        entries.append({
            "claim_id": row["claim_id"],
            "selection_mode": mode,
            "matched_keywords": hits,
            "owner_document": row.get("claim_owner_document"),
            "line": row.get("claim_line"),
            "claim_type": row.get("claim_type"),
            "verdict_in_ledger": row.get("verdict"),
            "text": (row.get("claim_text") or "")[:400],
            "direction_ids": rec.get("direction_ids", []),
            "result_ids": rec.get("result_ids", []),
            "semantic_status": rec.get("semantic_status"),
            "review_verdict": None,
            "review_reason": None,
        })

    payload = {
        "schema_version": "understanding-claim-sample/v1",
        "sampling_rule": {
            "keyword_inclusion": {"en": KEYWORDS_EN, "zh": KEYWORDS_ZH},
            "keyword_cap": KEYWORD_CAP,
            "keyword_subsampling": "equal-spacing subsample of the keyword stratum when it exceeds the cap",
            "equal_spacing_fill": "ordered by claim_id; take every k-th remaining claim to reach SAMPLE_SIZE",
            "sample_size": SAMPLE_SIZE,
        },
        "counts": {
            "total_claims": len(rows),
            "keyword_selected": len(keyword_selected),
            "fill_selected": len(fill),
            "sample_size": len(entries),
        },
        "entries": entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "SAMPLED", "counts": payload["counts"], "output": str(out_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
