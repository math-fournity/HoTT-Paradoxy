#!/usr/bin/env python3
"""Prepare revision 32 to align the F-011 README hashes after S031."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"
GATE_ID = "A-MATH-PROOF-DELIVERY-GATE-001"
RESULT_ID = "A-ERCF-TRUNCATION-DEFENSE-001"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
FORMAL_HASH = "f0af95cef2821255758e0f2c07e3cf134be1e3f739e7becd1e669b631fd0a4b1"
RUNS_HASH = "a3dd7871007895efe98bfa128496af7015562ee56f3585f8a9959b7581467bde"

SPEC = importlib.util.spec_from_file_location("runtime_ercf_truncation_final", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | 本轮只同步 F-011 stable record 的两个 README source hash；不改变截断证明、判词、方向语义或该用户原文。 | S031/SESSION.md；S032/SESSION.md；核心认知.md {unit['id']} | partiality quotient natural consumer 与 ERCF-3 仍开放。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只同步 revision 32/projection generation 016。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只同步 revision 32/projection generation 016。",
        "- update_decision: `A-MATH-PROOF-DELIVERY-GATE-001 的 formal/runs README hash 与 MEMORY/LESSONS/RESUME/session receipt 更新。`",
        "- cross_conflicts: `RESOLVED` — task hydration 不再因两个已更新入口的旧 hash 把证明误标 review。",
        "- unresolved: `fresh model behavior、Git version-close 与下一数学工作包仍开放。`",
        "", "## 汇总", "", "`NOT_TOUCHED=36`；本轮数学状态不变。", "",
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
    if state.get("revision") != 31 or state.get("latest_session") != "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE":
        raise SystemExit("EXPECTED_REVISION_31_S031")
    if sha(root / FORMAL_README) != FORMAL_HASH or sha(root / RUNS_README) != RUNS_HASH:
        raise SystemExit("CURRENT_README_HASH_MISMATCH")
    stale = []
    for record_id, record in state["records"].items():
        for relative, expected in record.get("source_hashes", {}).items():
            path = root / relative
            if not path.is_file() or sha(path) != expected:
                stale.append((record_id, relative))
    if stale != [(GATE_ID, FORMAL_README), (GATE_ID, RUNS_README)]:
        raise SystemExit(f"UNEXPECTED_STALE_SET:{stale}")

    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"), "source_state_revision: 31", "source_state_revision: 32")
    direction = replace_once(direction, "projection_generation: 20260912-direction-015", "projection_generation: 20260912-direction-016")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"), "source_state_revision: 31", "source_state_revision: 32")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-015", "projection_generation: 20260912-outcome-016")
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    anchor = "- `MP-ERCF-TRUNC-001` 是首个原生 Cubical package：Agda 2.8.0/Cubical v0.9 final run、5 类外部依赖 hash、index row manifest 和 exact replay PASS；判词 `DEFENSE_WORKS`。"
    memory = replace_once(memory, anchor, anchor + "\n- S032 同步 F-011 record 的 formal/runs README hash；原生 proof task hydration 现在成功且 `review_required=[]`，数学状态不变。")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "40. proof package 同轮更新" not in lessons:
        lessons += "\n40. proof package 同轮更新 source/run/index 与人读入口时，必须对 stable record 的全部 `source_hashes` 做全量差异审计；只更新新增 proof/hash 仍会让旧 README hash 传播 stale，最终验收必须以 task hydration 的 `review_required=[]` 收口。"
    lessons += "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n\nS031 已完成", "## 当前停止点\n\nS032 已同步 F-011 stable record 的 formal/runs README hash；`A-ERCF-TRUNCATION-DEFENSE-001` research task hydration 成功且 `review_required=[]`。数学与下一方向均不变。\n\nS031 已完成")

    gate = state["records"][GATE_ID]
    gate["source_hashes"][FORMAL_README] = FORMAL_HASH
    gate["source_hashes"][RUNS_README] = RUNS_HASH
    gate["revalidation"] = "After S031 changed the formal and run indexes, both README hashes were aligned and the native proof task plan returned review_required empty. Proof source/run/index and mathematics are unchanged."
    state["revision"] = 32
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({"last_checkpoint_session": SESSION_ID, "status": "NATIVE_TRUNCATION_DEFENSE_MACHINE_PROVED_HYDRATABLE_PARTIALITY_QUOTIENT_NEXT", "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT"})
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-016"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-016"

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete", "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE", RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, FORMAL_README, RUNS_README, "scripts/audit/prepare_ercf_truncation_final_alignment_checkpoint.py"],
        "source_hashes": {FORMAL_README: FORMAL_HASH, RUNS_README: RUNS_HASH},
        "mathematical_status": "UNCHANGED_FROM_MP_ERCF_TRUNC_001", "cognition_status": "F011_README_HASHES_ALIGNED_NATIVE_TASK_NOT_REVIEW_STALE",
        "scope": "Align two stale human-readable proof index hashes after S031 so native task hydration remains clean; no mathematical or direction change.",
    }
    session = f"""# {SESSION_ID}

- 触发：S031 后原生 proof task plan 成功，但 `review_required` 包含 result 与 F-011 Gate。
- 根因：全量 source-hash 审计只发现 `{FORMAL_README}`、`{RUNS_README}` 仍是 S030 值；二者已由 S031 合法更新。
- 修复：只同步这两个 hash，并修正 S031 preparer；proof source/run/matrix/toolchain 不改。
- 预期验收：`A-ERCF-TRUNCATION-DEFENSE-001` plan 成功且 `review_required=[]`；旧 Lean/native exact replay 均通过。
- 数学状态：C-67–C-70 仍为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS`；不是悖论。
- 三件套：无语义变化，只同步 revision 32/generation 016；core 不变。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "observed_stale": [{"record": GATE_ID, "path": FORMAL_README}, {"record": GATE_ID, "path": RUNS_README}],
        "unexpected_stale_remainder": 0,
        "post_checkpoint_required": ["native task review_required empty", "Lean/native exact replay", "36/36 audit", "27 directions/29 outcomes", "fresh revision 32", "projection freshness", "full regression", "git diff --check"],
        "mathematics": "UNCHANGED_FROM_MP_ERCF_TRUNC_001", "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "This in-scope final alignment fixes the two stale stable-record hashes revealed by post-S031 task hydration; it changes no mathematical claim, direction or external state.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 32, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
