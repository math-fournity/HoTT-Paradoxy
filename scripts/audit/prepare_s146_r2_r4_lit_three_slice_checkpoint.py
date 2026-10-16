#!/usr/bin/env python3
"""Prepare revision 146: R2/R4/literature three-slice completion and next candidate."""
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
SESSION_ID = "S-RES-20260914-146-R2-R4-LIT-THREE-SLICE"
PREV = "S-GOV-20260914-145-R2-REGRESSION-SEMANTICS"
STATUS = "CORE_GENERATION_4_R2_CONDITIONAL_INTERNAL_UNDEC_G_HOTT_SYNTAX_SLICE_COMPLETE_2LTT_FR_UIP_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_DENOM_ID = "A-LIT-DENOMINATOR-001"
LIT_CLASSICS_ID = "A-LIT-CLASSICS-001"
PROOF_GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
POST_ID = "A-POST-1944-PRIMARY-REVIEW-001"
CT_ID = "A-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001"
ORACLE_ID = "A-ORACLE-MODALITIES-SOURCE-QUALIFICATION-001"
GROUP_ID = "A-CUBICAL-GROUPOID-SYNTAX-REPLAY-001"
LIT_HOTT_ID = "A-LIT-HOTT-COMPUTABILITY-001"
SYNTAX_ID = "A-G-HOTT-SYNTAX-001"
CAND_ID = "A-CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001"

GOAL = "goal.md"
FEATURE = "feature-list.md"
PROGRAM_INDEX = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
PROGRAM_TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
LIT_DENOM_INDEX = ".codex/research/hott/LIT-DENOMINATOR-001.md"
LIT_DENOM_003 = ".codex/research/hott/LIT-DENOMINATOR-001/003 - 预注册核心 Seed 与谱系覆盖槽.md"
LIT_CLASSICS_INDEX = ".codex/research/hott/LIT-CLASSICS-001.md"
LIT_CLASSICS_ROOT = ".codex/research/hott/LIT-CLASSICS-001"
LIT_HOTT_INDEX = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md"
LIT_HOTT_ROOT = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001"

MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
HOTT_README = "HoTT/README.md"
README_SHARD = "README/001 - 当前入口与关键文件.md"
VERIFIER = "scripts/audit/verify_formal_proof_run.py"

CT_PROOF = "MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001"
CT_CLAIMS = ["C-219", "C-220", "C-221", "C-222"]
CT_RUN_ID = "20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01"
CT_RUN = f"HoTT/verification/runs/{CT_RUN_ID}"
CT_FORMAL = "HoTT/formal/external-coq-parametric-ct"
CT_AUDIT = "audit/R2-ParametricCT内部不可判定性重放与前提边界-20260914.md"

GROUP_PROOF = "MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001"
GROUP_CLAIMS = ["C-223", "C-224", "C-225", "C-226"]
GROUP_RUN_ID = "20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01"
GROUP_RUN = f"HoTT/verification/runs/{GROUP_RUN_ID}"
GROUP_FORMAL = "HoTT/formal/external-cubical-groupoid-syntax"
GROUP_AUDIT = "audit/G-HOTT-SYNTAX首个精确机器切片与2LTT边界-20260914.md"

POST_AUDIT = "audit/Post-1944原文来源与首轮审读-20260914.md"
POST_IMPORT = "audit/literature/LIT-CLASSICS-001/post-1944-primary/IMPORT.json"
POST_PAGE_MAP = "audit/literature/LIT-CLASSICS-001/post-1944-primary/PAGE_MAP.json"
POST_TEXT = "audit/literature/LIT-CLASSICS-001/post-1944-primary/full.txt"
POST_MANAGER = "scripts/audit/import_post_1944_primary.py"
ORACLE_IMPORT = "audit/literature/LIT-HOTT-COMPUTABILITY-001/oracle-modalities/IMPORT.json"
ORACLE_MANIFEST = "audit/literature/LIT-HOTT-COMPUTABILITY-001/oracle-modalities/SOURCE_TREE_MANIFEST.json"
ORACLE_MANAGER = "scripts/audit/import_oracle_modalities_source.py"
LIT_HOTT_AUDIT = "audit/LIT-HOTT-COMPUTABILITY首轮来源资格化与接口映射-20260914.md"
TWO_LTT = "audit/literature/LIT-CLASSICS-001/mineru/Annenkov-Capriotti-Kraus-Sattler-2017-2LTT/full.md"
PREPARE = "scripts/audit/prepare_s146_r2_r4_lit_three_slice_checkpoint.py"

SPEC = importlib.util.spec_from_file_location("runtime_s146", RUNTIME_PATH)
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


def record_hashes(paths: list[str]) -> dict[str, str]:
    return {path: R.sha((ROOT / path).read_bytes()) for path in paths}


def run_assets(run: str) -> list[str]:
    return [
        f"{run}/RUN.json", f"{run}/source-manifest.json",
        f"{run}/index-row-manifest.json", f"{run}/stdout.txt",
        f"{run}/stderr.txt", f"{run}/environment.txt",
    ]


def assert_run(run: str, proof: str, claims: list[str]) -> None:
    receipt = json.loads((ROOT / f"{run}/RUN.json").read_text(encoding="utf-8"))
    rows = json.loads((ROOT / f"{run}/index-row-manifest.json").read_text(encoding="utf-8"))
    if (
        receipt.get("proof_id") != proof
        or receipt.get("claim_ids") != claims
        or receipt.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or receipt.get("exit_code") != 0
        or receipt.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or rows.get("claim_ids") != claims
        or len(rows.get("rows", [])) != len(claims) + 1
    ):
        raise SystemExit(f"PROOF_RUN_NOT_FINAL:{proof}")


