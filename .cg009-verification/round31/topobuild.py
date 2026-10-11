#!/usr/bin/env python3
"""Independent from-scratch compile of a GodelQ package copy (CG-009 round 31).

Topologically sorts GodelQ-internal imports, compiles each file with the pinned
Lean 4.34.0 against pinned Foundation/Mathlib/Batteries, records exit codes and
#print axioms output. Stops at the first failure unless --keep-going.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

LEAN = "/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean"
FBUILD = "/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean"
ASTRA = Path("/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435")
PACKAGES = ["batteries", "aesop", "Qq", "proofwidgets", "importGraph", "LeanSearchClient", "plausible", "Cli"]

IMPORT_RE = re.compile(r"^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z][\w\.]*)\s*$", re.MULTILINE)


def lean_path(build: Path) -> str:
    parts = [str(build), FBUILD]
    for p in PACKAGES:
        parts.append(str(ASTRA / ".lake/packages" / p / ".lake/build/lib/lean"))
    return ":".join(parts)


def module_of(path: Path, src_root: Path) -> str:
    rel = path.relative_to(src_root)
    return ".".join(rel.with_suffix("").parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--build", required=True)
    ap.add_argument("--only", action="append", default=None)
    ap.add_argument("--timeout", type=int, default=540)
    ap.add_argument("--keep-going", action="store_true")
    ap.add_argument("--resume", action="store_true", help="skip files whose olean already exists")
    args = ap.parse_args()

    src_root = Path(args.src).resolve()
    build = Path(args.build).resolve()
    build.mkdir(parents=True, exist_ok=True)

    files = {module_of(p, src_root): p for p in src_root.rglob("*.lean")}
    deps: dict[str, set[str]] = {}
    for mod, p in files.items():
        text = p.read_text()
        ds = set()
        for m in IMPORT_RE.findall(text):
            if m in files:
                ds.add(m)
        deps[mod] = ds

    order: list[str] = []
    state: dict[str, int] = {}

    def visit(m: str, stack: list[str]) -> None:
        if state.get(m) == 2:
            return
        if state.get(m) == 1:
            print(f"  !! cycle: {' -> '.join(stack + [m])}", file=sys.stderr)
            return
        state[m] = 1
        for d in sorted(deps[m]):
            visit(d, stack + [m])
        state[m] = 2
        order.append(m)

    for m in sorted(files):
        visit(m, [])

    todo = order
    if args.only:
        keep = set()
        for m in order:
            if any(o in m for o in args.only):
                keep.add(m)
        changed = True
        while changed:
            changed = False
            for m in list(keep):
                for d in deps[m]:
                    if d not in keep:
                        keep.add(d)
                        changed = True
        todo = [m for m in order if m in keep]

    env = dict(os.environ)
    env["LEAN_PATH"] = lean_path(build)

    failures = []
    for i, mod in enumerate(todo, 1):
        src = files[mod]
        out = build / (mod.replace(".", "/") + ".olean")
        out.parent.mkdir(parents=True, exist_ok=True)
        if args.resume and out.exists():
            pass
        elif out.exists():
            out.unlink()
        cmd = [LEAN, "-DautoImplicit=false", "-R", str(src_root), "-o", str(out), str(src)]
        try:
            r = subprocess.run(cmd, env=env, capture_output=True, text=True,
                               timeout=args.timeout)
            code = r.returncode
            out_text = (r.stdout + r.stderr).strip()
        except subprocess.TimeoutExpired:
            code = "TIMEOUT"
            out_text = f"timeout after {args.timeout}s"
        status = "OK " if code == 0 else f"FAIL({code})"
        tail = out_text.splitlines()[-1] if out_text else ""
        print(f"[{i:2}/{len(todo)}] {status} {mod}  {tail[:120]}", flush=True)
        if code != 0:
            failures.append((mod, code, out_text))
            if not args.keep_going:
                break

    print("\n=== summary ===")
    print(f"compiled {len(todo) - len(failures)}/{len(todo)} OK")
    for mod, code, text in failures:
        print(f"\n--- {mod} ({code}) ---")
        print("\n".join(text.splitlines()[:25]))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
