#!/usr/bin/env python3
"""Prepare revision 38: record MP-GUARD-ERASURE-001 and route the cost package.

The run machine-proves the guard/stage-erasure equivalence (C-92–C-95):
erasure-while-keeping-the-update-law holds iff the law has a fixed point, with
the negation law refuted and the oscillating orbit as the concrete witness.
The checkpoint records the result and session, applies the projection text
updates, repairs the fourteen stale source hashes, and moves the projections
to revision 38 with the same-function-different-time (cost) package next.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-038-GUARD-ERASURE"
PREV_SESSION = "S-RES-20260912-037-CONTEXT-CHARACTERIZATION"
RESULT_ID = "A-GUARD-ERASURE-FORMAL-001"
PROOF_ID = "MP-GUARD-ERASURE-001"
RUN_ID = "20260912-MP-GUARD-ERASURE-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/GuardErasure.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/GuardErasure.README.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/guard-erasure机器证明实施证据-20260912.md"
NEW_STATUS = "GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_guard_erasure", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:70]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "本轮把阶段擦除判别做成等价判据，仍是边界结果而非内部矛盾，符合“找现实相对非现实性”的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 guard-erasure 上获得等价判据：只有律有不动点时，忘掉阶段才与保留律相容。"),
        "KC-000013": ("DEEPENED", "理论工具性的“省略阶段”被精确刻画：省略何时合法、何时非法由不动点存在性判定。"),
        "KC-000014": ("ALIGNED", "方向 B 的判别工具扩展到阶段/guard：把“已有不动点”与“可擦除阶段”严格等同。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0 且 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在 guard-erasure 支线上推进；结论是边界判据而非悖论。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”在阶段擦除上被精确刻画：擦除阶段必须付出不动点代价。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”再次具体化：省略阶段的收益由律的不动点结构决定。"),
        "KC-000031": ("ALIGNED", "HoTT/类型论的严格性表现为可证伪的等价判据，而不是 coverage failure。"),
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
            ("NOT_TOUCHED", "本轮聚焦 guard/stage 擦除与不动点存在的等价判据；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S038/SESSION.md；核心认知.md `{unit['id']}` | cost 工作包、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — `DIR-L-GUARD-ERASURE` 闭合为等价判据（`C-92`–`C-95`）；第一工作包转为同函数异时（cost）第一机器构造；revision 38/generation 022。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-GUARD-ERASURE`（`GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`）。",
        "- update_decision: `MP-GUARD-ERASURE-001 进入 formal/run/index/STATE；C-92–C-95 进入 claim matrix；七个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 七个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `cost 工作包、guarded/clocked 完整翻译、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S037 方向更新后的第一工作包（guard-erasure 第一机器构造）。",
        "- 构造：显式源演算（`ℕ → X` 阶段流 + `shift`）、忘却翻译（阶段不变性 + 保更新律）、双向引理（必要性/充分性）、否定律反例与具体振荡轨道。",
        "- 结果：`MP-GUARD-ERASURE-001`（C-92–C-95）通过 kernel：保律地擦除阶段 ⇔ 律有不动点；`not` 无不动点故不可擦除；`orbit` 给出具体见证。判词 `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`（非悖论）。",
        "- 运行：final run `20260912-MP-GUARD-ERASURE-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。",
        "- 旧证据：矩阵第五次增长后，六个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：`⊥` 导入与 `¬` 本地定义两处机械修正；命题未削弱。",
        "- 边界：使用 ℕ-indexed 显式阶段模型；不做 guarded/clocked 完整翻译；不主张物理时间、HoTT 独有或原创性（历史条件形式见 ZCore）。",
        "- 三件套：direction/panorama revision 38/generation 022；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ]
    return "\n".join(lines)


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT`",
        "状态：`CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 37", "source_state_revision: 38")
    direction = sub_once(direction, "projection_generation: 20260912-direction-021", "projection_generation: 20260912-direction-022")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT",
        "semantic_status: CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-W-R041-PAPER`",
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE`、`OUT-W-R041-PAPER`",
    )
    direction = sub_once(
        direction,
        "；下一步转 guard-erasure 第一机器构造（source/target 演算 + forgetful translation + consumer 审计），再寻找自然 consumer 桥梁",
        "；下一步转同函数异时（cost）第一机器构造（程序语法/求值/成本 + 裸函数非因子化 + 显式成本表示正例），再寻找自然 consumer 桥梁",
    )
    direction = sub_once(
        direction,
        "| `DIR-L-GUARD-ERASURE` | 忘掉阶段/guard 但保持更新律是否造成固定点或现实过程失真 | LocalGPT、WebGPT `C-TIME-SCHEDULE-001` | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `PARADOX_DISCOVERY` | `OUT-L-GUARD-ERASURE`（一般条件边界） | 写明 source/target 演算、forgetful translation、不可擦除 observable 和合法推演 | `/Volumes/D/ALL-Markdown/HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md` §10；`workspace/HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md` |",
        "| `DIR-L-GUARD-ERASURE` | 忘掉阶段/guard 但保持更新律是否造成固定点或现实过程失真 | LocalGPT、WebGPT `C-TIME-SCHEDULE-001` | `CLOSED_WITH_SCOPE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `PARADOX_DISCOVERY` | `OUT-L-GUARD-ERASURE`（一般条件边界）、`OUT-TOP-GUARD-ERASURE`（机器化等价判据 C-92–C-95） | 显式源演算 + 忘却翻译下已证明：保律地擦除阶段 ⇔ 律有不动点；否定律被拒绝、振荡轨道为见证；无自然 consumer，guarded/clocked 完整翻译作为未来细化 | `HoTT/formal/partiality-race-timeout/GuardErasure.agda`；`audit/guard-erasure机器证明实施证据-20260912.md`；ZCore 历史形式 |",
    )
    direction = sub_once(
        direction,
        "| `DIR-L-SAME-FUNCTION-DIFFERENT-TIME` | 同一外延函数的不同实现具有不同时间/资源成本 | LocalGPT current owner | `CANDIDATE` | `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `HOTT_OBJECT` | `OUT-L-TIME-BOUNDARY`（一手 cost-aware 支持）；形式化未完成 | 固定 program/semantics/cost 和实现 identity，寻找非因子化或严格正例 |",
        "| `DIR-L-SAME-FUNCTION-DIFFERENT-TIME` | 同一外延函数的不同实现具有不同时间/资源成本 | LocalGPT current owner | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `HOTT_OBJECT` | `OUT-L-TIME-BOUNDARY`（一手 cost-aware 支持）；形式化未完成 | 第一机器构造：固定 program/semantics/cost 与实现 identity，用同一 Cubical 工具链证明裸函数表示不可恢复成本（非因子化）与显式成本表示的充分性（正例） |",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-CONTEXT-CHARACTERIZATION` | partiality 片段的正反结构已完全闭合",
        "`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE` | partiality 片段与 guard-erasure 支线的正反结构已完全闭合",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-CONTEXT-CHARACTERIZATION` | partiality 片段已形成完整的正反结构与完整刻画",
        "`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE` | partiality 片段与 guard-erasure 支线已形成完整的正反结构",
    )
    direction = sub_once(
        direction,
        "；`MP-CONTEXT-CHARACTERIZATION-001` 原生给出上下文等价完整刻画（`C-89`–`C-91`：`≡c` = 代表相等）。",
        "；`MP-CONTEXT-CHARACTERIZATION-001` 原生给出上下文等价完整刻画（`C-89`–`C-91`：`≡c` = 代表相等）；`MP-GUARD-ERASURE-001` 原生证明阶段擦除与不动点存在的等价（`C-92`–`C-95`）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：guard-erasure 第一机器构造——固定 source（带 stage/guard 的演算）与 target（无 stage 片段）及 forgetful translation，机器检验条件不动点/非因子化引理的精确形式，并审计是否存在真实 consumer（无则记 `REPRESENTATION_BOUNDARY`）。",
        "4. **当前第一工作包**：同函数异时（cost）第一机器构造——固定程序语法/求值与成本，证明裸函数表示不可恢复成本（非因子化必要方向），再给出显式成本表示的充分性正例；随后评估自然 consumer。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT`",
        "状态：`CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 37", "source_state_revision: 38")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-021", "projection_generation: 20260912-outcome-022")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_CONTEXT_FULLY_CHARACTERIZED_GUARD_ERASURE_NEXT",
        "semantic_status: CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT",
    )
    new_row = (
        "| `OUT-TOP-GUARD-ERASURE` | `MP-GUARD-ERASURE-001`：显式阶段流演算 + 忘却翻译下的 guard/stage 擦除判别——保更新律地擦除阶段 ⇒ 不动点（`C-92`）、不动点 ⇒ 可擦除（`C-94`），否定律被拒绝（`C-93`），振荡轨道为具体见证（`C-95`） |"
        " `DIR-L-GUARD-ERASURE`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-A-REALITY-RELATIVE`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；擦除可行性 = 不动点存在性 |"
        " 不做 guarded/clocked 完整翻译；不主张物理时间、HoTT 独有或原创性 |"
        " `HoTT/formal/partiality-race-timeout/GuardErasure.agda`；final run `20260912-MP-GUARD-ERASURE-001-01`；claim matrix C-92–C-95；`audit/guard-erasure机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", new_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "、上下文等价层次、商值 continuation 单子与上下文等价完整刻画已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`）。更宽值类型、自然 consumer、",
        "、上下文等价层次、商值 continuation 单子、上下文等价完整刻画与 guard-erasure 等价判据已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`）。同函数异时（cost）、guarded/clocked 翻译、自然 consumer、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "`MP-CONTEXT-CHARACTERIZATION-001` 完整刻画上下文等价（Bool 片段上 `≡c` 恰为代表相等）；五者都不是 HoTT 悖论。",
        "`MP-CONTEXT-CHARACTERIZATION-001` 完整刻画上下文等价（Bool 片段上 `≡c` 恰为代表相等）；`MP-GUARD-ERASURE-001` 证明阶段擦除与不动点存在的等价；六者都不是 HoTT 悖论。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | guard-erasure 第一机器构造 | next-candidate / same Cubical toolchain | 固定 source（带 stage/guard）与 target（无 stage）演算及 forgetful translation；机器检验条件不动点/非因子化引理的精确形式；审计真实 consumer（无则记 `REPRESENTATION_BOUNDARY`） |",
        "| 已闭合工作包 5 | 阶段擦除等价判据（`C-92`–`C-95`） | machine-proved-local-uncommitted / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` | 保律擦除 ⇔ 不动点存在；否定律被拒绝、常值/幂等律可构造；无自然 consumer |\n"
        "| 第一工作包 | 同函数异时（cost）第一机器构造 | next-candidate / same Cubical toolchain | 固定程序语法/求值与成本；证明裸函数表示不可恢复成本（非因子化），并给出显式成本表示的充分性正例 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "1. `MP-CONTEXT-CHARACTERIZATION-001` 完成上下文等价完整刻画：C-89–C-91 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`；Bool 片段上 `p ≡c q ↔ p ≡ q`（代表相等即最细）。\n2. 当前第一数学工作包转为 guard-erasure 第一机器构造：固定 source/target 演算与 forgetful translation，机器检验条件不动点/非因子化引理，并审计真实 consumer。",
        "1. `MP-GUARD-ERASURE-001` 完成 guard/stage 擦除等价判据：C-92–C-95 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`；保律地擦除阶段 ⇔ 律有不动点（否定律被拒绝、常值/幂等律可构造）。\n2. 当前第一数学工作包转为同函数异时（cost）第一机器构造：固定程序语法/求值与成本，证明裸函数表示不可恢复成本，并给出显式成本表示的充分性正例。",
    )
    memory = sub_once(
        memory,
        "- `MP-CONTEXT-CHARACTERIZATION-001` 是第六个 F-011 package：Bool 片段上下文等价完整刻画（C-89–C-91，`≡c` = 代表相等）；final run `20260912-MP-CONTEXT-CHARACTERIZATION-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`。",
        "- `MP-CONTEXT-CHARACTERIZATION-001` 是第六个 F-011 package：Bool 片段上下文等价完整刻画（C-89–C-91，`≡c` = 代表相等）；final run `20260912-MP-CONTEXT-CHARACTERIZATION-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`。\n- `MP-GUARD-ERASURE-001` 是第七个 F-011 package：阶段擦除 ⇔ 不动点存在（C-92–C-95）；final run `20260912-MP-GUARD-ERASURE-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`。",
    )
    memory = sub_once(
        memory,
        "`A-CONTEXT-CHARACTERIZATION-FORMAL-001`。partiality 片段已完全闭合（边界 + 单子 + 完整刻画）；下一步转 guard-erasure 第一机器构造，不直接跳 ERCF-3。",
        "`A-CONTEXT-CHARACTERIZATION-FORMAL-001`、`A-GUARD-ERASURE-FORMAL-001`。partiality 与 guard-erasure 两条支线均已闭合为机器判据；下一步转同函数异时（cost）第一机器构造，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S038 完成 `MP-GUARD-ERASURE-001`（C-92–C-95）：显式阶段流演算 + 忘却翻译下，保更新律地擦除阶段 ⇔ 律有不动点（否定律被拒绝、常值/幂等律可构造、振荡轨道为见证）。下一工作包转为同函数异时（cost）第一机器构造；ERCF-3 仍等待自然 consumer。\n\n",
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
    if state.get("revision") != 37 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_37_AND_S037")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != ["C-92", "C-93", "C-94", "C-95"]
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
        f"HoTT/verification/runs/{RUN_ID}/RUN.json": sha(run_dir / "RUN.json"),
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": sha(run_dir / "index-row-manifest.json"),
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": sha(run_dir / "source-manifest.json"),
        AUDIT_DOC: sha(root / AUDIT_DOC),
    }

    expected_stale = {
        ("A-CONTEXT-CHARACTERIZATION-FORMAL-001", MATRIX),
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

    row_stable_note = "After C-92 through C-95 were appended (S038), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "A-RACE-TIMEOUT-FORMAL-001",
        "A-CONTEXTUAL-EQUIV-FORMAL-001",
        "A-QUOTIENT-MONAD-FORMAL-001",
        "A-CONTEXT-CHARACTERIZATION-FORMAL-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S038 added the guard-erasure equivalence (C-92–C-95); the economy question now has a second machine判据 (erasure ⇔ fixed point). C4 text is unchanged and the remaining items stay open."

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S038 appended the guard-erasure package; all seven proof packages re-validated (six row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S038 appended the guard-erasure package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-022"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the guard-erasure equivalence: erasure-while-keeping-the-law holds iff the law has a fixed point; the first work package switches to the same-function-different-time (cost) machine construction."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-022"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the guard-erasure equivalence C-92–C-95 alongside the partiality strand; the next strand is the cost factorization construction."
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
        "classification": "GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE",
        "proof_id": PROOF_ID,
        "claim_ids": ["C-92", "C-93", "C-94", "C-95"],
        "run_id": RUN_ID,
        "mathematical_status": "STAGE_ERASURE_WITH_KEPT_LAW_IFF_FIXED_POINT_EXISTS",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [
            SOURCE,
            SOURCE_README,
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
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0; source, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX,
                "scripts/audit/verify_formal_proof_run.py",
                AUDIT_DOC,
            ],
        },
        "scope": "Native Cubical Agda guard/stage-erasure equivalence with an explicit staged-stream source calculus and an explicit forgetful translation: collapse + kept update law implies a fixed point (C-92), any fixed point yields such a collapse (C-94); the negation law admits none (C-93) and the oscillating orbit is the concrete witness (C-95). Not a HoTT paradox; no guarded/clocked completeness claim.",
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
            "scripts/audit/prepare_guard_erasure_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_GUARD_ERASURE_EQUIVALENCE",
        "cognition_status": "GUARD_ERASURE_EQUIVALENCE_PROVED_AND_COST_PACKAGE_ROUTED",
        "scope": "Run the guard-erasure work package natively (C-92–C-95), revalidate the six older packages row-stable, and route the same-function-different-time (cost) machine construction as the next package.",
    }

    state["revision"] = 38
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, fix a tiny program syntax with an evaluation relation and a step-cost function; prove that the bare extensional function cannot recover the cost (non-factorization) while an explicit cost-refined representation can (positive control); then audit whether a natural consumer demands budgeted delivery from the bare function.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-92", "C-93", "C-94", "C-95"],
        "final_run": {
            "run_id": RUN_ID,
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "older_proofs_after_matrix_growth": {
            rid: "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH"
            for rid in (
                "20260912-MP-ERCF-001-02",
                "20260912-MP-ERCF-TRUNC-001-01",
                "20260912-MP-RACE-TIMEOUT-001-01",
                "20260912-MP-CONTEXTUAL-EQUIV-001-01",
                "20260912-MP-QUOTIENT-MONAD-001-01",
                "20260912-MP-CONTEXT-CHARACTERIZATION-001-01",
            )
        },
        "stale_source_hash_repair": {"observed": 14, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 38",
            "projection freshness PASS (27 directions / 34 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 38",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE",
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
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved guard-erasure equivalence (C-92–C-95), repairs the fourteen stale source hashes, applies the projection text updates, and routes the cost work package. No Git commit, tag or push.",
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
        "revision": 38,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
