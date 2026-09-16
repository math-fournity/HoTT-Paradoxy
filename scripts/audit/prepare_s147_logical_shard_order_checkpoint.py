#!/usr/bin/env python3
"""Prepare revision 147: enforce canonical logical-shard reading order."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260915-147-LOGICAL-SHARD-ORDER"
PREV = "S-RES-20260914-146-R2-R4-LIT-THREE-SLICE"
STATUS = "CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_COMPLETE_2LTT_FR_UIP_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
ORDER_ID = "A-LOGICAL-DOCUMENT-CANONICAL-ORDER-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
CAND_ID = "A-CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001"
RUNTIME = ".codex/tools/cognition_runtime.py"
RUNTIME_TEST = ".codex/skills/hott-paradox-research/checks/test_cognition_runtime.py"
PROTOCOL = ".codex/cognition/PROTOCOL.md"
PROJECT_AGENTS = "AGENTS.md"

SPEC = importlib.util.spec_from_file_location("runtime_s147", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)

import sys

SCRIPTS = ROOT / "scripts/audit"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000007": "加载器现把 source-guided 候选的局部分片恢复到 canonical logical-document 顺序，避免 AI 先看到结论片再补前提片。",
        "KC-000021": "本轮只提升认知输入顺序证据：runtime 3.6.1、39 项回归与实际 Goal task plan；不提升任何数学主张。",
        "KC-000027": "HoTT-specific 候选仍按 LIT-HOTT 001→004 的前提、内部否定、Oracle 时序、2LTT 候选顺序进入上下文。",
        "KC-000036": "跨压缩恢复的机器顺序缺口已闭合；2LTT→UIP、完整 R4、对角不完备与现实桥梁仍开放。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮为认知水合顺序纠正，无新数学结论。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{RUNTIME}`；`{RUNTIME_TEST}`；{kid} | "
            "2LTT replacement→UIP、HoTT 必要性、自然 consumer、现实同任务桥梁与全面覆盖仍开放。 |"
        )
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 revision；下一候选不变。",
        "- panorama_change: YES_GOVERNANCE_EVIDENCE — 新增 logical-shard canonical-order 结果行。",
        "- essay_change: NO。",
        "- update_decision: runtime 修一般顺序不变量，避免只改当前 candidate path 掩盖同类复发。",
        "- cross_conflicts: 内容此前完整但 LIT-HOTT 在 Goal task plan 中显示 004→001→002→003；现恢复 index table 的 001→002→003→004。",
        "- unresolved: fresh receipt 需在 checkpoint 后以 revision 147 重建；模型理解与数学真值均不由该收据认证。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 146 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_146_S146")
    if ORDER_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("S147_RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    for old, new in (
        ("source_state_revision: 146", "source_state_revision: 147"),
        ("projection_generation: 20260914-direction-128", "projection_generation: 20260915-direction-129"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    row = (
        "| `OUT-TOP-LOGICAL-SHARD-CANONICAL-ORDER` | active/direct source 先选中末分片时，runtime 仍把逻辑文档恢复为 index table 顺序 | "
        "`DIR-G-CHECKPOINT-HYDRATION-INTEGRITY` | 当前项目加载治理 | `VERIFIED_WITH_SCOPE` | runtime 3.6.1 保留原 selection reasons 并重排；39/39 单测 PASS；Goal task 的 LIT-HOTT 顺序为 001→002→003→004 | "
        "不证明模型理解或任何数学命题；不改变 2LTT candidate 的证据等级 | `.codex/tools/cognition_runtime.py`；"
        "`.codex/skills/hott-paradox-research/checks/test_cognition_runtime.py`；S147 checkpoint |\n"
    )
    projection_edit.append_to_shard(panorama, "全景视野/002 - 治理、门禁与骨架结果.md", row)
    for old, new in (
        ("source_state_revision: 146", "source_state_revision: 147"),
        ("projection_generation: 20260914-outcome-128", "projection_generation: 20260915-outcome-129"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory["shards"]["MEMORY/001 - 当前执行队列.md"] = replace_once(
        memory["shards"]["MEMORY/001 - 当前执行队列.md"],
        "runtime 3.6.0 / LOAD_SET v4 / PROTOCOL v2.6",
        "runtime 3.6.1 / LOAD_SET v4 / PROTOCOL v2.6",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S147 logical-shard order corrective：活动候选先选中 LIT-HOTT 第 004 片时，旧 runtime 会在随后展开 index 后保留 004→001→002→003。runtime 3.6.1 现按 canonical table 恢复 001→002→003→004，同时保留 selection reasons；回归增至 39/39 PASS。研究状态与下一 2LTT→UIP 候选不变。\n",
    )

    essay = projection_edit.load(ROOT, R.ESSAY)
    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "# HoTT 研究前沿（S146 R2/R4/LIT 三向薄切完成）",
        "# HoTT 研究前沿（S147 认知分片顺序纠正，研究候选不变）",
    )
    frontier = replace_once(
        frontier,
        "ambient R2、完整 R4、CE-MAP、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
        "ambient R2、完整 R4、CE-MAP、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。S147 只修复 LIT-HOTT 逻辑分片在 task hydration 中的 canonical 顺序，不改变这些研究判词。",
    )

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n105. 分片全文‘都在 plan 中’还不等于读取顺序正确：active record 可能先把末片加入 selection，随后 index 展开若只去重会留下 004→001→002→003。加载器识别 canonical index 后必须把已有分片移回 table 顺序，同时保留原 selection reasons；回归要覆盖‘分片先于索引’而不只覆盖‘索引直接展开’。\n"
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS147 corrective：runtime 3.6.1 已把先行活动分片恢复到 canonical index table 顺序；39/39 单测与 Goal task 实例均通过，LIT-HOTT 现为 001→002→003→004。研究判词不变，下一步仍机器化并消融 `A-CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001`。\n\n",
    )

    state["revision"] = 147
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_LOGICAL_SHARD_CANONICAL_ORDER"
    state["execution_control"]["status"] = STATUS
    state["projection"]["status"] = STATUS
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260915-direction-129"
    direction_record["scope"] = "Current main-only portfolio through C-226: R2 conditional internal no-decider and the exact groupoid-syntax slice are replayed; 2LTT internal fibrant replacement -> UIP is the next source-reported candidate."
    outcome_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    outcome_record["projection_generation"] = "20260915-outcome-129"
    outcome_record["scope"] = "Integrated outcomes through C-226 plus runtime 3.6.1 canonical logical-shard ordering; no ambient no-decider or qualified HoTT reality-relative paradox."

    sources = [RUNTIME, RUNTIME_TEST, PROJECT_AGENTS, PROTOCOL]
    state["records"][ORDER_ID] = {
        "classification": "LOGICAL_DOCUMENT_CANONICAL_TABLE_ORDER",
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / 39_TESTS_AND_LIVE_TASK_PLAN",
        "full_sources": sources,
        "kind": "governance_runtime_repair",
        "lifecycle_status": "CLOSED",
        "path": RUNTIME,
        "related_records": ["A-LOAD-GOVERNANCE-V3-001", GOAL_ID, CAND_ID, SESSION_ID],
        "resolution": {
            "evidence": [RUNTIME, RUNTIME_TEST, RESULT_REL],
            "reason": "A shard selected before its index is repositioned into canonical table order without losing prior selection reasons; regression and the live Goal plan pass.",
        },
        "scope": "Input ordering and plan metadata only; model ingestion, comprehension and mathematics are not certified.",
        "source_hashes": {path: R.sha((ROOT / path).read_bytes()) for path in sources},
        "status": "closed",
    }
    load_record = state["records"]["A-LOAD-GOVERNANCE-V3-001"]
    add_once(load_record.setdefault("full_sources", []), RUNTIME_TEST)
    load_record["revalidation"] = (
        "S-GOV-20260915-147-LOGICAL-SHARD-ORDER upgrades the current runtime to 3.6.1: canonical index table order now overrides earlier direct shard selection while preserving selection provenance; 39 regression tests pass."
    )
    goal_record = state["records"][GOAL_ID]
    for identity in (ORDER_ID, SESSION_ID):
        add_once(goal_record.setdefault("related_records", []), identity)
    goal_record["revalidation"] = (
        "S147 corrected cross-session hydration order without changing the research frontier; 2LTT internal fibrant replacement -> UIP remains the next active candidate."
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 类型：S146 后的认知水合顺序 corrective。
- 触发：活动候选先选中 `LIT-HOTT-COMPUTABILITY-001` 第 004 片，Goal task plan 随后展开 index 时输出 004→001→002→003。
- 修正：runtime 3.6.1 在识别 canonical index 后按 table 顺序重排已有分片，并保留原 selection reasons。
- 验证：runtime 单测 39/39 PASS；实际 Goal task plan 输出 001→002→003→004，`review_required=[]`、`query_first_promoted=[]`。
- 边界：只证明输入计划的机械顺序；模型理解与数学不由本轮认证。
- 研究：2LTT internal fibrant replacement→UIP 仍是下一 active candidate；Goal 保持 active。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "new_math_claims": [],
        "runtime": {"version": "3.6.1", "tests": 39, "status": "PASS"},
        "live_task_plan": {
            "task": GOAL_ID,
            "logical_document": "LIT-HOTT-COMPUTABILITY-001",
            "shards": ["001", "002", "003", "004"],
            "review_required": [],
            "query_first_promoted": [],
        },
        "post_checkpoint_required": ["regenerate fresh-three-way receipt at revision 147", "rerun projection freshness"],
        "next": [CAND_ID],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, *sources],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, ORDER_ID, GOAL_ID, CAND_ID],
        "scope": "Correct logical-document reading order and preserve the unchanged 2LTT research frontier.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[lessons_path] = lessons
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs

    changed = [PROJECT_AGENTS, PROTOCOL, RUNTIME, RUNTIME_TEST, *texts.keys()]
    for record in state["records"].values():
        hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(hashes, dict):
            continue
        rebound = []
        for path in changed:
            if path not in hashes or path == R.STATE:
                continue
            data = texts[path].encode("utf-8") if path in texts else (ROOT / path).read_bytes()
            current_hash = R.sha(data)
            if hashes[path] != current_hash:
                hashes[path] = current_hash
                rebound.append(path)
        if rebound and record is not state["records"][ORDER_ID]:
            note = f"{SESSION_ID}: revalidated after canonical logical-shard order governance update at {', '.join(rebound)}; mathematical scopes are unchanged."
            previous = record.get("revalidation")
            record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note

    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": path,
                "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None,
                "text": value,
            }
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 147, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
