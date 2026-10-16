"""Rebuildable query projection over cases, runs, reviews and result owners.

The index is derived data: the receipts remain the authoritative artifacts.
Read commands never write the projection unless a rebuild is explicitly asked
for (audit observation: `list`/`get`/`query` must not be described as writes).
"""
from __future__ import annotations

from pathlib import Path

from .util import read_json, sha256_file, utc_now, write_json


def build_index(root: Path) -> dict:
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
            "case_revision": run.get("case_revision"),
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
    evaluations = root / "evaluations"
    for run_file in sorted(evaluations.glob("*/runs/*/RUN.json")):
        run = read_json(run_file)
        if run.get("schema_version") in {
            "machine-overview-m4-lite-run/v1", "machine-overview-m4-replay-run/v2",
        }:
            entries.append({
                "kind": "evaluation",
                "id": run.get("run_id"),
                "path": run_file.relative_to(root).as_posix(),
                "sha256": sha256_file(run_file),
                "status": run.get("status", "DESCRIPTIVE_M4_LITE"),
            })
    for decision_file in sorted(evaluations.glob("*/DECISIONS.json")):
        decision = read_json(decision_file)
        if decision.get("schema_version") == "machine-overview-natural-consumer-decisions/v1":
            entries.append({
                "kind": "source-audit",
                "id": decision.get("audit_id"),
                "path": decision_file.relative_to(root).as_posix(),
                "sha256": sha256_file(decision_file),
                "status": decision.get("status"),
            })
    for report in sorted(evaluations.glob("*/REPORT.md")):
        entries.append({
            "kind": "evaluation-report",
            "id": report.parent.name,
            "path": report.relative_to(root).as_posix(),
            "sha256": sha256_file(report),
        })
    for assessment in sorted(evaluations.glob("*/ASSESSMENT.md")):
        entries.append({
            "kind": "source-audit-report",
            "id": assessment.parent.name,
            "path": assessment.relative_to(root).as_posix(),
            "sha256": sha256_file(assessment),
        })
    return {
        "schema_version": "machine-overview-index/v1",
        "generated_at_utc": utc_now(),
        "entries": entries,
    }


def rebuild_index(repo_root: Path, root: Path) -> dict:
    index = build_index(root)
    write_json(root / "generated-index" / "index.json", index)
    return index


def load_index(repo_root: Path, root: Path) -> dict:
    path = root / "generated-index" / "index.json"
    if path.is_file():
        return read_json(path)
    return build_index(root)


def query(root: Path, *, kind: str | None = None, text: str | None = None) -> list[dict]:
    index = _load_readonly(root)
    entries = index["entries"]
    if kind:
        entries = [entry for entry in entries if entry["kind"] == kind]
    if text:
        lowered = text.lower()
        entries = [entry for entry in entries
                   if lowered in str(entry.get("id", "")).lower()
                   or lowered in entry["path"].lower()
                   or lowered in str(entry.get("case_id", "")).lower()]
    return entries


def get(root: Path, identifier: str, *, revision: int | None = None) -> list[dict]:
    entries = [entry for entry in _load_readonly(root)["entries"] if entry.get("id") == identifier]
    if revision is not None:
        entries = [entry for entry in entries if entry.get("revision") == revision]
    return entries


def _load_readonly(root: Path) -> dict:
    path = root / "generated-index" / "index.json"
    if path.is_file():
        return read_json(path)
    return build_index(root)
