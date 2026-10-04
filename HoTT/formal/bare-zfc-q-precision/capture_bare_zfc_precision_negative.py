#!/usr/bin/env python3
"""Capture the expected rejection of the coarse OriginDone decoder."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261004-MP-BARE-ZFC-Q-PRECISION-NEG-001"
PROOF_ID = "MP-BARE-ZFC-Q-PRECISION-NEG-001"
SOURCE = Path("HoTT/formal/bare-zfc-q-precision/WrongBareZFCPrecision.lean")
PARENT_SOURCE = Path("HoTT/formal/bare-zfc-q-precision/BareZFCPrecision.lean")
CLAIM = Path("HoTT/formal/bare-zfc-q-precision/CLAIM.md")
PACKAGE_README = Path("HoTT/formal/bare-zfc-q-precision/README.md")
TOOLCHAIN = Path("HoTT/formal/bare-zfc-q-precision/LEAN_CORE_TOOLCHAIN.json")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith("20261004-MP-BARE-ZFC-Q-PRECISION-NEG-"):
        raise SystemExit("RUN_ID_INVALID")
    inputs = [ROOT / p for p in (
        SOURCE, PARENT_SOURCE, CLAIM, PACKAGE_README, TOOLCHAIN,
        Path(__file__).relative_to(ROOT),
    )]
    if any(not path.is_file() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    toolchain = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    lean = Path(str(toolchain["lean"]["root"])) / "bin" / "lean"
    if not lean.is_file() or lean.is_symlink():
        raise SystemExit("LEAN_BINARY_INVALID")
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    argv = [str(lean), SOURCE.as_posix()]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    diagnostic = result.stdout + result.stderr
    expected = result.returncode != 0 and b"False \xe2\x86\x94 True" in diagnostic
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(path) for path in inputs],
        "external_dependencies": [{
            "label": "lean-4.34.1-core-binary",
            "local_path": str(lean),
            "bytes": lean.stat().st_size,
            "sha256": sha(lean.read_bytes()),
        }],
        "policy": "This is an expected rejection: the coarse view cannot be used to manufacture an OriginDone decoder.",
    }
    environment = (
        f"platform={platform.platform()}\nlean={version}\n"
        "expected=Lean rejects a False ↔ True strict-contract branch\n"
    ).encode("utf-8")
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-364"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": toolchain["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "EXPECTED_KERNEL_REJECTION" if expected else "UNEXPECTED_CONTROL_RESULT",
        "scope": "Negative control: a constant resolved view cannot prove the strict OriginDone branch.",
        "non_goals": [
            "Does not prove bare ZFC inconsistency or inability to encode a process.",
            "Does not establish a source fact or a physical motion conclusion.",
        ],
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", result.stdout),
        ("stderr", "stderr.txt", result.stderr),
        ("environment", "environment.txt", environment),
        ("source_manifest", "source-manifest.json", json_bytes(manifest)),
    ):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode}, ensure_ascii=False))
    if not expected:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
