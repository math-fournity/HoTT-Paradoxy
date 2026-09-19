#!/usr/bin/env python3
"""Validate the v5 host-neutral routing invariants without modifying the repo.

Checks:
  A1: root and .codex AGENTS files do not embed a concrete generation-N identity.
  R3: operational governance prose contains no host-exclusive Codex wording.
  Z1: the three .zcode workspace skills are exact relative symlinks to the
      canonical .codex skill directories.

Exit 0 means every listed invariant passed for the inspected project root.
Exit 1 means at least one invariant failed.  Exit 2 is command misuse.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[2]
AGENT_PATHS = (Path("AGENTS.md"), Path(".codex/AGENTS.md"))
GENERATION_IDENTITY = re.compile(r"generation-[0-9]+", re.IGNORECASE)
HOST_EXCLUSIVE = (
    re.compile(r"仅\s*Codex", re.IGNORECASE),
    re.compile(r"Codex\s*专属", re.IGNORECASE),
    re.compile(r"\bonly\s+Codex\b", re.IGNORECASE),
    re.compile(r"\bCodex-only\b", re.IGNORECASE),
    re.compile(r"只能被\s*codex", re.IGNORECASE),
)
SKILL_LINKS = {
    "hott-local-session-governance": "../../.codex/skills/hott-local-session-governance",
    "hott-paradox-research": "../../.codex/skills/hott-paradox-research",
    "hott-paradox-search-sop": "../../.codex/skills/hott-paradox-search-sop",
}


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def line_hits(path: Path, patterns: tuple[re.Pattern[str], ...]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for number, line in enumerate(text(path).splitlines(), 1):
        for pattern in patterns:
            if pattern.search(line):
                findings.append({"path": str(path), "line": number, "text": line})
                break
    return findings


def governance_markdown(root: Path) -> list[Path]:
    """Return current operational governance prose, never historical receipts.

    Checkpoint before/after snapshots and research-session evidence can preserve
    historical host-specific wording.  They are audit evidence, not a current
    policy surface, so scanning them would both create false failures and make
    the receipt proportional to retention volume rather than the live contract.
    """
    paths = [root / "AGENTS.md", root / ".codex" / "AGENTS.md", root / ".codex" / "cognition" / "PROTOCOL.md"]
    skills = root / ".codex" / "skills"
    if skills.is_dir():
        paths.extend(path for path in skills.glob("*/SKILL.md") if path.is_file())
    commands = root / ".zcode" / "commands"
    if commands.is_dir():
        paths.extend(path for path in commands.glob("*.md") if path.is_file())
    return sorted(set(path for path in paths if path.is_file()))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args(argv)
    root = args.project_root.resolve()
    result: dict[str, object] = {
        "schema_version": "hott-governance-v5-invariants/v1",
        "project_root": str(root),
        "checks": {},
        "failures": [],
    }
    failures: list[dict[str, object]] = []

    a1: list[dict[str, object]] = []
    for rel in AGENT_PATHS:
        path = root / rel
        if not path.is_file():
            a1.append({"path": str(rel), "reason": "MISSING_AGENT_FILE"})
            continue
        a1.extend(line_hits(path, (GENERATION_IDENTITY,)))
    result["checks"]["A1_no_dynamic_generation_identity"] = {
        "paths": [str(path) for path in AGENT_PATHS],
        "findings": a1,
    }
    failures.extend({"check": "A1", **row} for row in a1)

    r3: list[dict[str, object]] = []
    for path in governance_markdown(root):
        r3.extend(line_hits(path, HOST_EXCLUSIVE))
    result["checks"]["R3_host_neutral_governance_prose"] = {
        "paths_scanned": [str(path.relative_to(root)) for path in governance_markdown(root)],
        "findings": r3,
    }
    failures.extend({"check": "R3", **row} for row in r3)

    z1: list[dict[str, object]] = []
    for name, expected_link in SKILL_LINKS.items():
        link = root / ".zcode" / "skills" / name
        expected_target = (link.parent / expected_link).resolve()
        if not link.is_symlink():
            z1.append({"path": str(link.relative_to(root)), "reason": "SYMLINK_MISSING"})
            continue
        actual_link = os.readlink(link)
        if actual_link != expected_link:
            z1.append({
                "path": str(link.relative_to(root)),
                "reason": "SYMLINK_TARGET_MISMATCH",
                "expected": expected_link,
                "actual": actual_link,
            })
            continue
        resolved = link.resolve()
        if resolved != expected_target or not (resolved / "SKILL.md").is_file():
            z1.append({"path": str(link.relative_to(root)), "reason": "SYMLINK_TARGET_UNUSABLE"})
    result["checks"]["Z1_zcode_skill_symlinks"] = {"findings": z1}
    failures.extend({"check": "Z1", **row} for row in z1)

    result["failures"] = failures
    result["status"] = "PASS" if not failures else "FAIL"
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
