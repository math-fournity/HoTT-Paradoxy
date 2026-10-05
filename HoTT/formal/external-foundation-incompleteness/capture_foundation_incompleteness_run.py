#!/usr/bin/env python3
"""Capture GZ-002 against a pinned Foundation Lean source tree.

The source tree remains external because it is an upstream Lean project.  This
script fixes its commit, project inputs, tracked source tree, selected build
module, and Lean qualification source before preserving one primary and one
expected-rejection run in this repository.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path("HoTT/formal/external-foundation-incompleteness")
SOURCE = PACKAGE / "Qualification.lean"
NEGATIVE = PACKAGE / "WrongMissingSoundness.lean"
CLAIM = PACKAGE / "CLAIM-R3-FOUNDATION-INCOMPLETENESS.md"
TOOLCHAIN = PACKAGE / "TOOLCHAIN.json"
DEFAULT_EXTERNAL_ROOT = Path("/private/tmp/foundation-zfc-f3972f4204fc")
RUN_PREFIX = "20261005-MP-FOUNDATION-INCOMPLETENESS-R3-001-"
NEG_PREFIX = "20261005-MP-FOUNDATION-INCOMPLETENESS-R3-NEG-001-"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def relative_row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": sha(data)}


def external_file(path: Path, label: str) -> dict[str, object]:
    data = path.read_bytes()
    return {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}


def deterministic_tree(root: Path) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    total = 0
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink() and path.name != ".DS_Store":
            data = path.read_bytes()
            row = {"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha(data)}
            rows.append(row)
            total += len(data)
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {"file_count": len(rows), "total_bytes": total, "tree_sha256": digest.hexdigest()}


def checked_project_file(root: Path, name: str, expected_sha: str) -> Path:
    path = root / name
    if not path.is_file() or path.is_symlink() or sha(path.read_bytes()) != expected_sha:
        raise RuntimeError(f"FOUNDATION_PROJECT_INPUT_MISMATCH:{name}")
    return path


def cmd_output(argv: list[str], cwd: Path) -> str:
    return subprocess.check_output(argv, cwd=cwd, text=True).strip()


def check_external_root(spec: dict[str, object]) -> tuple[Path, Path, Path, Path, Path, Path, str]:
    external_root = Path(os.environ.get("FOUNDATION_R3_ROOT", str(DEFAULT_EXTERNAL_ROOT))).resolve()
    if not external_root.is_dir() or external_root.is_symlink():
        raise RuntimeError("FOUNDATION_ROOT_INVALID")
    if cmd_output(["git", "rev-parse", "HEAD"], external_root) != spec["external_project"]["commit"]:
        raise RuntimeError("FOUNDATION_COMMIT_MISMATCH")
    if subprocess.run(["git", "diff", "--quiet"], cwd=external_root).returncode != 0:
        raise RuntimeError("FOUNDATION_TRACKED_WORKTREE_DIRTY")
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=external_root).returncode != 0:
        raise RuntimeError("FOUNDATION_INDEX_DIRTY")
    # The previously used source checkout may carry only this unrelated,
    # untracked local probe.  It is outside Foundation/ and cannot affect the
    # imported module or the recorded source-tree hash.
    dirty = cmd_output(["git", "status", "--porcelain=v1"], external_root)
    allowed = "?? GodelBaseline.lean"
    if dirty not in ("", allowed):
        raise RuntimeError("FOUNDATION_UNEXPECTED_WORKTREE_DELTA")
    required = spec["external_project"]["required_project_files"]
    lakefile = checked_project_file(external_root, "lakefile.toml", required["lakefile.toml_sha256"])
    manifest = checked_project_file(external_root, "lake-manifest.json", required["lake_manifest_sha256"])
    toolchain_file = checked_project_file(external_root, "lean-toolchain", required["lean_toolchain_sha256"])
    source_tree = external_root / spec["external_project"]["source_tree_subpath"]
    if not source_tree.is_dir() or source_tree.is_symlink():
        raise RuntimeError("FOUNDATION_SOURCE_TREE_INVALID")
    elan = Path(cmd_output(["bash", "-c", "command -v elan"], external_root))
    lake = Path(cmd_output([str(elan), "which", "lake"], external_root)).resolve()
    lean = Path(cmd_output([str(elan), "which", "lean"], external_root)).resolve()
    if not lake.is_file() or not lean.is_file():
        raise RuntimeError("FOUNDATION_LEAN_TOOLCHAIN_MISSING")
    return external_root, source_tree, lakefile, manifest, toolchain_file, lake, str(lean)


def main() -> None:
    negative = "--negative" in sys.argv[1:]
    prefix = NEG_PREFIX if negative else RUN_PREFIX
    run_id = next((arg for arg in sys.argv[1:] if not arg.startswith("--")), f"{prefix}01")
    if "/" in run_id or not run_id.startswith(prefix):
        raise SystemExit("RUN_ID_INVALID")
    source = NEGATIVE if negative else SOURCE
    inputs = [ROOT / path for path in (SOURCE, NEGATIVE, CLAIM, TOOLCHAIN, Path(__file__).relative_to(ROOT))]
    if any(not path.is_file() or path.is_symlink() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    spec = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    external_root, source_tree, lakefile, manifest, toolchain_file, lake, lean_str = check_external_root(spec)
    lean = Path(lean_str)
    expected_lean_hash = spec["lean"]["binary_sha256"]
    if sha(lean.read_bytes()) != expected_lean_hash:
        raise SystemExit("FOUNDATION_LEAN_BINARY_MISMATCH")

    run_dir = ROOT / "HoTT/verification/runs" / run_id
    if run_dir.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    started = dt.datetime.now(dt.timezone.utc)
    build = subprocess.run([str(lake), "build", spec["external_project"]["source_module"]], cwd=external_root, capture_output=True)
    argv = [str(lake), "--dir", str(external_root), "env", str(lean), str(source)]
    qualification = subprocess.run(argv, cwd=ROOT, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    # `command_argv` below deliberately replays only the qualification check.
    # Its required stdout/stderr must consequently be the qualification bytes
    # themselves.  The preceding source-module build is retained as separate
    # auxiliary evidence instead of being smuggled into replay-comparison
    # fields.
    stdout = qualification.stdout
    stderr = qualification.stderr
    accepted = build.returncode == 0 and qualification.returncode == 0
    negative_ok = (
        negative
        and build.returncode == 0
        and qualification.returncode != 0
        and b"T.SoundOnHierarchy" in qualification.stdout + qualification.stderr
    )
    proof_id = "MP-FOUNDATION-INCOMPLETENESS-R3-NEG-001" if negative else "MP-FOUNDATION-INCOMPLETENESS-R3-001"
    claim_ids = ["C-369 (negative control)"] if negative else ["C-369"]
    external_dependencies = [
        # The exact same upstream Foundation source tree is already qualified
        # by the common verifier as `foundation-lean-zf-source-tree`; its
        # tree hash binds the whole `Foundation/` directory, including both
        # the ZF modules and `FirstOrder/Incompleteness/First.lean`.
        {"label": "foundation-lean-zf-source-tree", "local_path": str(source_tree), **deterministic_tree(source_tree), "git_commit": spec["external_project"]["commit"]},
        external_file(lakefile, "foundation-lean-incompleteness-lakefile"),
        external_file(manifest, "foundation-lean-incompleteness-manifest"),
        external_file(toolchain_file, "foundation-lean-incompleteness-toolchain-file"),
        external_file(lean, "foundation-lean-4.34.0-binary"),
        external_file(lake, "foundation-lake-4.34.0-binary"),
    ]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": proof_id,
        "run_id": run_id,
        "files": [relative_row(path) for path in inputs],
        "external_dependencies": external_dependencies,
        "scope": "Pinned Foundation Lean first-order arithmetic incompleteness source replay; no exact HoTT, ZFC acceptance, or process-completion bridge claim.",
    }
    environment = (
        f"platform={platform.platform()}\n"
        f"external_root={external_root}\n"
        f"external_commit={spec['external_project']['commit']}\n"
        f"lake={lake}\nlean={lean}\n"
        f"source_module={spec['external_project']['source_module']}\n"
        f"build_exit={build.returncode}\n"
        f"build_stdout_sha256={sha(build.stdout)}\n"
        f"build_stderr_sha256={sha(build.stderr)}\n"
    ).encode()
    receipt: dict[str, object] = {
        "schema_version": "formal-proof-run/v1",
        "run_id": run_id,
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "proof_assistant": "Lean",
        "proof_assistant_detail": "Lean 4 via pinned Foundation Lake project",
        "proof_assistant_version": cmd_output([str(lean), "--version"], external_root),
        "theory_variant": spec["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": qualification.returncode,
        "build": {
            "argv": [str(lake), "build", spec["external_project"]["source_module"]],
            "exit_code": build.returncode,
            "stdout": {"path": "build.stdout.txt", "bytes": len(build.stdout), "sha256": sha(build.stdout)},
            "stderr": {"path": "build.stderr.txt", "bytes": len(build.stderr), "sha256": sha(build.stderr)},
        },
        "status": "NEGATIVE_CONTROL_REJECTED" if negative_ok else ("KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED"),
        "scope": "C-369 checks a pinned Foundation first-order arithmetic incompleteness theorem and its explicit source assumptions. It is an R3 source calibration only.",
        "non_goals": [
            "Does not instantiate an exact HoTT calculus or establish HoTT essentiality.",
            "Does not establish a bare-ZFC acceptance interface, an adequacy lift, or a completion bridge.",
            "Does not prove any ZFC object-language contradiction or bare-ZFC precision defect.",
            "Does not make a bounded proof-search observation stand for incompleteness.",
        ],
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run_dir.mkdir(parents=True)
    manifest_bytes = json_bytes(source_manifest)
    write_new(run_dir / "build.stdout.txt", build.stdout)
    write_new(run_dir / "build.stderr.txt", build.stderr)
    for key, name, data in (
        ("stdout", "stdout.txt", stdout),
        ("stderr", "stderr.txt", stderr),
        ("environment", "environment.txt", environment),
        ("source_manifest", "source-manifest.json", manifest_bytes),
    ):
        write_new(run_dir / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run_dir / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": run_id, "build_exit": build.returncode, "qualification_exit": qualification.returncode}, ensure_ascii=False))
    raise SystemExit(0 if (negative_ok if negative else accepted) else 1)


if __name__ == "__main__":
    main()
