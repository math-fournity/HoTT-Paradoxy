#!/usr/bin/env python3
"""Verify one persisted F-011 proof run and optionally replay its exact command."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
REQUIRED = {"RUN.json", "stdout.txt", "stderr.txt", "environment.txt", "source-manifest.json"}
EXTERNAL_TREE_LABELS = {
    "cubical-extracted-tree",
    "agda-unimath-extracted-tree",
    "coq-undecidability-extracted-tree",
    "coq-parametric-ct-extracted-tree",
    "cubical-groupoid-syntax-extracted-tree",
    # The Foundation Lean ZF model is an external source tree.  A source
    # manifest that invokes it must pin the tree itself, not merely a README
    # or a lockfile, because the theorem imports its `Seq` implementation.
    "foundation-lean-zf-source-tree",
}
AUDIT_TOOL_PROVENANCE_PATHS = {
    # This verifier is recorded so the historical audit procedure is visible,
    # but it is not read by RUN.command_argv and is not a proof input.  Its
    # evolution must not masquerade as theorem-source drift.
    "scripts/audit/verify_formal_proof_run.py",
    # Capture programs determine how a historical receipt was written but are
    # not invoked by that receipt's command.  Preserve their old hash in the
    # manifest while allowing later capture-tool maintenance to be reported as
    # provenance drift rather than theorem-source drift.
    "scripts/audit/capture_agda_proof_run.py",
}


class ProofRunError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ProofRunError(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ProofRunError(f"INVALID_JSON:{path}") from exc
    if not isinstance(value, dict):
        raise ProofRunError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def deterministic_tree(root: Path) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise ProofRunError(f"EXTERNAL_TREE_INVALID:{root}")
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


def check_external_dependency(row: object) -> str:
    if not isinstance(row, dict) or not isinstance(row.get("label"), str) or not isinstance(row.get("local_path"), str):
        raise ProofRunError("EXTERNAL_DEPENDENCY_ROW_INVALID")
    label = str(row["label"])
    path = Path(str(row["local_path"]))
    if not path.is_absolute() or path.is_symlink():
        raise ProofRunError(f"EXTERNAL_DEPENDENCY_PATH_INVALID:{label}")
    if label in EXTERNAL_TREE_LABELS:
        actual = deterministic_tree(path)
        expected = {key: row.get(key) for key in ("file_count", "total_bytes", "tree_sha256")}
        if actual != expected:
            raise ProofRunError(f"EXTERNAL_TREE_MISMATCH:{label}")
    else:
        if not path.is_file():
            raise ProofRunError(f"EXTERNAL_FILE_MISSING:{label}")
        data = path.read_bytes()
        if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
            raise ProofRunError(f"EXTERNAL_FILE_MISMATCH:{label}")
        publisher_digest = row.get("publisher_digest")
        if publisher_digest is not None and publisher_digest != row.get("sha256"):
            raise ProofRunError(f"PUBLISHER_DIGEST_MISMATCH:{label}")
    return label


def unique_index_line(lines: list[str], identity: str, kind: str) -> str:
    prefix = f"| `{identity}` |" if kind == "proof" else f"| {identity} |"
    matches = [line for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise ProofRunError(f"INDEX_ROW_COUNT:{identity}:{len(matches)}")
    return matches[0]


def validate_index_rows(run_dir: Path, run: dict[str, object], index_text: str, indexed_snapshot_sha: str) -> str:
    manifest_path = run_dir / "index-row-manifest.json"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        raise ProofRunError("INDEX_EVOLVED_WITHOUT_ROW_MANIFEST")
    manifest = read_json(manifest_path)
    proof_id = str(run["proof_id"])
    claim_ids = list(map(str, run["claim_ids"]))
    if (
        manifest.get("schema_version") != "proof-index-row-manifest/v1"
        or manifest.get("run_id") != run.get("run_id")
        or manifest.get("proof_id") != proof_id
        or manifest.get("claim_ids") != claim_ids
        or manifest.get("index_path") != "HoTT/CLAIM_EVIDENCE_MATRIX.md"
        or manifest.get("index_snapshot_sha256") != indexed_snapshot_sha
    ):
        raise ProofRunError("INDEX_ROW_MANIFEST_IDENTITY_INVALID")
    rows = manifest.get("rows")
    expected = [("proof", proof_id), *(('claim', claim_id) for claim_id in claim_ids)]
    if not isinstance(rows, list) or len(rows) != len(expected):
        raise ProofRunError("INDEX_ROW_MANIFEST_COUNT_INVALID")
    lines = index_text.splitlines()
    for row, (kind, identity) in zip(rows, expected, strict=True):
        if not isinstance(row, dict) or row.get("kind") != kind or row.get("id") != identity:
            raise ProofRunError(f"INDEX_ROW_MANIFEST_ORDER_INVALID:{identity}")
        line = unique_index_line(lines, identity, kind)
        if row.get("line_sha256") != sha(line.encode("utf-8")):
            raise ProofRunError(f"INDEX_ROW_CHANGED:{identity}")
    return "ROW_STABLE_AFTER_INDEX_EVOLUTION"


def check_artifact(run_dir: Path, row: object, label: str) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise ProofRunError(f"ARTIFACT_ROW_INVALID:{label}")
    relative = safe_relative(str(row["path"]))
    path = run_dir / relative
    if not path.is_file() or path.is_symlink():
        raise ProofRunError(f"ARTIFACT_MISSING_OR_SYMLINK:{label}:{relative}")
    data = path.read_bytes()
    if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
        raise ProofRunError(f"ARTIFACT_HASH_OR_SIZE_MISMATCH:{label}")
    return path


def agda_options(source: str) -> list[str]:
    """Read OPTIONS outside nested comments and string/character literals.

    This is an option-provenance check, not a replacement for Agda's lexer or
    kernel. Actual accepted runs and their source/command identities remain
    required. In particular, a string containing a fake pragma grants no flag.
    """
    flags: list[str] = []
    i, depth, n = 0, 0, len(source)
    while i < n:
        if depth:
            if source.startswith("{-", i):
                depth += 1; i += 2
            elif source.startswith("-}", i):
                depth -= 1; i += 2
            else:
                i += 1
        elif source.startswith("--", i):
            stop = source.find("\n", i)
            i = n if stop < 0 else stop + 1
        elif source.startswith("{-#", i):
            end = source.find("#-}", i + 3)
            if end < 0:
                raise ProofRunError("AGDA_UNTERMINATED_PRAGMA")
            match = re.fullmatch(r"\{-#\s*OPTIONS\b(.*?)#-\}", source[i:end + 3], re.S)
            if match:
                flags.extend(match.group(1).split())
            i = end + 3
        elif source.startswith("{-", i):
            depth = 1; i += 2
        elif source[i] == '"':
            i += 1
            while i < n:
                if source[i] == "\\":
                    i += 2
                elif source[i] == '"':
                    i += 1; break
                else:
                    i += 1
        elif source[i] == "'" and (m := re.match(r"'(?:\\.|[^'\\\n])'", source[i:])):
            # A primed identifier (x') is not a character literal.
            i += len(m.group(0))
        else:
            i += 1
    return flags


def validate(root: Path, run_relative: Path, rerun: bool) -> dict[str, object]:
    root = root.resolve()
    expected_prefix = Path("HoTT/verification/runs")
    try:
        run_relative.relative_to(expected_prefix)
    except ValueError as exc:
        raise ProofRunError("RUN_OUTSIDE_AUTHORITATIVE_ROOT") from exc
    run_dir = root / run_relative
    if not run_dir.is_dir() or run_dir.is_symlink():
        raise ProofRunError("RUN_DIRECTORY_INVALID")
    if not REQUIRED <= {path.name for path in run_dir.iterdir() if path.is_file()}:
        raise ProofRunError("RUN_REQUIRED_FILES_MISSING")

    run = read_json(run_dir / "RUN.json")
    if run.get("schema_version") != "formal-proof-run/v1":
        raise ProofRunError("RUN_SCHEMA_INVALID")
    if run.get("run_id") != run_dir.name:
        raise ProofRunError("RUN_ID_DIRECTORY_MISMATCH")
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("exit_code") != 0:
        raise ProofRunError("RUN_NOT_KERNEL_ACCEPTED")
    if run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise ProofRunError("RUN_NOT_INDEXED")
    proof_id = run.get("proof_id")
    claim_ids = run.get("claim_ids")
    if not isinstance(proof_id, str) or not proof_id or not isinstance(claim_ids, list) or not claim_ids:
        raise ProofRunError("PROOF_OR_CLAIM_IDS_INVALID")
    if len(claim_ids) != len(set(claim_ids)) or any(not isinstance(item, str) or not item for item in claim_ids):
        raise ProofRunError("CLAIM_IDS_INVALID_OR_DUPLICATE")

    stdout_path = check_artifact(run_dir, run.get("stdout"), "stdout")
    stderr_path = check_artifact(run_dir, run.get("stderr"), "stderr")
    check_artifact(run_dir, run.get("environment"), "environment")
    source_manifest_path = check_artifact(run_dir, run.get("source_manifest"), "source_manifest")
    source_manifest = read_json(source_manifest_path)
    if source_manifest.get("schema_version") != "formal-proof-source-manifest/v1" or source_manifest.get("proof_id") != proof_id or source_manifest.get("run_id") != run.get("run_id"):
        raise ProofRunError("SOURCE_MANIFEST_IDENTITY_INVALID")
    source_rows = source_manifest.get("files")
    if not isinstance(source_rows, list) or not source_rows:
        raise ProofRunError("SOURCE_MANIFEST_FILES_MISSING")
    source_paths: list[str] = []
    audit_tool_provenance_drift: list[dict[str, str]] = []
    for row in source_rows:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str):
            raise ProofRunError("SOURCE_ROW_INVALID")
        relative = safe_relative(str(row["path"]))
        path = root / relative
        if not path.is_file() or path.is_symlink():
            raise ProofRunError(f"SOURCE_MISSING_OR_SYMLINK:{relative}")
        data = path.read_bytes()
        if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
            if relative.as_posix() in AUDIT_TOOL_PROVENANCE_PATHS:
                audit_tool_provenance_drift.append({
                    "path": relative.as_posix(),
                    "captured_sha256": str(row.get("sha256")),
                    "current_sha256": sha(data),
                })
                source_paths.append(relative.as_posix())
                continue
            raise ProofRunError(f"SOURCE_HASH_OR_SIZE_MISMATCH:{relative}")
        if path.suffix == ".lean":
            text_data = data.decode("utf-8")
            if re.search(r"\b(sorry|admit)\b", text_data):
                raise ProofRunError(f"LEAN_PLACEHOLDER_FORBIDDEN:{relative}")
        if path.suffix == ".agda":
            text_data = data.decode("utf-8")
            forbidden = (
                "{!!}", "{-# TERMINATING #-}", "{-# NON_TERMINATING #-}",
                "--allow-unsolved-metas", "--allow-incomplete-matches", "--type-in-type",
                "--no-positivity-check", "--no-termination-check", "--no-universe-check",
            )
            for marker in forbidden:
                if marker in text_data:
                    raise ProofRunError(f"AGDA_UNSAFE_OR_INCOMPLETE_MARKER:{relative}:{marker}")
            theory = str(run.get("theory_variant", "")).lower()
            pragma_flags = agda_options(text_data)
            # Branch on the most specific marker first: a without-K run may
            # legitimately describe itself as having "no cubical features",
            # so the substring "cubical" alone must not select the cubical
            # requirement.
            if "agda-flat" in theory:
                # Historical Agda-flat packages use a modal crisp-variable
                # extension and mix ordinary --without-K modules with
                # --rewriting/--no-pattern-matching entrypoints.  There is no
                # single source pragma shared by every file in that closure.
                # The run-specific replay must pin and verify the exact
                # Agda-flat image and source tree; the generic verifier still
                # enforces the unsafe/incomplete-marker checks above.
                pass
            elif "without-k" in theory:
                if "--without-K" not in pragma_flags or "--exact-split" not in pragma_flags:
                    raise ProofRunError(f"AGDA_WITHOUT_K_OPTIONS_REQUIRED:{relative}")
            elif "cubical" in theory:
                if "--safe" not in pragma_flags or "--cubical" not in pragma_flags:
                    raise ProofRunError(f"AGDA_SAFE_CUBICAL_PRAGMA_REQUIRED:{relative}")
            else:
                raise ProofRunError(f"AGDA_THEORY_VARIANT_UNSUPPORTED:{relative}:{run.get('theory_variant')}")
        source_paths.append(relative.as_posix())

    external_rows = source_manifest.get("external_dependencies", [])
    if not isinstance(external_rows, list):
        raise ProofRunError("EXTERNAL_DEPENDENCIES_INVALID")
    external_labels = [check_external_dependency(row) for row in external_rows]

    index = run.get("index")
    if not isinstance(index, dict) or not isinstance(index.get("path"), str):
        raise ProofRunError("INDEX_ROW_MISSING")
    index_relative = safe_relative(str(index["path"]))
    if index_relative.as_posix() != "HoTT/CLAIM_EVIDENCE_MATRIX.md":
        raise ProofRunError("INDEX_PATH_INVALID")
    index_path = root / index_relative
    index_data = index_path.read_bytes()
    indexed_snapshot_sha = index.get("sha256")
    if not isinstance(indexed_snapshot_sha, str):
        raise ProofRunError("INDEX_SNAPSHOT_HASH_MISSING")
    index_text = index_data.decode("utf-8")
    for identity in [proof_id, str(run["run_id"]), *map(str, claim_ids)]:
        if identity not in index_text:
            raise ProofRunError(f"INDEX_IDENTITY_MISSING:{identity}")
    if indexed_snapshot_sha == sha(index_data):
        index_validation = "EXACT_INDEX_SNAPSHOT_MATCH"
    else:
        index_validation = validate_index_rows(run_dir, run, index_text, indexed_snapshot_sha)

    replay = "NOT_RUN"
    if rerun:
        command = run.get("command_argv")
        if not isinstance(command, list) or len(command) < 2 or any(not isinstance(arg, str) or not arg for arg in command):
            raise ProofRunError("COMMAND_ARGV_INVALID")
        result = subprocess.run(command, cwd=root, capture_output=True, check=False)
        if result.returncode != run.get("exit_code"):
            raise ProofRunError("REPLAY_EXIT_MISMATCH")
        if result.stdout != stdout_path.read_bytes() or result.stderr != stderr_path.read_bytes():
            raise ProofRunError("REPLAY_OUTPUT_MISMATCH")
        replay = "EXACT_EXIT_STDOUT_STDERR_MATCH"

    return {
        "status": "PASS_WITH_SCOPE",
        "schema_version": "formal-proof-run-verification/v1",
        "run_id": run["run_id"],
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "source_paths": source_paths,
        "audit_tool_provenance_drift": audit_tool_provenance_drift,
        "external_dependencies": external_labels,
        "kernel_status": run["status"],
        "index_status": run["index_status"],
        "index_validation": index_validation,
        "replay": replay,
        "git_status": run.get("git_status"),
        "scope": run.get("scope"),
        "non_goals": run.get("non_goals"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()
    try:
        result = validate(args.project_root, safe_relative(args.run_dir), args.rerun)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ProofRunError, OSError, UnicodeError, ValueError, TypeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
