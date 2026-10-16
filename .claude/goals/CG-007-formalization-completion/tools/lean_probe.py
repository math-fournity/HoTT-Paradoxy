#!/usr/bin/env python3
"""CG-007 single-file Lean probe (NOT a receipt tool).

Type-checks one scratch .lean file against the pinned toolchain and the already-built package
oleans, without touching the package or the receipts.

Usage:
    python3 -B lean_probe.py <package-dir> <probe.lean> [<extra .lean> ...]

The probe file may import any module already compiled by devbuild.py.  Exit code is lean's.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit(__doc__)

pkg = Path(sys.argv[1]).resolve()
probes = [Path(p).resolve() for p in sys.argv[2:]]
toolchain = json.loads((pkg / "LEAN_TOOLCHAIN.json").read_text(encoding="utf-8"))
closure = json.loads((pkg / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))
prefix = Path(toolchain["prefix"])

build_root = Path(os.environ.get("CG007_BUILD_DIR", pkg.parents[4] / ".cg007-build")) / pkg.name
options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
lean_path = ":".join([str(build_root)] + [str(p) for p in closure["lean_path"]])
env = {
    "PATH": f"{prefix}/bin:/usr/bin:/bin",
    "LEAN_SYSROOT": str(prefix),
    "LEAN_PATH": lean_path,
    "HOME": str(build_root),
}
profile = "(version 1)(allow default)(deny network*)"

rc = 0
for probe in probes:
    cmd = ["/usr/bin/sandbox-exec", "-p", profile, str(prefix / "bin" / "lean"), *options,
           "-R", str(pkg), str(probe)]
    r = subprocess.run(cmd, cwd=pkg, env=env, capture_output=True, check=False)
    print(f"## probe {probe.name} (exit {r.returncode})")
    sys.stdout.write(r.stdout.decode(errors="replace"))
    sys.stdout.write(r.stderr.decode(errors="replace"))
    if r.returncode != 0:
        rc = r.returncode
sys.exit(rc)
