#!/usr/bin/env python3
"""Verify a fixed-source L5 consumer-qualification matrix.

The semantic decisions are explicit human/AI review data.  This program does
not infer them from keywords.  It verifies source bytes, source anchors, roster
and Q1-Q6 completeness, then derives the bounded all-criteria verdict and the
four-capability separation mechanically.
"""
from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
import re
import subprocess
import sys
from pathlib import Path

from machine_overview.util import (
    MachineOverviewError,
    git_state,
    json_bytes,
    read_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_json,
)

SCOPE_SCHEMA = "machine-overview-l5-consumer-scope/v1"
DECISIONS_SCHEMA = "machine-overview-l5-consumer-decisions/v1"
RUN_SCHEMA = "machine-overview-l5-consumer-run/v1"
CRITERIA = [f"Q{i}" for i in range(1, 7)]
CAPABILITIES = [
    "given_proof_check",
    "bounded_proof_search",
    "finite_truth_decision",
    "same_layer_total_self_reliability",
]
CRITERION_STATUSES = {"PASS", "PARTIAL", "FAIL", "NOT_APPLICABLE"}
CAPABILITY_STATUSES = {
    "CLAIMED_WITH_SCOPE",
    "BOUNDED_ONLY",
    "INFRASTRUCTURE_PRIMITIVE",
    "IN_PROGRESS",
    "NOT_CLAIMED",
    "NOT_APPLICABLE",
}


class _VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.hidden += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)


def root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip()).resolve()


def _under(path: Path, parent: Path, label: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(parent.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"L5_SOURCE_OUTSIDE_ROOT:{label}:{path}") from exc
    return resolved


def _normalized(data: bytes, kind: str) -> str:
    text = data.decode("utf-8", errors="strict")
    if kind == "html":
        parser = _VisibleText()
        parser.feed(text)
        text = " ".join(parser.parts)
    return " ".join(html.unescape(text).split())


def _artifact(root_path: Path, cache_root: Path, row: dict, label: str) -> tuple[Path, bytes]:
    location = row.get("location")
    if location == "repo":
        path = _under(root_path / safe_relative(row.get("path", "")), root_path, label)
    elif location == "external_cache":
        path = _under(Path(row.get("path", "")), cache_root, label)
    else:
        raise MachineOverviewError(f"L5_SOURCE_LOCATION_INVALID:{label}:{location}")
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"L5_SOURCE_INVALID:{label}")
    data = path.read_bytes()
    if len(data) != row.get("bytes") or sha256_bytes(data) != row.get("sha256"):
        raise MachineOverviewError(f"L5_SOURCE_CHANGED:{label}")
    return path, data


def validate_scope(root_path: Path, scope: dict) -> dict[str, dict]:
    if scope.get("schema_version") != SCOPE_SCHEMA:
        raise MachineOverviewError("L5_SCOPE_SCHEMA_INVALID")
    if [row.get("id") for row in scope.get("criteria", [])] != CRITERIA:
        raise MachineOverviewError("L5_SCOPE_CRITERIA_INVALID")
    if [row.get("id") for row in scope.get("capabilities", [])] != CAPABILITIES:
        raise MachineOverviewError("L5_SCOPE_CAPABILITIES_INVALID")
    cache_root = Path(scope.get("external_cache_root", ""))
    if not cache_root.is_dir() or cache_root.is_symlink():
        raise MachineOverviewError("L5_EXTERNAL_CACHE_INVALID")
    sources = scope.get("sources", [])
    source_ids = [row.get("source_id") for row in sources]
    if not source_ids or len(source_ids) != len(set(source_ids)):
        raise MachineOverviewError("L5_SOURCE_ROSTER_INVALID")
    artifacts: dict[str, dict] = {}
    for source in sources:
        for row in source.get("artifacts", []):
            artifact_id = row.get("artifact_id")
            if not isinstance(artifact_id, str) or artifact_id in artifacts:
                raise MachineOverviewError(f"L5_ARTIFACT_ID_INVALID:{artifact_id}")
            path, data = _artifact(root_path, cache_root, row, artifact_id)
            artifacts[artifact_id] = {
                "row": row,
                "path": str(path),
                "normalized": _normalized(data, row.get("kind", "text")),
            }
    return artifacts


