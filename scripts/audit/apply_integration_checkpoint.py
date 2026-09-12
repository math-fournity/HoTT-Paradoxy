#!/usr/bin/env python3
"""Apply the final integration checkpoint through the canonical runtime.

The script constructs the next immutable STATE and session record in memory;
the runtime alone writes the transaction, state files, HEAD, backups and
receipt.  It is intentionally one-shot and has no external-repo side effects.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-INTEGRATION-20260912-003"


def load_runtime():
    spec = importlib.util.spec_from_file_location("handoff_cognition_runtime", RUNTIME_PATH)
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
    if state.get("revision") != 2 or state.get("latest_session") != "S-INTEGRATION-20260912-002":
        raise SystemExit("unexpected checkpoint base")
    state["revision"] = 3
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "status": "CHECKPOINTED_HANDOFF_WITH_RECONCILIATION_OPEN",
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_COMMITTED_EXPECTED",
    })
    # The runtime correctly rejected the first attempt because the
    # reconciliation record depends on a review_required ledger record.  Keep
    # that uncertainty explicit instead of claiming the chapters are ready.
    state["active"] = []
    if "A-UNDERSTANDING-RECONCILIATION-001" not in state["review_due"]:
        state["review_due"].append("A-UNDERSTANDING-RECONCILIATION-001")
    state["records"]["A-UNDERSTANDING-RECONCILIATION-001"]["status"] = "review_required"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "status": "closed",
        "scope": "Runtime-backed final integration checkpoint and durable handoff of remaining reconciliation work",
        "full_sources": [
            "理解章节/C0-当前整合审计与证据边界-20260912.md",
            "audit/ledger-summary.json",
            "audit/verification-report.json",
            "audit/external-validation-20260912.json",
            "核心认知.md",
        ],
        "depends_on": ["S-INTEGRATION-20260912-002"],
        "resolution": {
            "reason": "The accepted integration checkpoint is complete; chapter-level semantic reconciliation, source replacement coverage, and historical mathematical claim review remain explicitly open.",
            "evidence": [
                f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
                "理解章节/C0-当前整合审计与证据边界-20260912.md",
                "audit/verification-report.json",
            ],
        },
    }
    session_text = f"""# Session {SESSION_ID}\n\n- 目的：以 session 002 / STATE revision 2 为 base，通过顶层 canonical cognition runtime 完成一次真实 checkpoint。\n- 授权：用户明确授权本顶层 repo 的方案执行和 Git 固化；仅写 runtime 白名单及本 session 资产，不修改外部 repo，不恢复 aistudio-docs，不 push。\n- 输入：核心认知 generation-1、三类 AI 历史 ledger、C0 当前审计层、外部 validator 结果和本地 `.codex` 协议。\n- 预期结果：STATE revision 3、latest_session={SESSION_ID}、HEAD 更新、transaction before/after/result 留证、旧 session identity 保留。\n- 研究边界：本 session 不新增 HoTT 数学推演、Lean/Agda 内核认证或现实物理认证；它只验证跨 Session 治理持久化链。\n- 后续：新 Session 必须先全文加载 `核心认知.md`，再处理 `A-UNDERSTANDING-RECONCILIATION-001`、`A-AISTUDIO-COVERAGE-001` 和 `A-HISTORICAL-MATH-CLAIMS-001`。\n"""
    mutable = ["MEMORY.md", ".codex/research/hott/FRONTIER.md", ".codex/research/hott/LESSONS.md", ".codex/research/hott/RESUME.md"]
    files = []
    for rel in mutable:
        files.append({"path": rel, "expected_sha256": sha(ROOT / rel), "text": (ROOT / rel).read_text(encoding="utf-8")})
    new_state_text = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    files.append({"path": ".codex/research/hott/STATE.json", "expected_sha256": sha(state_path), "text": new_state_text})
    files.append({"path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md", "expected_sha256": None, "text": session_text})
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
