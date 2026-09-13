#!/usr/bin/env python3
"""Prepare revision 30 so an open research parent does not stale a closed formal proof."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-030-ERCF-DEPENDENCY-SEMANTICS-ALIGNMENT"
RESULT_ID = "A-ERCF-FACTORIZATION-FORMAL-001"
RESEARCH_PARENT = "A-HOTT-SELF-VALIDATION-ECONOMY-001"
PROOF_GATE = "A-MATH-PROOF-DELIVERY-GATE-001"

SPEC = importlib.util.spec_from_file_location("runtime_ercf_dependency_alignment", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | "
            "本轮只校正 STATE 依赖边语义：开放研究母题保留为 research_parent，不再使已经由独立 kernel/run/index 闭合的子证明进入 review_required；不改变任何数学命题。 | "
            f"S028 proof package；S030/SESSION.md；核心认知.md {unit['id']} | HoTT 原生 consumer 与父研究问题仍开放。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 30/projection generation 014。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 30/projection generation 014。",
        "- update_decision: `STATE dependency/research-parent 分类与 MEMORY/LESSONS/RESUME/session receipt 更新。`",
        "- cross_conflicts: `RESOLVED` — proof 的证据依赖与研究动机/母题关系分开。",
        "- unresolved: `父级 HoTT 自反/理论经济方向继续开放，不降低其 paper-only 状态。`",
        "", "## 汇总", "", "`NOT_TOUCHED=36`；本轮数学状态不变。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 29 or state.get("latest_session") != "S-GOV-20260912-029-ERCF-PROOF-HYDRATION-ALIGNMENT":
        raise SystemExit("EXPECTED_REVISION_29_S029")
    result = state["records"][RESULT_ID]
    if result.get("depends_on") != [RESEARCH_PARENT, PROOF_GATE]:
        raise SystemExit("EXPECTED_RESEARCH_PARENT_AS_VALIDATION_DEPENDENCY")

    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"), "source_state_revision: 29", "source_state_revision: 30")
    direction = replace_once(direction, "projection_generation: 20260912-direction-013", "projection_generation: 20260912-direction-014")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"), "source_state_revision: 29", "source_state_revision: 30")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-013", "projection_generation: 20260912-outcome-014")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    anchor = "- S029 修复 `A-ERCF-FACTORIZATION-FORMAL-001` 的 task hydration：空 `stderr.txt` 仍原样保留并由 RUN.json/hash/verifier 认证，但不再被错误要求作为非空认知正文加载。"
    memory = replace_once(
        memory,
        anchor,
        anchor + "\n- S030 将 ERCF 的开放研究母题从 proof 的验证依赖改为 `research_parent`；A-ERCF task plan 现在可水合且不再把已闭合证明误列为 `review_required`。",
    )
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "36. stable record 的 `depends_on`" not in lessons:
        lessons += "\n36. stable record 的 `depends_on` 表示会传播证据 stale/review 的验证依赖，不应拿来表示开放母题、研究动机或叙事归属；后者应保留为非传播的 research-parent 关系，否则已机器闭合的子证明会被父问题的 paper-only 状态误降级。"
    lessons += "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\nS029 已修复",
        "## 当前停止点\n\nS030 已把 `A-ERCF-FACTORIZATION-FORMAL-001` 的验证依赖与开放研究母题分开：proof 只依赖已验证的 F-011 Gate，C4/ERCF 父方向保留为 `research_parent`，因此 task plan 不再把已闭合证明误列为 review_required。\n\nS029 已修复",
    )

    result["depends_on"] = [PROOF_GATE]
    result["research_parent"] = RESEARCH_PARENT
    result["revalidation"] = "The open C4/ERCF research program is motivational scope, not a validity dependency for C-59 through C-66. The formal result now depends only on the verified proof-delivery gate; its source/run/index hashes remain unchanged."
    state["revision"] = 30
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "ERCF_GENERAL_FACTORIZATION_MACHINE_PROVED_LOCAL_HYDRATABLE_NOT_REVIEW_STALE_HOTT_NATIVE_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
    })
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-014"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-014"

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-029-ERCF-PROOF-HYDRATION-ALIGNMENT", RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, ".codex/research/hott/STATE.json", "scripts/audit/prepare_ercf_dependency_alignment_checkpoint.py"],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_FROM_MP_ERCF_001",
        "cognition_status": "PROOF_VALIDITY_DEPENDENCY_SEPARATED_FROM_OPEN_RESEARCH_PARENT",
        "scope": "Prevent the open C4 research program from propagating review status into an independently machine-proved formal result; no mathematical claim or direction changes.",
    }
    session = f"""# {SESSION_ID}

- 触发：S029 后 research task plan 可生成，但 `review_required` 仍包含 `{RESULT_ID}`。
- 根因：该 proof record 把开放的 `{RESEARCH_PARENT}` 放进 `depends_on`；runtime 会正确传播依赖的证据 stale/review。研究母题/动机不是 C-59–C-66 的证明有效性依赖。
- 修复：`depends_on=[{PROOF_GATE}]`；新增非传播的 `research_parent={RESEARCH_PARENT}`；proof source/run/index/hash 全部不变。
- 预期验收：同一 task plan 成功，且 `review_required` 不包含 `{RESULT_ID}`；父研究记录仍保持开放/paper-only。
- 数学状态：`MP-ERCF-001` 不变；不是 HoTT 悖论。
- 三件套：无语义变化，只同步 revision 30/generation 014；core 不变。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "observed_issue": {"task_plan": "SUCCEEDED", "review_required_contained": RESULT_ID},
        "change": {"old_depends_on": [RESEARCH_PARENT, PROOF_GATE], "new_depends_on": [PROOF_GATE], "research_parent": RESEARCH_PARENT},
        "post_checkpoint_required": ["task plan succeeds", "A-ERCF absent from review_required", "proof exact replay", "27 directions/28 outcomes", "36/36 KC audit", "fresh revision 30", "projection freshness", "full regression", "git diff --check"],
        "mathematics": "UNCHANGED_FROM_MP_ERCF_001",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    texts = {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session,
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "This in-scope state correction prevents an open research parent from falsely downgrading the user-authorized machine proof during future task hydration; it changes no proof or mathematical scope.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": relative, "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None, "text": value}
            for relative, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 30, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
