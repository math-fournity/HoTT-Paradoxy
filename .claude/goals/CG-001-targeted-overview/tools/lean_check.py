#!/usr/bin/env python3
"""Build-and-check driver for pinned Lean 4 sources (CG-001, goal-local).

Why this exists: an F-011 receipt replays exactly one command, but a Lean
negative control imports the module it tests, so that module must be compiled
first.  This driver compiles the given sources in order into a temporary build
directory with the pinned toolchain, optionally replays the last module with
`leanchecker --fresh` (every constant, imported or new, re-added to a fresh
kernel environment), and passes Lean's outputs through unchanged, each preceded
by one fixed header line.  The build directory never appears in the output, so
a replay is byte-for-byte comparable.

The pinned binaries are called by absolute path with a minimal environment
(PATH=<prefix>/bin:/usr/bin:/bin, LEAN_SYSROOT=<prefix>, LEAN_PATH=<build>),
so the elan proxy is never reached (see the incident note in the toolchain
record: an unisolated call once made elan download another toolchain).

Usage (cwd = repository root, paths relative to it):
  python3 -B .claude/goals/CG-001-targeted-overview/tools/lean_check.py \
      --toolchain HoTT/formal/claude-cg001/pedometer-ablation-lean/LEAN_TOOLCHAIN.json \
      [--leanchecker] <Source1.lean> [<Source2.lean> ...]
Exit code: the first nonzero exit code of a step, else 0.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[4]
FORBIDDEN_WORDS = ("sorry", "admit", "native_decide", "unsafe", "implemented_by", "extern", "opaque")
FORBIDDEN_PATTERNS = (r"^\s*(private\s+|protected\s+)?axiom\b", r"debug\.skipKernelTC", r"ofReduceBool", r"reduceBool")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def source_violations(text: str) -> list[str]:
    found = [w for w in FORBIDDEN_WORDS if re.search(rf"\b{w}\b", text)]
    found += [p for p in FORBIDDEN_PATTERNS if re.search(p, text, flags=re.MULTILINE)]
    return found


def check_toolchain(record: dict) -> Path:
    prefix = Path(record["prefix"])
    for row in record["pinned_files"]:
        data = (prefix / row["relative_path"]).read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"LEAN_TOOLCHAIN_FILE_MISMATCH:{row['relative_path']}")
    return prefix


def emit(header: str, result: subprocess.CompletedProcess) -> None:
    sys.stdout.buffer.write(f"## {header}\n".encode("utf-8"))
    sys.stdout.buffer.write(result.stdout)
    sys.stdout.buffer.flush()
    sys.stderr.buffer.write(result.stderr)
    sys.stderr.buffer.flush()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--toolchain", required=True)
    parser.add_argument("--leanchecker", action="store_true")
    parser.add_argument("sources", nargs="+")
    args = parser.parse_args()

    record = json.loads((ROOT / safe_relative(args.toolchain)).read_text(encoding="utf-8"))
    prefix = check_toolchain(record)
    sources = [safe_relative(s) for s in args.sources]
    for relative in sources:
        if relative.suffix != ".lean":
            raise SystemExit(f"NOT_A_LEAN_SOURCE:{relative}")
        bad = source_violations((ROOT / relative).read_text(encoding="utf-8"))
        if bad:
            raise SystemExit(f"LEAN_FORBIDDEN_MARKER:{relative}:{bad}")

    with tempfile.TemporaryDirectory(prefix="cg001-lean-") as build:
        env = {
            "HOME": os.environ.get("HOME", "/"),
            "PATH": f"{prefix}/bin:/usr/bin:/bin",
            "LEAN_SYSROOT": str(prefix),
            "LEAN_PATH": build,
        }
        for relative in sources:
            argv = [str(prefix / "bin/lean"), "-R", relative.parent.as_posix(),
                    "-o", str(Path(build) / f"{relative.stem}.olean"), relative.as_posix()]
            result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, stdin=subprocess.DEVNULL, check=False)
            emit(f"lean {relative.as_posix()}", result)
            if result.returncode != 0:
                sys.stdout.buffer.write(f"## exit {result.returncode}\n".encode("utf-8"))
                return result.returncode
        if args.leanchecker:
            module = sources[-1].stem
            argv = [str(prefix / "bin/leanchecker"), "--fresh", module]
            result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, stdin=subprocess.DEVNULL, check=False)
            emit(f"leanchecker --fresh {module}", result)
            if result.returncode != 0:
                sys.stdout.buffer.write(f"## exit {result.returncode}\n".encode("utf-8"))
                return result.returncode
    sys.stdout.buffer.write(b"## exit 0\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
