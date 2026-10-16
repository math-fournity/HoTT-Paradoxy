#!/usr/bin/env python3
"""Pinned development check; deliberately not an F-011/canonical receipt.

The frozen driver requires sandbox-exec, unavailable in this WorkBuddy host.
This tool checks the same pins and source restrictions, invokes Lean directly
with a minimal environment, and records that isolation difference explicitly.
It does not change the frozen driver or classify host failures as proof failures.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path("HoTT/formal/claude-cg001/godel-q-zfc-z0-full")
DRIVER = Path(".claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py")
BASE_RUN = Path("HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01/RUN.json")
SELF = Path(__file__).resolve().relative_to(ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def module_digest(root: Path, module: str) -> str:
    base = root.joinpath(*module.split("."))
    digest = hashlib.sha256()
    for suffix in (".olean", ".olean.private", ".olean.server"):
        path = Path(str(base) + suffix)
        if path.exists():
            digest.update(suffix.encode())
            digest.update(file_sha(path).encode())
    return digest.hexdigest()


def encode(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()


def file_row(relative: Path) -> dict:
    data = (ROOT / relative).read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True)
    parser.add_argument("--package", default=PACKAGE.as_posix())
    parser.add_argument("--standalone", action="store_true")
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--expect", choices=("ACCEPT", "REJECT"), default="ACCEPT")
    parser.add_argument("--error-marker", default="")
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("frozen_driver", ROOT / DRIVER)
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    package = driver.safe_relative(args.package)
    if package.parts[:2] != ("HoTT", "formal"):
        raise SystemExit("PACKAGE_OUTSIDE_PROOF_ROOT")
    target = driver.safe_relative(args.target)
    run_relative = driver.safe_relative(args.run_dir)
    if run_relative.parts[:3] != ("HoTT", "verification", "runs"):
        raise SystemExit("RUN_OUTSIDE_EVIDENCE_ROOT")
    run_dir = ROOT / run_relative
    if run_dir.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    toolchain = json.loads((ROOT / PACKAGE / "LEAN_TOOLCHAIN.json").read_text())
    closure = json.loads((ROOT / PACKAGE / "MATHLIB_CLOSURE.json").read_text())
    prefix = Path(toolchain["prefix"])
    for row in toolchain["pinned_files"]:
        path = prefix / row["relative_path"]
        if path.stat().st_size != row["bytes"] or file_sha(path) != row["sha256"]:
            raise SystemExit("LEAN_PIN_MISMATCH:" + row["relative_path"])
    print("TOOLCHAIN_PINS_OK", flush=True)
    roots = {k: Path(v) for k, v in closure["library_roots"].items()}
    for index, row in enumerate(closure["modules"]):
        if module_digest(roots[row["root"]], row["module"]) != row["digest"]:
            raise SystemExit("MODULE_PIN_MISMATCH:" + row["module"])
        if index % 400 == 0:
            print("PIN_CHECK " + str(index), flush=True)
    print("MODULE_PINS_OK " + str(len(closure["modules"])), flush=True)
    base = json.loads((ROOT / BASE_RUN).read_text())
    argv = base["command_argv"]
    sources = [] if args.standalone else [driver.safe_relative(x) for x in argv[argv.index("--package") + 2:]]
    sources.append(target)
    import re
    for rel in sources:
        text = (ROOT / package / rel).read_text()
        for word in driver.FORBIDDEN_WORDS:
            if re.search(r"\b" + word + r"\b", text):
                raise SystemExit("FORBIDDEN_SOURCE_MARKER:" + str(rel) + ":" + word)
        for pattern in driver.FORBIDDEN_PATTERNS:
            if re.search(pattern, text, flags=re.MULTILINE):
                raise SystemExit("FORBIDDEN_SOURCE_PATTERN:" + str(rel))
    build = ROOT / ".workbuddy-ai/builds/w8-direct" / package.name
    build.mkdir(parents=True, exist_ok=True)
    state_path = build / "state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    options = [f"-D{k}={v}" for k, v in closure["lean_options"].items()]
    env = {"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix),
           "LEAN_PATH": ":".join([str(build), *closure["lean_path"]]), "HOME": str(build)}
    version = subprocess.run([str(prefix / "bin/lean"), "--version"], env=env,
                             capture_output=True, check=True).stdout.decode().strip()
    if version != toolchain["version_line"]:
        raise SystemExit("LEAN_VERSION_MISMATCH")
    run_dir.mkdir(parents=True)
    started = datetime.now(timezone.utc)
    t0 = time.monotonic()
    stdout = bytearray()
    stderr = bytearray()
    chain = hashlib.sha256(encode({"toolchain": toolchain, "closure": closure}))
    commands = []
    exit_code = 0
    failed_source = None
    cache_count = 0
    for rel in sources:
        chain.update(rel.as_posix().encode())
        chain.update((ROOT / package / rel).read_bytes())
        key = chain.hexdigest()
        out = build / rel.with_suffix("")
        cached_out = build / (str(rel) + ".stdout")
        cached_err = build / (str(rel) + ".stderr")
        cmd = [str(prefix / "bin/lean"), *options, "-R", ".", "-o", str(out) + ".olean",
               "-i", str(out) + ".ilean", rel.as_posix()]
        commands.append(cmd)
        stdout.extend(("## lean " + rel.as_posix() + "\n").encode())
        cache_row = state.get(rel.as_posix(), {})
        olean = Path(str(out) + ".olean")
        if rel != target and cache_row.get("key") == key and olean.exists() and cached_out.exists() and cached_err.exists() and cache_row.get("olean_sha256") == sha(olean.read_bytes()):
            stdout.extend(cached_out.read_bytes())
            stderr.extend(cached_err.read_bytes())
            cache_count += 1
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(cmd, cwd=ROOT / PACKAGE, env=env, capture_output=True,
                                stdin=subprocess.DEVNULL, timeout=180)
        stdout.extend(result.stdout)
        stderr.extend(result.stderr)
        cached_out.write_bytes(result.stdout)
        cached_err.write_bytes(result.stderr)
        print(f"CHECK {rel} exit={result.returncode}", flush=True)
        if result.returncode:
            state.pop(rel.as_posix(), None)
            exit_code = result.returncode
            failed_source = rel.as_posix()
            break
        state[rel.as_posix()] = {"key": key, "olean_sha256": sha(olean.read_bytes())}
    state_path.write_bytes(encode(state))
    accepted = exit_code == 0 and b"sorryAx" not in stdout
    marker_ok = not args.error_marker or args.error_marker.encode() in stdout + stderr
    matches = accepted if args.expect == "ACCEPT" else (exit_code != 0 and failed_source == target.as_posix() and marker_ok)
    status = "DEVELOPMENT_LEAN_ACCEPTED" if accepted else "DEVELOPMENT_CHECK_FAILED"
    if args.expect == "REJECT" and matches:
        status = "DEVELOPMENT_NEGATIVE_CONTROL_REJECTED_AT_TARGET"
    files = [package / s for s in sources] + [PACKAGE / "LEAN_TOOLCHAIN.json", PACKAGE / "MATHLIB_CLOSURE.json", BASE_RUN, DRIVER, SELF]
    (run_dir / "stdout.txt").write_bytes(stdout)
    (run_dir / "stderr.txt").write_bytes(stderr)
    (run_dir / "source-manifest.json").write_bytes(encode({"files": [file_row(p) for p in files], "module_pins_checked": len(closure["modules"]), "closure_aggregate_sha256": closure["aggregate_sha256"]}))
    (run_dir / "environment.txt").write_text("\n".join(["platform=" + platform.platform(), "python=" + sys.executable, "lean=" + version, "isolation=direct invocation; no additional sandbox-exec; not F-011", "network_activity=no network commands or package manager invoked", "cached_dependency_count=" + str(cache_count)]) + "\n")
    (run_dir / "RUN.json").write_bytes(encode({"schema_version": "workbuddy-development-run/v1", "run_id": run_dir.name, "status": status, "exit_code": exit_code, "expected_outcome": args.expect, "outcome_matches_expectation": matches, "target": target.as_posix(), "failed_source": failed_source, "started_at_utc": started.isoformat(), "completed_at_utc": datetime.now(timezone.utc).isoformat(), "duration_seconds": round(time.monotonic() - t0, 3), "commands": commands, "cached_dependency_count": cache_count, "source_policy": "frozen driver restrictions, no proof placeholders", "pin_policy": "all toolchain files and closure module digests checked", "proof_gate_status": "NOT_F011_EXTRA_SANDBOX_UNAVAILABLE", "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED", "non_goals": ["No unconditional D3 or keyE proof", "No canonical receipt or publication claim"]}))
    print(encode({"status": status, "exit_code": exit_code, "matches": matches, "run_dir": str(run_dir), "failed_source": failed_source}).decode())
    return 0 if matches else 42


if __name__ == "__main__":
    raise SystemExit(main())
