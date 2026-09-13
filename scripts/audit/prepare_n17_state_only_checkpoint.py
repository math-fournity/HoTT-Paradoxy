#!/usr/bin/env python3
"""Prepare revision 63: state/session checkpoint for S063 (N17).

The projection files (方向追踪.md, 全景视野.md, MEMORY.md, FRONTIER.md, LESSONS.md,
RESUME.md) were already updated in place this turn with anchor-based edits; this
script only advances STATE.json, writes the session evidence, and records HEAD.json,
so no text is applied twice.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260913-063-N17-COMPLETION-FORMS-AND-BATCH6"
PREV_SESSION = "S-RES-20260913-062-N16-TRUNC-NORECOVERY-AND-BATCH5"
RESULT_ID = "A-TRUNC-COMPLETION-FORMS-001"
REPORT = "audit/truncation-completion-and-batch6-20260913.md"
SRC = "HoTT/formal/truncation-no-recovery/TruncationNoRecovery.agda"
README = "HoTT/formal/truncation-no-recovery/README.md"
TOOLCHAIN = "HoTT/formal/truncation-no-recovery/TOOLCHAIN.json"
LIBREG = "HoTT/formal/truncation-no-recovery/AGDA_LIBRARIES"
RUN_DIR = "HoTT/verification/runs/20260913-MP-TRUNC-NORECOVERY-001-02"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SAMPLE_SCRIPT = "scripts/audit/sample_understanding_claims_batch6.py"
FILL_SCRIPT = "scripts/audit/fill_understanding_claim_sample_batch6.py"
SAMPLE_JSON = "audit/understanding-claim-sample-batch6-20260912.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [
    REPORT, SRC, README, TOOLCHAIN, LIBREG, MATRIX,
    f"{RUN_DIR}/RUN.json", f"{RUN_DIR}/index-row-manifest.json",
    SAMPLE_SCRIPT, FILL_SCRIPT, SAMPLE_JSON,
]
NEW_STATUS = "N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES"


def sha(root: Path, rel: str) -> str:
    return hashlib.sha256((root / rel).read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    spec = importlib.util.spec_from_file_location("runtime_n17", RUNTIME_PATH)
    assert spec and spec.loader
    R = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(R)

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 62 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_62_AND_S062")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root, rel) for rel in EVIDENCE}
    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    allowed = {MATRIX, SRC, "HoTT/formal/README.md", "HoTT/verification/runs/README.md",
               "HoTT/README.md", "HoTT/verification/VERIFICATION_REPORT.md"}
    unexpected = sorted({rel for _, rel in observed_stale} - allowed)
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = ("Revalidated after S063 (C-139/C-140 completion-form extension of MP-TRUNC-NORECOVERY-001 "
            "and the batch-6 sample); no other proof source, run body or understanding-chapter file changed.")
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root, rel) if (root / rel).is_file() else None)
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "formal_proof_extension_and_sample",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "COMPLETION_IMPOSSIBILITY_INTERNAL_NEGATION_FORMS",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-TRUNC-NORECOVERY-001"],
        "full_sources": EVIDENCE,
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "formal": {
            "proof_id": "MP-TRUNC-NORECOVERY-001",
            "claim_ids": ["C-139", "C-140"],
            "run_id": "20260913-MP-TRUNC-NORECOVERY-001-02",
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "resolution": {
            "reason": "C-139/C-140 restate the no-recovery fence as the internal emptiness of the completion-candidate type (section candidates for Bool; completion candidates for a general separated realization). Run -02 re-checks the whole package on the pinned toolchain (exit 0, zero warnings, exact replay) and the batch-6 sample adds 40 verdicts (27/0/0/13); cumulative 242/2396 with no UNSUPPORTED and no E6.",
            "evidence": EVIDENCE,
        },
        "scope": "Internal negation forms of the truncation no-recovery fence plus the sixth evidence-queue sample. Same DEFENSE_WORKS family; no HoTT inconsistency; E6 remains open.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, *EVIDENCE],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "mathematical_status": "MACHINE_PROVED_COMPLETION_IMPOSSIBILITY_FORMS",
        "cognition_status": "N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED",
        "scope": "Completion-impossibility internal negation forms, batch-6 sample, routing of N18.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260913-direction-047" if rid.startswith("I-DIRECTION") else "20260913-outcome-047"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (REPORT, f"{RUN_DIR}/RUN.json", SAMPLE_JSON, MATRIX, SRC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)

    state["revision"] = 63
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N18: continue the evidence queue by the same proportional rule over the next owner tier "
            "(A3, A9, A0, A2, ...), deduplicated against batches 1-6. If a natural-use chain (E6) appears, "
            "switch immediately to F-011 packaging. Fallback: ERCF-3 T3 (gated by the C8 stop conditions)."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "work_kind": "formal_extension_and_batch6",
        "mathematical_claim_added": True,
        "claim_matrix_updated": {"proof_row": "MP-TRUNC-NORECOVERY-001", "claims": ["C-139", "C-140"]},
        "formal_run": {
            "run_id": "20260913-MP-TRUNC-NORECOVERY-001-02",
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
            "exit_code": 0,
            "stderr_bytes": 0,
            "warnings": 0,
            "index_rows": 8,
        },
        "batch6": {
            "rule": "owners by prior sampling ratio ascending, budget 40, max 5 per owner, equidistant, batches 1-5 excluded",
            "sample_size": 40,
            "verdicts": {"SUPPORTED": 27, "SUPERSEDED_BY_MACHINE_RESULT": 0, "UNSUPPORTED": 0, "PENDING": 13},
            "cumulative": {"sampled": 242, "coverage": "10.1%", "SUPPORTED": 149, "SUPERSEDED": 12, "UNSUPPORTED": 0, "PENDING": 81},
            "e6_found": False,
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"report": REPORT, "sample": SAMPLE_JSON},
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    session_text = "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S062 路由的 N17（证据队列第 6 批）+ 用户主方向的完成资格边界。",
        "- 机器扩展 `MP-TRUNC-NORECOVERY-001`（C-139–C-140）：`noSectionCandidate`（Bool completion-candidate 类型为空）与 `noCompletionCandidate`（一般分离实现下 completion-candidate 类型为空），把 C-136/C-135 改写成理论内部的“完成不可行”否定形式。",
        "- final run `20260913-MP-TRUNC-NORECOVERY-001-02`：Agda 2.8.0-3d04bac + Cubical v0.9、`--safe --cubical --guardedness`、exit 0、stderr 0、零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、独立 `--rerun` 为 `EXACT_EXIT_STDOUT_STDERR_MATCH`；matrix 覆盖 C-134–C-140，冻结 8 行 manifest。",
        "- 第六批抽样：40 条（B5/B3/A8/A7/B1/读遍账本/A1/全量精读 各 5），`SUPPORTED=27`、`PENDING=13`、0 `UNSUPPORTED`、0 `SUPERSEDED`；六批累计 242/2,396（10.1%）：149/12/0/81；E6 六批一致未出现。",
        "- 边界：C-139/C-140 与 C-135/C-136 同族，不新增独立强度；非集合（高阶）目标不外推；不证明 HoTT 内部矛盾；未 commit/tag/push。",
        "- 三件套：direction/panorama revision 63/generation 047；core 不变；无 理解章节 变更。",
        "",
    ])
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "‘不可完成’特征：C-139/C-140 给出理论内部证明完成候选类型为空的形式。"),
        "KC-000013": ("ALIGNED", "理论工具性：完成资格在截断接口被执行而非绕过。"),
        "KC-000022": ("ALIGNED", "B 方向（理论假装已完成）：完成候选类型为空，未发现绕越实例。"),
        "KC-000029": ("DEEPENED", "理论经济：被遗忘的 witness 身份不可由理论自身恢复，本轮给出内部否定形式。"),
        "KC-000036": ("ALIGNED", "E6 六批未出现；gated 状态不变。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(
            unit["id"],
            ("NOT_TOUCHED", "本轮是 S063 机器扩展与第六批抽样；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S063/SESSION.md；{REPORT}；{RUN_DIR}/RUN.json | E6 与队列余量仍开放。 |")
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — C-139/C-140 完成（理论内部否定形式）；N17 第六批 40 条完成（六批累计 242/2,396）；第一工作包转 N18；revision 63/generation 047。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-COMPLETION-FORMS` 与 `OUT-TOP-EVIDENCE-QUEUE-BATCH6`；理解章节 inventory 不变。",
        "- update_decision: `新增 run -02 证据、claim matrix 两行与冻结 8 行 manifest；抽样工件进入 audit/；不重写冻结账本。`",
        "- cross_conflicts: `NONE_OBSERVED` — C-139/C-140 与 C-135/C-136 同向；六批抽样连续无 UNSUPPORTED、无 E6。",
        "- unresolved: `E6、队列余量（冻结分母约 90%）、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `MACHINE_PROVED_COMPLETION_FORMS_PLUS_BATCH6`（新增 2 条机器 claim；无悖论升级）。", "",
    ])
    audit_text = "\n".join(lines)

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next "
            "package. This in-scope checkpoint records the C-139/C-140 extension (internal negation forms of the truncation "
            "no-recovery fence; run -02, exit 0, exact replay, 8-row frozen manifest) and the batch-6 sample (40 claims; "
            "27/0/0/13; cumulative 242/2396 with no UNSUPPORTED and no E6). It routes N18. No Git commit, tag or push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": R.STATE,
                "expected_sha256": hashlib.sha256((root / R.STATE).read_bytes()).hexdigest(),
                "text": json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            },
            {"path": session_path, "expected_sha256": None, "text": session_text},
            {"path": audit_path, "expected_sha256": None, "text": audit_text},
            {"path": runs_path, "expected_sha256": None, "text": runs},
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 63,
                      "session_id": SESSION_ID, "stale_repaired": len(observed_stale)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
