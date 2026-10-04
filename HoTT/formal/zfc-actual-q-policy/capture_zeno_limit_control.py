#!/usr/bin/env python3
"""Capture the pinned Mathlib control for C-361 without changing source."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-01"
PROOF_ID = "MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001"
SOURCE = Path("HoTT/formal/zfc-actual-q-policy/ZenoLimitControl.lean")
TOOLCHAIN = Path("HoTT/formal/astra-real-geometry/TOOLCHAIN.json")
LEAN_PATH_FILE = Path("audit/astra-real-geometry-20260919/environment-qualification/LEAN_PATH.txt")
LEAN = Path("/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean")


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
    if "/" in RUN_ID or not RUN_ID.startswith("20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-"):
        raise SystemExit("RUN_ID_INVALID")
    # Only compiler inputs and the capture contract are frozen here.  Claim
    # prose and source cards are evidence documentation, not imports or
    # command inputs; including them would needlessly invalidate a kernel run
    # whenever its human-readable scope explanation is improved.
    inputs = [ROOT / p for p in (SOURCE, TOOLCHAIN, LEAN_PATH_FILE, Path(__file__).relative_to(ROOT))]
    if any(not p.is_file() for p in inputs) or not LEAN.is_file():
        raise SystemExit("REQUIRED_INPUT_MISSING")
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    lean_path = (ROOT / LEAN_PATH_FILE).read_text(encoding="utf-8").strip()
    if not lean_path:
        raise SystemExit("LEAN_PATH_EMPTY")
    # Keep the Mathlib import root in the persisted command itself.  The
    # generic proof-run verifier replays `command_argv` without inheriting this
    # process environment, so an environment-only LEAN_PATH would make a
    # successful first run irreproducible.
    argv = ["/usr/bin/env", f"LEAN_PATH={lean_path}", str(LEAN), SOURCE.as_posix()]
    env = os.environ.copy()
    env["LEAN_PATH"] = lean_path
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(p) for p in inputs],
        "external_dependencies": [{
            "label": "lean-4.34.0-binary",
            "local_path": str(LEAN),
            "bytes": LEAN.stat().st_size,
            "sha256": sha(LEAN.read_bytes()),
        }],
        "policy": "Pinned Mathlib real-analysis control; the classical dependency report remains in Lean stdout.",
    }
    manifest_data = json_bytes(manifest)
    environment = (
        f"platform={platform.platform()}\nlean={version}\nlean_path={lean_path}\n"
        "imports=Mathlib.Analysis.SpecificLimits.Normed\n"
        "axioms=printed-in-stdout; expected classical/Mathlib dependencies\n"
    ).encode("utf-8")
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-361"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4.34.0 plus pinned Mathlib real analysis; strict finite-stage control and closed-time endpoint positive control, not a formalization of ZFC or physical motion.",
        "command_argv": argv,
        "cwd": str(ROOT),
        "lean_path": lean_path,
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "For s_n = 1 - (1/2)^n, formal limit completion does not imply finite natural-stage endpoint completion; a separate closed continuous-time model has endpoint arrival.",
        "non_goals": [
            "Does not attribute StrictSequentialDone to the Standard Solution or mathematical community.",
            "Does not prove that continuous motion fails to arrive, that ZFC is inconsistent, or that all limit arguments are illusory.",
            "Does not supply an actual Zeno/HoTT same-Q mapping or source-owned acceptance policy.",
        ],
        "axiom_policy": "Expected Mathlib/classical dependencies are retained verbatim from Lean #print axioms and are not described as no-axiom proof.",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (("stdout", "stdout.txt", result.stdout), ("stderr", "stderr.txt", result.stderr), ("environment", "environment.txt", environment), ("source_manifest", "source-manifest.json", manifest_data)):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode, "stdout_sha256": sha(result.stdout), "stderr_sha256": sha(result.stderr)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
