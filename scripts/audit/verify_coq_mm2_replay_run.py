#!/usr/bin/env python3
"""Verify and optionally replay the byte-preserved external Coq MM2 run."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUN = Path("HoTT/verification/runs/20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01")
IMPORTER = ROOT / "scripts/audit/import_coq_undecidability_mm2.py"
REQUIRED = {"RUN.json", "stdout.txt", "stderr.txt", "environment.txt", "source-manifest.json", "index-row-manifest.json"}
RUN_PROFILES = {
    "20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01": {
        "proof_id": "MP-COQ-MM2-UNDECIDABILITY-REPLAY-001",
        "claim_ids": ["C-208"],
        "stdout_markers": [
            b"MM2_HALTING_undec",
            b"Undecidability.undecidable MM2.MM2_HALTING",
        ],
        "profile": "UPSTREAM_MM2_THEOREM_REPLAY",
    },
    "20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01": {
        "proof_id": "MP-COQ-MM2-PROGRAMCODE-BRIDGE-001",
        "claim_ids": ["C-214", "C-215", "C-216", "C-217", "C-218"],
        "stdout_markers": [
            b"MM2_to_PC_HALTING",
            b"MM2_HALTING \xe2\xaa\xaf PC_HALTING",
            b"PC_HALTING_undec",
            b"undecidable PC_HALTING",
        ],
        "profile": "SAME_KERNEL_PROGRAMCODE_REDUCTION",
    },
}


class VerificationError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str) -> Path:
    parsed = PurePosixPath(value)
    if not value or parsed.is_absolute() or any(part in {"", ".", ".."} for part in parsed.parts):
        raise VerificationError(f"UNSAFE_PATH:{value}")
    return Path(*parsed.parts)


def read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError(f"INVALID_JSON:{path}") from exc
    if not isinstance(value, dict):
        raise VerificationError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def check_artifact(run_dir: Path, row: object, label: str) -> bytes:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise VerificationError(f"ARTIFACT_ROW_INVALID:{label}")
    path = run_dir / safe_relative(str(row["path"]))
    if not path.is_file() or path.is_symlink():
        raise VerificationError(f"ARTIFACT_MISSING:{label}")
    data = path.read_bytes()
    if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
        raise VerificationError(f"ARTIFACT_IDENTITY_MISMATCH:{label}")
    return data


def unique_index_line(lines: list[str], identity: str, kind: str) -> str:
    prefix = f"| `{identity}` |" if kind == "proof" else f"| {identity} |"
    matches = [line for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise VerificationError(f"INDEX_ROW_COUNT:{identity}:{len(matches)}")
    return matches[0]


def verify(run_relative: Path, rerun: bool) -> dict[str, object]:
    try:
        run_relative.relative_to(Path("HoTT/verification/runs"))
    except ValueError as exc:
        raise VerificationError("RUN_OUTSIDE_AUTHORITATIVE_ROOT") from exc
    run_dir = ROOT / run_relative
    if not run_dir.is_dir() or run_dir.is_symlink():
        raise VerificationError("RUN_DIRECTORY_INVALID")
    if not REQUIRED <= {path.name for path in run_dir.iterdir() if path.is_file()}:
        raise VerificationError("RUN_REQUIRED_FILES_MISSING")
    profile = RUN_PROFILES.get(run_dir.name)
    if profile is None:
        raise VerificationError(f"UNSUPPORTED_RUN:{run_dir.name}")
    run = read_json(run_dir / "RUN.json")
    if (
        run.get("schema_version") != "formal-proof-run/v1"
        or run.get("run_id") != run_dir.name
        or run.get("proof_id") != profile["proof_id"]
        or run.get("claim_ids") != profile["claim_ids"]
        or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("exit_code") != 0
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
    ):
        raise VerificationError("RUN_IDENTITY_OR_STATUS_INVALID")
    stdout = check_artifact(run_dir, run.get("stdout"), "stdout")
    stderr = check_artifact(run_dir, run.get("stderr"), "stderr")
    check_artifact(run_dir, run.get("environment"), "environment")
    manifest_data = check_artifact(run_dir, run.get("source_manifest"), "source_manifest")
    manifest = json.loads(manifest_data.decode("utf-8"))
    if (
        manifest.get("schema_version") != "formal-proof-source-manifest/v1"
        or manifest.get("proof_id") != run["proof_id"]
        or manifest.get("run_id") != run["run_id"]
    ):
        raise VerificationError("SOURCE_MANIFEST_IDENTITY_INVALID")
    rows = manifest.get("files")
    if not isinstance(rows, list) or not rows:
        raise VerificationError("SOURCE_ROWS_MISSING")
    source_paths = []
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str):
            raise VerificationError("SOURCE_ROW_INVALID")
        relative = safe_relative(str(row["path"]))
        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            raise VerificationError(f"SOURCE_MISSING:{relative}")
        data = path.read_bytes()
        if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
            raise VerificationError(f"SOURCE_IDENTITY_MISMATCH:{relative}")
        if path.suffix in {".v", ".py", ".md", ".json"}:
            data.decode("utf-8")
        source_paths.append(relative.as_posix())

    spec = importlib.util.spec_from_file_location("coq_mm2_importer_verify", IMPORTER)
    if spec is None or spec.loader is None:
        raise VerificationError("IMPORTER_LOAD_FAILED")
    manager = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(manager)
    qualified, tree_manifest = manager.qualify_version("replay", manager.VERSIONS["replay"])
    external = manifest.get("external_dependencies")
    if not isinstance(external, list) or len(external) != 2:
        raise VerificationError("EXTERNAL_DEPENDENCIES_INVALID")
    by_label = {row.get("label"): row for row in external if isinstance(row, dict)}
    archive_row = by_label.get("coq-undecidability-codeload-archive")
    tree_row = by_label.get("coq-undecidability-extracted-tree")
    if not isinstance(archive_row, dict) or not isinstance(tree_row, dict):
        raise VerificationError("EXTERNAL_LABELS_MISSING")
    archive_path = Path(str(archive_row.get("local_path", "")))
    archive_data = archive_path.read_bytes()
    if archive_row.get("bytes") != len(archive_data) or archive_row.get("sha256") != sha(archive_data):
        raise VerificationError("EXTERNAL_ARCHIVE_MISMATCH")
    expected_tree = {key: tree_row.get(key) for key in ("file_count", "total_bytes", "tree_sha256")}
    actual_tree = {key: tree_manifest[key] for key in ("file_count", "total_bytes", "tree_sha256")}
    if actual_tree != expected_tree or tree_row.get("upstream_commit") != qualified["commit"] or tree_row.get("git_tree") != qualified["git_tree"]:
        raise VerificationError("EXTERNAL_TREE_MISMATCH")

    index = run.get("index")
    if not isinstance(index, dict) or index.get("path") != "HoTT/CLAIM_EVIDENCE_MATRIX.md":
        raise VerificationError("INDEX_METADATA_INVALID")
    index_data = (ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md").read_bytes()
    index_text = index_data.decode("utf-8")
    frozen = read_json(run_dir / "index-row-manifest.json")
    if (
        frozen.get("schema_version") != "proof-index-row-manifest/v1"
        or frozen.get("run_id") != run["run_id"]
        or frozen.get("proof_id") != run["proof_id"]
        or frozen.get("claim_ids") != run["claim_ids"]
        or frozen.get("index_snapshot_sha256") != index.get("sha256")
    ):
        raise VerificationError("INDEX_ROW_MANIFEST_IDENTITY_INVALID")
    expected_rows = [
        ("proof", str(run["proof_id"])),
        *(("claim", claim_id) for claim_id in run["claim_ids"]),
    ]
    manifest_rows = frozen.get("rows")
    if not isinstance(manifest_rows, list) or len(manifest_rows) != len(expected_rows):
        raise VerificationError("INDEX_ROW_MANIFEST_COUNT_INVALID")
    lines = index_text.splitlines()
    for row, (kind, identity) in zip(manifest_rows, expected_rows, strict=True):
        if not isinstance(row, dict) or row.get("kind") != kind or row.get("id") != identity:
            raise VerificationError(f"INDEX_ROW_ORDER_INVALID:{identity}")
        line = unique_index_line(lines, identity, kind)
        if row.get("line_sha256") != sha(line.encode("utf-8")):
            raise VerificationError(f"INDEX_ROW_CHANGED:{identity}")

    required_stdout = [
        b"The Coq Proof Assistant, version 8.15.2",
        *profile["stdout_markers"],
        b"Closed under the global context",
    ]
    if any(marker not in stdout for marker in required_stdout):
        raise VerificationError("KERNEL_OUTPUT_MARKER_MISSING")
    expected_warnings = [b"L/Tactics/Extract.v", b"L/Tactics/GenEncode.v"]
    if any(marker not in stderr for marker in expected_warnings):
        raise VerificationError("EXPECTED_COQDEP_WARNING_SET_CHANGED")

    replay = "NOT_RUN"
    if rerun:
        command = run.get("command_argv")
        if not isinstance(command, list) or any(not isinstance(item, str) for item in command):
            raise VerificationError("COMMAND_ARGV_INVALID")
        result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
        if result.returncode != 0 or result.stdout != stdout or result.stderr != stderr:
            raise VerificationError("EXACT_REPLAY_MISMATCH")
        replay = "EXACT_EXIT_STDOUT_STDERR_MATCH"
    return {
        "status": "PASS_WITH_SCOPE",
        "schema_version": "coq-mm2-replay-verification/v1",
        "profile": profile["profile"],
        "run_id": run["run_id"],
        "proof_id": run["proof_id"],
        "claim_ids": run["claim_ids"],
        "source_files": len(source_paths),
        "external_tree_files": actual_tree["file_count"],
        "upstream_commit": qualified["commit"],
        "upstream_git_tree": qualified["git_tree"],
        "kernel_status": run["status"],
        "assumptions": "CLOSED_UNDER_GLOBAL_CONTEXT",
        "definition_boundary": "undecidable P := decidable P -> enumerable (complement SBTM_HALT)",
        "license_encoding": "ORIGINAL_ISO_8859_BYTES_PRESERVED",
        "coqdep_warnings": ["L/Tactics/Extract.v", "L/Tactics/GenEncode.v"],
        "index_validation": "ROW_STABLE_AFTER_INDEX_EVOLUTION",
        "replay": replay,
        "git_status": run.get("git_status"),
        "scope": run.get("scope"),
        "non_goals": run.get("non_goals"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", default=DEFAULT_RUN.as_posix())
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()
    try:
        result = verify(safe_relative(args.run_dir), args.rerun)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (VerificationError, OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
