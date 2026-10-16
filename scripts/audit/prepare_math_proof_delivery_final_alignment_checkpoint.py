#!/usr/bin/env python3
"""Prepare revision 27 to align current memory after F-011 verification."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-027-MATH-PROOF-GATE-FINAL-ALIGNMENT"
SPEC = importlib.util.spec_from_file_location("runtime_math_proof_gate_final", RUNTIME_PATH)
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
            "本轮只把 F-011 已完成的静态验证和 project-local 3.2 candidate 身份收敛到 current MEMORY/STATE/projection revision；不改变、证明或反驳该用户原文。 | "
            f"S026/SESSION.md；audit/数学结论机器证明交付门禁实施证据-20260912.md；核心认知.md {unit['id']} | "
            "未来数学 claim 仍须单独通过 F-011。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 27/projection generation 011。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 27/projection generation 011。",
        "- update_decision: `current MEMORY 的 3.1 stale 文本改为 3.2，并记录 S026 验证；STATE/HEAD/RESUME 原子对齐。`",
        "- cross_conflicts: `NONE_AFTER_ALIGNMENT` — F-011、C4 PAPER_ONLY、formal/run/index owner 和未提交边界一致。",
        "- unresolved: `fresh model behavior、首个真实 proof package、旧数学结论重放和 Git version-close 仍开放。`",
        "", "## 汇总", "", "`NOT_TOUCHED=36`；本轮不把治理收尾冒充数学进展。", "",
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
    if state.get("revision") != 26 or state.get("latest_session") != "S-GOV-20260912-026-MATH-PROOF-DELIVERY-GATE":
        raise SystemExit("EXPECTED_REVISION_26_S026")

    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"), "source_state_revision: 26", "source_state_revision: 27")
    direction = replace_once(direction, "projection_generation: 20260912-direction-010", "projection_generation: 20260912-direction-011")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"), "source_state_revision: 26", "source_state_revision: 27")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-010", "projection_generation: 20260912-outcome-011")
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(
        memory,
        "- project-local governance 3.1 是未提交 candidate；最近已封存 tag 仍为 `governance-v3.0.0`。本轮未获 commit/tag/push 授权。",
        "- project-local governance 3.2 是未提交 candidate；最近已封存 tag 仍为 `governance-v3.0.0`。本轮未获 commit/tag/push 授权。",
    )
    gate_marker = "- F-011 proof-delivery Gate 已在根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范、formal/run/index owner 中实现；4/4 正负向 static tests PASS。它只证明治理结构，不证明未来模型行为或任何数学命题。"
    memory = replace_once(
        memory,
        gate_marker,
        gate_marker + "\n- S026 checkpoint 已把门禁写入 direction v1.4、panorama v1.4 和 STATE stable record；S027 仅完成 current version/verification alignment。",
    )
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip("\n") + "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "F-011 已成为所有未来数学结论的硬交付 Gate：",
        "S027 已完成 F-011 的 current version/verification 对齐；F-011 已成为所有未来数学结论的硬交付 Gate：",
    )
    state["revision"] = 27
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "MATH_PROOF_DELIVERY_GATE_V3_2_LOCALLY_VERIFIED_FRESH_BEHAVIOR_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
    })
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-011"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-011"
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-026-MATH-PROOF-DELIVERY-GATE", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [session_path, audit_path, runs_path, "audit/数学结论机器证明交付门禁实施证据-20260912.md", "scripts/audit/prepare_math_proof_delivery_final_alignment_checkpoint.py"],
        "source_hashes": {},
        "mathematical_status": "NO_MATHEMATICAL_CONCLUSION_GOVERNANCE_ALIGNMENT_ONLY",
        "cognition_status": "MATH_PROOF_DELIVERY_GATE_CURRENT_VERSION_AND_VERIFICATION_ALIGNED",
        "scope": "Align current MEMORY version, projection revisions and final local verification identity after F-011 implementation; no mathematical claim or proof package is produced.",
    }
    session = f"""# {SESSION_ID}

- 触发：S026 后 current MEMORY 仍写 project-local governance 3.1，而实际 LOAD_SET/Skill/PROTOCOL 已是 3.2；需按 checkpoint owner 原位收敛。
- 动作：更新 MEMORY、direction/panorama revision、STATE/HEAD/RESUME，并保存 36/36 `NOT_TOUCHED` 回评。
- 验证基础：F-011 static tests 4/4、verifier PASS；S026 three-way 27 directions/27 outcomes、fresh/projection/full regression PASS。
- 数学边界：本轮无数学结论、无 proof package；C4 仍 `PAPER_ONLY`。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "semantic_change": False,
        "alignment": ["project-local governance 3.2 candidate", "projection revision 27", "STATE/HEAD/latest session"],
        "pre_checkpoint_verification": {"proof_gate_tests": "4/4 PASS", "proof_gate_verifier": "PASS_WITH_SCOPE", "three_way": "27 directions / 27 outcomes PASS", "fresh_revision_26": "PASS_WITH_SCOPE"},
        "post_checkpoint_required": ["36/36 audit", "fresh revision 27", "projection freshness", "proof gate tests", "full regression", "git diff --check"],
        "mathematics": "NOT_APPLICABLE_GOVERNANCE_ONLY", "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume, R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "The user authorized the project-local proof-delivery governance change; this final alignment corrects stale current version text and synchronizes checkpoint-managed owners without changing scope.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 27, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
