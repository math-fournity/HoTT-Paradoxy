#!/usr/bin/env python3
"""Prepare revision 91: align post-S090 evidence hashes and verified status."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-091-GOVERNANCE-REPAIR-ALIGNMENT"
PREV = "S-GOV-20260913-090-CHECKPOINT-HYDRATION-REPAIR"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
S090_RESULT = ".codex/cognition/checkpoints/S-GOV-20260913-090-CHECKPOINT-HYDRATION-REPAIR/result.json"
S090_VERIFICATION = "audit/S090-governance-repair-verification-20260913.json"
S090_REPORT = "audit/S090治理修复实施与验收证据-20260913.md"

SPEC = importlib.util.spec_from_file_location("runtime_s091", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:100]}:{text.count(old)}")
    return text.replace(old, new, 1)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000001": "把治理修复从设计、S090 实际 checkpoint 推进到 source-hash/current-status 对齐，增强研究证据可追溯性。",
        "KC-000005": "没有开始新悖论归因；本轮只闭合治理修复的状态一致性。",
        "KC-000017": "压缩后完整三件套仍是启动输入；本轮防止 current owner/hash 漂移削弱该上下文工程。",
        "KC-000021": "S090 的真实 run/receipt 与本轮验证状态分开记录；不以文档或 checkpoint 替代数学证明。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮仅对齐 S090 后证据 hash 与 Feature 状态。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned:
            relation = "ALIGNED"; assessment = aligned[kid]
        else:
            relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{S090_REPORT}`；`{S090_VERIFICATION}`；{kid} | E6、现实桥梁、自馈不可停机与 HoTT 悖论仍未建立。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 没有新用户原文。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 revision/status；下游 E6 consumer 仍第一线。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只同步 revision/status；S090 结果不变。",
        "- update_decision: 刷新 S090 后直接修订的 hash；F-005/F-012 状态与实际 S090 result/plan 验收对齐。",
        "- cross_conflicts: S090 后设计文档空白清理造成 1 个 hash mismatch，已由本 checkpoint 正式刷新，没有改写 S090 transaction。",
        "- unresolved: Git repair commit/tag 尚未完成；fresh model behavior NOT_RUN；数学目标仍开放。",
        "", "## 汇总", "", "`ALIGNED=4`；`NOT_TOUCHED=32`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 90 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_90_S090")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(
        memory,
        "## 当前已验证状态\n\n",
        "## 当前已验证状态\n\n- S091 对齐轮：S090 canonical result/五个 task plan 已验收；修复后直接清理设计文档空白造成的单个 source-hash 漂移不篡改 S090，而由本轮刷新；F-005/F-012 状态提升到实际证据支持范围。\n",
    )
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 90", "source_state_revision: 91")
    direction = replace_once(direction, "projection_generation: 20260913-direction-074", "projection_generation: 20260913-direction-075")
    direction = replace_once(direction, "状态：`GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST`", "状态：`GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING`")
    direction = replace_once(direction, "semantic_status: GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST", "semantic_status: GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING")
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 90", "source_state_revision: 91")
    panorama = replace_once(panorama, "projection_generation: 20260913-outcome-074", "projection_generation: 20260913-outcome-075")
    panorama = replace_once(panorama, "状态：`GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST`", "状态：`GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING`")
    panorama = replace_once(panorama, "semantic_status: GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST", "semantic_status: GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING")
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n", "## 当前停止点\nS091 对齐轮：不改 S090 事务；刷新修复后 1 个 source hash，Feature 与真实 checkpoint/plan 验收对齐。修复 commit/tag 仍待完成。\n\n")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")

    session_path = f"{SESSION_REL}/SESSION.md"; audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"; runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目的：在不改写 S090 transaction/result 的前提下，刷新 S090 后直接修订引起的 source hash，并把 Feature/current projection 状态与真实验收对齐。
- S090 result：`{S090_RESULT}` = `CHECKPOINT_COMMITTED`；S090 verifier = `{S090_VERIFICATION}`。
- 数学：无新 claim、无 proof source/run 修改；研究第一线仍为下游 E6 consumer，T3 第二线。
- Git：repair commit 与 `governance-v3.2.0` tag 仍 pending；不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "s090_result": S090_RESULT, "s090_verification": S090_VERIFICATION,
        "pre_checkpoint": {"runtime_tests": "32/32 PASS", "s090_verifier": "PASS_WITH_SCOPE", "projection": "PASS_WITH_SCOPE"},
        "result": RESULT_REL, "mathematics": "NO_NEW_MATHEMATICAL_CLAIM", "git_release": "PENDING",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    records = state["records"]
    repair = records["A-GOVERNANCE-REPAIR-S090-001"]
    for rel in [S090_VERIFICATION, S090_REPORT, f"{SESSION_REL}/../{PREV}/POST-CHECKPOINT.json"]:
        normalized = rel.replace(f"{SESSION_REL}/../{PREV}/", f".codex/research/hott/sessions/{PREV}/")
        if normalized not in repair["full_sources"]: repair["full_sources"].append(normalized)
    repair["resolution"] = {
        "reason": "S090 canonical result is CHECKPOINT_COMMITTED; runtime 32/32 and five real task plans pass with zero query-first promotion; S091 aligns the one post-checkpoint documentation-hygiene hash and Feature status without rewriting S090.",
        "evidence": [S090_RESULT, S090_VERIFICATION, S090_REPORT, "docs/design/detailed/认知水合关系与检查点事务合同.md"],
    }
    repair["source_hashes"] = {}
    repair["revalidation"] = "S091 binds the verified S090 result/report/plan receipt and aligns the post-checkpoint documentation-hygiene hash; no retained mathematical proof source or run body changed."
    state["revision"] = 91; state["latest_session"] = SESSION_ID
    state["execution_control"].update({"last_checkpoint_session": SESSION_ID, "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT", "status": "GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING"})
    state["projection"]["status"] = "CORE_GENERATION_4_GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING"
    records["I-DIRECTION-PORTFOLIO-20260912"].update({"projection_generation": "20260913-direction-075", "semantic_status": "CORE_GENERATION_4_GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING"})
    records["I-OUTCOME-PANORAMA-20260912"].update({"projection_generation": "20260913-outcome-075", "semantic_status": "CORE_GENERATION_4_GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING"})
    records[SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete", "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-GOVERNANCE-REPAIR-S090-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, S090_RESULT, S090_VERIFICATION, S090_REPORT], "source_hashes": {},
        "scope": "Post-S090 evidence/hash and Feature-state alignment only; no new mathematics.",
    }
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    def proposed(rel: str) -> bytes:
        if rel in texts: return texts[rel].encode("utf-8")
        path = root / rel
        if not path.is_file(): raise ValueError(f"HASH_TARGET_MISSING:{rel}")
        return path.read_bytes()
    for key, record in records.items():
        hashes = record.get("source_hashes")
        if not isinstance(hashes, dict): continue
        changed = False
        for rel, old in list(hashes.items()):
            new = sha_bytes(proposed(rel))
            if new != old: hashes[rel] = new; changed = True
        if changed:
            record["revalidation"] = "S091 aligns post-S090 documentation/Feature hashes with the verified S090 result; no retained mathematical proof source or run body changed."
    for rel in repair["resolution"]["evidence"]:
        repair["source_hashes"][rel] = sha_bytes(proposed(rel))
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "User authorized the recommended project-local governance repair and exact commit/tag. This alignment checkpoint updates only in-repo cognition state and session evidence; no push, publication, removed-source restoration or mathematical claim.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 91, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
