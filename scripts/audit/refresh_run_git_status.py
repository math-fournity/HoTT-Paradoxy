#!/usr/bin/env python3
"""Refresh the git_status field of formal-proof-run/v1 receipts.

All receipt directories under HoTT/verification/runs/ are tracked and committed;
nothing has been pushed. Records the accurate state LOCAL_COMMITTED_NOT_PUSHED.
Does not touch non-formal (machine-overview-verify-run/*) schemas.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

NEW = "LOCAL_COMMITTED_NOT_PUSHED"


def tracked(run_dir: Path, root: Path) -> bool:
    rel = run_dir.relative_to(root).as_posix()
    out = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--error-unmatch", f"{rel}/RUN.json"],
        capture_output=True, text=True,
    )
    return out.returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    changed, unchanged, skipped = [], [], []
    for run_json in sorted((root / "HoTT/verification/runs").glob("*/RUN.json")):
        run = json.loads(run_json.read_bytes())
        if run.get("schema_version") != "formal-proof-run/v1":
            skipped.append(run_json.parent.name)
            continue
        if not tracked(run_json.parent, root):
            print(f"UNTRACKED {run_json.parent.name} -- left untouched")
            continue
        if run.get("git_status") == NEW:
            unchanged.append(run_json.parent.name)
            continue
        run["git_status"] = NEW
        if args.write:
            run_json.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(run_json.parent.name)

    print(f"changed={len(changed)} unchanged={len(unchanged)} skipped_other_schema={len(skipped)}")
    if changed and not args.write:
        print("(dry-run; re-run with --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
