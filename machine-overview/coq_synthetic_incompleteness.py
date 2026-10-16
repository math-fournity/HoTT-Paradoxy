#!/usr/bin/env python3
"""Verify the pinned native Coq replay of the CSL 2023 incompleteness source."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


SCHEMA = "coq-synthetic-incompleteness-qualification/v1"
SOURCE_SCHEMA = "coq-synthetic-incompleteness-source-manifest/v1"
STABLE_SCHEMA = "coq-stable-build-artifact-manifest/v1"
AUX_SCHEMA = "coq-aux-build-artifact-manifest/v1"


class VerificationError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError(f"JSON_READ_FAILED:{path}") from exc
    if not isinstance(value, dict):
        raise VerificationError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def verify_file(row: dict, label: str) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise VerificationError(f"FILE_ROW_INVALID:{label}")
    path = Path(row["path"])
    if not path.is_absolute() or not path.is_file() or path.is_symlink():
        raise VerificationError(f"FILE_MISSING_OR_SYMLINK:{label}:{path}")
    data = path.read_bytes()
    if len(data) != row.get("bytes") or sha(data) != row.get("sha256"):
        raise VerificationError(f"FILE_HASH_CHANGED:{label}:{path}")
    return path


def git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise VerificationError(f"GIT_COMMAND_FAILED:{' '.join(args)}")
    return completed.stdout


def manifest_hash(rows: list[dict]) -> str:
    payload = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    ).encode("utf-8")
    return sha(payload)


def source_row(path: Path, root: Path) -> dict:
    data = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "bytes": len(data),
        "sha256": sha(data),
    }


def verify_source(receipt: dict) -> dict:
    source = receipt["source"]
    root = Path(source["local_path"])
    if not root.is_dir() or root.is_symlink():
        raise VerificationError("SOURCE_ROOT_INVALID")
    if git(root, "rev-parse", "HEAD").strip() != source["commit"]:
        raise VerificationError("SOURCE_COMMIT_CHANGED")
    if git(root, "branch", "--show-current").strip() != source["branch"]:
        raise VerificationError("SOURCE_BRANCH_CHANGED")
    if git(root, "status", "--short").strip():
        raise VerificationError("SOURCE_WORKTREE_DIRTY")
    tracked = [
        value.decode("utf-8")
        for value in subprocess.check_output(
            ["git", "-C", str(root), "ls-files", "-z"]
        ).split(b"\0")
        if value
    ]
    rows = [source_row(root / relative, root) for relative in sorted(tracked)]
    if len(rows) != source["tracked_file_count"]:
        raise VerificationError("SOURCE_FILE_COUNT_CHANGED")
    if sum(row["bytes"] for row in rows) != source["tracked_total_bytes"]:
        raise VerificationError("SOURCE_BYTE_COUNT_CHANGED")
    if manifest_hash(rows) != source["tracked_tree_sha256"]:
        raise VerificationError("SOURCE_TREE_HASH_CHANGED")

    manifest_path = verify_file(receipt["source_manifest"], "source-manifest")
    manifest = read_json(manifest_path)
    if manifest.get("schema_version") != SOURCE_SCHEMA:
        raise VerificationError("SOURCE_MANIFEST_SCHEMA_INVALID")
    if manifest.get("files") != rows:
        raise VerificationError("SOURCE_MANIFEST_ROWS_CHANGED")
    return {
        "commit": source["commit"],
        "files": len(rows),
        "bytes": sum(row["bytes"] for row in rows),
        "tree_sha256": manifest_hash(rows),
    }


def verify_image(row: dict, label: str) -> dict:
    completed = subprocess.run(
        ["docker", "image", "inspect", row["reference"]],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise VerificationError(f"DOCKER_IMAGE_UNAVAILABLE:{label}")
    values = json.loads(completed.stdout)
    if not isinstance(values, list) or len(values) != 1:
        raise VerificationError(f"DOCKER_INSPECT_INVALID:{label}")
    actual = values[0]
    if actual.get("Id") != row.get("id"):
        raise VerificationError(f"DOCKER_IMAGE_ID_CHANGED:{label}")
    if actual.get("Architecture") != row.get("architecture") or actual.get("Os") != row.get("os"):
        raise VerificationError(f"DOCKER_PLATFORM_CHANGED:{label}")
    if sorted(actual.get("RepoDigests") or []) != sorted(row.get("repo_digests") or []):
        raise VerificationError(f"DOCKER_DIGEST_CHANGED:{label}")
    if "size_bytes" in row and actual.get("Size") != row["size_bytes"]:
        raise VerificationError(f"DOCKER_SIZE_CHANGED:{label}")
    return {"id": actual["Id"], "architecture": actual["Architecture"], "os": actual["Os"]}


def verify_artifact_manifest(
    row: dict, root: Path, schema: str, label: str
) -> tuple[list[dict], dict]:
    path = verify_file(row["manifest"], f"{label}.manifest")
    value = read_json(path)
    if value.get("schema_version") != schema or not isinstance(value.get("rows"), list):
        raise VerificationError(f"ARTIFACT_MANIFEST_SCHEMA_INVALID:{label}")
    rows = value["rows"]
    actual = []
    for item in rows:
        relative = item.get("path")
        if not isinstance(relative, str) or Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise VerificationError(f"ARTIFACT_PATH_INVALID:{label}:{relative}")
        path = root / relative
        if not path.is_file() or path.is_symlink():
            raise VerificationError(f"ARTIFACT_MISSING:{label}:{relative}")
        actual.append(source_row(path, root))
    if actual != rows:
        raise VerificationError(f"ARTIFACT_ROWS_CHANGED:{label}")
    summary = {
        "count": len(rows),
        "bytes": sum(item["bytes"] for item in rows),
        "manifest_sha256": manifest_hash(rows),
    }
    for key in ("count", "bytes", "manifest_sha256"):
        if summary[key] != row.get(key):
            raise VerificationError(f"ARTIFACT_SUMMARY_CHANGED:{label}:{key}")
    return rows, summary


def verify_builds(receipt: dict) -> dict:
    build = receipt["build"]
    first = build["first"]
    replay = build["replay"]
    if first.get("exit_code") != 0 or replay.get("exit_code") != 0:
        raise VerificationError("BUILD_EXIT_NONZERO")
    first_out = verify_file(first["stdout"], "first.stdout").read_bytes()
    first_err = verify_file(first["stderr"], "first.stderr").read_bytes()
    replay_out = verify_file(replay["stdout"], "replay.stdout").read_bytes()
    replay_err = verify_file(replay["stderr"], "replay.stderr").read_bytes()
    first_root = Path(first["cwd"])
    replay_root = Path(replay["cwd"])
    stable_first, stable_first_summary = verify_artifact_manifest(
        first["stable_artifacts"], first_root, STABLE_SCHEMA, "first.stable"
    )
    stable_replay, stable_replay_summary = verify_artifact_manifest(
        replay["stable_artifacts"], replay_root, STABLE_SCHEMA, "replay.stable"
    )
    aux_first, aux_first_summary = verify_artifact_manifest(
        first["aux_artifacts"], first_root, AUX_SCHEMA, "first.aux"
    )
    aux_replay, aux_replay_summary = verify_artifact_manifest(
        replay["aux_artifacts"], replay_root, AUX_SCHEMA, "replay.aux"
    )
    comparison = build["comparison"]
    recomputed = {
        "stdout_exact": first_out == replay_out,
        "stderr_exact": first_err == replay_err,
        "stable_artifact_paths_and_hashes_exact": stable_first == stable_replay,
        "aux_artifact_path_sets_equal": [row["path"] for row in aux_first]
        == [row["path"] for row in aux_replay],
        "aux_artifact_hashes_exact": aux_first == aux_replay,
        "aux_nondeterministic_count": sum(
            left["sha256"] != right["sha256"]
            for left, right in zip(aux_first, aux_replay)
        ),
        "target_exact": first["target"] == replay["target"],
    }
    if recomputed != comparison:
        raise VerificationError("BUILD_COMPARISON_CHANGED")
    if not all(
        recomputed[key]
        for key in (
            "stdout_exact",
            "stderr_exact",
            "stable_artifact_paths_and_hashes_exact",
            "aux_artifact_path_sets_equal",
            "target_exact",
        )
    ):
        raise VerificationError("STABLE_BUILD_REPLAY_NOT_EXACT")
    if recomputed["aux_artifact_hashes_exact"]:
        raise VerificationError("AUX_NONDETERMINISM_EXPECTATION_CHANGED")
    for row, root, label in (
        (first["target"], first_root, "first.target"),
        (replay["target"], replay_root, "replay.target"),
    ):
        target = root / row["path"]
        data = target.read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["sha256"]:
            raise VerificationError(f"TARGET_CHANGED:{label}")
    return {
        "stable_artifacts": stable_first_summary,
        "aux_artifacts_first": aux_first_summary,
        "aux_artifacts_replay": aux_replay_summary,
        "comparison": recomputed,
        "target_sha256": first["target"]["sha256"],
    }


def verify_qualification(receipt: dict, rerun: bool) -> dict:
    row = receipt["qualification_probe"]
    source = verify_file(row["source"], "qualification.source")
    stdout = verify_file(row["stdout"], "qualification.stdout").read_bytes()
    stderr = verify_file(row["stderr"], "qualification.stderr").read_bytes()
    if row.get("exit_code") != 0 or stderr:
        raise VerificationError("QUALIFICATION_RECORDED_FAILURE")
    text = stdout.decode("utf-8")
    for constant in row["checked_constants"]:
        if constant not in text:
            raise VerificationError(f"QUALIFICATION_CONSTANT_MISSING:{constant}")
    if text.count("Closed under the global context") < 3:
        raise VerificationError("QUALIFICATION_ASSUMPTION_OUTPUT_MISSING")
    rerun_status = "NOT_REQUESTED"
    if rerun:
        completed = subprocess.run(row["argv"], capture_output=True, check=False)
        if completed.returncode != 0:
            raise VerificationError("QUALIFICATION_RERUN_EXIT_NONZERO")
        if completed.stdout != stdout or completed.stderr != stderr:
            raise VerificationError("QUALIFICATION_RERUN_OUTPUT_CHANGED")
        rerun_status = "EXACT_EXIT_STDOUT_STDERR_MATCH"
    return {
        "source_sha256": sha(source.read_bytes()),
        "constants": row["checked_constants"],
        "closed_under_global_context_occurrences": text.count(
            "Closed under the global context"
        ),
        "rerun": rerun_status,
    }


def verify(receipt_path: Path, rerun_qualification: bool) -> dict:
    receipt = read_json(receipt_path.resolve())
    if receipt.get("schema_version") != SCHEMA:
        raise VerificationError("RECEIPT_SCHEMA_INVALID")
    if receipt.get("verdict") != "NATIVE_COQ_BUILD_AND_CLEAN_REPLAY_PASS_WITH_SCOPE":
        raise VerificationError("RECEIPT_VERDICT_INVALID")
    verify_file(receipt["container"]["dockerfile"], "dockerfile")
    verify_file(receipt["environment"]["stdout"], "environment.stdout")
    verify_file(receipt["environment"]["stderr"], "environment.stderr")
    source = verify_source(receipt)
    images = {
        "base": verify_image(receipt["container"]["base_image"], "base"),
        "derived": verify_image(receipt["container"]["derived_image"], "derived"),
    }
    builds = verify_builds(receipt)
    qualification = verify_qualification(receipt, rerun_qualification)
    return {
        "status": "COQ_SYNTHETIC_INCOMPLETENESS_REPLAY_VALID",
        "evaluation_id": receipt["evaluation_id"],
        "source": source,
        "images": images,
        "builds": builds,
        "qualification": qualification,
        "scope": receipt["scope"],
        "non_goals": receipt["non_goals"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("verify", nargs="?")
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--rerun-qualification", action="store_true")
    args = parser.parse_args()
    try:
        result = verify(args.receipt, args.rerun_qualification)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (VerificationError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
