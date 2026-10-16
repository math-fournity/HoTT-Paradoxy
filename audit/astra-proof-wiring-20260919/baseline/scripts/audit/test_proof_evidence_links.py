#!/usr/bin/env python3
"""Regression tests for proof/run/index identity and replay registration.

All mutations occur below a temporary project root. The real repository is
used only as a read-only source of files and Git metadata.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
T3 = "HoTT/formal/ercf3-t3"
VERIFIER_PATH = ROOT / "scripts/audit/verify_proof_version_closure.py"
MARK_PATH = ROOT / "scripts/audit/mark_proof_run_indexed.py"
FREEZE_PATH = ROOT / "scripts/audit/freeze_proof_index_rows.py"

SPEC = importlib.util.spec_from_file_location("proof_closure_under_test", VERIFIER_PATH)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def read_json(root: Path, rel: str) -> dict:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def materialize_dir(path: Path) -> None:
    if path.is_symlink():
        target = path.resolve()
        path.unlink()
        path.mkdir()
        for child in target.iterdir():
            (path / child.name).symlink_to(child, target_is_directory=child.is_dir())
    elif not path.exists():
        materialize_dir(path.parent)
        path.mkdir()


def write_copy(root: Path, rel: str, data: bytes) -> None:
    path = root / rel
    cursor = root
    for part in Path(rel).parts[:-1]:
        cursor = cursor / part
        materialize_dir(cursor)
    if path.is_symlink():
        path.unlink()
    path.write_bytes(data)


def temporary_root(parent: str) -> Path:
    root = Path(parent) / "project"
    root.mkdir()
    for child in ROOT.iterdir():
        (root / child.name).symlink_to(child, target_is_directory=child.is_dir())
    return root


def command(path: Path, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", "-B", str(path), "--project-root", str(root), *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )


def registry_row(registry: dict, proof_id: str) -> dict:
    return next(row for row in registry["later_packages"] if row["proof_id"] == proof_id)


class ProofEvidenceLinkTests(unittest.TestCase):
    maxDiff = None

    def run_mutation(self, mutate) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(prefix="hott-proof-links-") as parent:
            root = temporary_root(parent)
            mutate(root)
            return command(VERIFIER_PATH, root)

    def test_current_registry_passes(self) -> None:
        result = command(VERIFIER_PATH, ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "PASS_WITH_SCOPE")
        self.assertEqual(payload["later_evidence"]["dependency_gap_allowlisted"], 6)
        self.assertEqual(payload["later_evidence"]["unique_source_files"], 21)

    def test_swapped_run_references_are_rejected(self) -> None:
        def mutate(root: Path) -> None:
            registry = read_json(root, REGISTRY)
            left, right = registry["later_packages"][-2:]
            left["run"], right["run"] = right["run"], left["run"]
            write_copy(root, REGISTRY, json_bytes(registry))

        result = self.run_mutation(mutate)
        self.assertEqual(result.returncode, 2)
        self.assertIn("LATER_RUN_PROOF_ID_MISMATCH", result.stdout)

    def test_omitted_frozen_claim_row_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            registry = read_json(root, REGISTRY)
            package = registry_row(registry, "MP-ERCF3-T3-CODING-IMAGE-001")
            rel = package["run"] + "/index-row-manifest.json"
            manifest = read_json(root, rel)
            manifest["rows"] = [row for row in manifest["rows"] if row["id"] != "C-186"]
            write_copy(root, rel, json_bytes(manifest))

        result = self.run_mutation(mutate)
        self.assertEqual(result.returncode, 2)
        self.assertIn("LATER_INDEX_ROW_SET_MISMATCH", result.stdout)

    def test_duplicate_matrix_identity_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            data = (root / MATRIX).read_bytes()
            write_copy(root, MATRIX, data + b"\n| C-186 | synthetic conflicting duplicate |\n")

        result = self.run_mutation(mutate)
        self.assertEqual(result.returncode, 2)
        self.assertIn("MATRIX_IDENTITY_NOT_UNIQUE:C-186:2", result.stdout)

    def test_source_drift_and_missing_stdout_are_rejected(self) -> None:
        def mutate_source(root: Path) -> None:
            rel = f"{T3}/RepairedSyntax.agda"
            write_copy(root, rel, (root / rel).read_bytes() + b"\n-- synthetic drift\n")

        source = self.run_mutation(mutate_source)
        self.assertEqual(source.returncode, 2)
        self.assertIn("LATER_SOURCE_HASH_DRIFT", source.stdout)

        def remove_stdout(root: Path) -> None:
            registry = read_json(root, REGISTRY)
            package = registry_row(registry, "MP-ERCF3-T3-REPAIRED-SYNTAX-001")
            rel = package["run"] + "/stdout.txt"
            write_copy(root, rel, (root / rel).read_bytes())
            (root / rel).unlink()

        stdout = self.run_mutation(remove_stdout)
        self.assertEqual(stdout.returncode, 2)
        self.assertIn("LATER_PACKAGE_FILE_MISSING", stdout.stdout)

    def test_claim_count_mismatch_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            registry = read_json(root, REGISTRY)
            registry["later_machine_proved_claim_count"] += 1
            write_copy(root, REGISTRY, json_bytes(registry))

        result = self.run_mutation(mutate)
        self.assertEqual(result.returncode, 2)
        self.assertIn("LATER_CLAIM_COUNT_MISMATCH", result.stdout)

    def test_run_identity_and_command_are_rejected(self) -> None:
        def mutate_identity(root: Path) -> None:
            registry = read_json(root, REGISTRY)
            package = registry_row(registry, "MP-ERCF3-T3-CODING-IMAGE-001")
            rel = package["run"] + "/RUN.json"
            run = read_json(root, rel)
            run["proof_id"] = "MP-UNRELATED"
            write_copy(root, rel, json_bytes(run))

        identity = self.run_mutation(mutate_identity)
        self.assertEqual(identity.returncode, 2)
        self.assertIn("LATER_RUN_PROOF_ID_MISMATCH", identity.stdout)

        def mutate_command(root: Path) -> None:
            registry = read_json(root, REGISTRY)
            package = registry_row(registry, "MP-ERCF3-T3-CODING-IMAGE-001")
            rel = package["run"] + "/RUN.json"
            run = read_json(root, rel)
            run["command_argv"] = ["/usr/bin/true", package["source"]]
            write_copy(root, rel, json_bytes(run))

        command_result = self.run_mutation(mutate_command)
        self.assertEqual(command_result.returncode, 2)
        self.assertIn("LATER_COMMAND_TOOL_MISMATCH", command_result.stdout)

    def test_historical_gap_exception_does_not_follow_new_run(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hott-proof-gap-") as parent:
            root = temporary_root(parent)
            registry = read_json(root, REGISTRY)
            package = copy.deepcopy(
                registry_row(registry, "MP-ERCF3-T3-REPAIRED-SYNTAX-001")
            )
            old_run = root / package["run"]
            new_id = "20260913-TEST-SAME-PROOF-NEW-RUN"
            new_rel = "HoTT/verification/runs/" + new_id
            cursor = root
            for part in Path(new_rel).parts[:-1]:
                cursor = cursor / part
                materialize_dir(cursor)
            shutil.copytree(old_run, root / new_rel, symlinks=False)

            source_manifest = read_json(root, new_rel + "/source-manifest.json")
            source_manifest["run_id"] = new_id
            manifest_data = json_bytes(source_manifest)
            write_copy(root, new_rel + "/source-manifest.json", manifest_data)
            run = read_json(root, new_rel + "/RUN.json")
            run["run_id"] = new_id
            run["source_manifest"]["bytes"] = len(manifest_data)
            run["source_manifest"]["sha256"] = digest(manifest_data)
            write_copy(root, new_rel + "/RUN.json", json_bytes(run))
            rows = read_json(root, new_rel + "/index-row-manifest.json")
            rows["run_id"] = new_id
            write_copy(root, new_rel + "/index-row-manifest.json", json_bytes(rows))
            package["run"] = new_rel

            old_root, old_matrix = V.ROOT, V.MATRIX
            try:
                V.ROOT = root
                V.MATRIX = root / MATRIX
                allowlist = V.load_gap_allowlist(registry)
                with self.assertRaisesRegex(
                    V.ClosureError,
                    "LATER_DEPENDENCY_GAP_NOT_ALLOWLISTED.*TEST-SAME-PROOF-NEW-RUN",
                ):
                    V.check_later_package(
                        root / new_rel,
                        package,
                        allowlist,
                        V.matrix_identity_lines((root / MATRIX).read_bytes()),
                    )
            finally:
                V.ROOT, V.MATRIX = old_root, old_matrix

    def test_mark_and_freeze_register_replay_without_rewriting_matrix(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hott-proof-replay-") as parent:
            root = temporary_root(parent)
            # Materialize the registry and all parent directories before a tool
            # uses atomic replace, so no write can traverse a source symlink.
            write_copy(root, REGISTRY, (ROOT / REGISTRY).read_bytes())
            registry = read_json(root, REGISTRY)
            package = registry_row(registry, "MP-ERCF3-T3-REPAIRED-SYNTAX-001")
            old_run = root / package["run"]
            new_id = "20260913-TEST-REPAIRED-SYNTAX-REPLAY-01"
            new_rel = "HoTT/verification/runs/" + new_id
            cursor = root
            for part in Path(new_rel).parts[:-1]:
                cursor = cursor / part
                materialize_dir(cursor)
            shutil.copytree(old_run, root / new_rel, symlinks=False)
            (root / new_rel / "index-row-manifest.json").unlink()

            manifest = read_json(root, new_rel + "/source-manifest.json")
            manifest["run_id"] = new_id
            listed = {row["path"] for row in manifest["files"]}
            for name in ("DiagonalLemma.agda", "DecodingFence.agda"):
                rel = f"{T3}/{name}"
                if rel not in listed:
                    data = (root / rel).read_bytes()
                    manifest["files"].append(
                        {"path": rel, "bytes": len(data), "sha256": digest(data)}
                    )
            manifest_data = json_bytes(manifest)
            write_copy(root, new_rel + "/source-manifest.json", manifest_data)

            run = read_json(root, new_rel + "/RUN.json")
            run["run_id"] = new_id
            run["index_status"] = "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE"
            run.pop("index", None)
            run["source_manifest"]["bytes"] = len(manifest_data)
            run["source_manifest"]["sha256"] = digest(manifest_data)
            write_copy(root, new_rel + "/RUN.json", json_bytes(run))

            before_matrix = (root / MATRIX).read_bytes()
            marked = command(MARK_PATH, root, "--run-dir", new_rel)
            self.assertEqual(marked.returncode, 0, marked.stdout + marked.stderr)
            self.assertEqual(json.loads(marked.stdout)["relation"], "REGISTERED_REPLAY")
            self.assertEqual((root / MATRIX).read_bytes(), before_matrix)

            registered = read_json(root, REGISTRY)["replay_runs"]["entries"]
            self.assertEqual([entry["run"] for entry in registered], [new_rel])
            self.assertNotIn(new_id, (root / MATRIX).read_text(encoding="utf-8"))
            marked_run = read_json(root, new_rel + "/RUN.json")
            self.assertEqual(marked_run["index"]["relation"], "REGISTERED_REPLAY")

            frozen = command(FREEZE_PATH, root, "--run-dir", new_rel)
            self.assertEqual(frozen.returncode, 0, frozen.stdout + frozen.stderr)
            row_manifest = read_json(root, new_rel + "/index-row-manifest.json")
            self.assertEqual(row_manifest["index_relation"], "REGISTERED_REPLAY")
            self.assertEqual(
                set(row["id"] for row in row_manifest["rows"]),
                {
                    "MP-ERCF3-T3-REPAIRED-SYNTAX-001",
                    "C-181",
                    "C-182",
                    "C-183",
                },
            )

            old_root, old_matrix = V.ROOT, V.MATRIX
            try:
                V.ROOT = root
                V.MATRIX = root / MATRIX
                current_registry = read_json(root, REGISTRY)
                entry = current_registry["replay_runs"]["entries"][0]
                replay_row = V.validate_replay_entry(entry, package)
                checked = V.check_later_package(
                    root / new_rel,
                    replay_row,
                    V.load_gap_allowlist(current_registry),
                    V.matrix_identity_lines((root / MATRIX).read_bytes()),
                )
                self.assertEqual(checked["dependency_gaps"], 0)
            finally:
                V.ROOT, V.MATRIX = old_root, old_matrix


if __name__ == "__main__":
    unittest.main()
