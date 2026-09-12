#!/usr/bin/env python3
"""Persist the cross-source provenance-label correction through the runtime."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "S-GOV-20260912-012-PROVENANCE-LABEL-FIX"


def runtime_module(root: Path):
    spec = importlib.util.spec_from_file_location("cognition_runtime", root / ".codex/tools/cognition_runtime.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def replace_once(text: str, old: str, new: str) -> str:
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)


def replace_line_start(text: str, prefix: str, new: str) -> str:
    lines = text.splitlines()
    indexes = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(indexes) == 1, (prefix, indexes)
    lines[indexes[0]] = new
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    rt = runtime_module(root)
    base = rt.plan(root)
    assert base["revision"] == 11, base["revision"]
    state = json.loads((root / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))
    state["revision"] = 12
    state["latest_session"] = SESSION_ID
    state["execution_control"] = {
        "background_work": False,
        "checkpoint_result": "CHECKPOINT_COMMITTED",
        "last_checkpoint_session": SESSION_ID,
        "new_math_research_started": False,
        "next_minimal_verification": "direct sentence review of 2396 understanding claims; aistudio coverage; historical mathematics review",
        "source_policy": "preserve historical snapshots; do not restore user-removed aistudio-docs",
        "status": "PROVENANCE_LABELS_CORRECTED_WITH_SCOPED_SEMANTIC_REVIEW",
    }
    state["projection"]["status"] = "PROVENANCE_LABELS_CORRECTED_WITH_SCOPED_SEMANTIC_REVIEW"
    state["records"]["A-PROVENANCE-LABEL-FIX-001"] = {
        "kind": "provenance_label_correction",
        "path": "audit/cross-source-reconciliation-report.md",
        "status": "closed",
        "scope": "Correct source-class wording so the 384 response rows are represented as the three-platform AI response ledger; count and row coverage remain unchanged.",
        "full_sources": ["audit/cross-source-reconciliation-report.md", "audit/cross-source-reconciliation.json", "scripts/audit/verify_cross_source_reconciliation.py"],
        "resolution": {
            "reason": "The register builder and verifier now use ai_response; the generated register reports LocalGPT 305 + WebGPT 55 + Gemini 24 and passes row/hash validation.",
            "evidence": ["audit/cross-source-reconciliation-report.md", "audit/cross-source-reconciliation.json", "scripts/audit/verify_cross_source_reconciliation.py"],
        },
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "status": "review_required",
        "scope": "Correct cross-source response provenance labels, revalidate register and persist the correction through the cognition checkpoint; no new mathematics.",
        "cognition_status": "PROVENANCE_LABELS_CORRECTED_WITH_SCOPED_SEMANTIC_REVIEW",
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "depends_on": ["S-GOV-20260912-011-FRESH-THREE-WAY"],
        "full_sources": [
            f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
            f".codex/research/hott/sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md",
            f".codex/research/hott/sessions/{SESSION_ID}/RUNS.json",
            "audit/cross-source-reconciliation-report.md",
            "scripts/audit/verify_cross_source_reconciliation.py",
        ],
    }

    direction = (root / "方向追踪.md").read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 11", "source_state_revision: 12")
    direction = replace_once(direction, "LocalGPT response 384", "AI response ledger 384（LocalGPT 305 + WebGPT 55 + Gemini 24）")
    panorama = (root / "全景视野.md").read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 11", "source_state_revision: 12")
    panorama = replace_once(panorama, "LocalGPT 384 条 visible response", "AI response ledger 384 条（LocalGPT 305 + WebGPT 55 + Gemini 24）")
    panorama = replace_line_start(
        panorama,
        "| `OUT-TOP-THREE-WAY-SKELETON`",
        "| `OUT-TOP-THREE-WAY-SKELETON` | 本轮三件套文档、LOAD_SET/runtime/validator 接入、generation-2、merge receipt、source register 和 fresh receipt | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-E-WEB-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION` | 当前顶层本轮升级 | `VERIFIED_WITH_SCOPE` | 三件套固定入口、22,226 行来源登记、25/24 文件处置、fresh load/负向收据和 revision 11 checkpoint 已验证 | 仍不证明 2,396 条 claim 的人工语义、数学认证或模型理解 | `方向追踪.md`；`全景视野.md`；`audit/cross-source-reconciliation.json`；`audit/fresh-three-way-verification-20260912.json`；`.codex/` |",
    )
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(memory, "当前治理 checkpoint 将由 `S-GOV-20260912-011-FRESH-THREE-WAY` 封存；STATE revision=11。", "当前治理 checkpoint 将由 `S-GOV-20260912-012-PROVENANCE-LABEL-FIX` 封存；STATE revision=12。")
    memory = replace_once(memory, "LocalGPT response 384", "AI response ledger 384（LocalGPT 305 + WebGPT 55 + Gemini 24）")
    memory = replace_once(memory, "运行 `verify_core_cognition.py`、`verify_three_way_cognition.py`、`verify_understanding_merge.py` 和 `verify_cross_source_reconciliation.py`；随后做 source/hash freshness 与缺件/错序/孤儿的负向演练。数学研究保持暂停", "运行 `verify_core_cognition.py`、`verify_three_way_cognition.py`、`verify_understanding_merge.py`、`verify_cross_source_reconciliation.py` 和 `verify_projection_freshness.py`；随后按需回源 2,396 条 claim。数学研究保持暂停")
    memory += "\n- provenance label correction：384 条 AI response ledger 已明确为 LocalGPT 305 + WebGPT 55 + Gemini 24；总 register 分母保持 22,226，标签修正不改变覆盖范围。\n"
    frontier = (root / ".codex/research/hott/FRONTIER.md").read_text(encoding="utf-8")
    frontier = frontier.replace("fresh EOF/hash receipt", "fresh EOF/hash receipt + provenance-label correction", 1)
    resume = (root / ".codex/research/hott/RESUME.md").read_text(encoding="utf-8")
    resume = resume.replace("运行 `rtk python3 scripts/audit/verify_three_way_cognition.py`，再用 `cognition_runtime.py plan/read/check` 记录三件套真实 EOF/hash 收据。", "运行 `rtk python3 scripts/audit/verify_three_way_cognition.py` 和 `rtk python3 scripts/audit/verify_projection_freshness.py`，再用 `cognition_runtime.py plan/read/check` 记录三件套真实 EOF/hash 收据。", 1)
    resume = resume.replace("来源覆盖登记、逐文件 merge receipt、core generation-2 和 fresh three-way EOF/hash rehearsal 已完成并 checkpoint", "来源覆盖登记、逐文件 merge receipt、core generation-2、fresh three-way EOF/hash rehearsal 和 provenance label correction 已完成并 checkpoint", 1)
    lessons = (root / ".codex/research/hott/LESSONS.md").read_text(encoding="utf-8")
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SESSION_ID,
        "runs": [
            {"command": "rtk python3 scripts/audit/verify_cross_source_reconciliation.py", "status": "PASS", "scope": "384 AI response rows are explicitly three-platform aggregate; total 22,226"},
            {"command": "rtk python3 scripts/audit/verify_projection_freshness.py", "status": "PASS_WITH_SCOPE", "scope": "post-correction state/projection/source/fresh consistency"},
            {"command": "rtk python3 scripts/audit/verify_three_way_cognition.py", "status": "PASS", "scope": "state revision 12; 24 directions; 22 outcomes"},
            {"command": "rtk git diff --check", "status": "PASS", "scope": "current patch whitespace"},
        ],
        "model_context": "NOT_CERTIFIED_BY_TOOL",
        "mathematics": "NOT_CERTIFIED",
    }
    session = """# Cross-source provenance label correction Session

