#!/usr/bin/env python3
"""Parallel module builder for Foundation (and missing Mathlib modules) — CG-006.

Why this exists: Foundation (FormalizedFormalLogic/Foundation) pins exactly the
Mathlib commit of the project-owned Astra build (5ed29652, Lean v4.34.0).  Running
lake there would risk rebuilding (rewriting) the Astra oleans that CG-005's runs
pin by hash.  This tool instead compiles, with the pinned Lean binary by absolute
path inside a network-denied sandbox, only the modules that have no olean yet, in
dependency order and in parallel, into a separate build tree whose Mathlib part
is a symlink mirror of the existing builds.

Usage:
  python3 -B ffl_build.py --build <dir> [--jobs N] <Target.Module> [...]
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

PREFIX = Path("/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0")
FOUNDATION = Path("/Volumes/D/HoTT-toolchain-cache/foundation-src")
ASTRA = Path("/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435")
CG005_OVERLAY = Path("/Volumes/D/HoTT-toolchain-cache/godel-q-mathlib-ext-v4.34.0/lib/lean")
PACKAGES = {"Batteries": "batteries", "Aesop": "aesop", "Qq": "Qq", "ProofWidgets": "proofwidgets",
            "ImportGraph": "importGraph", "LeanSearchClient": "LeanSearchClient", "Plausible": "plausible"}
CORE = ("Init", "Lean", "Std", "Lake")
IMPORT_RE = re.compile(r"^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z][\w\.]*)", re.MULTILINE)
MATHLIB_OPTS = ["-DautoImplicit=false", "-DmaxSynthPendingDepth=3", "-Dpp.unicode.fun=true"]
FOUNDATION_OPTS = ["-DautoImplicit=false", "-Dpp.unicode.fun=true"]
PROFILE = "(version 1)(allow default)(deny network*)"


def source_of(module: str) -> Path | None:
    top = module.split(".")[0]
    if top == "Foundation":
        base = FOUNDATION
    elif top == "Mathlib":
        base = ASTRA
    elif top in PACKAGES:
        base = ASTRA / ".lake/packages" / PACKAGES[top]
    else:
        return None
    path = base.joinpath(*module.split(".")).with_suffix(".lean")
    return path if path.exists() else None


def imports(path: Path) -> list[str]:
    """Imports from the file header only (Lean requires imports before any other command)."""
    text = re.sub(r"/-.*?-/", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
    found = []
    for line in text.splitlines():
        s = line.split("--", 1)[0].strip()
        if not s or s in ("module", "prelude"):
            continue
        m = re.match(r"^(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?(.+)$", s)
        if not m:
            break
        found += [w for w in m.group(1).split() if re.match(r"^[A-Za-z][\w\.]*$", w)]
    return found


def mirror(build_lib: Path) -> None:
    """Symlink every existing Mathlib artifact (resolved to its real file) into build_lib."""
    src = CG005_OVERLAY / "Mathlib"
    for dirpath, _, files in os.walk(src):
        rel = os.path.relpath(dirpath, src)
        out = build_lib / "Mathlib" / rel
        out.mkdir(parents=True, exist_ok=True)
        for name in files:
            target = out / name
            if not target.exists() and not target.is_symlink():
                target.symlink_to(os.path.realpath(os.path.join(dirpath, name)))
    for name in os.listdir(CG005_OVERLAY):
        p = CG005_OVERLAY / name
        if p.is_file() or p.is_symlink():
            t = build_lib / name
            if not t.exists() and not t.is_symlink():
                t.symlink_to(os.path.realpath(p))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", required=True)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("targets", nargs="+")
    args = ap.parse_args()
    build_lib = Path(args.build) / "lib/lean"
    build_lib.mkdir(parents=True, exist_ok=True)
    mirror(build_lib)
    pkg_libs = [ASTRA / ".lake/packages" / p / ".lake/build/lib/lean" for p in PACKAGES.values()]
    lean_path = ":".join([str(build_lib)] + [str(p) for p in pkg_libs])

    deps: dict[str, list[str]] = {}
    stack = list(args.targets)
    while stack:
        m = stack.pop()
        if m in deps or m.split(".")[0] in CORE:
            continue
        src = source_of(m)
        if src is None:
            raise SystemExit(f"NO_SOURCE:{m}")
        deps[m] = [i for i in imports(src) if i.split(".")[0] not in CORE]
        stack += deps[m]

    def have_olean(m: str) -> bool:
        top = m.split(".")[0]
        if top in PACKAGES:
            return (ASTRA / ".lake/packages" / PACKAGES[top] / ".lake/build/lib/lean").joinpath(*m.split(".")).with_suffix(".olean").exists()
        return build_lib.joinpath(*m.split(".")).with_suffix(".olean").exists()

    todo = {m for m in deps if not have_olean(m)}
    print(f"closure={len(deps)} to_compile={len(todo)}", flush=True)
    done: set[str] = set()
    failed: dict[str, str] = {}
    lock = threading.Lock()
    env = {"PATH": f"{PREFIX}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(PREFIX), "LEAN_PATH": lean_path,
           "HOME": str(Path(args.build))}

    def compile_one(m: str) -> tuple[str, int, float, str]:
        src = source_of(m)
        top = m.split(".")[0]
        root = FOUNDATION if top == "Foundation" else (ASTRA if top == "Mathlib" else ASTRA / ".lake/packages" / PACKAGES[top])
        out = build_lib.joinpath(*m.split("."))
        out.parent.mkdir(parents=True, exist_ok=True)
        opts = FOUNDATION_OPTS if top == "Foundation" else MATHLIB_OPTS
        cmd = ["/usr/bin/sandbox-exec", "-p", PROFILE, str(PREFIX / "bin/lean"), *opts, "-R", str(root),
               "-o", str(out) + ".olean", "-i", str(out) + ".ilean", str(src)]
        t0 = time.time()
        r = subprocess.run(cmd, env=env, capture_output=True, text=True)
        return m, r.returncode, time.time() - t0, (r.stdout + r.stderr)[-4000:]

    pending = set(todo)
    running: dict[cf.Future, str] = {}
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        while pending or running:
            ready = [m for m in sorted(pending)
                     if all((d not in todo) or (d in done) for d in deps[m])
                     and not any(d in failed for d in deps[m])]
            blocked = [m for m in pending if any(d in failed for d in deps[m])]
            for m in blocked:
                pending.discard(m)
                failed[m] = "BLOCKED_BY_FAILED_DEPENDENCY"
            for m in ready:
                if len(running) >= args.jobs:
                    break
                pending.discard(m)
                running[pool.submit(compile_one, m)] = m
            if not running:
                if pending:
                    print("DEADLOCK", sorted(pending)[:5], flush=True)
                    return 2
                break
            finished, _ = cf.wait(list(running), return_when=cf.FIRST_COMPLETED)
            for fut in finished:
                m, rc, dt, log = fut.result()
                del running[fut]
                with lock:
                    if rc == 0:
                        done.add(m)
                        print(f"ok {dt:6.1f}s {m}", flush=True)
                    else:
                        failed[m] = log
                        print(f"FAIL rc={rc} {m}\n{log}", flush=True)
    print(f"compiled={len(done)} failed={len([f for f in failed.values() if f != 'BLOCKED_BY_FAILED_DEPENDENCY'])} blocked={len([f for f in failed.values() if f == 'BLOCKED_BY_FAILED_DEPENDENCY'])}", flush=True)
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
