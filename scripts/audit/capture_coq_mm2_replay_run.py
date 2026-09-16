#!/usr/bin/env python3
"""Capture an immutable F-011 run for the external Coq MM2 theorem replay."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01"
PROOF_ID = "MP-COQ-MM2-UNDECIDABILITY-REPLAY-001"
CLAIM_IDS = ["C-208"]
RUN_REL = Path("HoTT/verification/runs") / RUN_ID
RUN_DIR = ROOT / RUN_REL
FORMAL_ROOT = Path("HoTT/formal/external-coq-mm2")
EXTERNAL_CACHE = Path("/Volumes/D/HoTT-toolchain-cache/coq-undecidability-c486697da8cfa4b9")


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


def absolute_file_row(path: Path, label: str) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"EXTERNAL_FILE_INVALID:{label}")
    data = path.read_bytes()
    return {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}


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
    tree_manifest = json.loads((ROOT / FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json").read_text(encoding="utf-8"))
    selected = [Path(row["path"]) for row in replay_source["selected_project_files"]]
    source_paths = [
        FORMAL_ROOT / "README.md",
        FORMAL_ROOT / "REPLAY_SOURCE.json",
        FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json",
        FORMAL_ROOT / "DOCKER_IMAGE.json",
        FORMAL_ROOT / "CheckMM2Undec.v",
        *selected,
        Path("scripts/audit/import_coq_undecidability_mm2.py"),
        Path("scripts/audit/replay_coq_mm2_undec.py"),
        Path("scripts/audit/capture_coq_mm2_replay_run.py"),
        Path("scripts/audit/verify_formal_proof_run.py"),
    ]
    deduped: list[Path] = []
    for path in source_paths:
        if path not in deduped:
            deduped.append(path)
    source_rows = [file_row(path) for path in deduped]

    archive = absolute_file_row(EXTERNAL_CACHE / "source.tar.gz", "coq-undecidability-codeload-archive")
    expected_archive = replay_source["upstream_identity"]["archive"]
    if archive["bytes"] != expected_archive["bytes"] or archive["sha256"] != expected_archive["sha256"]:
        raise SystemExit("EXTERNAL_ARCHIVE_MISMATCH")
    tree = {
        "label": "coq-undecidability-extracted-tree",
        "local_path": str(EXTERNAL_CACHE / "git-export"),
        "file_count": tree_manifest["file_count"],
        "total_bytes": tree_manifest["total_bytes"],
        "tree_sha256": tree_manifest["tree_sha256"],
        "upstream_commit": replay_source["upstream_identity"]["commit"],
        "git_tree": replay_source["upstream_identity"]["git_tree"],
    }
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": source_rows,
        "external_dependencies": [archive, tree],
    }
    source_manifest_data = json_bytes(source_manifest)
    command = ["/usr/bin/env", "python3", "-B", "scripts/audit/replay_coq_mm2_undec.py"]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        "docker_client_server=29.4.0/29.4.0",
        "docker_image_id=sha256:d4a84f07bbfe0bf3f2dce5b07e7fb43423ff64f990678a114ec6b080d131010b",
        "docker_platform=linux/amd64",
        "coq_version=8.15.2",
        "ocaml_version=4.07.1",
        "upstream_branch=coq-8.15",
        "upstream_commit=c486697da8cfa4b9bb11b4c53eea7d57781c0deb",
        "upstream_git_tree=6469b73eb0e8cd73d8ecd0cac5711a07912c54d2",
        "replay_target=Undecidability.MinskyMachines.MM2_undec.MM2_HALTING_undec",
        "trust_scope=Coq kernel plus pinned Docker image and full upstream source tree",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "proof_assistant": "Coq",
        "proof_assistant_version": "The Coq Proof Assistant, version 8.15.2; compiled with OCaml 4.07.1",
        "theory_variant": "Coq 8.15.2 Calculus of Inductive Constructions; external library theorem replay",
        "command_argv": command,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": "Replay upstream coq-library-undecidability@c486697 MM2_HALTING_undec and print its assumptions: under the library definition, decidability of MM2_HALTING implies enumerability of complement SBTM_HALT (C-208).",
        "non_goals": [
            "The upstream theorem is not an unconditional proof of not-decidable in pure constructive type theory; undecidable is the library's synthetic implication.",
            "This run does not yet prove the compiler bridge from upstream MM2 to the project's Cubical Agda ProgramCode.",
            "It does not establish exact HoTT incompleteness, HoTT essentiality, a natural consumer, a reality bridge or a contradiction in HoTT.",
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
        "external_dependencies": 2,
        "index_status": run["index_status"],
    }, ensure_ascii=False))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
