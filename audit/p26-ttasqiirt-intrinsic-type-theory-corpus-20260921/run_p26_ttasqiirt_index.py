#!/usr/bin/env python3
"""Capture default and --safe checks of the fixed external TTasQIIRT index."""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "runs" / "20260921-P26-TTASQIIRT-INDEX-01"
EXTERNAL = Path("/tmp/ttasqiirt-p26-8db08306")
AGDA = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda")
FILES = [
    "README.md",
    "src/index.agda",
    "src/Theory/SC/QIIRT-tyOf/Syntax.agda",
    "src/Theory/SC/QIIRT-tyOf/Rec.agda",
    "src/Theory/SC/QIIRT-tyOf/Model/Set.agda",
    "src/Theory/SC/QIIRT-tyOf/IxModel/NbE.agda",
    "src/Theory/SC+Pi+B/QIIRT-tyOf/Syntax.agda",
    "src/Theory/SC+Pi+B/QIIRT-tyOf/Model/Set.agda",
    "src/Theory/SC+Pi+B/QIIRT-tyOf/IxModel/Canonicity.agda",
    "src/Theory/SC/QIIRT-tyOf/IxModel/LogPred.agda",
    "src/Theory/SC/QIIRT-tyOf/IxModel/StrictLogPred.agda",
    "src/Cubical/Reflection/StrictEquiv.agda",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(label: str, argv: list[str]) -> dict:
    started = time.monotonic()
    completed = subprocess.run(argv, cwd=EXTERNAL / "src", text=True, capture_output=True, check=False)
    duration = time.monotonic() - started
    stdout = OUT / f"{label}-stdout.txt"
    stderr = OUT / f"{label}-stderr.txt"
    stdout.write_text(completed.stdout, encoding="utf-8")
    stderr.write_text(completed.stderr, encoding="utf-8")
    return {
        "argv": argv,
        "exit_code": completed.returncode,
        "duration_seconds": duration,
        "stdout": {"path": stdout.name, "sha256": sha256(stdout), "bytes": stdout.stat().st_size},
        "stderr": {"path": stderr.name, "sha256": sha256(stderr), "bytes": stderr.stat().st_size},
    }


def main() -> None:
    assert (EXTERNAL / ".git").exists() and AGDA.is_file()
    check = subprocess.run(["git", "-C", str(EXTERNAL), "rev-parse", "HEAD"], text=True, capture_output=True, check=True).stdout.strip()
    if check != "8db08306287333067b2749f95f8ad3ba7a0e14d1":
        raise RuntimeError(f"wrong checkout: {check}")
    if OUT.exists():
        raise RuntimeError(f"run directory already exists: {OUT}")
    OUT.mkdir(parents=True)
    version = subprocess.run([str(AGDA), "--version"], text=True, capture_output=True, check=True).stdout
    default = run("default-ignore-interfaces", [str(AGDA), "--ignore-interfaces", "index.agda"])
    safe = run("safe-ignore-interfaces", [str(AGDA), "--safe", "--ignore-interfaces", "index.agda"])
    manifest = {path: sha256(EXTERNAL / path) for path in FILES}
    source_manifest = OUT / "source-manifest.json"
    source_manifest.write_text(json.dumps({"external_commit": check, "files": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    environment = OUT / "environment.txt"
    environment.write_text(f"agda={version}external={EXTERNAL}\ncommit={check}\n", encoding="utf-8")
    result = {
        "schema_version": "p26-external-agda-index-run/v1",
        "run_id": "20260921-P26-TTASQIIRT-INDEX-01",
        "external_commit": check,
        "workdir": "src",
        "toolchain": version.strip(),
        "default_ignore_interfaces": default,
        "safe_ignore_interfaces": safe,
        "source_manifest": {"path": source_manifest.name, "sha256": sha256(source_manifest)},
        "environment": {"path": environment.name, "sha256": sha256(environment)},
        "status": "DEFAULT_ENTRYPOINT_ACCEPTED_SAFE_CONFIGURATION_REJECTED_WITH_SCOPE" if default["exit_code"] == 0 and safe["exit_code"] == 42 else "UNEXPECTED_RUN_RESULT",
        "scope": "External-source entrypoint execution only. The default run does not establish --safe qualification, no-glue/univalence-free execution, all source completeness, or a HoTT theorem.",
    }
    (OUT / "RUN.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "DEFAULT_ENTRYPOINT_ACCEPTED_SAFE_CONFIGURATION_REJECTED_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
