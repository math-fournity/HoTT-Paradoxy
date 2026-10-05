#!/usr/bin/env python3
"""Capture the source-bound positive M-level Appendix-C vocabulary control."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_ID = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "20261005-MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001"
)
PROOF_ID = "MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001"
SOURCE = Path("HoTT/formal/godel-q-reflection/SetMMAppendixCVarExtension.lean")
GENERATED = Path("HoTT/formal/godel-q-reflection/SetMMAppendixCGenerated.lean")
CLAIM = Path("HoTT/formal/godel-q-reflection/SetMMAppendixCVarExtension-CLAIM.md")
PACKAGE_README = Path("HoTT/formal/godel-q-reflection/README.md")
TOOLCHAIN = Path("HoTT/formal/godel-q-reflection/LEAN_CORE_TOOLCHAIN.json")
GENERATOR = Path("scripts/audit/generate_setmm_appendix_c_vocabulary.py")
RUNNER = Path("HoTT/formal/godel-q-reflection/run_setmm_appendix_c_var_extension.py")
RAW_SETMM = Path("/Volumes/D/HoTT-downloads/godel-q-setmm-160ebb/set.mm")
EXPECTED_SETMM_SHA256 = "d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a"


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
    if "/" in RUN_ID or not RUN_ID.startswith("20261005-MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-"):
        raise SystemExit("RUN_ID_INVALID")
    inputs = [
        ROOT / item
        for item in (SOURCE, GENERATED, CLAIM, PACKAGE_README, TOOLCHAIN, GENERATOR, RUNNER, Path(__file__).relative_to(ROOT))
    ]
    if any(not path.is_file() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    if not RAW_SETMM.is_file() or sha(RAW_SETMM.read_bytes()) != EXPECTED_SETMM_SHA256:
        raise SystemExit("RAW_SETMM_IDENTITY_MISMATCH")
    toolchain = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    lean_spec = toolchain.get("lean")
    if not isinstance(lean_spec, dict) or not isinstance(lean_spec.get("root"), str):
        raise SystemExit("LEAN_TOOLCHAIN_INVALID")
    lean = Path(str(lean_spec["root"])) / "bin" / "lean"
    if not lean.is_file() or lean.is_symlink():
        raise SystemExit("LEAN_BINARY_INVALID")
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")

    started = dt.datetime.now(dt.timezone.utc)
    command = [
        sys.executable,
        str(RUNNER),
        "--mode", "positive",
        "--lean", str(lean),
        "--source", SOURCE.as_posix(),
    ]
    with tempfile.TemporaryDirectory(prefix="godel-q-setmm-appendix-c-capture-") as scratch_text:
        summary_path = Path(scratch_text) / "summary.json"
        result = subprocess.run(command + ["--summary", str(summary_path)], cwd=ROOT, capture_output=True)
        if not summary_path.is_file():
            raise RuntimeError("RUNNER_SUMMARY_MISSING")
        runner_summary = json.loads(summary_path.read_text(encoding="utf-8"))
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    combined_stdout = result.stdout
    combined_stderr = result.stderr
    accepted = result.returncode == 0 and b"sorryAx" not in combined_stdout and b"declaration uses 'sorry'" not in combined_stderr
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(path) for path in inputs],
        "external_dependencies": [
            {
                "label": "lean-4.34.1-core-binary",
                "local_path": str(lean),
                "bytes": lean.stat().st_size,
                "sha256": sha(lean.read_bytes()),
            },
            {
                "label": "set.mm-160ebb-raw-source",
                "local_path": str(RAW_SETMM),
                "bytes": RAW_SETMM.stat().st_size,
                "sha256": EXPECTED_SETMM_SHA256,
            },
        ],
        "policy": "The generator must reproduce the tracked vocabulary source byte-for-byte. Lean checks only the M-level finite-vocabulary embedding and infinite fresh-variable extension stated in the claim document.",
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-369"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": toolchain["theory_variant"],
        "command_argv": command,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Source-bound M-level proof: the exact raw set.mm vocabulary and its $f assignments embed injectively into an explicit countably infinite fresh extension for each source variable type.",
        "non_goals": [
            "No ZF-internal mFS witness for the whole set.mm database.",
            "No mPPSt/mThm proof-trace adequacy, adequate Prv, diagonal sentence, or incompleteness theorem.",
            "No OriginDone, reality map rho, completion bridge, actual Q policy, or bare ZFC conclusion.",
        ],
        "axiom_policy": "The proof source prints Lean kernel axiom reports; accepted status requires all selected theorems to be free of axioms and of sorryAx.",
        "generated_source_check": {
            "status": runner_summary["generated_source_status"],
            "generator_exit_code": runner_summary["generator_exit_code"],
            "generated_compile_exit_code": runner_summary["generated_compile_exit_code"],
        },
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", combined_stdout),
        ("stderr", "stderr.txt", combined_stderr),
        ("environment", "environment.txt", (f"platform={platform.platform()}\nlean={version}\nimports=generated local module + Lean core only\nraw_setmm_sha256={EXPECTED_SETMM_SHA256}\n").encode("utf-8")),
        ("source_manifest", "source-manifest.json", json_bytes(manifest)),
    ):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode}, ensure_ascii=False))


if __name__ == "__main__":
    main()
