#!/usr/bin/env python3
"""Backfill the missing `index` field of formal-proof-run/v1 receipts.

For each run whose RUN.json declares index_status == INDEXED_IN_CLAIM_EVIDENCE_MATRIX
but carries no `index` object, locate the matrix snapshot in which the run's
identity first appears (walking Git history forward from the commit that added
the run directory), record {path, sha256}, and write the full
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


def find_index_line(lines: list[str], identity: str, kind: str) -> str:
    prefix = f"| `{identity}` |" if kind == "proof" else f"| {identity} |"
    matches = [l for l in lines if l.startswith(prefix)]
    if len(matches) != 1:
        raise ValueError(f"not a unique index line: {identity} ({len(matches)} matches)")
    return matches[0]


def build_manifest(run: dict, snapshot_text: str, snapshot_sha: str) -> dict:
    proof_id = str(run["proof_id"])
    claim_ids = [str(c) for c in (run.get("claim_ids") or [])]
    lines = snapshot_text.splitlines()
    rows = []
    for kind, identity in [("proof", proof_id), *(("claim", c) for c in claim_ids)]:
        line = find_index_line(lines, identity, kind)
        rows.append({"kind": kind, "id": identity, "line_sha256": sha(line.encode("utf-8"))})
    return {
        "schema_version": MANIFEST_SCHEMA,
        "run_id": str(run.get("run_id")),
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "index_path": MATRIX,
        "index_snapshot_sha256": snapshot_sha,
        "rows": rows,
        "note": "backfilled by backfill_run_index_field.py; snapshot = first matrix revision containing this run's identity",
    }


def identities_of(run: dict) -> list[str]:
    ids = [str(run.get("proof_id", "")), str(run.get("run_id", ""))]
    ids += [str(c) for c in run.get("claim_ids", []) or []]
    return [i for i in ids if i and i != "None"]


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

        # 快照选择：身份在当前矩阵则用当前快照（EXACT_INDEX_SNAPSHOT_MATCH 路径，
        # 无需 manifest）；否则回退到首个含身份的历史版本。
        head_commit = mcommits[0]
        head_blob = matrix_at(root, head_commit)
        head_text = head_blob.decode("utf-8", errors="replace")
        if all(i in head_text for i in identities_of(run)):
            blob, commit, use_head = head_blob, head_commit, True
        else:
            chrono = list(reversed(mcommits))
            try:
                added_idx = chrono.index(added)
            except ValueError:
                added_idx = 0
            blob, commit, use_head = None, None, False
            for c in chrono[added_idx:]:
                b = matrix_at(root, c)
                if all(i in b.decode("utf-8", errors="replace") for i in identities_of(run)):
                    blob, commit = b, c
                    break
            if blob is None:
                gaps.append(f"{run_dir.name}: identity not in any matrix revision at/after {added[:8]}")
                stats["gap"] += 1
                continue

        snapshot_sha = sha(blob)
        run["index"] = {"path": MATRIX, "sha256": snapshot_sha}
        if args.write:
            run_json.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            # manifest 仅在行唯一时写（多 run 同 proof_id 时跳过，走 EXACT 路径）
            try:
                manifest = build_manifest(run, blob.decode("utf-8"), snapshot_sha)
                (run_dir / "index-row-manifest.json").write_text(
                    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            except ValueError as e:
                print(f"  (skip manifest for {run_dir.name}: {e})")
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
