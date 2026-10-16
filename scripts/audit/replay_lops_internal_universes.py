#!/usr/bin/env python3
"""Replay the complete LOPS 2018 Agda-flat supplement plus modal controls."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "HoTT/formal/external-agda-flat-internal-universes"
UPSTREAM = PACKAGE / "upstream"
CONTROLS = PACKAGE / "controls"
TOOLCHAIN = PACKAGE / "AGDA_FLAT_IMAGE.json"
TMP_PARENT = Path("/Volumes/D/HoTT-toolchain-cache/agda-flat-replay-tmp")


def emit(stream, data: bytes) -> None:
    stream.buffer.write(data)
    stream.flush()


def phase(name: str) -> None:
    print(f"LOPS_REPLAY_PHASE:{name}", flush=True)


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, capture_output=True, check=False)


def main() -> int:
    verify = run([sys.executable, "-B", "scripts/audit/import_lops_internal_universes.py"])
    if verify.returncode != 0 or b'"status": "VALID"' not in verify.stdout:
        emit(sys.stdout, verify.stdout)
        emit(sys.stderr, verify.stderr)
        print("LOPS_IMPORTED_SOURCE_INVALID", file=sys.stderr)
        return 42

    toolchain = json.loads(TOOLCHAIN.read_text(encoding="utf-8"))
    image = toolchain["image"]
    inspect = run(["docker", "image", "inspect", image["tag"], "--format", "{{.Id}} {{.Size}}"])
    expected = f"{image['id']} {image['size_bytes']}\n".encode("utf-8")
    if inspect.returncode != 0 or inspect.stdout != expected:
        emit(sys.stdout, inspect.stdout)
        emit(sys.stderr, inspect.stderr)
        print("LOPS_AGDA_FLAT_IMAGE_MISMATCH", file=sys.stderr)
        return 42

    TMP_PARENT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="lops-", dir=TMP_PARENT) as temp_name:
        work = Path(temp_name) / "work"
        shutil.copytree(UPSTREAM, work)
        shutil.copy2(CONTROLS / "CrispPositive.agda", work / "CrispPositive.agda")
        shutil.copy2(CONTROLS / "CrispNegative.agda", work / "CrispNegative.agda")
        base = [
            "docker", "run", "--rm", "--platform", toolchain["platform"],
            "-v", f"{work}:/work", "-w", "/work", image["tag"],
            "/opt/agda-flat/bin/agda",
        ]

        phase("VERSION")
        version = run(base + ["--version"])
        emit(sys.stdout, version.stdout)
        emit(sys.stderr, version.stderr)
        if version.returncode != 0 or version.stdout.decode("utf-8", "replace").strip() != toolchain["agda_version"]:
            print("LOPS_AGDA_FLAT_VERSION_MISMATCH", file=sys.stderr)
            return 42

        phase("UPSTREAM_FULL_SUITE")
        upstream = run(base + ["--ignore-interfaces", "-i", "/work", "/work/README.agda"])
        emit(sys.stdout, upstream.stdout)
        emit(sys.stderr, upstream.stderr)
        required = (
            b"Finished theorem-3-1.", b"Finished theorem-5-2.",
            b"Finished theorem-5-2-relative.", b"Finished proposition-6-2.",
            b"Finished README.",
        )
        if upstream.returncode != 0 or any(marker not in upstream.stdout for marker in required):
            print("LOPS_UPSTREAM_SUITE_FAILED", file=sys.stderr)
            return 42

        phase("CRISP_POSITIVE")
        positive = run(base + ["--ignore-interfaces", "-i", "/work", "/work/CrispPositive.agda"])
        emit(sys.stdout, positive.stdout)
        emit(sys.stderr, positive.stderr)
        if positive.returncode != 0 or b"Finished CrispPositive." not in positive.stdout:
            print("LOPS_CRISP_POSITIVE_FAILED", file=sys.stderr)
            return 42

        phase("CRISP_NEGATIVE_EXPECTED_REJECTION")
        negative = run(base + ["--ignore-interfaces", "-i", "/work", "/work/CrispNegative.agda"])
        emit(sys.stdout, negative.stdout)
        emit(sys.stderr, negative.stderr)
        diagnostic = b"Variable x is declared top, so it cannot be used here"
        if negative.returncode == 0 or diagnostic not in negative.stdout + negative.stderr:
            print("LOPS_CRISP_NEGATIVE_NOT_REJECTED_AS_EXPECTED", file=sys.stderr)
            return 42
        print(f"LOPS_CRISP_NEGATIVE_EXIT:{negative.returncode}", flush=True)

    phase("COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
