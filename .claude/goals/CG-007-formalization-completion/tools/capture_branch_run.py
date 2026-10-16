#!/usr/bin/env python3
"""Capture a GPT-branch Lean-core run as an F-011 receipt (goal-local, CG-007 W9 coverage).

Why this exists: the GPT branches origin/dev-02, origin/dev-03 and origin/dev-04 left Lean-core
formal packages whose sources import nothing but Lean 4 core (plus one package-local module).
They have per-branch receipts on their own branches, but no receipt under `dev`, so the
`形式化追踪/` coverage table cannot point at a `dev`-visible receipt for them. This tool compiles
each such source with the pinned Lean 4.34.1 binary inside a network-denied sandbox and writes
the standard formal-proof-run/v1 receipt.

Driver semantics:
  * the pinned Lean binary is called by absolute path; the elan proxy is never used;
  * a package-local module dependency (GodelQ/MetaSubtheoryAudit.lean) is built first into a
    temporary build directory that is placed on LEAN_PATH; the temporary directory never appears
    in the captured output, so a replay is byte-for-byte comparable;
  * network is denied by sandbox-exec; no credential or full environment dump is retained.

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-007-formalization-completion/tools/capture_branch_run.py \
      --package HoTT/formal/branch-formalization-coverage \
      --run-id <id> --proof-id <id> --claim-id <id> [--claim-id ...] \
      --expect ACCEPT|REJECT --source GodelQ/A.lean [--source ...] \
      --scope "..." [--non-goal "..."]...
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[4]
PINS_TOOL = Path(".claude/goals/CG-007-formalization-completion/tools/make_pins.py")
SELF = Path(".claude/goals/CG-007-formalization-completion/tools/capture_branch_run.py")
TOOLCHAIN = Path("HoTT/formal/branch-formalization-coverage/LEAN_TOOLCHAIN.json")


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
    args = parser.parse_args()

    package = safe_relative(args.package)
    if not (ROOT / package).is_dir():
        raise SystemExit(f"PACKAGE_MISSING:{package}")
    run_dir = ROOT / "HoTT/verification/runs" / args.run_id
    if run_dir.exists():
        raise SystemExit(f"RUN_ALREADY_EXISTS:{args.run_id}")

    toolchain = json.loads(TOOLCHAIN.read_text(encoding="utf-8"))
    lean = Path(toolchain["lean"]["root"]) / "bin" / "lean"
    binary = lean.read_bytes()
    if len(binary) != toolchain["lean"]["binary_bytes"] or sha(binary) != toolchain["lean"]["binary_sha256"]:
        raise SystemExit("LEAN_BINARY_MISMATCH")
    version = subprocess.run([str(lean), "--version"], capture_output=True, check=True,
                             env={"PATH": f"{lean.parent}:/usr/bin:/bin", "LEAN_SYSROOT": str(lean.parent.parent)},
                             stdin=subprocess.DEVNULL).stdout.decode().strip()
    if version != toolchain["lean"]["version_line"]:
        raise SystemExit("LEAN_VERSION_LINE_MISMATCH")

    sources = [safe_relative(s) for s in args.source]
    import re
    for rel in sources:
        text = (ROOT / package / "GodelQ" / rel.name).read_text(encoding="utf-8")
        # Drop comment bodies: the words appear in ordinary English prose ("a policy admitted on
        # ...") as well as in Lean tactics, and only the latter are forbidden.  The two drivers
        # zfc_lean_check.py and verify_cg001_run.py apply the same pattern to the raw file, so the
        # check here mirrors theirs minus the false positives from prose in doc-strings.
        code = re.sub(r"/-.*?-/", "", text, flags=re.DOTALL)
        code = re.sub(r"--[^\n]*", "", code)
        found = [w for w in ("sorry", "admit", "native_decide", "unsafe", "implemented_by",
                             "extern", "opaque") if re.search(rf"\b{w}\b", code)]
        found += [pat for pat in (r"^\s*(private\s+|protected\s+)?axiom\b", r"debug\.skipKernelTC",
                                  r"ofReduceBool", r"reduceBool")
                  if re.search(pat, code, flags=re.MULTILINE)]
        if found:
            raise SystemExit(f"FORBIDDEN_SOURCE_MARKER:{rel}:{found}")

    # Build the single package-local dependency first, into a scratch dir not shown in output.
    dep = Path("GodelQ/MetaSubtheoryAudit.lean")
    outputs = []
    profile = "(version 1)(allow default)(deny network*)"
    with tempfile.TemporaryDirectory(prefix="branch-cov-build-") as tmp:
        build = Path(tmp)
        env = {
            "PATH": f"{lean.parent}:/usr/bin:/bin",
            "LEAN_SYSROOT": str(lean.parent.parent),
            "LEAN_PATH": str(build),
            "HOME": str(build),
        }
        # The sources use a root-level `import MetaSubtheoryAudit`, so the dependency module must
        # be emitted at the root of the temporary build directory for LEAN_PATH to resolve it.
        dep_cmd = ["/usr/bin/sandbox-exec", "-p", profile, str(lean),
                   "-o", str(build / "MetaSubtheoryAudit.olean"), "-i",
                   str(build / "MetaSubtheoryAudit.ilean"), "MetaSubtheoryAudit.lean"]
        dep_result = subprocess.run(dep_cmd, cwd=ROOT / package / "GodelQ", env=env, capture_output=True, check=False)
        outputs.append((dep, dep_result))
        for rel in sources:
            cmd = ["/usr/bin/sandbox-exec", "-p", profile, str(lean), rel.name]
            result = subprocess.run(cmd, cwd=ROOT / package / "GodelQ", env=env, capture_output=True, check=False)
            outputs.append((rel, result))

    accepted = all(r.returncode == 0 for _, r in outputs)
    expected_accept = args.expect == "ACCEPT"
    combined_out = b"".join(f"## lean {rel.as_posix()}\n".encode() + r.stdout for rel, r in outputs)
    combined_err = b"".join(f"## lean {rel.as_posix()}\n".encode() + r.stderr for rel, r in outputs)

    env_text = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"lean_prefix={lean.parent.parent}",
        f"lean_version={version}",
        "dependency_policy=Lean core only plus the package-local module GodelQ.MetaSubtheoryAudit, built first into a temporary directory; network denied by sandbox-exec; elan proxy not used",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
    ]) + "\n"

    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        # MetaSubtheoryAudit is both a package-local dependency and one of the requested sources;
        # list each file once.
        "files": [file_row(package / "GodelQ" / s.name)
                  for s in dict.fromkeys(sources + [dep])],
        "external_dependencies": [{"label": "lean-core-binary", "local_path": str(lean),
                                   "bytes": len(binary), "sha256": sha(binary)}],
    }

    run_dir.mkdir(parents=True)
    started = datetime.now(timezone.utc)
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Lean 4",
        "proof_assistant_version": version,
        # Mirrors CG-007's capture_run.py: the recorded command is this driver's own invocation,
        # which is what a replay must reproduce.  The per-source Lean invocations are printed as
        # one fixed header line per step inside stdout.txt, so a replay is comparable step by step.
        "command_argv": [sys.executable, "-B", SELF.as_posix(), "--package", package.as_posix(),
                         "--run-id", args.run_id, "--proof-id", args.proof_id,
                         "--expect", args.expect, "--scope", args.scope],
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "exit_code": 0 if accepted else 1,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "expected_outcome": args.expect,
        "outcome_matches_expectation": accepted == expected_accept,
        "scope": args.scope,
        "non_goals": args.non_goal,
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "stdout": artifact(run_dir, "stdout.txt", combined_out),
        "stderr": artifact(run_dir, "stderr.txt", combined_err),
        "environment": artifact(run_dir, "environment.txt", env_text.encode("utf-8")),
        "source_manifest": artifact(run_dir, "source-manifest.json", json_bytes(manifest)),
    }
    if not accepted:
        run["rejection_stage"] = "KERNEL_ERROR_IN_TARGET" if b"(kernel)" in combined_out else "ELABORATION_ERROR_IN_TARGET"
        run["status_vocabulary_note"] = ("KERNEL_REJECTED is the repository-wide status word for 'the proof checker rejected "
                                         "the target'. rejection_stage says which Lean stage refused it.")
    (run_dir / "RUN.json").write_bytes(json_bytes(run))
    print(json.dumps({"status": run["status"], "run_path": f"HoTT/verification/runs/{args.run_id}",
                      "exit_code": run["exit_code"], "matches": accepted == expected_accept,
                      "stdout_bytes": len(combined_out), "stderr_bytes": len(combined_err)}))
    return 0 if accepted == expected_accept else 42


if __name__ == "__main__":
    raise SystemExit(main())
