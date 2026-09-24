#!/usr/bin/env python3
"""Mark a captured run indexed only after an exact proof/run relation exists.

Primary runs must already be the package's run in PROOF_VERSION_CLOSURE.json.
A later replay of the same proof and claims is registered in the registry's
append-only replay_runs list before RUN.json is marked. The matrix rows remain
unchanged, so a replay never overwrites the primary evidence pointer.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import uuid
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import proof_claim_ids as claim_identity
RUN_ROOT = PurePosixPath("HoTT/verification/runs")
INDEX_PATH = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
REGISTRY_PATH = "HoTT/verification/PROOF_VERSION_CLOSURE.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: object) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise SystemExit(f"UNSAFE_PATH:{value}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return path.as_posix()


def expand_claim_ids(value: object) -> list[str]:
    try:
        return claim_identity.expand_claim_ids(value)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def atomic_json(path: Path, value: dict) -> None:
    data = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    temp = path.with_name(f".{path.name}.tmp-{uuid.uuid4().hex}")
    try:
        with temp.open("xb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
        try:
            fd = os.open(path.parent, os.O_RDONLY)
            os.fsync(fd)
            os.close(fd)
        except OSError:
            pass
    finally:
        if temp.exists():
            temp.unlink()


def matrix_identity_lines(data: bytes) -> dict[str, list[str]]:
    return claim_identity.matrix_identity_lines(data)


def require_unique(index: dict[str, list[str]], identity: str) -> None:
    count = len(index.get(identity, []))
    if count != 1:
        raise SystemExit(f"INDEX_ROW_COUNT:{identity}:{count}")


def package_mapping(registry: dict) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for key in ("packages", "later_packages"):
        rows = registry.get(key)
        if not isinstance(rows, list):
            raise SystemExit(f"REGISTRY_{key.upper()}_INVALID")
        for row in rows:
            proof_id = row.get("proof_id") if isinstance(row, dict) else None
            if not isinstance(proof_id, str) or proof_id in mapping:
                raise SystemExit(f"REGISTRY_PROOF_ID_INVALID:{proof_id}")
            mapping[proof_id] = row
    return mapping


def verify_receipt_file(run_dir: Path, run: dict, key: str, name: str) -> None:
    row = run.get(key)
    if not isinstance(row, dict) or row.get("path") != name:
        raise SystemExit(f"RUN_RECEIPT_FIELD_INVALID:{key}")
    data = (run_dir / name).read_bytes()
    if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
        raise SystemExit(f"RUN_RECEIPT_HASH_MISMATCH:{name}")


def replay_entry(run_relative: str, package: dict, run: dict) -> dict:
    return {
        "run": run_relative,
        "proof_id": package["proof_id"],
        "claim_ids": list(run["claim_ids"]),
        "source": package["source"],
        "source_manifest_sha256": run["source_manifest"]["sha256"],
        "stdout_sha256": run["stdout"]["sha256"],
        "stderr_sha256": run["stderr"]["sha256"],
        "environment_sha256": run["environment"]["sha256"],
        "relation": "REPLAY_OF_EXISTING_CLAIMS",
        "registered_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }


def same_replay_identity(left: dict, right: dict) -> bool:
    fields = (
        "run",
        "proof_id",
        "claim_ids",
        "source",
        "source_manifest_sha256",
        "stdout_sha256",
        "stderr_sha256",
        "environment_sha256",
        "relation",
    )
    return all(left.get(field) == right.get(field) for field in fields)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    run_relative = safe_relative(args.run_dir)
    try:
        PurePosixPath(run_relative).relative_to(RUN_ROOT)
    except ValueError as exc:
        raise SystemExit("RUN_OUTSIDE_AUTHORITATIVE_ROOT") from exc

    run_dir = root / run_relative
    run_path = run_dir / "RUN.json"
    run = load_object(run_path)
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("exit_code") != 0:
        raise SystemExit("RUN_NOT_KERNEL_ACCEPTED")
    if run.get("run_id") != PurePosixPath(run_relative).name:
        raise SystemExit("RUN_DIRECTORY_ID_MISMATCH")
    if run.get("index_status") not in {
        "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
    }:
        raise SystemExit(f"UNEXPECTED_INDEX_STATUS:{run.get('index_status')}")

    proof_id = run.get("proof_id")
    claim_ids = run.get("claim_ids")
    if not isinstance(proof_id, str) or not isinstance(claim_ids, list) or not claim_ids:
        raise SystemExit("RUN_IDENTITIES_INVALID")

    registry_path = root / REGISTRY_PATH
    registry = load_object(registry_path)
    if registry.get("schema_version") != "hott-proof-version-closure/v2":
        raise SystemExit("PROOF_REGISTRY_V2_REQUIRED")
    packages = package_mapping(registry)
    package = packages.get(proof_id)
    if package is None:
        raise SystemExit(f"PROOF_NOT_REGISTERED:{proof_id}")
    expected_claims = expand_claim_ids(package.get("claim_ids"))
    if claim_ids != expected_claims:
        raise SystemExit("RUN_CLAIMS_DO_NOT_MATCH_REGISTERED_PACKAGE")

    manifest = load_object(run_dir / "source-manifest.json")
    if manifest.get("proof_id") != proof_id or manifest.get("run_id") != run.get("run_id"):
        raise SystemExit("SOURCE_MANIFEST_IDENTITY_MISMATCH")
    files = manifest.get("files")
    source = package.get("source")
    if not isinstance(files, list) or not isinstance(source, str) or source not in {
        row.get("path") for row in files if isinstance(row, dict)
    }:
        raise SystemExit("REGISTERED_SOURCE_NOT_IN_MANIFEST")
    for key, name in (
        ("stdout", "stdout.txt"),
        ("stderr", "stderr.txt"),
        ("environment", "environment.txt"),
        ("source_manifest", "source-manifest.json"),
    ):
        verify_receipt_file(run_dir, run, key, name)

    index_data = (root / INDEX_PATH).read_bytes()
    index = matrix_identity_lines(index_data)
    require_unique(index, proof_id)
    for claim_id in claim_ids:
        require_unique(index, str(claim_id))

    is_primary = package.get("run") == run_relative
    relation = "PRIMARY_RUN" if is_primary else "REGISTERED_REPLAY"
    replay_spec = registry.get("replay_runs")
    if (
        not isinstance(replay_spec, dict)
        or replay_spec.get("schema_version") != "proof-replay-registry/v1"
        or not isinstance(replay_spec.get("entries"), list)
    ):
        raise SystemExit("REPLAY_REGISTRY_INVALID")

    registry_changed = False
    if not is_primary:
        candidate = replay_entry(run_relative, package, run)
        existing = [
            entry
            for entry in replay_spec["entries"]
            if isinstance(entry, dict) and entry.get("run") == run_relative
        ]
        if len(existing) > 1:
            raise SystemExit("REPLAY_REGISTRATION_DUPLICATE")
        if existing and not same_replay_identity(existing[0], candidate):
            raise SystemExit("REPLAY_REGISTRATION_CONFLICT")
        if not existing:
            replay_spec["entries"].append(candidate)
            replay_spec["entries"].sort(key=lambda entry: entry["run"])
            registry_changed = True

    if run.get("index_status") == "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        if registry_changed:
            atomic_json(registry_path, registry)
        print(
            json.dumps(
                {
                    "status": "ALREADY_INDEXED",
                    "run_id": run.get("run_id"),
                    "relation": relation,
                    "claims": len(claim_ids),
                },
                ensure_ascii=False,
            )
        )
        return 0

    run["index"] = {
        "path": INDEX_PATH,
        "sha256": sha(index_data),
        "relation": relation,
        "registry_path": REGISTRY_PATH,
    }
    run["index_status"] = "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"

    # Write the replay relationship first. If the process stops before RUN.json
    # is replaced, a retry observes the exact existing relationship and safely
    # completes the second write.
    if registry_changed:
        atomic_json(registry_path, registry)
    atomic_json(run_path, run)
    print(
        json.dumps(
            {
                "status": "INDEXED",
                "run_id": run.get("run_id"),
                "relation": relation,
                "index_sha256": run["index"]["sha256"],
                "claims": len(claim_ids),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
