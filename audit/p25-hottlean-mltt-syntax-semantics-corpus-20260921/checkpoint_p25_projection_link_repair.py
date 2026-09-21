#!/usr/bin/env python3
"""Repair P25's cross-projection links in a new canonical checkpoint."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-GOV-20260921-ASTRA-P25-PROJECTION-LINK-REPAIR"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime_module():
    spec = importlib.util.spec_from_file_location("cognition_runtime", ROOT / ".codex/tools/cognition_runtime.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def edit_module():
    sys.path.insert(0, str(ROOT / "scripts/audit"))
    import projection_edit  # noqa: PLC0415
    return projection_edit


def legacy_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.MULTILINE)
    assert len(headings) == 46
    text = f"# {SID} 核心认知回评\n\n{core['generation']}；46 条。本单元只修复投影引用完整性；兼容单文件审计继续登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    text += "- core_change: NO\n- direction_change: add OUT links to the P25 and ABX current direction rows.\n- panorama_change: no semantic outcome change; existing OUT IDs supply the repaired links.\n- essay_change: NO\n- update_decision: checkpoint revision242 fixes a verifier-detected projection link defect without changing the P26 task.\n- cross_conflicts: no mathematical or HoTT claim changes.\n- unresolved: P26 remains next; source-level and reality-task gaps remain open.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    text += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in headings:
        text += f"| `{kc}` | {title} | `NOT_TOUCHED` | 本单元没有检验该用户原文，只修复方向—成果投影的链接。 | 新研究结果或用户原文才会改变。 |\n"
    return text + "\n## 波次定位\n\n这是 P25 后的最小 current-truth 修复：方向行必须指向已有 OUT 行。它使三方投影验证可用，但不改变 P25、P26 或任何数学判词。\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    runtime = runtime_module()
    edit = edit_module()
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 241 and state["latest_session"] == "S-RES-20260921-ASTRA-P25-HOTTLEAN-CORPUS"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha256(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P25-PROJECTION-REPAIR-PLAN.json").write_bytes(runtime.dump(plan))
    state["revision"] = 242
    state["latest_session"] = SID
    portfolio = state["records"][PLAN]
    portfolio["related_records"] = list(dict.fromkeys(portfolio.get("related_records", []) + [SID]))
    portfolio["revalidation"] = portfolio.get("revalidation", "") + " Revision242 repairs direction-to-outcome links after P25 projection deduplication; P26 task and source scope unchanged."
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "PROJECTION_LINK_REPAIR_CHECKPOINTED",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, "R-P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-20260921"],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"]["last_checkpoint_session"] = SID
    state["execution_control"]["checkpoint_result"] = f".codex/cognition/checkpoints/{SID}/result.json"
    state["execution_control"]["current_phase"] = "PHASE_2_P25_PROJECTION_LINKS_REPAIRED_P26_INTRINSIC_QIIRT_AUDIT_NEXT"

    memory = edit.load(ROOT, "MEMORY.md")
    directions = edit.load(ROOT, "方向追踪.md")
    panorama = edit.load(ROOT, "全景视野.md")
    essay = edit.load(ROOT, "扩展认知.md")
    edit.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md", "；revision241。", "；revision242（方向—成果链接修复，不改P26）。")
    edit.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", "\nS-GOV-20260921-ASTRA-P25-PROJECTION-LINK-REPAIR：P25去重后补齐DIR→OUT引用，三方投影验证由FAIL恢复为预期可通过；P26不变；revision242。\n")

    edit.replace_in_index(directions, "source_state_revision: 241", "source_state_revision: 242")
    edit.replace_in_index(directions, "projection_generation: 20260921-direction-241", "projection_generation: 20260921-direction-242")
    edit.replace_in_index(directions, "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT", "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT_LINKS_REPAIRED")
    edit.replace_in_shard(
        directions,
        "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P25：HoTTLean真实 syntax/checker/model 审计 | P24/P25 | `P26_INTRINSIC_QIIRT_SOURCE_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | P19–P25 | P25确认host/object分层，P26查native intrinsic syntax | P25 report；revision241 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P25：HoTTLean真实 syntax/checker/model 审计 | P24/P25 | `P26_INTRINSIC_QIIRT_SOURCE_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | P25确认host/object分层，P26查native intrinsic syntax | P25 report；revision242 |",
    )
    edit.replace_in_shard(
        directions,
        "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P25 | `P3_PAUSED / INDEPENDENT_P26_RUNNING` | `EVIDENCE_DISCIPLINE` | P15/P17/P25 | 仅新版本固定实际 K 或强 R 才重开 | P21/P25 reports；revision241 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P25 | `P3_PAUSED / INDEPENDENT_P26_RUNNING` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P25 reports；revision242 |",
    )

    edit.replace_in_index(panorama, "source_state_revision: 241", "source_state_revision: 242")
    edit.replace_in_index(panorama, "projection_generation: 20260921-outcome-241", "projection_generation: 20260921-outcome-242")
    edit.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT", "semantic_status: FOUR_TRACK_P25_STRATIFIED_CONSUMER_P26_INTRINSIC_QIIRT_NEXT_LINKS_REPAIRED")

    simple = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in runtime.MUTABLE if rel not in {runtime.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[runtime.PREFIX + "RESUME.md"] = simple[runtime.PREFIX + "RESUME.md"].replace("；revision241。", "；revision242（投影链接修复，P26不变）。", 1)
    rows: list[dict] = []
    for doc in (memory, directions, panorama, essay):
        rows.extend(edit.payload_rows(doc, ROOT))
    seen = {row["path"] for row in rows}
    for rel in runtime.MUTABLE:
        if rel not in seen:
            text = runtime.dump(state).decode("utf-8") if rel == runtime.STATE else simple[rel]
            rows.append({"path": rel, "expected_sha256": sha256(ROOT / rel), "text": text})
    session = f"""# {SID}

- host: codex-desktop
- model: runtime-model-not-certified-by-tool
- tier: T3
- status: `PROJECTION_LINK_REPAIR_CHECKPOINTED / P26_UNCHANGED / NO_NEW_HOTT_DEFECT_CLAIM`
- load_receipt: research plan snapshot `{plan['snapshot']}`; post-P25 current projection identity and link checks.
- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。
"""
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID, "primary_runs": [{"kind": "three-way cognition validator", "before": "DIRECTION_WITHOUT_RESULT_OR_REASON", "repair": "DIR-U-HOTT-FOUR-TRACK→OUT-HOTT-FOUR-TRACK-PLAN and DIR-U-ABX-ORIGINAL-CIRCLE→OUT-ABX-ACTION-INTAKE"}], "new_math_claims": [], "new_kernel_replay": False}
    rows.extend([
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": runtime.dump(runs).decode("utf-8")},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": legacy_audit(state["current_core"])},
    ])
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [PLAN], "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。", "files": rows}
    (OUT / "P25-PROJECTION-REPAIR-PAYLOAD.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("P25-PROJECTION-REPAIR-APPLY.json" if args.apply else "P25-PROJECTION-REPAIR-DRY-RUN.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
