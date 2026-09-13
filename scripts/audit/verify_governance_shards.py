#!/usr/bin/env python3
"""Run the project-pinned governance shard validator and emit a receipt.

Read-only: the validator only reads Markdown.  The receipt is written to
``--out`` (default: stdout only, no file).  A pinned sha256 makes a silent
local edit of the vendored validator fail closed instead of passing unnoticed.

Exit codes: 0 = PASS, 1 = validator FAIL or pinned-copy drift, 2 = usage error.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = Path(__file__).resolve().parent / "validate_governance_shards.py"
PINNED_VALIDATOR_SHA256 = "788dee0f376dcba2c9e0ba966560ad4862cbe2067465f3a584099640328de0fe"
SOURCE_COMMIT = "2e4e4d2dbe13046470bc79e98e64735312ee9bd5"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--out", type=Path, help="write the JSON receipt to this path")
    args = parser.parse_args(argv)
    root = args.project_root.resolve()
    try:
        validator_bytes = VALIDATOR.read_bytes()
    except OSError as exc:
        print(json.dumps({"status": "BLOCKED", "error": f"validator unreadable: {exc}"}, ensure_ascii=False))
        return 1
    digest = sha256(validator_bytes)
    receipt: dict[str, object] = {
        "schema_version": "governance-shard-verification/v1",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "project_root": str(root),
        "validator": str(VALIDATOR.relative_to(ROOT)) if VALIDATOR.is_relative_to(ROOT) else str(VALIDATOR),
        "validator_sha256": digest,
        "validator_source_commit": SOURCE_COMMIT,
        "pinned_validator_sha256": PINNED_VALIDATOR_SHA256,
        "command": [sys.executable, "-B", str(VALIDATOR), "--scan", str(root)],
    }
    if digest != PINNED_VALIDATOR_SHA256:
        receipt.update({"status": "BLOCKED", "reason": "VALIDATOR_PINNED_COPY_DRIFT"})
        _emit(receipt, args.out)
        return 1
    proc = subprocess.run(receipt["command"], capture_output=True, text=True, check=False)
    stdout = proc.stdout
    stderr = proc.stderr
    receipt.update({
        "exit_code": proc.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "status": "PASS" if proc.returncode == 0 else "FAIL",
        "indexes": _count(stdout, "indexes="),
        "soft_target_notices": _count(stdout, "notices="),
        "line_targets_blocking": False,
    })
    _emit(receipt, args.out)
    return 0 if proc.returncode == 0 else 1


def _count(text: str, needle: str) -> int | None:
    marker = text.find(needle)
    if marker < 0:
        return None
    tail = text[marker + len(needle):]
    digits = ""
    for char in tail:
        if char.isdigit():
            digits += char
        else:
            break
    return int(digits) if digits else None


def _emit(receipt: dict[str, object], out: Path | None) -> None:
    body = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if out is not None:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
    print(body, end="")


if __name__ == "__main__":
    raise SystemExit(main())
