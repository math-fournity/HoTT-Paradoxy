#!/usr/bin/env python3
"""Capture the F-011 Boulier--Tabareau replacement-boundary replay."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20260915-MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001-01"
PROOF_ID = "MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001"
CLAIM_IDS = ["C-239", "C-240", "C-241", "C-242", "C-243"]
RUN_REL = Path("HoTT/verification/runs") / RUN_ID
RUN_DIR = ROOT / RUN_REL
PACKAGE = Path("HoTT/formal/external-coq-interval-replacement")
ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/boulier-tabareau-internalcubical-28a2568.tar.gz")


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


def external_file(path: Path, label: str) -> dict[str, object]:
    data = path.read_bytes()
    return {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data); handle.flush(); os.fsync(handle.fileno())


def main() -> int:
    if not (ROOT / ".git").is_dir():
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")
    if RUN_DIR.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")
    toolchain = json.loads((ROOT / PACKAGE / "COQ_IMAGE.json").read_text(encoding="utf-8"))
    source_paths = [
        PACKAGE / "README.md", PACKAGE / "CLAIM-DEGENERATE-REGULAR-FIBRANCY.md",
        PACKAGE / "CheckReplacementBoundary.v", PACKAGE / "COQ_IMAGE.json",
        PACKAGE / "SOURCE_TREE_MANIFEST.json",
        Path("scripts/audit/qualify_coq_interval_replacement.py"),
        Path("scripts/audit/replay_coq_interval_replacement.py"),
        Path("scripts/audit/capture_coq_interval_replacement_run.py"),
        Path("scripts/audit/verify_formal_proof_run.py"),
    ]
    source_rows = [file_row(path) for path in source_paths]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": source_rows,
        "external_dependencies": [external_file(ARCHIVE, "boulier-tabareau-internalcubical-git-archive")],
    }
    source_manifest_data = json_bytes(source_manifest)
    command = ["/usr/bin/env", "python3", "-B", "scripts/audit/replay_coq_interval_replacement.py"]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    environment = "\n".join([
        f"platform={platform.platform()}", f"machine={platform.machine()}", f"python={platform.python_version()}",
        f"coq_image={toolchain['image']['reference']}", f"coq_image_id={toolchain['image']['id']}",
        f"coq_version={toolchain['coq_version']}",
        "upstream=gitlab.inria.fr/sboulier/thesis-formalizations emptyctx@28a256848a134d9111a2f332083b3d3ff35a58d3",
        "replay=Inconsistency.vo plus FibRepl.vo plus assumptions/decomposition probe from a fresh archive extraction",
        "trust_scope=Coq kernel plus explicit Interval Type Theory/QIT/regular-replacement axioms and pinned source/image",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1", "run_id": RUN_ID, "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS, "proof_assistant": "Coq", "proof_assistant_version": toolchain["coq_version"],
        "theory_variant": "Coq 8.13.2 external Interval Type Theory regular/degenerate fibrant replacement replay",
        "command_argv": command, "cwd": str(ROOT),
        "started_at_utc": started.isoformat(), "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(), "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": "Replay the regular-family replacement contradiction, the degenerate QIT replacement, RFib/DFib/transport decomposition and exact assumptions boundary from the cited emptyctx source snapshot.",
        "non_goals": [
            "The source has explicit axioms for interval/cofibrancy/equality, QIT reduction and regular replacement; replay does not discharge them.",
            "InternalCubical-Coq has no license file in the frozen subtree, so source is hash-qualified externally rather than vendored.",
            "Model_structure.v is not part of the accepted target: Coq 8.13.2 fails at a version-sensitive implicit placeholder, while source history targets Coq 8.10.",
            "The run does not prove basic HoTT inconsistent, originality, or a same-task empirical reality bridge.",
        ],
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": len(source_manifest_data), "sha256": sha(source_manifest_data)},
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE", "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    RUN_DIR.mkdir(parents=True, exist_ok=False)
    try:
        exclusive_write(RUN_DIR / "stdout.txt", result.stdout)
        exclusive_write(RUN_DIR / "stderr.txt", result.stderr)
        exclusive_write(RUN_DIR / "environment.txt", environment)
        exclusive_write(RUN_DIR / "source-manifest.json", source_manifest_data)
        exclusive_write(RUN_DIR / "RUN.json", json_bytes(run))
    except BaseException:
        print(f"PARTIAL_RUN_DIRECTORY_RETAINED:{RUN_REL.as_posix()}"); raise
    print(json.dumps({
        "status": run["status"], "run_path": RUN_REL.as_posix(), "exit_code": result.returncode,
        "stdout_bytes": len(result.stdout), "stderr_bytes": len(result.stderr),
        "source_files": len(source_rows), "external_dependencies": 1, "index_status": run["index_status"],
    }, ensure_ascii=False))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
