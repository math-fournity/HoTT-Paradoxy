#!/usr/bin/env python3
"""Prepare revision 119: register the technical report written for external audit."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-119-AUDIT-REPORT-FOR-EXTERNAL-AUDIT"
PREV = "S-RES-20260913-118-ERCF3-T3-REPAIRED-SYNTAX"
RESULT_ID = "A-AUDIT-REPORT-TONGGUAN-001"
REPORT = "audit/统观工作技术报告-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s119", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "本报告把「证据纪律/交付等级」写成可审计条目（含 14 条已知弱点），不新增结论。"),
    "KC-000017": ("ALIGNED", "报告要求每条事实性主张给出文件/claim/run/提交锚点，并列出未验证部分。"),
    "KC-000005": ("ALIGNED", "报告区分 MACHINE_PROVED / VERIFIED_WITH_SCOPE / PAPER_ONLY / DOCUMENTED，不互相冒充。"),
    "KC-000014": ("ALIGNED", "报告逐段写明义务边界（编码已闭合 vs 表示性未做）。"),
    "KC-000030": ("ALIGNED", "报告如实登记停点：编码线自足部分收口，其余等外部输入。"),
    "KC-000036": ("ALIGNED", "报告明确 T3 机械部分预计为 GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC，不升级为 HoTT 特有结论。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是**审计输入撰写**（把统观线整理为可外部审计的技术报告），不产生新的数学或理论结论。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = AUDIT_FOCUS.get(
            kid, ("NOT_TOUCHED", f"本轮没有研究或重新裁决「{label}」的数学/哲学内容。")
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{REPORT}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO — 报告不改方向行（无新研究方向或优先级变化）。",
        "- panorama_change: NO — 报告不新增成果行（它是对已登记成果的复核叙述）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 新增一个审计输入产物并登记其记录；研究停点与门 A/门 B 状态不变。",
        "- cross_conflicts: 报告显式登记 14 条已知弱点（含扫描 JSON 与报告数字的规则版本差异）。",
        "- unresolved: 外部审计意见未回收；表示性/反射/对角不动点未做；门 A/门 B 仍等外部输入。",
        "",
        "## 汇总",
        "",
        f"`ALIGNED={aligned}`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 118 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_118_S118")
    if not (root / REPORT).is_file():
        raise SystemExit("REPORT_MISSING")

    mem = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        mem,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S119 审计输入：`audit/统观工作技术报告-20260913.md`（rev119 撰写，`DOCUMENTED`）。"
        "内容：统观线（Astra 轨迹审计 → C11 账本 v2 → P1/P2/P3 + 18 包回溯 + 粗域扫描 → triage 关闭 → "
        "自主构造三轮 → 两扇门收口 → C11 评审吸收 → T3 编码链 C-157–C-183）的完整技术报告，"
        "含证据锚点、14 条已知弱点、18 条审计问题清单、复现命令、claim↔包↔run 对照表。"
        "本轮不新增数学 claim、不改判词、不动三件套/四件套；停点与门 A/门 B 状态不变。\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户请求：把「从统观开始」的工作完整写成一份技术报告，供外部 AI 审计。
- 交付：`{REPORT}`（单文件、自包含；含 §0 摘要、§1–§9 时间线与方法、§10 已知弱点、§11 审计问题清单、
  §12 复现命令、§13 术语表、附录 A/B）。
- 性质：`CURRENT_WORK_PACKAGE_REPORT / AUDIT_INPUT`；不新增数学 claim、不改判词、不升级任何等级。
- 记录：`{RESULT_ID}`（`DOCUMENTED`，路径 {REPORT}）。
- 边界：报告内所有事实性主张均给锚点（文件路径 / claim ID / run ID / 提交）；未回收外部意见；
  表示性/反射/对角不动点未做；ERCF-3 保持 `GATED`；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "deliverable": {
                "kind": "audit_input_report",
                "path": REPORT,
                "evidence_status": "DOCUMENTED",
                "covers": [
                    "audit/astra-1-astra-2会话轨迹审计-20260913.md",
                    "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md",
                    "audit/p1-时序线候选与支付装置审计-20260913.md",
                    "audit/p2-p3与粗域接口搜索-20260913.md",
                    "audit/triage批次与自主构造第一轮-20260913.md",
                    "audit/自主构造第二轮-识别不敏感与相干义务-20260913.md",
                    "audit/自主构造第三轮-表达与身份两轴-20260913.md",
                    "audit/c11评审吸收与独立核验-20260913.md",
                    "HoTT/formal/ercf3-t3/README.md",
                    "HoTT/CLAIM_EVIDENCE_MATRIX.md",
                ],
            },
            "new_math_claims": [],
            "verdict_changes": [],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 119
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_AUDIT_REPORT_FOR_EXTERNAL_AUDIT",
            "status": STATUS,
            "next_minimal_verification": (
                "The user is handing `audit/统观工作技术报告-20260913.md` to an external AI for audit. Until that audit "
                "comes back, do not add more T3 coding-side work: the self-contained coding line is closed (codings at both "
                "levels C-176/C-180, substitution/quotation shapes C-181-C-183). When the external findings arrive, absorb "
                "them with the same procedure used for the C11 review: byte-preserved import, item-by-item independent "
                "verification, in-place revision, corrective re-pin, all six verifiers. The remaining research obligations "
                "(object-level representability, proof-predicate representability, reflection, diagonal fixed point) still "
                "need the door-B consumer; ERCF-3 stays GATED."
            ),
        }
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [
            SESSION_ID,
            "A-THEORY-ECONOMY-LEDGER-001",
            "A-AUTONOMOUS-ROUND3-001",
            "A-C11-REVIEW-ABSORPTION-001",
            "A-ERCF3-T3-REPAIRED-SYNTAX-001",
        ],
        "full_sources": [
            REPORT,
            "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md",
            "audit/自主构造第三轮-表达与身份两轴-20260913.md",
            "HoTT/formal/ercf3-t3/README.md",
        ],
        "source_hashes": {REPORT: R.sha((root / REPORT).read_bytes())},
        "scope": (
            "Technical report for external audit covering the panoramic ('统观') workline from the Astra-1/Astra-2 "
            "trajectory audit through the C11 economy ledger (v2), P1/P2/P3 and the 18-package retrodiction, the coarse "
            "consumer scan and triage closure, the three autonomous-construction rounds, the two-door closure, the C11 "
            "review absorption, and the T3 coding chain (C-157-C-183). It states no new mathematical claim, changes no "
            "verdict, and explicitly lists 14 known weaknesses and 18 audit questions. It is DOCUMENTED, not machine-proved."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REPORT],
        "source_hashes": {},
        "scope": (
            "Registration of the external-audit input report: session records, a DOCUMENTED result record with the report "
            "hash, and a sequence-log entry. No research fact, verdict, projection or claim changed."
        ),
    }

    # The checkpoint requires *every* MUTABLE document in the payload: the ones
    # this session does not edit are passed through with their current bytes.
    texts: dict[str, str] = {rel: (root / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    texts[mem["index_path"]] = mem["index_text"]
    texts.update(mem["shards"])
    for rel in (R.DIRECTION, R.PANORAMA, R.ESSAY):
        texts.update(projection_edit.load(root, rel)["shards"])
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User request: write a complete technical report of the work starting from the panoramic survey ('统观'), so "
            "that an external AI can audit it. This checkpoint registers the report (hash-pinned), the session records and "
            "a sequence-log entry. No new claim, no verdict change, no push."
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
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 119,
                "session_id": SESSION_ID,
                "files": len(texts),
                "report_sha256": R.sha((root / REPORT).read_bytes())[:16],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
