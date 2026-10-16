#!/usr/bin/env python3
"""Prepare revision 100: promote the core-essay to the fourth always-full document."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-100-FOUR-SET-UPGRADE"
PREV = "S-GOV-20260913-099-MATRIX-APPEND-ONLY-FIX"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/governance-v4.0.0-four-set-evidence-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
PREV_STATUS_SHORT = "GOVERNANCE_V3_5_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
RELEASE_REF = "governance-v4.0.0"
EXPECTED_REPINNED = {"AGENTS.md", "HoTT/CLAIM_EVIDENCE_MATRIX.md",
                     "scripts/audit/build_core_cognition_audit.py"}

SPEC = importlib.util.spec_from_file_location("runtime_s100", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:70]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000007": "第四件把‘模型不要顺着训练先验解释悖论’这一要求变成每次压缩边界都在场的连续阐释。",
        "KC-000017": "长文逐字内嵌 36 段用户原文；引入时明确其角色是 AI 阐释层，原文权威仍是 core。",
        "KC-000021": "长文中的任何数学判断都不因常驻加载而成为结论；结论仍走机器证明门禁。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮把长文提升为常驻第四件，不改 KC 原文。", "",
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
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 revision 字段（99→100）。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只同步 revision 字段（99→100）。",
        "- essay_change: YES — 加 `essay-role:v1` 角色声明与分片，并把“不改变加载配置”的旧自述原位改为 v4.0.0 常驻第四件（用户原文引文逐字未动）。",
        "- update_decision: 按用户裁定 §19（选 A）把长文提升为常驻第四件；runtime/LOAD_SET/PROTOCOL/Skill/AGENTS/合同/校验器/审计字段同步。",
        "- cross_conflicts: 长文此前自述“不改变自动加载配置”，与本次升级冲突；已原位修订该句（AI 撰写部分），未触碰 36 段用户引文。",
        "- unresolved: fresh model behavior NOT_RUN；四件套使每次启动必读体量 +约 75 KB；不 push。",
        "", "## 汇总", "", "`ALIGNED=3`；`NOT_TRACED=33`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 99 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_99_S099")

    repinned: set[str] = set()
    for record in state["records"].values():
        for rel, old_hash in list((record.get("source_hashes") or {}).items()):
            target = root / rel
            if not target.exists():
                continue
            new_hash = R.sha(target.read_bytes())
            if new_hash != old_hash:
                repinned.add(rel)
                record["source_hashes"][rel] = new_hash
                record["revalidation"] = (
                    f"{rel} re-hashed by {SESSION_ID} after the four-set upgrade "
                    "(AGENTS.md now lists the fourth document; the claim matrix was re-appended at S099 and its pins are refreshed here; the core-cognition audit builder gained the essay_change field)."
                )
    if repinned != EXPECTED_REPINNED:
        raise SystemExit(f"UNEXPECTED_REPINNED_HASHES:{sorted(repinned)}")

    projections = {}
    for key, rel, gen in (("DIRECTION", R.DIRECTION, "direction"), ("PANORAMA", R.PANORAMA, "outcome")):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(doc, "source_state_revision: 99", "source_state_revision: 100")
        projection_edit.replace_in_index(doc, f"projection_generation: 20260913-{gen}-083",
                                         f"projection_generation: 20260913-{gen}-084")
        projection_edit.replace_in_index(doc, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
        projection_edit.replace_in_index(doc, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
        projections[key] = doc
    essay = projection_edit.load(root, R.ESSAY)
    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.replace_in_shard(
        memory, "MEMORY/001 - 当前执行队列.md",
        "1. 外部 AI 工作已吸收（S098）",
        "1. 三件套已升级为**四件套**（S100，用户裁定 §19 选 A）：`从抽象到悖论——…md` 成为常驻第四件（AI 阐释层，5 片）；"
        "runtime 3.6.0 / LOAD_SET v4 / PROTOCOL v2.6 / 审计新增 `essay_change`。外部 AI 工作已吸收（S098）",
    )
    projection_edit.append_to_shard(
        memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S100 四件套升级：按用户裁定 §19 选 A，把 `从抽象到悖论——HoTT研究的核心问题意识与思想展开.md` 提升为常驻第四件——"
        "5 片（问题意识/前提与时间/芝诺圆环ASK方向/走进 HoTT 与自反/表达界限与编写说明），索引保留 `essay-role:v1` 角色声明与首屏 banner；"
        "角色是 AI 阐释层，core 仍是唯一用户原文权威。加载链：runtime 3.6.0（`FULL_SET` 四元组、schema `cognition-load-set/v4`、"
        "`always_full_documents`/`document_order`、逐 KC 审计新增 `essay_change`）+ LOAD_SET 4.0.0 + PROTOCOL v2.6 + Skill 3.6.0 + AGENTS/合同同步；"
        "`plan` 现为 41 文档 / 820,100 B；validator 9 canonical index（含长文）PASS；三方校验 28 方向 / 90 结果。"
        "启动必读体量因此增加约 75 KB（约 +10%），这是四件套的已知代价。\n",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n79. 把一份 AI 撰写的长文提升为常驻输入时，必须在加载层同时声明**角色**：`LOAD_SET.full_set_roles` + 文档内 `essay-role:v1` "
        "让“AI 阐释层”和“用户原文权威”在上下文里可区分；否则常驻加载本身会重演 rulings §9/§12 要防的‘AI 展开被当成用户原意’。"
        "另外：MUTABLE 集合新增成员后 HEAD 会 `HEAD_TRACKING_INCOMPLETE`，必须先用 canonical `initialize_cognition_head.py` 重新引导"
        "（它现在直接从 `runtime.MUTABLE` 取集合，避免漏项）。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"), "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：三件套已升级为**四件套**（新增常驻第四件 = AI 阐释层长文，5 片，含 `essay-role:v1`）；"
        f"runtime 3.6.0 / LOAD_SET v4 / PROTOCOL v2.6 / Skill 3.6.0；下次启动按 核心认知 → 方向追踪 → 全景视野 → 长文 顺序读全。"
        f"下一项回到研究第一线（E6 consumer）或用户指定课题。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户审阅长文后说“甚至我们要从三件套升级到四件套”，并在 A/B/C 中选择 **A**（授权见 `rulings.md` §19）。
- 第 1 步：长文加 `essay-role:v1` 角色声明（AI 阐释层）、原位修正“不改变加载配置”旧自述、分 5 片 + 首屏 banner。
- 第 2 步：加载链升四件套——runtime 3.6.0（`FULL_SET` 四元组 / schema v4 / `always_full_documents` / `document_order` / `essay_change`）、
  LOAD_SET 4.0.0（含 `full_set_roles`）、PROTOCOL v2.6、本地治理 Skill 3.6.0、根/`.codex` AGENTS、分片合同 §7、`feature-list` F-014。
- 校验器：`verify_fresh_three_way.py`（四件套身份/顺序/分片展开）、`verify_three_way_cognition.py`（四件套固定顺序 + 长文角色 marker）、
  `build_core_cognition_audit.py`（7 字段）同步；测试 fixture 与负向用例同步（runtime 38/38、三方 6/6）。
- 明确边界：长文是 AI 阐释层，不产出数学结论、不反向改写 core；每次启动必读体量 +约 75 KB。不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "release_ref": RELEASE_REF,
        "full_set": list(R.FULL_SET),
        "mathematics": "NO_MATHEMATICAL_CHANGE",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 100
    state["latest_session"] = SESSION_ID
    state["load_policy"].update({"runtime_version": R.VERSION, "manifest_version": "4.0.0",
                                 "full_trio": list(R.FULL_SET[:3])})
    state["load_policy"]["full_set"] = list(R.FULL_SET)
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_FOUR_SET_UPGRADE",
        "status": STATUS,
        "release_ref": RELEASE_REF,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update({"projection_generation": "20260913-direction-084"})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update({"projection_generation": "20260913-outcome-084"})
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-LOAD-GOVERNANCE-V3-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         R.ESSAY, ".codex/tools/cognition_runtime.py", ".codex/cognition/LOAD_SET.json"],
        "source_hashes": {R.ESSAY: R.sha((root / R.ESSAY).read_bytes())},
        "scope": "Four-set upgrade: the AI-exposition essay becomes the permanent fourth always-full document with an explicit role boundary; loader, config, protocol, skill, agents, contract, verifiers and audit fields updated. No mathematical change.",
    }
    texts = {
        R.DIRECTION: projections["DIRECTION"]["index_text"],
        R.PANORAMA: projections["PANORAMA"]["index_text"],
        R.ESSAY: essay["index_text"],
        "MEMORY.md": memory["index_text"],
        f"{R.PREFIX}FRONTIER.md": (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    for doc in (projections["DIRECTION"], projections["PANORAMA"], essay, memory):
        texts.update(doc["shards"])
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": ("User chose plan A of the four-set upgrade: the core-essay becomes the permanent fourth always-full document "
                          "(AI exposition layer, sharded, role-marked), with runtime/LOAD_SET/PROTOCOL/Skill/AGENTS/contract/verifier/audit-field "
                          "updates. No mathematical change; no push."),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 100,
                      "session_id": SESSION_ID, "repinned": sorted(repinned), "files": len(texts)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
