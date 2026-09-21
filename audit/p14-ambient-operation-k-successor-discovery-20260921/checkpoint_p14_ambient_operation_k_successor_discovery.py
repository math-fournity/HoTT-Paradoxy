#!/usr/bin/env python3
"""Checkpoint P14's bounded actual-HoTT consumer selection and route P15."""
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
SID = "S-RES-20260921-ASTRA-P14-AMBIENT-OPERATION-K-DISCOVERY"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN_ID = "R-HOTT-FOUR-TRACK-PLAN-20260921"
ABX_ID = "R-ABX-ACTION-20260921"
P14_ID = "R-P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-20260921"
P13_ID = "R-P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-20260921"
PREVIOUS_IDS = (
    "R-P1-RMIN-SPEC-20260921", "R-P2-KTHEORY-SIP-20260921",
    "R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921", "R-P5-SUCCESSOR-DISCOVERY-20260921",
    "R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921", "R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921",
    "R-P8-RZK-DIRECTED-IMPLEMENTATION-20260921", "R-P9-SHOTT-DIRUNIV-CORPUS-20260921",
    "R-P10-SECOND-SUCCESSOR-DISCOVERY-20260921", "R-P11-COQHOTT-CIRCLE-COEQUALIZER-20260921",
    "R-P12-THIRD-SUCCESSOR-DISCOVERY-20260921", P13_ID,
)
REPORT = "audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-REPORT.md"
FREEZE = "audit/p14-ambient-operation-k-successor-discovery-20260921/P14-PRIETO-CUBIDES-CANDIDATE-FREEZE.json"
VERIFY = "audit/p14-ambient-operation-k-successor-discovery-20260921/verify_p14_ambient_operation_k_successor_discovery.py"
RECEIPT = "audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-VERIFICATION.json"
CHECKPOINT = "audit/p14-ambient-operation-k-successor-discovery-20260921/checkpoint_p14_ambient_operation_k_successor_discovery.py"
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
PLAN = "HoTT后续研究总体方案.md"
PLAN_SHARDS = tuple("HoTT后续研究总体方案/" + name for name in (
    "001 - 上一轮问答与四分支校正.md", "002 - 共同任务、术语与优先级原则.md",
    "003 - 分支顺序、准入与停止条件.md", "004 - 令牌经济、反漂移与每单元复核.md",
    "005 - 当前第一步与交接.md",
))
P14_SOURCES = (
    REPORT, FREEZE, VERIFY, RECEIPT, CHECKPOINT, PLAN_VERIFY, PLAN_RECEIPT, PLAN, *PLAN_SHARDS,
    "goal.md", "goal-3.md", "feature-list.md", "rulings.md", "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md",
    "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-EVIDENCE-FREEZE.json",
    "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/DISCOVERY-CANDIDATES.json",
    "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/TRIAGE.json",
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
    touched = {5, 10, 15, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    result = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P14_PRIETO_CUBIDES_CANDIDATE_SELECTED_P15_CORPUS_AUDIT_NEXT
- panorama_change: VERSION_PINNED_ACTUAL_HOTT_AGDA_CANDIDATE_SELECTED_WITH_NO_K_VERDICT
- essay_change: NO
- update_decision: P14 selects one version-pinned actual HoTT-related Agda corpus after public and local reconnaissance; P15 must inspect the fixed pages before classifying it as a consumer or a task-different defense.
- cross_conflicts: a publication's use of the word "embedding" does not make its combinatorial Map/walk/spherical task identical to P13's point-set M/N operation-sensitive completion task.
- unresolved: P15 K-input/K-output/K-claim/K-forgetting/K-version, an actual K, any theory-rule bridge, and any HoTT-defect conclusion remain open.
- writer_compatibility: `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`; runtime 3.6.1 permits this complete legacy 46-KC single-file audit in the atomic bundle, not nested audit shards.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for ordinal, (kc, topic) in enumerate(headings, 1):
        if ordinal in touched:
            relation = "DEEPENED"
            assessment = "P14把现实对齐的K问题落实为公开实际HoTT相关语料的版本冻结与任务比较，拒绝从题名或相邻术语直接推断忘却或完成提升。"
            evidence = f"{REPORT}；P15若发现固定模块只以bare H承载P13 Done才改变K判词。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本单元只完成P14候选选择与来源身份冻结。"
            evidence = "goal.md §2；无新数学定理、原生HoTT运行或HoTT缺陷结论。"
        result += f"| `{kc}` | {topic} | {relation} | {assessment} | {evidence} |\n"
    return result + """

## 扩展认知逐片复认

001–008：P14把现实对齐落实为输入、操作、观察与完成标准的消费者审计，而不把相似的数学名词自动当作同一任务。既有社区形式化是可检验的边界来源，不是推翻或确认用户问题的替代判词。

## 波次定位

1. **最终目标连接：** P14把P13的operation-sensitive R合同接入一个真实、版本固定的HoTT/Agda候选，令P15可首次检查实际使用者是否保留结构。
2. **全局坐标：** P14属于P3 K_app的successor discovery；P15是同一候选的有界source audit，不重做P13几何。
3. **实际价值：** 本地题录由`DISCOVERY_UNREVIEWED`升为可定位五模块、版本和P7准入项的候选卡，减少重复劳动。
4. **继续检验：** P15只读固定论文与五个发布页面，逐项比较Map/face/walk数据与P13的bare H/Done；结果可以是task-different defense或仍未决，不能预设命中。
5. **不延续P14的理由：** 选择分母已经冻结；进一步关键词扩展不会替代固定语料的输入/输出审计。
6. **裁决：** `SWITCH_BRANCH / SUCCESSOR_SELECTED`；P15尚未开始；无K或HoTT缺陷结论。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    subprocess.check_call([sys.executable, "-B", PLAN_VERIFY, "--write"], cwd=ROOT)
    for source in P14_SOURCES:
        assert (ROOT / source).is_file(), source

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 233
    assert state["latest_session"] == "S-RES-20260921-ASTRA-P13-AMBIENT-PAIR-RMIN"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha(ROOT / path) == digest for path, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID])
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P14-AMBIENT-OPERATION-K-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    previous = state["latest_session"]
    state["revision"] = 234
    state["latest_session"] = SID
    for ident in (*PREVIOUS_IDS, PLAN_ID, ABX_ID):
        record = state["records"][ident]
        record["related_records"] = list(dict.fromkeys(record.get("related_records", []) + [P14_ID, SID]))
        paths = set(record.get("full_sources", [])) | set(record.get("source_hashes", {}))
        record["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
        record["revalidation"] = record.get("revalidation", "") + " Revision234 records P14's version-pinned Prieto-Cubides candidate selection; prior result scope unchanged."

    portfolio = state["records"][PLAN_ID]
    portfolio["evidence_status"] = "USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_DEFENSE / P10_COQHOTT_CANDIDATE_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_AMBIENT_PAIR_CANDIDATE_SELECTED / P13_R_AMBIENT_SPECIALIZATION_ACCEPTED / P14_PRIETO_CUBIDES_CANDIDATE_SELECTED / P15_SPHERICAL_MAPS_AGDA_CORPUS_NEXT / GOAL_ACTIVE"
    portfolio["status"] = "four_track_first_pass_p5_p6_p7_p8_p9_complete_p10_selected_p11_gluing_defense_p12_ambient_pair_selected_p13_r_ambient_accepted_p14_prieto_selected_p15_next"
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(P14_SOURCES)))
    paths = set(portfolio["full_sources"]) | set(portfolio.get("source_hashes", {}))
    portfolio["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    portfolio["revalidation"] = "Revision234 completes P14: Prieto-Cubides CPP2022 published Agda formalisation is a version-pinned actual-HoTT-related candidate. P15 must compare its explicit combinatorial input/output with P13's operation-sensitive M/N contract."
    portfolio["scope"] = "P14 selects a source denominator only. It neither reads all source text nor establishes actual K, a theorem-level bridge, an implementation discrepancy, or a HoTT defect."

    abx = state["records"][ABX_ID]
    abx["full_sources"] = list(dict.fromkeys(abx.get("full_sources", []) + list(P14_SOURCES)))
    paths = set(abx["full_sources"]) | set(abx.get("source_hashes", {}))
    abx["source_hashes"].update({path: sha(ROOT / path) for path in paths if (ROOT / path).is_file()})
    abx["revalidation"] = "Revision234 selects a version-pinned actual-HoTT-related Agda corpus for the next P7 audit. Its apparent explicit Map/face/walk inputs are a defense signal, not a finished K verdict."
    abx["scope"] = "P14 adds no actual K. P15 must determine whether the fixed corpus's task is different or has a P13-relevant bare-H-to-Done promotion."

    state["records"][P14_ID] = {
        "kind": "result", "path": REPORT, "lifecycle_status": "CURRENT",
        "evidence_status": "SUCCESSOR_SELECTED / PRIETO_CUBIDES_SPHERICAL_MAPS_AGDA_CANDIDATE / P15_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "status": "complete_with_scope_p15_prieto_cubides_spherical_maps_agda_corpus_next", "depends_on": [],
        "related_records": [PLAN_ID, ABX_ID, *PREVIOUS_IDS, previous],
        "full_sources": list(dict.fromkeys(P14_SOURCES)),
        "source_hashes": {path: sha(ROOT / path) for path in dict.fromkeys(P14_SOURCES)},
        "scope": "P14 freezes one public actual HoTT-related Agda corpus as a P15 candidate. It does not inspect source semantics beyond published identity markers or establish K.",
    }
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY_CHECKPOINTED_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [P14_ID, PLAN_ID, ABX_ID, previous],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_PRIETO_SELECTED_P15_NEXT",
        current_phase="PHASE_2_P14_PRIETO_CUBIDES_CANDIDATE_SELECTED_P15_SPHERICAL_MAPS_AGDA_CORPUS_NEXT",
        second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_PRIETO_SELECTED_P15_NEXT",
        last_checkpoint_session=SID,
        checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json",
        next_minimal_verification="P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-001. Inspect only the fixed author-published CPP2022-paper/Map/Map.Face.Walk.Homotopy/Map.Spherical/Map.Spherical-is-enough pages and paper context. Apply P7 K-input/K-output/K-claim/K-forgetting/K-version; distinguish explicit Map/Face/Walk data from P13 bare H_intrinsic and determine task equivalence. Do not compile Agda, download/clone unknown source, or broaden to the full website.",
    )
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_P9_COMPLETE / P10_SELECTED / P11_COQHOTT_GLUING_DEFENSE / P12_AMBIENT_PAIR_SELECTED / P13_R_AMBIENT_SPECIALIZATION_ACCEPTED / P14_PRIETO_CUBIDES_CANDIDATE_SELECTED / NEXT_P15_SPHERICAL_MAPS_AGDA_CORPUS / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for bounded actual-HoTT-consumer selection
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: select one version-pinned actual HoTT-related source denominator after P13's operation-sensitive R qualification
- load_receipt: `audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / SUCCESSOR_SELECTED / P15_NEXT

P14 performed a bounded public and local reconnaissance. It selected the author-published Prieto-Cubides CPP2022 Agda formalisation as a source denominator because its published identity, modules, and relationship to embeddings/isotopy are inspectable, while the local literature register contained only an unreviewed title signal. It did not compile Agda, replay a kernel, claim task equivalence, find K, or claim a HoTT defect.

| element | use | effect on this unit |
|---|---|---|
| P13 contract | used | fixes bare `H_intrinsic` and the two operation-sensitive Done targets |
| CPP2022 paper and five author pages | used | freezes an actual published HoTT-related Agda candidate and five P15 modules |
| local LIT-DENOMINATOR record | used | proves prior local state was unreviewed, avoiding false novelty or repeated work |
| Agda kernel | not run | P14 is source identity and candidate selection only |
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{
            "kind": "p14-public-local-source-selection",
            "command": "P14 fixed-source identity check; local LIT denominator check; P14 verifier; four-track plan verifier",
            "result": "PASS_WITH_SCOPE; Prieto-Cubides candidate selected; P15 routed",
            "mathematics": "NO_NEW_KERNEL_RUN",
        }],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "P14 source-denominator selection only.",
    }
    drow = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P14实际语料选择与P15源码审计 | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P13_R_AMBIENT_ACCEPTED / P14_PRIETO_CUBIDES_CANDIDATE_SELECTED / NEXT_P15_SPHERICAL_MAPS_AGDA_CORPUS / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P14 | P15逐项审计版本固定Map/Face/Walk/Spherical模块 | `HoTT后续研究总体方案.md`；P14 report；revision234 receipt |"
    arow = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P14实际消费者候选后的P15审计 | H/R/K、P1–P14 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P14_PRIETO_CUBIDES_CANDIDATE_SELECTED / NEXT_P15_SPHERICAL_MAPS_AGDA_CORPUS` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P14 | 检查显式Map/face/walk是否保留结构、任务是否不同 | `ABX行动.md`；P14 report；revision234 receipt |"
    prow = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P14 Prieto-Cubides实际HoTT/Agda候选选择 | `DIR-U-HOTT-FOUR-TRACK` | P13 Done合同、CPP2022论文/五个发布模块、LIT题录 | `SUCCESSOR_SELECTED / P15_NEXT / NO_ACTUAL_K` | 固定版本、模块和P7五项；不重做几何或全站搜索 | 不证明任务同一、K、HoTT缺陷或Agda kernel replay | `audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-REPORT.md`；revision234 receipt |"
    aprow = "| `OUT-ABX-ACTION-INTAKE` | ABX P14实际消费者候选选择 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P13 operation contracts + Prieto-Cubides published Map/Face/Walk/Spherical source identity | `P14_PRIETO_CUBIDES_CANDIDATE_SELECTED / P15_AUDIT_NEXT` | P15必须比较任务，显式结构是防御信号而非自动判词 | 不证明传统同胚错误、真实K或HoTT缺陷 | `ABX行动.md`；P14 report；revision234 receipt |"
    memory = "P14实际消费者 successor discovery 已完成：公开/本地侦察选择 Prieto-Cubides CPP2022 的作者发布 Agda formalisation 为版本冻结 P15 语料；本地旧题录仅为 `DISCOVERY_UNREVIEWED`。候选可见 `Map`、face、walk-homotopy、spherical 模块，是结构保留的初步信号，尚未完成P7五项或K判词。当前P15只审固定论文与五页面，比较其显式数据和P13 bare H_intrinsic/Done_ambient^fin/Done_curve；不编译、下载或扩站扫描。入口：`audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-REPORT.md`；revision234 checkpoint。"
    frontier = "- P14已完成：Prieto-Cubides CPP2022 Agda formalisation由本地未审题录升为版本冻结候选。当前P15在固定五模块中逐项做P7 K审计，判断显式Map/Face/Walk是否使任务不同或是否有bare-H-to-Done提升；不重跑几何、不扩展网站。入口：`audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-REPORT.md`。"
    resume = "当前 active goal 在P14后继续：P14选择了Prieto-Cubides CPP2022作者发布Agda formalisation，P15=PRIETO_CUBIDES_SPHERICAL_MAPS_AGDA_CORPUS。只读CPP2022-paper、Map、Map.Face.Walk.Homotopy、Map.Spherical、Map.Spherical-is-enough与论文背景，按P7 K-input/K-output/K-claim/K-forgetting/K-version比较显式Map/Face/Walk和P13 bare H_intrinsic/Done。不得编译、克隆、下载未知源码或扩大到全站。入口：`audit/p14-ambient-operation-k-successor-discovery-20260921/P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-REPORT.md`；revision234 checkpoint。"
    log = "\nS-RES-20260921-ASTRA-P14-AMBIENT-OPERATION-K-DISCOVERY：P14完成。Prieto-Cubides CPP2022的作者发布Agda formalisation从本地未审题录升级为版本冻结实际HoTT相关语料候选；P15只审固定五模块的显式输入、输出、claim、forgetting和版本，不预设K或HoTT缺陷；revision234 checkpoint。\n"

    files = []
    for rel in list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT)):
        raw = (ROOT / rel).read_bytes()
        text = raw.decode(encoding="utf-8")
        if rel == runtime.STATE:
            text = runtime.dump(state).decode(encoding="utf-8")
        elif rel == runtime.DIRECTION:
            text = repl(repl(repl(text, "source_state_revision: 233", "source_state_revision: 234"), "projection_generation: 20260921-direction-233", "projection_generation: 20260921-direction-234"), "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_PRIETO_CUBIDES_CANDIDATE_SELECTED_P15_NEXT")
        elif rel == runtime.PANORAMA:
            text = repl(repl(repl(text, "source_state_revision: 233", "source_state_revision: 234"), "projection_generation: 20260921-outcome-233", "projection_generation: 20260921-outcome-234"), "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT", "semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_PRIETO_CUBIDES_CANDIDATE_SELECTED_P15_NEXT")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            text = row(row(text, "| `DIR-U-HOTT-FOUR-TRACK` |", drow), "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", arow)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            text = row(row(text, "| `OUT-HOTT-FOUR-TRACK-PLAN` |", prow), "| `OUT-ABX-ACTION-INTAKE` |", aprow)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            text = row(text, "P13环境对R_min资格化已完成：", memory)
        elif rel == "MEMORY/003 - 当前验证状态与顺序日志.md":
            text += log
        elif rel == runtime.PREFIX + "FRONTIER.md":
            text = row(text, "- P13已完成：", frontier)
        elif rel == runtime.PREFIX + "RESUME.md":
            text = row(text, "当前 active goal 在P13后继续：", resume)
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": text})
    for name, text in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode(encoding="utf-8")), ("CORE_COGNITION_AUDIT.md", audit(state["current_core"]))):
        files.append({"path": BASE + name, "expected_sha256": None, "text": text})
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN_ID],
        "authorization": "用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。",
        "files": files,
    }
    (OUT / "P14-AMBIENT-OPERATION-K-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P14-AMBIENT-OPERATION-K-checkpoint-apply.json" if args.apply else "P14-AMBIENT-OPERATION-K-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
