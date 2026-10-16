#!/usr/bin/env python3
"""Prepare revision 39: record MP-COST-FACTORIZATION-001 and route R034.

The run machine-proves the first same-function/different-time instance
(C-96–C-99): extensional equality via funext, non-recoverability of cost from
the bare function, and the cost-refined positive control. The checkpoint
records the result and session, applies the projection text updates, repairs
the fifteen stale source hashes, and moves the projections to revision 39
with the R034 native path-certificate check next.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-039-COST-FACTORIZATION"
PREV_SESSION = "S-RES-20260912-038-GUARD-ERASURE"
RESULT_ID = "A-COST-FACTORIZATION-FORMAL-001"
PROOF_ID = "MP-COST-FACTORIZATION-001"
RUN_ID = "20260912-MP-COST-FACTORIZATION-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/CostFactorization.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/CostFactorization.README.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/cost-factorization机器证明实施证据-20260912.md"
NEW_STATUS = "COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_cost_factorization", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "本轮把第一候选（同函数异时）做成机器实例：外延相同、成本不可恢复——这正是“理论推演出的现实反差”的标准形状，且不是内部矛盾。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 cost 支线上具体化：裸函数表示不携带成本资格，任何只依赖它的成本 consumer 都不存在。"),
        "KC-000013": ("DEEPENED", "“省略现实因素换取工具性”在 cost 表示上被精确化：省略执行时间后，成本恢复被 funext 等式排除。"),
        "KC-000014": ("ALIGNED", "方向 B 的判别工具获得 cost 实例：函数层面的存在/分类不等于按期交付能力。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0 且 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在 cost 支线推进；结论是表示限制 + 正控制，不是悖论。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”在 cost 上被具体化：时序/成本信息一旦被函数外延性商去，就无法从裸函数恢复。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”在 cost 上再次具体化：丢掉执行成本正是经济收益，代价是成本 consumer 不存在。"),
        "KC-000031": ("ALIGNED", "HoTT 的等式原则（funext）给出精确的表示限制，而非 coverage failure；细化表示可恢复。"),
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
            ("NOT_TOUCHED", "本轮聚焦同函数异时的 cost 实例与表示限制；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S039/SESSION.md；核心认知.md `{unit['id']}` | R034 原生核查、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — `DIR-L-SAME-FUNCTION-DIFFERENT-TIME` 闭合为机器实例（`C-96`–`C-99`）；第一工作包转为 R034 path-certificate 原生核查；revision 39/generation 023。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-COST-FACTORIZATION`（`NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`）。",
        "- update_decision: `MP-COST-FACTORIZATION-001 进入 formal/run/index/STATE；C-96–C-99 进入 claim matrix；八个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 八个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `R034 核查、更深 cost 语义、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S038 方向更新后的第一工作包（同函数异时 cost 第一机器构造）。",
        "- 构造：小程序语法 `Prog = fast | slow k`、语法导向成本 `cost`、裸表示 `fun`、细化表示 `refine`；不可区分性用 funext 路径 + transport；成本恢复 no-go 作为谓词实例。",
        "- 结果：`MP-COST-FACTORIZATION-001`（C-96–C-99）通过 kernel：外延相同而成本不同；裸函数上不存在可区分谓词；无从裸函数恢复成本的 consumer；细化表示可恢复/可区分。判词 `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`（非悖论）。",
        "- 运行：final run `20260912-MP-COST-FACTORIZATION-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。",
        "- 旧证据：矩阵第六次增长后，七个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：`¬` 本地定义一处机械修正；命题未削弱。",
        "- 边界：成本是明示语法导向计数；不主张真实编译器/硬件成本、原创性；natural consumer 仍为开放 Gate。",
        "- 三件套：direction/panorama revision 39/generation 023；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ]
    return "\n".join(lines)


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT`",
        "状态：`CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 38", "source_state_revision: 39")
    direction = sub_once(direction, "projection_generation: 20260912-direction-022", "projection_generation: 20260912-direction-023")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT",
        "semantic_status: CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE`、`OUT-W-R041-PAPER`",
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION`、`OUT-W-R041-PAPER`",
    )
    direction = sub_once(
        direction,
        "；下一步转同函数异时（cost）第一机器构造（程序语法/求值/成本 + 裸函数非因子化 + 显式成本表示正例），再寻找自然 consumer 桥梁",
        "；下一步做 R034 path-certificate 原生核查（Cubical Path/transport 正例 + no-selector 边界），再寻找自然 consumer 桥梁",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE` | partiality 片段与 guard-erasure 支线的正反结构已完全闭合",
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION` | partiality、guard-erasure 与 cost 支线的正反结构已完全闭合",
    )
    direction = sub_once(direction, "C4；六个 proof packages", "C4；七个 proof packages")
    direction = sub_once(
        direction,
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE` | partiality 片段与 guard-erasure 支线已形成完整的正反结构（商可分裂且单子成立；上下文等价严格保留时序；race/deadline 不可下降），仍未产生现实相对悖论；下一步转 guard-erasure 第一机器构造寻找新的现实相对实例",
        "、`OUT-TOP-CONTEXT-CHARACTERIZATION`、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION` | partiality、guard-erasure 与 cost 支线已形成完整的正反结构（含表示限制与细化正控制），仍未产生现实相对悖论；下一步做 R034 path-certificate 原生核查寻找新的现实相对实例",
    )
    direction = sub_once(
        direction,
        "| `DIR-L-SAME-FUNCTION-DIFFERENT-TIME` | 同一外延函数的不同实现具有不同时间/资源成本 | LocalGPT current owner | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `HOTT_OBJECT` | `OUT-L-TIME-BOUNDARY`（一手 cost-aware 支持）；形式化未完成 | 第一机器构造：固定 program/semantics/cost 与实现 identity，用同一 Cubical 工具链证明裸函数表示不可恢复成本（非因子化）与显式成本表示的充分性（正例） |",
        "| `DIR-L-SAME-FUNCTION-DIFFERENT-TIME` | 同一外延函数的不同实现具有不同时间/资源成本 | LocalGPT current owner | `CLOSED_WITH_SCOPE` | `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `HOTT_OBJECT` | `OUT-L-TIME-BOUNDARY`（一手 cost-aware 支持）、`OUT-TOP-COST-FACTORIZATION`（机器化 C-96–C-99） | 第一机器构造已闭合：funext 使外延相等，裸函数上无谓词可区分两程序，成本恢复 consumer 不存在；细化表示可恢复（正控制）；更深（真实编译器/资源语义）作为未来细化 |",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-PATH-CERTIFICATE` | path-indexed closed certificate、`¬MereMove` 与实际迁移环境的关系 | WebGPT `P-PATH-CERTIFICATE-034`；用户提供同 SHA Web 展示文件 | `SUPPORTING_DIRECTION` | `HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY`, `EVIDENCE_DISCIPLINE` | `OUT-W-TRANSPORT-REFLECTION`、`OUT-TOP-DIRECTION-PARADOX-REVIEW` | 以真实 Cubical Agda Path/Univalence/Truncation 完成原生核查并保留固定 Bool 对、实际路径 transport 正例；普通 Lean Eq 不替代 |",
        "| `DIR-W-PATH-CERTIFICATE` | path-indexed closed certificate、`¬MereMove` 与实际迁移环境的关系 | WebGPT `P-PATH-CERTIFICATE-034`；用户提供同 SHA Web 展示文件 | `NEXT_CANDIDATE` | `HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY`, `EVIDENCE_DISCIPLINE` | `OUT-W-TRANSPORT-REFLECTION`、`OUT-TOP-DIRECTION-PARADOX-REVIEW` | 以真实 Cubical Agda Path/Univalence/Truncation 完成 R034 原生核查：固定 Bool 对与同 SHA certificate 正例、no-selector 边界；普通 Lean Eq 不替代 |",
    )
    direction = sub_once(
        direction,
        "；`MP-GUARD-ERASURE-001` 原生证明阶段擦除与不动点存在的等价（`C-92`–`C-95`）。",
        "；`MP-GUARD-ERASURE-001` 原生证明阶段擦除与不动点存在的等价（`C-92`–`C-95`）；`MP-COST-FACTORIZATION-001` 原生证明同函数异时的表示限制与细化正控制（`C-96`–`C-99`）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：同函数异时（cost）第一机器构造——固定程序语法/求值与成本，证明裸函数表示不可恢复成本（非因子化必要方向），再给出显式成本表示的充分性正例；随后评估自然 consumer。",
        "4. **当前第一工作包**：R034 path-certificate 原生核查——用真实 Cubical Agda Path/Univalence/Truncation 固定 Bool 对与 transport 正例，核 certificate/no-selector 边界；普通 Lean Eq 不替代。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT`",
        "状态：`CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 38", "source_state_revision: 39")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-022", "projection_generation: 20260912-outcome-023")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_GUARD_ERASURE_EQUIVALENCE_PROVED_COST_FACTORIZATION_NEXT",
        "semantic_status: CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT",
    )
    new_row = (
        "| `OUT-TOP-COST-FACTORIZATION` | `MP-COST-FACTORIZATION-001`：同函数异时第一机器实例——`fast`/`slow k` 外延相同成本不同（`C-96`）、裸函数上无可区分谓词（`C-97`）、成本恢复 consumer 不存在（`C-98`）、细化表示可恢复（`C-99`） |"
        " `DIR-L-SAME-FUNCTION-DIFFERENT-TIME`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；不可区分性由 funext 路径 + transport 给出 |"
        " 成本为明示语法导向计数；不主张真实编译器/硬件成本、原创性或自然 consumer |"
        " `HoTT/formal/partiality-race-timeout/CostFactorization.agda`；final run `20260912-MP-COST-FACTORIZATION-001-01`；claim matrix C-96–C-99；`audit/cost-factorization机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", new_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "、上下文等价完整刻画与 guard-erasure 等价判据已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`）。同函数异时（cost）、guarded/clocked 翻译、自然 consumer、",
        "、上下文等价完整刻画、guard-erasure 等价判据与同函数异时 cost 实例已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` / `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`）。R034 原生核查、更深 cost 语义、自然 consumer、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "`MP-GUARD-ERASURE-001` 证明阶段擦除与不动点存在的等价；六者都不是 HoTT 悖论。",
        "`MP-GUARD-ERASURE-001` 证明阶段擦除与不动点存在的等价；`MP-COST-FACTORIZATION-001` 给出同函数异时的表示限制与细化正控制；七者都不是 HoTT 悖论。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | 同函数异时（cost）第一机器构造 | next-candidate / same Cubical toolchain | 固定程序语法/求值与成本；证明裸函数表示不可恢复成本（非因子化），并给出显式成本表示的充分性正例 |",
        "| 已闭合工作包 6 | 同函数异时 cost 实例（`C-96`–`C-99`） | machine-proved-local-uncommitted / `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` | funext 使外延相等；裸函数无谓词可区分；细化表示可恢复（正控制） |\n"
        "| 第一工作包 | R034 path-certificate 原生核查 | next-candidate / same Cubical toolchain | 固定 Bool 对与 transport 正例，核 certificate/no-selector 边界；普通 Lean Eq 不替代 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "1. `MP-GUARD-ERASURE-001` 完成 guard/stage 擦除等价判据：C-92–C-95 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`；保律地擦除阶段 ⇔ 律有不动点（否定律被拒绝、常值/幂等律可构造）。\n2. 当前第一数学工作包转为同函数异时（cost）第一机器构造：固定程序语法/求值与成本，证明裸函数表示不可恢复成本，并给出显式成本表示的充分性正例。",
        "1. `MP-COST-FACTORIZATION-001` 完成同函数异时第一机器实例：C-96–C-99 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`；funext 使外延相等，裸函数上无谓词可区分、成本不可恢复，细化表示可恢复。\n2. 当前第一数学工作包转为 R034 path-certificate 原生核查：用真实 Cubical Path/Univalence/Truncation 固定 Bool 对与 transport 正例，核 certificate/no-selector 边界。",
    )
    memory = sub_once(
        memory,
        "- `MP-GUARD-ERASURE-001` 是第七个 F-011 package：阶段擦除 ⇔ 不动点存在（C-92–C-95）；final run `20260912-MP-GUARD-ERASURE-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`。",
        "- `MP-GUARD-ERASURE-001` 是第七个 F-011 package：阶段擦除 ⇔ 不动点存在（C-92–C-95）；final run `20260912-MP-GUARD-ERASURE-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`。\n- `MP-COST-FACTORIZATION-001` 是第八个 F-011 package：同函数异时实例与表示限制（C-96–C-99）；final run `20260912-MP-COST-FACTORIZATION-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`。",
    )
    memory = sub_once(
        memory,
        "`A-CONTEXT-CHARACTERIZATION-FORMAL-001`、`A-GUARD-ERASURE-FORMAL-001`。partiality 与 guard-erasure 两条支线均已闭合为机器判据；下一步转同函数异时（cost）第一机器构造，不直接跳 ERCF-3。",
        "`A-CONTEXT-CHARACTERIZATION-FORMAL-001`、`A-GUARD-ERASURE-FORMAL-001`、`A-COST-FACTORIZATION-FORMAL-001`。partiality、guard-erasure 与 cost 三条支线均已闭合为机器判据；下一步做 R034 path-certificate 原生核查，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S039 完成 `MP-COST-FACTORIZATION-001`（C-96–C-99）：同函数异时第一机器实例——funext 使外延相等，裸函数上无谓词可区分、成本不可恢复，细化表示可恢复（正控制）。下一工作包转为 R034 path-certificate 原生核查；ERCF-3 仍等待自然 consumer。\n\n",
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
    if state.get("revision") != 38 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_38_AND_S038")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != ["C-96", "C-97", "C-98", "C-99"]
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
        ("A-GUARD-ERASURE-FORMAL-001", MATRIX),
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

    row_stable_note = "After C-96 through C-99 were appended (S039), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "A-RACE-TIMEOUT-FORMAL-001",
        "A-CONTEXTUAL-EQUIV-FORMAL-001",
        "A-QUOTIENT-MONAD-FORMAL-001",
        "A-CONTEXT-CHARACTERIZATION-FORMAL-001",
        "A-GUARD-ERASURE-FORMAL-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S039 added the cost-factorization instance (C-96–C-99); the economy question now has a cost-side machine instance with a refinement positive control. C4 text is unchanged and the remaining items stay open."

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S039 appended the cost-factorization package; all eight proof packages re-validated (seven row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S039 appended the cost-factorization package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-023"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the cost instance: extensional equality hides cost and the refined representation recovers it; the first work package switches to the R034 native path-certificate check."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-023"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the cost-factorization instance C-96–C-99 alongside the partiality and guard strands; the next strand is the R034 native check."
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
        "classification": "NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL",
        "proof_id": PROOF_ID,
        "claim_ids": ["C-96", "C-97", "C-98", "C-99"],
        "run_id": RUN_ID,
        "mathematical_status": "BARE_FUNCTION_CANNOT_RECOVER_COST_REFINED_REPRESENTATION_CAN",
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
        "scope": "Native Cubical Agda cost instance: fast and slow k share the extensional function (funext) but differ in syntax-directed cost (C-96); no predicate on the bare function type distinguishes extensionally equal programs (C-97); no consumer recovers the cost value from the bare function (C-98); the cost-refined representation recovers and separates (C-99). Representation limit with positive control; not a HoTT paradox.",
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
            "scripts/audit/prepare_cost_factorization_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_COST_FACTORIZATION",
        "cognition_status": "COST_FACTORIZATION_PROVED_AND_R034_CHECK_ROUTED",
        "scope": "Run the cost-factorization work package natively (C-96–C-99), revalidate the seven older packages row-stable, and route the R034 native path-certificate check as the next package.",
    }

    state["revision"] = 39
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, fix a Bool pair and perform the R034 native check: closed certificate/transport positive control with real Cubical Path (and Univalence/Truncation where needed), plus the no-selector boundary; ordinary Lean Eq does not substitute.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-96", "C-97", "C-98", "C-99"],
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
                "20260912-MP-GUARD-ERASURE-001-01",
            )
        },
        "stale_source_hash_repair": {"observed": 15, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 39",
            "projection freshness PASS (27 directions / 35 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 39",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL",
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
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved cost-factorization instance (C-96–C-99), repairs the fifteen stale source hashes, applies the projection text updates, and routes the R034 native check. No Git commit, tag or push.",
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
        "revision": 39,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
