#!/usr/bin/env python3
"""Prepare revision 135: register the main-project R1 fixed-machine proof."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260914-135-R1-FIXED-MACHINE-MAIN"
PREV = "S-GOV-20260914-134-LIT-HYDRATION-REPIN"
RECORD_ID = "A-CUBICAL-MACHINE-HALTING-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
PROOF_GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
PROOF_ID = "MP-CUBICAL-MACHINE-HALTING-001"
CLAIM_IDS = ["C-188", "C-189", "C-190"]
RUN_ID = "20260914-MP-CUBICAL-MACHINE-HALTING-001-01"
SOURCE = "HoTT/formal/cubical-machine-halting/MachineHalting.agda"
CLAIM = "HoTT/formal/cubical-machine-halting/CLAIM.md"
RUN = f"HoTT/verification/runs/{RUN_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
TOOLCHAIN = "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/partiality-race-timeout/AGDA_LIBRARIES"
AUDIT = "audit/R1固定机器主库重放与边界判定-20260914.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
STATUS = "CORE_GENERATION_4_R1_FIXED_MACHINE_MAIN_PROVED_R2_PROGRAMCODE_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s135", RUNTIME_PATH)
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
        "KC-000010": "把固定对象程序的发散明确限定为 R1 校准，未冒充现实相对非现实性结论。",
        "KC-000012": "ASK 的计算合法性被拆成固定程序性质与覆盖全部程序的统一判定；后者仍归 R2。",
        "KC-000013": "本轮证明对象程序发散，同时证明 kernel 检查正常完成，避免把两个计算层混同。",
        "KC-000021": "源码、工具链、run、stdout/stderr、索引行和 exact replay 已形成 F-011 证据链。",
        "KC-000024": "不可停机路线推进到 main 中机器证明的固定程序层；通用不可判定与 exact HoTT 仍开放。",
        "KC-000027": "HoTT 代码框架已承载对象机停机命题；下一步须加入有限程序语法与通用有界解释器。",
        "KC-000028": "本轮没有把自反真理验证归约为一个显然循环；真正的自应用／统一判定义务留给 R2–R4。",
        "KC-000036": "Gödel 不完备性未由 R1 得出；程序编码、可证性表示、反射和 exact calculus 义务保持显式。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮完成 R1 固定机器主库重放，未找到最终 HoTT 悖论。", "",
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
            "R2、exact HoTT、自然 consumer、现实同任务桥梁与全文学术覆盖仍开放。 |"
        )
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — R1 转完成，当前焦点转 R2 ProgramCode。",
        "- panorama_change: YES_IN_PLACE — 新增 OUT-TOP-R1-FIXED-MACHINE-001。",
        "- essay_change: NO。",
        "- program_plan_change: YES_IN_PLACE — 第 005/006 片更新 R1 main 证据状态与下一顺序。",
        "- update_decision: R1 进入当前主库形式证据；研究队列转向 R2-PROGRAMCODE-001。",
        "- cross_conflicts: 对象程序不停止而 Agda 检查正常结束；二者不是同一计算事件。",
        "- unresolved: R2 ProgramCode/公平枚举/不可判定归约、R4 exact HoTT、自然 consumer、现实同任务桥梁、primary corpus review。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        SOURCE, CLAIM, MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README,
        TOOLCHAIN, LIBRARIES, AUDIT, PROGRAM_005, PROGRAM_006,
        f"{RUN}/RUN.json", f"{RUN}/stdout.txt", f"{RUN}/stderr.txt",
        f"{RUN}/environment.txt", f"{RUN}/source-manifest.json", f"{RUN}/index-row-manifest.json",
    ]
    if any(not (ROOT / rel).is_file() for rel in required):
        raise SystemExit("R1_EVIDENCE_MISSING")
    run = json.loads((ROOT / f"{RUN}/RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != CLAIM_IDS
        or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("exit_code") != 0
        or run.get("stderr", {}).get("bytes") != 0
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
    ):
        raise SystemExit("R1_RUN_NOT_FINAL")
    frozen = json.loads((ROOT / f"{RUN}/index-row-manifest.json").read_text(encoding="utf-8"))
    if frozen.get("proof_id") != PROOF_ID or frozen.get("claim_ids") != CLAIM_IDS or len(frozen.get("rows", [])) != 4:
        raise SystemExit("R1_INDEX_ROWS_NOT_FROZEN")

    plan = R.plan(ROOT, profile="research")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 134 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_134_S134")
    if RECORD_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("R1_RECORD_ALREADY_EXISTS")

    program_005 = (ROOT / PROGRAM_005).read_text(encoding="utf-8")
    program_006 = (ROOT / PROGRAM_006).read_text(encoding="utf-8")
    if "`R1_MAIN_MACHINE_PROVED / R2_OPEN`" not in program_005:
        raise SystemExit("PROGRAM_005_R1_STATUS_NOT_UPDATED")
    if (
        "/ R1_MACHINE_PROVED_IN_MAIN_WITH_F011" not in program_006
        or "`MACHINE_PROVED_IN_MAIN_WITH_F011`" not in program_006
        or "下一步进入 `R2-PROGRAMCODE-001`" not in program_006
    ):
        raise SystemExit("PROGRAM_006_R1_STATUS_NOT_UPDATED")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 为唯一工作面推进基于计算合法性／不可停机代码的 HoTT 悖论探索；R1 固定机器已机器闭合，继续完成 R2、exact HoTT Gödel 与现实桥梁 | 用户 2026-09-14 当前指令与 active goal；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-COMPUTABILITY-CONTINUITY-AUDIT`、`OUT-TOP-LIT-DENOMINATOR-001`、`OUT-TOP-R1-FIXED-MACHINE-001` | 当前做 `R2-PROGRAMCODE-001`；完成程序语法／decoder／bounded evaluator 薄链后返回 `LIT-CLASSICS-001`；R2 通用不可判定、R4 与现实桥梁仍开放 | active goal；项目程序化探索规划第 005/006 片；`audit/R1固定机器主库重放与边界判定-20260914.md` |",
    )
    for old, new in (
        ("source_state_revision: 134", "source_state_revision: 135"),
        ("projection_generation: 20260914-direction-116", "projection_generation: 20260914-direction-117"),
        ("semantic_status: CORE_GENERATION_4_LIT_DENOMINATOR_V1_FROZEN_R1_MAIN_REPLAY_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_LIT_DENOMINATOR_V1_FROZEN_R1_MAIN_REPLAY_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.append_to_shard(
        panorama,
        "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-TOP-R1-FIXED-MACHINE-001` | Cubical Agda 固定双计数器程序校准：停机正控制、固定循环逐有限步不终止、无截断有限停机见证 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 main 的 `MP-CUBICAL-MACHINE-HALTING-001` / C-188–C-190 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R1_FIXED_MACHINE_CALIBRATION_COMPLETE / R2_OPEN` | Agda 2.8.0-3d04bac + Cubical v0.9，exit 0、stderr 0；proof+3 claim 行冻结；`--rerun` exact stdout/stderr/exit match；对象循环不停止而 kernel 检查正常完成 | 不推出通用停机不可判定、通用机、Gödel、HoTT 特有发散、自然 consumer、现实同任务桥梁或 HoTT 矛盾 | `HoTT/formal/cubical-machine-halting/CLAIM.md`；`HoTT/verification/runs/20260914-MP-CUBICAL-MACHINE-HALTING-001-01/RUN.json`；`audit/R1固定机器主库重放与边界判定-20260914.md` |",
    )
    for old, new in (
        ("source_state_revision: 134", "source_state_revision: 135"),
        ("projection_generation: 20260914-outcome-116", "projection_generation: 20260914-outcome-117"),
        ("semantic_status: CORE_GENERATION_4_LIT_DENOMINATOR_V1_FROZEN_R1_MAIN_REPLAY_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_LIT_DENOMINATOR_V1_FROZEN_R1_MAIN_REPLAY_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "3. 当前 Host goal",
        "3. 当前 Host goal 已激活并以 `.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md` 保存 exact objective；R1 固定机器已在 main 形成 `MP-CUBICAL-MACHINE-HALTING-001` / C-188–C-190 / canonical run，并通过 exact replay。它不满足最终 goal 的 HoTT 必要性、自然 consumer 和现实同任务条件；goal 保持 ACTIVE。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "6. 当前仍未得到",
        "6. 当前仍未得到 E6、现实桥梁、`NATURAL_USAGE_MISMATCH`、HoTT-essential 自馈不可停机实例或 HoTT 内部矛盾。17 个冻结 package + 12 个 later package 只支持各自精确范围；最新 R1 包仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "8. `LIT-DENOMINATOR-001`",
        "8. `LIT-DENOMINATOR-001` v1 已冻结；R1 固定对象机 main 重放也已完成。当前下一步是 `R2-PROGRAMCODE-001`（有限程序语法、decoder、universal bounded evaluator 与一致性），形成薄链后返回 `LIT-CLASSICS-001`；随后推进公平枚举与通用不可判定。不 push、不 tag。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S135 R1 固定机器主库重放：从只读 contributor 逐字节取得 `MachineHalting.agda`（3,094 bytes，SHA-256 `c53089ec…`），在 main 分配 `MP-CUBICAL-MACHINE-HALTING-001` / C-188–C-190 / run `20260914-MP-CUBICAL-MACHINE-HALTING-001-01`。Agda 2.8.0 + Cubical v0.9：exit 0、stderr 0；四条索引行冻结；独立 `--rerun` 为 exact exit/stdout/stderr match。证明固定正控制停机、固定循环逐有限步不终止及无截断停机见证；kernel 检查自身正常完成。判词 `R1_FIXED_MACHINE_CALIBRATION_COMPLETE / R2_OPEN`，不是通用不可判定、Gödel 或最终 HoTT 悖论。下一步 R2 ProgramCode。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S130 主项目单工作面与计算合法性）", "# HoTT 研究前沿（S135 R1 固定机器主库重放完成）")
    frontier = replace_once(
        frontier,
        "`LIT-DENOMINATOR-001` v1 已冻结：18×2 discovery、1,941 candidates、32/164/1,745 total triage、33 seed 13 exact/20 manual。全文/citation/场馆与 primary qualification 仍 OPEN。当前第一工作包转为 R1 main 独立重放；闭合后做 `R2-PROGRAMCODE-001`，随后返回 `LIT-CLASSICS-001`。R2 universal halting undecidability、exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
        "`LIT-DENOMINATOR-001` v1 已冻结。R1 固定机器现已在 main 以 `MP-CUBICAL-MACHINE-HALTING-001` / C-188–C-190 通过 F-011 与 exact replay；对象循环不停止，Agda 检查自身正常完成。当前第一工作包是 `R2-PROGRAMCODE-001`；完成程序语法／decoder／bounded evaluator 薄链后返回 `LIT-CLASSICS-001`。通用停机不可判定、公平枚举、exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS135：R1 固定机器已在 main 通过 F-011。证明包 `MP-CUBICAL-MACHINE-HALTING-001` / C-188–C-190；run `20260914-MP-CUBICAL-MACHINE-HALTING-001-01` exit 0、stderr 0、索引四行冻结、exact replay。对象循环发散不等于 proof checker 发散，也不等于通用不可判定或 HoTT 悖论。下一步直接做 `R2-PROGRAMCODE-001`，然后回 `LIT-CLASSICS-001`。\n\n",
    )

    state["revision"] = 135
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R1_FIXED_MACHINE_MAIN"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Implement R2-PROGRAMCODE-001 in main: finite ProgramCode syntax, total decoder, universal bounded evaluator, semantic agreement and positive/negative controls; then return to LIT-CLASSICS-001."
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-117"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = STATUS
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-117"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = STATUS

    evidence = [
        SOURCE, CLAIM, TOOLCHAIN, LIBRARIES, f"{RUN}/RUN.json", f"{RUN}/source-manifest.json",
        f"{RUN}/index-row-manifest.json", f"{RUN}/stdout.txt", f"{RUN}/stderr.txt",
        f"{RUN}/environment.txt", MATRIX, REGISTRY, AUDIT,
        "scripts/audit/capture_agda_proof_run.py", "scripts/audit/mark_proof_run_indexed.py",
        "scripts/audit/freeze_proof_index_rows.py", "scripts/audit/verify_formal_proof_run.py",
    ]
    state["records"][RECORD_ID] = {
        "claim_ids": CLAIM_IDS,
        "classification": "FIXED_MACHINE_HALTING_DIVERGENCE_CALIBRATION",
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": evidence,
        "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT",
        "mathematical_status": "R1_FIXED_MACHINE_CALIBRATION_COMPLETE_R2_OPEN",
        "path": SOURCE,
        "proof_id": PROOF_ID,
        "research_parent": GOAL_ID,
        "related_records": [PROOF_GATE_ID, PLAN_ID, COVERAGE_ID, SESSION_ID],
        "resolution": {
            "evidence": [f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", MATRIX, AUDIT],
            "reason": "Current-main Cubical Agda run exited 0 with stderr 0; proof and three claim rows are frozen; exact command replay matched exit/stdout/stderr. The result is deliberately limited to one halting and one looping program."
        },
        "run_id": RUN_ID,
        "scope": "R1 fixed-machine calibration in Cubical Agda: haltProgram has a truncated finite halting witness (C-188); loopProgram is non-final at every finite observation index (C-189) and has no truncated finite halting witness (C-190). The checker run itself terminates. No universal undecidability, Goedel theorem, HoTT-essential mechanism, natural consumer or reality bridge.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in evidence},
        "status": "complete",
        "version_closure": {
            "registry": REGISTRY,
            "scope_preserved": True,
            "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"
        },
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
    goal["revalidation"] = f"{SESSION_ID}: R1 fixed-machine proof completed in main; goal remains active because R2/R4, HoTT essentiality, natural consumer, same-reality-task witness and primary corpus review remain open."
    plan_record = state["records"][PLAN_ID]
    for rel in [PROGRAM_005, PROGRAM_006]:
        add_once(plan_record["full_sources"], rel)
        plan_record["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
    add_once(plan_record.setdefault("related_records", []), RECORD_ID)
    plan_record["revalidation"] = f"{SESSION_ID}: R1 status advanced from contributor evidence to main F-011 proof; completeness envelope unchanged and R2 remains open."
    coverage = state["records"][COVERAGE_ID]
    add_once(coverage.setdefault("related_records", []), RECORD_ID)
    coverage["revalidation"] = f"{SESSION_ID}: R1 main proof completed; R2, exact HoTT, reality bridge and comprehensive primary-corpus coverage remain open."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：把只读 contributor 的固定机器候选在 main 以新身份独立重放并闭合 F-011。
- proof/claims：`{PROOF_ID}` / `C-188`–`C-190`。
- run：`{RUN_ID}`；Agda 2.8.0-3d04bac + Cubical v0.9；exit 0、stderr 0。
- 索引：1 proof + 3 claim 行冻结；`verify_formal_proof_run.py --rerun` exact exit/stdout/stderr match。
- 数学范围：固定 halt 正控制、固定 loop 逐有限步不终止、无截断有限停机见证。
- 判词：`R1_FIXED_MACHINE_CALIBRATION_COMPLETE / R2_OPEN`；不是通用不可判定、Gödel、HoTT-essential 机制或现实相对悖论。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
- 下一步：`R2-PROGRAMCODE-001`，然后 `LIT-CLASSICS-001`。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "run_id": RUN_ID,
        "kernel": {"status": "KERNEL_ACCEPTED_WITH_SCOPE", "exit_code": 0, "stderr_bytes": 0},
        "index_rows": 4,
        "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "next": "R2-PROGRAMCODE-001",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, AUDIT, f"{RUN}/RUN.json"],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, RECORD_ID, GOAL_ID],
        "scope": "Register the main-project R1 fixed-machine proof and route the active work to R2-PROGRAMCODE-001.",
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
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Advance the active user goal by completing the main-project R1 fixed-machine proof and continuing to R2.",
        "load_profile": "research",
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
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 135, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
