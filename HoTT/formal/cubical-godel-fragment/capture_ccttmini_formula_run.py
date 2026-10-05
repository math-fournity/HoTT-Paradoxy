#!/usr/bin/env python3
"""Capture the GZ-010 CCTTmini₀ formula/certificate-predicate interface."""
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
PACKAGE = Path("HoTT/formal/cubical-godel-fragment")
BASE = PACKAGE / "CCTTmini.agda"
NAT = PACKAGE / "CCTTminiNat.agda"
SOURCE = PACKAGE / "CCTTminiFormula.agda"
NEGATIVE = PACKAGE / "WrongCCTTminiFormula.agda"
CLAIM = PACKAGE / "FORMULA_PREDICATE_CLAIM.md"
TOOLCHAIN = PACKAGE / "TOOLCHAIN.json"
RUN_PREFIX = "20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-001-"
NEG_PREFIX = "20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-NEG-001-"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()


def source_row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def main() -> int:
    negative = "--negative" in sys.argv[1:]
    prefix = NEG_PREFIX if negative else RUN_PREFIX
    run_id = next((arg for arg in sys.argv[1:] if not arg.startswith("--")), f"{prefix}01")
    if "/" in run_id or not run_id.startswith(prefix):
        raise SystemExit("RUN_ID_INVALID")
    source = NEGATIVE if negative else SOURCE
    inputs = [ROOT / path for path in (BASE, NAT, SOURCE, NEGATIVE, CLAIM, TOOLCHAIN, Path(__file__).relative_to(ROOT))]
    if any(not path.is_file() or path.is_symlink() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    spec = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    agda = Path(spec["agda"]["binary"])
    if not agda.is_file() or agda.is_symlink() or sha(agda.read_bytes()) != spec["agda"]["sha256"]:
        raise SystemExit("AGDA_BINARY_MISMATCH")
    run_dir = ROOT / "HoTT/verification/runs" / run_id
    if run_dir.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    argv = [
        str(agda), "--ignore-interfaces", "--safe", "--cubical",
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
    negative_ok = negative and result.returncode != 0 and b"!= botF" in result.stdout + result.stderr
    proof_id = "MP-CUBICAL-GODEL-FORMULA-PREDICATE-NEG-001" if negative else "MP-CUBICAL-GODEL-FORMULA-PREDICATE-001"
    claim_ids = ["C-379–C-382 (negative control)"] if negative else ["C-379", "C-380", "C-381", "C-382"]
    warning_marker = b"UnsupportedIndexedMatch"
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": proof_id,
        "run_id": run_id,
        "files": [source_row(path) for path in inputs],
        "external_dependencies": [{
            "label": "agda-2.8.0-macos-arm64",
            "local_path": str(agda),
            "bytes": agda.stat().st_size,
            "sha256": sha(agda.read_bytes()),
        }],
        "scope": "CCTTmini₀ formula syntax and meta-level certificate-predicate interface; no arithmetic representability or fixed point.",
    }
    receipt: dict[str, object] = {
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
        "warnings": {
            "unsupported_indexed_match_present": warning_marker in result.stdout + result.stderr,
            "scope": "Inherited from CCTTminiNat's auxiliary bound proof; C-379–C-382 do not claim transport-level computation for it."
        },
        "scope": "C-379–C-382 concern only formula syntax that cites CCTTmini₀ certificate codes and a separate meta-level ProvWitness interface.",
        "non_goals": [
            "Does not make validCode or ProvWitness an object-arithmetic representable predicate.",
            "Does not define formula Nat coding, formula substitution, a diagonal fixed point, or an incompleteness theorem.",
            "Does not formalize full cctt/redtt/Cubical Agda/HoTT semantics, H0 transport, or bare-ZFC attribution.",
        ],
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run_dir.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", result.stdout),
        ("stderr", "stderr.txt", result.stderr),
        ("environment", "environment.txt", (
            f"platform={platform.platform()}\n"
            f"XDG_DATA_HOME={env['XDG_DATA_HOME']}\n"
            f"XDG_CONFIG_HOME={env['XDG_CONFIG_HOME']}\n"
            f"TMPDIR={env['TMPDIR']}\n"
        ).encode()),
        ("source_manifest", "source-manifest.json", json_bytes(manifest)),
    ):
        write_new(run_dir / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run_dir / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": run_id, "exit": result.returncode, "warning": receipt["warnings"]}, ensure_ascii=False))
    return 0 if (negative_ok if negative else accepted) else 1


if __name__ == "__main__":
    raise SystemExit(main())
