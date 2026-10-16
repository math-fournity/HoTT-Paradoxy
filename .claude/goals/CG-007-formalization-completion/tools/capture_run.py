#!/usr/bin/env python3
"""Capture one CG-007 Lean run as an F-011 receipt (goal-local).

Copied from CG-006's capture_z0_run.py (itself a copy of the frozen capture_zfc_run.py); the only
changes are that the package path, the theory-variant text and the audit-session text are
arguments, plus the PINS_TOOL/SELF paths and this docstring.  The driver CG-006 zfc_lean_check.py
is reused unchanged (it takes the package as an argument).  Same receipt format
(formal-proof-run/v1: RUN.json, stdout.txt, stderr.txt, environment.txt, source-manifest.json), so
.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py checks and replays these runs as it
does the others.  The recorded command runs zfc_lean_check.py, which verifies the pinned Lean files
and every Foundation/Mathlib/dependency module digest in the import closure before compiling.

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-007-formalization-completion/tools/capture_run.py \
      --package HoTT/formal/claude-cg001/<package> \
      --run-id 2026MMDD-CG001-<NAME>-01 --proof-id MP-CG001-<NAME>-001 \
      --claim-id CG001-C-NNN [--claim-id ...] --expect ACCEPT|REJECT \
      --source GodelQ/<A>.lean [--source ... ; package-relative, build order, last = target] \
      --scope "..." [--non-goal "..."]... [--theory-variant "..."] [--audit-session "..."]
Exit code: 0 when the outcome matches --expect, 42 otherwise (receipt written either way).
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
DRIVER = Path(".claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py")
PINS_TOOL = Path(".claude/goals/CG-007-formalization-completion/tools/make_pins.py")
SELF = Path(".claude/goals/CG-007-formalization-completion/tools/capture_run.py")
DEFAULT_VARIANT = ("Lean 4 kernel with Mathlib and FormalizedFormalLogic/Foundation (classical); first-order ZFC over ℒₛₑₜ, "
                   "arithmetic, computability and abstract proof theory; never HoTT paths")


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
    parser.add_argument("--package", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--proof-id", required=True)
    parser.add_argument("--claim-id", action="append", required=True)
    parser.add_argument("--expect", choices=["ACCEPT", "REJECT"], required=True)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    parser.add_argument("--theory-variant", default=DEFAULT_VARIANT)
    parser.add_argument("--audit-session", default="Claude CG-007 line, Claude Code desktop session d58e0c0d, branch dev (main checkout), 2026-10-08")
    args = parser.parse_args()
    PACKAGE = safe_relative(args.package)
    if PACKAGE.parts[:3] != ("HoTT", "formal", "claude-cg001") or len(PACKAGE.parts) != 4:
        raise SystemExit(f"UNSAFE_PACKAGE:{args.package}")

    if "-CG001-" not in args.run_id:
        raise SystemExit("RUN_NOT_OWNED_BY_CG001")
    run_dir = ROOT / "HoTT/verification/runs" / args.run_id
    if run_dir.exists():
        raise SystemExit(f"RUN_ALREADY_EXISTS:{args.run_id}")

    toolchain = json.loads((ROOT / PACKAGE / "LEAN_TOOLCHAIN.json").read_text(encoding="utf-8"))
    closure = json.loads((ROOT / PACKAGE / "MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))
    prefix = Path(toolchain["prefix"])
    external = []
    for row in toolchain["pinned_files"]:
        path = prefix / row["relative_path"]
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"LEAN_TOOLCHAIN_FILE_MISMATCH:{row['relative_path']}")
        external.append({"label": f"lean-{row['relative_path']}", "local_path": str(path),
                         "bytes": len(data), "sha256": sha(data)})
    build_root = Path(closure["library_roots"]["foundation-build"])
    for row in closure["foundation_build"]["locally_built_files"]:
        if not row["path"].endswith((".olean", ".olean.private", ".olean.server")):
            continue
        path = build_root / row["path"]
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"FOUNDATION_BUILD_FILE_MISMATCH:{row['path']}")
        external.append({"label": f"foundation-build-{row['path']}", "local_path": str(path),
                         "bytes": len(data), "sha256": sha(data)})

    sources = [safe_relative(s) for s in args.source]
    files = [PACKAGE / s for s in sources] + [PACKAGE / "CLAIM.md", PACKAGE / "LEAN_TOOLCHAIN.json",
                                              PACKAGE / "MATHLIB_CLOSURE.json", DRIVER, PINS_TOOL, SELF]
    version = subprocess.run([str(prefix / "bin/lean"), "--version"], capture_output=True, check=True,
                             env={"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix)},
                             stdin=subprocess.DEVNULL).stdout.decode().strip()
    if version != toolchain["version_line"]:
        raise SystemExit("LEAN_VERSION_LINE_MISMATCH")
    argv = [sys.executable, "-B", DRIVER.as_posix(), "--package", PACKAGE.as_posix(),
            *[s.as_posix() for s in sources]]

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
        f"mathlib_source_commit={closure['mathlib_source']['commit']}",
        f"foundation_source_commit={closure['foundation_source']['commit']}",
        f"closure_modules={closure['module_count']}",
        f"closure_aggregate_sha256={closure['aggregate_sha256']}",
        f"theory_variant={args.theory_variant}",
        "dependency_policy=pinned toolchain files and per-module digests of the Foundation/Mathlib import closure checked by the driver before compilation; network denied by sandbox-exec; elan proxy not used",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
    ]) + "\n"

    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": [file_row(p) for p in files],
        "external_dependencies": external,
    }

    accepted = result.returncode == 0
    expected_accept = args.expect == "ACCEPT"
    out_text = result.stdout.decode("utf-8", errors="replace")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Lean 4",
        "proof_assistant_version": version,
        "theory_variant": args.theory_variant,
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": round(duration, 6),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "expected_outcome": args.expect,
        "outcome_matches_expectation": accepted == expected_accept,
        "scope": args.scope,
        "non_goals": args.non_goal,
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "stdout": artifact(run_dir, "stdout.txt", result.stdout),
        "stderr": artifact(run_dir, "stderr.txt", result.stderr),
        "environment": artifact(run_dir, "environment.txt", env_text.encode("utf-8")),
        "source_manifest": artifact(run_dir, "source-manifest.json", json_bytes(manifest)),
        "audit_session": args.audit_session,
        "audit_notes": [],
    }
    if not accepted:
        run["rejection_stage"] = "KERNEL_ERROR_IN_TARGET" if "(kernel)" in out_text else "ELABORATION_ERROR_IN_TARGET"
        run["status_vocabulary_note"] = ("KERNEL_REJECTED is the repository-wide status word for 'the proof checker rejected "
                                         "the target'. rejection_stage says which Lean stage refused it.")
    (run_dir / "RUN.json").write_bytes(json_bytes(run))
    print(json.dumps({"status": run["status"], "run_path": f"HoTT/verification/runs/{args.run_id}",
                      "exit_code": result.returncode, "matches": accepted == expected_accept,
                      "stdout_bytes": len(result.stdout), "stderr_bytes": len(result.stderr),
                      "source_files": len(manifest["files"]), "external": len(external)}))
    return 0 if accepted == expected_accept else 42


if __name__ == "__main__":
    raise SystemExit(main())
