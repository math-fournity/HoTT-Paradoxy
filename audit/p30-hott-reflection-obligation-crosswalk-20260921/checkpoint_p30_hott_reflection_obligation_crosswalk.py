#!/usr/bin/env python3
"""Checkpoint P30's fixed-source reflection crosswalk and route P31."""
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
SID = "S-RES-20260921-ASTRA-P30-HOTT-REFLECTION-CROSSWALK"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P29 = "R-P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-20260921"
P30 = "R-P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-20260921"
DIR = "audit/p30-hott-reflection-obligation-crosswalk-20260921"
SOURCES = (
    f"{DIR}/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md",
    f"{DIR}/P30-HOTT-REFLECTION-CROSSWALK-SOURCE-FREEZE.json",
    f"{DIR}/verify_p30_hott_reflection_obligation_crosswalk.py",
    f"{DIR}/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-VERIFICATION.json",
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
    result = (
        f"# {SID} 核心认知回评\n\n"
        f"{core['generation']}；46 条；兼容单文件审计登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
        "- core_change: NO\n"
        "- direction_change: P30 fixed crosswalk completed; P31 independent Agda source audit next.\n"
        "- panorama_change: six obligations and P31 candidate boundary recorded.\n"
        "- essay_change: NO\n"
        "- update_decision: do not convert syntax/staging/host reflection into self-validation; inspect P31 source.\n"
        "- cross_conflicts: no HoTT defect, same-layer global self-validation, or O6 task bridge established.\n"
        "- unresolved: P31 fixed-source audit and a future actual HoTT/reality-task consumer.\n"
        "- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
        "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    )
    deepened = {"KC-000025", "KC-000026", "KC-000027", "KC-000028", "KC-000029", "KC-000035", "KC-000036", "KC-000041", "KC-000043", "KC-000044", "KC-000045", "KC-000046"}
    for kc, title in rows:
        relation = "DEEPENED" if kc in deepened else "NOT_TOUCHED"
        assessment = "P30将反射资格拆为六项，不把已知层级边界误称为HoTT结论。" if relation == "DEEPENED" else "本单元未直接检验该用户原文。"
        result += f"| `{kc}` | {title} | `{relation}` | {assessment} | P30 report；P31源码可推翻部分矩阵。 |\n"
    return result + "\n## 波次定位\n\nP30完成已审资产的资格交叉表；P31以不同Agda provability source检验O1–O6，避免对旧分母重复扫描。\n"


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
    assert state["revision"] == 246 and state["latest_session"] == "S-RES-20260921-ASTRA-P29-CLIMBER-CORPUS"
    head = json.loads((ROOT / r.HEAD).read_text())
    assert all(h(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = r.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P30-CHECKPOINT-PLAN.json").write_bytes(r.dump(plan))

    state["revision"] = 247
    state["latest_session"] = SID
    plan_record = state["records"][PLAN]
    plan_record["related_records"] = list(dict.fromkeys(plan_record.get("related_records", []) + [P30, SID]))
    plan_record["status"] = "four_track_p3_paused_p1_expression_p4_not_triggered_p22_parked_p31_tt_provability_audit_next"
    plan_record["evidence_status"] = (
        "P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / "
        "P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / P22_GUARDED_BRIDGE_PARKED / "
        "P30_SIX_OBLIGATION_CROSSWALK / P31_TT_PROVABILITY_SOURCE_AUDIT_NEXT / GOAL_ACTIVE"
    )
    plan_record["full_sources"] = list(dict.fromkeys(plan_record.get("full_sources", []) + list(SOURCES)))
    plan_record["source_hashes"].update({path: h(ROOT / path) for path in plan_record["full_sources"] if (ROOT / path).is_file()})
    plan_record["revalidation"] = plan_record.get("revalidation", "") + " Revision247 records P30 six-obligation crosswalk and selects P31 tt-provability source audit; P29 scope unchanged."
    state["records"][P30] = {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "CLOSE_WITH_SCOPE / SIX_OBLIGATION_CROSSWALK_COMPLETED / NO_FIXED_HOTT_RELATED_ASSET_ESTABLISHES_THE_FULL_STRONG_REFLECTION_CHAIN / P31_TT_PROVABILITY_SOURCE_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P29, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {path: h(ROOT / path) for path in SOURCES},
        "scope": "Fixed P24-P29 source crosswalk plus public candidate selection; no HoTT theorem, defect, or global absence conclusion.",
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P30_CHECKPOINTED_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P29, P30],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_P22_PARKED_P31_TT_PROVABILITY_AUDIT_NEXT",
        "current_phase": "PHASE_2_P30_SIX_OBLIGATION_CROSSWALK_P31_TT_PROVABILITY_AUDIT_NEXT",
        "second_phase_status": "P3_PAUSED_P1_POSITIVE_CONTROL_P4_NOT_TRIGGERED_GUARD_PARKED_P31_NEXT",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-001. At fixed GallagherCommaJack/tt-provability master 69de7983019f2f044a40624b81662d862aca3dff, clone into a temporary read-only directory and freeze source/toolchain. Inspect exact syntax, any object provability or modal operator, derivability/checker, reflection or Löb consumer, soundness owner, level/rung behavior, actual use, and relation to HoTT/ABX. Do not infer HoTT relevance from the repository title or Agda language.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_GUARD_PARKED / P30_SIX_OBLIGATION_CROSSWALK / NEXT_P31_TT_PROVABILITY_AUDIT / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = e.load(ROOT, "MEMORY.md")
    direction = e.load(ROOT, "方向追踪.md")
    panorama = e.load(ROOT, "全景视野.md")
    essay = e.load(ROOT, "扩展认知.md")
    e.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md",
        "P29 已编译核对 Climber：object `prov`、RFN(T₀)与Con(T₀)一阶阶梯成立，但每一级soundness/interpretation属于Lean元语言，且非HoTT。下一=P30：以P29六义务逐项对照现有HoTT资产并选择下一专属来源；P3/P1/P4/Guard继续停放。入口：`audit/p29-climber-object-provability-soundness-corpus-20260921/P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-REPORT.md`；revision246。",
        "P30 已完成：P24–P29按六项反射义务交叉，现有固定HoTT相关资产没有完整强链；P31固定 `tt-provability@69de798` 源码审计其实际层级。P3/P1/P4/Guard继续停放。入口：`audit/p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md`；revision247。")
    e.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260921-ASTRA-P30-HOTT-REFLECTION-CROSSWALK：P24–P29六义务表完成，P31 `tt-provability@69de798`固定source audit next；revision247。\n")

    e.replace_in_index(direction, "source_state_revision: 246", "source_state_revision: 247")
    e.replace_in_index(direction, "projection_generation: 20260921-direction-246", "projection_generation: 20260921-direction-247")
    e.replace_in_index(direction, "semantic_status: FOUR_TRACK_P29_GENERIC_REFLECTION_CONTROL_P30_HOTT_CROSSWALK_NEXT", "semantic_status: FOUR_TRACK_P30_SIX_OBLIGATION_CROSSWALK_P31_TT_PROVABILITY_NEXT")
    e.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P29：Climber object prov/RFN审计 | P28/P29 | `P30_HOTT_REFLECTION_CROSSWALK_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | generic reflection正确分层，需HoTT对照 | P29 report；revision246 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P30：P24–P29六义务交叉表 | P29/P30 | `P31_TT_PROVABILITY_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | 强链未在固定HoTT相关资产建立；审计新Agda source | P30 report；revision247 |")
    e.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P29 | `P3_PAUSED / P30_HOTT_CROSSWALK` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P29 reports；revision246 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P30 | `P3_PAUSED / P31_TT_PROVABILITY_AUDIT` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P30 reports；revision247 |")

    e.replace_in_index(panorama, "source_state_revision: 246", "source_state_revision: 247")
    e.replace_in_index(panorama, "projection_generation: 20260921-outcome-246", "projection_generation: 20260921-outcome-247")
    e.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P29_GENERIC_REFLECTION_CONTROL_P30_HOTT_CROSSWALK_NEXT", "semantic_status: FOUR_TRACK_P30_SIX_OBLIGATION_CROSSWALK_P31_TT_PROVABILITY_NEXT")
    e.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-HOTT-FOUR-TRACK-PLAN` | P29 Climber object prov/RFN审计 | `DIR-U-HOTT-FOUR-TRACK` | P28/P29 | `P29_SCOPED / P30_NEXT` | generic prov/rung依赖元语言soundness | 不证明HoTT缺陷 | P29 report；revision246 |",
        "| `OUT-HOTT-FOUR-TRACK-PLAN` | P30 P24–P29六义务交叉表 | `DIR-U-HOTT-FOUR-TRACK` | P24–P30 | `P30_SCOPED / P31_NEXT` | 固定HoTT相关资产无完整强链；新source待审 | 不证明HoTT缺陷 | P30 report；revision247 |")
    e.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P29已审Climber | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29 | `P3_PAUSED / P30_CROSSWALK_NEXT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P29 reports；revision246 |",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P30已交叉 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30 | `P3_PAUSED / P31_TT_PROVABILITY_AUDIT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P30 reports；revision247 |")
    e.append_to_shard(panorama, "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md", "\n## P30：反射义务交叉表（revision247）\n\nP24–P29按对象prov、派生、consumer、soundness、rung、同任务六义务核对；固定HoTT相关资产未给完整强链。P31审计新的Agda provability source。\n")
    e.append_to_shard(panorama, "全景视野/008 - 当前未完成.md", "\n13. `P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-001`：固定 `tt-provability@69de798`，审计其对象可证明性、reflection/Löb、soundness、层级与HoTT/现实任务关系。\n")

    simple = {path: (ROOT / path).read_text() for path in r.MUTABLE if path not in {r.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[r.PREFIX + "FRONTIER.md"] = simple[r.PREFIX + "FRONTIER.md"].replace(
        "- P29确认Climber@`6994d29dda860c3a82de207b1f39ea89526f61c9`具有object prov/RFN/Con一阶梯，但解释和soundness在Lean元语言，非HoTT/非同层全局自验证。下一P30做HoTT义务交叉表。入口：`audit/p29-climber-object-provability-soundness-corpus-20260921/P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-REPORT.md`。",
        "- P30完成P24–P29六义务交叉表：固定HoTT相关资产没有完整强反射链；新P31候选是Agda `tt-provability@69de798`，须从源码判其理论层级。入口：`audit/p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md`。", 1)
    simple[r.PREFIX + "RESUME.md"] = simple[r.PREFIX + "RESUME.md"].replace(
        "当前 active goal 在P29后继续：Climber@`6994d29dda860c3a82de207b1f39ea89526f61c9` 的object prov/RFN/Con一阶梯已build/smoke核对，但soundness/interpretation在Lean元语言，非HoTT实例。P30逐项交叉到现有HoTT assets；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p29-climber-object-provability-soundness-corpus-20260921/P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-REPORT.md`；revision246。",
        "当前 active goal 在P30后继续：P24–P29六义务表显示固定HoTT相关资产无完整强反射链；P31固定 `tt-provability@69de7983019f2f044a40624b81662d862aca3dff` 的Agda源码，先判实际理论层级再讨论HoTT关系。不要重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md`；revision247。", 1)

    rows = []
    for document in (memory, direction, panorama, essay):
        rows += e.payload_rows(document, ROOT)
    present = {row["path"] for row in rows}
    for path in r.MUTABLE:
        if path not in present:
            rows.append({"path": path, "expected_sha256": h(ROOT / path), "text": r.dump(state).decode() if path == r.STATE else simple[path]})
    session = (
        f"# {SID}\n\n"
        "- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n"
        "- status: `P30_CHECKPOINTED_WITH_SCOPE / P31_TT_PROVABILITY_AUDIT_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`\n"
        f"- load_receipt: research plan snapshot `{plan['snapshot']}`; P24–P29 reports, local reconnaissance and bounded public search reviewed.\n"
        "- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"
    )
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [{"kind": "P30 source crosswalk verifier", "result": "PASS_WITH_SCOPE", "receipt": SOURCES[-1]}],
        "new_math_claims": [],
        "new_kernel_replay": False,
    }
    rows += [
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": r.dump(runs).decode()},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": core_audit(state["current_core"])},
    ]
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SID,
        "load_profile": "research",
        "task_ids": [PLAN],
        "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。",
        "files": rows,
    }
    (OUT / "P30-CHECKPOINT-PAYLOAD.json").write_bytes(r.dump(payload))
    result = r.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P30-CHECKPOINT-APPLY.json" if args.apply else "P30-CHECKPOINT-DRY-RUN.json")).write_bytes(r.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
