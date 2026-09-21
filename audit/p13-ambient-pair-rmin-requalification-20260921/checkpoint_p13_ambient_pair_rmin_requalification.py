#!/usr/bin/env python3
"""Checkpoint P13's operation-sensitive R_ambient qualification and route P14."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-RES-20260921-ASTRA-P13-AMBIENT-PAIR-RMIN"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN_ID = "R-HOTT-FOUR-TRACK-PLAN-20260921"
ABX_ID = "R-ABX-ACTION-20260921"
P13_ID = "R-P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-20260921"
PREVIOUS_IDS = (
    "R-P1-RMIN-SPEC-20260921", "R-P2-KTHEORY-SIP-20260921",
    "R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921", "R-P5-SUCCESSOR-DISCOVERY-20260921",
    "R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921", "R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921",
    "R-P8-RZK-DIRECTED-IMPLEMENTATION-20260921", "R-P9-SHOTT-DIRUNIV-CORPUS-20260921",
    "R-P10-SECOND-SUCCESSOR-DISCOVERY-20260921", "R-P11-COQHOTT-CIRCLE-COEQUALIZER-20260921",
    "R-P12-THIRD-SUCCESSOR-DISCOVERY-20260921",
)
REPORT = "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md"
FREEZE = "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-EVIDENCE-FREEZE.json"
VERIFY = "audit/p13-ambient-pair-rmin-requalification-20260921/verify_p13_ambient_pair_rmin_requalification.py"
RECEIPT = "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-VERIFICATION.json"
CHECKPOINT = "audit/p13-ambient-pair-rmin-requalification-20260921/checkpoint_p13_ambient_pair_rmin_requalification.py"
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
PLAN = "HoTT后续研究总体方案.md"
PLAN_SHARDS = tuple("HoTT后续研究总体方案/" + name for name in (
    "001 - 上一轮问答与四分支校正.md", "002 - 共同任务、术语与优先级原则.md",
    "003 - 分支顺序、准入与停止条件.md", "004 - 令牌经济、反漂移与每单元复核.md",
    "005 - 当前第一步与交接.md",
))
P13_SOURCES = (
    REPORT, FREEZE, VERIFY, RECEIPT, CHECKPOINT, PLAN_VERIFY, PLAN_RECEIPT, PLAN, *PLAN_SHARDS,
    "goal.md", "goal-3.md", "feature-list.md", "rulings.md", "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    "audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md",
    "audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md",
    "audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md",
    "HoTT/formal/astra-real-geometry/PuncturedCircle.lean",
    "HoTT/formal/astra-real-geometry/AmbientCircle.lean",
    "HoTT/formal/astra-real-geometry/DeformationCircle.lean",
    "HoTT/formal/astra-real-geometry/EndpointClosure.lean",
    "HoTT/formal/astra-real-geometry/StructuredCurve.lean",
    "HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02/RUN.json",
    "HoTT/verification/runs/20260920-MP-ASTRA-CURVE-DEFORMATION-001-02/RUN.json",
    "HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/RUN.json",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repl(text: str, old: str, new: str) -> str:
    value, count = re.subn(re.escape(old), new, text, count=1)
    assert count == 1, old
    return value


def row(text: str, prefix: str, value: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = value
            return "\n".join(lines) + "\n"
    raise AssertionError(prefix)


def audit(core: dict[str, object]) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.M)
    assert len(headings) == core["kc_count"] == 46
    touched = {3, 4, 5, 10, 15, 19, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    result = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P13_R_AMBIENT_SPECIALIZATION_ACCEPTED_P14_AMBIENT_OPERATION_K_DISCOVERY_NEXT
- panorama_change: OPERATION_CLASS_SPLIT_WITH_FINITE_AMBIENT_NEGATIVE_AND_CURVE_EMBEDDING_POSITIVE_CONTROL
- essay_change: NO
- update_decision: P13 accepts an operation-sensitive R_ambient specialization, preserving both its finite ambient-homeomorphism negative control and its curve-embedding positive control; P14 must seek an actual consumer rather than repeat geometry.
- cross_conflicts: C-268 and C-269 concern distinct operation contracts, so their opposite Done results do not form P and not-P for one task.
- unresolved: an actual K, a rule bridge, a theory–implementation discrepancy, and any HoTT-defect conclusion remain open.
- writer_compatibility: `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`; runtime 3.6.1 permits this complete legacy 46-KC single-file audit in the atomic bundle, not nested audit shards.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for ordinal, (kc, topic) in enumerate(headings, 1):
        if ordinal in touched:
            relation = "DEEPENED"
            assessment = "P13把同一M/N对的内在同胚、有限环境同胚失败与曲线embedding成功分开，要求任何现实/理论完成判断携带operation class。"
            evidence = f"{REPORT}；P14若发现bare H_intrinsic被实际当作某个operation-sensitive Done才改变K判词。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本单元只资格化P13的既有几何证据与operation-sensitive Done。"
            evidence = "goal.md §2；无新数学定理、原生HoTT运行或HoTT缺陷结论。"
        result += f"| `{kc}` | {topic} | {relation} | {assessment} | {evidence} |\n"
    return result + """

