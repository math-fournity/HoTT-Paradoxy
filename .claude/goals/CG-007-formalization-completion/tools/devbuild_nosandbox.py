#!/usr/bin/env python3
"""Local drop-in driver for CG-006 package build, WITHOUT sandbox-exec.

Mirrors .claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py
but invokes bin/lean directly (the environment forbids /usr/bin/sandbox-exec).
All compilation is local against cached Foundation/Mathlib oleans; no network.

Usage:
  python3 /tmp/build_z0.py [--no-pin-check] --package <rel> <GodelQ/A.lean> [...]
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[0]  # not used; package resolved from --package relative to cwd
FORBIDDEN_WORDS = ("sorry", "admit", "native_decide", "unsafe", "implemented_by", "extern", "opaque")
FORBIDDEN_PATTERNS = (r"^\s*(private\s+|protected\s+)?axiom\b", r"debug\.skipKernelTC", r"ofReduceBool", r"reduceBool")

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_relative(value: str) -> Path:
    from pathlib import PurePosixPath
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)

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
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--no-pin-check", action="store_true")
    ap.add_argument("--no-forbidden-check", action="store_true")
    ap.add_argument("sources", nargs="+")
    args = ap.parse_args()

    package = Path(args.package).resolve()
    toolchain = json.loads((package / "LEAN_TOOLCHAIN.json").read_text(encoding="utf-8"))
    closure = json.loads((package / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))

    prefix = Path(toolchain["prefix"])
    if not args.no_pin_check:
        for row in toolchain["pinned_files"]:
            data = (prefix / row["relative_path"]).read_bytes()
            if len(data) != row["bytes"] or sha(data) != row["sha256"]:
                sys.stdout.write(f"## PINNED_INPUT_MISMATCH LEAN_TOOLCHAIN_FILE:{row['relative_path']}\n"); return 3
        roots = {name: Path(path) for name, path in closure["library_roots"].items()}
        for row in closure["modules"]:
            root = roots[row["root"]]
            if module_digest(root, row["module"]) != row["digest"]:
                sys.stdout.write(f"## PINNED_INPUT_MISMATCH MATHLIB_CLOSURE_MODULE:{row['module']}\n"); return 3
        sys.stdout.write(f"## PINNED_INPUT_OK modules={len(closure['modules'])}\n"); sys.stdout.flush()

    sources = [safe_relative(s) for s in args.sources]
    if not args.no_forbidden_check:
        for rel in sources:
            text = (package / rel).read_text(encoding="utf-8")
            found = [w for w in FORBIDDEN_WORDS if __import__("re").search(rf"\b{w}\b", text)]
            found += [p for p in FORBIDDEN_PATTERNS if __import__("re").search(p, text, flags=__import__("re").MULTILINE)]
            if found:
                sys.stdout.write(f"## FORBIDDEN_SOURCE_MARKER:{rel}:{found}\n"); return 3

    options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
    build = Path(os.environ.get("Z0_BUILD_DIR", "/tmp/z0_build_lib"))
    build.mkdir(parents=True, exist_ok=True)
    lean_path = ":".join([str(build)] + [str(p) for p in closure["lean_path"]])
    env = {"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix),
           "LEAN_PATH": lean_path, "HOME": str(build)}
    for rel in sources:
        module_rel = rel.with_suffix("")
        out = build / module_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        cmd = [str(prefix / "bin" / "lean"), *options, "-R", ".", "-o", str(out) + ".olean",
               "-i", str(out) + ".ilean", rel.as_posix()]
        result = subprocess.run(cmd, cwd=package, env=env, capture_output=True, check=False)
        sys.stdout.buffer.write(f"## lean {rel.as_posix()} (rc={result.returncode})\n".encode())
        sys.stdout.buffer.write(result.stdout)
        sys.stdout.buffer.flush()
        sys.stderr.buffer.write(result.stderr)
        sys.stderr.buffer.flush()
        if result.returncode != 0:
            return result.returncode
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
