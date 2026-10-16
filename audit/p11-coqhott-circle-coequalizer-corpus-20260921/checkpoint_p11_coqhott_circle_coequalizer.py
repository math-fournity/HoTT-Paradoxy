#!/usr/bin/env python3
"""Checkpoint the bounded Coq-HoTT Circle/Coeq P11 source audit."""
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
SID = "S-RES-20260921-ASTRA-P11-COQHOTT-CIRCLE-COEQUALIZER"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN_ID = "R-HOTT-FOUR-TRACK-PLAN-20260921"
ABX_ID = "R-ABX-ACTION-20260921"
PREVIOUS_IDS = (
    "R-P1-RMIN-SPEC-20260921", "R-P2-KTHEORY-SIP-20260921", "R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921",
    "R-P5-SUCCESSOR-DISCOVERY-20260921", "R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921",
    "R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921", "R-P8-RZK-DIRECTED-IMPLEMENTATION-20260921",
    "R-P9-SHOTT-DIRUNIV-CORPUS-20260921", "R-P10-SECOND-SUCCESSOR-DISCOVERY-20260921",
)
P11_ID = "R-P11-COQHOTT-CIRCLE-COEQUALIZER-20260921"
REPORT = "audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md"
AUDIT = "audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-SOURCE-AUDIT.json"
VERIFY = "audit/p11-coqhott-circle-coequalizer-corpus-20260921/verify_p11_coqhott_circle_coequalizer.py"
RECEIPT = "audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-VERIFICATION.json"
CHECKPOINT = "audit/p11-coqhott-circle-coequalizer-corpus-20260921/checkpoint_p11_coqhott_circle_coequalizer.py"
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
PLAN = "HoTT后续研究总体方案.md"
PLAN_SHARDS = tuple("HoTT后续研究总体方案/" + n for n in (
    "001 - 上一轮问答与四分支校正.md", "002 - 共同任务、术语与优先级原则.md",
    "003 - 分支顺序、准入与停止条件.md", "004 - 令牌经济、反漂移与每单元复核.md", "005 - 当前第一步与交接.md"))
