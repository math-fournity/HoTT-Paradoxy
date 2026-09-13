#!/usr/bin/env python3
"""Shared reader for v2 sharded logical Markdown documents.

An indexed canonical path is a logical document: the index file plus every
shard listed in its table, in table order.  ``logical_text`` rebuilds the
original continuous text (marker block, shard H1 and the following blank line
are the only added metadata), so consumers that compare or count content keep
working after a shard migration.

Read-only, stdlib only.
"""
from __future__ import annotations

import re
from pathlib import Path, PurePosixPath

INDEX_MARKER = "<!-- governance-shard-index:v2"
SHARD_MARKER = "<!-- governance-shard:v2"
TABLE_START = "<!-- governance-shard-table:start -->"
TABLE_END = "<!-- governance-shard-table:end -->"
ROW_RE = re.compile(r"^\|\s*`?([A-Za-z0-9._-]+)`?\s*\|\s*\[([^]]+)\]\(([^)]+)\)\s*\|")
# Keep in step with the canonical validator's discovery window: a marker quoted
# inside a documentation example must not turn the file into an index.
INDEX_SCAN_LINES = 20


def parse_index(text: str, rel: str | None = None) -> dict | None:
    """Return index metadata plus ordered shard paths, or None for a plain file.

    ``shards`` are the link paths exactly as written in the index table, i.e.
    **relative to the index's own directory** (the validator resolves them that
    way).  When ``rel`` is supplied, ``shard_paths`` additionally holds the same
    shards as **repo-relative** paths, matching ``cognition_runtime``'s
    ``parse_shard_index``.  Use ``shard_paths`` when joining with the repo root.
    """
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines[:INDEX_SCAN_LINES]) if line.strip() == INDEX_MARKER), None)
    if start is None:
        return None
    meta: dict[str, str] = {}
    closed = False
    for line in lines[start + 1:]:
        stripped = line.strip()
        if stripped == "-->":
            closed = True
            break
        if not stripped or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        meta[key.strip()] = value.strip()
    if not closed or not meta.get("shard_root"):
        raise ValueError("SHARD_INDEX_MARKER_UNTERMINATED")
    try:
        table = text.split(TABLE_START, 1)[1].split(TABLE_END, 1)[0]
    except IndexError as exc:
        raise ValueError("SHARD_INDEX_TABLE_MISSING") from exc
    shards: list[str] = []
    for line in table.splitlines():
        match = ROW_RE.match(line.strip())
        if not match:
            continue
        path = match.group(3).strip()
        if path.startswith("<") and path.endswith(">"):
            path = path[1:-1]
        shards.append(path)
    if not shards:
        raise ValueError("SHARD_INDEX_TABLE_EMPTY")
    result = {"logical_id": meta.get("logical_id"), "mode": meta.get("mode"),
              "shard_root": meta["shard_root"], "last_shard": meta.get("last_shard"),
              "append_target": meta.get("append_target"), "shards": shards}
    if rel is not None:
        base = PurePosixPath(rel).parent
        result["shard_paths"] = [link if str(base) == "." else (base / link).as_posix()
                                 for link in shards]
    return result


def shard_body(shard_text: str) -> str:
    """Strip the shard marker block, the leading H1 and the following blank line."""
    lines = shard_text.splitlines(keepends=True)
    start = next((i for i, line in enumerate(lines) if line.strip() == SHARD_MARKER), None)
    if start is None:
        return shard_text
    index = start
    for offset in range(start + 1, len(lines)):
        if lines[offset].strip() == "-->":
            index = offset
            break
    body = lines[index + 1:]
    while body and not body[0].strip():
        body.pop(0)
    if body and body[0].startswith("# "):
        body.pop(0)
        while body and not body[0].strip():
            body.pop(0)
    return "".join(body)


def logical_text(root: Path, rel: str) -> str | None:
    """Return the reconstructed logical text, or None when ``rel`` is not an index."""
    path = root / rel
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    index = parse_index(text, rel)
    if index is None:
        return None
    stem = PurePosixPath(rel).stem
    parts: list[str] = []
    for shard_rel in index["shard_paths"]:
        parts.append(shard_body((root / shard_rel).read_text(encoding="utf-8")))
    if index["shard_root"] != stem:
        raise ValueError(f"SHARD_ROOT_MISMATCH:{rel}")
    return "".join(parts)
