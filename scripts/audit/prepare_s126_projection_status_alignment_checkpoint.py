#!/usr/bin/env python3
"""Prepare revision 126: align the load-plan status pointer and report hash."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-126-PROJECTION-STATUS-ALIGNMENT"
PREV = "S-GOV-20260913-125-ROUND2-AUDIT-REPAIR-TAKEOVER"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_ROUND2_AUDIT_REPAIR_TAKEOVER"
REPORT = "audit/统观工作技术报告-20260913.md"
TAKEOVER_REPORT = "audit/独立审计第二轮整改与接管-20260913.md"
LOAD_SET = ".codex/cognition/LOAD_SET.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s126", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本 corrective 只消除 LOAD_SET 重复状态字段的陈旧值并重绑技术报告哈希。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    focus = {
        "KC-000017": ("ALIGNED", "发现启动计划仍显示旧状态后立即纠正，不把上一轮 PASS 当作无遗漏证明。"),
        "KC-000021": ("ALIGNED", "保持 S125 证据关系验证；本轮不修改 proof、run 或数学状态。"),
        "KC-000030": ("CORRECTED", "重复状态字段改为指向 STATE/投影 owner，避免下一 checkpoint 再次漂移。"),
    }
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(
            kid,
            ("NOT_TOUCHED", f"本 corrective 没有触及“{label}”的数学或哲学内容。"),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{TAKEOVER_REPORT}`；{kid} | "
            "S125 开放项不变。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: REVISION_ONLY — 内容不变，只与 STATE revision 126 同步。",
        "- panorama_change: REVISION_ONLY — 内容不变，只与 STATE revision 126 同步。",
        "- essay_change: NO — 第四件不变。",
        "- update_decision: LOAD_SET.projection_status 改成唯一 current owner 指针；技术报告补明确 triage 当前状态。",
        "- cross_conflicts: NONE_AFTER_ALIGNMENT。",
        "- unresolved: S125 登记的数学、triage、未落账轴与 fresh model 开放项全部保持。",
    ]
    return "\n".join(lines) + "\n"


def append_note(record: dict, note: str) -> None:
    old = str(record.get("revalidation", "")).strip()
    record["revalidation"] = (old + " " + note).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 125 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_125_S125")

    load_set = json.loads((root / LOAD_SET).read_text(encoding="utf-8"))
    if load_set.get("projection_status") != "CURRENT_STATUS_OWNED_BY_STATE_PROJECTION_AND_DIRECTION_PANORAMA_INDEXES":
        raise SystemExit("LOAD_SET_STATUS_POINTER_NOT_APPLIED")

    direction = projection_edit.load(root, R.DIRECTION)
    projection_edit.replace_in_index(direction, "source_state_revision: 125", "source_state_revision: 126")
    projection_edit.replace_in_index(
        direction,
        "projection_generation: 20260913-direction-107",
        "projection_generation: 20260913-direction-108",
    )
    panorama = projection_edit.load(root, R.PANORAMA)
    projection_edit.replace_in_index(panorama, "source_state_revision: 125", "source_state_revision: 126")
    projection_edit.replace_in_index(
        panorama,
        "projection_generation: 20260913-outcome-107",
        "projection_generation: 20260913-outcome-108",
    )
    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S126 corrective：S125 后 governance plan 仍从 `LOAD_SET.projection_status` 输出旧 v3.4 状态；"
        "该重复字段现改为指向 STATE/方向/全景唯一 current owner，避免每次 revision 人工同步另一份状态。"
        "同时把技术报告 §5.1 的旧 triage 判词明确标成历史并写入当前 `TRIAGE_PAUSED_COST_BENEFIT_QUEUE_OPEN`。"
        "方向/全景内容不变，只同步 revision 126；数学状态不变。\n",
    )
    essay = projection_edit.load(root, R.ESSAY)

    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260913-direction-108"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260913-outcome-108"
    report_record = state["records"]["A-AUDIT-REPORT-TONGGUAN-001"]
    report_record["source_hashes"][REPORT] = R.sha((root / REPORT).read_bytes())
    append_note(
        report_record,
        f"{SESSION_ID} re-pinned the report after section 5.1 labelled the old triage verdict historical and stated the current open-queue disposition.",
    )
    load_record = state["records"]["A-LOAD-GOVERNANCE-V3-001"]
    append_note(
        load_record,
        f"{SESSION_ID} replaced LOAD_SET's duplicated concrete projection status with a pointer to STATE/projection indexes; loading order and document set are unchanged.",
    )
    repair_record = state["records"]["A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001"]
    repair_record["related_records"].append(SESSION_ID)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 触发：S125 后 governance plan 的 `projection_status` 仍显示 LOAD_SET 中旧 v3.4 具体状态。
- 修复：LOAD_SET 只保留 current owner 指针；STATE 与方向/全景继续拥有具体状态。
- 同步：方向/全景内容不变，source revision 与 projection generation 同事务推进到 126/108。
- 报告：`{REPORT}` 的 triage 历史判词改为显式 historical，并写出当前开放队列状态。
- 验证：checkpoint 后复跑六个 canonical verifier 与九项 proof evidence regression。
- 不变：S125 全部语义修复、proof/run/matrix、数学 claim、ERCF-3 `GATED` 状态。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "change": "projection status pointer alignment and report wording correction",
            "new_math_claims": [],
            "push": "NOT_AUTHORIZED",
            "tag": "NOT_CREATED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 126
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_PROJECTION_STATUS_ALIGNMENT"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, "A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, LOAD_SET, REPORT],
        "source_hashes": {},
        "scope": "Corrective alignment of a duplicated load-plan status field and the technical-report triage wording.",
    }

    texts: dict[str, str] = {
        rel: (root / rel).read_text(encoding="utf-8") for rel in R.MUTABLE
    }
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "Correct the stale duplicated projection-status output discovered during the authorized takeover repair, "
            "and re-pin the report wording. Preserve S125 semantics and make no external or mathematical change."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes())
                if (root / rel).exists()
                else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 126,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
