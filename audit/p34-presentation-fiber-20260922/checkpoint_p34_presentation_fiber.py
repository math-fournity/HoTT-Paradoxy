#!/usr/bin/env python3
"""Checkpoint P34's presentation-fiber control and select the bounded P35 gate."""
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
SID = "S-RES-20260922-ASTRA-P34-PRESENTATION-FIBER"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P33 = "R-P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-20260922"
P34 = "R-P34-PRESENTATION-FIBER-20260922"
DIR = "audit/p34-presentation-fiber-20260922"
SOURCES = (
    f"{DIR}/P34-PRESENTATION-FIBER-REPORT.md",
    f"{DIR}/P34-PRESENTATION-FIBER-SOURCE-FREEZE.json",
    f"{DIR}/capture_p34_presentation_fiber.py",
    f"{DIR}/verify_p34_presentation_fiber.py",
    f"{DIR}/P34-PRESENTATION-FIBER-VERIFICATION.json",
    "HoTT/formal/agda-unimath/hott-z/PresentationFiber.agda",
    "HoTT/verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01/RUN.json",
    "HoTT/verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01/source-manifest.json",
    "HoTT/CLAIM_EVIDENCE_MATRIX.md",
    "HoTT/verification/PROOF_VERSION_CLOSURE.json",
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
    deepened = {
        "KC-000004", "KC-000005", "KC-000010", "KC-000015", "KC-000021", "KC-000022",
        "KC-000037", "KC-000038", "KC-000039", "KC-000040", "KC-000041", "KC-000042",
        "KC-000043", "KC-000044", "KC-000045", "KC-000046",
    }
    out = f"# {SID} 核心认知回评\n\n"
    out += f"{core['generation']}；46 条；兼容单文件审计登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    out += "- core_change: NO\n"
    out += "- direction_change: P34 closes one P1 static presentation-fiber edge; P35 is a bounded coverage gate for the existing process contract.\n"
    out += "- panorama_change: C-326 has a saved Agda kernel receipt and an explicit no-defect/no-K boundary.\n"
    out += "- essay_change: NO\n"
    out += "- update_decision: preserve original X, keep P2 closed/P3 paused/P4 untriggered, and test whether CurveRun already covers the P35 interface before creating any wrapper.\n"
    out += "- cross_conflicts: no HoTT defect, actual K, implementation discrepancy, complete origin theory, or reality bridge has been established.\n"
    out += "- unresolved: P35 coverage decision; thereafter a distinct P1 obligation or an independently qualified P3/P4 ingress.\n"
    out += "- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    out += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in rows:
        relation = "DEEPENED" if kc in deepened else "NOT_TOUCHED"
        if relation == "DEEPENED":
            judgement = "P34保留原X的来源—呈现—闭合观察，以同一后端区分同裸carrier的presentation；未把结构差异转写为HoTT缺陷。"
            evidence = "C-326、P34 report；若P35显示现有CurveRun已全覆盖，则停止重包装。"
        else:
            judgement = "本单元未直接检验该用户原文；它保留为下一轮P1/P3/P4选择的约束。"
            evidence = "P34 report；新原始证据或P35覆盖裁决可改变后继。"
        out += f"| `{kc}` | {title} | `{relation}` | {judgement} | {evidence} |\n"
    out += "\n## 波次定位\n\n"
    out += "- 最终目标连接：P1/R_min 的静态 presentation 边；没有越过 K_theory、K_app 或 K_engine。\n"
    out += "- 完整路径：`G0 → P1 → P6/P7/P19 → P33 coverage closure → P34`。\n"
    out += "- 新事实：C-326 在 fixed agda-unimath no-erasure 后端中保存同一 Bare fiber 的两种端点闭合相异 presentation。\n"
    out += "- 正控制：`fullTransportPath` 保留闭合端点；反解释：这只是 rich data/fiber 分离，不能推出 HoTT 规则错误。\n"
    out += "- 裁决：`CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P35_FIBERWISE_TRACE_COVERAGE_GATE`。\n"
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rt = runtime()
    ed = editor()
    assert all((ROOT / rel).is_file() for rel in SOURCES)
    verification = json.loads((ROOT / SOURCES[4]).read_text())
    assert verification["status"] == "PASS_WITH_SCOPE"
    state = json.loads((ROOT / rt.STATE).read_text())
    assert state["revision"] == 251
    assert state["latest_session"] == "S-GOV-20260922-ASTRA-P33-SOURCE-HASH-REPAIR"
    head = json.loads((ROOT / rt.HEAD).read_text())
    assert all(h(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = rt.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P34-CHECKPOINT-PLAN.json").write_bytes(rt.dump(plan))

    state["revision"] = 252
    state["latest_session"] = SID
    p = state["records"][PLAN]
    p["related_records"] = list(dict.fromkeys(p.get("related_records", []) + [P34, SID]))
    p["status"] = "p1_presentation_fiber_formalized_p35_coverage_gate_next"
    p["evidence_status"] = (
        "P1_PRESENTATION_FIBER_FORMAL_CHECKED_WITH_SCOPE / "
        "P2_REFLECTION_SUBLINE_CLOSED_BY_EXACT_COVERAGE / P3_PAUSED_SAME_CLASS / "
        "P4_NOT_TRIGGERED / P35_FIBERWISE_TRACE_COVERAGE_GATE_NEXT / GOAL_ACTIVE"
    )
    p["full_sources"] = list(dict.fromkeys(p.get("full_sources", []) + list(SOURCES)))
    p.setdefault("source_hashes", {}).update({rel: h(ROOT / rel) for rel in p["full_sources"] if (ROOT / rel).is_file()})
    p["revalidation"] = p.get("revalidation", "") + " Revision252 records C-326 presentation-fiber kernel control and selects P35 only as an exact-coverage gate for CurveRun."

    state["records"][P34] = {
        "kind": "result",
        "path": SOURCES[0],
        "lifecycle_status": "CURRENT",
        "evidence_status": "FORMAL_CHECKED_WITH_SCOPE / SAME_BARE_FIBER_HAS_DISTINCT_PRESENTATIONS / ENDPOINT_CLOSURE_SEPARATES_PRESENTATIONS / P35_FIBERWISE_TRACE_COVERAGE_GATE_NEXT / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P33, SID],
        "full_sources": list(SOURCES),
        "source_hashes": {rel: h(ROOT / rel) for rel in SOURCES},
        "scope": "Fixed agda-unimath no-erasure P1 control: a selected Bare fiber contains closed and open presentations separated by endpoint coincidence. It does not establish a full origin/process/Done theory, K_theory, K_app, K_engine, a HoTT defect, or a reality bridge.",
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P34_PRESENTATION_FIBER_CHECKPOINTED_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P33, P34],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P1_PRESENTATION_FIBER_FORMALIZED_P35_COVERAGE_GATE_NEXT",
        "current_phase": "PHASE_2_P34_P1_PRESENTATION_FIBER_FORMALIZED_P35_COVERAGE_GATE_NEXT",
        "second_phase_status": "P1_ACTIVE_P35_COVERAGE_GATE_P2_REFLECTION_CLOSED_P3_PAUSED_P4_NOT_TRIGGERED",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": (
            "P35-P1-FIBERWISE-TRACE-COVERAGE-001. With P34's fixed PresentationFiber members and the same original X, "
            "compare existing NativeTaskIntegration.CurveRun field-by-field against a proposed fiberwise source/operation/observation/Done contract. "
            "If CurveRun already covers every obligation after specialization/transport, report EXACT_COVERAGE and do not add a wrapper record or new kernel claim; "
            "otherwise formalize only the precise missing field. Do not assert HoTT defect, K_theory, K_app, K_engine, or reality bridge."
        ),
    })
    state["projection"]["status"] = "FOUR_TRACK_P1_PRESENTATION_FIBER_FORMALIZED / P35_FIBERWISE_TRACE_COVERAGE_GATE_NEXT / P2_CLOSED / P3_PAUSED / P4_NOT_TRIGGERED / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    memory = ed.load(ROOT, "MEMORY.md")
    direction = ed.load(ROOT, "方向追踪.md")
    panorama = ed.load(ROOT, "全景视野.md")
    essay = ed.load(ROOT, "扩展认知.md")
    ed.replace_in_shard(
        memory, "MEMORY/001 - 当前执行队列.md",
        "P33 的source-freeze收据已在revision251修复；P33覆盖结论与P34 P1来源—操作—复原关系发现不变。P3仍等待实际K，P4未触发。入口：`audit/p33-2ltt-v5-self-metatheory-boundary-audit-20260922/P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-REPORT.md`；revision251。",
        "P34 已以 C-326 在同一 agda-unimath 后端固定 `PresentationFiber`：同一 `Bare` fiber 中的闭合与开端点呈现不同；下一=P35逐项核对既有 `CurveRun` 是否已完全覆盖 fiberwise 过程合同。P3仍等待实际K，P4未触发。入口：`audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md`；revision252。",
    )
    ed.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-RES-20260922-ASTRA-P34-PRESENTATION-FIBER：C-326同裸carrier的presentation fiber已在固定Agda后端核验；P35仅做CurveRun的fiberwise exact-coverage gate；revision252。\n")

    ed.replace_in_index(direction, "source_state_revision: 251", "source_state_revision: 252")
    ed.replace_in_index(direction, "projection_generation: 20260922-direction-251", "projection_generation: 20260922-direction-252")
    ed.replace_in_index(direction, "semantic_status: FOUR_TRACK_P33_COVERAGE_CLOSED_P34_P1_ORIGIN_RELATION_NEXT", "semantic_status: FOUR_TRACK_P34_PRESENTATION_FIBER_FORMALIZED_P35_COVERAGE_GATE_NEXT")
    ed.replace_in_shard(
        direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P33：2LTT v5边界覆盖裁决 | P32/P33 | `P34_P1_ORIGIN_RELATION_DISCOVERY_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | P2反射边界已覆盖，回到原X/P1 | P33 report；revision250 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P34：same-backend presentation fiber 控制 | P33/P34 | `P35_FIBERWISE_TRACE_COVERAGE_GATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、C-326 | P1静态fiber已核；先判CurveRun是否已覆盖过程合同 | P34 report/run；revision252 |",
    )
    ed.replace_in_shard(
        direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P33 | `P3_PAUSED / P34_P1_RELATION_DISCOVERY` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P33 reports；revision250 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P34 | `P3_PAUSED / P35_P1_COVERAGE_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P34 reports；revision252 |",
    )

    ed.replace_in_index(panorama, "source_state_revision: 251", "source_state_revision: 252")
    ed.replace_in_index(panorama, "projection_generation: 20260922-outcome-251", "projection_generation: 20260922-outcome-252")
    ed.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P33_COVERAGE_CLOSED_P34_P1_ORIGIN_RELATION_NEXT", "semantic_status: FOUR_TRACK_P34_PRESENTATION_FIBER_FORMALIZED_P35_COVERAGE_GATE_NEXT")
    ed.replace_in_shard(
        panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-HOTT-FOUR-TRACK-PLAN` | P33 2LTT v5边界覆盖裁决 | `DIR-U-HOTT-FOUR-TRACK` | P32/P33 | `P33_COVERAGE_CLOSED / P34_NEXT` | 已有条件边界不连原X，回到P1 | 不证明HoTT缺陷 | P33 report；revision250 |",
        "| `OUT-HOTT-FOUR-TRACK-PLAN` | P33 2LTT v5边界覆盖裁决 | `DIR-U-HOTT-FOUR-TRACK` | P32/P33 | `P33_COVERAGE_CLOSED / P34_COMPLETED` | 已有条件边界不连原X，回到P1 | 不证明HoTT缺陷 | P33 report；revision250 |\n| `OUT-P34-PRESENTATION-FIBER` | C-326 同一 `Bare` fiber 的呈现分离 | `DIR-U-HOTT-FOUR-TRACK` | fixed agda-unimath no-erasure source/run | `FORMAL_CHECKED_WITH_SCOPE / P35_COVERAGE_GATE_NEXT` | 闭合与开端点presentation都可位于同一裸carrier fiber，且无fiber path | 不证明完整来源/过程/Done、HoTT缺陷、actual K或现实桥 | P34 report/run；revision252 |",
    )
    ed.replace_in_shard(
        panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P33回到P1 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33 | `P3_PAUSED / P34_P1_RELATION_DISCOVERY` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P33 reports；revision250 |",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P34转入P35覆盖门 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34 | `P3_PAUSED / P35_P1_COVERAGE_GATE` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P34 reports；revision252 |",
    )
    ed.replace_in_shard(
        panorama, "全景视野/008 - 当前未完成.md",
        "16. `P34-P1-ORIGIN-RELATION-DISCOVERY-001`：从R_min/P6/P7/P19等资产出发，选择未覆盖的来源—操作—复原数学关系或不变量。",
        "16. `P35-P1-FIBERWISE-TRACE-COVERAGE-001`：逐项判定既有`CurveRun`是否已经覆盖P34指定fiber成员之间的过程/完成合同；全覆盖即停止，不另造wrapper。",
    )

    simple = {rel: (ROOT / rel).read_text() for rel in rt.MUTABLE if rel not in {rt.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[rt.PREFIX + "FRONTIER.md"] = simple[rt.PREFIX + "FRONTIER.md"].replace(
        "- P33确认2LTT v5相关边界已由既有机器/来源资产覆盖且不连原X；P34回到P1寻找来源—操作—复原数学关系。入口：`audit/p33-2ltt-v5-self-metatheory-boundary-audit-20260922/P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-REPORT.md`。",
        "- P34以C-326在fixed agda-unimath后端核验同一Bare fiber的闭合/开端点presentation分离；P35只核既有CurveRun是否已经覆盖fiberwise过程合同。入口：`audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md`。",
        1,
    )
    simple[rt.PREFIX + "RESUME.md"] = simple[rt.PREFIX + "RESUME.md"].replace(
        "当前 active goal 在P33后回到P1：2LTT v5相关边界已被本地原文/机器控制覆盖，且不提供原X/O6桥。P34发现未覆盖的来源—操作—复原数学关系；P3等待实际K、P4未触发。入口：`audit/p33-2ltt-v5-self-metatheory-boundary-audit-20260922/P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-REPORT.md`；revision251（P33 source-freeze receipt repaired）。",
        "当前 active goal 已完成P34：C-326固定同一Bare fiber中的闭合/开端点presentation差异，不把它误报为HoTT缺陷。P35只做既有CurveRun的fiberwise过程合同exact-coverage核对；P3仍等待实际K、P4未触发。入口：`audit/p34-presentation-fiber-20260922/P34-PRESENTATION-FIBER-REPORT.md`；revision252。",
        1,
    )

    rows = []
    for document in (memory, direction, panorama, essay):
        rows.extend(ed.payload_rows(document, ROOT))
    seen = {row["path"] for row in rows}
    for rel in rt.MUTABLE:
        if rel not in seen:
            rows.append({"path": rel, "expected_sha256": h(ROOT / rel), "text": rt.dump(state).decode() if rel == rt.STATE else simple[rel]})
    session = f"# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n- status: `P34_PRESENTATION_FIBER_FORMAL_CHECKED_WITH_SCOPE / P35_COVERAGE_GATE_NEXT / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM`\n- load_receipt: research plan snapshot `{plan['snapshot']}`; P34 local/history reconnaissance, source freeze, claim matrix, kernel run and verifier reviewed.\n- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [{"kind": "Agda P34 presentation-fiber kernel check", "result": "KERNEL_ACCEPTED_WITH_SCOPE", "receipt": SOURCES[6]}],
        "new_math_claims": ["C-326"],
        "new_kernel_replay": True,
        "scope": "Local P1 fiber control only; P35 will test exact coverage before any new wrapper is constructed.",
    }
    rows += [
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": rt.dump(runs).decode()},
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
    (OUT / "P34-CHECKPOINT-PAYLOAD.json").write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P34-CHECKPOINT-APPLY.json" if args.apply else "P34-CHECKPOINT-DRY-RUN.json")).write_bytes(rt.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
