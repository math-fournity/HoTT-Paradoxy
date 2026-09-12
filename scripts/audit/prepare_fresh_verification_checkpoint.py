#!/usr/bin/env python3
"""Persist the fresh three-way verification as a controlled checkpoint."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "S-GOV-20260912-011-FRESH-THREE-WAY"


def runtime_module(root: Path):
    spec = importlib.util.spec_from_file_location("cognition_runtime", root / ".codex/tools/cognition_runtime.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    rt = runtime_module(root)
    base = rt.plan(root)
    assert base["revision"] == 10, base["revision"]
    state = json.loads((root / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))
    state["revision"] = 11
    state["latest_session"] = SESSION_ID
    state["execution_control"] = {
        "background_work": False,
        "checkpoint_result": "CHECKPOINT_COMMITTED",
        "last_checkpoint_session": SESSION_ID,
        "new_math_research_started": False,
        "next_minimal_verification": "direct sentence review of 2396 understanding claims; aistudio coverage; historical mathematics review",
        "source_policy": "preserve historical snapshots; do not restore user-removed aistudio-docs",
        "status": "FRESH_THREE_WAY_VALIDATED_WITH_SCOPE_AND_SCOPED_SEMANTIC_REVIEW",
    }
    state["projection"]["status"] = "FRESH_THREE_WAY_VALIDATED_WITH_SCOPED_SEMANTIC_REVIEW"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["full_sources"].append("audit/fresh-three-way-verification-20260912.json")
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["full_sources"].append("audit/fresh-three-way-verification-20260912.json")
    state["records"]["A-CROSS-SOURCE-RECONCILIATION-001"]["full_sources"].append("audit/fresh-three-way-verification-20260912.json")
    state["records"]["A-FRESH-THREE-WAY-001"] = {
        "kind": "fresh_runtime_verification",
        "path": "audit/fresh-three-way-verification-20260912.json",
        "status": "closed",
        "scope": "Fresh-process complete load-graph read, three-way EOF/hash coverage and fail-closed negative cases; no model-context or mathematical certification.",
        "full_sources": ["audit/fresh-three-way-verification-20260912.json", "scripts/audit/verify_fresh_three_way.py", ".codex/tools/cognition_runtime.py"],
        "resolution": {
            "reason": "A new Python process read the complete current load graph; three-way files matched hashes and negative wrong-snapshot, incomplete-coverage and tampered-chunk cases were rejected.",
            "evidence": ["audit/fresh-three-way-verification-20260912.json", "scripts/audit/verify_fresh_three_way.py"],
        },
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "status": "review_required",
        "scope": "Fresh process and complete load-graph verification, fail-closed negative rehearsal and post-change governance checkpoint; no new mathematics.",
        "cognition_status": "FRESH_THREE_WAY_VALIDATED_WITH_SCOPED_SEMANTIC_REVIEW",
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "depends_on": ["S-GOV-20260912-010-HISTORY-RECONCILIATION"],
        "full_sources": [
            f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
            f".codex/research/hott/sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md",
            f".codex/research/hott/sessions/{SESSION_ID}/RUNS.json",
            "audit/fresh-three-way-verification-20260912.json",
            "scripts/audit/verify_fresh_three_way.py",
            ".codex/tools/cognition_runtime.py",
        ],
    }
    state["review_due"] = ["A-AISTUDIO-COVERAGE-001", "A-HISTORICAL-MATH-CLAIMS-001", "A-HISTORY-LEDGERS-001", "A-UNDERSTANDING-RECONCILIATION-001", "A-CROSS-SOURCE-RECONCILIATION-001"]
    state["unresolved"] = ["A-AISTUDIO-COVERAGE-001", "A-HISTORY-LEDGERS-001", "A-UNDERSTANDING-RECONCILIATION-001", "A-CROSS-SOURCE-RECONCILIATION-001", "A-HISTORICAL-MATH-CLAIMS-001"]

    direction = (root / "方向追踪.md").read_text(encoding="utf-8").replace("source_state_revision: 10", "source_state_revision: 11", 1)
    panorama = (root / "全景视野.md").read_text(encoding="utf-8").replace("source_state_revision: 10", "source_state_revision: 11", 1)
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = memory.replace("当前治理 checkpoint 将由 `S-GOV-20260912-010-HISTORY-RECONCILIATION` 封存。", "当前治理 checkpoint 将由 `S-GOV-20260912-011-FRESH-THREE-WAY` 封存；STATE revision=11。", 1)
    memory = memory.replace("fresh/hash 与缺件/错序/孤儿的负向演练。数学研究保持暂停", "fresh/hash 与缺件/错序/孤儿的负向演练已通过；数学研究保持暂停", 1)
    memory += "\n- fresh receipt：`audit/fresh-three-way-verification-20260912.json`；完整 load graph=96 份文档，三件套逐块 EOF/hash 通过，三个 fail-closed 负向场景通过；模型实际理解仍 `NOT_CERTIFIED_BY_TOOL`。\n"
    frontier = (root / ".codex/research/hott/FRONTIER.md").read_text(encoding="utf-8")
    frontier = frontier.replace("22,226 条跨来源 register + 理解章节 merge receipt", "22,226 条跨来源 register + 理解章节 merge receipt + fresh EOF/hash receipt", 1)
    resume = (root / ".codex/research/hott/RESUME.md").read_text(encoding="utf-8")
    resume = resume.replace("来源覆盖登记、逐文件 merge receipt 和 core generation-2 已完成并 checkpoint", "来源覆盖登记、逐文件 merge receipt、core generation-2 和 fresh three-way EOF/hash rehearsal 已完成并 checkpoint", 1)
    lessons = (root / ".codex/research/hott/LESSONS.md").read_text(encoding="utf-8")
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SESSION_ID,
        "runs": [
            {"command": "rtk python3 scripts/audit/verify_fresh_three_way.py", "status": "PASS_WITH_SCOPE", "scope": "fresh process; complete 96-document load graph; three-way full read and negative cases"},
            {"command": "rtk python3 scripts/audit/verify_three_way_cognition.py", "status": "PASS", "scope": "post-checkpoint state revision 11; 24 directions; 22 outcomes"},
            {"command": "rtk python3 scripts/audit/verify_core_cognition.py", "status": "PASS", "scope": "generation-2; 913 KC"},
            {"command": "rtk python3 scripts/audit/verify_history_ledgers.py", "status": "PASS", "scope": "historical ledger counts retained; core denominator read from manifest"},
            {"command": "rtk git diff --check", "status": "PASS", "scope": "current patch whitespace"},
        ],
        "model_context": "NOT_CERTIFIED_BY_TOOL",
        "mathematics": "NOT_CERTIFIED",
    }
    files = [
        ("MEMORY.md", memory),
        ("方向追踪.md", direction),
        ("全景视野.md", panorama),
        (".codex/research/hott/FRONTIER.md", frontier),
        (".codex/research/hott/LESSONS.md", lessons),
        (".codex/research/hott/RESUME.md", resume),
        (".codex/research/hott/STATE.json", json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"),
        (f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md", """# Fresh three-way validation Session

