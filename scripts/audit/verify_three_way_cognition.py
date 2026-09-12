#!/usr/bin/env python3
"""Validate the local three-way cognition projection.

This validator checks the mechanical contract around 核心认知.md, 方向追踪.md and
全景视野.md.  It does not judge whether a direction is mathematically good or
whether an AI understood a paragraph.  It only rejects missing/incorrect entry
order, broken projection markers, duplicate IDs, missing direction/result links,
and a projection whose declared STATE revision is stale.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


THREE_WAY = ["核心认知.md", "方向追踪.md", "全景视野.md"]
DIRECTION = "方向追踪.md"
PANORAMA = "全景视野.md"
STATE = ".codex/research/hott/STATE.json"
LOAD_SET = ".codex/cognition/LOAD_SET.json"
CORE_MANIFEST = "核心认知.manifest.json"
DIRECTION_RE = re.compile(r"^\| `(?P<id>DIR-[A-Z0-9-]+)` \|", re.M)
OUTCOME_RE = re.compile(r"^\| `(?P<id>OUT-[A-Z0-9-]+)` \|", re.M)


class ThreeWayError(RuntimeError):
    pass


def read_text(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file() or path.is_symlink():
        raise ThreeWayError(f"MISSING_OR_SYMLINK:{rel}")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ThreeWayError(f"UNREADABLE_UTF8:{rel}") from exc


def read_json(root: Path, rel: str) -> dict[str, object]:
    try:
        value = json.loads(read_text(root, rel))
    except json.JSONDecodeError as exc:
        raise ThreeWayError(f"INVALID_JSON:{rel}") from exc
    if not isinstance(value, dict):
        raise ThreeWayError(f"JSON_OBJECT_REQUIRED:{rel}")
    return value


def unique_ids(pattern: re.Pattern[str], body: str, label: str) -> list[str]:
    ids = [match.group("id") for match in pattern.finditer(body)]
    if not ids:
        raise ThreeWayError(f"NO_{label.upper()}_IDS")
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        raise ThreeWayError(f"DUPLICATE_{label.upper()}_IDS:{','.join(duplicates)}")
    return ids


def projection_state_revision(body: str, label: str) -> int:
    match = re.search(r"(?m)^source_state_revision: (\d+)\s*$", body)
    if not match:
        raise ThreeWayError(f"PROJECTION_STATE_REVISION_MISSING:{label}")
    return int(match.group(1))


def validate(root: Path) -> dict[str, object]:
    root = root.resolve()
    load_set = read_json(root, LOAD_SET)
    fixed = load_set.get("fixed_full_text")
    if not isinstance(fixed, list) or fixed[:3] != THREE_WAY:
        raise ThreeWayError("THREE_WAY_FIXED_ORDER_INVALID")
    if load_set.get("three_way_order") != THREE_WAY:
        raise ThreeWayError("THREE_WAY_DECLARED_ORDER_INVALID")
    for rel in THREE_WAY:
        read_text(root, rel)

    core_manifest = read_json(root, CORE_MANIFEST)
    if core_manifest.get("schema_version") != "core-cognition/v1":
        raise ThreeWayError("CORE_MANIFEST_SCHEMA_INVALID")
    units = core_manifest.get("units")
    if not isinstance(units, list) or not units:
        raise ThreeWayError("CORE_UNITS_MISSING")

    state = read_json(root, STATE)
    revision = state.get("revision")
    if type(revision) is not int or revision < 1:
        raise ThreeWayError("STATE_REVISION_INVALID")

    direction_body = read_text(root, DIRECTION)
    panorama_body = read_text(root, PANORAMA)
    if "integrated-direction-portfolio:v1" not in direction_body:
        raise ThreeWayError("DIRECTION_MARKER_MISSING")
    if "integrated-outcome-panorama:v1" not in panorama_body:
        raise ThreeWayError("PANORAMA_MARKER_MISSING")
    if projection_state_revision(direction_body, DIRECTION) != revision:
        raise ThreeWayError("DIRECTION_STATE_REVISION_STALE")
    if projection_state_revision(panorama_body, PANORAMA) != revision:
        raise ThreeWayError("PANORAMA_STATE_REVISION_STALE")

    direction_ids = unique_ids(DIRECTION_RE, direction_body, "direction")
    outcome_ids = unique_ids(OUTCOME_RE, panorama_body, "outcome")
    direction_set = set(direction_ids)
    outcome_set = set(outcome_ids)

    direction_rows = [line for line in direction_body.splitlines() if line.startswith("| `DIR-")]
    for line in direction_rows:
        referenced = set(re.findall(r"OUT-[A-Z0-9-]+", line))
        if not referenced and "NO_RESULT_YET" not in line:
            raise ThreeWayError(f"DIRECTION_WITHOUT_RESULT_OR_REASON:{line[:80]}")
        missing = sorted(referenced - outcome_set)
        if missing:
            raise ThreeWayError(f"DIRECTION_RESULT_ORPHAN:{','.join(missing)}")

    outcome_rows = [line for line in panorama_body.splitlines() if line.startswith("| `OUT-")]
    for line in outcome_rows:
        referenced = set(re.findall(r"DIR-[A-Z0-9-]+", line))
        if not referenced and "UNMAPPED" not in line:
            raise ThreeWayError(f"OUTCOME_WITHOUT_DIRECTION_OR_REASON:{line[:80]}")
        missing = sorted(referenced - direction_set)
        if missing:
            raise ThreeWayError(f"OUTCOME_DIRECTION_ORPHAN:{','.join(missing)}")

    return {
        "status": "PASS",
        "schema_version": "integrated-three-way-cognition/v1",
        "state_revision": revision,
        "core_units_declared": len(units),
        "direction_count": len(direction_ids),
        "outcome_count": len(outcome_ids),
        "fixed_order": THREE_WAY,
        "model_context": "NOT_CERTIFIED_BY_TOOL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    try:
        print(json.dumps(validate(args.root), ensure_ascii=False, indent=2))
        return 0
    except ThreeWayError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
