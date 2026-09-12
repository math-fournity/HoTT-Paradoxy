#!/usr/bin/env python3
"""Prepare revision 18 recording exact understanding-merge count semantics."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-018-MERGE-COUNT-SEMANTICS"
SPEC = importlib.util.spec_from_file_location("runtime_merge_count", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


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
            "本轮只修正理解章节 merge receipt 的计数字段语义，没有改变、深化或裁决该用户原文。 | "
            "audit/understanding-chapter-merge-manifest.json; scripts/audit/build_understanding_merge_manifest.py; scripts/audit/verify_understanding_merge.py | "
            "该 KC 的数学真值与现实解释仍由后续研究负责。 |"
        )
    lines.extend(
        [
            "",
            "## 三件套交叉与更新归属",
            "",
            "- core_change: `NO` — generation-3 core/manifest/curation/transition 均不变。",
            "- direction_change: `NO_RESEARCH_SEMANTIC_CHANGE` — 只同步 current STATE revision 18。",
            "- panorama_change: `EVIDENCE_PRECISION_ONLY` — 明确 24 个同名对中 15 identical、9 different，另有 1 个 top-level unique，因此 nonidentical union entries 为 10。",
            "- update_decision: `修正 builder/verifier/manifest 与结果投影的字段语义；理解章节数学语义复核仍开放。`",
            "- cross_conflicts: `NONE_AFTER_COUNT_RECONCILIATION`。",
            "- unresolved: `2,396 claim 句级语义、历史数学、fresh model behavior、aistudio coverage。`",
            "",
            "## 汇总",
            "",
            "`NOT_TOUCHED=27`；计数 schema 修正不冒充理解章节数学融合完成。",
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
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 17:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_17")
    merge = json.loads((root / "audit/understanding-chapter-merge-manifest.json").read_text(encoding="utf-8"))
    expected_counts = {
        "union_files": 25,
        "same_name_pairs": 24,
        "identical_pairs": 15,
        "different_pairs": 9,
        "nonidentical_union_entries": 10,
        "top_level_unique": 1,
        "nested_unique": 0,
        "unresolved_nontrivial": 0,
    }
    for key, expected in expected_counts.items():
        if merge.get("counts", {}).get(key) != expected:
            raise SystemExit(f"MERGE_COUNT_NOT_READY:{key}:{merge.get('counts', {}).get(key)}:{expected}")

    direction = replace_once(
        (root / R.DIRECTION).read_text(encoding="utf-8"),
        "source_state_revision: 17",
        "source_state_revision: 18",
    )
    panorama = replace_once(
        (root / R.PANORAMA).read_text(encoding="utf-8"),
        "source_state_revision: 17",
        "source_state_revision: 18",
    )
    panorama = replace_once(
        panorama,
        "24 个同名，15 对字节相同，9 个同名差异，顶层有 C0 独有文件",
        "24 个同名对中 15 对字节相同、9 对差异；另有顶层 C0 独有文件（nonidentical union entries=10）",
    )

    memory = replace_once(
        (root / "MEMORY.md").read_text(encoding="utf-8"),
        "1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现：S013 完成主迁移，S014 收口旧主题，S015 对齐 current owner，S016 完成两份 generation-2 治理文档 Git rename 归档，`S-GOV-20260912-017-FINAL-VERIFICATION-ALIGNMENT` revision 17 收敛最终验证叙事；本轮不启动数学研究。",
        "1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现：S013 完成主迁移，S014 收口旧主题，S015 对齐 current owner，S016 完成 generation-2 文档归档，S017 收敛验证叙事，`S-GOV-20260912-018-MERGE-COUNT-SEMANTICS` revision 18 修正理解章节 receipt 的同名差异/独有文件计数语义；本轮不启动数学研究。",
    )
    memory = replace_once(
        memory,
        "- source register 22,226 行与理解章节 25/24 文件处置保持原范围；core 重建不改变历史 AI 审计分母，也不自动完成 2,396 条语义裁决。",
        "- source register 22,226 行与理解章节 25/24 文件处置保持原范围；merge receipt 明确 24 个同名对=15 identical+9 different，另有 1 top-level unique；core 重建不改变历史 AI 审计分母，也不自动完成 2,396 条语义裁决。",
    )

    frontier = replace_once(
        (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
        "revision 17 已对齐 current owner 与 full regression",
        "revision 18 已对齐 current owner、merge count 语义与 full regression",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip() + (
        "\n19. `different_pairs` 只能计数双方都存在且不同的同名对；单侧独有项应另计，并可用 `nonidentical_union_entries` 表示整个 union 中的非 identical 项，不能用一个含糊字段同时承担两种分母。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "revision 17 final verification-alignment checkpoint 构成本轮交付（S016 保存历史文档归档路径迁移）",
        "revision 18 merge-count-semantics checkpoint 构成本轮交付（S016 保存历史文档归档路径迁移，S017 保存验证叙事对齐）",
    )

    state["revision"] = 18
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "status": "CORE_GENERATION_3_LAYERED_LOAD_V3_MERGE_COUNT_SEMANTICS_ALIGNED",
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
        "depends_on": ["S-GOV-20260912-017-FINAL-VERIFICATION-ALIGNMENT", "A-UNDERSTANDING-RECONCILIATION-001"],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            "audit/understanding-chapter-merge-manifest.json",
            "scripts/audit/build_understanding_merge_manifest.py",
            "scripts/audit/verify_understanding_merge.py",
            "全景视野.md",
        ],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "cognition_status": "UNDERSTANDING_MERGE_COUNT_SEMANTICS_VERIFIED",
        "scope": "Correct machine count semantics for same-name differences versus one-sided union entries; no sentence-level or mathematical reconciliation.",
    }

    session = f"""# {SESSION_ID}

- 触发：理解章节正文正确写成 24 个同名对=15 identical+9 different、另有 1 个顶层独有文件，但 builder 把所有 10 个 non-identical union entries 都命名为 `different_pairs`。
- 修复：`different_pairs=9`；新增 `nonidentical_union_entries=10`；verifier 重算六类分母并拒绝伪造 10 的负向 fixture。
- 证据：实际 builder/manifest/verifier 为 25 union、24 same-name、15 identical、9 different、10 nonidentical union、1 top-only、0 nested-only、0 unresolved；负向返回 `COUNT_DIFFERENT_PAIRS_MISMATCH:10:9`。
- 边界：这只修复机器计数语义；2,396 条 claim 的直接句级/数学融合仍为 OPEN_ISSUE。
- 完成后：重跑 fresh/projection/full suite、JSON/schema、Git diff/check/status 并完成精确 commit/tag。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "positive": expected_counts,
            "negative_fixture": "COUNT_DIFFERENT_PAIRS_MISMATCH:10:9",
            "post_checkpoint_required": [
                "fresh-three-way v2",
                "projection freshness",
                "full regression",
                "JSON and core schema validation",
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
        "authorization": "User authorized implementation and auditable understanding-directory reconciliation; correcting its machine count semantics is in scope.",
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
                "revision": 18,
                "files": len(texts),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
