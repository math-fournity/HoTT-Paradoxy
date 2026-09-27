#!/usr/bin/env python3
"""Capture one pinned Lean 4 run as an F-011 receipt (Cloud-Opus audit, 2026-09-27).

Purpose: replay Opus's Lean contrast CG001-C-72 ("in Lean 4, with UIP, the
universe is a set") on the Linux Lean 4.34.0 release asset, which has the same
source commit as the macOS toolchain of the original runs.

Built on the CG-001 goal-local capture tool
(.claude/goals/CG-001-targeted-overview/tools/capture_lean_proof_run.py, which
is read-only for this session and hard-wires the macOS toolchain record) and on
its driver lean_check.py, which is called UNCHANGED as the recorded command.
The driver prints only fixed header lines and Lean's own output (no machine
paths), so stdout can be compared byte for byte with the original macOS receipt.

Differences from the CG-001 tool, each recorded in RUN.json:
  * --toolchain selects the record (default: the Linux record of this audit);
  * run ids must contain -COPUS-;
  * the deterministic hash of the whole lib/lean/Init tree is checked at capture
    time (the canonical verifier only re-checks pinned files, via the driver);
  * the release asset is listed as an external dependency, with
    publisher_digest = null (no publisher digest was readable in this session);
  * expected_outcome, outcome_matches_expectation and rejection_stage are
    recorded, so tools/verify_copus_run.py can check negative controls.

Usage (cwd = repository root):
  python3 -B Cloud-Opus审计并补完GLM/tools/capture_copus_lean_run.py \
      --run-id 20260927-COPUS-<NAME>-01 --proof-id <ID> --claim-id <ID> \
      --source <A.lean> [--source <B.lean> ...] [--leanchecker] \
      [--manifest-file <path>]... --expect ACCEPT|REJECT --scope "..." \
      [--non-goal "..."]... [--audit-note "..."]...
Exit code: 0 when the outcome matches the expectation, 1 otherwise.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOOLCHAIN = "HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json"
DRIVER = Path(".claude/goals/CG-001-targeted-overview/tools/lean_check.py")
CANONICAL_VERIFIER = ROOT / "scripts/audit/verify_formal_proof_run.py"


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


def deterministic_tree(path: Path) -> dict[str, object]:
    spec = importlib.util.spec_from_file_location("canonical_verifier", CANONICAL_VERIFIER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.deterministic_tree(path)


IO_FAILURE_MARKERS = ("failed to open file", "unknown module prefix", "No such file or directory")


def classify_failure(stdout: str, sources: list[Path]) -> str:
    """Name the step that failed, from the driver's '## <step>' headers.

    ELABORATION_ERROR_IN_TARGET  the last source was compiled and Lean reported an error in it
    ERROR_IN_EARLIER_SOURCE      compilation stopped at a source before the target
    TOOLCHAIN_OR_IO_FAILURE      Lean could not read a toolchain or build file
    LEANCHECKER_FAILURE          the fresh-kernel replay step failed
    DRIVER_OR_TOOL_FAILURE       anything else (no header, driver refused to run, ...)
    """
    step = None
    body: list[str] = []
    for line in stdout.splitlines():
        if line.startswith("## ") and not line.startswith("## exit "):
            step, body = line[3:], []
        elif not line.startswith("## exit "):
            body.append(line)
    if step is None:
        return "DRIVER_OR_TOOL_FAILURE"
    text = "\n".join(body)
    if any(marker in text for marker in IO_FAILURE_MARKERS):
        return "TOOLCHAIN_OR_IO_FAILURE"
    if step.startswith("leanchecker"):
        return "LEANCHECKER_FAILURE"
    target = sources[-1].as_posix()
    if step == f"lean {target}" and f"{target}:" in text and "error:" in text:
        return "ELABORATION_ERROR_IN_TARGET"
    if step.startswith("lean "):
        return "ERROR_IN_EARLIER_SOURCE"
    return "DRIVER_OR_TOOL_FAILURE"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--proof-id", required=True)
    parser.add_argument("--claim-id", action="append", required=True)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--leanchecker", action="store_true")
    parser.add_argument("--manifest-file", action="append", default=[])
    parser.add_argument("--toolchain", default=DEFAULT_TOOLCHAIN)
    parser.add_argument("--expect", choices=["ACCEPT", "REJECT"], required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    parser.add_argument("--audit-note", action="append", default=[])
    args = parser.parse_args()

    if not all(c.isalnum() or c in "._-" for c in args.run_id) or "-COPUS-" not in args.run_id:
        raise SystemExit("RUN_ID_INVALID_OR_NOT_COPUS")
    run_dir = ROOT / "HoTT/verification/runs" / args.run_id
    if run_dir.exists():
        raise SystemExit(f"RUN_ALREADY_EXISTS:{args.run_id}")

    toolchain_relative = safe_relative(args.toolchain)
    toolchain = json.loads((ROOT / toolchain_relative).read_text(encoding="utf-8"))
    prefix = Path(toolchain["prefix"])
    external = []
    for row in toolchain["pinned_files"]:
        path = prefix / row["relative_path"]
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise SystemExit(f"LEAN_TOOLCHAIN_FILE_MISMATCH:{row['relative_path']}")
        external.append({"label": f"lean-{row['relative_path']}", "local_path": str(path),
                         "bytes": len(data), "sha256": sha(data)})
    tree_record = toolchain.get("init_tree")
    if tree_record:
        actual = deterministic_tree(prefix / tree_record["relative_path"])
        expected = {k: tree_record[k] for k in ("file_count", "total_bytes", "tree_sha256")}
        if actual != expected:
            raise SystemExit("LEAN_INIT_TREE_MISMATCH")
    asset = toolchain.get("release_asset")
    if asset:
        data = Path(asset["local_archive"]).read_bytes()
        if len(data) != asset["bytes"] or sha(data) != asset["sha256"]:
            raise SystemExit("LEAN_RELEASE_ASSET_MISMATCH")
        external.append({"label": "lean-release-asset", "local_path": asset["local_archive"],
                         "bytes": len(data), "sha256": sha(data), "publisher_digest": None,
                         "url": asset["url"]})

    sources = [safe_relative(s) for s in args.source]
    extra = [safe_relative(s) for s in args.manifest_file] + [toolchain_relative, DRIVER]
    version = subprocess.run([str(prefix / "bin/lean"), "--version"], capture_output=True, check=True,
                             env={"PATH": f"{prefix}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(prefix)},
                             stdin=subprocess.DEVNULL).stdout.decode().strip()
    if version != toolchain["version_line"]:
        raise SystemExit("LEAN_VERSION_LINE_MISMATCH")
    argv = [sys.executable, "-B", DRIVER.as_posix(), "--toolchain", toolchain_relative.as_posix(),
            *(["--leanchecker"] if args.leanchecker else []), *[s.as_posix() for s in sources]]

    run_dir.mkdir(parents=True)
    started = datetime.now(timezone.utc)
    t0 = time.monotonic()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, stdin=subprocess.DEVNULL, check=False)
    duration = time.monotonic() - t0
    completed = datetime.now(timezone.utc)

    accepted = result.returncode == 0
    stage = None if accepted else classify_failure(result.stdout.decode("utf-8", "replace"), sources)
    # A negative control counts only when Lean rejects the TARGET (last) source itself.
    # A failure while compiling an earlier source, a missing toolchain file, or a
    # leanchecker failure is a tool failure, never a rejection "for the right reason".
    genuine_rejection = stage == "ELABORATION_ERROR_IN_TARGET"
    matches = accepted if args.expect == "ACCEPT" else genuine_rejection

    env_text = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"python_executable={sys.executable}",
        f"lean_prefix={prefix}",
        f"lean_version={version}",
        f"leanchecker_fresh_replay={'yes' if args.leanchecker else 'no'}",
        "theory_variant=Lean 4 kernel; set-level model statements only (equality has UIP; no HoTT paths)",
        "dependency_policy=pinned toolchain files by SHA-256 (launchers, shared libraries, Init.olean, Init/Prelude.olean) re-checked by the driver on every replay; whole lib/lean/Init tree hash checked at capture; minimal environment; no elan",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
    ]) + "\n"

    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": [file_row(p) for p in [*sources, *extra]],
        "external_dependencies": external,
    }
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
        "status": ("KERNEL_ACCEPTED_WITH_SCOPE" if accepted
                   else "KERNEL_REJECTED" if genuine_rejection else "TOOL_FAILURE"),
        "expected_outcome": args.expect,
        "outcome_matches_expectation": matches,
        "rejection_stage": stage,
        "scope": args.scope,
        "non_goals": args.non_goal,
        "audit_session": "Cloud-Opus (Claude Code cloud session), branch claude/charming-pasteur-mvzlio",
        "audit_notes": args.audit_note,
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "stdout": artifact(run_dir, "stdout.txt", result.stdout),
        "stderr": artifact(run_dir, "stderr.txt", result.stderr),
        "environment": artifact(run_dir, "environment.txt", env_text.encode("utf-8")),
        "source_manifest": artifact(run_dir, "source-manifest.json", json_bytes(manifest)),
    }
    (run_dir / "RUN.json").write_bytes(json_bytes(run))
    print(json.dumps({"run": f"HoTT/verification/runs/{args.run_id}", "status": run["status"],
                      "exit_code": result.returncode, "expected": args.expect, "matches": matches,
                      "rejection_stage": stage, "seconds": round(duration, 1)}, ensure_ascii=False))
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
