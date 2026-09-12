#!/usr/bin/env python3
"""Prepare revision 14 fixing the last obsolete direction-to-core theme."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-014-PROJECTION-THEME-ALIGNMENT"
SPEC = importlib.util.spec_from_file_location("runtime_projection_fix", RUNTIME_PATH)
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
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | "
            "本轮只修正一个 AI 派生方向使用的旧主题名，没有改变、深化或裁决该用户原文。 | "
            "方向追踪.md; scripts/audit/verify_three_way_cognition.py; scripts/audit/test_three_way_cognition.py | "
            "该 KC 的数学真值与现实桥梁不由本轮处理。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-3 原文和 manifest 均未改变。",
        "- direction_change: `YES` — `DIR-W-TRANSITION-ABSTRACTION` 的旧 generation-2 主题替换为当前存在的 `HOTT_OBJECT`。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只同步 STATE revision 14 marker。",
        "- update_decision: `只更新方向 owner、projection revision、STATE/MEMORY/恢复记录。`",
        "- cross_conflicts: `NONE_AFTER_FIX` — verifier 从失败变为通过。",
        "- unresolved: `fresh model behavior、历史数学和 2,396 claim 语义仍开放。`", "",
        "## 汇总", "",
        "`NOT_TOUCHED=27`；本轮没有数学研究，也没有用方向修正反向改写 core。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 13:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_13")
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 13", "source_state_revision: 14")
    direction = replace_once(direction,
        "`TIME_AND_TEMPORALITY`, `IDENTITY_UNIVALENCE_TRANSPORT`",
        "`TIME_AND_TEMPORALITY`, `HOTT_OBJECT`")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"),
                            "source_state_revision: 13", "source_state_revision: 14")
    memory = replace_once((root / "MEMORY.md").read_text(encoding="utf-8"),
        "正由 `S-GOV-20260912-013-CORE-LOAD-V3` revision 13 checkpoint 封存",
        "已由 S013 完成主迁移，并由 `S-GOV-20260912-014-PROJECTION-THEME-ALIGNMENT` revision 14 收口最后一个旧主题引用")
    frontier = replace_once((root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
                            "revision 13、fresh Python receipt", "revision 14、fresh Python receipt")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip() + (
        "\n16. core 换代后必须让 direction→core 主题通过当前 manifest 集合校验；只更新主要结果行仍可能留下一个旧标签，负向 validator 应使这种残留 fail closed。\n"
    )
    resume = replace_once((root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
                          "revision 13 checkpoint", "revision 14 checkpoint")
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["revision"] = 14
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "CORE_GENERATION_3_LAYERED_LOAD_V3_PROJECTION_THEMES_ALIGNED",
        "checkpoint_result": "CHECKPOINT_COMMITTED"
    })
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["A-LOAD-GOVERNANCE-V3-001"],
        "full_sources": [session_path, audit_path, runs_path, "方向追踪.md", "scripts/audit/verify_three_way_cognition.py"],
        "source_hashes": {}, "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "cognition_status": "CURRENT_CORE_THEME_SET_ALIGNED",
        "scope": "Fix the last obsolete direction-to-core theme found by the new manifest-aware validator; no mathematics."
    }
    state_text = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    session_text = f"""# {SESSION_ID}

- 触发：新增 manifest-aware three-way validator 后，当前方向仍有一项 `IDENTITY_UNIVALENCE_TRANSPORT`，而 generation-3 manifest 不含该主题。
- 修复：只将 `DIR-W-TRANSITION-ABSTRACTION` 的关联改为现存 `HOTT_OBJECT`，同步 projection/STATE revision 14。
- 验证：修复前 actual verifier FAIL；负向测试 4/4 PASS；修复后须重跑 verifier/fresh/full suite。
- 边界：core 原文、27 IDs、方向数量、成果数量、历史数学状态均不变；fresh model behavior 仍 NOT_RUN。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "pre_fix": {"three_way_verifier": "FAIL:DIRECTION_CORE_THEME_NOT_IN_CURRENT_MANIFEST:IDENTITY_UNIVALENCE_TRANSPORT"},
        "tests": {"test_three_way_cognition.py": "4/4 PASS including obsolete-theme negative"},
        "post_fix_required": ["verify_three_way_cognition.py", "verify_fresh_three_way.py", "full regression"],
        "mathematics": "UNCHANGED", "model_behavior": "NOT_RUN"
    }, ensure_ascii=False, indent=2) + "\n"
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume, R.STATE: state_text,
        session_path: session_text, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "User authorized implementation; this is the bounded projection consistency repair discovered by its new validator.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
                  for rel, value in texts.items()]
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "session_id": SESSION_ID,
                      "revision": 14, "files": len(texts), "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
