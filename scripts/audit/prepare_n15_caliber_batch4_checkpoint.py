#!/usr/bin/env python3
"""Prepare revision 61: record the N15 caliber reconciliation and batch-4 sample.

S061 (a) reconciled the reporting denominators mechanically
(`scripts/audit/reconcile_reporting_denominators.py` +
`audit/reporting-denominators-reconciliation-20260912.json`): the 2,369 sentence
ledger and the frozen 2,396 claim ledger are different units; 22 of 24 owners
reproduce their frozen count exactly today, only README/C0 grew; the live claim
surface is now 4,547 rows; 119 vs 125 is a scope difference (the six
parallel-session records are excluded).  (b) ran the batch-4 proportional sample
(40 claims / eight lowest-ratio owners / 28-0-0-12; cumulative 162/2,396 with no
UNSUPPORTED and no E6).  Next work package: optional batch 5 and the standing E6
gate; fallback ERCF-3 T3 stays gated.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-061-N15-CALIBER-AND-BATCH4"
PREV_SESSION = "S-RES-20260912-060-EVIDENCE-HYGIENE-BATCH3"
RESULT_ID = "A-N15-CALIBER-BATCH4-001"
REPORT = "audit/reporting-denominators-and-batch4-20260912.md"
RECONCILE_SCRIPT = "scripts/audit/reconcile_reporting_denominators.py"
RECONCILE_JSON = "audit/reporting-denominators-reconciliation-20260912.json"
SAMPLE_SCRIPT = "scripts/audit/sample_understanding_claims_batch4.py"
FILL_SCRIPT = "scripts/audit/fill_understanding_claim_sample_batch4.py"
SAMPLE_JSON = "audit/understanding-claim-sample-batch4-20260912.json"
SPOT_SCRIPT = "scripts/audit/verify_batch4_spot_checks.py"
SPOT_JSON = "audit/understanding-claim-batch4-spot-checks-20260912.json"
SENTENCE_LEDGER = "AI对话录/sentence_ledger_annotated.json"
USER_DISPOSITION = "audit/user-message-disposition.jsonl"
CLAIM_LEDGER = "audit/claim-evidence-ledger.jsonl"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [
    REPORT, RECONCILE_SCRIPT, RECONCILE_JSON, SAMPLE_SCRIPT, FILL_SCRIPT,
    SAMPLE_JSON, SPOT_SCRIPT, SPOT_JSON,
]
NEW_STATUS = "N15_CALIBER_AND_BATCH4_REVIEWED_QUEUE_CONTINUES"

SPEC = importlib.util.spec_from_file_location("runtime_n15", RUNTIME_PATH)
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
        "KC-000001": ("ALIGNED", "三问文档与账本口径的区分被进一步机械化；本轮给出口径对照表。"),
        "KC-000021": ("ALIGNED", "口径重算与专项核验脚本均只读、可复跑；未把未运行项升级。"),
        "KC-000025": ("DEEPENED", "‘为什么慢’再获一层证据：第四批 28/40 为引文/路由/已实现事实，PENDING 全为解释/计划/口径类。"),
        "KC-000035": ("ALIGNED", "HoTT 表达性问题不因报告口径工作改变。"),
        "KC-000036": ("ALIGNED", "E6 四批未出现；gated 状态不变。"),
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
            ("NOT_TOUCHED", "本轮是 S061 报告口径重算与第四批抽样；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S061/SESSION.md；{REPORT}；{RECONCILE_JSON} | 证据队列余量与 E6 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N15a 口径对照表完成（2369/2396、119/125、4,547 当前面）；N15b 第四批 40 条完成；第一工作包转队列继续（可选第 5 批）+ E6 gate；revision 61/generation 045。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-N15-CALIBER-BATCH4`；理解章节 inventory 不变。",
        "- update_decision: `新增 audit/ 与 scripts/audit/ 工件；不改写 理解章节，不新增 claim matrix 行，不重写冻结账本。`",
        "- cross_conflicts: `NONE_OBSERVED` — 两个口径差异均为单位/范围差，由机器重算解释；四批抽样连续无 UNSUPPORTED、无 E6。",
        "- unresolved: `证据队列余下 ~93%（冻结分母）、重新抽取与否、E6、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `BOUNDED_CALIBER_RECONCILIATION_AND_BATCH4_REVIEW`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S060 路由的第一工作包 N15（口径统一 + 按比例继续抽样）。",
        "- (a) 口径对照：`scripts/audit/reconcile_reporting_denominators.py` + `audit/reporting-denominators-reconciliation-20260912.json` 从各 canonical 源重算：句级账本 2,369 句 / 171 遍历单元（38 Codex + 111 网页 + 22 Gemini，0 缺锚）；归档 user records 125（119 历史对话 + 6 并行会话越界补充，32 条 EXCLUDED_OUT_OF_SCOPE）；冻结 claim 账本 2,396 行 / 24 owner。复算显示 22/24 owner 计数完全一致（2,268 行），仅 `C0`（82→91）与 `README.md`（46→60）增长；当前理解章节 claim 面 4,547 行（C1–C10 增量 2,128）。两条“不一致”均为单位/范围差，非丢件或冲突。",
        "- (b) 第四批抽样：按前 1–3 批已抽样比升序分配 40 条（每 owner≤5），覆盖 A8/A0/B3/A5/读遍账本/升级方案-v2/A10/A2；判词 `SUPPORTED=28`、`SUPERSEDED=0`、`UNSUPPORTED=0`、`PENDING=12`；四批累计 162/2,396（6.76%）：93/12/0/57；E6 四批一致未出现，不触发 F-011。",
        "- 专项核验：`scripts/audit/verify_batch4_spot_checks.py` 14/14 PASS（MinerU SHA、EARLY-GEMINI 归档、B3 70/3 与 0ⁿ1 陈述、Löb 前提、Gemini 21/36/24、LocalGPT 220、WebGPT 111、A2 读法原则、读遍账本 HoTT-2 读数、40 条判词完整性、无无证据 UNSUPPORTED）。",
        "- 边界：冻结 2,396 分母不变；4,547 只是同规则在当前文档上的重放值；抽样判词只覆盖样本；`SUPPORTED` 只表示登记角色内可核，不表示数学已证；本轮不改写 理解章节。",
        "- 三件套：direction/panorama revision 61/generation 045；core 不变；无 理解章节 变更。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES`",
        "状态：`CORE_GENERATION_4_N15_CALIBER_AND_BATCH4_REVIEWED_QUEUE_CONTINUES`",
    )
    direction = sub_once(direction, "source_state_revision: 60", "source_state_revision: 61")
    direction = sub_once(direction, "projection_generation: 20260912-direction-044", "projection_generation: 20260912-direction-045")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES",
        "semantic_status: CORE_GENERATION_4_N15_CALIBER_AND_BATCH4_REVIEWED_QUEUE_CONTINUES",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N15 口径统一与队列继续——先把剩余口径不一致一次性对齐（句级账本 2369 vs claims 2,396；119 vs 125 user messages 等），产出《口径对照表》；再按 owner 抽样比继续加深（A0 3.5%、A11 5.2%、A8 3.0% 等优先），四值判词与前批去重；若发现 E6 立即转 F-011。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
        "4. **当前第一工作包**：N16 证据队列按比例继续（可选第 5 批）——沿用同一抽样规则覆盖下一档 owner（`A11` 5.2%、`B5` 5.2%、`A7` 6.5% 等），四值判词与前四批去重；若发现 E6 立即转 F-011。N15 已完成（a 口径对照表；b 第四批 40 条 28/0/0/12；四批累计 162/2,396）。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
    )
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES`",
        "状态：`CORE_GENERATION_4_N15_CALIBER_AND_BATCH4_REVIEWED_QUEUE_CONTINUES`",
    )
    panorama = sub_once(panorama, "source_state_revision: 60", "source_state_revision: 61")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-044", "projection_generation: 20260912-outcome-045")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_EVIDENCE_HYGIENE_CLOSED_BATCH3_DONE_QUEUE_CONTINUES",
        "semantic_status: CORE_GENERATION_4_N15_CALIBER_AND_BATCH4_REVIEWED_QUEUE_CONTINUES",
    )
    row = (
        "| `OUT-TOP-N15-CALIBER-BATCH4` | S061 N15——(a) 报告口径机器对照表：句级账本 2,369 句/171 遍历单元、归档 user records 125（119 历史 + 6 越界补充）、冻结 claim 账本 2,396 行/24 owner；22/24 owner 计数完全复现（2,268 行），仅 README（46→60）与 C0（82→91）增长；当前理解章节 claim 面 4,547 行（C1–C10 增量 2,128）。(b) 第四批按比例抽样 40 条：`SUPPORTED=28`/`PENDING=12`/0 `UNSUPPORTED`/0 `SUPERSEDED`；四批累计 162/2,396（93/12/0/57）；专项核验 14/14 PASS |"
        " `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 只读账本重算工具 + 人工抽样复核 + 专项核验脚本 | `DOCUMENTED / BOUNDED_CALIBER_RECONCILIATION_AND_BATCH4_REVIEW` |"
        " 两条历史口径差异被机器解释为单位/范围差；四批抽样无 UNSUPPORTED、无 E6 |"
        " 冻结 2,396 分母不变；4,547 只是当前文档重放值；重新抽取未获授权；`CL-001619` 字节级重哈希未重跑 |"
        " `audit/reporting-denominators-and-batch4-20260912.md`；`audit/reporting-denominators-reconciliation-20260912.json`；`audit/understanding-claim-sample-batch4-20260912.json`；`audit/understanding-claim-batch4-spot-checks-20260912.json` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "S060 完成漂移有界修复（检测机械化、issue 关闭）与第三批低覆盖抽样（32 条，三批累计 122/2,396，仍无 `UNSUPPORTED`、无 E6）；R032 回放、",
        "S060 完成漂移有界修复（检测机械化、issue 关闭）与第三批低覆盖抽样（32 条，三批累计 122/2,396，仍无 `UNSUPPORTED`、无 E6）；S061 完成 N15（a 口径对照表；b 第四批 40 条 28/0/0/12，四批累计 162/2,396，仍无 `UNSUPPORTED`、无 E6），并修正两项口径表述；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S060 完成其有界修复（检查工具 + owner hash sidecar + 29 条漂移定位，issue 关闭）与第三批抽样（32 条，三批累计 122/2,396，仍无 `UNSUPPORTED`、无 E6）。所有新结论继续执行 F-011。",
        "S060 完成其有界修复（检查工具 + owner hash sidecar + 29 条漂移定位，issue 关闭）与第三批抽样（32 条，三批累计 122/2,396，仍无 `UNSUPPORTED`、无 E6）；S061 完成 N15 口径对照（2369 句/171 单元、125/119 记录、2,396 冻结行、22/24 owner 计数复现、当前面 4,547 行）与第四批按比例抽样（40 条 28/0/0/12，四批累计 162/2,396，无 UNSUPPORTED、无 E6；专项核验 14/14）。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N15 口径统一与队列继续 | caliber alignment + proportion sampling | 先对齐 2369/2396 等口径并产出对照表；再按抽样比加深（A0/A11/A8 优先）；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
        "| 已闭合工作包 19 | 口径对照与第四批（S061，N15） | `BOUNDED_CALIBER_RECONCILIATION_AND_BATCH4_REVIEW` | 口径差异 = 单位/范围差（机器重算）；第四批 40 条 28/0/0/12；四批累计 162/2,396，无 UNSUPPORTED、无 E6 |\n"
        "| 第一工作包 | N16 证据队列按比例继续（可选第 5 批） | proportion sampling | 下一档 owner（A11/B5/A7 等）沿用同一规则并与前四批去重；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N15 口径统一与队列继续：先对齐剩余口径不一致（句级账本 2369 vs claims 2,396；119 vs 125 user messages 等）并产出《口径对照表》；再按 owner 抽样比继续加深（A0 3.5%、A11 5.2%、A8 3.0% 优先）；若发现 E6 立即转 F-011。备选：ERCF-3 T3（gated）。",
        "2. 当前第一工作包转为 N16 证据队列按比例继续（可选第 5 批）：沿用同一抽样规则覆盖下一档 owner（`A11` 5.2%、`B5` 5.2%、`A7` 6.5% 等）并与前四批去重；若发现 E6 立即转 F-011。N15 已完成（a 口径对照表；b 第四批 40 条 28/0/0/12；四批累计 162/2,396）。备选：ERCF-3 T3（gated）。",
    )
    memory = sub_once(
        memory,
        "- S060 完成 N14：",
        "- S061 完成 N15：(a) 报告口径机器对照——`scripts/audit/reconcile_reporting_denominators.py` + `audit/reporting-denominators-reconciliation-20260912.json`：句级账本 2,369 句/171 遍历单元、归档 user records 125（119 历史 + 6 越界）、冻结 claim 账本 2,396 行/24 owner；22/24 owner 计数完全复现（2,268 行），仅 README（46→60）与 C0（82→91）增长；当前理解章节 claim 面 4,547 行（C1–C10 增量 2,128）；(b) 第四批按比例抽样 40 条（A8/A0/B3/A5/读遍账本/升级方案-v2/A10/A2），`SUPPORTED=28`/`PENDING=12`/0 `UNSUPPORTED`/0 `SUPERSEDED`；四批累计 162/2,396（93/12/0/57），E6 四批一致未出现；专项核验 14/14 PASS；下一工作包 N16（队列按比例继续），备选 ERCF-3 T3（gated）。\n- S060 完成 N14：",
    )
    memory = sub_once(
        memory,
        "`A-EVIDENCE-QUEUE-BATCH2-001`、`A-CLAIM-LEDGER-DRIFT-001`（CLOSED_WITH_SCOPE）、`A-EVIDENCE-HYGIENE-BATCH3-001`。",
        "`A-EVIDENCE-QUEUE-BATCH2-001`、`A-CLAIM-LEDGER-DRIFT-001`（CLOSED_WITH_SCOPE）、`A-EVIDENCE-HYGIENE-BATCH3-001`、`A-N15-CALIBER-BATCH4-001`。",
    )
    memory = sub_once(
        memory,
        "S060 完成漂移修复（检测机械化、issue 关闭）与第三批抽样（三批累计 122/2,396，仍无 UNSUPPORTED、无 E6），转 N15（口径统一 + 队列继续），不直接跳 ERCF-3 构造。",
        "S060 完成漂移修复（检测机械化、issue 关闭）与第三批抽样（三批累计 122/2,396，仍无 UNSUPPORTED、无 E6）；S061 完成 N15（口径机器对照 + 第四批 40 条，四批累计 162/2,396，仍无 UNSUPPORTED、无 E6），转 N16（队列按比例继续），不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S061 完成 N15：(a) 口径机器对照——`scripts/audit/reconcile_reporting_denominators.py` 重算：句级账本 2,369 句/171 遍历单元（38 Codex + 111 网页 + 22 Gemini，0 缺锚）；归档 user records 125 = 119 历史对话 + 6 并行会话越界补充（32 条 EXCLUDED_OUT_OF_SCOPE）；冻结 claim 账本 2,396 行/24 owner，其中 22/24 owner 计数完全复现（2,268 行），仅 README（46→60）与 C0（82→91）增长；当前理解章节 claim 面 4,547 行（C1–C10 增量 2,128）。两条历史“不一致”均为单位/范围差，不是丢件。(b) 第四批按比例抽样 40 条（前 1–3 批抽样比升序，每 owner≤5）：`SUPPORTED=28`、`PENDING=12`、0 `UNSUPPORTED`、0 `SUPERSEDED`；四批累计 162/2,396（6.76%）：93/12/0/57；专项核验 14/14 PASS；E6 四批一致未出现，不触发 F-011。报告 `audit/reporting-denominators-and-batch4-20260912.md`；下一工作包为 N16 队列按比例继续（下一档 A11/B5/A7 等），备选 ERCF-3 T3（gated）。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "59. 快照账本漂移的“有界修复”不是重写历史，",
        "60. 报告口径必须先各带单位再比较：2,369 是用户侧句级账本（句/引文片段，171 遍历单元），2,396 是理解章节行/句抽取账本（24 owner 的冻结行数），119 是三条对话录历史消息数，125 是含 6 条并行会话越界补充的归档记录数。机器复算显示冻结账本的 22/24 owner 至今逐条复现计数（2,268 行），增长集中在 C 系列新文档（2,128 行）与 README/C0 两处增量——说明“口径不一致”多数是单位/范围差而不是数据丢失；同时暴露冻结分母相对当前文档面（4,547 行）的真实覆盖率，任何“已全量覆盖”表述都必须写成相对冻结分母。\n"
        "59. 快照账本漂移的“有界修复”不是重写历史，",
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
    if state.get("revision") != 60 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_60_AND_S060")
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
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, MERGE_MANIFEST})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S061 N15 caliber reconciliation and batch-4 sample; "
        "no proof source, run, claim-matrix row or understanding-chapter file changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "caliber_reconciliation_and_sample",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "BOUNDED_CALIBER_RECONCILIATION_AND_BATCH4_REVIEW",
        "research_parent": "A-HISTORICAL-MATH-CLAIMS-001",
        "depends_on": ["A-EVIDENCE-HYGIENE-BATCH3-001"],
        "full_sources": EVIDENCE + [SENTENCE_LEDGER, USER_DISPOSITION, CLAIM_LEDGER],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "resolution": {
            "reason": "Mechanical recount shows the historical caliber pairs are unit/scope differences (2369 sentences / 171 units, 125 records vs 119 dialogue messages, 2396 frozen rows with 22/24 owners reproducing exactly, 4547 current-document rows). The batch-4 proportional sample adds 40 verdicts (28/0/0/12); cumulative 162/2396 with no UNSUPPORTED and no E6.",
            "evidence": EVIDENCE,
        },
        "scope": "Bounded accounting reconciliation (read-only recounts) plus the fourth evidence-queue sample. Conclusions hold for the fixed sources, rules and versions listed in the report; no mathematical claim is added or upgraded.",
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
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_CALIBER_AND_BATCH4",
        "cognition_status": "N15_CALIBER_RECONCILED_AND_BATCH4_REVIEWED",
        "scope": "Caliber reconciliation, batch-4 proportional sample, and routing of N16.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-045" if rid.startswith("I-DIRECTION") else "20260912-outcome-045"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (REPORT, RECONCILE_SCRIPT, RECONCILE_JSON, SAMPLE_JSON, SPOT_JSON):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N15 caliber reconciliation and batch-4 sample: the two historical caliber pairs are "
        "explained mechanically as unit/scope differences; the first work package becomes N16 (optional batch 5) with "
        "the standing E6 gate."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the reporting-denominator reconciliation and the fourth evidence-queue sample; the next strand is N16."
    )

    state["revision"] = 61
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N16: continue the evidence queue by the same proportional rule over the next owner tier "
            "(A11 5.2%, B5 5.2%, A7 6.5%, ...), deduplicated against batches 1-4; keep the frozen 2,396 "
            "denominator and the 4,547 current-surface recount clearly separated. If a natural-use chain (E6) "
            "appears, switch immediately to F-011 packaging. Fallback: ERCF-3 T3 (gated by the C8 stop conditions)."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "work_kind": "caliber_reconciliation_and_batch4",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "caliber_reconciliation": {
            "tool": RECONCILE_SCRIPT,
            "report": RECONCILE_JSON,
            "sentences": 2369,
            "traversal_units": 171,
            "user_records": 125,
            "history_messages": 119,
            "excluded_parallel_session": 6,
            "claims_frozen": 2396,
            "owners_identical_count": 22,
            "owners_identical_rows": 2268,
            "owners_grown": {"理解章节/README.md": [46, 60], "理解章节/C0-当前整合审计与证据边界-20260912.md": [82, 91]},
            "current_surface_rows": 4547,
            "c_series_increment": 2128,
        },
        "batch4": {
            "rule": "authors by prior sampling ratio ascending, 40-budget, max 5 per owner, equidistant, batches 1-3 excluded",
            "sample_size": 40,
            "owners": ["理解章节/A8-材料与保全.md", "理解章节/A0-总目标.md", "理解章节/B3-网页GPT工作史-II.md",
                        "理解章节/A5-HoTT怀疑演进.md", "理解章节/读遍账本.md", "理解章节/升级方案-v2.md",
                        "理解章节/A10-怎么找.md", "理解章节/A2-参照悖论谱.md"],
            "verdicts": {"SUPPORTED": 28, "SUPERSEDED_BY_MACHINE_RESULT": 0, "UNSUPPORTED": 0, "PENDING": 12},
            "cumulative": {"sampled": 162, "coverage": "6.76%", "SUPPORTED": 93, "SUPERSEDED": 12, "UNSUPPORTED": 0, "PENDING": 57},
            "e6_found": False,
        },
        "spot_checks": {"tool": SPOT_SCRIPT, "report": SPOT_JSON, "passed": 14, "failed": 0},
        "evidence": {"report": REPORT, "sample": SAMPLE_JSON},
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
            "This in-scope checkpoint records the N15 caliber reconciliation (read-only recount of 2369/171/125/119/2396/4547; "
            "22/24 owners reproduce exactly; README/C0 growth) and the batch-4 proportional sample (40 claims; 28/0/0/12; cumulative "
            "162/2396 with no UNSUPPORTED and no E6). It routes N16 (queue continuation). No new mathematical claim, no Git commit, "
            "tag or push."
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
        "revision": 61,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
