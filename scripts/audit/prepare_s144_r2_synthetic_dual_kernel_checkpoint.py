#!/usr/bin/env python3
"""Prepare revision 144: R2 synthetic reduction and dual-kernel correspondence."""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260914-144-R2-SYNTHETIC-DUAL-KERNEL"
PREV = "S-RES-20260914-143-R2-SEMIHALT"
STATUS = "CORE_GENERATION_4_R2_SYNTHETIC_DUAL_KERNEL_COMPLETE_INTERNAL_UNDEC_R3_R4_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

OLD_GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_ID = "A-LIT-CLASSICS-001"
PROOF_GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
SEMI_ID = "A-CUBICAL-SEMI-HALTING-001"
SOURCE_ID = "A-COQ-MM2-SOURCE-QUALIFICATION-001"
COQ_SEED_ID = "A-COQ-MM2-UNDECIDABILITY-REPLAY-001"
AGDA_BRIDGE_ID = "A-CUBICAL-MM2-BRIDGE-001"
COQ_BRIDGE_ID = "A-COQ-MM2-PROGRAMCODE-BRIDGE-001"
CROSS_ID = "A-R2-CROSS-KERNEL-CORRESPONDENCE-001"

GOAL = "goal.md"
GOAL_COMPAT = ".codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
LIT_SHARD = ".codex/research/hott/LIT-CLASSICS-001/006 - 当前判词、缺口与下一机器工作包.md"
README_SHARD = "README/001 - 当前入口与关键文件.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
FEATURE = "feature-list.md"

COQ_ROOT = "HoTT/formal/external-coq-mm2"
COQ_SEED_PROOF = "MP-COQ-MM2-UNDECIDABILITY-REPLAY-001"
COQ_SEED_CLAIMS = ["C-208"]
COQ_SEED_RUN_ID = "20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01"
COQ_SEED_RUN = f"HoTT/verification/runs/{COQ_SEED_RUN_ID}"
AGDA_BRIDGE_PROOF = "MP-CUBICAL-MM2-BRIDGE-001"
AGDA_BRIDGE_CLAIMS = ["C-209", "C-210", "C-211", "C-212", "C-213"]
AGDA_BRIDGE_RUN_ID = "20260914-MP-CUBICAL-MM2-BRIDGE-001-01"
AGDA_BRIDGE_RUN = f"HoTT/verification/runs/{AGDA_BRIDGE_RUN_ID}"
COQ_BRIDGE_PROOF = "MP-COQ-MM2-PROGRAMCODE-BRIDGE-001"
COQ_BRIDGE_CLAIMS = ["C-214", "C-215", "C-216", "C-217", "C-218"]
COQ_BRIDGE_RUN_ID = "20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01"
COQ_BRIDGE_RUN = f"HoTT/verification/runs/{COQ_BRIDGE_RUN_ID}"

SOURCE_AUDIT = "audit/R2通用性源模型资格化-20260914.md"
AGDA_AUDIT = "audit/R2-MM2编译桥机器证明-20260914.md"
COQ_AUDIT = "audit/R2-Coq-MM2同核归约机器证明-20260914.md"
CROSS_SPEC = "HoTT/formal/cubical-machine-halting/R2-TASKSPEC.json"
CROSS_DOC = "HoTT/formal/cubical-machine-halting/R2-CROSS-KERNEL-CORRESPONDENCE.md"
CROSS_RECEIPT = "audit/R2-cross-kernel-correspondence-20260914.json"
CROSS_VERIFIER = "scripts/audit/verify_r2_cross_kernel_correspondence.py"
PREPARE = "scripts/audit/prepare_s144_r2_synthetic_dual_kernel_checkpoint.py"

