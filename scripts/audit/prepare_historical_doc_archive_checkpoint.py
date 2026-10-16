#!/usr/bin/env python3
"""Prepare revision 16 for user-authorized historical-governance document archival."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-016-HISTORICAL-DOC-ARCHIVE"
OLD_PLAN = "实施方案-三件套研究连续性治理与理解章节融合-20260912.md"
OLD_COMPARISON = "治理框架对比审计与核心认知增补评估-20260912.md"
ARCHIVE_PREFIX = "history/governance-v2.1.0/"
NEW_PLAN = ARCHIVE_PREFIX + OLD_PLAN
NEW_COMPARISON = ARCHIVE_PREFIX + OLD_COMPARISON

SPEC = importlib.util.spec_from_file_location("runtime_historical_archive", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_historical_sources(state: dict) -> dict[str, int]:
    """Migrate current registry consumers while leaving immutable checkpoint copies untouched."""
    counts = {OLD_PLAN: 0, OLD_COMPARISON: 0}
    replacements = {OLD_PLAN: NEW_PLAN, OLD_COMPARISON: NEW_COMPARISON}
    for record in state["records"].values():
        sources = record.get("full_sources")
        if not isinstance(sources, list):
            continue
        for index, source in enumerate(sources):
            if source in replacements:
                counts[source] += 1
                sources[index] = replacements[source]
    expected = {OLD_PLAN: 1, OLD_COMPARISON: 2}
    if counts != expected:
        raise ValueError(f"HISTORICAL_SOURCE_REPLACEMENT_COUNT:{counts}:expected={expected}")
    return counts


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | "
            "本轮只迁移已退出 current truth 的 generation-2 治理文档及其当前路径 consumer，没有改变、深化或裁决该用户原文。 | "
            "history/README.md; 方向追踪.md; .codex/research/hott/STATE.json; README.md | "
            "该 KC 的数学真值与现实解释仍由后续研究负责。 |"
        )
    lines.extend(
        [
            "",
            "## 三件套交叉与更新归属",
            "",
            "- core_change: `NO` — generation-3 core/manifest/curation/transition 均不变；历史归档授权属于治理裁定。",
            "- direction_change: `NO_RESEARCH_SEMANTIC_CHANGE` — 只把理解章节融合方向的旧方案 locator 改为可解析的 history 路径并同步 revision 16。",
            "- panorama_change: `NO_RESEARCH_RESULT_CHANGE` — 只登记历史路径收敛和 revision 16 checkpoint。",
            "- update_decision: `治理授权写入 rulings；历史文档与 replacement 写入 history/README；当前 consumer 经 direction/STATE 原位迁移。`",
            "- cross_conflicts: `NONE_AFTER_CURRENT_CONSUMER_MIGRATION`；不可变旧 checkpoint 内的旧路径保留为当时历史证据。",
            "- unresolved: `fresh model behavior、数学认证、aistudio coverage、2,396 claim 语义。`",
            "",
            "## 汇总",
            "",
            "`NOT_TOUCHED=27`；本轮没有数学研究，也没有把治理归档动作注入 core。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    for relative in (NEW_PLAN, NEW_COMPARISON, "history/README.md"):
        if not (root / relative).is_file():
            raise SystemExit(f"ARCHIVED_TARGET_MISSING:{relative}")
    for relative in (OLD_PLAN, OLD_COMPARISON):
        if (root / relative).exists():
            raise SystemExit(f"OLD_TOP_LEVEL_PATH_STILL_EXISTS:{relative}")

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 15:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_15")

    direction = replace_once(
        (root / R.DIRECTION).read_text(encoding="utf-8"),
        "source_state_revision: 15",
        "source_state_revision: 16",
    )
    direction = replace_once(direction, f"`{OLD_PLAN}`", f"`{NEW_PLAN}`")

    panorama = replace_once(
        (root / R.PANORAMA).read_text(encoding="utf-8"),
        "source_state_revision: 15",
        "source_state_revision: 16",
    )
    panorama = replace_once(
        panorama,
        "revision 15 final checkpoint",
        "revision 16 historical-document archive checkpoint",
    )

    memory = replace_once(
        (root / "MEMORY.md").read_text(encoding="utf-8"),
        "1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现，已由 S013 完成主迁移、S014 收口旧主题引用，并由 `S-GOV-20260912-015-FINAL-STATE-ALIGNMENT` revision 15 统一当前 receipt/owner 文字；本轮不启动数学研究。",
        "1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现：S013 完成主迁移，S014 收口旧主题，S015 对齐 current owner，`S-GOV-20260912-016-HISTORICAL-DOC-ARCHIVE` revision 16 完成用户授权的两份 generation-2 治理文档 Git rename 归档和当前 consumer 路由；本轮不启动数学研究。",
    )
    memory = replace_once(
        memory,
        "- 默认 governance/research profile 均为 15/20 documents，三件套固定前三项、历史 Session 自动加载=0；当前精确 bytes/lines/snapshot 由 revision 15 的 `audit/fresh-three-way-verification-20260912.json` 持有，MEMORY 不复制易漂移数值。",
        "- 默认 governance/research profile 均为 15/20 documents，三件套固定前三项、历史 Session 自动加载=0；当前精确 bytes/lines/snapshot 由与 STATE 当前 revision 对齐的 `audit/fresh-three-way-verification-20260912.json` 持有，不一致时必须重生成，MEMORY 不复制易漂移数值。",
    )

    frontier = replace_once(
        (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
        "完成 revision 15 后运行 fresh/full regression 并精确 Git/tag",
        "完成 revision 16 历史路径收敛后运行 fresh/full regression 并精确 Git/tag",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip() + (
        "\n17. 已退出 current truth 的文档 rename 归档时，必须迁移当前 README/方向/STATE consumer 与 replacement；不可变 checkpoint 中的旧路径保留为当时证据。原始 pack 的 `archive/` 与叙事治理史的 `history/` 职责不同。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "revision 15 checkpoint 构成本轮交付",
        "revision 16 historical-document archive checkpoint 构成本轮交付",
    )

    replaced_counts = replace_historical_sources(state)
    state["revision"] = 16
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "status": "CORE_GENERATION_3_LAYERED_LOAD_V3_HISTORICAL_ROUTES_ALIGNED",
            "checkpoint_result": "CHECKPOINT_COMMITTED",
        }
    )
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-015-FINAL-STATE-ALIGNMENT"],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            "history/README.md",
            NEW_PLAN,
            NEW_COMPARISON,
            "方向追踪.md",
            "README.md",
        ],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "cognition_status": "HISTORICAL_GOVERNANCE_DOCUMENT_ROUTES_ALIGNED",
        "scope": "Archive two superseded generation-2 governance reports by Git rename and migrate current consumers; no mathematics.",
    }

    session = f"""# {SESSION_ID}

