#!/usr/bin/env python3
"""Prepare revision 33: record the new-session handover verification (S033).

The new session independently replayed both F-011 proof packages and re-ran the
full governance/verification matrix before trusting the preceding handover
report. Mathematics, directions and outcomes are unchanged; this checkpoint
records the session, aligns the MEMORY/RESUME receipts and moves the projection
revision markers from 32 to 33.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-033-HANDOVER-VERIFICATION"
PREV_SESSION = "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE_PRE = f"{SESSION_REL}/evidence/PRE-CHECKPOINT.json"
EVIDENCE_POST = f"{SESSION_REL}/evidence/POST-CHECKPOINT.json"

SPEC = importlib.util.spec_from_file_location("runtime_handover_verify", RUNTIME_PATH)
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
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | 本轮是接手验证会话：独立重放两个 F-011 proof package 并复跑治理/验证套件；未研究、改写或重新裁决该条用户原文。 | S033/evidence/PRE-CHECKPOINT.json；核心认知.md `{unit['id']}` | partiality quotient natural consumer 与 ERCF-3 仍开放。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只把 `source_state_revision` 同步到 33、projection generation 到 017。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只把 `source_state_revision` 同步到 33、projection generation 到 017。",
        "- update_decision: `S033 session record、MEMORY/RESUME 接手收据与 revision 对齐；proof/数学 owner 与方向、全景语义不变。`",
        "- cross_conflicts: `NONE_OBSERVED` — 上一 AI 回复中的哈希、行数、计数与状态声明在可机械复核范围内全部与直接证据一致。",
        "- unresolved: `fresh model behavior、Git version-close 与 DIR-W-RACE-TIMEOUT 工作包仍开放。`",
        "", "## 汇总", "", "`NOT_TOUCHED=36`；本轮数学状态不变。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：用户把本 repo 与上一 AI 的最后回复交给新 Session；接手要求是独立验证，不继承旧结论。",
        "- 闭包：按固定顺序全文读取三件套（core 32,253B/337 行、direction 24,772B/161 行、panorama 27,570B/144 行）与 boot/research profile；三件套 sha256 与 STATE/HEAD 声明一致。",
        "- 独立重放：`MP-ERCF-001` → `KERNEL_ACCEPTED_WITH_SCOPE / ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH`；`MP-ERCF-TRUNC-001` → `KERNEL_ACCEPTED_WITH_SCOPE / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`。",
        "- 套件复跑：core 7/7、runtime 28/28、reader 17/17、three-way 4/4、F-011 4/4；核心/三方/投影/merge/跨源/ledger/fresh/proof-governance verifier 全部 PASS。",
        "- 声明核对：C4 773 行 SHA `a1510b93…`、core manifest SHA `d3791f58…`、STATE revision 32、27 directions/29 outcomes、60 条 source_hash 零 stale、无锁/事务残留，全部与上一 AI 回复一致。",
        "- 结论：上一 AI 的状态声明在可机械复核范围内成立；未发现冲突。截断判词仍 `DEFENSE_WORKS`，不是悖论；下一步仍是 `DIR-W-RACE-TIMEOUT`。",
        "- 三件套：无语义变化；只把 revision 同步到 33、projection generation 到 017。",
        "- Git：未 commit、未 tag、未 push；本轮不启动新数学研究。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 32 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_32_AND_S032")

    pre = json.loads((root / EVIDENCE_PRE).read_text(encoding="utf-8"))
    if pre.get("status") != "PASS" or pre.get("session_id") != SESSION_ID:
        raise SystemExit("PRE_EVIDENCE_NOT_PASS")
    replay_results = {row["name"]: row for row in pre["replays"]}
    if not (
        replay_results["lean-factorization"]["ok"]
        and replay_results["agda-truncation"]["ok"]
        and all(row["ok"] for row in pre["suites"])
        and all(row["ok"] for row in pre["verifiers"])
    ):
        raise SystemExit("PRE_EVIDENCE_INCOMPLETE")
    if pre["static_checks"]["source_hash_stale"] != 0:
        raise SystemExit("SOURCE_HASH_STALE")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    anchor = "- S032 同步 F-011 record 的 formal/runs README hash；原生 proof task hydration 现在成功且 `review_required=[]`，数学状态不变。"
    new_line = (
        "- S033（接手会话）以新 Session 独立重放 `MP-ERCF-001`（`ROW_STABLE_AFTER_INDEX_EVOLUTION`）与 "
        "`MP-ERCF-TRUNC-001`（`EXACT_INDEX_SNAPSHOT_MATCH`），两者均 "
        "`KERNEL_ACCEPTED_WITH_SCOPE / EXACT_EXIT_STDOUT_STDERR_MATCH`；core 7/7、runtime 28/28、reader 17/17、"
        "three-way 4/4、F-011 4/4 与全部 verifier 复跑 PASS；上一 AI 状态声明在可机械复核范围内成立，数学与方向不变。"
    )
    memory = replace_once(memory, anchor, anchor + "\n" + new_line)

    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 32", "source_state_revision: 33")
    direction = replace_once(
        direction, "projection_generation: 20260912-direction-016", "projection_generation: 20260912-direction-017"
    )
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 32", "source_state_revision: 33")
    panorama = replace_once(
        panorama, "projection_generation: 20260912-outcome-016", "projection_generation: 20260912-outcome-017"
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume_line = (
        "S033 以新 Session 接手：独立重放 `MP-ERCF-001` 与 `MP-ERCF-TRUNC-001`，并复跑全部治理套件与 verifier，"
        "全部 PASS；上一 AI 回复中的哈希、行数与计数声明在可机械复核范围内全部成立。"
        "停止点与下一工作包（`DIR-W-RACE-TIMEOUT` partiality quotient bind×race）不变。\n\n"
    )
    resume = replace_once(resume, "## 当前停止点\n\n", "## 当前停止点\n\n" + resume_line)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")

    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "phase_note": "pre-checkpoint independent verification captured before this checkpoint",
            "git_head": pre["git"]["head"],
            "replays": {row["name"]: row["result"] for row in pre["replays"]},
            "suites": {row["name"]: {"exit_code": row["exit_code"], "ok": row["ok"]} for row in pre["suites"]},
            "verifiers": {
                row["name"]: {"exit_code": row["exit_code"], "status": (row["result"] or {}).get("status")}
                for row in pre["verifiers"]
            },
            "static_checks": pre["static_checks"],
            "evidence": {"pre": EVIDENCE_PRE, "post": EVIDENCE_POST},
            "post_checkpoint_required": [
                "fresh three-way receipt regenerated at revision 33",
                "projection freshness PASS",
                "three-way PASS (27 directions / 29 outcomes)",
                "core 36 units PASS",
                "checkpoint result CHECKPOINT_COMMITTED revision 33",
                "git diff --check clean",
                "no write lock / transaction residual",
            ],
            "mathematics": "UNCHANGED_FROM_MP_ERCF_001_AND_MP_ERCF_TRUNC_001",
            "git_commit": "NOT_AUTHORIZED_THIS_TURN",
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n"

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    state["revision"] = 33
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        }
    )
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, "A-ERCF-TRUNCATION-DEFENSE-001", "A-ERCF-FACTORIZATION-FORMAL-001"],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            EVIDENCE_PRE,
            EVIDENCE_POST,
            "scripts/audit/verify_handover_session.py",
            "scripts/audit/prepare_handover_verification_checkpoint.py",
        ],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_FROM_MP_ERCF_001_AND_MP_ERCF_TRUNC_001",
        "cognition_status": "FRESH_SESSION_HANDOVER_INDEPENDENT_REPLAY_AND_FULL_SUITE_VERIFICATION_PASS",
        "scope": "New-session takeover: full-trio closure, independent exact replay of both F-011 proof packages, full governance/verification matrix re-run, and claim-by-claim consistency audit of the preceding handover report. No new mathematics and no direction change.",
    }

    texts = {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User handed this repo over to a new session. The project protocol requires independent verification and a session record for each work unit. This checkpoint writes only in-repo cognition state (session record, MEMORY/RESUME receipts, revision markers) and makes no Git commit, tag, push, external call or mathematical change.",
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
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 33, "session_id": SESSION_ID},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