P11_SOURCES = (
    REPORT, AUDIT, VERIFY, RECEIPT, CHECKPOINT, PLAN_VERIFY, PLAN_RECEIPT, PLAN, *PLAN_SHARDS,
    "goal.md", "goal-3.md", "feature-list.md", "rulings.md", "ABX行动.md", "ABX行动/005 - 状态、停止条件与未来交接.md",
    "audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md",
    "audit/p10-second-successor-discovery-20260921/P10-COQHOTT-CANDIDATE-FREEZE.json",
    "audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-VERIFICATION.json",
    "audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md",
    "HoTT/formal/astra-s1-consumer-check/SC00.agda",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repl(text: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, text, count=1)
    assert count == 1, old
    return result


def row(text: str, prefix: str, value: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            lines[i] = value
            return "\n".join(lines) + "\n"
    raise AssertionError(prefix)


def audit(core: dict[str, object]) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.M)
    assert len(headings) == core["kc_count"] == 46
    touched = {10, 14, 15, 19, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    result = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P11_COQHOTT_GLUING_DEFENSE_P12_THIRD_SUCCESSOR_DISCOVERY_NEXT
- panorama_change: NONDIRECTED_HOTT_SOURCE_EXPLICIT_GLUING_DEFENSE_WITH_ADMITTED_BOUNDARY
- essay_change: NO
- update_decision: P11 closes the five-file Coq-HoTT Circle/Coeq source denominator as task-distinct explicit gluing, while retaining its visible admitted boundary as neither a K nor P4 evidence.
- cross_conflicts: source-level explicit structure and an admitted dependency are distinct evidence types; neither establishes a HoTT defect.
- unresolved: actual K, a rule bridge, independently stronger R/Done and a reproducible theory–implementation discrepancy remain open.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for ordinal, (kc, topic) in enumerate(headings, 1):
        if ordinal in touched:
            relation = "DEEPENED"
            assessment = "P11 在非定向实际HoTT source中检查粘合/消去；maps、cglue、loop coherence与Torus结构显式出现，未把synthetic Circle当作原来源—复原任务。"
            evidence = f"{REPORT}；P12若定位不同规则、消费者、R/Done或实现差异才改变该范围。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本单元只审计固定 Coq-HoTT 五文件的K准入与信任边界。"
            evidence = "goal.md §2；无新数学定理或HoTT缺陷结论。"
        result += f"| `{kc}` | {topic} | {relation} | {assessment} | {evidence} |\n"
    return result + """

## 扩展认知逐片复认

001–008：P11 用实际 source 解释“端点识别”：它是明确的构造子、路径与coherence合同，而非把无法完成的逼近当成已完成。可见的`Admitted`保持为信任边界，不能被夸大为数学或实现失败。

## 波次定位

1. **最终目标连接：** P11 检验 P3 实际消费者链中的非定向粘合/闭合构造。
2. **全局坐标：** P10选择Coq-HoTT五文件；P11用P7五项关闭该分母；P12重新生成未覆盖入口。
3. **实际价值：** 新增外部library的explicit glue/coherence defense与显式Admitted trust boundary两类可定位事实。
4. **继续检验：** P12必须改变候选类，不能增加同一Circle/Coeq caller或关键词。
5. **不延续的理由：** P11的K-input/K-claim/K-forgetting均已有直接source事实；全库扩展不会成为同一分母的新判别。
6. **裁决：** `SWITCH_BRANCH`，进入P12 discovery；P11不产生K或数学结论。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    subprocess.check_call([sys.executable, "-B", PLAN_VERIFY, "--write"], cwd=ROOT)
    for source in P11_SOURCES:
        assert (ROOT / source).is_file(), source
    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 230 and state["latest_session"] == "S-RES-20260921-ASTRA-P10-SECOND-SUCCESSOR-DISCOVERY"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha(ROOT / p) == h for p, h in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID])
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P11-COQHOTT-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    assert json.loads((ROOT / RECEIPT).read_text(encoding="utf-8"))["status"] == "PASS_WITH_SCOPE"
    assert json.loads((ROOT / PLAN_RECEIPT).read_text(encoding="utf-8"))["status"] == "PASS_WITH_SCOPE"

    previous = state["latest_session"]
    state["revision"] = 231
    state["latest_session"] = SID
    for ident in (*PREVIOUS_IDS, PLAN_ID, ABX_ID):
        record = state["records"][ident]
        record["related_records"] = list(dict.fromkeys(record.get("related_records", []) + [P11_ID, SID]))
        paths = set(record.get("full_sources", [])) | set(record.get("source_hashes", {}))
        record["source_hashes"].update({p: sha(ROOT / p) for p in paths if (ROOT / p).is_file()})
        record["revalidation"] = record.get("revalidation", "") + " Revision231 records P11's explicit Coq-HoTT gluing defense; prior scope unchanged."

    p = state["records"][PLAN_ID]
    p["evidence_status"] = "USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_DEFENSE / P10_COQHOTT_CANDIDATE_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_THIRD_SUCCESSOR_DISCOVERY_NEXT / GOAL_ACTIVE"
    p["status"] = "four_track_first_pass_p5_p6_p7_p8_p9_complete_p10_selected_p11_gluing_defense_p12_next"
    p["full_sources"] = list(dict.fromkeys(p.get("full_sources", []) + list(P11_SOURCES)))
    p["related_records"] = list(dict.fromkeys(p.get("related_records", []) + [P11_ID, SID]))
    paths = set(p["full_sources"]) | set(p.get("source_hashes", {}))
    p["source_hashes"].update({x: sha(ROOT / x) for x in paths if (ROOT / x).is_file()})
    p["revalidation"] = "Revision231 completes P11: Coq-HoTT Circle/Coeq/Torus five-file source has explicit glue/coherence and no original Done_s claim; its Admitted torus lemma is a declared trust boundary only. P12 is required discovery."
    p["scope"] = "P11 is a five-file source audit, not a Coq-HoTT build/replay, global library audit, K, theory–implementation difference or HoTT defect. P12 must select a non-overlapping candidate class."

    abx = state["records"][ABX_ID]
    abx["full_sources"] = list(dict.fromkeys(abx.get("full_sources", []) + list(P11_SOURCES)))
    paths = set(abx["full_sources"]) | set(abx.get("source_hashes", {}))
    abx["source_hashes"].update({x: sha(ROOT / x) for x in paths if (ROOT / x).is_file()})
    abx["revalidation"] = "Revision231 Coq-HoTT Circle/Coeq source is an explicit gluing/coherence defense, while Torus Admitted remains a source-level trust boundary. P12 must use an unreviewed candidate class."
    abx["scope"] = "P11 found no K in Coq-HoTT's fixed Circle/Coeq/Torus five-file source. It does not establish whole-library absence, build status or a HoTT defect."

    state["records"][P11_ID] = {
        "kind": "result", "path": REPORT, "lifecycle_status": "CURRENT",
        "evidence_status": "NOT_A_CONSUMER / DEFENSE_EXPLICIT_GLUING_AND_COHERENCE / EXPLICIT_ADMITTED_TORUS_BOUNDARY / P12_THIRD_SUCCESSOR_DISCOVERY_REQUIRED / NO_NEW_MATHEMATICAL_CLAIM",
        "status": "complete_with_scope_p12_third_successor_discovery_next", "depends_on": [],
        "related_records": [PLAN_ID, ABX_ID, *PREVIOUS_IDS, previous],
        "full_sources": list(dict.fromkeys(P11_SOURCES)),
        "source_hashes": {x: sha(ROOT / x) for x in dict.fromkeys(P11_SOURCES)},
        "scope": "P11 audits only Coq-HoTT e3deab71 README/Coeq/Circle/Torus/TorusEquivCircles. It finds explicit glue/coherence inputs and no original Done_s call. It does not compile source, verify Admitted, establish K or a HoTT defect.",
    }
    state["records"][SID] = {"kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL", "evidence_status": "P11_COQHOTT_CIRCLE_COEQUALIZER_AUDIT_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope", "depends_on": [], "related_records": [P11_ID, PLAN_ID, ABX_ID, previous], "full_sources": [BASE + x for x in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")]}
    state["execution_control"].update(
        status="FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_NEXT",
        current_phase="PHASE_2_P11_COQHOTT_GLUING_DEFENSE_P12_THIRD_SUCCESSOR_DISCOVERY_NEXT",
        second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_NEXT",
        last_checkpoint_session=SID, checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json",
        next_minimal_verification="P12-THIRD-SUCCESSOR-DISCOVERY-001. Do public/community plus local/historical reconnaissance across unreviewed rules, non-Circle/Coeq non-directed actual consumers, independently stronger R/Done and theory-implementation differences; select exactly one uncovered denominator. Do not extend the Rzk/sHoTT or Coq-HoTT Circle/Coeq clusters.",
    )
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_COQHOTT_GLUING_DEFENSE / NEXT_P12_THIRD_SUCCESSOR_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for version-pinned Coq-HoTT source audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: apply P7 K-admission harness to the Coq-HoTT Circle/Coeq/Torus candidate
- load_receipt: `audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / NOT_A_CONSUMER / DEFENSE_EXPLICIT_GLUING_AND_COHERENCE / P12_NEXT

The fixed source makes the coequalizer maps, glue paths, circle loop coherence and torus base/loop/surface explicit. It does not consume the original bare presentation or claim the original Done_s. `Torus_rec_beta_surf` is source-level Admitted and is recorded as a trust boundary, not an implementation discrepancy or mathematical defect.

| element | use | effect on this unit |
|---|---|---|
| fixed Coq-HoTT five-file source | used | tests a non-directed external HoTT library denominator |
| P7 admission harness | used | distinguishes explicit synthetic gluing from a bare-to-Done_s task bridge |
| `Admitted` source review | used | preserves an explicit trust boundary without overstating it as a kernel result |
| Coq compiler | not run | no build, kernel replay or semantic implementation conclusion |
"""
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID, "primary_runs": [{"kind": "p11-source-audit-and-k-admission-verification", "command": "version-pinned Coq-HoTT clone/source read; lexical boundary check; P7 five-condition audit; local P1–P11 and plan verifiers", "result": "PASS_WITH_SCOPE; explicit gluing/coherence defense, no K; Admitted trust boundary recorded", "mathematics": "NOT_A_NEW_KERNEL_RUN"}], "new_math_claims": [], "new_kernel_replay": False, "scope": "P11 fixed five-file external source audit only."}
    drow = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P11 Coq-HoTT gluing防御与P12第三后继发现 | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_COQHOTT_GLUING_DEFENSE / NEXT_P12_THIRD_SUCCESSOR_DISCOVERY / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P11 | P12在四类未覆盖入口选一个新分母，不延长已审簇 | `HoTT后续研究总体方案.md`；P11 report；revision231 receipt |"
    arow = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P11 Coq-HoTT gluing防御后的P12发现 | H/R/K、P1–P11 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P11_GLUING_DEFENSE / NEXT_P12_THIRD_SUCCESSOR_DISCOVERY` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P11 | 比较未审规则、非Circle/Coeq消费者、更强R/Done、实现差异 | `ABX行动.md`；P11 report；revision231 receipt |"
    prow = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P11 Coq-HoTT Circle/Coeq source audit | `DIR-U-HOTT-FOUR-TRACK` | Coq-HoTT@e3deab71 README、Coeq、Circle、Torus、TorusEquivCircles | `NOT_A_CONSUMER / DEFENSE_EXPLICIT_GLUING_AND_COHERENCE / P12_NEXT` | maps/glue/coherence/base/loop/surface显式；Torus Admitted为信任边界 | 不证明构建、Admitted真伪、K或HoTT缺陷 | `audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md`；revision231 receipt |"
    aprow = "| `OUT-ABX-ACTION-INTAKE` | ABX P11 Coq-HoTT Circle/Coeq五文件 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P7五项判别、Coq-HoTT@e3deab71 | `NOT_A_CONSUMER / P12_THIRD_SUCCESSOR_DISCOVERY_NEXT` | explicit glue/coherence防御；Admitted不等于P4 | 不证明全库、K或HoTT缺陷 | `ABX行动.md`；P11 report；revision231 receipt |"
    memory = "P11 Coq-HoTT Circle/Coeq五文件审计已完成：Coeq maps/cglue、Circle loop coherence和Torus base/loops/surface均显式，未有原U_bare→Done_s或同任务声明，判NOT_A_CONSUMER/DEFENSE。Torus的Admitted仅登记信任边界。当前P12必须离开Rzk/sHoTT与Circle/Coeq簇，在四类未覆盖入口重新选择。入口：`audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md`；revision231 checkpoint。"
    frontier = "- P11 Coq-HoTT@e3deab71已完成：Circle/Coeq/Torus显式保留maps/glue/coherence/base/loop/surface，无原Done_s调用，非K；Torus Admitted只是信任边界。当前P12重新在未审规则、非Circle/Coeq消费者、更强R/Done或可重放实现差异中选一个分母，不延长已审簇。入口：`audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md`。"
    resume = "当前 active goal 在P11后继续：Coq-HoTT@e3deab71 Circle/Coeq/Torus五文件是显式glue/coherence防御，非K；Torus Admitted保持信任边界。P12=THIRD_SUCCESSOR_DISCOVERY：先做公开/本地资产侦察，比较未审规则、非Circle/Coeq非directed消费者、独立更强R/Done与理论—实现差异，选定一个不被P1–P11覆盖的分母。入口：`audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md`；revision231 checkpoint。"
    log = "\nS-RES-20260921-ASTRA-P11-COQHOTT-CIRCLE-COEQUALIZER：P11完成。Coq-HoTT@e3deab71五文件显式保留Coeq maps/cglue、Circle loop coherence与Torus结构，无原Done_s，判NOT_A_CONSUMER/DEFENSE；Torus Admitted仅为信任边界。P12重新比较四类未覆盖入口；revision231 checkpoint。\n"

    files = []
    for rel in list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT)):
        raw = (ROOT / rel).read_bytes(); text = raw.decode(encoding="utf-8")
        if rel == runtime.STATE: text = runtime.dump(state).decode(encoding="utf-8")
        elif rel == runtime.DIRECTION:
            text = repl(repl(repl(text, "source_state_revision: 230", "source_state_revision: 231"), "projection_generation: 20260921-direction-230", "projection_generation: 20260921-direction-231"), "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_COQHOTT_CANDIDATE_SELECTED_P11_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_NEXT")
        elif rel == runtime.PANORAMA:
            text = repl(repl(repl(text, "source_state_revision: 230", "source_state_revision: 231"), "projection_generation: 20260921-outcome-230", "projection_generation: 20260921-outcome-231"), "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_COQHOTT_CANDIDATE_SELECTED_P11_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_NEXT")
        elif rel == "方向追踪/002 - 治理与用户方向.md": text = row(row(text, "| `DIR-U-HOTT-FOUR-TRACK` |", drow), "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", arow)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md": text = row(row(text, "| `OUT-HOTT-FOUR-TRACK-PLAN` |", prow), "| `OUT-ABX-ACTION-INTAKE` |", aprow)
        elif rel == "MEMORY/001 - 当前执行队列.md": text = row(text, "P10 第二后继发现已完成：", memory)
        elif rel == "MEMORY/003 - 当前验证状态与顺序日志.md": text += log
        elif rel == runtime.PREFIX + "FRONTIER.md": text = repl(text, "- P10已完成：Coq-HoTT@e3deab71 Circle/Coeq/Torus 是离开directed簇后选定的非定向source candidate；它显式涉及glue/coherence但未被判为K。当前P11仅审计固定五文件的K-input/K-output/K-claim/K-forgetting/K-version；不编译或扫描全库。入口：`audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md`。", frontier)
        elif rel == runtime.PREFIX + "RESUME.md": text = repl(text, "当前 active goal 在P10后继续：P10比较四类入口并选择Coq-HoTT@e3deab71 Circle/Coeq/Torus五文件，作为非directed P3 candidate。P11=COQHOTT_CIRCLE_COEQUALIZER_CORPUS：冻结实际输入/输出/调用链，按P7五项检查是否只显式保存glue/coherence，或真有U_bare→原Done_s承诺；不把synthetic Circle名称当原圆环完成。入口：`audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md`；revision230 checkpoint。", resume)
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": text})
    for name, text in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode(encoding="utf-8")), ("CORE_COGNITION_AUDIT.md", audit(state["current_core"]))): files.append({"path": BASE + name, "expected_sha256": None, "text": text})
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN_ID], "authorization": "用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。", "files": files}
    (OUT / "P11-COQHOTT-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P11-COQHOTT-checkpoint-apply.json" if args.apply else "P11-COQHOTT-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({k: v for k, v in result.items() if k != "paths"}, ensure_ascii=False))


if __name__ == "__main__": main()
