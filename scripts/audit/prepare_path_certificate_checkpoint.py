#!/usr/bin/env python3
"""Prepare revision 40: record MP-PATH-CERTIFICATE-001 and route online causality.

The run natively verifies the R034 path-certificate boundary (C-100–C-105):
ua computation, truncation propositionality, the MereMove non-inhabitation
via a Sigma-loop with dependent transport, and the path-indexed positive
control. The checkpoint records the result and session, applies the
projection text updates, repairs the sixteen stale source hashes, and moves
the projections to revision 40 with the online-causality package next.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-040-PATH-CERTIFICATE"
PREV_SESSION = "S-RES-20260912-039-COST-FACTORIZATION"
RESULT_ID = "A-PATH-CERTIFICATE-FORMAL-001"
PROOF_ID = "MP-PATH-CERTIFICATE-001"
RUN_ID = "20260912-MP-PATH-CERTIFICATE-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/PathCertificate.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/PathCertificate.README.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/path-certificate机器证明实施证据-20260912.md"
NEW_STATUS = "PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_path_certificate", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "R034 原生核查再次给出边界（有路径可迁移、仅等价存在不可统一迁移），不是内部矛盾，符合“找现实相对非现实性”的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在路径证书上精确化：缺失的不是运行时间，而是理论上不存在的相干选择。"),
        "KC-000013": ("DEEPENED", "“把路径信息商去（截断）再要求统一迁移”被机器证明不可能——这就是该抽象的经济收益与代价。"),
        "KC-000014": ("ALIGNED", "方向 B 的判别工具获得 R034 实例：仅知道等价存在不等于拥有统一迁移或有效交付。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0 且 exact replay，且未用普通 Lean Eq 替代。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在路径证书支线推进；结论是边界判据而非悖论。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序/过程”在路径证书上被具体化：路径被截断后，统一迁移所需的相干选择不存在。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”再次具体化：把路径商成截断命题是收益，代价是统一迁移接口非栖居。"),
        "KC-000031": ("ALIGNED", "HoTT 的规则（截断消去限制、transport 需要实际路径）给出精确边界，不是 coverage failure。"),
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
            ("NOT_TOUCHED", "本轮聚焦 R034 路径证书边界的原生核查；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S040/SESSION.md；核心认知.md `{unit['id']}` | 在线因果、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — `DIR-W-PATH-CERTIFICATE` 闭合为原生核查（`C-100`–`C-105`）；第一工作包转为在线因果资格第一机器构造；revision 40/generation 024。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-PATH-CERTIFICATE`（`MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`）。",
        "- update_decision: `MP-PATH-CERTIFICATE-001 进入 formal/run/index/STATE；C-100–C-105 进入 claim matrix；九个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 九个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `在线因果、R032 证书语法回放、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S039 方向更新后的第一工作包（R034 path-certificate 原生核查）。",
        "- 构造：`notEquiv`/`loop := ua notEquiv`；`C := Σ[ Y ∈ Type ] ∥ Bool ≡ Y ∥₁` 与基点 `z₀`；`isProp→PathP` + `ΣPathP` 构造回路；反证用依赖截面 `s`、`fromPathP ω` 与 `uaβ`。",
        "- 结果：`MP-PATH-CERTIFICATE-001`（C-100–C-105）通过 kernel：ua 路径按 not 计算；截断命题性；固定端点接口存在；固定源统一变体与全宇宙 MereMove 非栖居；路径版接口存在。判词 `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`（非悖论）。",
        "- 运行：final run `20260912-MP-PATH-CERTIFICATE-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。",
        "- 旧证据：矩阵第七次增长后，八个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：宇宙层级（Type₁）与最终等式方向两处机械修正；命题未削弱。未使用普通 Lean Eq。",
        "- 边界：未实现 R032 证书语法回放，未处理 HoTT+选择关系，未主张原创性。",
        "- 三件套：direction/panorama revision 40/generation 024；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ]
    return "\n".join(lines)


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT`",
        "状态：`CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 39", "source_state_revision: 40")
    direction = sub_once(direction, "projection_generation: 20260912-direction-023", "projection_generation: 20260912-direction-024")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT",
        "semantic_status: CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION`、`OUT-W-R041-PAPER`",
        "、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE`、`OUT-W-R041-PAPER`",
    )
    direction = sub_once(
        direction,
        "；下一步做 R034 path-certificate 原生核查（Cubical Path/transport 正例 + no-selector 边界），再寻找自然 consumer 桥梁",
        "；下一步做在线因果资格第一机器构造（guarded/online 接口：完整流函数 vs 只读已到达输入的策略），再寻找自然 consumer 桥梁",
    )
    direction = sub_once(
        direction,
        "| `DIR-L-TIME-WORK-DIMENSION` | 理论自身的工作层时间：对象时间、弱 reduction、强内生时态、在线因果资格和物理时间分层 | LocalGPT；WebGPT `C-TIME-*`；本轮 C1 复审 | `CANDIDATE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `THEORY_SCHEMA` | `OUT-L-TIME-BOUNDARY`、`OUT-W-TEMPORAL-TRANSPORT`、`OUT-TOP-DIRECTION-PARADOX-REVIEW` | 选一个真实 guarded/clocked 接口，区分完整流函数与遵守输入到达顺序的在线策略；若只剩预知未来的人为合同则停止 |",
        "| `DIR-L-TIME-WORK-DIMENSION` | 理论自身的工作层时间：对象时间、弱 reduction、强内生时态、在线因果资格和物理时间分层 | LocalGPT；WebGPT `C-TIME-*`；本轮 C1 复审 | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `THEORY_SCHEMA` | `OUT-L-TIME-BOUNDARY`、`OUT-W-TEMPORAL-TRANSPORT`、`OUT-TOP-DIRECTION-PARADOX-REVIEW` | 第一机器构造：固定 guarded/online 接口，区分完整流函数与只读已到达输入的策略；证明一个在线资格边界并给出可在线完成的正例；若只剩预知未来的人为合同则停止 |",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-PATH-CERTIFICATE` | path-indexed closed certificate、`¬MereMove` 与实际迁移环境的关系 | WebGPT `P-PATH-CERTIFICATE-034`；用户提供同 SHA Web 展示文件 | `NEXT_CANDIDATE` | `HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY`, `EVIDENCE_DISCIPLINE` | `OUT-W-TRANSPORT-REFLECTION`、`OUT-TOP-DIRECTION-PARADOX-REVIEW` | 以真实 Cubical Agda Path/Univalence/Truncation 完成 R034 原生核查：固定 Bool 对与同 SHA certificate 正例、no-selector 边界；普通 Lean Eq 不替代 |",
        "| `DIR-W-PATH-CERTIFICATE` | path-indexed closed certificate、`¬MereMove` 与实际迁移环境的关系 | WebGPT `P-PATH-CERTIFICATE-034`；用户提供同 SHA Web 展示文件 | `CLOSED_WITH_SCOPE` | `HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY`, `EVIDENCE_DISCIPLINE` | `OUT-W-TRANSPORT-REFLECTION`、`OUT-TOP-DIRECTION-PARADOX-REVIEW`、`OUT-TOP-PATH-CERTIFICATE`（原生核查 C-100–C-105） | R034 核心边界已原生闭合：ua 计算、截断命题性、固定端点正例、MereMove 非栖居、路径版迁移正例；R032 证书语法回放与选择关系保留为未来细化 |",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION` | partiality、guard-erasure 与 cost 支线的正反结构已完全闭合",
        "、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE` | partiality、guard-erasure、cost 与路径证书支线的正反结构已完全闭合",
    )
    direction = sub_once(direction, "C4；七个 proof packages", "C4；八个 proof packages")
    direction = sub_once(
        direction,
        "、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION` | partiality、guard-erasure 与 cost 支线已形成完整的正反结构（含表示限制与细化正控制），仍未产生现实相对悖论；下一步做 R034 path-certificate 原生核查寻找新的现实相对实例",
        "、`OUT-TOP-GUARD-ERASURE`、`OUT-TOP-COST-FACTORIZATION`、`OUT-TOP-PATH-CERTIFICATE` | partiality、guard-erasure、cost 与路径证书支线已形成完整的正反结构（含表示限制、细化正控制与统一迁移非栖居），仍未产生现实相对悖论；下一步做在线因果资格第一机器构造寻找新的现实相对实例",
    )
    direction = sub_once(
        direction,
        "；`MP-COST-FACTORIZATION-001` 原生证明同函数异时的表示限制与细化正控制（`C-96`–`C-99`）。",
        "；`MP-COST-FACTORIZATION-001` 原生证明同函数异时的表示限制与细化正控制（`C-96`–`C-99`）；`MP-PATH-CERTIFICATE-001` 原生核查 R034 路径证书边界（`C-100`–`C-105`：MereMove 非栖居 + 路径正例）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：R034 path-certificate 原生核查——用真实 Cubical Agda Path/Univalence/Truncation 固定 Bool 对与 transport 正例，核 certificate/no-selector 边界；普通 Lean Eq 不替代。",
        "4. **当前第一工作包**：在线因果资格第一机器构造——固定 guarded/online 接口（完整流函数 vs 只读已到达输入的策略），证明一个在线资格边界并给出可在线完成的正例；若只剩预知未来的人为合同则停止。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT`",
        "状态：`CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 39", "source_state_revision: 40")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-023", "projection_generation: 20260912-outcome-024")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_COST_FACTORIZATION_PROVED_R034_NATIVE_CHECK_NEXT",
        "semantic_status: CORE_GENERATION_4_PATH_CERTIFICATE_PROVED_ONLINE_CAUSALITY_NEXT",
    )
    new_row = (
        "| `OUT-TOP-PATH-CERTIFICATE` | `MP-PATH-CERTIFICATE-001`：R034 路径证书边界的原生核查——`ua` 路径按 `not` 计算（`C-100`）、截断命题性（`C-101`）、固定端点接口存在（`C-102`）、固定源统一变体与全宇宙 `MereMove` 非栖居（`C-103`、`C-104`）、路径版迁移存在（`C-105`） |"
        " `DIR-W-PATH-CERTIFICATE`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；Σ回路 + 依赖运输给出构造性反证，未用普通 Lean Eq |"
        " 未实现 R032 证书语法回放；不证明 HoTT+选择不一致；不排除所有局部实例；不主张原创性 |"
        " `HoTT/formal/partiality-race-timeout/PathCertificate.agda`；final run `20260912-MP-PATH-CERTIFICATE-001-01`；claim matrix C-100–C-105；`audit/path-certificate机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", new_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "、guard-erasure 等价判据与同函数异时 cost 实例已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` / `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`）。R034 原生核查、更深 cost 语义、自然 consumer、",
        "、guard-erasure 等价判据、同函数异时 cost 实例与 R034 路径证书原生核查已机器闭合（`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` / `MONAD_STRUCTURE_CONSTRUCTED` / `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` / `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` / `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` / `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`）。在线因果、R032 回放、更深 cost 语义、自然 consumer、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "`MP-COST-FACTORIZATION-001` 给出同函数异时的表示限制与细化正控制；七者都不是 HoTT 悖论。",
        "`MP-COST-FACTORIZATION-001` 给出同函数异时的表示限制与细化正控制；`MP-PATH-CERTIFICATE-001` 原生核查 R034 路径证书边界（MereMove 非栖居 + 路径正例）；八者都不是 HoTT 悖论。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | R034 path-certificate 原生核查 | next-candidate / same Cubical toolchain | 固定 Bool 对与 transport 正例，核 certificate/no-selector 边界；普通 Lean Eq 不替代 |",
        "| 已闭合工作包 7 | R034 路径证书原生核查（`C-100`–`C-105`） | machine-proved-local-uncommitted / `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS` | ua 计算、截断命题性、MereMove 非栖居、路径版与固定端点正例；未用普通 Lean Eq |\n"
        "| 第一工作包 | 在线因果资格第一机器构造 | next-candidate / same Cubical toolchain | 固定 guarded/online 接口（完整流函数 vs 只读已到达输入的策略）；证明在线资格边界并给出可在线完成正例 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "1. `MP-COST-FACTORIZATION-001` 完成同函数异时第一机器实例：C-96–C-99 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`；funext 使外延相等，裸函数上无谓词可区分、成本不可恢复，细化表示可恢复。\n2. 当前第一数学工作包转为 R034 path-certificate 原生核查：用真实 Cubical Path/Univalence/Truncation 固定 Bool 对与 transport 正例，核 certificate/no-selector 边界。",
        "1. `MP-PATH-CERTIFICATE-001` 完成 R034 路径证书原生核查：C-100–C-105 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`；固定端点与路径版迁移可构造，全宇宙统一迁移（MereMove）非栖居（Σ回路 + 依赖运输，构造性反证）。\n2. 当前第一数学工作包转为在线因果资格第一机器构造：固定 guarded/online 接口（完整流函数 vs 只读已到达输入的策略），证明在线资格边界并给出可在线完成的正例。",
    )
    memory = sub_once(
        memory,
        "- `MP-COST-FACTORIZATION-001` 是第八个 F-011 package：同函数异时实例与表示限制（C-96–C-99）；final run `20260912-MP-COST-FACTORIZATION-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`。",
        "- `MP-COST-FACTORIZATION-001` 是第八个 F-011 package：同函数异时实例与表示限制（C-96–C-99）；final run `20260912-MP-COST-FACTORIZATION-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`。\n- `MP-PATH-CERTIFICATE-001` 是第九个 F-011 package：R034 路径证书边界原生核查（C-100–C-105）；final run `20260912-MP-PATH-CERTIFICATE-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`。",
    )
    memory = sub_once(
        memory,
        "`A-GUARD-ERASURE-FORMAL-001`、`A-COST-FACTORIZATION-FORMAL-001`。partiality、guard-erasure 与 cost 三条支线均已闭合为机器判据；下一步做 R034 path-certificate 原生核查，不直接跳 ERCF-3。",
        "`A-GUARD-ERASURE-FORMAL-001`、`A-COST-FACTORIZATION-FORMAL-001`、`A-PATH-CERTIFICATE-FORMAL-001`。partiality、guard-erasure、cost 与路径证书四条支线均已闭合为机器判据；下一步做在线因果资格第一机器构造，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S040 完成 `MP-PATH-CERTIFICATE-001`（C-100–C-105）：R034 路径证书边界原生核查——有实际路径时可迁移（ua 计算 + transport 正例），仅有等价存在（截断）时统一迁移 MereMove 非栖居（Σ回路 + 依赖运输，构造性反证）。下一工作包转为在线因果资格第一机器构造；ERCF-3 仍等待自然 consumer。\n\n",
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
    if state.get("revision") != 39 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_39_AND_S039")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(100, 106)]
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

    row_stable_note = "After C-100 through C-105 were appended (S040), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "A-RACE-TIMEOUT-FORMAL-001",
        "A-CONTEXTUAL-EQUIV-FORMAL-001",
        "A-QUOTIENT-MONAD-FORMAL-001",
        "A-CONTEXT-CHARACTERIZATION-FORMAL-001",
        "A-GUARD-ERASURE-FORMAL-001",
        "A-COST-FACTORIZATION-FORMAL-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S040 added the R034 path-certificate native check (C-100–C-105): the truncation economy removes the actual path and the unified move is non-inhabited, while path-indexed and fixed-pair moves exist. C4 text is unchanged and the remaining items stay open."

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S040 appended the path-certificate package; all nine proof packages re-validated (eight row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S040 appended the path-certificate package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-024"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the R034 native check: path-indexed and fixed-pair moves exist while the unified MereMove is non-inhabited; the first work package switches to the online-causality construction."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-024"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the R034 native verification C-100–C-105; the next strand is the online-causality interface."
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
        "classification": "MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(100, 106)],
        "run_id": RUN_ID,
        "mathematical_status": "PATH_MOVE_EXISTS_MERE_MOVE_EMPTY_NATIVE_CUBICAL",
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
        "scope": "Native Cubical Agda verification of the R034 path-certificate boundary: ua computation (C-100), truncation propositionality (C-101), fixed-pair interface (C-102), non-inhabitation of the fixed-source and general unified moves (C-103, C-104) and the path-indexed move (C-105). Constructive refutation, no Lean Eq substitution, not a HoTT paradox.",
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
            "scripts/audit/prepare_path_certificate_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_PATH_CERTIFICATE",
        "cognition_status": "PATH_CERTIFICATE_VERIFIED_AND_ONLINE_CAUSALITY_ROUTED",
        "scope": "Natively verify the R034 boundary (C-100–C-105), revalidate the eight older packages row-stable, and route the online-causality construction as the next package.",
    }

    state["revision"] = 40
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, fix a guarded/online interface (complete stream function versus a strategy that reads only inputs already arrived), prove an online-qualification boundary, and give a positive control of a task that can be completed online.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(100, 106)],
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
            )
        },
        "stale_source_hash_repair": {"observed": 16, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 40",
            "projection freshness PASS (27 directions / 36 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 40",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS",
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
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-verified R034 path-certificate boundary (C-100–C-105), repairs the sixteen stale source hashes, applies the projection text updates, and routes the online-causality package. No Git commit, tag or push.",
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
        "revision": 40,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
