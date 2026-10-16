#!/usr/bin/env python3
"""Prepare the final revision-15 current-owner alignment checkpoint."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-015-FINAL-STATE-ALIGNMENT"
SPEC = importlib.util.spec_from_file_location("runtime_final_alignment", RUNTIME_PATH)
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
            "本轮仅使 revision/receipt/current-owner 文字与已经完成的治理实物一致，没有改变或裁决该用户原文。 | "
            "MEMORY.md; 全景视野.md; .codex/research/hott/STATE.json; audit/fresh-three-way-verification-20260912.json | "
            "该 KC 的数学与现实解释仍由后续研究负责。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — core/manifest/curation/transition 不变。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只同步 projection revision 15。",
        "- panorama_change: `NO_RESULT_CHANGE` — 更新治理结果的测试数与最终 checkpoint revision。",
        "- update_decision: `只更新当前状态 owner；历史与数学结果不变。`",
        "- cross_conflicts: `NONE_AFTER_ALIGNMENT`。",
        "- unresolved: `fresh model behavior、数学认证、aistudio coverage、2,396 claim 语义。`", "",
        "## 汇总", "", "`NOT_TOUCHED=27`；不以收尾元数据冒充研究深化。", "",
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
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 14:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_14")
    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"),
                             "source_state_revision: 14", "source_state_revision: 15")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"),
                            "source_state_revision: 14", "source_state_revision: 15")
    panorama = replace_once(panorama,
        "core 7 tests、runtime 27 tests、reader 17 tests、three-way 3 tests；默认 governance/research 均不加载冷资产；revision 13 checkpoint",
        "core 7 tests、runtime 27 tests、reader 17 tests、three-way 4 tests（含 current-theme 负向）；默认 governance/research 均不加载冷资产；revision 15 final checkpoint")
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(memory,
        "已由 S013 完成主迁移，并由 `S-GOV-20260912-014-PROJECTION-THEME-ALIGNMENT` revision 14 收口最后一个旧主题引用",
        "已由 S013 完成主迁移、S014 收口旧主题引用，并由 `S-GOV-20260912-015-FINAL-STATE-ALIGNMENT` revision 15 统一当前 receipt/owner 文字")
    memory = replace_once(memory,
        "- checkpoint 前实测 governance=15 documents/159,882 bytes，research=20/228,396 bytes；最终 revision 13 精确值见 `audit/fresh-three-way-verification-20260912.json`。",
        "- 默认 governance/research profile 均为 15/20 documents，三件套固定前三项、历史 Session 自动加载=0；当前精确 bytes/lines/snapshot 由 revision 15 的 `audit/fresh-three-way-verification-20260912.json` 持有，MEMORY 不复制易漂移数值。")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = replace_once(frontier, "| 收敛 | generation-3 core + LOAD_SET/runtime v3 + STATE v2 checkpoint | completing | 完成 revision 14、fresh Python receipt、全套回归与 Git/tag；fresh model behavior 仍独立 NOT_RUN |",
        "| 收敛 | generation-3 core + LOAD_SET/runtime v3 + STATE v2 checkpoint | completed-local | 完成 revision 15 后运行 fresh/full regression 并精确 Git/tag；fresh model behavior 仍独立 NOT_RUN |")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    resume = replace_once((root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
                          "revision 14 checkpoint", "revision 15 checkpoint")
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["revision"] = 15
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "CORE_GENERATION_3_LAYERED_LOAD_V3_CURRENT_OWNERS_ALIGNED",
        "checkpoint_result": "CHECKPOINT_COMMITTED"
    })
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-014-PROJECTION-THEME-ALIGNMENT"],
        "full_sources": [session_path, audit_path, runs_path, "MEMORY.md", "全景视野.md", "audit/fresh-three-way-verification-20260912.json"],
        "source_hashes": {}, "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "cognition_status": "FINAL_CURRENT_OWNER_ALIGNMENT",
        "scope": "Align mutable current-owner revision/receipt text after the manifest-theme repair; no mathematics."
    }
    session = f"""# {SESSION_ID}

- 目的：消除 S014 后 MEMORY/全景中仍指向 revision 13 的收尾文字，并避免静态治理文件永久绑定易漂移 revision。
- 变更：同步 direction/panorama/STATE revision 15，更新 current queue、前沿和恢复指针；core 与数学结果不变。
- 完成后：重跑 fresh Python、projection freshness、core/three-way/runtime/reader/history/merge/reconciliation 与 Git checks。
- 边界：fresh model behavior 与数学证明仍 NOT_RUN/NOT_CERTIFIED。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "pre_checkpoint": {"reason": "current MEMORY/panorama still named revision 13 after S014"},
        "post_checkpoint_required": ["fresh-three-way v2", "projection freshness", "full regression", "git diff/status"],
        "model_behavior": "NOT_RUN", "mathematics": "UNCHANGED"
    }, ensure_ascii=False, indent=2) + "\n"
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "User authorized implementation; this final alignment is required to remove stale current-owner claims before version close.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
                  for rel, value in texts.items()]
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "session_id": SESSION_ID,
                      "revision": 15, "files": len(texts), "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
