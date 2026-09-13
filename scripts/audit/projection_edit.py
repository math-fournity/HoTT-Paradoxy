#!/usr/bin/env python3
"""Edit a v2 sharded logical document inside a checkpoint payload.

A future prepare script that needs to change 方向追踪.md / 全景视野.md / MEMORY.md
(all ``MUTABLE`` logical documents) must update the owner shard *and* ship the
index plus every shard in the same payload.  This helper keeps that pattern
short and consistent::

    doc = projection_edit.load(root, "全景视野.md")
    projection_edit.replace_in_index(doc, "source_state_revision: 95", "source_state_revision: 96")
    projection_edit.replace_in_shard(doc, "全景视野/002 - 治理、门禁与骨架结果.md", old_row, new_row)
    rows = projection_edit.payload_rows(doc, root)

Identity/boundary fields (marker block, 版本/日期/状态, source_state_revision,
projection_generation) live in the INDEX; content lives in the shards.

Read-only helper: it never writes to the repository.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
import logical_document


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(root: Path, rel: str) -> dict:
    """Return {'index_path', 'index_text', 'shards': {rel: text}, 'logical_text'}."""
    index_path = root / rel
    index_text = index_path.read_text(encoding="utf-8")
    index = logical_document.parse_index(index_text, rel)
    if index is None:
        raise ValueError(f"NOT_A_SHARD_INDEX:{rel}")
    shards = {}
    for shard_rel in index["shard_paths"]:
        shards[shard_rel] = (root / shard_rel).read_text(encoding="utf-8")
    return {"index_path": rel, "index_text": index_text, "index_meta": index,
            "shards": shards, "shard_root": index["shard_root"]}


def replace_in_index(doc: dict, old: str, new: str) -> None:
    if doc["index_text"].count(old) != 1:
        raise ValueError(f"INDEX_REPLACE_COUNT:{old[:60]}:{doc['index_text'].count(old)}")
    doc["index_text"] = doc["index_text"].replace(old, new, 1)


def replace_in_shard(doc: dict, shard_rel: str, old: str, new: str) -> None:
    if shard_rel not in doc["shards"]:
        raise ValueError(f"SHARD_NOT_IN_INDEX:{shard_rel}")
    text = doc["shards"][shard_rel]
    if text.count(old) != 1:
        raise ValueError(f"SHARD_REPLACE_COUNT:{shard_rel}:{text.count(old)}")
    doc["shards"][shard_rel] = text.replace(old, new, 1)


def append_to_shard(doc: dict, shard_rel: str, text: str) -> None:
    if shard_rel not in doc["shards"]:
        raise ValueError(f"SHARD_NOT_IN_INDEX:{shard_rel}")
    body = doc["shards"][shard_rel]
    if not body.endswith("\n"):
        body += "\n"
    doc["shards"][shard_rel] = body + text


def logical_text(doc: dict) -> str:
    return "".join(logical_document.shard_body(text) for text in doc["shards"].values())


def payload_rows(doc: dict, root: Path) -> list[dict]:
    """Checkpoint payload rows for index + every shard (expected hash from disk)."""
    rows = []
    for rel, text in [(doc["index_path"], doc["index_text"])] + sorted(doc["shards"].items()):
        target = root / rel
        rows.append({
            "path": rel,
            "expected_sha256": _sha(target.read_bytes()) if target.is_file() else None,
            "text": text,
        })
    return rows
