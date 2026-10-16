#!/usr/bin/env python3
"""Replay upstream MM2_HALTING_undec from a pristine, hash-qualified tree."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts/audit/import_coq_undecidability_mm2.py"
IMAGE_ID = "sha256:d4a84f07bbfe0bf3f2dce5b07e7fb43423ff64f990678a114ec6b080d131010b"
SOURCE = Path("/Volumes/D/HoTT-toolchain-cache/coq-undecidability-c486697da8cfa4b9/git-export")
SCRATCH_PARENT = Path("/Volumes/D/HoTT-toolchain-cache/coq-mm2-replay-scratch")
PROBE = ROOT / "HoTT/formal/external-coq-mm2/CheckMM2Undec.v"


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 2


def main() -> int:
    spec = importlib.util.spec_from_file_location("coq_mm2_importer", IMPORTER)
    if spec is None or spec.loader is None:
        return fail("IMPORTER_LOAD_FAILED")
    manager = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(manager)
    try:
        documents, _ = manager.expected_documents()
        for path, expected in documents.items():
            if not path.is_file() or path.is_symlink() or path.read_bytes() != expected:
                return fail(f"PROJECT_SOURCE_QUALIFICATION_MISMATCH:{path}")
    except Exception as exc:  # manager emits the precise qualification reason
        return fail(f"SOURCE_QUALIFICATION_FAILED:{exc}")

    inspect = subprocess.run(
        ["docker", "image", "inspect", IMAGE_ID, "--format", "{{.Id}}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if inspect.returncode != 0 or inspect.stdout.strip() != IMAGE_ID:
        return fail("DOCKER_IMAGE_ID_MISMATCH_OR_MISSING")
    if not SOURCE.is_dir() or SOURCE.is_symlink() or not PROBE.is_file() or PROBE.is_symlink():
        return fail("REPLAY_INPUT_MISSING_OR_SYMLINK")

    SCRATCH_PARENT.mkdir(parents=True, exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="mm2-undec-", dir=SCRATCH_PARENT))
    work = scratch / "source"
    try:
        shutil.copytree(SOURCE, work, copy_function=shutil.copy2)
        shutil.copy2(PROBE, work / "theories/R2CheckMM2Undec.v")
        command = [
            "docker", "run", "--rm", "--platform", "linux/amd64",
            "-v", f"{work}:/work", "-w", "/work/theories", IMAGE_ID,
            "bash", "--login", "-lc",
            "coqc --version && make -j1 MinskyMachines/MM2_undec.vo && "
            "coqc -Q . Undecidability R2CheckMM2Undec.v",
        ]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
        sys.stdout.buffer.write(result.stdout)
        sys.stderr.buffer.write(result.stderr)
        if result.returncode != 0:
            return result.returncode
        required = [
            b"The Coq Proof Assistant, version 8.15.2",
            b"MM2_HALTING_undec",
            b"undecidable MM2_HALTING",
            b"Closed under the global context",
        ]
        if any(marker not in result.stdout for marker in required):
            return fail("REPLAY_OUTPUT_REQUIRED_MARKER_MISSING")
        return 0
    finally:
        shutil.rmtree(scratch, ignore_errors=False)


if __name__ == "__main__":
    raise SystemExit(main())