## 扩展认知逐片复认

001–008：P13把现实对齐落实为同一对象的两个受控操作合同，而不是把理论标签当作现实完成。标准术语帮助命名差异，但只由固定源、任务和运行收据决定本轮结论。

## 波次定位

1. **最终目标连接：** P13收紧R端，避免未来K审计把“同胚”“环境同胚”和“曲线变形”混成一个完成命题。
2. **全局坐标：** P12选择环境对；P13资格化operation-sensitive R；P14转入实际消费者discover，不重复几何。
3. **实际价值：** 同一输入上有相反的操作控制，排除两种过强叙述，并给出future-K的精确Done目标。
4. **继续检验：** P14必须改变为版本固定调用链、输入和输出审计；重跑Lean或搜同义术语无资格继续。
5. **不延续P13的理由：** P13的正反操作对照已闭合，新增几何例子不会改变该合同。
6. **裁决：** `SWITCH_BRANCH / R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE`，P14尚未开始；无K或HoTT缺陷结论。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    subprocess.check_call([sys.executable, "-B", PLAN_VERIFY, "--write"], cwd=ROOT)
    for source in P13_SOURCES:
        assert (ROOT / source).is_file(), source

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 232
    assert state["latest_session"] == "S-RES-20260921-ASTRA-P12-THIRD-SUCCESSOR-DISCOVERY"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha(ROOT / path) == digest for path, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID])
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P13-AMBIENT-PAIR-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    previous = state["latest_session"]
    state["revision"] = 233
    state["latest_session"] = SID
    for ident in (*PREVIOUS_IDS, PLAN_ID, ABX_ID):
        record = state["records"][ident]
        record["related_records"] = list(dict.fromkeys(record.get("related_records", []) + [P13_ID, SID]))
        paths = set(record.get("full_sources", [])) | set(record.get("source_hashes", {}))
        record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
        record["revalidation"] = record.get("revalidation", "") + " Revision233 records P13's operation-sensitive R_ambient qualification; prior scope unchanged."

    portfolio = state["records"][PLAN_ID]
    portfolio["evidence_status"] = "USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_DEFENSE / P10_COQHOTT_CANDIDATE_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_AMBIENT_PAIR_CANDIDATE_SELECTED / P13_R_AMBIENT_SPECIALIZATION_ACCEPTED / P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY_NEXT / GOAL_ACTIVE"
    portfolio["status"] = "four_track_first_pass_p5_p6_p7_p8_p9_complete_p10_selected_p11_gluing_defense_p12_ambient_pair_selected_p13_r_ambient_accepted_p14_next"
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(P13_SOURCES)))
    portfolio["related_records"] = list(dict.fromkeys(portfolio.get("related_records", []) + [P13_ID, SID]))
    paths = set(portfolio["full_sources"]) | set(portfolio.get("source_hashes", {}))
    portfolio["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    portfolio["revalidation"] = "Revision233 completes P13: fixed finite ambient-homeomorphism and curve-embedding operation classes give opposite, scoped Done outcomes on the same M/N pair. P14 must select an actual consumer candidate."
    portfolio["scope"] = "P13 qualifies a classical operation-sensitive R specialization. It does not rerun Lean, establish native HoTT, find K, or claim a HoTT defect."

    abx = state["records"][ABX_ID]
    abx["full_sources"] = list(dict.fromkeys(abx.get("full_sources", []) + list(P13_SOURCES)))
    paths = set(abx["full_sources"]) | set(abx.get("source_hashes", {}))
    abx["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    abx["revalidation"] = "Revision233 establishes R_ambient only with explicit operation classes: finite ambient-homeomorphism reconstruction is false, curve embedding deformation is true. P14 searches for an actual bare-to-Done consumer."
    abx["scope"] = "P13 gives no actual K. It supplies two operation-sensitive completion contracts for P14's K-admission discovery."

    state["records"][P13_ID] = {
        "kind": "result", "path": REPORT, "lifecycle_status": "CURRENT",
        "evidence_status": "R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE / OPERATION_CLASS_SPLIT_REQUIRED / P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY_NEXT / NO_ACTUAL_K / NO_NEW_MATHEMATICAL_CLAIM",
        "status": "complete_with_scope_p14_ambient_operation_k_successor_discovery_next", "depends_on": [],
        "related_records": [PLAN_ID, ABX_ID, *PREVIOUS_IDS, previous],
        "full_sources": list(dict.fromkeys(P13_SOURCES)),
        "source_hashes": {path: sha(ROOT / path) for path in dict.fromkeys(P13_SOURCES)},
        "scope": "P13 distinguishes finite ambient-homeomorphism failure from curve-embedding deformation success. It is a classical R_min specialization, not actual K or HoTT evidence.",
    }
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "P13_AMBIENT_PAIR_RMIN_REQUALIFICATION_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [P13_ID, PLAN_ID, ABX_ID, previous],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT",
        current_phase="PHASE_2_P13_R_AMBIENT_SPECIALIZATION_ACCEPTED_P14_AMBIENT_OPERATION_K_DISCOVERY_NEXT",
        second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT",
        last_checkpoint_session=SID,
        checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json",
        next_minimal_verification="P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-001. Perform public/community plus local/historical reconnaissance for a version-pinned actual HoTT/cubical/related consumer. Apply P7 K-input/K-output/K-claim/K-forgetting/K-version to determine whether bare H_intrinsic is actually promoted to Done_ambient^fin or Done_curve. Select one new candidate or a next discovery denominator; do not repeat C-265–C-277 geometry.",
    )
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_AMBIENT_PAIR_SELECTED / P13_R_AMBIENT_SPECIALIZATION_ACCEPTED / NEXT_P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for operation-sensitive R specialization
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: decide whether existing ambient-pair evidence is a non-arbitrary R_min specialization
- load_receipt: `audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / R_AMBIENT_SPECIALIZATION_ACCEPTED / P14_NEXT

P13 did not run Lean. It reconciled pre-existing checked sources: finite lists of ambient-plane homeomorphisms cannot map N to M, while a jointly continuous family of curve embeddings does map N to M. The distinction belongs to the operation contract, so it cannot support either a general impossibility claim or a HoTT defect claim.

| element | use | effect on this unit |
|---|---|---|
| C-265–C-268 | used | fixes intrinsic and finite ambient-homeomorphism controls |
| C-269/C-270 | used | supplies the curve-embedding positive operation control |
| C-275–C-277 | used | confirms boundary/completion remains a separate structured layer |
| public isotopy references | used | standardize terminology; no extension theorem applied to this model |
| Lean kernel | not run | no new theorem or replay |
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{
            "kind": "p13-existing-evidence-requalification",
            "command": "source/run-manifest identity check; P13 verifier; four-track plan verifier; public terminology check",
            "result": "PASS_WITH_SCOPE; operation-sensitive R_ambient specialization accepted; P14 routed",
            "mathematics": "NO_NEW_KERNEL_RUN",
        }],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "P13 existing-source qualification only.",
    }
    drow = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P13操作敏感R专门化与P14实际K发现 | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_GLUING_DEFENSE / P12_AMBIENT_PAIR_SELECTED / P13_R_AMBIENT_ACCEPTED / NEXT_P14_AMBIENT_OPERATION_K_DISCOVERY / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P13 | P14选择版本固定实际调用链并应用P7五项 | `HoTT后续研究总体方案.md`；P13 report；revision233 receipt |"
    arow = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P13操作合同后的P14实际K发现 | H/R/K、P1–P13 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P13_R_AMBIENT_ACCEPTED / NEXT_P14_AMBIENT_OPERATION_K_DISCOVERY` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P13 | 检查bare H_intrinsic是否实际被当作operation-sensitive Done | `ABX行动.md`；P13 report；revision233 receipt |"
    prow = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P13环境操作敏感R专门化 | `DIR-U-HOTT-FOUR-TRACK` | C-265–C-270/C-275–C-277与公开isotopy术语 | `R_AMBIENT_SPECIALIZATION_ACCEPTED / OPERATION_CLASS_SPLIT_REQUIRED / P14_NEXT` | C-268有限环境操作失败、C-269曲线embedding成功 | 不证明一般不可复原、K或HoTT缺陷 | `audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md`；revision233 receipt |"
    aprow = "| `OUT-ABX-ACTION-INTAKE` | ABX P13环境操作敏感完成合同 | `DIR-U-ABX-ORIGINAL-CIRCLE` | 固定M/N的ambient与curve operation classes | `R_AMBIENT_SPECIALIZATION_ACCEPTED / P14_K_DISCOVERY_NEXT` | future-K必须区分bare H与具体Done | 不证明传统同胚错误、真实K或HoTT缺陷 | `ABX行动.md`；P13 report；revision233 receipt |"
    memory = "P13环境对R_min资格化已完成：C-268只否定有限整平面homeomorphism复原，C-269给出同一M/N的逐时曲线embedding连续变形；因此R_ambient只在明确operation class下是非任意合同，不能推出一般不可复原或一般可复原。当前P14必须从版本固定实际HoTT/立方/相关调用链中寻找是否有人只用bare H_intrinsic却宣称Done_ambient^fin或Done_curve；按P7五项准入，不重跑C-265–C-277。入口：`audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md`；revision233 checkpoint。"
    frontier = "- P13已完成：C-268有限环境homeomorphism失败与C-269曲线embedding成功是不同operation contracts；R_ambient只作为operation-sensitive R_min专门化接受。当前P14选版本固定实际消费者，审计bare H_intrinsic是否越级为Done；不重复几何。入口：`audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md`。"
    resume = "当前 active goal 在P13后继续：P13接受operation-sensitive R_ambient；同一M/N在有限Plane homeomorphism列表下不能复原，在逐时curve embedding下可以变形。P14=AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY：先做公开/本地侦察，选版本固定HoTT/立方/相关实际调用链，用P7五项查bare H_intrinsic是否被当成Done_ambient^fin或Done_curve；不重跑C-265–C-277。入口：`audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md`；revision233 checkpoint。"
    log = "\nS-RES-20260921-ASTRA-P13-AMBIENT-PAIR-RMIN：P13完成。C-268的有限环境homeomorphism反控制与C-269的曲线embedding正控制属于不同operation contracts；R_ambient仅作为operation-sensitive R_min专门化接受。P14开始寻找实际bare-to-Done消费者；revision233 checkpoint。\n"

    files = []
    for rel in list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT)):
        raw = (ROOT / rel).read_bytes()
        text = raw.decode(encoding="utf-8")
        if rel == runtime.STATE:
            text = runtime.dump(state).decode(encoding="utf-8")
        elif rel == runtime.DIRECTION:
            text = repl(repl(repl(text, "source_state_revision: 232", "source_state_revision: 233"), "projection_generation: 20260921-direction-232", "projection_generation: 20260921-direction-233"), "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT")
        elif rel == runtime.PANORAMA:
            text = repl(repl(repl(text, "source_state_revision: 232", "source_state_revision: 233"), "projection_generation: 20260921-outcome-232", "projection_generation: 20260921-outcome-233"), "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            text = row(row(text, "| `DIR-U-HOTT-FOUR-TRACK` |", drow), "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", arow)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            text = row(row(text, "| `OUT-HOTT-FOUR-TRACK-PLAN` |", prow), "| `OUT-ABX-ACTION-INTAKE` |", aprow)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            text = row(text, "P12第三次successor discovery已完成：", memory)
        elif rel == "MEMORY/003 - 当前验证状态与顺序日志.md":
            text += log
        elif rel == runtime.PREFIX + "FRONTIER.md":
            text = repl(text, "- P12已完成：已有C-265–C-268把内在同胚与固定Plane、环境homeomorphism和有限环境操作分开；它是R_ambient专门化候选，不是K或HoTT结果。当前P13只资格化其Input/Operation/Observation/Done映射，不重跑Lean；若仅同义重述，生成下一不同分母。入口：`audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md`。", frontier)
        elif rel == runtime.PREFIX + "RESUME.md":
            text = repl(text, "当前 active goal 在P12后继续：P12以公开/本地双重侦察选择了C-265–C-268的R_ambient环境对候选。P13=AMBIENT_PAIR_RMIN_REQUALIFICATION：不重跑Lean，固定Plane/嵌入/闭包余集/ambient operation，映射C-266内在同胚、C-267环境homeomorphism、C-268有限环境复原到OriginDirectedDiagram的Input/Operation/Observation/Done；只输出R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE或RESTATEMENT_ONLY，然后仍按active-goal生成后继。入口：`audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md`；revision232 checkpoint。", resume)
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": text})
    for name, text in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode(encoding="utf-8")), ("CORE_COGNITION_AUDIT.md", audit(state["current_core"]))):
        files.append({"path": BASE + name, "expected_sha256": None, "text": text})
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN_ID],
        "authorization": "用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。",
        "files": files,
    }
    (OUT / "P13-AMBIENT-PAIR-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P13-AMBIENT-PAIR-checkpoint-apply.json" if args.apply else "P13-AMBIENT-PAIR-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
