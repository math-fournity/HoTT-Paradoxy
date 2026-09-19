#!/usr/bin/env python3
"""Reconcile one reviewed committed file with the derived cognition HEAD.

This recovery does not create or rewrite a historical checkpoint receipt.
It accepts only the exact drift independently located on 2026-09-19.
"""
import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "tracking-recovery"
TARGET = "MEMORY/001 - 当前执行队列.md"
OLD = "968fb7361d56df903378707cbd818a89bddea55ed3046108ba4c7b0b5ce82f0e"
NEW = "f8bb3441a8ae5273ab54b722f3b0d8e531c9a17ba03cbd0cccf509e3b3720d66"
BASE = "40b1ca78fe0e391201848923e09423808a2178ee"
CHANGE = "49d5286827e5cb9424025e421af3960abbec9192"
sha = lambda b: hashlib.sha256(b).hexdigest()

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("cognition", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runtime)
    hp = ROOT / runtime.HEAD
    before = hp.read_bytes()
    head = json.loads(before)
    state_bytes = (ROOT / runtime.STATE).read_bytes()
    state = json.loads(state_bytes)
    assert git("rev-parse", "HEAD").decode().strip() == BASE
    assert not (ROOT / runtime.LOCK).exists() and not (ROOT / runtime.TXN).exists()
    assert head["revision"] == state["revision"] == 171
    assert head["latest_session"] == state["latest_session"]
    assert not git("status", "--porcelain=v1", "--", TARGET, runtime.HEAD, runtime.STATE)
    assert sha(git("show", CHANGE + "^:" + TARGET)) == OLD
    assert sha(git("show", CHANGE + ":" + TARGET)) == NEW
    assert sha((ROOT / TARGET).read_bytes()) == NEW
    drift = [p for p, h in head["tracked"].items() if sha((ROOT / p).read_bytes()) != h]
    assert drift == [TARGET] and head["tracked"][TARGET] == OLD, drift
    # The only accepted semantic delta is the committed addition of release-plan item 27.
    delta = git("diff", CHANGE + "^", CHANGE, "--unified=0", "--", TARGET)
    report = {"status": "DRY_RUN", "authorization": "用户：先修复全项目加载与检查点，再执行",
              "role": "CANONICAL_INTEGRATOR_FOR_THIS_BOUNDED_RECOVERY",
              "target_head": BASE, "source_commit": CHANGE, "path": TARGET,
              "expected_old_sha256": OLD, "accepted_sha256": NEW,
              "state_sha256": sha(state_bytes), "state_changed": False,
              "historical_checkpoint_changed": False, "new_checkpoint_created": False}
    if args.apply:
        OUT.mkdir(parents=True, exist_ok=False)
        (OUT / "HEAD.before.json").write_bytes(before)
        (OUT / "accepted.diff").write_bytes(delta)
        head["tracked"][TARGET] = NEW
        head["updated_at_utc"] = runtime.stamp()
        after = runtime.dump(head)
        assert hp.read_bytes() == before and (ROOT / runtime.STATE).read_bytes() == state_bytes
        runtime.atomic(hp, after)
        (OUT / "HEAD.after.json").write_bytes(after)
        report.update(status="DERIVED_TRACKING_RECONCILED", head_before_sha256=sha(before), head_after_sha256=sha(after))
        (OUT / "REPAIR.json").write_bytes(runtime.dump(report))
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
