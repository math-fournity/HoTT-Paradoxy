#!/usr/bin/env python3
"""Prepare revision 57: record the N12 evidence-queue sample review and route T4.

S057 ran the bounded N12 sample: 30 equal-spaced keyword-selected claims plus
10 equal-spacing fill claims (40 of 2,396; 1.67%), each given a sentence-level
verdict (SUPPORTED 13 / SUPERSEDED_BY_MACHINE_RESULT 7 / UNSUPPORTED 0 /
PENDING 20).  No E6 (natural-use chain) surfaced.  The next work package is
T4: the fifth-layer consumer audit (ownership claims of self-verification).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-057-EVIDENCE-QUEUE-SAMPLE"
PREV_SESSION = "S-RES-20260912-056-A-DIRECTION-CANDIDATES"
RESULT_ID = "A-EVIDENCE-QUEUE-SAMPLE-001"
REPORT = "audit/understanding-claims-sampling-20260912.md"
SAMPLE = "audit/understanding-claim-sample-20260912.json"
SCRIPT = "scripts/audit/sample_understanding_claims.py"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [REPORT, SAMPLE, SCRIPT]
NEW_STATUS = "EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_evidence_sample", RUNTIME_PATH)
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
        "KC-000005": ("ALIGNED", "S057 的抽样复核保持‘先找悖论后归因’的顺序，不把历史叙述升级为结论。"),
        "KC-000007": ("PENDING_NOTE", "用户对 LLM 模式匹配的期待在 S057 中体现为：历史主张需句级裁决而非模式匹配。"),
        "KC-000012": ("DEEPENED", "ASK 资格分析的历史主张在样本中被分类为 SUPERSEDED/PENDING，与 C8/C9/C10 一致。"),
        "KC-000013": ("ALIGNED", "理论经济的历史表述在样本中由机器结果接管（cost/商下降），无 UNSUPPORTED。"),
        "KC-000021": ("ALIGNED", "抽样脚本与报告均落盘可复跑；未把未运行项升级。"),
        "KC-000025": ("ALIGNED", "‘为什么慢’在 S057 中获得证据队列层面的解释：大量历史主张仍 PENDING。"),
        "KC-000035": ("ALIGNED", "HoTT 能否表达本项目理论的问题不受抽样影响，保持分层记录。"),
        "KC-000036": ("ALIGNED", "E6 未出现，ERCF/W51/A 的 gated 状态不变。"),
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
            ("NOT_TOUCHED", "本轮是 S057 证据队列有界抽样复核；未研究、改写或重新裁决该条用户原文。"),
        )
        if relation in ("ALIGNED", "DEEPENED"):
            pass
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S057/SESSION.md；{REPORT} | T4 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N12 完成（40/2,396 样本，无 UNSUPPORTED、无 E6）；第一工作包转 T4 第五层 consumer 审计；revision 57/generation 041。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-EVIDENCE-QUEUE-SAMPLE`（理解章节 inventory 不变，audit/ 资产）。",
        "- update_decision: `抽样报告与机器可读样本进入 audit/ 与 session evidence；抽样脚本可复跑；不新增 claim matrix 行。`",
        "- cross_conflicts: `NONE_OBSERVED` — 样本结论与 C8/C9/C10 的 E6 缺口一致。",
        "- unresolved: `证据队列余下 ~98% 主张、T4、E6、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `BOUNDED_SAMPLE_WITH_PENDING_MAJORITY`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S056 路由的第一工作包 N12（证据队列有界推进）。",
        "- 抽样规则（`scripts/audit/sample_understanding_claims.py`，确定性）：关键词层 134 条等距封顶 30 条 + 等距补足 10 条 = 40 条（2,396 的 1.67%）。",
        "- 判词分布：`SUPPORTED=13`、`SUPERSEDED_BY_MACHINE_RESULT=7`、`UNSUPPORTED=0`、`PENDING=20`；PENDING 集中在解释性/框架表述、历史叙述与口径类条目。",
        "- E6 检查：样本内未出现 natural-use chain；`CL-001577`（B01-TARGET OPEN）与 `CL-000612`（W51 第三层待补）均确认尚无真实接口。",
        "- 产出：`audit/understanding-claims-sampling-20260912.md`（逐条判词表）+ `audit/understanding-claim-sample-20260912.json`（机器可读样本）。",
        "- 边界：只支持本次抽样范围内结论；不宣称 2,396 条全量裁决；不新增数学 claim；未发现 E6 故未触发 F-011。",
        "- 三件套：direction/panorama revision 57/generation 041；core 不变；无 理解章节 变更（merge manifest 不重建）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT`",
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 56", "source_state_revision: 57")
    direction = sub_once(direction, "projection_generation: 20260912-direction-040", "projection_generation: 20260912-direction-041")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT",
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N12 证据队列有界推进——按固定规则从 2,396 条 understanding claim 中抽样（含 `univalence`/`HIT`/`truncation`/`Cauchy`/`SIP`/`cost` 关键词者全部入选，另按行号等距补足），逐条给出句级判词（`SUPPORTED` / `UNSUPPORTED` / `SUPERSEDED_BY_MACHINE_RESULT` / `PENDING`）与证据边界；若抽样中发现自然使用链（E6），立即转 F-011 机器化。备选（ERCF 线）：T4 第五层 consumer 审计。",
        "4. **当前第一工作包**：T4 第五层 consumer 审计——固定版本审计真实系统（证明助手/库/论文承诺）对“自证/已验证交付”的声明是否满足 C9 §4 四条件（真实性、资格越级、无新增假设、可核查性）；满足则转 F-011 机器化并按 `NATURAL_USAGE_MISMATCH` 候选处理；不满足则把围栏记入审计并回到证据队列第二批抽样（按 owner 文档分层）。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT`",
        "状态：`CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 56", "source_state_revision: 57")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-040", "projection_generation: 20260912-outcome-041")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT",
        "semantic_status: CORE_GENERATION_4_EVIDENCE_QUEUE_SAMPLE_REVIEWED_T4_CONSUMER_AUDIT_NEXT",
    )
    row = (
        "| `OUT-TOP-EVIDENCE-QUEUE-SAMPLE` | S057 N12 证据队列有界抽样——固定规则抽样 40/2,396（关键词层 134 条等距封顶 30 + 等距补足 10）；逐条句级判词：`SUPPORTED=13`、`SUPERSEDED_BY_MACHINE_RESULT=7`、`UNSUPPORTED=0`、`PENDING=20`；样本内未出现 E6 |"
        " `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工抽样复核 + 确定性脚本 | `DOCUMENTED / BOUNDED_SAMPLE_WITH_PENDING_MAJORITY` |"
        " 7 条历史主张已被机器结果接管（cost/商下降/race/W51）；20 条 PENDING 需句级裁决或历史重核；负结论只覆盖本次抽样 |"
        " 不宣称 2,396 条全量裁决；不新增数学 claim；PENDING 不得被当作支持或否证 |"
        " `audit/understanding-claims-sampling-20260912.md`；`audit/understanding-claim-sample-20260912.json`；`scripts/audit/sample_understanding_claims.py` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "S056 的 N11 把 13 个 A 方向候选归约为三类并判 `A_DIRECTION_BOUNDED_NEGATIVE`；R032 回放、",
        "S056 的 N11 把 13 个 A 方向候选归约为三类并判 `A_DIRECTION_BOUNDED_NEGATIVE`；S057 的证据队列首批抽样（40/2,396）无 `UNSUPPORTED`、无 E6，7 条历史主张由机器结果接管；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S056 的 N11 生成 13 个 A 方向候选并把它们归约为三类（表示/资格边界、通用边界、元层/工具链观察），判 `A_DIRECTION_BOUNDED_NEGATIVE`，升级唯一口 = E6。所有新结论继续执行 F-011。",
        "S056 的 N11 生成 13 个 A 方向候选并把它们归约为三类（表示/资格边界、通用边界、元层/工具链观察），判 `A_DIRECTION_BOUNDED_NEGATIVE`，升级唯一口 = E6；S057 的证据队列首批抽样（40/2,396）无 `UNSUPPORTED`、无 E6。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N12 证据队列有界推进 | fixed-rule sample review | 固定抽样规则（关键词全选 + 行号等距补足）；逐条句级判词与证据边界；发现 E6 即转 F-011；备选 T4 |",
        "| 已闭合工作包 15 | 证据队列首批抽样（S057，N12） | `BOUNDED_SAMPLE_WITH_PENDING_MAJORITY` | 40/2,396；`SUPPORTED=13`/`SUPERSEDED=7`/`UNSUPPORTED=0`/`PENDING=20`；无 E6 |\n"
        "| 第一工作包 | T4 第五层 consumer 审计 | fixed-version consumer audit | 按 C9 §4 四条件审计真实系统对“自证/已验证交付”的声明；满足转 F-011；否则回证据队列第二批（按 owner 分层） |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N12 证据队列有界推进：按固定规则从 2,396 条 understanding claim 中抽样（含 univalence/HIT/truncation/Cauchy/SIP/cost 关键词者全部入选，另按行号等距补足），逐条给出句级判词（SUPPORTED / UNSUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / PENDING）与证据边界；若抽样中发现自然使用链（E6），立即转 F-011 机器化。备选（ERCF 线）：T4 第五层 consumer 审计。",
        "2. 当前第一工作包转为 T4 第五层 consumer 审计：固定版本审计真实系统（证明助手/库/论文承诺）对“自证/已验证交付”的声明是否满足 C9 §4 四条件；满足则转 F-011 并按 NATURAL_USAGE_MISMATCH 候选处理；不满足则记围栏并回到证据队列第二批抽样（按 owner 文档分层）。",
    )
    memory = sub_once(
        memory,
        "- S056 完成 N11（A 方向候选生成）：",
        "- S057 完成 N12 首批抽样复核：`audit/understanding-claims-sampling-20260912.md` + `audit/understanding-claim-sample-20260912.json`（40/2,396，固定规则：关键词层 134 条等距封顶 30 + 等距补足 10）；判词 `SUPPORTED=13`、`SUPERSEDED_BY_MACHINE_RESULT=7`、`UNSUPPORTED=0`、`PENDING=20`；样本内无 E6（`CL-001577` 复核 B01-TARGET 仍 OPEN）；下一工作包转 T4 第五层 consumer 审计。\n"
        "- S056 完成 N11（A 方向候选生成）：",
    )
    memory = sub_once(
        memory,
        "`A-A-DIRECTION-CANDIDATES-001`。",
        "`A-A-DIRECTION-CANDIDATES-001`、`A-EVIDENCE-QUEUE-SAMPLE-001`。",
    )
    memory = sub_once(
        memory,
        "S056 完成 N11 并把 A 方向候选收口为 `A_DIRECTION_BOUNDED_NEGATIVE`（升级唯一口 = E6），转 N12 证据队列，不直接跳 ERCF-3 构造。",
        "S056 完成 N11 并把 A 方向候选收口为 `A_DIRECTION_BOUNDED_NEGATIVE`（升级唯一口 = E6）；S057 完成证据队列首批抽样（无 UNSUPPORTED、无 E6）并转 T4 第五层 consumer 审计，不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S057 完成 N12 首批抽样复核：`scripts/audit/sample_understanding_claims.py` 以固定规则抽取 40/2,396 条 understanding claim（关键词层 134 条等距封顶 30 条 + 等距补足 10 条），逐条判词为 `SUPPORTED=13`、`SUPERSEDED_BY_MACHINE_RESULT=7`、`UNSUPPORTED=0`、`PENDING=20`；样本内无 E6（`CL-001577` 复核 B01-TARGET 仍 OPEN），故未触发 F-011。报告 `audit/understanding-claims-sampling-20260912.md`，机器可读样本 `audit/understanding-claim-sample-20260912.json`；本轮未改 理解章节（merge manifest 不重建）。下一工作包为 T4 第五层 consumer 审计（按 C9 §4 四条件）；备选证据队列第二批（按 owner 文档分层）。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "55. 候选生成要有“必填门槛”和“归约表”：",
        "56. 证据队列的“有界推进”要靠固定抽样规则而不是穷举：关键词层全选中位后等距封顶、剩余层等距补足，样本量取 40/2,396（1.67%），逐条给四值判词（SUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / UNSUPPORTED / PENDING）。实测分布（13/7/0/20）说明：历史主张的主要缺口不是“被否证”，而是解释性表述与历史叙述尚未句级裁决；机器结果已经接管的那部分（cost、商下降、race、W51）可以安全地从 PENDING 池移出。抽取脚本必须确定性、可复跑，报告只支持样本范围结论。\n"
        "55. 候选生成要有“必填门槛”和“归约表”：",
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
    if state.get("revision") != 56 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_56_AND_S056")
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
        "Revalidated after the S057 evidence-queue sample review; no proof source, run, claim-matrix row or understanding-chapter file changed."
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
        "classification": "BOUNDED_SAMPLE_WITH_PENDING_MAJORITY",
        "research_parent": "A-HISTORICAL-MATH-CLAIMS-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [REPORT, SAMPLE, SCRIPT, "audit/claim-evidence-ledger.jsonl",
                         "audit/cross-source-reconciliation.json", MATRIX],
        "source_hashes": {REPORT: new_hashes[REPORT], SAMPLE: new_hashes[SAMPLE], SCRIPT: new_hashes[SCRIPT]},
        "resolution": {
            "reason": "40 of 2,396 claims sampled by a deterministic fixed rule; verdict distribution SUPPORTED 13 / SUPERSEDED_BY_MACHINE_RESULT 7 / UNSUPPORTED 0 / PENDING 20; no E6 surfaced, so no F-011 packaging was triggered.",
            "evidence": [REPORT, SAMPLE, SCRIPT],
        },
        "scope": "Bounded sample review of the understanding claims (first batch): fixed sampling rule, per-claim verdicts, distribution, and the E6 check. Conclusions hold for the sampled 40 claims only.",
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
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_EVIDENCE_QUEUE_SAMPLE",
        "cognition_status": "EVIDENCE_QUEUE_SAMPLE_REVIEWED_AND_T4_ROUTED",
        "scope": "First bounded evidence-queue sample review (N12) and routing of the T4 fifth-layer consumer audit.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-041" if rid.startswith("I-DIRECTION") else "20260912-outcome-041"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (REPORT, SAMPLE):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N12 sample review: no UNSUPPORTED, no E6; the first work package is the T4 fifth-layer consumer audit."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the N12 bounded sample review (40/2396; pending majority); the next strand is T4."
    )

    state["revision"] = 57
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "T4 fifth-layer consumer audit: in a fixed version set, audit real systems (proof assistants / libraries / paper claims) that assert self-verification or verified delivery, "
            "against the four conditions of C9 section 4 (real and retrievable; qualification escalation on the same task; no added assumptions; machine-checkable). "
            "If a candidate satisfies them, switch to F-011 packaging and treat it as a NATURAL_USAGE_MISMATCH candidate. "
            "Otherwise record the fences and return to a second evidence-queue batch stratified by owner document."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "review_kind": "evidence_queue_bounded_sample",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "sample": {
            "total_claims": 2396,
            "keyword_stratum_hits": 134,
            "keyword_cap": 30,
            "fill": 10,
            "sample_size": 40,
            "coverage": "1.67%",
            "verdicts": {"SUPPORTED": 13, "SUPERSEDED_BY_MACHINE_RESULT": 7, "UNSUPPORTED": 0, "PENDING": 20},
            "e6_found": False,
            "notes": "CL-001577 confirms B01-TARGET remains OPEN; CL-000612 (W51 third layer) superseded by C9.",
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
            "This in-scope checkpoint records the N12 bounded evidence-queue sample review (40/2396; no UNSUPPORTED, no E6), "
            "and routes the T4 fifth-layer consumer audit. No new mathematical claim, no Git commit, tag or push."
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
        "revision": 57,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
