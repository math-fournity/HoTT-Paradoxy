#!/usr/bin/env python3
"""Capture the F-011 replay of the LOPS 2018 no-go/crisp dual package."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20260915-MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001-01"
PROOF_ID = "MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001"
CLAIM_IDS = ["C-233", "C-234", "C-235", "C-236", "C-237", "C-238"]
RUN_REL = Path("HoTT/verification/runs") / RUN_ID
RUN_DIR = ROOT / RUN_REL
PACKAGE = Path("HoTT/formal/external-agda-flat-internal-universes")
ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/lops-internal-universes-2018/internal-universes.zip")
AGDA_SOURCE_ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/agda-flat-70899fb-source.tar.gz")
CABAL_ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/agda-flat-70899fb/cabal-install-2.4.1.0-x86_64-unknown-linux.tar.xz")


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
    toolchain = json.loads((ROOT / PACKAGE / "AGDA_FLAT_IMAGE.json").read_text(encoding="utf-8"))
    source_paths = [
        PACKAGE / "README.md",
        PACKAGE / "CLAIM-INTERNAL-UNIVERSE-CRISP.md",
        PACKAGE / "SOURCE_TREE_MANIFEST.json",
        PACKAGE / "AGDA_FLAT_IMAGE.json",
        PACKAGE / "Dockerfile.agda-flat",
        PACKAGE / "cabal.config.replay",
        PACKAGE / "controls/CrispPositive.agda",
        PACKAGE / "controls/CrispNegative.agda",
        Path("scripts/audit/import_lops_internal_universes.py"),
        Path("scripts/audit/replay_lops_internal_universes.py"),
        Path("scripts/audit/capture_lops_internal_universes_run.py"),
        Path("scripts/audit/verify_formal_proof_run.py"),
    ]
    source_paths.extend(sorted((ROOT / PACKAGE / "upstream").rglob("*.agda")))
    normalized: list[Path] = []
    for path in source_paths:
        normalized.append(path.relative_to(ROOT) if path.is_absolute() else path)
    source_rows = [file_row(path) for path in normalized]
    external_dependencies = [
        external_file(ARCHIVE, "lops-cambridge-official-source-zip"),
        external_file(AGDA_SOURCE_ARCHIVE, "agda-flat-git-archive"),
        external_file(CABAL_ARCHIVE, "cabal-install-static-archive"),
    ]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": source_rows,
        "external_dependencies": external_dependencies,
    }
    source_manifest_data = json_bytes(source_manifest)
    command = ["/usr/bin/env", "python3", "-B", "scripts/audit/replay_lops_internal_universes.py"]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"agda_flat_version={toolchain['agda_version']}",
        f"agda_flat_image_id={toolchain['image']['id']}",
        f"agda_flat_source_commit={toolchain['agda_flat_source']['commit']}",
        f"agda_flat_source_git_tree={toolchain['agda_flat_source']['git_tree']}",
        "upstream=Licata-Orton-Pitts-Spitters FSCD 2018 Cambridge dataset DOI 10.17863/CAM.22369",
        "replay=complete official README.agda plus crisp-positive and expected crisp-local-negative controls",
        "trust_scope=Agda-flat kernel plus explicit source postulates, pinned Docker image/source/archive and modal type checker",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "proof_assistant": "Agda-flat",
        "proof_assistant_version": toolchain["agda_version"],
        "theory_variant": "Agda-flat 2.6.0.1 modal crisp type theory; external source replay",
        "command_argv": command,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": "Replay the complete official LOPS 2018 Agda supplement: ordinary internal weak fibration classifiers imply interval collapse; crisp/tiny-interval assumptions construct a classifier; modal controls accept crisp and reject local arguments.",
        "non_goals": [
            "The source explicitly postulates funext, UIP, a nontrivial interval, cofibrancy and the tiny-path-functor adjunction; replay does not prove these assumptions in every HoTT model.",
            "The positive theorem is in crisp modal type theory and deliberately restricts substitution; it is not the ordinary internal classifier rejected by Theorem 3.1.",
            "This is a published theorem/source replay, not a novelty claim or proof that basic HoTT is inconsistent.",
            "The run does not establish an empirical same-task reality bridge or that every natural consumer rejects the crisp payment.",
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
        "status": run["status"], "run_path": RUN_REL.as_posix(), "exit_code": result.returncode,
        "stdout_bytes": len(result.stdout), "stderr_bytes": len(result.stderr),
        "source_files": len(source_rows), "external_dependencies": len(external_dependencies),
        "index_status": run["index_status"],
    }, ensure_ascii=False))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