def compute(root_path: Path, scope_path: Path, decisions_path: Path) -> dict:
    scope = read_json(scope_path)
    decisions = read_json(decisions_path)
    artifacts = validate_scope(root_path, scope)
    if decisions.get("schema_version") != DECISIONS_SCHEMA:
        raise MachineOverviewError("L5_DECISIONS_SCHEMA_INVALID")
    if decisions.get("audit_id") != scope.get("audit_id"):
        raise MachineOverviewError("L5_AUDIT_ID_MISMATCH")
    scope_sources = [row["source_id"] for row in scope["sources"]]
    rows = decisions.get("sources", [])
    if [row.get("source_id") for row in rows] != scope_sources:
        raise MachineOverviewError("L5_DECISION_ROSTER_MISMATCH")

    anchor_checks = []
    normalized_rows = []
    for row in rows:
        criteria = row.get("criteria", {})
        capabilities = row.get("capabilities", {})
        if list(criteria) != CRITERIA:
            raise MachineOverviewError(f"L5_CRITERIA_COVERAGE_INVALID:{row['source_id']}")
        if list(capabilities) != CAPABILITIES:
            raise MachineOverviewError(f"L5_CAPABILITY_COVERAGE_INVALID:{row['source_id']}")
        for criterion_id, decision in criteria.items():
            if decision.get("status") not in CRITERION_STATUSES:
                raise MachineOverviewError(f"L5_CRITERION_STATUS_INVALID:{row['source_id']}:{criterion_id}")
            evidence = decision.get("evidence", [])
            if not evidence:
                raise MachineOverviewError(f"L5_CRITERION_EVIDENCE_MISSING:{row['source_id']}:{criterion_id}")
            for evidence_row in evidence:
                artifact_id = evidence_row.get("artifact_id")
                artifact = artifacts.get(artifact_id)
                if artifact is None:
                    raise MachineOverviewError(f"L5_EVIDENCE_ARTIFACT_UNKNOWN:{artifact_id}")
                for needle in evidence_row.get("anchors", []):
                    normalized_needle = " ".join(html.unescape(needle).split())
                    found = normalized_needle in artifact["normalized"]
                    anchor_checks.append({
                        "source_id": row["source_id"],
                        "criterion": criterion_id,
                        "artifact_id": artifact_id,
                        "anchor_sha256": sha256_bytes(normalized_needle.encode("utf-8")),
                        "found": found,
                    })
                    if not found:
                        raise MachineOverviewError(
                            f"L5_EVIDENCE_ANCHOR_MISSING:{row['source_id']}:{criterion_id}:{artifact_id}"
                        )
        for capability_id, capability in capabilities.items():
            if capability.get("status") not in CAPABILITY_STATUSES:
                raise MachineOverviewError(
                    f"L5_CAPABILITY_STATUS_INVALID:{row['source_id']}:{capability_id}"
                )
        qualified = (
            all(criteria[item]["status"] == "PASS" for item in CRITERIA)
            and capabilities["same_layer_total_self_reliability"]["status"] == "CLAIMED_WITH_SCOPE"
        )
        normalized_rows.append({
            "source_id": row["source_id"],
            "system": row.get("system"),
            "relation_to_hott": row.get("relation_to_hott"),
            "criteria": criteria,
            "capabilities": capabilities,
            "qualified_same_layer_self_reliability_consumer": qualified,
            "near_hit_rank": row.get("near_hit_rank"),
            "classification": row.get("classification"),
        })

    hits = [row["source_id"] for row in normalized_rows if row["qualified_same_layer_self_reliability_consumer"]]
    ranked = sorted(
        (row for row in normalized_rows if isinstance(row.get("near_hit_rank"), int)),
        key=lambda item: (item["near_hit_rank"], item["source_id"]),
    )
    capability_counts = {
        capability: {
            status: sum(row["capabilities"][capability]["status"] == status for row in normalized_rows)
            for status in sorted(CAPABILITY_STATUSES)
        }
        for capability in CAPABILITIES
    }
    return {
        "audit_id": scope["audit_id"],
        "scope": {
            "path": scope_path.relative_to(root_path).as_posix(),
            "bytes": scope_path.stat().st_size,
            "sha256": sha256_file(scope_path),
        },
        "decisions": {
            "path": decisions_path.relative_to(root_path).as_posix(),
            "bytes": decisions_path.stat().st_size,
            "sha256": sha256_file(decisions_path),
        },
        "source_count": len(normalized_rows),
        "artifact_count": len(artifacts),
        "anchor_checks": anchor_checks,
        "all_anchors_found": all(item["found"] for item in anchor_checks),
        "sources": normalized_rows,
        "capability_counts": capability_counts,
        "qualified_hits": hits,
        "strongest_near_hit": ranked[0]["source_id"] if ranked else None,
        "verdict": "QUALIFIED_CONSUMER_FOUND" if hits else "NO_QUALIFIED_CONSUMER_IN_FROZEN_SET",
        "semantic_limit": (
            "Source bytes, anchor presence, roster and matrix completeness are machine-verified. "
            "Q1-Q6 meanings are explicit review judgments; this is a bounded source-set result, "
            "not a global nonexistence theorem or a proof of an HoTT bug."
        ),
    }


