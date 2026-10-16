#!/usr/bin/env python3
"""Verify one Cloud-Opus F-011 run by reusing the canonical verifier's checks.

Pattern: .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py.
Imports scripts/audit/verify_formal_proof_run.py and reuses every check it has
(required files, RUN/source-manifest schema and identity, artifact hashes, source
hashes, forbidden Agda markers, OPTIONS --safe --cubical, external toolchain file
and tree hashes, exact replay of command_argv with byte-equal stdout/stderr), and
adds one stricter check: no `postulate` keyword in code outside comments/strings
(the canonical verifier relies on --safe for this).
Only the index check differs: the shared matrix rows for these runs are written in
the same commit as this audit (work order §6/D2), while PROOF_VERSION_CLOSURE.json
belongs to the integrator; so the index is checked against (a) exactly one row per
identity in Cloud-Opus审计并补完GLM/证据索引.md and (b) the presence of every
identity in HoTT/CLAIM_EVIDENCE_MATRIX.md.  The result is labelled accordingly and
never claims INDEXED_IN_CLAIM_EVIDENCE_MATRIX in the canonical sense.
Added 2026-09-27 (self-audit of the Lean work): for a Lean run whose manifest
lists a Cloud-Opus Lean toolchain record, the whole-tree hashes in that record
(init_tree, extra_trees) are recomputed here too; the driver re-checks only the
pinned files, and the canonical verifier knows no Lean tree labels.

Usage:
  python3 Cloud-Opus审计并补完GLM/tools/verify_copus_run.py --run-dir HoTT/verification/runs/<id> [--rerun] [--expect-rejected]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "scripts/audit/verify_formal_proof_run.py"
GOAL_INDEX = ROOT / "Cloud-Opus审计并补完GLM/证据索引.md"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
# Exactly the canonical substring markers (verify_formal_proof_run.py).
FORBIDDEN = ("{!!}", "{-# TERMINATING #-}", "{-# NON_TERMINATING #-}",
             "--allow-unsolved-metas", "--allow-incomplete-matches", "--type-in-type",
             "--no-positivity-check", "--no-termination-check", "--no-universe-check")


def agda_code_only(source: str) -> str:
    """Source text with nested comments, line comments, pragmas and string
    literals removed (same lexing rules as the canonical agda_options)."""
    out: list[str] = []
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
            i = n if stop < 0 else stop
        elif source.startswith("{-#", i):
            end = source.find("#-}", i + 3)
            i = n if end < 0 else end + 3
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
            out.append(" ")
        else:
            out.append(source[i]); i += 1
    return "".join(out)


# Stricter than canonical (which relies on --safe alone): the keyword
# `postulate` must not occur in code; occurrences inside comments are text.
POSTULATE_KEYWORD = re.compile(r"(?:^|\s)postulate(?:\s|$)")


def load_canonical():
    spec = importlib.util.spec_from_file_location("canonical_verify", CANONICAL)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def validate(run_relative: Path, rerun: bool, expect_rejected: bool) -> dict:
    cv = load_canonical()
    Err = cv.ProofRunError
    run_relative.relative_to(Path("HoTT/verification/runs"))
    if "-COPUS-" not in run_relative.name:
        raise Err("RUN_NOT_OWNED_BY_COPUS")
    run_dir = ROOT / run_relative
    if not run_dir.is_dir() or run_dir.is_symlink():
        raise Err("RUN_DIRECTORY_INVALID")
    if not cv.REQUIRED <= {p.name for p in run_dir.iterdir() if p.is_file()}:
        raise Err("RUN_REQUIRED_FILES_MISSING")
    run = cv.read_json(run_dir / "RUN.json")
    if run.get("schema_version") != "formal-proof-run/v1" or run.get("run_id") != run_dir.name:
        raise Err("RUN_IDENTITY_INVALID")
    if expect_rejected:
        if run.get("exit_code") == 0 or run.get("status") not in ("KERNEL_REJECTED", "REJECTED_BEFORE_TYPE_CHECKING"):
            raise Err("NEGATIVE_CONTROL_NOT_REJECTED")
        if run.get("expected_outcome") != "REJECT":
            raise Err("NEGATIVE_CONTROL_EXPECTATION_NOT_RECORDED")
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
    if manifest.get("schema_version") != "formal-proof-source-manifest/v1" or manifest.get("proof_id") != proof_id or manifest.get("run_id") != run.get("run_id"):
        raise Err("SOURCE_MANIFEST_IDENTITY_INVALID")
    source_paths = []
    for row in manifest["files"]:
        relative = cv.safe_relative(str(row["path"]))
        data = (ROOT / relative).read_bytes()
        if row.get("bytes") != len(data) or row.get("sha256") != cv.sha(data):
            raise Err(f"SOURCE_HASH_OR_SIZE_MISMATCH:{relative}")
        if relative.suffix == ".agda":
            text = data.decode("utf-8")
            for marker in FORBIDDEN:
                if marker in text:
                    raise Err(f"AGDA_UNSAFE_MARKER:{relative}:{marker}")
            if POSTULATE_KEYWORD.search(agda_code_only(text)):
                raise Err(f"AGDA_POSTULATE_IN_CODE:{relative}")
            flags = cv.agda_options(text)
            if "--safe" not in flags or "--cubical" not in flags:
                raise Err(f"AGDA_SAFE_CUBICAL_PRAGMA_REQUIRED:{relative}")
        source_paths.append(relative.as_posix())
    external = [cv.check_external_dependency(row) for row in manifest.get("external_dependencies", [])]
    trees_rechecked = []
    for relative in source_paths:
        if relative.startswith("HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN") and relative.endswith(".json"):
            record = cv.read_json(ROOT / relative)
            prefix = Path(record["prefix"])
            for tree in ([record["init_tree"]] if record.get("init_tree") else []) + list(record.get("extra_trees", [])):
                actual = cv.deterministic_tree(prefix / tree["relative_path"])
                if actual != {k: tree.get(k) for k in ("file_count", "total_bytes", "tree_sha256")}:
                    raise Err(f"LEAN_TREE_MISMATCH:{tree['relative_path']}")
                trees_rechecked.append(tree["relative_path"])

    index_text = GOAL_INDEX.read_text(encoding="utf-8")
    matrix_text = MATRIX.read_text(encoding="utf-8")
    goal_rows = {}
    for identity in [proof_id, str(run["run_id"]), *claim_ids]:
        rows = [line for line in index_text.splitlines() if line.startswith(f"| `{identity}` |")]
        if len(rows) != 1:
            raise Err(f"GOAL_INDEX_ROW_COUNT:{identity}:{len(rows)}")
        goal_rows[identity] = cv.sha(rows[0].encode("utf-8"))
        if identity not in matrix_text:
            raise Err(f"MATRIX_IDENTITY_MISSING:{identity}")

    replay = "NOT_RUN"
    if rerun:
        result = subprocess.run(run["command_argv"], cwd=ROOT, capture_output=True, check=False)
        if result.returncode != run.get("exit_code"):
            raise Err("REPLAY_EXIT_MISMATCH")
        if result.stdout != stdout_path.read_bytes() or result.stderr != stderr_path.read_bytes():
            raise Err("REPLAY_OUTPUT_MISMATCH")
        replay = "EXACT_EXIT_STDOUT_STDERR_MATCH"
    return {
        "status": "NEGATIVE_CONTROL_REJECTED_AS_EXPECTED" if expect_rejected else "PASS_WITH_SCOPE",
        "verifier": "Cloud-Opus goal-local (reuses canonical verify_formal_proof_run.py checks; index = goal index + matrix presence)",
        "canonical_verifier_sha256": cv.sha(CANONICAL.read_bytes()),
        "run_id": run["run_id"], "proof_id": proof_id, "claim_ids": claim_ids,
        "run_status": run["status"], "exit_code": run["exit_code"],
        "rejection_stage": run.get("rejection_stage"), "agda_error_tag": run.get("agda_error_tag"),
        "source_paths": source_paths, "external_dependencies": external,
        "toolchain_trees_rechecked": trees_rechecked,
        "index": "GOAL_LOCAL_INDEX_PLUS_MATRIX_PRESENCE", "goal_index_row_sha256": goal_rows,
        "replay": replay, "git_status": run.get("git_status"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--rerun", action="store_true")
    ap.add_argument("--expect-rejected", action="store_true")
    a = ap.parse_args()
    try:
        print(json.dumps(validate(Path(a.run_dir), a.rerun, a.expect_rejected), ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
