#!/usr/bin/env python3
"""Use one follow-up runtime checkpoint to align current memory with STATE."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-INTEGRATION-20260912-004"


def load_runtime():
    spec = importlib.util.spec_from_file_location("handoff_cognition_runtime_refresh", RUNTIME_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"canonical runtime unavailable: {RUNTIME_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    runtime = load_runtime()
    base = runtime.plan(ROOT)
    state_path = ROOT / ".codex/research/hott/STATE.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("revision") != 3 or state.get("latest_session") != "S-INTEGRATION-20260912-003":
        raise SystemExit("unexpected refresh base")
    state["revision"] = 4
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "status": "CHECKPOINTED_HANDOFF_WITH_RECONCILIATION_OPEN",
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_COMMITTED",
    })
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "status": "closed",
        "scope": "Post-checkpoint current-memory alignment and final handoff receipt",
        "full_sources": [
            "MEMORY.md",
            ".codex/research/hott/STATE.json",
            ".codex/cognition/HEAD.json",
            "audit/verification-report.json",
        ],
        "depends_on": ["S-INTEGRATION-20260912-003"],
        "resolution": {
            "reason": "Current memory and resume pointers were aligned through the runtime checkpoint after the integration checkpoint itself succeeded.",
            "evidence": [
                f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
                "audit/verification-report.json",
            ],
        },
    }
    memory_path = ROOT / "MEMORY.md"
    memory = memory_path.read_text(encoding="utf-8")
    memory = memory.replace("当前交接波次由 `S-INTEGRATION-20260912-002` 封存", "当前交接波次由 `S-INTEGRATION-20260912-004` 封存")
    memory = memory.replace("- `核心认知.md` 当前 generation", "- cognition runtime 当前状态为 STATE revision 4 / latest session `S-INTEGRATION-20260912-004`；该状态只表示交接 checkpoint 已持久化，不表示数学或模型理解已认证。\n- `核心认知.md` 当前 generation")
    memory = memory.replace("逐句回连直接证据，不能把当前 C0 当作最终论文。", "逐句回连直接证据，不能把当前 C0 当作最终论文。\n4. **Checkpoint 运行事实**：session 003 的第一次尝试因依赖 review_required 被正确拒绝，第二次提交成功；session 004 用同一 runtime 对齐 MEMORY/RESUME/LESSONS，当前 transaction/lock 已清理，before/after/result receipts 保留。")
    state_text = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    frontier_path = ROOT / ".codex/research/hott/FRONTIER.md"
    lessons_path = ROOT / ".codex/research/hott/LESSONS.md"
    lessons = lessons_path.read_text(encoding="utf-8")
    if "session 003 的第一次尝试" not in lessons:
        lessons += "\n7. runtime 先拒绝依赖状态不一致，再在显式降级 review_required 后提交成功；拒绝收据和开放项都应保留。\n"
    resume_path = ROOT / ".codex/research/hott/RESUME.md"
    resume = resume_path.read_text(encoding="utf-8")
    resume = resume.replace("本 session 是 repo 初始化和交接治理工程", "当前已由 session 003/004 完成 repo 初始化、交接治理和 runtime checkpoint")
    mutable = [memory_path, frontier_path, lessons_path, resume_path]
    files = [{"path": str(path.relative_to(ROOT)), "expected_sha256": sha(path), "text": (memory if path == memory_path else lessons if path == lessons_path else resume if path == resume_path else path.read_text(encoding="utf-8"))} for path in mutable]
    files.append({"path": ".codex/research/hott/STATE.json", "expected_sha256": sha(state_path), "text": state_text})
    files.append({
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "expected_sha256": None,
        "text": f"# Session {SESSION_ID}\n\n- 目的：对齐 runtime checkpoint 后的 MEMORY、LESSONS、RESUME 与 STATE 当前叙述。\n- base：session 003 / STATE revision 3；新状态：revision 4。\n- 结果：通过 canonical cognition runtime 写入并回读；本 session 不新增数学研究。\n- 当前未决：理解章节逐句 evidence mapping、aistudio-docs replacement coverage、历史数学 claim review。\n",
    })
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly authorized top-level repo initialization, plan execution and durable checkpoint writes in this repo.",
        "files": files,
    }
    result = runtime.checkpoint(ROOT, base["snapshot"], payload, apply=True)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
