"""Shared helpers: hashing, atomic writes, Git state, path safety.

The coordinator is standard-library only on purpose: the first version must
run inside the pinned research environment without installing anything new.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath


class MachineOverviewError(RuntimeError):
    """A classified coordinator failure (fail closed, never silent)."""


RUNNER_SOURCE_RELATIVE_PATHS_V2 = (
    "machine-overview/mo.py",
    "machine-overview/registry.json",
    "machine-overview/machine_overview/__init__.py",
    "machine-overview/machine_overview/__main__.py",
    "machine-overview/machine_overview/case.py",
    "machine-overview/machine_overview/cli.py",
    "machine-overview/machine_overview/correspondence.py",
    "machine-overview/machine_overview/index.py",
    "machine-overview/machine_overview/model.py",
    "machine-overview/machine_overview/profile.py",
    "machine-overview/machine_overview/report.py",
    "machine-overview/machine_overview/search.py",
    "machine-overview/machine_overview/util.py",
    "machine-overview/machine_overview/verify.py",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deterministic_tree(root: Path) -> dict[str, object]:
    """Hash a source tree exactly like the project's formal-run manifests."""
    if not root.is_dir() or root.is_symlink():
        raise MachineOverviewError(f"TREE_ROOT_INVALID:{root}")
    rows: list[dict[str, object]] = []
    total = 0
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink() and path.suffix != ".agdai" and path.name != ".DS_Store":
            data = path.read_bytes()
            rows.append({"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha256_bytes(data)})
            total += len(data)
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {"file_count": len(rows), "total_bytes": total, "tree_sha256": digest.hexdigest()}


def file_row(path: Path, label: str | None = None) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"FILE_MISSING_OR_SYMLINK:{path}")
    data = path.read_bytes()
    row: dict[str, object] = {"bytes": len(data), "sha256": sha256_bytes(data)}
    row["local_path" if label is not None else "path"] = str(path if path.is_absolute() else path.as_posix())
    if label is not None:
        row["label"] = label
    return row


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise MachineOverviewError(f"INVALID_JSON:{path}") from exc
    if not isinstance(value, dict):
        raise MachineOverviewError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(dir=path.parent, prefix=path.name + ".", suffix=".tmp", delete=False)
    try:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
        handle.close()
        os.replace(handle.name, path)
    except BaseException:
        handle.close()
        try:
            os.unlink(handle.name)
        except OSError:
            pass
        raise


def write_json(path: Path, value: object) -> None:
    write_bytes(path, json_bytes(value))


def write_text(path: Path, text: str) -> None:
    write_bytes(path, text.encode("utf-8"))


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if (
        not value
        or "\\" in value
        or "\x00" in value
        or path.is_absolute()
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        raise MachineOverviewError(f"UNSAFE_RELATIVE_PATH:{value}")
    return Path(*path.parts)


def run_git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise MachineOverviewError(f"GIT_COMMAND_FAILED:{args}:{result.stderr.strip()}")
    return result.stdout.strip()


def find_repo_root(start: Path | None = None) -> Path:
    base = (start or Path.cwd()).resolve()
    try:
        return Path(run_git(base, "rev-parse", "--show-toplevel"))
    except MachineOverviewError as exc:
        raise MachineOverviewError(f"GIT_WORK_TREE_REQUIRED:{base}") from exc


def git_state(root: Path) -> dict[str, object]:
    """Record the Git identity of the *worktree* (works with .git files)."""
    tracked = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no"],
        capture_output=True,
        text=True,
        check=False,
    )
    complete = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
        capture_output=True,
        text=True,
        check=False,
    )
    tracked_lines = tracked.stdout.splitlines()
    complete_lines = complete.stdout.splitlines()
    untracked_lines = [line for line in complete_lines if line.startswith("?? ")]
    return {
        "worktree_root": str(root),
        "head": run_git(root, "rev-parse", "HEAD"),
        "branch": run_git(root, "rev-parse", "--abbrev-ref", "HEAD"),
        "git_dir": run_git(root, "rev-parse", "--git-dir"),
        "git_common_dir": run_git(root, "rev-parse", "--git-common-dir"),
        "tracked_dirty": bool(tracked_lines),
        "tracked_dirty_entries": len(tracked_lines),
        "untracked_entries": len(untracked_lines),
        "worktree_dirty": bool(complete_lines),
        "worktree_dirty_entries": len(complete_lines),
    }


def runner_source_paths(repo_root: Path) -> list[Path]:
    """Files whose bytes determine coordinator behaviour for a run."""
    paths = [repo_root / safe_relative(relative) for relative in RUNNER_SOURCE_RELATIVE_PATHS_V2]
    for path in paths:
        if not path.is_file() or path.is_symlink():
            raise MachineOverviewError(f"RUNNER_SOURCE_INVALID:{path}")
    return paths


