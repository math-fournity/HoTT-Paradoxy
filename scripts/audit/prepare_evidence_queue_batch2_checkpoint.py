#!/usr/bin/env python3
"""Prepare revision 59: record the N13 stratified sample (batch 2) and open the ledger-drift issue.

S059 sampled 50 of 2,396 claims stratified by owner document class
(C 10 / meta 10 / A 15 / B 15; batch-1 claims excluded; equal spacing within
each stratum).  Verdicts: SUPPORTED 30 / SUPERSEDED_BY_MACHINE_RESULT 5 /
UNSUPPORTED 0 / PENDING 15.  Two C0 claims still carry generation-2 text in
the snapshot ledger (line/text drift), so a new OPEN_ISSUE records the drift
and a bounded repair.  Next work package: N14 (drift repair / batch 3).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-059-EVIDENCE-QUEUE-BATCH2"
PREV_SESSION = "S-RES-20260912-058-T4-SELF-VERIFICATION-CONSUMER"
RESULT_ID = "A-EVIDENCE-QUEUE-BATCH2-001"
DRIFT_ID = "A-CLAIM-LEDGER-DRIFT-001"
REPORT = "audit/understanding-claims-sampling-batch2-20260912.md"
SAMPLE = "audit/understanding-claim-sample-batch2-20260912.json"
SCRIPT = "scripts/audit/sample_understanding_claims_batch2.py"
LEDGER = "audit/claim-evidence-ledger.jsonl"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [REPORT, SAMPLE, SCRIPT]
NEW_STATUS = "EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN"

SPEC = importlib.util.spec_from_file_location("runtime_evidence_batch2", RUNTIME_PATH)
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
        "KC-000005": ("ALIGNED", "批次二继续保持‘先找悖论后归因’；行锚漂移被记录而非静默修正。"),
        "KC-000012": ("ALIGNED", "ASK 相关历史主张在批次二中被逐条分类（SUPPORTED/PENDING/SUPERSEDED）。"),
        "KC-000021": ("ALIGNED", "抽样脚本、样本与报告均落盘可复跑；未把未运行项升级。"),
        "KC-000025": ("DEEPENED", "‘为什么慢’在批次二中获得证据卫生层面的新解释：快照账本的行锚漂移使历史主张复核成本上升。"),
        "KC-000035": ("ALIGNED", "HoTT 表达性问题不受抽样影响；C8/C9/C10 的层映射保持。"),
        "KC-000036": ("ALIGNED", "E6 仍未出现；ERCF/W51/A 的 gated 状态不变。"),
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
            ("NOT_TOUCHED", "本轮是 S059 证据队列分层抽样（第二批）与行锚漂移记录；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S059/SESSION.md；{REPORT} | N14 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N13 完成（50 条分层样本；两批累计 90/2,396）；第一工作包转 N14（行锚漂移有界修复 / 第三批抽样）；新开 `A-CLAIM-LEDGER-DRIFT-001`；revision 59/generation 043。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-EVIDENCE-QUEUE-BATCH2`；理解章节 inventory 不变。",
        "- update_decision: `批次二报告、样本与脚本进入 audit/ 与 session evidence；行锚漂移以 OPEN_ISSUE 记录；不新增 claim matrix 行。`",
        "- cross_conflicts: `NONE_OBSERVED` — 批次二与批次一、C8/C9/C10 的 E6 缺口一致；行锚漂移为证据卫生问题，不影响机器闭合结果。",
        "- unresolved: `A-CLAIM-LEDGER-DRIFT-001、证据队列余下 ~96%、E6、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `BOUNDED_SAMPLE_BATCH2_WITH_LEDGER_DRIFT_FINDING`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S058 路由的第一工作包 N13（按 owner 文档分层抽样）。",
        "- 抽样规则（`scripts/audit/sample_understanding_claims_batch2.py`）：按 owner 文档分层（C 10 / meta 10 / A 15 / B 15，层内先剔除第一批样本再等距取样）→ 50 条。",
        "- 判词分布：`SUPPORTED=30`、`SUPERSEDED_BY_MACHINE_RESULT=5`、`UNSUPPORTED=0`、`PENDING=15`；两批累计 90/2,396（3.76%）：43/12/0/35。",
        "- 新发现：`CL-001835`/`CL-001876`（C0）账本文本仍为 generation-2 口径（903 KC），而 owner 文档已更新——claim 账本缺 owner-doc hash，行锚/文本漂移。已开 `A-CLAIM-LEDGER-DRIFT-001`（OPEN_ISSUE / REVIEW_REQUIRED），并有界记录不影响机器闭合结果。",
        "- E6 检查：第二批仍未出现 natural-use chain。",
        "- 边界：样本只覆盖固定分层规则；PENDING 不当作支持或否证；不新增 claim matrix 行。",
        "- 三件套：direction/panorama revision 59/generation 043；core 不变；无 理解章节 变更。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT`",
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN`",
    )
    direction = sub_once(direction, "source_state_revision: 58", "source_state_revision: 59")
    direction = sub_once(direction, "projection_generation: 20260912-direction-042", "projection_generation: 20260912-direction-043")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT",
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N13 证据队列第二批——按 owner 文档分层抽样（对 `理解章节/` 的 A/B/C 系列与 `audit/` 账本分别建层，层内等距取样），沿用四值判词（`SUPPORTED` / `SUPERSEDED_BY_MACHINE_RESULT` / `UNSUPPORTED` / `PENDING`），与第一批样本去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
        "4. **当前第一工作包**：N14 证据卫生与第三批——(a) 有界修复 `A-CLAIM-LEDGER-DRIFT-001`（给 claim 账本增加 owner-document hash + 行锚复核脚本，或按变更文件集重抽取）；(b) 启动第三批分层抽样，优先覆盖未抽到的 owner 文档（A4/A9/B0/B5 等）并与前两批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT`",
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN`",
    )
    panorama = sub_once(panorama, "source_state_revision: 58", "source_state_revision: 59")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-042", "projection_generation: 20260912-outcome-043")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_T4_SELF_VERIFICATION_AUDIT_BOUNDED_DEFENSE_EVIDENCE_QUEUE_BATCH2_NEXT",
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_BATCH2_REVIEWED_LEDGER_DRIFT_ISSUE_OPEN",
    )
    row = (
        "| `OUT-TOP-EVIDENCE-QUEUE-BATCH2` | S059 N13 分层抽样（第二批）——按 owner 文档分层（C 10/meta 10/A 15/B 15），50 条逐条判词：`SUPPORTED=30`、`SUPERSEDED_BY_MACHINE_RESULT=5`、`UNSUPPORTED=0`、`PENDING=15`；两批累计 90/2,396；发现并记录 claim 账本行锚漂移（`A-CLAIM-LEDGER-DRIFT-001`）；E6 未出现 |"
        " `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工分层抽样 + 确定性脚本 | `DOCUMENTED / BOUNDED_SAMPLE_BATCH2_WITH_LEDGER_DRIFT_FINDING` |"
        " 5 条历史主张由机器结果/后续综合接管；行锚漂移为证据卫生问题且不影响已机器闭合结果 |"
        " 不宣称全量裁决；PENDING 不当作支持或否证；漂移修复与第三批抽样仍开放 |"
        " `audit/understanding-claims-sampling-batch2-20260912.md`；`audit/understanding-claim-sample-batch2-20260912.json`；`scripts/audit/sample_understanding_claims_batch2.py` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "S058 的 T4 五源审计无 P8 候选（`BOUNDED_DEFENSE_WITH_TRUST_BASE`），五层审计塔完整；R032 回放、",
        "S058 的 T4 五源审计无 P8 候选（`BOUNDED_DEFENSE_WITH_TRUST_BASE`），五层审计塔完整；S059 第二批分层抽样（50 条，两批累计 90/2,396）无 `UNSUPPORTED`、无 E6，并记录 claim 账本行锚漂移 issue；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S058 的 T4 五源审计（Agda safe/Agda cubical/MetaRocq/Rocq/NBE-in-TT）判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`，五层审计塔完整。所有新结论继续执行 F-011。",
        "S058 的 T4 五源审计（Agda safe/Agda cubical/MetaRocq/Rocq/NBE-in-TT）判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`，五层审计塔完整；S059 第二批分层抽样（50 条，两批累计 90/2,396）无 `UNSUPPORTED`、无 E6，另开 `A-CLAIM-LEDGER-DRIFT-001`。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N13 证据队列第二批 | stratified sample review | 按 owner 文档分层抽样（A/B/C 系列与 audit 账本分层；层内等距）；四值判词；与第一批去重；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
        "| 已闭合工作包 17 | 证据队列第二批（S059，N13） | `BOUNDED_SAMPLE_BATCH2_WITH_LEDGER_DRIFT_FINDING` | 50 条分层样本；两批累计 90/2,396；无 UNSUPPORTED、无 E6；行锚漂移入 issue |\n"
        "| 第一工作包 | N14 证据卫生与第三批 | bounded repair + stratified sample | (a) `A-CLAIM-LEDGER-DRIFT-001` 有界修复（owner-doc hash + 行锚复核或按变更集重抽取）；(b) 第三批覆盖未抽 owner 文档（A4/A9/B0/B5 等）并与前两批去重；发现 E6 即转 F-011 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N13 证据队列第二批：按 owner 文档分层抽样（`理解章节/` A/B/C 系列与 `audit/` 账本分别建层，层内等距取样），沿用四值判词并与第一批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
        "2. 当前第一工作包转为 N14 证据卫生与第三批：(a) 有界修复 `A-CLAIM-LEDGER-DRIFT-001`（给 claim 账本增加 owner-document hash + 行锚复核脚本，或按变更文件集重抽取）；(b) 第三批分层抽样，优先覆盖未抽到的 owner 文档（A4/A9/B0/B5 等）并与前两批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（gated）。",
    )
    memory = sub_once(
        memory,
        "- S058 完成 T4 第五层 consumer 审计：",
        "- S059 完成 N13 第二批分层抽样：`audit/understanding-claims-sampling-batch2-20260912.md` + `audit/understanding-claim-sample-batch2-20260912.json`（50 条：C 10/meta 10/A 15/B 15）；判词 `SUPPORTED=30`、`SUPERSEDED_BY_MACHINE_RESULT=5`、`UNSUPPORTED=0`、`PENDING=15`；两批累计 90/2,396；E6 未出现；发现 claim 账本行锚漂移（`CL-001835`/`CL-001876` 仍为 generation-2 文本）并开 `A-CLAIM-LEDGER-DRIFT-001`；下一工作包转 N14。\n"
        "- S058 完成 T4 第五层 consumer 审计：",
    )
    memory = sub_once(
        memory,
        "`A-T4-SELF-VERIFICATION-AUDIT-001`。",
        "`A-T4-SELF-VERIFICATION-AUDIT-001`、`A-EVIDENCE-QUEUE-BATCH2-001`、`A-CLAIM-LEDGER-DRIFT-001`。",
    )
    memory = sub_once(
        memory,
        "S058 完成 T4 五源审计（无 P8，判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`）并转 N13 证据队列第二批，不直接跳 ERCF-3 构造。",
        "S058 完成 T4 五源审计（无 P8，判 `BOUNDED_DEFENSE_WITH_TRUST_BASE`）；S059 完成第二批分层抽样（两批累计 90/2,396，无 UNSUPPORTED、无 E6）并开行锚漂移 issue，转 N14（证据卫生 + 第三批），不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S059 完成 N13 第二批分层抽样：按 owner 文档分层（C 10 / meta 10 / A 15 / B 15，层内先剔除第一批再等距）抽取 50/2,396，判词 `SUPPORTED=30`、`SUPERSEDED_BY_MACHINE_RESULT=5`、`UNSUPPORTED=0`、`PENDING=15`；两批累计 90/2,396（3.76%）无 `UNSUPPORTED`、无 E6。新发现：`CL-001835`/`CL-001876`（C0）账本文本仍为 generation-2 口径（903 KC），而 owner 文档已更新——claim 账本缺 owner-document hash，行锚/文本漂移；已开 `A-CLAIM-LEDGER-DRIFT-001`（OPEN_ISSUE），并有界记录不影响已机器闭合结果。报告与样本见 `audit/understanding-claims-sampling-batch2-20260912.md` 与 `audit/understanding-claim-sample-batch2-20260912.json`。下一工作包为 N14（行锚漂移有界修复 + 第三批抽样）；备选 ERCF-3 T3（gated）。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "57. “自证声明”类 consumer 的审计要按四条件逐源核对，",
        "58. 快照账本必须记录被引 owner 文档的 hash：claim-evidence-ledger 的 `claim_owner_document`+`claim_line` 在 owner 文档被更新后会行锚/文本漂移（实例：C0 的 generation-2 903-KC 文本 vs 当前 generation-3/4 正文）。在给出逐条裁决前先核 owner 文档当前内容；修复方向是给账本加 owner-doc hash 与行锚复核（或按变更集重抽取），而不是静默修正。同时，分层抽样（按 owner 类）比纯等距更能覆盖真实认知分布：第二批 50 条中 30 条直接 `SUPPORTED`、15 条 `PENDING` 集中于解释与问句片段，说明“待裁决”的主体是表述类型而不是未知事实。\n"
        "57. “自证声明”类 consumer 的审计要按四条件逐源核对，",
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
    if state.get("revision") != 58 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_58_AND_S058")
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
        "Revalidated after the S059 stratified sample (batch 2); no proof source, run, claim-matrix row or understanding-chapter file changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "evidence_queue_sample_review",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "BOUNDED_SAMPLE_BATCH2_WITH_LEDGER_DRIFT_FINDING",
        "research_parent": "A-HISTORICAL-MATH-CLAIMS-001",
        "depends_on": ["A-EVIDENCE-QUEUE-SAMPLE-001", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [REPORT, SAMPLE, SCRIPT, LEDGER,
                         "audit/understanding-claims-sampling-20260912.md",
                         "理解章节/C0-当前整合审计与证据边界-20260912.md"],
        "source_hashes": {REPORT: new_hashes[REPORT], SAMPLE: new_hashes[SAMPLE], SCRIPT: new_hashes[SCRIPT]},
        "resolution": {
            "reason": "50 claims sampled by owner-document stratum (batch-1 excluded, equal spacing within stratum); verdicts 30/5/0/15; two C0 claims show generation-2 text drift in the snapshot ledger, recorded as a new open issue.",
            "evidence": [REPORT, SAMPLE, SCRIPT, LEDGER],
        },
        "scope": "Second bounded evidence-queue sample (stratified by owner document), the cumulative two-batch distribution (90/2396), and the claim-ledger line/text drift finding with a bounded repair plan. Conclusions hold for the sampled claims only.",
    }

    state["records"][DRIFT_ID] = {
        "kind": "evidence_drift",
        "path": LEDGER,
        "status": "open",
        "lifecycle_status": "OPEN_ISSUE",
        "evidence_status": "REVIEW_REQUIRED",
        "classification": "CLAIM_LEDGER_LINE_AND_TEXT_DRIFT",
        "depends_on": [RESULT_ID],
        "full_sources": [REPORT, LEDGER, "理解章节/C0-当前整合审计与证据边界-20260912.md"],
        "source_hashes": {REPORT: new_hashes[REPORT], LEDGER: sha(root / LEDGER)},
        "resolution": {
            "reason": "The snapshot ledger records claim_owner_document and claim_line but no owner-document hash; owner documents edited after the snapshot cause line/text drift (example: CL-001835/CL-001876 still carry generation-2 903-KC text while C0 now states generation-3/27 and the current core is generation-4/36).",
            "evidence": [REPORT, LEDGER],
        },
        "scope": "Bounded repair path: add owner-document hashes plus a line-anchor rebase check (or re-extract claims for changed files). Until then, any claim citation must re-check the owner document's current content. Does not affect machine-closed results.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID, DRIFT_ID],
        "full_sources": [session_path, audit_path, runs_path, *EVIDENCE, LEDGER],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_EVIDENCE_QUEUE_BATCH2",
        "cognition_status": "EVIDENCE_QUEUE_BATCH2_REVIEWED_AND_LEDGER_DRIFT_ISSUE_OPEN",
        "scope": "N13 stratified evidence-queue sample (batch 2), the ledger drift finding, and routing of N14.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-043" if rid.startswith("I-DIRECTION") else "20260912-outcome-043"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (REPORT, SAMPLE):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N13 stratified sample: cumulative 90/2396 with no UNSUPPORTED and no E6; a ledger-drift issue is open; the first work package is N14."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the second evidence-queue sample and the claim-ledger drift finding; the next strand is N14."
    )

    state["revision"] = 59
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N14: (a) bounded repair of A-CLAIM-LEDGER-DRIFT-001 - add owner-document hashes plus a line-anchor rebase check (or re-extract claims for changed files); "
            "(b) start the third stratified sample covering owner documents not yet sampled (A4/A9/B0/B5 etc.), deduplicated against batches 1-2. "
            "If a natural-use chain (E6) appears, switch immediately to F-011 packaging. Fallback: ERCF-3 T3 (gated by the C8 stop conditions)."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "review_kind": "evidence_queue_stratified_sample_batch2",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "sample": {
            "batch": 2,
            "strata": {"C": 10, "meta": 10, "A": 15, "B": 15},
            "sample_size": 50,
            "verdicts": {"SUPPORTED": 30, "SUPERSEDED_BY_MACHINE_RESULT": 5, "UNSUPPORTED": 0, "PENDING": 15},
            "cumulative": {"sampled": 90, "SUPPORTED": 43, "SUPERSEDED_BY_MACHINE_RESULT": 12, "UNSUPPORTED": 0, "PENDING": 35},
            "e6_found": False,
            "drift_finding": {"issue": DRIFT_ID, "claims": ["CL-001835", "CL-001876"],
                              "reason": "generation-2 text in snapshot ledger vs updated owner document"},
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"report": REPORT, "sample": SAMPLE, "script": SCRIPT},
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
            "This in-scope checkpoint records the N13 stratified evidence-queue sample (batch 2, 50/2396; no UNSUPPORTED, no E6), "
            "opens A-CLAIM-LEDGER-DRIFT-001 for the snapshot-ledger line/text drift, and routes N14. "
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
        "revision": 59,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
