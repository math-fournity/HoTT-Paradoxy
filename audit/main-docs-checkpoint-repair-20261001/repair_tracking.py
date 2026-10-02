#!/usr/bin/env python3
"""Reconcile the two known committed MEMORY hashes in derived cognition HEAD.

This is a bounded pre-checkpoint repair, modeled on the project's 2026-09-19
tracking-recovery procedure. It does not modify STATE.json or create/replace a
checkpoint receipt. The following canonical cognition_runtime checkpoint is
the only operation that advances STATE/HEAD revision and records the task.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE_COMMIT = "d766ebd95e480cb182d812f11a5a5959fb248c10"
EXPECTED_CURRENT_COMMIT = "72520807057c974a7d565159b2fe1e6f47be972d"
EXPECTED_REVISION = 294
EXPECTED_SESSION = "S-GOV-20261001-CIRCLE-ZENO-ATTRIBUTION-UPDATE"
CHECKPOINT = ".codex/cognition/checkpoints/" + EXPECTED_SESSION
TARGETS = {
    "MEMORY/001 - 当前执行队列.md": {
        "old": "ed38ace85ad288e3154c2559ab45644c12693dc51c3771a236749f3933c7ed7d",
        "new": "da354866d875f333be051672fbf8891bfbcb59e62711252ce98c901b55b5d6ca",
    },
    "MEMORY/003 - 当前验证状态与顺序日志.md": {
        "old": "a1c1b2140557e91ce447dbd7d3b3de7ffc572b292b1a39cc5f0f83168031a8df",
        "new": "b2e554a3ecfeb03bc6b91add9289476cdc3f01cff870f4b5b2afd93d8463e386",
    },
}
PUBLICATION_COMMITS = {
    "c42dad4e28ea41813e0a0c9395fca52b19ff7409",
    "9d686d1d7515ba357fc9979a9024c68f6cb7daae",
    "8830767eb4e2fd10f44791126278764cc0f7e96e",
}


def load_runtime():
    spec = importlib.util.spec_from_file_location(
        "cognition_runtime_tracking_repair", ROOT / ".codex/tools/cognition_runtime.py"
    )
    if not spec or not spec.loader:
        raise SystemExit("COGNITION_RUNTIME_NOT_LOADABLE")
    runtime = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runtime)
    return runtime


R = load_runtime()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def prepare() -> tuple[dict, bytes, bytes, dict[str, bytes]]:
    if ROOT.resolve() != Path("/Volumes/D/HoTT_AI_HANDOFF_20260911").resolve():
        raise SystemExit("UNEXPECTED_REPOSITORY_ROOT")
    if git("branch", "--show-current").decode().strip() != "dev":
        raise SystemExit("UNEXPECTED_SOURCE_BRANCH")
    if git("rev-parse", "HEAD").decode().strip() != EXPECTED_CURRENT_COMMIT:
        raise SystemExit("UNEXPECTED_SOURCE_HEAD")
    if (ROOT / R.LOCK).exists() or (ROOT / R.TXN).exists():
        raise SystemExit("CHECKPOINT_WRITER_OR_TRANSACTION_ACTIVE")

    state_bytes = (ROOT / R.STATE).read_bytes()
    state = json.loads(state_bytes)
    head_path = ROOT / R.HEAD
    before = head_path.read_bytes()
    head = json.loads(before)
    if state.get("revision") != EXPECTED_REVISION or head.get("revision") != EXPECTED_REVISION:
        raise SystemExit("UNEXPECTED_REVISION")
    if state.get("latest_session") != EXPECTED_SESSION or head.get("latest_session") != EXPECTED_SESSION:
        raise SystemExit("UNEXPECTED_LATEST_SESSION")
    if git("status", "--porcelain=v1", "--", R.STATE, R.HEAD, *TARGETS).decode().strip():
        raise SystemExit("TRACKING_REPAIR_TARGETS_NOT_GIT_CLEAN")

    actual_drift = {
        rel: sha((ROOT / rel).read_bytes())
        for rel, expected in head.get("tracked", {}).items()
        if sha((ROOT / rel).read_bytes()) != expected
    }
    expected_drift = {rel: item["new"] for rel, item in TARGETS.items()}
    if actual_drift != expected_drift:
        raise SystemExit(f"TRACKING_DRIFT_SET_MISMATCH:{json.dumps(actual_drift, sort_keys=True)}")

    diffs: dict[str, bytes] = {}
    for rel, pins in TARGETS.items():
        old_copy = ROOT / CHECKPOINT / "after" / rel
        if not old_copy.is_file() or sha(old_copy.read_bytes()) != pins["old"]:
            raise SystemExit(f"CHECKPOINT_AFTER_COPY_MISMATCH:{rel}")
        if head["tracked"].get(rel) != pins["old"]:
            raise SystemExit(f"HEAD_BASE_HASH_MISMATCH:{rel}")
        current = (ROOT / rel).read_bytes()
        if sha(current) != pins["new"]:
            raise SystemExit(f"CURRENT_HASH_MISMATCH:{rel}")
        if sha(git("show", f"{EXPECTED_CURRENT_COMMIT}:{rel}")) != pins["new"]:
            raise SystemExit(f"COMMITTED_BLOB_MISMATCH:{rel}")
        changed = set(git("log", "--format=%H", f"{BASE_COMMIT}..{EXPECTED_CURRENT_COMMIT}", "--", rel).decode().splitlines())
        if changed != PUBLICATION_COMMITS:
            raise SystemExit(f"UNEXPECTED_COMMIT_PROVENANCE:{rel}:{sorted(changed)}")
        diff = subprocess.run(
            ["git", "diff", "--no-ext-diff", "--no-index", "--unified=3", "--", str(old_copy), str(ROOT / rel)],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if diff.returncode not in (0, 1):
            raise SystemExit(f"DIFF_CAPTURE_FAILED:{rel}:{diff.stderr.decode(errors='replace')}")
        diffs[rel] = diff.stdout

    after_head = dict(head)
    after_head["tracked"] = dict(head["tracked"])
    for rel, pins in TARGETS.items():
        after_head["tracked"][rel] = pins["new"]
    after_head["updated_at_utc"] = R.stamp()
    after = R.dump(after_head)
    receipt = {
        "schema_version": "derived-cognition-tracking-repair/v1",
        "status": "PREPARED",
        "authorization_scope": "Reconcile only the two clean, committed MEMORY publication-log files against their exact post-S-GOV-20261001 checkpoint copies before a new canonical checkpoint. No STATE record, historical receipt, mathematics, or user file is rewritten.",
        "repository_head": EXPECTED_CURRENT_COMMIT,
        "base_checkpoint": CHECKPOINT,
        "base_checkpoint_session": EXPECTED_SESSION,
        "revision": EXPECTED_REVISION,
        "latest_session": EXPECTED_SESSION,
        "publication_commits_after_checkpoint": sorted(PUBLICATION_COMMITS),
        "state_sha256_before": sha(state_bytes),
        "head_sha256_before": sha(before),
        "head_sha256_after": sha(after),
        "state_changed": False,
        "historical_checkpoint_receipt_changed": False,
        "new_checkpoint_created": False,
        "files": {rel: {"old_sha256": data["old"], "new_sha256": data["new"]} for rel, data in TARGETS.items()},
    }
    return receipt, before, after, diffs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    receipt, before, after, diffs = prepare()
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    if not args.apply:
        return 0
    output_names = ["HEAD.before.json", "HEAD.after.json", "MEMORY-001.diff", "MEMORY-003.diff", "REPAIR.json"]
    for name in output_names:
        if (OUT / name).exists():
            raise SystemExit(f"REPAIR_EVIDENCE_ALREADY_EXISTS:{name}")
    head_path = ROOT / R.HEAD
    if head_path.read_bytes() != before or sha((ROOT / R.STATE).read_bytes()) != receipt["state_sha256_before"]:
        raise SystemExit("TRACKING_REPAIR_BASE_CHANGED_DURING_APPLY")
    if (ROOT / R.LOCK).exists() or (ROOT / R.TXN).exists():
        raise SystemExit("CHECKPOINT_WRITER_OR_TRANSACTION_ACTIVE")
    R.atomic(OUT / "HEAD.before.json", before)
    R.atomic(OUT / "HEAD.after.json", after)
    R.atomic(OUT / "MEMORY-001.diff", diffs["MEMORY/001 - 当前执行队列.md"])
    R.atomic(OUT / "MEMORY-003.diff", diffs["MEMORY/003 - 当前验证状态与顺序日志.md"])
    R.atomic(head_path, after)
    applied = dict(receipt)
    applied["status"] = "DERIVED_TRACKING_RECONCILED"
    applied["applied_head_sha256"] = sha(head_path.read_bytes())
    if applied["applied_head_sha256"] != applied["head_sha256_after"]:
        raise SystemExit("HEAD_POSTWRITE_MISMATCH")
    R.atomic(OUT / "REPAIR.json", R.dump(applied))
    print(json.dumps({"status": applied["status"], "receipt": str(OUT / "REPAIR.json")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
