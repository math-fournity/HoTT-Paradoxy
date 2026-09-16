#!/usr/bin/env python3
"""Capture the F-011 replay of the CSL 2026 groupoid-syntax formalisation."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01"
PROOF_ID = "MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001"
CLAIM_IDS = ["C-223", "C-224", "C-225", "C-226"]
RUN_REL = Path("HoTT/verification/runs") / RUN_ID
RUN_DIR = ROOT / RUN_REL
FORMAL_ROOT = Path("HoTT/formal/external-cubical-groupoid-syntax")
SOURCE_CACHE = Path("/Volumes/D/HoTT-literature-cache/groupoid-syntax-cohtt-5babc385")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def file_row(relative: Path) -> dict[str, object]:
    path = ROOT / relative
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"SOURCE_INVALID:{relative}")
    data = path.read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def external_file(path: Path, label: str, publisher_digest: str | None = None) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"EXTERNAL_FILE_INVALID:{label}")
    data = path.read_bytes()
    row: dict[str, object] = {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}
    if publisher_digest is not None:
        row["publisher_digest"] = publisher_digest
    return row


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def main() -> int:
    if not (ROOT / ".git").is_dir():
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")
    if RUN_DIR.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")
    replay_source = json.loads((ROOT / FORMAL_ROOT / "REPLAY_SOURCE.json").read_text(encoding="utf-8"))
    toolchain_path = Path("HoTT/formal/partiality-race-timeout/TOOLCHAIN.json")
    toolchain = json.loads((ROOT / toolchain_path).read_text(encoding="utf-8"))
    source_paths = [
        FORMAL_ROOT / "README.md",
        FORMAL_ROOT / "CLAIM-G-HOTT-SYNTAX.md",
        FORMAL_ROOT / "CheckGroupoidSyntax.agda",
        FORMAL_ROOT / "cohtt-replay.agda-lib",
        FORMAL_ROOT / "REPLAY_SOURCE.json",
        FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json",
        FORMAL_ROOT / "TARGET_SOURCE_MANIFEST.json",
        toolchain_path,
        Path("scripts/audit/import_cubical_groupoid_syntax.py"),
        Path("scripts/audit/replay_cubical_groupoid_syntax.py"),
        Path("scripts/audit/capture_cubical_groupoid_syntax_run.py"),
        Path("scripts/audit/verify_formal_proof_run.py"),
    ]
    source_rows = [file_row(path) for path in source_paths]

    upstream_archive = external_file(SOURCE_CACHE / "source.tar.gz", "cubical-groupoid-syntax-bitbucket-archive")
    if (
        upstream_archive["bytes"] != replay_source["archive"]["bytes"]
        or upstream_archive["sha256"] != replay_source["archive"]["sha256"]
    ):
        raise SystemExit("UPSTREAM_ARCHIVE_MISMATCH")
    cohtt_tree = {
        "label": "cubical-groupoid-syntax-extracted-tree",
        "local_path": str(SOURCE_CACHE / "git-export"),
        **replay_source["verifier_tree_excluding_ds_store"],
        "upstream_commit": replay_source["commit"],
        "git_tree": replay_source["git_tree"],
    }
    agda = toolchain["agda"]
    cubical = toolchain["cubical_library"]
    external_dependencies = [
        upstream_archive,
        cohtt_tree,
        external_file(Path(agda["local_archive"]), "agda-release-archive", agda["asset_sha256"]),
        external_file(Path(agda["local_binary"]), "agda-binary"),
        external_file(Path(cubical["local_archive"]), "cubical-release-archive", cubical["asset_sha256"]),
        {
            "label": "cubical-extracted-tree",
            "local_path": cubical["local_root"],
            "file_count": cubical["tree_file_count"],
            "total_bytes": cubical["tree_total_bytes"],
            "tree_sha256": cubical["tree_sha256"],
            "version": cubical["version"],
            "tag_commit": cubical["tag_commit"],
        },
    ]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": source_rows,
        "external_dependencies": external_dependencies,
    }
    source_manifest_data = json_bytes(source_manifest)
    command = ["/usr/bin/env", "python3", "-B", "scripts/audit/replay_cubical_groupoid_syntax.py"]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        "agda_version=2.8.0-3d04bac",
        f"agda_binary_sha256={agda['binary_sha256']}",
        "cubical_library_version=0.9",
        f"cubical_tree_sha256={cubical['tree_sha256']}",
        "upstream=bitbucket.org/akaposi/cohtt",
        "upstream_commit=5babc385d01500c1777ff932dd8c79299a1d766a",
        "upstream_git_tree=13849af00ff393300c0ae6cdd47ba6ddfa0d1cd8",
        "replay=two-phase fresh dependency baseline then upstream library flags and project theorem probe",
        "trust_scope=Cubical Agda kernel plus pinned binary, Cubical v0.9 tree and hash-qualified cohtt source",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "proof_assistant": "Agda",
        "proof_assistant_version": "Agda version 2.8.0-3d04bac",
        "theory_variant": "Cubical Agda with native Path and higher inductive types; external groupoid-syntax replay",
        "command_argv": command,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": "Replay all 20 current TT modules from akaposi/cohtt@5babc385 and check a project probe for isSetTy plus Con/Sub/Ty/Tm isomorphisms between groupoid and set syntax.",
        "non_goals": [
            "This is an exact machine-replayed syntax slice with Pi, U/El and a base family, not a complete HoTT calculus.",
            "It has no natural numbers, general identity type, object-level univalence or HIT rules, proof-code enumerator, arithmetic interpretation or Goedel sentence.",
            "The replay does not establish undecidability, incompleteness, HoTT essentiality, a natural consumer, a reality bridge or a paradox.",
            "The upstream code tree has no explicit source-code license file; no redistribution permission is inferred.",
        ],
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": len(source_manifest_data), "sha256": sha(source_manifest_data)},
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    RUN_DIR.mkdir(parents=True, exist_ok=False)
    try:
        exclusive_write(RUN_DIR / "stdout.txt", result.stdout)
        exclusive_write(RUN_DIR / "stderr.txt", result.stderr)
        exclusive_write(RUN_DIR / "environment.txt", environment)
        exclusive_write(RUN_DIR / "source-manifest.json", source_manifest_data)
        exclusive_write(RUN_DIR / "RUN.json", json_bytes(run))
    except BaseException:
        print(f"PARTIAL_RUN_DIRECTORY_RETAINED:{RUN_REL.as_posix()}")
        raise
    print(json.dumps({
        "status": run["status"],
        "run_path": RUN_REL.as_posix(),
        "exit_code": result.returncode,
        "stdout_bytes": len(result.stdout),
        "stderr_bytes": len(result.stderr),
        "source_files": len(source_rows),
        "external_dependencies": len(external_dependencies),
        "index_status": run["index_status"],
    }, ensure_ascii=False))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