- session_id: `S-GOV-20260912-012-PROVENANCE-LABEL-FIX`
- scope: 修正 384 条 AI response ledger 的来源类别措辞，重新生成/验证跨源 register，并持久化 revision 12 checkpoint
- authorization: 用户已要求完整审计和执行方案；不修改外部源、不恢复 `aistudio-docs`、不删除 nested 历史源
- mathematical_status: `UNCHANGED_FROM_R039_HISTORICAL_SCOPE`
- cognition_status: `PROVENANCE_LABELS_CORRECTED_WITH_SCOPED_SEMANTIC_REVIEW`

## 三方判定

- `core_change`: `NONE`；用户原文和 generation-2 不变。
- `direction_change`: `NONE_SEMANTIC_CHANGE`；只同步 source-class 事实标签和 STATE revision。
- `panorama_change`: `CORRECT_STATUS_LABEL`；总分母和结果内容不变。
- `update_decision`: `TECHNICAL_OWNER`；错误属于 provenance 表述，更新 register/report/STATE，不改 core。
- `cross_conflicts`: `MODEL_CONTEXT_NOT_CERTIFIED`、`WEBGPT_REVISION_40_41`、`LOCALGPT_DIRTY_VS_SNAPSHOT`。
- `unresolved`: `A-AISTUDIO-COVERAGE-001`、`A-HISTORY-LEDGERS-001`、`A-UNDERSTANDING-RECONCILIATION-001`、`A-HISTORICAL-MATH-CLAIMS-001`。

## 结果边界

修正后 384 条 response 明确为 LocalGPT 305 + WebGPT 55 + Gemini 24；这只是来源类别纠正，不是将 384 条都归给 LocalGPT。register 总数仍为 22,226，数学认证和模型理解均未由本 Session 提供。
"""
    files = [
        ("MEMORY.md", memory),
        ("方向追踪.md", direction),
        ("全景视野.md", panorama),
        (".codex/research/hott/FRONTIER.md", frontier),
        (".codex/research/hott/LESSONS.md", lessons),
        (".codex/research/hott/RESUME.md", resume),
        (".codex/research/hott/STATE.json", json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"),
        (f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md", session),
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
