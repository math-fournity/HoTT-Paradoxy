#!/usr/bin/env python3
"""Run one pinned Cubical Agda proof and persist an immutable F-011 receipt."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
RUN_ROOT = Path("HoTT/verification/runs")


class CaptureError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or "\\" in value or "\x00" in value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise CaptureError(f"UNSAFE_RELATIVE_PATH:{value}")
    return Path(*path.parts)


def file_row(path: Path, *, label: str | None = None) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise CaptureError(f"FILE_MISSING_OR_SYMLINK:{path}")
    data = path.read_bytes()
    row: dict[str, object] = {"bytes": len(data), "sha256": sha(data)}
    row["path" if label is None else "local_path"] = str(path if path.is_absolute() else path.as_posix())
    if label is not None:
        row["label"] = label
    return row


def deterministic_tree(root: Path) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise CaptureError(f"TREE_ROOT_INVALID:{root}")
    rows: list[dict[str, object]] = []
    total = 0
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink() and path.suffix != ".agdai" and path.name != ".DS_Store":
            data = path.read_bytes()
            row = {"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha(data)}
            rows.append(row)
            total += len(data)
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {"file_count": len(rows), "total_bytes": total, "tree_sha256": digest.hexdigest()}


def expect_file(path: Path, bytes_expected: object, hash_expected: object, label: str) -> None:
    row = file_row(path)
    if row["bytes"] != bytes_expected or row["sha256"] != hash_expected:
        raise CaptureError(f"PINNED_FILE_MISMATCH:{label}")


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--proof-id", required=True)
    parser.add_argument("--claim-id", action="append", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--toolchain", required=True)
    parser.add_argument("--manifest-file", action="append", default=[])
    parser.add_argument("--scope", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    args = parser.parse_args()

    root = args.project_root.resolve()
    if not (root / ".git").is_dir():
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")
    if not args.run_id or "/" in args.run_id or not all(c.isalnum() or c in "._-" for c in args.run_id):
        raise SystemExit("RUN_ID_INVALID")
    run_relative = RUN_ROOT / args.run_id
    run_dir = root / run_relative
    if run_dir.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")

    source = safe_relative(args.source)
    toolchain_relative = safe_relative(args.toolchain)
    manifest_paths = [source, toolchain_relative]
    for value in args.manifest_file:
        path = safe_relative(value)
        if path not in manifest_paths:
            manifest_paths.append(path)
    source_rows = []
    for relative in manifest_paths:
        path = root / relative
        row = file_row(path)
        row["path"] = relative.as_posix()
        source_rows.append(row)

    toolchain = json.loads((root / toolchain_relative).read_text(encoding="utf-8"))
    if toolchain.get("schema_version") != "hott-cubical-agda-toolchain/v1":
        raise SystemExit("TOOLCHAIN_SCHEMA_INVALID")
    library_registry = safe_relative(str(toolchain.get("project_library_registry", "")))
    if library_registry not in manifest_paths:
        manifest_paths.append(library_registry)
        path = root / library_registry
        row = file_row(path)
        row["path"] = library_registry.as_posix()
        source_rows.append(row)
    agda = toolchain["agda"]
    cubical = toolchain["cubical_library"]
    cache = toolchain["runtime_cache"]
    agda_archive = Path(agda["local_archive"])
    agda_binary = Path(agda["local_binary"])
    cubical_archive = Path(cubical["local_archive"])
    cubical_root = Path(cubical["local_root"])
    library_file = Path(cubical["library_file"])
    expect_file(agda_archive, agda["asset_bytes"], agda["asset_sha256"], "agda-release-asset")
    expect_file(agda_binary, agda["binary_bytes"], agda["binary_sha256"], "agda-binary")
    expect_file(cubical_archive, cubical["asset_bytes"], cubical["asset_sha256"], "cubical-release-asset")
    expect_file(library_file, cubical["library_file_bytes"], cubical["library_file_sha256"], "cubical-library-file")
    tree = deterministic_tree(cubical_root)
    if tree != {"file_count": cubical["tree_file_count"], "total_bytes": cubical["tree_total_bytes"], "tree_sha256": cubical["tree_sha256"]}:
        raise SystemExit("CUBICAL_TREE_MISMATCH")

    for key in ("xdg_data_home", "xdg_config_home", "tmpdir"):
        path = Path(cache[key])
        path.mkdir(parents=True, exist_ok=True)
        if path.is_symlink():
            raise SystemExit(f"RUNTIME_CACHE_SYMLINK:{key}")

    source_parent = (root / source).parent
    env_command = [
        "/usr/bin/env",
        f"XDG_DATA_HOME={cache['xdg_data_home']}",
        f"XDG_CONFIG_HOME={cache['xdg_config_home']}",
        f"TMPDIR={cache['tmpdir']}",
        str(agda_binary),
        "--ignore-interfaces",
        f"--library-file={root / library_registry}",
        "-l", f"cubical-{cubical['version']}",
        "-i", str(source_parent),
        source.as_posix(),
    ]
    version_command = env_command[:4] + [str(agda_binary), "--version"]
    version = subprocess.run(version_command, cwd=root, capture_output=True, check=False)
    if version.returncode != 0:
        raise SystemExit("AGDA_VERSION_COMMAND_FAILED")

    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(env_command, cwd=root, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    external = [
        {**file_row(agda_archive, label="agda-release-asset"), "publisher_digest": agda["asset_sha256"], "url": agda["asset_url"]},
        {**file_row(agda_binary, label="agda-binary")},
        {**file_row(cubical_archive, label="cubical-release-asset"), "publisher_digest": cubical["asset_sha256"], "url": cubical["asset_url"]},
        {**file_row(library_file, label="cubical-library-file")},
        {"label": "cubical-extracted-tree", "local_path": str(cubical_root), **tree, "release_tag": cubical["release_tag"], "tag_commit": cubical["tag_commit"]},
    ]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": source_rows,
        "external_dependencies": external,
    }
    source_manifest_data = json_bytes(source_manifest)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"agda_executable={agda_binary}",
        "agda_version=" + version.stdout.decode("utf-8", "replace").strip().replace("\n", " | "),
        f"cubical_library_version={cubical['version']}",
        f"cubical_library_tag_commit={cubical['tag_commit']}",
        f"cubical_library_tree_sha256={tree['tree_sha256']}",
        "theory_variant=Cubical Agda native Path and higher inductive types; source OPTIONS --safe --cubical",
        "dependency_policy=official release assets pinned by publisher SHA-256 plus extracted binary/library tree hashes",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Cubical Agda",
        "proof_assistant_version": version.stdout.decode("utf-8", "replace").strip(),
        "theory_variant": toolchain["theory_variant"],
        "command_argv": env_command,
        "cwd": str(root),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": args.scope,
        "non_goals": args.non_goal,
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": len(source_manifest_data), "sha256": sha(source_manifest_data)},
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }

    run_dir.mkdir(parents=True, exist_ok=False)
    try:
        exclusive_write(run_dir / "stdout.txt", result.stdout)
        exclusive_write(run_dir / "stderr.txt", result.stderr)
        exclusive_write(run_dir / "environment.txt", environment)
        exclusive_write(run_dir / "source-manifest.json", source_manifest_data)
        exclusive_write(run_dir / "RUN.json", json_bytes(run))
    except BaseException:
        print(f"PARTIAL_RUN_DIRECTORY_RETAINED:{run_relative.as_posix()}")
        raise

    print(json.dumps({
        "status": run["status"],
        "run_path": run_relative.as_posix(),
        "exit_code": result.returncode,
        "stdout_bytes": len(result.stdout),
        "stderr_bytes": len(result.stderr),
        "source_files": len(source_rows),
        "external_dependencies": len(external),
        "index_status": run["index_status"],
    }, ensure_ascii=False))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
