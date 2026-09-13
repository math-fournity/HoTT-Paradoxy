#!/usr/bin/env python3
"""Prepare revision 37: record MP-CONTEXT-CHARACTERIZATION-001 and route guard-erasure.

The run proves the full characterization of the contextual equivalence on the
Bool fragment (C-89–C-91): lt trichotomy, general strict-time separation, and
p ≡c q ↔ p ≡ q. The checkpoint records the result and session, applies the
projection updates with exact text substitutions, repairs the thirteen stale
source hashes, and moves the projections to revision 37.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-037-CONTEXT-CHARACTERIZATION"
PREV_SESSION = "S-RES-20260912-036-QUOTIENT-MONAD"
RESULT_ID = "A-CONTEXT-CHARACTERIZATION-FORMAL-001"
PROOF_ID = "MP-CONTEXT-CHARACTERIZATION-001"
RUN_ID = "20260912-MP-CONTEXT-CHARACTERIZATION-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/ContextCharacterization.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/ContextCharacterization.README.md"
DEP1 = "HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda"
DEP2 = "HoTT/formal/partiality-race-timeout/ContextualEquivalence.agda"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/context-characterization机器证明实施证据-20260912.md"
NEW_STATUS = "CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_context_char", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:60]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "本轮把 partiality 片段的边界收束为完整刻画（≡c = 代表相等），仍不是内部矛盾，符合“找现实相对非现实性”的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 partiality 片段被完全分离：结果商与上下文等价的关系已被完整刻画，资格越级只可能在自然接口层。"),
        "KC-000013": ("DEEPENED", "理论工具性的边界被完全定位：遗忘完成先后的收益与代价都被精确刻画。"),
        "KC-000014": ("ALIGNED", "方向 B 的判别工具进一步精确：结果类可以承载单子，但不能承载 race/deadline；两者界线已被完整刻画。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0 且 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在 partiality 片段达到完整刻画；仍未证实悖论。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”在 Bool 片段被完整排除（≡c 保留全部时序信息）。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”被完全刻画：经济收益可分裂、可做单子，但上下文等价要求保留时序。"),
        "KC-000031": ("ALIGNED", "HoTT 严格性再次表现为完整刻画与正面结构，不是 coverage failure。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(
            unit["id"],
            ("NOT_TOUCHED", "本轮聚焦 Bool 片段上下文等价的完整刻画；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S037/SESSION.md；核心认知.md `{unit['id']}` | guard-erasure 工作包、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — 上下文等价完整刻画（`C-89`–`C-91`）；第一工作包转为 guard-erasure 第一机器构造；revision 37/generation 021。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-CONTEXT-CHARACTERIZATION`（`CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`）。",
        "- update_decision: `MP-CONTEXT-CHARACTERIZATION-001 进入 formal/run/index/STATE；C-89–C-91 进入 claim matrix；六个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 六个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `guard-erasure、更宽值类型、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S036 方向更新后的第一工作包（`≡c` 完整刻画）。",
        "- 构造：`lt-trichotomy`（C-89，归纳）；`timing-separates`（C-90，合并 deadline-0 与单向 lt）；`deadline-lt/gt-separates`、`same-time-values` 与双向收口 `≡c-iff-≡`（C-91）。",
        "- 结果：`MP-CONTEXT-CHARACTERIZATION-001`（C-89–C-91）通过 kernel：Bool 片段上 `p ≡c q ↔ p ≡ q`；代表相等即最细，任何上下文扩展不能区分更多。判词 `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`（非悖论）。",
        "- 运行：final run `20260912-MP-CONTEXT-CHARACTERIZATION-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。",
        "- 旧证据：矩阵第四次增长后，五个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：`_⊎_` 解析歧义、`if_then_else_` 导入、等式链方向反转，均为机械修正，命题未削弱。",
        "- 边界：只覆盖 Bool 片段与固定上下文族；不推广到一般值类型/一般商；不证明现实失配或 HoTT 内部矛盾。",
        "- 三件套：direction/panorama revision 37/generation 021；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ]
    return "\n".join(lines)


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_QUOTIENT_MONAD_CONSTRUCTED_CONTEXT_CHARACTERIZATION_NEXT`",
        "状态：`CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 36", "source_state_revision: 37")
    direction = sub_once(direction, "projection_generation: 20260912-direction-020", "projection_generation: 20260912-direction-021")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_QUOTIENT_MONAD_CONSTRUCTED_CONTEXT_CHARACTERIZATION_NEXT",
        "semantic_status: CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-QUOTIENT-MONAD`、`OUT-W-R041-PAPER`",
        "、`OUT-TOP-QUOTIENT-MONAD`、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-W-R041-PAPER`",
    )
    direction = sub_once(
        direction,
        "；下一步机器化 `≡c` 的完整刻画与更宽上下文语言，再寻找自然 consumer 桥梁",
        "；下一步转 guard-erasure 第一机器构造（source/target 演算 + forgetful translation + consumer 审计），再寻找自然 consumer 桥梁",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-QUOTIENT-MONAD` | partiality 片段的正面结构已闭合：结果商可分裂、商值 continuation 单子成立；经济收益的边界（race/deadline 不可下降、上下文等价严格更细）保持",
        "`OUT-TOP-QUOTIENT-MONAD`、`OUT-TOP-CONTEXT-CHARACTERIZATION` | partiality 片段的正反结构已完全闭合（商可分裂、单子成立、`≡c` = 代表相等）；经济收益的边界（race/deadline 不可下降）保持",
    )
    direction = sub_once(direction, "C4；五个 proof packages", "C4；六个 proof packages")
    direction = sub_once(
        direction,
        "`OUT-TOP-QUOTIENT-MONAD` | partiality 片段已形成完整的正反结构",
        "`OUT-TOP-QUOTIENT-MONAD`、`OUT-TOP-CONTEXT-CHARACTERIZATION` | partiality 片段已形成完整的正反结构与完整刻画",
    )
    direction = sub_once(
        direction,
        "下一步在 `≡c` 刻画与更宽上下文语言之后寻找新的现实相对实例",
        "下一步转 guard-erasure 第一机器构造寻找新的现实相对实例",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-QUOTIENT-MONAD` | 截断排除",
        "`OUT-TOP-QUOTIENT-MONAD`、`OUT-TOP-CONTEXT-CHARACTERIZATION` | 截断排除",
    )
    direction = sub_once(
        direction,
        "与商值 continuation 单子（C-84–C-88）均已机器闭合；",
        "、商值 continuation 单子（C-84–C-88）与上下文等价完整刻画（C-89–C-91）均已机器闭合；",
    )
    direction = sub_once(
        direction,
        "；`MP-QUOTIENT-MONAD-001` 原生构造商值 continuation 单子（`C-84`–`C-88`）。",
        "；`MP-QUOTIENT-MONAD-001` 原生构造商值 continuation 单子（`C-84`–`C-88`）；`MP-CONTEXT-CHARACTERIZATION-001` 原生给出上下文等价完整刻画（`C-89`–`C-91`：`≡c` = 代表相等）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：`≡c` 的完整刻画与更宽上下文语言——补 `lt`/`leb` trichotomy 后证明 Bool 片段上 `p ≡c q ↔ p ≡ q`；再评估加入商值 continuation 上下文后的最粗等价是否仍严格保留时序。",
        "4. **当前第一工作包**：guard-erasure 第一机器构造——固定 source（带 stage/guard 的演算）与 target（无 stage 片段）及 forgetful translation，机器检验条件不动点/非因子化引理的精确形式，并审计是否存在真实 consumer（无则记 `REPRESENTATION_BOUNDARY`）。",
    )
    direction = sub_once(
        direction,
        "AND_PARTIALITY_CONTEXT_AND_MONAD_BOUNDARY`：C-59–C-66、C-67–C-70、C-71–C-76、C-77–C-83 与 C-84–C-88 分别机器闭合",
        "AND_PARTIALITY_CONTEXT_MONAD_AND_CHARACTERIZATION_BOUNDARY`：C-59–C-66、C-67–C-70、C-71–C-76、C-77–C-83、C-84–C-88 与 C-89–C-91 分别机器闭合",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_QUOTIENT_MONAD_CONSTRUCTED_CONTEXT_CHARACTERIZATION_NEXT`",
        "状态：`CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 36", "source_state_revision: 37")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-020", "projection_generation: 20260912-outcome-021")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_QUOTIENT_MONAD_CONSTRUCTED_CONTEXT_CHARACTERIZATION_NEXT",
        "semantic_status: CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT",
    )
    new_row = (
        "| `OUT-TOP-CONTEXT-CHARACTERIZATION` | `MP-CONTEXT-CHARACTERIZATION-001`：Bool 片段上下文等价的完整刻画——`lt` 三分律（`C-89`）、一般严格时间分离（`C-90`）、`p ≡c q ↔ p ≡ q`（`C-91`）；代表相等即最细，任何上下文扩展不能区分更多 |"
        " `DIR-W-RACE-TIMEOUT`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；最粗可替换等价 = 代表相等 |"
        " 只覆盖 Bool 片段与固定上下文族；不推广到一般值类型/一般商，不证明现实失配或 HoTT 内部矛盾 |"
        " `HoTT/formal/partiality-race-timeout/ContextCharacterization.agda`；final run `20260912-MP-CONTEXT-CHARACTERIZATION-001-01`；claim matrix C-89–C-91；`audit/context-characterization机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", new_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "、上下文等价层次与商值 continuation 单子已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED`）。`≡c` 的完整刻画、更宽上下文语言、自然 consumer、",
        "、上下文等价层次、商值 continuation 单子与上下文等价完整刻画已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`）。更宽值类型、自然 consumer、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "`MP-QUOTIENT-MONAD-001` 构造了结果商上的商值 continuation 单子（商可分裂、无需选择）；四者都不是 HoTT 悖论。",
        "`MP-QUOTIENT-MONAD-001` 构造了结果商上的商值 continuation 单子（商可分裂、无需选择）；`MP-CONTEXT-CHARACTERIZATION-001` 完整刻画上下文等价（Bool 片段上 `≡c` 恰为代表相等）；五者都不是 HoTT 悖论。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | `≡c` 完整刻画与更宽上下文语言 | next-candidate / same Cubical toolchain | 补 `lt`/`leb` trichotomy，证明 Bool 片段上 `p ≡c q ↔ p ≡ q`；再评估加入商值 continuation 上下文后的最粗等价是否仍严格保留时序 |",
        "| 已闭合工作包 4 | 上下文等价完整刻画（`C-89`–`C-91`） | machine-proved-local-uncommitted / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` | `≡c` 恰为代表相等；Bool 片段内任何上下文扩展不能区分更多 |\n"
        "| 第一工作包 | guard-erasure 第一机器构造 | next-candidate / same Cubical toolchain | 固定 source（带 stage/guard）与 target（无 stage）演算及 forgetful translation；机器检验条件不动点/非因子化引理的精确形式；审计真实 consumer（无则记 `REPRESENTATION_BOUNDARY`） |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "1. `MP-QUOTIENT-MONAD-001` 完成 R041 §2.1 在本片段的正面解答：C-84–C-88 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / MONAD_STRUCTURE_CONSTRUCTED`；结果商有 canonical section，商值 continuation 单子（单位律 + 代表层/商层关联律）成立，无需选择公理。\n2. 当前第一数学工作包转为 `≡c` 的完整刻画与更宽上下文语言：补 `lt`/`leb` trichotomy 证明 Bool 片段 `p ≡c q ↔ p ≡ q`，再评估加入商值 continuation 上下文后的最粗等价。",
        "1. `MP-CONTEXT-CHARACTERIZATION-001` 完成上下文等价完整刻画：C-89–C-91 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`；Bool 片段上 `p ≡c q ↔ p ≡ q`（代表相等即最细）。\n2. 当前第一数学工作包转为 guard-erasure 第一机器构造：固定 source/target 演算与 forgetful translation，机器检验条件不动点/非因子化引理，并审计真实 consumer。",
    )
    memory = sub_once(
        memory,
        "- `MP-QUOTIENT-MONAD-001` 是第五个 F-011 package：结果商 canonical section 与商值 continuation 单子（C-84–C-88，含单位律与关联律）；final run `20260912-MP-QUOTIENT-MONAD-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `MONAD_STRUCTURE_CONSTRUCTED`（正面结构结果）。",
        "- `MP-QUOTIENT-MONAD-001` 是第五个 F-011 package：结果商 canonical section 与商值 continuation 单子（C-84–C-88，含单位律与关联律）；final run `20260912-MP-QUOTIENT-MONAD-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `MONAD_STRUCTURE_CONSTRUCTED`（正面结构结果）。\n- `MP-CONTEXT-CHARACTERIZATION-001` 是第六个 F-011 package：Bool 片段上下文等价完整刻画（C-89–C-91，`≡c` = 代表相等）；final run `20260912-MP-CONTEXT-CHARACTERIZATION-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`。",
    )
    memory = sub_once(
        memory,
        "`A-CONTEXTUAL-EQUIV-FORMAL-001`、`A-QUOTIENT-MONAD-FORMAL-001`。partiality 片段已闭合为\"边界 + 正面单子结构\"；下一步做 `≡c` 完整刻画与更宽上下文语言，不直接跳 ERCF-3。",
        "`A-CONTEXTUAL-EQUIV-FORMAL-001`、`A-QUOTIENT-MONAD-FORMAL-001`、`A-CONTEXT-CHARACTERIZATION-FORMAL-001`。partiality 片段已完全闭合（边界 + 单子 + 完整刻画）；下一步转 guard-erasure 第一机器构造，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S037 完成 `MP-CONTEXT-CHARACTERIZATION-001`（C-89–C-91）：Bool 片段上下文等价完整刻画，`p ≡c q ↔ p ≡ q`（代表相等即最细，任何上下文扩展不能区分更多）。下一工作包转为 guard-erasure 第一机器构造；ERCF-3 仍等待自然 consumer。\n\n",
    )

    return {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}RESUME.md": resume,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 36 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_36_AND_S036")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != ["C-89", "C-90", "C-91"]
    ):
        raise SystemExit("FINAL_RUN_NOT_ACCEPTED_AND_INDEXED")
    for required in ("index-row-manifest.json", "source-manifest.json", "stdout.txt", "stderr.txt", "environment.txt"):
        if not (run_dir / required).is_file():
            raise SystemExit(f"RUN_FILE_MISSING:{required}")

    new_hashes = {
        MATRIX: sha(root / MATRIX),
        FORMAL_README: sha(root / FORMAL_README),
        RUNS_README: sha(root / RUNS_README),
        SOURCE: sha(root / SOURCE),
        SOURCE_README: sha(root / SOURCE_README),
        DEP1: sha(root / DEP1),
        DEP2: sha(root / DEP2),
        f"HoTT/verification/runs/{RUN_ID}/RUN.json": sha(run_dir / "RUN.json"),
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": sha(run_dir / "index-row-manifest.json"),
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": sha(run_dir / "source-manifest.json"),
        AUDIT_DOC: sha(root / AUDIT_DOC),
    }

    expected_stale = {
        ("A-CONTEXTUAL-EQUIV-FORMAL-001", MATRIX),
        ("A-ERCF-FACTORIZATION-FORMAL-001", MATRIX),
        ("A-ERCF-TRUNCATION-DEFENSE-001", MATRIX),
        ("A-HOTT-SELF-VALIDATION-ECONOMY-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", FORMAL_README),
        ("A-MATH-PROOF-DELIVERY-GATE-001", RUNS_README),
        ("A-QUOTIENT-MONAD-FORMAL-001", MATRIX),
        ("A-RACE-TIMEOUT-FORMAL-001", MATRIX),
        ("S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT", FORMAL_README),
        ("S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT", RUNS_README),
        ("S-RES-20260912-028-ERCF-FACTORIZATION-LEAN", MATRIX),
        ("S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE", MATRIX),
    }
    observed_stale = set()
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            if not path.is_file() or sha(path) != exp:
                observed_stale.add((rid, rel))
    if observed_stale != expected_stale:
        raise SystemExit(f"UNEXPECTED_STALE_SET:{sorted(observed_stale)}")

    row_stable_note = "After C-89 through C-91 were appended (S037), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "A-RACE-TIMEOUT-FORMAL-001",
        "A-CONTEXTUAL-EQUIV-FORMAL-001",
        "A-QUOTIENT-MONAD-FORMAL-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S037 completed the contextual-equivalence strand: ≡c coincides with representational equality on the Bool fragment (C-89–C-91). C4 text is unchanged and the remaining items stay open."
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
        if rel not in economy["full_sources"]:
            economy["full_sources"].append(rel)
    economy["mathematical_status"] = "FACTORIZATION_TRUNCATION_PARTIALITY_CONTEXT_MONAD_AND_CHARACTERIZATION_PROVED_NATURAL_CONSUMER_OPEN"

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, DEP2, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S037 appended the context-characterization package; all six proof packages re-validated (five row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."
    gate["scope"] = "Require machine proof source/run/index before delivery. Lean, native Cubical truncation, race/timeout, contextual equivalence, quotient monad and context characterization packages pass; dependencies are publisher/hash pinned and old index rows remain immutable. Fresh-model behavior and Git version closure remain open."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S037 appended the context-characterization package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-021"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the full characterization: on the Bool fragment the coarsest equivalence respected by the fixed context family is representational equality; the first work package switches to the guard-erasure machine construction."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-021"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the context-characterization result C-89–C-91 completing the partiality strand; the natural consumer remains unfound and the next strand is guard-erasure."
    for rec in (direction_rec, panorama_rec):
        for rel in (SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)

    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED",
        "proof_id": PROOF_ID,
        "claim_ids": ["C-89", "C-90", "C-91"],
        "run_id": RUN_ID,
        "mathematical_status": "CONTEXTUAL_EQUIVALENCE_EQUALS_REPRESENTATIONAL_EQUALITY_ON_BOOL_FRAGMENT",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001", "A-CONTEXTUAL-EQUIV-FORMAL-001"],
        "full_sources": [
            SOURCE,
            SOURCE_README,
            DEP1,
            DEP2,
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/stdout.txt",
            f"HoTT/verification/runs/{RUN_ID}/stderr.txt",
            f"HoTT/verification/runs/{RUN_ID}/environment.txt",
            MATRIX,
            "scripts/audit/capture_agda_proof_run.py",
            "scripts/audit/mark_proof_run_indexed.py",
            "scripts/audit/freeze_proof_index_rows.py",
            "scripts/audit/verify_formal_proof_run.py",
            AUDIT_DOC,
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            SOURCE_README: new_hashes[SOURCE_README],
            DEP1: new_hashes[DEP1],
            DEP2: new_hashes[DEP2],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0; source, dependencies, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX,
                "scripts/audit/verify_formal_proof_run.py",
                AUDIT_DOC,
            ],
        },
        "scope": "Native Cubical Agda full characterization of the contextual equivalence on the Bool fragment of the R041 delay model: lt trichotomy (C-89), general strict-time separation (C-90), and p ≡c q ↔ p ≡ q (C-91). Representational equality is the finest possible, so no context extension can distinguish more in this fragment. Not a HoTT paradox.",
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            SOURCE,
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            AUDIT_DOC,
            "scripts/audit/prepare_context_characterization_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED",
        "cognition_status": "CONTEXT_CHARACTERIZATION_COMPLETED_AND_GUARD_ERASURE_ROUTED",
        "scope": "Complete the contextual-equivalence strand (C-89–C-91), revalidate the five older packages row-stable, and route the guard-erasure first machine construction as the next package.",
    }

    state["revision"] = 37
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, fix an explicit source calculus with stage/guard and a target fragment without stages, define the forgetful translation, machine-check the precise conditional fixed-point/non-factorization lemma, and audit whether a real consumer of the collapsed representation exists (otherwise record REPRESENTATION_BOUNDARY).",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-89", "C-90", "C-91"],
        "final_run": {
            "run_id": RUN_ID,
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "older_proofs_after_matrix_growth": {
            "20260912-MP-ERCF-001-02": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
            "20260912-MP-ERCF-TRUNC-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
            "20260912-MP-RACE-TIMEOUT-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
            "20260912-MP-CONTEXTUAL-EQUIV-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
            "20260912-MP-QUOTIENT-MONAD-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "stale_source_hash_repair": {"observed": 13, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 37",
            "projection freshness PASS (27 directions / 33 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 37",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    edited = apply_projection_edits(root)
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    texts = {
        **edited,
        f"{R.PREFIX}LESSONS.md": lessons,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved full characterization of the contextual equivalence (C-89–C-91), fixes the thirteen stale source hashes, applies the projection text updates, and routes the guard-erasure work package. No Git commit, tag or push.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 37,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
