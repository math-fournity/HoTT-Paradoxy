#!/usr/bin/env python3
"""Capture the M1 finite-observation trace theorem with pinned Cubical Agda."""
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
TOOLCHAIN = Path("HoTT/formal/zfc-h0-final-closure/TOOLCHAIN.json")
CLAIM = Path("HoTT/formal/zfc-h0-final-closure/CLAIM.md")
README = Path("HoTT/formal/zfc-h0-final-closure/README.md")
SOURCE = Path("HoTT/formal/zfc-h0-final-closure/H0TraceObservation.agda")
NEGATIVE = Path("HoTT/formal/zfc-h0-final-closure/WrongH0TraceFiniteHalt.agda")
UPSTREAM = (
    Path("HoTT/formal/claude-cg001/pedometer-semantics/PedometerSemantics.agda"),
    Path("HoTT/formal/claude-cg001/pedometer-semantics/DelayMonad.agda"),
    Path("HoTT/formal/claude-cg001/questioning-delay/QuestioningDelay.agda"),
    # This is a transitive source input of QuestioningDelay, observed in the
    # real Agda compiler output and therefore part of the proof closure.
    Path("HoTT/formal/claude-cg001/universe-questioning/UniverseHasNoLevel.agda"),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    negative = "--negative" in sys.argv[1:]
    expected_prefix = "20261004-MP-ZFC-H0-TRACE-NEG-001-" if negative else "20261004-MP-ZFC-H0-TRACE-001-"
    default = f"{expected_prefix}01"
    run_id = next((arg for arg in sys.argv[1:] if not arg.startswith("--")), default)
    if "/" in run_id or not run_id.startswith(expected_prefix):
        raise SystemExit("RUN_ID_INVALID")
    source = NEGATIVE if negative else SOURCE
    # Only elaborator inputs plus the package-local claim/toolchain contract
    # are frozen here.  The README and total SOP route to this package but are
    # not inputs read by Agda; including evolving routing prose would create a
    # false theorem-source drift on every planning update.
    inputs = [ROOT / path for path in (TOOLCHAIN, CLAIM, SOURCE, NEGATIVE, *UPSTREAM, Path(__file__).relative_to(ROOT))]
    if any(not path.is_file() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    spec = json.loads((ROOT / TOOLCHAIN).read_text())
    agda = Path(spec["agda"]["binary"])
    if not agda.is_file() or sha(agda.read_bytes()) != spec["agda"]["sha256"]:
        raise SystemExit("AGDA_BINARY_MISMATCH")
    library_file = ROOT / str(spec["project_library_registry"])
    if not library_file.is_file():
        raise SystemExit("AGDA_LIBRARY_REGISTRY_MISSING")
    run = ROOT / "HoTT/verification/runs" / run_id
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    argv = [
        str(agda), "--ignore-interfaces", f"--library-file={library_file}", "-l", "cubical-0.9",
        *sum((["-i", str(ROOT / root)] for root in spec["include_roots"]), []),
        str(source),
    ]
    env = os.environ.copy()
    cache = agda.parent
    env.update({
        "XDG_DATA_HOME": str(cache / "xdg-data"),
        "XDG_CONFIG_HOME": str(cache / "xdg-config"),
        "TMPDIR": str(cache / "tmp"),
    })
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(agda), "--version"], text=True).strip()
    accepted = result.returncode == 0
    negative_ok = negative and result.returncode != 0 and b"nothing != just 1" in result.stdout
    proof_id = "MP-ZFC-H0-TRACE-NEG-001" if negative else "MP-ZFC-H0-TRACE-001"
    claim_ids = ["C-365"] if not negative else ["C-365 (negative control)"]
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": proof_id,
        "run_id": run_id,
        "files": [row(path) for path in inputs],
        "external_dependencies": [
            {
                "label": "agda-2.8.0-macos-arm64",
                "local_path": str(agda),
                "bytes": agda.stat().st_size,
                "sha256": sha(agda.read_bytes()),
            },
            {
                "label": "cubical-extracted-tree",
                "local_path": str(Path(spec["cubical_library"]["library_file"]).parent),
                "file_count": 1111,
                "total_bytes": 7511145,
                "tree_sha256": spec["cubical_library"]["tree_sha256"],
                "tag_commit": spec["cubical_library"]["commit"],
            },
        ],
        "scope": "Exact native Delay/runFor observation fragment; no full semantic model claim.",
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": run_id,
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "proof_assistant": "Cubical Agda",
        "proof_assistant_version": version,
        "theory_variant": spec["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "NEGATIVE_CONTROL_REJECTED" if negative_ok else ("KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED"),
        "scope": "C-365: the native fixed H0 Delay/runFor output maps into a set-valued finite trace and remains all-nothing at every finite fuel. This is H0_OPERATIONAL_FRAGMENT_ONLY, not H0Map or a bare-ZFC theorem.",
        "non_goals": [
            "Does not interpret the complete Cubical Agda 2.8.0 plus cubical 0.9 library in CCHM or ZFC.",
            "Does not establish H0Map, C_accept, AdequacyLift, SameFullQ, P, or bare-ZFC attribution.",
            "Does not treat the source target as a proof of an actual foundation policy.",
        ],
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", result.stdout),
        ("stderr", "stderr.txt", result.stderr),
        ("environment", "environment.txt", (f"platform={platform.platform()}\nXDG_DATA_HOME={env['XDG_DATA_HOME']}\nXDG_CONFIG_HOME={env['XDG_CONFIG_HOME']}\nTMPDIR={env['TMPDIR']}\n").encode()),
        ("source_manifest", "source-manifest.json", json_bytes(manifest)),
    ):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": run_id, "exit": result.returncode}, ensure_ascii=False))
    if negative:
        raise SystemExit(0 if negative_ok else 1)
    raise SystemExit(0 if accepted else 1)


if __name__ == "__main__":
    main()
