#!/usr/bin/env python3
"""Verify S090 checkpoint receipts and real task-hydration reductions."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION = "S-GOV-20260913-090-CHECKPOINT-HYDRATION-REPAIR"
CHECKPOINT = ROOT / ".codex/cognition/checkpoints" / SESSION
OUTPUT = ROOT / "audit/S090-governance-repair-verification-20260913.json"
HISTORICAL = [
    "S-RES-20260913-086-N40-NOCANONICAL-NATIVE",
    "S-RES-20260913-087-N41-BATCH12",
    "S-RES-20260913-088-N42-UNIMATH-REPLAY",
    "S-RES-20260913-089-N43-HANDOFF-REPORT",
]
BASELINES = {
    "A-NOCANONICAL-POINT-001": {"total_bytes": 26395830, "total_lines": 556646, "documents": 151},
    "A-BATCH12-001": {"total_bytes": 26570797, "total_lines": 560286, "documents": 163},
    "A-UNIMATH-NOSECTION-REPLAY-001": {"total_bytes": 3683462, "total_lines": 21885, "documents": 42},
    "A-HANDOFF-REPORT-S086-S088-001": {"total_bytes": 29415715, "total_lines": 573563, "documents": 188},
}

SPEC = importlib.util.spec_from_file_location("runtime_verify_s090", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class VerificationError(RuntimeError):
    pass


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def plan_row(record: str) -> dict:
    plan = R.plan(ROOT, profile="research", task_ids=(record,))
    diagnostics = plan["hydration_diagnostics"]
    if plan["hydrated_records"] != [record]:
        raise VerificationError(f"UNEXPECTED_TRANSITIVE_HYDRATION:{record}")
    if diagnostics["query_first_promoted"]:
        raise VerificationError(f"QUERY_FIRST_PROMOTED:{record}")
    return {
        "snapshot": plan["snapshot"],
        "total_bytes": plan["total_bytes"],
        "total_lines": plan["total_lines"],
        "documents": len(plan["documents"]),
        "hydrated_records": plan["hydrated_records"],
        "review_required": plan["review_required"],
        "query_first_promoted": diagnostics["query_first_promoted"],
        "largest_documents": diagnostics["largest_documents"],
    }


def build() -> dict:
    state = load(ROOT / R.STATE)
    if state.get("revision", 0) < 90:
        raise VerificationError("STATE_BEFORE_S090")
    result = load(CHECKPOINT / "result.json")
    transaction = load(CHECKPOINT / "transaction.json")
    if result.get("status") != "CHECKPOINT_COMMITTED" or result.get("session_id") != SESSION or result.get("revision") != 90:
        raise VerificationError("S090_RESULT_INVALID")
    if transaction.get("schema_version") != "cognition-transaction/v1" or transaction.get("session_id") != SESSION:
        raise VerificationError("S090_TRANSACTION_INVALID")
    rows = transaction.get("rows")
    if not isinstance(rows, list) or len(rows) != 11:
        raise VerificationError("S090_TRANSACTION_ROWS_INVALID")
    required_session = {
        f".codex/research/hott/sessions/{SESSION}/SESSION.md",
        f".codex/research/hott/sessions/{SESSION}/RUNS.json",
        f".codex/research/hott/sessions/{SESSION}/CORE_COGNITION_AUDIT.md",
    }
    paths = {row.get("path") for row in rows}
    if not required_session <= paths or R.HEAD not in paths:
        raise VerificationError("S090_ATOMIC_SESSION_BUNDLE_MISSING")
    if (ROOT / R.LOCK).exists() or (ROOT / R.TXN).exists():
        raise VerificationError("ACTIVE_WRITER_OR_TRANSACTION_REMAINS")

    historical = []
    for sid in HISTORICAL:
        post_path = ROOT / R.PREFIX / "sessions" / sid / "POST-CHECKPOINT.json"
        post = load(post_path)
        checkpoint = ROOT / ".codex/cognition/checkpoints" / sid
        if post.get("checkpoint_applied") is not True or checkpoint.exists():
            raise VerificationError(f"HISTORICAL_GAP_CHANGED:{sid}")
        historical.append({
            "session_id": sid,
            "post_path": post_path.relative_to(ROOT).as_posix(),
            "post_sha256": sha(post_path),
            "post_claim": "checkpoint_applied=true",
            "canonical_checkpoint_directory_exists": False,
            "status": "CHECKPOINT_RECEIPT_MISSING",
        })

    plans = {}
    for record, before in BASELINES.items():
        after = plan_row(record)
        if after["total_bytes"] >= before["total_bytes"] or after["documents"] >= before["documents"]:
            raise VerificationError(f"HYDRATION_NOT_REDUCED:{record}")
        plans[record] = {
            "before_revision_89": before,
            "after_current": after,
            "byte_reduction": before["total_bytes"] - after["total_bytes"],
            "line_reduction": before["total_lines"] - after["total_lines"],
            "document_reduction": before["documents"] - after["documents"],
        }
    kc_gap = plan_row("A-KC-AUDIT-GAP-001")

    expected_empty = [
        "A-NOCANONICAL-POINT-001", "A-BATCH12-001", "A-UNIMATH-NOSECTION-REPLAY-001",
        "A-UNIMATH-E6-SCAN-001", "A-HANDOFF-REPORT-S086-S088-001",
    ]
    for record in expected_empty:
        if state["records"][record].get("depends_on") != []:
            raise VerificationError(f"NARRATIVE_DEPENDENCY_REMAINS:{record}")
    if state["records"]["A-KC-AUDIT-GAP-001"].get("path_mode") != "scope_locator":
        raise VerificationError("KC_GAP_SCOPE_MODE_MISSING")

    mismatches = []
    pin_count = 0
    for key, record in state["records"].items():
        for rel, expected in record.get("source_hashes", {}).items():
            pin_count += 1
            path = ROOT / rel
            if not path.is_file() or sha(path) != expected:
                mismatches.append({"record": key, "path": rel})
    if mismatches:
        raise VerificationError(f"SOURCE_HASH_MISMATCHES:{len(mismatches)}")

    return {
        "schema_version": "s090-governance-repair-verification/v1",
        "status": "PASS_WITH_SCOPE",
        "current_state_revision": state["revision"],
        "s090_checkpoint": {
            "session_id": SESSION,
            "result_path": (CHECKPOINT / "result.json").relative_to(ROOT).as_posix(),
            "result_sha256": sha(CHECKPOINT / "result.json"),
            "result_status": result["status"],
            "transaction_path": (CHECKPOINT / "transaction.json").relative_to(ROOT).as_posix(),
            "transaction_sha256": sha(CHECKPOINT / "transaction.json"),
            "transaction_rows": len(rows),
            "atomic_session_bundle": sorted(required_session),
            "active_lock_or_transaction": False,
        },
        "historical_checkpoint_receipt_gaps": historical,
        "task_hydration": plans,
        "kc_audit_gap_task": kc_gap,
        "state_source_hashes": {"pins": pin_count, "mismatches": 0},
        "scope": [
            "Verifies project-local checkpoint artifacts, record relationship behavior, current source hashes and plan assembly only.",
            "Does not certify model comprehension, KC semantic quality, mathematical correctness, Git version closure or absence of all E6 consumers.",
        ],
    }


def encode(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def atomic_write(path: Path, data: bytes) -> None:
    fd, raw = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    temp = Path(raw)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data); handle.flush(); os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists(): temp.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        value = build(); data = encode(value); output = args.output.resolve()
        if args.write:
            output.parent.mkdir(parents=True, exist_ok=True); atomic_write(output, data); status = "WROTE"
            receipt_hash = hashlib.sha256(data).hexdigest()
        else:
            if not output.is_file():
                raise VerificationError("OUTPUT_MISSING_USE_WRITE")
            stored = load(output)
            if (stored.get("schema_version") != "s090-governance-repair-verification/v1"
                    or stored.get("status") != "PASS_WITH_SCOPE"
                    or stored.get("s090_checkpoint", {}).get("result_sha256") != value["s090_checkpoint"]["result_sha256"]
                    or len(stored.get("historical_checkpoint_receipt_gaps", [])) != len(HISTORICAL)):
                raise VerificationError("STORED_RECEIPT_IDENTITY_INVALID")
            # Plan totals can legitimately move when unrelated boot documents grow.
            # The live verifier rechecks the material invariant instead: each plan
            # remains reduced from its frozen rev89 baseline and promotes no
            # query-first asset.  The receipt preserves the S090 observation.
            receipt_hash = sha(output)
            status = "PASS_WITH_SCOPE"
        print(json.dumps({
            "status": status,
            "current_state_revision": value["current_state_revision"],
            "checkpoint_result": value["s090_checkpoint"]["result_status"],
            "historical_receipt_gaps": len(value["historical_checkpoint_receipt_gaps"]),
            "task_plans": {key: {"bytes": row["after_current"]["total_bytes"], "documents": row["after_current"]["documents"]} for key, row in value["task_hydration"].items()},
            "kc_gap_task_bytes": value["kc_audit_gap_task"]["total_bytes"],
            "source_hash_mismatches": value["state_source_hashes"]["mismatches"],
            "output_sha256": receipt_hash,
        }, ensure_ascii=False))
        return 0
    except (VerificationError, OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
