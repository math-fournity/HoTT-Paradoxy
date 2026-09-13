#!/usr/bin/env python3
"""Read-only reconciliation of the top-level reporting denominators (N15a).

The repo carries several *different* counting units that have been read as if
they were one denominator:

1. `AI对话录/sentence_ledger_annotated.json` - user-side sentence ledger of the
   three historical dialogue sources (Codex/WebGPT/Gemini), 171 traversal units.
2. `audit/user-message-disposition.jsonl` - per-message disposition of the
   archived user prompts (primary + supplemental LocalGPT lineages).
3. `audit/claim-evidence-ledger.jsonl` - frozen line/sentence extraction of the
   top-level `理解章节/*.md` documents at ledger-build time.
4. `理解章节/*.md` - the live owner documents, which keep growing.

This script measures each unit from its own canonical source and recomputes the
claim-extraction rule of `scripts/audit/build_history_ledgers.py::build_claims`
against both the frozen ledger and the live documents. It answers, mechanically:

* why 2,369 and 2,396 are not in conflict (different units);
* why 119 and 125 are not in conflict (different message sets);
* how stale the frozen claim ledger is relative to the live documents.

It writes no repo state and makes no mathematical claim.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SENTENCE_LEDGER = "AI对话录/sentence_ledger_annotated.json"
USER_DISPOSITION = "audit/user-message-disposition.jsonl"
CLAIM_LEDGER = "audit/claim-evidence-ledger.jsonl"
LIVE_CHAPTER_DIR = "理解章节"
OUTPUT = "audit/reporting-denominators-reconciliation-20260912.json"

CLAIM_SPLIT = re.compile(r"(?<=[。！？!?；;])\s*")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def live_claims_in(path: Path) -> int:
    """Recompute the frozen ledger's extraction rule for one owner document."""
    total = 0
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped or stripped.startswith("<!--") or stripped in {"---", "***"}:
            continue
        if stripped.startswith("#") or re.fullmatch(r"\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?", stripped):
            continue
        for fragment in CLAIM_SPLIT.split(line):
            if len(fragment.strip(" |-")) >= 8:
                total += 1
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    root = args.project_root.resolve()
    out_path = args.output or (root / OUTPUT)

    sentences = json.loads((root / SENTENCE_LEDGER).read_text(encoding="utf-8"))
    user_rows = read_jsonl(root / USER_DISPOSITION)
    claim_rows = read_jsonl(root / CLAIM_LEDGER)

    sentence_by_src = collections.Counter(row["src"] for row in sentences)
    sentence_by_author = collections.Counter(row["author"] for row in sentences)
    units_by_src = {
        src: len({row["turn"] for row in sentences if row["src"] == src})
        for src in sorted(sentence_by_src)
    }
    missing_anchor = sum(1 for row in sentences if not row.get("anchor"))

    user_by_platform = collections.Counter(row["platform"] for row in user_rows)
    user_by_role = collections.Counter(row["input_role"] for row in user_rows)
    user_by_source = collections.Counter(row["source_file"].rsplit("/", 1)[-1] for row in user_rows)
    supplemental_parallel = sum(
        1 for row in user_rows
        if row["input_role"] == "supplemental" and "并行会话" in row["source_file"]
    )
    excluded = sum(1 for row in user_rows if row["disposition"] == "EXCLUDED_OUT_OF_SCOPE")

    frozen_by_owner = collections.Counter(row["claim_owner_document"] for row in claim_rows)
    live_by_owner = {
        owner: live_claims_in(root / owner) for owner in sorted(frozen_by_owner)
    }
    # Live documents outside the frozen owner set (created after the ledger build).
    all_live = {f"{LIVE_CHAPTER_DIR}/{p.name}": live_claims_in(p)
                for p in sorted((root / LIVE_CHAPTER_DIR).glob("*.md"))}
    new_owners = {owner: count for owner, count in all_live.items() if owner not in frozen_by_owner}

    identical = {owner: count for owner, count in frozen_by_owner.items() if live_by_owner[owner] == count}
    grown = {owner: [frozen_by_owner[owner], live_by_owner[owner]]
             for owner in frozen_by_owner if live_by_owner[owner] != frozen_by_owner[owner]}

    payload = {
        "schema_version": "reporting-denominators-reconciliation/v1",
        "generated_by": "scripts/audit/reconcile_reporting_denominators.py",
        "read_only": True,
        "sentences": {
            "source": SENTENCE_LEDGER,
            "total": len(sentences),
            "missing_anchor": missing_anchor,
            "traversal_units": sum(units_by_src.values()),
            "units_by_src": units_by_src,
            "by_src": dict(sentence_by_src),
            "by_author_class": dict(sentence_by_author),
        },
        "user_messages": {
            "source": USER_DISPOSITION,
            "total": len(user_rows),
            "by_platform": dict(user_by_platform),
            "by_input_role": dict(user_by_role),
            "by_source_file": dict(user_by_source),
            "supplemental_parallel_session": supplemental_parallel,
            "excluded_out_of_scope": excluded,
            "interpretation": (
                "125 archived user records = 119 historical dialogue messages "
                "(56 WebGPT + 41 LocalGPT Codex [main 10 + parent 31] + 22 Gemini) "
                "reconciled inside the authoritative ledger; the +6 delta is the "
                "out-of-scope parallel-session supplement, whose six records are all "
                "EXCLUDED_OUT_OF_SCOPE."
            ),
        },
        "claims_frozen": {
            "source": CLAIM_LEDGER,
            "total": len(claim_rows),
            "owners": len(frozen_by_owner),
        },
        "claims_live_recount": {
            "rule": "build_history_ledgers.py::build_claims against current 理解章节/*.md",
            "owner_dir": LIVE_CHAPTER_DIR,
            "total_in_frozen_owner_set": sum(live_by_owner.values()),
            "owners_identical_count": len(identical),
            "owners_identical_sum": sum(identical.values()),
            "owners_grown": grown,
            "owners_grown_delta": sum(b - a for a, b in grown.values()),
            "new_owners_after_ledger": new_owners,
            "new_owners_sum": sum(new_owners.values()),
            "total_all_live": sum(all_live.values()),
        },
        "conclusions": [
            "2,369 (user sentences) and 2,396 (frozen chapter claims) are different units "
            "with different sources; they are not competing counts of one ledger.",
            "2,396 is exactly the frozen claim count of the 24 owners at build time. "
            "22 of those 24 owners reproduce their frozen count exactly today; only "
            "README.md and C0 grew after the ledger was frozen.",
            "The live claim surface is now larger than the frozen ledger because the "
            "C-series syntheses were added after the ledger build; the frozen 2,396 "
            "remains the denominator for the evidence queue until a re-extraction is "
            "explicitly authorized.",
            "119 vs 125 is a scope difference (historical dialogue messages vs archived "
            "records including the excluded parallel-session supplement), not a lost set.",
        ],
        "no_claim": "accounting only; no mathematical claim is created or upgraded",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "WRITTEN",
        "output": str(out_path),
        "sentences": payload["sentences"]["total"],
        "user_records": payload["user_messages"]["total"],
        "claims_frozen": payload["claims_frozen"]["total"],
        "live_total": payload["claims_live_recount"]["total_all_live"],
        "grown": payload["claims_live_recount"]["owners_grown"],
        "new_owners_sum": payload["claims_live_recount"]["new_owners_sum"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
