#!/usr/bin/env python3
"""Replay the CSL 2026 groupoid-syntax source and project theorem probe."""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts/audit/import_cubical_groupoid_syntax.py"
FORMAL = ROOT / "HoTT/formal/external-cubical-groupoid-syntax"
TOOLCHAIN = ROOT / "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
SOURCE = Path("/Volumes/D/HoTT-literature-cache/groupoid-syntax-cohtt-5babc385/git-export")
WORK = Path("/Volumes/D/HoTT-literature-cache/groupoid-syntax-cohtt-5babc385/replay-work")


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 2


def load_manager():
    spec = importlib.util.spec_from_file_location("cubical_groupoid_syntax_importer", IMPORTER)
    if spec is None or spec.loader is None:
        raise RuntimeError("IMPORTER_LOAD_FAILED")
    manager = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(manager)
    return manager


def emit_phase(name: str, result: subprocess.CompletedProcess[bytes]) -> None:
    sys.stdout.buffer.write(f"===== {name} STDOUT =====\n".encode("utf-8"))
    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(f"===== {name} STDERR =====\n".encode("utf-8"))
    sys.stderr.buffer.write(result.stderr)


def main() -> int:
    try:
        manager = load_manager()
        for path, expected in manager.expected_documents().items():
            if not path.is_file() or path.is_symlink() or path.read_bytes() != expected:
                return fail(f"PROJECT_SOURCE_QUALIFICATION_MISMATCH:{path}")
        toolchain = json.loads(TOOLCHAIN.read_text(encoding="utf-8"))
        agda = Path(toolchain["agda"]["local_binary"])
        cubical = Path(toolchain["cubical_library"]["local_root"])
        if not agda.is_file() or agda.is_symlink() or not cubical.is_dir() or cubical.is_symlink():
            return fail("PINNED_AGDA_OR_CUBICAL_TREE_MISSING")
        if WORK.exists():
            return fail("REPLAY_WORK_DIRECTORY_ALREADY_EXISTS")
        WORK.mkdir(parents=True, exist_ok=False)
        source_copy = WORK / "cohtt"
        cubical_copy = WORK / "cubical"
        try:
            shutil.copytree(SOURCE, source_copy, ignore=shutil.ignore_patterns("*.agdai"))
            shutil.copytree(cubical, cubical_copy, ignore=shutil.ignore_patterns("*.agdai", ".DS_Store"))
            shutil.copy2(FORMAL / "CheckGroupoidSyntax.agda", source_copy / "CheckGroupoidSyntax.agda")

            env = os.environ.copy()
            env.update({
                "XDG_DATA_HOME": toolchain["runtime_cache"]["xdg_data_home"],
                "XDG_CONFIG_HOME": toolchain["runtime_cache"]["xdg_config_home"],
                "TMPDIR": toolchain["runtime_cache"]["tmpdir"],
            })
            version = subprocess.run([str(agda), "--version"], cwd=ROOT, env=env, capture_output=True, check=False)
            emit_phase("AGDA_VERSION", version)
            if version.returncode != 0:
                return version.returncode

            phase1 = subprocess.run([
                str(agda),
                "-i", str(source_copy),
                "-i", str(cubical_copy),
                "--safe", "--cubical", "--guardedness",
                "-WnoUnsupportedIndexedMatch",
                "--ignore-interfaces",
                str(source_copy / "TT/README.agda"),
            ], cwd=ROOT, env=env, capture_output=True, check=False)
            emit_phase("PHASE1_FRESH_SOURCE_BASELINE", phase1)
            if phase1.returncode != 0:
                return phase1.returncode

            for interface in source_copy.rglob("*.agdai"):
                interface.unlink()
            upstream_lib = source_copy / "cohtt.agda-lib"
            upstream_lib.rename(source_copy / "cohtt.agda-lib.upstream")
            shutil.copy2(FORMAL / "cohtt-replay.agda-lib", source_copy / "cohtt-replay.agda-lib")
            libraries = WORK / "libraries"
            libraries.write_text(
                f"{source_copy / 'cohtt-replay.agda-lib'}\n{cubical_copy / 'cubical.agda-lib'}\n",
                encoding="utf-8",
            )

            phase2 = subprocess.run([
                str(agda),
                f"--library-file={libraries}",
                "-l", "cohtt-replay",
                str(source_copy / "TT/README.agda"),
            ], cwd=ROOT, env=env, capture_output=True, check=False)
            emit_phase("PHASE2_UPSTREAM_FLAGS_ALL_TT_MODULES", phase2)
            if phase2.returncode != 0:
                return phase2.returncode

            probe = subprocess.run([
                str(agda),
                f"--library-file={libraries}",
                "-l", "cohtt-replay",
                str(source_copy / "CheckGroupoidSyntax.agda"),
            ], cwd=ROOT, env=env, capture_output=True, check=False)
            emit_phase("PHASE3_PROJECT_THEOREM_PROBE", probe)
            if probe.returncode != 0:
                return probe.returncode

            combined = version.stdout + phase1.stdout + phase2.stdout + probe.stdout
            required = [
                b"Agda version 2.8.0",
                b"Checking TT.Groupoid.Syntax",
                b"Checking TT.Groupoid.NTy",
                b"Checking TT.Groupoid.IsoSet",
                b"Checking TT.Groupoid.CwF",
                b"Checking CheckGroupoidSyntax",
            ]
            if any(marker not in combined for marker in required):
                return fail("REPLAY_OUTPUT_REQUIRED_MARKER_MISSING")
            return 0
        finally:
            shutil.rmtree(WORK, ignore_errors=False)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        return fail(f"REPLAY_SETUP_FAILED:{exc}")


if __name__ == "__main__":
    raise SystemExit(main())
