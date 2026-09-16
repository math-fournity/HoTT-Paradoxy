#!/usr/bin/env python3
"""Freshly build and qualify the exact CSL 2023 Coq R3 package."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "HoTT/formal/external-coq-synthetic-incompleteness"
ARCHIVE = PACKAGE / "upstream-cd7d849.tar.gz"
TOOLCHAIN = PACKAGE / "TOOLCHAIN.json"
UPSTREAM_RECEIPT = ROOT / "audit/imports/machine-overview-ce-map-20260915/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/BUILD-RECEIPT.json"
TMP_PARENT = Path("/Volumes/D/HoTT-toolchain-cache/coq-synthetic-incompleteness-main-tmp")
TARGET = Path("theories/FOL/Incompleteness/fol_incompleteness.vo")
STABLE_SUFFIXES = {".vo", ".vos", ".vok", ".glob"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def emit(stream, data: bytes) -> None:
    stream.buffer.write(data)
    stream.flush()


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, capture_output=True, check=False)


def row(path: Path, root: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha(data)}


def manifest_hash(rows: list[dict[str, object]]) -> str:
    payload = b"".join(
        (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
        for value in rows
    )
    return sha(payload)


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
    qualify = run([sys.executable, "-B", "scripts/audit/import_coq_synthetic_incompleteness.py", "validate"])
    emit(sys.stdout, qualify.stdout)
    emit(sys.stderr, qualify.stderr)
    if qualify.returncode != 0 or b'"status": "VALID"' not in qualify.stdout:
        return 42

    toolchain = json.loads(TOOLCHAIN.read_text(encoding="utf-8"))
    upstream = json.loads(UPSTREAM_RECEIPT.read_text(encoding="utf-8"))
    image = toolchain["derived_image"]
    inspect = run(["docker", "image", "inspect", image["reference"], "--format", "{{.Id}} {{.Size}} {{.Architecture}} {{.Os}}"])
    emit(sys.stdout, inspect.stdout)
    emit(sys.stderr, inspect.stderr)
    expected_inspect = f"{image['id']} {image['size_bytes']} {image['architecture']} {image['os']}\n".encode()
    if inspect.returncode != 0 or inspect.stdout != expected_inspect:
        print("COQ_R3_IMAGE_MISMATCH", file=sys.stderr)
        return 42

    TMP_PARENT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="r3-", dir=TMP_PARENT) as temp_name:
        work = Path(temp_name)
        safe_extract(work)
        base = [
            "docker",
            "run",
            "--rm",
            "--platform",
            toolchain["platform"],
            "-v",
            f"{work}:/work",
            "-w",
            "/work",
            image["reference"],
        ]

        print("COQ_R3_REPLAY_PHASE:VERSION", flush=True)
        version = run(base + ["coqc", "--version"])
        emit(sys.stdout, version.stdout)
        emit(sys.stderr, version.stderr)
        if version.returncode != 0 or b"version 8.15.2" not in version.stdout:
            return 42

        print("COQ_R3_REPLAY_PHASE:FRESH_BUILD", flush=True)
        build = run(base + ["bash", "-lc", "make FOL/Incompleteness/fol_incompleteness.vo"])
        emit(sys.stdout, build.stdout)
        emit(sys.stderr, build.stderr)
        expected_build = upstream["build"]["first"]
        if (
            build.returncode != 0
            or len(build.stdout) != expected_build["stdout"]["bytes"]
            or sha(build.stdout) != expected_build["stdout"]["sha256"]
            or len(build.stderr) != expected_build["stderr"]["bytes"]
            or sha(build.stderr) != expected_build["stderr"]["sha256"]
        ):
            print("COQ_R3_FRESH_BUILD_OUTPUT_MISMATCH", file=sys.stderr)
            return 42
        target = work / TARGET
        if not target.is_file():
            print("COQ_R3_TARGET_MISSING", file=sys.stderr)
            return 42
        target_data = target.read_bytes()
        if len(target_data) != expected_build["target"]["bytes"] or sha(target_data) != expected_build["target"]["sha256"]:
            print("COQ_R3_TARGET_HASH_MISMATCH", file=sys.stderr)
            return 42
        stable = [row(path, work) for path in sorted(path for path in work.rglob("*") if path.is_file() and path.suffix in STABLE_SUFFIXES)]
        expected_stable = expected_build["stable_artifacts"]
        if (
            len(stable) != expected_stable["count"]
            or sum(value["bytes"] for value in stable) != expected_stable["bytes"]
            or manifest_hash(stable) != expected_stable["manifest_sha256"]
        ):
            print("COQ_R3_STABLE_ARTIFACT_MISMATCH", file=sys.stderr)
            return 42
        print(f"COQ_R3_TARGET_SHA256:{sha(target_data)}", flush=True)
        print(f"COQ_R3_STABLE_ARTIFACTS:{len(stable)}:{manifest_hash(stable)}", flush=True)

        shutil.copy2(PACKAGE / "Qualification.v", work / "theories/Qualification.v")
        qualification_base = [
            "docker",
            "run",
            "--rm",
            "--platform",
            toolchain["platform"],
            "-v",
            f"{work}:/work",
            "-w",
            "/work/theories",
            image["reference"],
            "coqc",
            "-Q",
            ".",
            "Undecidability",
            "Qualification.v",
        ]
        print("COQ_R3_REPLAY_PHASE:QUALIFICATION_FIRST", flush=True)
        first = run(qualification_base)
        emit(sys.stdout, first.stdout)
        emit(sys.stderr, first.stderr)
        print("COQ_R3_REPLAY_PHASE:QUALIFICATION_REPLAY", flush=True)
        second = run(qualification_base)
        if first.returncode != 0 or second.returncode != 0 or first.stdout != second.stdout or first.stderr != second.stderr:
            emit(sys.stdout, second.stdout)
            emit(sys.stderr, second.stderr)
            print("COQ_R3_QUALIFICATION_REPLAY_MISMATCH", file=sys.stderr)
            return 42
        required = (
            b"self_halting_diverge",
            b"recursively_separating_diverge",
            b"insep_essential_incompleteness",
            b"epf_mu_ctq",
            b"Q_incomplete",
            b"is_universal theta",
            b"strongly_separates",
            b"CTQ ->",
            b"Definitions.enumerable T",
            b"~ Theories.tprv T Core.falsity",
        )
        if any(marker not in first.stdout for marker in required) or first.stdout.count(b"Closed under the global context") != 3 or first.stderr:
            print("COQ_R3_QUALIFICATION_CONTENT_MISMATCH", file=sys.stderr)
            return 42
        expected_qualification = upstream["qualification_probe"]
        if len(first.stdout) != expected_qualification["stdout_bytes"] or sha(first.stdout) != expected_qualification["stdout_sha256"]:
            print("COQ_R3_QUALIFICATION_PRIOR_REPLAY_MISMATCH", file=sys.stderr)
            return 42
        print(f"COQ_R3_QUALIFICATION_SHA256:{sha(first.stdout)}", flush=True)

    print("COQ_R3_REPLAY_PHASE:COMPLETE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
