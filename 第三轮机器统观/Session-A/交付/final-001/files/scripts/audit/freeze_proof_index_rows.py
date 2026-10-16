#!/usr/bin/env python3
"""Freeze the exact proof/claim rows for an already indexed immutable run."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath

from mark_proof_run_indexed import (
    expand_claim_ids,
    load_object,
    package_mapping,
    replay_entry,
    same_replay_identity,
)


ROOT = Path(__file__).resolve().parents[2]
RUN_ROOT = Path("HoTT/verification/runs")
REGISTRY_PATH = "HoTT/verification/PROOF_VERSION_CLOSURE.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def unique_row(lines: list[str], identity: str, prefix: str) -> str:
    matches = [line for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise ValueError(f"INDEX_ROW_COUNT:{identity}:{len(matches)}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    run_relative = safe_relative(args.run_dir)
    try:
        run_relative.relative_to(RUN_ROOT)
    except ValueError as exc:
        raise SystemExit("RUN_OUTSIDE_AUTHORITATIVE_ROOT") from exc
    run_dir = root / run_relative
    output = run_dir / "index-row-manifest.json"
    if output.exists():
        raise SystemExit("INDEX_ROW_MANIFEST_ALREADY_EXISTS")
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_ACCEPTED_AND_INDEXED")
    index = run.get("index")
    if not isinstance(index, dict) or index.get("path") != "HoTT/CLAIM_EVIDENCE_MATRIX.md":
        raise SystemExit("INDEX_IDENTITY_INVALID")
    index_path = root / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
    index_data = index_path.read_bytes()
    if index.get("sha256") != sha(index_data):
        raise SystemExit("INDEX_SNAPSHOT_ALREADY_CHANGED")
    proof_id = run.get("proof_id")
    claim_ids = run.get("claim_ids")
    if not isinstance(proof_id, str) or not isinstance(claim_ids, list) or not claim_ids:
        raise SystemExit("RUN_IDENTITIES_INVALID")
    if run.get("run_id") != run_dir.name:
        raise SystemExit("RUN_DIRECTORY_ID_MISMATCH")
    registry = load_object(root / REGISTRY_PATH)
    if registry.get("schema_version") != "hott-proof-version-closure/v2":
        raise SystemExit("PROOF_REGISTRY_V2_REQUIRED")
    package = package_mapping(registry).get(proof_id)
    if package is None or expand_claim_ids(package.get("claim_ids")) != claim_ids:
        raise SystemExit("RUN_DOES_NOT_MATCH_REGISTERED_PACKAGE")
    if package.get("run") == run_relative.as_posix():
        relation = "PRIMARY_RUN"
    else:
        replay_spec = registry.get("replay_runs")
        entries = replay_spec.get("entries") if isinstance(replay_spec, dict) else None
        matches = [
            entry
            for entry in entries or []
            if isinstance(entry, dict) and entry.get("run") == run_relative.as_posix()
        ]
        if len(matches) != 1 or not same_replay_identity(
            matches[0], replay_entry(run_relative.as_posix(), package, run)
        ):
            raise SystemExit("REPLAY_RELATION_MISSING_OR_MISMATCHED")
        relation = "REGISTERED_REPLAY"
    if index.get("relation") != relation or index.get("registry_path") != REGISTRY_PATH:
        raise SystemExit("INDEX_RELATION_INVALID")
    lines = index_data.decode("utf-8").splitlines()
    identities = [("proof", proof_id, f"| `{proof_id}` |")]
    identities.extend(("claim", str(claim_id), f"| {claim_id} |") for claim_id in claim_ids)
    rows = []
    for kind, identity, prefix in identities:
        line = unique_row(lines, identity, prefix)
        rows.append({"kind": kind, "id": identity, "line_sha256": sha(line.encode("utf-8"))})
    payload = {
        "schema_version": "proof-index-row-manifest/v1",
        "run_id": run.get("run_id"),
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "index_path": "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        "index_snapshot_sha256": index.get("sha256"),
        "index_relation": relation,
        "registry_path": REGISTRY_PATH,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "row_hash_semantics": "SHA-256 of the exact UTF-8 Markdown table line without its line terminator",
        "rows": rows,
    }
    data = (json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    with output.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    print(json.dumps({"status": "FROZEN", "run_id": run.get("run_id"), "rows": len(rows), "path": str(output.relative_to(root)), "sha256": sha(data)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
