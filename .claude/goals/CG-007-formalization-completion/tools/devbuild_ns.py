#!/usr/bin/env python3
"""devbuild.py 的本地变体：去掉 sandbox-exec（当前宿主不允许嵌套沙箱）。

只用于开发迭代；正式收据仍必须用包内冻结的 zfc_lean_check.py（它带沙箱）。
用法与 devbuild.py 相同：devbuild_ns.py <package-dir> <src1> [<src2> ...]
"""
import hashlib, json, subprocess, sys, time
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent
pkg = Path(sys.argv[1]).resolve()
sources = sys.argv[2:]
toolchain = json.loads((pkg / "LEAN_TOOLCHAIN.json").read_text())
closure = json.loads((pkg / "MATHLIB_CLOSURE.json").read_text())
prefix = Path(toolchain["prefix"])
build = SCRATCH / "devbuild_ns" / pkg.name
build.mkdir(parents=True, exist_ok=True)
state_file = build / "_state.json"
state = json.loads(state_file.read_text()) if state_file.exists() else {}
options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
lean_path = ":".join([str(build)] + [str(p) for p in closure["lean_path"]])
env = {"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix),
       "LEAN_PATH": lean_path, "HOME": str(build)}
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
    cmd = [str(prefix / "bin" / "lean"), *options, "-R", ".",
           "-o", str(out) + ".olean", "-i", str(out) + ".ilean", rel]
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
