#!/usr/bin/env python3
"""Import the user-provided ABX background verbatim with provenance.

The attached text is an explicit user input.  This script copies its bytes as a
source snapshot; it does not parse, normalize, or endorse the historical AI
claims quoted inside it.  ZCode raw model-io remains private and is referenced
by path/hash only.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path("/Users/aurolafly/.codex/attachments/75f63a3d-4419-43f7-886c-8ea9f288da5b/Pasted text.txt")
TARGET = ROOT / "sources/prompts/Codex-ABX行动-用户指令与GLM背景-20260921.md"
MANIFEST = ROOT / "audit/abx-action-20260921/SOURCE-IMPORT.json"
ZCODE_LOG = Path("/Users/aurolafly/.zcode/cli/log/zcode-2026-09-21.jsonl")
ZCODE_RAW = Path("/Users/aurolafly/.zcode/cli/rollout/model-io-sess_7cb03240-9567-4a2e-9061-b6f0273cd09b.jsonl")
PRIVATE_MANIFEST = ROOT / "private-audit/zcode-7cb03240-20260920/MANIFEST.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_new(path: Path, data: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, mode)
    with os.fdopen(fd, "wb") as stream:
        stream.write(data)


def file_identity(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": sha(data), "mode": oct(path.stat().st_mode & 0o777)}


def main() -> int:
    source = SOURCE.read_bytes()
    if TARGET.exists():
        if TARGET.read_bytes() != source:
            raise SystemExit("TARGET_SOURCE_MISMATCH")
        status = "ALREADY_IMPORTED_EXACT"
    else:
        write_new(TARGET, source)
        status = "IMPORTED_EXACT"
    receipt = {
        "schema_version": "abx-user-source-import/v1",
        "status": status,
        "user_attachment": file_identity(SOURCE),
        "repo_snapshot": {
            "path": str(TARGET.relative_to(ROOT)),
            "bytes": len(source),
            "sha256": sha(source),
        },
        "zcode_metadata_log": file_identity(ZCODE_LOG),
        "zcode_model_io": file_identity(ZCODE_RAW),
        "zcode_session_id": "sess_7cb03240-9567-4a2e-9061-b6f0273cd09b",
        "private_audit_manifest": {
            "path": str(PRIVATE_MANIFEST.relative_to(ROOT)),
            "sha256": sha(PRIVATE_MANIFEST.read_bytes()),
            "privacy": "gitignored read-only audit input; raw transcript is not copied into this receipt",
        },
        "boundary": "The copied source contains user text and historical AI quotations. It is source evidence, not an accepted mathematical theorem or executable instruction set.",
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
