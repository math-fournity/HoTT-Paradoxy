#!/usr/bin/env python3
"""Verify the structural contract for mathematical-proof-before-delivery governance.

This verifier proves only that the project-local policy, storage roots, run
contract, claim index and routing markers agree. It cannot prove that a model
will follow the policy or that any mathematical proposition is true.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
MARKER = "math-proof-delivery-gate:v1"
REQUIRED_MARKERS = {
    "AGENTS.md": MARKER,
    ".codex/cognition/PROTOCOL.md": MARKER,
    ".codex/skills/hott-paradox-research/SKILL.md": MARKER,
    "docs/quality/数学结论机器证明与证据留存规范.md": "math-proof-storage-contract:v1",
    "HoTT/formal/README.md": "math-proof-source-contract:v1",
    "HoTT/verification/runs/README.md": "math-proof-run-contract:v1",
    "HoTT/CLAIM_EVIDENCE_MATRIX.md": "math-proof-index-contract:v1",
}
ROUTING_MARKERS = {
    ".codex/AGENTS.md": (
        "数学结论交付门禁",
        "根 AGENTS `MATH_PROOF_BEFORE_DELIVERY_V1`",
        "docs/quality/数学结论机器证明与证据留存规范.md",
    ),
    ".codex/skills/hott-local-session-governance/SKILL.md": (
        "数学证明门禁",
        ".codex/cognition/PROTOCOL.md",
        "根 `AGENTS.md`",
    ),
}
EXPECTED_ROOTS = {
    ("AGENTS.md", "proof_source_root"): "HoTT/formal",
    ("AGENTS.md", "proof_run_root"): "HoTT/verification/runs",
    ("AGENTS.md", "proof_index"): "HoTT/CLAIM_EVIDENCE_MATRIX.md",
    ("HoTT/formal/README.md", "authoritative_source_root"): "HoTT/formal",
    ("HoTT/verification/runs/README.md", "authoritative_run_root"): "HoTT/verification/runs",
    ("HoTT/CLAIM_EVIDENCE_MATRIX.md", "authoritative_index"): "HoTT/CLAIM_EVIDENCE_MATRIX.md",
}
REQUIRED_RUN_FILES = {"RUN.json", "stdout.txt", "stderr.txt", "environment.txt", "source-manifest.json"}


class ProofGovernanceError(RuntimeError):
    pass


def read(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file() or path.is_symlink():
        raise ProofGovernanceError(f"MISSING_OR_SYMLINK:{rel}")
    try:
        body = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ProofGovernanceError(f"UNREADABLE_UTF8:{rel}") from exc
    if not body.strip():
        raise ProofGovernanceError(f"EMPTY_REQUIRED_FILE:{rel}")
    return body


def field(body: str, name: str, rel: str) -> str:
    matches = re.findall(rf"(?m)^{re.escape(name)}:\s*(\S+)\s*$", body)
    if len(matches) != 1:
        raise ProofGovernanceError(f"CONTRACT_FIELD_COUNT:{rel}:{name}:{len(matches)}")
    return matches[0]


def safe_project_relative(value: str, expected: str, rel: str, name: str) -> None:
    candidate = PurePosixPath(value)
    if value != expected or candidate.is_absolute() or ".." in candidate.parts or value.startswith("/tmp"):
        raise ProofGovernanceError(f"ROOT_CONTRACT_INVALID:{rel}:{name}:{value}")


def validate(root: Path) -> dict[str, object]:
    root = root.resolve()
    bodies = {rel: read(root, rel) for rel in REQUIRED_MARKERS}
    for rel, marker in REQUIRED_MARKERS.items():
        if marker not in bodies[rel]:
            raise ProofGovernanceError(f"MARKER_MISSING:{rel}:{marker}")
    for rel, markers in ROUTING_MARKERS.items():
        body = read(root, rel)
        for marker in markers:
            if marker not in body:
                raise ProofGovernanceError(f"ROUTING_MARKER_MISSING:{rel}:{marker}")
    for (rel, name), expected in EXPECTED_ROOTS.items():
        safe_project_relative(field(bodies[rel], name, rel), expected, rel, name)

    run_files = set(field(bodies["HoTT/verification/runs/README.md"], "required_files", "HoTT/verification/runs/README.md").split(","))
    if run_files != REQUIRED_RUN_FILES:
        raise ProofGovernanceError(f"RUN_REQUIRED_FILES_INVALID:{sorted(run_files)}")

    agents = bodies["AGENTS.md"]
    for phrase in (
        "MATH_PROOF_BEFORE_DELIVERY_V1", "MACHINE_PROVED", "PAPER_ONLY",
        "SOURCE_REPORTED_NOT_REPLAYED", "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    ):
        if phrase not in agents:
            raise ProofGovernanceError(f"AGENTS_CONTRACT_TERM_MISSING:{phrase}")
    if "F-011" not in read(root, "feature-list.md"):
        raise ProofGovernanceError("FEATURE_F011_MISSING")
    if "数学结论交付前必须机器证明" not in read(root, "rulings.md"):
        raise ProofGovernanceError("USER_RULING_MISSING")
    if "MATH_PROOF_BEFORE_DELIVERY_V1" not in read(root, "HoTT/README.md"):
        raise ProofGovernanceError("HOTT_ROUTE_MISSING")

    for path in (root / "HoTT/formal", root / "HoTT/verification/runs"):
        if not path.is_dir() or path.is_symlink():
            raise ProofGovernanceError(f"AUTHORITATIVE_DIRECTORY_INVALID:{path.relative_to(root)}")

    return {
        "status": "PASS_WITH_SCOPE",
        "schema_version": "math-proof-delivery-governance-check/v1",
        "marker_files": len(REQUIRED_MARKERS),
        "routing_files": len(ROUTING_MARKERS),
        "proof_source_root": "HoTT/formal",
        "proof_run_root": "HoTT/verification/runs",
        "proof_index": "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        "required_run_files": sorted(REQUIRED_RUN_FILES),
        "model_behavior": "NOT_CERTIFIED_BY_STATIC_CHECK",
        "mathematics": "NOT_CERTIFIED_BY_GOVERNANCE_CHECK",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(json.dumps(validate(args.project_root), ensure_ascii=False, indent=2))
        return 0
    except (ProofGovernanceError, OSError, ValueError, TypeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
