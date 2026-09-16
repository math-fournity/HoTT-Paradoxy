#!/usr/bin/env python3
"""Capture the F-011 run for conditional internal no-decider theorems."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01"
PROOF_ID = "MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001"
CLAIM_IDS = ["C-219", "C-220", "C-221", "C-222"]
RUN_REL = Path("HoTT/verification/runs") / RUN_ID
RUN_DIR = ROOT / RUN_REL
FORMAL_ROOT = Path("HoTT/formal/external-coq-parametric-ct")
EXTERNAL_CACHE = Path("/Volumes/D/HoTT-literature-cache/parametric-ct-b9523cb")


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
    source_paths = [
        FORMAL_ROOT / "README.md",
        FORMAL_ROOT / "CLAIM-R2-INTERNAL-UNDEC.md",
        FORMAL_ROOT / "CheckInternalUndec.v",
        FORMAL_ROOT / "Dockerfile",
        FORMAL_ROOT / "DOCKER_IMAGE.json",
        FORMAL_ROOT / "REPLAY_SOURCE.json",
        FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json",
        FORMAL_ROOT / "TARGET_CLOSURE.json",
        Path("scripts/audit/import_coq_parametric_ct.py"),
        Path("scripts/audit/replay_coq_parametric_ct_internal_undec.py"),
        Path("scripts/audit/capture_coq_parametric_ct_internal_undec_run.py"),
        Path("scripts/audit/verify_formal_proof_run.py"),
    ]
    source_rows = [file_row(path) for path in source_paths]

    archive = absolute_file_row(EXTERNAL_CACHE / "source.tar.gz", "coq-parametric-ct-codeload-archive")
    expected_archive = replay_source["archive"]
    if archive["bytes"] != expected_archive["bytes"] or archive["sha256"] != expected_archive["sha256"]:
        raise SystemExit("EXTERNAL_ARCHIVE_MISMATCH")
    tree = {
        "label": "coq-parametric-ct-extracted-tree",
        "local_path": str(EXTERNAL_CACHE / "git-export"),
        "file_count": tree_manifest["file_count"],
        "total_bytes": tree_manifest["total_bytes"],
        "tree_sha256": tree_manifest["tree_sha256"],
        "upstream_commit": replay_source["commit"],
        "git_tree": replay_source["git_tree"],
    }
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": source_rows,
        "external_dependencies": [archive, tree],
    }
    source_manifest_data = json_bytes(source_manifest)
    command = [
        "/usr/bin/env", "python3", "-B",
        "scripts/audit/replay_coq_parametric_ct_internal_undec.py",
    ]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        "docker_platform=linux/amd64",
        "docker_image_id=sha256:7e35dbfedcb7281c00420071437fce8316345ab006b1699cd0926f525a669df8",
        "docker_base=coqorg/coq:8.13.2@sha256:1f69b9224f068d408e6be7a3f536f67395d00c3497b97bdb99ee2d2c4c91954c",
        "coq_version=8.13.2",
        "ocaml_version=4.07.1",
        "coq_equations=1.2.3+8.13",
        "coq_stdpp=1.5.0",
        "upstream_branch=code",
        "upstream_commit=b9523cb33180dc58b227432e60045cc38615b711",
        "upstream_git_tree=9cfc31a04f31e0a73cd9494a8d745a39ee639082",
        "target=Axioms/halting.vo plus CheckInternalUndec.v",
        "trust_scope=Coq kernel plus pinned Docker image and hash-qualified upstream source tree",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "proof_assistant": "Coq",
        "proof_assistant_version": "The Coq Proof Assistant, version 8.13.2; compiled with OCaml 4.07.1",
        "theory_variant": "Coq 8.13.2 Calculus of Inductive Constructions; external Parametric CT theorem replay",
        "command_argv": command,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": "Replay EPF_SCT_halting, K_nat_bool_undec and K_nat_undec from coq-synthetic-computability@b9523cb. The conclusions are internal negations under the explicit sum premise EPF_bool + SCT; Print Assumptions must report Closed under the global context for all three.",
        "non_goals": [
            "This run does not prove EPF_bool or SCT in ambient HoTT; they remain explicit premises.",
            "It does not establish an unconditional no-decider theorem for the project's ProgramCode or any exact HoTT calculus.",
            "It does not use univalence, Path, HIT or modality and therefore does not establish HoTT essentiality.",
            "It does not establish a natural consumer, a same-task reality bridge, Goedel incompleteness or a contradiction in HoTT.",
            "The pinned upstream tree contains no license file; no redistribution permission is inferred.",
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
