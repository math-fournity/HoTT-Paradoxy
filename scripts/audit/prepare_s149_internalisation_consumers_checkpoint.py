#!/usr/bin/env python3
"""Prepare revision 149: close internalisation consumers and route CE-MAP."""
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
SESSION_ID = "S-RES-20260915-149-INTERNALISATION-CONSUMERS"
PREV = "S-RES-20260915-148-2LTT-FR-UIP"
STATUS = "CORE_GENERATION_4_C188_C243_INTERNALISATION_CLASS_DEFENSE_WORKS_CE_MAP_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_ID = "A-LIT-HOTT-COMPUTABILITY-001"
SYNTAX_ID = "A-G-HOTT-SYNTAX-001"
CONSUMER_ID = "A-NATURAL-CONSUMER-2LTT-REPLACEMENT-002"
LOPS_ID = "A-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001"
ITT_ID = "A-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001"
CE_ID = "A-CE-MAP-001"
GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"

LOPS_PROOF = "MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001"
LOPS_CLAIMS = ["C-233", "C-234", "C-235", "C-236", "C-237", "C-238"]
LOPS_RUN_ID = "20260915-MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001-01"
LOPS_RUN = f"HoTT/verification/runs/{LOPS_RUN_ID}"
LOPS_PACKAGE = "HoTT/formal/external-agda-flat-internal-universes"

ITT_PROOF = "MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001"
ITT_CLAIMS = ["C-239", "C-240", "C-241", "C-242", "C-243"]
ITT_RUN_ID = "20260915-MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001-01"
ITT_RUN = f"HoTT/verification/runs/{ITT_RUN_ID}"
ITT_PACKAGE = "HoTT/formal/external-coq-interval-replacement"

AUDIT = "audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md"
LIT_INDEX = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md"
LIT_ROOT = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001"
LIT_006 = f"{LIT_ROOT}/006 - internal classifier消费者与受限恢复.md"
CE_DOC = ".codex/research/hott/CE-MAP-001.md"
GOAL = "goal.md"
FEATURE = "feature-list.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
PROGRAM_TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
VERIFIER = "scripts/audit/verify_formal_proof_run.py"
PREPARE = "scripts/audit/prepare_s149_internalisation_consumers_checkpoint.py"

SPEC = importlib.util.spec_from_file_location("runtime_s149", RUNTIME_PATH)
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


def file_hashes(paths: list[str], future: dict[str, str] | None = None) -> dict[str, str]:
    future = future or {}
    return {p: R.sha(future[p].encode("utf-8") if p in future else (ROOT / p).read_bytes()) for p in paths}


def run_assets(run: str, *, include_stderr: bool) -> list[str]:
    values = [f"{run}/RUN.json", f"{run}/source-manifest.json", f"{run}/index-row-manifest.json", f"{run}/stdout.txt", f"{run}/environment.txt"]
    if include_stderr:
        values.append(f"{run}/stderr.txt")
    return values


def command_pass(argv: list[str], required: str) -> None:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    if result.returncode != 0 or required not in output:
        raise SystemExit(f"PRECHECK_FAILED:{' '.join(argv)}\n{output}")


