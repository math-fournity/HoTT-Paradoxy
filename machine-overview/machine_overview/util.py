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
import tempfile
from pathlib import Path, PurePosixPath


class MachineOverviewError(RuntimeError):
    """A classified coordinator failure (fail closed, never silent)."""


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
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no"],
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "worktree_root": str(root),
        "head": run_git(root, "rev-parse", "HEAD"),
        "branch": run_git(root, "rev-parse", "--abbrev-ref", "HEAD"),
        "git_dir": run_git(root, "rev-parse", "--git-dir"),
        "git_common_dir": run_git(root, "rev-parse", "--git-common-dir"),
        "tracked_dirty": bool(status.stdout.strip()),
        "tracked_dirty_entries": len(status.stdout.splitlines()),
    }


def load_locked_profile(repo_root: Path, profile_path: Path) -> dict:
    profile = read_json(profile_path)
    if profile.get("schema_version") != "machine-overview-profile/v1":
        raise MachineOverviewError("PROFILE_SCHEMA_INVALID")
    return profile
