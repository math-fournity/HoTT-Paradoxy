#!/usr/bin/env python3
"""Checkpoint P31's static modal/Löb source audit and route P32 discovery."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-RES-20260921-ASTRA-P31-TT-PROVABILITY-CORPUS"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P30 = "R-P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-20260921"
P31 = "R-P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-20260921"
DIR = "audit/p31-tt-provability-type-theory-corpus-20260921"
SOURCES = (
    f"{DIR}/P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-REPORT.md",
    f"{DIR}/P31-TT-PROVABILITY-SOURCE-FREEZE.json",
    f"{DIR}/run_p31_tt_provability.py",
    f"{DIR}/runs/20260921-P31-TT-PROVABILITY-SOURCE-01/RUN.json",
    f"{DIR}/verify_p31_tt_provability_type_theory_corpus.py",
    f"{DIR}/P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-VERIFICATION.json",
)


def h(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime():
    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def editor():
    sys.path.insert(0, str(ROOT / "scripts/audit"))
    import projection_edit
    return projection_edit


def core_audit(core: dict) -> str:
    rows = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(rows) == 46
    output = (
        f"# {SID} 核心认知回评\n\n{core['generation']}；46 条；兼容单文件审计登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
        "- core_change: NO\n- direction_change: P31 non-HoTT modal source closed; P32 HoTT-specific discovery next.\n"
        "- panorama_change: source-level modal/Löb/trust boundary recorded.\n- essay_change: NO\n"
        "- update_decision: distinguish modal syntax from verified provability/soundness and actual HoTT use.\n"
        "- cross_conflicts: no HoTT defect, trusted self-validation, or O6 task bridge established.\n"
        "- unresolved: P32 discovery and any future version-pinned actual HoTT reflection consumer.\n"
        "- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
        "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    )
    deepened = {"KC-000025", "KC-000026", "KC-000027", "KC-000028", "KC-000029", "KC-000035", "KC-000036", "KC-000041", "KC-000043", "KC-000044", "KC-000045", "KC-000046"}
    for kc, title in rows:
        relation = "DEEPENED" if kc in deepened else "NOT_TOUCHED"
        assessment = "P31区分modal/Löb语法、信任边界与HoTT实际消费者。" if relation == "DEEPENED" else "本单元未直接检验该用户原文。"
        output += f"| `{kc}` | {title} | `{relation}` | {assessment} | P31 report；P32实际source可推翻边界。 |\n"
    return output + "\n## 波次定位\n\nP31关闭非HoTT experimental modal source；P32只搜HoTT-specific actual reflection consumer，避免generic control重复。\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    r = runtime()
    e = editor()
    assert all((ROOT / path).is_file() for path in SOURCES)
    verification = json.loads((ROOT / SOURCES[-1]).read_text())
    assert verification["status"] == "PASS_WITH_SCOPE"
    state = json.loads((ROOT / r.STATE).read_text())
    assert state["revision"] == 247 and state["latest_session"] == "S-RES-20260921-ASTRA-P30-HOTT-REFLECTION-CROSSWALK"
    head = json.loads((ROOT / r.HEAD).read_text())
    assert all(h(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = r.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P31-CHECKPOINT-PLAN.json").write_bytes(r.dump(plan))

    state["revision"] = 248
    state["latest_session"] = SID
    plan_record = state["records"][PLAN]
    plan_record["related_records"] = list(dict.fromkeys(plan_record.get("related_records", []) + [P31, SID]))
    plan_record["status"] = "four_track_p3_paused_p1_expression_p4_not_triggered_p22_parked_p32_hott_specific_reflection_discovery_next"
    plan_record["evidence_status"] = (
        "P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / "
        "P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / P22_GUARDED_BRIDGE_PARKED / "
        "P31_NON_HOTT_MODAL_LOB_CONTROL / P32_HOTT_SPECIFIC_REFLECTION_DISCOVERY_NEXT / GOAL_ACTIVE"
    )
    plan_record["full_sources"] = list(dict.fromkeys(plan_record.get("full_sources", []) + list(SOURCES)))
    plan_record["source_hashes"].update({path: h(ROOT / path) for path in plan_record["full_sources"] if (ROOT / path).is_file()})
    plan_record["revalidation"] = plan_record.get("revalidation", "") + " Revision248 records P31 non-HoTT modal/Löb source audit and routes P32 HoTT-specific discovery; P30 scope unchanged."
    state["records"][P31] = {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "CLOSE_WITH_SCOPE / MODAL_BOX_QUOTATION_AND_LOB_SYNTAX_CONFIRMED / NOT_A_GODEL_STYLE_OBJECT_PROVABILITY_CHAIN / SOUNDNESS_NOT_ESTABLISHED_AND_TRUST_BOUNDARIES_EXPLICIT / NOT_HOTT_AND_NO_SAME_TASK_CONSUMER / P32_HOTT_SPECIFIC_DISCOVERY_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P30, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {path: h(ROOT / path) for path in SOURCES},
        "scope": "Fixed experimental Agda modal source audit; no Agda kernel replay, HoTT theorem, defect, or same-task result.",
    }
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "P31_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope", "depends_on": [],
        "related_records": [PLAN, P30, P31],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_P22_PARKED_P32_HOTT_SPECIFIC_REFLECTION_DISCOVERY_NEXT",
        "current_phase": "PHASE_2_P31_NON_HOTT_MODAL_CONTROL_P32_HOTT_SPECIFIC_REFLECTION_DISCOVERY_NEXT",
        "second_phase_status": "P3_PAUSED_P1_POSITIVE_CONTROL_P4_NOT_TRIGGERED_GUARD_PARKED_P32_NEXT",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P32-HOTT-SPECIFIC-REFLECTION-CONSUMER-DISCOVERY-2026-001. First conduct local/historical reconnaissance, then run a bounded public primary-source search. Select only a version-pinned source that has both an actual HoTT/Cubical/univalence/HIT identity and an actual object provability, quotation/evaluation, or modal/Löb consumer. For each candidate freeze O1–O6 and exclude host-only reflection, generic modal syntax, and title-only matches. If none qualifies, report the declared denominator and generate a new axis rather than infer global absence.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_GUARD_PARKED / P31_NON_HOTT_MODAL_LOB_CONTROL / NEXT_P32_HOTT_SPECIFIC_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = e.load(ROOT, "MEMORY.md")
    direction = e.load(ROOT, "方向追踪.md")
    panorama = e.load(ROOT, "全景视野.md")
    essay = e.load(ROOT, "扩展认知.md")
    e.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md",
        "P30 已完成：P24–P29按六项反射义务交叉，现有固定HoTT相关资产没有完整强链；P31固定 `tt-provability@69de798` 源码审计其实际层级。P3/P1/P4/Guard继续停放。入口：`audit/p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md`；revision247。",
        "P31 已审 `tt-provability@69de798`：有modal box/quotation/Löb syntax，但非HoTT、无可信object-provability/soundness/O6链，且Agda toolchain不可用。下一=P32：仅寻找同时具HoTT feature与实际reflection consumer的版本固定来源。P3/P1/P4/Guard继续停放。入口：`audit/p31-tt-provability-type-theory-corpus-20260921/P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-REPORT.md`；revision248。")
    e.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260921-ASTRA-P31-TT-PROVABILITY-CORPUS：非HoTT modal/Löb source的syntax/trust boundary已审；P32 HoTT-specific reflection discovery next；revision248。\n")

    e.replace_in_index(direction, "source_state_revision: 247", "source_state_revision: 248")
    e.replace_in_index(direction, "projection_generation: 20260921-direction-247", "projection_generation: 20260921-direction-248")
    e.replace_in_index(direction, "semantic_status: FOUR_TRACK_P30_SIX_OBLIGATION_CROSSWALK_P31_TT_PROVABILITY_NEXT", "semantic_status: FOUR_TRACK_P31_NON_HOTT_MODAL_LOB_P32_HOTT_DISCOVERY_NEXT")
    e.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P30：P24–P29六义务交叉表 | P29/P30 | `P31_TT_PROVABILITY_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | 强链未在固定HoTT相关资产建立；审计新Agda source | P30 report；revision247 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P31：非HoTT modal/Löb源码审计 | P30/P31 | `P32_HOTT_SPECIFIC_DISCOVERY_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | modal语法存在但非可信HoTT链；转向严格来源发现 | P31 report；revision248 |")
    e.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P30 | `P3_PAUSED / P31_TT_PROVABILITY_AUDIT` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P30 reports；revision247 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P31 | `P3_PAUSED / P32_HOTT_DISCOVERY` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P31 reports；revision248 |")

    e.replace_in_index(panorama, "source_state_revision: 247", "source_state_revision: 248")
    e.replace_in_index(panorama, "projection_generation: 20260921-outcome-247", "projection_generation: 20260921-outcome-248")
    e.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P30_SIX_OBLIGATION_CROSSWALK_P31_TT_PROVABILITY_NEXT", "semantic_status: FOUR_TRACK_P31_NON_HOTT_MODAL_LOB_P32_HOTT_DISCOVERY_NEXT")
    e.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-HOTT-FOUR-TRACK-PLAN` | P30 P24–P29六义务交叉表 | `DIR-U-HOTT-FOUR-TRACK` | P24–P30 | `P30_SCOPED / P31_NEXT` | 固定HoTT相关资产无完整强链；新source待审 | 不证明HoTT缺陷 | P30 report；revision247 |",
        "| `OUT-HOTT-FOUR-TRACK-PLAN` | P31 非HoTT modal/Löb source审计 | `DIR-U-HOTT-FOUR-TRACK` | P30/P31 | `P31_SCOPED / P32_NEXT` | modal syntax/trust boundary不等于HoTT self-validation | 不证明HoTT缺陷 | P31 report；revision248 |")
    e.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P30已交叉 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30 | `P3_PAUSED / P31_TT_PROVABILITY_AUDIT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P30 reports；revision247 |",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P31已审modal source | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31 | `P3_PAUSED / P32_HOTT_DISCOVERY` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P31 reports；revision248 |")
    e.append_to_shard(panorama, "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md", "\n## P31：非HoTT modal/Löb源码审计（revision248）\n\n固定Agda source有box/quotation/Löb syntax，但全称TODO、公理、关闭检查和语义洞使soundness未建立，且无HoTT/O6。P32转向严格HoTT来源发现。\n")
    e.append_to_shard(panorama, "全景视野/008 - 当前未完成.md", "\n14. `P32-HOTT-SPECIFIC-REFLECTION-CONSUMER-DISCOVERY-2026-001`：只搜同时有HoTT/Cubical/univalence/HIT身份和实际reflection/provability/quotation consumer的版本固定来源。\n")

    simple = {path: (ROOT / path).read_text() for path in r.MUTABLE if path not in {r.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[r.PREFIX + "FRONTIER.md"] = simple[r.PREFIX + "FRONTIER.md"].replace(
        "- P30完成P24–P29六义务交叉表：固定HoTT相关资产没有完整强反射链；新P31候选是Agda `tt-provability@69de798`，须从源码判其理论层级。入口：`audit/p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md`。",
        "- P31确认`tt-provability@69de798`有modal/Löb syntax，但source的TODO/postulate/关闭检查/semantic hole使其不是可信HoTT self-validation；P32只搜HoTT-specific实际consumer。入口：`audit/p31-tt-provability-type-theory-corpus-20260921/P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-REPORT.md`。", 1)
    simple[r.PREFIX + "RESUME.md"] = simple[r.PREFIX + "RESUME.md"].replace(
        "当前 active goal 在P30后继续：P24–P29六义务表显示固定HoTT相关资产无完整强反射链；P31固定 `tt-provability@69de7983019f2f044a40624b81662d862aca3dff` 的Agda源码，先判实际理论层级再讨论HoTT关系。不要重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md`；revision247。",
        "当前 active goal 在P31后继续：`tt-provability@69de798`提供modal/Löb syntax但非HoTT，且其可信soundness未由可运行内核建立。P32按双维条件寻找版本固定HoTT-specific reflection consumer；不要重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p31-tt-provability-type-theory-corpus-20260921/P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-REPORT.md`；revision248。", 1)

    rows = []
    for document in (memory, direction, panorama, essay):
        rows += e.payload_rows(document, ROOT)
    present = {row["path"] for row in rows}
    for path in r.MUTABLE:
        if path not in present:
            rows.append({"path": path, "expected_sha256": h(ROOT / path), "text": r.dump(state).decode() if path == r.STATE else simple[path]})
    session = (
        f"# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n"
        "- status: `P31_CHECKPOINTED_WITH_SCOPE / P32_HOTT_SPECIFIC_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`\n"
        f"- load_receipt: research plan snapshot `{plan['snapshot']}`; P31 source freeze/run and O1–O6 report reviewed.\n"
        "- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"
    )
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID,
            "primary_runs": [{"kind": "P31 fixed source audit", "result": "SOURCE_AUDIT_COMPLETED_WITH_SCOPE / KERNEL_REPLAY_NOT_RUN_TOOLCHAIN_UNAVAILABLE", "receipt": SOURCES[3]}, {"kind": "P31 source verifier", "result": "PASS_WITH_SCOPE"}],
            "new_math_claims": [], "new_kernel_replay": False}
    rows += [{"path": BASE + "SESSION.md", "expected_sha256": None, "text": session}, {"path": BASE + "RUNS.json", "expected_sha256": None, "text": r.dump(runs).decode()}, {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": core_audit(state["current_core"])}]
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN], "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。", "files": rows}
    (OUT / "P31-CHECKPOINT-PAYLOAD.json").write_bytes(r.dump(payload))
    result = r.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P31-CHECKPOINT-APPLY.json" if args.apply else "P31-CHECKPOINT-DRY-RUN.json")).write_bytes(r.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