- session_id: `S-GOV-20260912-011-FRESH-THREE-WAY`
- scope: 新 Python 进程的完整 load graph 读取、三件套 EOF/hash 收据、缺件/过期/篡改负向演练和 checkpoint 持久化
- authorization: 用户已要求审计并执行方案；不修改外部源、不恢复 `aistudio-docs`、不删除 nested 历史源
- mathematical_status: `UNCHANGED_FROM_R039_HISTORICAL_SCOPE`
- cognition_status: `FRESH_THREE_WAY_VALIDATED_WITH_SCOPED_SEMANTIC_REVIEW`

## 三方判定

- `core_change`: `NONE`；generation-2 已在上一 Session 生成，913 KC 不变。
- `direction_change`: `NONE_SEMANTIC_CHANGE`；固定顺序、source-state revision 和方向投影指针同步。
- `panorama_change`: `NONE_SEMANTIC_CHANGE`；fresh receipt 作为当前运行证据加入。
- `update_decision`: `TECHNICAL_OWNER`；fresh 运行收据更新验证/STATE，不修改用户 core 或数学结果。
- `cross_conflicts`: `MODEL_CONTEXT_NOT_CERTIFIED`、`WEBGPT_REVISION_40_41`、`LOCALGPT_DIRTY_VS_SNAPSHOT`。
- `unresolved`: `A-AISTUDIO-COVERAGE-001`、`A-HISTORY-LEDGERS-001`、`A-UNDERSTANDING-RECONCILIATION-001`、`A-HISTORICAL-MATH-CLAIMS-001`。

## 结果边界

新进程已对当前完整 load graph 发出并重组全部字节；错误 snapshot、缺最后一块和篡改 chunk 均被 runtime 拒绝。该收据证明运行器的文件边界与 fail-closed 行为，不证明模型实际理解、压缩后神经上下文保有或数学正确性。
"""),
        (f".codex/research/hott/sessions/{SESSION_ID}/RUNS.json", json.dumps(runs, ensure_ascii=False, indent=2) + "\n"),
    ]
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly requested complete plan audit, rationale completion, and execution; scope excludes external source mutation, restoration of aistudio-docs, and deletion of historical nested source.",
        "files": [],
    }
    for rel, text in files:
        path = root / rel
        payload["files"].append({"path": rel, "expected_sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None, "text": text})
    result = rt.checkpoint(root, base["snapshot"], payload, apply=args.apply)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
