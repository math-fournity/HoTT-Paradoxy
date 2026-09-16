#!/usr/bin/env python3
"""Prepare revision 137: register the R2 ProgramCode bounded-evaluator slice."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260914-137-R2-PROGRAMCODE-THIN-SLICE"
PREV = "S-GOV-20260914-136-R1-HYDRATION-REPIN"
RECORD_ID = "A-CUBICAL-PROGRAM-CODE-001"
R1_ID = "A-CUBICAL-MACHINE-HALTING-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
PROOF_GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
PROOF_ID = "MP-CUBICAL-PROGRAM-CODE-001"
CLAIM_IDS = ["C-191", "C-192", "C-193", "C-194"]
RUN_ID = "20260914-MP-CUBICAL-PROGRAM-CODE-001-01"
SOURCE = "HoTT/formal/cubical-machine-halting/ProgramCode.agda"
PARENT_SOURCE = "HoTT/formal/cubical-machine-halting/MachineHalting.agda"
CLAIM = "HoTT/formal/cubical-machine-halting/CLAIM-R2-PROGRAMCODE.md"
RUN = f"HoTT/verification/runs/{RUN_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
TOOLCHAIN = "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/partiality-race-timeout/AGDA_LIBRARIES"
AUDIT = "audit/R2有限程序与有界解释器机器证明-20260914.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
STATUS = "CORE_GENERATION_4_R2_PROGRAMCODE_THIN_SLICE_PROVED_LIT_CLASSICS_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s137", RUNTIME_PATH)
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
        "KC-000002": "Theory Schema 从函数空间程序推进到有限 ProgramCode、decoder、step 与 bounded observation 的显式组合。",
        "KC-000010": "本轮仍以现实相对目标为完成标准；ProgramCode 基础没有被误晋升为最终悖论。",
        "KC-000012": "ASK 的计算合法性获得可执行前置：所有有限表共享 bounded evaluator；无界是否停机仍不可由 fuel 自动回答。",
        "KC-000013": "区分‘给定 fuel 必结束’与‘统一判断是否存在停机 fuel’，明确理论工具不能偷换量词。",
        "KC-000021": "C-191–C-194 已有原生 kernel、完整 source manifest、索引冻结和 exact replay。",
        "KC-000024": "不可停机路线新增有限程序语法与统一 bounded execution；公平枚举和不可判定归约仍开放。",
        "KC-000027": "HoTT 代码框架现在可解释任意有限指令表，但计算通用性与 HoTT 必要性尚未建立。",
        "KC-000028": "自馈／自应用没有被静态 ProgramCode 自动获得；需要自然数编码、代码变换和通用性。",
        "KC-000036": "ProgramCode 是 Gödel 路线的前置编码层之一，尚无证明代码、反射、fixed point 或 exact HoTT 不完备性。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮完成 R2 ProgramCode 第一薄层，通用不可判定与最终悖论仍开放。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{AUDIT}`；{kid} | 数值编码、公平枚举、通用性、不可判定、R4、自然 consumer 与现实桥梁仍开放。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — ProgramCode 薄层完成，下一有界单元转 LIT-CLASSICS-001。",
        "- panorama_change: YES_IN_PLACE — 新增 OUT-TOP-R2-PROGRAMCODE-001。",
        "- essay_change: NO。",
        "- update_decision: R2 基础登记为机器证明，但 R2 不可判定整体保持 OPEN。",
        "- cross_conflicts: bounded evaluator 的总性与 halting decider 的总性量词不同；前者不能冒充后者。",
        "- unresolved: numeric code/enumeration、fairness、universality/reduction、second kernel、exact HoTT、natural consumer、reality bridge、primary corpus review。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    required = [
        SOURCE, PARENT_SOURCE, CLAIM, MATRIX, REGISTRY, FORMAL_README, RUNS_README,
        HOTT_README, TOOLCHAIN, LIBRARIES, AUDIT, PROGRAM_005, PROGRAM_006,
        f"{RUN}/RUN.json", f"{RUN}/stdout.txt", f"{RUN}/stderr.txt",
        f"{RUN}/environment.txt", f"{RUN}/source-manifest.json", f"{RUN}/index-row-manifest.json",
    ]
    if any(not (ROOT / rel).is_file() for rel in required):
        raise SystemExit("R2_PROGRAMCODE_EVIDENCE_MISSING")
    run = json.loads((ROOT / f"{RUN}/RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != CLAIM_IDS
        or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("exit_code") != 0
        or run.get("stderr", {}).get("bytes") != 0
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
    ):
        raise SystemExit("R2_PROGRAMCODE_RUN_NOT_FINAL")
    frozen = json.loads((ROOT / f"{RUN}/index-row-manifest.json").read_text(encoding="utf-8"))
    if frozen.get("claim_ids") != CLAIM_IDS or len(frozen.get("rows", [])) != 5:
        raise SystemExit("R2_PROGRAMCODE_INDEX_ROWS_NOT_FROZEN")
    if "PROGRAMCODE_THIN_SLICE_MACHINE_PROVED" not in (ROOT / PROGRAM_005).read_text(encoding="utf-8"):
        raise SystemExit("PROGRAM_005_NOT_UPDATED")
    if "R2_PROGRAMCODE_THIN_SLICE_MACHINE_PROVED" not in (ROOT / PROGRAM_006).read_text(encoding="utf-8"):
        raise SystemExit("PROGRAM_006_NOT_UPDATED")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 136 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_136_S136")
    if RECORD_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("R2_PROGRAMCODE_RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 为唯一工作面推进基于计算合法性／不可停机代码的 HoTT 悖论探索；R1 与 R2 ProgramCode 第一薄层已机器闭合，继续公平枚举、不可判定、exact HoTT Gödel 与现实桥梁 | 用户 2026-09-14 当前指令与 active goal；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-COMPUTABILITY-CONTINUITY-AUDIT`、`OUT-TOP-LIT-DENOMINATOR-001`、`OUT-TOP-R1-FIXED-MACHINE-001`、`OUT-TOP-R2-PROGRAMCODE-001` | 当前做 `LIT-CLASSICS-001`；随后回到 ProgramCode 数值编码／枚举、`R2-FAIR-001` 与 certified undecidability；R4 与现实桥梁仍开放 | active goal；项目程序化探索规划第 005/006 片；`audit/R2有限程序与有界解释器机器证明-20260914.md` |",
    )
    for old, new in (
        ("source_state_revision: 136", "source_state_revision: 137"),
        ("projection_generation: 20260914-direction-118", "projection_generation: 20260914-direction-119"),
        ("semantic_status: CORE_GENERATION_4_R1_FIXED_MACHINE_MAIN_PROVED_R2_PROGRAMCODE_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R1_FIXED_MACHINE_MAIN_PROVED_R2_PROGRAMCODE_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.append_to_shard(
        panorama,
        "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-TOP-R2-PROGRAMCODE-001` | R2 第一薄层：有限双计数器 ProgramCode、总 decoder、任意 fuel／程序表上的 universal bounded evaluator、R1 语义一致性与 halt/loop controls | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 main 的 `MP-CUBICAL-PROGRAM-CODE-001` / C-191–C-194 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_PROGRAMCODE_THIN_SLICE_COMPLETE / R2_UNDECIDABILITY_OPEN` | Agda 2.8.0-3d04bac + Cubical v0.9，exit 0、stderr 0；proof+4 claim 行冻结；`--rerun` exact match；source manifest 含父语义 | 不含自然数 Gödel code、公平枚举、语言通用性、certified undecidability、Gödel、HoTT essentiality、自然 consumer、现实桥梁或内部矛盾 | `HoTT/formal/cubical-machine-halting/CLAIM-R2-PROGRAMCODE.md`；`HoTT/verification/runs/20260914-MP-CUBICAL-PROGRAM-CODE-001-01/RUN.json`；`audit/R2有限程序与有界解释器机器证明-20260914.md` |",
    )
    for old, new in (
        ("source_state_revision: 136", "source_state_revision: 137"),
        ("projection_generation: 20260914-outcome-118", "projection_generation: 20260914-outcome-119"),
        ("semantic_status: CORE_GENERATION_4_R1_FIXED_MACHINE_MAIN_PROVED_R2_PROGRAMCODE_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R1_FIXED_MACHINE_MAIN_PROVED_R2_PROGRAMCODE_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "3. 当前 Host goal",
        "3. 当前 Host goal 保持 ACTIVE。R1 已闭合；R2 第一薄层现有 `MP-CUBICAL-PROGRAM-CODE-001` / C-191–C-194：有限 ProgramCode、总 decoder、universal bounded evaluator、一致性与 controls 均机器通过。数值编码／公平枚举／通用性／不可判定、HoTT 必要性、自然 consumer 和现实同任务条件仍开放。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "6. 当前仍未得到",
        "6. 当前仍未得到 E6、现实桥梁、`NATURAL_USAGE_MISMATCH`、HoTT-essential 自馈不可停机实例或 HoTT 内部矛盾。17 个冻结 package + 13 个 later package 只支持各自精确范围；最新 R1/R2 包仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "8. `LIT-DENOMINATOR-001`",
        "8. `LIT-DENOMINATOR-001` v1、R1 与 R2 ProgramCode 第一薄层已完成。当前转 `LIT-CLASSICS-001`，冻结 Turing／Church／Gödel／Kleene 等一手前提和可执行归约接口；随后回 ProgramCode 数值编码／枚举与 `R2-FAIR-001`。不 push、不 tag。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S137 R2 ProgramCode 第一薄层：新增 `ProgramCode.agda` 与 `MP-CUBICAL-PROGRAM-CODE-001` / C-191–C-194。有限指令表、表外 halt 的总 decoder、任意有限 fuel 上总结束的 universal bounded evaluator、与 R1 iterate/finality 一致，以及 halt/loop controls 均由 Agda 2.8.0 + Cubical v0.9 接受；run exit 0、stderr 0，五条索引行冻结，exact replay。bounded evaluator 不回答是否存在任意停机步；numeric code/fairness/universality/undecidability 保持 OPEN。下一步 `LIT-CLASSICS-001`。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S135 R1 固定机器主库重放完成）", "# HoTT 研究前沿（S137 R2 ProgramCode 第一薄层完成）")
    frontier = replace_once(
        frontier,
        "`LIT-DENOMINATOR-001` v1 已冻结。R1 固定机器现已在 main 以 `MP-CUBICAL-MACHINE-HALTING-001` / C-188–C-190 通过 F-011 与 exact replay；对象循环不停止，Agda 检查自身正常完成。当前第一工作包是 `R2-PROGRAMCODE-001`；完成程序语法／decoder／bounded evaluator 薄链后返回 `LIT-CLASSICS-001`。通用停机不可判定、公平枚举、exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
        "R1 固定机器与 R2 ProgramCode 第一薄层均已在 main 通过 F-011。后者以 C-191–C-194 给出有限程序表、总 decoder、universal bounded evaluator、R1 一致性与 controls；它仍没有 numeric code、fair enumeration、universality 或 undecidability。当前第一工作包转为 `LIT-CLASSICS-001`；随后返回 ProgramCode 编码／枚举与 `R2-FAIR-001`。exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS137：R2 ProgramCode 第一薄层已在 main 通过 F-011。`MP-CUBICAL-PROGRAM-CODE-001` / C-191–C-194；run exit 0、stderr 0、五行冻结、exact replay。已完成有限表／decoder／bounded evaluator／一致性／controls；numeric code、公平枚举、通用性和不可判定仍 OPEN。下一步 `LIT-CLASSICS-001`，之后返回 R2。\n\n",
    )

    state["revision"] = 137
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R2_PROGRAMCODE_THIN_SLICE"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Execute LIT-CLASSICS-001: qualify primary Turing/Church/Goedel/Kleene sources and extract exact machine/reduction premises; then return to numeric ProgramCode enumeration and R2-FAIR-001."
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-119"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = STATUS
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-119"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = STATUS

    evidence = [
        SOURCE, PARENT_SOURCE, CLAIM, TOOLCHAIN, LIBRARIES,
        f"{RUN}/RUN.json", f"{RUN}/source-manifest.json", f"{RUN}/index-row-manifest.json",
        f"{RUN}/stdout.txt", f"{RUN}/environment.txt", MATRIX, REGISTRY, AUDIT,
        "scripts/audit/capture_agda_proof_run.py", "scripts/audit/mark_proof_run_indexed.py",
        "scripts/audit/freeze_proof_index_rows.py", "scripts/audit/verify_formal_proof_run.py",
    ]
    state["records"][RECORD_ID] = {
        "claim_ids": CLAIM_IDS,
        "classification": "R2_PROGRAMCODE_BOUNDED_EVALUATOR_FOUNDATION",
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": evidence,
        "kind": "formal_mathematical_result", "lifecycle_status": "CURRENT",
        "mathematical_status": "R2_PROGRAMCODE_THIN_SLICE_COMPLETE_UNDECIDABILITY_OPEN",
        "path": SOURCE, "proof_id": PROOF_ID, "research_parent": GOAL_ID,
        "related_records": [PROOF_GATE_ID, R1_ID, PLAN_ID, COVERAGE_ID, SESSION_ID],
        "resolution": {
            "evidence": [f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", MATRIX, AUDIT],
            "reason": "Native Cubical Agda run exited 0 with stderr 0; proof and four claim rows are frozen; exact replay matched. The theorem covers finite syntax, bounded evaluation and controls, while numeric enumeration, universality and undecidability remain explicit obligations."
        },
        "run_id": RUN_ID,
        "scope": "R2 ProgramCode thin slice in Cubical Agda: finite instruction-table syntax and total decoder (C-191); a bounded evaluator for every finite table with agreement to R1 iteration/finality (C-192); a halting control (C-193); and a loop control with no truncated finite halting witness (C-194). No numeric coding, fair enumeration, computational universality, certified undecidability, Goedel theorem, HoTT essentiality, natural consumer or reality bridge.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in evidence},
        "status": "complete",
        "version_closure": {"registry": REGISTRY, "scope_preserved": True, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"},
    }
    changed_hash_paths = [MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README]
    for record in state["records"].values():
        hashes = record.get("source_hashes")
        if not isinstance(hashes, dict):
            continue
        for rel in changed_hash_paths:
            if rel in hashes:
                hashes[rel] = R.sha((ROOT / rel).read_bytes())
    goal = state["records"][GOAL_ID]
    add_once(goal.setdefault("related_records", []), RECORD_ID)
    goal["revalidation"] = f"{SESSION_ID}: R2 ProgramCode bounded-evaluator slice completed; goal remains active because numeric/fair/universal undecidability, R4, HoTT essentiality, natural consumer, reality witness and primary corpus review remain open."
    plan_record = state["records"][PLAN_ID]
    for rel in [PROGRAM_005, PROGRAM_006]:
        plan_record["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
    add_once(plan_record.setdefault("related_records", []), RECORD_ID)
    plan_record["revalidation"] = f"{SESSION_ID}: finite ProgramCode/decoder/bounded evaluator slice proved; R2 undecidability and completeness envelope remain open."
    coverage = state["records"][COVERAGE_ID]
    add_once(coverage.setdefault("related_records", []), RECORD_ID)
    coverage["revalidation"] = f"{SESSION_ID}: R2 bounded-evaluator foundation completed; next alternation is LIT-CLASSICS-001, while R2 undecidability and comprehensive coverage remain open."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：R2-PROGRAMCODE-001 第一薄层。
- proof/claims：`{PROOF_ID}` / C-191–C-194。
- 实现：有限 ProgramCode、总 decoder、universal bounded evaluator、R1 一致性、halt/loop controls。
- run：`{RUN_ID}`；Agda 2.8.0-3d04bac + Cubical v0.9；exit 0、stderr 0。
- 证据：1 proof + 4 claim 行冻结；`verify_formal_proof_run.py --rerun` exact match。
- 边界：numeric code/fair enumeration/universality/undecidability、Gödel、HoTT essentiality、自然 consumer、现实 bridge 均 OPEN。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
- 下一步：`LIT-CLASSICS-001`，然后返回 R2 编码／公平枚举。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL, "proof_id": PROOF_ID, "claim_ids": CLAIM_IDS,
        "run_id": RUN_ID, "kernel": {"status": "KERNEL_ACCEPTED_WITH_SCOPE", "exit_code": 0, "stderr_bytes": 0},
        "index_rows": 5, "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "next": "LIT-CLASSICS-001",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, AUDIT, f"{RUN}/RUN.json"],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, RECORD_ID, GOAL_ID],
        "scope": "Register the R2 ProgramCode bounded-evaluator slice and route the next alternation to LIT-CLASSICS-001.",
        "source_hashes": {}, "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "Advance the active goal by machine-proving the R2 ProgramCode bounded-evaluator slice and continuing with the declared literature/implementation alternation.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 137, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
