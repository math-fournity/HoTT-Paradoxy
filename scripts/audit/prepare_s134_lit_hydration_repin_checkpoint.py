#!/usr/bin/env python3
"""Prepare revision 134: route large literature JSON through small receipts."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260914-134-LIT-HYDRATION-REPIN"
PREV = "S-RES-20260914-133-LIT-DENOMINATOR-001"
LIT_ID = "A-LIT-DENOMINATOR-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
AUDIT_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
INDEX = ".codex/research/hott/LIT-DENOMINATOR-001.md"
TEST = "scripts/audit/test_lit_denominator.py"
MANIFEST = "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/MANIFEST.json"
RECEIPT = "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/TRIAGE-RECEIPT.json"
CANDIDATES = "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/DISCOVERY-CANDIDATES.json"
TRIAGE = "audit/literature/LIT-DENOMINATOR-001/discovery-20260914/TRIAGE.json"
STATUS = "CORE_GENERATION_4_LIT_DENOMINATOR_V1_FROZEN_R1_MAIN_REPLAY_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s134", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只修复文献任务水合，不改变 S133 研究结论。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "ALIGNED" if kid in {"KC-000007", "KC-000021"} else "NOT_TOUCHED"
        assessment = "大型派生候选/triage 由小 receipt 认证并按需读取，防止元数据吞噬研究正文。" if relation == "ALIGNED" else f"本轮没有重新裁决“{label}”的内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{RECEIPT}`；{kid} | S133 开放义务不变。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO。", "- direction_change: NO_SEMANTIC_CHANGE。", "- panorama_change: NO_SEMANTIC_CHANGE。", "- essay_change: NO。",
        "- update_decision: large discovery JSON 改由 MANIFEST/TRIAGE-RECEIPT 路由。",
        "- cross_conflicts: S133 task hydration 直接提升两个大型 source_hash 文件；本轮删除该提升并保留 hash receipt。",
        "- unresolved: 与 S133 相同。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 133 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_133_S133")
    if SESSION_ID in state["records"]:
        raise SystemExit("SESSION_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    projection_edit.replace_in_index(direction, "source_state_revision: 133", "source_state_revision: 134")
    projection_edit.replace_in_index(direction, "projection_generation: 20260914-direction-115", "projection_generation: 20260914-direction-116")
    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.replace_in_index(panorama, "source_state_revision: 133", "source_state_revision: 134")
    projection_edit.replace_in_index(panorama, "projection_generation: 20260914-outcome-115", "projection_generation: 20260914-outcome-116")
    memory = projection_edit.load(ROOT, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S134 文献水合重绑定：S133 显式 task plan 因 source_hash 自动提升而载入 1.56 MiB TRIAGE + 1.28 MiB candidates，总装配 4.12 MiB。新增小型 `TRIAGE-RECEIPT.json`，认证两文件 bytes/hash/计数；stable record 只水合 denominator、MANIFEST、receipt 与工具/测试，大型派生表按需读取。研究语义与下一 R1 不变。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n\n", "## 当前停止点\n\nS134：LIT task hydration 已改为小 manifest/receipt 路由，大型 candidates/triage 按需读取；S133 分母与下一 R1 main replay 不变。\n\n")

    state["revision"] = 134
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_LIT_HYDRATION_REPIN"
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-116"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-116"

    lit = state["records"][LIT_ID]
    lit["source_hashes"].pop(CANDIDATES, None)
    lit["source_hashes"].pop(TRIAGE, None)
    for rel in [INDEX, TEST, MANIFEST, RECEIPT]:
        lit["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
        add_once(lit["full_sources"], rel)
    lit["revalidation"] = f"{SESSION_ID}: large generated JSON identity routed through MANIFEST and TRIAGE-RECEIPT; explicit hydration no longer promotes their full bodies."
    for record_id in [PLAN_ID, GOAL_ID, AUDIT_ID]:
        record = state["records"][record_id]
        if INDEX in record.get("source_hashes", {}):
            record["source_hashes"][INDEX] = R.sha((ROOT / INDEX).read_bytes())
    state["records"][PLAN_ID]["revalidation"] = f"{SESSION_ID}: literature index re-pinned after receipt routing; plan semantics unchanged."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 发现：S133 literature task hydration 为 4,121,461 bytes，最大两项是 TRIAGE 1,562,324 bytes 与 candidates 1,275,732 bytes。
- 修复：新增 `{RECEIPT}`，记录两项 bytes/hash 与 32/164/1745、33/13/20 计数；从 STATE source_hash hydration 删除大型正文。
- 边界：大型 JSON 原件未改、未删除；按需读取。S133 分母和下一 R1 不变；无数学 claim。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL, "before_task_bytes": 4121461,
        "removed_full_hydration": {TRIAGE: 1562324, CANDIDATES: 1275732},
        "receipt": RECEIPT, "new_math_claims": []
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "MECHANICALLY_VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, RECEIPT],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, LIT_ID], "scope": "Re-pin literature hydration through small receipts; no research-semantic change.",
        "source_hashes": {}, "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "Preserve useful main-project cognition while avoiding automatic full hydration of multi-megabyte derived literature files.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 134, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
