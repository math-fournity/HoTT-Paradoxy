#!/usr/bin/env python3
"""Replay the Parametric CT internal no-decider theorems in a clean tree."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts/audit/import_coq_parametric_ct.py"
FORMAL = ROOT / "HoTT/formal/external-coq-parametric-ct"
SOURCE = Path("/Volumes/D/HoTT-literature-cache/parametric-ct-b9523cb/git-export")
SCRATCH_PARENT = Path("/Volumes/D/HoTT-literature-cache/parametric-ct-b9523cb/replay-scratch")
IMAGE_ID = "sha256:7e35dbfedcb7281c00420071437fce8316345ab006b1699cd0926f525a669df8"


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 2


def load_manager():
    spec = importlib.util.spec_from_file_location("coq_parametric_ct_importer", IMPORTER)
    if spec is None or spec.loader is None:
        raise RuntimeError("IMPORTER_LOAD_FAILED")
    manager = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(manager)
    return manager


def main() -> int:
    try:
        manager = load_manager()
        for path, expected in manager.expected_documents().items():
            if not path.is_file() or path.is_symlink() or path.read_bytes() != expected:
                return fail(f"PROJECT_SOURCE_QUALIFICATION_MISMATCH:{path}")
        image = json.loads((FORMAL / "DOCKER_IMAGE.json").read_text(encoding="utf-8"))
        if image.get("image_id") != IMAGE_ID:
            return fail("PROJECT_DOCKER_IMAGE_ID_MISMATCH")
        inspect = subprocess.run(
            ["docker", "image", "inspect", IMAGE_ID, "--format", "{{.Id}}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if inspect.returncode != 0 or inspect.stdout.strip() != IMAGE_ID:
            return fail("DOCKER_IMAGE_ID_MISMATCH_OR_MISSING")
        if not SOURCE.is_dir() or SOURCE.is_symlink():
            return fail("QUALIFIED_SOURCE_TREE_MISSING_OR_SYMLINK")
        probe = FORMAL / "CheckInternalUndec.v"
        if not probe.is_file() or probe.is_symlink():
            return fail("PROJECT_PROBE_MISSING_OR_SYMLINK")

        SCRATCH_PARENT.mkdir(parents=True, exist_ok=True)
        scratch = Path(tempfile.mkdtemp(prefix="internal-undec-", dir=SCRATCH_PARENT))
        work = scratch / "source"
        work.mkdir()
        try:
            for relative in manager.TARGET_SOURCE_FILES:
                src = SOURCE / relative
                dst = work / relative
                if not src.is_file() or src.is_symlink():
                    return fail(f"TARGET_SOURCE_MISSING_OR_SYMLINK:{relative}")
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            shutil.copy2(probe, work / "CheckInternalUndec.v")
            project = "-Q . Undecidability\n" + "\n".join([
                *manager.TARGET_SOURCE_FILES,
                "CheckInternalUndec.v",
            ]) + "\n"
            (work / "_CoqProject").write_text(project, encoding="utf-8")
            command = [
                "docker", "run", "--rm", "--platform", "linux/amd64",
                "-v", f"{work}:/work", "-w", "/work", IMAGE_ID,
                "bash", "--login", "-lc",
                "coqc --version && "
                "coq_makefile -f _CoqProject -o Makefile.coq && "
                "make --no-print-directory -f Makefile.coq -j1 Axioms/halting.vo && "
                "coqc -Q . Undecidability CheckInternalUndec.v",
            ]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
            sys.stdout.buffer.write(result.stdout)
            sys.stderr.buffer.write(result.stderr)
            if result.returncode != 0:
                return result.returncode
            required = [
                b"The Coq Proof Assistant, version 8.13.2",
                b"EPF_SCT_halting",
                b"K_nat_bool_undec",
                b"K_nat_undec",
                b"bestaxioms.EPF_bool + bestaxioms.SCT",
                b"~ Definitions.decidable",
            ]
            if any(marker not in result.stdout for marker in required):
                return fail("REPLAY_OUTPUT_REQUIRED_MARKER_MISSING")
            if result.stdout.count(b"Closed under the global context") != 3:
                return fail("REPLAY_ASSUMPTION_CLOSURE_COUNT_MISMATCH")
            return 0
        finally:
            shutil.rmtree(scratch, ignore_errors=False)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        return fail(f"REPLAY_SETUP_FAILED:{exc}")


if __name__ == "__main__":
    raise SystemExit(main())
