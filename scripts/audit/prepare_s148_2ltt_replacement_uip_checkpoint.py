#!/usr/bin/env python3
"""Prepare revision 148: record the 2LTT replacement-to-UIP proof and next consumer task."""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260915-148-2LTT-FR-UIP"
PREV = "S-GOV-20260915-147-LOGICAL-SHARD-ORDER"
STATUS = "CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_2LTT_FR_UIP_MACHINE_PROVED_NATURAL_CONSUMER_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_ID = "A-LIT-HOTT-COMPUTABILITY-001"
SYNTAX_ID = "A-G-HOTT-SYNTAX-001"
CAND_ID = "A-CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001"
FORMAL_ID = "A-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001"
CONSUMER_ID = "A-NATURAL-CONSUMER-2LTT-REPLACEMENT-002"
PROOF_GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"

PROOF_ID = "MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001"
CLAIMS = ["C-227", "C-228", "C-229", "C-230", "C-231", "C-232"]
RUN_ID = "20260915-MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001-01"
RUN = f"HoTT/verification/runs/{RUN_ID}"
PACKAGE = "HoTT/formal/two-level-fibrant-replacement-uip"
SOURCE = f"{PACKAGE}/TwoLevelReplacementUIP.agda"
CLAIM_DOC = f"{PACKAGE}/CLAIM-TWO-LEVEL-FIBRANT-REPLACEMENT-UIP.md"
PACKAGE_README = f"{PACKAGE}/README.md"
AUDIT = "audit/2LTT内部纤维替换导致UIP机器证明与悖论判别-20260915.md"
LIT_INDEX = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md"
LIT_ROOT = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001"
LIT_005 = f"{LIT_ROOT}/005 - 2LTT replacement机器结果与消费者下一步.md"
PAPER = "audit/literature/LIT-CLASSICS-001/mineru/Annenkov-Capriotti-Kraus-Sattler-2017-2LTT/full.md"
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
PREPARE = "scripts/audit/prepare_s148_2ltt_replacement_uip_checkpoint.py"

SPEC = importlib.util.spec_from_file_location("runtime_s148", RUNTIME_PATH)
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


def hashes(paths: list[str], future: dict[str, str] | None = None) -> dict[str, str]:
    future = future or {}
    return {
        path: R.sha(future[path].encode("utf-8") if path in future else (ROOT / path).read_bytes())
        for path in paths
    }


def run_assets() -> list[str]:
    # stderr is intentionally omitted from task hydration because it is the
    # valid zero-byte artifact fixed by RUN.json.
    return [
        f"{RUN}/RUN.json", f"{RUN}/source-manifest.json",
        f"{RUN}/index-row-manifest.json", f"{RUN}/stdout.txt",
        f"{RUN}/environment.txt",
    ]


