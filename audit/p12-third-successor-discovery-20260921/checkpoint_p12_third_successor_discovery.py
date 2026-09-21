#!/usr/bin/env python3
"""Checkpoint the P12 ambient-pair successor selection and route P13."""
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
SID = "S-RES-20260921-ASTRA-P12-THIRD-SUCCESSOR-DISCOVERY"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN_ID = "R-HOTT-FOUR-TRACK-PLAN-20260921"
ABX_ID = "R-ABX-ACTION-20260921"
P12_ID = "R-P12-THIRD-SUCCESSOR-DISCOVERY-20260921"
PREVIOUS_IDS = (
    "R-P1-RMIN-SPEC-20260921", "R-P2-KTHEORY-SIP-20260921",
    "R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921", "R-P5-SUCCESSOR-DISCOVERY-20260921",
    "R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921", "R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921",
    "R-P8-RZK-DIRECTED-IMPLEMENTATION-20260921", "R-P9-SHOTT-DIRUNIV-CORPUS-20260921",
    "R-P10-SECOND-SUCCESSOR-DISCOVERY-20260921", "R-P11-COQHOTT-CIRCLE-COEQUALIZER-20260921",
)
REPORT = "audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md"
FREEZE = "audit/p12-third-successor-discovery-20260921/P12-AMBIENT-PAIR-CANDIDATE-FREEZE.json"
VERIFY = "audit/p12-third-successor-discovery-20260921/verify_p12_third_successor_discovery.py"
RECEIPT = "audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-VERIFICATION.json"
CHECKPOINT = "audit/p12-third-successor-discovery-20260921/checkpoint_p12_third_successor_discovery.py"
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
PLAN = "HoTT后续研究总体方案.md"
PLAN_SHARDS = tuple("HoTT后续研究总体方案/" + name for name in (
    "001 - 上一轮问答与四分支校正.md", "002 - 共同任务、术语与优先级原则.md",
    "003 - 分支顺序、准入与停止条件.md", "004 - 令牌经济、反漂移与每单元复核.md",
    "005 - 当前第一步与交接.md",
))
P12_SOURCES = (
    REPORT, FREEZE, VERIFY, RECEIPT, CHECKPOINT, PLAN_VERIFY, PLAN_RECEIPT, PLAN, *PLAN_SHARDS,
    "goal.md", "goal-3.md", "feature-list.md", "rulings.md", "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    "audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md",
    "HoTT/formal/astra-real-geometry/AmbientCircle.lean",
    "HoTT/formal/astra-real-geometry/PuncturedCircle.lean",
    "HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02/RUN.json",
    "HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02/source-manifest.json",
    "audit/astra-ambient-geometry-20260920/DELIVERY.json",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repl(text: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, text, count=1)
    assert count == 1, old
    return result


def row(text: str, prefix: str, value: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = value
            return "\n".join(lines) + "\n"
    raise AssertionError(prefix)


def core_audit(core: dict[str, object]) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.M)
    assert len(headings) == core["kc_count"] == 46
    touched = {3, 4, 5, 10, 15, 19, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    result = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P12_AMBIENT_PAIR_CANDIDATE_SELECTED_P13_RMIN_REQUALIFICATION_NEXT
- panorama_change: AMBIENT_PAIR_SPECIALIZATION_CANDIDATE_WITH_INTRINSIC_AND_OPERATION_CONTROLS
- essay_change: NO
- update_decision: P12 closes only its four-entry discovery denominator and routes the active goal to P13, which will decide whether the existing ambient-pair relation is a non-arbitrary R_min specialization.
- cross_conflicts: intrinsic homeomorphism, fixed ambient homeomorphism, and finite ambient-operation reconstruction are distinct relations; no one of them establishes a HoTT defect or complete reality relation.
- unresolved: P13 R_ambient qualification, actual K, a rule bridge, and a reproducible theory–implementation difference remain open.
- writer_compatibility: `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`; runtime 3.6.1 currently permits this full 46-KC legacy single-file audit in the atomic session bundle, not nested audit shards.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for ordinal, (kc, topic) in enumerate(headings, 1):
        if ordinal in touched:
            relation = "DEEPENED"
            assessment = "P12将既有去点圆/开区间的内在同胚与固定实平面、嵌入和有限环境操作的差异分开，选择R_ambient专门化候选而不宣称通常拓扑不同。"
            evidence = f"{REPORT}；P13若仅是既有字段改名则为RESTATEMENT_ONLY，若形成非任意合同也仍需未来K。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本单元只作P12的有界候选选择与既有资产资格化。"
            evidence = "goal.md §2；没有新数学定理、原生HoTT运行或HoTT缺陷结论。"
        result += f"| `{kc}` | {topic} | {relation} | {assessment} | {evidence} |\n"
    return result + """

## 扩展认知逐片复认

001–008：P12从现实中的固定环境、允许操作和复原条件来阅读“同胚”，把解释断裂变成可审查的 pair/operation 规格候选；这是一条发现与资格化路径，不是对HoTT的结论。

## 波次定位

1. **最终目标连接：** P12服务P1/P6的来源—操作—复原边，测试“内在同胚不足”能否转成标准且机器化的受限关系。
2. **全局坐标：** P11关闭Circle/Coeq分母；P12避开已审簇，复用C-265–C-268并选择P13；P13为future-K提供或拒绝一个精确强任务合同。
3. **实际价值：** 新增的是可定位的复用裁决和P13合同，而不是新证明；它避免重复Circle/HIT、Rzk或sHoTT语料。
4. **继续检验：** P13必须改变观察量为ambient input/operation/done映射；重复Lean或更换关键词没有资格继续。
5. **不延续P12的理由：** 四类入口的声明范围已经完成，继续同一discovery不会改变分母；目标改由P13的不同资格化问题持续推进。
6. **裁决：** `SWITCH_BRANCH / SUCCESSOR_SELECTED`；P13开始前不主张K、理论桥、实现差异或HoTT缺陷。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    subprocess.check_call([sys.executable, "-B", PLAN_VERIFY, "--write"], cwd=ROOT)
    for source in P12_SOURCES:
        assert (ROOT / source).is_file(), source

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 231
    assert state["latest_session"] == "S-RES-20260921-ASTRA-P11-COQHOTT-CIRCLE-COEQUALIZER"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha(ROOT / path) == digest for path, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID])
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P12-AMBIENT-PAIR-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    assert json.loads((ROOT / RECEIPT).read_text(encoding="utf-8"))["status"] == "PASS_WITH_SCOPE"
    assert json.loads((ROOT / PLAN_RECEIPT).read_text(encoding="utf-8"))["status"] == "PASS_WITH_SCOPE"

    previous = state["latest_session"]
    state["revision"] = 232
    state["latest_session"] = SID
    for ident in (*PREVIOUS_IDS, PLAN_ID, ABX_ID):
        record = state["records"][ident]
        record["related_records"] = list(dict.fromkeys(record.get("related_records", []) + [P12_ID, SID]))
        paths = set(record.get("full_sources", [])) | set(record.get("source_hashes", {}))
        record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
        record["revalidation"] = record.get("revalidation", "") + " Revision232 records P12's ambient-pair successor selection; prior scope unchanged."

    portfolio = state["records"][PLAN_ID]
    portfolio["evidence_status"] = "USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_DEFENSE / P10_COQHOTT_CANDIDATE_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_AMBIENT_PAIR_CANDIDATE_SELECTED / P13_AMBIENT_PAIR_RMIN_REQUALIFICATION_NEXT / GOAL_ACTIVE"
    portfolio["status"] = "four_track_first_pass_p5_p6_p7_p8_p9_complete_p10_selected_p11_gluing_defense_p12_ambient_pair_selected_p13_next"
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(P12_SOURCES)))
    portfolio["related_records"] = list(dict.fromkeys(portfolio.get("related_records", []) + [P12_ID, SID]))
    paths = set(portfolio["full_sources"]) | set(portfolio.get("source_hashes", {}))
    portfolio["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    portfolio["revalidation"] = "Revision232 completes P12: existing C-265–C-268 separates intrinsic homeomorphism from fixed ambient homeomorphism and finite ambient reconstruction. P13 alone decides whether R_ambient is a non-arbitrary R_min specialization."
    portfolio["scope"] = "P12 is a bounded public/local successor discovery. It selects an existing ambient-pair R candidate but does not replay Lean, formalize native HoTT, establish K, or claim a HoTT defect."

    abx = state["records"][ABX_ID]
    abx["full_sources"] = list(dict.fromkeys(abx.get("full_sources", []) + list(P12_SOURCES)))
    paths = set(abx["full_sources"]) | set(abx.get("source_hashes", {}))
    abx["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    abx["revalidation"] = "Revision232 selects R_ambient as an existing classical ambient-pair control for P13 qualification. It is not an actual K or a HoTT conclusion."
    abx["scope"] = "P12 finds no K in its declared discovery denominator. P13 tests only whether the existing ambient-pair relation strengthens R_min with a non-arbitrary task contract."

    state["records"][P12_ID] = {
        "kind": "result", "path": REPORT, "lifecycle_status": "CURRENT",
        "evidence_status": "SUCCESSOR_SELECTED / AMBIENT_PAIR_RMIN_REQUALIFICATION_CANDIDATE / P13_NOT_STARTED / NO_NEW_MATHEMATICAL_CLAIM",
        "status": "complete_with_scope_p13_ambient_pair_rmin_requalification_next", "depends_on": [],
        "related_records": [PLAN_ID, ABX_ID, *PREVIOUS_IDS, previous],
        "full_sources": list(dict.fromkeys(P12_SOURCES)),
        "source_hashes": {path: sha(ROOT / path) for path in dict.fromkeys(P12_SOURCES)},
        "scope": "P12 selects existing Lean ambient-pair controls as an R_min specialization candidate. It does not rerun Lean, establish a native HoTT theorem, an actual K, or a HoTT defect.",
    }
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "P12_THIRD_SUCCESSOR_DISCOVERY_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [P12_ID, PLAN_ID, ABX_ID, previous],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_NEXT",
        current_phase="PHASE_2_P12_AMBIENT_PAIR_CANDIDATE_SELECTED_P13_RMIN_REQUALIFICATION_NEXT",
        second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_NEXT",
        last_checkpoint_session=SID,
        checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json",
        next_minimal_verification="P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-001. Do not rerun Lean. Map C-266 intrinsic-homeomorphism, C-267 fixed-ambient-homeomorphism and C-268 finite-ambient-operation controls to OriginDirectedDiagram Input/Operation/Observation/Done, then decide R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE or RESTATEMENT_ONLY. Neither result establishes K or a HoTT defect.",
    )
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_AMBIENT_PAIR_SELECTED / NEXT_P13_AMBIENT_PAIR_RMIN_REQUALIFICATION / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for bounded successor discovery
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: select one new P12 denominator without repeating P8/P9/P11 source clusters
- load_receipt: `audit/p12-third-successor-discovery-20260921/P12-AMBIENT-PAIR-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / AMBIENT_PAIR_RMIN_REQUALIFICATION_CANDIDATE / P13_NEXT

P12 found a pre-existing classical Lean control set, not a new HoTT result. It preserves intrinsic homeomorphism while separately testing fixed-plane ambient homeomorphism and a finite ambient-operation reconstruction class. P13 will decide whether that difference is a reusable, non-arbitrary R_min/Done specialization.

| element | use | effect on this unit |
|---|---|---|
| public pair/ambient-topology search | used | confirms standard adjacent terminology but no exact HoTT consumer |
| C-265–C-268 source/run manifests | used, not rerun | establishes precise local reuse and operation scope |
| P6/P7 contracts | used | locates the unmapped ambient-operation gap for P13 |
| Lean kernel | not run | no new theorem, proof replay or native HoTT conclusion |
| P8/P9/P11 source clusters | excluded | prevents synonymic continuation of closed denominators |
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{
            "kind": "p12-successor-discovery-and-plan-verification",
            "command": "public/community and local/historical reconnaissance; P12 candidate verifier; four-track plan verifier",
            "result": "PASS_WITH_SCOPE; ambient-pair R_min candidate selected; P13 routed",
            "mathematics": "NO_NEW_KERNEL_RUN",
        }],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "P12 bounded successor discovery and existing-asset qualification only.",
    }
    drow = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P12环境对候选与P13资格化 | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_GLUING_DEFENSE / P12_AMBIENT_PAIR_SELECTED / NEXT_P13_AMBIENT_PAIR_RMIN_REQUALIFICATION / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P12 | P13审查R_ambient是否补充非任意Input/Operation/Observation/Done合同 | `HoTT后续研究总体方案.md`；P12 report；revision232 receipt |"
    arow = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P12环境对R候选后的P13资格化 | H/R/K、P1–P12 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P12_AMBIENT_PAIR_SELECTED / NEXT_P13_AMBIENT_PAIR_RMIN_REQUALIFICATION` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P12 | 只映射既有C-266–C-268的ambient输入、操作、观察和Done | `ABX行动.md`；P12 report；revision232 receipt |"
    prow = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P12环境对R_min候选选择 | `DIR-U-HOTT-FOUR-TRACK` | C-265–C-268、pair/ambient标准术语、P6/P7 | `SUCCESSOR_SELECTED / AMBIENT_PAIR_RMIN_REQUALIFICATION_CANDIDATE / P13_NEXT` | 内在同胚、环境homeomorphism与有限操作复原被分开 | 不证明完整现实关系、K或HoTT缺陷 | `audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md`；revision232 receipt |"
    aprow = "| `OUT-ABX-ACTION-INTAKE` | ABX P12环境对R候选 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C-265–C-268、P7五项与P6结构比较 | `AMBIENT_PAIR_CANDIDATE / P13_RMIN_REQUALIFICATION_NEXT` | 只给出R端专门化候选；没有K | 不证明传统同胚错误、完整复原不可能或HoTT缺陷 | `ABX行动.md`；P12 report；revision232 receipt |"
    memory = "P12第三次successor discovery已完成：未重复Rzk/sHoTT或Coq-HoTT Circle/Coeq，公开检索确认pair/ambient-homeomorphism是标准相邻结构但未发现精确HoTT consumer；本地复用C-265–C-268，选择R_ambient为R_min专门化候选。当前P13不重跑Lean，只映射内在同胚、固定环境homeomorphism和有限环境操作到Input/Operation/Observation/Done，判R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE或RESTATEMENT_ONLY。两者都不构成K或HoTT缺陷。入口：`audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md`；revision232 checkpoint。"
    frontier = "- P12已完成：已有C-265–C-268把内在同胚与固定Plane、环境homeomorphism和有限环境操作分开；它是R_ambient专门化候选，不是K或HoTT结果。当前P13只资格化其Input/Operation/Observation/Done映射，不重跑Lean；若仅同义重述，生成下一不同分母。入口：`audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md`。"
    resume = "当前 active goal 在P12后继续：P12以公开/本地双重侦察选择了C-265–C-268的R_ambient环境对候选。P13=AMBIENT_PAIR_RMIN_REQUALIFICATION：不重跑Lean，固定Plane/嵌入/闭包余集/ambient operation，映射C-266内在同胚、C-267环境homeomorphism、C-268有限环境复原到OriginDirectedDiagram的Input/Operation/Observation/Done；只输出R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE或RESTATEMENT_ONLY，然后仍按active-goal生成后继。入口：`audit/p12-third-successor-discovery-20260921/P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md`；revision232 checkpoint。"
    log = "\nS-RES-20260921-ASTRA-P12-THIRD-SUCCESSOR-DISCOVERY：P12完成。公开资料确认pair/ambient-homeomorphism是标准相邻结构；本地C-265–C-268将内在同胚、固定环境homeomorphism和有限环境操作分开。选择R_ambient为P13专门化候选；P13不重跑Lean，不主张K或HoTT缺陷；revision232 checkpoint。\n"

    files = []
    for rel in list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT)):
        raw = (ROOT / rel).read_bytes()
        text = raw.decode(encoding="utf-8")
        if rel == runtime.STATE:
            text = runtime.dump(state).decode(encoding="utf-8")
        elif rel == runtime.DIRECTION:
            text = repl(repl(repl(
                text, "source_state_revision: 231", "source_state_revision: 232"),
                "projection_generation: 20260921-direction-231", "projection_generation: 20260921-direction-232"),
                "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_NEXT",
                "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_NEXT")
        elif rel == runtime.PANORAMA:
            text = repl(repl(repl(
                text, "source_state_revision: 231", "source_state_revision: 232"),
                "projection_generation: 20260921-outcome-231", "projection_generation: 20260921-outcome-232"),
                "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_NEXT",
                "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_NEXT")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            text = row(row(text, "| `DIR-U-HOTT-FOUR-TRACK` |", drow), "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", arow)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            text = row(row(text, "| `OUT-HOTT-FOUR-TRACK-PLAN` |", prow), "| `OUT-ABX-ACTION-INTAKE` |", aprow)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            text = row(text, "P11 Coq-HoTT Circle/Coeq五文件审计已完成：", memory)
        elif rel == "MEMORY/003 - 当前验证状态与顺序日志.md":
            text += log
        elif rel == runtime.PREFIX + "FRONTIER.md":
            text = repl(text, "- P11 Coq-HoTT@e3deab71已完成：Circle/Coeq/Torus显式保留maps/glue/coherence/base/loop/surface，无原Done_s调用，非K；Torus Admitted只是信任边界。当前P12重新在未审规则、非Circle/Coeq消费者、更强R/Done或可重放实现差异中选一个分母，不延长已审簇。入口：`audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md`。", frontier)
        elif rel == runtime.PREFIX + "RESUME.md":
            text = repl(text, "当前 active goal 在P11后继续：Coq-HoTT@e3deab71 Circle/Coeq/Torus五文件是显式glue/coherence防御，非K；Torus Admitted保持信任边界。P12=THIRD_SUCCESSOR_DISCOVERY：先做公开/本地资产侦察，比较未审规则、非Circle/Coeq非directed消费者、独立更强R/Done与理论—实现差异，选定一个不被P1–P11覆盖的分母。入口：`audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md`；revision231 checkpoint。", resume)
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": text})
    for name, text in (
        ("SESSION.md", session),
        ("RUNS.json", runtime.dump(runs).decode(encoding="utf-8")),
        ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"])),
    ):
        files.append({"path": BASE + name, "expected_sha256": None, "text": text})
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID,
        "load_profile": "research", "task_ids": [PLAN_ID],
        "authorization": "用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。",
        "files": files,
    }
    (OUT / "P12-AMBIENT-PAIR-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    target = OUT / ("P12-AMBIENT-PAIR-checkpoint-apply.json" if args.apply else "P12-AMBIENT-PAIR-checkpoint-dry-run.json")
    target.write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
