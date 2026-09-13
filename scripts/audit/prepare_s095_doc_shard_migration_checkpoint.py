#!/usr/bin/env python3
"""Prepare revision 95: migrate README/MEMORY/理解章节 C1-C4 into v2 shard indexes."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-095-DOC-SHARD-MIGRATION"
PREV = "S-GOV-20260913-094-SHARD-FOUNDATION"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/governance-v3.3.0-doc-shard-migration-evidence-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V3_3_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V3_3_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
PREV_STATUS_SHORT = "GOVERNANCE_V3_3_SHARD_FOUNDATION_DOWNSTREAM_E6_CONSUMER_FIRST"
RELEASE_REF = "governance-v3.3.0"
RELEASE_PARENT = "293d368"
EXPECTED_REPINNED = {
    "audit/understanding-chapter-merge-manifest.json",
    "理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md",
    "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md",
}
BUNDLE = ROOT / f"{SESSION_REL}/evidence/memory-shard-bundle.json"

SPEC = importlib.util.spec_from_file_location("runtime_s095", RUNTIME_PATH)
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
        "KC-000007": "逻辑文档 = 索引 + 全部 shard，加载器强制全片覆盖，防止未来 AI 用模式匹配与部分读取替代原正文。",
        "KC-000017": "保存用户原文的载体（理解章节、MEMORY、README）已按自然语义边界分片，但读取仍是完整按序加载，不因分片降低用户认知输入。",
        "KC-000021": "proof Gate 的唯一索引 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 明确保留单文件；本轮不改任何数学结论或证明证据。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮为文档结构迁移，不涉及数学内容。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned:
            relation = "ALIGNED"; assessment = aligned[kid]
        else:
            relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容；正文逐字保留，仅改变载体分片。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{EVIDENCE}`；{kid} | 数学开放项不变。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文；`核心认知.md` 未改动（未分片，hash 不变）。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 `source_state_revision` 与 projection generation。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只同步 `source_state_revision` 与 projection generation。",
        "- update_decision: `README.md`、`MEMORY.md`、`理解章节/C1`–`C4` 迁为 v2 索引 + 分片；正文逐字保留；三件套与 proof matrix 保持单文件。",
        "- cross_conflicts: 初始迁移把分片目录写到了仓库根（路径按仓库根而非索引同级解析）；已移走错误产物、从 boundary tag 精确还原五个文件后按修正工具重做，并在 LESSONS 登记该失败。",
        "- unresolved: fresh model behavior NOT_RUN；共享主库 3.16.0 仍未发布；不 push。",
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
    if state.get("revision") != 94 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_94_S094")

    repinned: set[str] = set()
    for key, record in state["records"].items():
        for rel, old_hash in list((record.get("source_hashes") or {}).items()):
            path = root / rel
            if not path.exists():
                continue
            new_hash = R.sha(path.read_bytes())
            if new_hash != old_hash:
                repinned.add(rel)
                record["source_hashes"][rel] = new_hash
                record["revalidation"] = (
                    f"{rel} re-hashed by {SESSION_ID}: the file is now a v2 shard index (or a manifest that compares "
                    "logical text). Content is byte-identical to the pre-migration file when shards are concatenated "
                    "in index order; the record's claim and scope are unchanged."
                )
    if repinned != EXPECTED_REPINNED:
        raise SystemExit(f"UNEXPECTED_REPINNED_HASHES:{sorted(repinned)}")

    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 94", "source_state_revision: 95")
    direction = replace_once(direction, "projection_generation: 20260913-direction-078", "projection_generation: 20260913-direction-079")
    direction = replace_once(direction, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
    direction = replace_once(direction, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 94", "source_state_revision: 95")
    panorama = replace_once(panorama, "projection_generation: 20260913-outcome-078", "projection_generation: 20260913-outcome-079")
    panorama = replace_once(panorama, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
    panorama = replace_once(panorama, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n74. 分片索引里的 shard 路径是**相对索引所在目录**解析的（规范与 validator 都如此）。工具与加载器必须"
        "归一化为仓库相对路径；只按仓库根解析时，根目录文档（README/MEMORY）会通过、子目录文档（理解章节/C*）"
        "会静默失败。首次迁移就撞上了这个坑：错误产物已移出仓库，受影响文件从 boundary tag 精确还原后重做。\n"
    )
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：project-local governance 3.3.0 的长治理文档分片迁移完成——`README.md`、"
        f"`MEMORY.md`、`理解章节/C1`–`C4` 已是 v2 索引 + 有序分片（正文逐字保留、逻辑文本与 boundary tag 逐字节相同）；"
        f"三件套与 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 保持单文件。下一项回到研究第一线（E6 consumer）或用户指定课题。\n\n",
    )

    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    memory_index = bundle["index_text"].replace(
        "> 合同：`docs/quality/长治理文档分片与索引合同.md`。\n",
        "> 合同：`docs/quality/长治理文档分片与索引合同.md`。\n"
        "> 写入规则：当前队列/证据上限/恢复入口在原位片修改；新的逐会话记录追加到 `MEMORY/003 - 当前验证状态与顺序日志.md` 末尾。\n",
    )
    shards = {row["path"]: row["text"] for row in bundle["shards"]}
    queue_path = "MEMORY/001 - 当前执行队列.md"
    log_path = "MEMORY/003 - 当前验证状态与顺序日志.md"
    queue = shards[queue_path]
    queue = replace_once(
        queue,
        "1. S090 当前治理修复：保留 S086–S089 `CHECKPOINT_RECEIPT_MISSING` 历史事实，runtime 3.2 强制 SESSION/RUNS/36-KC audit 同事务并以 canonical result 为应用收据；修正五个 stable record 的水合关系和目录 scope。",
        "1. project-local governance 3.3.0 长治理文档分片已闭合（S094 能力/合同 + S095 迁移：`README.md`、`MEMORY.md`、`理解章节/C1`–`C4`）；回滚边界 `governance-v3.2.0-pre-sharding`，不 push。",
    )
    queue = replace_once(
        queue,
        "7. 版本闭合：接手现场 `35cace7`、proof/治理修复资产 `d3dfb0e…`、current metadata S092 与本地 annotated `governance-v3.2.0` 形成可恢复链；未 push。",
        "7. 版本闭合：接手现场 `35cace7`、proof/治理修复资产 `d3dfb0e…`、S092 release parent `667c7e8`、分片基础 `293d368` 与本地 annotated `governance-v3.3.0` 形成可恢复链；未 push。",
    )
    shards[queue_path] = queue
    log = shards[log_path]
    if not log.endswith("\n"):
        log += "\n"
    log += (
        f"\n- S095 文档分片迁移：`README.md`、`MEMORY.md`、`理解章节/C1`–`C4` 迁为 v2 索引 + 有序分片；"
        f"逻辑文本按索引顺序拼接与 boundary tag `governance-v3.2.0-pre-sharding` 逐字节相同；validator PASS（indexes=6、notices=0）；"
        f"runtime 3.3.0 对逻辑文档强制全片覆盖；proof matrix 与三件套保持单文件。\n"
    )
    log += (
        f"- S094 分片基础：runtime 3.3.0 逻辑文档展开（索引 + 全部分片、fail closed、`HEAD` 分片跟踪）、"
        f"`docs/quality/长治理文档分片与索引合同.md`、pin 的 v2 校验器与包装器、5 条 runtime 负向测试；"
        f"迁移前在途成果由 commit `4022206` 收口并打 boundary tag。\n"
    )
    shards[log_path] = log

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户要求见 `rulings.md` §17；CP-1（S094）已建立逻辑文档加载能力与合同，本轮执行实际迁移。
- 迁移对象与布局：`README.md`→4 片（topical）；`MEMORY.md`→3 片（sequential，append_target=`MEMORY/003`）；
  `理解章节/C1`→4、`C2`→6、`C3`→5、`C4`→6 片（topical，按原 H2 语义簇）。
- 对账：每个逻辑文档按索引顺序拼接 shard 正文后与 boundary tag 内容逐字节相同；`MEMORY` 因顺序日志需作为末片而重排片序，
  采用逐行多重集 + 每片逐字切片对账（工具报告 `content_preserved_multiset=true`）。
- 失败与修正：首轮迁移把分片目录写到仓库根（shard 路径应相对索引目录解析）；错误产物已移出仓库、五个文件从
  boundary tag 精确还原后重做。该失败写入 `LESSONS.md` 第 74 条与迁移证据。
- consumer 同步：`build_history_ledgers`（claim 枚举按逻辑文本）、`build_understanding_merge_manifest`/`verify_understanding_merge`
  （逻辑文本对账 + 逻辑 hash 校验）、STATE 中 3 类 source hash re-pin（merge manifest、C3、C4）。
- 不改任何 KC、mathematical status、proof source/run/index；`HoTT/CLAIM_EVIDENCE_MATRIX.md` 明确保留单文件。
- 本地 annotated `{RELEASE_REF}` 指向本 checkpoint 后的 commit；不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "release_ref": RELEASE_REF,
        "migrated_logical_documents": ["README", "MEMORY", "UNDERSTANDING-C1", "UNDERSTANDING-C2",
                                       "UNDERSTANDING-C3", "UNDERSTANDING-C4"],
        "shard_count": 28,
        "mathematics": "NO_NEW_OR_CHANGED_MATHEMATICAL_CLAIM",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 95
    state["latest_session"] = SESSION_ID
    state["load_policy"].update({"runtime_version": R.VERSION, "manifest_version": R.VERSION})
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_DOC_SHARD_MIGRATION",
        "status": STATUS,
        "release_ref": RELEASE_REF,
        "release_parent_commit": RELEASE_PARENT,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-079", "semantic_status": STATUS})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-079", "semantic_status": STATUS})
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-LOAD-GOVERNANCE-V3-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         "docs/quality/长治理文档分片与索引合同.md",
                         "scripts/audit/shard_migrate_document.py",
                         f"{SESSION_REL}/evidence/shard-reports/README.json",
                         f"{SESSION_REL}/evidence/shard-reports/MEMORY.json"],
        "source_hashes": {},
        "scope": "Document-shard migration of README/MEMORY/理解章节 C1-C4 into v2 indexes with byte-identical logical content; no mathematical or research change.",
    }
    texts = {
        "MEMORY.md": memory_index, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    texts.update(shards)
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": (
            "User authorized implementing the approved sharding plan (rulings.md §17): phase CP-2 migrates the six "
            "non-trio logical documents into v2 shard indexes, re-pins the affected STATE source hashes with "
            "revalidation, and keeps every KC, mathematical status and proof asset unchanged. No push."
        ),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 95,
                      "session_id": SESSION_ID, "repinned": sorted(repinned),
                      "memory_shards": sorted(shards)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
