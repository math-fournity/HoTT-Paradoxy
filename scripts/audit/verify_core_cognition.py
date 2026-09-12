#!/usr/bin/env python3
"""Verify the core-cognition Markdown/manifest round trip.

This validator checks identity, order, exact payload hashes, source-file hashes,
message coverage, and contiguous IDs.  It does not judge the mathematical
truth of any user statement and it does not claim that a model understood the
file merely because the file was read.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_core(text: str) -> list[tuple[str, dict[str, object], str]]:
    lines = text.splitlines(keepends=True)
    output: list[tuple[str, dict[str, object], str]] = []
    i = 0
    while i < len(lines):
        match = re.match(r"^### (KC-[0-9]{6}) · .*$", lines[i].rstrip("\r\n"))
        if not match:
            i += 1
            continue
        unit_id = match.group(1)
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines) or not lines[i].startswith("<!-- KC-METADATA "):
            raise ValueError(f"{unit_id}: metadata missing")
        meta_line = lines[i].rstrip("\r\n")
        if not meta_line.endswith(" -->"):
            raise ValueError(f"{unit_id}: malformed metadata")
        metadata = json.loads(meta_line[len("<!-- KC-METADATA ") : -4])
        if metadata.get("id") != unit_id:
            raise ValueError(f"{unit_id}: metadata id mismatch")
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines):
            raise ValueError(f"{unit_id}: payload missing")
        opening = lines[i].rstrip("\r\n")
        fence_match = re.fullmatch(r"(~{3,})text", opening)
        if not fence_match:
            raise ValueError(f"{unit_id}: opening fence missing")
        marker = fence_match.group(1)
        i += 1
        payload_lines: list[str] = []
        while i < len(lines):
            candidate = lines[i].rstrip("\r\n")
            if candidate == marker:
                break
            payload_lines.append(lines[i])
            i += 1
        if i >= len(lines):
            raise ValueError(f"{unit_id}: closing fence missing")
        payload = "".join(payload_lines)
        if payload.endswith("\n"):
            payload = payload[:-1]
        if payload.endswith("\r"):
            payload = payload[:-1]
        output.append((unit_id, metadata, payload))
        i += 1
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--core", type=Path, default=Path("核心认知.md"))
    parser.add_argument("--manifest", type=Path, default=Path("核心认知.manifest.json"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    core_path = root / args.core
    manifest_path = root / args.manifest
    core_bytes = core_path.read_bytes()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "core-cognition/v1":
        raise SystemExit("FAIL schema_version")
    actual_core_sha = sha(core_bytes)
    if actual_core_sha != manifest.get("core_document_sha256"):
        raise SystemExit(f"FAIL core hash: {actual_core_sha} != {manifest.get('core_document_sha256')}")
    records = parse_core(core_bytes.decode("utf-8"))
    unit_rows = manifest.get("units")
    if not isinstance(unit_rows, list):
        raise SystemExit("FAIL manifest units missing")
    if len(records) != len(unit_rows):
        raise SystemExit(f"FAIL unit count: core={len(records)} manifest={len(unit_rows)}")
    expected_ids = [f"KC-{i:06d}" for i in range(1, len(records) + 1)]
    actual_ids = [item[0] for item in records]
    if actual_ids != expected_ids:
        raise SystemExit("FAIL non-contiguous or reordered IDs")
    for (unit_id, metadata, payload), expected in zip(records, unit_rows):
        if metadata != expected:
            raise SystemExit(f"FAIL metadata mismatch: {unit_id}")
        payload_hash = sha(payload.encode("utf-8"))
        if payload_hash != expected.get("unit_sha256"):
            raise SystemExit(f"FAIL payload hash: {unit_id}")
        if len(payload.encode("utf-8")) != expected.get("unit_bytes"):
            raise SystemExit(f"FAIL payload bytes: {unit_id}")
    files = manifest.get("files")
    if not isinstance(files, list):
        raise SystemExit("FAIL files missing")
    for row in files:
        path = root / str(row["path"])
        actual = sha(path.read_bytes())
        if actual != row["sha256"]:
            raise SystemExit(f"FAIL source hash: {path}")
    dispositions = manifest.get("message_disposition")
    if not isinstance(dispositions, list):
        raise SystemExit("FAIL message disposition missing")
    message_ids = [str(row["source_message_id"]) for row in dispositions]
    if len(message_ids) != len(set(message_ids)):
        raise SystemExit("FAIL duplicate source message IDs")
    units_by_message: Counter[str] = Counter(str(row["source_message_id"]) for row in unit_rows)
    for row in dispositions:
        if int(row["unit_count"]) != units_by_message[str(row["source_message_id"])] and row["disposition"] == "INCLUDED":
            raise SystemExit(f"FAIL disposition unit count: {row['source_message_id']}")
    included_messages = {str(row["source_message_id"]) for row in dispositions if row["disposition"] == "INCLUDED"}
    if not set(units_by_message) <= included_messages:
        raise SystemExit("FAIL unit references excluded message")
    counts = manifest.get("counts", {})
    if counts.get("core_units") != len(records) or counts.get("messages_parsed") != len(dispositions):
        raise SystemExit("FAIL summary counts")
    print(json.dumps({
        "status": "PASS",
        "core_units": len(records),
        "messages": len(dispositions),
        "included_messages": len(included_messages),
        "core_sha256": actual_core_sha,
        "source_files": len(files),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
