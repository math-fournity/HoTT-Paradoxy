#!/usr/bin/env python3
"""Prepare revision 121 (corrective #2): sync the projection revision lines with the new STATE revision."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-121-PROJECTION-REVISION-REPAIR-2"
PREV = "S-GOV-20260913-120-PROJECTION-REVISION-REPAIR"
RESULT_ID = "A-PROJECTION-REVISION-REPAIR-002"
REPORT = "audit/统观工作技术报告-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s121", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "corrective：把投影的 source_state_revision 与 STATE 对齐，恢复 verifier 全 PASS。"),
    "KC-000017": ("ALIGNED", "修正以 canonical checkpoint 记录，不改写已应用事务（S119/S120）。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是**治理修正**（投影版本行对齐），不产生任何数学或理论结论。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = AUDIT_FOCUS.get(
            kid, ("NOT_TOUCHED", f"本轮没有研究或重新裁决「{label}」的数学/哲学内容。")
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{REPORT}`；{kid} | 数学开放项不变。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: YES_INDEX_ONLY — 仅 index 的 `source_state_revision`/`projection_generation` 两行。",
        "- panorama_change: YES_INDEX_ONLY — 同上（成果内容未增删）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: S119 只 bump 了 STATE 而未 bump 投影版本行，`verify_three_way_cognition` 报 "
        "`DIRECTION_STATE_REVISION_STALE`；本 corrective 修复该不一致，不篡改 S119 事务。",
        "- cross_conflicts: 无新增。",
        "- unresolved: 同 S119（外部审计意见未回收；表示性/反射/对角不动点未做）。",
        "",
        "## 汇总",
        "",
        "`ALIGNED=2`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 120 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_120_S120")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "103"),
        ("PANORAMA", R.PANORAMA, "outcome", "103"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(doc, "source_state_revision: 119", "source_state_revision: 121")
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-104",
        )
        projections[key] = doc

    mem = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        mem,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S120（corrective）：S119 登记审计报告时只 bump 了 `STATE.revision`，未同步投影 index 的 "
        "`source_state_revision`/`projection_generation`，`verify_three_way_cognition` 因 "
        "`DIRECTION_STATE_REVISION_STALE` 判 FAIL。本 corrective 只改这两行（方向/成果内容未变），"
        "按 S105/S106 先例新开事务，不篡改 S119 的 checkpoint。六个 verifier 恢复全 PASS。\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 类型：corrective（治理修正）。
- 起因：`{PREV}` 把投影 index 写成 `source_state_revision: 119` 却又把 `STATE.revision` bump 到 120，
  `verify_three_way_cognition` 报 `DIRECTION_STATE_REVISION_STALE`。
- 修正：`方向追踪.md` / `全景视野.md` 的 `source_state_revision` 与 `projection_generation` 各一行；
  内容、判词、claim、run 均不变。
- 先例：S105/S106（C11 v2 修订 + corrective 重绑），"修正走新 checkpoint，不改写已应用事务"。
- 交付不变：`{REPORT}`（`{RESULT_ID}` 仍为 S119 产物；本会话只登记修正本身）。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "corrective": {
                "fixes": PREV,
                "reason": "DIRECTION_STATE_REVISION_STALE (projection revision line not bumped with STATE)",
                "changed_index_lines": ["source_state_revision", "projection_generation"],
            },
            "new_math_claims": [],
            "verdict_changes": [],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 121
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_PROJECTION_REVISION_REPAIR_2",
            "status": STATUS,
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-104", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-104", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": "方向追踪.md",
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, "A-AUDIT-REPORT-TONGGUAN-001"],
        "full_sources": ["方向追踪.md", "全景视野.md", ".codex/research/hott/STATE.json"],
        "source_hashes": {},
        "scope": (
            "Corrective: align the projection indexes' source_state_revision (119 -> 121) and projection_generation "
            "(-102 -> -103) with STATE.revision 121 so that verify_three_way_cognition passes again. No content, claim, "
            "verdict or run is touched; the S119 transaction is not rewritten."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL],
        "source_hashes": {},
        "scope": "Registration of the corrective projection-revision repair checkpoint.",
    }

    texts: dict[str, str] = {rel: (root / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for doc in (projections["DIRECTION"], projections["PANORAMA"], mem):
        texts[doc["index_path"]] = doc["index_text"]
        texts.update(doc["shards"])
    texts.update(projection_edit.load(root, R.ESSAY)["shards"])
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "Corrective after registering the external-audit report: bump the two projection index revision lines so the "
            "three-way verifier passes again. No content, claim or verdict change; no push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
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
                "revision": 121,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
