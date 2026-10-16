#!/usr/bin/env python3
"""Replay the Boulier--Tabareau regular/degenerate replacement boundary."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "HoTT/formal/external-coq-interval-replacement"
ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/boulier-tabareau-internalcubical-28a2568.tar.gz")
TOOLCHAIN = PACKAGE / "COQ_IMAGE.json"
TMP_PARENT = Path("/Volumes/D/HoTT-toolchain-cache/coq-interval-replacement-tmp")


def emit(stream, data: bytes) -> None:
    stream.buffer.write(data); stream.flush()


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, capture_output=True, check=False)


def safe_extract(destination: Path) -> None:
    with tarfile.open(ARCHIVE, "r:gz") as archive:
        for member in archive.getmembers():
            target = destination / member.name
            try:
                target.resolve().relative_to(destination.resolve())
            except ValueError as exc:
                raise RuntimeError(f"ARCHIVE_PATH_ESCAPE:{member.name}") from exc
        archive.extractall(destination, filter="data")


def main() -> int:
    qualification = run([sys.executable, "-B", "scripts/audit/qualify_coq_interval_replacement.py"])
    if qualification.returncode != 0 or b'"status": "VALID"' not in qualification.stdout:
        emit(sys.stdout, qualification.stdout); emit(sys.stderr, qualification.stderr)
        return 42
    toolchain = json.loads(TOOLCHAIN.read_text(encoding="utf-8"))
    image = toolchain["image"]
    inspect = run(["docker", "image", "inspect", image["reference"], "--format", "{{.Id}} {{.Size}}"])
    if inspect.returncode != 0 or inspect.stdout != f"{image['id']} {image['size_bytes']}\n".encode():
        emit(sys.stdout, inspect.stdout); emit(sys.stderr, inspect.stderr)
        print("COQ_INTERVAL_IMAGE_MISMATCH", file=sys.stderr)
        return 42

    TMP_PARENT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="bt-", dir=TMP_PARENT) as temp_name:
        temp = Path(temp_name)
        safe_extract(temp)
        work = temp / "InternalCubical-Coq"
        shutil.copy2(PACKAGE / "CheckReplacementBoundary.v", work / "CheckReplacementBoundary.v")
        base = [
            "docker", "run", "--rm", "--platform", toolchain["platform"],
            "-v", f"{work}:/work", "-w", "/work", image["reference"],
        ]

        print("COQ_INTERVAL_REPLAY_PHASE:VERSION", flush=True)
        version = run(base + ["coqc", "--version"])
        emit(sys.stdout, version.stdout); emit(sys.stderr, version.stderr)
        if version.returncode != 0 or b"version 8.13.2" not in version.stdout:
            return 42

        print("COQ_INTERVAL_REPLAY_PHASE:NEGATIVE_AND_POSITIVE_TARGETS", flush=True)
        build = run(base + ["bash", "-lc", "coq_makefile -f _CoqProject -o Makefile.generated && make -f Makefile.generated -j1 Inconsistency.vo FibRepl.vo && coqc -R . Internal CheckReplacementBoundary.v"])
        emit(sys.stdout, build.stdout); emit(sys.stderr, build.stderr)
        required = (
            b"COQC Inconsistency.v", b"COQC FibRepl.v", b"Fib_repl",
            b"repl_ind'", b"TransFib_HFib", b"extension_rule__emptyctx",
            b"RFib_repl", b"repl_rec'",
        )
        if build.returncode != 0 or any(marker not in build.stdout + build.stderr for marker in required):
            print("COQ_INTERVAL_TARGET_REPLAY_FAILED", file=sys.stderr)
            return 42

    print("COQ_INTERVAL_REPLAY_PHASE:COMPLETE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
