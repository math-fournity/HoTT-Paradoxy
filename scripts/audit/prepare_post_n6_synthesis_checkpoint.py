#!/usr/bin/env python3
"""Prepare revision 49: record the N7 post-N6 distance synthesis and route N8.

N7 tallied the twelve machine packages (C-59-C-123) and the N1/N2/N5 audits,
confirmed that the verdict remains REPRESENTATION_BOUNDARY with no
NATURAL_USAGE_MISMATCH, enumerated the remaining domains, and selected
N8: the SIP/representation consumer machine construction.
Paper-only; no claim is upgraded.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-049-POST-N6-SYNTHESIS"
PREV_SESSION = "S-RES-20260912-048-PARTIAL-DECISION"
RESULT_ID = "A-POST-N6-DISTANCE-001"
C7 = "理解章节/C7-post-N6距离综合与剩余域选择-20260912.md"
MERGE = "audit/understanding-chapter-merge-manifest.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_post_n6", RUNTIME_PATH)
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
        "KC-000005": ("ALIGNED", "N7 继续以“找到具体机制”为目标，把未找到 E6 记为范围化结论而非悖论。"),
        "KC-000010": ("ALIGNED", "N7 重估现实相对距离，仍明确区分 defense/boundary/candidate。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题被重述为 E1–E6 距离分解，并指向应用层调用链。"),
        "KC-000013": ("ALIGNED", "理论经济/遗忘在十二包台账中按判词分布汇总，不升级为结论。"),
        "KC-000014": ("ALIGNED", "方向 B 的剩余域（SIP/表示消费者、Cauchy modulus、应用层）被显式列出。"),
        "KC-000022": ("ALIGNED", "两类现实相对框架保持不变；N7 不升级任何命题。"),
        "KC-000027": ("ALIGNED", "HoTT 继承程序界限的观察被重述为“核心库系统性资格分离”。"),
        "KC-000029": ("DEEPENED", "理论经济在十二包中反复出现为商/截断/成本/时序的资格分离。"),
        "KC-000031": ("ALIGNED", "所有防御结果继续记为 DEFENSE_WORKS，不判为覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 前置仍开放；N7 不启动反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是 N7 post-N6 距离综合；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S049/SESSION.md；理解章节/C7-post-N6距离综合与剩余域选择-20260912.md | N8、ERCF-3 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N7 完成十二包距离综合；第一工作包转 N8 SIP/表示消费者机器构造；revision 49/generation 033。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-POST-N6-DISTANCE`；理解章节 inventory 更新为 32/24。",
        "- update_decision: `C7 进入理解章节；十二包判词分布与剩余域固定；N8 选定为 SIP/表示消费者机器构造。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十二个 proof 包与三个审计结论一致。",
        "- unresolved: `N8、Cauchy/应用层审计、ERCF-3 前置、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮无新数学结论，状态为 `DISTANCE_LEVEL_2_WITH_NO_E6`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S048 后的 N7 post-N6 距离综合。",
        "- 输入：十二个机器包（C-59–C-123）、C5/C6、N1/N2/N5 审计、方向/全景投影。",
        "- 结果：判词分布为 1 个 `DEFENSE_WORKS`、4 个边界类、5 个结构性正结果/完整刻画、1 个在线因果边界、1 个通用骨架；仍无 `NATURAL_USAGE_MISMATCH` 或内部不一致。E1–E5 反复成立，E6 仍在已审计集合中缺失。",
        "- 剩余域：SIP/表示消费者、Cauchy modulus + 外部 Real 库、工具链/应用层消费者、ERCF-3 前置。",
        "- 选择：N8 SIP/表示消费者机器构造（结构签名外可观察量 vs SIP/UA 等价；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 cost/provenance 则停止并转 Cauchy/应用层审计）。",
        "- 边界：本轮 paper-only，无新机器运行；claim matrix 未变。",
        "- 三件套：direction/panorama revision 49/generation 033；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT`",
        "状态：`CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 48", "source_state_revision: 49")
    direction = sub_once(direction, "projection_generation: 20260912-direction-032", "projection_generation: 20260912-direction-033")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT",
        "semantic_status: CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N7 post-N6 距离综合——汇总十二个机器包（C-59–C-123）的判词分布，重新评估离 `NATURAL_USAGE_MISMATCH` 的距离，明确剩余未触达域（SIP/表示消费者机器化、Cauchy modulus 外部库、工具链/应用层消费者），并选择下一机器构造或审计；不得升级任何未证命题。",
        "4. **当前第一工作包**：N8 SIP/表示消费者机器构造——在原声 Cubical Agda 中固定带签名的结构类型，构造签名内同构、签名外可观察量不同的最小实例；用 SIP/UA 得到等价并机器证明签名外观察量不可统一恢复；给出把观察量加入签名后的细化正控制；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 cost/provenance 边界则停止并转 Cauchy/应用层审计。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT`",
        "状态：`CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 48", "source_state_revision: 49")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-032", "projection_generation: 20260912-outcome-033")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT",
        "semantic_status: CORE_GENERATION_4_POST_N6_DISTANCE_SYNTHESIS_COMPLETE_SIP_REPRESENTATION_NEXT",
    )
    row = (
        "| `OUT-TOP-POST-N6-DISTANCE` | N7 post-N6 距离综合：十二个机器包（C-59–C-123）判词分布（1 个 `DEFENSE_WORKS`、4 个边界类、5 个结构性正结果/完整刻画、1 个在线因果边界、1 个通用骨架）；仍无 `NATURAL_USAGE_MISMATCH`；剩余域为 SIP/表示消费者、Cauchy modulus、工具链/应用层、ERCF-3 前置 |"
        " `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工综合 | `DOCUMENTED` |"
        " 十二包台账、判词分布、E1–E6 更新、剩余域与 N8 选择已固定；C5/C6 与 N1/N2/N5 审计逐项引用 |"
        " 不新增数学 claim；不把“未找到 E6”写成“E6 不存在” |"
        " `理解章节/C7-post-N6距离综合与剩余域选择-20260912.md`；`HoTT/CLAIM_EVIDENCE_MATRIX.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 31/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C6 共 7 个独有文件（nonidentical union entries=16）；逐文件处置已生成 |",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 32/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C7 共 8 个独有文件（nonidentical union entries=17）；逐文件处置已生成 |",
    )
    panorama = sub_once(
        panorama,
        "C3/C4/C5/C6 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4/C5/C6 自动裁决 |",
        "C3/C4/C5/C6/C7 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4/C5/C6/C7 自动裁决 |",
    )
    panorama = sub_once(
        panorama,
        "N6 partial/total decision 最小机器边界已机器闭合（C-118–C-123）；N7 post-N6 距离综合、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N6 partial/total decision 最小机器边界已机器闭合（C-118–C-123）；N7 post-N6 距离综合已完成；N8 SIP/表示消费者机器构造、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N6 把 strict vs partial classifier 做成最小原生机器边界（C-118–C-123，零 warning），判 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。所有新结论继续执行 F-011。",
        "N6 把 strict vs partial classifier 做成最小原生机器边界（C-118–C-123，零 warning），判 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`；N7 完成十二包距离综合，确认仍无 E6，剩余域为 SIP/表示、Cauchy、应用层与 ERCF-3 前置。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N7 post-N6 距离综合 | synthesis / paper-only | 汇总十二个机器包（C-59–C-123）判词分布，重估 `NATURAL_USAGE_MISMATCH` 距离，列出剩余未触达域并选择下一机器构造/审计；不升级任何命题 |",
        "| 第一工作包 | N8 SIP/表示消费者机器构造 | formal / native Cubical Agda | 固定带签名结构类型；签名内同构、签名外可观察量不同的最小实例；SIP/UA 等价下不可统一恢复签名外观察量；细化签名正控制；预期最多 `REPRESENTATION_BOUNDARY` |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N7 post-N6 距离综合：汇总十二个机器包（C-59–C-123）的判词分布，重估离 `NATURAL_USAGE_MISMATCH` 的距离，列出剩余未触达域（SIP/表示消费者、Cauchy modulus、工具链/应用层消费者）并选择下一机器构造或审计；不升级任何命题。",
        "2. 当前第一工作包转为 N8 SIP/表示消费者机器构造：在原生 Cubical Agda 中固定带签名结构类型，构造签名内同构、签名外可观察量不同的最小实例；SIP/UA 等价下机器证明签名外观察量不可统一恢复，并给出细化签名正控制；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 cost/provenance 则停止并转 Cauchy/应用层审计。",
    )
    memory = sub_once(
        memory,
        "- N6 partial/total classifier 边界（S048）已由 `MP-PARTIAL-DECISION-001` 原生机器化：C-118–C-123，零 warning、exact replay；十一个旧包在矩阵增长后全部 row-stable；判词 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。",
        "- N6 partial/total classifier 边界（S048）已由 `MP-PARTIAL-DECISION-001` 原生机器化：C-118–C-123，零 warning、exact replay；十一个旧包在矩阵增长后全部 row-stable；判词 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。\n"
        "- N7 post-N6 距离综合（S049）：十二包判词分布固定（1 defense、4 边界、5 正结果、1 在线因果边界、1 通用骨架）；仍无 `NATURAL_USAGE_MISMATCH`；剩余域为 SIP/表示、Cauchy modulus、应用层、ERCF-3 前置；选 N8 SIP/表示消费者机器构造。",
    )
    memory = sub_once(
        memory,
        "`A-DERIVED-DEVELOPMENT-AUDIT-001`、`A-PARTIAL-DECISION-FORMAL-001`。七条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界并转 N7 距离综合，不直接跳 ERCF-3。",
        "`A-DERIVED-DEVELOPMENT-AUDIT-001`、`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`。七条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成十二包距离综合并转 N8 SIP/表示消费者，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S049 完成 N7 post-N6 距离综合：十二个机器包（C-59–C-123）判词分布固定；仍无 `NATURAL_USAGE_MISMATCH`；剩余域为 SIP/表示消费者、Cauchy modulus、工具链/应用层、ERCF-3 前置。下一工作包为 N8 SIP/表示消费者机器构造；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "47. 最小的 strict-vs-partial 机器边界不需要完整 partiality monad：`Q = A/R_A`（a~b）、`D≈ = Delay Bool/R_D`（now x ~ later (now x)）、代表层 `P0 a = now true`、`P0 b = later (now true)` 就足以证明「strict 扩展不存在、up-to-≈ partial classifier 存在、strict 消费者不能下降、代表层消费者仍可区分」。先做最小片段再决定是否升级到完整单子。",
        "47. 最小的 strict-vs-partial 机器边界不需要完整 partiality monad：`Q = A/R_A`（a~b）、`D≈ = Delay Bool/R_D`（now x ~ later (now x)）、代表层 `P0 a = now true`、`P0 b = later (now true)` 就足以证明「strict 扩展不存在、up-to-≈ partial classifier 存在、strict 消费者不能下降、代表层消费者仍可区分」。先做最小片段再决定是否升级到完整单子。\n"
        "48. post-N6 距离综合确认：十二个机器包全部以 defense/boundary/positive structure 收口；核心库接口、提取后端与派生开发自述都在各自范围内执行资格分离。E6 若存在，更可能在应用层“自然使用链”或 SIP/表示消费者中；继续重审核心库只会重复已有防御。",
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
    if state.get("revision") != 48 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_48_AND_S048")
    for required in (C7, MERGE, MATRIX):
        if not (root / required).is_file():
            raise SystemExit(f"REQUIRED_FILE_MISSING:{required}")
    merge = json.loads((root / MERGE).read_text(encoding="utf-8"))
    if merge.get("counts", {}).get("union_files") != 32 or merge.get("counts", {}).get("top_level_unique") != 8:
        raise SystemExit("MERGE_MANIFEST_NOT_REBUILT_FOR_C7")

    new_hashes = {C7: sha(root / C7), MERGE: sha(root / MERGE), MATRIX: sha(root / MATRIX)}
    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MERGE})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE:{unexpected}")
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes[rel]
        state["records"][rid]["revalidation"] = "The understanding-chapter merge manifest was rebuilt after C7 was added; the record's scope is unchanged."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "research_synthesis",
        "path": C7,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "POST_N6_DISTANCE_LEVEL_2_SIP_REPRESENTATION_ROUTED",
        "full_sources": [C7, MERGE, MATRIX,
                         "理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md",
                         "理解章节/C6-新候选生成与派生开发消费者审计-20260912.md",
                         "audit/natural-consumer审计-20260912.md",
                         "audit/rp-b01-extraction-interface审计-20260912.md",
                         "audit/derived-development-consumer审计-20260912.md",
                         "audit/transition-lift机器证明实施证据-20260912.md",
                         "audit/partial-decision机器证明实施证据-20260912.md"],
        "source_hashes": {C7: new_hashes[C7], MERGE: new_hashes[MERGE], MATRIX: new_hashes[MATRIX]},
        "resolution": {
            "reason": "Twelve-package tally and audit synthesis: verdicts remain defense/boundary/positive; no NATURAL_USAGE_MISMATCH or inconsistency; N8 SIP/representation machine construction routed.",
            "evidence": [C7, MATRIX, MERGE],
        },
        "scope": "Post-N6 distance synthesis over C-59-C-123, C5/C6 and the N1/N2/N5 audits; enumerate remaining domains; select N8. No new mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C7, MERGE, MATRIX],
        "source_hashes": {C7: new_hashes[C7], MERGE: new_hashes[MERGE]},
        "mathematical_status": "NO_NEW_MATHEMATICS_POST_N6_SYNTHESIS",
        "cognition_status": "POST_N6_DISTANCE_SYNTHESIZED_AND_SIP_REPRESENTATION_ROUTED",
        "scope": "Read the twelve packages and audits; tally verdicts; reassess E6 distance; enumerate remaining domains; route N8; no claim upgrade.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-033" if rid.startswith("I-DIRECTION") else "20260912-outcome-033"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (C7, MERGE):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the post-N6 distance synthesis: twelve packages remain defense/boundary/positive; the first work package is the N8 SIP/representation machine construction."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the post-N6 distance synthesis and remaining-domain selection; the next strand is N8."
    )

    state["revision"] = 49
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N8: build a minimal native Cubical SIP/representation boundary. Fix a structure type with a signature; construct two structures isomorphic within the signature "
            "but differing in an observable outside it (tag/cost/provenance); use SIP/UA to identify them and machine-prove that no uniform function recovers the outside-signature observable; "
            "provide a refinement positive control where adding the observable to the signature recovers/distinguishes it. Expected verdict at most REPRESENTATION_BOUNDARY. "
            "If the construction only re-derives the cost/provenance boundary without SIP/UA in the key step, stop and switch to the Cauchy-modulus or application-layer audit."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "kind": "research_synthesis",
        "new_machine_proofs": [],
        "proof_sources_changed": False,
        "claim_matrix_sha256": new_hashes[MATRIX],
        "evidence": {"c7": C7, "merge_manifest": MERGE, "matrix": MATRIX},
        "mathematics": "NO_NEW_MATHEMATICS / DISTANCE_LEVEL_2_NO_E6",
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
            "This in-scope checkpoint records the N7 post-N6 distance synthesis (C7), updates the understanding-chapter inventory, "
            "and routes the N8 SIP/representation machine construction. No mathematical claim is upgraded. No Git commit, tag or push."
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
        "revision": 49,
        "session_id": SESSION_ID,
        "merge_union_files": merge["counts"]["union_files"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
