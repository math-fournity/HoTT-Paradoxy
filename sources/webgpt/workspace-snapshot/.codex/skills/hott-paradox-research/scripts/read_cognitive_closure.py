#!/usr/bin/env python3
"""Read the complete designated closure in consecutive, unabridged chunks.

Standard library only. Does not write files, run project code, access the network,
load a cached summary, or certify that a model has received all tool responses.
Every Skill invocation must start at line 1 again.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

CLOSURE_RELATIVE_PATH = "认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md"
CLOSURE_ID = "CC-20260901-z-law-final-temporal-negation-naive-set-hott"

class ClosureReadError(RuntimeError):
    """No partial/summary fallback is permitted."""

def infer_project_root(script_path: Path | None = None) -> Path:
    script = (script_path or Path(__file__)).resolve()
    expected = (".codex", "skills", "hott-paradox-research", "scripts")
    if tuple(script.parts[-5:-1]) != expected:
        raise ClosureReadError("Cannot infer the project root from this script location; use the exact --project-root.")
    return script.parents[4]

def read_chunk(
    project_root: Path | str | None = None,
    *,
    start_line: int = 1,
    max_bytes: int = 10000,
    expected_sha256: str | None = None,
) -> dict:
    """Return a full consecutive range with raw text, never a summary.

    expected_sha256 binds chunks to one file version, not to a previous execution.
    A read reaching EOF does not prove earlier chunks entered a model context.
    """
    if isinstance(start_line, bool) or not isinstance(start_line, int) or start_line < 1:
        raise ClosureReadError("start_line must be a positive integer.")
    if isinstance(max_bytes, bool) or not isinstance(max_bytes, int) or not 1 <= max_bytes <= 131072:
        raise ClosureReadError("max_bytes must be between 1 and 131072.")
    if start_line != 1 and expected_sha256 is None:
        raise ClosureReadError("Continuation requires this invocation's first-chunk SHA-256; start each invocation at line 1.")
    if expected_sha256 is not None and (
        len(expected_sha256) != 64 or any(c not in "0123456789abcdef" for c in expected_sha256)
    ):
        raise ClosureReadError("expected_sha256 must be 64 lowercase hexadecimal characters.")

    root = infer_project_root() if project_root is None else Path(project_root).resolve()
    path = root / CLOSURE_RELATIVE_PATH
    current = root
    for component in Path(CLOSURE_RELATIVE_PATH).parts:
        current = current / component
        if current.is_symlink():
            raise ClosureReadError("The designated closure path must not redirect through a symlink.")
    if not path.is_file():
        raise ClosureReadError(f"BLOCKED_FULL_CLOSURE_LOAD: designated unpacked file not found: {path}")

    before = path.stat()
    data = path.read_bytes()
    after = path.stat()
    if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
        raise ClosureReadError("File changed during the read. Restart at line 1.")
    digest = hashlib.sha256(data).hexdigest()
    if expected_sha256 is not None and digest != expected_sha256:
        raise ClosureReadError("File SHA-256 changed between chunks. Restart at line 1; do not combine snapshots.")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ClosureReadError("Closure is not valid UTF-8; no replacement/summary allowed.") from exc
    if not text.strip():
        raise ClosureReadError("Closure file is empty.")
    if f"Closure ID：`{CLOSURE_ID}`" not in "\n".join(text.splitlines()[:12]):
        raise ClosureReadError("The file at the designated path has a different Closure ID.")

    lines = text.splitlines(keepends=True)
    if start_line > len(lines):
        raise ClosureReadError("start_line exceeds the actual last line; prior EOF is not a cached load certificate.")
    selected = []
    used = 0
    i = start_line - 1
    while i < len(lines):
        b = len(lines[i].encode("utf-8"))
        if used + b > max_bytes:
            if not selected:
                raise ClosureReadError(f"Line {i+1} requires {b} bytes. Increase max_bytes; the line will not be truncated.")
            break
        selected.append(lines[i])
        used += b
        i += 1
    chunk = "".join(selected)
    return {
        "project_root": str(root),
        "path": str(path),
        "closure_id": CLOSURE_ID,
        "file_sha256": digest,
        "total_bytes": len(data),
        "total_lines": len(lines),
        "start_line": start_line,
        "end_line": i,
        "chunk_bytes": len(chunk.encode("utf-8")),
        "next_start_line": None if i == len(lines) else i + 1,
        "file_eof": i == len(lines),
        "text": chunk,
        "model_context_completeness": "NOT_CERTIFIED_BY_READER",
        "invocation_policy": "RESTART_AT_LINE_1_EVERY_INVOCATION_OR_CONTEXT_COMPACTION",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--start-line", type=int, default=1)
    parser.add_argument("--max-bytes", type=int, default=10000)
    parser.add_argument("--expected-sha256")
    args = parser.parse_args()
    try:
        result = read_chunk(args.project_root, start_line=args.start_line,
                            max_bytes=args.max_bytes, expected_sha256=args.expected_sha256)
        body = result.pop("text")
        print("BEGIN_CLOSURE_CHUNK")
        print(json.dumps(result, ensure_ascii=False))
        print("BEGIN_ORIGINAL_TEXT")
        sys.stdout.write(body)
        if not body.endswith("\n"):
            sys.stdout.write("\n")
        print("END_ORIGINAL_TEXT")
        print("END_CLOSURE_CHUNK")
        return 0
    except (ClosureReadError, OSError) as exc:
        print(json.dumps({"status": "BLOCKED_FULL_CLOSURE_LOAD", "error": str(exc)},
                         ensure_ascii=False), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
