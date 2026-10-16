#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portable replay of the proof runs recorded in this branch.

Every directory HoTT/verification/runs/<run-id>/ holds a receipt (RUN.json, stdout.txt, stderr.txt,
environment.txt, source-manifest.json) written when the run was captured.  The receipts record absolute
paths of the capturing machine, so they are evidence of what ran, not commands you can paste.  This script
rebuilds each command with paths relative to the repository root and your own toolchain, runs it, and
compares the result with the receipt:

* outcome class: accepted (exit 0) or rejected (non-zero), as recorded;
* output: stdout normalized (repository root, cubical library root and Lean library root replaced by
  placeholders, trailing spaces dropped) compared line by line with the recorded stdout.

A negative control passes only if it is rejected again; with matching output it is rejected for the
recorded reason.

Toolchain (versions used for the receipts):
* Agda 2.8.0 with the cubical library v0.9 (Cubical Agda);
* Lean 4.34.0, core only (no Mathlib), for the runs captured by lean_check.py;
* Lean 4.34.0 with compiled libraries, for the runs captured by zfc_lean_check.py or godelq_lean_check.py
  (packages that import Mathlib or Foundation): FormalizedFormalLogic/Foundation at commit 1fb01b72, which pins
  Lean 4.34.0 and Mathlib 5ed29652.  In a checkout of that commit run `lake exe cache get` (Mathlib's prebuilt
  modules) and `lake build`; the receipts were made against the same commits, built on the capturing machine.
