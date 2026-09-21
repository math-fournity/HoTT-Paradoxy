#!/usr/bin/env python3
"""Checkpoint P10's bounded selection of the Coq-HoTT P11 source audit."""
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
SID = "S-RES-20260921-ASTRA-P10-SECOND-SUCCESSOR-DISCOVERY"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN_ID = "R-HOTT-FOUR-TRACK-PLAN-20260921"
ABX_ID = "R-ABX-ACTION-20260921"
PREVIOUS_IDS = (
    "R-P1-RMIN-SPEC-20260921",
    "R-P2-KTHEORY-SIP-20260921",
    "R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921",
    "R-P5-SUCCESSOR-DISCOVERY-20260921",
    "R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921",
    "R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921",
    "R-P8-RZK-DIRECTED-IMPLEMENTATION-20260921",
    "R-P9-SHOTT-DIRUNIV-CORPUS-20260921",
)
P10_ID = "R-P10-SECOND-SUCCESSOR-DISCOVERY-20260921"
REPORT = "audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md"
FREEZE = "audit/p10-second-successor-discovery-20260921/P10-COQHOTT-CANDIDATE-FREEZE.json"
VERIFY = "audit/p10-second-successor-discovery-20260921/verify_p10_second_successor_discovery.py"
RECEIPT = "audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-VERIFICATION.json"
CHECKPOINT = "audit/p10-second-successor-discovery-20260921/checkpoint_p10_second_successor_discovery.py"
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
PLAN = "HoTT后续研究总体方案.md"
PLAN_SHARDS = tuple(
    "HoTT后续研究总体方案/" + name
    for name in (
        "001 - 上一轮问答与四分支校正.md",
        "002 - 共同任务、术语与优先级原则.md",
        "003 - 分支顺序、准入与停止条件.md",
        "004 - 令牌经济、反漂移与每单元复核.md",
        "005 - 当前第一步与交接.md",
    )
)
VERIFIERS = (
    "audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py",
    "audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py",
    "audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py",
    VERIFY,
    PLAN_VERIFY,
)
P10_SOURCES = (
    REPORT,
    FREEZE,
    VERIFY,
    RECEIPT,
    CHECKPOINT,
    *VERIFIERS,
    PLAN,
    *PLAN_SHARDS,
    PLAN_RECEIPT,
    "goal.md",
    "goal-3.md",
    "feature-list.md",
    "rulings.md",
    "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    "audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md",
    "audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-VERIFICATION.json",
    "audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md",
    "HoTT/formal/astra-s1-consumer-check/SC00.agda",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, text, count=1)
    assert count == 1, old
    return result


