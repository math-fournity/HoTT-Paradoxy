#!/usr/bin/env python3
"""Prepare revision 128: re-pin the dual-track decision and normalize current EOFs."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-128-DUAL-TRACK-FORMAT-ALIGNMENT"
PREV = "S-GOV-20260913-127-MACHINE-OVERVIEW-DUAL-TRACK-DECISION"
RESULT_ID = "A-MACHINE-OVERVIEW-DUAL-TRACK-DECISION-001"
DECISION = "docs/decisions/统观双轨协作与阶段汇合决策-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_MACHINE_OVERVIEW_COORDINATION"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s128", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [index for index, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def append_revalidation(record: dict, note: str) -> None:
    previous = str(record.get("revalidation", "")).strip()
    record["revalidation"] = (previous + " " + note).strip()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000017": ("ALIGNED", "发现新决策文档的格式与 source pin 需对齐后使用 corrective，而不改写 S127 历史事务。"),
        "KC-000021": ("ALIGNED", "本轮不改变 proof/run/index，也不产生数学结论。"),
        "KC-000030": ("ALIGNED", "双轨职责和 Gate 语义保持，只修可读格式与可恢复哈希。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本 corrective 只重绑 S127 决策文档哈希、规范当前 owner EOF，并同步 revision。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(
            kid,
            ("NOT_TOUCHED", f"本 corrective 没有触及“{label}”的数学、物理或研究方向内容。"),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{DECISION}`；{kid} | "
            "S127 开放项保持。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: REVISION_AND_EOF_ONLY — 双轨方向行与优先级不变。",
        "- panorama_change: REVISION_AND_EOF_ONLY — 双轨结果与证据边界不变。",
        "- essay_change: NO — 第四件不变。",
        "- update_decision: 重绑决策文档哈希，移除新文档行尾空格，current row shards 保持单一 EOF newline。",
        "- cross_conflicts: NONE_AFTER_ALIGNMENT。",
        "- unresolved: M 轨 P1/P2、M2–M5、Gate A/B/C 与 S 轨下一候选均不变。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 127 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_127_S127")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction["shards"]["方向追踪/002 - 治理与用户方向.md"] = (
        direction["shards"]["方向追踪/002 - 治理与用户方向.md"].rstrip("\n") + "\n"
    )
    for old, new in (
        ("source_state_revision: 127", "source_state_revision: 128"),
        ("projection_generation: 20260913-direction-109", "projection_generation: 20260913-direction-110"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama["shards"]["全景视野/002 - 治理、门禁与骨架结果.md"] = (
        panorama["shards"]["全景视野/002 - 治理、门禁与骨架结果.md"].rstrip("\n") + "\n"
    )
    for old, new in (
        ("source_state_revision: 127", "source_state_revision: 128"),
        ("projection_generation: 20260913-outcome-109", "projection_generation: 20260913-outcome-110"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "8. 版本闭合：",
        "8. 版本链以 S127/S128 canonical checkpoint 收据和包含本单元的后续本地 commit 为准；不 push、不 tag、不合并机器分支。",
    ).rstrip("\n") + "\n"
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S128 corrective：S127 的双轨职责、Gate A/B/C 与外部证据判断不变；本轮只移除新决策首页的行尾空格、把两个新增投影行恢复为单一 EOF newline、重绑决策 source hash，并把投影 revision 同步到 128。S127 checkpoint 历史不改；未新增数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    state["revision"] = 128
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_DUAL_TRACK_FORMAT_ALIGNMENT"
    state["execution_control"]["status"] = STATUS
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260913-direction-110"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260913-outcome-110"
    result = state["records"][RESULT_ID]
    result["source_hashes"][DECISION] = R.sha((ROOT / DECISION).read_bytes())
    append_revalidation(
        result,
        f"{SESSION_ID} re-pinned the decision after whitespace-only formatting cleanup; responsibilities, gates and evidence verdict are unchanged.",
    )
    result["related_records"].append(SESSION_ID)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 触发：S127 暂存审阅发现新决策首页有行尾空格，两个新增投影 row shard 无 EOF newline，MEMORY 版本行仍写 checkpoint pending。
- 动作：只做格式/哈希/revision 对齐；S127 的双轨职责、Gate A/B/C、最新 M1 `REQUEST_CHANGES` 与不集成判断不变。
- 边界：不修改外部导入原件或 S127 before/after 快照；它们按字节保全，历史空格不清洗。
- 没有：不改机器 worktree、不合并、不 push/tag、不启动数学研究、不新增数学 claim。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "change": "whitespace-only decision cleanup, current row-shard EOF normalization, source-hash and revision alignment",
            "semantic_change": "NONE",
            "new_math_claims": [],
            "machine_worktree_mutation": "NONE",
            "merge": "NOT_PERFORMED_GATE_A_NOT_MET",
            "push": "NOT_AUTHORIZED",
            "tag": "NOT_CREATED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, DECISION],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, RESULT_ID],
        "scope": "Corrective formatting, source-hash and projection-revision alignment after the S127 dual-track decision; no semantic or mathematical change.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[session_path] = session
    texts[audit_path] = audit_text(ROOT)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Correct the formatting and source-hash alignment discovered while completing the user-authorized dual-track coordination decision; preserve S127 semantics.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 128, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
