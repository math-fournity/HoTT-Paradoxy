#!/usr/bin/env python3
"""Checkpoint P35 exact coverage and route the active P1 leaf to provenance review."""
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
SID = "S-RES-20260922-ASTRA-P35-FIBERWISE-TRACE-COVERAGE"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P34 = "R-P34-PRESENTATION-FIBER-20260922"
P35 = "R-P35-FIBERWISE-TRACE-COVERAGE-20260922"
DIR = "audit/p35-fiberwise-trace-coverage-20260922"
SOURCES = (
    f"{DIR}/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md",
    f"{DIR}/P35-FIBERWISE-TRACE-SOURCE-FREEZE.json",
    f"{DIR}/verify_p35_fiberwise_trace_coverage.py",
    f"{DIR}/P35-FIBERWISE-TRACE-COVERAGE-VERIFICATION.json",
    "HoTT/formal/agda-unimath/hott-z/PresentationFiber.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeCurveTask.agda",
    "HoTT/verification/runs/20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01/RUN.json",
    "HoTT/verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01/RUN.json",
    "audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md",
    "audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-VERIFICATION.json",
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
    deepened = {"KC-000004", "KC-000005", "KC-000010", "KC-000015", "KC-000021", "KC-000022", "KC-000037", "KC-000038", "KC-000039", "KC-000040", "KC-000041", "KC-000042", "KC-000043", "KC-000044", "KC-000045", "KC-000046"}
    out = f"# {SID} 核心认知回评\n\n{core['generation']}；46 条；兼容单文件审计登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    out += "- core_change: NO\n- direction_change: P35 closes a duplicate P1 wrapper route and selects P36 source/provenance coverage.\n- panorama_change: no new mathematics; C-320/C-326 are reused with their existing scopes.\n- essay_change: NO\n- update_decision: do not create PresentationRun; inspect the original circle-minus-point source edge next.\n- cross_conflicts: no HoTT defect, K, engine discrepancy, complete origin theory, or reality bridge established.\n- unresolved: P36 provenance-origin coverage; P3 and P4 retain their prior gates.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    out += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in rows:
        relation = "DEEPENED" if kc in deepened else "NOT_TOUCHED"
        if relation == "DEEPENED":
            judgement = "P35保持原X的过程/端点观察，证实现有CurveRun已覆盖窄合同，并拒绝把一个新名字当作发现。"
            evidence = "P35 report/verification；P36来源审计可改变下一边的资格。"
        else:
            judgement = "本单元未直接检验该用户原文；它仍约束P36和可能的P3/P4重新进入。"
            evidence = "P35 report；新的原始来源或实际K可改变判断。"
        out += f"| `{kc}` | {title} | `{relation}` | {judgement} | {evidence} |\n"
    out += "\n## 波次定位\n\n- 最终目标连接：P1/R_min 的 fiberwise operation—endpoint completion 子边。\n- 实际价值：确认该子边已经由现有 C-320/C-326 资产覆盖，阻止同义 wrapper。\n- 裁决：`CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P36_PROVENANCE_ORIGIN_COVERAGE_GATE`。\n"
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
    assert state["revision"] == 252
    assert state["latest_session"] == "S-RES-20260922-ASTRA-P34-PRESENTATION-FIBER"
    head = json.loads((ROOT / rt.HEAD).read_text())
    assert all(h(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = rt.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P35-CHECKPOINT-PLAN.json").write_bytes(rt.dump(plan))

    state["revision"] = 253
    state["latest_session"] = SID
    p = state["records"][PLAN]
    p["related_records"] = list(dict.fromkeys(p.get("related_records", []) + [P35, SID]))
    p["status"] = "p1_fiberwise_trace_covered_p36_provenance_origin_gate_next"
    p["evidence_status"] = "P1_PRESENTATION_FIBER_FORMAL_CHECKED_WITH_SCOPE / P1_FIBERWISE_TRACE_EXACT_COVERAGE_WITH_SCOPE / P2_REFLECTION_SUBLINE_CLOSED_BY_EXACT_COVERAGE / P3_PAUSED_SAME_CLASS / P4_NOT_TRIGGERED / P36_PROVENANCE_ORIGIN_COVERAGE_GATE_NEXT / GOAL_ACTIVE"
    p["full_sources"] = list(dict.fromkeys(p.get("full_sources", []) + list(SOURCES)))
    p.setdefault("source_hashes", {}).update({rel: h(ROOT / rel) for rel in p["full_sources"] if (ROOT / rel).is_file()})
    p["revalidation"] = p.get("revalidation", "") + " Revision253 closes P35 by exact source-field coverage, declines a duplicate wrapper, and selects P36 provenance-origin coverage."
    state["records"][P35] = {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_PROVENANCE_ORIGIN_COVERAGE_GATE_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P34, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {rel: h(ROOT / rel) for rel in SOURCES},
        "scope": "The P35-specific fiberwise continuous-process contract is already covered by P34 fiber inputs plus C-320 CurveRun and target transport. No new theorem, wrapper term, full origin theory, K, HoTT defect, or reality bridge is asserted.",
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P35_EXACT_COVERAGE_CHECKPOINTED_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P34, P35],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P1_FIBERWISE_TRACE_COVERED_P36_PROVENANCE_ORIGIN_GATE_NEXT",
        "current_phase": "PHASE_2_P35_FIBERWISE_TRACE_COVERED_P36_PROVENANCE_ORIGIN_GATE_NEXT",
        "second_phase_status": "P1_ACTIVE_P36_PROVENANCE_GATE_P2_REFLECTION_CLOSED_P3_PAUSED_P4_NOT_TRIGGERED",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P36-P1-PROVENANCE-ORIGIN-COVERAGE-001. Starting from fixed original X and P34/P35 controls, inspect StrongPuncture, PunctureApartness, NativeRealCircleQualification, NativeRichCurve and NativeSourceContract for an explicit circle-plus-designated-point → puncture/source operation, its observations, and its Done witness. Classify exact coverage, partial reuse, or a single precise missing field; do not create a provenance wrapper before the coverage comparison, and do not assert HoTT defect, actual K, engine issue, or reality bridge.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P1_FIBERWISE_TRACE_EXACT_COVERAGE / P36_PROVENANCE_ORIGIN_COVERAGE_GATE_NEXT / P2_CLOSED / P3_PAUSED / P4_NOT_TRIGGERED / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = ed.load(ROOT, "MEMORY.md")
    direction = ed.load(ROOT, "方向追踪.md")
    panorama = ed.load(ROOT, "全景视野.md")
    essay = ed.load(ROOT, "扩展认知.md")
    ed.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md", "P34 已以 C-326 在同一 agda-unimath 后端固定 `PresentationFiber`：同一 `Bare` fiber 中的闭合与开端点呈现不同；下一=P35逐项核对既有 `CurveRun` 是否已完全覆盖 fiberwise 过程合同。P3仍等待实际K，P4未触发。入口：`audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md`；revision252。", "P35 已确认既有 `CurveRun` 与 P34 fiber 输入完整覆盖声明的连续过程/endpoint Done 合同，未新增 wrapper 或 kernel claim；下一=P36审计原圆去点source是否已有明确的 circle-plus-point provenance operation。P3仍等待实际K，P4未触发。入口：`audit/p35-fiberwise-trace-coverage-20260922/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md`；revision253。")
    ed.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260922-ASTRA-P35-FIBERWISE-TRACE-COVERAGE：C-320/C-326已完整覆盖P35窄过程合同，未新造wrapper；P36 provenance-origin coverage gate next；revision253。\n")

    ed.replace_in_index(direction, "source_state_revision: 252", "source_state_revision: 253")
    ed.replace_in_index(direction, "projection_generation: 20260922-direction-252", "projection_generation: 20260922-direction-253")
    ed.replace_in_index(direction, "semantic_status: FOUR_TRACK_P34_PRESENTATION_FIBER_FORMALIZED_P35_COVERAGE_GATE_NEXT", "semantic_status: FOUR_TRACK_P35_TRACE_COVERAGE_CLOSED_P36_PROVENANCE_ORIGIN_NEXT")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md", "| `DIR-U-HOTT-FOUR-TRACK` | P34：same-backend presentation fiber 控制 | P33/P34 | `P35_FIBERWISE_TRACE_COVERAGE_GATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、C-326 | P1静态fiber已核；先判CurveRun是否已覆盖过程合同 | P34 report/run；revision252 |", "| `DIR-U-HOTT-FOUR-TRACK` | P35：fiberwise trace exact coverage | P34/P35 | `P36_PROVENANCE_ORIGIN_COVERAGE_GATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、C-320/C-326 | 已覆盖过程合同，审计circle-minus-point来源边 | P35 report；revision253 |")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md", "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P34 | `P3_PAUSED / P35_P1_COVERAGE_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P34 reports；revision252 |", "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P35 | `P3_PAUSED / P36_P1_PROVENANCE_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P35 reports；revision253 |")

    ed.replace_in_index(panorama, "source_state_revision: 252", "source_state_revision: 253")
    ed.replace_in_index(panorama, "projection_generation: 20260922-outcome-252", "projection_generation: 20260922-outcome-253")
    ed.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P34_PRESENTATION_FIBER_FORMALIZED_P35_COVERAGE_GATE_NEXT", "semantic_status: FOUR_TRACK_P35_TRACE_COVERAGE_CLOSED_P36_PROVENANCE_ORIGIN_NEXT")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", "| `OUT-P34-PRESENTATION-FIBER` | C-326 同一 `Bare` fiber 的呈现分离 | `DIR-U-HOTT-FOUR-TRACK` | fixed agda-unimath no-erasure source/run | `FORMAL_CHECKED_WITH_SCOPE / P35_COVERAGE_GATE_NEXT` | 闭合与开端点presentation都可位于同一裸carrier fiber，且无fiber path | 不证明完整来源/过程/Done、HoTT缺陷、actual K或现实桥 | P34 report/run；revision252 |", "| `OUT-P34-PRESENTATION-FIBER` | C-326 同一 `Bare` fiber 的呈现分离 | `DIR-U-HOTT-FOUR-TRACK` | fixed agda-unimath no-erasure source/run | `FORMAL_CHECKED_WITH_SCOPE / P35_COVERAGE_CLOSED` | 闭合与开端点presentation都可位于同一裸carrier fiber，且无fiber path | 不证明完整来源/过程/Done、HoTT缺陷、actual K或现实桥 | P34 report/run；revision252 |\n| `OUT-P35-FIBERWISE-TRACE-COVERAGE` | P34 fiber 与 C-320 `CurveRun` 的合同覆盖审计 | `DIR-U-HOTT-FOUR-TRACK` | fixed local source/run receipts | `EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_NEXT` | 已有资产覆盖声明的fiberwise过程/endpoint Done，避免同义wrapper | 不证明完整R_origin、HoTT缺陷、actual K、现实桥或新数学命题 | P35 report/verification；revision253 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P34转入P35覆盖门 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34 | `P3_PAUSED / P35_P1_COVERAGE_GATE` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P34 reports；revision252 |", "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P35转入P36来源覆盖门 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34/P35 | `P3_PAUSED / P36_P1_PROVENANCE_GATE` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P35 reports；revision253 |")
    ed.replace_in_shard(panorama, "全景视野/008 - 当前未完成.md", "16. `P35-P1-FIBERWISE-TRACE-COVERAGE-001`：逐项判定既有`CurveRun`是否已经覆盖P34指定fiber成员之间的过程/完成合同；全覆盖即停止，不另造wrapper。", "16. `P36-P1-PROVENANCE-ORIGIN-COVERAGE-001`：审计当前`StrongPuncture`等资产是否保存circle-plus-designated-point到source的明确operation/provenance；全覆盖即停止。")

    simple = {rel: (ROOT / rel).read_text() for rel in rt.MUTABLE if rel not in {rt.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[rt.PREFIX + "FRONTIER.md"] = simple[rt.PREFIX + "FRONTIER.md"].replace("- P34以C-326在fixed agda-unimath后端核验同一Bare fiber的闭合/开端点presentation分离；P35只核既有CurveRun是否已经覆盖fiberwise过程合同。入口：`audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md`。", "- P35确认P34 fiber与既有C-320 CurveRun已覆盖声明的过程/endpoint合同，因此不新造wrapper；P36审计circle-plus-point→source的provenance operation。入口：`audit/p35-fiberwise-trace-coverage-20260922/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md`。", 1)
    simple[rt.PREFIX + "RESUME.md"] = simple[rt.PREFIX + "RESUME.md"].replace("当前 active goal 已完成P34：C-326固定同一Bare fiber中的闭合/开端点presentation差异，不把它误报为HoTT缺陷。P35只做既有CurveRun的fiberwise过程合同exact-coverage核对；P3仍等待实际K、P4未触发。入口：`audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md`；revision252。", "当前 active goal 已完成P35：既有C-320 CurveRun加P34 fiber和target transport已完整覆盖声明的fiberwise过程/endpoint合同，故没有增加wrapper或新claim。P36只审计原circle-minus-point source provenance；P3仍等待实际K、P4未触发。入口：`audit/p35-fiberwise-trace-coverage-20260922/P35-FIBERWISE-TRACE-COVERAGE-REPORT.md`；revision253。", 1)

    rows = []
    for document in (memory, direction, panorama, essay):
        rows.extend(ed.payload_rows(document, ROOT))
    seen = {row["path"] for row in rows}
    for rel in rt.MUTABLE:
        if rel not in seen:
            rows.append({"path": rel, "expected_sha256": h(ROOT / rel), "text": rt.dump(state).decode() if rel == rt.STATE else simple[rel]})
    session = f"# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n- status: `P35_EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_PROVENANCE_GATE_NEXT`\n- load_receipt: research plan snapshot `{plan['snapshot']}`; P35 report, source freeze, verifier, P34/C-320 source and saved runs reviewed.\n- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID, "primary_runs": [{"kind": "P35 source-field verifier", "result": "PASS_WITH_SCOPE", "receipt": SOURCES[3]}], "new_math_claims": [], "new_kernel_replay": False, "scope": "Exact coverage audit only; P35 introduced no wrapper source or new kernel claim."}
    rows += [{"path": BASE + "SESSION.md", "expected_sha256": None, "text": session}, {"path": BASE + "RUNS.json", "expected_sha256": None, "text": rt.dump(runs).decode()}, {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": core_audit(state["current_core"])}]
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN], "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。", "files": rows}
    (OUT / "P35-CHECKPOINT-PAYLOAD.json").write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P35-CHECKPOINT-APPLY.json" if args.apply else "P35-CHECKPOINT-DRY-RUN.json")).write_bytes(rt.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