def replace_row(text: str, prefix: str, value: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = value
            return "\n".join(lines) + "\n"
    raise AssertionError(prefix)


def core_audit(core: dict[str, object]) -> str:
    rows = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.M)
    assert len(rows) == core["kc_count"] == 46
    touched = {10, 14, 15, 19, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    text = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P10_COQHOTT_CANDIDATE_SELECTED_P11_COEQUALIZER_CORPUS_NEXT
- panorama_change: SECOND_SUCCESSOR_DISCOVERY_SELECTS_NON_DIRECTED_HOTT_SOURCE
- essay_change: NO
- update_decision: P10 compares four remaining ingress classes, selects a real Coq-HoTT Circle/Coeq/Torus source denominator, and does not yet adjudicate K.
- cross_conflicts: explicit Coeq glue/coherence is a candidate-source fact, not a proof that it preserves or violates the original source—operation—completion task.
- unresolved: P11 must still test K-input, K-output, K-claim, K-forgetting and K-version against the fixed five-file source chain.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for ordinal, (kc_id, topic) in enumerate(rows, 1):
        if ordinal in touched:
            relation = "DEEPENED"
            assessment = "P10 把现实对齐要求落实为候选分母的输入/粘合/完成审计，选择非定向 Coq-HoTT source，而没有把名称或一点评紧化类比当成圆环命中。"
            evidence = f"{REPORT}；P11若显示真实 U_bare→Done_s 调用或相反的显式数据防御，才改变该选择后的判词。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本单元只比较下一分母入口，不提出新的数学推导或现实结论。"
            evidence = "goal.md §2；无新数学定理或HoTT缺陷结论。"
        text += f"| `{kc_id}` | {topic} | {relation} | {assessment} | {evidence} |\n"
    return text + """

## 扩展认知逐片复认

001–008：P10 贯彻“从现实理解理论”的动作，但把 Coq-HoTT Circle 的 synthetic 构造与点集去点—闭合任务分开。它产生的只是可审计 source candidate；P11 必须让实际输入、操作、观察和完成条件决定结果。

## 波次定位

1. **最终目标连接：** P10 为 P3 实际消费者链选择一个直接涉及粘合/闭合的非定向 HoTT source。
2. **全局坐标：** P8/P9结束定向簇；P10比较规则、消费者、更强规格、实现差异四类入口；P11仅审计 Coq-HoTT 五文件。
3. **实际价值：** 新增 Coq-HoTT 的固定 commit、Circle/Coeq 显式构造与 Torus downstream caller，减少“只有定向扩展付费”的不确定性。
4. **继续检验：** P11将改变 source denominator 的审计深度，而非在 P10 中继续扩充关键词；它会固定 K 的五项输入/输出/声明/忘却/版本判据。
5. **不延续的理由：** P10 是选择任务，四类比较已经完成；再列出更多候选不会提高当前判词。
6. **裁决：** `SWITCH_BRANCH`，进入 P11；P10自身不发现K且不新增数学结论。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    for verifier in VERIFIERS:
        subprocess.check_call([sys.executable, "-B", verifier, "--write"], cwd=ROOT)
    for source in P10_SOURCES:
        assert (ROOT / source).is_file(), source

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 229
    assert state["latest_session"] == "S-RES-20260921-ASTRA-P9-SHOTT-DIRUNIV-CORPUS"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID])
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P10-COQHOTT-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    for receipt in (PLAN_RECEIPT, RECEIPT):
        assert json.loads((ROOT / receipt).read_text(encoding="utf-8"))["status"] == "PASS_WITH_SCOPE"

    previous_session = state["latest_session"]
    state["revision"] = 230
    state["latest_session"] = SID
    for record_id in (*PREVIOUS_IDS, PLAN_ID, ABX_ID):
        record = state["records"][record_id]
        record["related_records"] = list(dict.fromkeys(record.get("related_records", []) + [P10_ID, SID]))
        paths = set(record.get("full_sources", [])) | set(record.get("source_hashes", {}))
        record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
        record["revalidation"] = record.get("revalidation", "") + " Revision230 records P10's bounded non-directed Coq-HoTT candidate selection; prior scope unchanged."

    plan_record = state["records"][PLAN_ID]
    plan_record["evidence_status"] = (
        "USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / "
        "P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / "
        "P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / "
        "P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_DEFENSE / P10_COQHOTT_CANDIDATE_SELECTED / "
        "P11_COQHOTT_CIRCLE_COEQUALIZER_CORPUS_NEXT / GOAL_ACTIVE"
    )
    plan_record["status"] = "four_track_first_pass_p5_p6_p7_p8_p9_complete_p10_coqhott_candidate_selected_p11_next"
    plan_record["full_sources"] = list(dict.fromkeys(plan_record.get("full_sources", []) + list(P10_SOURCES)))
    plan_record["related_records"] = list(dict.fromkeys(plan_record.get("related_records", []) + [P10_ID, SID]))
    paths = set(plan_record["full_sources"]) | set(plan_record.get("source_hashes", {}))
    plan_record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    plan_record["revalidation"] = "Revision230 completes P10: four ingress classes were compared and a pinned non-directed Coq-HoTT Circle/Coeq/Torus corpus was selected for P11. P10 does not find K or a HoTT defect."
    plan_record["scope"] = "P10 is a bounded successor-discovery selection. P11, not P10, audits the frozen Coq-HoTT five-file source chain; neither action audits all Coq-HoTT, replays its build, finds K, or proves a HoTT defect."

    abx_record = state["records"][ABX_ID]
    abx_record["full_sources"] = list(dict.fromkeys(abx_record.get("full_sources", []) + list(P10_SOURCES)))
    paths = set(abx_record["full_sources"]) | set(abx_record.get("source_hashes", {}))
    abx_record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    abx_record["revalidation"] = "Revision230 selects a distinct Coq-HoTT Circle/Coeq/Torus source chain after P8/P9 defenses; P11 must test it by P7 admission before any K claim."
    abx_record["scope"] = "P10 produces a candidate-source selection only; the frozen Coq-HoTT source is not yet K and P11 remains a bounded five-file audit."

    state["records"][P10_ID] = {
        "kind": "candidate_generation",
        "path": REPORT,
        "lifecycle_status": "CURRENT",
        "evidence_status": "SUCCESSOR_SELECTED / COQHOTT_CIRCLE_COEQUALIZER_CORPUS_CANDIDATE / P11_NOT_STARTED / NO_NEW_MATHEMATICAL_CLAIM",
        "status": "complete_with_scope_p11_coqhott_circle_coequalizer_next",
        "depends_on": [],
        "related_records": [PLAN_ID, ABX_ID, *PREVIOUS_IDS, previous_session],
        "full_sources": list(dict.fromkeys(P10_SOURCES)),
        "source_hashes": {path: sha(ROOT / path) for path in dict.fromkeys(P10_SOURCES)},
        "scope": "P10 compares four remaining ingress classes and selects Coq-HoTT master e3deab71 Circle/Coeq/Torus source as P11. It neither audits P11 nor proves a K, source semantics, compilation result or HoTT defect.",
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P10_SECOND_SUCCESSOR_DISCOVERY_CHECKPOINTED_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [P10_ID, PLAN_ID, ABX_ID, previous_session],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_NEXT",
        current_phase="PHASE_2_P10_COQHOTT_CANDIDATE_SELECTED_P11_SOURCE_AUDIT_NEXT",
        second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_NEXT",
        last_checkpoint_session=SID,
        checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json",
        next_minimal_verification=(
            "P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-001. Audit only Coq-HoTT@e3deab71 README, Coeq, Circle, Torus and TorusEquivCircles "
            "under P7 K-input/K-output/K-claim/K-forgetting/K-version; distinguish explicit HIT glue/coherence from the original C,p,M,N,e Done_s task."
        ),
    )
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_P9_COMPLETE / P10_COQHOTT_CANDIDATE_SELECTED / NEXT_P11_COQHOTT_CIRCLE_COEQUALIZER / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for P10 successor discovery and P11 source-audit selection
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: select exactly one non-redundant next denominator after P8/P9 directed defenses
- load_receipt: `audit/p10-second-successor-discovery-20260921/P10-COQHOTT-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / COQHOTT_CIRCLE_COEQUALIZER_CORPUS_CANDIDATE / P11_NEXT

P10 compared an unreviewed rule/model route, non-directed actual consumer route, stronger R/Done route, and theory–implementation discrepancy route. It selected Coq-HoTT@e3deab71 Circle/Coeq/Torus source because the exact code exposes glue/coherence and has a downstream consumer. This is a candidate selection, not a K judgment or source-build replay.

| element | use | effect on this unit |
|---|---|---|
| public Coq-HoTT source + fixed clone | used | establishes a non-directed version-pinned candidate source |
| P7 admission harness | used | prevents Circle/Coeq terminology from being treated as automatic K |
| local C-304 S¹ controls | partial reuse | distinguishes related Cubical mechanism from new Coq-HoTT source/caller |
| Coq-HoTT compiler | not run | selection does not certify build, kernel acceptance or metatheory |
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {
                "kind": "p10-public-local-successor-discovery",
                "command": "bounded public source search; git ls-remote HoTT/Coq-HoTT; detached shallow clone; source identity and local-asset comparison; P1–P10/plan verifiers",
                "result": "PASS_WITH_SCOPE; selected Coq-HoTT Circle/Coeq/Torus candidate for P11 without adjudicating K",
                "mathematics": "NOT_A_NEW_KERNEL_RUN",
            }
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "scope": "P10 successor discovery only.",
    }
    direction_row = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P10 Coq-HoTT候选选择与P11 source audit | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_P8_P9_COMPLETE / P10_COQHOTT_CANDIDATE_SELECTED / NEXT_P11_COQHOTT_CIRCLE_COEQUALIZER / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P10 | P11只审计Coq-HoTT五文件的K五项，不扩展库 | `HoTT后续研究总体方案.md`；P10 report；revision230 receipt |"
    abx_direction_row = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P10 Coq-HoTT候选后的P11五文件source audit | H/R/K、P1–P10 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P10_CANDIDATE_SELECTED / NEXT_P11_COQHOTT_CIRCLE_COEQUALIZER` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P10 | 逐项区分Coeq glue与原Done_s，不把Circle名称当K | `ABX行动.md`；P10 report；revision230 receipt |"
    panorama_row = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P10 第二后继发现：Coq-HoTT Circle/Coeq候选 | `DIR-U-HOTT-FOUR-TRACK` | Coq-HoTT@e3deab71 Circle、Coeq、Torus与TorusEquivCircles | `SUCCESSOR_SELECTED / P11_NOT_STARTED` | 非定向实际HoTT source显式写glue/coherence并有下游consumer | 不证明源码已审、K、HoTT缺陷或理论—实现差异 | `audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md`；revision230 receipt |"
    abx_panorama_row = "| `OUT-ABX-ACTION-INTAKE` | ABX P10 Coq-HoTT Circle/Coeq候选选择 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P10四类入口比较、Coq-HoTT@e3deab71五文件 | `SUCCESSOR_SELECTED / NEXT_P11_COQHOTT_CIRCLE_COEQUALIZER` | 选择非directed source，不预设K；P11固定K五项 | 不证明全库无/有K、K或HoTT缺陷 | `ABX行动.md`；P10 report；revision230 receipt |"
    memory = "P10 第二后继发现已完成：四类入口比较后，Coq-HoTT@e3deab71 的Circle/Coeq/Torus五文件是唯一选定的非directed实际HoTT source candidate；`Circle := Coeq Unit Unit idmap idmap` 和下游Torus consumer显式露出glue/coherence。P10未判K。当前P11只按P7五项审计该五文件，核对其是否有真正U_bare→原Done_s调用。入口：`audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md`；revision230 checkpoint。"
    frontier = "- P10已完成：Coq-HoTT@e3deab71 Circle/Coeq/Torus 是离开directed簇后选定的非定向source candidate；它显式涉及glue/coherence但未被判为K。当前P11仅审计固定五文件的K-input/K-output/K-claim/K-forgetting/K-version；不编译或扫描全库。入口：`audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md`。"
    resume = "当前 active goal 在P10后继续：P10比较四类入口并选择Coq-HoTT@e3deab71 Circle/Coeq/Torus五文件，作为非directed P3 candidate。P11=COQHOTT_CIRCLE_COEQUALIZER_CORPUS：冻结实际输入/输出/调用链，按P7五项检查是否只显式保存glue/coherence，或真有U_bare→原Done_s承诺；不把synthetic Circle名称当原圆环完成。入口：`audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md`；revision230 checkpoint。"
    log = "\nS-RES-20260921-ASTRA-P10-SECOND-SUCCESSOR-DISCOVERY：P10完成。四类剩余入口比较后选定Coq-HoTT@e3deab71 Circle/Coeq/Torus五文件为非directed source candidate；P10不判K。P11将按P7五项审计实际输入、输出、声明、忘却与版本；revision230 checkpoint。\n"

    files = []
    for relative_path in list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT)):
        raw = (ROOT / relative_path).read_bytes()
        text = raw.decode(encoding="utf-8")
        if relative_path == runtime.STATE:
            text = runtime.dump(state).decode(encoding="utf-8")
        elif relative_path == runtime.DIRECTION:
            text = replace_once(text, "source_state_revision: 229", "source_state_revision: 230")
            text = replace_once(text, "projection_generation: 20260921-direction-229", "projection_generation: 20260921-direction-230")
            text = replace_once(text, "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SECOND_SUCCESSOR_DISCOVERY_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_COQHOTT_CANDIDATE_SELECTED_P11_NEXT")
        elif relative_path == runtime.PANORAMA:
            text = replace_once(text, "source_state_revision: 229", "source_state_revision: 230")
            text = replace_once(text, "projection_generation: 20260921-outcome-229", "projection_generation: 20260921-outcome-230")
            text = replace_once(text, "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SECOND_SUCCESSOR_DISCOVERY_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_COQHOTT_CANDIDATE_SELECTED_P11_NEXT")
        elif relative_path == "方向追踪/002 - 治理与用户方向.md":
            text = replace_row(text, "| `DIR-U-HOTT-FOUR-TRACK` |", direction_row)
            text = replace_row(text, "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", abx_direction_row)
        elif relative_path == "全景视野/003 - 当前机器证明包与原生重放.md":
            text = replace_row(text, "| `OUT-HOTT-FOUR-TRACK-PLAN` |", panorama_row)
            text = replace_row(text, "| `OUT-ABX-ACTION-INTAKE` |", abx_panorama_row)
        elif relative_path == "MEMORY/001 - 当前执行队列.md":
            text = replace_row(text, "P9 sHoTT diruniv语料审计已完成：", memory)
        elif relative_path == "MEMORY/003 - 当前验证状态与顺序日志.md":
            text += log
        elif relative_path == runtime.PREFIX + "FRONTIER.md":
            text = replace_once(text, "- P9 sHoTT@e76c196已完成：diruniv把协变资格、端点、函数、transport及部分假设显式保留，非K。当前P10做公开与本地/历史双重侦察，在未审规则、非directed实际消费者、更强R/Done或可重放理论—实现差异中只选一个新分母；不延长Rzk/sHoTT directed簇。入口：`audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md`。", frontier)
        elif relative_path == runtime.PREFIX + "RESUME.md":
            text = replace_once(text, "当前 active goal 在P9后继续：sHoTT@e76c196固定diruniv语料是显式协变/模态结构防御，非K。P10=SECOND_SUCCESSOR_DISCOVERY：先做公开/本地资产侦察，重新比较未审规则、非directed消费者、独立更强R/Done与理论—实现语义差异，选定一个不被P1–P9覆盖的分母；不得继续Rzk/sHoTT directed簇。入口：`audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md`；revision229 checkpoint。", resume)
        files.append({"path": relative_path, "expected_sha256": runtime.sha(raw), "text": text})
    for name, text in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode(encoding="utf-8")), ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"]))):
        files.append({"path": BASE + name, "expected_sha256": None, "text": text})

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SID,
        "load_profile": "research",
        "task_ids": [PLAN_ID],
        "authorization": "用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。",
        "files": files,
    }
    (OUT / "P10-COQHOTT-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    output = OUT / ("P10-COQHOTT-checkpoint-apply.json" if args.apply else "P10-COQHOTT-checkpoint-dry-run.json")
    output.write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