def command_pass(argv: list[str], required: str) -> None:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    if result.returncode != 0 or required not in output:
        raise SystemExit(f"PRECHECK_FAILED:{' '.join(argv)}\n{output}")


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "两层 code/El 接口阻止宿主 Path 消去越界，精确定位理论层级改变，而不是把同名 Type 混为一层。",
        "KC-000005": "候选数学核已完成 C-227–C-232；本轮没有因投入量把它升级为最终悖论，第一 successor 转 natural consumer。",
        "KC-000007": "source-guided 候选已进入生成→形式化→控制→判词→下一消费者的真实闭环。",
        "KC-000010": "basic 2LTT/HoTT、可选 context-uniform R 与现实使用三者保持分层，未把已知 no-go 冒充 HoTT BUG。",
        "KC-000012": "R 的形成/引入/依赖消去与 outer UIP 是显式 ASK 前提；COMP-R 未进入接口。",
        "KC-000013": "对象存在、逐对象外部 replacement、内部统一 type former 与现实交付继续区分。",
        "KC-000015": "C-228 把抽象变化固定为 R 对 p-dependent StrictWitness 的 context-uniform 可用性。",
        "KC-000021": "C-227–C-232 具 source/run/index/freeze/exact replay；Git 仍 local-uncommitted。",
        "KC-000022": "A 读法是统一内化新增相干义务，B 读法是 external capability 被提升为 internal operation；两者都待 natural consumer。",
        "KC-000027": "原生 S¹ 非平凡环路参与反控制，HoTT higher structure 不再只是口头标签。",
        "KC-000029": "理论经济收益与代价被同一构造表达：逐例外部操作压成统一内部接口，代价是 inner UIP。",
        "KC-000031": "发现的是学界已知可选扩展边界；拒绝 R 或用 crisp/modal restriction 是现有防线。",
        "KC-000035": "两层表达边界通过 Inner code 与 outer Type 机械化，避免单层 shallow embedding 假证。",
        "KC-000036": "R4 仍缺完整 calculus/representability/Gödel sentence；本包只闭合 replacement→UIP 分支。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；Goal 保持 active。", "",
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
            "natural consumer、same-task reality、ambient R2、完整 R4、CE-MAP 与全面覆盖仍开放。 |"
        )
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — replacement 数学核关闭，第一 successor 转 natural consumer/crisp ablation。",
        "- panorama_change: YES_IN_PLACE — 新增 C-227–C-232 proof outcome，并原位更新 candidate 判词。",
        "- essay_change: NO。",
        "- update_decision: 2LTT candidate 关闭为机器证明的已知扩展边界；另建 active consumer task，Goal 不完成。",
        "- cross_conflicts: 论文已知 no-go 与用户希望寻找新 HoTT BUG 不同；机器化提高证据，不制造原创性。",
        "- unresolved: natural consumer、crisp/base-change same-task ablation、reality bridge、full R4/Gödel、coverage。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        GOAL, FEATURE, PROGRAM_005, PROGRAM_006, PROGRAM_TEST, LIT_INDEX, LIT_005,
        SOURCE, CLAIM_DOC, PACKAGE_README, AUDIT, MATRIX, REGISTRY,
        FORMAL_README, RUNS_README, HOTT_README, PREPARE,
        "scripts/audit/capture_agda_proof_run.py", "scripts/audit/verify_formal_proof_run.py",
        *run_assets(),
    ]
    if any(not (ROOT / path).is_file() for path in required):
        raise SystemExit(f"S148_EVIDENCE_MISSING:{[p for p in required if not (ROOT / p).is_file()]}")
    receipt = json.loads((ROOT / f"{RUN}/RUN.json").read_text(encoding="utf-8"))
    frozen = json.loads((ROOT / f"{RUN}/index-row-manifest.json").read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or receipt.get("exit_code") != 0
        or receipt.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or receipt.get("proof_id") != PROOF_ID
        or receipt.get("claim_ids") != CLAIMS
        or frozen.get("claim_ids") != CLAIMS
        or len(frozen.get("rows", [])) != 7
    ):
        raise SystemExit("S148_PROOF_RUN_NOT_FINAL")
    registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
    if len(registry.get("later_packages", [])) != 22 or registry.get("later_machine_proved_claim_count") != 84:
        raise SystemExit("S148_REGISTRY_COUNT_INVALID")
    command_pass(["python3", "-B", "scripts/audit/verify_formal_proof_run.py", "--run-dir", RUN], '"status": "PASS_WITH_SCOPE"')
    command_pass(["python3", "-B", PROGRAM_TEST], "Ran 5 tests")
    command_pass(["python3", "-B", "scripts/audit/verify_governance_shards.py"], '"status": "PASS"')

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 147 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_147_S147")
    if FORMAL_ID in state["records"] or CONSUMER_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("S148_RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    d2 = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][d2] = replace_line(
        direction["shards"][d2], "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 与根 `goal.md` 为唯一工作面推进计算合法性／不可停机／Gödel 到 HoTT 现实相对悖论；R2 有 conditional internal no-decider，G-HOTT-SYNTAX 有 exact slice，C-227–C-232 已闭合 2LTT replacement→UIP 核 | 用户当前 App Goal；`goal.md`；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY`, `THEORY_ECONOMY` | `OUT-TOP-R2-PARAMETRIC-CT-INTERNAL-UNDEC`、`OUT-TOP-G-HOTT-GROUPOID-SYNTAX`、`OUT-TOP-2LTT-FR-UIP-CANDIDATE` | 当前做 `NATURAL-CONSUMER-002` 与 crisp/base-change 同任务消融；并行保持 CE-MAP、Oracle、ambient R2、完整 R4、现实 bridge | `goal.md`；C-219–C-232；`audit/2LTT内部纤维替换导致UIP机器证明与悖论判别-20260915.md` |",
    )
    d3 = "方向追踪/003 - LocalGPT 与 WebGPT 方向.md"
    direction["shards"][d3] = replace_line(
        direction["shards"][d3], "| `DIR-L-THEORY-SCHEMA-VARIANTS`",
        "| `DIR-L-THEORY-SCHEMA-VARIANTS` | bare/axiomatic、cubical、guarded/clocked、directed、linear/quantitative/effectful 与 2LTT/groupoid-syntax 变体规则比较 | LocalGPT、WebGPT Theory Schema；当前 LIT-HOTT | `SUPPORTING_DIRECTION` | `THEORY_SCHEMA`, `HOTT_OBJECT`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `OUT-L-TIME-BOUNDARY`、`OUT-TOP-G-HOTT-GROUPOID-SYNTAX`、`OUT-TOP-2LTT-FR-UIP-CANDIDATE` | C-223–C-226 固定 exact syntax slice；C-227–C-232 固定 context-uniform R→UIP；下一核对 natural consumer、crisp/base-change 与完整 R4 | `HoTT/THEORY_SCHEMA.md`；`LIT-HOTT-COMPUTABILITY-001.md`；C-223–C-232 |",
    )
    for old, new in (
        ("source_state_revision: 147", "source_state_revision: 148"),
        ("projection_generation: 20260915-direction-129", "projection_generation: 20260915-direction-130"),
        ("状态：`CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_COMPLETE_2LTT_FR_UIP_NEXT`", f"状态：`{STATUS}`"),
        ("semantic_status: CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_COMPLETE_2LTT_FR_UIP_NEXT", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    proof_row = (
        "| `OUT-TOP-2LTT-FR-UIP-MACHINE` | C-227–C-232：边界保持两层接口中，context-uniform FORM/INTRO/dependent-ELIM for R + outer UIP 推出 inner UIP；原生 S¹ 与 native identity-R controls | "
        "`DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-L-THEORY-SCHEMA-VARIANTS`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | `MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / KNOWN_INCOMPATIBLE_EXTENSION_BOUNDARY` | Agda 2.8.0/Cubical v0.9，exit 0、stderr 0、7 rows frozen、exact replay | "
        "不证明 basic HoTT/2LTT 矛盾、原创性、natural consumer 或现实桥梁；COMP-R 未使用 | C-227–C-232；`audit/2LTT内部纤维替换导致UIP机器证明与悖论判别-20260915.md` |\n"
    )
    projection_edit.append_to_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", proof_row)
    p4 = "全景视野/004 - 距离综合与消费者审计.md"
    panorama["shards"][p4] = replace_line(
        panorama["shards"][p4], "| `OUT-TOP-2LTT-FR-UIP-CANDIDATE`",
        "| `OUT-TOP-2LTT-FR-UIP-CANDIDATE` | 2LTT §2.7 的 external pointwise replacement→context-uniform internal R→inner UIP 已由 C-227–C-232 机器重构；论文指出 external replacement 通常不保 base change | `DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-THEORY-SCHEMA-VARIANTS` | 2LTT primary + 当前 formal/run | `MACHINE_PROVED_LOCAL_UNCOMMITTED / KNOWN_INCOMPATIBLE_EXTENSION_BOUNDARY / NATURAL_CONSUMER_OPEN` | 最小两层接口、S¹ 非平凡环路、identity-R 消融和 COMP-R 非必要均已机器化 | basic theory 可拒绝 R 或限制 crisp；尚无 natural consumer、same-task reality 与 novelty；未达到最终悖论 | `LIT-HOTT-COMPUTABILITY-001/005 - 2LTT replacement机器结果与消费者下一步.md`；C-227–C-232；当前审计 |",
    )
    for old, new in (
        ("source_state_revision: 147", "source_state_revision: 148"),
        ("projection_generation: 20260915-outcome-129", "projection_generation: 20260915-outcome-130"),
        ("状态：`CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_COMPLETE_2LTT_FR_UIP_NEXT`", f"状态：`{STATUS}`"),
        ("semantic_status: CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_COMPLETE_2LTT_FR_UIP_NEXT", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m1 = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][m1] = replace_once(memory["shards"][m1],
        "C-188–C-226 已在 main 形成 R1/R2 与首个 exact syntax slice：R2 synthetic dual-kernel + 显式 EPF/SCT 前提下 internal no-decider；groupoid syntax 20 模块/`isSetTy`/四类同构 exact replay。最终 HoTT witness 未找到。",
        "C-188–C-232 已在 main 形成 R1/R2、exact syntax slice 与 2LTT replacement→UIP 条件边界：C-227–C-232 具 S¹/identity-R controls 与 exact replay。最终 HoTT witness 未找到。")
    memory["shards"][m1] = replace_once(memory["shards"][m1],
        "17 个冻结 + 21 个 later package", "17 个冻结 + 22 个 later package")
    memory["shards"][m1] = replace_once(memory["shards"][m1],
        "Post primary、Parametric CT、Oracle Modalities、2LTT 与 groupoid-syntax 三向薄切已完成 scoped 增量。当前优先 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001` 最小机器化，并行 CE-MAP、Oracle old-toolchain/modal→ambient、ambient R2、完整 R4、natural consumer/reality。",
        "Post/Parametric CT/Oracle/groupoid-syntax 三向薄切与 2LTT replacement 数学核均已完成 scoped 增量。当前优先 `NATURAL-CONSUMER-002` + crisp/base-change 消融，并行 CE-MAP、Oracle old-toolchain/modal→ambient、ambient R2、完整 R4 与 reality。")
    m2 = "MEMORY/002 - 当前证据上限与恢复入口.md"
    memory["shards"][m2] = replace_once(memory["shards"][m2],
        "2LTT/QIIT/QIIRT/内部模型资料支持自我元理论分层；C-223–C-226 机器重放了一个 Π/U/El groupoid-syntax exact slice。2LTT internal fibrant replacement→UIP 目前仍是 source-reported candidate，不自动证明 HoTT coverage failure。",
        "2LTT/QIIT/QIIRT/内部模型资料支持自我元理论分层；C-223–C-226 机器重放 Π/U/El groupoid-syntax exact slice；C-227–C-232 机器证明 context-uniform replacement fragment→inner UIP，并有 S¹/identity-R controls。它是已发表可选扩展边界，不自动证明 HoTT coverage failure。")
    memory["shards"][m2] = replace_once(memory["shards"][m2],
        "C-223–C-226 是首个 exact syntax slice。完整 R4、HoTT essentiality、natural consumer、现实桥梁与学术全面覆盖均开放。",
        "C-223–C-226 是首个 exact syntax slice，C-227–C-232 闭合 replacement→UIP 分支。完整 R4、ambient HoTT no-decider、natural consumer、现实桥梁与学术全面覆盖均开放。")
    projection_edit.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S148 2LTT replacement→UIP：`MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` / C-227–C-232 在边界保持的 inner-code/outer-Type 接口中证明 context-uniform R + outer UIP ⇒ inner UIP，并排除非平凡 inner loop；原生 `S¹.loop ≠ refl` 与 native identity-R 消融通过。run exit 0、stderr 0、7 行冻结、exact replay；22 later packages/84 claims。判词为已发表可选扩展边界，下一步 natural consumer/crisp/base-change；Goal 保持 active。\n")

    essay = projection_edit.load(ROOT, R.ESSAY)
    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier,
        "# HoTT 研究前沿（S147 认知分片顺序纠正，研究候选不变）",
        "# HoTT 研究前沿（S148 2LTT replacement→UIP 数学核完成）")
    frontier = replace_once(frontier,
        "C-188–C-226 已在 main 形成分层链：R2 synthetic dual-kernel 保持；C-219–C-222 重放显式 EPF_bool/SCT 前提下 internal `~decidable`；C-223–C-226 重放 exact groupoid-syntax slice。Post primary 与 Oracle 34 文件源树已入 main。三条旧薄切完成后，当前优先 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001`：机器化 external pointwise replacement→context-stable internal R→inner UIP，并做 univalence/crisp 消融。ambient R2、完整 R4、CE-MAP、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。S147 只修复 LIT-HOTT 逻辑分片在 task hydration 中的 canonical 顺序，不改变这些研究判词。",
        "C-188–C-232 已在 main 形成分层链：R2 conditional internal no-decider、exact groupoid-syntax slice，以及 C-227–C-232 的 context-uniform replacement→inner UIP 条件边界。S¹ 非平凡环路与 identity-R 消融均已机器化；这是已发表可选扩展 no-go，不是 basic HoTT/2LTT 矛盾。当前优先 `NATURAL-CONSUMER-002` 与 crisp/base-change 同任务消融；ambient R2、完整 R4、CE-MAP、现实 bridge 与全面覆盖均 OPEN。")
    frontier = replace_once(frontier,
        "| 当前高判别候选 | 2LTT internal fibrant replacement→inner UIP | `SOURCE_REPORTED_NOT_REPLAYED / ACTIVE` | 固定最小 R rules；机器证明 UIP；用 univalence/Bool 或 circle 反控制；消融 context stability/crisp/outer；失败则降级并回 CE-MAP |",
        "| 当前高判别候选 | 2LTT replacement 的 natural consumer 与 crisp/base-change 支付 | `MATH_CORE_MACHINE_PROVED / CONSUMER_OPEN` | 冻结真实调用链与同一任务；识别 p-dependent R 使用；对 crisp/outer-only 接口做消融；无 consumer 则封为 known boundary 并回 CE-MAP |")

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n106. 两层理论不能用一个宿主 `Type` 的浅嵌入冒充：若 inner Path 可借宿主 J 直接消去到任意 outer 命题，R 的关键作用会被绕过。以 Inner code/El 和只能返回 code 的 Jᵢ 分层，才能让 p-dependent outer witness 必须经 R 内化。\n"
        "\n107. 2LTT fibrant replacement→UIP 的最小依赖比论文规则清单更窄：outer UIP、inner Id/J/Π、FORM/INTRO/dependent-ELIM 足够；COMP-R 不需要。消融不能只删名为 R 的接口，必须检查 strict bridge 与 R 对 p-dependent context 的统一可用性。\n"
        "\n108. run source manifest 中的 current 文档一经捕获就成为该 run 的不可变输入；后续研究更新应新增 logical shard 或新 run，不能原位改写后降低 source-drift 校验。本轮恢复第 004 片精确 hash，并以第 005 片承载新结果。\n"
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS148：`MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` / C-227–C-232 已完成 source/run/index/freeze/exact replay。最小两层接口证明 context-uniform R + outer UIP ⇒ inner UIP；原生 S¹ 与 identity-R controls 通过；COMP-R 未使用。判词=已发表可选扩展边界，非 basic HoTT/2LTT BUG。下一 active=`NATURAL-CONSUMER-002` + crisp/base-change 同任务消融；Goal 保持 active。\n\n")

    state["revision"] = 148
    state["latest_session"] = SESSION_ID
    state["active"] = ["I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912", GOAL_ID, CONSUMER_ID]
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_2LTT_FR_UIP_MACHINE_PROOF"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Freeze and inspect natural 2LTT/HTS/Reedy/crisp consumers of external-to-internal fibrant replacement; identify actual p-dependent context-uniform R use and run crisp/base-change same-task ablation before any paradox upgrade."
    state["projection"]["status"] = STATUS
    for key, generation in (("I-DIRECTION-PORTFOLIO-20260912", "20260915-direction-130"), ("I-OUTCOME-PANORAMA-20260912", "20260915-outcome-130")):
        state["records"][key]["projection_generation"] = generation
        state["records"][key]["semantic_status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = "Current main-only portfolio through C-232: the 2LTT replacement-to-UIP core is machine-proved as a known optional-extension boundary; natural consumer and same-task reality remain open."
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = "Integrated outcomes through C-232 plus runtime 3.6.1 ordering; no ambient no-decider, full R4 incompleteness, natural-use mismatch or qualified reality-relative paradox."

    formal_sources = [
        SOURCE, CLAIM_DOC, PACKAGE_README, PAPER, LIT_005, AUDIT,
        *run_assets(), MATRIX, REGISTRY,
        "scripts/audit/capture_agda_proof_run.py", "scripts/audit/verify_formal_proof_run.py",
    ]
    state["records"][FORMAL_ID] = {
        "claim_ids": CLAIMS,
        "classification": "TWO_LEVEL_CONTEXT_UNIFORM_REPLACEMENT_IMPLIES_INNER_UIP",
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": formal_sources,
        "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT",
        "mathematical_status": "KNOWN_INCOMPATIBLE_OPTIONAL_EXTENSION_BOUNDARY",
        "path": SOURCE,
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "research_parent": GOAL_ID,
        "related_records": [PROOF_GATE_ID, PLAN_ID, LIT_ID, SYNTAX_ID, CAND_ID, CONSUMER_ID, SESSION_ID],
        "resolution": {"evidence": [f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", MATRIX, AUDIT], "reason": "Boundary-preserving inner-code/outer-Type formalisation proves formulas (2.14)/(2.13), based/full inner UIP and nontrivial-loop exclusion; native S1 and identity-R controls pass; exact replay matches."},
        "scope": "C-227-C-232 only. Published Theorem 2.20 core; no native 2LTT kernel/model instantiation, basic-theory inconsistency, novelty, natural consumer or reality bridge.",
        "source_hashes": hashes(formal_sources),
        "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }
    cand = state["records"][CAND_ID]
    cand["lifecycle_status"] = "CLOSED"
    cand["evidence_status"] = "MACHINE_PROVED_LOCAL_UNCOMMITTED / KNOWN_INCOMPATIBLE_EXTENSION_BOUNDARY"
    cand["status"] = "closed"
    cand["full_sources"] = [LIT_005, SOURCE, CLAIM_DOC, AUDIT, f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", GOAL]
    cand["source_hashes"] = hashes(cand["full_sources"])
    cand["resolution"] = {"evidence": [SOURCE, f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", AUDIT], "reason": "The conditional incompatibility and controls are machine-proved; the candidate does not meet the natural-consumer or reality-bridge gates."}
    cand["related_records"] = [SYNTAX_ID, FORMAL_ID, LIT_ID, CONSUMER_ID, SESSION_ID]
    cand["scope"] = "Machine-proved published optional-extension boundary: context-uniform R plus outer UIP forces inner UIP. Natural consumer, same-task reality, basic-theory defect and novelty are not established."
    cand["revalidation"] = f"{SESSION_ID}: replaced source-reported status with the exact C-227-C-232 source/run/index/freeze/replay evidence and closed only the candidate evaluation; the natural-consumer successor remains open."

    consumer_sources = [LIT_005, AUDIT, CLAIM_DOC, PAPER, GOAL]
    state["records"][CONSUMER_ID] = {
        "classification": "NATURAL_CONSUMER_AND_CRISP_BASE_CHANGE_ABLATION_FOR_2LTT_REPLACEMENT",
        "depends_on": [],
        "evidence_status": "RESEARCH_TASK_PRE_REGISTERED / NOT_RUN",
        "full_sources": consumer_sources,
        "kind": "candidate_search_task",
        "lifecycle_status": "ACTIVE_WORK",
        "path": LIT_005,
        "research_parent": GOAL_ID,
        "related_records": [FORMAL_ID, CAND_ID, LIT_ID, SYNTAX_ID, SESSION_ID],
        "scope": "Find and freeze real 2LTT/HTS/Reedy/modal/crisp consumers that require p-dependent context-uniform replacement; compare the same task under crisp/base-change restrictions and preserve naturality/completion semantics.",
        "source_hashes": hashes(consumer_sources),
        "status": "active",
    }

    lit_sources = [LIT_INDEX, *[str(p.relative_to(ROOT)) for p in sorted((ROOT / LIT_ROOT).glob("*.md"))], AUDIT, CLAIM_DOC, f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json"]
    lit = state["records"][LIT_ID]
    lit["full_sources"] = list(dict.fromkeys([*lit_sources, *lit.get("full_sources", [])]))
    lit["source_hashes"] = hashes(lit["full_sources"])
    lit["scope"] = "First HoTT-computability slice plus machine-proved 2LTT replacement-to-UIP core. Natural consumer/crisp-base-change, Brouwer Trees, Extension Types, Dominances, strictified syntax and citation coverage remain open."
    lit["revalidation"] = f"{SESSION_ID}: added the immutable C-227-C-232 proof/run audit and new shard 005 while preserving captured shard 004 byte-for-byte; literature and consumer coverage remain open."
    for identity in (FORMAL_ID, CONSUMER_ID, SESSION_ID): add_once(lit.setdefault("related_records", []), identity)

    syntax = state["records"][SYNTAX_ID]
    syntax["evidence_status"] = "FIRST_EXACT_MACHINE_REPLAYED_SLICE / 2LTT_REPLACEMENT_UIP_BOUNDARY_MACHINE_PROVED / FULL_CALCULUS_OPEN"
    syntax["scope"] = "Exact groupoid syntax slice and the 2LTT replacement-to-UIP optional-extension boundary are machine-replayed/proved; full Nat/Path/univalence/HIT derivation syntax, proof enumeration, arithmetic and R4 remain open."
    for identity in (FORMAL_ID, CONSUMER_ID, SESSION_ID): add_once(syntax.setdefault("related_records", []), identity)

    gate = state["records"][PROOF_GATE_ID]
    for path in [SOURCE, f"{RUN}/RUN.json", f"{RUN}/source-manifest.json", f"{RUN}/index-row-manifest.json", MATRIX, REGISTRY]:
        add_once(gate.setdefault("full_sources", []), path)
    for identity in (FORMAL_ID, SESSION_ID): add_once(gate.setdefault("related_records", []), identity)
    gate["source_hashes"] = hashes(gate["full_sources"])
    gate["scope"] = "Require exact statement, proof source, kernel run and claim/proof index before delivery. Current registry has 17 frozen packages, one scoped external replay and 22 later packages / 84 claims; new assets remain local uncommitted."
    gate["revalidation"] = f"{SESSION_ID}: C-227-C-232 are indexed, row-frozen and exact-replayed; registry counts 22 later packages/84 claims. Global Git closure remains blocked by intentionally uncommitted R1+ assets."

    for key in (PLAN_ID, COVERAGE_ID, GOAL_ID):
        record = state["records"][key]
        for identity in (FORMAL_ID, CONSUMER_ID, SESSION_ID): add_once(record.setdefault("related_records", []), identity)
    plan_record = state["records"][PLAN_ID]
    for path in (PROGRAM_005, PROGRAM_006, PROGRAM_TEST, LIT_INDEX, LIT_005, AUDIT): add_once(plan_record.setdefault("full_sources", []), path)
    plan_record["source_hashes"] = hashes(plan_record["full_sources"])
    plan_record["revalidation"] = f"{SESSION_ID}: the 2LTT replacement math core is machine-proved; next bounded successor is the natural-consumer/crisp-base-change task, while CE-MAP and other return paths remain open."
    coverage = state["records"][COVERAGE_ID]
    for path in (LIT_INDEX, LIT_005, AUDIT): add_once(coverage.setdefault("full_sources", []), path)
    coverage["source_hashes"] = hashes(coverage["full_sources"])
    coverage["revalidation"] = f"{SESSION_ID}: one source-reported 2LTT theorem is now machine-reconstructed; comprehensive literature and consumer coverage remain review_required."
    goal_record = state["records"][GOAL_ID]
    for path in (GOAL, FEATURE, LIT_INDEX): add_once(goal_record.setdefault("full_sources", []), path)
    goal_record["source_hashes"] = hashes(goal_record["full_sources"])
    goal_record["revalidation"] = f"{SESSION_ID}: C-227-C-232 close the 2LTT replacement conditional math core, but the published boundary lacks a natural consumer and same-task reality bridge; Goal remains active and moves to {CONSUMER_ID}."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：2LTT internal context-uniform fibrant replacement→inner UIP 的最小机器构造、控制与悖论资格判别。
- 证明：`{PROOF_ID}` / C-227–C-232；boundary-preserving Inner code/outer Type；COMP-R 未假设。
- 控制：native Cubical `S¹.loop ≠ refl`；删去 strict 两层桥的 `NativeR X = X` dependent-elim 正控制。
- 运行：`{RUN_ID}`；exit 0、stderr 0、7 rows frozen、exact replay。
- 判词：`KNOWN_INCOMPATIBLE_EXTENSION_BOUNDARY`；论文已知，不是 basic HoTT/2LTT BUG 或原创性主张。
- 下一步：`{CONSUMER_ID}`，冻结真实 external→internal replacement consumer，并做 crisp/base-change same-task ablation。
- Goal：保持 active；ambient R2、完整 R4/Gödel、CE-MAP、现实桥梁与全面覆盖仍开放。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "formal_runs": [{"proof_id": PROOF_ID, "run_id": RUN_ID, "claims": CLAIMS, "status": "PASS_WITH_SCOPE / EXACT_REPLAY"}],
        "regressions": {"programmatic_plan": "5/5 PASS", "proof_evidence_global": "EXPECTED_BLOCKED_UNTRACKED_R1_PLUS_ASSETS", "single_run": "PASS_WITH_SCOPE"},
        "completeness_audit": {
            "cell": "TC-11 external-pointwise-to-internal-context-uniform × OP-02/03 × inner-path consumer",
            "generator": "source-guided then typed formalisation and rule ablation",
            "oracles": ["Cubical Agda kernel", "F-011 exact replay", "primary 2LTT source"],
            "controls": ["native S1 nontrivial loop", "native identity replacement without strict bridge", "COMP-R omitted"],
            "unexpected_result": "COMP-R is unnecessary; nondependent recR derived from dependent ELIM-R suffices",
            "remainder": ["natural consumer", "crisp/base-change same-task ablation", "reality bridge", "full R4"],
        },
        "next": [CONSUMER_ID, "CE-MAP-001", "CRISP-REPLACEMENT-ABLATION-001", "ORACLE-MODALITY-REPLAY-001", "R2-AMBIENT-UNDEC-001", "G-HOTT-SYNTAX-EXPAND-001"],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, AUDIT, SOURCE, f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json"],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, GOAL_ID, PLAN_ID, LIT_ID, SYNTAX_ID, CAND_ID, FORMAL_ID, CONSUMER_ID],
        "scope": "Machine-close the published 2LTT replacement-to-UIP core and route the still-open natural-consumer/reality qualification.",
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

    changed = [
        GOAL, FEATURE, PROGRAM_005, PROGRAM_006, PROGRAM_TEST, LIT_INDEX, LIT_005,
        MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README,
        f"{RUN}/RUN.json", f"{RUN}/index-row-manifest.json", *texts.keys(),
    ]
    for record in state["records"].values():
        source_hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(source_hashes, dict):
            continue
        rebound = []
        for path in changed:
            if path not in source_hashes or path == R.STATE:
                continue
            data = texts[path].encode("utf-8") if path in texts else (ROOT / path).read_bytes()
            current = R.sha(data)
            if source_hashes[path] != current:
                source_hashes[path] = current
                rebound.append(path)
        if rebound and record is not state["records"][FORMAL_ID]:
            note = f"{SESSION_ID}: revalidated current owner/proof-index evolution at {', '.join(rebound)}; prior mathematical scopes remain unchanged."
            previous = record.get("revalidation")
            record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note

    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value}
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 148, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
