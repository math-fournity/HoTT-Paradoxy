#!/usr/bin/env python3
"""Capture or recheck the pinned cctt GZ-005 input-domain controls.

The upstream command-line program uses an exit status that is insufficient as
an acceptance oracle: it can print a type error and still return zero.  This
script therefore records both process status and diagnostic-text criteria.
It intentionally creates a checker-evidence receipt, not a proof-assistant
kernel receipt and not a mathematical theorem.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path("HoTT/formal/external-cctt-r4")
TOOLCHAIN = ROOT / PACKAGE / "TOOLCHAIN.json"
PROFILE = ROOT / PACKAGE / "restricted_profile.py"
DEFAULT_EXTERNAL_ROOT = Path("/tmp/gz005-cctt-3695c69e")
RUN_ID = "20261005-CCTT-R4-INPUT-DOMAIN-002"
RUN_RELATIVE = Path("HoTT/verification/runs") / RUN_ID
ERROR_RE = re.compile(r"(?m)^ERROR(?:\s|$)")
CHECKED_RE = re.compile(r"(?m)^checked\s+[0-9]+\s+definitions$")

FIXTURES = {
    "Positive": {
        "profile_accepted": True,
        "diagnostic_accepted": True,
        "feature_markers": ["inductive Nat", "=", "Glue", "coe", "hcom"],
    },
    "Hole": {
        "profile_accepted": False,
        "profile_reason": "HOLE_TOKEN",
        "diagnostic_accepted": True,
    },
    "Recursive": {
        "profile_accepted": False,
        "profile_reason": "TOP_LEVEL_RECURSION_CYCLE:loop",
        "diagnostic_accepted": True,
    },
    "TypeError": {
        "profile_accepted": True,
        "diagnostic_accepted": False,
    },
}


class CaptureError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()


def command(argv: list[str], cwd: Path, *, timeout: int | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout, check=False)


def command_text(argv: list[str], cwd: Path) -> str:
    result = command(argv, cwd)
    if result.returncode:
        raise CaptureError(
            f"COMMAND_FAILED:{' '.join(argv)}:{result.stderr.decode('utf-8', 'replace').strip()}"
        )
    return result.stdout.decode("utf-8").strip()


def regular_file(path: Path, label: str) -> Path:
    if not path.is_file() or path.is_symlink():
        raise CaptureError(f"REQUIRED_REGULAR_FILE_MISSING:{label}:{path}")
    return path


def external_file(path: Path, label: str) -> dict[str, object]:
    data = regular_file(path, label).read_bytes()
    return {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}


def project_file(path: Path) -> dict[str, object]:
    data = regular_file(path, "project").read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": sha(data)}


def tracked_tree(root: Path) -> dict[str, object]:
    listed = command(["git", "ls-files", "-z"], root).stdout.split(b"\0")
    rows: list[dict[str, object]] = []
    for raw in listed:
        if not raw:
            continue
        relative = raw.decode("utf-8")
        path = root / relative
        data = regular_file(path, f"upstream-tracked:{relative}").read_bytes()
        rows.append({"path": relative, "bytes": len(data), "sha256": sha(data)})
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {"tracked_file_count": len(rows), "tracked_tree_sha256": digest.hexdigest()}


def load_toolchain() -> dict[str, Any]:
    value = json.loads(regular_file(TOOLCHAIN, "toolchain").read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != "cctt-r4-toolchain/v1":
        raise CaptureError("TOOLCHAIN_SCHEMA_INVALID")
    return value


def allowed_status(root: Path, spec: dict[str, Any]) -> None:
    status = command_text(["git", "status", "--porcelain=v1"], root)
    allowed = {f"?? {entry}" for entry in spec["upstream"]["expected_untracked_after_stack_build"]}
    actual = {line for line in status.splitlines() if line}
    if actual - allowed:
        raise CaptureError(f"UPSTREAM_UNEXPECTED_WORKTREE_DELTA:{sorted(actual - allowed)}")


def check_external_root(spec: dict[str, Any]) -> tuple[Path, Path, Path, Path]:
    root = Path(os.environ.get("CCTT_R4_ROOT", str(DEFAULT_EXTERNAL_ROOT))).resolve()
    if not root.is_dir() or root.is_symlink():
        raise CaptureError("CCTT_EXTERNAL_ROOT_INVALID")
    if command_text(["git", "rev-parse", "HEAD"], root) != spec["upstream"]["commit"]:
        raise CaptureError("CCTT_EXTERNAL_COMMIT_MISMATCH")
    if command(["git", "diff", "--quiet"], root).returncode != 0:
        raise CaptureError("CCTT_EXTERNAL_TRACKED_WORKTREE_DIRTY")
    if command(["git", "diff", "--cached", "--quiet"], root).returncode != 0:
        raise CaptureError("CCTT_EXTERNAL_INDEX_DIRTY")
    for filename, expected in (
        ("stack.yaml", spec["upstream"]["stack_yaml_sha256"]),
        ("package.yaml", spec["upstream"]["package_yaml_sha256"]),
        ("stack.yaml.lock", spec["upstream"]["stack_lock_sha256"]),
    ):
        data = regular_file(root / filename, filename).read_bytes()
        if sha(data) != expected:
            raise CaptureError(f"CCTT_PROJECT_INPUT_HASH_MISMATCH:{filename}")
    # Homebrew exposes these commands through symlinked shims.  The receipt
    # hashes the resolved executable bytes, while the command remains the
    # resolved absolute path so a captured run cannot silently change shims.
    stack = Path(command_text(["bash", "-c", "command -v stack"], root)).resolve()
    ghc = Path(command_text(["bash", "-c", "command -v ghc"], root)).resolve()
    return root, stack, ghc, root / "stack.yaml.lock"


def build_checker(root: Path, stack: Path) -> tuple[Path, subprocess.CompletedProcess[bytes]]:
    build = command([str(stack), "--system-ghc", "build"], root, timeout=120)
    if build.returncode:
        raise CaptureError("CCTT_STACK_BUILD_FAILED")
    install_root = Path(command_text([str(stack), "--system-ghc", "path", "--local-install-root"], root))
    candidates = sorted(
        path for path in install_root.rglob("cctt") if path.is_file() and os.access(path, os.X_OK)
    )
    if len(candidates) != 1:
        raise CaptureError(f"CCTT_BINARY_AMBIGUOUS_OR_MISSING:{[str(p) for p in candidates]}")
    return candidates[0], build


def profile_result(source: Path) -> tuple[dict[str, Any], subprocess.CompletedProcess[bytes]]:
    result = command([sys.executable, str(PROFILE), str(source)], ROOT, timeout=10)
    try:
        value = json.loads(result.stdout.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise CaptureError("PROFILE_OUTPUT_NOT_JSON") from exc
    if not isinstance(value, dict) or not isinstance(value.get("accepted"), bool):
        raise CaptureError("PROFILE_OUTPUT_SCHEMA_INVALID")
    return value, result


def checker_result(binary: Path, source: Path) -> tuple[dict[str, object], subprocess.CompletedProcess[bytes]]:
    result = command([str(binary), str(source)], ROOT, timeout=10)
    combined = result.stdout + result.stderr
    text = combined.decode("utf-8", "replace")
    return {
        "process_exit_code": result.returncode,
        "has_error_diagnostic": bool(ERROR_RE.search(text)),
        "has_checked_definitions_marker": bool(CHECKED_RE.search(text)),
        "diagnostic_accepted": result.returncode == 0
        and not ERROR_RE.search(text)
        and bool(CHECKED_RE.search(text)),
    }, result


def fixture_results(binary: Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    records: dict[str, Any] = {}
    artifacts: dict[str, bytes] = {}
    for name, expected in FIXTURES.items():
        source = ROOT / PACKAGE / f"{name}.cctt"
        profile, profile_process = profile_result(source)
        checker, checker_process = checker_result(binary, source)
        feature_markers = expected.get("feature_markers", [])
        source_text = source.read_text(encoding="utf-8")
        missing_markers = [marker for marker in feature_markers if marker not in source_text]
        if profile["accepted"] != expected["profile_accepted"]:
            raise CaptureError(f"PROFILE_EXPECTATION_FAILED:{name}:{profile}")
        if not profile["accepted"] and expected.get("profile_reason") not in profile.get("reasons", []):
            raise CaptureError(f"PROFILE_REASON_EXPECTATION_FAILED:{name}:{profile}")
        if checker["diagnostic_accepted"] != expected["diagnostic_accepted"]:
            raise CaptureError(f"CHECKER_DIAGNOSTIC_EXPECTATION_FAILED:{name}:{checker}")
        if missing_markers:
            raise CaptureError(f"POSITIVE_FEATURE_MARKERS_MISSING:{missing_markers}")
        records[name] = {
            "source": project_file(source),
            "profile": {**profile, "process_exit_code": profile_process.returncode},
            "checker": checker,
        }
        artifacts[f"fixtures/{name}.profile.stdout.txt"] = profile_process.stdout
        artifacts[f"fixtures/{name}.profile.stderr.txt"] = profile_process.stderr
        artifacts[f"fixtures/{name}.checker.stdout.txt"] = checker_process.stdout
        artifacts[f"fixtures/{name}.checker.stderr.txt"] = checker_process.stderr

    recursive_source = ROOT / PACKAGE / "Recursive.cctt"
    try:
        nf = command([str(binary), str(recursive_source), "nf", "loop"], ROOT, timeout=2)
        nf_record: dict[str, object] = {
            "observation": "PROCESS_EXITED_WITHIN_2_SECONDS",
            "process_exit_code": nf.returncode,
            "contains_recursive_thunk_diagnostic": "<<loop>>" in (nf.stdout + nf.stderr).decode("utf-8", "replace"),
        }
        artifacts["fixtures/Recursive.normalization.stdout.txt"] = nf.stdout
        artifacts["fixtures/Recursive.normalization.stderr.txt"] = nf.stderr
    except subprocess.TimeoutExpired as exc:
        nf_record = {"observation": "TIMEOUT_AFTER_2_SECONDS"}
        artifacts["fixtures/Recursive.normalization.stdout.txt"] = exc.stdout or b""
        artifacts["fixtures/Recursive.normalization.stderr.txt"] = exc.stderr or b""
    records["Recursive"]["normalization_observation"] = nf_record
    return records, artifacts


def check_all() -> tuple[dict[str, Any], subprocess.CompletedProcess[bytes], dict[str, Any], dict[str, bytes], Path, Path, Path, Path]:
    spec = load_toolchain()
    upstream, stack, ghc, lock = check_external_root(spec)
    binary, build = build_checker(upstream, stack)
    allowed_status(upstream, spec)
    records, artifacts = fixture_results(binary)
    return spec, build, records, artifacts, upstream, stack, ghc, binary


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise CaptureError(f"REFUSE_OVERWRITE:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def file_descriptor(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": path.name, "bytes": len(data), "sha256": sha(data)}


def capture() -> int:
    started = dt.datetime.now(dt.timezone.utc)
    spec, build, records, artifacts, upstream, stack, ghc, binary = check_all()
    run_dir = ROOT / RUN_RELATIVE
    if run_dir.exists():
        raise CaptureError("RUN_ALREADY_EXISTS")
    manifest = {
        "schema_version": "cctt-r4-source-manifest/v1",
        "run_id": RUN_ID,
        "package_files": [
            project_file(ROOT / PACKAGE / name)
            for name in sorted(
                [
                    "Positive.cctt", "Hole.cctt", "Recursive.cctt", "TypeError.cctt",
                    "restricted_profile.py", "capture_cctt_r4_run.py", "verify_cctt_r4_run.py",
                    "TOOLCHAIN.json", "README.md",
                ]
            )
        ],
        "external_dependencies": [
            {"label": "cctt-tracked-source-tree", "local_path": str(upstream), "git_commit": spec["upstream"]["commit"], **tracked_tree(upstream)},
            external_file(upstream / "stack.yaml", "cctt-stack-yaml"),
            external_file(upstream / "package.yaml", "cctt-package-yaml"),
            external_file(upstream / "stack.yaml.lock", "cctt-stack-lock"),
            external_file(stack, "stack-binary"),
            external_file(ghc, "system-ghc-binary"),
            external_file(binary, "cctt-checker-binary"),
        ],
        "scope": "Pinned cctt checker and restricted input-domain controls for G1/R4. This is not a kernel proof, full proof relation, or Gödel instance.",
    }
    environment = (
        f"platform={platform.platform()}\n"
        f"python={sys.version}\n"
        f"upstream_root={upstream}\n"
        f"upstream_commit={spec['upstream']['commit']}\n"
        f"stack={stack}\n"
        f"ghc={ghc}\n"
        f"ghc_version={command_text([str(ghc), '--version'], upstream)}\n"
        f"checker={binary}\n"
        f"checker_sha256={sha(binary.read_bytes())}\n"
        f"build_exit={build.returncode}\n"
    ).encode()
    completed = dt.datetime.now(dt.timezone.utc)
    receipt: dict[str, Any] = {
        "schema_version": "cctt-r4-checker-run/v1",
        "run_id": RUN_ID,
        "unit_id": "GZ-005",
        "route": "G1-R4",
        "status": "CHECKER_INPUT_DOMAIN_CONTROLS_PASS_WITH_SCOPE",
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "build": {
            "argv": [str(stack), "--system-ghc", "build"],
            "exit_code": build.returncode,
        },
        "checker_acceptance_contract": spec["checker_acceptance"],
        "fixtures": records,
        "scope": "Demonstrates a bounded restricted cctt input contract with explicit controls. It does not establish a total proof checker, termination, Gödel representability, exact HoTT incompleteness, or any bare-ZFC result.",
        "non_goals": [
            "No cctt CLI exit code alone is treated as checker acceptance.",
            "No finite observation of recursive normalization proves global nontermination.",
            "No project-defined restricted profile is called an actual mathematical-community or ZFC acceptance interface.",
        ],
    }
    write_new(run_dir / "build.stdout.txt", build.stdout)
    write_new(run_dir / "build.stderr.txt", build.stderr)
    for relative, data in artifacts.items():
        write_new(run_dir / relative, data)
    write_new(run_dir / "environment.txt", environment)
    write_new(run_dir / "source-manifest.json", json_bytes(manifest))
    for name in ["build.stdout.txt", "build.stderr.txt", "environment.txt", "source-manifest.json", *sorted(artifacts)]:
        path = run_dir / name
        receipt.setdefault("artifacts", {})[name] = {"bytes": len(path.read_bytes()), "sha256": sha(path.read_bytes())}
    write_new(run_dir / "RUN.json", json_bytes(receipt))
    print(json.dumps({"run_id": RUN_ID, "status": receipt["status"], "fixtures": records}, ensure_ascii=False, sort_keys=True))
    return 0


def verify_live() -> int:
    spec, build, records, _, upstream, stack, ghc, binary = check_all()
    payload = {
        "status": "LIVE_CONTROLS_PASS_WITH_SCOPE",
        "upstream_commit": spec["upstream"]["commit"],
        "build_exit": build.returncode,
        "checker_sha256": sha(binary.read_bytes()),
        "ghc_version": command_text([str(ghc), "--version"], upstream),
        "fixtures": records,
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true", help="re-run controls without writing a receipt")
    args = parser.parse_args()
    try:
        return verify_live() if args.verify else capture()
    except (CaptureError, OSError, subprocess.TimeoutExpired) as exc:
        print(f"GZ005_CAPTURE_ERROR:{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