def run(root_path: Path, scope_path: Path, decisions_path: Path, output_path: Path) -> dict:
    if output_path.exists():
        raise MachineOverviewError("L5_AUDIT_RUN_ALREADY_EXISTS")
    deterministic = compute(root_path, scope_path, decisions_path)
    evaluator = Path(__file__).resolve()
    payload = {
        "schema_version": RUN_SCHEMA,
        "run_id": output_path.parent.name,
        "generated_at_utc": utc_now(),
        "evaluator": {
            "path": evaluator.relative_to(root_path).as_posix(),
            "bytes": evaluator.stat().st_size,
            "sha256": sha256_file(evaluator),
        },
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
        "git": git_state(root_path),
    }
    output_path.parent.mkdir(parents=True, exist_ok=False)
    write_json(output_path, payload)
    return payload


def verify(root_path: Path, run_path: Path) -> dict:
    payload = read_json(run_path)
    if payload.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("L5_AUDIT_RUN_SCHEMA_INVALID")
    evaluator = payload.get("evaluator", {})
    evaluator_path = root_path / safe_relative(evaluator.get("path", ""))
    if (not evaluator_path.is_file() or evaluator_path.stat().st_size != evaluator.get("bytes")
            or sha256_file(evaluator_path) != evaluator.get("sha256")):
        raise MachineOverviewError("L5_AUDIT_EVALUATOR_CHANGED")
    deterministic = payload["deterministic"]
    scope_path = root_path / safe_relative(deterministic["scope"]["path"])
    decisions_path = root_path / safe_relative(deterministic["decisions"]["path"])
    current = compute(root_path, scope_path, decisions_path)
    digest = sha256_bytes(json_bytes(current))
    if current != deterministic or digest != payload.get("deterministic_sha256"):
        raise MachineOverviewError("L5_AUDIT_REPLAY_MISMATCH")
    return {
        "status": "L5_CONSUMER_AUDIT_VALID",
        "audit_id": current["audit_id"],
        "verdict": current["verdict"],
        "source_count": current["source_count"],
        "qualified_hits": current["qualified_hits"],
        "deterministic_sha256": digest,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--scope", required=True)
    run_parser.add_argument("--decisions", required=True)
    run_parser.add_argument("--out", required=True)
    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("--run", required=True)
    args = parser.parse_args(argv)
    repo = root()
    try:
        if args.command == "run":
            result = run(repo, repo / args.scope, repo / args.decisions, repo / args.out)
            print(json.dumps({
                "status": "L5_CONSUMER_AUDIT_WRITTEN",
                "verdict": result["deterministic"]["verdict"],
                "deterministic_sha256": result["deterministic_sha256"],
            }, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(verify(repo, repo / args.run), ensure_ascii=False, indent=2))
    except (MachineOverviewError, OSError, ValueError, KeyError, UnicodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

