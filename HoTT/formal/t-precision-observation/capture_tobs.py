#!/usr/bin/env python3
"""Capture the positive Lean-core run for MP-T-PRECISION-TOBS-001."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261004-MP-T-PRECISION-TOBS-001-01"
PROOF_ID = "MP-T-PRECISION-TOBS-001"
CLAIM_IDS = ["C-367"]
SOURCE = Path("HoTT/formal/t-precision-observation/ObservationPrecision.lean")
CLAIM = Path("HoTT/formal/t-precision-observation/CLAIM.md")
README = Path("HoTT/formal/t-precision-observation/README.md")
TOOLCHAIN = Path("HoTT/formal/t-precision-observation/LEAN_CORE_TOOLCHAIN.json")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def dump(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith("20261004-MP-T-PRECISION-TOBS-001-"):
        raise SystemExit("RUN_ID_INVALID")
    inputs = [ROOT / p for p in (
        SOURCE, CLAIM, README, TOOLCHAIN,
        Path(__file__).relative_to(ROOT),
    )]
    if any(not path.is_file() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    spec = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    lean_root = Path(spec["lean"]["root"])
    lean = lean_root / "bin" / "lean"
    core = lean_root / "src/lean/Init/Core.lean"
    prelude = lean_root / "src/lean/Init/Prelude.lean"
    if any(not path.is_file() or path.is_symlink() for path in (lean, core, prelude)):
        raise SystemExit("LEAN_INPUT_INVALID")
    if sha(lean.read_bytes()) != spec["lean"]["binary_sha256"]:
        raise SystemExit("LEAN_BINARY_HASH_MISMATCH")
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    argv = [str(lean), SOURCE.as_posix()]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    accepted = result.returncode == 0 and b"depends on any axioms" not in result.stdout
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(path) for path in inputs],
        "external_dependencies": [
            {"label": "lean-core-binary", "local_path": str(lean), "bytes": lean.stat().st_size, "sha256": sha(lean.read_bytes())},
            {"label": "lean-core-init-core", "local_path": str(core), "bytes": core.stat().st_size, "sha256": sha(core.read_bytes())},
            {"label": "lean-core-init-prelude", "local_path": str(prelude), "bytes": prelude.stat().st_size, "sha256": sha(prelude.read_bytes())},
        ],
        "policy": "The kernel proves only the stated function/Prop factorization boundary. The T0 card, source denominator, and user source are linked from CLAIM.md as contextual evidence and do not become kernel inputs.",
    }
    environment = (
        f"platform={platform.platform()}\nlean={version}\n"
        "imports=Lean core only\naxioms=printed in stdout; expected none\n"
    ).encode()
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": spec["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Abstract collision-to-no-decoder theorem plus finite Bool/Unit control and identity positive control.",
        "non_goals": spec["non_goals"],
        "axiom_policy": "Each selected theorem prints a Lean axiom report; acceptance requires no line saying it depends on axioms.",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", result.stdout),
        ("stderr", "stderr.txt", result.stderr),
        ("environment", "environment.txt", environment),
        ("source_manifest", "source-manifest.json", dump(manifest)),
    ):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", dump(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode}, ensure_ascii=False))


if __name__ == "__main__":
    main()
