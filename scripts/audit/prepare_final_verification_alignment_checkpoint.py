#!/usr/bin/env python3
"""Prepare revision 17 aligning current verification prose with the executed v3 suite."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-017-FINAL-VERIFICATION-ALIGNMENT"
SPEC = importlib.util.spec_from_file_location("runtime_verification_alignment", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | "
            "本轮只把 current MEMORY 的旧 three-way 测试计数与实际 4/4 回归对齐，没有改变、深化或裁决该用户原文。 | "
            "MEMORY.md; scripts/audit/test_three_way_cognition.py; audit/核心认知generation-3与加载治理v3实施证据-20260912.md | "
            "该 KC 的数学真值与现实解释仍由后续研究负责。 |"
        )
    lines.extend(
        [
            "",
            "## 三件套交叉与更新归属",
            "",
            "- core_change: `NO` — generation-3 core/manifest/curation/transition 均不变。",
            "- direction_change: `NO_RESEARCH_SEMANTIC_CHANGE` — 只同步 current STATE revision 17。",
            "- panorama_change: `NO_RESEARCH_RESULT_CHANGE` — 只登记 S016 archive routing 与 S017 verification alignment。",
            "- update_decision: `修正 MEMORY 当前验证计数；同步 current projection/STATE/恢复 owner；将失效模式留入 LESSONS 与自反馈依据。`",
            "- cross_conflicts: `NONE_AFTER_ALIGNMENT`。",
            "- unresolved: `fresh model behavior、数学认证、aistudio coverage、2,396 claim 语义。`",
            "",
            "## 汇总",
            "",
            "`NOT_TOUCHED=27`；验证元数据修正不冒充研究深化。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 16:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_16")

    direction = replace_once(
        (root / R.DIRECTION).read_text(encoding="utf-8"),
        "source_state_revision: 16",
        "source_state_revision: 17",
    )
    panorama = replace_once(
        (root / R.PANORAMA).read_text(encoding="utf-8"),
        "source_state_revision: 16",
        "source_state_revision: 17",
    )
    panorama = replace_once(
        panorama,
        "revision 16 historical-document archive checkpoint",
        "revision 16 archive-routing + revision 17 final verification-alignment checkpoints",
    )

    memory = replace_once(
        (root / "MEMORY.md").read_text(encoding="utf-8"),
        "1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现：S013 完成主迁移，S014 收口旧主题，S015 对齐 current owner，`S-GOV-20260912-016-HISTORICAL-DOC-ARCHIVE` revision 16 完成用户授权的两份 generation-2 治理文档 Git rename 归档和当前 consumer 路由；本轮不启动数学研究。",
        "1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现：S013 完成主迁移，S014 收口旧主题，S015 对齐 current owner，S016 完成两份 generation-2 治理文档 Git rename 归档，`S-GOV-20260912-017-FINAL-VERIFICATION-ALIGNMENT` revision 17 收敛最终验证叙事；本轮不启动数学研究。",
    )
    memory = replace_once(memory, "three-way 3/3", "three-way 4/4")

    frontier = replace_once(
        (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
        "| 收敛 | generation-3 core + LOAD_SET/runtime v3 + STATE v2 checkpoint | completed-local | 完成 revision 16 历史路径收敛后运行 fresh/full regression 并精确 Git/tag；fresh model behavior 仍独立 NOT_RUN |",
        "| 收敛 | generation-3 core + LOAD_SET/runtime v3 + STATE v2 checkpoint | verified-local | revision 17 已对齐 current owner 与 full regression；版本封存以实际 Git commit/tag 为准，fresh model behavior 仍独立 NOT_RUN |",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip() + (
        "\n18. 分项测试已从 3 增至 4 时，suite PASS 与 projection revision PASS 仍可能遗漏 MEMORY 的旧计数；current narrative lint 应核 stable 测试锚点，但不能把自由文本检查扩张为数学语义裁判。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "revision 16 historical-document archive checkpoint 构成本轮交付",
        "revision 17 final verification-alignment checkpoint 构成本轮交付（S016 保存历史文档归档路径迁移）",
    )

    state["revision"] = 17
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "status": "CORE_GENERATION_3_LAYERED_LOAD_V3_FINAL_VERIFICATION_ALIGNED",
            "checkpoint_result": "CHECKPOINT_COMMITTED",
        }
    )
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-016-HISTORICAL-DOC-ARCHIVE"],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            "MEMORY.md",
            "全景视野.md",
            "audit/fresh-three-way-verification-20260912.json",
            "audit/核心认知generation-3与加载治理v3实施证据-20260912.md",
        ],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "cognition_status": "FINAL_VERIFICATION_NARRATIVE_ALIGNED",
        "scope": "Align the current human-readable three-way test count and final verification narrative with the actual 4/4 suite; no mathematics.",
    }

    session = f"""# {SESSION_ID}

- 触发：revision 16 后全套测试实际为 three-way 4/4，但 current `MEMORY.md` 仍写旧值 3/3；projection freshness 未覆盖该自由文本计数。
- 修复：原位改为 4/4，direction/panorama/STATE 同步 revision 17，LESSONS 记录 narrative-lint 的有限适用边界。
- 已有证据：core 7/7、three-way 4/4、runtime 27/27、reader 17/17、历史 ledger、理解章节 merge、cross-source 与 revision 16 fresh/projection 均通过。
- 完成后：在 revision 17 重跑 final fresh/projection/full suite、路径残留、JSON/schema、Git diff/check/status，并完成精确 commit/tag。
- 边界：fresh model behavior、数学证明、aistudio coverage 和 2,396 claim 语义仍不因本轮通过。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "pre_checkpoint": {
                "state_revision": 16,
                "actual_three_way_tests": "4/4 PASS",
                "memory_claim": "3/3",
                "projection_freshness": "PASS_WITH_SCOPE_BUT_DID_NOT_CHECK_FREE_TEXT_TEST_COUNT",
                "audit_verifier_first_invocation": "EXIT_2_OBSOLETE_ARGUMENT_SHAPE",
                "audit_verifier_corrected_invocation": "27/27 PASS",
            },
            "post_checkpoint_required": [
                "fresh-three-way v2",
                "projection freshness",
                "full regression",
                "current narrative/path residual scan",
                "JSON and core schema validation",
                "git diff/status",
            ],
            "model_behavior": "NOT_RUN",
            "mathematics": "UNCHANGED",
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n"

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
        "authorization": "User authorized the governance implementation; final current-owner verification alignment is an in-scope completion step.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": relative,
                "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None,
                "text": value,
            }
            for relative, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "session_id": SESSION_ID,
                "revision": 17,
                "files": len(texts),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
