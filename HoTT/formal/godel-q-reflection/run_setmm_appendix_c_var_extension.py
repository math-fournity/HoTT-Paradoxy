#!/usr/bin/env python3
"""Run the reproducible Appendix-C vocabulary-extension Lean controls.

This runner has no persistent output except an optional JSON summary requested
by a capture script.  It rebuilds the generated local import in a temporary
directory, so the command saved in a proof receipt can be replayed without a
hidden ``LEAN_PATH`` or stale ``.olean`` file.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RAW_SETMM = Path("/Volumes/D/HoTT-downloads/godel-q-setmm-160ebb/set.mm")
EXPECTED_SETMM_SHA256 = "d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a"
GENERATOR = ROOT / "scripts/audit/generate_setmm_appendix_c_vocabulary.py"
GENERATED = ROOT / "HoTT/formal/godel-q-reflection/SetMMAppendixCGenerated.lean"
POSITIVE = ROOT / "HoTT/formal/godel-q-reflection/SetMMAppendixCVarExtension.lean"
NEGATIVE = ROOT / "HoTT/formal/godel-q-reflection/WrongSetMMFiniteVocabulary.lean"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def emit_summary(path: Path | None, value: dict[str, object]) -> None:
    if path is not None:
        path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=("positive", "negative"))
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()

    expected_source = POSITIVE if args.mode == "positive" else NEGATIVE
    source = (ROOT / args.source).resolve()
    if source != expected_source.resolve():
        raise SystemExit(f"SOURCE_MODE_MISMATCH:{source}")
    if not args.lean.is_file() or args.lean.is_symlink():
        raise SystemExit("LEAN_BINARY_INVALID")
    if not RAW_SETMM.is_file() or sha(RAW_SETMM.read_bytes()) != EXPECTED_SETMM_SHA256:
        raise SystemExit("RAW_SETMM_IDENTITY_MISMATCH")

    with tempfile.TemporaryDirectory(prefix="godel-q-setmm-appendix-c-run-") as scratch_text:
        scratch = Path(scratch_text)
        regenerated = scratch / GENERATED.name
        generation = subprocess.run(
            [sys.executable, str(GENERATOR), "--input", str(RAW_SETMM), "--output", str(regenerated)],
            cwd=ROOT,
            capture_output=True,
        )
        if generation.returncode != 0 or regenerated.read_bytes() != GENERATED.read_bytes():
            sys.stderr.buffer.write(generation.stdout + generation.stderr)
            raise SystemExit("GENERATED_SOURCE_DRIFT")

        generated_compile = subprocess.run(
            [str(args.lean), "-o", str(scratch / "SetMMAppendixCGenerated.olean"), str(GENERATED)],
            cwd=ROOT,
            capture_output=True,
        )
        if generated_compile.returncode != 0:
            sys.stderr.buffer.write(generated_compile.stdout + generated_compile.stderr)
            raise SystemExit("GENERATED_LEAN_COMPILE_REJECTED")

        environment = dict(os.environ)
        environment["LEAN_PATH"] = str(scratch)
        positive_compile = None
        if args.mode == "negative":
            positive_compile = subprocess.run(
                [str(args.lean), "-o", str(scratch / "SetMMAppendixCVarExtension.olean"), str(POSITIVE)],
                cwd=ROOT,
                env=environment,
                capture_output=True,
            )
            if positive_compile.returncode != 0:
                sys.stderr.buffer.write(positive_compile.stdout + positive_compile.stderr)
                raise SystemExit("POSITIVE_PRECONDITION_REJECTED")
        result = subprocess.run([str(args.lean), str(source)], cwd=ROOT, env=environment, capture_output=True)

    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(result.stderr)
    emit_summary(
        args.summary,
        {
            "schema_version": "setmm-appendix-c-runner/v1",
            "mode": args.mode,
            "raw_setmm_sha256": EXPECTED_SETMM_SHA256,
            "generated_source_status": "BYTE_IDENTICAL",
            "generator_exit_code": generation.returncode,
            "generated_compile_exit_code": generated_compile.returncode,
            "positive_compile_exit_code": None if positive_compile is None else positive_compile.returncode,
            "lean_exit_code": result.returncode,
        },
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
