#!/usr/bin/env python3
"""Build-and-check driver for the CG-005 Gödel-Q Lean package (goal-local).

Why this exists: the CG-001 driver (lean_check.py) compiles Lean-core sources only.
The Gödel-Q package imports Mathlib's computability and analysis libraries.  This
driver compiles the package sources in order into a fresh temporary build
directory with the pinned Lean binary, against a pinned, project-owned Mathlib
build, and refuses to run if any pinned input has changed:

* the Lean toolchain files listed in LEAN_TOOLCHAIN.json (bytes + SHA-256);
* every compiled Mathlib/dependency module in the import closure recorded in
  MATHLIB_CLOSURE.json (SHA-256 of .olean, .olean.private, .olean.server);
* the Lean options used for compilation.

The pinned binary is called by absolute path inside a network-denied macOS sandbox
(`sandbox-exec` with `(deny network*)`), with a minimal environment
(PATH=<prefix>/bin:/usr/bin:/bin, LEAN_SYSROOT=<prefix>, LEAN_PATH=<build>:<pinned
library roots>), so the elan proxy is never reached and nothing can be downloaded.
Outputs are passed through unchanged, each step preceded by one fixed header line;
the temporary build directory never appears in the output, so a replay is
byte-for-byte comparable.

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-005-godel-q-synthesis/tools/godelq_lean_check.py \
      --package HoTT/formal/claude-cg001/godel-q <GodelQ/A.lean> [<GodelQ/B.lean> ...]
Source paths are relative to the package directory and compiled in the given order;
the last one is the target.  Exit code: the first nonzero exit code of a step, 3 when
a pinned input does not match, else 0.
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


def fail(code: str) -> int:
    sys.stdout.write(f"## PINNED_INPUT_MISMATCH {code}\n")
    sys.stdout.flush()
    return 3


def module_digest(lib_root: Path, module: str) -> str:
    base = lib_root.joinpath(*module.split("."))
    digest = hashlib.sha256()
    for suffix in (".olean", ".olean.private", ".olean.server"):
        path = Path(str(base) + suffix)
        if path.exists():
            digest.update(suffix.encode())
            digest.update(sha(path.read_bytes()).encode())
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--package", required=True)
    parser.add_argument("sources", nargs="+")
    args = parser.parse_args()

    package = ROOT / safe_relative(args.package)
    toolchain = json.loads((package / "LEAN_TOOLCHAIN.json").read_text(encoding="utf-8"))
    closure = json.loads((package / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))

    prefix = Path(toolchain["prefix"])
    for row in toolchain["pinned_files"]:
        data = (prefix / row["relative_path"]).read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            return fail(f"LEAN_TOOLCHAIN_FILE:{row['relative_path']}")

    roots = {name: Path(path) for name, path in closure["library_roots"].items()}
    for row in closure["modules"]:
        root = roots[row["root"]]
        if module_digest(root, row["module"]) != row["digest"]:
            return fail(f"MATHLIB_CLOSURE_MODULE:{row['module']}")

    sources = [safe_relative(s) for s in args.sources]
    for rel in sources:
        text = (package / rel).read_text(encoding="utf-8")
        found = [w for w in FORBIDDEN_WORDS if re.search(rf"\b{w}\b", text)]
        found += [p for p in FORBIDDEN_PATTERNS if re.search(p, text, flags=re.MULTILINE)]
        if found:
            return fail(f"FORBIDDEN_SOURCE_MARKER:{rel}:{found}")

    options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
    profile = "(version 1)(allow default)(deny network*)"
    with tempfile.TemporaryDirectory(prefix="godelq-build-") as tmp:
        build = Path(tmp)
        lean_path = ":".join([str(build)] + [str(p) for p in closure["lean_path"]])
        env = {
            "PATH": f"{prefix}/bin:/usr/bin:/bin",
            "LEAN_SYSROOT": str(prefix),
            "LEAN_PATH": lean_path,
            "HOME": str(build),
        }
        for rel in sources:
            module_rel = rel.with_suffix("")
            out = build / module_rel
            out.parent.mkdir(parents=True, exist_ok=True)
            cmd = ["/usr/bin/sandbox-exec", "-p", profile, str(prefix / "bin" / "lean"), *options,
                   "-R", ".", "-o", str(out) + ".olean", "-i", str(out) + ".ilean", rel.as_posix()]
            result = subprocess.run(cmd, cwd=package, env=env, capture_output=True, check=False)
            sys.stdout.buffer.write(f"## lean {rel.as_posix()}\n".encode("utf-8"))
            sys.stdout.buffer.write(result.stdout)
            sys.stdout.buffer.flush()
            sys.stderr.buffer.write(result.stderr)
            sys.stderr.buffer.flush()
            if result.returncode != 0:
                return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
