#!/usr/bin/env python3
"""Prepare revision 96: shard 方向追踪.md (5) and 全景视野.md (8) into v2 indexes."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-096-PROJECTION-SHARD-MIGRATION"
PREV = "S-GOV-20260913-095-DOC-SHARD-MIGRATION"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/governance-v3.4.0-projection-shard-evidence-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V3_4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V3_4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
PREV_STATUS_SHORT = "GOVERNANCE_V3_3_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
RELEASE_REF = "governance-v3.4.0"
EXPECTED_REPINNED = {"AGENTS.md"}
DIRECTION_QUEUE_OLD = (
    "1. project-local governance 3.3.0 长治理文档分片已闭合（S094 能力/合同 + S095 迁移："
    "`README.md`、`MEMORY.md`、`理解章节/C1`–`C4`）；回滚边界 `governance-v3.2.0-pre-sharding`，不 push。"
)

SPEC = importlib.util.spec_from_file_location("runtime_s096", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
sys_path_added = str(SCRIPTS)
import sys
if sys_path_added not in sys.path:
    sys.path.insert(0, sys_path_added)
import projection_edit  # noqa: E402  (canonical index/shard edit helper)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:70]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000007": "三件套分片后仍强制“索引 + 全部分片”，并以 0/0 空壳 PASS 断言堵住只读索引的退化路径。",
        "KC-000017": "用户原文账本加载语义不变；分片只改载体分片与写入局部性，不减少每次 Session 的必读内容。",
        "KC-000021": "proof Gate 的唯一索引 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 继续单文件；本轮不改任何数学结论。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮为三件套分片迁移，不涉及数学内容。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned:
            relation = "ALIGNED"; assessment = aligned[kid]
        else:
            relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容；投影行文本逐字保留。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{EVIDENCE}`；{kid} | 数学开放项不变。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文；`核心认知.md` 未改动且保持单文件。",
        "- direction_change: STRUCTURE_ONLY — `方向追踪.md` 迁为 5 片；28 条 `DIR-*` 行文本不变，仅 revision/状态字段与载体分片变化。",
        "- panorama_change: STRUCTURE_ONLY — `全景视野.md` 迁为 8 片；89 条 `OUT-*` 行文本不变。",
        "- update_decision: 按用户裁定 §18 执行第二波；索引保留身份字段，行分片重复表头（唯一允许重复），`verify_three_way_cognition.py` 改为逻辑文本解析并新增 0/0 fail-closed。",
        "- cross_conflicts: 全局规范的默认读法是“按任务读 owner shard”，与本项目“三件套必须全文”冲突；以项目不变量 + runtime 全片覆盖为准，并在合同 §7 明写。",
        "- unresolved: fresh model behavior NOT_RUN；共享主库 3.16.0 仍未发布；不 push。",
        "", "## 汇总", "", "`ALIGNED=3`；`NOT_TOUCHED=33`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def store(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 95 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_95_S095")

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
                    f"{rel} re-hashed by {SESSION_ID} after the wave-2 governance edit "
                    "(three-way projections sharded + routing text updated); the record's claim and scope are unchanged."
                )
    if repinned != EXPECTED_REPINNED:
        raise SystemExit(f"UNEXPECTED_REPINNED_HASHES:{sorted(repinned)}")

    evidence_dir = root / SESSION_REL / "evidence"
    projections = {}
    for key, rel in (("DIRECTION", R.DIRECTION), ("PANORAMA", R.PANORAMA)):
        bundle = json.loads((evidence_dir / f"bundles/{key}.json").read_text(encoding="utf-8"))
        doc = {"index_path": rel, "index_text": bundle["index_text"],
               "shards": {row["path"]: row["text"] for row in bundle["shards"]}}
        projection_edit.replace_in_index(doc, "source_state_revision: 95", "source_state_revision: 96")
        projection_edit.replace_in_index(
            doc, f"projection_generation: 20260913-{'direction' if key == 'DIRECTION' else 'outcome'}-079",
            f"projection_generation: 20260913-{'direction' if key == 'DIRECTION' else 'outcome'}-080")
        projection_edit.replace_in_index(doc, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
        projection_edit.replace_in_index(doc, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
        projections[key] = doc

    memory = {"index_path": "MEMORY.md", "index_text": store(root, "MEMORY.md"),
              "shards": {row["path"]: store(root, row["path"]) for row in
                         R.parse_shard_index((root / "MEMORY.md").read_bytes(), "MEMORY.md")["shards"]}}
    projection_edit.replace_in_shard(
        memory, "MEMORY/001 - 当前执行队列.md", DIRECTION_QUEUE_OLD,
        "1. project-local governance 3.4.0：三件套分片完成（S096 迁移 `方向追踪.md` 5 片 / `全景视野.md` 8 片，行级对账、"
        "表头是唯一重复），`verify_three_way_cognition.py` 改为逻辑文本解析并拒绝 0/0 空壳 PASS；"
        "前一波 v3.3.0 已迁移 `README.md`/`MEMORY.md`/`理解章节/C1`–`C4`。回滚边界 `governance-v3.2.0-pre-sharding`、`governance-v3.3.0`，不 push.",
    )
    projection_edit.append_to_shard(
        memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S096 三件套分片（第二波）：`方向追踪.md` → 5 片（28 条 `DIR-*` 行）、`全景视野.md` → 8 片（89 条 `OUT-*` 行）；"
        "索引保留 marker/`source_state_revision`/`projection_generation`/`semantic_status`；行分片自带表头且逐行对账"
        "（每行恰好一次 + 表头重复数 = 行分片数 − 1）；`verify_three_way_cognition.py` 按逻辑文本解析并新增 "
        "`DIRECTION_ROWS_EMPTY`/`OUTCOME_ROWS_EMPTY`/`PROJECTION_SHARD_UNREADABLE`；新工具 `migrate_projection_shards.py`、"
        "`projection_edit.py`；38/38 runtime 单测 + 6/6 三方单测。\n",
    )

    lessons = store(root, f"{R.PREFIX}LESSONS.md")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n75. 大表分片必须保留**表头**（否则 Markdown 渲染失效），因此对账规则要从“整文拼接逐字节相同”升级为"
        "“每行恰好消费一次 + 唯一允许的额外行 = 表头行 × (行分片数 − 1)”；投影的身份字段（marker 块、"
        "`source_state_revision`/`projection_generation`/`semantic_status`）必须留在索引，因为 runtime 与 freshness "
        "校验直读该物理路径。只按“文件级 hash”迁移会破坏这两点。\n"
    )
    resume = store(root, f"{R.PREFIX}RESUME.md")
    resume = replace_once(
        resume, "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：三件套分片完成——`方向追踪.md`（5 片）与 `全景视野.md`（8 片）已是 v2 索引 + 行分片，"
        f"`核心认知.md` 保持单文件；全文加载语义不变（索引 + 全部分片）。三方校验改为逻辑文本解析并拒绝 0/0 空壳 PASS；"
        f"下一项回到研究第一线（E6 consumer）或用户指定课题。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户审查分片现状后说“开始第二波”，授权见 `rulings.md` §18（合同 §7 要求的三件套迁移必须由用户明确发起）。
- 迁移：`方向追踪.md` → 5 片（28 条方向行按家族分配）；`全景视野.md` → 8 片（89 条结果行按家族分配，含 1 行跨块归位）。
- 关键规则：原文头部（marker/`source_state_revision`/`projection_generation`/`semantic_status`）留在索引；行分片自带表头两行，
  对账证明“每行恰好一次、表头重复数 = 行分片数 − 1”；工具 `migrate_projection_shards.py`，编辑 helper `projection_edit.py`。
- 消费端强化：`verify_three_way_cognition.py` 按逻辑文本解析 `DIR-*`/`OUT-*` 并新增 0/0 与缺片 fail-closed；`test_three_way_cognition.py` 新增分片用例。
- 不改任何 KC、数学判词、proof source/run/index；`HoTT/CLAIM_EVIDENCE_MATRIX.md` 保持单文件。
- 本地 annotated `{RELEASE_REF}` 指向本 checkpoint 后的 commit；不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "release_ref": RELEASE_REF,
        "migrated_logical_documents": ["DIRECTION", "PANORAMA"],
        "shard_count": {"DIRECTION": 5, "PANORAMA": 8},
        "row_count": {"DIRECTION": 28, "PANORAMA": 89},
        "mathematics": "NO_NEW_OR_CHANGED_MATHEMATICAL_CLAIM",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 96
    state["latest_session"] = SESSION_ID
    state["load_policy"].update({"runtime_version": R.VERSION, "manifest_version": "3.4.0"})
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PROJECTION_SHARD_MIGRATION",
        "status": STATUS,
        "release_ref": RELEASE_REF,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-080", "semantic_status": STATUS})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-080", "semantic_status": STATUS})
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         "scripts/audit/migrate_projection_shards.py", "scripts/audit/projection_edit.py",
                         "scripts/audit/verify_three_way_cognition.py",
                         f"{SESSION_REL}/evidence/shard-reports/PANORAMA.json",
                         f"{SESSION_REL}/evidence/shard-reports/DIRECTION.json"],
        "source_hashes": {},
        "scope": "Wave-2 shard migration of the two three-way projections into v2 indexes with line-exact reconciliation; no mathematical or research change.",
    }
    texts = {
        R.DIRECTION: projections["DIRECTION"]["index_text"],
        R.PANORAMA: projections["PANORAMA"]["index_text"],
        "MEMORY.md": memory["index_text"],
        f"{R.PREFIX}FRONTIER.md": store(root, f"{R.PREFIX}FRONTIER.md"),
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    texts.update(projections["DIRECTION"]["shards"])
    texts.update(projections["PANORAMA"]["shards"])
    texts.update(memory["shards"])
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": (
            "User said 开始第二波 and rulings.md §18 authorizes sharding 方向追踪.md and 全景视野.md while keeping the "
            "full-load invariant (index plus every shard), preserving identity fields in the index, and hardening the "
            "three-way verifier. No push; no mathematical change."
        ),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 96,
                      "session_id": SESSION_ID, "repinned": sorted(repinned),
                      "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