def assert_run(run: str, proof: str, claims: list[str]) -> None:
    receipt = json.loads((ROOT / f"{run}/RUN.json").read_text(encoding="utf-8"))
    rows = json.loads((ROOT / f"{run}/index-row-manifest.json").read_text(encoding="utf-8"))
    if (receipt.get("proof_id") != proof or receipt.get("claim_ids") != claims
            or receipt.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or receipt.get("exit_code") != 0
            or receipt.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
            or rows.get("claim_ids") != claims or len(rows.get("rows", [])) != len(claims) + 1):
        raise SystemExit(f"PROOF_RUN_NOT_FINAL:{proof}")


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "global/local 与 fiberwise/familywise 的抽象差被两个作者源码包机器化；理论简化的具体删项已可定位。",
        "KC-000005": "natural consumer 已找到，但受限接口保住来源任务；候选按反解释降为 defense works，下一步回 CE-MAP。",
        "KC-000007": "source-guided proposal 经作者代码、历史工具链、负控制与跨框架重放，形成新的机器搜索样板。",
        "KC-000010": "没有把 internal classifier extension 写成 basic HoTT BUG，也没有把已发表 no-go 写成原创发现。",
        "KC-000011": "global 数据先固定、local variable 后使用的依赖顺序属于时序；本轮没有用它替代物理时间/稠密性。",
        "KC-000012": "LOPS/ITT postulates、tiny adjunction、RFib_repl、qq、extension_rule__emptyctx 均在 assumptions/source 中显式保留。",
        "KC-000013": "global classifier真实能力与 local/open classifier更强任务被分开，避免能力层级冒充。",
        "KC-000015": "抽象变化固定为 global→local、fiberwise→familywise，以及删除 transport/context来源。",
        "KC-000021": "C-233–C-243 两个 external package 均有 source/toolchain/run/index/freeze/exact replay；Git仍未闭合。",
        "KC-000022": "方向 B 的能力提升与方向 A 的新增 context/naturality 义务在同一 TaskSpec 中出现。",
        "KC-000027": "CCHM/CCTT、interval/path、fibration universe 与 HIT consumer 使现象具 HoTT/cubical 特异性。",
        "KC-000029": "理论经济收益是把 global/pointwise 构造内化；支付是 crisp zone、DFib+Trans 或 pointwise-fibrant input。",
        "KC-000031": "来源系统主动实施支付并完成真实任务，故本轮判 defense works with explicit payment。",
        "KC-000035": "modal type checker 的 local-variable拒绝证明表达层级不是纯文字围栏。",
        "KC-000036": "CE-MAP 将归约同型 no-go并保留 Gödel/R3/R4、Oracle、现实与物理时间未覆盖 cells。",
    }
    lines = [f"# 核心认知逐编号回评：{SESSION_ID}", "",
             f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；Goal 保持 active。", "",
             "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
             "|---|---|---|---|---|---|"]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{AUDIT}`；{kid} | CE-MAP、经验 reality、ambient R2、完整 R4/Gödel、全面覆盖仍开放。 |")
    lines += ["", "## 四件套交叉与更新归属", "",
              "- core_change: NO — 无新用户悖论／元数学原文。",
              "- direction_change: YES_IN_PLACE — consumer/支付审计关闭，第一 successor 转 CE-MAP。",
              "- panorama_change: YES_IN_PLACE — 新增 LOPS/ITT 两个 machine outcome 与综合 defense outcome。",
              "- essay_change: NO。",
              "- update_decision: natural consumer record 闭合为 defense works；新增 active CE-MAP TaskSpec。",
              "- cross_conflicts: naive local/open classifier是扩大任务域；不能与成功 global/qualified task伪称同一输入域。",
              "- unresolved: CE-MAP remainder、经验现实桥梁、R3/R4 Gödel、ambient R2、Oracle、物理时间与全面文献。"]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    required = [GOAL, FEATURE, PROGRAM_005, PROGRAM_006, PROGRAM_TEST, LIT_INDEX, LIT_006, CE_DOC,
                AUDIT, MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, VERIFIER, PREPARE,
                *run_assets(LOPS_RUN, include_stderr=False), *run_assets(ITT_RUN, include_stderr=True)]
    if any(not (ROOT / p).is_file() for p in required):
        raise SystemExit(f"S149_EVIDENCE_MISSING:{[p for p in required if not (ROOT / p).is_file()]}")
    assert_run(LOPS_RUN, LOPS_PROOF, LOPS_CLAIMS)
    assert_run(ITT_RUN, ITT_PROOF, ITT_CLAIMS)
    registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
    if len(registry.get("later_packages", [])) != 24 or registry.get("later_machine_proved_claim_count") != 95:
        raise SystemExit("S149_REGISTRY_COUNT_INVALID")
    command_pass(["python3", "-B", VERIFIER, "--run-dir", LOPS_RUN], '"status": "PASS_WITH_SCOPE"')
    command_pass(["python3", "-B", VERIFIER, "--run-dir", ITT_RUN], '"status": "PASS_WITH_SCOPE"')
    command_pass(["python3", "-B", PROGRAM_TEST], "Ran 5 tests")
    command_pass(["python3", "-B", "scripts/audit/verify_governance_shards.py"], '"status": "PASS"')

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 148 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_148_S148")
    for identity in (LOPS_ID, ITT_ID, CE_ID, SESSION_ID):
        if identity in state["records"]:
            raise SystemExit(f"S149_RECORD_ALREADY_EXISTS:{identity}")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    d2 = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][d2] = replace_line(direction["shards"][d2], "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 与根 `goal.md` 为唯一工作面推进计算合法性／不可停机／Gödel 到 HoTT 现实相对悖论；C-188–C-243 已形成 R2、syntax 与 internalisation 正负链，natural consumer存在但受限接口保住任务 | 用户当前 App Goal；`goal.md`；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY`, `THEORY_ECONOMY` | `OUT-TOP-2LTT-FR-UIP-MACHINE`、`OUT-TOP-LOPS-INTERNAL-UNIVERSE-CRISP`、`OUT-TOP-ITT-REPLACEMENT-BOUNDARY`、`OUT-TOP-INTERNALISATION-CONSUMER-DEFENSE` | 当前做 `CE-MAP-001`，归约同型 no-go并选择未被 defense覆盖的 cell；保持 Gödel/R3/R4、Oracle、ambient R2、时间与 reality 返回口 | `goal.md`；C-188–C-243；当前 consumer 审计 |")
    d3 = "方向追踪/003 - LocalGPT 与 WebGPT 方向.md"
    direction["shards"][d3] = replace_line(direction["shards"][d3], "| `DIR-L-THEORY-SCHEMA-VARIANTS`",
        "| `DIR-L-THEORY-SCHEMA-VARIANTS` | bare/axiomatic、cubical、guarded/clocked、directed、linear/quantitative/effectful 与 2LTT/groupoid-syntax/ITT/crisp 变体规则比较 | LocalGPT、WebGPT Theory Schema；当前 LIT-HOTT | `SUPPORTING_DIRECTION` | `THEORY_SCHEMA`, `HOTT_OBJECT`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `OUT-L-TIME-BOUNDARY`、`OUT-TOP-G-HOTT-GROUPOID-SYNTAX`、`OUT-TOP-2LTT-FR-UIP-MACHINE`、`OUT-TOP-LOPS-INTERNAL-UNIVERSE-CRISP`、`OUT-TOP-ITT-REPLACEMENT-BOUNDARY` | C-223–C-243 固定 syntax/internalisation/支付切片；下一由 CE-MAP归约并继续完整 R4 | `HoTT/THEORY_SCHEMA.md`；`LIT-HOTT-COMPUTABILITY-001.md`；C-223–C-243 |")
    for old, new in (("source_state_revision: 148", "source_state_revision: 149"),
                     ("projection_generation: 20260915-direction-130", "projection_generation: 20260915-direction-131"),
                     ("状态：`CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_2LTT_FR_UIP_MACHINE_PROVED_NATURAL_CONSUMER_NEXT`", f"状态：`{STATUS}`"),
                     ("semantic_status: CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_2LTT_FR_UIP_MACHINE_PROVED_NATURAL_CONSUMER_NEXT", f"semantic_status: {STATUS}")):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    p3 = "全景视野/003 - 当前机器证明包与原生重放.md"
    projection_edit.append_to_shard(panorama, p3,
        "| `OUT-TOP-LOPS-INTERNAL-UNIVERSE-CRISP` | C-233–C-238：LOPS 官方 Agda-flat full suite；ordinary internal classifier→fiberwise-to-familywise→interval collapse；crisp/tiny classifier recovery + local negative control | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-L-THEORY-SCHEMA-VARIANTS`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | `MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001` | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / NO_GO_AND_CRISP_RECOVERY` | clean Agda-flat 2.6.0.1-70899fb；13 upstream files；positive/local-negative；exact replay | explicit funext/UIP/interval/cof/tiny postulates；不证明 basic HoTT 矛盾、原创性或经验 reality | C-233–C-238；当前 consumer 审计 |\n")
    projection_edit.append_to_shard(panorama, p3,
        "| `OUT-TOP-ITT-REPLACEMENT-BOUNDARY` | C-239–C-243：regular open-family replacement→False；actual QIT只给 DFib；RFib ↔ DFib+Trans；motive/emptyctx 限制 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-L-THEORY-SCHEMA-VARIANTS`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | `MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001` | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / REGULAR_NOGO_DEGENERATE_RECOVERY` | emptyctx@28a2568，Coq 8.13.2，fresh source/assumptions exact replay | subtree无 license不 vendored；完整 Model_structure 未在8.13重放；不证明 basic HoTT/reality | C-239–C-243；当前 consumer 审计 |\n")
    p4 = "全景视野/004 - 距离综合与消费者审计.md"
    panorama["shards"][p4] = replace_line(panorama["shards"][p4], "| `OUT-TOP-2LTT-FR-UIP-CANDIDATE`",
        "| `OUT-TOP-2LTT-FR-UIP-CANDIDATE` | 2LTT replacement→UIP 已机器证明；LOPS/ITT/Swan/Reedy 发现真实 consumer 与三类支付：crisp global、DFib+Trans、pointwise-fibrant input | `DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-THEORY-SCHEMA-VARIANTS` | C-227–C-243 + primary consumer chain | `NATURAL_CONSUMER_FOUND / DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT / NOT_GOAL_COMPLETE` | exact no-go、native controls、作者 dual replays 与 modal rejection | unqualified local/open task扩大输入域；受限接口完成真实来源任务；非 basic BUG、非原创、经验 bridge OPEN | `LIT-HOTT-COMPUTABILITY-001/006 - internal classifier消费者与受限恢复.md`；当前 consumer 审计 |")
    projection_edit.append_to_shard(panorama, p4,
        "| `OUT-TOP-INTERNALISATION-CONSUMER-DEFENSE` | fibration universe、HIT、model structure、Reedy diagrams 是真实 natural consumers；普通 internalisation抹掉 global/local、transport或pointwise资格，受限系统恢复并完成来源任务 | `DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | LOPS、ITT、Swan–Uemura、2LTT primary + C-227–C-243 | `VERIFIED_WITH_SCOPE / DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT` | 两作者机器 dual replay + 两 primary consumer 对照 | 不排除其它 consumer 拒绝支付；不证明经验现实悖论或全部 internalisation class | `audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md` |\n")
    for old, new in (("source_state_revision: 148", "source_state_revision: 149"),
                     ("projection_generation: 20260915-outcome-130", "projection_generation: 20260915-outcome-131"),
                     ("状态：`CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_2LTT_FR_UIP_MACHINE_PROVED_NATURAL_CONSUMER_NEXT`", f"状态：`{STATUS}`"),
                     ("semantic_status: CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_2LTT_FR_UIP_MACHINE_PROVED_NATURAL_CONSUMER_NEXT", f"semantic_status: {STATUS}")):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m1 = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][m1] = replace_once(memory["shards"][m1], "## 当前执行队列（2026-09-14）", "## 当前执行队列（2026-09-15）")
    memory["shards"][m1] = replace_once(memory["shards"][m1],
        "C-188–C-232 已在 main 形成 R1/R2、exact syntax slice 与 2LTT replacement→UIP 条件边界：C-227–C-232 具 S¹/identity-R controls 与 exact replay。最终 HoTT witness 未找到。",
        "C-188–C-243 已在 main 形成 R1/R2、exact syntax 与 internalisation 正负链：2LTT R→UIP、LOPS classifier/crisp、ITT regular/degenerate+transport 均 exact replay。natural consumer 存在但受限接口保住任务；最终 HoTT witness 未找到。")
    memory["shards"][m1] = replace_once(memory["shards"][m1], "17 个冻结 + 22 个 later package", "17 个冻结 + 24 个 later package")
    memory["shards"][m1] = replace_once(memory["shards"][m1],
        "Post/Parametric CT/Oracle/groupoid-syntax 三向薄切与 2LTT replacement 数学核均已完成 scoped 增量。当前优先 `NATURAL-CONSUMER-002` + crisp/base-change 消融，并行 CE-MAP、Oracle old-toolchain/modal→ambient、ambient R2、完整 R4 与 reality。",
        "Post/Parametric CT/Oracle/groupoid-syntax、2LTT replacement 与 natural-consumer/支付消融均有 scoped evidence。当前优先 `CE-MAP-001`；并行保留 Oracle、ambient R2、完整 R4/Gödel、物理时间与 reality。")
    m2 = "MEMORY/002 - 当前证据上限与恢复入口.md"
    memory["shards"][m2] = replace_once(memory["shards"][m2],
        "2LTT/QIIT/QIIRT/内部模型资料支持自我元理论分层；C-223–C-226 机器重放 Π/U/El groupoid-syntax exact slice；C-227–C-232 机器证明 context-uniform replacement fragment→inner UIP，并有 S¹/identity-R controls。它是已发表可选扩展边界，不自动证明 HoTT coverage failure。",
        "2LTT/QIIT/QIIRT/内部模型资料支持自我元理论分层；C-223–C-243 已机器覆盖 groupoid syntax、R→UIP、internal classifier interval collapse/crisp recovery 与 regular/degenerate+transport。natural consumer真实，但受限接口完成来源任务，故仍是 defense/qualification boundary。")
    memory["shards"][m2] = replace_once(memory["shards"][m2],
        "C-223–C-226 是首个 exact syntax slice，C-227–C-232 闭合 replacement→UIP 分支。完整 R4、ambient HoTT no-decider、natural consumer、现实桥梁与学术全面覆盖均开放。",
        "C-223–C-243 形成 syntax/internalisation/consumer/支付链。完整 R4/Gödel、ambient HoTT no-decider、CE-MAP、经验现实桥梁与学术全面覆盖均开放。")
    projection_edit.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S149 internalisation consumers：LOPS 官方 Agda-flat C-233–C-238 与 ITT Coq C-239–C-243 exact replay；fibration universe/HIT/model structure/Reedy natural consumers 已找到。ordinary local/open promotion导致 interval collapse/False；crisp global、DFib+Trans、pointwise-fibrant input完成来源任务，判 `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`。registry=17 frozen +24 later/95 claims；下一 `CE-MAP-001`；Goal active。\n")

    essay = projection_edit.load(ROOT, R.ESSAY)
    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S148 2LTT replacement→UIP 数学核完成）", "# HoTT 研究前沿（S149 internalisation consumer/支付消融完成）")
    frontier = replace_once(frontier,
        "C-188–C-232 已在 main 形成分层链：R2 conditional internal no-decider、exact groupoid-syntax slice，以及 C-227–C-232 的 context-uniform replacement→inner UIP 条件边界。S¹ 非平凡环路与 identity-R 消融均已机器化；这是已发表可选扩展 no-go，不是 basic HoTT/2LTT 矛盾。当前优先 `NATURAL-CONSUMER-002` 与 crisp/base-change 同任务消融；ambient R2、完整 R4、CE-MAP、现实 bridge 与全面覆盖均 OPEN。",
        "C-188–C-243 已在 main 形成 R2、syntax 与 internalisation 正负链。LOPS/ITT exact replay确认 global→local、fiberwise→familywise会坍缩 interval/推出 False；fibration universe、HIT、model structure、Reedy natural consumers真实，但 crisp、DFib+Trans、pointwise-fibrant限制完成来源任务。当前判 `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`，第一 successor=`CE-MAP-001`；ambient R2、完整 R4/Gödel、物理时间、经验 reality 与全面覆盖均 OPEN。")
    frontier = replace_once(frontier,
        "| 当前高判别候选 | 2LTT replacement 的 natural consumer 与 crisp/base-change 支付 | `MATH_CORE_MACHINE_PROVED / CONSUMER_OPEN` | 冻结真实调用链与同一任务；识别 p-dependent R 使用；对 crisp/outer-only 接口做消融；无 consumer 则封为 known boundary 并回 CE-MAP |",
        "| 当前高判别候选 | CE-MAP 八轴映射与 internalisation 同型类归约 | `TASKSPEC_ACTIVE / IMPLEMENTATION_NOT_STARTED` | 构建 canonical mapping/UNCLASSIFIED/receipt；归约 C-227–C-243；选择未被 defense覆盖的 cell并保留 Gödel/时间/reality 返回口 |")
    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"): lessons += "\n"
    lessons += ("\n109. natural consumer存在不自动构成 natural-use mismatch：必须比较消费者真实 input domain。LOPS 的 global classifier与 naive local classifier、ITT 的 DFib replacement与 open-family RFib replacement不是同一资格范围；扩大后的任务失败不能归咎于完成原任务的受限接口。\n"
                "\n110. global/local context zone是一种精确时序/来源纪律：先固定 global object后编码，不允许 code依赖当前 local i。modal checker的 expected rejection把这条先后约束从哲学描述变成可执行判据；它不等于物理时间或稠密连续性。\n"
                "\n111. fibrancy payment有可归约的三种实现：crisp/global restriction、DFib+Trans decomposition、pointwise-fibrant input。CE-MAP 应把同型 no-go归类而非重复当新悖论，同时保留它们对不同 consumers 的差异。\n"
                "\n112. 外部源码无 license时不因公开可读就复制正文；可保存 deterministic archive/hash/tree、项目 probe 与 run。来源许可和数学重放是两条独立证据维度。\n")
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS149：C-233–C-238 LOPS Agda-flat full suite与 C-239–C-243 ITT Coq regular/degenerate boundary均 exact replay。natural consumers=fibration universe/HIT/model structure/Reedy；ordinary local/open promotion失败，crisp global、DFib+Trans、pointwise input保住真实任务，判 defense works。registry=24 later/95 claims；active=`A-CE-MAP-001`；Goal保持 active。\n\n")

    state["revision"] = 149
    state["latest_session"] = SESSION_ID
    state["active"] = ["I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912", GOAL_ID, CE_ID]
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_INTERNALISATION_CONSUMER_DEFENSE"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Implement CE-MAP-001 canonical eight-axis mapping, preserve every frozen input and UNCLASSIFIED remainder, reduce the C-227-C-243 internalisation class with explicit preservation contracts, then select the next uncovered HoTT-specific cell."
    state["projection"]["status"] = STATUS
    for key, generation in (("I-DIRECTION-PORTFOLIO-20260912", "20260915-direction-131"), ("I-OUTCOME-PANORAMA-20260912", "20260915-outcome-131")):
        state["records"][key]["projection_generation"] = generation
        state["records"][key]["semantic_status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = "Current portfolio through C-243: internalisation consumers are real but qualified interfaces complete source tasks; CE-MAP is active and Goal remains open."
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = "Integrated outcomes through C-243: internal classifier/replacement class is machine-replayed and defended with explicit payment; no qualified reality-relative paradox or full R4/Godel result."

    lops_sources = [f"{LOPS_PACKAGE}/README.md", f"{LOPS_PACKAGE}/CLAIM-INTERNAL-UNIVERSE-CRISP.md", f"{LOPS_PACKAGE}/SOURCE_TREE_MANIFEST.json", f"{LOPS_PACKAGE}/AGDA_FLAT_IMAGE.json", f"{LOPS_PACKAGE}/controls/CrispPositive.agda", f"{LOPS_PACKAGE}/controls/CrispNegative.agda", *[str(p.relative_to(ROOT)) for p in sorted((ROOT / LOPS_PACKAGE / "upstream").rglob("*.agda"))], *run_assets(LOPS_RUN, include_stderr=False), MATRIX, REGISTRY, AUDIT, "scripts/audit/import_lops_internal_universes.py", "scripts/audit/replay_lops_internal_universes.py", "scripts/audit/capture_lops_internal_universes_run.py", VERIFIER]
    state["records"][LOPS_ID] = {"claim_ids": LOPS_CLAIMS, "classification": "INTERNAL_FIBRATION_CLASSIFIER_NOGO_AND_CRISP_RECOVERY", "depends_on": [], "evidence_status": "MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE", "full_sources": lops_sources, "kind": "external_formal_source_replay", "lifecycle_status": "CURRENT", "mathematical_status": "ORDINARY_INTERNAL_CLASSIFIER_COLLAPSES_INTERVAL_CRISP_CLASSIFIER_CONSTRUCTED", "path": f"{LOPS_PACKAGE}/upstream/README.agda", "proof_id": LOPS_PROOF, "run_id": LOPS_RUN_ID, "research_parent": GOAL_ID, "related_records": [GATE_ID, PLAN_ID, LIT_ID, SYNTAX_ID, CONSUMER_ID, CE_ID, SESSION_ID], "resolution": {"evidence": [f"{LOPS_RUN}/RUN.json", f"{LOPS_RUN}/index-row-manifest.json", MATRIX, AUDIT], "reason": "Official full suite and modal controls exact-replay in clean Agda-flat."}, "scope": "C-233-C-238 with explicit funext/UIP/interval/cof/tiny postulates; published no-go/crisp recovery, not basic HoTT inconsistency or empirical reality bridge.", "source_hashes": file_hashes(lops_sources), "status": "complete", "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True}}
    itt_sources = [f"{ITT_PACKAGE}/README.md", f"{ITT_PACKAGE}/CLAIM-DEGENERATE-REGULAR-FIBRANCY.md", f"{ITT_PACKAGE}/CheckReplacementBoundary.v", f"{ITT_PACKAGE}/COQ_IMAGE.json", f"{ITT_PACKAGE}/SOURCE_TREE_MANIFEST.json", *run_assets(ITT_RUN, include_stderr=True), MATRIX, REGISTRY, AUDIT, "scripts/audit/qualify_coq_interval_replacement.py", "scripts/audit/replay_coq_interval_replacement.py", "scripts/audit/capture_coq_interval_replacement_run.py", VERIFIER]
    state["records"][ITT_ID] = {"claim_ids": ITT_CLAIMS, "classification": "REGULAR_REPLACEMENT_NOGO_DEGENERATE_TRANSPORT_RECOVERY", "depends_on": [], "evidence_status": "MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE", "full_sources": itt_sources, "kind": "external_formal_source_replay", "lifecycle_status": "CURRENT", "mathematical_status": "REGULAR_FAMILY_REPLACEMENT_FALSE_DEGENERATE_REPLACEMENT_PLUS_TRANSPORT_BOUNDARY", "path": f"{ITT_PACKAGE}/CheckReplacementBoundary.v", "proof_id": ITT_PROOF, "run_id": ITT_RUN_ID, "research_parent": GOAL_ID, "related_records": [GATE_ID, PLAN_ID, LIT_ID, SYNTAX_ID, CONSUMER_ID, CE_ID, SESSION_ID], "resolution": {"evidence": [f"{ITT_RUN}/RUN.json", f"{ITT_RUN}/index-row-manifest.json", MATRIX, AUDIT], "reason": "Fresh external source build replays negative regular replacement, positive degenerate QIT replacement, fibrancy decomposition and assumptions."}, "scope": "C-239-C-243 only; no subtree redistribution, full Model_structure replay, basic HoTT inconsistency, novelty or empirical reality bridge.", "source_hashes": file_hashes(itt_sources), "status": "complete", "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True}}

    consumer = state["records"][CONSUMER_ID]
    consumer["lifecycle_status"] = "CLOSED"; consumer["status"] = "closed"
    consumer["evidence_status"] = "VERIFIED_WITH_SCOPE / NATURAL_CONSUMER_FOUND / DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT"
    consumer["full_sources"] = [LIT_006, AUDIT, f"{LOPS_RUN}/RUN.json", f"{LOPS_RUN}/index-row-manifest.json", f"{ITT_RUN}/RUN.json", f"{ITT_RUN}/index-row-manifest.json", GOAL]
    consumer["source_hashes"] = file_hashes(consumer["full_sources"])
    consumer["resolution"] = {"evidence": [AUDIT, f"{LOPS_RUN}/RUN.json", f"{ITT_RUN}/RUN.json"], "reason": "Natural consumers were found, but crisp/global, DFib+Trans and pointwise-fibrant restrictions complete their source-defined tasks; the unqualified local/open promotion changes the input domain."}
    consumer["scope"] = "Consumer existence and payment mechanisms are closed with scope. Other consumers may reject payment; empirical same-task reality and basic-theory defect remain open."
    consumer["revalidation"] = f"{SESSION_ID}: replaced NOT_RUN with primary-source and C-233-C-243 machine evidence; closed as defense works, not as a paradox."
    for identity in (LOPS_ID, ITT_ID, CE_ID, SESSION_ID): add_once(consumer.setdefault("related_records", []), identity)

    ce_sources = [CE_DOC, PROGRAM_005, PROGRAM_006, LIT_006, AUDIT, MATRIX, REGISTRY, GOAL]
    state["records"][CE_ID] = {"classification": "EIGHT_AXIS_CANDIDATE_EVIDENCE_MAP_AND_CLASS_REDUCTION", "depends_on": [], "evidence_status": "TASKSPEC_ACTIVE / IMPLEMENTATION_NOT_STARTED", "full_sources": ce_sources, "kind": "machine_overview_coverage_task", "lifecycle_status": "ACTIVE_WORK", "path": CE_DOC, "research_parent": GOAL_ID, "related_records": [PLAN_ID, LIT_ID, LOPS_ID, ITT_ID, CONSUMER_ID, SESSION_ID], "scope": "Map every frozen case/proof/candidate/literature consumer to eight axes, preserve UNCLASSIFIED, reduce only with task/context/observation/completion preservation, and select an uncovered successor.", "source_hashes": file_hashes(ce_sources), "status": "active"}

    lit = state["records"][LIT_ID]
    lit_add = [LIT_INDEX, LIT_006, AUDIT, f"{LOPS_RUN}/RUN.json", f"{LOPS_RUN}/index-row-manifest.json", f"{ITT_RUN}/RUN.json", f"{ITT_RUN}/index-row-manifest.json"]
    for p in lit_add: add_once(lit.setdefault("full_sources", []), p)
    lit["source_hashes"] = file_hashes(lit["full_sources"])
    lit["scope"] = "HoTT-computability/internalisation corpus through C-243: LOPS and ITT consumers/payments machine-replayed; CE-MAP, Dominances, Brouwer Trees, Extension Types, strictified syntax and citation coverage remain open."
    lit["revalidation"] = f"{SESSION_ID}: added shard 006 and the LOPS/ITT exact replays; comprehensive corpus/consumer coverage remains open."
    for identity in (LOPS_ID, ITT_ID, CE_ID, SESSION_ID): add_once(lit.setdefault("related_records", []), identity)
    syntax = state["records"][SYNTAX_ID]
    syntax["evidence_status"] = "FIRST_EXACT_SYNTAX_SLICE / INTERNALISATION_CLASS_C227_C243_MACHINE_EVIDENCE / FULL_CALCULUS_OPEN"
    syntax["scope"] = "Groupoid syntax plus replacement/classifier consumer/defense class are machine-evidenced through C-243; full Nat/Path/univalence/HIT derivation syntax, proof enumeration, arithmetic and R4/Godel remain open."
    for identity in (LOPS_ID, ITT_ID, CE_ID, SESSION_ID): add_once(syntax.setdefault("related_records", []), identity)
    gate = state["records"][GATE_ID]
    for p in [f"{LOPS_RUN}/RUN.json", f"{LOPS_RUN}/index-row-manifest.json", f"{ITT_RUN}/RUN.json", f"{ITT_RUN}/index-row-manifest.json", REGISTRY, MATRIX, VERIFIER]: add_once(gate.setdefault("full_sources", []), p)
    gate["source_hashes"] = file_hashes(gate["full_sources"])
    gate["scope"] = "Exact statement/source/kernel/index gate; registry now has 17 frozen packages, one scoped external replay and 24 later packages / 95 claims."
    gate["revalidation"] = f"{SESSION_ID}: C-233-C-243 are indexed, row-frozen and exact-replayed; all new assets remain local uncommitted."
    for identity in (LOPS_ID, ITT_ID, SESSION_ID): add_once(gate.setdefault("related_records", []), identity)

    for key in (PLAN_ID, COVERAGE_ID, GOAL_ID):
        record = state["records"][key]
        for identity in (LOPS_ID, ITT_ID, CONSUMER_ID, CE_ID, SESSION_ID): add_once(record.setdefault("related_records", []), identity)
    plan_record = state["records"][PLAN_ID]
    for p in (PROGRAM_005, PROGRAM_006, CE_DOC, LIT_INDEX, LIT_006, AUDIT): add_once(plan_record.setdefault("full_sources", []), p)
    plan_record["source_hashes"] = file_hashes(plan_record["full_sources"])
    plan_record["revalidation"] = f"{SESSION_ID}: natural consumer/payment slice is closed as defense works; CE-MAP is the next breadth-first coverage unit."
    coverage = state["records"][COVERAGE_ID]
    for p in (LIT_INDEX, LIT_006, AUDIT): add_once(coverage.setdefault("full_sources", []), p)
    coverage["source_hashes"] = file_hashes(coverage["full_sources"])
    coverage["revalidation"] = f"{SESSION_ID}: LOPS/ITT source and machine evidence deepen one internalisation class; comprehensive literature denominator and holdout remain review_required."
    goal_record = state["records"][GOAL_ID]
    for p in (GOAL, FEATURE, CE_DOC, LIT_INDEX): add_once(goal_record.setdefault("full_sources", []), p)
    goal_record["source_hashes"] = file_hashes(goal_record["full_sources"])
    goal_record["revalidation"] = f"{SESSION_ID}: natural consumers exist but qualified interfaces complete their real tasks; no basic HoTT defect or empirical bridge. Goal remains active and moves to {CE_ID}."

    session_path = f"{SESSION_REL}/SESSION.md"; audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"; runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：2LTT/internal classifier/replacement 的 natural consumer 与 crisp/degenerate/transport 消融。
- LOPS：`{LOPS_PROOF}` / C-233–C-238；官方 13-source full suite + modal controls；exact replay。
- ITT：`{ITT_PROOF}` / C-239–C-243；regular no-go、degenerate QIT、DFib+Trans、motive/emptyctx assumptions；exact replay。
- consumers：fibration universe、HIT、universe-of-all-types model structure、Reedy diagrams。
- 判词：unqualified local/open scope promotion fails；qualified interfaces complete source tasks；`DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`，非 basic HoTT BUG。
- 下一：`{CE_ID}`，归约 internalisation 同型类、列 UNCLASSIFIED、选未覆盖 cell；Gödel/R3/R4、Oracle、时间、reality保持。
- Goal：active；Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
"""
    runs = json.dumps({"schema_version": "hott-session-runs/v2", "session_id": SESSION_ID, "checkpoint_result": RESULT_REL,
        "formal_runs": [{"proof_id": LOPS_PROOF, "run_id": LOPS_RUN_ID, "claims": LOPS_CLAIMS, "status": "PASS_WITH_SCOPE / EXACT_REPLAY"}, {"proof_id": ITT_PROOF, "run_id": ITT_RUN_ID, "claims": ITT_CLAIMS, "status": "PASS_WITH_SCOPE / EXACT_REPLAY"}],
        "source_controls": {"lops": "13 sources / clean agda-flat / local negative", "itt": "20-file external archive / no-license boundary / assumptions", "model_structure_coq8132": "EXPECTED_VERSION_COMPATIBILITY_FAILURE_AT_PLACEHOLDER"},
        "verdict": "NATURAL_CONSUMER_FOUND_DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT_NOT_GOAL_COMPLETE",
        "next": [CE_ID, "CLASSIFIER-REALITY-BRIDGE-001", "R3-R4-GODEL-RETURN-001", "ORACLE-MODALITY-REPLAY-001", "R2-AMBIENT-UNDEC-001"]}, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {"depends_on": [], "evidence_status": "MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE", "full_sources": [session_path, audit_path, runs_path, RESULT_REL, AUDIT, f"{LOPS_RUN}/RUN.json", f"{ITT_RUN}/RUN.json"], "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path, "related_records": [PREV, GOAL_ID, PLAN_ID, LIT_ID, SYNTAX_ID, CONSUMER_ID, LOPS_ID, ITT_ID, CE_ID], "scope": "Close natural-consumer/payment evidence for the internalisation class and route CE-MAP without completing the Goal.", "source_hashes": {}, "status": "complete"}

    texts: dict[str, str] = {p: (ROOT / p).read_text(encoding="utf-8") for p in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]; texts.update(document["shards"])
    texts[frontier_path] = frontier; texts[lessons_path] = lessons; texts[resume_path] = resume
    texts[session_path] = session; texts[audit_path] = audit_text(); texts[runs_path] = runs
    changed = [GOAL, FEATURE, PROGRAM_005, PROGRAM_006, PROGRAM_TEST, LIT_INDEX, LIT_006, CE_DOC, MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, VERIFIER, f"{LOPS_RUN}/RUN.json", f"{LOPS_RUN}/index-row-manifest.json", f"{ITT_RUN}/RUN.json", f"{ITT_RUN}/index-row-manifest.json", *texts.keys()]
    for record in state["records"].values():
        source_hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(source_hashes, dict): continue
        rebound = []
        for p in changed:
            if p not in source_hashes or p == R.STATE: continue
            data = texts[p].encode("utf-8") if p in texts else (ROOT / p).read_bytes()
            h = R.sha(data)
            if source_hashes[p] != h: source_hashes[p] = h; rebound.append(p)
        if rebound and record not in (state["records"][LOPS_ID], state["records"][ITT_ID]):
            note = f"{SESSION_ID}: revalidated after current owner/proof-index/verifier evolution at {', '.join(rebound)}; prior mathematical scopes remain unchanged."
            previous = record.get("revalidation"); record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID, "authorization": "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries.", "load_profile": "governance", "task_ids": [], "files": [{"path": p, "expected_sha256": R.sha((ROOT / p).read_bytes()) if (ROOT / p).exists() else None, "text": value} for p, value in texts.items()]}
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 149, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
