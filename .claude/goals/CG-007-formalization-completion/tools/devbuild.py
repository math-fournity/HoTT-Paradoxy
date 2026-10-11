#!/usr/bin/env python3
"""CG-007 development-only incremental Lean build (NOT a receipt tool).

Compiles a list of package-relative Lean sources in order, using the pinned toolchain and
LEAN_PATH recorded in the package's own LEAN_TOOLCHAIN.json / MATHLIB_CLOSURE.json, inside a
network-denied sandbox.  A source is skipped when it and every source before it are unchanged
since the last successful run (chained SHA-256 over the ordered source list).

Usage:
    python3 -B devbuild.py <package-dir> <src1> [<src2> ...]

The build directory defaults to $CG007_BUILD_DIR, else <repo>/.cg007-build/<package-name>.
It is deliberately outside the package so that build artifacts never enter the receipts.
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit(__doc__)

pkg = Path(sys.argv[1]).resolve()
sources = sys.argv[2:]
toolchain = json.loads((pkg / "LEAN_TOOLCHAIN.json").read_text(encoding="utf-8"))
closure = json.loads((pkg / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))
prefix = Path(toolchain["prefix"])

# Build dir: outside the package, so nothing here can leak into a receipt.
default_root = pkg.parents[4] / ".cg007-build"
build = Path(os.environ.get("CG007_BUILD_DIR", default_root)) / pkg.name
build.mkdir(parents=True, exist_ok=True)
state_file = build / "_state.json"
state = json.loads(state_file.read_text(encoding="utf-8")) if state_file.exists() else {}

options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
lean_path = ":".join([str(build)] + [str(p) for p in closure["lean_path"]])
env = {
    "PATH": f"{prefix}/bin:/usr/bin:/bin",
    "LEAN_SYSROOT": str(prefix),
    "LEAN_PATH": lean_path,
    "HOME": str(build),
}
profile = "(version 1)(allow default)(deny network*)"

chain = hashlib.sha256()
rc = 0
for rel in sources:
    src = (pkg / rel).read_bytes()
    chain.update(rel.encode())
    chain.update(hashlib.sha256(src).digest())
    key = chain.hexdigest()
    out = build / Path(rel).with_suffix("")
    if state.get(rel) == key and Path(str(out) + ".olean").exists():
        print(f"## skip {rel}")
        continue
    out.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    cmd = ["/usr/bin/sandbox-exec", "-p", profile, str(prefix / "bin" / "lean"), *options,
           "-R", ".", "-o", str(out) + ".olean", "-i", str(out) + ".ilean", rel]
    r = subprocess.run(cmd, cwd=pkg, env=env, capture_output=True, check=False)
    print(f"## lean {rel} ({time.time() - t0:.1f}s, exit {r.returncode})")
    sys.stdout.write(r.stdout.decode(errors="replace"))
    sys.stdout.write(r.stderr.decode(errors="replace"))
    if r.returncode != 0:
        state.pop(rel, None)
        rc = r.returncode
        break
    state[rel] = key
state_file.write_text(json.dumps(state, indent=1), encoding="utf-8")
sys.exit(rc)
