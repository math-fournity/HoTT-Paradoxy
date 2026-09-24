#!/usr/bin/env python3
"""CG-001 goal-local verifier for F-011 proof runs.

Why this exists: the canonical verifier scripts/audit/verify_formal_proof_run.py
requires each run to be indexed in HoTT/CLAIM_EVIDENCE_MATRIX.md, which is owned by
the research integrator (Codex Session C) and is read-only for this goal.  This tool
imports the canonical module and reuses every one of its checks (artifact hashes,
source-manifest hashes, forbidden Agda markers, OPTIONS pragma, external toolchain
tree hashes, exact replay of command_argv), and replaces only the shared-matrix index
check with a check against this goal's own index file.  Results are labelled
GOAL_LOCAL_INDEX_ONLY and never claim INDEXED_IN_CLAIM_EVIDENCE_MATRIX.

Usage:
  python3 .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py \
      --run-dir HoTT/verification/runs/<run-id> [--rerun] [--expect-rejected]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CANONICAL = ROOT / "scripts/audit/verify_formal_proof_run.py"
GOAL_INDEX = ROOT / ".claude/goals/CG-001-targeted-overview/证据索引.md"


def load_canonical():
    spec = importlib.util.spec_from_file_location("canonical_verify", CANONICAL)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def goal_index_rows(text: str, identity: str) -> list[str]:
    prefix = f"| `{identity}` |"
    return [line for line in text.splitlines() if line.startswith(prefix)]


def validate(run_relative: Path, rerun: bool, expect_rejected: bool) -> dict[str, object]:
    cv = load_canonical()
    Err = cv.ProofRunError
    run_relative.relative_to(Path("HoTT/verification/runs"))
    if "-CG001-" not in run_relative.name:
        raise Err("RUN_NOT_OWNED_BY_CG001")
    run_dir = ROOT / run_relative
    if not run_dir.is_dir() or run_dir.is_symlink():
        raise Err("RUN_DIRECTORY_INVALID")
    if not cv.REQUIRED <= {p.name for p in run_dir.iterdir() if p.is_file()}:
        raise Err("RUN_REQUIRED_FILES_MISSING")
    run = cv.read_json(run_dir / "RUN.json")
    if run.get("schema_version") != "formal-proof-run/v1" or run.get("run_id") != run_dir.name:
        raise Err("RUN_IDENTITY_INVALID")
    if expect_rejected:
        if run.get("status") != "KERNEL_REJECTED" or run.get("exit_code") == 0:
            raise Err("NEGATIVE_CONTROL_NOT_REJECTED")
    elif run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("exit_code") != 0:
        raise Err("RUN_NOT_KERNEL_ACCEPTED")
    if run.get("index_status") != "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE":
        raise Err("UNEXPECTED_INDEX_STATUS")
    proof_id = str(run["proof_id"])
    claim_ids = [str(c) for c in run["claim_ids"]]

    stdout_path = cv.check_artifact(run_dir, run.get("stdout"), "stdout")
    stderr_path = cv.check_artifact(run_dir, run.get("stderr"), "stderr")
    cv.check_artifact(run_dir, run.get("environment"), "environment")
    manifest_path = cv.check_artifact(run_dir, run.get("source_manifest"), "source_manifest")
    manifest = cv.read_json(manifest_path)
    if manifest.get("proof_id") != proof_id or manifest.get("run_id") != run.get("run_id"):
        raise Err("SOURCE_MANIFEST_IDENTITY_INVALID")
    source_paths: list[str] = []
    forbidden = (
        "{!!}", "{-# TERMINATING #-}", "{-# NON_TERMINATING #-}", "postulate",
        "--allow-unsolved-metas", "--allow-incomplete-matches", "--type-in-type",
        "--no-positivity-check", "--no-termination-check", "--no-universe-check",
    )
    for row in manifest["files"]:
        relative = cv.safe_relative(str(row["path"]))
        data = (ROOT / relative).read_bytes()
        if row.get("bytes") != len(data) or row.get("sha256") != cv.sha(data):
            raise Err(f"SOURCE_HASH_OR_SIZE_MISMATCH:{relative}")
        if relative.suffix == ".agda":
            text = data.decode("utf-8")
            for marker in forbidden:
                if marker in text:
                    raise Err(f"AGDA_UNSAFE_MARKER:{relative}:{marker}")
            flags = cv.agda_options(text)
            if "--safe" not in flags or "--cubical" not in flags:
                raise Err(f"AGDA_SAFE_CUBICAL_PRAGMA_REQUIRED:{relative}")
        source_paths.append(relative.as_posix())
    external = [cv.check_external_dependency(row) for row in manifest.get("external_dependencies", [])]

    index_text = GOAL_INDEX.read_text(encoding="utf-8")
    index_rows = {}
    for identity in [proof_id, str(run["run_id"]), *claim_ids]:
        rows = goal_index_rows(index_text, identity)
        if len(rows) != 1:
            raise Err(f"GOAL_INDEX_ROW_COUNT:{identity}:{len(rows)}")
        index_rows[identity] = cv.sha(rows[0].encode("utf-8"))

    replay = "NOT_RUN"
    if rerun:
        result = subprocess.run(run["command_argv"], cwd=ROOT, capture_output=True, check=False)
        if result.returncode != run.get("exit_code"):
            raise Err("REPLAY_EXIT_MISMATCH")
        if result.stdout != stdout_path.read_bytes() or result.stderr != stderr_path.read_bytes():
            raise Err("REPLAY_OUTPUT_MISMATCH")
        replay = "EXACT_EXIT_STDOUT_STDERR_MATCH"

    return {
        "status": "PASS_WITH_SCOPE" if not expect_rejected else "NEGATIVE_CONTROL_REJECTED_AS_EXPECTED",
        "verifier": "CG-001 goal-local (reuses canonical verify_formal_proof_run.py checks; index check replaced)",
        "canonical_verifier_sha256": cv.sha(CANONICAL.read_bytes()),
        "run_id": run["run_id"],
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "kernel_status": run["status"],
        "exit_code": run["exit_code"],
        "source_paths": source_paths,
        "external_dependencies": external,
        "index": "GOAL_LOCAL_INDEX_ONLY",
        "goal_index_row_sha256": index_rows,
        "shared_matrix_index": "NOT_INDEXED_RELAY_DRAFT_ONLY",
        "replay": replay,
        "git_status": run.get("git_status"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument("--expect-rejected", action="store_true")
    args = parser.parse_args()
    try:
        print(json.dumps(validate(Path(args.run_dir), args.rerun, args.expect_rejected), ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:  # report every failure as data
        print(json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
