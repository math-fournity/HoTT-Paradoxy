#!/usr/bin/env python3
"""Checkpoint the P26 intrinsic QIIRT audit and route P27 discovery."""
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
SID = "S-RES-20260921-ASTRA-P26-TTASQIIRT-CORPUS"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P25 = "R-P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-20260921"
P26 = "R-P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-20260921"
DIR = "audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921"
SOURCES = (
    f"{DIR}/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md",
    f"{DIR}/P26-TTASQIIRT-SOURCE-FREEZE.json",
    f"{DIR}/run_p26_ttasqiirt_index.py",
    f"{DIR}/runs/20260921-P26-TTASQIIRT-INDEX-01/RUN.json",
    f"{DIR}/verify_p26_ttasqiirt_intrinsic_type_theory_corpus.py",
    f"{DIR}/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-VERIFICATION.json",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime_module():
    spec = importlib.util.spec_from_file_location("cognition_runtime", ROOT / ".codex/tools/cognition_runtime.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def edit_module():
    sys.path.insert(0, str(ROOT / "scripts/audit"))
    import projection_edit  # noqa: PLC0415
    return projection_edit


def audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.MULTILINE)
    assert len(headings) == 46
    touched = {"KC-000025", "KC-000026", "KC-000027", "KC-000028", "KC-000029", "KC-000035", "KC-000036", "KC-000041", "KC-000043", "KC-000044", "KC-000045", "KC-000046"}
    text = f"# {SID} 核心认知回评\n\n{core['generation']}；46 条。兼容单文件审计继续登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    text += "- core_change: NO\n- direction_change: P26 intrinsic syntax scoped; P27 reflection-consumer discovery next.\n- panorama_change: default entrypoint acceptance, safe rejection, UIP/termination boundaries and missing strong reflection recorded.\n- essay_change: NO\n- update_decision: close fixed TTasQIIRT denominator and pursue a different external consumer-discovery cell.\n- cross_conflicts: no actual K, same-layer global self-validation or HoTT defect established.\n- unresolved: P27 source discovery plus theory/reality bridges remain open.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    text += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in headings:
        if kc in touched:
            text += f"| `{kc}` | {title} | `DEEPENED` | P26显示内在syntax可以存在，但未形成对象可证明性/全局自证。 | P26 report；P27的新actual consumer可改变。 |\n"
        else:
            text += f"| `{kc}` | {title} | `NOT_TOUCHED` | P26未直接检验本条用户原文。 | 新source/用户原文才会触及。 |\n"
    return text + "\n## 波次定位\n\nP26为自反方向提供native intrinsic syntax正控制，也用安全选项/明确未完成模块避免夸大。P27把搜索转向真正的对象proof-predicate/reflection consumer。\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    runtime = runtime_module()
    edit = edit_module()
    assert all((ROOT / source).is_file() for source in SOURCES)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 242 and state["latest_session"] == "S-GOV-20260921-ASTRA-P25-PROJECTION-LINK-REPAIR"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha256(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P26-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    state["revision"] = 243
    state["latest_session"] = SID
    portfolio = state["records"][PLAN]
    portfolio["related_records"] = list(dict.fromkeys(portfolio.get("related_records", []) + [P26, SID]))
    portfolio["status"] = "four_track_p3_paused_p1_expression_p4_not_triggered_p22_parked_p27_reflection_consumer_discovery_next"
    portfolio["evidence_status"] = "P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / P22_GUARDED_BRIDGE_PARKED / P26_INTRINSIC_SYNTAX_SCOPED / P27_REFLECTION_CONSUMER_DISCOVERY_NEXT / GOAL_ACTIVE"
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(SOURCES)))
    portfolio["source_hashes"].update({source: sha256(ROOT / source) for source in portfolio["full_sources"] if (ROOT / source).is_file()})
    portfolio["revalidation"] = portfolio.get("revalidation", "") + " Revision243 records P26 TTasQIIRT intrinsic syntax audit and selects P27 reflection-consumer discovery; P25 source scope unchanged."
    state["records"][P26] = {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "CLOSE_WITH_SCOPE / NATIVE_INTRINSIC_SYNTAX_AND_METATHEORY_ENTRYPOINT_ACCEPTED_WITH_SCOPE / INTRINSIC_SYNTAX_NOT_GLOBAL_SELF_VALIDATION / EXPLICIT_UIP_AND_TERMINATION_TRUST_BOUNDARIES / P27_REFLECTION_CONSUMER_DISCOVERY_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P25, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {source: sha256(ROOT / source) for source in SOURCES},
        "scope": "Fixed external source and entrypoint run; no HoTT theorem, same-layer global self-validation or defect claim.",
    }
    state["records"][SID] = {"kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL", "evidence_status": "P26_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope", "depends_on": [], "related_records": [PLAN, P25, P26], "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")]}
    state["execution_control"].update({
        "status": "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_P22_PARKED_P27_REFLECTION_CONSUMER_DISCOVERY_NEXT",
        "current_phase": "PHASE_2_P26_INTRINSIC_SYNTAX_SCOPED_P27_REFLECTION_CONSUMER_DISCOVERY_NEXT",
        "second_phase_status": "P3_PAUSED_P1_POSITIVE_CONTROL_P4_NOT_TRIGGERED_GUARD_PARKED_P27_NEXT",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P27-REFLECTION-CONSUMER-DISCOVERY-2026-001. Perform fresh public/community and local/historical reconnaissance outside P24 Coquand BRA, P25 HoTTLean, P26 TTasQIIRT and closed P3 consumers. Select one version-pinned actual object proof-predicate/quotation/reflection/self-soundness consumer or a new bounded source-coverage denominator; freeze Input/Operation/Observation/Done and do not turn host reflection into object reflection.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_GUARD_PARKED / P26_INTRINSIC_SYNTAX_SCOPED / NEXT_P27_REFLECTION_CONSUMER_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = edit.load(ROOT, "MEMORY.md")
    directions = edit.load(ROOT, "方向追踪.md")
    panorama = edit.load(ROOT, "全景视野.md")
    essay = edit.load(ROOT, "扩展认知.md")
    old_queue = "P25 已确认 HoTTLean 是实际 syntax/checker/model consumer，但以 Lean host—MLTT object 分层，不构成同层全局自身真理验证。下一=P26：固定 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 审计 native QIIT/QIIRT intrinsic syntax、NbE、模型及 proof-predicate/reflection 调用链；P3/P1/P4/Guard 继续停放。入口：`audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md`；revision242（方向—成果链接修复，不改P26）。"
    new_queue = "P26 已确认 TTasQIIRT 的 native QIIRT intrinsic syntax和主入口可检查，但对象proof-predicate/global self-validation未建立；入口还带 UIP、TERMINATING和安全配置边界。下一=P27：在未审公开/本地来源中寻找实际 object proof-predicate/quotation/reflection/self-soundness consumer；P3/P1/P4/Guard继续停放。入口：`audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md`；revision243。"
    edit.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md", old_queue, new_queue)
    edit.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260921-ASTRA-P26-TTASQIIRT-CORPUS：TTasQIIRT@8db0830 的 default index接受、safe拒绝与UIP/TERMINATING边界记录；P27反射消费者发现下一；revision243。\n")

    edit.replace_in_index(directions, "source_state_revision: 242", "source_state_revision: 243")
    edit.replace_in_index(directions, "projection_generation: 20260921-direction-242", "projection_generation: 20260921-direction-243")
    edit.replace_in_index(directions, "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT_LINKS_REPAIRED", "semantic_status: FOUR_TRACK_P26_INTRINSIC_SYNTAX_SCOPED_P27_REFLECTION_CONSUMER_DISCOVERY_NEXT")
    edit.replace_in_shard(directions, "方向追踪/002 - 治理与用户方向.md", "| `DIR-U-HOTT-FOUR-TRACK` | P25：HoTTLean真实 syntax/checker/model 审计 | P24/P25 | `P26_INTRINSIC_QIIRT_SOURCE_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | P25确认host/object分层，P26查native intrinsic syntax | P25 report；revision242 |", "| `DIR-U-HOTT-FOUR-TRACK` | P26：TTasQIIRT native intrinsic syntax审计 | P25/P26 | `P27_REFLECTION_CONSUMER_DISCOVERY_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | 内在syntax正控制，强self-validation仍缺 | P26 report；revision243 |")
    edit.replace_in_shard(directions, "方向追踪/002 - 治理与用户方向.md", "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P25 | `P3_PAUSED / INDEPENDENT_P26_RUNNING` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P25 reports；revision242 |", "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P26 | `P3_PAUSED / INDEPENDENT_P27_DISCOVERY` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P26 reports；revision243 |")

    edit.replace_in_index(panorama, "source_state_revision: 242", "source_state_revision: 243")
    edit.replace_in_index(panorama, "projection_generation: 20260921-outcome-242", "projection_generation: 20260921-outcome-243")
    edit.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT_LINKS_REPAIRED", "semantic_status: FOUR_TRACK_P26_INTRINSIC_SYNTAX_SCOPED_P27_REFLECTION_CONSUMER_DISCOVERY_NEXT")
    edit.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", "| `OUT-HOTT-FOUR-TRACK-PLAN` | P25 HoTTLean syntax/checker/model 审计 | `DIR-U-HOTT-FOUR-TRACK` | P24/P25 | `P25_SCOPED / P26_NEXT` | 实际consumer以Lean host分层；非同层自证 | 不证明HoTT缺陷 | P25 report；revision241 |", "| `OUT-HOTT-FOUR-TRACK-PLAN` | P26 TTasQIIRT native intrinsic syntax审计 | `DIR-U-HOTT-FOUR-TRACK` | P25/P26 | `P26_SCOPED / P27_NEXT` | 内在syntax/NbE不等于object provability/global self-validation | 不证明HoTT缺陷 | P26 report；revision243 |")
    edit.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P25 已完成 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25 | `P3_PAUSED / P26_INDEPENDENT_NEXT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P25 reports；revision241 |", "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P26 已完成 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26 | `P3_PAUSED / P27_DISCOVERY_NEXT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P26 reports；revision243 |")
    edit.append_to_shard(panorama, "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md", "\n## P26：TTasQIIRT intrinsic syntax审计（revision243）\n\n固定 TTasQIIRT@`8db0830`在默认Agda入口下接受 QIIRT syntax/model/NbE，但安全配置拒绝 `TERMINATING`，standard model显式假设UIP，advanced Canonicity/LogPred未导入。它是内在syntax正控制，不是对象可证明性/全局自身验证。P27转向异类反射消费者发现。\n")
    edit.append_to_shard(panorama, "全景视野/008 - 当前未完成.md", "\n9. `P27-REFLECTION-CONSUMER-DISCOVERY-2026-001`：排除 P24/P25/P26 与已审P3后，在2025–2026公开/本地来源中寻找版本固定的实际对象proof-predicate/quotation/reflection/self-soundness consumer。\n")

    simple = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in runtime.MUTABLE if rel not in {runtime.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[runtime.PREFIX + "FRONTIER.md"] = simple[runtime.PREFIX + "FRONTIER.md"].replace("- P25确认 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 是真实 syntax/checker/model consumer，但强保证显式在 Lean host；固定 commit 无对象 proof-predicate/reflection/global self-validation consumer。下一 P26 审计 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 的 native intrinsic QIIRT；不重审停放分支。入口：`audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md`。", "- P26确认 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 的native intrinsic syntax与默认入口接受；它没有object proof-predicate/global self-validation，且有UIP/TERMINATING/安全边界。下一P27在不同2025–2026来源中发现实际反射consumer；不重审停放分支。入口：`audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md`。", 1)
    simple[runtime.PREFIX + "RESUME.md"] = simple[runtime.PREFIX + "RESUME.md"].replace("当前 active goal 在P25后继续：HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 已确认为实际 syntax/checker/model consumer，却将 reflection/semantic soundness留在 Lean host，非同层全局自验证。P26 固定 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1`，审计 native QIIT/QIIRT 内在 type theory 及 object proof-predicate/reflection；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md`；revision242（投影链接修复，P26不变）。", "当前 active goal 在P26后继续：TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 的native QIIRT syntax和默认入口已核，但对象proof-predicate/global self-validation未建立，且UIP/TERMINATING/安全配置边界明示。P27对不同2025–2026来源做反射消费者发现；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md`；revision243。", 1)
    rows=[]
    for doc in (memory, directions, panorama, essay): rows.extend(edit.payload_rows(doc, ROOT))
    seen={row['path'] for row in rows}
    for rel in runtime.MUTABLE:
        if rel not in seen:
            rows.append({'path':rel,'expected_sha256':sha256(ROOT/rel),'text':runtime.dump(state).decode('utf-8') if rel==runtime.STATE else simple[rel]})
    session=f"""# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n- status: `P26_CHECKPOINTED_WITH_SCOPE / P27_REFLECTION_CONSUMER_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`\n- load_receipt: research plan snapshot `{plan['snapshot']}`; P26 fixed source, default/safe external run, and current projections reviewed.\n- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"""
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[{'kind':'TTasQIIRT fixed external index','result':'default exit 0 / safe exit 42','receipt':f'{DIR}/runs/20260921-P26-TTASQIIRT-INDEX-01/RUN.json'},{'kind':'P26 source verifier','result':'PASS_WITH_SCOPE'}],'new_math_claims':[],'new_kernel_replay':False,'scope':'External-source evidence only; no new HoTT theorem.'}
    rows += [{'path':BASE+'SESSION.md','expected_sha256':None,'text':session},{'path':BASE+'RUNS.json','expected_sha256':None,'text':runtime.dump(runs).decode('utf-8')},{'path':BASE+'CORE_COGNITION_AUDIT.md','expected_sha256':None,'text':audit(state['current_core'])}]
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[PLAN],'authorization':'用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。','files':rows}
    (OUT/'P26-CHECKPOINT-PAYLOAD.json').write_bytes(runtime.dump(payload))
    result=runtime.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('P26-CHECKPOINT-APPLY.json' if args.apply else 'P26-CHECKPOINT-DRY-RUN.json')).write_bytes(runtime.dump(result))
    print(json.dumps({key:value for key,value in result.items() if key!='paths'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
