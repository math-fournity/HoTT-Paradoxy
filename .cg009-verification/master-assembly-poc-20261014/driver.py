#!/usr/bin/env python3
"""Master assembly PoC driver (2026-10-14).

Compiles the transitive closure of a target module inside the private
assembly tree, in topological order, from source, with fresh outputs.
Seeds from the 9276 devbuild olean cache where available (baseline files),
compiles everything else (the 40 migrated NL-chain files).

Evidence discipline: exit code + `#print axioms` from the logs.
"""
import os, re, subprocess, sys, time

ASM = "/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0/.cg009-verification/master-assembly-poc-20261014"
OUT = os.path.join(ASM, "build")
SEED = "/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0/.cg009-verification/master-verify-9276-20261014"
LEAN = "/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean"
ASTRA = "/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435"
FOUNDATION = "/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean"

TARGETS = ["GodelQ.ZFC.ShCraigElimSetupQ", "GodelQ.MasterAssemblyProbe"]

def src_path(mod):
    return os.path.join(ASM, mod.replace(".", "/") + ".lean")

def olean_in(root, mod):
    return os.path.join(root, mod.replace(".", "/") + ".olean")

def imports_of(mod):
    p = src_path(mod)
    if not os.path.exists(p):
        return []
    out = []
    for line in open(p, encoding="utf-8"):
        m = re.match(r'\s*import\s+(\S+)', line)
        if m:
            mod2 = m.group(1)
            # only local GodelQ modules matter for ordering
            if mod2.startswith("GodelQ."):
                out.append(mod2)
    return out

def closure(targets):
    seen, todo = set(), list(targets)
    while todo:
        cur = todo.pop()
        if cur in seen:
            continue
        seen.add(cur)
        if not os.path.exists(src_path(cur)):
            # external module (foundation/mathlib) — not our business
            continue
        todo.extend(imports_of(cur))
    return seen

def toposort(mods):
    mods = set(mods)
    deps = {m: [d for d in imports_of(m) if d in mods] for m in mods}
    order, done = [], set()
    while len(order) < len(mods):
        progressed = False
        for m in sorted(mods):
            if m in done:
                continue
            if all(d in done for d in deps[m]):
                order.append(m)
                done.add(m)
                progressed = True
        if not progressed:
            cyc = sorted(m for m in mods if m not in done)
            print("CYCLE among:", cyc, file=sys.stderr)
            for m in cyc:
                print(f"  {m} <- {deps[m]}", file=sys.stderr)
            sys.exit(2)
    return order

def main():
    os.makedirs(os.path.join(OUT, "GodelQ/ZFC"), exist_ok=True)
    mods = closure(TARGETS)
    print(f"closure: {len(mods)} local modules")
    order = toposort(mods)

    env = dict(os.environ)
    env["LEAN_SYSROOT"] = "/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/lib/lean"
    lp = [OUT, SEED, FOUNDATION]
    for p in ["batteries", "aesop", "Qq", "proofwidgets", "importGraph", "LeanSearchClient", "plausible", "Cli"]:
        lp.append(f"{ASTRA}/.lake/packages/{p}/.lake/build/lib/lean")
    env["LEAN_PATH"] = ":".join(lp)

    ok = skip = bad = 0
    failed = []
    t0 = time.time()
    for m in order:
        o = olean_in(OUT, m)
        if os.path.exists(o):
            skip += 1
            continue
        src = src_path(m)
        log = os.path.join(OUT, m.replace(".", "_") + ".log")
        with open(log, "w") as lf:
            try:
                r = subprocess.run([LEAN, f"--o={o}", "-R", ASM, src],
                                   stdout=lf, stderr=subprocess.STDOUT,
                                   env=env, timeout=300)
                rc = r.returncode
            except subprocess.TimeoutExpired:
                rc = 124
        txt = open(log, encoding="utf-8", errors="replace").read()
        if rc != 0 or "error:" in txt:
            bad += 1
            failed.append(m)
            errs = [l for l in txt.splitlines() if "error:" in l][:2]
            print(f"FAIL {m} rc={rc}")
            for e in errs:
                print("   ", e[:160])
        else:
            ok += 1
            print(f"ok   {m}")
    dt = time.time() - t0
    print(f"\n=== done: compiled={ok} skipped={skip} failed={bad} in {dt:.0f}s ===")
    if failed:
        print("failed:", " ".join(failed))
        sys.exit(1)

if __name__ == "__main__":
    main()
