#!/usr/bin/env python3
"""Prepare revision 60: record the N14 evidence-hygiene repair and batch-3 sample.

S060 (a) implemented the bounded repair for A-CLAIM-LEDGER-DRIFT-001
(read-only anchor checker + owner-document hash sidecar + drift report:
MATCH 327 / PREFIX 550 / CONTAINED 1490 / DRIFTED 29, all in README and C0)
and closed the issue with scope; (b) ran the batch-3 sample over the eight
lowest-coverage owners (32 claims; SUPPORTED 22 / PENDING 10 / no UNSUPPORTED,
no E6).  Next work package: N15 (caliber unification + queue continuation).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-060-EVIDENCE-HYGIENE-BATCH3"
PREV_SESSION = "S-RES-20260912-059-EVIDENCE-QUEUE-BATCH2"
RESULT_ID = "A-EVIDENCE-HYGIENE-BATCH3-001"
DRIFT_ID = "A-CLAIM-LEDGER-DRIFT-001"
DRIFT_REPORT = "audit/claim-ledger-drift-repair-20260912.md"
DRIFT_CHECK = "audit/claim-ledger-drift-check-20260912.json"
OWNER_HASHES = "audit/claim-ledger-owner-hashes-20260912.json"
CHECKER = "scripts/audit/verify_claim_ledger_anchors.py"
BATCH3_REPORT = "audit/understanding-claims-sampling-batch3-20260912.md"
BATCH3_SAMPLE = "audit/understanding-claim-sample-batch3-20260912.json"
BATCH3_SCRIPT = "scripts/audit/sample_understanding_claims_batch3.py"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [DRIFT_REPORT, DRIFT_CHECK, OWNER_HASHES, CHECKER, BATCH3_REPORT, BATCH3_SAMPLE, BATCH3_SCRIPT]
NEW_STATUS = "EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES"

SPEC = importlib.util.spec_from_file_location("runtime_evidence_hygiene", RUNTIME_PATH)
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
        "KC-000005": ("ALIGNED", "N14 保持先证据后归因：漂移被机械定位后仍不改写历史账本。"),
        "KC-000012": ("ALIGNED", "ASK/资格相关历史主张在第三批中继续被分类（无 UNSUPPORTED）。"),
        "KC-000021": ("ALIGNED", "漂移检查与抽样脚本均落盘可复跑；未把未运行项升级。"),
        "KC-000025": ("DEEPENED", "‘为什么慢’再获一层证据：待裁决主体是表述类型（解释/计划/口径），不是未知事实。"),
        "KC-000035": ("ALIGNED", "HoTT 表达性问题的层映射不受证据卫生工作影响。"),
        "KC-000036": ("ALIGNED", "E6 连续三批未出现；gated 状态不变。"),
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
            ("NOT_TOUCHED", "本轮是 S060 证据卫生（漂移修复）与第三批抽样；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S060/SESSION.md；{DRIFT_REPORT}；{BATCH3_REPORT} | N15 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N14 完成（漂移检测机械化、issue 关闭；第三批 32 条完成）；第一工作包转 N15（口径统一 + 队列继续）；revision 60/generation 044。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-EVIDENCE-HYGIENE-BATCH3`；理解章节 inventory 不变。",
        "- update_decision: `漂移修复与第三批工件进入 audit/ 与 session evidence；`A-CLAIM-LEDGER-DRIFT-001` 转 CLOSED_WITH_SCOPE；不新增 claim matrix 行。`",
        "- cross_conflicts: `NONE_OBSERVED` — 漂移只影响 README/C0 的 29 条行锚；三批抽样连续无 UNSUPPORTED、无 E6。",
        "- unresolved: `口径统一（2369/2396 等）、证据队列余下 ~95%、E6、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `BOUNDED_DRIFT_REPAIR_AND_BATCH3_REVIEW`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S059 路由的第一工作包 N14（证据卫生 + 第三批）。",
        "- (a) 漂移修复：新增 `scripts/audit/verify_claim_ledger_anchors.py`（只读检查）+ `audit/claim-ledger-owner-hashes-20260912.json`（24 份 owner hash sidecar）+ `audit/claim-ledger-drift-check-20260912.json`；全量 2,396 条检查：`MATCH=327`、`PREFIX=550`、`CONTAINED=1490`、`DRIFTED=29`（README 14 + C0 15）、`LINE_OUT_OF_RANGE=0`、`MISSING_FILE=0`；引用政策固定（引用 claim 行先核 owner 当前文本）；`A-CLAIM-LEDGER-DRIFT-001` → `CLOSED_WITH_SCOPE`。",
        "- (b) 第三批抽样：按前两批抽样比最低的 8 个 owner（A2/B5/A9/读遍账本/全量精读/A4/审计锚点/A1）各等距取 4 条 → 32 条；判词 `SUPPORTED=22`、`SUPERSEDED=0`、`UNSUPPORTED=0`、`PENDING=10`；三批累计 122/2,396（5.09%）：65/12/0/45；E6 连续三批未出现。",
        "- 边界：漂移检查不改写历史账本；全量重抽取保留为可选项；PENDING 不当作支持或否证。",
        "- 三件套：direction/panorama revision 60/generation 044；core 不变；无 理解章节 变更。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN`",
        "状态：`CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES`",
    )
    direction = sub_once(direction, "source_state_revision: 59", "source_state_revision: 60")
    direction = sub_once(direction, "projection_generation: 20260912-direction-043", "projection_generation: 20260912-direction-044")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN",
        "semantic_status: CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N14 证据卫生与第三批——(a) 有界修复 `A-CLAIM-LEDGER-DRIFT-001`（给 claim 账本增加 owner-document hash + 行锚复核脚本，或按变更文件集重抽取）；(b) 启动第三批分层抽样，优先覆盖未抽到的 owner 文档（A4/A9/B0/B5 等）并与前两批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
        "4. **当前第一工作包**：N15 口径统一与队列继续——先把剩余口径不一致一次性对齐（句级账本 2369 vs claims 2,396；119 vs 125 user messages 等），产出《口径对照表》；再按 owner 抽样比继续加深（A0 3.5%、A11 5.2%、A8 3.0% 等优先），四值判词与前批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN`",
        "状态：`CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES`",
    )
    panorama = sub_once(panorama, "source_state_revision: 59", "source_state_revision: 60")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-043", "projection_generation: 20260912-outcome-044")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN",
        "semantic_status: CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES",
    )
    row = (
        "| `OUT-TOP-EVIDENCE-HYGIENE-BATCH3` | S060 N14——(a) claim 账本漂移有界修复：只读检查工具 + 24 份 owner hash sidecar + 全量检查报告（`MATCH=327`/`PREFIX=550`/`CONTAINED=1490`/`DRIFTED=29`，全部在 README/C0），`A-CLAIM-LEDGER-DRIFT-001` 转 `CLOSED_WITH_SCOPE`；(b) 第三批低覆盖 owner 抽样 32 条：`SUPPORTED=22`/`PENDING=10`/0 `UNSUPPORTED`；三批累计 122/2,396 |"
        " `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前证据卫生工具 + 人工抽样复核 | `DOCUMENTED / BOUNDED_DRIFT_REPAIR_AND_BATCH3_REVIEW` |"
        " 漂移被机械定位且引用政策固定；三批抽样无 UNSUPPORTED、无 E6 |"
        " 全量账本重抽取仍为可选项；口径统一（2369/2396）留待 N15 |"
        " `audit/claim-ledger-drift-repair-20260912.md`；`audit/understanding-claims-sampling-batch3-20260912.md`；`scripts/audit/verify_claim_ledger_anchors.py` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "S059 第二批分层抽样（50 条，两批累计 90/2,396）无 `UNSUPPORTED`、无 E6，并记录 claim 账本行锚漂移 issue；R032 回放、",
        "S059 第二批分层抽样（50 条，两批累计 90/2,396）无 `UNSUPPORTED`、无 E6，并记录 claim 账本行锚漂移 issue；S060 完成漂移有界修复（检测机械化、issue 关闭）与第三批低覆盖抽样（32 条，三批累计 122/2,396，仍无 `UNSUPPORTED`、无 E6）；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S059 第二批分层抽样（50 条，两批累计 90/2,396）无 `UNSUPPORTED`、无 E6，另开 `A-CLAIM-LEDGER-DRIFT-001`。所有新结论继续执行 F-011。",
        "S059 第二批分层抽样（50 条，两批累计 90/2,396）无 `UNSUPPORTED`、无 E6，另开 `A-CLAIM-LEDGER-DRIFT-001`；S060 完成其有界修复（检查工具 + owner hash sidecar + 29 条漂移定位，issue 关闭）与第三批抽样（32 条，三批累计 122/2,396，仍无 `UNSUPPORTED`、无 E6）。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N14 证据卫生与第三批 | bounded repair + stratified sample | (a) `A-CLAIM-LEDGER-DRIFT-001` 有界修复（owner-doc hash + 行锚复核或按变更集重抽取）；(b) 第三批覆盖未抽 owner 文档（A4/A9/B0/B5 等）并与前两批去重；发现 E6 即转 F-011 |",
        "| 已闭合工作包 18 | 证据卫生修复与第三批（S060，N14） | `BOUNDED_DRIFT_REPAIR_AND_BATCH3_REVIEW` | 漂移检测机械化（29 条定位于 README/C0）；issue 关闭；32 条低覆盖抽样 22/10/0/0 |\n"
        "| 第一工作包 | N15 口径统一与队列继续 | caliber alignment + proportion sampling | 先对齐 2369/2396 等口径并产出对照表；再按抽样比加深（A0/A11/A8 优先）；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N14 证据卫生与第三批：(a) 有界修复 `A-CLAIM-LEDGER-DRIFT-001`（给 claim 账本增加 owner-document hash + 行锚复核脚本，或按变更文件集重抽取）；(b) 第三批分层抽样，优先覆盖未抽到的 owner 文档（A4/A9/B0/B5 等）并与前两批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（gated）。",
        "2. 当前第一工作包转为 N15 口径统一与队列继续：先对齐剩余口径不一致（句级账本 2369 vs claims 2,396；119 vs 125 user messages 等）并产出《口径对照表》；再按 owner 抽样比继续加深（A0 3.5%、A11 5.2%、A8 3.0% 优先）；若发现 E6 立即转 F-011。备选：ERCF-3 T3（gated）。",
    )
    memory = sub_once(
        memory,
        "- S059 完成 N13 第二批分层抽样：",
        "- S060 完成 N14：(a) claim 账本漂移有界修复——`scripts/audit/verify_claim_ledger_anchors.py`（只读）+ `audit/claim-ledger-owner-hashes-20260912.json`（24 份 owner hash）+ `audit/claim-ledger-drift-check-20260912.json`；全量检查 `MATCH=327`/`PREFIX=550`/`CONTAINED=1490`/`DRIFTED=29`（README 14 + C0 15），`A-CLAIM-LEDGER-DRIFT-001` 转 `CLOSED_WITH_SCOPE`；(b) 第三批低覆盖 owner 抽样 32 条（A2/B5/A9/读遍账本/全量精读/A4/审计锚点/A1），`SUPPORTED=22`/`PENDING=10`/0 `UNSUPPORTED`；三批累计 122/2,396（65/12/0/45），E6 连续三批未出现；下一工作包转 N15 口径统一与队列继续。\n"
        "- S059 完成 N13 第二批分层抽样：",
    )
    memory = sub_once(
        memory,
        "`A-EVIDENCE-QUEUE-BATCH2-001`、`A-CLAIM-LEDGER-DRIFT-001`。",
        "`A-EVIDENCE-QUEUE-BATCH2-001`、`A-CLAIM-LEDGER-DRIFT-001`（CLOSED_WITH_SCOPE）、`A-EVIDENCE-HYGIENE-BATCH3-001`。",
    )
    memory = sub_once(
        memory,
        "S059 完成第二批分层抽样（两批累计 90/2,396，无 UNSUPPORTED、无 E6）并开行锚漂移 issue，转 N14（证据卫生 + 第三批），不直接跳 ERCF-3 构造。",
        "S059 完成第二批分层抽样（两批累计 90/2,396，无 UNSUPPORTED、无 E6）并开行锚漂移 issue；S060 完成漂移修复（检测机械化、issue 关闭）与第三批抽样（三批累计 122/2,396，仍无 UNSUPPORTED、无 E6），转 N15（口径统一 + 队列继续），不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S060 完成 N14：(a) `A-CLAIM-LEDGER-DRIFT-001` 有界修复——新增只读锚点检查 `scripts/audit/verify_claim_ledger_anchors.py`、24 份 owner hash sidecar 与全量检查报告；2,396 条 claim 中 `DRIFTED=29`（README 14 + C0 15，均为账本建立后被改写的当前边界文档），引用政策固定（引用 claim 行先核 owner 当前文本），issue 转 `CLOSED_WITH_SCOPE`；(b) 第三批低覆盖 owner 抽样 32 条（按前批抽样比最低的 8 个 owner 各 4 条）：`SUPPORTED=22`、`PENDING=10`、0 `UNSUPPORTED`；三批累计 122/2,396（5.09%）：65/12/0/45，E6 连续三批未出现。下一工作包为 N15（口径统一 + 按比例继续加深）；备选 ERCF-3 T3（gated）。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "58. 快照账本必须记录被引 owner 文档的 hash：",
        "59. 快照账本漂移的“有界修复”不是重写历史，而是三件套：只读检查器（逐条比对当前行文本）、owner hash sidecar（未来编辑可对比发现）、显式引用政策（引用 claim 行先核 owner 当前内容）。实测 2,396 条中仅 29 条漂移且全部集中在两份被改写的“当前边界”文档（README/C0），说明漂移与“文档是否持续维护”强相关而不是普遍噪声。第三批抽样证明“低覆盖 owner 加深”与“关键词/等距”互补：新增 22 条 SUPPORTED 中大量是引文、路由元数据与已实现实践，PENDING 全为解释/计划/口径类——证据队列的剩余工作因此可以按“表述类型”而不是“未知事实”来排队。\n"
        "58. 快照账本必须记录被引 owner 文档的 hash：",
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
    if state.get("revision") != 59 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_59_AND_S059")
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
        "Revalidated after the S060 evidence-hygiene repair and batch-3 sample; no proof source, run, claim-matrix row or understanding-chapter file changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "evidence_hygiene_and_sample",
        "path": DRIFT_REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "BOUNDED_DRIFT_REPAIR_AND_BATCH3_REVIEW",
        "research_parent": "A-HISTORICAL-MATH-CLAIMS-001",
        "depends_on": [DRIFT_ID, "A-EVIDENCE-QUEUE-BATCH2-001"],
        "full_sources": EVIDENCE + ["audit/claim-evidence-ledger.jsonl"],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "resolution": {
            "reason": "Read-only anchor check plus owner-hash sidecar locate the drift (29 claims in README/C0); the batch-3 sample over the eight lowest-coverage owners adds 32 verdicts (22/10/0/0) with no E6.",
            "evidence": EVIDENCE,
        },
        "scope": "Bounded claim-ledger drift repair (detection + policy; no ledger rewrite) and the third evidence-queue sample. Conclusions hold for the checked anchors and the sampled 32 claims.",
    }

    drift = state["records"][DRIFT_ID]
    drift["status"] = "closed"
    drift["lifecycle_status"] = "CLOSED"
    drift["evidence_status"] = "VERIFIED_WITH_SCOPE"
    drift["resolution"] = {
        "reason": "Bounded repair implemented: read-only anchor checker, owner-document hash sidecar, and an explicit citation policy; 29 drifted claims located (README 14 / C0 15).",
        "evidence": [DRIFT_REPORT, DRIFT_CHECK, OWNER_HASHES, CHECKER],
    }
    drift["scope"] = "Closed with scope: drift detection and citation policy are in place; full ledger re-extraction (embedding owner hashes into the ledger) remains an optional follow-up."
    drift["closed_by"] = RESULT_ID

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID, DRIFT_ID],
        "full_sources": [session_path, audit_path, runs_path, *EVIDENCE],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_EVIDENCE_HYGIENE_BATCH3",
        "cognition_status": "DRIFT_REPAIR_CLOSED_AND_BATCH3_REVIEWED",
        "scope": "Ledger drift bounded repair, batch-3 low-coverage sample, and routing of N15.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-044" if rid.startswith("I-DIRECTION") else "20260912-outcome-044"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (DRIFT_REPORT, BATCH3_REPORT):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N14 evidence-hygiene repair and batch-3 sample: drift detection is mechanical; the first work package is N15 (caliber unification plus queue continuation)."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the ledger-drift repair and the third evidence-queue sample; the next strand is N15."
    )

    state["revision"] = 60
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N15: unify the remaining caliber mismatches (annotated sentence ledger 2369 vs claims 2396; 119 vs 125 user messages, etc.) into a single caliber table, "
            "then continue the evidence queue by sampling ratio (A0 3.5%, A11 5.2%, A8 3.0% first), deduplicated against batches 1-3. "
            "If a natural-use chain (E6) appears, switch immediately to F-011 packaging. Fallback: ERCF-3 T3 (gated by the C8 stop conditions)."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "work_kind": "evidence_hygiene_repair_and_batch3",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "drift_repair": {
            "tool": CHECKER,
            "sidecar": OWNER_HASHES,
            "report": DRIFT_CHECK,
            "totals": {"MATCH": 327, "PREFIX": 550, "CONTAINED": 1490, "DRIFTED": 29, "LINE_OUT_OF_RANGE": 0, "MISSING_FILE": 0},
            "drifted_owners": {"理解章节/README.md": 14, "理解章节/C0-当前整合审计与证据边界-20260912.md": 15},
            "issue": DRIFT_ID,
            "issue_status": "CLOSED_WITH_SCOPE",
        },
        "batch3": {
            "rule": "eight lowest-coverage owners, four equal-spaced claims each, batches 1-2 excluded",
            "sample_size": 32,
            "verdicts": {"SUPPORTED": 22, "SUPERSEDED_BY_MACHINE_RESULT": 0, "UNSUPPORTED": 0, "PENDING": 10},
            "cumulative": {"sampled": 122, "coverage": "5.09%", "SUPPORTED": 65, "SUPERSEDED": 12, "UNSUPPORTED": 0, "PENDING": 45},
            "e6_found": False,
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"drift_repair": DRIFT_REPORT, "batch3": BATCH3_REPORT},
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
            "This in-scope checkpoint records the N14 bounded ledger-drift repair (checker + owner-hash sidecar + report; DRIFTED=29; issue closed with scope) "
            "and the batch-3 low-coverage sample (32 claims; 22/0/0/10). It routes N15 (caliber unification plus queue continuation). "
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
        "revision": 60,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