SPEC = importlib.util.spec_from_file_location("runtime_s144", RUNTIME_PATH)
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
    matches = [index for index, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def run_assets(run: str) -> list[str]:
    return [
        f"{run}/RUN.json", f"{run}/source-manifest.json",
        f"{run}/index-row-manifest.json", f"{run}/stdout.txt",
        f"{run}/stderr.txt", f"{run}/environment.txt",
    ]


def assert_run(run: str, proof: str, claims: list[str], frozen_rows: int) -> dict:
    value = json.loads((ROOT / f"{run}/RUN.json").read_text(encoding="utf-8"))
    frozen = json.loads((ROOT / f"{run}/index-row-manifest.json").read_text(encoding="utf-8"))
    if (
        value.get("proof_id") != proof
        or value.get("claim_ids") != claims
        or value.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or value.get("exit_code") != 0
        or value.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or frozen.get("claim_ids") != claims
        or len(frozen.get("rows", [])) != frozen_rows
    ):
        raise SystemExit(f"PROOF_RUN_NOT_FINAL:{proof}")
    return value


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "Theory Schema 已把外部关系机、Coq 显式 target、Agda 函数式源与 ProgramCode 分为四模型并固定 correspondence。",
        "KC-000010": "R2 synthetic reduction 被严格登记为一般计算机制；最终 HoTT 现实相对见证仍未找到。",
        "KC-000012": "ASK 在本轮出现为定义前提：synthetic `undecidable` 不能绕过对 complement enumerability／CT/EPF 的询问。",
        "KC-000013": "有限 stage、关系闭包与停机存在量词逐层对齐；普通存在与命题截断的落定顺序差异明确保留。",
        "KC-000021": "C-208–C-218 具有两个 Coq run、一个 Agda run、冻结索引、exact replay 和跨内核 receipt。",
        "KC-000024": "不可停机路线完成 synthetic R2 reduction；内部 no-decider、R3 和 exact HoTT R4 成为下一前沿。",
        "KC-000027": "两 kernel 对同一显式机器 TaskSpec 提供独立证据，但 higher HoTT structure 仍未参与关键 reduction。",
        "KC-000028": "MM2 hardness 不等于对象内自馈；s-m-n、自应用、fixed point 与自然 self-validation consumer 仍开放。",
        "KC-000036": "R2 为 Gödel 路线提供计算底座；proof predicate、representability、exact calculus 与 inner/outer 仍须单独闭合。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮闭合 R2 synthetic dual-kernel reduction，Goal 保持 active。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{SOURCE_AUDIT}`；{kid} | "
            "内部 no-decider、R3/R4、CE-MAP、HoTT essentiality、natural consumer 与现实桥梁仍开放。 |"
        )
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — R2 synthetic dual-kernel 完成，转内部前提、R3/R4 与文献三向薄切。",
        "- panorama_change: YES_IN_PLACE — 新增 Coq seed、Agda bridge、Coq same-kernel reduction 与 cross-kernel correspondence 四项结果。",
        "- essay_change: NO。",
        "- update_decision: 根 goal.md 成为唯一 objective owner；旧 active-goal 路径降为兼容指针。",
        "- cross_conflicts: 上游 `undecidable` 是 implication，不是内部否定；Coq exists 与 Agda truncation 表示不同；跨 kernel 不称 definitional equality。",
        "- unresolved: CT/EPF/representability 或 diagonal、R3 proof code、exact HoTT R4、CE-MAP、Post/HoTT 文献、natural consumer、same-task reality bridge。",
    ]
    return "\n".join(lines) + "\n"


