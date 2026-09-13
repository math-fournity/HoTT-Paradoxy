#!/usr/bin/env python3
"""Prepare revision 122: re-pin the audit report after its addendum and log the corrective history."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-122-AUDIT-REPORT-ADDENDUM-REPIN"
PREV = "S-GOV-20260913-121-PROJECTION-REVISION-REPAIR-2"
RESULT_ID = "A-AUDIT-REPORT-TONGGUAN-001"
REPORT = "audit/统观工作技术报告-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s122", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "把报告自身的登记/修正历史（含一次被 verifier 抓住的错误）如实写进审计输入。"),
    "KC-000017": ("ALIGNED", "重绑只更新报告哈希与其 revalidation 说明，主张与判词不变。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是**审计输入的附记与哈希重绑**，不产生任何数学或理论结论。",
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
        "- direction_change: NO — 本轮不改投影内容（S121 已对齐版本行）。",
        "- panorama_change: NO — 无新成果行。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 报告加「附记」（登记历史与一次被 verifier 抓住的错误），记录哈希重绑；主张与判词不变。",
        "- cross_conflicts: 无新增；报告正文的 rev118 与附记的 rev121/122 的差异已在附记中显式说明。",
        "- unresolved: 同前（外部审计意见未回收；表示性/反射/对角不动点未做）。",
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
    if state.get("revision") != 121 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_121_S121")
    record = state["records"].get(RESULT_ID)
    if not record:
        raise SystemExit("REPORT_RECORD_MISSING")
    old_hash = (record.get("source_hashes") or {}).get(REPORT)
    new_hash = R.sha((root / REPORT).read_bytes())
    if old_hash == new_hash:
        raise SystemExit("REPORT_HASH_UNCHANGED")
    record["source_hashes"] = {REPORT: new_hash}
    record["revalidation"] = (
        f"{REPORT} re-hashed by {SESSION_ID}: the report gained an addendum recording its own registration history "
        "(revisions 119-121, including the corrective that mis-set the projection revision line). Content outside the "
        "addendum unchanged; scope, evidence status (DOCUMENTED) and all claims/verdicts unchanged."
    )
    record["full_sources"] = sorted(set(record.get("full_sources", []) + [REPORT, ".codex/research/hott/STATE.json"]))

    mem = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        mem,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S122：审计报告加「附记」并重绑哈希（`A-AUDIT-REPORT-TONGGUAN-001`）。附记如实记录 119–121 三个事务，"
        "其中 S120 是一次**被 verifier 抓住的错误**（把投影 `source_state_revision` 写成 119 而 `STATE.revision` 是 120），"
        "S121 对齐后六个 verifier 全 PASS。报告正文主张、判词、claim 均未变；重绑只更新哈希与 revalidation 说明。\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 类型：审计输入的附记 + 哈希重绑（corrective 收尾）。
- 变更：`{REPORT}` 追加「附记」（119–121 的登记历史，含 S120 的错误与 S121 的修正）；
  `{RESULT_ID}.source_hashes[{REPORT}]` 由 `{str(old_hash)[:16]}…` 更新为 `{new_hash[:16]}…`，并写入 revalidation 说明。
- 不变：报告正文主张、全部 claim、判词、run、闭包登记、投影内容（S121 已对齐）。
- 目的：交给外部审计的文本与 repo 记录一致；同时把一个"治理机制抓到自己错误"的实例留在审计输入里。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "repinned": {REPORT: {"old_prefix": str(old_hash)[:16], "new_prefix": new_hash[:16]}},
            "new_math_claims": [],
            "verdict_changes": [],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 122
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_AUDIT_REPORT_ADDENDUM_REPIN",
            "status": STATUS,
            "next_minimal_verification": (
                "The external-audit input `audit/统观工作技术报告-20260913.md` is final as of revision 122 (record "
                "A-AUDIT-REPORT-TONGGUAN-001, re-hashed). Await the external audit; on arrival absorb its findings with the "
                "C11-review procedure (byte-preserved import, item-by-item verification, in-place revision, corrective "
                "re-pin, all six verifiers). Do not add more T3 coding-side work meanwhile: the self-contained coding line "
                "is closed and the remaining obligations (object-level representability, proof-predicate representability, "
                "reflection, diagonal fixed point) need the door-B consumer. ERCF-3 stays GATED."
            ),
        }
    )
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REPORT],
        "source_hashes": {},
        "scope": "Registration of the audit-report addendum and the re-pin of its hash on the report record.",
    }

    texts: dict[str, str] = {rel: (root / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    texts[mem["index_path"]] = mem["index_text"]
    texts.update(mem["shards"])
    for rel in (R.DIRECTION, R.PANORAMA, R.ESSAY):
        texts.update(projection_edit.load(root, rel)["shards"])
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "Finalize the external-audit input: add the addendum documenting its own registration/corrective history and "
            "re-pin the report hash on its record. No claim, verdict or projection change; no push."
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
                "revision": 122,
                "session_id": SESSION_ID,
                "files": len(texts),
                "report_sha256": new_hash[:16],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