def runner_identity(repo_root: Path) -> dict[str, object]:
    executable = Path(sys.executable).resolve()
    if not executable.is_file():
        raise MachineOverviewError(f"PYTHON_EXECUTABLE_MISSING:{executable}")
    return {
        "schema_version": "machine-overview-runner-identity/v1",
        "python": {
            "version": sys.version,
            "executable": str(executable),
            "bytes": executable.stat().st_size,
            "sha256": sha256_file(executable),
        },
        "sources": [
            {
                "path": path.relative_to(repo_root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
            for path in runner_source_paths(repo_root)
        ],
        "git": git_state(repo_root),
    }


def capture_runner_snapshot(repo_root: Path, run_dir: Path) -> dict[str, object]:
    """Persist the exact coordinator and interpreter identity used by a run."""
    identity = runner_identity(repo_root)
    snapshot_root = run_dir / "runner-snapshot"
    rows: list[dict[str, object]] = []
    for source in identity["sources"]:
        relative = safe_relative(str(source["path"]))
        source_path = repo_root / relative
        snapshot_path = snapshot_root / relative
        data = source_path.read_bytes()
        write_bytes(snapshot_path, data)
        rows.append({
            **source,
            "snapshot_path": snapshot_path.relative_to(run_dir).as_posix(),
        })
    identity["sources"] = rows
    manifest_path = run_dir / "runner-manifest.json"
    write_json(manifest_path, identity)
    return {
        "path": manifest_path.relative_to(run_dir).as_posix(),
        "bytes": manifest_path.stat().st_size,
        "sha256": sha256_file(manifest_path),
    }


def assert_runner_unchanged(
    repo_root: Path, run_dir: Path, binding: dict, *, require_live_match: bool = True,
) -> None:
    """Check the saved snapshot and ensure live sources did not change mid-run."""
    manifest_path = run_dir / safe_relative(binding["path"])
    if not manifest_path.is_file():
        raise MachineOverviewError("RUNNER_MANIFEST_MISSING")
    if manifest_path.stat().st_size != binding.get("bytes") or sha256_file(manifest_path) != binding.get("sha256"):
        raise MachineOverviewError("RUNNER_MANIFEST_HASH_MISMATCH")
    manifest = read_json(manifest_path)
    if manifest.get("schema_version") != "machine-overview-runner-identity/v1":
        raise MachineOverviewError("RUNNER_MANIFEST_SCHEMA_INVALID")
    rows = manifest.get("sources", [])
    if not isinstance(rows, list) or [row.get("path") for row in rows] != list(RUNNER_SOURCE_RELATIVE_PATHS_V2):
        raise MachineOverviewError("RUNNER_SOURCE_ROSTER_MISMATCH")
    python = manifest.get("python", {})
    if (not isinstance(python, dict) or not isinstance(python.get("version"), str)
            or not isinstance(python.get("executable"), str) or not isinstance(python.get("bytes"), int)
            or not isinstance(python.get("sha256"), str) or len(python["sha256"]) != 64):
        raise MachineOverviewError("RUNNER_PYTHON_IDENTITY_INVALID")
    if require_live_match:
        live_python = Path(sys.executable).resolve()
        if (str(live_python) != python["executable"] or live_python.stat().st_size != python["bytes"]
                or sha256_file(live_python) != python["sha256"] or sys.version != python["version"]):
            raise MachineOverviewError("RUNNER_PYTHON_IDENTITY_CHANGED")
    for row in rows:
        relative = safe_relative(row["path"])
        expected_snapshot = Path("runner-snapshot") / relative
        if row.get("snapshot_path") != expected_snapshot.as_posix():
            raise MachineOverviewError(f"RUNNER_SNAPSHOT_PATH_MISMATCH:{relative.as_posix()}")
        snapshot = run_dir / safe_relative(row["snapshot_path"])
        paths = [(snapshot, "snapshot")]
        if require_live_match:
            paths.append((repo_root / relative, "live"))
        for path, label in paths:
            if not path.is_file() or path.is_symlink():
                raise MachineOverviewError(f"RUNNER_SOURCE_MISSING:{label}:{relative.as_posix()}")
            if path.stat().st_size != row.get("bytes") or sha256_file(path) != row.get("sha256"):
                raise MachineOverviewError(f"RUNNER_SOURCE_HASH_MISMATCH:{label}:{relative.as_posix()}")


def load_runner_registry_snapshot(run_dir: Path, binding: dict) -> dict:
    """Load the registry bytes already covered by the runner manifest."""
    manifest_path = run_dir / safe_relative(binding["path"])
    manifest = read_json(manifest_path)
    rows = manifest.get("sources", [])
    matches = [row for row in rows if row.get("path") == "machine-overview/registry.json"]
    if len(matches) != 1:
        raise MachineOverviewError("RUNNER_REGISTRY_SNAPSHOT_MISSING")
    return read_json(run_dir / safe_relative(matches[0]["snapshot_path"]))


def load_locked_profile(repo_root: Path, profile_path: Path) -> dict:
    profile = read_json(profile_path)
    if profile.get("schema_version") != "machine-overview-profile/v1":
        raise MachineOverviewError("PROFILE_SCHEMA_INVALID")
    return profile
