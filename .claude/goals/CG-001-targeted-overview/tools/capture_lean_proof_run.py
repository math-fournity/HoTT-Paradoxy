#!/usr/bin/env python3
"""Capture one pinned Lean 4 proof run as an F-011 receipt (CG-001, goal-local).

Why this exists: the pedometer ablation (C-49 to C-53) asks for more than one
proof system.  Lean 4 serves as an independent second kernel for set-level
model statements (never for HoTT paths: Lean's equality has uniqueness of
identity proofs).  This tool writes the same receipt format as the Agda and Rzk
capture tools (formal-proof-run/v1: RUN.json, stdout.txt, stderr.txt,
environment.txt, source-manifest.json), so verify_cg001_run.py checks and
replays Lean runs exactly as it does the others.  The recorded command runs
lean_check.py, which compiles the sources in order with the pinned toolchain
(HoTT/formal/claude-cg001/pedometer-ablation-lean/LEAN_TOOLCHAIN.json) and,
with --leanchecker, replays the last module in a fresh kernel environment.

Usage:
  python3 .claude/goals/CG-001-targeted-overview/tools/capture_lean_proof_run.py \
      --run-id 20260925-CG001-<NAME>-01 --proof-id MP-CG001-<NAME>-001 \
      --claim-id CG001-C-NN --source HoTT/formal/claude-cg001/<pkg>/<File>.lean \
      [--source <more, in build order; the last is the target>] [--leanchecker] \
      --manifest-file HoTT/formal/claude-cg001/<pkg>/CLAIM.md \
      --scope "..." [--non-goal "..."]...
Exit code: 0 when every step succeeds, 42 when a step fails (receipt written either way).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[4]
TOOLCHAIN = Path("HoTT/formal/claude-cg001/pedometer-ablation-lean/LEAN_TOOLCHAIN.json")
DRIVER = Path(".claude/goals/CG-001-targeted-overview/tools/lean_check.py")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def file_row(relative: Path) -> dict[str, object]:
    data = (ROOT / relative).read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def artifact(run_dir: Path, name: str, data: bytes) -> dict[str, object]:
    (run_dir / name).write_bytes(data)
    return {"path": name, "bytes": len(data), "sha256": sha(data)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--proof-id", required=True)
    parser.add_argument("--claim-id", action="append", required=True)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--leanchecker", action="store_true")
    parser.add_argument("--manifest-file", action="append", default=[])
    parser.add_argument("--scope", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    args = parser.parse_args()

    if "-CG001-" not in args.run_id:
        raise SystemExit("RUN_NOT_OWNED_BY_CG001")
    run_dir = ROOT / "HoTT/verification/runs" / args.run_id
    if run_dir.exists():
        raise SystemExit(f"RUN_ALREADY_EXISTS:{args.run_id}")

    toolchain = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    prefix = Path(toolchain["prefix"])
    external = []
    for row in toolchain["pinned_files"]:
        path = prefix / row["relative_path"]
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"LEAN_TOOLCHAIN_FILE_MISMATCH:{row['relative_path']}")
        external.append({"label": f"lean-{row['relative_path']}", "local_path": str(path),
                         "bytes": len(data), "sha256": sha(data)})

    sources = [safe_relative(s) for s in args.source]
    extra = [safe_relative(s) for s in args.manifest_file] + [TOOLCHAIN, DRIVER]
    version = subprocess.run([str(prefix / "bin/lean"), "--version"], capture_output=True, check=True,
                             env={"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix)},
                             stdin=subprocess.DEVNULL).stdout.decode().strip()
    if version != toolchain["version_line"]:
        raise SystemExit("LEAN_VERSION_LINE_MISMATCH")
    argv = [sys.executable, "-B", DRIVER.as_posix(), "--toolchain", TOOLCHAIN.as_posix(),
            *(["--leanchecker"] if args.leanchecker else []), *[s.as_posix() for s in sources]]

    run_dir.mkdir(parents=True)
    started = datetime.now(timezone.utc)
    t0 = time.monotonic()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, stdin=subprocess.DEVNULL, check=False)
    duration = time.monotonic() - t0
    completed = datetime.now(timezone.utc)

    env_text = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"python_executable={sys.executable}",
        f"lean_prefix={prefix}",
        f"lean_version={version}",
        f"leanchecker_fresh_replay={'yes' if args.leanchecker else 'no'}",
        "theory_variant=Lean 4 kernel; set-level model statements only (equality has UIP; no HoTT paths)",
        "dependency_policy=pinned toolchain files by SHA-256 (launchers, shared libraries, Init.olean, Init/Prelude.olean); minimal environment, elan proxy not used",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
    ]) + "\n"

    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": [file_row(p) for p in [*sources, *extra]],
        "external_dependencies": external,
    }

    accepted = result.returncode == 0
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Lean 4",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 kernel; set-level model statements only",
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": round(duration, 6),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": args.scope,
        "non_goals": args.non_goal,
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "stdout": artifact(run_dir, "stdout.txt", result.stdout),
        "stderr": artifact(run_dir, "stderr.txt", result.stderr),
        "environment": artifact(run_dir, "environment.txt", env_text.encode("utf-8")),
        "source_manifest": artifact(run_dir, "source-manifest.json", json_bytes(manifest)),
    }
    (run_dir / "RUN.json").write_bytes(json_bytes(run))
    print(json.dumps({"status": run["status"], "run_path": f"HoTT/verification/runs/{args.run_id}",
                      "exit_code": result.returncode, "stdout_bytes": len(result.stdout),
                      "stderr_bytes": len(result.stderr), "source_files": len(manifest["files"])}))
    return 0 if accepted else 42


if __name__ == "__main__":
    raise SystemExit(main())