def command_pass(argv: list[str], required: str | None = None) -> None:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    if result.returncode != 0 or (required is not None and required not in output):
        raise SystemExit(f"PRECHECK_FAILED:{' '.join(argv)}\n{output}")


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "以机器重放的 groupoid syntax 取代不完整的 paper rule list，Theory Schema 首次得到 exact syntax slice；完整 R4 仍开放。",
        "KC-000005": "三条薄切完成后产生 fibrant-replacement→UIP 新候选；先固定现象与消融，不要求本轮完成最终归因。",
        "KC-000007": "LLM source-guided pattern matching从 2LTT 的外部逐例 replacement/内部统一 naturality 反差提出新候选，并交给机器义务。",
        "KC-000010": "C-219–C-226 都未被包装成最终悖论；现实同任务、natural consumer 与 HoTT 必要性继续作为完成门。",
        "KC-000011": "Post adaptive oracle 与 Oracle query continuation 明确属于时序；没有用它们替代运动/时空的时间轴。",
        "KC-000012": "EPF/SCT 作为 ASK 前提显式保留；Oracle ECT/CT 的 four postulate groups 被逐项定位。",
        "KC-000013": "synthetic implication、conditional internal negation、ambient unconditional negation被分层，防止理论能力越级。",
        "KC-000015": "fibrant replacement 候选把逐例外部操作提升为 context-stable 内部 type former，正是可检查的抽象变化。",
        "KC-000021": "C-219–C-226 两个 proof package均有 source/run/index/frozen/exact replay；Post/Oracle 只按各自证据层级登记。",
        "KC-000022": "fibrant replacement 候选同时有 A 读法（统一内化新增相干困难）与 B 读法（external capability→internal operation）。",
        "KC-000024": "R2 已到显式前提下的 internal no-decider；仍不等于 exact HoTT 不完备或现实相对悖论。",
        "KC-000027": "HoTT-specific modality/syntax 已真实进入源码与 kernel；一般计算边界与 HoTT 特有机制仍分开。",
        "KC-000028": "groupoid syntax 只闭合 syntax setness，不闭合 proof predicate/self-reflection；自馈回环仍待 R3/R4。",
        "KC-000029": "2LTT replacement 的经济收益是把外部逐例构造压成统一内部接口；代价候选是 base-change/naturality 与 UIP。",
        "KC-000031": "2LTT 明确展示一个看似自然的最小 replacement interface不能在有趣同伦模型中按强规则内化，形成新的覆盖边界候选。",
        "KC-000035": "groupoid syntax 与 2LTT 说明表达元理论需要选择层级和相干；尚未证明 HoTT 完整表达用户悖论理论。",
        "KC-000036": "exact syntax 首片与 conditional internal no-decider 已就位，但 proof enumeration、arithmetic representability、fixed point 与 independent sentence仍开放。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮完成三条 breadth slice，Goal 保持 active。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{LIT_HOTT_AUDIT}`；{kid} | "
            "ambient R2、完整 R4、CE-MAP、natural consumer、现实桥梁与最终悖论仍开放。 |"
        )
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — 三条薄切完成，下一高判别候选转 2LTT fibrant replacement→UIP。",
        "- panorama_change: YES_IN_PLACE — 新增 Parametric CT、groupoid-syntax、Post/Oracle/2LTT 与候选边界。",
        "- essay_change: NO。",
        "- update_decision: source-guided unexpected result 新增 TC-11×OP-02/03×context-stability cell，并保留 CE-MAP/Oracle/R2/R4/现实返回口。",
        "- cross_conflicts: 2LTT suggested syntax 非完整 raw calculus；Oracle CT/ECT 含 postulates；internal no-decider 含显式前提；groupoid slice 非完整 HoTT。",
        "- unresolved: fibrant replacement theorem 本项目机器化、univalence control、HoTT essentiality、natural consumer、same-task reality、完整 coverage。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        GOAL, FEATURE, PROGRAM_INDEX, PROGRAM_005, PROGRAM_006, PROGRAM_TEST,
        LIT_DENOM_INDEX, LIT_DENOM_003, LIT_CLASSICS_INDEX, LIT_HOTT_INDEX,
        MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, README_SHARD,
        VERIFIER, CT_AUDIT, GROUP_AUDIT, POST_AUDIT, POST_IMPORT, POST_PAGE_MAP,
        POST_TEXT, POST_MANAGER, ORACLE_IMPORT, ORACLE_MANIFEST, ORACLE_MANAGER,
        LIT_HOTT_AUDIT, TWO_LTT, PREPARE,
        f"{CT_FORMAL}/README.md", f"{CT_FORMAL}/CLAIM-R2-INTERNAL-UNDEC.md",
        f"{CT_FORMAL}/CheckInternalUndec.v", f"{CT_FORMAL}/REPLAY_SOURCE.json",
        f"{GROUP_FORMAL}/README.md", f"{GROUP_FORMAL}/CLAIM-G-HOTT-SYNTAX.md",
        f"{GROUP_FORMAL}/CheckGroupoidSyntax.agda", f"{GROUP_FORMAL}/REPLAY_SOURCE.json",
        *run_assets(CT_RUN), *run_assets(GROUP_RUN),
    ]
    required.extend(str(path.relative_to(ROOT)) for path in sorted((ROOT / LIT_HOTT_ROOT).glob("*.md")))
    required.extend(str(path.relative_to(ROOT)) for path in sorted((ROOT / LIT_CLASSICS_ROOT).glob("*.md")))
    if any(not (ROOT / path).is_file() for path in required):
        missing = [path for path in required if not (ROOT / path).is_file()]
        raise SystemExit(f"S146_EVIDENCE_MISSING:{missing}")

    assert_run(CT_RUN, CT_PROOF, CT_CLAIMS)
    assert_run(GROUP_RUN, GROUP_PROOF, GROUP_CLAIMS)
    registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
    if registry.get("later_machine_proved_claim_count") != 78 or len(registry.get("later_packages", [])) != 21:
        raise SystemExit("S146_REGISTRY_COUNT_INVALID")
    command_pass(["python3", "-B", "scripts/audit/import_coq_parametric_ct.py"], '"status": "VALID"')
    command_pass(["python3", "-B", "scripts/audit/import_cubical_groupoid_syntax.py"], '"status": "VALID"')
    command_pass(["python3", "-B", ORACLE_MANAGER], '"status": "VALID"')
    command_pass([
        "/Users/aurolafly/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3",
        "-B", POST_MANAGER,
    ], '"status": "VALID"')
    command_pass(["python3", "-B", VERIFIER, "--run-dir", CT_RUN], '"status": "PASS_WITH_SCOPE"')
    command_pass(["python3", "-B", VERIFIER, "--run-dir", GROUP_RUN], '"status": "PASS_WITH_SCOPE"')
    command_pass(["python3", "-B", PROGRAM_TEST], "Ran 5 tests")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 145 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_145_S145")
    for identity in (POST_ID, CT_ID, ORACLE_ID, GROUP_ID, LIT_HOTT_ID, SYNTAX_ID, CAND_ID, SESSION_ID):
        if identity in state["records"]:
            raise SystemExit(f"S146_RECORD_ALREADY_EXISTS:{identity}")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    shard2 = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][shard2] = replace_line(
        direction["shards"][shard2], "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 与根 `goal.md` 为唯一工作面推进计算合法性／不可停机／Gödel 到 HoTT 现实相对悖论；R2 已有 synthetic reduction 与显式 EPF/SCT 前提下的 internal no-decider，G-HOTT-SYNTAX 有 exact groupoid slice；下一优先 2LTT fibrant replacement→UIP | 用户当前 App Goal；`goal.md`；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY`, `THEORY_ECONOMY` | `OUT-TOP-R2-PARAMETRIC-CT-INTERNAL-UNDEC`、`OUT-TOP-G-HOTT-GROUPOID-SYNTAX`、`OUT-TOP-LIT-HOTT-COMPUTABILITY`、`OUT-TOP-2LTT-FR-UIP-CANDIDATE` | 当前机器化 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001` 并做 univalence/context-stability 消融；并行保持 CE-MAP、Oracle replay、ambient R2、完整 R4、natural consumer 与现实 bridge | `goal.md`；C-219–C-226；`audit/LIT-HOTT-COMPUTABILITY首轮来源资格化与接口映射-20260914.md` |",
    )
    shard3 = "方向追踪/003 - LocalGPT 与 WebGPT 方向.md"
    direction["shards"][shard3] = replace_line(
        direction["shards"][shard3], "| `DIR-L-THEORY-SCHEMA-VARIANTS`",
        "| `DIR-L-THEORY-SCHEMA-VARIANTS` | bare/axiomatic、cubical、guarded/clocked、directed、linear/quantitative/effectful 与 2LTT/groupoid-syntax 变体规则比较 | LocalGPT、WebGPT Theory Schema；当前 LIT-HOTT | `SUPPORTING_DIRECTION` | `THEORY_SCHEMA`, `HOTT_OBJECT`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `OUT-L-TIME-BOUNDARY`、`OUT-TOP-G-HOTT-GROUPOID-SYNTAX`、`OUT-TOP-2LTT-FR-UIP-CANDIDATE` | C-223–C-226 已固定首个 exact syntax slice；下一机器化 2LTT internal replacement→UIP，并区分 basic conservativity、strengthenings 与完整 R4 | `HoTT/THEORY_SCHEMA.md`；`LIT-HOTT-COMPUTABILITY-001.md`；C-223–C-226 |",
    )
    for old, new in (
        ("source_state_revision: 145", "source_state_revision: 146"),
        ("projection_generation: 20260914-direction-127", "projection_generation: 20260914-direction-128"),
        ("semantic_status: CORE_GENERATION_4_R2_SYNTHETIC_DUAL_KERNEL_COMPLETE_INTERNAL_UNDEC_R3_R4_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_SYNTHETIC_DUAL_KERNEL_COMPLETE_INTERNAL_UNDEC_R3_R4_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    proof_shard = "全景视野/003 - 当前机器证明包与原生重放.md"
    for row in (
        "| `OUT-TOP-R2-PARAMETRIC-CT-INTERNAL-UNDEC` | C-219–C-222：固定 Parametric CT Coq 源树，在显式 `EPF_bool + SCT` 前提下重放三个 internal `~decidable` theorem，assumptions closed | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | `MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONDITIONAL_INTERNAL_NOT_DECIDABLE` | Coq 8.13.2，20 文件 target closure，三个 assumptions closed，exact replay | 不证明 EPF/SCT 在 ambient HoTT 中成立；不使用 HoTT 特有结构 | C-219–C-222；`audit/R2-ParametricCT内部不可判定性重放与前提边界-20260914.md` |\n",
        "| `OUT-TOP-G-HOTT-GROUPOID-SYNTAX` | C-223–C-226：CSL 2026 groupoid syntax 的 20 模块两阶段 Cubical Agda replay；`Con/Sub/Ty/Tm`、Π/U/El/coherence、`isSetTy` 与 set-syntax 四类同构 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-L-THEORY-SCHEMA-VARIANTS`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | `MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / FIRST_EXACT_G_HOTT_SYNTAX_SLICE` | Agda 2.8.0/Cubical v0.9，91 文件源树，20 TT 模块，project probe，exact replay | 不含 Nat/general Id/object univalence/HIT/proof enumeration/arithmetic；不证明 R4 | C-223–C-226；`audit/G-HOTT-SYNTAX首个精确机器切片与2LTT边界-20260914.md` |\n",
    ):
        projection_edit.append_to_shard(panorama, proof_shard, row)
    distance_shard = "全景视野/004 - 距离综合与消费者审计.md"
    for row in (
        "| `OUT-TOP-LIT-HOTT-COMPUTABILITY` | Post primary、Parametric CT、Oracle Modalities、2LTT 与 groupoid-syntax 的首轮文献—机器接口；Oracle 34 文件 MIT 源树与 four postulate groups 固定 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-L-THEORY-SCHEMA-VARIANTS` | 当前 LIT-HOTT 工作包 | `VERIFIED_WITH_SCOPE / MIXED_MACHINE_REPLAY_AND_SOURCE_QUALIFICATION` | 三条 breadth slice 都有真实 evidence；modality/syntax/时序前提可进入 TaskSpec | 不证明全面文献覆盖、Oracle theorem replay 或最终悖论 | `.codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md`；`audit/LIT-HOTT-COMPUTABILITY首轮来源资格化与接口映射-20260914.md` |\n",
        "| `OUT-TOP-2LTT-FR-UIP-CANDIDATE` | 2LTT §2.7 source-reported：把逐对象外部 fibrant replacement 提升为 context-stable internal R type former 会迫使 inner UIP；外部 replacement 通常不保 base change | `DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-THEORY-SCHEMA-VARIANTS` | 2LTT primary + 当前综合 | `COUNTEREXAMPLE_CANDIDATE / SOURCE_REPORTED_NOT_REPLAYED` | 有自然理论动机、精确规则形状、明确 HoTT 高阶后果和 context-stability/crisp 消融 | 尚无本项目机器证明、univalence control、natural consumer 与现实同任务桥梁；可能降级为人为不相容扩展 | `LIT-HOTT-COMPUTABILITY-001/004 - 2LTT、groupoid-syntax 与下一候选.md`；`audit/G-HOTT-SYNTAX首个精确机器切片与2LTT边界-20260914.md` |\n",
    ):
        projection_edit.append_to_shard(panorama, distance_shard, row)
    for old, new in (
        ("source_state_revision: 145", "source_state_revision: 146"),
        ("projection_generation: 20260914-outcome-127", "projection_generation: 20260914-outcome-128"),
        ("semantic_status: CORE_GENERATION_4_R2_SYNTHETIC_DUAL_KERNEL_COMPLETE_INTERNAL_UNDEC_R3_R4_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_SYNTHETIC_DUAL_KERNEL_COMPLETE_INTERNAL_UNDEC_R3_R4_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "3. 当前 App Goal",
        "3. 当前 App Goal 为短指针，根 `goal.md` 是唯一完整 objective owner。C-188–C-226 已在 main 形成 R1/R2 与首个 exact syntax slice：R2 synthetic dual-kernel + 显式 EPF/SCT 前提下 internal no-decider；groupoid syntax 20 模块/`isSetTy`/四类同构 exact replay。最终 HoTT witness 未找到。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "6. 当前仍未得到",
        "6. 当前仍未得到 ambient HoTT 无条件 no-decider、R3 independent sentence、完整 R4 calculus/incompleteness、E6、现实桥梁、`NATURAL_USAGE_MISMATCH` 或 HoTT 内部矛盾。17 个冻结 + 21 个 later package 只支持各自范围；新资产仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "8. 文献分母",
        "8. Post primary、Parametric CT、Oracle Modalities、2LTT 与 groupoid-syntax 三向薄切已完成 scoped 增量。当前优先 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001` 最小机器化，并行 CE-MAP、Oracle old-toolchain/modal→ambient、ambient R2、完整 R4、natural consumer/reality。未获授权不 push、不 tag。",
    )
    evidence_shard = "MEMORY/002 - 当前证据上限与恢复入口.md"
    memory["shards"][evidence_shard] = replace_line(
        memory["shards"][evidence_shard], "- 2LTT/QIIT/QIIRT",
        "- 2LTT/QIIT/QIIRT/内部模型资料支持自我元理论分层；C-223–C-226 机器重放了一个 Π/U/El groupoid-syntax exact slice。2LTT internal fibrant replacement→UIP 目前仍是 source-reported candidate，不自动证明 HoTT coverage failure。",
    )
    memory["shards"][evidence_shard] = replace_line(
        memory["shards"][evidence_shard], "- 可计算性主线目前",
        "- 可计算性主线已有 C-188–C-218 的 R1/R2 基础与 synthetic reduction，C-219–C-222 又给显式 `EPF_bool + SCT` 前提下 internal `~decidable`；它不是 ambient HoTT 无条件结论。C-223–C-226 是首个 exact syntax slice。完整 R4、HoTT essentiality、natural consumer、现实桥梁与学术全面覆盖均开放。",
    )
    memory["shards"][evidence_shard] = replace_once(
        memory["shards"][evidence_shard],
        "优先读第 006 片和 `audit/imports/machine-overview-computability-20260914/IMPORT.json`；",
        "优先读第 006 片、`.codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md` 全部 shards 和 `audit/imports/machine-overview-computability-20260914/IMPORT.json`；",
    )
    memory["index_text"] = replace_once(memory["index_text"], "S023–S145 逐会话记录", "S023–S146 逐会话记录")
    projection_edit.append_to_shard(
        memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S146 三向薄切：Post 1944 primary 33 页抽取/首读；`MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001` / C-219–C-222 在显式 EPF_bool/SCT 前提下重放 internal no-decider；`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` / C-223–C-226 两阶段重放 20 个 groupoid-syntax 模块、`isSetTy` 与四类同构；Oracle 34 文件 MIT 源树和 four postulate groups 进入 main。三条均 exact/source-verified，Git local-uncommitted。下一高判别候选=2LTT internal fibrant replacement→UIP；Goal 保持 active。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S144 R2 synthetic dual-kernel 完成）", "# HoTT 研究前沿（S146 R2/R4/LIT 三向薄切完成）")
    frontier = replace_once(
        frontier,
        "R1/R2 C-188–C-218 已在 main 通过 F-011。Coq 同核完成 MM2→显式 target total reduction 与 synthetic-undecidability，Agda 独立完成 MM2→ProgramCode halting equivalence；四模型 correspondence 28 anchors/282 controls PASS。`undecidable` 仍只是 `decidable P→enumerable(complement SBTM_HALT)`，内部无条件 no-decider OPEN。这仍是一般计算性基础。当前第一轮为 `R2-INTERNAL-UNDEC-001`、`G-HOTT-SYNTAX-001`/R3、Post/HoTT computability 文献三向薄切；CE-MAP、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
        "C-188–C-226 已在 main 形成分层链：R2 synthetic dual-kernel 保持；C-219–C-222 重放显式 EPF_bool/SCT 前提下 internal `~decidable`；C-223–C-226 重放 exact groupoid-syntax slice。Post primary 与 Oracle 34 文件源树已入 main。三条旧薄切完成后，当前优先 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001`：机器化 external pointwise replacement→context-stable internal R→inner UIP，并做 univalence/crisp 消融。ambient R2、完整 R4、CE-MAP、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
    )
    marker = "| 槽位 | 当前对象 | 状态 | 下一判别动作 |\n|---|---|---|---|\n"
    frontier = replace_once(
        frontier, marker,
        marker + "| 当前高判别候选 | 2LTT internal fibrant replacement→inner UIP | `SOURCE_REPORTED_NOT_REPLAYED / ACTIVE` | 固定最小 R rules；机器证明 UIP；用 univalence/Bool 或 circle 反控制；消融 context stability/crisp/outer；失败则降级并回 CE-MAP |\n",
    )

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n101. 不可判定性至少分三层：synthetic implication、显式计算原则前提下的对象语言 internal negation、ambient 无条件 negation。`Print Assumptions: Closed` 不会删除 theorem type 左侧的 EPF/SCT；登记强度必须按完整类型而不是定理名。\n"
        "\n102. paper 给规则清单不等于 exact syntax。2LTT 论文主动说明 suggested syntax 非完整 specification；可冻结的第一片来自作者 Cubical Agda groupoid-syntax 源码、完整模块入口和 kernel replay。exact slice 仍不得冒充完整 calculus。\n"
        "\n103. Agda library flags 与依赖源码重检可能有作用域差：`--hidden-argument-puns` 全局命令行会使 Cubical v0.9 旧源码重解析失败，而 library-mode 可在固定依赖接口上重查上层模块。可靠 replay 应保存两阶段边界与 derived manifest 的唯一改动。\n"
        "\n104. source-guided 搜索可产生比继续堆通用 Gödel 基础更接近用户目标的候选：2LTT 中外部逐对象 fibrant replacement 可存在，但若提升为 context-stable internal type former会迫使 inner UIP。下一步必须机器化和消融，判断它是自然理论经济失配还是人为不相容扩展。\n"
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS146：三条旧 breadth slice 均形成真实 evidence。Post primary 33 页抽取/首读；C-219–C-222 在显式 EPF_bool/SCT 前提下 machine-replay internal no-decider；C-223–C-226 machine-replay exact groupoid-syntax slice；Oracle 34 文件 MIT 源树与 four postulate groups 入 main。两个新 F-011 runs exact replay；registry=17 frozen +21 later/78 claims；Git local-uncommitted。下一优先 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001` 最小机器化/消融；Goal 保持 active。\n\n",
    )

    state["revision"] = 146
    state["latest_session"] = SESSION_ID
    state["active"] = ["I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912", GOAL_ID, CAND_ID]
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R2_R4_LIT_THREE_SLICE"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Formalise the minimum 2LTT internal fibrant-replacement rules implying inner UIP, add a native univalence/Bool or circle control, and ablate context stability/crisp/outer restrictions; keep CE-MAP and Oracle/ambient-R2/full-R4 return paths open."
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-128"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = STATUS
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-128"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = STATUS

    post_sources = [POST_AUDIT, POST_IMPORT, POST_PAGE_MAP, POST_TEXT, POST_MANAGER]
    state["records"][POST_ID] = {
        "classification": "POST_1944_PRIMARY_BODY_REVIEWED_AND_TASK_MAPPED", "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / PRIMARY_BODY_REVIEWED / NO_NEW_MATH_CLAIM",
        "full_sources": post_sources, "kind": "literature_primary_review", "lifecycle_status": "CURRENT",
        "path": POST_AUDIT, "related_records": [GOAL_ID, LIT_CLASSICS_ID, LIT_HOTT_ID, COVERAGE_ID, SESSION_ID],
        "scope": "BAMS 50(5) issue identity, pages 284-316 extraction, page boundaries, four-page visual check, full-text first pass and Post enumeration/reduction/oracle/completion mapping; source-reported theorems are not replayed.",
        "source_hashes": record_hashes(post_sources), "status": "complete",
    }

    ct_sources = [
        f"{CT_FORMAL}/README.md", f"{CT_FORMAL}/CLAIM-R2-INTERNAL-UNDEC.md",
        f"{CT_FORMAL}/CheckInternalUndec.v", f"{CT_FORMAL}/REPLAY_SOURCE.json",
        f"{CT_FORMAL}/SOURCE_TREE_MANIFEST.json", f"{CT_FORMAL}/TARGET_CLOSURE.json",
        *run_assets(CT_RUN), MATRIX, REGISTRY, CT_AUDIT,
        "scripts/audit/import_coq_parametric_ct.py",
        "scripts/audit/replay_coq_parametric_ct_internal_undec.py",
        "scripts/audit/capture_coq_parametric_ct_internal_undec_run.py", VERIFIER,
    ]
    state["records"][CT_ID] = {
        "claim_ids": CT_CLAIMS, "classification": "R2_CONDITIONAL_INTERNAL_NOT_DECIDABLE",
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": ct_sources, "kind": "formal_mathematical_result", "lifecycle_status": "CURRENT",
        "mathematical_status": "CONDITIONAL_INTERNAL_NEGATION_UNDER_EXPLICIT_EPF_BOOL_OR_SCT",
        "path": f"{CT_FORMAL}/CheckInternalUndec.v", "proof_id": CT_PROOF, "run_id": CT_RUN_ID,
        "research_parent": GOAL_ID, "related_records": [PROOF_GATE_ID, PLAN_ID, COVERAGE_ID, LIT_HOTT_ID, SESSION_ID],
        "resolution": {"evidence": [f"{CT_RUN}/RUN.json", f"{CT_RUN}/index-row-manifest.json", MATRIX, CT_AUDIT], "reason": "Coq 8.13.2 rebuilt the 20-file target closure, accepted three internal no-decider theorems under EPF_bool + SCT, reported Closed under the global context three times, and exact replay matched."},
        "scope": "C-219-C-222 only. EPF_bool + SCT remains an explicit premise; no ambient HoTT theorem, ProgramCode reduction, HoTT essentiality, natural consumer or reality bridge.",
        "source_hashes": record_hashes(ct_sources), "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }

    oracle_source_root = "audit/literature/LIT-HOTT-COMPUTABILITY-001/oracle-modalities/source-e6e3f75"
    oracle_sources = [
        ORACLE_IMPORT, ORACLE_MANIFEST, ORACLE_MANAGER, LIT_HOTT_AUDIT,
        f"{oracle_source_root}/README.md", f"{oracle_source_root}/LICENSE",
        f"{oracle_source_root}/OracleModality.agda", f"{oracle_source_root}/RelativisedCC.agda",
        f"{oracle_source_root}/ParallelSearch.agda", f"{oracle_source_root}/Continuity.agda",
        f"{oracle_source_root}/Axioms/ComputableChoice.agda",
        f"{oracle_source_root}/Axioms/MarkovInduction.agda",
        f"{oracle_source_root}/Axioms/NegativeResizing.agda",
    ]
    state["records"][ORACLE_ID] = {
        "classification": "ORACLE_MODALITIES_SOURCE_AND_AXIOM_BOUNDARY_QUALIFIED", "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / SOURCE_QUALIFIED_NOT_REPLAYED",
        "full_sources": oracle_sources, "kind": "external_source_qualification", "lifecycle_status": "CURRENT",
        "path": ORACLE_IMPORT, "related_records": [GOAL_ID, CT_ID, LIT_HOTT_ID, COVERAGE_ID, CAND_ID, SESSION_ID],
        "scope": "Full 34-file MIT source at e6e3f75, with Turing-reducibility consumers and negative-resizing/Markov-induction/phi0/computable-choice postulates mapped. Exact Agda 2.6.4.3/Cubical v0.7 replay remains open.",
        "source_hashes": record_hashes(oracle_sources), "status": "complete",
    }

    group_sources = [
        f"{GROUP_FORMAL}/README.md", f"{GROUP_FORMAL}/CLAIM-G-HOTT-SYNTAX.md",
        f"{GROUP_FORMAL}/CheckGroupoidSyntax.agda", f"{GROUP_FORMAL}/cohtt-replay.agda-lib",
        f"{GROUP_FORMAL}/REPLAY_SOURCE.json", f"{GROUP_FORMAL}/SOURCE_TREE_MANIFEST.json",
        f"{GROUP_FORMAL}/TARGET_SOURCE_MANIFEST.json", *run_assets(GROUP_RUN), MATRIX, REGISTRY,
        GROUP_AUDIT, "scripts/audit/import_cubical_groupoid_syntax.py",
        "scripts/audit/replay_cubical_groupoid_syntax.py",
        "scripts/audit/capture_cubical_groupoid_syntax_run.py", VERIFIER,
    ]
    state["records"][GROUP_ID] = {
        "claim_ids": GROUP_CLAIMS, "classification": "G_HOTT_SYNTAX_EXACT_GROUPOID_SLICE_REPLAY",
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE",
        "full_sources": group_sources, "kind": "formal_mathematical_result", "lifecycle_status": "CURRENT",
        "mathematical_status": "EXACT_GROUPoid_SYNTAX_SLICE_SETNESS_AND_SET_SYNTAX_ISOMORPHISMS",
        "path": f"{GROUP_FORMAL}/CheckGroupoidSyntax.agda", "proof_id": GROUP_PROOF, "run_id": GROUP_RUN_ID,
        "research_parent": GOAL_ID, "related_records": [PROOF_GATE_ID, PLAN_ID, LIT_HOTT_ID, SYNTAX_ID, CAND_ID, SESSION_ID],
        "resolution": {"evidence": [f"{GROUP_RUN}/RUN.json", f"{GROUP_RUN}/index-row-manifest.json", MATRIX, GROUP_AUDIT], "reason": "All 20 TT modules were checked from source, rechecked under upstream library flags after deleting cohtt interfaces, and the project isSetTy/four-isomorphism probe passed; exact replay matched."},
        "scope": "C-223-C-226 exact Pi/U/El/base-family groupoid syntax slice only; full HoTT syntax, proof enumeration, arithmetic and R4 incompleteness remain open.",
        "source_hashes": record_hashes(group_sources), "status": "complete",
        "version_closure": {"registry": REGISTRY, "status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "scope_preserved": True},
    }

    lit_hott_sources = [
        LIT_HOTT_INDEX,
        *[str(path.relative_to(ROOT)) for path in sorted((ROOT / LIT_HOTT_ROOT).glob("*.md"))],
        LIT_HOTT_AUDIT, CT_AUDIT, GROUP_AUDIT, POST_AUDIT, ORACLE_IMPORT, ORACLE_MANIFEST,
    ]
    state["records"][LIT_HOTT_ID] = {
        "classification": "HOTT_COMPUTABILITY_MODALITY_SYNTAX_PRIMARY_CORPUS",
        "depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE / MIXED_MACHINE_REPLAY_AND_SOURCE_QUALIFICATION",
        "full_sources": lit_hott_sources, "kind": "literature_primary_corpus_review", "lifecycle_status": "OPEN_ISSUE",
        "path": LIT_HOTT_INDEX, "related_records": [GOAL_ID, PLAN_ID, COVERAGE_ID, LIT_CLASSICS_ID, POST_ID, CT_ID, ORACLE_ID, GROUP_ID, SYNTAX_ID, CAND_ID, SESSION_ID],
        "scope": "First HoTT-computability slice: Parametric CT conditional internal negation, Oracle Modalities source/axiom map, 2LTT boundary, groupoid-syntax exact replay and Post temporal-order mapping. Brouwer Trees, Extension Types, Dominances, strictified syntax and citation coverage remain open.",
        "source_hashes": record_hashes(lit_hott_sources), "status": "active",
    }

    syntax_sources = [LIT_HOTT_INDEX, f"{LIT_HOTT_ROOT}/004 - 2LTT、groupoid-syntax 与下一候选.md", GROUP_AUDIT, TWO_LTT, f"{GROUP_RUN}/RUN.json", f"{GROUP_RUN}/index-row-manifest.json"]
    state["records"][SYNTAX_ID] = {
        "classification": "G_HOTT_SYNTAX_PROGRESSIVE_EXACT_CALCULUS", "depends_on": [],
        "evidence_status": "FIRST_EXACT_MACHINE_REPLAYED_SLICE / FULL_CALCULUS_OPEN",
        "full_sources": syntax_sources, "kind": "research_frontier", "lifecycle_status": "CURRENT",
        "path": f"{GROUP_FORMAL}/CLAIM-G-HOTT-SYNTAX.md", "related_records": [GOAL_ID, GROUP_ID, LIT_HOTT_ID, CAND_ID, SESSION_ID],
        "scope": "Exact groupoid syntax slice is replayed; Nat, general identity/Path, object univalence/HIT, raw derivation/checker, proof enumeration, arithmetic representation and R4 remain open.",
        "source_hashes": record_hashes(syntax_sources), "status": "active",
    }

    cand_sources = [f"{LIT_HOTT_ROOT}/004 - 2LTT、groupoid-syntax 与下一候选.md", GROUP_AUDIT, TWO_LTT, GOAL]
    state["records"][CAND_ID] = {
        "classification": "TWO_LEVEL_INTERNAL_FIBRANT_REPLACEMENT_UIP_CANDIDATE", "depends_on": [],
        "evidence_status": "COUNTEREXAMPLE_CANDIDATE / SOURCE_REPORTED_NOT_REPLAYED",
        "full_sources": cand_sources, "kind": "candidate", "lifecycle_status": "ACTIVE_WORK",
        "path": f"{LIT_HOTT_ROOT}/004 - 2LTT、groupoid-syntax 与下一候选.md", "research_parent": GOAL_ID,
        "related_records": [SYNTAX_ID, GROUP_ID, LIT_HOTT_ID, ORACLE_ID, SESSION_ID],
        "scope": "Test whether pointwise external fibrant replacement, when promoted to a context-stable internal type former, forces inner UIP and conflicts with native homotopy controls. Must distinguish natural theory economy from a researcher-invented incompatible extension.",
        "source_hashes": record_hashes(cand_sources), "status": "active",
    }

    goal_record = state["records"][GOAL_ID]
    add_once(goal_record["full_sources"], LIT_HOTT_INDEX)
    for identity in (POST_ID, CT_ID, ORACLE_ID, GROUP_ID, LIT_HOTT_ID, SYNTAX_ID, CAND_ID, SESSION_ID):
        add_once(goal_record.setdefault("related_records", []), identity)
    goal_record["source_hashes"] = record_hashes(goal_record["full_sources"])
    goal_record["revalidation"] = f"{SESSION_ID}: three breadth-first slices have real evidence through C-226; Goal remains active. The next discriminating candidate is internal fibrant replacement -> UIP, while ambient R2, full R4, CE-MAP, natural consumer, reality bridge and comprehensive literature coverage remain open."

    plan_record = state["records"][PLAN_ID]
    add_once(plan_record["full_sources"], GOAL)
    for path in [LIT_HOTT_INDEX, *[str(p.relative_to(ROOT)) for p in sorted((ROOT / LIT_HOTT_ROOT).glob("*.md"))]]:
        add_once(plan_record["full_sources"], path)
    for identity in (POST_ID, CT_ID, ORACLE_ID, GROUP_ID, LIT_HOTT_ID, SYNTAX_ID, CAND_ID, SESSION_ID):
        add_once(plan_record.setdefault("related_records", []), identity)
    plan_record["source_hashes"] = record_hashes(plan_record["full_sources"])
    plan_record["revalidation"] = f"{SESSION_ID}: R2 conditional internal negation and first exact groupoid-syntax slice are machine-replayed; Post and Oracle source boundaries are current. Next candidate and return paths are recorded without closing the exploration envelope."

    coverage = state["records"][COVERAGE_ID]
    for path in (LIT_HOTT_INDEX, LIT_HOTT_AUDIT):
        add_once(coverage["full_sources"], path)
    for identity in (POST_ID, CT_ID, ORACLE_ID, GROUP_ID, LIT_HOTT_ID, SYNTAX_ID, CAND_ID, SESSION_ID):
        add_once(coverage.setdefault("related_records", []), identity)
    coverage["source_hashes"] = record_hashes(coverage["full_sources"])
    coverage["scope"] = "Literature denominator remains open, but Post primary, Parametric CT source/replay, Oracle Modalities 34-file source and groupoid-syntax exact replay now close the first HoTT-computability slice. Classic residual, citation/venue, old toolchains, Brouwer Trees, Extension Types and holdout remain open."
    coverage["revalidation"] = f"{SESSION_ID}: prior claim that Post/CT/Oracle/groupoid-syntax were all un-ingested is superseded by direct source and run evidence; comprehensive coverage remains review_required."

    classics = state["records"][LIT_CLASSICS_ID]
    for path in post_sources:
        add_once(classics["full_sources"], path)
    for path in sorted((ROOT / LIT_CLASSICS_ROOT).glob("*.md")):
        add_once(classics["full_sources"], str(path.relative_to(ROOT)))
    for identity in (POST_ID, CT_ID, ORACLE_ID, GROUP_ID, LIT_HOTT_ID, SESSION_ID):
        add_once(classics.setdefault("related_records", []), identity)
    classics["source_hashes"] = record_hashes(classics["full_sources"])
    classics["evidence_status"] = "DOCUMENTED / PRIMARY_RELEVANT_SECTIONS_REVIEWED / POST_AND_ROSSER_PRIMARY_BODY_REVIEWED / HOTT_COMPUTABILITY_FIRST_SLICE"
    classics["scope"] = "Classic premise chain through Post 1944 primary and the first Parametric CT/Oracle/2LTT/groupoid-syntax successor slice. Tarski/HBL/Rice-Shapiro/Rogers/Myhill/Chaitin, citation chains and selected theorem replays remain open."
    classics["revalidation"] = f"{SESSION_ID}: Post primary body is closed with source/page receipts; LIT-HOTT-COMPUTABILITY-001 now owns modern HoTT-specific successors."

    denom = state["records"].get(LIT_DENOM_ID)
    if isinstance(denom, dict):
        add_once(denom.setdefault("related_records", []), SESSION_ID)
        hashes = denom.get("source_hashes")
        if isinstance(hashes, dict) and LIT_DENOM_003 in hashes:
            hashes[LIT_DENOM_003] = R.sha((ROOT / LIT_DENOM_003).read_bytes())
        denom["revalidation"] = f"{SESSION_ID}: denominator v1 remains frozen; current seed statuses now record Post, Parametric CT, Oracle Modalities and groupoid-syntax evidence without changing the discovery snapshot."

    gate = state["records"][PROOF_GATE_ID]
    for path in [
        f"{CT_FORMAL}/CheckInternalUndec.v", f"{CT_RUN}/RUN.json", f"{CT_RUN}/index-row-manifest.json",
        f"{GROUP_FORMAL}/CheckGroupoidSyntax.agda", f"{GROUP_RUN}/RUN.json", f"{GROUP_RUN}/index-row-manifest.json",
        REGISTRY, MATRIX, VERIFIER,
    ]:
        add_once(gate["full_sources"], path)
    for identity in (CT_ID, GROUP_ID, SESSION_ID):
        add_once(gate.setdefault("related_records", []), identity)
    gate["source_hashes"] = record_hashes(gate["full_sources"])
    gate["revalidation"] = f"{SESSION_ID}: registry now contains 17 frozen packages plus 21 later packages/78 claims. C-219-C-226 are indexed, row-frozen and exact-replayed; all new assets remain local uncommitted."

    changed = [
        GOAL, FEATURE, PROGRAM_005, PROGRAM_006, PROGRAM_TEST, LIT_DENOM_003,
        LIT_CLASSICS_INDEX, *[str(p.relative_to(ROOT)) for p in sorted((ROOT / LIT_CLASSICS_ROOT).glob("*.md"))],
        LIT_HOTT_INDEX, *[str(p.relative_to(ROOT)) for p in sorted((ROOT / LIT_HOTT_ROOT).glob("*.md"))],
        MATRIX, REGISTRY, FORMAL_README, RUNS_README, HOTT_README, README_SHARD, VERIFIER,
    ]
    for record in state["records"].values():
        hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(hashes, dict):
            continue
        rebound: list[str] = []
        for path in changed:
            if path in hashes:
                current_hash = R.sha((ROOT / path).read_bytes())
                if hashes[path] != current_hash:
                    hashes[path] = current_hash
                    rebound.append(path)
        if rebound:
            note = (
                f"{SESSION_ID}: revalidated after current-owner/index/audit-tool evolution at "
                f"{', '.join(rebound)}. Prior proof scopes are unchanged; C-219-C-226 and the new literature/candidate "
                "states are additive and separately identified."
            )
            previous = record.get("revalidation")
            record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：R2 internal-no-decider、G-HOTT-SYNTAX 与 Post/HoTT literature 三向薄切。
- Post：BAMS 50(5) 印刷页 284–316，33 页抽取、页界、四页视觉与全文首读完成；theorems 未重放。
- R2：`{CT_PROOF}` / C-219–C-222；显式 EPF_bool/SCT 前提下 internal no-decider；三个 assumptions closed；exact replay。
- syntax：`{GROUP_PROOF}` / C-223–C-226；20 个 TT 模块两阶段重放、`isSetTy` 与四类同构；exact replay。
- Oracle：34 文件 MIT 源树导入；negative resizing、Markov induction、φ₀、computable choice 四组 postulate 固定；旧工具链未重放。
- 新候选：2LTT internal context-stable fibrant replacement→inner UIP；source-reported，尚未机器证明。
- Goal：保持 active；ambient R2、完整 R4、CE-MAP、natural consumer、HoTT essentiality、现实桥梁与全面文献覆盖仍开放。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "formal_runs": [
            {"proof_id": CT_PROOF, "run_id": CT_RUN_ID, "claims": CT_CLAIMS, "status": "PASS_WITH_SCOPE / EXACT_REPLAY"},
            {"proof_id": GROUP_PROOF, "run_id": GROUP_RUN_ID, "claims": GROUP_CLAIMS, "status": "PASS_WITH_SCOPE / EXACT_REPLAY"},
        ],
        "source_qualifications": {
            "post_1944": {"status": "PRIMARY_BODY_REVIEWED", "receipt": POST_IMPORT},
            "oracle_modalities": {"status": "SOURCE_QUALIFIED_NOT_REPLAYED", "receipt": ORACLE_IMPORT, "files": 34},
        },
        "completeness_audit": {
            "cells_touched": [
                "TC-08×OP-08/03×conditional-internal-negation×Coq",
                "TC-06×OP-11×oracle-continuation×Cubical-source",
                "TC-09/11×OP-12×groupoid-syntax×Cubical-kernel",
                "TC-11×OP-02/03×fibrant-replacement-context-stability×candidate",
            ],
            "untouched_axes": ["physical-time/continuous-motion", "complete-HIT/universe syntax", "empirical reality task"],
            "generators": ["GNR-4 universal-computation premise qualification", "GNR-6 source-guided proposal and replay"],
            "finite_denominators": "CT 109-file and groupoid 91-file trees complete for named snapshots; Oracle 34-file tree copied with remainder 0; open candidate classes not declared complete",
            "reducer": "NOT_APPLICABLE; no witness minimisation or class-wide reduction in this unit",
            "oracles": ["Coq kernel", "Cubical Agda kernel", "archive-vs-git tree comparison", "primary-page/source review"],
            "false_positive_controls": ["EPF/SCT premise retained", "groupoid slice not full HoTT", "Oracle postulates explicit", "2LTT theorem candidate not replayed"],
            "holdout": "Independent authors/frameworks represented, but formal holdout denominator remains open",
            "taxonomy_revision": "Added conditional-internal-negation level and TC-11 external-pointwise-to-internal-context-stable candidate cell",
            "next_successor": CAND_ID,
            "reopen_or_fallback": "If internal-R rules are artificial or ablation removes HoTT necessity, downgrade and return to CE-MAP/Oracle/ambient-R2/full-R4 cells",
        },
        "next": [CAND_ID, "CE-MAP-001", "ORACLE-MODALITY-REPLAY-001", "R2-AMBIENT-UNDEC-001", "G-HOTT-SYNTAX-EXPAND-001"],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, CT_AUDIT, GROUP_AUDIT, POST_AUDIT, LIT_HOTT_AUDIT],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, GOAL_ID, PLAN_ID, POST_ID, CT_ID, ORACLE_ID, GROUP_ID, LIT_HOTT_ID, SYNTAX_ID, CAND_ID],
        "scope": "Close the three breadth-first slices with exact machine/source evidence and select, without proving, the 2LTT internal fibrant-replacement -> UIP candidate.",
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
        "authorization": "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {
                "path": path,
                "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None,
                "text": value,
            }
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 146, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
