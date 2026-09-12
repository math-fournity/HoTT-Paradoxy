#!/usr/bin/env python3
"""Verify exhaustive source-row coverage and safe ID/link boundaries."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WEB_STATE = Path("sources/webgpt/workspace-snapshot/.codex/research/hott/STATE.json")
LEDGERS = {
    "local_response": Path("audit/ai-response-ledger.jsonl"),
    "local_tool_event": Path("audit/tool-event-ledger.jsonl"),
    "local_work_product": Path("audit/work-product-ledger.jsonl"),
    "understanding_claim": Path("audit/claim-evidence-ledger.jsonl"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def jsonl_count(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path, default=Path("audit/cross-source-reconciliation.json"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    manifest = json.loads((root / args.manifest).read_text(encoding="utf-8"))
    errors: list[str] = []
    entries = manifest.get("entries", [])
    expected_sources = {"webgpt_state": len(json.loads((root / WEB_STATE).read_text(encoding="utf-8"))["records"])}
    expected_sources.update({kind: jsonl_count(root / path) for kind, path in LEDGERS.items()})
    actual_sources: dict[str, int] = {}
    for entry in entries:
        actual_sources[str(entry.get("source_class"))] = actual_sources.get(str(entry.get("source_class")), 0) + 1
        if not entry.get("source_id"):
            errors.append(f"MISSING_SOURCE_ID:{entry.get('source_class')}:{entry.get('source_row_number')}")
        if not entry.get("source_locator"):
            errors.append(f"MISSING_LOCATOR:{entry.get('source_id')}")
        if not entry.get("direction_ids") and not entry.get("unmapped_reason"):
            errors.append(f"DIRECTION_ORPHAN_WITHOUT_REASON:{entry.get('source_id')}")
        if not entry.get("result_ids") and not entry.get("unmapped_reason"):
            errors.append(f"RESULT_ORPHAN_WITHOUT_REASON:{entry.get('source_id')}")
        if not entry.get("mapping_basis"):
            errors.append(f"MISSING_MAPPING_BASIS:{entry.get('source_id')}")
    if actual_sources != expected_sources:
        errors.append(f"SOURCE_ROW_COUNTS_MISMATCH:expected={expected_sources}:actual={actual_sources}")
    for source_class, path in [("webgpt_state", WEB_STATE), *LEDGERS.items()]:
        row = manifest.get("source_files", {}).get(source_class, {})
        if row.get("sha256") != sha256(root / path):
            errors.append(f"SOURCE_FILE_HASH_MISMATCH:{source_class}")
    counts = manifest.get("counts", {})
    if counts.get("total_register_entries") != len(entries):
        errors.append("TOTAL_COUNT_MISMATCH")
    if counts.get("invalid_direction_ids") != 0 or manifest.get("invalid_direction_ids"):
        errors.append("INVALID_DIRECTION_DOMAIN")
    if counts.get("invalid_result_ids") != 0 or manifest.get("invalid_result_ids"):
        errors.append("INVALID_RESULT_DOMAIN")
    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors[:50], "error_count": len(errors)}, ensure_ascii=False))
        return 1
    print(json.dumps({
        "status": "PASS",
        "total_register_entries": len(entries),
        "source_rows": actual_sources,
        "all_source_rows_have_direction_or_reason": True,
        "all_source_rows_have_result_or_reason": True,
        "mathematical_certification": "NOT_PERFORMED_BY_THIS_REGISTER",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
