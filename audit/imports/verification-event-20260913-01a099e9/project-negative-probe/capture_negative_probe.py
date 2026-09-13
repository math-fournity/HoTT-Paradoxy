#!/usr/bin/env python3
"""Frozen negative-calibration probe for MP-VERIFICATION-EVENT-001.

The project capture script (scripts/audit/capture_agda_proof_run.py) runs Agda
with a single include directory (the source's own directory), so it cannot
express "negative/BadCast.agda imports ../VerificationEvent.agda".  Instead of
changing that shared Gate tool, this probe reproduces the exact frozen command
shape with two `-i` paths and records raw stdout/stderr/exit code.

It is a calibration probe, NOT a formal-proof run receipt: the expected result
is kernel rejection (exit 42, UnequalTerms on BadCast.agda line 10).  The
preserved external package keeps its own negative-002 receipt as primary
negative evidence.

Usage: python3 capture_negative_probe.py --project-root /path/to/repo
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

AGDA = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda")
AGDA_SHA256 = "ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e"
CACHE = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64")
SOURCE = "HoTT/formal/verification-event/negative/BadCast.agda"
INCLUDES = ("HoTT/formal/verification-event", "HoTT/formal/verification-event/negative")
REGISTRY = "HoTT/formal/verification-event/AGDA_LIBRARIES"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    if sha(AGDA.read_bytes()) != AGDA_SHA256:
        raise SystemExit("AGDA_BINARY_HASH_MISMATCH")
    command = [
        "/usr/bin/env",
        f"XDG_DATA_HOME={CACHE / 'xdg-data'}",
        f"XDG_CONFIG_HOME={CACHE / 'xdg-config'}",
        f"TMPDIR={CACHE / 'tmp'}",
        str(AGDA), "--ignore-interfaces",
        f"--library-file={root / REGISTRY}",
        "-l", "cubical-0.9",
    ]
    for include in INCLUDES:
        command += ["-i", include]
    command.append(SOURCE)
    result = subprocess.run(command, cwd=root, capture_output=True, check=False)
    out = Path(__file__).resolve().parent
    (out / "command.txt").write_text(" ".join(command) + "\n", encoding="utf-8")
    (out / "stdout.txt").write_bytes(result.stdout)
    (out / "stderr.txt").write_bytes(result.stderr)
    text = result.stdout.decode("utf-8", "replace")
    expectation = ("[UnequalTerms]" in text and "afterP != initial" in text
                   and "BadCast.agda" in text and result.returncode == 42)
    (out / "exit_code.txt").write_text(f"{result.returncode}\n", encoding="utf-8")
    (out / "probe.json").write_text(json.dumps({
        "schema_version": "negative-calibration-probe/v1",
        "probe_id": "MP-VERIFICATION-EVENT-001-NEGATIVE-PROBE",
        "proof_id": "MP-VERIFICATION-EVENT-001",
        "source": SOURCE,
        "agda_binary": str(AGDA),
        "agda_sha256": AGDA_SHA256,
        "command_argv": command,
        "exit_code": result.returncode,
        "expected_exit_code": 42,
        "expectation_met": expectation,
        "stdout_sha256": sha(result.stdout),
        "stderr_sha256": sha(result.stderr),
        "status": "KERNEL_REJECTED_AS_EXPECTED" if expectation else "UNEXPECTED",
        "boundary": ("Calibration probe only: it is not a formal-proof-run/v1 receipt and must not be "
                     "cited as a passing proof. Primary negative evidence remains the preserved external "
                     "negative-002 receipt."),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "KERNEL_REJECTED_AS_EXPECTED" if expectation else "UNEXPECTED",
                      "exit_code": result.returncode, "expectation_met": expectation}, ensure_ascii=False))
    return 0 if expectation else 1


if __name__ == "__main__":
    raise SystemExit(main())
