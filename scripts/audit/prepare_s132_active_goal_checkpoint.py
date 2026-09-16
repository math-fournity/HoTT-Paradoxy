#!/usr/bin/env python3
"""Prepare revision 132: register the active machine-overview goal in main."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260914-132-ACTIVE-MACHINE-OVERVIEW-GOAL"
PREV = "S-GOV-20260914-131-PROGRAMMATIC-TEST-REPIN"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
AUDIT_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
GOAL = ".codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md"
STATUS = "CORE_GENERATION_4_ACTIVE_HOTT_MACHINE_OVERVIEW_GOAL"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s132", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": "新 goal 把找什么、怎么找、凭什么和最终完成条件写成同一执行合同。",
        "KC-000007": "goal 要求 AI 提案、机器 oracle、学术来源和独立 holdout 分离。",
        "KC-000010": "goal 明确现实相对见证才是完成门，一般不完备不替代。",
        "KC-000012": "ASK/计算合法性被落实到 R0–R4 与候选资格链。",
        "KC-000014": "方向 B 与方向 A 在 goal 中保持同等资格。",
        "KC-000017": "goal 强制从 main 的用户认知出发并以反解释抵抗训练惯性。",
        "KC-000021": "所有数学结论仍须 main proof/source/run/index。",
        "KC-000022": "A/B 两类、机器证明和现实 bridge 共同成为完成条件。",
        "KC-000024": "不可停机路线被分解为对象程序、统一不可判定、证明搜索和 Gödel 层级。",
        "KC-000025": "自指候选不得以小循环完成，必须闭合 universal/representability。",
        "KC-000026": "exact HoTT/2LTT 自身语法与元层被列为 R4 义务。",
        "KC-000027": "程序边界进入 HoTT 后仍须 HoTT 必要性消融。",
        "KC-000028": "自我验证回环必须由数学不完成证书和自然 consumer 支持。",
        "KC-000029": "理论经济与被省略资格通过八轴和 A/B 检查。",
        "KC-000035": "HoTT 表达本研究与 HoTT 导致目标现象被分开。",
        "KC-000036": "Gödel/Kleene/Lawvere/Löb 只在服务现实相对链时进入最终完成。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮登记用户要求的新 active goal，不新增数学 claim。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的内容。")
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{GOAL}`；{kid} | goal 目标仍待实际研究完成。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — goal 是执行要求，不是新的悖论/元数学原文单元。",
        "- direction_change: NO_SEMANTIC_CHANGE — index revision 前移，现有计算合法性方向承载 goal。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 尚无新研究结果。",
        "- essay_change: NO。",
        "- update_decision: exact goal objective 保存到 main 并成为 active stable record。",
        "- cross_conflicts: Host goal 与项目文件内容一致；文件存在不证明完成。",
        "- unresolved: goal 正文列出的 literature、R2/R3/R4、HoTT essentiality、natural consumer、reality bridge 与覆盖证书。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (ROOT / GOAL).is_file():
        raise SystemExit("GOAL_FILE_MISSING")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 131 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_131_S131")
    if GOAL_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("GOAL_OR_SESSION_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    projection_edit.replace_in_index(direction, "source_state_revision: 131", "source_state_revision: 132")
    projection_edit.replace_in_index(direction, "projection_generation: 20260914-direction-113", "projection_generation: 20260914-direction-114")
    projection_edit.replace_in_index(direction, "semantic_status: CORE_GENERATION_4_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY", f"semantic_status: {STATUS}")
    projection_edit.replace_in_index(direction, "状态：`CORE_GENERATION_4_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY`", f"状态：`{STATUS}`")
    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.replace_in_index(panorama, "source_state_revision: 131", "source_state_revision: 132")
    projection_edit.replace_in_index(panorama, "projection_generation: 20260914-outcome-113", "projection_generation: 20260914-outcome-114")
    projection_edit.replace_in_index(panorama, "semantic_status: CORE_GENERATION_4_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY", f"semantic_status: {STATUS}")
    projection_edit.replace_in_index(panorama, "状态：`CORE_GENERATION_4_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY`", f"状态：`{STATUS}`")

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue],
        "3. 项目级程序化探索规划",
        "3. 当前 Host goal 已激活并以 `.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md` 保存 exact objective；它要求至少一个候选贯通精确 HoTT 规则、机器证明的不完成/不相容、HoTT 必要性、自然 consumer、现实同任务对应和方向 A/B，且学术覆盖与 CandidateClass 覆盖证书闭合后才可完成。项目级程序化探索规划现为 v2 index + 6 shards；第 006 片记录 R1 contributor 证据、R2/R4 开放、41 条文献分母与 2024–2026 漏项。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S132 active goal：按用户要求创建 Host goal，并把同一 objective 保存为 `.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md`；STATE 新增 active record。goal 不允许以 R0/R1、一般 Turing/Gödel、计划、局部 no-go 或表示边界提前完成；最终必须有 HoTT 必要性、自然 consumer、现实同任务 A/B 见证、机器证据、学术覆盖和 CandidateClass 覆盖。无新数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "S130 改变工作面与研究准备状态，不新增数学 claim。",
        "S132 已登记当前 active goal；S130 改变工作面与研究准备状态。两者都不新增数学 claim。exact objective 见 `.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md`。",
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS132：当前 Host goal 已激活并在 main 保存 exact objective。完成门=合格的 HoTT 现实相对 A/B 见证 + 机器证明 + HoTT 必要性 + natural consumer + same-task reality bridge + 学术/搜索覆盖；当前从 `LIT-DENOMINATOR-001` 开始，R2 并行。\n\n",
    )

    state["revision"] = 132
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_ACTIVE_MACHINE_OVERVIEW_GOAL"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Execute LIT-DENOMINATOR-001 in main while preparing the R2 ProgramCode/fair-enumeration thin path; do not mark the goal complete before its full qualification gate."
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-114"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = STATUS
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-114"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = STATUS
    add_once(state["active"], GOAL_ID)
    state["records"][GOAL_ID] = {
        "classification": "ACTIVE_HOTT_NONREALITY_MACHINE_OVERVIEW_GOAL",
        "depends_on": [],
        "evidence_status": "USER_AUTHORIZED_ACTIVE_GOAL",
        "full_sources": [GOAL, ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md", "feature-list.md", "rulings.md"],
        "kind": "active_goal",
        "lifecycle_status": "ACTIVE_WORK",
        "path": GOAL,
        "related_records": [PLAN_ID, AUDIT_ID, SESSION_ID],
        "scope": "Continue until at least one exact HoTT, machine-proved, HoTT-essential, natural-consumer, same-reality-task A/B witness is found and the declared academic/search coverage gates are met; R0/R1 or generic Turing/Godel boundaries cannot complete the goal.",
        "source_hashes": {GOAL: R.sha((ROOT / GOAL).read_bytes()), "feature-list.md": R.sha((ROOT / "feature-list.md").read_bytes()), "rulings.md": R.sha((ROOT / "rulings.md").read_bytes())},
        "status": "active",
    }
    plan_record = state["records"][PLAN_ID]
    add_once(plan_record["full_sources"], GOAL)
    add_once(plan_record.setdefault("related_records", []), GOAL_ID)
    plan_record["source_hashes"][GOAL] = R.sha((ROOT / GOAL).read_bytes())
    continuity_record = state["records"]["A-MACHINE-OVERVIEW-SINGLE-WORK-SURFACE-DECISION-001"]
    continuity_record["source_hashes"]["feature-list.md"] = R.sha((ROOT / "feature-list.md").read_bytes())
    continuity_record["source_hashes"]["rulings.md"] = R.sha((ROOT / "rulings.md").read_bytes())
    continuity_record["revalidation"] = f"{SESSION_ID}: active goal registered in main; single-work-surface decision unchanged, and Feature/ruling hashes re-pinned."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户要求：根据旧 goal 与 revision 131 当前状态，给出并启用能持续驱动机器统观直到找到合格 HoTT 非现实性悖论的新 goal。
- Host：goal 已创建为 active，无显式 token budget。
- 项目：exact objective 保存到 `{GOAL}`，STATE 新增 `{GOAL_ID}` 并进入 active 集合。
- 完成边界：R0/R1、一般不可判定/不完备、计划与局部负结论均不能完成；必须贯通 HoTT 必要性、natural consumer、same-task reality A/B、机器证明和覆盖门。
- 数学：无新 claim；下一工作单元 `LIT-DENOMINATOR-001`，R2 thin path 交替推进。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "host_goal": {"thread_id": "01a09a72-aeb6-7a50-81d6-d24f43c5e912", "status": "active", "token_budget": None},
        "project_goal": GOAL, "record_id": GOAL_ID, "new_math_claims": []
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "DOCUMENTED / HOST_GOAL_CREATED",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, GOAL],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, GOAL_ID, PLAN_ID],
        "scope": "Create and persist the user-requested active goal; no mathematical claim.",
        "source_hashes": {}, "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "The user explicitly requested a new active goal that continues the machine overview until a qualified HoTT nonreality paradox is found.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 132, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