def record_hashes(paths: list[str]) -> dict[str, str]:
    return {path: R.sha((ROOT / path).read_bytes()) for path in paths}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        GOAL, GOAL_COMPAT, PROGRAM_005, PROGRAM_006, LIT_SHARD, README_SHARD,
        MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, FEATURE,
        SOURCE_AUDIT, AGDA_AUDIT, COQ_AUDIT, CROSS_SPEC, CROSS_DOC,
        CROSS_RECEIPT, CROSS_VERIFIER, PREPARE,
        f"{COQ_ROOT}/REPLAY_SOURCE.json", f"{COQ_ROOT}/SOURCE_TREE_MANIFEST.json",
        f"{COQ_ROOT}/DOCKER_IMAGE.json", f"{COQ_ROOT}/CheckMM2Undec.v",
        f"{COQ_ROOT}/MM2ProgramCodeBridge.v", f"{COQ_ROOT}/CLAIM-R2-COQ-MM2-BRIDGE.md",
        "HoTT/formal/cubical-machine-halting/MM2Bridge.agda",
        "HoTT/formal/cubical-machine-halting/CLAIM-R2-MM2-BRIDGE.md",
        *run_assets(COQ_SEED_RUN), *run_assets(AGDA_BRIDGE_RUN), *run_assets(COQ_BRIDGE_RUN),
    ]
    if any(not (ROOT / path).is_file() for path in required):
        raise SystemExit("S144_EVIDENCE_MISSING")
    assert_run(COQ_SEED_RUN, COQ_SEED_PROOF, COQ_SEED_CLAIMS, 2)
    assert_run(AGDA_BRIDGE_RUN, AGDA_BRIDGE_PROOF, AGDA_BRIDGE_CLAIMS, 6)
    assert_run(COQ_BRIDGE_RUN, COQ_BRIDGE_PROOF, COQ_BRIDGE_CLAIMS, 6)
    registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
    if registry.get("later_machine_proved_claim_count") != 70 or len(registry.get("later_packages", [])) != 19:
        raise SystemExit("S144_REGISTRY_COUNT_INVALID")
    cross = json.loads((ROOT / CROSS_RECEIPT).read_text(encoding="utf-8"))
    if (
        cross.get("status") != "PASS_WITH_SCOPE"
        or cross.get("anchors_checked") != 28
        or len(cross.get("formal_packages", [])) != 3
        or cross.get("executable_controls", {}).get("total") != 282
    ):
        raise SystemExit("S144_CROSS_KERNEL_RECEIPT_INVALID")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 143 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_143_S143")
    for identity in (GOAL_ID, SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID):
        if identity in state["records"]:
            raise SystemExit(f"S144_RECORD_ALREADY_EXISTS:{identity}")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][shard] = replace_line(
        direction["shards"][shard], "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 与根 `goal.md` 为唯一工作面推进计算合法性／不可停机／Gödel 到 HoTT 现实相对悖论；R2 synthetic reduction 已双内核闭合，继续内部 no-decider 前提、R3、exact HoTT R4 与现实桥梁 | 用户当前 App Goal；`goal.md`；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-R2-COQ-MM2-SEED-001`、`OUT-TOP-R2-MM2-AGDA-BRIDGE-001`、`OUT-TOP-R2-COQ-SAME-KERNEL-001`、`OUT-TOP-R2-CROSS-KERNEL-001`、`OUT-TOP-LIT-CLASSICS-001` | 当前做 `R2-INTERNAL-UNDEC-001`、`G-HOTT-SYNTAX-001` 与 Post/HoTT computability 文献三向薄切；CE-MAP、natural consumer、R4 与现实 bridge 仍开放 | `goal.md`；C-208–C-218；`audit/R2-cross-kernel-correspondence-20260914.json` |",
    )
    for old, new in (
        ("source_state_revision: 143", "source_state_revision: 144"),
        ("projection_generation: 20260914-direction-125", "projection_generation: 20260914-direction-126"),
        ("semantic_status: CORE_GENERATION_4_R2_SEMIHALT_COMPLETE_UNIVERSALITY_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_SEMIHALT_COMPLETE_UNIVERSALITY_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    target_shard = "全景视野/003 - 当前机器证明包与原生重放.md"
    for row in (
        "| `OUT-TOP-R2-COQ-MM2-SEED-001` | Coq Undecidability Library MM2 seed：777 文件 Git-verified tree 下重放 `MM2_HALTING_undec`，assumptions closed；定义为 synthetic implication | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | C-208 / `MP-COQ-MM2-UNDECIDABILITY-REPLAY-001` | `REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE / LOCAL_UNCOMMITTED` | Coq 8.15.2；exact replay；原 ISO-8859 license 字节保留；两条目标闭包外 coqdep 告警保留 | 不等于无条件 `¬decidable`；不证明 Agda bridge 或 HoTT 悖论 | run `20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01`；`audit/R2通用性源模型资格化-20260914.md` |\n",
        "| `OUT-TOP-R2-MM2-AGDA-BRIDGE-001` | Cubical Agda label-1 MM2→ProgramCode：查表、finality、step、任意有限 run/finalAt 与截断 halting 双向保持 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | C-209–C-213 / `MP-CUBICAL-MM2-BRIDGE-001` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / AGDA_LOCAL_HALTING_EQUIVALENCE` | exit 0、stderr 0、零 warning；6 行冻结；exact replay | 不自动搬运 Coq theorem；无内部 no-decider、HoTT essentiality 或现实 bridge | `MM2Bridge.agda`；run `20260914-MP-CUBICAL-MM2-BRIDGE-001-01` |\n",
        "| `OUT-TOP-R2-COQ-SAME-KERNEL-001` | Coq 同核显式 target：关系 MM2 termination↔finite functional observation；total `MM2_HALTING ⪯ PC_HALTING`；target synthetic-undecidability | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | C-214–C-218 / `MP-COQ-MM2-PROGRAMCODE-BRIDGE-001` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SAME_KERNEL_TOTAL_REDUCTION` | 777 文件干净树；assumptions closed；6 行冻结；exact replay | synthetic implication，不是内部否定；Coq/Agda AST 不称同一 | run `20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01`；`audit/R2-Coq-MM2同核归约机器证明-20260914.md` |\n",
        "| `OUT-TOP-R2-CROSS-KERNEL-001` | 四模型 R2 TaskSpec correspondence：Coq source/target 与 Agda source/target 的 state/instruction/label/branch/finality/halting 对账 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | C-208–C-218 + deterministic correspondence receipt | `VERIFIED_WITH_SCOPE / DUAL_KERNEL_SCOPED_CORRESPONDENCE` | 3 formal packages、28 source anchors、282 executable controls PASS | 有限 controls 不承担全称证明；Coq exists 与 Agda truncation 不同；不主张跨 kernel definitional equality | `R2-TASKSPEC.json`；`R2-CROSS-KERNEL-CORRESPONDENCE.md`；`audit/R2-cross-kernel-correspondence-20260914.json` |\n",
    ):
        projection_edit.append_to_shard(panorama, target_shard, row)
    for old, new in (
        ("source_state_revision: 143", "source_state_revision: 144"),
        ("projection_generation: 20260914-outcome-125", "projection_generation: 20260914-outcome-126"),
        ("semantic_status: CORE_GENERATION_4_R2_SEMIHALT_COMPLETE_UNIVERSALITY_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_SEMIHALT_COMPLETE_UNIVERSALITY_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "3. 当前 Host goal",
        "3. 当前 App Goal 为短指针，根 `goal.md` 是唯一完整 objective owner。R1/R2 C-188–C-218 已在 main 分包通过 F-011：R2 synthetic MM2→显式 target reduction 在 Coq 同核闭合，Agda 有独立 MM2→ProgramCode 停机等价；28 anchors/3 packages/282 controls correspondence PASS。最终 HoTT witness 未找到。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "6. 当前仍未得到",
        "6. 当前仍未得到内部无条件 `¬decidable`、R3 exact independent sentence、R4 exact HoTT incompleteness、E6、现实桥梁、`NATURAL_USAGE_MISMATCH`、HoTT-essential 自馈不可停机实例或 HoTT 内部矛盾。17 个冻结 package + 19 个 later package 只支持各自范围；新资产仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "8. `LIT-DENOMINATOR-001`",
        "8. 文献分母、LIT Classics 与 R2 synthetic dual-kernel 已完成 scoped 增量。当前按 `goal.md` 做三向薄切：`R2-INTERNAL-UNDEC-001` 前提资格化、`G-HOTT-SYNTAX-001`/R3、Post primary + `LIT-HOTT-COMPUTABILITY-001`；随后回 CE-MAP/natural consumer/reality。未获授权不 push、不 tag。",
    )
    memory["index_text"] = replace_once(memory["index_text"], "S023–S143 逐会话记录", "S023–S144 逐会话记录")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S144 R2 synthetic dual-kernel：冻结/重放 Coq Library `coq-8.15@c486697` 777 文件 MM2 seed（C-208）；Agda 证明 MM2→ProgramCode 查表/step/run/halting 等价（C-209–C-213）；Coq 同核证明关系终止↔有限观察、`MM2_HALTING ⪯ PC_HALTING` 与 target synthetic-undecidability（C-214–C-218）；三个 run exact replay。`R2-CROSS-KERNEL-001` 28 anchors/3 packages/282 controls PASS。`undecidable` 保持 implication，不是内部 `¬decidable`。根 `goal.md` 成为 current owner。下一步内部前提、R3/R4 与文献三向薄切。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S143 R2 SEMIHALT 完成）", "# HoTT 研究前沿（S144 R2 synthetic dual-kernel 完成）")
    frontier = replace_once(
        frontier,
        "S132 已登记当前 active goal；S130 改变工作面与研究准备状态。两者都不新增数学 claim。exact objective 见 `.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md`。main 现在是唯一 active write root/current-truth owner；外部 machine-overview 只作候选实现与证据来源。",
        "当前 App Goal 是短指针；完整 exact objective 的唯一 owner 是根 `goal.md`，旧 `.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md` 只作兼容入口。main 是唯一 active write root/current-truth owner；外部 machine-overview 只作候选实现与证据来源。",
    )
    frontier = replace_once(
        frontier,
        "R1 与 R2 ProgramCode/NATCODE/FAIR/SEMIHALT 已在 main 通过 F-011。C-203–C-207 证明 `CodeHalts` 当且仅当某个有限 stage 返回正答案，并给出公平的全域正见证流；有限 stage 的 `nothing` 没有被解释成无界否定。这仍是一般计算性基础。LIT Classics 有 16 个不同内容组，Rosser primary reviewed。当前第一工作包是 `R2-UNIVERSALITY-001` 的源模型／归约资格化，并与 Post/HoTT computability 文献交替；UNDEC、exact HoTT、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
        "R1/R2 C-188–C-218 已在 main 通过 F-011。Coq 同核完成 MM2→显式 target total reduction 与 synthetic-undecidability，Agda 独立完成 MM2→ProgramCode halting equivalence；四模型 correspondence 28 anchors/282 controls PASS。`undecidable` 仍只是 `decidable P→enumerable(complement SBTM_HALT)`，内部无条件 no-decider OPEN。这仍是一般计算性基础。当前第一轮为 `R2-INTERNAL-UNDEC-001`、`G-HOTT-SYNTAX-001`/R3、Post/HoTT computability 文献三向薄切；CE-MAP、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
    )

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += "\n99. 外部库写 `undecidable P` 时必须先展开定义再决定交付强度：本轮 Coq 定理实际是 `decidable P → enumerable(complement SBTM_HALT)`，不是纯构造内部 `¬decidable P`。正确跨框架做法是三段式：同核 source→target total reduction；第二 kernel 对同形 TaskSpec 独立证明；machine-readable correspondence 固定字段、量词和表示差异。有限 controls 只查分支交换，全称强度仍由各 kernel theorem 承担；跨 kernel 不能称 definitional equality。\n"

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS144：根 `goal.md` 成为唯一完整 objective owner；App Goal 为短指针。R2 synthetic dual-kernel 已闭合 C-208–C-218：Coq seed、Agda bridge、Coq same-kernel reduction 三个 run 均 exact replay；cross-kernel 28 anchors/3 packages/282 controls PASS。`undecidable` 是 synthetic implication，内部 `¬decidable` 仍 OPEN。Git local-uncommitted。下一步内部前提、G-HOTT-SYNTAX/R3、Post/HoTT 文献三向薄切。\n\n",
    )

    state["revision"] = 144
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R2_SYNTHETIC_DUAL_KERNEL"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Run three breadth-first thin slices: qualify CT/EPF/representability for R2 internal no-decider; freeze the minimum exact HoTT/2LTT syntax boundary for R3/R4; ingest Post primary and LIT-HOTT-COMPUTABILITY sources."
    state["projection"]["status"] = STATUS
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260914-direction-126"
    direction_record["semantic_status"] = STATUS
    direction_record["scope"] = "Current main-only portfolio after S144: R2 synthetic MM2 reduction is dual-kernel machine-proved locally; internal not-decidable, R3/R4, CE-MAP, natural consumer and reality bridge remain open."
    outcome_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    outcome_record["projection_generation"] = "20260914-outcome-126"
    outcome_record["semantic_status"] = STATUS
    outcome_record["scope"] = "Integrated outcomes through C-218 and R2 cross-kernel correspondence; no unconditional internal no-decider or qualified HoTT reality-relative paradox."

    source_evidence = [
        f"{COQ_ROOT}/REPLAY_SOURCE.json", f"{COQ_ROOT}/SOURCE_TREE_MANIFEST.json",
        "audit/literature/LIT-MECH-META-001/coq-library-undecidability/QUALIFICATION.json",
        "audit/literature/LIT-MECH-META-001/coq-library-undecidability/CURRENT_TREE_MANIFEST.json",
        "scripts/audit/import_coq_undecidability_mm2.py", SOURCE_AUDIT,
    ]
    state["records"][SOURCE_ID] = {
        "classification": "COQ_UNDECIDABILITY_MM2_SOURCE_DENOMINATOR_QUALIFIED",
        "depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE / SOURCE_QUALIFIED",
        "full_sources": source_evidence, "kind": "external_source_qualification",
        "lifecycle_status": "CURRENT", "path": f"{COQ_ROOT}/REPLAY_SOURCE.json",
        "related_records": [GOAL_ID, PLAN_ID, COVERAGE_ID, LIT_ID, COQ_SEED_ID, SESSION_ID],
        "scope": "Git/codeload qualification of coq-8.15@c486697 (777 files) and current rocq-9.2@c7257b7 (720 files), selected MM2/synthetic sources and exact archive/tree identities; semantic claims remain separately proved/reviewed.",
        "source_hashes": record_hashes(source_evidence), "status": "complete",
    }

    seed_evidence = [
        f"{COQ_ROOT}/CheckMM2Undec.v", f"{COQ_ROOT}/REPLAY_SOURCE.json",
        f"{COQ_ROOT}/upstream-coq-8.15-c486697/theories/Synthetic/Definitions.v",
        f"{COQ_ROOT}/upstream-coq-8.15-c486697/theories/Synthetic/Undecidability.v",
        f"{COQ_ROOT}/upstream-coq-8.15-c486697/theories/MinskyMachines/MM2.v",
        f"{COQ_ROOT}/upstream-coq-8.15-c486697/theories/MinskyMachines/MM2_undec.v",
        *run_assets(COQ_SEED_RUN), MATRIX, REGISTRY, SOURCE_AUDIT,
        "scripts/audit/verify_coq_mm2_replay_run.py",
    ]
    state["records"][COQ_SEED_ID] = {
        "claim_ids": COQ_SEED_CLAIMS, "classification": "EXTERNAL_MM2_SYNTHETIC_UNDECIDABILITY_REPLAY",
        "depends_on": [], "evidence_status": "REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE / LOCAL_UNCOMMITTED",
        "full_sources": seed_evidence, "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT", "mathematical_status": "MM2_SYNTHETIC_UNDECIDABILITY_REPLAYED_DEFINITION_BOUNDARY_PRESERVED",
        "path": f"{COQ_ROOT}/CheckMM2Undec.v", "proof_id": COQ_SEED_PROOF,
        "research_parent": GOAL_ID, "related_records": [PROOF_GATE_ID, SOURCE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID],
        "resolution": {"evidence": [f"{COQ_SEED_RUN}/RUN.json", f"{COQ_SEED_RUN}/index-row-manifest.json", MATRIX, SOURCE_AUDIT], "reason": "Coq 8.15.2 rebuilt the 777-file source closure, accepted MM2_HALTING_undec, and Print Assumptions reported Closed under the global context; exact replay matched. Undecidable is the upstream synthetic implication."},
        "run_id": COQ_SEED_RUN_ID,
        "scope": "C-208 only: MM2_HALTING_undec under undecidable P := decidable P -> enumerable(complement SBTM_HALT). No unconditional not-decidable or Agda theorem transport.",
        "source_hashes": record_hashes(seed_evidence), "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }

    agda_evidence = [
        "HoTT/formal/cubical-machine-halting/MM2Bridge.agda",
        "HoTT/formal/cubical-machine-halting/CLAIM-R2-MM2-BRIDGE.md",
        "HoTT/formal/cubical-machine-halting/ProgramCode.agda",
        "HoTT/formal/cubical-machine-halting/NatProgramCode.agda",
        *run_assets(AGDA_BRIDGE_RUN), MATRIX, REGISTRY, AGDA_AUDIT,
        "scripts/audit/verify_formal_proof_run.py",
    ]
    state["records"][AGDA_BRIDGE_ID] = {
        "claim_ids": AGDA_BRIDGE_CLAIMS, "classification": "R2_AGDA_MM2_PROGRAMCODE_HALTING_EQUIVALENCE",
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": agda_evidence, "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT", "mathematical_status": "AGDA_LOCAL_MM2_TO_PROGRAMCODE_BIDIRECTIONAL_HALTING",
        "path": "HoTT/formal/cubical-machine-halting/MM2Bridge.agda", "proof_id": AGDA_BRIDGE_PROOF,
        "research_parent": GOAL_ID, "related_records": [PROOF_GATE_ID, SEMI_ID, SOURCE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID],
        "resolution": {"evidence": [f"{AGDA_BRIDGE_RUN}/RUN.json", f"{AGDA_BRIDGE_RUN}/index-row-manifest.json", MATRIX, AGDA_AUDIT], "reason": "Cubical Agda accepted lookup, finality, step, all finite runs and truncated halting equivalence with zero warnings; exact replay matched."},
        "run_id": AGDA_BRIDGE_RUN_ID,
        "scope": "C-209-C-213 local functional MM2 to ProgramCode compilation/halting equivalence; no cross-kernel definitional equality or unconditional undecidability.",
        "source_hashes": record_hashes(agda_evidence), "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }

    coq_evidence = [
        f"{COQ_ROOT}/MM2ProgramCodeBridge.v", f"{COQ_ROOT}/CLAIM-R2-COQ-MM2-BRIDGE.md",
        f"{COQ_ROOT}/REPLAY_SOURCE.json", *run_assets(COQ_BRIDGE_RUN),
        MATRIX, REGISTRY, COQ_AUDIT, SOURCE_AUDIT,
        "scripts/audit/verify_coq_mm2_replay_run.py",
    ]
    state["records"][COQ_BRIDGE_ID] = {
        "claim_ids": COQ_BRIDGE_CLAIMS, "classification": "R2_COQ_SAME_KERNEL_MM2_PROGRAMCODE_REDUCTION",
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": coq_evidence, "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT", "mathematical_status": "COQ_TOTAL_MM2_TO_EXPLICIT_TARGET_REDUCTION_AND_SYNTHETIC_UNDECIDABILITY",
        "path": f"{COQ_ROOT}/MM2ProgramCodeBridge.v", "proof_id": COQ_BRIDGE_PROOF,
        "research_parent": GOAL_ID, "related_records": [PROOF_GATE_ID, SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, CROSS_ID, SESSION_ID],
        "resolution": {"evidence": [f"{COQ_BRIDGE_RUN}/RUN.json", f"{COQ_BRIDGE_RUN}/index-row-manifest.json", MATRIX, COQ_AUDIT], "reason": "Coq 8.15.2 accepted relational-functional equivalence, compiler preservation, total many-one reduction and target synthetic-undecidability; assumptions closed and exact replay matched."},
        "run_id": COQ_BRIDGE_RUN_ID,
        "scope": "C-214-C-218 same-kernel Coq target and MM2 reduction. Undecidable remains a synthetic implication; no Coq/Agda definitional identity or internal negated decidability.",
        "source_hashes": record_hashes(coq_evidence), "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }

    cross_evidence = [CROSS_SPEC, CROSS_DOC, CROSS_RECEIPT, CROSS_VERIFIER, SOURCE_AUDIT, AGDA_AUDIT, COQ_AUDIT]
    state["records"][CROSS_ID] = {
        "classification": "R2_DUAL_KERNEL_SCOPED_CORRESPONDENCE",
        "depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": cross_evidence, "kind": "cross_kernel_correspondence",
        "lifecycle_status": "CURRENT", "path": CROSS_DOC,
        "research_parent": GOAL_ID, "related_records": [SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, PLAN_ID, SESSION_ID],
        "resolution": {"evidence": [CROSS_RECEIPT, CROSS_SPEC, CROSS_DOC], "reason": "Three formal packages, 28 source anchors and 282 branch/field controls passed. Universal claims come from the separate kernels; cross-kernel definitional equality is not claimed."},
        "scope": "Four-model state/instruction/label/branch/finality/halting correspondence with explicit Coq-exists versus Agda-truncation boundary.",
        "source_hashes": record_hashes(cross_evidence), "status": "complete",
    }

    changed = [
        GOAL, GOAL_COMPAT, PROGRAM_005, PROGRAM_006, LIT_SHARD, README_SHARD,
        MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, FEATURE,
        SOURCE_AUDIT, AGDA_AUDIT, COQ_AUDIT, CROSS_SPEC, CROSS_DOC, CROSS_RECEIPT,
    ]
    for record in state["records"].values():
        hashes = record.get("source_hashes")
        if not isinstance(hashes, dict):
            continue
        for path in changed:
            if path in hashes:
                hashes[path] = R.sha((ROOT / path).read_bytes())

    old_goal = state["records"][OLD_GOAL_ID]
    goal = copy.deepcopy(old_goal)
    goal["path"] = GOAL
    goal["full_sources"] = [GOAL, GOAL_COMPAT, PROGRAM_005.rsplit("/", 1)[0] + ".md", FEATURE, "rulings.md", ".codex/research/hott/LIT-DENOMINATOR-001.md", ".codex/research/hott/LIT-CLASSICS-001.md"]
    goal["source_hashes"] = record_hashes(goal["full_sources"])
    goal["lifecycle_status"] = "ACTIVE_WORK"
    goal["evidence_status"] = "USER_AUTHORIZED_ACTIVE_GOAL"
    goal["status"] = "active"
    goal["scope"] = "Complete the exact objective in root goal.md, continuously maintaining governance and evidence across compaction boundaries; completion still requires one exact-HoTT, HoTT-essential, natural-consumer, same-reality-task A/B witness plus the declared coverage gates."
    goal["related_records"] = list(dict.fromkeys([OLD_GOAL_ID, *goal.get("related_records", [])]))
    for identity in (SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID):
        add_once(goal.setdefault("related_records", []), identity)
    goal["revalidation"] = f"{SESSION_ID}: root goal.md is the canonical objective owner. C-208-C-218 close R2 synthetic dual-kernel reduction with scoped correspondence; Goal remains active because internal no-decider, R3/R4, CE-MAP, natural consumer, HoTT essentiality, reality bridge and literature coverage remain open."
    state["records"][GOAL_ID] = goal
    old_goal["lifecycle_status"] = "HISTORICAL"
    old_goal["evidence_status"] = "SUPERSEDED_BY_ROOT_GOAL_MD / HISTORICAL_POINTER"
    old_goal["status"] = "closed"
    old_goal["resolution"] = {
        "reason": "The user replaced the long App objective with a short pointer and made root goal.md the only complete current objective owner. The research objective continues under A-HOTT-MACHINE-OVERVIEW-GOAL-002; this record is retained for old Session references.",
        "evidence": [GOAL, GOAL_COMPAT, f"{SESSION_REL}/SESSION.md"],
    }
    old_goal["source_hashes"][GOAL_COMPAT] = R.sha((ROOT / GOAL_COMPAT).read_bytes())
    add_once(old_goal.setdefault("related_records", []), GOAL_ID)
    add_once(old_goal["related_records"], SESSION_ID)

    plan_record = state["records"][PLAN_ID]
    for path in (PROGRAM_005, PROGRAM_006):
        plan_record["source_hashes"][path] = R.sha((ROOT / path).read_bytes())
    for identity in (SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID):
        add_once(plan_record.setdefault("related_records", []), identity)
    plan_record["revalidation"] = f"{SESSION_ID}: P4 synthetic R2 reduction is dual-kernel complete with scoped correspondence; internal no-decider, CE-MAP, R3/R4 and final witness gates remain open."

    coverage = state["records"][COVERAGE_ID]
    coverage["source_hashes"][PROGRAM_006] = R.sha((ROOT / PROGRAM_006).read_bytes())
    for identity in (SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID):
        add_once(coverage.setdefault("related_records", []), identity)
    coverage["revalidation"] = f"{SESSION_ID}: Coq MM2 source denominator is qualified/replayed and R2 TaskSpec mapped; Post, CT/EPF/Oracle, comprehensive citation coverage and final HoTT witness remain open."

    lit = state["records"][LIT_ID]
    lit["source_hashes"][LIT_SHARD] = R.sha((ROOT / LIT_SHARD).read_bytes())
    for identity in (SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID):
        add_once(lit.setdefault("related_records", []), identity)
    lit["revalidation"] = f"{SESSION_ID}: shard 006 records R2 synthetic dual-kernel complete and internal negation open; Post and HoTT computability/citation coverage remain open."

    semi = state["records"][SEMI_ID]
    for identity in (SOURCE_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID, SESSION_ID):
        add_once(semi.setdefault("related_records", []), identity)
    semi["revalidation"] = f"{SESSION_ID}: downstream MM2 reductions consume the semi-halting foundation; C-203-C-207 remain unchanged."

    gate = state["records"][PROOF_GATE_ID]
    for identity in (COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID):
        add_once(gate.setdefault("related_records", []), identity)
    gate["revalidation"] = f"{SESSION_ID}: three new proof packages C-208-C-218 have source/run/index/frozen-row evidence; Coq-specific verifier preserves the ISO-8859 license and exact warning stream. Git closure remains open."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：R2 synthetic universality/reduction 的双内核闭合与 Goal owner 迁移。
- Coq seed：`{COQ_SEED_PROOF}` / C-208；777 文件干净树；assumptions closed；exact replay。
- Agda bridge：`{AGDA_BRIDGE_PROOF}` / C-209–C-213；lookup/final/step/run/halting 双向保持；exact replay。
- Coq same-kernel bridge：`{COQ_BRIDGE_PROOF}` / C-214–C-218；`MM2_HALTING ⪯ PC_HALTING` + target synthetic-undecidability；assumptions closed；exact replay。
- correspondence：28 anchors、3 packages、282 controls PASS；不主张 cross-kernel definitional equality。
- 定义边界：`undecidable P = decidable P → enumerable(complement SBTM_HALT)`；内部 `¬decidable` OPEN。
- Goal：根 `goal.md` canonical；App Goal short pointer；旧路径 compatibility-only。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
- 下一步：R2 internal premise、G-HOTT-SYNTAX/R3、Post/HoTT literature 三向薄切。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "proofs": [
            {"proof_id": COQ_SEED_PROOF, "claim_ids": COQ_SEED_CLAIMS, "run_id": COQ_SEED_RUN_ID, "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE", "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH", "assumptions": "CLOSED_UNDER_GLOBAL_CONTEXT"},
            {"proof_id": AGDA_BRIDGE_PROOF, "claim_ids": AGDA_BRIDGE_CLAIMS, "run_id": AGDA_BRIDGE_RUN_ID, "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE", "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH", "stderr_bytes": 0},
            {"proof_id": COQ_BRIDGE_PROOF, "claim_ids": COQ_BRIDGE_CLAIMS, "run_id": COQ_BRIDGE_RUN_ID, "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE", "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH", "assumptions": "CLOSED_UNDER_GLOBAL_CONTEXT"},
        ],
        "cross_kernel": {"status": "PASS_WITH_SCOPE", "anchors": 28, "formal_packages": 3, "controls": 282, "receipt": CROSS_RECEIPT},
        "definition_boundary": "SYNTHETIC_UNDECIDABILITY_NOT_INTERNAL_NEGATED_DECIDABILITY",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "next": ["R2-INTERNAL-UNDEC-001", "G-HOTT-SYNTAX-001", "POST-AND-LIT-HOTT-COMPUTABILITY"],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, SOURCE_AUDIT, AGDA_AUDIT, COQ_AUDIT, CROSS_RECEIPT],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, OLD_GOAL_ID, GOAL_ID, SOURCE_ID, COQ_SEED_ID, AGDA_BRIDGE_ID, COQ_BRIDGE_ID, CROSS_ID],
        "scope": "Register C-208-C-218, scoped cross-kernel correspondence and root goal.md ownership; route internal no-decider/R3-R4/literature successors.",
        "source_hashes": {}, "status": "complete",
    }

    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
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
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "Continue the active root goal.md objective by closing the scoped R2 synthetic dual-kernel reduction, preserving its definition boundary, and routing the next breadth-first successors.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value} for path, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 144, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
