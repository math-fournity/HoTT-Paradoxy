#!/usr/bin/env python3
"""Prepare revision 145: re-pin the R2 semantic regression test."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SCRIPTS = ROOT / "scripts/audit"
SESSION_ID = "S-GOV-20260914-145-R2-REGRESSION-SEMANTICS"
PREV = "S-RES-20260914-144-R2-SYNTHETIC-DUAL-KERNEL"
STATUS = "CORE_GENERATION_4_R2_SYNTHETIC_DUAL_KERNEL_COMPLETE_INTERNAL_UNDEC_R3_R4_NEXT"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
CROSS_ID = "A-R2-CROSS-KERNEL-CORRESPONDENCE-001"
TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
PREPARE = "scripts/audit/prepare_s145_r2_regression_semantics_checkpoint.py"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s145", RUNTIME_PATH)
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


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000012": "旧 regression literal 把 R2 目标写成已成立的内部无条件 no-decider；本轮改为 synthetic reduction 与内部否定分层。",
        "KC-000013": "测试现在固定当前量词层级，不再用历史目标句覆盖已经澄清的时序状态。",
        "KC-000021": "专项测试 5/5 PASS；变更只校准 oracle，不新增或修改 C-208–C-218 数学命题。",
        "KC-000024": "计算路线保持 R2 synthetic complete / internal negation open，防止未来测试要求恢复过强结论。",
        "KC-000036": "Gödel/不可判定前提继续显式；回归测试不会把 implication 冒充否定。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只修正 R2 语义 regression oracle。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "CORRECTED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{TEST}`；{kid} | Goal 的内部 no-decider、R3/R4、CE-MAP、natural consumer 与现实桥梁仍开放。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO。",
        "- direction_change: NO_CONTENT_CHANGE — 只 bump projection identity 到 revision 145。",
        "- panorama_change: NO_CONTENT_CHANGE — 只 bump projection identity 到 revision 145。",
        "- essay_change: NO。",
        "- update_decision: 旧 literal 被测试失败发现；更新 test owner 与 STATE pin，不恢复已否定的过强措辞。",
        "- cross_conflicts: regression test 必须固定 current semantic contract，不能固定 historical wording。",
        "- unresolved: 与 S144 相同；无新数学状态。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (ROOT / TEST).is_file() or not (ROOT / PREPARE).is_file():
        raise SystemExit("S145_INPUT_MISSING")
    check = __import__("subprocess").run(
        ["python3", "-B", TEST], cwd=ROOT, capture_output=True, text=True, check=False
    )
    if check.returncode != 0 or "Ran 5 tests" not in check.stderr + check.stdout or "OK" not in check.stderr + check.stdout:
        raise SystemExit("S145_PROGRAMMATIC_TEST_NOT_PASSING")
    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 144 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_144_S144")
    if SESSION_ID in state["records"]:
        raise SystemExit("S145_SESSION_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    projection_edit.replace_in_index(direction, "source_state_revision: 144", "source_state_revision: 145")
    projection_edit.replace_in_index(direction, "projection_generation: 20260914-direction-126", "projection_generation: 20260914-direction-127")
    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.replace_in_index(panorama, "source_state_revision: 144", "source_state_revision: 145")
    projection_edit.replace_in_index(panorama, "projection_generation: 20260914-outcome-126", "projection_generation: 20260914-outcome-127")
    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory["index_text"] = replace_once(memory["index_text"], "S023–S144 逐会话记录", "S023–S145 逐会话记录")
    projection_edit.append_to_shard(
        memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S145 corrective：S144 后专项 test 仍要求历史 literal“R2 不存在全域总停机判定器”，与当前已证范围冲突并 FAIL。测试改为要求 `R2 synthetic dual-kernel complete`、精确 implication 定义与 C-214–C-218，5/5 PASS。数学源码、claim、run、判词不变；只重绑 test hash 和 projection revision。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)
    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += "\n100. Regression oracle 不能把历史目标句当永久真值。当前证据把 R2 分成 synthetic implication 已证与内部 `¬decidable` 未证后，旧测试仍要求“R2 不存在总判定器”，其失败是有价值的语义告警。修法是让测试同时断言 scoped 状态、精确定义和最新 claim IDs，而不是把文档改回过强措辞。\n"
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS145 corrective：程序化专项测试已从历史 R2 no-decider literal 改为验证当前 synthetic implication/内部否定分层、C-214–C-218，5/5 PASS。S144 数学状态不变；下一步仍为内部前提、G-HOTT-SYNTAX/R3、Post/HoTT 文献三向薄切。\n\n",
    )

    state["revision"] = 145
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R2_REGRESSION_SEMANTICS_CORRECTIVE"
    state["execution_control"]["status"] = STATUS
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-127"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-127"
    plan_record = state["records"][PLAN_ID]
    plan_record["source_hashes"][TEST] = R.sha((ROOT / TEST).read_bytes())
    add_once(plan_record.setdefault("related_records", []), SESSION_ID)
    plan_record["revalidation"] = f"{SESSION_ID}: regression now asserts the current synthetic-undecidability definition boundary and C-214-C-218; 5/5 pass. No mathematical status changed."
    for identity in (GOAL_ID, CROSS_ID):
        add_once(state["records"][identity].setdefault("related_records", []), SESSION_ID)
    state["records"][GOAL_ID]["revalidation"] = f"{SESSION_ID}: S144 objective and open gates unchanged; the programmatic regression oracle now preserves the synthetic/internal distinction."
    state["records"][CROSS_ID]["revalidation"] = f"{SESSION_ID}: correspondence proof/receipt unchanged; only the higher-level regression literal was corrected and re-pinned."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 类型：S144 后的语义 regression corrective。
- 触发：专项 test 仍固定旧的无条件 R2 no-decider 目标句，和当前 scoped 结论冲突。
- 修正：断言 R2 synthetic dual-kernel 状态、精确定义 `decidable P→enumerable(complement SBTM_HALT)` 与 C-214–C-218。
- 验证：`test_hott_programmatic_exploration_completeness.py` 5/5 PASS。
- 数学：C-208–C-218 源码、run、索引与判词均未改变。
- 下一步：继续 `goal.md` 三向薄切。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "regression": {"path": TEST, "tests": 5, "status": "PASS", "semantic_change": "HISTORICAL_UNCONDITIONAL_LITERAL_TO_CURRENT_SYNTHETIC_BOUNDARY"},
        "new_math_claims": [], "next": ["R2-INTERNAL-UNDEC-001", "G-HOTT-SYNTAX-001", "POST-AND-LIT-HOTT-COMPUTABILITY"],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, TEST, PREPARE],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, GOAL_ID, PLAN_ID, CROSS_ID],
        "scope": "Correct and re-pin the R2 semantic regression oracle after S144; no mathematical change.",
        "source_hashes": {}, "status": "complete",
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
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "Maintain the active goal.md governance continuity by correcting a stale regression oracle without changing mathematical claims.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value} for path, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 145, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
