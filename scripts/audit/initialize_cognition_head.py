#!/usr/bin/env python3
"""Create the initial cognition HEAD receipt for the current immutable state."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".codex/research/hott/STATE.json"
TRACKED = [
    ROOT / "MEMORY.md",
    ROOT / "方向追踪.md",
    ROOT / "全景视野.md",
    ROOT / ".codex/research/hott/FRONTIER.md",
    ROOT / ".codex/research/hott/LESSONS.md",
    ROOT / ".codex/research/hott/RESUME.md",
    STATE,
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    if state.get("schema_version") not in {"hott-working-state/v1", "hott-working-state/v2"}:
        raise SystemExit("STATE_SCHEMA")
    if not state.get("latest_session"):
        raise SystemExit("LATEST_SESSION_MISSING")
    receipt = {
        "schema_version": "cognition-head/v1",
        "revision": state["revision"],
        "latest_session": state["latest_session"],
        "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "tracked": {str(path.relative_to(ROOT)): sha(path) for path in TRACKED},
        "initialized_by": "scripts/audit/initialize_cognition_head.py",
    }
    target = ROOT / ".codex/cognition/HEAD.json"
    target.write_text(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "INITIALIZED", "revision": state["revision"], "latest_session": state["latest_session"], "head": str(target)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
