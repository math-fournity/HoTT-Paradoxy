"""Rebuildable query projection over cases, runs, reviews and reports.

The index is derived data: the receipts remain the authoritative artifacts.
"""
from __future__ import annotations

from pathlib import Path

from .util import read_json, sha256_file, utc_now, write_json


def rebuild_index(repo_root: Path, root: Path) -> dict:
    entries: list[dict] = []
    for case_file in sorted((root / "cases").glob("*/case-revision-*.json")):
        case = read_json(case_file)
        entries.append({
            "kind": "case",
            "id": case["case_id"],
            "revision": case["revision"],
            "path": case_file.relative_to(root).as_posix(),
            "sha256": sha256_file(case_file),
        })
    for run_file in sorted((root / "runs").glob("*/RUN.json")):
        run = read_json(run_file)
        entries.append({
            "kind": run.get("kind", "run"),
            "id": run.get("run_id"),
            "case_id": run.get("case_id"),
            "path": run_file.relative_to(root).as_posix(),
            "sha256": sha256_file(run_file),
            "status": run.get("status") or run.get("exit_reason"),
        })
    for review_file in sorted((root / "reviews").glob("*.json")):
        review = read_json(review_file)
        entries.append({
            "kind": "review",
            "id": review.get("review_id"),
            "case_id": review.get("case_id"),
            "path": review_file.relative_to(root).as_posix(),
            "sha256": sha256_file(review_file),
        })
    for report in sorted((root / "reports").glob("*.md")):
        entries.append({
            "kind": "report",
            "id": report.stem,
            "path": report.relative_to(root).as_posix(),
            "sha256": sha256_file(report),
        })
    index = {
        "schema_version": "machine-overview-index/v1",
        "generated_at_utc": utc_now(),
        "entries": entries,
    }
    write_json(root / "generated-index" / "index.json", index)
    return index


def load_index(repo_root: Path, root: Path) -> dict:
    path = root / "generated-index" / "index.json"
    if not path.is_file():
        return rebuild_index(repo_root, root)
    return read_json(path)


def query(root: Path, *, kind: str | None = None, text: str | None = None) -> list[dict]:
    index = load_index(root.parents[0], root)
    entries = index["entries"]
    if kind:
        entries = [entry for entry in entries if entry["kind"] == kind]
    if text:
        lowered = text.lower()
        entries = [entry for entry in entries if lowered in str(entry.get("id", "")).lower()
                   or lowered in entry["path"].lower()
                   or lowered in str(entry.get("case_id", "")).lower()]
    return entries


def get(root: Path, identifier: str) -> dict:
    for entry in load_index(root.parents[0], root)["entries"]:
        if entry.get("id") == identifier:
            return entry
    return {"status": "NOT_FOUND", "id": identifier}
