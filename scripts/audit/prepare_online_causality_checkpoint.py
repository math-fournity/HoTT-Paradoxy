#!/usr/bin/env python3
"""Prepare revision 41: record MP-ONLINE-CAUSALITY-001 and route the C5 synthesis.

The run machine-proves the online-causality boundary (C-106–C-109): no
time-0 lookahead, positive controls for reading the first input at time 0 and
the second from time 1, and the knowledge gap between complete stream
functions and online strategies. The checkpoint records the result and
session, applies the projection text updates, repairs the seventeen stale
source hashes, and moves the projections to revision 41 with the C5
synthesis (paradox-distance assessment over the ten machine packages) next.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-041-ONLINE-CAUSALITY"
PREV_SESSION = "S-RES-20260912-040-PATH-CERTIFICATE"
RESULT_ID = "A-ONLINE-CAUSALITY-FORMAL-001"
PROOF_ID = "MP-ONLINE-CAUSALITY-001"
RUN_ID = "20260912-MP-ONLINE-CAUSALITY-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/OnlineCausality.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/OnlineCausality.README.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/online-causality机器证明实施证据-20260912.md"
NEW_STATUS = "ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_online_causality", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "在线因果边界是「现实可完成/理论额外困难」框架中的表示/资格边界，不是内部矛盾。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在在线模型上具体化：时刻 0 的策略拿不到未来输入，这不是运行太慢，而是资格不足。"),
        "KC-000013": ("DEEPENED", "“省略时序”在在线模型中被精确化：完整流函数可以读未来，按序策略不可以。"),
        "KC-000014": ("ALIGNED", "方向 B 的工具再获实例：完整知识版本可构造，不等于在线交付资格存在。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0、零警告且 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在在线因果支线推进；结论是边界 + 正控制。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”在在线接口上被具体化：时间索引结构直接决定可行策略类。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”再次具体化：忘掉到达顺序换取简洁表示，代价是时刻 0 的前视能力不存在。"),
        "KC-000031": ("ALIGNED", "边界来自建模事实而非人为合同；正控制表明并非所有在线任务都不可行。"),
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
            ("NOT_TOUCHED", "本轮聚焦在线因果资格边界；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S041/SESSION.md；核心认知.md `{unit['id']}` | C5 综合、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — `DIR-L-TIME-WORK-DIMENSION` 闭合为在线因果边界（`C-106`–`C-109`）；第一工作包转为 C5 综合评估；revision 41/generation 025。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-ONLINE-CAUSALITY`（`ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`）。",
        "- update_decision: `MP-ONLINE-CAUSALITY-001 进入 formal/run/index/STATE；C-106–C-109 进入 claim matrix；十个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `C5 综合、natural consumer、R036/R038 原生升级、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S040 方向更新后的第一工作包（在线因果资格第一机器构造）。",
        "- 构造：`Stream := ℕ → Bool`；前缀为嵌套对（`Prefix zero = Bool`，`Prefix (suc n) = Bool × Prefix n`）；在线策略 `(n) → Prefix n → Bool`；完整流函数 `Stream → Bool`。",
        "- 结果：`MP-ONLINE-CAUSALITY-001`（C-106–C-109）通过 kernel：时刻 0 无前视；读第一个输入（时刻 0）与读第二个输入（时刻 1 起）两个正例；完整知识 ≠ 在线资格。判词 `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`（非悖论）。",
        "- 运行：final run `20260912-MP-ONLINE-CAUSALITY-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`），零警告。",
        "- 旧证据：矩阵第八次增长后，九个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：初版 Fin 索引前缀触发 `UnsupportedIndexedMatch` 警告；改为嵌套对前缀后零警告通过，命题未削弱。",
        "- 边界：不主张物理时间、HoTT 独有或 guarded/clocked 完整翻译；正控制说明并非所有在线任务不可行。",
        "- 三件套：direction/panorama revision 41/generation 025；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ]
    return "\n".join(lines)


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT`",
        "状态：`CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 40", "source_state_revision: 41")
    direction = sub_once(direction, "projection_generation: 20260912-direction-024", "projection_generation: 20260912-direction-025")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT",
        "semantic_status: CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE`、`OUT-W-R041-PAPER`",
        "、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE`、`OUT-TOP-ONLINE-CAUSALITY`、`OUT-W-R041-PAPER`",
    )
    direction = sub_once(
        direction,
        "；下一步做在线因果资格第一机器构造（guarded/online 接口：完整流函数 vs 只读已到达输入的策略），再寻找自然 consumer 桥梁",
        "；下一步做 C5 综合评估（从十个机器结果评估悖论距离、剩余候选与自然 consumer 审计），再决定是否启动 ERCF-3 或 W51×RP-B01",
    )
    direction = sub_once(
        direction,
        "| `DIR-L-TIME-WORK-DIMENSION` | 理论自身的工作层时间：对象时间、弱 reduction、强内生时态、在线因果资格和物理时间分层 | LocalGPT；WebGPT `C-TIME-*`；本轮 C1 复审 | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `THEORY_SCHEMA` | `OUT-L-TIME-BOUNDARY`、`OUT-W-TEMPORAL-TRANSPORT`、`OUT-TOP-DIRECTION-PARADOX-REVIEW` | 第一机器构造：固定 guarded/online 接口，区分完整流函数与只读已到达输入的策略；证明一个在线资格边界并给出可在线完成的正例；若只剩预知未来的人为合同则停止 |",
        "| `DIR-L-TIME-WORK-DIMENSION` | 理论自身的工作层时间：对象时间、弱 reduction、强内生时态、在线因果资格和物理时间分层 | LocalGPT；WebGPT `C-TIME-*`；本轮 C1 复审 | `CLOSED_WITH_SCOPE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `THEORY_SCHEMA` | `OUT-L-TIME-BOUNDARY`、`OUT-W-TEMPORAL-TRANSPORT`、`OUT-TOP-DIRECTION-PARADOX-REVIEW`、`OUT-TOP-ONLINE-CAUSALITY`（C-106–C-109） | 在线因果边界已闭合：时刻 0 无前视、两个分时刻正例、完整知识 ≠ 在线资格；guarded/clocked 完整翻译与物理时间保留为未来细化 |",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE` | partiality、guard-erasure、cost 与路径证书支线的正反结构已完全闭合",
        "、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE`、`OUT-TOP-ONLINE-CAUSALITY` | partiality、guard-erasure、cost、路径证书与在线因果支线的正反结构已完全闭合",
    )
    direction = sub_once(direction, "C4；八个 proof packages", "C4；九个 proof packages")
    direction = sub_once(
        direction,
        "、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE` | partiality、guard-erasure、cost 与路径证书支线已形成完整的正反结构（含表示限制、细化正控制与统一迁移非栖居），仍未产生现实相对悖论；下一步做在线因果资格第一机器构造寻找新的现实相对实例",
        "、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE`、`OUT-TOP-ONLINE-CAUSALITY` | partiality、guard-erasure、cost、路径证书与在线因果支线已形成完整的正反结构（含表示限制、细化正控制、统一迁移非栖居与在线资格边界），仍未产生现实相对悖论；下一步做 C5 综合评估统筹剩余候选",
    )
    direction = sub_once(
        direction,
        "；`MP-PATH-CERTIFICATE-001` 原生核查 R034 路径证书边界（`C-100`–`C-105`：MereMove 非栖居 + 路径正例）。",
        "；`MP-PATH-CERTIFICATE-001` 原生核查 R034 路径证书边界（`C-100`–`C-105`：MereMove 非栖居 + 路径正例）；`MP-ONLINE-CAUSALITY-001` 原生给出在线因果资格边界（`C-106`–`C-109`）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：在线因果资格第一机器构造——固定 guarded/online 接口（完整流函数 vs 只读已到达输入的策略），证明一个在线资格边界并给出可在线完成的正例；若只剩预知未来的人为合同则停止。",
        "4. **当前第一工作包**：C5 综合评估——从十个机器结果（MP-ERCF-001、MP-ERCF-TRUNC-001、MP-RACE-TIMEOUT-001、MP-CONTEXTUAL-EQUIV-001、MP-QUOTIENT-MONAD-001、MP-CONTEXT-CHARACTERIZATION-001、MP-GUARD-ERASURE-001、MP-COST-FACTORIZATION-001、MP-PATH-CERTIFICATE-001、MP-ONLINE-CAUSALITY-001）评估当前「悖论距离」、列出剩余候选与自然 consumer 审计结论，统筹是否启动 ERCF-3/W51×RP-B01 或 R036/R038 原生升级。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT`",
        "状态：`CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 40", "source_state_revision: 41")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-024", "projection_generation: 20260912-outcome-025")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT",
        "semantic_status: CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT",
    )
    new_row = (
        "| `OUT-TOP-ONLINE-CAUSALITY` | `MP-ONLINE-CAUSALITY-001`：在线因果资格边界——时刻 0 无前视（`C-106`）、读第一个输入（`C-107`）与自时刻 1 读第二个输入（`C-108`）的正例、完整知识 ≠ 在线资格（`C-109`） |"
        " `DIR-L-TIME-WORK-DIMENSION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-A-REALITY-RELATIVE`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0（零警告）、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH` |"
        " 不主张物理时间、HoTT 独有或 guarded/clocked 完整翻译；不证明所有在线任务不可完成 |"
        " `HoTT/formal/partiality-race-timeout/OnlineCausality.agda`；final run `20260912-MP-ONLINE-CAUSALITY-001-01`；claim matrix C-106–C-109；`audit/online-causality机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", new_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "、同函数异时 cost 实例与 R034 路径证书原生核查已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` / `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` / `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`）。在线因果、R032 回放、更深 cost 语义、自然 consumer、",
        "、同函数异时 cost 实例、R034 路径证书原生核查与在线因果边界已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` / `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` / `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS` / `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`）。C5 综合评估、R036/R038 原生升级、R032 回放、自然 consumer、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "`MP-PATH-CERTIFICATE-001` 原生核查 R034 路径证书边界（MereMove 非栖居 + 路径正例）；八者都不是 HoTT 悖论。",
        "`MP-PATH-CERTIFICATE-001` 原生核查 R034 路径证书边界（MereMove 非栖居 + 路径正例）；`MP-ONLINE-CAUSALITY-001` 给出在线因果资格边界（时刻 0 无前视 + 分时刻正例）；九者都不是 HoTT 悖论。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | 在线因果资格第一机器构造 | next-candidate / same Cubical toolchain | 固定 guarded/online 接口（完整流函数 vs 只读已到达输入的策略）；证明在线资格边界并给出可在线完成正例 |",
        "| 已闭合工作包 8 | 在线因果资格边界（`C-106`–`C-109`） | machine-proved-local-uncommitted / `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS` | 时刻 0 无前视；读第一个输入与自时刻 1 读第二个输入的正例；完整知识 ≠ 在线资格 |\n"
        "| 第一工作包 | C5 综合评估（悖论距离与剩余候选） | synthesis / paper-only | 从十个机器结果评估当前悖论距离、列出剩余候选与自然 consumer 审计结论；统筹 ERCF-3/W51×RP-B01 与 R036/R038 原生升级 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "1. `MP-PATH-CERTIFICATE-001` 完成 R034 路径证书原生核查：C-100–C-105 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`；固定端点与路径版迁移可构造，全宇宙统一迁移（MereMove）非栖居（Σ回路 + 依赖运输，构造性反证）。\n2. 当前第一数学工作包转为在线因果资格第一机器构造：固定 guarded/online 接口（完整流函数 vs 只读已到达输入的策略），证明在线资格边界并给出可在线完成的正例。",
        "1. `MP-ONLINE-CAUSALITY-001` 完成在线因果资格边界：C-106–C-109 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`；时刻 0 无前视；读第一个输入（时刻 0）与读第二个输入（时刻 1 起）为正例；完整知识 ≠ 在线资格。\n2. 当前第一工作包转为 C5 综合评估：从十个机器结果评估悖论距离、剩余候选与自然 consumer 审计，统筹 ERCF-3/W51×RP-B01 与 R036/R038 原生升级。",
    )
    memory = sub_once(
        memory,
        "- `MP-PATH-CERTIFICATE-001` 是第九个 F-011 package：R034 路径证书边界原生核查（C-100–C-105）；final run `20260912-MP-PATH-CERTIFICATE-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`。",
        "- `MP-PATH-CERTIFICATE-001` 是第九个 F-011 package：R034 路径证书边界原生核查（C-100–C-105）；final run `20260912-MP-PATH-CERTIFICATE-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`。\n- `MP-ONLINE-CAUSALITY-001` 是第十个 F-011 package：在线因果资格边界（C-106–C-109，零警告）；final run `20260912-MP-ONLINE-CAUSALITY-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`。",
    )
    memory = sub_once(
        memory,
        "`A-PATH-CERTIFICATE-FORMAL-001`。partiality、guard-erasure、cost 与路径证书四条支线均已闭合为机器判据；下一步做在线因果资格第一机器构造，不直接跳 ERCF-3。",
        "`A-PATH-CERTIFICATE-FORMAL-001`、`A-ONLINE-CAUSALITY-FORMAL-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；下一步做 C5 综合评估统筹剩余候选，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S041 完成 `MP-ONLINE-CAUSALITY-001`（C-106–C-109）：在线因果资格边界——时刻 0 无前视；读第一个输入（时刻 0）与读第二个输入（自时刻 1）为正例；完整知识 ≠ 在线资格。下一工作包转为 C5 综合评估（十个机器结果的悖论距离与剩余候选）；ERCF-3 仍等待自然 consumer。\n\n",
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
    if state.get("revision") != 40 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_40_AND_S040")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(106, 110)]
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
        ("A-COST-FACTORIZATION-FORMAL-001", MATRIX),
        ("A-ERCF-FACTORIZATION-FORMAL-001", MATRIX),
        ("A-ERCF-TRUNCATION-DEFENSE-001", MATRIX),
        ("A-GUARD-ERASURE-FORMAL-001", MATRIX),
        ("A-HOTT-SELF-VALIDATION-ECONOMY-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", FORMAL_README),
        ("A-MATH-PROOF-DELIVERY-GATE-001", RUNS_README),
        ("A-PATH-CERTIFICATE-FORMAL-001", MATRIX),
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

    row_stable_note = "After C-106 through C-109 were appended (S041), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "A-RACE-TIMEOUT-FORMAL-001",
        "A-CONTEXTUAL-EQUIV-FORMAL-001",
        "A-QUOTIENT-MONAD-FORMAL-001",
        "A-CONTEXT-CHARACTERIZATION-FORMAL-001",
        "A-GUARD-ERASURE-FORMAL-001",
        "A-COST-FACTORIZATION-FORMAL-001",
        "A-PATH-CERTIFICATE-FORMAL-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S041 added the online-causality boundary (C-106–C-109): complete knowledge versus online qualification. C4 text is unchanged and the remaining items stay open."

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S041 appended the online-causality package; all ten proof packages re-validated (nine row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S041 appended the online-causality package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-025"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the online-causality boundary: five machine strands are closed; the first work package is the C5 synthesis assessing the paradox distance over the ten packages."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-025"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the online-causality boundary C-106–C-109; the next strand is the C5 synthesis."
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
        "classification": "ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(106, 110)],
        "run_id": RUN_ID,
        "mathematical_status": "COMPLETE_KNOWLEDGE_VERSUS_ONLINE_QUALIFICATION_SEPARATED",
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
            "reason": "Final native Cubical run exited 0 with zero warnings; source, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX,
                "scripts/audit/verify_formal_proof_run.py",
                AUDIT_DOC,
            ],
        },
        "scope": "Native Cubical Agda online-causality boundary: no time-0 lookahead (C-106), reading the first input at time 0 (C-107) and the second from time 1 (C-108), and the knowledge gap between complete stream functions and online strategies (C-109). Boundary with positive controls; not a HoTT paradox; no physical-time claim.",
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
            "scripts/audit/prepare_online_causality_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_ONLINE_CAUSALITY",
        "cognition_status": "ONLINE_CAUSALITY_BOUNDARY_PROVED_AND_C5_SYNTHESIS_ROUTED",
        "scope": "Run the online-causality work package natively (C-106–C-109), revalidate the nine older packages row-stable, and route the C5 synthesis (paradox-distance assessment over the ten packages) as the next package.",
    }

    state["revision"] = 41
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "Read 理解章节/C1–C4, the ten machine packages and the direction/panorama projections; write C5 as a paper-only synthesis that assesses the current paradox distance, enumerates the remaining candidates (ERCF-3/W51×RP-B01, R036/R038 native upgrades, natural consumer audit) with explicit evidence boundaries, and does not upgrade any unproved claim.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(106, 110)],
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
                "20260912-MP-COST-FACTORIZATION-001-01",
                "20260912-MP-PATH-CERTIFICATE-001-01",
            )
        },
        "stale_source_hash_repair": {"observed": 17, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 41",
            "projection freshness PASS (27 directions / 37 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 41",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS",
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
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved online-causality boundary (C-106–C-109), repairs the seventeen stale source hashes, applies the projection text updates, and routes the C5 synthesis. No Git commit, tag or push.",
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
        "revision": 41,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
