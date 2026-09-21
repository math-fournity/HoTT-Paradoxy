#!/usr/bin/env python3
"""Checkpoint the P25 HoTTLean audit, remove stale duplicate projections, and route P26."""
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
SID = "S-RES-20260921-ASTRA-P25-HOTTLEAN-CORPUS"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P24 = "R-P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-20260921"
P25 = "R-P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-20260921"
DIR = "audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921"
SOURCES = (
    f"{DIR}/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md",
    f"{DIR}/P25-HOTTLEAN-SOURCE-FREEZE.json",
    f"{DIR}/verify_p25_hottlean_mltt_syntax_semantics_corpus.py",
    f"{DIR}/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-VERIFICATION.json",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_runtime():
    spec = importlib.util.spec_from_file_location("cognition_runtime", ROOT / ".codex/tools/cognition_runtime.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_edit():
    sys.path.insert(0, str(ROOT / "scripts/audit"))
    import projection_edit  # noqa: PLC0415
    return projection_edit


def headings() -> list[tuple[str, str]]:
    found = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.MULTILINE)
    assert len(found) == 46
    return found


def audit(core: dict) -> str:
    touched = {
        "KC-000025": ("DEEPENED", "实际 HoTTLean consumer 的 syntax/checker/model 链已审计；自指仍不由名称自动产生。", "P25 report §§3–5；P26 source may change the intrinsic-syntax assessment."),
        "KC-000026": ("DEEPENED", "当前 commit 没有同层 global self-verification；它将证明与模型留在 Lean host。", "P25 report §4；actual object proof predicate/reflection would falsify."),
        "KC-000027": ("TENSION", "P25 显示程序化 checker 可分层实现，但没有把其一般界限转写为 HoTT 自身失败。", "P25 report §§4、8；P26 exact source determines successor."),
        "KC-000028": ("DEEPENED", "host MetaM partial checker、object syntax 和 model soundness 被区分；没有运行环证据。", "P25 report §§3–4；specific nontermination trace is a falsifier."),
        "KC-000029": ("DEEPENED", "论文的有限 universe/可判定 checking 选择可定位，但 P25 不判为非现实。", "P25 report §4；a same-task reality bridge remains required."),
        "KC-000035": ("DEEPENED", "HoTTLean 表达部分 MLTT 与模型推理；这不等于完整表达用户全部研究理论。", "P25 report §§3–5；P26 intrinsic syntax is a separate test."),
        "KC-000036": ("DEEPENED", "当前工程是 host 元理论研究对象 syntax，不是对象层证明自身 Gödel性质。", "P25 report §4；object-level proof predicate/reflection would change the verdict."),
        "KC-000041": ("ALIGNED", "本轮用本地 checkout、commit hash、source hash和论文交叉，而不是仅用语言模型模式。", "P25 source freeze; source update can falsify."),
        "KC-000043": ("CORRECTED", "避免把 host quotation/`Expr.code` 误读为对象自指；精确层级区分克服惯性。", "P25 report §4；a true object quotation operator is a falsifier."),
        "KC-000044": ("DEEPENED", "P25 保留理论可解释现实的可能性，并明确未建立该工程的现实同任务桥。", "P25 report §8；P26 may provide another interpretation boundary."),
        "KC-000045": ("DEEPENED", "可解释性需要实际 input/operation/observation/done；syntax/model soundness不足以替代现实对齐。", "P25 report §§1、8；actual R_min consumer would change."),
        "KC-000046": ("DEEPENED", "以具体外部工程检验理论，而没有将语法或 checker 的存在当作最后答案。", "P25 report §5；P26 sets a distinct next action."),
    }
    text = f"# {SID} 核心认知回评\n\n{core['generation']}；46 条。兼容单文件格式仍登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    text += "- core_change: NO\n- direction_change: P25 HoTTLean consumer closed with explicit stratification; P26 intrinsic QIIRT source audit next.\n- panorama_change: actual syntax/checker/model consumer and host-object boundary recorded.\n- essay_change: NO\n- update_decision: close P25 fixed commit, repair duplicate current projection IDs, and advance to the different P26 intrinsic-syntax denominator.\n- cross_conflicts: no same-layer global self-verification consumer or HoTT defect established.\n- unresolved: P26 source, actual K, theory necessity, and reality-task bridge remain open.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    text += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in headings():
        relation, assessment, evidence = touched.get(kc, ("NOT_TOUCHED", "P25 未直接检验这一用户原文。", "P26 的不同内在化源或新用户原文才会触及。"))
        text += f"| `{kc}` | {title} | `{relation}` | {assessment} | {evidence} |\n"
    return text + "\n## 波次定位\n\nP25证实一个实际但分层的 syntax/checker/model consumer；它缩小了同层自验证猜想的适用范围。P26改用 native QIIT/QIIRT 内在化，因而具有新的可判别分母。\n"


def result_record() -> dict:
    return {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "CLOSE_WITH_SCOPE / ACTUAL_SYNTACTIC_MODEL_CONSUMER_CONFIRMED / NOT_A_SAME_LAYER_GLOBAL_SELF_VALIDATION_CONSUMER_WITHIN_FIXED_COMMIT / DEFENSE_BY_EXPLICIT_HOST_OBJECT_STRATIFICATION_AND_SCOPE / P26_INTRINSIC_QIIRT_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P24, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {source: sha256(ROOT / source) for source in SOURCES},
        "scope": "Fixed external HoTTLean source audit; no build replay, HoTT theorem, actual K, or defect claim.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    runtime = load_runtime()
    edit = load_edit()
    assert all((ROOT / source).is_file() for source in SOURCES)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 240 and state["latest_session"] == "S-RES-20260921-ASTRA-P24-ERCF3-QUALIFICATION"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha256(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P25-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    state["revision"] = 241
    state["latest_session"] = SID
    portfolio = state["records"][PLAN]
    portfolio["related_records"] = list(dict.fromkeys(portfolio.get("related_records", []) + [P25, SID]))
    portfolio["status"] = "four_track_p3_paused_p1_expression_p4_not_triggered_p22_parked_p26_intrinsic_qiirt_next"
    portfolio["evidence_status"] = (
        "P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / "
        "P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / P22_GUARDED_BRIDGE_PARKED / "
        "P25_STRATIFIED_SYNTACTIC_MODEL_CONSUMER / P26_INTRINSIC_QIIRT_CANDIDATE_NEXT / GOAL_ACTIVE"
    )
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(SOURCES)))
    portfolio["source_hashes"].update({source: sha256(ROOT / source) for source in portfolio["full_sources"] if (ROOT / source).is_file()})
    portfolio["revalidation"] = portfolio.get("revalidation", "") + " Revision241 records P25 HoTTLean fixed-source audit and selects P26 native QIIRT intrinsic-syntax corpus; prior P24 scope unchanged."
    state["records"][P25] = result_record()
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P25_CHECKPOINTED_WITH_SCOPE_AND_PROJECTION_DEDUPLICATED",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P24, P25],
        "full_sources": [BASE + item for item in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_P22_PARKED_P26_INTRINSIC_QIIRT_NEXT",
        "current_phase": "PHASE_2_P25_HOTTLEAN_STRATIFIED_P26_INTRINSIC_QIIRT_AUDIT_NEXT",
        "second_phase_status": "P3_PAUSED_P1_POSITIVE_CONTROL_P4_NOT_TRIGGERED_GUARD_PARKED_P26_NEXT",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": (
            "P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-001. At fixed TTasQIIRT master "
            "8db08306287333067b2749f95f8ad3ba7a0e14d1, inspect native QIIT/QIIRT intrinsic type-theory syntax, "
            "standard-model/NbE/strictification paths, and any object proof-predicate/reflection/global-self-validation consumer. "
            "Freeze Input/Operation/Observation/Done; distinguish intrinsic syntax from complete HoTT self-truth. "
            "Do not re-audit P25 or parked P3/P1/P4 branches."
        ),
    })
    state["projection"]["status"] = "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_GUARD_PARKED / P25_STRATIFIED_CONSUMER_SCOPED / NEXT_P26_INTRINSIC_QIIRT / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = edit.load(ROOT, "MEMORY.md")
    directions = edit.load(ROOT, "方向追踪.md")
    panorama = edit.load(ROOT, "全景视野.md")
    essay = edit.load(ROOT, "扩展认知.md")
    old_queue = "P23/P24 已完成 ERCF3 独立入口与对象层 bridge qualification：修复编码是正控制，但 `Prov`→对象可表述性→反射→对角不动点及自然自验证消费者仍未建立。下一=P25：固定 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 审计 Syntax/Typechecker/Model 的实际层级与调用链；不重审 P3/P1/P4/Guard 停放分支。入口：`audit/p24-ercf3-proof-predicate-qualification-20260921/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md`；revision240。"
    new_queue = "P25 已确认 HoTTLean 是实际 syntax/checker/model consumer，但以 Lean host—MLTT object 分层，不构成同层全局自身真理验证。下一=P26：固定 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 审计 native QIIT/QIIRT intrinsic syntax、NbE、模型及 proof-predicate/reflection 调用链；P3/P1/P4/Guard 继续停放。入口：`audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md`；revision241。"
    edit.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md", old_queue, new_queue)
    edit.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260921-ASTRA-P25-HOTTLEAN-CORPUS：HoTTLean@31133dd 是实际 syntax/checker/model consumer，但强保证留在 Lean host；P26 native QIIRT commit 8db0830 为下一分母。当前投影重复 ID 已原位去重；revision241。\n")

    edit.replace_in_index(directions, "source_state_revision: 240", "source_state_revision: 241")
    edit.replace_in_index(directions, "projection_generation: 20260921-direction-240", "projection_generation: 20260921-direction-241")
    edit.replace_in_index(directions, "semantic_status: FOUR_TRACK_P24_ERC3_BRIDGE_SCOPED_P25_HOTTLEAN_NEXT", "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT")
    old_dir = "| `DIR-U-HOTT-FOUR-TRACK` | P24：ERCF3对象层桥资格审计 | P23/P24独立入口 | `P25_HOTTLEAN_SOURCE_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | P19–P24 | P24局部缺口关闭，P25查真实层级/consumer | P24 report；revision240 |"
    new_dir = "| `DIR-U-HOTT-FOUR-TRACK` | P25：HoTTLean真实 syntax/checker/model 审计 | P24/P25 | `P26_INTRINSIC_QIIRT_SOURCE_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | P19–P25 | P25确认host/object分层，P26查native intrinsic syntax | P25 report；revision241 |"
    edit.replace_in_shard(directions, "方向追踪/002 - 治理与用户方向.md", old_dir, new_dir)
    abx_current_old = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX P21停放消费者扫描 | P21 | `P3_PAUSED / P23_NEXT` | `EVIDENCE_DISCIPLINE` | P15/P17 | 等待新实际K | P21 report；revision239 |"
    abx_current_new = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P25 | `P3_PAUSED / INDEPENDENT_P26_RUNNING` | `EVIDENCE_DISCIPLINE` | P15/P17/P25 | 仅新版本固定实际 K 或强 R 才重开 | P21/P25 reports；revision241 |"
    edit.replace_in_shard(directions, "方向追踪/002 - 治理与用户方向.md", abx_current_old, abx_current_new)
    for stale in (
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P3 实际消费者 `K_app` 分支 | 原圆环 A/B/X H/R/K 整备、P1共同任务、P2 SIP无桥 | `P1_P2_CLOSED / P3_DENOMINATOR_SELECTION_PENDING / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P1/P2；C250–324、D1/D2/D3 | 先排除已有资产，冻结一个新消费者分母；不重做no-hit | `ABX行动.md`；总体方案；revision221 receipt |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P3 实际消费者 `K_app` 分支 | 原圆环 A/B/X H/R/K 整备与P1共同任务资格化 | `P1_ACCEPTED / P3_PENDING_P2 / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P1；C250–324、D1/D2/D3 | P2结束前不扩展K扫描；既有no-hit不重做 | `ABX行动.md`；总体方案；revision220 receipt |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P3 实际消费者 `K_app` 分支 | 原圆环 A/B/X H/R/K 整备 | `P3_PENDING_P1_AND_P2 / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；C250–324、D1/D2/D3 | P1/P2前不扩展K扫描；既有no-hit不重做 | `ABX行动.md`；总体方案；revision219 receipt |",
    ):
        edit.replace_in_shard(directions, "方向追踪/002 - 治理与用户方向.md", stale, "")

    edit.replace_in_index(panorama, "source_state_revision: 240", "source_state_revision: 241")
    edit.replace_in_index(panorama, "projection_generation: 20260921-outcome-240", "projection_generation: 20260921-outcome-241")
    edit.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P24_ERC3_BRIDGE_SCOPED_P25_HOTTLEAN_NEXT", "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT")
    old_out = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P24 ERCF3对象层桥资格审计 | `DIR-U-HOTT-FOUR-TRACK` | P23/P24 | `P24_SCOPED / P25_NEXT` | 语法编码不等于对象可证明性/反射/consumer | 不证明HoTT缺陷 | P24 report；revision240 |"
    new_out = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P25 HoTTLean syntax/checker/model 审计 | `DIR-U-HOTT-FOUR-TRACK` | P24/P25 | `P25_SCOPED / P26_NEXT` | 实际consumer以Lean host分层；非同层自证 | 不证明HoTT缺陷 | P25 report；revision241 |"
    edit.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", old_out, new_out)
    out_current_old = "| `OUT-ABX-ACTION-INTAKE` | ABX P21综合停放 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22 | `P3_PAUSED / P23_NEXT` | 避免重复 | 不证明原M/N桥 | P21 report；revision239 |"
    out_current_new = "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P25 已完成 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25 | `P3_PAUSED / P26_INDEPENDENT_NEXT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P25 reports；revision241 |"
    edit.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", out_current_old, out_current_new)
    for stale in (
        "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者分支 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、D1/D2/D3、Book/社区来源、P1/P2 | `P1_P2_CLOSED / P3_DENOMINATOR_SELECTION_PENDING / NO_ACTUAL_K` | H/R/U与操作合同已有控制；SIP无规则桥 | 不证明新拓扑、外部全库无K或HoTT缺陷 | `ABX行动.md`；总体方案；revision221 receipt |",
        "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者分支 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、D1/D2/D3、Book/社区来源及P1合同 | `P1_ACCEPTED / P3_PENDING_P2 / NO_ACTUAL_K` | H/R/U与操作合同已有控制；P1固定共同Done；有界K分母无命中 | 不证明新拓扑、外部全库无K或HoTT缺陷 | `ABX行动.md`；总体方案；revision220 receipt |",
        "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者分支 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、D1/D2/D3、Book/社区来源 | `P3_PENDING_P1_P2 / NO_ACTUAL_K` | H/R/U与操作合同已有控制；有界K分母无命中 | 不证明新拓扑、外部全库无K或HoTT缺陷 | `ABX行动.md`；总体方案；revision219 receipt |",
    ):
        edit.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", stale, "")
    edit.append_to_shard(panorama, "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md", "\n## P25：HoTTLean 分层 consumer 审计（revision241）\n\n固定 HoTTLean@`31133dd` 确有 `Expr`/`Wf*`、host MetaM checker 与 model soundness；对象 `code/el` 是类型宇宙编码，not syntax quotation，且未在固定 literal 分母发现对象 provability/reflection consumer。判词 `ACTUAL_SYNTACTIC_MODEL_CONSUMER_CONFIRMED / DEFENSE_BY_EXPLICIT_HOST_OBJECT_STRATIFICATION_AND_SCOPE`；P26转向 native QIIRT。\n")
    edit.append_to_shard(panorama, "全景视野/008 - 当前未完成.md", "\n8. `P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-001`：固定 TTasQIIRT 的 native QIIT/QIIRT intrinsic syntax、standard model、NbE、strictification 与对象 proof-predicate/reflection/global-self-validation 资格审计。\n")

    simple = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in runtime.MUTABLE if rel not in {runtime.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[runtime.PREFIX + "FRONTIER.md"] = simple[runtime.PREFIX + "FRONTIER.md"].replace(
        "- P24已关闭 ERCF3 本地对象层 bridge 分母：编码正控制存在，但 `Prov` 表示性、反射、对角不动点和自然同层自验证 consumer 均未建立。下一 P25 审计 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 的 Syntax/Typechecker/Model 层级；不重审停放分支。入口：`audit/p24-ercf3-proof-predicate-qualification-20260921/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md`。",
        "- P25确认 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 是真实 syntax/checker/model consumer，但强保证显式在 Lean host；固定 commit 无对象 proof-predicate/reflection/global self-validation consumer。下一 P26 审计 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 的 native intrinsic QIIRT；不重审停放分支。入口：`audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md`。",
        1,
    )
    simple[runtime.PREFIX + "RESUME.md"] = simple[runtime.PREFIX + "RESUME.md"].replace(
        "当前 active goal 在P24后继续：P23/P24 已把 ERCF3 的对象语法、可证明性表示、反射、对角与 natural consumer 分开资格化；固定源码未闭合对象层 bridge。P25 审计 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 的 Syntax/Typechecker/Model 实际层级与调用链；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p24-ercf3-proof-predicate-qualification-20260921/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md`；revision240。",
        "当前 active goal 在P25后继续：HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 已确认为实际 syntax/checker/model consumer，却将 reflection/semantic soundness留在 Lean host，非同层全局自验证。P26 固定 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1`，审计 native QIIT/QIIRT 内在 type theory 及 object proof-predicate/reflection；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md`；revision241。",
        1,
    )

    rows: list[dict] = []
    for doc in (memory, directions, panorama, essay):
        rows.extend(edit.payload_rows(doc, ROOT))
    seen = {row["path"] for row in rows}
    for rel in runtime.MUTABLE:
        if rel not in seen:
            text = runtime.dump(state).decode("utf-8") if rel == runtime.STATE else simple[rel]
            rows.append({"path": rel, "expected_sha256": sha256(ROOT / rel), "text": text})

    session = f"""# {SID}

- host: codex-desktop
- model: runtime-model-not-certified-by-tool
- tier: T3
- status: `P25_CHECKPOINTED_WITH_SCOPE / P26_INTRINSIC_QIIRT_SOURCE_AUDIT_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`
- load_receipt: research plan snapshot `{plan['snapshot']}`; current four-piece closure, P25 fixed checkout, P25 report and projection identity scan reviewed.
- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。

## element_usage

| 元件 | 实际使用 | 未使用会拦住什么 | 未使用且无影响 |
|---|---|---|---|
| Goal 3 §2.1 | 是：论文、repo commit和Zenodo/QIIRT successor核验 | 会遗漏新社区成果 | — |
| Goal 3 §2.2 | 是：本地/历史/`/Volumes/D`侦察、external checkout | 会重复或误称新分母 | — |
| current projection owner | 是：发现并原位去除四重 stale IDs | current truth继续冲突 | — |
| F-011 | 是：没有数学结论或新 kernel proof | 会把source审计夸大为定理 | — |
| P3/P4 audit trail | 未触发：本单元不是前提实质判定 | 若执行P3/P4才需要 | 无影响于P25 |
| Sub Agent | 未使用：项目禁令 | 禁令保护单写者 | — |
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {"kind": "P25 fixed-source verifier", "command": "python3 -B audit/p25-hottlean-mltt-syntax-semantics-corpus-20260921/verify_p25_hottlean_mltt_syntax_semantics_corpus.py", "result": "PASS_WITH_SCOPE"},
            {"kind": "current projection identity scan", "command": "parse direction/panorama shard tables for duplicate IDs", "result": "four stale ABX rows in each current projection removed"},
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "scope": "P25 is a source-level consumer audit and current-projection correction, not an external build or mathematical proof.",
    }
    rows.extend([
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": runtime.dump(runs).decode("utf-8")},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": audit(state["current_core"])},
    ])
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN], "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。", "files": rows}
    (OUT / "P25-CHECKPOINT-PAYLOAD.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P25-CHECKPOINT-APPLY.json" if args.apply else "P25-CHECKPOINT-DRY-RUN.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
