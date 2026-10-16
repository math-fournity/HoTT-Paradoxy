#!/usr/bin/env python3
"""Prepare revision 131: re-pin the corrected programmatic completeness test."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260914-131-PROGRAMMATIC-TEST-REPIN"
PREV = "S-GOV-20260914-130-COMPUTABILITY-CONTINUITY-LITERATURE-AUDIT"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
STATUS = "CORE_GENERATION_4_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s131", RUNTIME_PATH)
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


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只重绑测试 hash 与验证状态，不改变 S130 的研究判断。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "ALIGNED" if kid in {"KC-000007", "KC-000021"} else "NOT_TOUCHED"
        assessment = (
            "专项测试现在检查六分片、import 字节/hash、R2 边界和文献漏项；只有通过后才恢复记录。"
            if relation == "ALIGNED"
            else f"本轮没有重新裁决“{label}”的内容；沿用 S130 公开回评。"
        )
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{TEST}`；{kid} | S130 的开放义务不变。 |")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只将 index 的 state revision 前移。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只将 index 的 state revision 前移。",
        "- essay_change: NO。",
        "- update_decision: re-pin corrected 5/5 programmatic test hash。",
        "- cross_conflicts: S130 source hash 与修正后的测试文件不同；本事务显式解决。",
        "- unresolved: 与 S130 相同；R2、exact HoTT、现实桥梁和文献覆盖仍开放。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 130 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_130_S130")
    if SESSION_ID in state["records"]:
        raise SystemExit("SESSION_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    projection_edit.replace_in_index(direction, "source_state_revision: 130", "source_state_revision: 131")
    projection_edit.replace_in_index(direction, "projection_generation: 20260914-direction-112", "projection_generation: 20260914-direction-113")
    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.replace_in_index(panorama, "source_state_revision: 130", "source_state_revision: 131")
    projection_edit.replace_in_index(panorama, "projection_generation: 20260914-outcome-112", "projection_generation: 20260914-outcome-113")
    memory = projection_edit.load(ROOT, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S131 程序化完备性测试重绑定：S130 后新增的 import/hash/R2/文献漏项断言初次因期望文字不匹配失败，修正为验证实际规范句并把测试名从 five-shards 改为 six-shards；最终 5/5 PASS。STATE 对该测试的 source hash 显式更新；S130 研究判断、单工作面、R0–R5 和下一队列不变。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    state["revision"] = 131
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_PROGRAMMATIC_TEST_REPIN"
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-113"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-113"
    record = state["records"][PLAN_ID]
    record["source_hashes"][TEST] = R.sha((ROOT / TEST).read_bytes())
    record["revalidation"] = f"{SESSION_ID}: corrected import/literature assertions and six-shard test pass 5/5; source hash re-pinned without changing the plan semantics."

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS131：程序化完备性专项测试已修正并 5/5 PASS，STATE source hash 重绑定；S130 单工作面、可计算性/文献覆盖判断与下一队列不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目的：修复 S130 后新增专项测试的文字期望与方法名，并重绑 STATE source hash。
- 首次结果：4 项旧测试通过，新 import/literature 断言因期望不存在的概括句而失败。
- 修复：断言实际规范句“文献分母没有闭合”；方法名改为 six-shards。
- 最终结果：5/5 PASS；无研究语义、数学 claim、工作面或优先级变化。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "initial_test": "4 PASS / 1 FAIL_EXPECTATION_TEXT",
        "final_test": "5/5 PASS",
        "source_hash_repin": TEST,
        "new_math_claims": [],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "MECHANICALLY_VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, TEST],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, PLAN_ID],
        "scope": "Correct and re-pin the programmatic completeness test after S130; no semantic or mathematical change.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Correct and verify the main-project continuity artifacts authorized by the user's single-work-surface instruction.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 131, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
