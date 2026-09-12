#!/usr/bin/env python3
"""Validate structural coverage and denominator contracts of history ledgers."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"FAIL {path}:{number}: {exc}") from exc
        if not isinstance(value, dict):
            raise SystemExit(f"FAIL {path}:{number}: object required")
        rows.append(value)
    return rows


def unique(rows: list[dict], key: str, label: str) -> None:
    values = [row.get(key) for row in rows]
    if any(value in (None, "") for value in values):
        raise SystemExit(f"FAIL {label}: missing {key}")
    if len(values) != len(set(values)):
        raise SystemExit(f"FAIL {label}: duplicate {key}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.project_root.resolve()
    audit = root / "audit"
    user = read_jsonl(audit / "user-message-disposition.jsonl")
    responses = read_jsonl(audit / "ai-response-ledger.jsonl")
    tools = read_jsonl(audit / "tool-event-ledger.jsonl")
    sections = read_jsonl(audit / "webgpt-section-ledger.jsonl")
    thoughts = read_jsonl(audit / "gemini-thought-ledger.jsonl")
    execution = read_jsonl(audit / "gemini-execution-ledger.jsonl")
    products = read_jsonl(audit / "work-product-ledger.jsonl")
    claims = read_jsonl(audit / "claim-evidence-ledger.jsonl")
    summary = json.loads((audit / "ledger-summary.json").read_text(encoding="utf-8"))
    core = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))

    unique(user, "source_message_id", "user disposition")
    unique(responses, "response_id", "AI responses")
    unique(tools, "tool_event_id", "tool events")
    unique(sections, "section_id", "WebGPT sections")
    unique(thoughts, "thought_id", "Gemini thoughts")
    unique(execution, "execution_id", "Gemini execution")
    unique(products, "artifact_id", "work products")
    unique(claims, "claim_id", "claims")

    message_counts = Counter((row.get("platform"), row.get("input_role")) for row in user)
    expected_messages = {
        ("LocalGPT", "primary"): 10,
        ("WebGPT", "primary"): 56,
        ("Gemini", "primary"): 22,
        ("LocalGPT", "supplemental"): 37,
    }
    for key, expected in expected_messages.items():
        if message_counts[key] != expected:
            raise SystemExit(f"FAIL user denominator {key}: {message_counts[key]} != {expected}")
    if len(user) != 125:
        raise SystemExit(f"FAIL user total: {len(user)} != 125")
    if not any(
        row.get("platform") == "Gemini"
        and row.get("disposition") == "ATTACHMENT_REFERENCE_ONLY"
        and row.get("attachment_reference")
        for row in user
    ):
        raise SystemExit("FAIL Gemini Drive attachment reference was not preserved")

    response_counts = Counter(row.get("platform") for row in responses)
    if response_counts != Counter({"LocalGPT": 305, "WebGPT": 55, "Gemini": 24}):
        raise SystemExit(f"FAIL response denominators: {response_counts}")
    local_primary = [row for row in responses if row.get("source_id") in {"codex-parent", "codex-hott2-main"}]
    if len(local_primary) != 220 or sum(not row.get("full_text_available") for row in local_primary):
        raise SystemExit("FAIL LocalGPT parent/main visible response full-text contract")
    if sum(row.get("section_type") == "prompt" for row in sections) != 56 or sum(row.get("section_type") == "response" for row in sections) != 55 or len(sections) != 111:
        raise SystemExit("FAIL WebGPT 56/55/111 section contract")

    tool_counts = Counter((row.get("source_id"), row.get("event_kind")) for row in tools)
    if tool_counts[("codex-parent", "tool_call")] != 1037 or tool_counts[("codex-parent", "tool_result")] != 1037:
        raise SystemExit("FAIL parent tool denominator")
    if tool_counts[("codex-hott2-main", "tool_call")] != 106 or tool_counts[("codex-hott2-main", "tool_result")] != 106:
        raise SystemExit("FAIL HoTT-2 main tool denominator")
    calls = {row.get("call_id"): row for row in tools if row.get("event_kind") == "tool_call"}
    results = {row.get("call_id"): row for row in tools if row.get("event_kind") == "tool_result"}
    for call_id, row in calls.items():
        if row.get("matching_result_id") != results.get(call_id, {}).get("tool_event_id"):
            raise SystemExit(f"FAIL unpaired tool call: {call_id}")
    for call_id, row in results.items():
        if row.get("matching_call_id") != calls.get(call_id, {}).get("tool_event_id"):
            raise SystemExit(f"FAIL unpaired tool result: {call_id}")

    if len(thoughts) != 21 or len(execution) != 36:
        raise SystemExit("FAIL Gemini thought/execution denominator")
    execution_counts = Counter(row.get("record_type") for row in execution)
    if execution_counts != Counter({"executableCode": 17, "codeExecutionResult": 17, "inlineFile": 2}):
        raise SystemExit(f"FAIL Gemini execution types: {execution_counts}")
    inline = [row for row in execution if row.get("record_type") == "inlineFile"]
    if len(inline) != 2 or any(not row.get("content") or row.get("decode_status") != "DECODED_UTF8" for row in inline):
        raise SystemExit("FAIL inlineFile decode/content contract")

    expected_summary = summary.get("counts", {})
    actual_summary = {
        "user_message_disposition": len(user),
        "ai_response_ledger": len(responses),
        "tool_event_ledger": len(tools),
        "webgpt_sections": len(sections),
        "gemini_thought_records": len(thoughts),
        "gemini_execution_records": len(execution),
        "work_products": len(products),
        "claim_evidence_rows": len(claims),
    }
    for key, value in actual_summary.items():
        if expected_summary.get(key) != value:
            raise SystemExit(f"FAIL ledger summary {key}: {expected_summary.get(key)} != {value}")
    if not summary.get("trajectory_sources") or summary.get("errors"):
        raise SystemExit("FAIL trajectory summary has no sources or contains errors")
    core_units = len(core.get("units", []))
    declared_core_units = core.get("counts", {}).get("core_units")
    if not isinstance(declared_core_units, int) or core_units != declared_core_units:
        raise SystemExit(f"FAIL core manifest unit count: {core_units} != {declared_core_units}")
    generation = core.get("generation")
    if not isinstance(generation, str) or not generation.startswith("core-cognition-generation-"):
        raise SystemExit("FAIL core generation identity")
    if any(not isinstance(row.get("claim_text"), str) or not row.get("claim_text") for row in claims):
        raise SystemExit("FAIL empty claim row")
    report = {
        "schema_version": "history-ledger-verification/v1",
        "status": "PASS",
        "source_summary": "audit/ledger-summary.json",
        "counts": {
            "user_messages": len(user),
            "responses": len(responses),
            "local_primary_responses": len(local_primary),
            "tool_events": len(tools),
            "webgpt_sections": len(sections),
            "gemini_thoughts": len(thoughts),
            "gemini_execution": dict(execution_counts),
            "work_products": len(products),
            "claims": len(claims),
            "core_units": core_units,
            "core_generation": generation,
        },
        "checks": [
            "primary and supplemental user-message denominators",
            "LocalGPT parent/main visible response count and full inspect availability",
            "LocalGPT tool call/result count and bidirectional call_id pairing",
            "WebGPT 56 prompt + 55 response + 111 section count",
            "Gemini 21 thought + 17 executableCode + 17 codeExecutionResult + 2 inlineFile",
            "unique IDs, nonempty claims, source manifest and generation-relative core boundary",
        ],
        "scope": "Structural/provenance verification only; no mathematical truth or model understanding certification",
    }
    (audit / "verification-report.json").write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "user_messages": len(user),
        "responses": len(responses),
        "local_primary_responses": len(local_primary),
        "tool_events": len(tools),
        "webgpt_sections": len(sections),
        "gemini_thoughts": len(thoughts),
        "gemini_execution": dict(execution_counts),
        "work_products": len(products),
        "claims": len(claims),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
