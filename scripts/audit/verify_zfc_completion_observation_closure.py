#!/usr/bin/env python3
"""Verify the bounded machine-evidence closure for the ZFC completion inquiry.

This verifier intentionally does *not* update or replace the canonical
HoTT/CLAIM_EVIDENCE_MATRIX.md.  It validates the contributor closing bundle:
fresh proof-run receipts, their source-manifest hashes, frozen Pattern-P input
cards, and the pinned main-branch HoTT documents.  Passing it establishes only
artifact integrity and the stated run outcomes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "zfc-completion-observation-closure/v1"

RUNS = (
    {
        "run_id": "20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-05",
        "proof_id": "MP-ZFC-OBSERVATION-BOUNDARY-001",
        "status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "exit": 0,
        "no_axioms": True,
    },
    {
        "run_id": "20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-05",
        "proof_id": "MP-ZFC-GEOMETRIC-COMPLETION-001",
        "status": "KERNEL_ACCEPTED_WITH_DECLARED_AXIOMS_AND_SCOPE",
        "exit": 0,
        "no_axioms": False,
    },
    {
        "run_id": "20261003-MP-ZFC-META-OBSERVATION-CONSISTENCY-001-04",
        "proof_id": "MP-ZFC-META-OBSERVATION-CONSISTENCY-001",
        "status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "exit": 0,
        "no_axioms": True,
    },
    {
        "run_id": "20261004-MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001-04",
        "proof_id": "MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001",
        "status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "exit": 0,
        "no_axioms": True,
    },
    {
        "run_id": "20261004-MP-ZFC-COMPLETION-SUBSTITUTION-PROFILE-001-04",
        "proof_id": "MP-ZFC-COMPLETION-SUBSTITUTION-PROFILE-001",
        "status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "exit": 0,
        "no_axioms": True,
    },
    {
        "run_id": "20261004-CG001-QUESTIONING-DELAY-ZFC-CLOSURE-01",
        "proof_id": "MP-CG001-QUESTIONING-DELAY-ZFC-CLOSURE-001",
        "status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "exit": 0,
        "no_axioms": None,
    },
    {
        "run_id": "20261004-CG001-QUESTIONING-DELAY-ZFC-CLOSURE-NEG-01",
        "proof_id": "MP-CG001-QUESTIONING-DELAY-ZFC-CLOSURE-NEG-001",
        "status": "KERNEL_REJECTED",
        "exit": 42,
        "agda_error_tag": "UnequalTerms",
    },
    {
        "run_id": "20261004-CG001-TRUNCATION-QUESTIONING-ZFC-CLOSURE-01",
        "proof_id": "MP-CG001-TRUNCATION-QUESTIONING-ZFC-CLOSURE-001",
        "status": "KERNEL_ACCEPTED_WITH_SCOPE",
        "exit": 0,
        "no_axioms": None,
    },
    {
        "run_id": "20261004-CG001-TRUNCATION-QUESTIONING-ZFC-CLOSURE-NEG-01",
        "proof_id": "MP-CG001-TRUNCATION-QUESTIONING-ZFC-CLOSURE-NEG-001",
        "status": "KERNEL_REJECTED",
        "exit": 42,
        "agda_error_tag": "UnequalTerms",
    },
)

FROZEN_FILES = {
    "audit/20261004-P-DAG-ZFC-P-100-TASKCARD.md": "6492ca5890e559f2f374ff9e4baafb0b4c81d15633bf6cecc3b399fd6e0812bb",
    "audit/20261004-P-DAG-ZFC-P-100-PROMPT.md": "65e3e438f2c7501de45ec8f8e4a9c2d253822a1fe22f15358d2f33e5f7a271c8",
    "audit/20261004-P-DAG-ZFC-P-101-PROMPT.md": "35ada926313f012a588dd1fa60f2aeae06df6dbc0653c3acdd543b5ba7ebd028",
    "audit/20261004-P-DAG-ZFC-P-102-PROMPT.md": "1337688b68b676b0b77e0151ed4b54cf43dd9d5f93e6422e9f88dacb3e69fb5d",
    "audit/20261004-P-DAG-ZFC-P-103-PROMPT.md": "55d9143e48543487cd9a1bcf6f8852726416d749a28afc96b969f451dbdd1ac5",
    "audit/20261004-P-DAG-ZFC-P-104-PROMPT.md": "a8ae166e292accb4a29aed7a759bb7ab5be8576c9eab557aca8ab09a1771a8f1",
    "audit/20261004-P-DAG-ZFC-P-105-PROMPT.md": "64f21099d66e384ba7cb0fb34cca68356906d2144c7adf08a5dec0d633566c42",
    "audit/20261004-P-DAG-ZFC-P-106-NODECARD.md": "a48f4e32801d678e06d90ef923f8331a501ae2aa2e10dc059fa68294a1439243",
}

MAIN_BLOBS = {
    "README.md": "eef5cea125b12ab991325748ee0a67d32d0968d6",
    "docs/社区审计提交/03-HoTT的芝诺.md": "c9057ff917cb8669186ac2f30ba95d36602192e3",
    "HoTT/formal/claude-cg001/questioning-delay/CLAIM.md": "ad397173e596fa518e739f79cadcfa33232a6e99",
    "HoTT/formal/claude-cg001/questioning-delay/QuestioningDelay.agda": "29f82274e71bcf71d8173417f1ef325586c9a4a5",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def result_path(run: dict[str, Any], name: str) -> str | None:
    entry = run.get(name)
    if isinstance(entry, dict) and isinstance(entry.get("path"), str):
        return entry["path"]
    if name == "source_manifest":
        entry = run.get("source_manifest.json")
        if isinstance(entry, dict) and isinstance(entry.get("path"), str):
            return entry["path"]
    return None


def check_file(path: Path, expected_bytes: int, expected_sha: str, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"MISSING_FILE:{path.relative_to(ROOT)}")
        return
    data = path.read_bytes()
    if len(data) != expected_bytes or sha(data) != expected_sha:
        errors.append(f"HASH_OR_SIZE_MISMATCH:{path.relative_to(ROOT)}")


def verify_run(spec: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    run_dir = ROOT / "HoTT/verification/runs" / spec["run_id"]
    run_path = run_dir / "RUN.json"
    if not run_path.is_file():
        errors.append(f"MISSING_RUN:{spec['run_id']}")
        return {"run_id": spec["run_id"], "status": "MISSING"}
    run = load_json(run_path)
    for key, expected in (("run_id", spec["run_id"]), ("proof_id", spec["proof_id"]),
                          ("status", spec["status"]), ("exit_code", spec["exit"])):
        if run.get(key) != expected:
            errors.append(f"RUN_FIELD_MISMATCH:{spec['run_id']}:{key}")
    if "agda_error_tag" in spec and run.get("agda_error_tag") != spec["agda_error_tag"]:
        errors.append(f"AGDA_TAG_MISMATCH:{spec['run_id']}")
    if spec["status"] == "KERNEL_REJECTED" and run.get("outcome_matches_expectation") is not True:
        errors.append(f"NEGATIVE_OUTCOME_NOT_MATCHED:{spec['run_id']}")
    for name in ("stdout", "stderr", "environment", "source_manifest"):
        relative = result_path(run, name)
        if relative is None:
            errors.append(f"RUN_RECEIPT_FIELD_MISSING:{spec['run_id']}:{name}")
            continue
        entry = run.get(name) or run.get("source_manifest.json")
        if not isinstance(entry, dict):
            errors.append(f"RUN_RECEIPT_SHAPE_MISSING:{spec['run_id']}:{name}")
            continue
        check_file(run_dir / relative, int(entry.get("bytes", -1)), str(entry.get("sha256", "")), errors)
    manifest_path = run_dir / "source-manifest.json"
    if manifest_path.is_file():
        manifest = load_json(manifest_path)
        for entry in manifest.get("files", []):
            if not isinstance(entry, dict):
                errors.append(f"SOURCE_MANIFEST_ENTRY_INVALID:{spec['run_id']}")
                continue
            relative = entry.get("path")
            if not isinstance(relative, str):
                errors.append(f"SOURCE_MANIFEST_PATH_INVALID:{spec['run_id']}")
                continue
            check_file(ROOT / relative, int(entry.get("bytes", -1)), str(entry.get("sha256", "")), errors)
    if spec.get("no_axioms") is True:
        stdout = (run_dir / "stdout.txt").read_text(encoding="utf-8", errors="replace")
        if "depends on any axioms" in stdout:
            errors.append(f"UNEXPECTED_AXIOM_DEPENDENCY:{spec['run_id']}")
        if "does not depend on any axioms" not in stdout:
            errors.append(f"NO_AXIOM_PRINT_MISSING:{spec['run_id']}")
    return {"run_id": spec["run_id"], "status": run.get("status"), "verified": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, help="optional JSON receipt path relative to repository root")
    args = parser.parse_args()
    errors: list[str] = []
    run_results = [verify_run(spec, errors) for spec in RUNS]
    frozen_results = []
    for relative, expected in FROZEN_FILES.items():
        path = ROOT / relative
        actual = sha(path.read_bytes()) if path.is_file() else None
        if actual != expected:
            errors.append(f"FROZEN_INPUT_MISMATCH:{relative}")
        frozen_results.append({"path": relative, "sha256": actual, "matches": actual == expected})
    main_results = []
    for relative, expected in MAIN_BLOBS.items():
        proc = subprocess.run(["git", "-C", str(ROOT), "rev-parse", f"main:{relative}"], capture_output=True, text=True, check=False)
        actual = proc.stdout.strip() if proc.returncode == 0 else None
        if actual != expected:
            errors.append(f"MAIN_BLOB_MISMATCH:{relative}")
        main_results.append({"path": relative, "blob": actual, "matches": actual == expected})
    receipt = {
        "schema_version": SCHEMA,
        "status": "PASS" if not errors else "FAIL",
        "runs": run_results,
        "frozen_inputs": frozen_results,
        "main_blobs": main_results,
        "errors": errors,
        "scope": "Artifact-integrity verification for the contributor ZFC completion-observation closing bundle; not a ZFC consistency, common-P, P-to-B, or same-task theorem.",
    }
    rendered = json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.out:
        target = (ROOT / args.out).resolve()
        target.relative_to(ROOT)
        if target.exists():
            raise SystemExit("REFUSE_OVERWRITE")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
