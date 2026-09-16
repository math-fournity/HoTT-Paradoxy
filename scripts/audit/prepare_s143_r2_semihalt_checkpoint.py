#!/usr/bin/env python3
"""Prepare revision 143: register the R2 semi-halting proof package."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260914-143-R2-SEMIHALT"
PREV = "S-RES-20260914-142-R2-FAIR"
RECORD_ID = "A-CUBICAL-SEMI-HALTING-001"
FAIR_ID = "A-CUBICAL-FAIR-ENUMERATION-001"
NATCODE_ID = "A-CUBICAL-NAT-PROGRAM-CODE-001"
PROGRAM_ID = "A-CUBICAL-PROGRAM-CODE-001"
R1_ID = "A-CUBICAL-MACHINE-HALTING-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_ID = "A-LIT-CLASSICS-001"
PROOF_GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
PROOF_ID = "MP-CUBICAL-SEMI-HALTING-001"
CLAIM_IDS = ["C-203", "C-204", "C-205", "C-206", "C-207"]
RUN_ID = "20260914-MP-CUBICAL-SEMI-HALTING-001-01"
SOURCE = "HoTT/formal/cubical-machine-halting/SemiHalting.agda"
PARENT_SOURCES = [
    "HoTT/formal/cubical-machine-halting/MachineHalting.agda",
    "HoTT/formal/cubical-machine-halting/ProgramCode.agda",
    "HoTT/formal/cubical-machine-halting/NatProgramCode.agda",
    "HoTT/formal/cubical-machine-halting/FairEnumeration.agda",
]
CLAIM = "HoTT/formal/cubical-machine-halting/CLAIM-R2-SEMIHALT.md"
RUN = f"HoTT/verification/runs/{RUN_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
FEATURE = "feature-list.md"
LIT_SHARD = ".codex/research/hott/LIT-CLASSICS-001/006 - 当前判词、缺口与下一机器工作包.md"
TOOLCHAIN = "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/partiality-race-timeout/AGDA_LIBRARIES"
AUDIT = "audit/R2半判定机器证明-20260914.md"
PREPARE = "scripts/audit/prepare_s143_r2_semihalt_checkpoint.py"
STATUS = "CORE_GENERATION_4_R2_SEMIHALT_COMPLETE_UNIVERSALITY_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s143", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "Theory Schema 获得了可执行的 stage-indexed partial answer 和全域公平正见证枚举，而不是只保留一个口头上的不可停机概念。",
        "KC-000010": "最终现实相对目标仍是完成判据；一般半判定结果没有被误晋升为 HoTT 悖论。",
        "KC-000012": "ASK 的计算合法性被精确区分：有限 stage 的 `nothing` 只回答有界问题，不能冒充无界否定。",
        "KC-000013": "时间／时序在此表现为 stage 与证据出现次序；正答案可在未来出现，因此有限缺席不能被异化为永久不存在。",
        "KC-000021": "C-203–C-207 已具原生 kernel run、完整 source manifest、索引冻结与 exact replay。",
        "KC-000024": "不可停机代码路线完成正半判定层；universality、总不可判定归约与 exact HoTT 自指仍开放。",
        "KC-000027": "HoTT 代码工作区现在能执行逐阶段查询并公平枚举正停机 case；HoTT 特有性尚未建立。",
        "KC-000028": "单个显式循环及其半判定无返回不是自馈；代码专门化、自应用和 recursion theorem 仍是后续义务。",
        "KC-000036": "Gödel 路线所需的可数程序与正可枚举层已推进，但对象理论证明谓词、表示性、反射和 fixed point 尚未闭合。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮关闭 R2 正半判定，universality、不可判定、exact HoTT 与最终悖论仍开放。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{AUDIT}`；{kid} | "
            "universality/reduction、总停机不可判定、R4、HoTT essentiality、natural consumer 与现实桥梁仍开放。 |"
        )
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — R2-SEMIHALT 完成，下一有界单元转 universality/reduction 与文献补齐。",
        "- panorama_change: YES_IN_PLACE — 新增 OUT-TOP-R2-SEMIHALT-001。",
        "- essay_change: NO。",
        "- update_decision: 半判定只登记为一般计算性基础；具体 loopCode 的全阶段不返回不冒充通用不可判定或 HoTT 悖论。",
        "- cross_conflicts: finite-stage totality、positive semi-decidability、specific divergence 和 universal undecidability 是四个不同量词层级。",
        "- unresolved: source-model universality/reduction、R2-UNDEC、second kernel、R4 exact calculus、HoTT essentiality、natural consumer、same-task reality bridge、Post 与当前文献覆盖。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        SOURCE, *PARENT_SOURCES, CLAIM, MATRIX, REGISTRY, FORMAL_README,
        RUNS_README, HOTT_README, FEATURE, LIT_SHARD, TOOLCHAIN, LIBRARIES,
        AUDIT, PREPARE, f"{RUN}/RUN.json", f"{RUN}/stdout.txt",
        f"{RUN}/stderr.txt", f"{RUN}/environment.txt",
        f"{RUN}/source-manifest.json", f"{RUN}/index-row-manifest.json",
    ]
    if any(not (ROOT / rel).is_file() for rel in required):
        raise SystemExit("R2_SEMIHALT_EVIDENCE_MISSING")

    run = json.loads((ROOT / f"{RUN}/RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != CLAIM_IDS
        or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("exit_code") != 0
        or run.get("stderr", {}).get("bytes") != 0
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
    ):
        raise SystemExit("R2_SEMIHALT_RUN_NOT_FINAL")
    frozen = json.loads((ROOT / f"{RUN}/index-row-manifest.json").read_text(encoding="utf-8"))
    if frozen.get("claim_ids") != CLAIM_IDS or len(frozen.get("rows", [])) != 6:
        raise SystemExit("R2_SEMIHALT_INDEX_ROWS_NOT_FROZEN")
    registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
    if registry.get("later_machine_proved_claim_count") != 59 or len(registry.get("later_packages", [])) != 16:
        raise SystemExit("R2_SEMIHALT_REGISTRY_COUNT_INVALID")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 142 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_142_S142")
    if RECORD_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("R2_SEMIHALT_RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 为唯一工作面推进基于计算合法性／不可停机代码的 HoTT 悖论探索；R1 与 R2 的编码、公平枚举、正半判定及 LIT Classics 已贯通，继续 universality/undec、exact HoTT Gödel 与现实桥梁 | 用户 2026-09-14 当前指令与 active goal；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-LIT-DENOMINATOR-001`、`OUT-TOP-R1-FIXED-MACHINE-001`、`OUT-TOP-R2-PROGRAMCODE-001`、`OUT-TOP-R2-NATCODE-001`、`OUT-TOP-R2-FAIR-001`、`OUT-TOP-R2-SEMIHALT-001`、`OUT-TOP-LIT-CLASSICS-001` | 当前做 `R2-UNIVERSALITY-001` 的源模型／归约资格化，并补 Post primary 与 `LIT-HOTT-COMPUTABILITY-001`；R2-UNDEC、R4 与现实桥梁仍开放 | active goal；`SemiHalting.agda`；run `20260914-MP-CUBICAL-SEMI-HALTING-001-01`；LIT Classics |",
    )
    for old, new in (
        ("source_state_revision: 142", "source_state_revision: 143"),
        ("projection_generation: 20260914-direction-124", "projection_generation: 20260914-direction-125"),
        ("semantic_status: CORE_GENERATION_4_R2_FAIR_COMPLETE_SEMIHALT_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_FAIR_COMPLETE_SEMIHALT_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.append_to_shard(
        panorama,
        "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-TOP-R2-SEMIHALT-001` | R2 分阶段停机半判定：有限 stage 的 `Maybe` approximant、正答案持续、`CodeHalts ↔ SemiReturns`、公平全域正见证枚举及 halt/loop controls | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 main 的 `MP-CUBICAL-SEMI-HALTING-001` / C-203–C-207 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_SEMIHALT_COMPLETE / UNIVERSALITY_OPEN` | Agda 2.8.0-3d04bac + Cubical v0.9，exit 0、stderr 0、零 warning；proof+5 claim 行冻结；exact replay；8 个 source files + 5 个外部依赖固定 | 有限 stage 的 `nothing` 不是无界否定；具体 loop 控制不推出语言通用性、no total decider、certified reduction、Gödel/Rosser/Löb、HoTT essentiality、natural consumer、现实桥梁或内部矛盾 | `HoTT/formal/cubical-machine-halting/CLAIM-R2-SEMIHALT.md`；run `20260914-MP-CUBICAL-SEMI-HALTING-001-01`；`audit/R2半判定机器证明-20260914.md` |\n",
    )
    for old, new in (
        ("source_state_revision: 142", "source_state_revision: 143"),
        ("projection_generation: 20260914-outcome-124", "projection_generation: 20260914-outcome-125"),
        ("semantic_status: CORE_GENERATION_4_R2_FAIR_COMPLETE_SEMIHALT_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_FAIR_COMPLETE_SEMIHALT_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "3. 当前 Host goal",
        "3. 当前 Host goal 保持 ACTIVE。R1 与 R2 的 ProgramCode/NATCODE/FAIR/SEMIHALT 已在 main 形成五个 F-011 package；最新 C-203–C-207 证明有限 stage 正答案持续、`CodeHalts` 与某阶段返回双向对应、公平正见证枚举及 controls。它仍是一般计算性基础；HoTT-essential 最终 witness 未找到。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "6. 当前仍未得到",
        "6. 当前仍未得到计算通用性／certified halting-undecidability、E6、现实桥梁、`NATURAL_USAGE_MISMATCH`、HoTT-essential 自馈不可停机实例或 HoTT 内部矛盾。17 个冻结 package + 16 个 later package 只支持各自精确范围；最新 R1/R2 包仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "8. `LIT-DENOMINATOR-001`",
        "8. `LIT-DENOMINATOR-001` v1、LIT Classics、R1 与 R2-SEMIHALT 前五包已完成 scoped 增量。当前做 `R2-UNIVERSALITY-001` 的标准源模型／reduction 资格化，并交替补 Post primary 与 `LIT-HOTT-COMPUTABILITY-001`；随后闭合 R2-UNDEC。未获授权不 push、不 tag。",
    )
    memory["index_text"] = replace_once(
        memory["index_text"], "S023–S142 逐会话记录", "S023–S143 逐会话记录"
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S143 R2 SEMIHALT：新增 `SemiHalting.agda` 与 `MP-CUBICAL-SEMI-HALTING-001` / C-203–C-207。有限 stage `Maybe` approximant、正答案持续、精确步／bounded observation 桥梁、`CodeHalts ↔ SemiReturns`、公平全域正见证枚举和 halt/loop controls 均由 Agda 2.8.0 + Cubical v0.9 接受；run exit 0、stderr 0、零 warning，proof+5 claim 行冻结，exact replay。具体 loop 的全阶段不返回不等于 universal undecidability。global version closure 仍因未跟踪 R1/R2 资产 BLOCKED。下一步 `R2-UNIVERSALITY-001` 与文献交替。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S142 R2 FAIR 完成）", "# HoTT 研究前沿（S143 R2 SEMIHALT 完成）")
    frontier = replace_once(
        frontier,
        "R1 与 R2 ProgramCode/NATCODE/FAIR 已在 main 通过 F-011。C-199–C-202 给每个 ProgramCode×Config×fuel case 一个显式有限到达 stage，并证明 scheduled observation 保持；这仍是一般计算枚举基础。LIT Classics 有 16 个不同内容组，Rosser primary reviewed。当前第一工作包是 `R2-SEMIHALT-001`；universality/UNDEC、exact HoTT、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
        "R1 与 R2 ProgramCode/NATCODE/FAIR/SEMIHALT 已在 main 通过 F-011。C-203–C-207 证明 `CodeHalts` 当且仅当某个有限 stage 返回正答案，并给出公平的全域正见证流；有限 stage 的 `nothing` 没有被解释成无界否定。这仍是一般计算性基础。LIT Classics 有 16 个不同内容组，Rosser primary reviewed。当前第一工作包是 `R2-UNIVERSALITY-001` 的源模型／归约资格化，并与 Post/HoTT computability 文献交替；UNDEC、exact HoTT、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
    )

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += "\n98. 半判定必须把三个层级写进接口与证明：每个有限 stage 的 approximant 总结束；`just` 是可核验的正见证并随 stage 保持；`nothing` 只表示当前界内尚未发现。再证明 `CodeHalts ↔ ∥Σ stage, isSome(semiHaltAt stage)=true∥`，才能同时得到 soundness/completeness 而不偷添总的负答案。某个显式 loop 的全阶段归纳证明仍只是一个程序的不变量，不能代替语言通用性与 halting-undecidability reduction。\n"

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS143：`R2-SEMIHALT-001` 已由 `MP-CUBICAL-SEMI-HALTING-001` / C-203–C-207 机器闭合。run exit 0、stderr 0、零 warning、6 行冻结、exact replay；`CodeHalts` 与某个有限 stage 返回双向对应，且公平正见证枚举 sound/complete。具体 loop 的不返回不等于 universal undecidability。Git 仍 local-uncommitted。下一步 `R2-UNIVERSALITY-001` 源模型／reduction 资格化，并交替补 Post/HoTT computability 文献。\n\n",
    )

    state["revision"] = 143
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R2_SEMIHALT"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Qualify R2-UNIVERSALITY-001: select a standard source machine and certified theorem/reduction path, "
        "freeze the translation and forward/backward halting-preservation obligations, while alternating Post primary and HoTT computability literature review."
    )
    state["projection"]["status"] = STATUS
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260914-direction-125"
    direction_record["semantic_status"] = STATUS
    direction_record["scope"] = "Current main-only portfolio after S143: R1 and R2 through positive semi-halting are machine-proved locally; R2 universality/reduction is next. Literature has 16 unique groups and Rosser primary review; exact HoTT witness requirements remain open."
    outcome_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    outcome_record["projection_generation"] = "20260914-outcome-125"
    outcome_record["semantic_status"] = STATUS
    outcome_record["scope"] = "Current integrated outcome panorama through S143, including C-203-C-207 semi-halting, with universality/UNDEC, exact HoTT, natural consumer and reality bridge open."

    evidence = [
        SOURCE, *PARENT_SOURCES, CLAIM, TOOLCHAIN, LIBRARIES,
        f"{RUN}/RUN.json", f"{RUN}/source-manifest.json", f"{RUN}/index-row-manifest.json",
        f"{RUN}/stdout.txt", f"{RUN}/environment.txt", MATRIX, REGISTRY, AUDIT,
        "scripts/audit/capture_agda_proof_run.py", "scripts/audit/mark_proof_run_indexed.py",
        "scripts/audit/freeze_proof_index_rows.py", "scripts/audit/verify_formal_proof_run.py", PREPARE,
    ]
    state["records"][RECORD_ID] = {
        "claim_ids": CLAIM_IDS,
        "classification": "R2_SEMI_HALTING_POSITIVE_SEARCH_AND_FAIR_ENUMERATION",
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": evidence,
        "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT",
        "mathematical_status": "R2_SEMIHALT_COMPLETE_UNIVERSALITY_OPEN",
        "path": SOURCE,
        "proof_id": PROOF_ID,
        "research_parent": GOAL_ID,
        "related_records": [PROOF_GATE_ID, R1_ID, PROGRAM_ID, NATCODE_ID, FAIR_ID, PLAN_ID, COVERAGE_ID, LIT_ID, SESSION_ID],
        "resolution": {
            "evidence": [f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", MATRIX, AUDIT],
            "reason": "Native Cubical Agda exited 0 with stderr 0 and zero warnings; proof and five claim rows are frozen; exact replay matched. CodeHalts is equivalent to finite-stage positive return and the fair enumerator is sound/complete for bounded positive cases. Universality and no-total-decider remain open.",
        },
        "run_id": RUN_ID,
        "scope": "C-203 finite-stage Maybe approximants and positive persistence; C-204 exact-step/bounded bridge; C-205 CodeHalts iff some finite semiHaltAt stage returns; C-206 fair global positive enumeration with canonical soundness/completeness; C-207 halt/loop controls. No ProgramCode universality, certified halting undecidability, s-m-n, Goedel/Rosser/Lob, exact HoTT incompleteness, HoTT essentiality, natural consumer, reality bridge or contradiction.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in evidence},
        "status": "complete",
        "version_closure": {"registry": REGISTRY, "scope_preserved": True, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"},
    }

    changed_hash_paths = [MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, FEATURE, LIT_SHARD]
    for record in state["records"].values():
        hashes = record.get("source_hashes")
        if not isinstance(hashes, dict):
            continue
        for rel in changed_hash_paths:
            if rel in hashes:
                hashes[rel] = R.sha((ROOT / rel).read_bytes())

    fair = state["records"][FAIR_ID]
    fair["mathematical_status"] = "R2_FAIR_COMPLETE_SEMIHALT_COMPLETED_DOWNSTREAM"
    add_once(fair.setdefault("related_records", []), RECORD_ID)
    add_once(fair["related_records"], SESSION_ID)
    fair["resolution"]["reason"] = "Native Cubical Agda exited 0 with stderr 0 and zero warnings; proof and four claim rows are frozen; exact replay matched. This package establishes fair finite-stage coverage. Downstream S143 now supplies the semi-halting consumer; universality and undecidability remain open."
    fair["revalidation"] = f"{SESSION_ID}: downstream C-203-C-207 consume the fair schedule and close positive semi-halting; this does not alter C-199-C-202 or prove universality/undecidability."

    natcode = state["records"][NATCODE_ID]
    natcode["mathematical_status"] = "R2_NATCODE_COMPLETE_FAIR_AND_SEMIHALT_COMPLETED_DOWNSTREAM"
    add_once(natcode.setdefault("related_records", []), RECORD_ID)
    add_once(natcode["related_records"], SESSION_ID)
    natcode["revalidation"] = f"{SESSION_ID}: downstream fair enumeration and positive semi-halting now consume the numeric code; C-195-C-198 remain unchanged and universality/undecidability remain open."

    goal = state["records"][GOAL_ID]
    add_once(goal.setdefault("related_records", []), RECORD_ID)
    add_once(goal["related_records"], SESSION_ID)
    goal["revalidation"] = f"{SESSION_ID}: C-203-C-207 close positive semi-halting and fair positive enumeration; goal remains active because universality/undecidability, exact HoTT, HoTT essentiality, natural consumer, same-task reality witness and coverage remain open."

    plan_record = state["records"][PLAN_ID]
    add_once(plan_record.setdefault("related_records", []), RECORD_ID)
    add_once(plan_record["related_records"], SESSION_ID)
    plan_record["revalidation"] = f"{SESSION_ID}: R2 positive semi-halting is proved; the completeness envelope now advances to source-model universality/reduction, R2-UNDEC, R4 and final witness gates."

    coverage = state["records"][COVERAGE_ID]
    add_once(coverage.setdefault("related_records", []), RECORD_ID)
    add_once(coverage["related_records"], SESSION_ID)
    coverage["revalidation"] = f"{SESSION_ID}: R2 positive semi-halting completed; literature coverage remains open, with Post primary and the universality/reduction source theorem now decisive inputs."

    lit = state["records"][LIT_ID]
    add_once(lit.setdefault("related_records", []), RECORD_ID)
    add_once(lit["related_records"], SESSION_ID)
    lit["revalidation"] = f"{SESSION_ID}: shard 006 now records R2-SEMIHALT complete and universality/reduction next. Rosser source status is unchanged; Post and comprehensive citation coverage remain open."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：R2-SEMIHALT-001。
- proof/claims：`{PROOF_ID}` / C-203–C-207。
- 实现：有限 stage partial answer、正答案持续、精确步／bounded bridge、`CodeHalts ↔ SemiReturns`、公平正见证枚举与 controls。
- run：`{RUN_ID}`；Agda 2.8.0-3d04bac + Cubical v0.9；exit 0、stderr 0、零 warning。
- 证据：1 proof + 5 claim 行冻结；`verify_formal_proof_run.py --rerun` exact match。
- 边界：具体 loop 的全阶段不返回不等于 universal undecidability；universality/reduction、R4、HoTT essentiality、natural consumer 与现实 bridge 均 OPEN。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
- 下一步：`R2-UNIVERSALITY-001` 源模型／归约资格化，并交替补 Post 与 HoTT computability 文献。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "proof": {
            "proof_id": PROOF_ID,
            "claim_ids": CLAIM_IDS,
            "run_id": RUN_ID,
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "exit_code": 0,
            "stderr_bytes": 0,
            "source_files": 8,
            "external_dependencies": 5,
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_rows": 6,
            "index_row_manifest_sha256": R.sha((ROOT / f"{RUN}/index-row-manifest.json").read_bytes()),
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
            "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        },
        "version_closure": {
            "status": "BLOCKED_EXPECTED_LOCAL_UNCOMMITTED",
            "first_blocker": "MachineHalting.agda not known to git; R1/R2 packages remain local uncommitted",
        },
        "next": "R2-UNIVERSALITY-001",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, AUDIT, f"{RUN}/RUN.json"],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_R2_SEMIHALT",
        "path": session_path,
        "related_records": [PREV, RECORD_ID, GOAL_ID],
        "scope": "Register the R2 positive semi-halting package and route the next bounded unit to universality/reduction qualification.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[lessons_path] = lessons
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Continue the active machine-overview goal by proving R2 positive semi-halting and advancing to the declared universality/reduction and literature work.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 143,
        "session_id": SESSION_ID,
        "files": len(texts),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
