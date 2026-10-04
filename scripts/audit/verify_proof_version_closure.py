#!/usr/bin/env python3
"""Verify frozen and post-snapshot proof evidence without re-running mathematics.

The v2 registry contract checks both file integrity and evidence relationships.
For every ``later_packages`` entry it binds the registry row to the RUN receipt,
source manifest, exact proof/claim row manifest, unique matrix rows, compiler
command and any historical dependency-gap exception. A valid proof run cannot
therefore be exchanged with another package, shrink its frozen claim set, or
inherit a dependency exception that belonged to an older run.

``replay_runs`` records a replay of already-indexed claims without rewriting the
primary matrix rows. Replay entries receive the same identity and integrity
checks as primary later packages. This script proves the stated Git/evidence
closure only; it does not ask the proof assistant to check the mathematics again.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import proof_claim_ids as claim_identity
import verify_formal_proof_run as formal_run
REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
INDEX_REL = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
RUN_ROOT = PurePosixPath("HoTT/verification/runs")
AUDIT_TOOL_PROVENANCE_PATHS = {
    "scripts/audit/verify_formal_proof_run.py",
    # Historical Agda captures record this writer for auditability, but the
    # recorded proof command invokes the pinned Agda binary and sources, not
    # this later-evolving capture program.
    "scripts/audit/capture_agda_proof_run.py",
}


class ClosureError(RuntimeError):
    pass


def run_git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if result.returncode != 0:
        raise ClosureError(
            f"GIT_FAILED:{' '.join(args)}:{result.stderr.decode(errors='replace').strip()}"
        )
    return result.stdout


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ClosureError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def safe_rel(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise ClosureError(f"UNSAFE_RELATIVE_PATH:{label}:{value}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ClosureError(f"UNSAFE_RELATIVE_PATH:{label}:{value}")
    return path.as_posix()


def expand_claim_ids(value: object) -> list[str]:
    try:
        return claim_identity.expand_claim_ids(value)
    except ValueError as exc:
        raise ClosureError(str(exc)) from exc


def matrix_identity_lines(data: bytes) -> dict[str, list[str]]:
    return claim_identity.matrix_identity_lines(data)


def unique_matrix_line(index: dict[str, list[str]], identity: str) -> str:
    matches = index.get(identity, [])
    if len(matches) != 1:
        raise ClosureError(f"MATRIX_IDENTITY_NOT_UNIQUE:{identity}:{len(matches)}")
    return matches[0]


def package_map(registry: dict) -> dict[str, dict]:
    rows: list[dict] = []
    for key in ("packages", "later_packages"):
        value = registry.get(key)
        if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
            raise ClosureError(f"{key.upper()}_INVALID")
        rows.extend(value)
    mapping: dict[str, dict] = {}
    claimed: dict[str, str] = {}
    for row in rows:
        proof_id = row.get("proof_id")
        if not isinstance(proof_id, str) or proof_id in mapping:
            raise ClosureError(f"PROOF_ID_DUPLICATE_OR_INVALID:{proof_id}")
        claims = expand_claim_ids(row.get("claim_ids"))
        for claim in claims:
            if claim in claimed:
                raise ClosureError(f"CLAIM_ID_REGISTERED_TWICE:{claim}:{claimed[claim]}:{proof_id}")
            claimed[claim] = proof_id
        mapping[proof_id] = row
    return mapping


def load_gap_allowlist(registry: dict) -> dict[tuple[str, str, str], dict]:
    spec = registry.get("later_package_dependency_gap_allowlist")
    if (
        not isinstance(spec, dict)
        or spec.get("schema_version") != "proof-dependency-gap-allowlist/v2"
        or not isinstance(spec.get("entries"), list)
    ):
        raise ClosureError("LATER_DEPENDENCY_GAP_ALLOWLIST_INVALID")
    output: dict[tuple[str, str, str], dict] = {}
    required = {
        "proof_id",
        "run_id",
        "module",
        "missing_path",
        "missing_sha256",
        "source_manifest_sha256",
        "stdout_sha256",
    }
    for row in spec["entries"]:
        if not isinstance(row, dict) or not required <= set(row):
            raise ClosureError("LATER_DEPENDENCY_GAP_ENTRY_INVALID")
        key = (row.get("proof_id"), row.get("run_id"), row.get("module"))
        if not all(isinstance(part, str) and part for part in key) or key in output:
            raise ClosureError(f"LATER_DEPENDENCY_GAP_ENTRY_IDENTITY_INVALID:{key}")
        missing_rel = safe_rel(row["missing_path"], "dependency-gap")
        missing = ROOT / missing_rel
        if not missing.is_file() or sha(missing.read_bytes()) != row.get("missing_sha256"):
            raise ClosureError(f"LATER_DEPENDENCY_GAP_SOURCE_DRIFT:{key[0]}:{key[1]}:{key[2]}")
        if Path(missing_rel).stem != key[2].split(".")[-1]:
            raise ClosureError(f"LATER_DEPENDENCY_GAP_MODULE_PATH_MISMATCH:{key[0]}:{key[1]}:{key[2]}")
        output[key] = row
    return output


def stdout_modules(text: str) -> set[str]:
    names: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"\s*Checking\s+(\S+)\s*\(", line)
        if match:
            names.add(match.group(1))
    return names


def checked_module_paths(text: str) -> dict[str, str]:
    """Retain the actual paths; a matching basename is not dependency evidence."""
    found: dict[str, str] = {}
    for line in text.splitlines():
        match = re.fullmatch(r"\s*Checking\s+(\S+)\s*\((.+)\)\.?", line)
        if not match:
            continue
        name, path = match.groups()
        if name in found and found[name] != path:
            raise ClosureError(f"CHECKED_MODULE_PATH_CONFLICT:{name}")
        found[name] = path
    return found


def observed_dependency_coverage(
    stdout: str, receipt: dict, manifest: dict, paths: list[str],
    gap_allowlist: dict[tuple[str, str, str], dict],
) -> dict[str, object]:
    proof_id, run_id = receipt["proof_id"], receipt["run_id"]
    cwd = receipt.get("cwd")
    if not isinstance(cwd, str) or not Path(cwd).is_absolute():
        raise ClosureError(f"RUN_CWD_INVALID:{proof_id}")
    external = manifest.get("external_dependencies", [])
    if not isinstance(external, list):
        raise ClosureError(f"EXTERNAL_DEPENDENCIES_INVALID:{proof_id}")
    trees: list[Path] = []
    for row in external:
        try:
            formal_run.check_external_dependency(row)
        except (formal_run.ProofRunError, OSError, ValueError) as exc:
            raise ClosureError(f"EXTERNAL_DEPENDENCY_INVALID:{proof_id}:{exc}") from exc
        if row["label"] in formal_run.EXTERNAL_TREE_LABELS:
            trees.append(Path(row["local_path"]))
    used: set[tuple[str, str, str]] = set()
    local_count = external_count = 0
    for module, raw in checked_module_paths(stdout).items():
        captured = Path(raw)
        if not captured.is_absolute():
            captured = Path(cwd) / captured
        if ".." in captured.parts:
            raise ClosureError(f"CHECKED_MODULE_PATH_TRAVERSAL:{module}")
        try:
            rel = captured.relative_to(Path(cwd)).as_posix()
        except ValueError:
            rel = None
        if rel is not None:
            if rel in paths:
                # The manifest bytes/hash have already been verified above.
                local_count += 1
                continue
            key = (proof_id, run_id, module)
            exception = gap_allowlist.get(key)
            if exception is None:
                raise ClosureError(f"LATER_DEPENDENCY_GAP_NOT_ALLOWLISTED:{proof_id}:{run_id}:{module}:{rel}")
            if (exception.get("missing_path") != rel
                or exception.get("source_manifest_sha256") != receipt["source_manifest"]["sha256"]
                or exception.get("stdout_sha256") != receipt["stdout"]["sha256"]):
                raise ClosureError(f"LATER_DEPENDENCY_GAP_EXCEPTION_IDENTITY_MISMATCH:{proof_id}:{run_id}:{module}")
            used.add(key)
            continue
        matches = []
        for tree in trees:
            try:
                suffix = captured.relative_to(tree)
            except ValueError:
                continue
            cursor = tree
            for component in suffix.parts:
                cursor /= component
                if cursor.is_symlink():
                    raise ClosureError(f"EXTERNAL_MODULE_SYMLINK:{module}:{raw}")
            if captured.is_file() and captured.suffix != ".agdai" and captured.name != ".DS_Store":
                matches.append(tree)
        if not matches:
            raise ClosureError(f"CHECKED_MODULE_NOT_PINNED:{proof_id}:{module}:{raw}")
        external_count += 1
    return {"local_modules": local_count, "external_modules": external_count,
            "used_gap_keys": used, "dependency_gaps": len(used)}


def receipt_file(run_dir: Path, receipt: dict, key: str, proof_id: str) -> Path:
    row = receipt.get(key)
    expected_name = {
        "stdout": "stdout.txt",
        "stderr": "stderr.txt",
        "environment": "environment.txt",
        "source_manifest": "source-manifest.json",
    }[key]
    if not isinstance(row, dict) or row.get("path") != expected_name:
        raise ClosureError(f"LATER_RECEIPT_FIELD_INVALID:{proof_id}:{key}")
    path = run_dir / expected_name
    if not path.is_file():
        raise ClosureError(f"LATER_RUN_FILE_MISSING:{proof_id}:{expected_name}")
    data = path.read_bytes()
    if row.get("bytes") != len(data) or row.get("sha256") != sha(data):
        raise ClosureError(f"LATER_RUN_FILE_HASH_DRIFT:{proof_id}:{expected_name}")
    return path


def check_later_package(
    run_dir: Path,
    registry_row: dict,
    gap_allowlist: dict[tuple[str, str, str], dict],
    matrix_index: dict[str, list[str]] | None = None,
) -> dict[str, object]:
    """Check one later package or registered replay and return used exceptions."""
    proof_id = registry_row.get("proof_id")
    if not isinstance(proof_id, str):
        raise ClosureError("LATER_PACKAGE_PROOF_ID_INVALID")
    run_rel = safe_rel(registry_row.get("run"), f"run:{proof_id}")
    expected_run_id = PurePosixPath(run_rel).name
    try:
        PurePosixPath(run_rel).relative_to(RUN_ROOT)
    except ValueError as exc:
        raise ClosureError(f"LATER_RUN_OUTSIDE_ROOT:{proof_id}:{run_rel}") from exc
    if run_dir.resolve() != (ROOT / run_rel).resolve():
        raise ClosureError(f"LATER_RUN_PATH_MISMATCH:{proof_id}:{run_rel}")
    if not run_dir.is_dir():
        raise ClosureError(f"LATER_RUN_DIRECTORY_MISSING:{proof_id}:{run_rel}")

    expected_claims = expand_claim_ids(registry_row.get("claim_ids"))
    source_rel = safe_rel(registry_row.get("source"), f"source:{proof_id}")
    toolchain_value = registry_row.get("toolchain")
    toolchain_rel = safe_rel(toolchain_value, f"toolchain:{proof_id}") if toolchain_value else None

    receipt = load(run_dir / "RUN.json")
    if receipt.get("run_id") != expected_run_id:
        raise ClosureError(f"LATER_RUN_ID_MISMATCH:{proof_id}:{receipt.get('run_id')}:{expected_run_id}")
    if receipt.get("proof_id") != proof_id:
        raise ClosureError(f"LATER_RUN_PROOF_ID_MISMATCH:{proof_id}:{receipt.get('proof_id')}")
    if receipt.get("claim_ids") != expected_claims:
        raise ClosureError(f"LATER_RUN_CLAIMS_MISMATCH:{proof_id}")
    if receipt.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or receipt.get("exit_code") != 0:
        raise ClosureError(f"LATER_PACKAGE_RUN_NOT_ACCEPTED:{proof_id}")
    if receipt.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise ClosureError(f"LATER_PACKAGE_RUN_NOT_INDEXED:{proof_id}")
    if not isinstance(receipt.get("index"), dict) or receipt["index"].get("path") != INDEX_REL:
        raise ClosureError(f"LATER_RUN_INDEX_IDENTITY_INVALID:{proof_id}")

    stdout_path = receipt_file(run_dir, receipt, "stdout", proof_id)
    receipt_file(run_dir, receipt, "stderr", proof_id)
    receipt_file(run_dir, receipt, "environment", proof_id)
    manifest_path = receipt_file(run_dir, receipt, "source_manifest", proof_id)

    manifest = load(manifest_path)
    if manifest.get("proof_id") != proof_id or manifest.get("run_id") != expected_run_id:
        raise ClosureError(f"LATER_SOURCE_MANIFEST_IDENTITY_MISMATCH:{proof_id}")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise ClosureError(f"LATER_SOURCE_MANIFEST_INVALID:{proof_id}")
    paths: list[str] = []
    audit_tool_provenance_drift = 0
    for source_row in files:
        if not isinstance(source_row, dict):
            raise ClosureError(f"LATER_SOURCE_ROW_INVALID:{proof_id}")
        rel = safe_rel(source_row.get("path"), f"manifest:{proof_id}")
        if rel in paths:
            raise ClosureError(f"LATER_SOURCE_PATH_DUPLICATE:{proof_id}:{rel}")
        paths.append(rel)
        path = ROOT / rel
        if not path.is_file():
            raise ClosureError(f"LATER_SOURCE_MISSING:{proof_id}:{rel}")
        data = path.read_bytes()
        if source_row.get("bytes") != len(data) or source_row.get("sha256") != sha(data):
            if rel in AUDIT_TOOL_PROVENANCE_PATHS:
                audit_tool_provenance_drift += 1
                continue
            raise ClosureError(f"LATER_SOURCE_HASH_DRIFT:{proof_id}:{rel}")
    required_manifest_paths = {source_rel}
    if toolchain_rel:
        required_manifest_paths.add(toolchain_rel)
    missing_required = required_manifest_paths - set(paths)
    if missing_required:
        raise ClosureError(f"LATER_SOURCE_MANIFEST_REQUIRED_PATH_MISSING:{proof_id}:{sorted(missing_required)}")

    command = receipt.get("command_argv")
    if not isinstance(command, list) or not command or any(not isinstance(arg, str) for arg in command):
        raise ClosureError(f"LATER_COMMAND_INVALID:{proof_id}")
    if command.count(source_rel) != 1:
        raise ClosureError(f"LATER_COMMAND_SOURCE_MISMATCH:{proof_id}")
    if toolchain_rel:
        toolchain = load(ROOT / toolchain_rel)
        agda = toolchain.get("agda")
        # Historical and current Cubical toolchain records use `binary` and
        # `local_binary` respectively.  Both are concrete executable paths;
        # accept either spelling only when the source manifest independently
        # pins that exact external binary.
        binary = ((agda.get("local_binary") or agda.get("binary"))
                  if isinstance(agda, dict) else None)
        if isinstance(binary, str) and isinstance(agda, dict):
            if not any(
                isinstance(row, dict) and row.get("local_path") == binary
                for row in manifest.get("external_dependencies", [])
            ):
                raise ClosureError(f"LATER_AGDA_BINARY_NOT_PINNED:{proof_id}")
        if binary is None and receipt.get("proof_assistant") == "Lean" and source_rel.endswith(".lean"):
            lean = toolchain.get("lean")
            lean_root = lean.get("root") if isinstance(lean, dict) else None
            if isinstance(lean_root, str) and Path(lean_root).is_absolute():
                binary = str(Path(lean_root) / "bin" / "lean")
                if not any(
                    isinstance(row, dict) and row.get("local_path") == binary
                    for row in manifest.get("external_dependencies", [])
                ):
                    raise ClosureError(f"LATER_LEAN_BINARY_NOT_PINNED:{proof_id}")
        if not isinstance(binary, str) or command.count(binary) != 1:
            raise ClosureError(f"LATER_COMMAND_TOOL_MISMATCH:{proof_id}")

    row_manifest = load(run_dir / "index-row-manifest.json")
    if (
        row_manifest.get("schema_version") != "proof-index-row-manifest/v1"
        or row_manifest.get("run_id") != expected_run_id
        or row_manifest.get("proof_id") != proof_id
        or row_manifest.get("claim_ids") != expected_claims
        or row_manifest.get("index_path") != INDEX_REL
    ):
        raise ClosureError(f"LATER_INDEX_ROW_MANIFEST_IDENTITY_MISMATCH:{proof_id}")
    rows = row_manifest.get("rows")
    if not isinstance(rows, list):
        raise ClosureError(f"LATER_INDEX_ROW_MANIFEST_INVALID:{proof_id}")
    expected_kinds = {proof_id: "proof", **{claim: "claim" for claim in expected_claims}}
    actual: dict[str, dict] = {}
    for row in rows:
        identity = row.get("id") if isinstance(row, dict) else None
        if not isinstance(identity, str) or identity in actual:
            raise ClosureError(f"LATER_INDEX_ROW_ID_DUPLICATE_OR_INVALID:{proof_id}:{identity}")
        actual[identity] = row
    if set(actual) != set(expected_kinds) or any(
        actual[identity].get("kind") != kind for identity, kind in expected_kinds.items()
    ):
        raise ClosureError(f"LATER_INDEX_ROW_SET_MISMATCH:{proof_id}")
    index = matrix_index if matrix_index is not None else matrix_identity_lines(MATRIX.read_bytes())
    for identity, row in actual.items():
        line = unique_matrix_line(index, identity)
        if row.get("line_sha256") != sha(line.encode("utf-8")):
            raise ClosureError(f"LATER_INDEX_ROW_MISSING_OR_REWRITTEN:{proof_id}:{identity}")

    coverage = observed_dependency_coverage(
        stdout_path.read_text(encoding="utf-8"), receipt, manifest, paths, gap_allowlist)

    return {
        "files": len(files),
        "source_paths": set(paths),
        "receipt_files": 4,
        "index_rows": len(rows),
        "dependency_gaps": coverage["dependency_gaps"],
        "used_gap_keys": coverage["used_gap_keys"],
        "observed_local_modules": coverage["local_modules"],
        "observed_external_modules": coverage["external_modules"],
        "audit_tool_provenance_drift": audit_tool_provenance_drift,
    }


def validate_replay_entry(entry: dict, package: dict) -> dict:
    proof_id = package["proof_id"]
    expected_claims = expand_claim_ids(package.get("claim_ids"))
    required = {
        "run",
        "proof_id",
        "claim_ids",
        "source",
        "source_manifest_sha256",
        "stdout_sha256",
        "stderr_sha256",
        "environment_sha256",
        "relation",
    }
    if not required <= set(entry):
        raise ClosureError(f"REPLAY_ENTRY_INVALID:{proof_id}")
    if entry.get("relation") != "REPLAY_OF_EXISTING_CLAIMS":
        raise ClosureError(f"REPLAY_RELATION_INVALID:{proof_id}:{entry.get('run')}")
    if (
        entry.get("proof_id") != proof_id
        or entry.get("claim_ids") != expected_claims
        or entry.get("source") != package.get("source")
        or entry.get("run") == package.get("run")
    ):
        raise ClosureError(f"REPLAY_PACKAGE_IDENTITY_MISMATCH:{proof_id}:{entry.get('run')}")
    run_rel = safe_rel(entry.get("run"), f"replay:{proof_id}")
    receipt = load(ROOT / run_rel / "RUN.json")
    for field, receipt_key in (
        ("source_manifest_sha256", "source_manifest"),
        ("stdout_sha256", "stdout"),
        ("stderr_sha256", "stderr"),
        ("environment_sha256", "environment"),
    ):
        row = receipt.get(receipt_key)
        if not isinstance(row, dict) or entry.get(field) != row.get("sha256"):
            raise ClosureError(f"REPLAY_RECEIPT_BINDING_MISMATCH:{proof_id}:{run_rel}:{field}")
    replay_row = dict(package)
    replay_row["run"] = run_rel
    return replay_row


def main() -> int:
    global ROOT, REGISTRY, MATRIX
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-tag", action="store_true")
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--proof-id", action="append", default=[],
                        help="Explicit package scope; omitted means the whole registry.")
    parser.add_argument("--evidence-only", action="store_true",
                        help="Check complete selected evidence without claiming Git version closure.")
    args = parser.parse_args()
    if args.evidence_only and args.require_tag:
        parser.error("--evidence-only cannot certify --require-tag")
    ROOT = args.project_root.resolve()
    REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
    MATRIX = ROOT / INDEX_REL
    try:
        registry = load(REGISTRY)
        commit = registry.get("proof_asset_commit")
        tree = registry.get("proof_asset_tree")
        if registry.get("schema_version") != "hott-proof-version-closure/v2" or not isinstance(commit, str):
            raise ClosureError("REGISTRY_IDENTITY_INVALID")
        if run_git("rev-parse", commit).decode().strip() != commit:
            raise ClosureError("PROOF_COMMIT_NOT_EXACT")
        if run_git("rev-parse", commit + "^{tree}").decode().strip() != tree:
            raise ClosureError("PROOF_TREE_MISMATCH")

        frozen = run_git("show", f"{commit}:{INDEX_REL}")
        expected = registry["matrix_at_proof_asset_commit"]
        frozen_identity = {"bytes": len(frozen), "lines": len(frozen.splitlines()), "sha256": sha(frozen)}
        if frozen_identity != {key: expected[key] for key in ("bytes", "lines", "sha256")}:
            raise ClosureError("FROZEN_MATRIX_IDENTITY_MISMATCH")
        current = MATRIX.read_bytes()
        if not current.startswith(frozen) or b"## Git \xe7\x89\x88\xe6\x9c\xac\xe9\x97\xad\xe5\x90\x88\xe7\x99\xbb\xe8\xae\xb0" not in current:
            raise ClosureError("CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR")
        matrix_index = matrix_identity_lines(current)

        packages = registry.get("packages")
        if not isinstance(packages, list) or len(packages) != 17:
            raise ClosureError("PACKAGE_COUNT_INVALID")
        all_packages = package_map(registry)
        selected_ids = set(args.proof_id)
        if len(selected_ids) != len(args.proof_id):
            raise ClosureError("PROOF_SELECTION_DUPLICATE")
        missing = sorted(selected_ids - set(all_packages))
        if missing:
            raise ClosureError(f"PROOF_SELECTION_UNKNOWN:{missing}")
        selected = selected_ids or set(all_packages)
        for proof_id, row in all_packages.items():
            unique_matrix_line(matrix_index, proof_id)
            for claim in expand_claim_ids(row.get("claim_ids")):
                unique_matrix_line(matrix_index, claim)

        for row in packages:
            proof_id = row["proof_id"]
            source = safe_rel(row.get("source"), f"frozen-source:{proof_id}")
            run_rel = safe_rel(row.get("run"), f"frozen-run:{proof_id}")
            for path in (source, f"{run_rel}/RUN.json", INDEX_REL):
                run_git("cat-file", "-e", f"{commit}:{path}")
            if selected_ids and proof_id in selected:
                # Selecting a historical package requests its present evidence,
                # not merely the existence of files in the old frozen commit.
                frozen_current = check_later_package(ROOT / run_rel, row, {}, matrix_index)
                if not args.evidence_only:
                    required = frozen_current["source_paths"] | {
                        f"{run_rel}/{name}" for name in (
                            "RUN.json", "stdout.txt", "stderr.txt", "environment.txt",
                            "source-manifest.json", "index-row-manifest.json")}
                    for path in sorted(required):
                        run_git("ls-files", "--error-unmatch", path)
                        if run_git("show", "HEAD:" + path) != (ROOT / path).read_bytes():
                            raise ClosureError(f"WORKING_FILE_NOT_VERSION_CLOSED:{proof_id}:{path}")

        later = registry.get("later_packages")
        if not isinstance(later, list):
            raise ClosureError("LATER_PACKAGES_INVALID")
        gap_allowlist = load_gap_allowlist(registry)
        used_gap_keys: set[tuple[str, str, str]] = set()
        evidence_totals: dict[str, object] = {
            "packages": 0,
            "source_manifest_rows": 0,
            "unique_source_files": set(),
            "index_rows": 0,
            "dependency_gap_allowlisted": 0,
        }
        for row in later:
            proof_id = row["proof_id"]
            if proof_id not in selected:
                continue
            run_rel = safe_rel(row.get("run"), f"later-run:{proof_id}")
            tracked = [
                safe_rel(row.get("source"), f"later-source:{proof_id}"),
                safe_rel(row.get("toolchain"), f"later-toolchain:{proof_id}"),
                f"{run_rel}/RUN.json",
                f"{run_rel}/stdout.txt",
                f"{run_rel}/stderr.txt",
                f"{run_rel}/environment.txt",
                f"{run_rel}/source-manifest.json",
                f"{run_rel}/index-row-manifest.json",
            ]
            for path in tracked:
                if not (ROOT / path).is_file():
                    raise ClosureError(f"LATER_PACKAGE_FILE_MISSING:{proof_id}:{path}")
            evidence = check_later_package(ROOT / run_rel, row, gap_allowlist, matrix_index)
            if not args.evidence_only:
                for path in sorted(set(tracked) | evidence["source_paths"]):
                    run_git("ls-files", "--error-unmatch", path)
                    if run_git("show", "HEAD:" + path) != (ROOT / path).read_bytes():
                        raise ClosureError(f"WORKING_FILE_NOT_VERSION_CLOSED:{proof_id}:{path}")
            evidence_totals["packages"] += 1
            evidence_totals["source_manifest_rows"] += evidence["files"]
            evidence_totals["unique_source_files"].update(evidence["source_paths"])
            evidence_totals["index_rows"] += evidence["index_rows"]
            evidence_totals["dependency_gap_allowlisted"] += evidence["dependency_gaps"]
            used_gap_keys.update(evidence["used_gap_keys"])

        expected_gap_keys = {key for key in gap_allowlist if key[0] in selected}
        if used_gap_keys != expected_gap_keys:
            unused = sorted(expected_gap_keys - used_gap_keys)
            raise ClosureError(f"UNUSED_LATER_DEPENDENCY_GAP_ALLOWLIST:{unused}")

        replay_spec = registry.get("replay_runs")
        if (
            not isinstance(replay_spec, dict)
            or replay_spec.get("schema_version") != "proof-replay-registry/v1"
            or not isinstance(replay_spec.get("entries"), list)
        ):
            raise ClosureError("REPLAY_REGISTRY_INVALID")
        replay_runs: set[str] = set()
        replay_totals = {"runs": 0, "source_manifest_rows": 0, "index_rows": 0}
        for entry in replay_spec["entries"]:
            if not isinstance(entry, dict):
                raise ClosureError("REPLAY_ENTRY_INVALID")
            run_rel = safe_rel(entry.get("run"), "replay-run")
            if run_rel in replay_runs:
                raise ClosureError(f"REPLAY_RUN_DUPLICATE:{run_rel}")
            replay_runs.add(run_rel)
            proof_id = entry.get("proof_id")
            package = all_packages.get(proof_id)
            if package is None:
                raise ClosureError(f"REPLAY_PROOF_NOT_REGISTERED:{proof_id}")
            if proof_id not in selected:
                continue
            replay_row = validate_replay_entry(entry, package)
            evidence = check_later_package(ROOT / run_rel, replay_row, gap_allowlist, matrix_index)
            if evidence["dependency_gaps"]:
                raise ClosureError(f"REPLAY_DEPENDENCY_GAP_FORBIDDEN:{proof_id}:{run_rel}")
            for filename in (
                "RUN.json",
                "stdout.txt",
                "stderr.txt",
                "environment.txt",
                "source-manifest.json",
                "index-row-manifest.json",
            ):
                if not args.evidence_only:
                    rel = f"{run_rel}/{filename}"
                    run_git("ls-files", "--error-unmatch", rel)
                    if run_git("show", "HEAD:" + rel) != (ROOT / rel).read_bytes():
                        raise ClosureError(f"WORKING_FILE_NOT_VERSION_CLOSED:{proof_id}:{rel}")
            replay_totals["runs"] += 1
            replay_totals["source_manifest_rows"] += evidence["files"]
            replay_totals["index_rows"] += evidence["index_rows"]

        all_later_claims = {claim for row in later for claim in expand_claim_ids(row.get("claim_ids"))}
        # The pre-existing numeric counter does not turn legacy candidate IDs
        # into new C-n claims. Report both namespaces explicitly.
        recomputed = sorted(claim for claim in all_later_claims if re.fullmatch(r"C-\d+", claim))
        declared = registry.get("later_machine_proved_claim_count")
        if not isinstance(declared, int) or declared != len(recomputed):
            raise ClosureError(
                f"LATER_CLAIM_COUNT_MISMATCH:declared={declared}:recomputed={len(recomputed)}"
            )

        state = load(ROOT / ".codex/research/hott/STATE.json")
        current_records = [
            row
            for row in state["records"].values()
            if row.get("version_closure", {}).get("proof_asset_commit") == commit
        ]
        if state.get("revision", 0) < 92 or len(current_records) < 19:
            raise ClosureError("STATE_VERSION_CLOSURE_NOT_APPLIED")

        if not args.evidence_only:
            for rel in (INDEX_REL, "HoTT/verification/PROOF_VERSION_CLOSURE.json"):
                if run_git("show", "HEAD:" + rel) != (ROOT / rel).read_bytes():
                    raise ClosureError(f"WORKING_INDEX_OR_REGISTRY_NOT_VERSION_CLOSED:{rel}")

        tag_status = "NOT_REQUIRED"
        if args.require_tag:
            tag = registry.get("release_ref")
            tag_commit = run_git("rev-list", "-n", "1", tag).decode().strip()
            head = run_git("rev-parse", "HEAD").decode().strip()
            if tag_commit != head:
                raise ClosureError("RELEASE_TAG_NOT_AT_HEAD")
            tag_status = "TAG_AT_HEAD"

        evidence_totals["unique_source_files"] = len(evidence_totals["unique_source_files"])
        print(
            json.dumps(
                {
                    "status": ("LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED" if args.evidence_only
                               else "SELECTED_PACKAGES_VERSION_CLOSED" if selected_ids else "PASS_WITH_SCOPE"),
                    "scope": "EXPLICIT_PROOF_SELECTION" if selected_ids else "FULL_REGISTRY",
                    "selected_proof_ids": sorted(selected),
                    "selected_claim_ids": sorted({c for p in selected for c in expand_claim_ids(all_packages[p]["claim_ids"])}),
                    "excluded_proof_ids": sorted(set(all_packages) - selected),
                    "git_version_closure": "NOT_CLAIMED" if args.evidence_only else "HEAD_BYTES_CHECKED",
                    "theory_option_qualification": "SEPARATE_VERIFY_FORMAL_PROOF_RUN_REQUIRED",
                    "inventory_counts_are_not_selected_validation_coverage": bool(selected_ids),
                    "proof_asset_commit": commit,
                    "packages": len(packages),
                    "machine_proved_claims": registry["machine_proved_claim_count"],
                    "later_packages": len(later),
                    "later_machine_proved_claims": len(recomputed),
                    "later_legacy_candidate_claims": len(all_later_claims) - len(recomputed),
                    "later_evidence": evidence_totals,
                    "replay_evidence": replay_totals,
                    "external_replayed_claims": registry["external_replayed_claim_count"],
                    "append_only_matrix_successor": True,
                    "state_records_with_closure": len(current_records),
                    "tag_status": tag_status,
                    "mathematics": "NOT_REPROVED_BY_GIT_CLOSURE",
                },
                ensure_ascii=False,
            )
        )
        return 0
    except (ClosureError, formal_run.ProofRunError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
