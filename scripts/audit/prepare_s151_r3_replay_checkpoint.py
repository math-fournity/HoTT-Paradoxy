#!/usr/bin/env python3
"""Prepare revision 151: record exact R3 replay and activate R4 Nat/effectivity."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SCRIPTS = ROOT / "scripts/audit"
SESSION_ID = "S-RES-20260915-151-R3-SOURCE-REPLAY"
PREV = "S-RES-20260915-150-CE-MAP-V1"
STATUS = "CORE_GENERATION_4_C244_C249_R3_REPLAYED_R4_NAT_EFFECTIVITY_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_CLASSICS_ID = "A-LIT-CLASSICS-001"
LIT_HOTT_ID = "A-LIT-HOTT-COMPUTABILITY-001"
SYNTAX_ID = "A-G-HOTT-SYNTAX-001"
GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
R3_PARENT_ID = "A-R3-R4-GODEL-RETURN-001"
R3_PROOF_ID = "A-COQ-SYNTHETIC-INCOMPLETENESS-R3-001"
MATRIX_ID = "A-R3-R4-OBLIGATION-MATRIX-001"
R4_ID = "A-R4-HOTT-NAT-EFFECTIVITY-001"

PROOF_ID = "MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001"
CLAIMS = ["C-244", "C-245", "C-246", "C-247", "C-248", "C-249"]
RUN_ID = "20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01"
RUN = f"HoTT/verification/runs/{RUN_ID}"
PACKAGE = "HoTT/formal/external-coq-synthetic-incompleteness"

R3_DOC = ".codex/research/hott/R3-R4-GODEL-RETURN-001.md"
R4_DOC = ".codex/research/hott/R4-HOTT-NAT-EFFECTIVITY-001.md"
GOAL = "goal.md"
FEATURE = "feature-list.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
PROGRAM_TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
LIT_005 = ".codex/research/hott/LIT-CLASSICS-001/005 - 现代机器化对照与R2-R4前提.md"
LIT_006 = ".codex/research/hott/LIT-CLASSICS-001/006 - 当前判词、缺口与下一机器工作包.md"
LIT_HOTT_004 = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001/004 - 2LTT、groupoid-syntax 与下一候选.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
IMPORTER = "scripts/audit/import_coq_synthetic_incompleteness.py"
REPLAY = "scripts/audit/replay_coq_synthetic_incompleteness.py"
CAPTURE = "scripts/audit/capture_coq_synthetic_incompleteness_run.py"
VERIFIER = "scripts/audit/verify_formal_proof_run.py"
OBLIGATION_MANAGER = "scripts/audit/build_r3_r4_obligations.py"
OBLIGATION_TEST = "scripts/audit/test_r3_r4_obligations.py"
OBLIGATION_ROOT = "audit/r3-r4-godel"
OBLIGATION_README = f"{OBLIGATION_ROOT}/README.md"
OBLIGATION_MAP = f"{OBLIGATION_ROOT}/R3-R4-OBLIGATIONS.json"
OBLIGATION_REPORT = f"{OBLIGATION_ROOT}/REPORT.md"
OBLIGATION_RECEIPT = f"{OBLIGATION_ROOT}/RECEIPT.json"
AUDIT = "audit/R3一般不完备性机器重放与HoTT-R4义务矩阵-20260915.md"
PREPARE = "scripts/audit/prepare_s151_r3_replay_checkpoint.py"

SPEC = importlib.util.spec_from_file_location("runtime_s151", RUNTIME_PATH)
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


def file_hashes(paths: list[str], future: dict[str, str] | None = None) -> dict[str, str]:
    future = future or {}
    return {
        path: R.sha(future[path].encode() if path in future else (ROOT / path).read_bytes())
        for path in paths
    }


def run_assets() -> list[str]:
    return [
        f"{RUN}/RUN.json",
        f"{RUN}/source-manifest.json",
        f"{RUN}/index-row-manifest.json",
        f"{RUN}/stdout.txt",
        f"{RUN}/stderr.txt",
        f"{RUN}/environment.txt",
    ]


def command_pass(argv: list[str], required: str) -> str:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    if result.returncode != 0 or required not in output:
        raise SystemExit(f"PRECHECK_FAILED:{' '.join(argv)}\n{output}")
    return output


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "R3 源理论、R4 target calculus 与宿主 kernel 被分层；没有把在 Coq 中形式化误作对象 theory=Coq/HoTT。",
        "KC-000005": "一般 R3 已机器闭合，但矩阵把 exact HoTT R4 的十项未满足义务完整暴露，拒绝以一般定理冒充终点。",
        "KC-000007": "807-file archive→fresh build→theorem signatures→assumptions→index→exact replay形成可执行 source-guided路径。",
        "KC-000010": "C-244–C-249 全部保留条件和 non-goals，不写成 HoTT 自身不完备或内部矛盾。",
        "KC-000011": "本轮 Gödel 线属于 proof/representation 的时序与有效性，不替代物理时间/稠密连续性方向。",
        "KC-000012": "universality、separation、Peirce、CTQ、Q containment、enumerability、consistency逐项保留。",
        "KC-000013": "proof checker必须停机、proof search可部分、独立性排除有限证明码三层被严格区分。",
        "KC-000015": "R3→R4 abstraction change固定为把一般 formal system参数实例化到 exact HoTT calculus，而非换宿主文件扩展名。",
        "KC-000021": "source archive、license、fresh build、stable artifacts、qualification、matrix/index与exact rerun构成多样证据。",
        "KC-000022": "方向 B 的自知/总证明能力没有从外层不完备性定理偷取；方向 A 的现实可完成性仍待独立 bridge。",
        "KC-000027": "R4 child优先真实 cubical implementations 的 Nat/Path/conversion，但先排除 holes/undefined/general recursion。",
        "KC-000029": "一般 R3 theorem带来理论经济，但 strong representation/CTQ等成本没有被隐藏。",
        "KC-000031": "R3 replay成功后不重复堆一般 Gödel实例，转向 exact target effectivity和HoTT essentiality。",
        "KC-000035": "12义务 machine matrix确保跨Session恢复时不会忘记 host/object、present/absent/open差异。",
        "KC-000036": "下一步以 certified-input profile检查 community calculus，阻止不完整输入先被当作 proof object。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；根 Goal 保持 active。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        identity = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if identity in focus else "NOT_TOUCHED"
        assessment = focus.get(identity, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(
            f"| `{identity}` | {label} | `{relation}` | {assessment} | `{AUDIT}`；{identity} | "
            "R4 proof code/representability/fixed point、HoTT essentiality、现实同任务、Oracle、物理时间与开放世界覆盖仍开放。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — R3 闭合，第一 successor 转 R4 Nat/Path/effectivity。",
        "- panorama_change: YES_IN_PLACE — 新增 R3 F-011 package 与 R3→R4 matrix outcome。",
        "- essay_change: NO。",
        "- update_decision: exact R3 baseline完成；R4 readiness=NOT_READY；Goal不完成。",
        "- cross_conflicts: Coq host theorem与HoTT object calculus不是同一 theory；explicit premises不因 global-context closed消失。",
        "- unresolved: R4十项 blockers、HoTT essentiality、经验 reality、Oracle、物理时间与全面文献。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    required = [
        R3_DOC,
        R4_DOC,
        GOAL,
        FEATURE,
        PROGRAM_005,
        PROGRAM_006,
        PROGRAM_TEST,
        LIT_005,
        LIT_006,
        LIT_HOTT_004,
        MATRIX,
        REGISTRY,
        FORMAL_README,
        RUNS_README,
        HOTT_README,
        IMPORTER,
        REPLAY,
        CAPTURE,
        VERIFIER,
        OBLIGATION_MANAGER,
        OBLIGATION_TEST,
        OBLIGATION_README,
        OBLIGATION_MAP,
        OBLIGATION_REPORT,
        OBLIGATION_RECEIPT,
        AUDIT,
        PREPARE,
        f"{PACKAGE}/README.md",
        f"{PACKAGE}/CLAIM-R3-SYNTHETIC-INCOMPLETENESS.md",
        f"{PACKAGE}/SOURCE_ARCHIVE.json",
        f"{PACKAGE}/SOURCE_TREE_MANIFEST.json",
        f"{PACKAGE}/TOOLCHAIN.json",
        f"{PACKAGE}/Qualification.v",
        f"{PACKAGE}/Dockerfile",
        f"{PACKAGE}/CeCILL_LICENSE.txt",
        f"{PACKAGE}/IMPORT.json",
        f"{PACKAGE}/upstream-cd7d849.tar.gz",
        *run_assets(),
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"S151_EVIDENCE_MISSING:{missing}")
    command_pass(["python3", "-B", IMPORTER, "validate"], '"status": "VALID"')
    verify_output = command_pass(["python3", "-B", VERIFIER, "--run-dir", RUN], '"status": "PASS_WITH_SCOPE"')
    command_pass(["python3", "-B", OBLIGATION_MANAGER, "validate"], '"status": "VALID"')
    command_pass(["python3", "-B", OBLIGATION_TEST], "Ran 5 tests")
    command_pass(["python3", "-B", PROGRAM_TEST], "Ran 5 tests")
    command_pass(["python3", "-B", "scripts/audit/verify_governance_shards.py"], '"status": "PASS"')
    proof_run = json.loads((ROOT / f"{RUN}/RUN.json").read_text(encoding="utf-8"))
    row_manifest = json.loads((ROOT / f"{RUN}/index-row-manifest.json").read_text(encoding="utf-8"))
    if (
        proof_run.get("proof_id") != PROOF_ID
        or proof_run.get("claim_ids") != CLAIMS
        or proof_run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or proof_run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or proof_run.get("exit_code") != 0
        or row_manifest.get("claim_ids") != CLAIMS
        or len(row_manifest.get("rows", [])) != 7
        or not any(value in verify_output for value in ("EXACT_INDEX_SNAPSHOT_MATCH", "ROW_STABLE_AFTER_INDEX_EVOLUTION"))
    ):
        raise SystemExit("S151_PROOF_RUN_INVALID")
    stdout = (ROOT / f"{RUN}/stdout.txt").read_text(encoding="utf-8")
    for marker in (
        "COQ_R3_TARGET_SHA256:e770c7bf44201f8e696cff4115452b3c02c22274604c787afccdf25edaee33e4",
        "COQ_R3_STABLE_ARTIFACTS:1284:6c2bd66c8547d75540bac15348291064348120f5d3a7342689f9402794d6b958",
        "COQ_R3_QUALIFICATION_SHA256:505b84bb69595703945b850b361115c510401066ce8162437d565eb1b18f441d",
        "COQ_R3_REPLAY_PHASE:COMPLETE",
    ):
        if marker not in stdout:
            raise SystemExit(f"S151_REPLAY_MARKER_MISSING:{marker}")
    registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
    if len(registry.get("later_packages", [])) != 25 or registry.get("later_machine_proved_claim_count") != 101:
        raise SystemExit("S151_REGISTRY_COUNT_INVALID")
    obligation = json.loads((ROOT / OBLIGATION_MAP).read_text(encoding="utf-8"))
    if obligation.get("counts", {}).get("by_status") != {
        "ABSENT_BY_DEFINITION": 3,
        "OPEN": 7,
        "PRESENT_MACHINE_PROVED": 2,
    } or obligation.get("r4_readiness") != "NOT_READY":
        raise SystemExit("S151_OBLIGATION_MATRIX_INVALID")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 150 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_150_S150")
    for identity in (R3_PROOF_ID, MATRIX_ID, R4_ID, SESSION_ID):
        if identity in state["records"]:
            raise SystemExit(f"S151_RECORD_ALREADY_EXISTS:{identity}")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    d2 = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][d2] = replace_line(
        direction["shards"][d2],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 与根 `goal.md` 为唯一工作面推进计算合法性／不可停机／Gödel 到 HoTT 现实相对悖论；CE-MAP v1 已坐标化478项，C-244–C-249 已重放一般R3不完备性 | 用户当前 App Goal；`goal.md`；F-011/F-015/F-016；R3 run/matrix | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY`, `THEORY_ECONOMY` | `OUT-TOP-CE-MAP-V1`、`OUT-TOP-R3-SYNTHETIC-INCOMPLETENESS`、`OUT-TOP-R3-R4-OBLIGATION-MATRIX` | 当前做 `R4-HOTT-NAT-EFFECTIVITY-001`：选择具 Nat/Path/conversion 且拒绝 incomplete input/general recursion的exact target；保持 Oracle、ambient R2、物理时间与 reality 返回口 | `goal.md`；C-244–C-249；R3/R4 matrix与child TaskSpec |",
    )
    for old, new in (
        ("source_state_revision: 150", "source_state_revision: 151"),
        ("projection_generation: 20260915-direction-132", "projection_generation: 20260915-direction-133"),
        ("状态：`CORE_GENERATION_4_CE_MAP_V1_COMPLETE_R3_R4_GODEL_NEXT`", f"状态：`{STATUS}`"),
        ("semantic_status: CORE_GENERATION_4_CE_MAP_V1_COMPLETE_R3_R4_GODEL_NEXT", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    p3 = "全景视野/003 - 当前机器证明包与原生重放.md"
    projection_edit.append_to_shard(
        panorama,
        p3,
        "| `OUT-TOP-R3-SYNTHETIC-INCOMPLETENESS` | C-244–C-249：general classifier divergence、essential incompleteness、EPFμ→CTQ、Robinson Q 条件独立句 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | `MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / R3_COMPLETE_WITH_SCOPE` | 807-file repo archive+license；Coq 8.15.2 fresh build；1,284 stable artifacts；qualification twice；index/freeze/exact rerun | explicit universality/separation/Peirce/CTQ/Q/enumerability/consistency；first-order arithmetic，非 exact HoTT R4/reality | C-244–C-249；R3审计 |\n",
    )
    p4 = "全景视野/004 - 距离综合与消费者审计.md"
    projection_edit.append_to_shard(
        panorama,
        p4,
        "| `OUT-TOP-R3-R4-OBLIGATION-MATRIX` | R3 source theorem到 C-223–C-226 groupoid-syntax target的12项保真义务 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` | deterministic matrix manager +两proof packages | `R3_BASELINE_COMPLETE / R4_NOT_READY / 2_PRESENT_3_ABSENT_7_OPEN` | input remainder=0；删H-NAT负控制；tests 5/5 | host能力不填object calculus；不证明缺项不可实现、HoTT essentiality或现实桥梁 | `audit/r3-r4-godel/REPORT.md`；R3审计 |\n",
    )
    for old, new in (
        ("source_state_revision: 150", "source_state_revision: 151"),
        ("projection_generation: 20260915-outcome-132", "projection_generation: 20260915-outcome-133"),
        ("状态：`CORE_GENERATION_4_CE_MAP_V1_COMPLETE_R3_R4_GODEL_NEXT`", f"状态：`{STATUS}`"),
        ("semantic_status: CORE_GENERATION_4_CE_MAP_V1_COMPLETE_R3_R4_GODEL_NEXT", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m1 = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "当前 App Goal 为短指针，根 `goal.md` 是唯一完整 objective owner。C-188–C-243 已形成 R1/R2、exact syntax 与 internalisation 正负链；CE-MAP v1 又把 478 个具名输入全部映射到八轴，保留 69 unknown并归约 internalisation/defense patterns。最终 HoTT witness 未找到。",
        "当前 App Goal 为短指针，根 `goal.md` 是唯一完整 objective owner。C-188–C-243 已形成 R1/R2、syntax/internalisation链，CE-MAP v1映射478项；C-244–C-249 又在main exact replay一般R3 essential incompleteness/Robinson Q。R4矩阵仅2 present/3 absent/7 open；最终 HoTT witness 未找到。",
    )
    memory["shards"][m1] = replace_once(memory["shards"][m1], "17 个冻结 + 24 个 later package", "17 个冻结 + 25 个 later package")
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "当前仍未得到 ambient HoTT 无条件 no-decider、机器重放的 exact R3 independent sentence、完整 R4 calculus/incompleteness、E6、现实桥梁、`NATURAL_USAGE_MISMATCH` 或 HoTT 内部矛盾。CE-MAP v1 只关闭具名坐标化；17 个冻结 + 25 个 later package 只支持各自范围；新资产仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
        "当前已机器重放带显式前提的一般 R3 independent sentence；仍未得到 ambient HoTT 无条件 no-decider、exact HoTT R4 calculus/incompleteness、E6、现实桥梁、`NATURAL_USAGE_MISMATCH` 或内部矛盾。CE-MAP/R3只关闭各自范围；17 个冻结 + 25 个 later package仍含未提交资产。",
    )
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "Post/Parametric CT/Oracle/groupoid-syntax、2LTT replacement、natural-consumer/支付消融与 CE-MAP v1 均有 scoped evidence。当前优先 `R3-R4-GODEL-RETURN-001`；并行保留 Oracle、ambient R2、物理时间与 reality。未获授权不 push、不 tag。",
        "Post/Parametric CT/Oracle/groupoid-syntax、internalisation、CE-MAP 与一般 R3 replay均有 scoped evidence。当前优先 `R4-HOTT-NAT-EFFECTIVITY-001`；并行保留 Oracle、ambient R2、物理时间与 reality。未获授权不 commit/push/tag。",
    )
    m2 = "MEMORY/002 - 当前证据上限与恢复入口.md"
    memory["shards"][m2] = replace_once(
        memory["shards"][m2],
        "CE-MAP v1 已关闭 revision-149 具名坐标化；完整 R3/R4 Gödel、ambient HoTT no-decider、经验现实桥梁与学术全面覆盖仍开放。",
        "CE-MAP v1 已关闭 revision-149 具名坐标化；C-244–C-249 关闭一般R3基准。exact HoTT R4、ambient HoTT no-decider、经验现实桥梁与学术全面覆盖仍开放。",
    )
    memory["shards"][m2] = replace_once(
        memory["shards"][m2],
        "`audit/ce-map/README.md`/`REPORT.md`/`RECEIPT.json` 与 `R3-R4-GODEL-RETURN-001.md`；具体 map item 用 manager query，不全文预载 594KB JSON；",
        "`audit/ce-map/README.md`/`REPORT.md`/`RECEIPT.json`、`R3-R4-GODEL-RETURN-001.md`、`audit/r3-r4-godel/REPORT.md` 与 `R4-HOTT-NAT-EFFECTIVITY-001.md`；具体 map item 用 manager query，不全文预载 594KB JSON；",
    )
    m3 = "MEMORY/003 - 当前验证状态与顺序日志.md"
    if not memory["shards"][m3].endswith("\n"):
        memory["shards"][m3] += "\n"
    memory["shards"][m3] += (
        "- S151 R3 source replay：`MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` / C-244–C-249；807-file repo archive+CeCILL，Coq 8.15.2 fresh build 614s，1,284 stable artifacts与qualification twice/exact rerun；一般R3闭合但 explicit premises保留。R3→R4矩阵12项=2 present/3 absent/7 open；下一 `R4-HOTT-NAT-EFFECTIVITY-001`；Goal active。\n"
    )

    essay = projection_edit.load(ROOT, R.ESSAY)
    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S150 CE-MAP v1 具名坐标化完成）", "# HoTT 研究前沿（S151 一般 R3 不完备性机器重放完成）")
    frontier = replace_once(
        frontier,
        "C-188–C-243 已形成 R2、syntax 与 internalisation 正负链。CE-MAP v1 进一步登记 478 个具名输入、保留 69 unknown，并把 unqualified internalisation 归为一个带 anti-preservation 的 pattern；qualified defenses完成来源任务。第一 successor=`R3-R4-GODEL-RETURN-001`；ambient R2、完整 R4/Gödel、物理时间、经验 reality 与全面覆盖均 OPEN。",
        "C-188–C-243 已形成 R2、syntax/internalisation链，CE-MAP v1登记478项；C-244–C-249从 exact Coq source重放一般 essential incompleteness与Robinson Q条件独立句。R3→R4矩阵=2 scoped present/3 absent/7 open，故一般R3不等于HoTT R4。第一 successor=`R4-HOTT-NAT-EFFECTIVITY-001`；ambient R2、exact R4、物理时间、经验 reality 与全面覆盖均 OPEN。",
    )
    frontier = replace_line(
        frontier,
        "| 当前高判别候选 |",
        "| 当前高判别候选 | community cubical calculus 的 Nat/Path/conversion 与 certified-input profile | `TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED` | 对 cubicaltt/redtt/cooltt/cctt 做 exact source/build；递归检查 import closure，拒绝 holes/undefined/unsolved goals/general recursion；跑正负 corpus并选择target |",
    )
    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n117. 一般 Gödel/R3 需要真实 source build和 theorem signature；但即使 exact replay，也不能跳过把 T 实例化为具名 HoTT calculus 的 proof-code/effectivity/representability义务。\n"
        "\n118. `Closed under the global context`只说明没有额外global axiom；theorem arrow左侧的 universality、CTQ、Peirce、enumerability与consistency仍是调用前提。\n"
        "\n119. source archive与许可证应进入main，避免F-011只依赖外部dirty worktree；binary source由external-dependency byte hash验证，非UTF8 license不应被无条件文本解码。\n"
        "\n120. executable cubical implementation不能因有Nat/Path就直接成为proof theory：holes、undefined、unsolved metavariables和unchecked recursion必须从certified acceptance relation中机械排除。\n"
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS151：C-244–C-249 general essential incompleteness/Robinson Q 已从repo-contained 807-file archive在Coq8.15.2 fresh build、index/freeze并exact rerun。R3→R4 12义务=2 scoped present/3 absent/7 open；对象仍first-order arithmetic，非HoTT。active=`A-R4-HOTT-NAT-EFFECTIVITY-001`，资格化cubicaltt/redtt/cooltt/cctt certified target；Goal保持active。\n\n",
    )

    state["revision"] = 151
    state["latest_session"] = SESSION_ID
    state["active"] = ["I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912", GOAL_ID, R4_ID]
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R3_SOURCE_REPLAY"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Execute R4-HOTT-NAT-EFFECTIVITY-001: qualify cubicaltt/redtt/cooltt/cctt, freeze one exact build and certified input profile, then run Nat/Path/cubical positive and typing/incomplete/recursion negative controls."
    )
    state["projection"]["status"] = STATUS
    for key, generation in (
        ("I-DIRECTION-PORTFOLIO-20260912", "20260915-direction-133"),
        ("I-OUTCOME-PANORAMA-20260912", "20260915-outcome-133"),
    ):
        state["records"][key]["projection_generation"] = generation
        state["records"][key]["semantic_status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = "Current portfolio through C-249: general R3 replayed, exact HoTT R4 Nat/effectivity active, Goal open."
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = "Integrated outcomes through C-249 plus R3-to-R4 matrix; no exact HoTT incompleteness, essentiality or reality bridge."

    proof_sources = [
        f"{PACKAGE}/README.md",
        f"{PACKAGE}/CLAIM-R3-SYNTHETIC-INCOMPLETENESS.md",
        f"{PACKAGE}/SOURCE_ARCHIVE.json",
        f"{PACKAGE}/SOURCE_TREE_MANIFEST.json",
        f"{PACKAGE}/TOOLCHAIN.json",
        f"{PACKAGE}/Qualification.v",
        f"{PACKAGE}/Dockerfile",
        f"{PACKAGE}/CeCILL_LICENSE.txt",
        f"{PACKAGE}/IMPORT.json",
        IMPORTER,
        REPLAY,
        CAPTURE,
        VERIFIER,
        *run_assets(),
        MATRIX,
        REGISTRY,
        AUDIT,
    ]
    state["records"][R3_PROOF_ID] = {
        "claim_ids": CLAIMS,
        "classification": "R3_CONDITIONAL_ESSENTIAL_INCOMPLETENESS_AND_ROBINSON_Q_REPLAY",
        "depends_on": [],
        "evidence_status": "MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": proof_sources,
        "kind": "external_formal_source_replay",
        "lifecycle_status": "CURRENT",
        "mathematical_status": "R3_CONDITIONAL_ESSENTIAL_INCOMPLETENESS_COMPLETE_HOTT_R4_OPEN",
        "path": f"{PACKAGE}/Qualification.v",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "research_parent": R3_PARENT_ID,
        "related_records": [GOAL_ID, PLAN_ID, COVERAGE_ID, LIT_CLASSICS_ID, LIT_HOTT_ID, SYNTAX_ID, MATRIX_ID, R4_ID, SESSION_ID],
        "resolution": {
            "evidence": [f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", MATRIX, AUDIT],
            "reason": "Repo-contained exact source archive fresh-built in Coq 8.15.2; target/stable artifacts and qualification match prior clean builds; generic verifier exact rerun passed.",
        },
        "scope": "C-244-C-249 only: conditional general formal-system and Robinson-Q incompleteness with all theorem parameters retained; not exact HoTT R4 or reality correspondence.",
        "source_hashes": file_hashes(proof_sources),
        "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }

    matrix_sources = [OBLIGATION_README, OBLIGATION_REPORT, OBLIGATION_RECEIPT, OBLIGATION_MANAGER, OBLIGATION_TEST, R3_DOC, R4_DOC, AUDIT]
    state["records"][MATRIX_ID] = {
        "classification": "R3_TO_EXACT_HOTT_R4_TWELVE_OBLIGATION_MATRIX",
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / 2_PRESENT_3_ABSENT_7_OPEN",
        "full_sources": matrix_sources,
        "kind": "cross_kernel_correspondence",
        "lifecycle_status": "CURRENT",
        "path": OBLIGATION_REPORT,
        "research_parent": R3_PARENT_ID,
        "related_records": [R3_PROOF_ID, SYNTAX_ID, R4_ID, SESSION_ID],
        "scope": "Complete status registration of twelve R3-to-R4 obligations for the current R3 source and groupoid-syntax target; absence/open does not prove impossibility.",
        "source_hashes": file_hashes(matrix_sources),
        "machine_managed_canonical": OBLIGATION_MAP,
        "artifact_hashes": file_hashes([OBLIGATION_MAP, OBLIGATION_REPORT, OBLIGATION_RECEIPT]),
        "status": "complete_with_scope",
    }

    r4_sources = [R4_DOC, R3_DOC, OBLIGATION_REPORT, OBLIGATION_RECEIPT, AUDIT, GOAL]
    state["records"][R4_ID] = {
        "classification": "EXECUTABLE_CUBICAL_NAT_PATH_CONVERSION_CERTIFIED_INPUT_TARGET",
        "depends_on": [],
        "evidence_status": "TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED",
        "full_sources": r4_sources,
        "kind": "candidate_search_task",
        "lifecycle_status": "ACTIVE_WORK",
        "path": R4_DOC,
        "research_parent": R3_PARENT_ID,
        "related_records": [GOAL_ID, PLAN_ID, COVERAGE_ID, LIT_HOTT_ID, SYNTAX_ID, R3_PROOF_ID, MATRIX_ID, SESSION_ID],
        "scope": "Qualify exact cubical implementations and define a certified acceptance relation excluding incomplete terms and unchecked recursion; advance only Nat/Path/conversion/effectivity obligations.",
        "source_hashes": file_hashes(r4_sources),
        "status": "active",
    }

    parent = state["records"][R3_PARENT_ID]
    parent_sources = [R3_DOC, R4_DOC, OBLIGATION_REPORT, OBLIGATION_RECEIPT, f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", AUDIT, GOAL]
    parent["evidence_status"] = "R3_SOURCE_REPLAY_COMPLETE / R4_OBLIGATION_MATRIX_COMPLETE / R4_CHILD_ACTIVE"
    parent["full_sources"] = parent_sources
    parent["source_hashes"] = file_hashes(parent_sources)
    parent["scope"] = "General R3 baseline C-244-C-249 complete; exact HoTT R4 has 2 scoped present, 3 absent and 7 open obligations; Nat/effectivity child active."
    parent["revalidation"] = f"{SESSION_ID}: exact R3 source replay completed; parent remains active for R4 and reality/essentiality obligations."
    for related in (R3_PROOF_ID, MATRIX_ID, R4_ID, SESSION_ID):
        add_once(parent.setdefault("related_records", []), related)

    for record_id in (GOAL_ID, PLAN_ID, COVERAGE_ID, LIT_CLASSICS_ID, LIT_HOTT_ID, SYNTAX_ID, GATE_ID):
        record = state["records"][record_id]
        for related in (R3_PARENT_ID, R3_PROOF_ID, MATRIX_ID, R4_ID, SESSION_ID):
            add_once(record.setdefault("related_records", []), related)
    goal_record = state["records"][GOAL_ID]
    for path in (GOAL, FEATURE, R3_DOC, R4_DOC, OBLIGATION_REPORT, OBLIGATION_RECEIPT, AUDIT):
        add_once(goal_record.setdefault("full_sources", []), path)
    goal_record["source_hashes"] = file_hashes(goal_record["full_sources"])
    goal_record["revalidation"] = f"{SESSION_ID}: general R3 is complete with explicit premises; exact HoTT R4, essentiality and reality bridge remain. Goal moves to {R4_ID}."
    plan_record = state["records"][PLAN_ID]
    for path in (PROGRAM_005, PROGRAM_006, R3_DOC, R4_DOC, OBLIGATION_REPORT, OBLIGATION_RECEIPT, AUDIT):
        add_once(plan_record.setdefault("full_sources", []), path)
    plan_record["source_hashes"] = file_hashes(plan_record["full_sources"])
    plan_record["revalidation"] = f"{SESSION_ID}: R3 exact replay closes one computation/Gödel slice; R4 certified executable target is next."
    coverage_record = state["records"][COVERAGE_ID]
    for path in (LIT_005, LIT_006, LIT_HOTT_004, R3_DOC, R4_DOC, AUDIT):
        add_once(coverage_record.setdefault("full_sources", []), path)
    coverage_record["source_hashes"] = file_hashes(coverage_record["full_sources"])
    coverage_record["revalidation"] = f"{SESSION_ID}: primary/code R3 theorem replayed; full citation chains and exact HoTT R4 corpus remain open."
    for record_id, paths in (
        (LIT_CLASSICS_ID, [LIT_005, LIT_006, AUDIT]),
        (LIT_HOTT_ID, [LIT_HOTT_004, R4_DOC, AUDIT]),
    ):
        record = state["records"][record_id]
        for path in paths:
            add_once(record.setdefault("full_sources", []), path)
        record["source_hashes"] = file_hashes(record["full_sources"])
        record["revalidation"] = f"{SESSION_ID}: R3 source theorem and R4 target/effectivity boundary incorporated; comprehensive corpus remains open."
    syntax = state["records"][SYNTAX_ID]
    for path in (R3_DOC, R4_DOC, OBLIGATION_REPORT, OBLIGATION_RECEIPT, AUDIT):
        add_once(syntax.setdefault("full_sources", []), path)
    syntax["source_hashes"] = file_hashes(syntax["full_sources"])
    syntax["evidence_status"] = "R3_BASELINE_MACHINE_REPLAYED / R4_MATRIX_2_PRESENT_3_ABSENT_7_OPEN / NAT_EFFECTIVITY_ACTIVE"
    syntax["scope"] = "General R3 complete; groupoid syntax supplies only scoped syntax/substitution. A second executable Nat/Path/conversion target is active; proof code/representability/fixed point/independence remain open."
    syntax["revalidation"] = f"{SESSION_ID}: exact R3 did not auto-fill object-HoTT obligations; activated certified target qualification."
    gate = state["records"][GATE_ID]
    for path in (*run_assets(), REGISTRY, MATRIX, VERIFIER):
        add_once(gate.setdefault("full_sources", []), path)
    gate["source_hashes"] = file_hashes(gate["full_sources"])
    gate["scope"] = "Exact statement/source/kernel/index gate; registry has 17 frozen packages, one scoped external replay and 25 later packages / 101 claims."
    gate["revalidation"] = f"{SESSION_ID}: C-244-C-249 indexed, row-frozen and exact-replayed; full Git closure remains blocked by untracked C-188+ assets."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session_text = f"""# {SESSION_ID}

