#!/usr/bin/env python3
"""Run one sealed Pattern-P turn through the isolated Codex App Server lane.

The frozen prompt is sent only as the App Server turn input.  ``blind-discovery``
has no theory source, project answer, or prior result.  ``source-match`` permits
only a frozen source card in that prompt and still prohibits project answers and
tools.  Raw prompt-input/wire/stderr/final text remain in a private 0700/0600 run
tree; stdout intentionally contains only a safe execution summary.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


MODEL = "gpt-5.6-terra"
EFFORT = "max"
TIER = "default"
PERMISSIONS = "governance-regression-fresh"
BLIND_NO_CANDIDATE_TERMINALS = (
    "NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY",
    "NO_MODEL_RECALL_CANDIDATE / FORMATION_ORIGIN_NOT_SUPPLIED",
)
WORKER_AGENTS = """# Isolated Pattern-P Worker

This workspace contains no project answer, prior result, or task materials.
Follow only the exact user turn. Do not use tools, files, web, commands, Git,
credentials, configuration inspection, delegation, or artifact creation.
Return only the requested public answer and then stop.
"""
WORKER_README = "# Isolated blind-discovery fixture\n\nNo project or theory source is stored here.\n"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def private_json(path: Path, value: Any, regression: Any) -> None:
    regression.atomic_write_json(path, value)
    path.chmod(0o600)


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


def write_worker_workspace(paths: dict[str, Path], regression: Any) -> None:
    regression.atomic_write_text(paths["probe_agents"], WORKER_AGENTS, 0o600)
    regression.atomic_write_text(paths["probe_readme"], WORKER_README, 0o600)


def read_frozen_turn(prompt_file: Path) -> str:
    """Extract the sole fenced text payload; audit prose must not enter model input."""
    raw = prompt_file.read_text(encoding="utf-8")
    opener = "```text\n"
    start = raw.find(opener)
    if start < 0:
        raise RuntimeError("--prompt-file must contain one fenced text payload")
    end = raw.find("\n```", start + len(opener))
    if end < 0 or raw.find(opener, start + len(opener)) >= 0:
        raise RuntimeError("--prompt-file must contain exactly one fenced text payload")
    return raw[start + len(opener):end]


def prompt_input_gate(
    paths: dict[str, Path],
    regression: Any,
    project_root: Path,
    prompt: str,
    profile: str,
) -> dict[str, Any]:
    """Inspect the compiled prompt before auth is borrowed or a model is sampled."""
    env = regression.regression_process_env(paths)
    result = subprocess.run(
        ["codex", "-C", str(paths["probe_workspace"]), "debug", "prompt-input", prompt],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=30,
        check=False,
    )
    raw = result.stdout.encode("utf-8")
    paths["private"].mkdir(parents=True, exist_ok=True, mode=0o700)
    prompt_path = paths["private"] / "prompt-input.json"
    stderr_path = paths["private"] / "prompt-input.stderr"
    prompt_path.write_bytes(raw)
    prompt_path.chmod(0o600)
    stderr_path.write_text(result.stderr, encoding="utf-8")
    stderr_path.chmod(0o600)
    checks: dict[str, bool] = {
        "project_root_absent": str(project_root.resolve()) not in result.stdout,
        "p_pattern_skill_absent": "hott-pattern-p-dynamic-dag-orchestration" not in result.stdout,
        "worker_contract_present": "Isolated Pattern-P Worker" in result.stdout,
    }
    if profile == "blind-discovery":
        checks.update(
            {
                "questioning_delay_absent": "QuestioningDelay" not in result.stdout,
                "pedometer_semantics_absent": "PedometerSemantics" not in result.stdout,
                "zfc_q_absent": "ZFC_Q_LOCATED" not in result.stdout,
                "power_set_absent": "Power Set" not in result.stdout,
                "known_ua_answer_absent": "ua : (A ≃ B)" not in result.stdout,
                "universe_no_level_answer_absent": "universeHasNoLevel" not in result.stdout,
                "q_is_never_answer_absent": "QIsNever" not in result.stdout,
                "task_prompt_present": "You are a blind P-DISCOVERY mapper." in result.stdout,
            }
        )
    elif profile == "source-match":
        checks.update(
            {
                "source_profile_present": "You are a P-VALIDATION source mapper." in result.stdout,
                "frozen_source_card_present": "BEGIN FROZEN SOURCE CARD" in result.stdout,
                "old_p2_control_absent": "P2-DELAY-001" not in result.stdout,
                "old_p3_control_absent": "P3-DELAY-001" not in result.stdout,
                "old_h010_output_absent": "HOTT-DISCOVERY-010" not in result.stdout,
            }
        )
    else:
        raise RuntimeError(f"unknown Pattern-P runner profile: {profile}")
    return {
        "returncode": result.returncode,
        "input_sha256": sha256_bytes(raw),
        "stderr_sha256": sha256_bytes(result.stderr.encode("utf-8")),
        "bytes": len(raw),
        "checks": checks,
        "status": "PASS" if result.returncode == 0 and all(checks.values()) else "FAIL",
    }


async def run_discovery(
    paths: dict[str, Path],
    regression: Any,
    broker: Any,
    prompt: str,
    *,
    profile: str,
    observation_interval_seconds: float,
) -> dict[str, Any]:
    """Run one no-tool Pattern-P turn with observation, never a time-based stop.

    The private wire and liveness receipt are the live observation surface.
    Elapsed time is evidence for the Master to inspect; it never triggers an
    automatic ``turn/interrupt`` request from this runner.
    """
    terminal = asyncio.Event()
    agent_parts: list[str] = []
    completed: dict[str, Any] = {}
    counts = {"command": 0, "file_change": 0, "approval_request": 0}
    started = time.monotonic()
    thread_id = ""
    turn_id = ""
    liveness_sequence = 0

    def write_liveness(status: str) -> None:
        nonlocal liveness_sequence
        liveness_sequence += 1
        snapshot = {
            "schema_version": f"p-dag-{profile}-liveness/v2",
            "sequence": liveness_sequence,
            "status": status,
            "thread_id": thread_id,
            "turn_id": turn_id,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "observation_interval_seconds": observation_interval_seconds,
            "automatic_wall_clock_interrupt": False,
            "command": counts["command"],
            "file_change": counts["file_change"],
            "approval_request": counts["approval_request"],
        }
        private_json(
            paths["private"] / "run-liveness.json",
            snapshot,
            regression,
        )
        history_path = paths["private"] / "run-liveness.jsonl"
        with history_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(snapshot, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        history_path.chmod(0o600)

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
        raise broker.BrokerError(403, f"blind discovery controller denies {method}")

    rpc = broker.JsonRpcProcess(
        command=["codex", "app-server", "--listen", "stdio://"],
        cwd=paths["probe_workspace"],
        trace_path=paths["private"] / "wire.jsonl",
        stderr_path=paths["private"] / "stderr.log",
        notification_handler=notify,
        request_handler=deny,
    )
    try:
        await rpc.start()
        await rpc.request(
            "initialize",
            {"clientInfo": {"name": "p-dag-blind-discovery", "version": "1"},
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
        private_json(paths["private"] / "thread-start.json", thread_start, regression)
        turn_start = await rpc.request(
            "turn/start",
            {
                "threadId": thread_id,
                "model": MODEL,
                "effort": EFFORT,
                "serviceTier": TIER,
                "input": [{"type": "text", "text": prompt}],
            },
            timeout=90,
        )
        turn = turn_start.get("turn") if isinstance(turn_start.get("turn"), dict) else {}
        turn_id = str(turn.get("id") or "")
        if not turn_id:
            raise RuntimeError("turn/start returned no turn id")
        private_json(paths["private"] / "turn-start.json", turn_start, regression)
        write_liveness("RUNNING")
        while not terminal.is_set():
            try:
                await asyncio.wait_for(
                    terminal.wait(), timeout=observation_interval_seconds
                )
            except asyncio.TimeoutError:
                write_liveness("STILL_RUNNING")
        write_liveness("TERMINAL")
        text = "".join(agent_parts).strip()
        final_path = paths["private"] / "final.txt"
        final_path.write_text(text + ("\n" if text else ""), encoding="utf-8")
        final_path.chmod(0o600)
        completed_turn = completed.get("turn") if isinstance(completed.get("turn"), dict) else {}
        words = len(text.split())
        word_limit = 350 if profile == "blind-discovery" else 900
        content_ok = bool(text) and words <= word_limit
        clean = all(value == 0 for value in counts.values())
        if profile == "blind-discovery":
            required_sections = {f"D{index}": f"D{index}" in text for index in range(6)}
            candidate_count = text.count("MODEL_RECALL_SITE_CANDIDATE")
            no_candidate_count = sum(
                text.count(terminal) for terminal in BLIND_NO_CANDIDATE_TERMINALS
            )
            terminal_choice_ok = (candidate_count == 1 and no_candidate_count == 0) or (
                candidate_count == 0 and no_candidate_count == 1
            )
            # A standalone exact terminal verdict is the semantic content of D2.
            # Keep the other D-sections mandatory, but do not reject an otherwise
            # structured no-candidate trace merely because its terminal is headed
            # by the verdict instead of repeating the literal ``D2`` label.
            required_sections["D2"] = required_sections["D2"] or terminal_choice_ok
            output_schema_ok = all(required_sections.values()) and terminal_choice_ok
        elif profile == "source-match":
            required_sections = {f"E{index}": f"E{index}" in text for index in range(8)}
            candidate_count = 0
            no_candidate_count = 0
            terminal_choice_ok = True
            output_schema_ok = all(required_sections.values())
        else:
            raise RuntimeError(f"unknown Pattern-P runner profile: {profile}")
        return {
            "status": "PASS" if content_ok and clean and output_schema_ok else "FAIL_OUTPUT_OR_TOOL_CONTRACT",
            "thread_id": thread_id,
            "turn_id": turn_id,
            "profile": profile,
            "exact_start": exact_start,
            "response_nonempty": bool(text),
            "final_sha256": sha256_bytes(text.encode("utf-8")),
            "final_bytes": len(text.encode("utf-8")),
            "final_words": words,
            "word_limit": word_limit,
            "required_sections": required_sections,
            "candidate_count": candidate_count,
            "no_candidate_count": no_candidate_count,
            "output_schema_ok": output_schema_ok,
            "turn_status": completed_turn.get("status"),
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "observation_interval_seconds": observation_interval_seconds,
            "automatic_wall_clock_interrupt": False,
            **counts,
        }
    finally:
        await rpc.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method-repo", type=Path, required=True)
    parser.add_argument("--private-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--prompt-file", type=Path, required=True)
    parser.add_argument(
        "--profile",
        choices=("blind-discovery", "source-match"),
        default="blind-discovery",
        help="blind discovery omits theory source; source match permits only a frozen source card in the turn input",
    )
    parser.add_argument(
        "--observation-interval-seconds",
        type=float,
        default=60.0,
        help="write private RUNNING/STILL_RUNNING liveness every interval; never stops a turn",
    )
    args = parser.parse_args()
    if "R-035" not in args.authorization:
        raise SystemExit("--authorization must include R-035")
    method_repo = args.method_repo.resolve()
    project_root = args.project_root.resolve()
    private_root = args.private_root.resolve()
    try:
        private_root.relative_to(project_root)
    except ValueError:
        pass
    else:
        raise SystemExit(
            "--private-root must be outside --project-root so ancestor AGENTS.md "
            "cannot enter the isolated App Server preflight"
        )
    if args.observation_interval_seconds <= 0:
        raise SystemExit("--observation-interval-seconds must be positive")
    prompt = read_frozen_turn(args.prompt_file)
    if args.profile == "blind-discovery":
        if "You are a blind P-DISCOVERY mapper." not in prompt:
            raise SystemExit("--prompt-file does not contain the frozen blind discovery profile")
    elif (
        "You are a P-VALIDATION source mapper." not in prompt
        or "BEGIN FROZEN SOURCE CARD" not in prompt
    ):
        raise SystemExit("--prompt-file does not contain the frozen source-match profile")
    require_clean_method_repo(method_repo)
    sys.path.insert(0, str(method_repo / "tools"))
    import governance_regression as regression  # type: ignore
    import agent_session_broker as broker  # type: ignore

    experiment_root = private_root / "governance-regression"
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
        write_worker_workspace(paths, regression)
        input_gate = prompt_input_gate(paths, regression, project_root, prompt, args.profile)
        private_json(paths["private"] / "prompt-input-gate.json", input_gate, regression)
        if input_gate["status"] != "PASS":
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
        behavior = asyncio.run(
            run_discovery(
                paths,
                regression,
                broker,
                prompt,
                profile=args.profile,
                observation_interval_seconds=args.observation_interval_seconds,
            )
        )
        behavior_name = (
            "blind-discovery-behavior.json"
            if args.profile == "blind-discovery"
            else "source-mapping-behavior.json"
        )
        private_json(paths["private"] / behavior_name, behavior, regression)
        summary = {
            "run_id": args.run_id,
            "status": behavior["status"],
            "profile": args.profile,
            "model": MODEL,
            "effort": EFFORT,
            "permission_profile": PERMISSIONS,
            "prompt_input_gate": input_gate["status"],
            "auth_borrowed": receipt.get("auth", {}).get("shape") == "AUTH_BORROWED_LOCAL_FILE",
            "post_auth_gate": receipt.get("permission_negatives", {}).get("status"),
            "final_sha256": behavior.get("final_sha256"),
            "final_bytes": behavior.get("final_bytes"),
            "final_words": behavior.get("final_words"),
            "command_count": behavior.get("command"),
            "file_change_count": behavior.get("file_change"),
            "approval_request_count": behavior.get("approval_request"),
            "observation_interval_seconds": behavior.get("observation_interval_seconds"),
            "automatic_wall_clock_interrupt": behavior.get(
                "automatic_wall_clock_interrupt"
            ),
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
