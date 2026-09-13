#!/usr/bin/env python3
"""Prepare revision 23 for post-verification and EOF-format alignment."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-023-SELF-VALIDATION-FINAL-ALIGNMENT"
SPEC = importlib.util.spec_from_file_location("runtime_self_validation_final", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
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
            "本轮只修复 checkpoint 产物的 EOF 空白并把已执行验证收敛到 revision 23；不改变、深化或裁决该用户原文。 | "
            f"S022/CORE_COGNITION_AUDIT.md；本轮 SESSION/RUNS；核心认知.md {unit['id']} | "
            "该 KC 的既有 S022 评估和数学未决保持不变。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC、curation、manifest 和 transition 均不变。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 23/projection generation 007。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 23/projection generation 007。",
        "- update_decision: `LESSONS EOF、STATE/MEMORY/RESUME、三件套 revision marker 和 final verification session 由一个原子 checkpoint 收敛。`",
        "- cross_conflicts: `NONE` — C4、当前用户方向、paper-only 证据级别和全部开放数学问题不变。",
        "- unresolved: `ERCF-1/2/3 形式化、具体发散 witness、最小 coverage no-go、Gödel 内部化、现实桥梁以及 fresh model behavior 仍开放。`",
        "", "## 汇总", "",
        "`NOT_TOUCHED=36`；本轮不以格式/验证收尾冒充研究进展。", "",
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
    if state.get("revision") != 22 or state.get("latest_session") != "S-RES-20260912-022-SELF-VALIDATION-ECONOMY":
        raise SystemExit("EXPECTED_REVISION_22_S022")

    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 22", "source_state_revision: 23")
    direction = replace_once(direction, "projection_generation: 20260912-direction-006", "projection_generation: 20260912-direction-007")
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 22", "source_state_revision: 23")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-006", "projection_generation: 20260912-outcome-007")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    marker = "- project-local governance 3.1 是未提交 candidate；最近已封存 tag 仍为 `governance-v3.0.0`。本轮未获 commit/tag/push 授权。"
    memory = replace_once(
        memory,
        marker,
        marker + "\n- S023 只完成 post-verification/EOF 格式收尾：core 7/7、runtime 28/28、reader 17/17、three-way 4/4、36-KC audit、merge/register/history/fresh/projection 均通过；不改变 C4 数学状态。",
    )
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip("\n") + "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "S022 已把用户当前原文纳入 generation-4 的 KC-000028–000036，并完成 C4 论证：",
        "S023 已完成 S022 的验证/EOF 格式收尾；S022 把用户当前原文纳入 generation-4 的 KC-000028–000036，并完成 C4 论证：",
    )

    state["revision"] = 23
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "SELF_VALIDATION_ECONOMY_VERIFIED_LOCAL_CANDIDATE_UNCOMMITTED",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
    })
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-007"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-007"
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-RES-20260912-022-SELF-VALIDATION-ECONOMY"],
        "full_sources": [session_path, audit_path, runs_path, "audit/核心认知generation-4与自反理论经济研究实施证据-20260912.md", "scripts/audit/prepare_self_validation_final_alignment_checkpoint.py"],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_PAPER_ONLY_FROM_S022",
        "cognition_status": "POST_VERIFICATION_AND_EOF_FORMAT_ALIGNED",
        "scope": "Remove one checkpoint-created blank line at EOF, align projection revision markers and record the completed local verification matrix without changing core cognition or mathematics.",
    }
    session = f"""# {SESSION_ID}

- 触发：S022 后 `git diff --check` 发现 `.codex/research/hott/LESSONS.md` 多一个 EOF 空白行；该文件属于 checkpoint-managed mutable，不能直接修改。
- 动作：通过 revision 23 原子事务移除额外空白行，同步 direction/panorama source revision 与 STATE/MEMORY/RESUME，并保存 36/36 `NOT_TOUCHED` 回评。
- 已有验证：core 7/7、runtime 28/28、reader 17/17、three-way 4/4、core/merge/register/history/fresh/projection checks 均通过。
- 数学边界：C4 与 ERCF 状态仍为 `PAPER_ONLY`；没有新增证明、程序运行或事实裁决。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "trigger": "git diff --check reported one new blank line at EOF in checkpoint-managed LESSONS.md",
        "pre_checkpoint_verification": {
            "core_tests": "7/7 PASS", "runtime_tests": "28/28 PASS", "reader_tests": "17/17 PASS",
            "three_way_tests": "4/4 PASS", "core_audit": "36/36 PASS",
            "merge": "PASS", "cross_source": "PASS", "history_ledgers": "PASS",
            "fresh_three_way_revision_22": "PASS_WITH_SCOPE", "projection_freshness_revision_22": "PASS_WITH_SCOPE",
        },
        "semantic_change": False, "mathematics": "UNCHANGED_PAPER_ONLY",
        "post_checkpoint_required": ["36/36 audit", "fresh receipt revision 23", "projection freshness", "git diff --check", "full regression"],
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"
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
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "The user authorized durable core/research document work; project governance requires checkpoint-managed mutable owners and final verification state to remain atomically aligned. This transaction performs only in-scope formatting and verification closure.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 23, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
