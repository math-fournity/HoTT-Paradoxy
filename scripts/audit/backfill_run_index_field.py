#!/usr/bin/env python3
"""Backfill the missing `index` field of formal-proof-run/v1 receipts.

For each run whose RUN.json declares index_status == INDEXED_IN_CLAIM_EVIDENCE_MATRIX
but carries no `index` object, locate the matrix snapshot in which the run's
identity first appears (walking Git history forward from the commit that added
the run directory), record {path, sha256}, and write the matching
index-row-manifest.json required by verify_formal_proof_run.py.

Truthful by construction: never fabricates a snapshot; runs whose identity is
absent from every matrix revision are reported as genuine gaps.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
MANIFEST_SCHEMA = "proof-index-row-manifest/v1"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(args: list[str], root: Path) -> str:
    out = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True, check=True, text=True,
    )
    return out.stdout


def run_added_commit(root: Path, run_dir: Path) -> str | None:
    out = git(["log", "--diff-filter=A", "--format=%H", "--", f"{run_dir.relative_to(root)}/"],
              root).strip()
    return out.splitlines()[0] if out else None


def matrix_commits(root: Path) -> list[str]:
    out = git(["log", "--format=%H", "--", MATRIX], root).strip()
    return out.splitlines() if out else []


def matrix_at(root: Path, commit: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{MATRIX}"],
        capture_output=True, check=True,
    ).stdout


def matrix_snapshot_with_identity(root: Path, identities: list[str], from_commits: list[str]) -> tuple[str, bytes] | None:
    for commit in from_commits:
        blob = matrix_at(root, commit)
        text = blob.decode("utf-8", errors="replace")
        if all(i in text for i in identities):
            return commit, blob
    return None


def identities_of(run: dict) -> list[str]:
    ids = [str(run.get("proof_id", "")), str(run.get("run_id", ""))]
    ids += [str(c) for c in run.get("claim_ids", []) or []]
    return [i for i in ids if i and i != "None"]


def write_manifest(run_dir: Path, snapshot_sha: str) -> Path:
    manifest = {
        "schema_version": MANIFEST_SCHEMA,
        "index_path": MATRIX,
        "index_snapshot_sha256": snapshot_sha,
        "note": "backfilled by backfill_run_index_field.py; snapshot = first matrix revision containing this run's identity",
    }
    path = run_dir / "index-row-manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--write", action="store_true", help="write RUN.json and manifests (default: dry-run)")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    mcommits = matrix_commits(root)
    if not mcommits:
        print("FATAL: no matrix history")
        return 2

    stats = {"backfilled": 0, "gap": 0, "skip_has_index": 0, "skip_not_indexed": 0, "skip_other_schema": 0}
    gaps: list[str] = []

    for run_json in sorted((root / "HoTT/verification/runs").glob("*/RUN.json")):
        run_dir = run_json.parent
        run = json.loads(run_json.read_bytes())
        if run.get("schema_version") != "formal-proof-run/v1":
            stats["skip_other_schema"] += 1
            continue
        if isinstance(run.get("index"), dict):
            stats["skip_has_index"] += 1
            continue
        if run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
            stats["skip_not_indexed"] += 1
            continue

        added = run_added_commit(root, run_dir)
        if added is None:
            gaps.append(f"{run_dir.name}: run dir not tracked in git history")
            stats["gap"] += 1
            continue

        # commits touching the matrix, newest-first; only consider commits at or after the run landed
        all_c = [c for c in mcommits]
        # prefer: first matrix revision (chronologically) at/after `added` containing the identity
        chrono = list(reversed(all_c))
        try:
            added_idx = chrono.index(added)
        except ValueError:
            added_idx = 0
        candidates = chrono[added_idx:] if added_idx >= 0 else chrono

        found = matrix_snapshot_with_identity(root, identities_of(run), candidates)
        if found is None:
            gaps.append(f"{run_dir.name}: identity not in any matrix revision at/after {added[:8]}")
            stats["gap"] += 1
            continue

        commit, blob = found
        snapshot_sha = sha(blob)
        run["index"] = {"path": MATRIX, "sha256": snapshot_sha}
        manifest_path = write_manifest(run_dir, snapshot_sha) if args.write else None
        if args.write:
            run_json.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        stats["backfilled"] += 1
        print(f"{'WROTE ' if args.write else 'would-write '} {run_dir.name} <- snapshot {snapshot_sha[:12]} @{commit[:8]}")

    print("\nstats:", json.dumps(stats, ensure_ascii=False))
    if gaps:
        print(f"\nGENUINE GAPS ({len(gaps)}):")
        for g in gaps:
            print("  -", g)
    return 0


if __name__ == "__main__":
    sys.exit(main())
