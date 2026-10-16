#!/usr/bin/env python3
"""Run one zero-theory Codex App Server isolation health check for Pattern P.

The script deliberately reuses the shared, versioned isolated-CODEX_HOME auth
gates rather than copying credentials into a normal worker directory.  Its only
model input is a fixed marker.  Raw wire, stderr, prompt-input JSON and detailed
home receipt remain in a private 0700/0600 experiment root; stdout is a safe
summary with no credential content, hash, size or path.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import time
from typing import Any


MARKER = "P_DAG_APPSERVER_ISOLATION_HEALTH_PASS"
MODEL = "gpt-5.6-terra"
EFFORT = "max"
TIER = "default"
PERMISSIONS = "governance-regression-fresh"
HEALTH_AGENT = """# Isolated P-DAG App Server Health Worker

This directory is a zero-theory health fixture. Follow only the exact user turn.
Do not read files, use tools, run commands, inspect credentials/configuration,
access networks, delegate, or create artifacts. Return the exact marker requested
by the user turn and then stop.
"""
HEALTH_README = "# P-DAG isolated App Server health fixture\n\nNo theory input.\n"


def private_json(path: Path, value: Any, regression: Any) -> None:
    """Write private JSON through the shared atomic writer."""
    regression.atomic_write_json(path, value)
    path.chmod(0o600)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def require_clean_method_repo(method_repo: Path) -> None:
    status = subprocess.run(
        ["git", "-C", str(method_repo), "status", "--porcelain=v1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if status.returncode != 0 or status.stdout.strip():
        raise RuntimeError("method repository must be a clean worktree before auth borrowing")
    for relative in ("tools/governance_regression.py", "tools/agent_session_broker.py"):
        if not (method_repo / relative).is_file():
            raise RuntimeError(f"method repository lacks required asset: {relative}")


def write_health_workspace(paths: dict[str, Path], regression: Any) -> None:
    """Replace only the text-only probe instructions after pre-copy gates pass."""
    regression.atomic_write_text(paths["probe_agents"], HEALTH_AGENT, 0o600)
    regression.atomic_write_text(paths["probe_readme"], HEALTH_README, 0o600)


def prompt_input_gate(paths: dict[str, Path], regression: Any, project_root: Path) -> dict[str, Any]:
    """Audit model-visible input without asking a model to sample."""
    env = regression.regression_process_env(paths)
    command = [
        "codex", "-C", str(paths["probe_workspace"]), "debug", "prompt-input",
        f"Return exactly one line: {MARKER}",
    ]
    result = subprocess.run(command, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, timeout=30, check=False)
    raw = result.stdout.encode("utf-8")
    paths["private"].mkdir(parents=True, exist_ok=True, mode=0o700)
    prompt_input = paths["private"] / "prompt-input.json"
    prompt_stderr = paths["private"] / "prompt-input.stderr"
    prompt_input.write_bytes(raw)
    prompt_input.chmod(0o600)
    prompt_stderr.write_text(result.stderr, encoding="utf-8")
    prompt_stderr.chmod(0o600)
    forbidden = {
        "project_root_absent": str(project_root.resolve()) not in result.stdout,
        "questioning_delay_absent": "QuestioningDelay" not in result.stdout,
        "zfc_q_absent": "ZFC_Q_LOCATED" not in result.stdout,
        "power_set_absent": "Power Set" not in result.stdout,
        # The local health contract itself names P-DAG, and Codex can list the
        # current home only as a denied path or Skill-root locator.  Neither is
        # an answer leak.  Reject actual P-project material and answer markers.
        "p_pattern_skill_absent": "hott-pattern-p-dynamic-dag-orchestration" not in result.stdout,
        "home_canary_present": "HOME_INSTRUCTION_CANARY:" in result.stdout,
        "workspace_contract_present": "Isolated P-DAG App Server Health Worker" in result.stdout,
    }
    return {
        "returncode": result.returncode,
        "input_sha256": sha256_bytes(raw),
        "stderr_sha256": sha256_bytes(result.stderr.encode("utf-8")),
        "bytes": len(raw),
        "checks": forbidden,
        "status": "PASS" if result.returncode == 0 and all(forbidden.values()) else "FAIL",
    }


async def run_appserver_health(paths: dict[str, Path], regression: Any, broker: Any) -> dict[str, Any]:
    """Run a single no-tool App Server turn under the verified fresh profile."""
    terminal = asyncio.Event()
    agent_parts: list[str] = []
    completed: dict[str, Any] = {}
    counts = {"command": 0, "file_change": 0, "approval_request": 0}
    started = time.monotonic()

    async def notify(method: str, params: dict[str, Any]) -> None:
        if method == "item/agentMessage/delta" and isinstance(params.get("delta"), str):
            agent_parts.append(params["delta"])
        if method == "item/completed":
            item = params.get("item") if isinstance(params.get("item"), dict) else {}
            kind = str(item.get("type") or "")
            if kind == "commandExecution":
                counts["command"] += 1
            elif kind == "fileChange":
                counts["file_change"] += 1
        if method == "turn/completed":
            completed.update(params)
            terminal.set()

    async def deny(method: str, params: dict[str, Any]) -> Any:
        counts["approval_request"] += 1
        raise broker.BrokerError(403, f"P-DAG health controller denies {method}")

    rpc = broker.JsonRpcProcess(
        command=["codex", "app-server", "--listen", "stdio://"],
        cwd=paths["probe_workspace"],
        trace_path=paths["private"] / "wire.jsonl",
        stderr_path=paths["private"] / "stderr.log",
        notification_handler=notify,
        request_handler=deny,
    )
    thread_id: str | None = None
    turn_id: str | None = None
    thread_start: dict[str, Any] = {}
    try:
        await rpc.start()
        await rpc.request(
            "initialize",
            {"clientInfo": {"name": "p-dag-isolation-health", "version": "1"},
             "capabilities": {"experimentalApi": True}},
            timeout=60,
        )
        await rpc.notify("initialized", {})
        thread_start = await rpc.request(
            "thread/start",
            {
                "cwd": str(paths["probe_workspace"]),
                "model": MODEL,
                "allowProviderModelFallback": False,
                "permissions": PERMISSIONS,
                "approvalPolicy": "never",
                "serviceTier": TIER,
                "ephemeral": True,
            },
            timeout=90,
        )
        thread = thread_start.get("thread") if isinstance(thread_start.get("thread"), dict) else {}
        thread_id = str(thread.get("id") or "")
        if not thread_id:
            raise RuntimeError("thread/start returned no thread id")
        exact_start = {
            "model": thread_start.get("model") == MODEL,
            "reasoning_effort": thread_start.get("reasoningEffort") == EFFORT,
            "approval_policy": thread_start.get("approvalPolicy") == "never",
            "permission_profile": isinstance(thread_start.get("activePermissionProfile"), dict)
            and thread_start["activePermissionProfile"].get("id") == PERMISSIONS,
            "cwd": thread_start.get("cwd") == str(paths["probe_workspace"]),
        }
        if not all(exact_start.values()):
            raise RuntimeError(f"thread/start echo mismatch: {exact_start}")
        turn_start = await rpc.request(
            "turn/start",
            {
                "threadId": thread_id,
                "model": MODEL,
                "effort": EFFORT,
                "serviceTier": TIER,
                "input": [{"type": "text", "text": f"Return exactly one line: {MARKER}"}],
            },
            timeout=90,
        )
        turn = turn_start.get("turn") if isinstance(turn_start.get("turn"), dict) else {}
        turn_id = str(turn.get("id") or "")
        if not turn_id:
            raise RuntimeError("turn/start returned no turn id")
        try:
            await asyncio.wait_for(terminal.wait(), timeout=90)
        except asyncio.TimeoutError:
            await rpc.request("turn/interrupt", {"threadId": thread_id, "turnId": turn_id}, timeout=30)
            try:
                await asyncio.wait_for(terminal.wait(), timeout=20)
            except asyncio.TimeoutError:
                return {"status": "TIMEOUT", "thread_id": thread_id, "turn_id": turn_id,
                        "exact_start": exact_start, **counts}
        private_json(paths["private"] / "thread-start.json", thread_start, regression)
        private_json(paths["private"] / "turn-start.json", turn_start, regression)
        text = "".join(agent_parts).strip()
        expected = text == MARKER
        completed_turn = completed.get("turn") if isinstance(completed.get("turn"), dict) else {}
        return {
            "status": "PASS" if expected and all(value == 0 for value in counts.values()) else "FAIL",
            "thread_id": thread_id,
            "turn_id": turn_id,
            "exact_start": exact_start,
            "agent_marker_exact": expected,
            "turn_status": completed_turn.get("status"),
            "elapsed_seconds": round(time.monotonic() - started, 3),
            **counts,
        }
    finally:
        await rpc.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method-repo", type=Path, required=True)
    parser.add_argument("--private-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--authorization", required=True,
                        help="must include R-035 and the user-authorized P-DAG scope")
    parser.add_argument("--project-root", type=Path, required=True)
    args = parser.parse_args()
    if "R-035" not in args.authorization:
        raise SystemExit("--authorization must include R-035")
    method_repo = args.method_repo.resolve()
    project_root = args.project_root.resolve()
    require_clean_method_repo(method_repo)
    sys.path.insert(0, str(method_repo / "tools"))
    import governance_regression as regression  # type: ignore
    import agent_session_broker as broker  # type: ignore

    experiment_root = (args.private_root.resolve() / "governance-regression")
    paths = regression.regression_home_paths(experiment_root, args.run_id, method_repo)
    receipt: dict[str, Any] | None = None
    summary: dict[str, Any] = {"run_id": args.run_id, "status": "NOT_STARTED"}
    old_env = dict(os.environ)
    try:
        receipt = regression.prepare_regression_home(paths)
        receipt = regression.run_home_permission_gate(receipt, paths)
        if receipt.get("verdict", {}).get("status") != "PASS":
            raise RuntimeError("pre-auth sandbox permission gate failed")
        receipt = regression.prepare_auth_borrowing_gate(receipt, paths)
        if receipt.get("verdict", {}).get("status") != "PASS":
            raise RuntimeError("pre-copy auth borrowing gate failed")
        write_health_workspace(paths, regression)
        context = prompt_input_gate(paths, regression, project_root)
        private_json(paths["private"] / "prompt-input-gate.json", context, regression)
        if context["status"] != "PASS":
            raise RuntimeError("model-visible prompt preflight failed")
        receipt = regression.copy_authorized_auth(
            receipt, paths, source_auth=paths["current_auth"], authorization=args.authorization
        )
        if receipt.get("verdict", {}).get("status") != "PASS":
            raise RuntimeError("authorized auth copy/login gate failed")
        receipt = regression.run_borrowed_auth_permission_gate(receipt, paths)
        if receipt.get("verdict", {}).get("status") != "PASS":
            raise RuntimeError("post-auth sandbox permission gate failed")
        os.environ.clear()
        os.environ.update(regression.regression_process_env(paths))
        behavior = asyncio.run(run_appserver_health(paths, regression, broker))
        private_json(paths["private"] / "health-behavior.json", behavior, regression)
        summary = {
            "run_id": args.run_id,
            "status": behavior["status"],
            "model": MODEL,
            "effort": EFFORT,
            "permission_profile": PERMISSIONS,
            "prompt_input_gate": context["status"],
            "auth_borrowed": receipt.get("auth", {}).get("shape") == "AUTH_BORROWED_LOCAL_FILE",
            "post_auth_gate": receipt.get("permission_negatives", {}).get("status"),
            "agent_marker_exact": behavior.get("agent_marker_exact"),
            "command_count": behavior.get("command"),
            "file_change_count": behavior.get("file_change"),
            "approval_request_count": behavior.get("approval_request"),
            "source_auth_content_recorded": False,
        }
    except Exception as exc:
        summary = {"run_id": args.run_id, "status": "FAIL", "error": type(exc).__name__,
                   "message": str(exc)[:500], "source_auth_content_recorded": False}
    finally:
        os.environ.clear()
        os.environ.update(old_env)
        if paths.get("auth") and paths["auth"].exists() and not paths["auth"].is_symlink():
            paths["auth"].unlink()
        if receipt is not None:
            private_json(paths["private"] / "home-receipt-final.json", receipt, regression)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if summary.get("status") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