- 工作单元：exact R3 synthetic essential incompleteness / Robinson Q source replay。
- source：807-file repo-contained archive + CeCILL；`csl@cd7d849`。
- kernel：Coq 8.15.2 fresh build约614s；1,284 stable artifacts；qualification twice；generic exact rerun。
- claims：C-244–C-249，explicit universality/separation/Peirce/CTQ/Q/enumerability/consistency retained。
- correspondence：R3→R4 12 obligations = 2 scoped present / 3 absent / 7 open；R4 NOT_READY。
- 下一：`{R4_ID}`，community cubical target + certified input profile。
- Goal：active；Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；version-closure verifier在未跟踪C-188正确阻塞；未 commit/push/tag。
"""
    runs_text = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "formal_runs": [{"proof_id": PROOF_ID, "run_id": RUN_ID, "claims": CLAIMS, "status": "PASS_WITH_SCOPE / INDEXED / FROZEN / EXACT_REPLAY"}],
            "r3_r4_matrix": {"path": OBLIGATION_MAP, "present": 2, "absent": 3, "open": 7, "tests": "5/5 PASS"},
            "version_closure": "BLOCKED_EXPECTED_AT_UNTRACKED_C188_SOURCE_NO_COMMIT_AUTHORIZATION",
            "verdict": "GENERAL_R3_COMPLETE_WITH_SCOPE_EXACT_HOTT_R4_OPEN",
            "next": [R4_ID, "R4-PROOF-CODE-001", "R4-REPRESENTABILITY-001", "REALITY-TASK-001", "ORACLE-MODALITY-REPLAY-001"],
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", OBLIGATION_REPORT, AUDIT],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, GOAL_ID, R3_PARENT_ID, R3_PROOF_ID, MATRIX_ID, R4_ID],
        "scope": "Close exact general R3 replay, preserve explicit premises, record R4 obligations and activate certified Nat/Path target without completing the Goal.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[lessons_path] = lessons
    texts[resume_path] = resume
    texts[session_path] = session_text
    texts[audit_path] = audit_text()
    texts[runs_path] = runs_text

    changed = [
        GOAL,
        FEATURE,
        PROGRAM_005,
        PROGRAM_006,
        LIT_005,
        LIT_006,
        LIT_HOTT_004,
        R3_DOC,
        R4_DOC,
        MATRIX,
        REGISTRY,
        FORMAL_README,
        RUNS_README,
        HOTT_README,
        VERIFIER,
        OBLIGATION_REPORT,
        OBLIGATION_RECEIPT,
        AUDIT,
        *run_assets(),
        *texts.keys(),
    ]
    for record in state["records"].values():
        hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(hashes, dict):
            continue
        rebound = []
        for path in changed:
            if path not in hashes or path == R.STATE:
                continue
            data = texts[path].encode() if path in texts else (ROOT / path).read_bytes()
            value = R.sha(data)
            if hashes[path] != value:
                hashes[path] = value
                rebound.append(path)
        if rebound and record not in (state["records"][R3_PROOF_ID], state["records"][MATRIX_ID], state["records"][R4_ID]):
            note = f"{SESSION_ID}: revalidated current owner/proof-index/verifier evolution at {', '.join(rebound)}; prior mathematical scopes remain unchanged."
            previous = record.get("revalidation")
            record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note

    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value}
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 151, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
