#!/usr/bin/env python3
"""Development-only incremental Lean build for the Z0D3 package. Not a receipt tool.

Usage: devbuild_min.py <package-dir> <src1> [<src2> ...]
Same pinned Lean, network-denied sandbox and LEAN_PATH as the project's zfc_lean_check.py,
but keeps a persistent build dir and skips unchanged sources.
"""
import hashlib, json, subprocess, sys, time
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent / "_build"
pkg = Path(sys.argv[1]).resolve()
sources = sys.argv[2:]
toolchain = json.loads((pkg / "LEAN_TOOLCHAIN.json").read_text())
closure = json.loads((pkg / "MATHLIB_CLOSURE.json").read_text())
prefix = Path(toolchain["prefix"])
build = SCRATCH / pkg.name
build.mkdir(parents=True, exist_ok=True)
state_file = build / "_state.json"
state = json.loads(state_file.read_text()) if state_file.exists() else {}
options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
lean_path = ":".join([str(build)] + [str(p) for p in closure["lean_path"]])
env = {"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix),
      "LEAN_PATH": lean_path, "HOME": str(build)}
profile = "(version 1)(allow default)(deny network*)"
chain = hashlib.sha256()
rc = 0
for rel in sources:
    src = (pkg / rel).read_bytes()
    chain.update(rel.encode()); chain.update(hashlib.sha256(src).digest())
    key = chain.hexdigest()
    out = build / Path(rel).with_suffix("")
    if state.get(rel) == key and Path(str(out) + ".olean").exists():
        print(f"## skip {rel}")
        continue
    out.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    cmd = ["/usr/bin/sandbox-exec", "-p", profile, str(prefix / "bin" / "lean"), *options,
           "-R", ".", "-o", str(out) + ".olean", "-i", str(out) + ".ilean", rel]
    r = subprocess.run(cmd, cwd=pkg, env=env, capture_output=True)
    print(f"## lean {rel} ({time.time()-t0:.1f}s, exit {r.returncode})")
    sys.stdout.write(r.stdout.decode(errors="replace"))
    sys.stdout.write(r.stderr.decode(errors="replace"))
    if r.returncode != 0:
        state.pop(rel, None)
        rc = r.returncode
        break
    state[rel] = key
state_file.write_text(json.dumps(state, indent=1))
sys.exit(rc)
