#!/usr/bin/env python3
"""Build an exhaustive, provenance-first cross-source reconciliation register.

The register is deliberately conservative.  It gives every WebGPT STATE
record and every row of the four top-level history ledgers a stable source
locator plus candidate direction/result links.  Rule-based links are
navigation aids, not semantic or mathematical certification; sentence-level
claims retain an explicit manual-review status.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WEB_STATE = Path("sources/webgpt/workspace-snapshot/.codex/research/hott/STATE.json")
WEB_ROOT = Path("sources/webgpt/workspace-snapshot")
LEDGERS = {
    "ai_response": Path("audit/ai-response-ledger.jsonl"),
    "local_tool_event": Path("audit/tool-event-ledger.jsonl"),
    "local_work_product": Path("audit/work-product-ledger.jsonl"),
    "understanding_claim": Path("audit/claim-evidence-ledger.jsonl"),
}

DIRECTION_IDS = {
    "DIR-U-A-REALITY-RELATIVE",
    "DIR-U-B-EFFECTIVE-DELIVERY",
    "DIR-L-TIME-WORK-DIMENSION",
    "DIR-L-SAME-FUNCTION-DIFFERENT-TIME",
    "DIR-L-GUARD-ERASURE",
    "DIR-L-RUSSELL-FORMATION",
    "DIR-L-SELF-REFLECTION",
    "DIR-L-MATRIX-CONTINUITY",
    "DIR-L-THEORY-SCHEMA-VARIANTS",
    "DIR-W-RACE-TIMEOUT",
    "DIR-W-SILENT-STEPS",
    "DIR-W-CURRENT-STATE-LIFT",
    "DIR-W-TRANSITION-ABSTRACTION",
    "DIR-W-PATH-CERTIFICATE",
    "DIR-W-DEPENDENT-MIGRATION",
    "DIR-W-RESTRICTED-REFLECTION",
    "DIR-W-PROOF-REFLECTION",
    "DIR-W-SELF-REFLECTION-DOMAIN",
    "DIR-W-SELF-REFERENCE",
    "DIR-W-RP-B01",
    "DIR-W-ATTACHED-HISTORY",
    "DIR-E-LOCAL-HISTORY-COVERAGE",
    "DIR-E-WEB-HISTORY-COVERAGE",
    "DIR-G-UNDERSTANDING-RECONCILIATION",
}
OUTCOME_IDS = {
    "OUT-TOP-CORE-FOUNDATION",
    "OUT-TOP-LEDGERS",
    "OUT-UNDERSTANDING-MERGE",
    "OUT-L-CORE-MATHEMATICAL",
    "OUT-L-TIME-BOUNDARY",
    "OUT-L-GUARD-ERASURE",
    "OUT-L-RUSSELL-MODEL",
    "OUT-L-REFLECTION-FAMILY",
    "OUT-L-CORPUS",
    "OUT-W-TEMPORAL-TRANSPORT",
    "OUT-W-EARLY-EFFECTIVE-CONSTRUCTION",
    "OUT-W-R036",
    "OUT-W-R038",
    "OUT-W-TRANSPORT-REFLECTION",
    "OUT-W-REFLECTION-FAMILY",
    "OUT-W-RP-B01",
    "OUT-W-R039",
    "OUT-W-R001",
    "OUT-W-ATTACHED-AUDITS",
    "OUT-W-GOVERNANCE-V12-V13",
    "OUT-W-PORTABLE-EXCHANGE",
    "OUT-TOP-THREE-WAY-SKELETON",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_hash(root: Path, relative: Path) -> str | None:
    path = root / relative
    return sha256(path.read_bytes()) if path.is_file() else None


def add_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def web_mapping(record_id: str, record: dict[str, object]) -> tuple[list[str], list[str], list[str], str]:
    text = " ".join(str(record.get(k, "")) for k in ("scope", "kind", "path", "status"))
    low = f"{record_id} {text}".lower()
    directions: list[str] = []
    outcomes: list[str] = []
    basis: list[str] = []

    def d(value: str, reason: str) -> None:
        add_unique(directions, value)
        add_unique(basis, reason)

    def o(value: str, reason: str) -> None:
        add_unique(outcomes, value)
        add_unique(basis, reason)

    if record_id == "U-GOAL-20260910-001":
        d("DIR-U-A-REALITY-RELATIVE", "explicit_user_goal")
        o("OUT-TOP-CORE-FOUNDATION", "user_goal_core_boundary")
    elif record_id in {"U-ASK-20260910-001", "U-DUAL-DIRECTION-JSON-001"}:
        d("DIR-U-B-EFFECTIVE-DELIVERY", "explicit_user_direction")
        o("OUT-W-RP-B01", "user_direction_result_family")
    elif record_id == "U-SELF-REFERENCE-20260911-001":
        d("DIR-W-SELF-REFERENCE", "explicit_user_self_reference_question")
        o("OUT-W-REFLECTION-FAMILY", "self_reference_result_family")
    elif record_id.startswith("P-"):
        direct = {
            "P-CURRENT-STATE-LIFTING-038": ("DIR-W-CURRENT-STATE-LIFT", "OUT-W-R038"),
            "P-DEPENDENT-MIGRATION-033": ("DIR-W-DEPENDENT-MIGRATION", "OUT-W-TRANSPORT-REFLECTION"),
            "P-PATH-CERTIFICATE-034": ("DIR-W-PATH-CERTIFICATE", "OUT-W-TRANSPORT-REFLECTION"),
            "P-PROOF-REFLECTION-031": ("DIR-W-PROOF-REFLECTION", "OUT-W-REFLECTION-FAMILY"),
            "P-RESTRICTED-REFLECTION-032": ("DIR-W-RESTRICTED-REFLECTION", "OUT-W-REFLECTION-FAMILY"),
            "P-RP-B01": ("DIR-W-RP-B01", "OUT-W-RP-B01"),
            "P-SELF-REFERENCE-001": ("DIR-W-SELF-REFERENCE", "OUT-W-REFLECTION-FAMILY"),
            "P-SELF-REFLECTION-DOMAIN-030": ("DIR-W-SELF-REFLECTION-DOMAIN", "OUT-W-REFLECTION-FAMILY"),
            "P-SILENT-STEPS-039": ("DIR-W-SILENT-STEPS", "OUT-W-R039"),
            "P-TRANSITION-ABSTRACTION-036": ("DIR-W-TRANSITION-ABSTRACTION", "OUT-W-R036"),
        }
        if record_id in direct:
            direction, outcome = direct[record_id]
            d(direction, "explicit_web_candidate_id")
            o(outcome, "explicit_web_candidate_result")
    elif record_id.startswith("C-UA-TIME-") or record_id == "C-TIME-SCHEDULE-001":
        d("DIR-L-TIME-WORK-DIMENSION", "explicit_web_time_claim_id")
        d("DIR-L-SAME-FUNCTION-DIFFERENT-TIME", "explicit_web_time_claim_id")
        o("OUT-W-TEMPORAL-TRANSPORT", "explicit_web_time_result_family")
    elif record_id.startswith("C-"):
        d("DIR-U-B-EFFECTIVE-DELIVERY", "explicit_web_constructive_claim_id")
        d("DIR-W-RP-B01", "explicit_web_constructive_claim_id")
        o("OUT-W-EARLY-EFFECTIVE-CONSTRUCTION", "explicit_web_constructive_result_family")
    elif record_id.startswith("Q-"):
        d("DIR-E-WEB-HISTORY-COVERAGE", "web_governance_unknown")
        o("OUT-W-ATTACHED-AUDITS", "web_governance_unknown")
        if record_id == "Q-R001-EVIDENCE":
            d("DIR-W-ATTACHED-HISTORY", "r001_source_gap")
            o("OUT-W-R001", "r001_source_gap")
    elif record_id.startswith("R-") or record_id.startswith("A-") or record_id.startswith("D-") or record_id.startswith("V-"):
        d("DIR-W-ATTACHED-HISTORY", "attached_or_historical_record")
        o("OUT-W-ATTACHED-AUDITS", "attached_or_historical_record")
        if record_id.startswith("R-R001"):
            o("OUT-W-R001", "r001_recovery_record")
    elif record_id.startswith("S-"):
        d("DIR-E-WEB-HISTORY-COVERAGE", "web_session_process_record")
        o("OUT-W-ATTACHED-AUDITS", "web_session_process_record")
        session_routes = [
            (r"S-ANS-20260910-(006|007|008)", "DIR-L-TIME-WORK-DIMENSION", "OUT-W-TEMPORAL-TRANSPORT"),
            (r"S-ANS-20260910-(010|011|014|015|016|017)", "DIR-U-B-EFFECTIVE-DELIVERY", "OUT-W-EARLY-EFFECTIVE-CONSTRUCTION"),
            (r"S-RES-20260911-030|S-RES-20260911-031|S-RES-20260911-032", "DIR-W-SELF-REFLECTION-DOMAIN", "OUT-W-REFLECTION-FAMILY"),
            (r"S-RES-20260911-033|S-RES-20260911-034", "DIR-W-DEPENDENT-MIGRATION", "OUT-W-TRANSPORT-REFLECTION"),
            (r"S-RES-20260911-036", "DIR-W-TRANSITION-ABSTRACTION", "OUT-W-R036"),
            (r"S-RES-20260911-038", "DIR-W-CURRENT-STATE-LIFT", "OUT-W-R038"),
            (r"S-RES-20260911-039", "DIR-W-SILENT-STEPS", "OUT-W-R039"),
            (r"S-GOV-20260911-040|S-GOV-20260911-041", "DIR-E-WEB-HISTORY-COVERAGE", "OUT-W-PORTABLE-EXCHANGE"),
            (r"S-GOV-20260910-012|S-GOV-20260910-013", "DIR-E-WEB-HISTORY-COVERAGE", "OUT-W-GOVERNANCE-V12-V13"),
        ]
        for pattern, direction, outcome in session_routes:
            if re.search(pattern, record_id):
                d(direction, "session_name_route")
                o(outcome, "session_name_route")
                break
    if not directions:
        d("DIR-E-WEB-HISTORY-COVERAGE", "safe_web_provenance_fallback")
    if not outcomes:
        o("OUT-W-ATTACHED-AUDITS", "safe_web_provenance_fallback")
    return directions, outcomes, basis, "EXPLICIT_OR_OWNER_ROUTE" if len(basis) and "safe_web_provenance_fallback" not in basis else "PROVENANCE_FALLBACK"


def local_mapping(source_class: str, row: dict[str, object]) -> tuple[list[str], list[str], list[str], str]:
    material = " ".join(
        str(row.get(k, ""))
        for k in (
            "content",
            "claim_text",
            "path",
            "claim_owner_document",
            "evidence",
            "raw_locator",
            "source_path",
            "repo",
            "disposition",
        )
    )
    low = material.lower()
    directions: list[str] = []
    outcomes: list[str] = []
    basis: list[str] = []

    def d(value: str, reason: str) -> None:
        add_unique(directions, value)
        add_unique(basis, reason)

    def o(value: str, reason: str) -> None:
        add_unique(outcomes, value)
        add_unique(basis, reason)

    if any(token in low for token in ("r039", "silent-steps", "may/must", "may but not must")):
        d("DIR-W-SILENT-STEPS", "result_name_or_content")
        o("OUT-W-R039", "result_name_or_content")
    elif "r038" in low or "current-state-lifting" in low or "current state lift" in low:
        d("DIR-W-CURRENT-STATE-LIFT", "result_name_or_content")
        o("OUT-W-R038", "result_name_or_content")
    elif "r036" in low or "transition-abstraction" in low or "state quotient" in low:
        d("DIR-W-TRANSITION-ABSTRACTION", "result_name_or_content")
        o("OUT-W-R036", "result_name_or_content")
    elif any(token in low for token in ("r033", "r034", "dependent-migration", "path-certificate", "set-valued transport", "naturality")):
        d("DIR-W-DEPENDENT-MIGRATION", "result_name_or_content")
        d("DIR-W-PATH-CERTIFICATE", "result_name_or_content")
        o("OUT-W-TRANSPORT-REFLECTION", "result_name_or_content")
    elif any(token in low for token in ("self-reference", "self-reference", "reflection", "löb", "loeb", "proof-reflection", "restricted-reflection")):
        d("DIR-L-SELF-REFLECTION", "reflection_owner_or_content")
        d("DIR-W-SELF-REFERENCE", "reflection_owner_or_content")
        o("OUT-L-REFLECTION-FAMILY", "reflection_owner_or_content")
        o("OUT-W-REFLECTION-FAMILY", "reflection_owner_or_content")
    elif any(token in low for token in ("guard-erasure", "guarded", "guard-erasure", "forgetful translation", "fixed point")):
        d("DIR-L-GUARD-ERASURE", "guard_owner_or_content")
        o("OUT-L-GUARD-ERASURE", "guard_owner_or_content")
    elif any(token in low for token in ("russell", "罗素", "rₙ₊₁", "formation rejection")):
        d("DIR-L-RUSSELL-FORMATION", "russell_owner_or_content")
        o("OUT-L-RUSSELL-MODEL", "russell_owner_or_content")
    elif any(token in low for token in ("matrix", "圆环", "circle paradox", "zeno", "芝诺", "winding")):
        d("DIR-L-MATRIX-CONTINUITY", "matrix_owner_or_content")
        d("DIR-U-A-REALITY-RELATIVE", "matrix_owner_or_content")
        o("OUT-L-CORPUS", "matrix_owner_or_content")
    elif any(token in low for token in ("intrinsic_temporality", "时间维度", "time dimension", "same-function-different-time", "same function", "temporality", "temporal")):
        d("DIR-L-TIME-WORK-DIMENSION", "time_owner_or_content")
        d("DIR-L-SAME-FUNCTION-DIFFERENT-TIME", "time_owner_or_content")
        o("OUT-L-TIME-BOUNDARY", "time_owner_or_content")
    elif any(token in low for token in ("effective delivery", "有效交付", "ho tt研究三问", "theory_schema", "claim_evidence_matrix", "core mathematical")):
        d("DIR-U-B-EFFECTIVE-DELIVERY", "effective-delivery_owner_or_content")
        o("OUT-L-CORE-MATHEMATICAL", "effective-delivery_owner_or_content")
    if any(token in low for token in ("trajectory", "ledger", "audit", "governance", "agents.md", "memory.md", "git", "source_manifest", "理解章节")):
        d("DIR-E-LOCAL-HISTORY-COVERAGE", "provenance_or_governance_anchor")
        o("OUT-TOP-LEDGERS", "provenance_or_governance_anchor")
    if source_class == "understanding_claim":
        basis.append("sentence_level_claim_row")
    if not directions:
        d("DIR-E-LOCAL-HISTORY-COVERAGE", "safe_local_provenance_fallback")
    if not outcomes:
        o("OUT-TOP-LEDGERS", "safe_local_provenance_fallback")
    explicit = not any("fallback" in item for item in basis)
    return directions, outcomes, basis, "OWNER_OR_CONTENT_ROUTE" if explicit else "PROVENANCE_FALLBACK"


def source_locator(row: dict[str, object], source_class: str, row_number: int) -> str:
    for key in ("raw_locator", "claim_owner_document", "path", "source_path"):
        value = row.get(key)
        if value:
            return str(value)
    return f"audit/{source_class}#row-{row_number}"


def register_row(
    root: Path,
    source_class: str,
    row_number: int,
    row: dict[str, object],
    source_file: Path,
    source_sha: str,
) -> dict[str, object]:
    if source_class == "webgpt_state":
        source_id = str(row["source_record_id"])
        directions, outcomes, basis, mapping_mode = web_mapping(source_id, row)
        semantic_status = "HISTORICAL_RECORD_REVIEW_REQUIRED"
        locator = str(row.get("source_locator", row.get("path", "")))
        row_hash = sha256(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        source_file_hash = row.get("source_file_sha256")
    else:
        id_key = {
            "ai_response": "response_id",
            "local_tool_event": "tool_event_id",
            "local_work_product": "artifact_id",
            "understanding_claim": "claim_id",
        }[source_class]
        source_id = str(row.get(id_key, f"{source_class}-{row_number:06d}"))
        directions, outcomes, basis, mapping_mode = local_mapping(source_class, row)
        semantic_status = (
            "PENDING_DIRECT_SENTENCE_ADJUDICATION"
            if source_class == "understanding_claim"
            else "SOURCE_REGISTERED_WITH_SCOPE"
        )
        locator = source_locator(row, source_class, row_number)
        row_hash = sha256(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        source_file_hash = row.get("source_sha256") or row.get("file_sha256")
    return {
        "source_class": source_class,
        "source_id": source_id,
        "source_file": source_file.as_posix(),
        "source_file_sha256": source_sha,
        "source_row_number": row_number,
        "source_row_sha256": row_hash,
        "source_locator": locator,
        "source_embedded_hash": source_file_hash,
        "direction_ids": directions,
        "result_ids": outcomes,
        "mapping_mode": mapping_mode,
        "mapping_basis": basis,
        "semantic_status": semantic_status,
        "unmapped_reason": None,
        "mathematical_certification": "NOT_PERFORMED_BY_THIS_REGISTER",
    }


def load_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def build(root: Path, as_of: str) -> tuple[dict[str, object], str]:
    web_data = json.loads((root / WEB_STATE).read_text(encoding="utf-8"))
    entries: list[dict[str, object]] = []
    source_files: dict[str, dict[str, object]] = {}
    web_sha = file_hash(root, WEB_STATE)
    source_files["webgpt_state"] = {"path": WEB_STATE.as_posix(), "sha256": web_sha, "rows": len(web_data["records"])}
    for record_id, record in sorted(web_data["records"].items()):
        row = dict(record)
        row["source_record_id"] = record_id
        entries.append(register_row(root, "webgpt_state", len(entries) + 1, row, WEB_STATE, str(web_sha)))
    for source_class, path in LEDGERS.items():
        rows = load_jsonl(root / path)
        source_sha = file_hash(root, path)
        source_files[source_class] = {"path": path.as_posix(), "sha256": source_sha, "rows": len(rows)}
        for row_number, row in enumerate(rows, start=1):
            entries.append(register_row(root, source_class, row_number, row, path, str(source_sha)))
    direction_counts: Counter[str] = Counter()
    outcome_counts: Counter[str] = Counter()
    class_counts: Counter[str] = Counter()
    semantic_counts: Counter[str] = Counter()
    mapping_counts: Counter[str] = Counter()
    for entry in entries:
        class_counts[str(entry["source_class"])] += 1
        semantic_counts[str(entry["semantic_status"])] += 1
        mapping_counts[str(entry["mapping_mode"])] += 1
        direction_counts.update(entry["direction_ids"])
        outcome_counts.update(entry["result_ids"])
    invalid_directions = sorted({d for e in entries for d in e["direction_ids"] if d not in DIRECTION_IDS})
    invalid_outcomes = sorted({o for e in entries for o in e["result_ids"] if o not in OUTCOME_IDS})
    manifest: dict[str, object] = {
        "schema_version": "cross-source-reconciliation/v1",
        "as_of_date": as_of,
        "source_policy": "All historical sources are read-only; this register stores locators and candidate links, not copied raw payloads.",
        "semantic_policy": "Rule/owner mapping is an auditable navigation layer. It does not certify mathematical truth, model understanding, or sentence-level semantic equivalence.",
        "source_boundaries": {
            "webgpt_state_revision": web_data.get("revision"),
            "webgpt_record_count": len(web_data["records"]),
            "localgpt_live_head": "8470721a07f28f842895a67f5fd885ab12c1ee33",
            "webgpt_snapshot_head": "26fcecfbfecf6db66a70c1bf3e067159bce3eb6a",
            "localgpt_dirty": True,
        },
        "source_files": source_files,
        "counts": {
            "total_register_entries": len(entries),
            "webgpt_state_records": len(web_data["records"]),
            "ai_response_rows": class_counts["ai_response"],
            "local_tool_event_rows": class_counts["local_tool_event"],
            "local_work_product_rows": class_counts["local_work_product"],
            "understanding_claim_rows": class_counts["understanding_claim"],
            "entries_with_direction": sum(bool(e["direction_ids"]) for e in entries),
            "entries_with_result": sum(bool(e["result_ids"]) for e in entries),
            "entries_with_unmapped_reason": sum(bool(e["unmapped_reason"]) for e in entries),
            "invalid_direction_ids": len(invalid_directions),
            "invalid_result_ids": len(invalid_outcomes),
        },
        "direction_counts": dict(sorted(direction_counts.items())),
        "result_counts": dict(sorted(outcome_counts.items())),
        "mapping_mode_counts": dict(sorted(mapping_counts.items())),
        "semantic_status_counts": dict(sorted(semantic_counts.items())),
        "invalid_direction_ids": invalid_directions,
        "invalid_result_ids": invalid_outcomes,
        "entries": entries,
    }
    report_lines = [
        "# 跨来源方向—成果逐项 reconciliation 报告",
        "",
        f"截至：`{as_of}`；Schema：`cross-source-reconciliation/v1`。",
        "",
        "> 本报告由机器登记器生成。它证明每个纳入范围的来源行都有稳定 locator、候选方向/成果链接和显式语义状态；它不把规则匹配、文件存在、历史 AI 自述或 ledger PASS 当作数学证明或模型理解证明。",
        "",
        "## 1. 覆盖分母",
        "",
        "| 来源 | 行数 | 处理方式 |",
        "|---|---:|---|",
        f"| WebGPT STATE revision {web_data.get('revision')} | {len(web_data['records'])} | 全部 record 逐项登记；保留历史状态和 source path |",
        f"| AI response ledger（LocalGPT 305 + WebGPT 55 + Gemini 24） | {class_counts['ai_response']} | 逐行 locator + 内容/owner 路由 |",
        f"| LocalGPT tool event | {class_counts['local_tool_event']} | 逐行 event locator；不把工具调用当结果 |",
        f"| work product | {class_counts['local_work_product']} | 逐项 artifact/file/tree locator |",
        f"| understanding claim | {class_counts['understanding_claim']} | 逐句/逐行 claim locator；全部保留直接语义复核状态 |",
        f"| **合计** | **{len(entries)}** | **无静默丢弃** |",
        "",
        "## 2. 映射与语义边界",
        "",
        f"- `entries_with_direction={manifest['counts']['entries_with_direction']}`；`entries_with_result={manifest['counts']['entries_with_result']}`；`unmapped_reason={manifest['counts']['entries_with_unmapped_reason']}`。",
        f"- 方向 ID 越界：`{len(invalid_directions)}`；结果 ID 越界：`{len(invalid_outcomes)}`。",
        f"- `understanding_claim` 的 `{semantic_counts['PENDING_DIRECT_SENTENCE_ADJUDICATION']}` 行仍需直接句级语义裁决；这不是遗漏，而是显式未知。",
        "- `EXPLICIT_OR_OWNER_ROUTE` 只表示 record ID、owner 路径或结果名称有直接路由依据；`PROVENANCE_FALLBACK` 只表示安全地归入历史/治理覆盖方向，不代表主题已经判断完成。",
        "",
        "## 3. 当前来源边界",
        "",
        "- LocalGPT live 工作树仍 dirty；register 不写入或清理 `/Volumes/D/ALL-Markdown`。",
        "- WebGPT 使用顶层保存的 workspace snapshot 和其 revision 41 STATE；原 workspace 不被修改。",
        "- 所有条目 `mathematical_certification=NOT_PERFORMED_BY_THIS_REGISTER`；已有 R039/R036 等结果的实际证据等级仍以 `全景视野.md` 与原 result owner 为准。",
        "- 方向/结果链接是当前投影的交叉入口；详细 raw payload、tool result、artifact、Git diff 和句子必须沿 locator 回源。",
        "",
        "## 4. 运行收据",
        "",
        "- 生成器：`scripts/audit/build_cross_source_reconciliation.py`",
        "- 验证器：`scripts/audit/verify_cross_source_reconciliation.py`",
        "- 预期验证：所有输入文件 hash、WebGPT 91 条 record、四类 LocalGPT/理解账本行数、ID 域和无理由孤儿均通过。",
        "",
    ]
    report = "\n".join(report_lines)
    return manifest, report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--as-of", default="2026-09-12")
    parser.add_argument("--output", type=Path, default=Path("audit/cross-source-reconciliation.json"))
    parser.add_argument("--report", type=Path, default=Path("audit/cross-source-reconciliation-report.md"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    manifest, report = build(root, args.as_of)
    output = root / args.output
    report_path = root / args.report
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")
    print(json.dumps({"status": "BUILT", "counts": manifest["counts"], "output": output.as_posix(), "report": report_path.as_posix()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
