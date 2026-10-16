#!/usr/bin/env python3
"""Checkpoint P36's source refinement finding and route to P37 weak-domain fidelity."""
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
SID = "S-RES-20260922-ASTRA-P36-PROVENANCE-ORIGIN-COVERAGE"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P35 = "R-P35-FIBERWISE-TRACE-COVERAGE-20260922"
P36 = "R-P36-PROVENANCE-ORIGIN-COVERAGE-20260922"
DIR = "audit/p36-provenance-origin-coverage-20260922"
SOURCES = (
    f"{DIR}/P36-PROVENANCE-ORIGIN-COVERAGE-REPORT.md",
    f"{DIR}/P36-PROVENANCE-ORIGIN-SOURCE-FREEZE.json",
    f"{DIR}/verify_p36_provenance_origin_coverage.py",
    f"{DIR}/P36-PROVENANCE-ORIGIN-COVERAGE-VERIFICATION.json",
    "HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda",
    "HoTT/formal/agda-unimath/hott-z/PunctureApartness.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeStereographic.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeOpenInterval.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda",
    "HoTT/verification/runs/20260920-MP-ASTRA-PUNCTURE-APARTNESS-001-01/RUN.json",
    "HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-STEREOGRAPHIC-001-01/RUN.json",
    "HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-INTERVAL-001-01/RUN.json",
    "HoTT/CLAIM_EVIDENCE_MATRIX.md",
    "goal-3-工作路径树/001 - 原初目标与当前工作树.md",
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
    deepened = {"KC-000003", "KC-000004", "KC-000005", "KC-000010", "KC-000015", "KC-000019", "KC-000020", "KC-000021", "KC-000022", "KC-000037", "KC-000038", "KC-000039", "KC-000040", "KC-000041", "KC-000042", "KC-000043", "KC-000044", "KC-000045", "KC-000046"}
    out = f"# {SID} 核心认知回评\n\n{core['generation']}；46 条；兼容单文件审计登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    out += "- core_change: NO\n- direction_change: P36 distinguishes the original weak puncture from the strong source actually used by mRich; P37 requalifies task fidelity.\n- panorama_change: no new theorem; C-283–C-290 are reused at their recorded scope.\n- essay_change: NO\n- update_decision: do not call StrongPuncture a silent representation of all ordinary punctures or a physical provenance event.\n- cross_conflicts: no HoTT defect, K, engine discrepancy, event-impossibility theorem, or reality bridge established.\n- unresolved: P37 weak/strong task correspondence and all independent P2/P3/P4 gates.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    out += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in rows:
        relation = "DEEPENED" if kc in deepened else "NOT_TOUCHED"
        if relation == "DEEPENED":
            judgement = "P36从实际圆、固定点、弱去点和强域细化出发修正原M的形式规格，不将该修正升级为理论缺陷。"
            evidence = "P36 report/verification；P37若显示原M本就选择强域则需降回正控制。"
        else:
            judgement = "本单元未直接检验该用户原文；它继续约束P37或其它根分支。"
            evidence = "P36 report；新的用户规格或source evidence可改变判断。"
        out += f"| `{kc}` | {title} | `{relation}` | {judgement} | {evidence} |\n"
    out += "\n## 波次定位\n\n- 最终目标连接：P1/R_min 的来源与输入忠实性。\n- 实际价值：发现现有mRich是strong refinement而不是把弱普通去点直接当输入，防止规格替换漂移。\n- 裁决：`CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION`。\n"
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rt = runtime()
    ed = editor()
    assert all((ROOT / rel).is_file() for rel in SOURCES)
    verification = json.loads((ROOT / SOURCES[3]).read_text())
    assert verification["status"] == "PASS_WITH_SCOPE"
    state = json.loads((ROOT / rt.STATE).read_text())
    assert state["revision"] == 253
    assert state["latest_session"] == "S-RES-20260922-ASTRA-P35-FIBERWISE-TRACE-COVERAGE"
    head = json.loads((ROOT / rt.HEAD).read_text())
    assert all(h(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = rt.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P36-CHECKPOINT-PLAN.json").write_bytes(rt.dump(plan))

    state["revision"] = 254
    state["latest_session"] = SID
    p = state["records"][PLAN]
    p["related_records"] = list(dict.fromkeys(p.get("related_records", []) + [P36, SID]))
    p["status"] = "p1_static_puncture_strong_refinement_p37_weak_fidelity_next"
    p["evidence_status"] = "P1_PRESENTATION_FIBER_FORMAL_CHECKED_WITH_SCOPE / P1_FIBERWISE_TRACE_EXACT_COVERAGE_WITH_SCOPE / P1_STATIC_PUNCTURE_PARTIAL_REUSE_STRONG_REFINEMENT / P2_REFLECTION_SUBLINE_CLOSED_BY_EXACT_COVERAGE / P3_PAUSED_SAME_CLASS / P4_NOT_TRIGGERED / P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION_NEXT / GOAL_ACTIVE"
    p["full_sources"] = list(dict.fromkeys(p.get("full_sources", []) + list(SOURCES)))
    p.setdefault("source_hashes", {}).update({rel: h(ROOT / rel) for rel in p["full_sources"] if (ROOT / rel).is_file()})
    p["revalidation"] = p.get("revalidation", "") + " Revision254 records P36 static puncture/strong refinement and supplied-provenance boundary; P37 weak-domain fidelity requalification next."
    state["records"][P36] = {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "PARTIAL_REUSE / STATIC_FIXED_POINT_PUNCTURE_DEFINED / ACTUAL_MRICH_IS_STRONG_REFINEMENT / HISTORICAL_PROVENANCE_NOT_FORMALIZED / P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P35, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {rel: h(ROOT / rel) for rel in SOURCES},
        "scope": "Current source audit only: static fixed-point puncture is defined, actual mRich is StrongPuncture, weak-to-strong refinement is conditional, and Input supplies rather than records historical provenance. No general event conclusion, HoTT defect, K, engine issue, or reality bridge.",
    }
    state["records"][SID] = {"kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL", "evidence_status": "P36_PROVENANCE_ORIGIN_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope", "depends_on": [], "related_records": [PLAN, P35, P36], "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")]}
    state["execution_control"].update({
        "status": "FOUR_TRACK_P1_STATIC_PUNCTURE_REFINEMENT_P37_WEAK_FIDELITY_NEXT",
        "current_phase": "PHASE_2_P36_STATIC_PUNCTURE_REFINEMENT_P37_WEAK_FIDELITY_NEXT",
        "second_phase_status": "P1_ACTIVE_P37_WEAK_FIDELITY_P2_REFLECTION_CLOSED_P3_PAUSED_P4_NOT_TRIGGERED",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P37-P1-WEAK-PUNCTURE-FIDELITY-REQUALIFICATION-001. Fix ordinary M as PuncturedRealCircle and current strong M as StrongPuncture. Audit which source-to-OpenRealInterval steps, observations, and Done clauses require Lift or Strong, and whether any original-X clause expressly selects that refinement. Reuse C-283–C-290; do not rerun them or create a new wrapper unless an exact uncovered field remains. Do not assert a HoTT defect, actual K, engine issue, historical-event impossibility, or reality bridge.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P1_STATIC_PUNCTURE_PARTIAL_REUSE_STRONG_REFINEMENT / P37_WEAK_FIDELITY_NEXT / P2_CLOSED / P3_PAUSED / P4_NOT_TRIGGERED / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = ed.load(ROOT, "MEMORY.md")
    direction = ed.load(ROOT, "方向追踪.md")
    panorama = ed.load(ROOT, "全景视野.md")
    essay = ed.load(ROOT, "扩展认知.md")
    ed.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md", "P35 已确认既有 `CurveRun` 与 P34 fiber 输入完整覆盖声明的连续过程/endpoint Done 合同，未新增 wrapper 或 kernel claim；下一=P36审计原圆去点source是否已有明确的 circle-plus-point provenance operation。P3仍等待实际K，P4未触发。入口：`audit/p35-fiberwise-trace-coverage-20260922/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md`；revision253。", "P36 已确认实际圆的静态指定点去除已定义，但当前 `mRich` 使用 `StrongPuncture` 而普通弱去点到强域需 `Lift`；`Input.source` 也没有历史provenance event。下一=P37复资格化原弱M与强域模型。P3仍等待实际K，P4未触发。入口：`audit/p36-provenance-origin-coverage-20260922/P36-PROVENANCE-ORIGIN-COVERAGE-REPORT.md`；revision254。")
    ed.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260922-ASTRA-P36-PROVENANCE-ORIGIN-COVERAGE：静态固定点去点已定义、mRich为StrongPuncture、source provenance未形式化；P37弱域任务忠实性复资格化next；revision254。\n")

    ed.replace_in_index(direction, "source_state_revision: 253", "source_state_revision: 254")
    ed.replace_in_index(direction, "projection_generation: 20260922-direction-253", "projection_generation: 20260922-direction-254")
    ed.replace_in_index(direction, "semantic_status: FOUR_TRACK_P35_TRACE_COVERAGE_CLOSED_P36_PROVENANCE_ORIGIN_NEXT", "semantic_status: FOUR_TRACK_P36_STATIC_PUNCTURE_REFINEMENT_P37_WEAK_FIDELITY_NEXT")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md", "| `DIR-U-HOTT-FOUR-TRACK` | P35：fiberwise trace exact coverage | P34/P35 | `P36_PROVENANCE_ORIGIN_COVERAGE_GATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、C-320/C-326 | 已覆盖过程合同，审计circle-minus-point来源边 | P35 report；revision253 |", "| `DIR-U-HOTT-FOUR-TRACK` | P36：静态去点与强域来源细化 | P35/P36 | `P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、C-283–C-290 | mRich为StrongPuncture；复资格化原弱M | P36 report；revision254 |")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md", "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P35 | `P3_PAUSED / P36_P1_PROVENANCE_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P35 reports；revision253 |", "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P36 | `P3_PAUSED / P37_P1_WEAK_FIDELITY` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P36 reports；revision254 |")

    ed.replace_in_index(panorama, "source_state_revision: 253", "source_state_revision: 254")
    ed.replace_in_index(panorama, "projection_generation: 20260922-outcome-253", "projection_generation: 20260922-outcome-254")
    ed.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P35_TRACE_COVERAGE_CLOSED_P36_PROVENANCE_ORIGIN_NEXT", "semantic_status: FOUR_TRACK_P36_STATIC_PUNCTURE_REFINEMENT_P37_WEAK_FIDELITY_NEXT")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", "| `OUT-P35-FIBERWISE-TRACE-COVERAGE` | P34 fiber 与 C-320 `CurveRun` 的合同覆盖审计 | `DIR-U-HOTT-FOUR-TRACK` | fixed local source/run receipts | `EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_NEXT` | 已有资产覆盖声明的fiberwise过程/endpoint Done，避免同义wrapper | 不证明完整R_origin、HoTT缺陷、actual K、现实桥或新数学命题 | P35 report/verification；revision253 |", "| `OUT-P35-FIBERWISE-TRACE-COVERAGE` | P34 fiber 与 C-320 `CurveRun` 的合同覆盖审计 | `DIR-U-HOTT-FOUR-TRACK` | fixed local source/run receipts | `EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_COMPLETED` | 已有资产覆盖声明的fiberwise过程/endpoint Done，避免同义wrapper | 不证明完整R_origin、HoTT缺陷、actual K、现实桥或新数学命题 | P35 report/verification；revision253 |\n| `OUT-P36-PROVENANCE-ORIGIN-COVERAGE` | 静态固定点去点与当前强域source审计 | `DIR-U-HOTT-FOUR-TRACK` | fixed local definitions plus C-283–C-290 receipts | `PARTIAL_REUSE / STRONG_REFINEMENT / P37_NEXT` | `PuncturedRealCircle`已定义；mRich使用StrongPuncture，source事件未记载 | 不证明历史事件不可能、HoTT缺陷、actual K或现实桥 | P36 report/verification；revision254 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P35转入P36来源覆盖门 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34/P35 | `P3_PAUSED / P36_P1_PROVENANCE_GATE` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P35 reports；revision253 |", "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P36转入P37弱域复资格化 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34/P35/P36 | `P3_PAUSED / P37_P1_WEAK_FIDELITY` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P36 reports；revision254 |")
    ed.replace_in_shard(panorama, "全景视野/008 - 当前未完成.md", "16. `P36-P1-PROVENANCE-ORIGIN-COVERAGE-001`：审计当前`StrongPuncture`等资产是否保存circle-plus-designated-point到source的明确operation/provenance；全覆盖即停止。", "16. `P37-P1-WEAK-PUNCTURE-FIDELITY-REQUALIFICATION-001`：以普通`PuncturedRealCircle`重审强域`mRich`、`Lift`与原M的任务忠实性；不让强域结论替代弱域。")

    simple = {rel: (ROOT / rel).read_text() for rel in rt.MUTABLE if rel not in {rt.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[rt.PREFIX + "FRONTIER.md"] = simple[rt.PREFIX + "FRONTIER.md"].replace("- P35确认P34 fiber与既有C-320 CurveRun已覆盖声明的过程/endpoint合同，因此不新造wrapper；P36审计circle-plus-point→source的provenance operation。入口：`audit/p35-fiberwise-trace-coverage-20260922/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md`。", "- P36确认静态circle-minus-east已定义但mRich为StrongPuncture细化、source event未记；P37以普通弱去点重新资格化任务。入口：`audit/p36-provenance-origin-coverage-20260922/P36-PROVENANCE-ORIGIN-COVERAGE-REPORT.md`。", 1)
    simple[rt.PREFIX + "RESUME.md"] = simple[rt.PREFIX + "RESUME.md"].replace("当前 active goal 已完成P35：既有C-320 CurveRun加P34 fiber和target transport已完整覆盖声明的fiberwise过程/endpoint合同，故没有增加wrapper或新claim。P36只审计原circle-minus-point source provenance；P3仍等待实际K、P4未触发。入口：`audit/p35-fiberwise-trace-coverage-20260922/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md`；revision253。", "当前 active goal 已完成P36：实际圆的弱静态去点已定义，但mRich是StrongPuncture，弱→强有Lift条件，Input也未保存历史来源event。P37复资格化原弱M与强域结论；P3仍等待实际K、P4未触发。入口：`audit/p36-provenance-origin-coverage-20260922/P36-PROVENANCE-ORIGIN-COVERAGE-REPORT.md`；revision254。", 1)

    rows = []
    for document in (memory, direction, panorama, essay):
        rows.extend(ed.payload_rows(document, ROOT))
    seen = {row["path"] for row in rows}
    for rel in rt.MUTABLE:
        if rel not in seen:
            rows.append({"path": rel, "expected_sha256": h(ROOT / rel), "text": rt.dump(state).decode() if rel == rt.STATE else simple[rel]})
    session = f"# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n- status: `P36_STATIC_PUNCTURE_PARTIAL_REUSE / STRONG_REFINEMENT / P37_WEAK_FIDELITY_NEXT / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM`\n- load_receipt: research plan snapshot `{plan['snapshot']}`; fixed local source definitions, C-283–C-290 receipts, P36 freeze and verifier reviewed.\n- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID, "primary_runs": [{"kind": "P36 source/provenance verifier", "result": "PASS_WITH_SCOPE", "receipt": SOURCES[3]}], "new_math_claims": [], "new_kernel_replay": False, "scope": "P36 source audit only; prior saved kernel receipts are reused and no new proof claim is made."}
    rows += [{"path": BASE + "SESSION.md", "expected_sha256": None, "text": session}, {"path": BASE + "RUNS.json", "expected_sha256": None, "text": rt.dump(runs).decode()}, {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": core_audit(state["current_core"])}]
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN], "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。", "files": rows}
    (OUT / "P36-CHECKPOINT-PAYLOAD.json").write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P36-CHECKPOINT-APPLY.json" if args.apply else "P36-CHECKPOINT-DRY-RUN.json")).write_bytes(rt.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
