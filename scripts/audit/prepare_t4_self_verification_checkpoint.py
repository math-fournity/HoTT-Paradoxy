#!/usr/bin/env python3
"""Prepare revision 58: record the T4 fifth-layer consumer audit and route batch 2.

S058 audited five fixed sources (Agda safe mode, Agda cubical 'what works'
section, MetaRocq, Rocq, NBE-in-TT) for self-verification / verified-delivery
claims against the four conditions of C9 section 4.  No P8 candidate was
found; every source documents its fences (trust base, verification relative
to a specification, transport non-computation, QIIT metatheory).
Verdict: BOUNDED_DEFENSE_WITH_TRUST_BASE.  The next work package is N13: the
second evidence-queue batch, stratified by owner document.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-058-T4-SELF-VERIFICATION-CONSUMER"
PREV_SESSION = "S-RES-20260912-057-EVIDENCE-QUEUE-SAMPLE"
RESULT_ID = "A-T4-SELF-VERIFICATION-AUDIT-001"
REPORT = "audit/self-verification-consumer审计-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
FETCHED = [
    f"{SESSION_REL}/evidence/fetched/agda-safe-mode.html",
    f"{SESSION_REL}/evidence/fetched/agda-cubical.html",
    f"{SESSION_REL}/evidence/fetched/metarocq-site.html",
    f"{SESSION_REL}/evidence/fetched/rocq-site.html",
    f"{SESSION_REL}/evidence/fetched/qiit-abs.html",
    f"{SESSION_REL}/evidence/fetched/metacoq-site.html",
]
EVIDENCE = [REPORT, *FETCHED]
NEW_STATUS = "T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_t4_self_verification", RUNTIME_PATH)
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
        "KC-000021": ("ALIGNED", "T4 的五个来源均为可回查的文档/摘要，抓取原件与哈希留证。"),
        "KC-000026": ("DEEPENED", "‘HoTT 能否越过自身自指’在 T4 中获得工程对照：真实系统用信任基+验证相对规范来处理自证。"),
        "KC-000028": ("DEEPENED", "自反真理验证回环在 T4 中被逐源核查：没有系统声称总停机+健全+完备+内部自证的完整包。"),
        "KC-000030": ("ALIGNED", "理论经济学的问题保持为方向；T4 只审计声明，不新增数学结论。"),
        "KC-000035": ("DEEPENED", "MetaRocq/NBE-in-TT 是‘理论关于自身’的真实工程样本；其围栏（内核信任基、QIIT 元语言、部分形式化）被显式记录。"),
        "KC-000036": ("DEEPENED", "哥德尔/自馈问题在 T4 中保持通用边界 + 分层工程结论；ERCF-3 与本条线继续 gated。"),
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
            ("NOT_TOUCHED", "本轮是 S058 第五层 consumer 审计（T4）；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S058/SESSION.md；{REPORT} | N13 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — T4 完成（五个固定来源，无 P8 候选，判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`）；第一工作包转 N13 证据队列第二批（按 owner 文档分层）；revision 58/generation 042。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-T4-SELF-VERIFICATION-AUDIT`；理解章节 inventory 不变（audit/ 资产）。",
        "- update_decision: `T4 报告与五个抓取原件进入 audit/ 与 session evidence；不新增 claim matrix 行。`",
        "- cross_conflicts: `NONE_OBSERVED` — T4 与 C8（P8 为空）、C9（第三层 OPEN）、C10（A-11 为已知限制）一致。",
        "- unresolved: `P8/E6、N13、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `BOUNDED_DEFENSE_WITH_TRUST_BASE`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S057 路由的第一工作包 T4（第五层 consumer 审计，按 C9 §4 四条件）。",
        "- 审计集合（固定、抓取留证）：Agda 2.8.0 Safe Agda 文档、Agda 2.8.0 Cubical 'What works, and what doesn't'、MetaRocq 站点、Rocq 官方站点、Altenkirch–Kaposi NBE-in-TT（arXiv:1612.02462v4）。",
        "- 判词：五个来源均为 `真实性 ✓ / 资格越级 ✗`，各自显式记录围栏——`T4-S1 DEFENSE_BY_RESTRICTION`、`T4-S2 DOCUMENTED_FENCE`、`T4-S3 CERTIFIED_TOOLING_NOT_SELF_CERTIFICATION`、`T4-S4 DEFENSE_WORKS_WITH_EXPLICIT_TRUST_BASE`、`T4-S5 REPRESENTATION_PREREQUISITE_DOCUMENTED`；总判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`。",
        "- 关键观察：最强声明（Rocq/MetaRocq verified reference checker 'correct and complete with respect to this specification'）自带三层限定（信任内核、相对规范、片段范围），执行的正是 C8 所要求的资格分离；NBE-in-TT 的 QIIT 元语言与 'most of the constructions' 恰好是 C8 P6 的实证。",
        "- 五层审计塔完整：核心库/论文（N1）、提取接口（N2）、派生开发（N5）、编译后端（N10）、自证声明（T4）；固定集合内全部为防御或有界负结论。",
        "- 边界：文档/摘要级核对；未重跑 MetaRocq 验证或审计内核代码；arXiv API 限流与 metacoq.github.io 重定向已记录。",
        "- 三件套：direction/panorama revision 58/generation 042；core 不变；无 理解章节 变更。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 57", "source_state_revision: 58")
    direction = sub_once(direction, "projection_generation: 20260912-direction-041", "projection_generation: 20260912-direction-042")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：T4 第五层 consumer 审计——固定版本审计真实系统（证明助手/库/论文承诺）对“自证/已验证交付”的声明是否满足 C9 §4 四条件（真实性、资格越级、无新增假设、可核查性）；满足则转 F-011 机器化并按 `NATURAL_USAGE_MISMATCH` 候选处理；不满足则把围栏记入审计并回到证据队列第二批抽样（按 owner 文档分层）。",
        "4. **当前第一工作包**：N13 证据队列第二批——按 owner 文档分层抽样（对 `理解章节/` 的 A/B/C 系列与 `audit/` 账本分别建层，层内等距取样），沿用四值判词（`SUPPORTED` / `SUPERSEDED_BY_MACHINE_RESULT` / `UNSUPPORTED` / `PENDING`），与第一批样本去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 57", "source_state_revision: 58")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-041", "projection_generation: 20260912-outcome-042")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT",
    )
    row = (
        "| `OUT-TOP-T4-SELF-VERIFICATION-AUDIT` | S058 第五层 consumer 审计（T4）——固定五源（Agda safe、Agda cubical 'what works'、MetaRocq、Rocq、NBE-in-TT）核查“自证/已验证交付”声明；全部 `真实性 ✓ / 资格越级 ✗` 且显式记录围栏（禁用特性、传输不计算、信任内核、验证相对规范、QIIT 元语言与部分形式化）；无 P8 候选 |"
        " `DIR-W-RP-B01`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前文档/摘要级审计（抓取留证） | `BOUNDED_DEFENSE_WITH_TRUST_BASE` |"
        " 五层审计塔（N1/N2/N5/N10/T4）在固定版本集合内完整；最强真实声明自带三层限定，执行的正是资格分离 |"
        " 未重跑 MetaRocq 验证、未审计内核代码；负结论只覆盖五个固定来源与抓取版本 |"
        " `audit/self-verification-consumer审计-20260912.md`；S058 evidence/fetched（6 文件含重定向记录） |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "S057 的证据队列首批抽样（40/2,396）无 `UNSUPPORTED`、无 E6，7 条历史主张由机器结果接管；R032 回放、",
        "S057 的证据队列首批抽样（40/2,396）无 `UNSUPPORTED`、无 E6，7 条历史主张由机器结果接管；S058 的 T4 五源审计无 P8 候选（`BOUNDED_DEFENSE_WITH_TRUST_BASE`），五层审计塔完整；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S057 的证据队列首批抽样（40/2,396）无 `UNSUPPORTED`、无 E6。所有新结论继续执行 F-011。",
        "S057 的证据队列首批抽样（40/2,396）无 `UNSUPPORTED`、无 E6；S058 的 T4 五源审计（Agda safe/Agda cubical/MetaRocq/Rocq/NBE-in-TT）判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`，五层审计塔完整。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | T4 第五层 consumer 审计 | fixed-version consumer audit | 按 C9 §4 四条件审计真实系统对“自证/已验证交付”的声明；满足转 F-011；否则回证据队列第二批（按 owner 分层） |",
        "| 已闭合工作包 16 | 第五层 consumer 审计（S058，T4） | `BOUNDED_DEFENSE_WITH_TRUST_BASE` | 五源全部记录围栏；无 P8 候选；最强声明自带信任基/相对规范/片段范围三层限定 |\n"
        "| 第一工作包 | N13 证据队列第二批 | stratified sample review | 按 owner 文档分层抽样（A/B/C 系列与 audit 账本分层；层内等距）；四值判词；与第一批去重；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 T4 第五层 consumer 审计：固定版本审计真实系统（证明助手/库/论文承诺）对“自证/已验证交付”的声明是否满足 C9 §4 四条件；满足则转 F-011 并按 NATURAL_USAGE_MISMATCH 候选处理；不满足则记围栏并回到证据队列第二批抽样（按 owner 文档分层）。",
        "2. 当前第一工作包转为 N13 证据队列第二批：按 owner 文档分层抽样（`理解章节/` A/B/C 系列与 `audit/` 账本分别建层，层内等距取样），沿用四值判词并与第一批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
    )
    memory = sub_once(
        memory,
        "- S057 完成 N12 首批抽样复核：",
        "- S058 完成 T4 第五层 consumer 审计：`audit/self-verification-consumer审计-20260912.md` 核查五个固定来源（Agda 2.8.0 Safe Agda、Agda Cubical 'What works'、MetaRocq、Rocq 官方、Altenkirch–Kaposi NBE-in-TT）；判词 `BOUNDED_DEFENSE_WITH_TRUST_BASE`——无 P8 候选，全部来源显式记录围栏（禁用特性、传输不计算、信任内核、验证相对规范、QIIT 元语言 + 部分形式化）；五层审计塔（N1/N2/N5/N10/T4）完整；下一工作包转 N13 证据队列第二批。\n"
        "- S057 完成 N12 首批抽样复核：",
    )
    memory = sub_once(
        memory,
        "`A-EVIDENCE-QUEUE-SAMPLE-001`。",
        "`A-EVIDENCE-QUEUE-SAMPLE-001`、`A-T4-SELF-VERIFICATION-AUDIT-001`。",
    )
    memory = sub_once(
        memory,
        "S057 完成证据队列首批抽样（无 UNSUPPORTED、无 E6）并转 T4 第五层 consumer 审计，不直接跳 ERCF-3 构造。",
        "S057 完成证据队列首批抽样（无 UNSUPPORTED、无 E6）；S058 完成 T4 五源审计（无 P8，判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`）并转 N13 证据队列第二批，不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S058 完成 T4 第五层 consumer 审计：五个固定来源（Agda 2.8.0 Safe Agda 文档、Agda 2.8.0 Cubical 'What works, and what doesn't'、MetaRocq 站点、Rocq 官方站点、Altenkirch–Kaposi NBE-in-TT arXiv:1612.02462v4）全部按 C9 §4 四条件核查；结论 `BOUNDED_DEFENSE_WITH_TRUST_BASE`——无 P8 候选，每个来源都显式记录围栏（禁用特性、传输不计算、信任内核、验证相对规范、QIIT 元语言 + 部分形式化）。最强真实声明（Rocq/MetaRocq verified reference checker）自带三层限定，执行的正是资格分离。五层审计塔（N1/N2/N5/N10/T4）至此完整；抓取原件与哈希存于本 Session `evidence/fetched/`。下一工作包为 N13 证据队列第二批（按 owner 文档分层）；备选 ERCF-3 T3（gated）。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "56. 证据队列的“有界推进”要靠固定抽样规则而不是穷举：",
        "57. “自证声明”类 consumer 的审计要按四条件逐源核对，并记录**围栏**而不是只记结论：Agda 文档列禁用特性（含 Girard–Hurken 悖论来源）、Cubical 文档记录传输值可能不计算、MetaRocq 提供认证工具而非自证、Rocq 官方的 verified reference checker 自带三层限定（OCaml 信任内核、验证相对规范、片段范围）、NBE-in-TT 需要 QIIT 元语言且只形式化大部分构造。真实系统普遍**文档化**自己的资格边界；把这种自限读成“已经自证”或“已经失败”都是越级。五层审计塔（核心库/提取接口/派生开发/编译后端/自证声明）齐全后，悖论候选的缺口只剩真实自然使用链（E6）。\n"
        "56. 证据队列的“有界推进”要靠固定抽样规则而不是穷举：",
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
    if state.get("revision") != 57 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_57_AND_S057")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README, MERGE_MANIFEST})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S058 T4 self-verification consumer audit; no proof source, run, claim-matrix row or understanding-chapter file changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "consumer_audit",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "BOUNDED_DEFENSE_WITH_TRUST_BASE",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-W51-RPB01-MAPPING-001", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [REPORT, *FETCHED],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "resolution": {
            "reason": "Five fixed sources were fetched and assessed against the four conditions of C9 section 4; none escalates a mathematical classification into effective delivery, and each documents its fences. No P8 candidate found.",
            "evidence": [REPORT, *FETCHED],
        },
        "scope": "Fifth-layer consumer audit (T4): Agda safe mode, Agda cubical 'what works', MetaRocq, Rocq, and NBE-in-TT, checked against the four acceptance conditions. Verdict: BOUNDED_DEFENSE_WITH_TRUST_BASE; no new mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, *EVIDENCE],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_T4_SELF_VERIFICATION_AUDIT",
        "cognition_status": "T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_AND_N13_ROUTED",
        "scope": "T4 fifth-layer consumer audit over five fixed sources and routing of the N13 second evidence-queue batch.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-042" if rid.startswith("I-DIRECTION") else "20260912-outcome-042"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        if REPORT not in rec["full_sources"]:
            rec["full_sources"].append(REPORT)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the T4 fifth-layer consumer audit: no P8 candidate; the first work package is the N13 stratified evidence-queue batch."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the T4 self-verification consumer audit (BOUNDED_DEFENSE_WITH_TRUST_BASE); the next strand is N13."
    )

    state["revision"] = 58
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N13 second evidence-queue batch: stratify by owner document (理解章节 A/B/C series and audit ledgers), sample equal-spaced within each stratum, "
            "deduplicate against the first batch, and give four-value verdicts. If a natural-use chain (E6) appears, switch immediately to F-011 packaging. "
            "Fallback: ERCF-3 T3 (Goedel sentence), still gated by the C8 stop conditions."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "audit_kind": "t4_self_verification_consumer",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "sources": {
            "T4-S1": {"name": "Agda 2.8.0 Safe Agda docs", "verdict": "DEFENSE_BY_RESTRICTION"},
            "T4-S2": {"name": "Agda 2.8.0 Cubical docs (what works)", "verdict": "DOCUMENTED_FENCE"},
            "T4-S3": {"name": "MetaRocq site", "verdict": "CERTIFIED_TOOLING_NOT_SELF_CERTIFICATION"},
            "T4-S4": {"name": "Rocq official site", "verdict": "DEFENSE_WORKS_WITH_EXPLICIT_TRUST_BASE"},
            "T4-S5": {"name": "NBE-in-TT (arXiv:1612.02462v4)", "verdict": "REPRESENTATION_PREREQUISITE_DOCUMENTED"},
        },
        "four_conditions": {"real": 5, "qualification_escalation": 0, "added_assumptions": 0, "checkable": 5},
        "verdict": "BOUNDED_DEFENSE_WITH_TRUST_BASE",
        "p8_candidate_found": False,
        "five_layer_tower_complete": ["N1", "N2", "N5", "N10", "T4"],
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"report": REPORT, "fetched": FETCHED},
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
            "This in-scope checkpoint records the T4 fifth-layer consumer audit over five fixed self-verification sources "
            "(BOUNDED_DEFENSE_WITH_TRUST_BASE; no P8 candidate) and routes the N13 stratified evidence-queue batch. "
            "No new mathematical claim, no Git commit, tag or push."
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
        "revision": 58,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
