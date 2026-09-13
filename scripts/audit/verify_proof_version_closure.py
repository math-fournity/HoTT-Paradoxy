#!/usr/bin/env python3
"""Verify the 17-package Git version-closure registry, the later packages' evidence, and optional release tag.

Audit revision (2026-09-13): an independent audit (finding F2) showed that the
`later_packages` branch only checked path existence, `ls-files`, `exit_code` and
the `index_status` string, so a rewritten matrix row, a tampered source file or a
deleted `stdout.txt` still produced `PASS_WITH_SCOPE`.  The same audit (finding
F7) showed that `later_machine_proved_claim_count` was a declared field that was
never recomputed.  This verifier now performs, for every later package:

  * source identity: every file in `<run>/source-manifest.json` exists and hashes
    to the recorded value (this includes the transitive import closure that the
    newer runs pin);
  * receipt identity: `RUN.json`'s recorded stdout/stderr/environment/
    source-manifest hashes match the files on disk;
  * frozen index rows: every `<run>/index-row-manifest.json` row still exists in
    the current matrix with the same line hash (append-only protection);
  * claim count: `later_machine_proved_claim_count` is recomputed from the
    `claim_ids` ranges and compared with the declared value.

The frozen 17-package checks are unchanged.  `--project-root` exists so that the
same verifier can be pointed at a temporary copy for controlled mutation tests.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"


class ClosureError(RuntimeError):
    pass


def run_git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if result.returncode != 0:
        raise ClosureError(f"GIT_FAILED:{' '.join(args)}:{result.stderr.decode(errors='replace').strip()}")
    return result.stdout


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict): raise ClosureError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def claim_numbers(value: object) -> list[int]:
    if not isinstance(value, str):
        raise ClosureError("CLAIM_IDS_NOT_STRING")
    numbers = [int(part) for part in re.findall(r"\d+", value)]
    if len(numbers) == 2 and numbers[1] >= numbers[0]:
        return list(range(numbers[0], numbers[1] + 1))
    if not numbers:
        raise ClosureError("CLAIM_IDS_UNPARSEABLE")
    return numbers


def stdout_modules(text: str) -> set[str]:
    names: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"\s*Checking\s+(\S+)\s*\(", line)
        if match:
            names.add(match.group(1))
    return names


def check_later_package(run_dir: Path, proof_id: str, gap_allowlist: set[str]) -> dict[str, int]:
    """Common evidence checks for one later (post-snapshot) package."""
    manifest = load(run_dir / "source-manifest.json")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise ClosureError(f"LATER_SOURCE_MANIFEST_INVALID:{proof_id}")
    for row in files:
        rel = row.get("path")
        if not isinstance(rel, str):
            raise ClosureError(f"LATER_SOURCE_ROW_INVALID:{proof_id}")
        path = ROOT / rel
        if not path.is_file():
            raise ClosureError(f"LATER_SOURCE_MISSING:{proof_id}:{rel}")
        if sha(path.read_bytes()) != row.get("sha256"):
            raise ClosureError(f"LATER_SOURCE_HASH_DRIFT:{proof_id}:{rel}")
    receipt = load(run_dir / "RUN.json")
    for key in ("stdout", "stderr", "environment", "source_manifest"):
        row = receipt.get(key)
        if not isinstance(row, dict) or not isinstance(row.get("path"), str):
            raise ClosureError(f"LATER_RECEIPT_FIELD_INVALID:{proof_id}:{key}")
        path = run_dir / row["path"]
        if not path.is_file():
            raise ClosureError(f"LATER_RUN_FILE_MISSING:{proof_id}:{row['path']}")
        data = path.read_bytes()
        if len(data) != row.get("bytes") or sha(data) != row.get("sha256"):
            raise ClosureError(f"LATER_RUN_FILE_HASH_DRIFT:{proof_id}:{row['path']}")
    index_rows = load(run_dir / "index-row-manifest.json")
    rows = index_rows.get("rows")
    if not isinstance(rows, list) or not rows:
        raise ClosureError(f"LATER_INDEX_ROW_MANIFEST_INVALID:{proof_id}")
    current = {sha(line.encode("utf-8")): line for line in MATRIX.read_text(encoding="utf-8").splitlines()}
    for row in rows:
        digest = row.get("line_sha256")
        if digest not in current:
            raise ClosureError(f"LATER_INDEX_ROW_MISSING_OR_REWRITTEN:{proof_id}:{row.get('id')}")
    checked = stdout_modules((run_dir / "stdout.txt").read_text(encoding="utf-8"))
    pinned = {Path(str(row.get("path"))).name.removesuffix(".agda") for row in files}
    gaps = sorted(checked - pinned)
    for module in gaps:
        if f"{proof_id}:{module}" not in gap_allowlist:
            raise ClosureError(f"LATER_DEPENDENCY_GAP_NOT_ALLOWLISTED:{proof_id}:{module}")
    return {"files": len(files), "receipt_files": 4, "index_rows": len(rows), "dependency_gaps": len(gaps)}


def main() -> int:
    global ROOT, REGISTRY, MATRIX
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-tag", action="store_true")
    parser.add_argument("--project-root", type=Path, default=ROOT)
    args = parser.parse_args()
    ROOT = args.project_root.resolve()
    REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
    MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
    try:
        registry = load(REGISTRY)
        commit = registry.get("proof_asset_commit"); tree = registry.get("proof_asset_tree")
        if registry.get("schema_version") != "hott-proof-version-closure/v1" or not isinstance(commit, str):
            raise ClosureError("REGISTRY_IDENTITY_INVALID")
        if run_git("rev-parse", commit).decode().strip() != commit:
            raise ClosureError("PROOF_COMMIT_NOT_EXACT")
        if run_git("rev-parse", commit + "^{tree}").decode().strip() != tree:
            raise ClosureError("PROOF_TREE_MISMATCH")
        frozen = run_git("show", f"{commit}:HoTT/CLAIM_EVIDENCE_MATRIX.md")
        expected = registry["matrix_at_proof_asset_commit"]
        if {"bytes": len(frozen), "lines": len(frozen.splitlines()), "sha256": sha(frozen)} != {key: expected[key] for key in ("bytes", "lines", "sha256")}:
            raise ClosureError("FROZEN_MATRIX_IDENTITY_MISMATCH")
        current = MATRIX.read_bytes()
        if not current.startswith(frozen) or b"## Git \xe7\x89\x88\xe6\x9c\xac\xe9\x97\xad\xe5\x90\x88\xe7\x99\xbb\xe8\xae\xb0" not in current:
            raise ClosureError("CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR")
        packages = registry.get("packages")
        if not isinstance(packages, list) or len(packages) != 17 or len({row.get("proof_id") for row in packages}) != 17:
            raise ClosureError("PACKAGE_COUNT_OR_ID_INVALID")
        for row in packages:
            for path in (row.get("source"), row.get("run") + "/RUN.json", "HoTT/CLAIM_EVIDENCE_MATRIX.md"):
                run_git("cat-file", "-e", f"{commit}:{path}")
        later = registry.get("later_packages", [])
        if not isinstance(later, list):
            raise ClosureError("LATER_PACKAGES_INVALID")
        later_ids = [row.get("proof_id") for row in later if isinstance(row, dict)]
        if len(later_ids) != len(later) or len(set(later_ids)) != len(later_ids):
            raise ClosureError("LATER_PACKAGES_INVALID")
        evidence_totals = {"packages": 0, "source_files": 0, "index_rows": 0}
        gap_spec = registry.get("later_package_dependency_gap_allowlist") or {}
        if not isinstance(gap_spec, dict) or not isinstance(gap_spec.get("entries"), list):
            raise ClosureError("LATER_DEPENDENCY_GAP_ALLOWLIST_INVALID")
        gap_allowlist = {entry for entry in gap_spec["entries"] if isinstance(entry, str)}
        evidence_totals["dependency_gap_allowlisted"] = 0
        for row in later:
            run_rel = row.get("run")
            for path in (row.get("source"), row.get("toolchain"), f"{run_rel}/RUN.json"):
                if not isinstance(path, str) or not (ROOT / path).is_file():
                    raise ClosureError(f"LATER_PACKAGE_FILE_MISSING:{row.get('proof_id')}:{path}")
                run_git("ls-files", "--error-unmatch", path)
            receipt = json.loads((ROOT / f"{run_rel}/RUN.json").read_text(encoding="utf-8"))
            if receipt.get("exit_code") != 0 or receipt.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
                raise ClosureError(f"LATER_PACKAGE_RUN_NOT_INDEXED:{row.get('proof_id')}")
            if not isinstance(row.get("claim_ids"), str) or not row["claim_ids"]:
                raise ClosureError(f"LATER_PACKAGE_CLAIMS_MISSING:{row.get('proof_id')}")
            evidence = check_later_package(ROOT / run_rel, str(row.get("proof_id")), gap_allowlist)
            evidence_totals["packages"] += 1
            evidence_totals["source_files"] += evidence["files"]
            evidence_totals["index_rows"] += evidence["index_rows"]
            evidence_totals["dependency_gap_allowlisted"] += evidence["dependency_gaps"]
        recomputed = sorted({n for row in later for n in claim_numbers(row.get("claim_ids"))})
        declared = registry.get("later_machine_proved_claim_count")
        if not isinstance(declared, int) or declared != len(recomputed):
            raise ClosureError(f"LATER_CLAIM_COUNT_MISMATCH:declared={declared}:recomputed={len(recomputed)}")
        state = load(ROOT / ".codex/research/hott/STATE.json")
        current_records = [row for row in state["records"].values() if row.get("version_closure", {}).get("proof_asset_commit") == commit]
        if state.get("revision", 0) < 92 or len(current_records) < 19:
            raise ClosureError("STATE_VERSION_CLOSURE_NOT_APPLIED")
        tag_status = "NOT_REQUIRED"
        if args.require_tag:
            tag = registry.get("release_ref")
            tag_commit = run_git("rev-list", "-n", "1", tag).decode().strip()
            head = run_git("rev-parse", "HEAD").decode().strip()
            if tag_commit != head:
                raise ClosureError("RELEASE_TAG_NOT_AT_HEAD")
            tag_status = "TAG_AT_HEAD"
        print(json.dumps({
            "status": "PASS_WITH_SCOPE", "proof_asset_commit": commit,
            "packages": len(packages), "machine_proved_claims": registry["machine_proved_claim_count"],
            "later_packages": len(later),
            "later_machine_proved_claims": len(recomputed),
            "later_evidence": evidence_totals,
            "external_replayed_claims": registry["external_replayed_claim_count"],
            "append_only_matrix_successor": True, "state_records_with_closure": len(current_records),
            "tag_status": tag_status, "mathematics": "NOT_REPROVED_BY_GIT_CLOSURE",
        }, ensure_ascii=False))
        return 0
    except (ClosureError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
