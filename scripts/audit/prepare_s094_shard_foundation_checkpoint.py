#!/usr/bin/env python3
"""Prepare revision 94: project-local governance 3.3.0 shard foundation (no document migration)."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-094-SHARD-FOUNDATION"
PREV = "S-GOV-20260913-093-RELEASE-STATE-ALIGNMENT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/governance-v3.3.0-shard-foundation-evidence-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V3_3_SHARD_FOUNDATION_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V3_3_SHARD_FOUNDATION_DOWNSTREAM_E6_CONSUMER_FIRST"
PREV_STATUS_SHORT = "GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPINNED = {"AGENTS.md"}

SPEC = importlib.util.spec_from_file_location("runtime_s094", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:80]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000007": "分片索引 + 全分片强制覆盖，防止未来 AI 用模式匹配和部分读取替代用户原文与历史证据。",
        "KC-000017": "本轮服务于“用户认知工程必须先于既有训练先验被完整加载”这一条：索引只路由，正文按序全读，且写入必须落到 owner/append 分片。",
        "KC-000021": "不改机器证明门禁本身；只更新其所在 `AGENTS.md` 的 hash 与 revalidation，未把治理结构变化冒充数学结论。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮为纯治理/加载结构改造，不涉及数学内容。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned:
            relation = "ALIGNED"; assessment = aligned[kid]
        else:
            relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{EVIDENCE}`；{kid} | 数学开放项不变。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文、无用户工作意识修正。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 `source_state_revision` 与 projection generation。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只同步 `source_state_revision` 与 projection generation。",
        "- update_decision: 新增 F-013、rulings §17、分片合同与 runtime 3.3.0 逻辑文档加载能力；不迁移任何既有文档，三件套与 proof matrix 明确保留。",
        "- cross_conflicts: 共享主库仍是旧 v1/200 行版本且 3.16.0 未打 tag；本项目按用户裁定 pin 候选副本并登记再同步触发条件。",
        "- unresolved: fresh model behavior NOT_RUN；文档迁移（CP-2）尚未执行；不 push。",
        "", "## 汇总", "", "`ALIGNED=3`；`NOT_TOUCHED=33`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 93 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_93_S093")

    repinned = []
    for key, record in state["records"].items():
        for rel, old_hash in list((record.get("source_hashes") or {}).items()):
            path = root / rel
            if not path.exists():
                continue
            new_hash = R.sha(path.read_bytes())
            if new_hash != old_hash:
                repinned.append((key, rel))
                record["source_hashes"][rel] = new_hash
                record["revalidation"] = (
                    f"{rel} re-hashed by {SESSION_ID} after the shard-foundation governance edit; "
                    "content change is the added 「长治理文档分片与索引」 routing section, not a change of the "
                    "record's claim or scope."
                )
    if {rel for _, rel in repinned} != EXPECTED_REPINNED:
        raise SystemExit(f"UNEXPECTED_REPINNED_HASHES:{sorted({rel for _, rel in repinned})}")

    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 93", "source_state_revision: 94")
    direction = replace_once(direction, "projection_generation: 20260913-direction-077", "projection_generation: 20260913-direction-078")
    direction = replace_once(direction, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
    direction = replace_once(direction, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 93", "source_state_revision: 94")
    panorama = replace_once(panorama, "projection_generation: 20260913-outcome-077", "projection_generation: 20260913-outcome-078")
    panorama = replace_once(panorama, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
    panorama = replace_once(panorama, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n73. 长治理文档分片必须先有“逻辑文档”加载语义再迁移正文：只把 canonical 路径换成索引、"
        "而加载器不展开分片，会让未来 Session 静默丢掉正文。正确顺序是 runtime/合同/校验入口先行（CP-1），"
        "文档迁移后行（CP-2）。300 行只是软目标，不能当拆分依据。\n"
    )
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：project-local governance 3.3.0 的分片基础已建立（runtime 3.3.0 逻辑文档加载、"
        f"分片合同、pin 的 v2 校验器、AGENTS/PROTOCOL/LOAD_SET/Skill 路由）；本轮不迁移任何既有文档，"
        f"三件套与 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 保留。文档迁移（CP-2）与 `governance-v3.3.0` tag 待下一步。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户要求：全局治理框架更新"长治理文档软分片与索引"后，本项目完成拆解改造且不影响未来工作；已确认边界见 `rulings.md` §17。
- 本轮动作（CP-1）：只建能力与合同，不迁移既有正文。runtime 3.3.0 解析 `governance-shard-index:v2`，把逻辑文档展开为
  "索引 + 按 table 顺序全部分片"，`check` 必须覆盖每一片，结构错误 fail closed；`MUTABLE` 文档分片进入 `HEAD.json.tracked`。
- 新增：`docs/quality/长治理文档分片与索引合同.md`、pin 的 v2 校验器副本与包装器、一次性迁移工具、5 条 runtime 负向测试。
- 保留：三件套、`HoTT/CLAIM_EVIDENCE_MATRIX.md`（行级 proof 收据耦合）、`AGENTS.md`、来源快照与历史交付分卷；触发条件写入合同 §7。
- 不改任何 KC、mathematical status、proof source/run/index；`AGENTS.md` 的 hash 仅因新增路由章节而 re-pin（带 revalidation）。
- 迁移（CP-2，revision 95）与本地 annotated `governance-v3.3.0` 待执行；不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "pinned_validator_source_commit": "2e4e4d2dbe13046470bc79e98e64735312ee9bd5",
        "mathematics": "NO_NEW_OR_CHANGED_MATHEMATICAL_CLAIM",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 94
    state["latest_session"] = SESSION_ID
    state["load_policy"].update({"runtime_version": R.VERSION, "manifest_version": R.VERSION})
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_SHARD_FOUNDATION",
        "status": STATUS,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-078", "semantic_status": STATUS})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-078", "semantic_status": STATUS})
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-GOVERNANCE-V3-2-RELEASE-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         "scripts/audit/verify_governance_shards.py", ".codex/tools/cognition_runtime.py",
                         "docs/quality/长治理文档分片与索引合同.md"],
        "source_hashes": {},
        "scope": "Project-local shard foundation only: logical-document loading, contract and validation entry points; no document migration and no mathematical change.",
    }
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": (
            "User authorized implementing the approved sharding plan: in-flight work was committed first, a boundary tag was "
            "created, and this checkpoint applies the project-local shard foundation (runtime 3.3.0 plus contract and routing). "
            "No document migration, no push, no mathematical change."
        ),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 94,
                      "session_id": SESSION_ID, "repinned": sorted({rel for _, rel in repinned})},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
