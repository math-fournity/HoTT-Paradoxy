#!/usr/bin/env python3
"""Create the initial cognition HEAD receipt for the current immutable state."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_DIR = ROOT / ".codex/tools"
STATE = ROOT / ".codex/research/hott/STATE.json"

sys.path.insert(0, str(RUNTIME_DIR))
import cognition_runtime as runtime  # noqa: E402  (project-local loader; single source of routing rules)

# The tracked set is exactly runtime.MUTABLE plus the shards of any sharded
# MUTABLE document; keep one source of truth so a new member cannot be missed.
TRACKED = [ROOT / rel for rel in runtime.MUTABLE]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_paths() -> dict[str, str]:
    """Track every MUTABLE document plus the shards of any sharded logical document."""
    tracked = {str(path.relative_to(ROOT)): sha(path) for path in TRACKED}
    for rel in runtime.MUTABLE:
        index = runtime.parse_shard_index((ROOT / rel).read_bytes(), rel)
        if index is None:
            continue
        for row in index["shards"]:
            tracked[row["path"]] = sha(ROOT / row["path"])
    return tracked


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
        "tracked": tracked_paths(),
        "initialized_by": "scripts/audit/initialize_cognition_head.py",
    }
    target = ROOT / ".codex/cognition/HEAD.json"
    target.write_text(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "INITIALIZED", "revision": state["revision"], "latest_session": state["latest_session"], "head": str(target)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
