#!/usr/bin/env python3
"""Deterministic `force` occurrence inventory for the fixed guarded source tree.

The inventory is lexical evidence for bounded manual review.  It does not
decide whether an occurrence is a semantically valid or invalid consumer.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from machine_overview.util import (
    MachineOverviewError,
    deterministic_tree,
    json_bytes,
    read_json,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_json,
)

SCHEMA = "machine-overview-force-consumer-inventory/v1"
PATTERN = re.compile(r"\bforce(?:-delay|\^)?\b|\bdelay-force\b")


def root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip()).resolve()


def compute(repo: Path, scope_path: Path) -> dict:
    scope = read_json(scope_path)
    tree = next(
        (row for row in scope.get("trees", []) if row.get("tree_id") == "AGDA-GUARDED-FORCING-TICKS-SRC"),
        None,
    )
    if tree is None:
        raise MachineOverviewError("FORCE_TREE_NOT_DECLARED")
    tree_root = Path(tree["path"]).resolve()
    if deterministic_tree(tree_root) != tree["identity"]:
        raise MachineOverviewError("FORCE_TREE_CHANGED")
    matches = []
    for path in sorted(tree_root.rglob("*.agda")):
        lines = path.read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines, 1):
            tokens = PATTERN.findall(line)
            if tokens:
                matches.append({
                    "path": path.relative_to(tree_root).as_posix(),
                    "line": number,
                    "text": line.rstrip(),
                    "token_count": len(tokens),
                })
    return {
        "evaluation_id": scope["evaluation_id"],
        "scope": {
            "path": scope_path.relative_to(repo).as_posix(),
            "bytes": scope_path.stat().st_size,
            "sha256": sha256_file(scope_path),
        },
        "tree": tree,
        "scanned_files": len(list(tree_root.rglob("*.agda"))),
        "files_with_matches": len({row["path"] for row in matches}),
        "matching_lines": len(matches),
        "token_occurrences": sum(row["token_count"] for row in matches),
        "matches": matches,
        "semantic_limit": (
            "This is an exhaustive lexical inventory over the six-file fixed tree. "
            "Whether a use preserves all-clock scope is a direct-source review judgment."
        ),
    }


def run(repo: Path, scope_path: Path, out: Path) -> dict:
    if out.exists():
        raise MachineOverviewError("FORCE_INVENTORY_EXISTS")
    deterministic = compute(repo, scope_path)
    evaluator = Path(__file__).resolve()
    payload = {
        "schema_version": SCHEMA,
        "generated_at_utc": utc_now(),
        "evaluator": {
            "path": evaluator.relative_to(repo).as_posix(),
            "bytes": evaluator.stat().st_size,
            "sha256": sha256_file(evaluator),
        },
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    write_json(out, payload)
    return payload


def verify(repo: Path, path: Path) -> dict:
    payload = read_json(path)
    if payload.get("schema_version") != SCHEMA:
        raise MachineOverviewError("FORCE_INVENTORY_SCHEMA_INVALID")
    evaluator = repo / payload["evaluator"]["path"]
    if (not evaluator.is_file() or evaluator.stat().st_size != payload["evaluator"]["bytes"]
            or sha256_file(evaluator) != payload["evaluator"]["sha256"]):
        raise MachineOverviewError("FORCE_INVENTORY_EVALUATOR_CHANGED")
    scope_path = repo / payload["deterministic"]["scope"]["path"]
    current = compute(repo, scope_path)
    digest = sha256_bytes(json_bytes(current))
    if current != payload["deterministic"] or digest != payload["deterministic_sha256"]:
        raise MachineOverviewError("FORCE_INVENTORY_REPLAY_MISMATCH")
    return {
        "status": "FORCE_CONSUMER_INVENTORY_VALID",
        "matching_lines": current["matching_lines"],
        "files_with_matches": current["files_with_matches"],
        "deterministic_sha256": digest,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--scope", required=True)
    run_parser.add_argument("--out", required=True)
    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("--inventory", required=True)
    args = parser.parse_args(argv)
    repo = root()
    try:
        if args.command == "run":
            payload = run(repo, repo / args.scope, repo / args.out)
            print(json.dumps({
                "status": "FORCE_CONSUMER_INVENTORY_WRITTEN",
                "matching_lines": payload["deterministic"]["matching_lines"],
                "deterministic_sha256": payload["deterministic_sha256"],
            }, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(verify(repo, repo / args.inventory), ensure_ascii=False, indent=2))
    except (MachineOverviewError, OSError, ValueError, KeyError, UnicodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

