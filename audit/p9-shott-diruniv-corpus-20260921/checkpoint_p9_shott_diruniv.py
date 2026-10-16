#!/usr/bin/env python3
"""Checkpoint the bounded sHoTT diruniv audit and select P10 discovery."""
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
SID = "S-RES-20260921-ASTRA-P9-SHOTT-DIRUNIV-CORPUS"
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
)
P9_ID = "R-P9-SHOTT-DIRUNIV-CORPUS-20260921"

REPORT = "audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md"
FREEZE = "audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-SOURCE-FREEZE.json"
VERIFY = "audit/p9-shott-diruniv-corpus-20260921/verify_p9_shott_diruniv_corpus.py"
RECEIPT = "audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-VERIFICATION.json"
CHECKPOINT = "audit/p9-shott-diruniv-corpus-20260921/checkpoint_p9_shott_diruniv.py"
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
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
VERIFIERS = (
    "audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py",
    "audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py",
    "audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py",
    "audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py",
    "audit/p6-origin-structure-stratified-20260921/verify_p6_origin_structure_stratified.py",
    "audit/p7-origin-directed-diagram-spec-20260921/verify_p7_origin_directed_diagram_spec.py",
    "audit/p8-directed-type-theory-implementation-discovery-20260921/verify_p8_directed_type_theory_implementation.py",
    VERIFY,
    PLAN_VERIFY,
)
PRIOR_RECEIPTS = (
    "audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md",
    "audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json",
    "audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md",
    "audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json",
    "audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md",
    "audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json",
    "audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md",
    "audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json",
    "audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md",
    "audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-VERIFICATION.json",
    "audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md",
    "audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-VERIFICATION.json",
    "audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md",
    "audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-VERIFICATION.json",
)
P9_SOURCES = (
    REPORT,
    FREEZE,
    VERIFY,
    RECEIPT,
    CHECKPOINT,
    *VERIFIERS,
    *PRIOR_RECEIPTS,
    PLAN,
    *PLAN_SHARDS,
    PLAN_RECEIPT,
    "goal.md",
    "goal-3.md",
    "feature-list.md",
    "rulings.md",
    "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    updated, count = re.subn(re.escape(old), new, text, count=1)
    assert count == 1, old
    return updated


def replace_row(text: str, prefix: str, value: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = value
            return "\n".join(lines) + "\n"
    raise AssertionError(prefix)


def core_audit(core: dict[str, object]) -> str:
    headings = re.findall(
        r"^### (KC-\d+) · .*? · (.+)$",
        (ROOT / "核心认知.md").read_text(encoding="utf-8"),
        re.M,
    )
    assert len(headings) == core["kc_count"] == 46
    touched = {10, 14, 15, 19, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    result = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P9_SHOTT_DIRUNIV_DEFENSE_P10_SECOND_SUCCESSOR_DISCOVERY_NEXT
- panorama_change: VERSION_PINNED_DIRECTED_UNIVALENCE_CORPUS_NOT_A_CONSUMER
- essay_change: NO
- update_decision: P9 fixes an actual directed-univalence formalisation corpus, whose covariant and endpoint inputs remain explicit; P10 leaves this directed cluster.
- cross_conflicts: the result supports neither a free bare-topological completion nor a global defense; it closes only this exact source denominator.
- unresolved: an actual K, a rule-level bridge, a stronger independently grounded R/Done, and a reproducible theory–implementation discrepancy remain open.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for ordinal, (kc_id, topic) in enumerate(headings, 1):
        if ordinal in touched:
            relation = "DEEPENED"
            assessment = "P9 在实际 directed-univalence 形式化语料中检查 P7 五项条件；协变资格、端点、函数、transport 与部分假设仍显式保留，未出现 bare 输入到强完成的越级。"
            evidence = f"{REPORT}；只有P10定位不同理论构造、消费者、规格或实现差异才改变此范围判词。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本单元只审计固定 sHoTT diruniv 语料的输入、输出、承诺与忘却边界。"
            evidence = "goal.md §2；无新数学定理或HoTT缺陷结论。"
        result += f"| `{kc_id}` | {topic} | {relation} | {assessment} | {evidence} |\n"
    return result + """

## 扩展认知逐片复认

001–008：P9 将现实对齐落实为一个可审计的输入/操作/完成检查，而不是把定向类型或公设名称直接判为现实性结论。P10必须离开同一 directed/simplicial 防御簇，并重新固定新分母。

## 波次定位

1. **最终目标连接：** P9 检验 P3 实际消费者见证链中的输入—忘却—强完成边。
2. **全局坐标：** P5 生成 P6；P6/P7 固定对象与 K 准入；P8 是语言/实现层防御；P9 是关联的实际 directed-univalence corpus 防御；P10 回到四类剩余入口。
3. **实际价值：** 新增可定位事实是 `S = Σ(A:U), is-a-cov A`、`𝕀→S` 和 `dirglue(A,B,f)` 的实际代码依赖，排除了“只因 directed univalence 便自动完成原圆环任务”的推断。
4. **继续检验：** 在同一 P9 branch 内继续只会扩大相邻关键词，不能改变 K-input/K-claim；P10必须改变理论构造、消费者分母、R/Done规格或实现语义。
5. **不延续的理由：** 固定 entry 的 K-input、K-claim 与 K-forgetting 已有直接反证；本分母结束，不结束 active goal。
6. **裁决：** `SWITCH_BRANCH`，进入 `P10-SECOND-SUCCESSOR-DISCOVERY-001`。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    for verifier in VERIFIERS:
        subprocess.check_call([sys.executable, "-B", verifier, "--write"], cwd=ROOT)
    for source in P9_SOURCES:
        assert (ROOT / source).is_file(), source

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)

    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 228
    assert state["latest_session"] == "S-RES-20260921-ASTRA-P8-RZK-DIRECTED-IMPLEMENTATION"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha(ROOT / path) == expected for path, expected in head["tracked"].items())

    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID])
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P9-SHOTT-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    for receipt in (*PRIOR_RECEIPTS, PLAN_RECEIPT, RECEIPT):
        if receipt.endswith(".json"):
            assert json.loads((ROOT / receipt).read_text(encoding="utf-8"))["status"] == "PASS_WITH_SCOPE"

    previous_session = state["latest_session"]
    state["revision"] = 229
    state["latest_session"] = SID
    for record_id in (*PREVIOUS_IDS, PLAN_ID, ABX_ID):
        record = state["records"][record_id]
        record["related_records"] = list(dict.fromkeys(record.get("related_records", []) + [P9_ID, SID]))
        paths = set(record.get("full_sources", [])) | set(record.get("source_hashes", {}))
        record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
        record["revalidation"] = record.get("revalidation", "") + " Revision229 records the bounded sHoTT diruniv defense; prior scope unchanged."

    plan_record = state["records"][PLAN_ID]
    plan_record["evidence_status"] = (
        "USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / "
        "P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / "
        "P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / "
        "P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_DEFENSE / P10_SECOND_SUCCESSOR_DISCOVERY_NEXT / GOAL_ACTIVE"
    )
    plan_record["status"] = "four_track_first_pass_p5_p6_p7_p8_p9_complete_p10_second_successor_discovery_next"
    plan_record["full_sources"] = list(dict.fromkeys(plan_record.get("full_sources", []) + list(P9_SOURCES)))
    plan_record["related_records"] = list(dict.fromkeys(plan_record.get("related_records", []) + [P9_ID, SID]))
    paths = set(plan_record["full_sources"]) | set(plan_record.get("source_hashes", {}))
    plan_record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    plan_record["revalidation"] = "Revision229 completes P9: sHoTT diruniv retains explicit covariant/modal structure and no OriginDirectedDiagram U_bare to Done_s call within the fixed corpus scope. P10 selects an independent second successor discovery."
    plan_record["scope"] = "P9 is a version-pinned sHoTT diruniv source audit. It does not audit all sHoTT, build/typecheck sHoTT, prove its metatheory, find K, or prove a HoTT defect."

    abx_record = state["records"][ABX_ID]
    abx_record["full_sources"] = list(dict.fromkeys(abx_record.get("full_sources", []) + list(P9_SOURCES)))
    paths = set(abx_record["full_sources"]) | set(abx_record.get("source_hashes", {}))
    abx_record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    abx_record["revalidation"] = "Revision229 sHoTT diruniv is an explicit covariant/modal-structure defense, not K. P10 must seek a non-directed new denominator."
    abx_record["scope"] = "P9 found no K in the frozen sHoTT diruniv corpus scope; P10 separately discovers a non-overlapping candidate class."

    state["records"][P9_ID] = {
        "kind": "result",
        "path": REPORT,
        "lifecycle_status": "CURRENT",
        "evidence_status": "NOT_A_CONSUMER / DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE / P10_SECOND_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_MATHEMATICAL_CLAIM",
        "status": "complete_with_scope_p10_second_successor_discovery_next",
        "depends_on": [],
        "related_records": [PLAN_ID, ABX_ID, *PREVIOUS_IDS, previous_session],
        "full_sources": list(dict.fromkeys(P9_SOURCES)),
        "source_hashes": {path: sha(ROOT / path) for path in dict.fromkeys(P9_SOURCES)},
        "scope": "P9 freezes LIshy2/sHoTT diruniv commit e76c196 and seven selected source files. It identifies explicit covariant/modal/endpoint inputs and no P7 K output/claim within that scope. It is not a whole-branch audit, typecheck replay, K, or HoTT defect.",
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P9_SHOTT_DIRUNIV_CORPUS_AUDIT_CHECKPOINTED_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [P9_ID, PLAN_ID, ABX_ID, previous_session],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_NEXT",
        current_phase="PHASE_2_P9_SHOTT_DIRUNIV_DEFENSE_P10_SECOND_SUCCESSOR_DISCOVERY_NEXT",
        second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_P9_COMPLETE_P10_NEXT",
        last_checkpoint_session=SID,
        checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json",
        next_minimal_verification=(
            "P10-SECOND-SUCCESSOR-DISCOVERY-001. Do public/community plus local/historical reconnaissance "
            "across remaining rules, non-directed actual consumers, stronger R/Done and theory-implementation "
            "differences; choose exactly one new uncovered denominator. Do not extend the Rzk/sHoTT directed cluster."
        ),
    )
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_P9_COMPLETE / NEXT_P10_SECOND_SUCCESSOR_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for version-pinned sHoTT directed-univalence corpus audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: apply P7 K-admission harness to Rzk-linked sHoTT diruniv formalisation
- load_receipt: `audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-CHECKPOINT-PLAN.json`; compression receipt reattested against revision228 `HEAD.json` tracked hashes, P8 46-KC audit, and core source excerpt.
- status: COMPLETED_WITH_SCOPE / NOT_A_CONSUMER / DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE / P10_NEXT

sHoTT@e76c196 is a pinned actual formalisation corpus, distinct from the P8 Rzk implementation denominator. Its selected code retains `is-a-cov`, directed interval, endpoints, functions, transport, assumptions and nearby postulates as explicit inputs or dependencies. It does not give a P7 bare-input-to-`Done_s` commitment. P10 must leave the directed/simplicial cluster.

| element | use | effect on this unit |
|---|---|---|
| P7 admission harness | used | rejects a theorem title or directed-univalence primitive as a K claim |
| source pin + selected blob hashes | used | fixes branch, commit and exact source denominator |
| P8/Rzk provenance | used | separates the corpus audit from the language-runtime audit |
| sHoTT typechecker | not run | source audit does not certify compilation or metatheory |
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {
                "kind": "p9-source-freeze-and-k-admission-verification",
                "command": "git ls-remote LIshy2/sHoTT diruniv; detached shallow clone; selected-source hash/lexical checks; local P1–P9 and plan verifiers",
                "result": "PASS_WITH_SCOPE; frozen diruniv corpus retains explicit covariant/modal inputs and is not K",
                "mathematics": "NOT_A_NEW_KERNEL_RUN",
            }
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "scope": "P9 version-pinned external source audit only.",
    }
    direction_row = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P9 sHoTT防御与P10第二后继发现 | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_P8_P9_COMPLETE / NEXT_P10_SECOND_SUCCESSOR_DISCOVERY / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P9 | P10在四类剩余入口选一个不重复分母；不延长directed/simplicial簇 | `HoTT后续研究总体方案.md`；P9 report；revision229 receipt |"
    abx_direction_row = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P9 sHoTT防御后的P10第二后继发现 | H/R/K、P1–P9 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P9_SHOTT_DIRUNIV_DEFENSE / NEXT_P10_SECOND_SUCCESSOR_DISCOVERY` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P9 | 重新比较规则、非定向消费者、更强R/Done与实现差异 | `ABX行动.md`；P9 report；revision229 receipt |"
    panorama_row = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P9 sHoTT directed-univalence语料审计 | `DIR-U-HOTT-FOUR-TRACK` | sHoTT@e76c196 triangulated diruniv与邻近前提 | `NOT_A_CONSUMER / DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE / P10_NEXT` | `is-a-cov`、端点、函数、transport及部分假设显式保留 | 不证明sHoTT全库、K或HoTT缺陷 | `audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md`；revision229 receipt |"
    abx_panorama_row = "| `OUT-ABX-ACTION-INTAKE` | ABX P9 sHoTT实际形式化语料 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P7五项判别、sHoTT@e76c196七文件 | `NOT_A_CONSUMER / P10_SECOND_SUCCESSOR_DISCOVERY_NEXT` | 显式协变/模态结构防御；不得机械延长directed簇 | 不证明全库无K、K或HoTT缺陷 | `ABX行动.md`；P9 report；revision229 receipt |"
    memory = "P9 sHoTT diruniv语料审计已完成：sHoTT@e76c196的`S = Σ(A:U), is-a-cov A`、`𝕀→S`与`dirglue(A,B,f)`把协变、端点、函数和transport显式保留，未给原圆环U_bare→Done_s，判为NOT_A_CONSUMER/DEFENSE。当前P10必须在规则、非directed消费者、更强R/Done、理论—实现差异四类入口重新选择一个不重复分母。入口：`audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md`；revision229 checkpoint。"
    frontier = "- P9 sHoTT@e76c196已完成：diruniv把协变资格、端点、函数、transport及部分假设显式保留，非K。当前P10做公开与本地/历史双重侦察，在未审规则、非directed实际消费者、更强R/Done或可重放理论—实现差异中只选一个新分母；不延长Rzk/sHoTT directed簇。入口：`audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md`。"
    resume = "当前 active goal 在P9后继续：sHoTT@e76c196固定diruniv语料是显式协变/模态结构防御，非K。P10=SECOND_SUCCESSOR_DISCOVERY：先做公开/本地资产侦察，重新比较未审规则、非directed消费者、独立更强R/Done与理论—实现语义差异，选定一个不被P1–P9覆盖的分母；不得继续Rzk/sHoTT directed簇。入口：`audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md`；revision229 checkpoint。"
    log = "\nS-RES-20260921-ASTRA-P9-SHOTT-DIRUNIV-CORPUS：P9完成。sHoTT@e76c196 diruniv显式保留is-a-cov、directed interval、端点、函数、transport、assume/postulate，无原圆环U_bare→Done_s，判NOT_A_CONSUMER/DEFENSE。P10重新比较规则、非directed消费者、更强R/Done与理论—实现差异四类入口；revision229 checkpoint。\n"

    files = []
    for relative_path in list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT)):
        raw = (ROOT / relative_path).read_bytes()
        text = raw.decode(encoding="utf-8")
        if relative_path == runtime.STATE:
            text = runtime.dump(state).decode(encoding="utf-8")
        elif relative_path == runtime.DIRECTION:
            text = replace_once(text, "source_state_revision: 228", "source_state_revision: 229")
            text = replace_once(text, "projection_generation: 20260921-direction-228", "projection_generation: 20260921-direction-229")
            text = replace_once(text, "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_COMPLETE_P9_SHOTT_DIRUNIV_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SECOND_SUCCESSOR_DISCOVERY_NEXT")
        elif relative_path == runtime.PANORAMA:
            text = replace_once(text, "source_state_revision: 228", "source_state_revision: 229")
            text = replace_once(text, "projection_generation: 20260921-outcome-228", "projection_generation: 20260921-outcome-229")
            text = replace_once(text, "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_COMPLETE_P9_SHOTT_DIRUNIV_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SECOND_SUCCESSOR_DISCOVERY_NEXT")
        elif relative_path == "方向追踪/002 - 治理与用户方向.md":
            text = replace_row(text, "| `DIR-U-HOTT-FOUR-TRACK` |", direction_row)
            text = replace_row(text, "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", abx_direction_row)
        elif relative_path == "全景视野/003 - 当前机器证明包与原生重放.md":
            text = replace_row(text, "| `OUT-HOTT-FOUR-TRACK-PLAN` |", panorama_row)
            text = replace_row(text, "| `OUT-ABX-ACTION-INTAKE` |", abx_panorama_row)
        elif relative_path == "MEMORY/001 - 当前执行队列.md":
            text = replace_row(text, "P8 Rzk 实现审计已完成：", memory)
        elif relative_path == "MEMORY/003 - 当前验证状态与顺序日志.md":
            text += log
        elif relative_path == runtime.PREFIX + "FRONTIER.md":
            text = replace_once(
                text,
                "- P8 Rzk@01b081e 已完成：显式direction/source/target/shape是防御，无原圆环Done承诺。当前P9固定sHoTT diruniv corpus，分离modal/postulate/formalisation与实际K，并逐项跑P7五条件。入口：`audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md`。",
                frontier,
            )
        elif relative_path == runtime.PREFIX + "RESUME.md":
            text = replace_once(
                text,
                "当前 active goal 在P8后继续：Rzk@01b081e固定六文件是显式有向输入防御，非K。P9=SHOTT_DIRUNIV_CORPUS_DENOMINATOR：冻结LIshy2/sHoTT diruniv branch/commit/entry/imports，分离modal/postulate/formalisation，然后以P7五项条件检查实际K。入口：`audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md`；revision228 checkpoint。",
                resume,
            )
        files.append({"path": relative_path, "expected_sha256": runtime.sha(raw), "text": text})
    for name, text in (
        ("SESSION.md", session),
        ("RUNS.json", runtime.dump(runs).decode(encoding="utf-8")),
        ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"])),
    ):
        files.append({"path": BASE + name, "expected_sha256": None, "text": text})

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SID,
        "load_profile": "research",
        "task_ids": [PLAN_ID],
        "authorization": "用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。",
        "files": files,
    }
    (OUT / "P9-SHOTT-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    output = OUT / ("P9-SHOTT-checkpoint-apply.json" if args.apply else "P9-SHOTT-checkpoint-dry-run.json")
    output.write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
