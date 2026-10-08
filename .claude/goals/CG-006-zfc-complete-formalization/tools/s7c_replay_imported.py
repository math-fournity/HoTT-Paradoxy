#!/usr/bin/env python3
"""CG-006 S7-c: replay runs imported byte-identically from GPT branches into the dev worktree.
Re-executes each RUN.json command (old worktree path -> this worktree) in a no-network sandbox
and compares exit code, stdout, stderr exactly and after path normalization."""
import json, os, subprocess, sys, time, hashlib, pathlib
WT = sys.argv[1]; LIST = sys.argv[2]; OUT = sys.argv[3]
SANDBOX = ["/usr/bin/sandbox-exec", "-p", "(version 1)(allow default)(deny network*)"]
KEEP_ENV = ("XDG_DATA_HOME", "XDG_CONFIG_HOME", "TMPDIR", "LEAN_PATH", "LEAN_SYSROOT")
def sha(b): return hashlib.sha256(b).hexdigest()
results = []
for rel in [l.strip() for l in open(LIST) if l.strip()]:
    rd = pathlib.Path(WT, rel)
    rec = {"run": rd.name}
    try:
        d = json.loads((rd / "RUN.json").read_text(), strict=False)
    except FileNotFoundError:
        rec.update(result="NO_RUN_JSON"); results.append(rec); continue
    argv = d.get("command_argv"); old = d.get("cwd")
    rec.update(recorded_status=d.get("status"), recorded_exit=d.get("exit_code"), proof_id=d.get("proof_id"))
    # receipt integrity: recorded hashes of stdout/stderr/source-manifest
    integ = {}
    for k in ("stdout", "stderr", "source_manifest", "environment"):
        meta = d.get(k)
        if isinstance(meta, dict) and meta.get("path") and (rd / meta["path"]).exists():
            integ[k] = sha((rd / meta["path"]).read_bytes()) == meta.get("sha256")
    rec["receipt_hashes_match"] = integ
    if not argv or not old:
        rec.update(result="NOT_REPLAYABLE_NO_COMMAND"); results.append(rec); continue
    argv2 = [a.replace(old, WT) for a in argv]
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": os.environ.get("HOME", "/tmp"), "LANG": "en_US.UTF-8"}
    envtxt = (rd / "environment.txt")
    if envtxt.exists():
        for line in envtxt.read_text(errors="replace").splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                if k in KEEP_ENV: env[k] = v.replace(old, WT)
    t0 = time.time()
    p = subprocess.run(SANDBOX + argv2, cwd=WT, env=env, capture_output=True, timeout=3600)
    rec["seconds"] = round(time.time() - t0, 1)
    so = (rd / "stdout.txt").read_bytes() if (rd / "stdout.txt").exists() else b""
    se = (rd / "stderr.txt").read_bytes() if (rd / "stderr.txt").exists() else b""
    norm = lambda b: b.replace(old.encode(), WT.encode())
    rec["exit"] = p.returncode
    rec["exit_match"] = (p.returncode == d.get("exit_code"))
    rec["stdout_exact"] = p.stdout == so; rec["stderr_exact"] = p.stderr == se
    rec["stdout_norm"] = p.stdout == norm(so); rec["stderr_norm"] = p.stderr == norm(se)
    if rec["exit_match"] and rec["stdout_exact"] and rec["stderr_exact"]:
        rec["result"] = "EXACT_EXIT_STDOUT_STDERR_MATCH"
    elif rec["exit_match"] and rec["stdout_norm"] and rec["stderr_norm"]:
        rec["result"] = "MATCH_AFTER_WORKTREE_PATH_NORMALIZATION"
    else:
        rec["result"] = "MISMATCH"
        pathlib.Path(OUT).with_suffix("").mkdir(parents=True, exist_ok=True)
        base = pathlib.Path(OUT).with_suffix("")
        (base / f"{rd.name}.stdout").write_bytes(p.stdout); (base / f"{rd.name}.stderr").write_bytes(p.stderr)
    rec["replay_stdout_sha256"] = sha(p.stdout); rec["replay_stderr_sha256"] = sha(p.stderr)
    results.append(rec); print(rec["run"], rec["result"], rec.get("seconds"), flush=True)
json.dump({"worktree": WT, "sandbox": SANDBOX[2], "results": results}, open(OUT, "w"), ensure_ascii=False, indent=1)
