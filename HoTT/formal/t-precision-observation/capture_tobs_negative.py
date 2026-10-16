#!/usr/bin/env python3
"""Capture the expected rejected coarse-decoder control for T-OBS-001."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261004-MP-T-PRECISION-TOBS-NEG-001-01"
SOURCE = Path("HoTT/formal/t-precision-observation/WrongObservationPrecision.lean")
TOOLCHAIN = Path("HoTT/formal/t-precision-observation/LEAN_CORE_TOOLCHAIN.json")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith("20261004-MP-T-PRECISION-TOBS-NEG-001-"):
        raise SystemExit("RUN_ID_INVALID")
    spec = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    lean = Path(spec["lean"]["root"]) / "bin" / "lean"
    inputs = [ROOT / SOURCE, ROOT / TOOLCHAIN, ROOT / Path(__file__).relative_to(ROOT)]
    if any(not path.is_file() for path in inputs) or not lean.is_file() or lean.is_symlink():
        raise SystemExit("REQUIRED_INPUT_MISSING")
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    argv = [str(lean), SOURCE.as_posix()]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    diagnostic = result.stdout + result.stderr
    rejected = result.returncode != 0 and b"False" in diagnostic and b"True" in diagnostic
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": "MP-T-PRECISION-TOBS-NEG-001",
        "run_id": RUN_ID,
        "files": [row(path) for path in inputs],
        "external_dependencies": [
            {"label": "lean-core-binary", "local_path": str(lean), "bytes": lean.stat().st_size, "sha256": sha(lean.read_bytes())},
        ],
        "policy": "Expected negative control: a one-value coarse observation cannot manufacture a decoder for an opposite-valued predicate.",
    }
    environment = f"platform={platform.platform()}\nlean={version}\nexpected=coarse decoder rejection\n".encode()
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": "MP-T-PRECISION-TOBS-NEG-001",
        "claim_ids": ["C-367"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": spec["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "EXPECTED_REJECTION_CONFIRMED" if rejected else "EXPECTED_REJECTION_NOT_CONFIRMED",
        "scope": "Negative control only; it verifies that the concrete false-to-true decoder is rejected.",
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": 0, "sha256": ""},
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    write_new(run / "stdout.txt", result.stdout)
    write_new(run / "stderr.txt", result.stderr)
    write_new(run / "environment.txt", environment)
    manifest_data = dump(manifest)
    write_new(run / "source-manifest.json", manifest_data)
    receipt["source_manifest"] = {"path": "source-manifest.json", "bytes": len(manifest_data), "sha256": sha(manifest_data)}
    write_new(run / "RUN.json", dump(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode}, ensure_ascii=False))


if __name__ == "__main__":
    main()
