#!/usr/bin/env python3
"""Verify the 17-package Git version-closure registry and optional release tag."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"


class ClosureError(RuntimeError):
    pass


def run_git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if result.returncode != 0:
        raise ClosureError(f"GIT_FAILED:{' '.join(args)}:{result.stderr.decode(errors='replace').strip()}")
    return result.stdout


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict): raise ClosureError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-tag", action="store_true")
    args = parser.parse_args()
    try:
        registry = load(REGISTRY)
        commit = registry.get("proof_asset_commit"); tree = registry.get("proof_asset_tree")
        if registry.get("schema_version") != "hott-proof-version-closure/v1" or not isinstance(commit, str):
            raise ClosureError("REGISTRY_IDENTITY_INVALID")
        if run_git("rev-parse", commit).decode().strip() != commit:
            raise ClosureError("PROOF_COMMIT_NOT_EXACT")
        if run_git("rev-parse", commit + "^{tree}").decode().strip() != tree:
            raise ClosureError("PROOF_TREE_MISMATCH")
        frozen = run_git("show", f"{commit}:HoTT/CLAIM_EVIDENCE_MATRIX.md")
        expected = registry["matrix_at_proof_asset_commit"]
        if {"bytes": len(frozen), "lines": len(frozen.splitlines()), "sha256": sha(frozen)} != {key: expected[key] for key in ("bytes", "lines", "sha256")}:
            raise ClosureError("FROZEN_MATRIX_IDENTITY_MISMATCH")
        current = MATRIX.read_bytes()
        if not current.startswith(frozen) or b"## Git \xe7\x89\x88\xe6\x9c\xac\xe9\x97\xad\xe5\x90\x88\xe7\x99\xbb\xe8\xae\xb0" not in current:
            raise ClosureError("CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR")
        packages = registry.get("packages")
        if not isinstance(packages, list) or len(packages) != 17 or len({row.get("proof_id") for row in packages}) != 17:
            raise ClosureError("PACKAGE_COUNT_OR_ID_INVALID")
        for row in packages:
            for path in (row.get("source"), row.get("run") + "/RUN.json", "HoTT/CLAIM_EVIDENCE_MATRIX.md"):
                run_git("cat-file", "-e", f"{commit}:{path}")
        state = load(ROOT / ".codex/research/hott/STATE.json")
        current_records = [row for row in state["records"].values() if row.get("version_closure", {}).get("proof_asset_commit") == commit]
        if state.get("revision", 0) < 92 or len(current_records) < 19:
            raise ClosureError("STATE_VERSION_CLOSURE_NOT_APPLIED")
        tag_status = "NOT_REQUIRED"
        if args.require_tag:
            tag = registry.get("release_ref")
            tag_commit = run_git("rev-list", "-n", "1", tag).decode().strip()
            head = run_git("rev-parse", "HEAD").decode().strip()
            if tag_commit != head:
                raise ClosureError("RELEASE_TAG_NOT_AT_HEAD")
            tag_status = "TAG_AT_HEAD"
        print(json.dumps({
            "status": "PASS_WITH_SCOPE", "proof_asset_commit": commit,
            "packages": len(packages), "machine_proved_claims": registry["machine_proved_claim_count"],
            "external_replayed_claims": registry["external_replayed_claim_count"],
            "append_only_matrix_successor": True, "state_records_with_closure": len(current_records),
            "tag_status": tag_status, "mathematics": "NOT_REPROVED_BY_GIT_CLOSURE",
        }, ensure_ascii=False))
        return 0
    except (ClosureError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