Give the paths with options or environment variables:
  --agda / AGDA                 the agda executable
  --cubical-lib / CUBICAL_LIB   the file cubical.agda-lib of cubical v0.9
  --lean-sysroot / LEAN_SYSROOT the Lean toolchain prefix (it contains bin/lean and bin/leanchecker)
  --foundation-root / FOUNDATION_ROOT
                                a built Foundation checkout; its .lake/build/lib/lean and the
                                .lake/packages/*/.lake/build/lib/lean of its dependencies (Mathlib among them)
                                become the library path
  --lean-lib DIR                a compiled library directory to add to the library path (repeatable), instead of
                                or in addition to --foundation-root
If your Agda keeps its data files in a non-default place, set XDG_DATA_HOME as you would for Agda itself.

Usage (from anywhere; paths are resolved against the repository root):
  python3 tools/replay.py --list
  python3 tools/replay.py [--jobs N] [--only SUBSTRING ...] [--json REPORT.json]
  python3 tools/replay.py --only 20260930-CG001-QUESTIONING-DELAY-MACOS-01

Each job works in its own temporary copy of HoTT/formal and of the cubical library, so parallel jobs never
write the same interface file.  Exit status: 0 when every selected run reproduces its recorded outcome class,
1 otherwise (2 for usage errors).  Runs whose toolchain is not given are reported as SKIPPED.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path, PurePosixPath

def find_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in [here] + list(here.parents):
        if (candidate / "HoTT/verification/runs").is_dir():
            return candidate
    raise SystemExit("cannot find the repository root (no HoTT/verification/runs above this script)")


ROOT = find_root()
RUNS = ROOT / "HoTT/verification/runs"
FORBIDDEN_LEAN = ("sorry", "admit", "native_decide", "unsafe", "implemented_by", "extern", "opaque")
FORBIDDEN_LEAN_PATTERNS = (r"^\s*(private\s+|protected\s+)?axiom\b", r"debug\.skipKernelTC", r"ofReduceBool", r"reduceBool")


def load_runs() -> list[dict]:
    runs = []
    for run_json in sorted(RUNS.glob("*/RUN.json")):
        try:
            record = json.loads(run_json.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if not isinstance(record, dict):
            continue
        record.setdefault("run_id", run_json.parent.name)
        record["_dir"] = run_json.parent
        record["_supported"] = isinstance(record.get("exit_code"), int) and isinstance(record.get("command_argv"), list)
        runs.append(record)
    return runs


LIB_TOOLS = ("zfc_lean_check.py", "godelq_lean_check.py")


def kind(record: dict) -> str:
    if any(str(a).endswith(LIB_TOOLS) for a in record.get("command_argv") or []):
        return "lean-lib"
    return "lean" if "lean" in str(record.get("proof_assistant", "")).lower() else "agda"


def safe_relative(value: str) -> str:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ValueError(f"UNSAFE_PATH:{value}")
    return path.as_posix()


def agda_plan(record: dict) -> dict:
    argv = [str(a) for a in record["command_argv"]]
    cwd = str(record.get("cwd", "")).rstrip("/")
    start = next(i for i, a in enumerate(argv) if a.rsplit("/", 1)[-1] == "agda")
    flags, includes = [], []
    rest = argv[start + 1:]
    target = safe_relative(rest[-1])
    i = 0
    while i < len(rest) - 1:
        a = rest[i]
        if a.startswith("--library-file="):
            i += 1
            continue
        if a == "-i":
            value = rest[i + 1]
            if value.startswith(cwd + "/"):
                value = value[len(cwd) + 1:]
            includes.append(safe_relative(value))
            i += 2
            continue
        if a == "-l":
            flags += [a, rest[i + 1]]
            i += 2
            continue
        flags.append(a)
        i += 1
    return {"flags": flags, "includes": includes, "target": target, "recorded_root": cwd}


def lean_plan(record: dict) -> dict:
    argv = [str(a) for a in record["command_argv"]]
    start = next(i for i, a in enumerate(argv) if a.endswith("lean_check.py"))
    rest = argv[start + 1:]
    leanchecker, sources, i = False, [], 0
    while i < len(rest):
        a = rest[i]
        if a == "--toolchain":
            i += 2
            continue
        if a == "--leanchecker":
            leanchecker = True
            i += 1
            continue
        sources.append(safe_relative(a))
        i += 1
    return {"sources": sources, "leanchecker": leanchecker, "recorded_root": str(record.get("cwd", "")).rstrip("/")}


def lean_lib_plan(record: dict) -> dict:
    """zfc_lean_check.py / godelq_lean_check.py: --package <dir> <sources relative to the package, in order>."""
    argv = [str(a) for a in record["command_argv"]]
    start = next(i for i, a in enumerate(argv) if a.endswith(LIB_TOOLS))
    rest = argv[start + 1:]
    package, sources, i = None, [], 0
    while i < len(rest):
        if rest[i] == "--package":
            package = safe_relative(rest[i + 1])
            i += 2
            continue
        sources.append(safe_relative(rest[i]))
        i += 1
    if package is None or not sources:
        raise ValueError("LEAN_LIB_COMMAND_UNREADABLE")
    return {"package": package, "sources": sources}


def library_dirs(opts: argparse.Namespace) -> list[str]:
    dirs = [Path(d) for d in (opts.lean_lib or [])]
    if opts.foundation_root:
        root = Path(opts.foundation_root)
        dirs.append(root / ".lake/build/lib/lean")
        packages = root / ".lake/packages"
        if packages.is_dir():
            dirs += sorted(p / ".lake/build/lib/lean" for p in packages.iterdir() if (p / ".lake/build/lib/lean").is_dir())
    return [str(d.resolve()) for d in dirs if d.is_dir()]


def normalize(text: str, roots: list[str]) -> list[str]:
    out = []
    for line in text.splitlines():
        for root in roots:
            if root:
                line = line.replace(root, "<REPO>")
        line = re.sub(r"/[^\s()]*?/cubical(?=/Cubical/)", "<CUBICAL>", line)
        line = re.sub(r"/[^\s()]*?/lib/lean(?=[/\s]|$)", "<LEANLIB>", line)
        out.append(line.rstrip())
    return out


def run_agda(record: dict, opts: argparse.Namespace, work: Path) -> tuple[int, str, str]:
    plan = agda_plan(record)
    repo = work / "repo"
    shutil.copytree(ROOT / "HoTT/formal", repo / "HoTT/formal")
    lib_src = Path(opts.cubical_lib).resolve().parent
    lib_copy = work / "cubical-lib" / lib_src.name
    shutil.copytree(lib_src, lib_copy, ignore=shutil.ignore_patterns("_build"))
    libraries = work / "libraries"
    libraries.write_text(str(lib_copy / Path(opts.cubical_lib).name) + "\n", encoding="utf-8")
    flags = [f for f in plan["flags"] if not (opts.use_interfaces and f == "--ignore-interfaces")]
    argv = [opts.agda] + flags + [f"--library-file={libraries}"]
    for inc in plan["includes"]:
        argv += ["-i", str(repo / inc)]
    argv.append(plan["target"])
    env = dict(os.environ)
    env["TMPDIR"] = str(work / "tmp")
    (work / "tmp").mkdir(exist_ok=True)
    result = subprocess.run(argv, cwd=repo, env=env, capture_output=True, stdin=subprocess.DEVNULL,
                            timeout=opts.timeout, check=False)
    text = result.stdout.decode("utf-8", "replace").replace(str(repo), "<REPO>")
    return result.returncode, text, result.stderr.decode("utf-8", "replace")


def run_lean(record: dict, opts: argparse.Namespace, work: Path) -> tuple[int, str, str]:
    plan = lean_plan(record)
    prefix = Path(opts.lean_sysroot)
    repo = work / "repo"
    shutil.copytree(ROOT / "HoTT/formal", repo / "HoTT/formal")
    for rel in plan["sources"]:
        text = (repo / rel).read_text(encoding="utf-8")
        bad = [w for w in FORBIDDEN_LEAN if re.search(rf"\b{w}\b", text)]
        bad += [p for p in FORBIDDEN_LEAN_PATTERNS if re.search(p, text, flags=re.MULTILINE)]
        if bad:
            return 99, f"LEAN_FORBIDDEN_MARKER:{rel}:{bad}\n", ""
    build = work / "lean-build"
    build.mkdir()
    env = {"HOME": os.environ.get("HOME", "/"), "PATH": f"{prefix}/bin:/usr/bin:/bin",
           "LEAN_SYSROOT": str(prefix), "LEAN_PATH": str(build)}
    out, err = [], []
    for rel in plan["sources"]:
        argv = [str(prefix / "bin/lean"), "-R", PurePosixPath(rel).parent.as_posix(),
                "-o", str(build / f"{PurePosixPath(rel).stem}.olean"), rel]
        r = subprocess.run(argv, cwd=repo, env=env, capture_output=True, stdin=subprocess.DEVNULL,
                           timeout=opts.timeout, check=False)
        out.append(f"## lean {rel}\n" + r.stdout.decode("utf-8", "replace"))
        err.append(r.stderr.decode("utf-8", "replace"))
        if r.returncode != 0:
            out.append(f"## exit {r.returncode}\n")
            return r.returncode, "".join(out), "".join(err)
    if plan["leanchecker"]:
        module = PurePosixPath(plan["sources"][-1]).stem
        r = subprocess.run([str(prefix / "bin/leanchecker"), "--fresh", module], cwd=repo, env=env,
                           capture_output=True, stdin=subprocess.DEVNULL, timeout=opts.timeout, check=False)
        out.append(f"## leanchecker --fresh {module}\n" + r.stdout.decode("utf-8", "replace"))
        err.append(r.stderr.decode("utf-8", "replace"))
        if r.returncode != 0:
            out.append(f"## exit {r.returncode}\n")
            return r.returncode, "".join(out), "".join(err)
    out.append("## exit 0\n")
    return 0, "".join(out), "".join(err)


def run_lean_lib(record: dict, opts: argparse.Namespace, work: Path) -> tuple[int, str, str]:
    """The steps of zfc_lean_check.py / godelq_lean_check.py with your own toolchain and libraries: compile the
    sources in order inside the package directory into a temporary build directory, each step preceded by the
    header line `## lean <source>`; stop at the first failure.  (The capture tools also checked the hashes of the
    toolchain files and of every compiled library module, recorded in the package's LEAN_TOOLCHAIN.json and
    MATHLIB_CLOSURE.json; your own build has other bytes, so that check is not repeated here.)"""
    plan = lean_lib_plan(record)
    prefix = Path(opts.lean_sysroot)
    repo = work / "repo"
    shutil.copytree(ROOT / "HoTT/formal", repo / "HoTT/formal")
    package = repo / plan["package"]
    closure = json.loads((package / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))
    options = [f"-D{k}={v}" for k, v in closure.get("lean_options", {}).items()]
    for rel in plan["sources"]:
        text = (package / rel).read_text(encoding="utf-8")
        bad = [w for w in FORBIDDEN_LEAN if re.search(rf"\b{w}\b", text)]
        bad += [p for p in FORBIDDEN_LEAN_PATTERNS if re.search(p, text, flags=re.MULTILINE)]
        if bad:
            return 99, f"LEAN_FORBIDDEN_MARKER:{rel}:{bad}\n", ""
    build = work / "lean-build"
    build.mkdir()
    env = {"HOME": str(build), "PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix),
           "LEAN_PATH": ":".join([str(build)] + library_dirs(opts))}
    out, err = [], []
    for rel in plan["sources"]:
        target = build / PurePosixPath(rel).with_suffix("")
        target.parent.mkdir(parents=True, exist_ok=True)
        argv = [str(prefix / "bin/lean"), *options, "-R", ".", "-o", f"{target}.olean", "-i", f"{target}.ilean", rel]
        r = subprocess.run(argv, cwd=package, env=env, capture_output=True, stdin=subprocess.DEVNULL,
                           timeout=opts.timeout, check=False)
        out.append(f"## lean {rel}\n" + r.stdout.decode("utf-8", "replace"))
        err.append(r.stderr.decode("utf-8", "replace"))
        if r.returncode != 0:
            return r.returncode, "".join(out), "".join(err)
    return 0, "".join(out), "".join(err)


def replay_one(record: dict, opts: argparse.Namespace) -> dict:
    run_id = record["run_id"]
    k = kind(record)
    expected_exit = int(record["exit_code"])
    row = {"run_id": run_id, "kind": k, "recorded_status": record.get("status"), "recorded_exit": expected_exit,
           "expected": "accepted" if expected_exit == 0 else "rejected"}
    if (k == "agda" and not (opts.agda and opts.cubical_lib)) or (k == "lean" and not opts.lean_sysroot):
        row.update(result="SKIPPED", reason="toolchain not given")
        return row
    if k == "lean-lib" and not (opts.lean_sysroot and library_dirs(opts)):
        row.update(result="SKIPPED", reason="Lean toolchain or Foundation/Mathlib build not given")
        return row
    started = time.time()
    with tempfile.TemporaryDirectory(prefix="replay-") as tmp:
        try:
            runner = {"agda": run_agda, "lean": run_lean, "lean-lib": run_lean_lib}[k]
            code, out, err = runner(record, opts, Path(tmp).resolve())
        except subprocess.TimeoutExpired:
            row.update(result="FAIL", reason=f"timeout after {opts.timeout} s", seconds=round(time.time() - started, 1))
            return row
    recorded_out = (record["_dir"] / "stdout.txt").read_text(encoding="utf-8", errors="replace")
    roots = [record.get("cwd", "").rstrip("/")]
    same_class = (code == 0) == (expected_exit == 0)
    same_out = normalize(out, roots) == normalize(recorded_out, roots)
    row.update(actual_exit=code, same_outcome_class=same_class, same_normalized_stdout=same_out,
               seconds=round(time.time() - started, 1))
    if not same_class:
        row["result"] = "FAIL"
        row["stdout_tail"] = out[-1200:]
    else:
        row["result"] = "PASS" if same_out else "PASS_OUTCOME_ONLY"
        if not same_out:
            a, b = normalize(out, roots), normalize(recorded_out, roots)
            row["first_stdout_difference"] = next(([i, x, y] for i, (x, y) in enumerate(zip(a, b)) if x != y),
                                                  [min(len(a), len(b)), len(a), len(b)])
    return row


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agda", default=os.environ.get("AGDA"))
    ap.add_argument("--cubical-lib", default=os.environ.get("CUBICAL_LIB"))
    ap.add_argument("--lean-sysroot", default=os.environ.get("LEAN_SYSROOT"))
    ap.add_argument("--foundation-root", default=os.environ.get("FOUNDATION_ROOT"),
                    help="a built Foundation checkout (commit 1fb01b72); its library and its dependencies' libraries are used")
    ap.add_argument("--lean-lib", action="append", default=[],
                    help="a compiled Lean library directory to add to the library path; repeatable")
    ap.add_argument("--only", action="append", default=[], help="run ids containing this text (or a glob); repeatable")
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--timeout", type=int, default=1800, help="seconds per run")
    ap.add_argument("--use-interfaces", action="store_true",
                    help="drop --ignore-interfaces (faster, but not the recorded command)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--json", help="write a JSON report here")
    opts = ap.parse_args(argv)

    runs = load_runs()
    if opts.only:
        runs = [r for r in runs if any((pat in r["run_id"]) or fnmatch.fnmatch(r["run_id"], pat) for pat in opts.only)]
    if opts.list:
        for r in runs:
            if not r["_supported"]:
                print(f"{r['run_id']}\tunsupported receipt format")
                continue
            print(f"{r['run_id']}\t{kind(r)}\t{'accepted' if r['exit_code'] == 0 else 'rejected'}\t{r.get('status')}")
        return 0
    unsupported = [r["run_id"] for r in runs if not r["_supported"]]
    if unsupported:
        print(f"skipping {len(unsupported)} receipts in an older format: {', '.join(unsupported[:5])}"
              + (" …" if len(unsupported) > 5 else ""), file=sys.stderr)
    runs = [r for r in runs if r["_supported"]]
    if not runs:
        print("no runs selected", file=sys.stderr)
        return 2
    if opts.use_interfaces:
        print("note: --use-interfaces drops --ignore-interfaces; outcomes should agree, stdout will not", file=sys.stderr)
    rows = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, opts.jobs)) as pool:
        futures = {pool.submit(replay_one, r, opts): r["run_id"] for r in runs}
        for fut in concurrent.futures.as_completed(futures):
            row = fut.result()
            rows.append(row)
            print(f"{row['result']:<17} {row['run_id']}  expected {row['expected']}"
                  + (f", exit {row.get('actual_exit')}, {row.get('seconds')} s" if "actual_exit" in row else ""), flush=True)
    rows.sort(key=lambda r: r["run_id"])
    counts: dict = {}
    for r in rows:
        counts[r["result"]] = counts.get(r["result"], 0) + 1
    print("SUMMARY", json.dumps(counts, sort_keys=True))
    if opts.json:
        Path(opts.json).write_text(json.dumps({"root": str(ROOT), "counts": counts, "runs": rows},
                                              ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 1 if counts.get("FAIL") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
