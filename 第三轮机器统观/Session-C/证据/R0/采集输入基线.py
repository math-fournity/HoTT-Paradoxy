"""Capture read-only Goal7 intake identities; does not certify cognition or mutate STATE."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent

def run(*args):
    return subprocess.check_output(args, cwd=ROOT)

def save_new(name, data):
    with (OUT / name).open("xb") as handle:
        handle.write(data)

def identity(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data), "lines": len(data.splitlines())}

plan_bytes = run("python3", "-B", ".codex/tools/cognition_runtime.py", "plan", "--profile", "research")
plan = json.loads(plan_bytes)
save_new("research-plan.json", plan_bytes)
save_new("git-status-before-z.bin", run("git", "status", "--porcelain=v1", "-z", "--untracked-files=all"))
save_new("git-index-before.patch", run("git", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"))
paths = ["AGENTS.md", ".codex/AGENTS.md", "goal-7.md", "最高指示.md",
         ".codex/cognition/TASK_ROUTING.md", ".codex/cognition/LOAD_SET.json",
         ".codex/cognition/PROTOCOL.md", ".codex/skills/SKILL_ROLES.json",
         ".codex/skills/hott-local-session-governance/SKILL.md",
         ".codex/skills/hott-machine-overview-execution/SKILL.md",
         ".codex/research/hott/STATE.json"]
receipt = {"recorded_at": datetime.now(timezone.utc).isoformat(),
           "purpose": "R0 input identity and pre-checkpoint working state only",
           "model_context": "NOT_CERTIFIED_BY_TOOL",
           "research_coverage": "NOT_ESTABLISHED",
           "head": run("git", "rev-parse", "HEAD").decode().strip(),
           "snapshot": plan["snapshot"], "revision": plan["revision"],
           "inputs": [identity(p) for p in paths],
           "four_set": [d for d in plan["documents"] if d["layer"] == "always_full_documents"],
           "actual_read_attestation": "../../执行记录/001 - R0接手与启动读取.md",
           "checkpoint": "NOT_APPLIED"}
save_new("INPUT-IDENTITY.json", (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode())
print(json.dumps({"snapshot": plan["snapshot"], "revision": plan["revision"],
                  "record": str(OUT / "INPUT-IDENTITY.json")}, ensure_ascii=False))