- 用户授权：`可以rename历史文件，直接放入归档目录中。`
- 变更：两份 generation-2 报告已由顶层 rename 到 `history/governance-v2.1.0/`，保留 current replacement；方向和当前 STATE consumer 改用新路径。
- 保留：immutable checkpoint/session 内旧路径继续表示当时现场；`archive/` 原始 pack store 不被混用；generation-3 core 与全部数学结果不变。
- 完成后：重跑 fresh Python、projection freshness、core/three-way/runtime/reader/history/merge/reconciliation、路径残留和 Git checks。
- 边界：fresh model behavior 与数学证明仍 NOT_RUN/NOT_CERTIFIED。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "pre_checkpoint": {
                "state_revision": 15,
                "git_renames": {OLD_PLAN: NEW_PLAN, OLD_COMPARISON: NEW_COMPARISON},
                "current_state_consumer_replacements": replaced_counts,
                "current_direction_consumer_replacements": 1,
            },
            "post_checkpoint_required": [
                "fresh-three-way v2",
                "projection freshness",
                "full regression",
                "current-path residual scan",
                "git diff/status",
            ],
            "model_behavior": "NOT_RUN",
            "mathematics": "UNCHANGED",
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n"

    texts = {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session,
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly authorized renaming historical files into an archive directory; project-local history/ is the existing narrative-history owner.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": relative,
                "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None,
                "text": value,
            }
            for relative, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "session_id": SESSION_ID,
                "revision": 16,
                "files": len(texts),
                "current_consumer_replacements": {"state": replaced_counts, "direction": 1},
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
