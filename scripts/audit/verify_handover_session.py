#!/usr/bin/env python3
"""Capture the S-GOV-20260912-033 handover verification evidence.

Phase `pre` runs the independent kernel replays, the governance test suites and
all verifiers against the pre-checkpoint revision and freezes the raw results
under the session evidence directory. Phase `post` regenerates the fresh
three-way receipt at the new revision and re-runs the revision-coupled checks.

This script performs no mathematics of its own; it records what the existing
verifiers actually returned, including failures.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "S-GOV-20260912-033-HANDOVER-VERIFICATION"
SESSION_DIR = ROOT / ".codex/research/hott/sessions" / SESSION_ID
EVIDENCE_DIR = SESSION_DIR / "evidence"

TRIO = ["核心认知.md", "方向追踪.md", "全景视野.md"]

REPLAYS = [
    (
        "lean-factorization",
        [
            "python3", "-B", "scripts/audit/verify_formal_proof_run.py",
            "--run-dir", "HoTT/verification/runs/20260912-MP-ERCF-001-02", "--rerun",
        ],
    ),
    (
        "agda-truncation",
        [
            "python3", "-B", "scripts/audit/verify_formal_proof_run.py",
            "--run-dir", "HoTT/verification/runs/20260912-MP-ERCF-TRUNC-001-01", "--rerun",
        ],
    ),
]

SUITES = [
    ("core", ["python3", "-B", "scripts/audit/test_core_cognition.py"]),
    ("three-way", ["python3", "-B", "scripts/audit/test_three_way_cognition.py"]),
    ("f011-governance", ["python3", "-B", "scripts/audit/test_math_proof_delivery_governance.py"]),
    ("cognition-runtime", ["python3", "-B", ".codex/skills/hott-paradox-research/checks/test_cognition_runtime.py"]),
    ("full-closure-reader", ["python3", "-B", ".codex/skills/hott-paradox-research/checks/test_full_closure_loading.py"]),
]

VERIFIERS = [
    ("core-cognition", ["python3", "-B", "scripts/audit/verify_core_cognition.py"]),
    ("three-way", ["python3", "-B", "scripts/audit/verify_three_way_cognition.py"]),
    ("projection-freshness", ["python3", "-B", "scripts/audit/verify_projection_freshness.py"]),
    ("understanding-merge", ["python3", "-B", "scripts/audit/verify_understanding_merge.py"]),
    ("cross-source-reconciliation", ["python3", "-B", "scripts/audit/verify_cross_source_reconciliation.py"]),
    ("history-ledgers", ["python3", "-B", "scripts/audit/verify_history_ledgers.py"]),
    ("math-proof-governance", ["python3", "-B", "scripts/audit/verify_math_proof_delivery_governance.py"]),
]

EXPECTED_REPLAY = {
    "lean-factorization": {
        "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "index_validation": "ROW_STABLE_AFTER_INDEX_EVOLUTION",
        "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
    },
    "agda-truncation": {
        "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
        "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
    },
}


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(argv: list[str]) -> dict:
    started = stamp()
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return {
        "argv": argv,
        "exit_code": proc.returncode,
        "started_at_utc": started,
        "completed_at_utc": stamp(),
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def extract_json(text: str) -> dict | None:
    text = text.strip()
    if not text:
        return None
    try:
        value = json.loads(text)
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        pass
    start, end = text.find("{"), text.rfind("}")
    if 0 <= start < end:
        try:
            value = json.loads(text[start : end + 1])
            return value if isinstance(value, dict) else None
        except json.JSONDecodeError:
            return None
    return None


def sha_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*argv: str) -> tuple[int, str]:
    proc = subprocess.run(["git", *argv], cwd=ROOT, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip()


def trio_records() -> list[dict]:
    rows = []
    for rel in TRIO:
        data = (ROOT / rel).read_bytes()
        rows.append(
            {
                "path": rel,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "lines": data.count(b"\n") + (0 if data.endswith(b"\n") else 1),
            }
        )
    return rows


def static_checks() -> dict:
    state = json.loads((ROOT / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))
    entries = stale = 0
    for record in state["records"].values():
        for rel, expected in record.get("source_hashes", {}).items():
            entries += 1
            if sha_file(ROOT / rel) != expected:
                stale += 1
    audits = {}
    for session in [
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
        "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT",
    ]:
        text = (ROOT / f".codex/research/hott/sessions/{session}/CORE_COGNITION_AUDIT.md").read_text(
            encoding="utf-8"
        )
        audits[session] = sum(1 for line in text.splitlines() if line.startswith("| `KC-"))
    return {
        "state_revision": state.get("revision"),
        "latest_session": state.get("latest_session"),
        "source_hash_entries": entries,
        "source_hash_stale": stale,
        "kc_audit_rows": audits,
        "write_lock_present": (ROOT / ".codex/cognition/WRITE_LOCK.json").exists(),
        "transaction_present": (ROOT / ".codex/cognition/TRANSACTION.json").exists(),
    }


def expected_replay_ok(name: str, result: dict) -> bool:
    expected = EXPECTED_REPLAY[name]
    return (
        result.get("status") == "PASS_WITH_SCOPE"
        and all(result.get(key) == value for key, value in expected.items())
    )


def unittest_ok(exit_code: int, text: str) -> bool:
    last = [line for line in text.splitlines() if line.strip()][-1:]
    return exit_code == 0 and bool(last) and (last[0] == "OK" or last[0].startswith("OK ("))


def phase_pre() -> int:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []

    replays = []
    for name, argv in REPLAYS:
        run_row = run(argv)
        result = extract_json(run_row["stdout"])
        ok = run_row["exit_code"] == 0 and result is not None and expected_replay_ok(name, result)
        if not ok:
            failures.append(f"replay:{name}")
        replays.append(
            {
                "name": name,
                "exit_code": run_row["exit_code"],
                "ok": ok,
                "result": result,
                "stderr_tail": run_row["stderr"][-400:],
                "started_at_utc": run_row["started_at_utc"],
                "completed_at_utc": run_row["completed_at_utc"],
            }
        )

    fresh_pre_path = EVIDENCE_DIR / "pre-fresh-three-way-receipt.json"
    verifier_commands = list(VERIFIERS) + [
        (
            "fresh-three-way",
            [
                "python3", "-B", "scripts/audit/verify_fresh_three_way.py",
                "--output",
                str(fresh_pre_path.relative_to(ROOT)),
            ],
        ),
    ]
    verifiers = []
    for name, argv in verifier_commands:
        run_row = run(argv)
        result = extract_json(run_row["stdout"])
        ok = (
            run_row["exit_code"] == 0
            and result is not None
            and result.get("status") in {"PASS", "PASS_WITH_SCOPE"}
        )
        if not ok:
            failures.append(f"verifier:{name}")
        verifiers.append(
            {
                "name": name,
                "exit_code": run_row["exit_code"],
                "ok": ok,
                "result": result,
                "stderr_tail": run_row["stderr"][-400:],
                "started_at_utc": run_row["started_at_utc"],
                "completed_at_utc": run_row["completed_at_utc"],
            }
        )

    suites = []
    for name, argv in SUITES:
        run_row = run(argv)
        # unittest writes its report to stderr; accept an OK verdict in either stream.
        verdict_text = run_row["stderr"] + run_row["stdout"]
        ok = unittest_ok(run_row["exit_code"], verdict_text)
        if not ok:
            failures.append(f"suite:{name}")
        tail = "\n".join(verdict_text.splitlines()[-6:])
        suites.append(
            {
                "name": name,
                "exit_code": run_row["exit_code"],
                "ok": ok,
                "tail": tail,
                "started_at_utc": run_row["started_at_utc"],
                "completed_at_utc": run_row["completed_at_utc"],
            }
        )

    head_code, head = git("rev-parse", "HEAD")
    subject_code, subject = git("log", "-1", "--format=%h %s")
    _, status = git("status", "--porcelain=v1")
    static = static_checks()
    if static["source_hash_stale"] != 0:
        failures.append("static:source_hash_stale")
    if static["write_lock_present"] or static["transaction_present"]:
        failures.append("static:lock_or_transaction")

    evidence = {
        "schema_version": "handover-verification-evidence/v1",
        "phase": "pre-checkpoint",
        "session_id": SESSION_ID,
        "captured_at_utc": stamp(),
        "git": {
            "head": head if head_code == 0 else None,
            "head_subject": subject if subject_code == 0 else None,
            "dirty_entries": len(status.splitlines()) if status else 0,
        },
        "trio": trio_records(),
        "replays": replays,
        "suites": suites,
        "verifiers": verifiers,
        "static_checks": static,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
    }
    (EVIDENCE_DIR / "PRE-CHECKPOINT.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": evidence["status"],
                "session_id": SESSION_ID,
                "replays": {row["name"]: row["ok"] for row in replays},
                "suites": {row["name"]: row["ok"] for row in suites},
                "verifiers": {row["name"]: row["ok"] for row in verifiers},
                "failures": failures,
            },
            ensure_ascii=False,
        )
    )
    return 0 if not failures else 1


def phase_post() -> int:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []

    fresh = run(["python3", "-B", "scripts/audit/verify_fresh_three_way.py"])
    fresh_result = extract_json(fresh["stdout"])
    if fresh["exit_code"] != 0 or fresh_result is None or fresh_result.get("status") != "PASS_WITH_SCOPE":
        failures.append("fresh-three-way-regeneration")

    post_commands = [
        ("core-cognition", ["python3", "-B", "scripts/audit/verify_core_cognition.py"]),
        ("three-way", ["python3", "-B", "scripts/audit/verify_three_way_cognition.py"]),
        ("three-way-tests", ["python3", "-B", "scripts/audit/test_three_way_cognition.py"]),
        ("projection-freshness", ["python3", "-B", "scripts/audit/verify_projection_freshness.py"]),
    ]
    post = []
    for name, argv in post_commands:
        run_row = run(argv)
        result = extract_json(run_row["stdout"])
        if name.endswith("-tests"):
            verdict_text = run_row["stderr"] + run_row["stdout"]
            ok = unittest_ok(run_row["exit_code"], verdict_text)
            result = {"unittest": "OK" if ok else "FAIL"}
        else:
            ok = (
                run_row["exit_code"] == 0
                and result is not None
                and result.get("status") in {"PASS", "PASS_WITH_SCOPE"}
            )
        if not ok:
            failures.append(f"post:{name}")
        post.append({"name": name, "exit_code": run_row["exit_code"], "ok": ok, "result": result})

    diff_code, _ = git("diff", "--check")
    if diff_code != 0:
        failures.append("git-diff-check")

    checkpoint_result_path = ROOT / ".codex/cognition/checkpoints" / SESSION_ID / "result.json"
    checkpoint_result = (
        json.loads(checkpoint_result_path.read_text(encoding="utf-8"))
        if checkpoint_result_path.is_file()
        else None
    )
    if (
        checkpoint_result is None
        or checkpoint_result.get("status") != "CHECKPOINT_COMMITTED"
        or checkpoint_result.get("revision") != 33
        or checkpoint_result.get("session_id") != SESSION_ID
    ):
        failures.append("checkpoint-result")

    state = json.loads((ROOT / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))
    head = json.loads((ROOT / ".codex/cognition/HEAD.json").read_text(encoding="utf-8"))
    revision_ok = (
        state.get("revision") == 33
        and state.get("latest_session") == SESSION_ID
        and head.get("revision") == 33
        and head.get("latest_session") == SESSION_ID
    )
    if not revision_ok:
        failures.append("revision-33")

    evidence = {
        "schema_version": "handover-verification-evidence/v1",
        "phase": "post-checkpoint",
        "session_id": SESSION_ID,
        "captured_at_utc": stamp(),
        "fresh_three_way": {
            "exit_code": fresh["exit_code"],
            "result": fresh_result,
            "receipt": "audit/fresh-three-way-verification-20260912.json",
        },
        "post_checks": post,
        "git_diff_check_exit": diff_code,
        "checkpoint_result": checkpoint_result,
        "state_revision": state.get("revision"),
        "state_latest_session": state.get("latest_session"),
        "head_revision": head.get("revision"),
        "revision_33_consistent": revision_ok,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
    }
    (EVIDENCE_DIR / "POST-CHECKPOINT.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": evidence["status"],
                "session_id": SESSION_ID,
                "post_checks": {row["name"]: row["ok"] for row in post},
                "revision_33_consistent": revision_ok,
                "failures": failures,
            },
            ensure_ascii=False,
        )
    )
    return 0 if not failures else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=["pre", "post"], required=True)
    args = parser.parse_args()
    return phase_pre() if args.phase == "pre" else phase_post()


if __name__ == "__main__":
    raise SystemExit(main())
