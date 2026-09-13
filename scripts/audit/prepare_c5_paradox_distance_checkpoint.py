#!/usr/bin/env python3
"""Prepare revision 42: record the C5 paradox-distance synthesis and route N1.

The session is paper-only synthesis: ten machine packages (C-59-C-109) are
already machine-proved and replayed; C5 assesses the distance to
NATURAL_USAGE_MISMATCH, identifies the missing natural consumer (E6), and
routes a bounded natural-consumer audit (N1). No claim is upgraded.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-042-C5-PARADOX-DISTANCE"
PREV_SESSION = "S-RES-20260912-041-ONLINE-CAUSALITY"
RESULT_ID = "A-C5-PARADOX-DISTANCE-001"
C5 = "理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md"
MERGE = "audit/understanding-chapter-merge-manifest.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_c5_distance", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "C5 继续把目标锁定在现实相对非现实性，明确区分内部不一致与表示/资格边界。"),
        "KC-000012": ("DEEPENED", "C5 把 ASK 的资格问题展开成 Q0–Q7 与 E1–E6 的保持性检查，并定位唯一缺环 E6。"),
        "KC-000013": ("ALIGNED", "理论工具性/异化在 C5 中以“抽象遗忘维度 + 下游操作”形式保持，不升级为已证悖论。"),
        "KC-000014": ("ALIGNED", "方向 B 的有效交付问题保留在 W51×RP-B01；B01-TARGET 仍为开放接口。"),
        "KC-000022": ("ALIGNED", "两类现实相对悖论仍是判别框架；C5 未把任一模型边界写成已完成目标。"),
        "KC-000024": ("DEEPENED", "十个机器包在表示/资格层面对时序与计算合法性给出成对正反控制，C5 汇总了这些边界。"),
        "KC-000027": ("ALIGNED", "HoTT 继承程序界限的怀疑保留在 RP-B01/自指线，仍要求 HoTT 特定接口。"),
        "KC-000029": ("DEEPENED", "理论经济收益被固定为升级链的 E3（合法抽象与其遗忘维度），并要求 E6 自然消费者。"),
        "KC-000031": ("ALIGNED", "严格范型拒绝继续记为 DEFENSE_WORKS，不判为覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3/自馈循环继续 gated；C5 明确不以一般 Gödel 口号提前启动。"),
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
            ("NOT_TOUCHED", "本轮是十包后的 C5 综合评估；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S042/SESSION.md；理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md | N1 审计、RP-B01 接口与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — C5 判定当前仍为第二级 `REPRESENTATION_BOUNDARY`，唯一决定性缺环是 natural consumer（E6）；第一工作包转为 N1 有界自然消费者审计；revision 42/generation 026。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-C5-PARADOX-DISTANCE`（paper-only 综合）；理解章节 inventory 更新为 30/24。",
        "- update_decision: `C5 文档进入理解章节；十包 claim 状态不变；N1 进入第一工作包；ERCF-3/W51×RP-B01 继续 gated。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十包 hash 与 claim matrix 未变，S041 重放结论继续有效。",
        "- unresolved: `N1 审计、B01-TARGET、ERCF-3、R036/R038 原生升级、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮无新数学结论，状态为 `PAPER_ONLY_SYNTHESIS_NO_CLAIM_UPGRADE`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S041 在线因果边界后的 C5 综合工作包（十包后的悖论距离评估与剩余候选统筹）。",
        "- 输入：C1–C4、十个机器包 README 与 final runs、`方向追踪.md`、`全景视野.md`、RP-B01 计划、R036/R038 证据。",
        "- 结论：十包全部保持原判词；当前仍在 `REPRESENTATION_BOUNDARY`（第二级）。升级链 E1–E5 已在固定模型中成立，E6（natural consumer）十包均缺失，是唯一决定性缺环。",
        "- 路线：第一工作包转为 N1 有界自然消费者审计（固定接口/版本/承诺/调用链，三值 verdict）；找到候选则进入 F-011 机器化，未找到则给出有界负结论并转 W51×RP-B01 接口或 R036/R038 原生升级。",
        "- 边界：不新增数学 claim；不升级任何 claim；RP-B01/ERCF-3 继续 gated；无物理时间与现实桥梁主张。",
        "- 三件套：direction/panorama revision 42/generation 026；核心认知不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT`",
        "状态：`CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 41", "source_state_revision: 42")
    direction = sub_once(direction, "projection_generation: 20260912-direction-025", "projection_generation: 20260912-direction-026")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT",
        "semantic_status: CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-ONLINE-CAUSALITY`、`OUT-W-R041-PAPER` | truncation `DEFENSE_WORKS`、partiality 两个 `REPRESENTATION_BOUNDARY` 与商值 continuation 单子均已落位（商可分裂、无需选择）；下一步做 C5 综合评估（从十个机器结果评估悖论距离、剩余候选与自然 consumer 审计），再决定是否启动 ERCF-3 或 W51×RP-B01 |",
        "`OUT-TOP-ONLINE-CAUSALITY`、`OUT-TOP-C5-PARADOX-DISTANCE`、`OUT-W-R041-PAPER` | truncation `DEFENSE_WORKS`、partiality 两个 `REPRESENTATION_BOUNDARY` 与商值 continuation 单子均已落位（商可分裂、无需选择）；C5 把距离固定在第二级并指出唯一决定性缺环是 natural consumer（E6）；下一步做 N1 有界自然消费者审计，再决定是否启动 ERCF-3 或 W51×RP-B01 |",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-PATH-CERTIFICATE`、`OUT-TOP-ONLINE-CAUSALITY` | partiality、guard-erasure、cost、路径证书与在线因果支线已形成完整的正反结构（含表示限制、细化正控制、统一迁移非栖居与在线资格边界），仍未产生现实相对悖论；下一步做 C5 综合评估统筹剩余候选 |",
        "`OUT-TOP-PATH-CERTIFICATE`、`OUT-TOP-ONLINE-CAUSALITY`、`OUT-TOP-C5-PARADOX-DISTANCE` | partiality、guard-erasure、cost、路径证书与在线因果支线已形成完整的正反结构（含表示限制、细化正控制、统一迁移非栖居与在线资格边界），仍未产生现实相对悖论；C5 判定距 `NATURAL_USAGE_MISMATCH` 只差 natural consumer（E6）；下一步做 N1 有界自然消费者审计 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：C5 综合评估——从十个机器结果（MP-ERCF-001、MP-ERCF-TRUNC-001、MP-RACE-TIMEOUT-001、MP-CONTEXTUAL-EQUIV-001、MP-QUOTIENT-MONAD-001、MP-CONTEXT-CHARACTERIZATION-001、MP-GUARD-ERASURE-001、MP-COST-FACTORIZATION-001、MP-PATH-CERTIFICATE-001、MP-ONLINE-CAUSALITY-001）评估当前「悖论距离」、列出剩余候选与自然 consumer 审计结论，统筹是否启动 ERCF-3/W51×RP-B01 或 R036/R038 原生升级。",
        "4. **当前第一工作包**：N1 有界自然消费者审计——固定真实 partiality/delay、truncation、univalent transport 与 cost 接口的版本、签名、承诺与调用链，逐条判定是否存在把较弱资格当较强资格的 consumer；找到则进入 F-011 机器化，未找到则给出有界负结论并转 W51×RP-B01 接口构造或 R036/R038 原生升级。",
    )
    direction = sub_once(
        direction,
        "5. **自然桥梁 Gate**：查明实际 HoTT consumer 是否把结果商提升成含完成先后的交付能力；已核证据内尚未找到桥梁，继续停在 `DEFENSE_WORKS/REPRESENTATION_BOUNDARY`，找到具体接口再开。",
        "5. **自然桥梁 Gate**：N1 审计实际 HoTT/类型论 consumer 是否把结果商、截断、裸函数、等价存在或在线限制提升成更强资格；已核证据内尚未找到桥梁，继续停在 `DEFENSE_WORKS/REPRESENTATION_BOUNDARY`，找到固定接口再开。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT`",
        "状态：`CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 41", "source_state_revision: 42")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-025", "projection_generation: 20260912-outcome-026")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_ONLINE_CAUSALITY_PROVED_C5_SYNTHESIS_NEXT",
        "semantic_status: CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT",
    )
    c5_row = (
        "| `OUT-TOP-C5-PARADOX-DISTANCE` | C5：十包后的悖论距离评估——当前仍在 `REPRESENTATION_BOUNDARY`（第二级）；升级链 E1–E5 已在固定模型中成立，E6（natural consumer）十包均缺失，是唯一决定性缺环；下一工作包为 N1 有界自然消费者审计 |"
        " `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-U-A-REALITY-RELATIVE`、`DIR-W-RACE-TIMEOUT`、`DIR-W-RP-B01`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工综合 | `DOCUMENTED` |"
        " C1–C4 与十个 machine packages（C-59–C-109）的 claim/README/run 范围已逐包对照；距离分解、候选清单与 N1 验收标准已固定 |"
        " 不新增数学 claim、不升级任何 claim、不证明现实桥梁或物理时间；E6 未找到前仍是表示/资格边界 |"
        " `理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md`；`HoTT/CLAIM_EVIDENCE_MATRIX.md`；十个 final runs |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", c5_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 29/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0/C1/C2/C3/C4 共 5 个独有文件（nonidentical union entries=14）；逐文件处置已生成 |",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 30/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C5 共 6 个独有文件（nonidentical union entries=15）；逐文件处置已生成 |",
    )
    panorama = sub_once(
        panorama,
        "C3/C4 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4 自动裁决 |",
        "C3/C4/C5 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4/C5 自动裁决 |",
    )
    panorama = sub_once(
        panorama,
        "C5 综合评估、R036/R038 原生升级、R032 回放、自然 consumer、B01-TARGET、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "C5 综合已完成并判定当前距离为第二级；N1 自然消费者审计、R036/R038 原生升级、R032 回放、B01-TARGET、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "九者都不是 HoTT 悖论。",
        "九者都不是 HoTT 悖论；C5 综合评估把当前判词固定在第二级 `REPRESENTATION_BOUNDARY`，并指出唯一决定性缺环是 natural consumer（E6）。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | C5 综合评估（悖论距离与剩余候选） | synthesis / paper-only | 从十个机器结果评估当前悖论距离、列出剩余候选与自然 consumer 审计结论；统筹 ERCF-3/W51×RP-B01 与 R036/R038 原生升级 |",
        "| 第一工作包 | N1 有界自然消费者审计 | audit / paper-and-library-evidence | 固定真实 partiality/delay、truncation、univalent transport 与 cost 接口的版本/签名/承诺/调用链；逐条判定是否存在 E6 升级；找到则 F-011 机器化，未找到则有界负结论转 RP-B01/R036-R038 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 C5 综合评估：从十个机器结果评估悖论距离、剩余候选与自然 consumer 审计，统筹 ERCF-3/W51×RP-B01 与 R036/R038 原生升级。",
        "2. 当前第一工作包转为 N1 有界自然消费者审计：固定真实 partiality/delay、truncation、univalent transport 与 cost 接口的版本/签名/承诺/调用链，逐条判定是否存在把较弱资格当较强资格的 consumer；找到则进入 F-011 机器化，未找到则给出有界负结论。",
    )
    memory = sub_once(
        memory,
        "- `MP-ONLINE-CAUSALITY-001` 是第十个 F-011 package：在线因果资格边界（C-106–C-109，零警告）；final run `20260912-MP-ONLINE-CAUSALITY-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`。",
        "- `MP-ONLINE-CAUSALITY-001` 是第十个 F-011 package：在线因果资格边界（C-106–C-109，零警告）；final run `20260912-MP-ONLINE-CAUSALITY-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`。\n"
        "- C5 综合（S042）已评估十包后的悖论距离：仍在 `REPRESENTATION_BOUNDARY`（第二级），唯一决定性缺环是 natural consumer（E6）；下一工作包转为 N1 有界自然消费者审计（paper + 库/论文证据）。",
    )
    memory = sub_once(
        memory,
        "`A-PATH-CERTIFICATE-FORMAL-001`、`A-ONLINE-CAUSALITY-FORMAL-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；下一步做 C5 综合评估统筹剩余候选，不直接跳 ERCF-3。",
        "`A-PATH-CERTIFICATE-FORMAL-001`、`A-ONLINE-CAUSALITY-FORMAL-001`、`A-C5-PARADOX-DISTANCE-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；C5 已把距离固定在第二级并转 N1 自然消费者审计，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S042 完成 C5 综合（paper-only）：十包后判词仍为 `REPRESENTATION_BOUNDARY`（第二级）；升级链 E1–E5 已在固定模型中成立，E6（natural consumer）是唯一决定性缺环。下一工作包为 N1 有界自然消费者审计（固定接口、版本、承诺、调用链，三值 verdict）；ERCF-3/W51×RP-B01 继续 gated，R036/R038 原生升级为第二线。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "40. proof package 同轮更新 source/run/index 与人读入口时，必须对 stable record 的全部 `source_hashes` 做全量差异审计；只更新新增 proof/hash 仍会让旧 README hash 传播 stale，最终验收必须以 task hydration 的 `review_required=[]` 收口。",
        "40. proof package 同轮更新 source/run/index 与人读入口时，必须对 stable record 的全部 `source_hashes` 做全量差异审计；只更新新增 proof/hash 仍会让旧 README hash 传播 stale，最终验收必须以 task hydration 的 `review_required=[]` 收口。\n"
        "41. 十个机器包之后的距离评估把 `NATURAL_USAGE_MISMATCH` 的六要素收敛为 E1–E6：E1–E5 已在固定模型中成立，E6（真实、固定版本、可回查的 natural consumer）是唯一决定性缺环。没有 E6 时只能停在 `REPRESENTATION_BOUNDARY`；审计负结论必须写成“在本次固定的审计集合内未发现”，不得写成“系统中不存在”。",
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
    if state.get("revision") != 41 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_41_AND_S041")

    for required in (C5, MERGE):
        if not (root / required).is_file():
            raise SystemExit(f"REQUIRED_FILE_MISSING:{required}")
    merge = json.loads((root / MERGE).read_text(encoding="utf-8"))
    if merge.get("counts", {}).get("union_files") != 30 or merge.get("counts", {}).get("top_level_unique") != 6:
        raise SystemExit("MERGE_MANIFEST_NOT_REBUILT_FOR_C5")

    new_hashes = {
        C5: sha(root / C5),
        MERGE: sha(root / MERGE),
        MATRIX: sha(root / MATRIX),
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "research_synthesis",
        "path": C5,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "PARADOX_DISTANCE_LEVEL_2_NATURAL_CONSUMER_AUDIT_ROUTED",
        "full_sources": [
            C5,
            MERGE,
            MATRIX,
            "理解章节/C1-后续研究方向独立复审-20260912.md",
            "理解章节/C2-历史悖论谱与HoTT处理机制全解-20260912.md",
            "理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md",
            "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md",
            "workspace/.codex/research/hott/candidates/RP-B01/PLAN.md",
            "workspace/.codex/research/hott/candidates/RP-B01/CLAIMS.json",
            "workspace/.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/CLAIMS.json",
            "workspace/.codex/research/hott/reviews/TRANSITION-ABSTRACTION-002/CLAIMS.json",
        ],
        "source_hashes": {C5: new_hashes[C5], MERGE: new_hashes[MERGE], MATRIX: new_hashes[MATRIX]},
        "resolution": {
            "reason": "Paper-only synthesis grounded in ten machine-proved packages; no claim upgraded, no new mathematical result.",
            "evidence": [C5, MATRIX, MERGE],
        },
        "scope": "Assess the distance to NATURAL_USAGE_MISMATCH after C-59–C-109, decompose it into E1–E6, enumerate remaining candidates with evidence boundaries, and route the bounded natural-consumer audit (N1). No new mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C5, MERGE, MATRIX],
        "source_hashes": {C5: new_hashes[C5], MERGE: new_hashes[MERGE]},
        "mathematical_status": "NO_NEW_MATHEMATICS_PAPER_ONLY_SYNTHESIS",
        "cognition_status": "C5_PARADOX_DISTANCE_ASSESSED_AND_NATURAL_CONSUMER_AUDIT_ROUTED",
        "scope": "Read C1–C4 and the ten packages; assess the distance to NATURAL_USAGE_MISMATCH; describe the E1–E6 decomposition; route N1; no claim upgrade.",
    }

    understanding = state["records"]["A-UNDERSTANDING-RECONCILIATION-001"]
    understanding["scope"] = (
        "File-level reconciliation is complete and non-destructive for the current 30/24 inventory "
        "(24 same-name pairs, 15 identical, 9 different, 6 top-only); C4 and C5 are top-level syntheses, "
        "while semantic equivalence and 2,396 historical claim review remain open."
    )
    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-026" if rid.startswith("I-DIRECTION") else "20260912-outcome-026"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        if C5 not in rec["full_sources"]:
            rec["full_sources"].append(C5)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the C5 paradox-distance synthesis: the verdict remains REPRESENTATION_BOUNDARY; "
        "the unique decisive gap is the natural consumer (E6); the first work package is the bounded N1 natural-consumer audit."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the C5 distance assessment and the 30/24 understanding-chapter inventory; "
        "the next strand is the N1 natural-consumer audit."
    )

    state["revision"] = 42
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "Conduct the bounded natural-consumer audit (N1): fix real HoTT/type-theory interfaces "
            "(partiality/delay quotient consumers with scheduling or race/timeout; truncation consumers with extraction-like promises; "
            "univalent transport consumers with cost/timing/provenance observables; cost/timing interfaces), record exact version/signature/promise/call chain, "
            "and decide for each whether it upgrades a weaker qualification to a stronger one on the same task. "
            "If a candidate is found, machine-formalize the fixed consumer under F-011; if not, record the bounded negative result and route W51×RP-B01 interface construction or R036/R038 native upgrade."
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
        "older_proof_replays": "NOT_RERUN_IN_S042_NO_PROOF_SOURCE_OR_MATRIX_CHANGE; S041 post-check replays remain authoritative for unchanged hashes",
        "evidence": {"c5": C5, "merge_manifest": MERGE, "matrix": MATRIX},
        "mathematics": "PAPER_ONLY_SYNTHESIS_NO_CLAIM_UPGRADE / REPRESENTATION_BOUNDARY_LEVEL_2",
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
            "This in-scope checkpoint records the C5 paper-only paradox-distance synthesis (revision 42), updates the understanding-chapter inventory, "
            "routes the bounded N1 natural-consumer audit, and upgrades no mathematical claim. No Git commit, tag or push."
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
        "revision": 42,
        "session_id": SESSION_ID,
        "merge_union_files": merge["counts"]["union_files"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
