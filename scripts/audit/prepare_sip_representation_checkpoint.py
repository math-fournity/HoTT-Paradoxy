#!/usr/bin/env python3
"""Prepare revision 50: record MP-SIP-REPRESENTATION-001 and route N9.

N8 built the minimal native Cubical SIP/UA boundary between structure
signature and outside-signature observables (C-124-C-128).  Verdict:
SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL.  The next work package is
N9: the Cauchy modulus boundary (with an external Real-library interface
audit as a secondary item).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-050-SIP-REPRESENTATION"
PREV_SESSION = "S-RES-20260912-049-POST-N6-SYNTHESIS"
RESULT_ID = "A-SIP-REPRESENTATION-FORMAL-001"
PROOF_ID = "MP-SIP-REPRESENTATION-001"
RUN_ID = "20260912-MP-SIP-REPRESENTATION-001-01"
SOURCE = "HoTT/formal/sip-representation/SIPRepresentation.agda"
SOURCE_README = "HoTT/formal/sip-representation/README.md"
TOOLCHAIN = "HoTT/formal/sip-representation/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/sip-representation/AGDA_LIBRARIES"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/sip-representation机器证明实施证据-20260912.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_sip_representation", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:80]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "N8 把 SIP/UA 替换许可缩到结构签名边界，不升级为悖论。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 N8 中具体化为“结构签名外的观察量是否需要额外表示数据”。"),
        "KC-000013": ("DEEPENED", "理论工具性的结构同一化在 N8 中得到机器化的正反控制。"),
        "KC-000014": ("ALIGNED", "方向 B 的交付资格在 SIP/UA 识别下再获边界实例。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮 Agda 2.8.0/Cubical v0.9 final run exit 0、零 warning、exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对框架保持不变；N8 是表示边界而非内部矛盾。"),
        "KC-000027": ("ALIGNED", "HoTT 继承程序界限的观察与 SIP 替换许可边界相容。"),
        "KC-000029": ("DEEPENED", "理论经济在 N8 中表现为“结构签名内替换、签名外保留表示”。"),
        "KC-000031": ("ALIGNED", "SIP/UA 只承诺签名内替换，继续记为防御/边界而非覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N8 不涉及自指反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是 N8 SIP/表示消费者机器边界；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S050/SESSION.md；HoTT/formal/sip-representation/SIPRepresentation.agda | N9、ERCF-3 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N8 完成并判 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`；第一工作包转 N9 Cauchy modulus 边界；revision 50/generation 034。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-SIP-REPRESENTATION`。",
        "- update_decision: `MP-SIP-REPRESENTATION-001 进入 formal/run/index/STATE；C-124–C-128 进入 claim matrix；十二个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十三个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `N9、Cauchy/应用层审计、ERCF-3 前置、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S049 后的 N8 工作包（SIP/表示消费者机器构造）。",
        "- 构造：`Str = Σ[ X ∈ Type₀ ] X`；`s=(Bool,true)`、`t=(Bool,false)`；识别 `s ≡ t` 由 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 构造；签名外观察量 `true`/`false`；细化结构 `Str' = Σ X, Σ x, Bool` 与投影 `obs'`。",
        "- 结果：`MP-SIP-REPRESENTATION-001`（C-124–C-128）通过 kernel：ua 识别 + 签名外观察量不同 + 任意 `Str→Bool` 常数化 + 无统一恢复 + 细化签名正控制。判词 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`（非悖论）。",
        "- 运行：final run `20260912-MP-SIP-REPRESENTATION-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`），零 warning。",
        "- 旧证据：矩阵第十一次增长后，十二个旧包全部重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：`⊥` 导入、签名外观察量不是 `Str→Bool`（设计修正）、`Type₁` Σ 的宇宙多态 `¬_`；均已按责任点修复，命题未削弱。",
        "- 边界：不调用完整 SIP 模块、不构造一般结构范畴定理、不证明真实库误用、不主张原创性。",
        "- 三件套：direction/panorama revision 50/generation 034；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT`",
        "状态：`CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 49", "source_state_revision: 50")
    direction = sub_once(direction, "projection_generation: 20260912-direction-033", "projection_generation: 20260912-direction-034")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT",
        "semantic_status: CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT",
    )
    direction = sub_once(
        direction,
        "；`MP-PARTIAL-DECISION-001` 原生给出 strict vs partial classifier 的最小边界（`C-118`–`C-123`）。",
        "；`MP-PARTIAL-DECISION-001` 原生给出 strict vs partial classifier 的最小边界（`C-118`–`C-123`）；`MP-SIP-REPRESENTATION-001` 原生给出 SIP/UA 替换许可的最小边界（`C-124`–`C-128`）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N8 SIP/表示消费者机器构造——在原声 Cubical Agda 中固定带签名的结构类型，构造签名内同构、签名外可观察量不同的最小实例；用 SIP/UA 得到等价并机器证明签名外观察量不可统一恢复；给出把观察量加入签名后的细化正控制；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 cost/provenance 边界则停止并转 Cauchy/应用层审计。",
        "4. **当前第一工作包**：N9 Cauchy modulus 边界——在同一工具链中固定 Cauchy 序列/等价的最小模型；证明商层不能统一恢复 modulus（或在无 modulus 数据时不能输出指定的界/十进制观察量）；给出携带 modulus 的细化表示正控制；并把可得的外部 Real 库接口作为固定审计子项；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 N6 partial/strict 形状则停止并转应用层审计。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT`",
        "状态：`CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 49", "source_state_revision: 50")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-033", "projection_generation: 20260912-outcome-034")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT",
        "semantic_status: CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT",
    )
    row = (
        "| `OUT-TOP-SIP-REPRESENTATION` | `MP-SIP-REPRESENTATION-001`：SIP/UA 替换许可的最小边界——`ua notEquiv` 识别 `(Bool,true)` 与 `(Bool,false)`（`C-124`）；签名外可观察量不同（`C-125`）；任意 `Str → Bool` 被识别强制为常数（`C-126`）；不存在统一恢复函数（`C-127`）；细化签名后投影恢复/区分两点（`C-128`，正控制） |"
        " `DIR-W-RP-B01`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0（零 warning）、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；十二个旧包 row-stable + exact replay |"
        " 不调用完整 SIP 模块、不构造一般结构范畴定理、不证明真实库误用或 HoTT 内部矛盾 |"
        " `HoTT/formal/sip-representation/`；final run `20260912-MP-SIP-REPRESENTATION-001-01`；claim matrix C-124–C-128；`audit/sip-representation机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N8 SIP/表示消费者机器构造、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N8 SIP/表示消费者机器构造已机器闭合（C-124–C-128）；N9 Cauchy modulus 边界、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N7 完成十二包距离综合，确认仍无 E6，剩余域为 SIP/表示、Cauchy、应用层与 ERCF-3 前置。所有新结论继续执行 F-011。",
        "N7 完成十二包距离综合，确认仍无 E6，剩余域为 SIP/表示、Cauchy、应用层与 ERCF-3 前置；N8 把 SIP/UA 替换许可做成最小机器边界（C-124–C-128，零 warning），判 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N8 SIP/表示消费者机器构造 | formal / native Cubical Agda | 固定带签名结构类型；签名内同构、签名外可观察量不同的最小实例；SIP/UA 等价下不可统一恢复签名外观察量；细化签名正控制；预期最多 `REPRESENTATION_BOUNDARY` |",
        "| 第一工作包 | N9 Cauchy modulus 边界 | formal / native Cubical Agda + external-library audit | 最小 Cauchy 序列/等价模型；商层不能统一恢复 modulus；携带 modulus 的细化表示正控制；外部 Real 库接口审计；预期最多 `REPRESENTATION_BOUNDARY` |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N8 SIP/表示消费者机器构造：在原生 Cubical Agda 中固定带签名结构类型，构造签名内同构、签名外可观察量不同的最小实例；SIP/UA 等价下机器证明签名外观察量不可统一恢复，并给出细化签名正控制；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 cost/provenance 则停止并转 Cauchy/应用层审计。",
        "2. 当前第一工作包转为 N9 Cauchy modulus 边界：在同一工具链中固定 Cauchy 序列/等价的最小模型；证明商层不能统一恢复 modulus（或无 modulus 数据时不能输出指定界/十进制观察量）；给出携带 modulus 的细化表示正控制；并把可得的 Real 库接口作为固定审计子项；预期最多 `REPRESENTATION_BOUNDARY`。",
    )
    memory = sub_once(
        memory,
        "- N7 post-N6 距离综合（S049）：十二包判词分布固定（1 defense、4 边界、5 正结果、1 在线因果边界、1 通用骨架）；仍无 `NATURAL_USAGE_MISMATCH`；剩余域为 SIP/表示、Cauchy modulus、应用层、ERCF-3 前置；选 N8 SIP/表示消费者机器构造。",
        "- N7 post-N6 距离综合（S049）：十二包判词分布固定（1 defense、4 边界、5 正结果、1 在线因果边界、1 通用骨架）；仍无 `NATURAL_USAGE_MISMATCH`；剩余域为 SIP/表示、Cauchy modulus、应用层、ERCF-3 前置；选 N8 SIP/表示消费者机器构造。\n"
        "- N8 SIP/UA 替换许可边界（S050）已由 `MP-SIP-REPRESENTATION-001` 原生机器化：C-124–C-128，零 warning、exact replay；十二个旧包在矩阵增长后全部 row-stable；判词 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。",
    )
    memory = sub_once(
        memory,
        "`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`。七条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成十二包距离综合并转 N8 SIP/表示消费者，不直接跳 ERCF-3。",
        "`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`、`A-SIP-REPRESENTATION-FORMAL-001`。八条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision、SIP/表示）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成距离综合，N8 关闭 SIP/表示边界并转 N9 Cauchy modulus，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S050 完成 N8：`MP-SIP-REPRESENTATION-001`（C-124–C-128）在 Agda 2.8.0/Cubical v0.9 下原生机器化 SIP/UA 替换许可边界，零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay；十二个旧包在矩阵增长后全部 row-stable。判词 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。下一工作包为 N9 Cauchy modulus 边界；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "48. post-N6 距离综合确认：十二个机器包全部以 defense/boundary/positive structure 收口；核心库接口、提取后端与派生开发自述都在各自范围内执行资格分离。E6 若存在，更可能在应用层“自然使用链”或 SIP/表示消费者中；继续重审核心库只会重复已有防御。",
        "48. post-N6 距离综合确认：十二个机器包全部以 defense/boundary/positive structure 收口；核心库接口、提取后端与派生开发自述都在各自范围内执行资格分离。E6 若存在，更可能在应用层“自然使用链”或 SIP/表示消费者中；继续重审核心库只会重复已有防御。\n"
        "49. 最小 SIP 边界可以用 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 手写，不需要完整 SIP 模块；关键是把“签名外观察量”写成需要额外表示数据（carrier 是 Bool）的值，而不是伪装成 `Str → Bool` 全函数。正控制则是把观察量加入签名，使识别不再成立。",
    )
    return {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
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
    if state.get("revision") != 49 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_49_AND_S049")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(124, 129)]
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
        TOOLCHAIN: sha(root / TOOLCHAIN),
        LIBRARIES: sha(root / LIBRARIES),
        f"HoTT/verification/runs/{RUN_ID}/RUN.json": sha(run_dir / "RUN.json"),
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": sha(run_dir / "index-row-manifest.json"),
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": sha(run_dir / "source-manifest.json"),
        AUDIT_DOC: sha(root / AUDIT_DOC),
    }
    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = "After C-124 through C-128 were appended (S050), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH for the twelve older packages."
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes[rel]
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(124, 129)],
        "run_id": RUN_ID,
        "mathematical_status": "MINIMAL_NATIVE_SIP_UA_SUBSTITUTIVITY_BOUNDARY",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [
            SOURCE, SOURCE_README, TOOLCHAIN, LIBRARIES,
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/stdout.txt",
            f"HoTT/verification/runs/{RUN_ID}/stderr.txt",
            f"HoTT/verification/runs/{RUN_ID}/environment.txt",
            MATRIX, "scripts/audit/capture_agda_proof_run.py",
            "scripts/audit/mark_proof_run_indexed.py",
            "scripts/audit/freeze_proof_index_rows.py",
            "scripts/audit/verify_formal_proof_run.py", AUDIT_DOC,
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE], SOURCE_README: new_hashes[SOURCE_README],
            TOOLCHAIN: new_hashes[TOOLCHAIN], LIBRARIES: new_hashes[LIBRARIES],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX], AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0 with zero warnings; source, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX, "scripts/audit/verify_formal_proof_run.py", AUDIT_DOC,
            ],
        },
        "scope": "Minimal native Cubical SIP/UA boundary: pointed structures (Bool,true) and (Bool,false) are identified by ua notEquiv (C-124); the outside-signature observable differs (C-125); any Bool-valued function on the structure type is constant on the pair (C-126); no uniform recovery exists (C-127); adding the observable to the signature recovers/distinguishes it (C-128). Boundary result with positive control; not a HoTT paradox.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, SOURCE, SOURCE_README,
                         f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                         f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC,
                         "scripts/audit/prepare_sip_representation_checkpoint.py"],
        "source_hashes": {SOURCE: new_hashes[SOURCE],
                          f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
                          AUDIT_DOC: new_hashes[AUDIT_DOC]},
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_SIP_REPRESENTATION",
        "cognition_status": "SIP_REPRESENTATION_BOUNDARY_PROVED_AND_CAUCHY_MODULUS_ROUTED",
        "scope": "Native Cubical SIP/UA boundary (C-124–C-128), revalidation of twelve older packages, and routing of the N9 Cauchy modulus work package.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-034" if rid.startswith("I-DIRECTION") else "20260912-outcome-034"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                    f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the native SIP/UA boundary: the substitutivity boundary is machine-proved; the first work package is the N9 Cauchy modulus boundary."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the native SIP/UA boundary (C-124-C-128); the next strand is N9."
    )

    state["revision"] = 50
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N9: build the minimal Cauchy modulus boundary in native Cubical Agda. Fix a minimal Cauchy sequence/equivalence model; machine-prove that the quotient cannot uniformly recover a modulus "
            "(or cannot output a specified bound/decimal observable without modulus data); provide a modulus-carrying refinement positive control; "
            "and audit an available external Real-library interface as a fixed secondary item. Expected verdict at most REPRESENTATION_BOUNDARY. "
            "If the construction only re-derives the N6 partial/strict shape, stop and switch to the application-layer audit."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(124, 129)],
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
                "20260912-MP-ERCF-001-02", "20260912-MP-ERCF-TRUNC-001-01",
                "20260912-MP-RACE-TIMEOUT-001-01", "20260912-MP-CONTEXTUAL-EQUIV-001-01",
                "20260912-MP-QUOTIENT-MONAD-001-01", "20260912-MP-CONTEXT-CHARACTERIZATION-001-01",
                "20260912-MP-GUARD-ERASURE-001-01", "20260912-MP-COST-FACTORIZATION-001-01",
                "20260912-MP-PATH-CERTIFICATE-001-01", "20260912-MP-ONLINE-CAUSALITY-001-01",
                "20260912-MP-TRANSITION-LIFT-001-01", "20260912-MP-PARTIAL-DECISION-001-01",
            )
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    edited = apply_projection_edits(root)
    texts = {
        **edited,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. "
            "This in-scope checkpoint records the native SIP/UA package MP-SIP-REPRESENTATION-001 (C-124-C-128), "
            "repairs the source hashes changed by the claim-matrix growth, and routes the N9 Cauchy modulus work package. "
            "No Git commit, tag or push."
        ),
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
        "revision": 50,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
