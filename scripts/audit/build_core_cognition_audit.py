#!/usr/bin/env python3
"""Create a full per-KC end-of-session assessment for a named session.

The generated assessment is intentionally conservative.  It does not use
semantic similarity to claim that a mathematical insight was proved.  For the
current integration session it marks governance/evidence/continuity KC units
as deepened because concrete audit assets were created, and marks all other
units as not touched by new mathematical reasoning.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--session-id", default="S-INTEGRATION-20260912-001")
    args = parser.parse_args()
    root = args.project_root.resolve()
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    units = manifest.get("units", [])
    target = root / ".codex/research/hott/sessions" / args.session_id / "CORE_COGNITION_AUDIT.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# 核心认知逐编号回评：{args.session_id}",
        "",
        "> 本回评针对本次“顶层 repo 初始化、来源固化、核心账本生成、历史 ledger 和本地治理搭建”工作单元。它不是数学证明，也不以关键词命中认证 AI 理解。",
        f"> 生成时间：{datetime.now(timezone.utc).isoformat()}；输入 generation：`{manifest.get('generation')}`；KC 总数：`{len(units)}`。",
        "",
        "## 判定枚举",
        "",
        "`DEEPENED` = 本轮把用户已提出的交接/证据/连续性要求落成了可复核资产；`ALIGNED` = 遵守但没有新增理解；`NOT_TOUCHED` = 本轮没有对相应数学/业务主张做新推演；`TENSION`/`CORRECTED`/`DEVIATED` 只在证据支持时使用。",
        "",
        "## 全量逐编号表",
        "",
        "| KC | 来源 | 主题 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|---|",
    ]
    counts = {key: 0 for key in ("DEEPENED", "ALIGNED", "CORRECTED", "TENSION", "DEVIATED", "NOT_TOUCHED")}
    governance_themes = {"HANDOFF_GOVERNANCE", "SESSION_CONTINUITY", "EVIDENCE_DISCIPLINE"}
    for unit in units:
        themes = set(unit.get("themes", []))
        if themes & governance_themes:
            relation = "DEEPENED"
            assessment = "本轮将该交接/连续性/证据要求落成 core manifest、历史 ledger、runtime 或逐编号回评入口；没有改写该 KC 原文，也没有把它提升为数学认证。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本轮是来源保全与治理整合，没有对该 HoTT/悖论业务主张进行新的合法推演、反解释或现实桥梁验证；原文仅被保留并建立定位。"
        if unit.get("author_class") == "USER_RELAYED_CONTEXT":
            assessment += " 该单元在来源中是 USER_RELAYED_CONTEXT，本轮不将其冒充用户已采纳结论。"
        counts[relation] += 1
        source = str(unit.get("source_locator", "")).replace("|", "\\|")
        themes_text = ", ".join(unit.get("themes", [])) or "—"
        lines.append(
            f"| `{unit['id']}` | `{unit.get('platform')}` / `{unit.get('timestamp_original')}` | {themes_text} | `{relation}` | {assessment} | `{source}`; `audit/ledger-summary.json` | 数学真值、外部覆盖和 AI 理解仍需独立核验。 |"
        )
    lines.extend(
        [
            "",
            "## 本轮总评",
            "",
            f"本轮逐一处理了 `{len(units)}` 个 KC：`{json.dumps(counts, ensure_ascii=False, sort_keys=True)}`。没有 `DEVIATED`、`CORRECTED` 或 `TENSION` 的证据性判定；这不等于所有历史观点一致，而是本轮没有进行足以裁决它们的数学工作。后续历史章节修订必须把 ledger 的可见回答、工具事件、代码/Git 和当前理解逐条连回这些 KC。",
            "",
            "全量机械结构可由 `scripts/audit/verify_core_cognition.py` 验证；逐编号语义回评由本文件的公开文字承担，脚本不把它认证为模型理解。",
            "",
        ]
    )
    target.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"status": "BUILT", "session_id": args.session_id, "kc_count": len(units), "relation_counts": counts, "path": str(target)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
