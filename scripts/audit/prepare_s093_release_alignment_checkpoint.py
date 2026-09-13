#!/usr/bin/env python3
"""Prepare revision 93: align current STATE after the release commit/tag step."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-093-RELEASE-STATE-ALIGNMENT"
PREV = "S-GOV-20260913-092-GOVERNANCE-V3-2-VERSION-CLOSURE"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
RELEASE_PARENT = "667c7e8a1d3349bf5c7ba766d937fc4cbf2cec6f"
PRE_ALIGNMENT_TAG_OBJECT = "9a9e2d2c0dbc5a1adf78cbe192bc9ec0d6abcf10"
RELEASE_REF = "governance-v3.2.0"

SPEC = importlib.util.spec_from_file_location("runtime_s093", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1: raise ValueError(f"REPLACE_COUNT:{old[:100]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000001": "修正发布后 current STATE，确保未来 AI 的证据入口与实际 Git 状态一致。",
        "KC-000017": "不让压缩后的 AI 读取到‘tag 已完成’与‘Git pending’冲突的启动记忆。",
        "KC-000021": "保持 proof/kernel 状态与 Git release 状态分层；本轮不重证数学。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只修发布后 current-state 漂移。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned: relation = "ALIGNED"; assessment = aligned[kid]
        else: relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `audit/governance-v3.2.0-release-evidence-20260913.md`；{kid} | 数学开放项不变。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 revision。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只同步 revision。",
        "- update_decision: 将 execution_control 从 Git pending 改为 S093 checkpoint applied + release parent version-closed；最终 local tag 在本 commit 后对齐。",
        "- cross_conflicts: S092 checkpoint 时的 pending 字段在 667c7e8 commit/tag 后过时；本轮原位修复，不移动/改写已有 commit。",
        "- unresolved: fresh model behavior NOT_RUN；并行工作树资产仍未提交；数学目标仍开放；不 push。",
        "", "## 汇总", "", "`ALIGNED=3`；`NOT_TOUCHED=33`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 92 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_92_S092")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(memory, "## 当前已验证状态\n\n", "## 当前已验证状态\n\n- S093 发布状态对齐：S092 后 commit `667c7e8…` 已形成；本轮把 current STATE 从 Git pending 改为 checkpoint applied/release parent version-closed，最终本地 tag 对齐本轮 commit；不改 proof 数学范围。\n")
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 92", "source_state_revision: 93")
    direction = replace_once(direction, "projection_generation: 20260913-direction-076", "projection_generation: 20260913-direction-077")
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 92", "source_state_revision: 93")
    panorama = replace_once(panorama, "projection_generation: 20260913-outcome-076", "projection_generation: 20260913-outcome-077")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"): lessons += "\n"
    lessons += "\n72. Release commit/tag 之后必须重新检查 current STATE 是否还写 `PENDING_GIT_COMMIT`。Checkpoint 记录的是写入时状态，不能自动感知后续 Git；最终可用状态应由一个新的、真实 receipt 对齐，而不是篡改旧 transaction。\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n", "## 当前停止点\nS093 release-state alignment：S092 后 release commit `667c7e8…` 已存在；current STATE 不再误写 Git pending。最终 local `governance-v3.2.0` tag 对齐本轮 commit，不 push。\n\n")

    session_path = f"{SESSION_REL}/SESSION.md"; audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"; runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 原因：S092 checkpoint 时正确记录 Git pending；后续 release commit `{RELEASE_PARENT}` 与初始本地 tag 已形成，使 current STATE 字段过时。
- 动作：不改 S092 transaction，不改 proof source/run/index；以新 checkpoint 对齐 current state，并在最终 commit 后把尚未对外发布的本地 `{RELEASE_REF}` tag 指向最终 HEAD。
- 旧 tag object：`{PRE_ALIGNMENT_TAG_OBJECT}`；旧 release commit 保留为父 commit，不重写。
- 数学与研究方向不变；不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "release_parent_commit": RELEASE_PARENT, "pre_alignment_tag_object": PRE_ALIGNMENT_TAG_OBJECT,
        "release_ref": RELEASE_REF, "checkpoint_result": RESULT_REL,
        "mathematics": "NO_NEW_OR_CHANGED_MATHEMATICAL_CLAIM", "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    records = state["records"]
    state["revision"] = 93; state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_RELEASE_PARENT_VERSION_CLOSED",
        "release_ref": RELEASE_REF,
        "release_parent_commit": RELEASE_PARENT,
        "status": "GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
    records["I-DIRECTION-PORTFOLIO-20260912"].update({"projection_generation": "20260913-direction-077", "semantic_status": "CORE_GENERATION_4_GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"})
    records["I-OUTCOME-PANORAMA-20260912"].update({"projection_generation": "20260913-outcome-077", "semantic_status": "CORE_GENERATION_4_GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"})
    release = records["A-GOVERNANCE-V3-2-RELEASE-001"]
    release["release_alignment"] = {
        "release_parent_commit": RELEASE_PARENT,
        "pre_alignment_tag_object": PRE_ALIGNMENT_TAG_OBJECT,
        "final_release_ref": RELEASE_REF,
        "final_ref_must_point_to_latest_commit": True,
    }
    release["resolution"]["reason"] = "Project-local governance 3.2 is closed by S090-S093 canonical checkpoints, proof-asset commit d3dfb0e, release parent 667c7e8 and the final local annotated release ref. S093 removes the stale post-commit pending field without rewriting S092; no push."
    records[SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete", "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-GOVERNANCE-V3-2-RELEASE-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, "audit/governance-v3.2.0-release-evidence-20260913.md"], "source_hashes": {},
        "scope": "Post-release current-state alignment only; no proof or research change.",
    }
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "User authorized the recommended exact local commit/tag. This final alignment corrects current Git state after the release commit while preserving all prior transactions and concurrent user work; no push or mathematical change.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 93, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
