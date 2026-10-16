#!/usr/bin/env python3
"""Prepare revision 97: reader banners on the three checkpoint-managed indexes."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-097-INDEX-READER-BANNER"
PREV = "S-GOV-20260913-096-PROJECTION-SHARD-MIGRATION"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/governance-v3.4.1-reader-banner-evidence-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V3_4_1_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V3_4_1_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
PREV_STATUS_SHORT = "GOVERNANCE_V3_4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
RELEASE_REF = "governance-v3.4.1"
EXPECTED_REPINNED = {"AGENTS.md", "audit/understanding-chapter-merge-manifest.json",
                     "理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md",
                     "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md"}
OLD_NOTE = "> 逻辑文档索引。读取顺序 = 本索引 + 下表全部分片；300 行是写作软目标，不是上限。"

SPEC = importlib.util.spec_from_file_location("runtime_s097", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402  (canonical index/shard edit helper)


def banner(count: int) -> str:
    return (f"> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 {count} 个分片；缺一片即未完成，按表顺序读取；"
            "300 行只是软目标，不是上限。")


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:70]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000007": "首屏 banner + 机械检查堵住“把索引当全文”的模式匹配捷径，模型必须先声明读的是索引。",
        "KC-000017": "用户原文账本与三件套的全文加载语义不变；banner 只强化读取纪律，不改变必读内容。",
        "KC-000021": "proof Gate 与其唯一索引未被本轮改动；只更新承载路由文本的 `AGENTS.md` hash。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮为读取纪律加固，不涉及数学内容。", "",
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
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只加首屏 banner 与 revision 字段（96→97）。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 同上。",
        "- update_decision: 8 个 canonical 索引全部加首屏 banner；banner 缺失/残缺由 `verify_governance_shards.py` 判 FAIL；`理解章节/C1`–`C4` 索引变更触发 merge manifest 重建与 14 条 record 的 hash 重签。",
        "- cross_conflicts: 全局规范没有 banner 要求；这是项目在“选择性读取”默认之上的加固，属于更严格而非冲突。",
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
    if state.get("revision") != 96 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_96_S096")

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
                    f"{rel} re-hashed by {SESSION_ID} after the reader-banner hardening "
                    "(routing text / merge manifest rebuilt with unchanged comparison counts); "
                    "the record's claim and scope are unchanged."
                )
    if repinned != EXPECTED_REPINNED:
        raise SystemExit(f"UNEXPECTED_REPINNED_HASHES:{sorted(repinned)}")

    memory = {"index_path": "MEMORY.md",
              "index_text": replace_once((root / "MEMORY.md").read_text(encoding="utf-8"), OLD_NOTE, banner(3)),
              "shards": {row["path"]: (root / row["path"]).read_text(encoding="utf-8")
                         for row in R.parse_shard_index((root / "MEMORY.md").read_bytes(), "MEMORY.md")["shards"]}}
    projections = {}
    for key, rel, count in (("DIRECTION", R.DIRECTION, 5), ("PANORAMA", R.PANORAMA, 8)):
        doc = projection_edit.load(root, rel)
        headline = "# 方向追踪" if key == "DIRECTION" else "# 全景视野"
        projection_edit.replace_in_index(doc, f"-->\n\n{headline}\n", f"-->\n\n{banner(count)}\n\n{headline}\n")
        projection_edit.replace_in_index(doc, "source_state_revision: 96", "source_state_revision: 97")
        projection_edit.replace_in_index(
            doc, f"projection_generation: 20260913-{'direction' if key == 'DIRECTION' else 'outcome'}-080",
            f"projection_generation: 20260913-{'direction' if key == 'DIRECTION' else 'outcome'}-081")
        projection_edit.replace_in_index(doc, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
        projection_edit.replace_in_index(doc, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
        projections[key] = doc

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n76. 分片把“读到索引”变成了“以为读到全文”的捷径，所以索引需要**首屏可见 banner**（而不是只在规范里写规则），"
        "并且 banner 必须被机械检查（`verify_governance_shards.py` → `MISSING_READER_BANNER`/`INCOMPLETE_READER_BANNER` 直接 FAIL）。"
        "另一条经验：`理解章节/C1`–`C4` 的索引文件被 merge manifest 逐文件 pin，任何索引文本改动（哪怕只加一行 banner）"
        "都必须重建 manifest 并在同一 checkpoint 重签 14 条 record。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"), "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：8 个 canonical 索引全部带首屏 banner（索引 ≠ 全文；全文 = 索引 + 全部分片），"
        f"并由 `verify_governance_shards.py` 机械检查；三件套加载与全文语义不变。下一项回到研究第一线（E6 consumer）或用户指定课题。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户说“开始加固”，授权沿用 `rulings.md` §17/§18 的边界（本地、不 push、只改治理载体）。
- 动作：8 个 canonical 索引加首屏 banner（`> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 N 个分片；缺一片即未完成…`）；
  其中 `README.md`/`理解章节/C1`–`C4` 为非 MUTABLE，直接提交；`MEMORY.md`/`方向追踪.md`/`全景视野.md` 经本 checkpoint 写入。
- 强制：`scripts/audit/logical_document.banner_issues` + `verify_governance_shards.py`（缺失/残缺即 FAIL，退出码 1）；
  单测 `test_shard_index_banners.py` 5/5。
- 连带：`理解章节/C1`–`C4` 索引变更 → merge manifest 重建（计数不变：35/24/15/9）+ 14 条 record 重签；
  `AGENTS.md` 路由文本新增 banner 一行 → 1 条 record 重签。
- 不改任何 KC、数学判词、proof source/run/index；三件套全文语义不变。不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "release_ref": RELEASE_REF,
        "banner_prefix": "> ⚠️ 逻辑文档索引：",
        "banner_check": "scripts/audit/verify_governance_shards.py",
        "mathematics": "NO_NEW_OR_CHANGED_MATHEMATICAL_CLAIM",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 97
    state["latest_session"] = SESSION_ID
    state["load_policy"].update({"manifest_version": "3.4.1"})
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_READER_BANNER",
        "status": STATUS,
        "release_ref": RELEASE_REF,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-081", "semantic_status": STATUS})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-081", "semantic_status": STATUS})
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         "scripts/audit/logical_document.py", "scripts/audit/verify_governance_shards.py",
                         "scripts/audit/test_shard_index_banners.py"],
        "source_hashes": {},
        "scope": "Reader-banner hardening of all canonical shard indexes plus mechanical enforcement; no mathematical or research change.",
    }
    texts = {
        "MEMORY.md": memory["index_text"],
        R.DIRECTION: projections["DIRECTION"]["index_text"],
        R.PANORAMA: projections["PANORAMA"]["index_text"],
        f"{R.PREFIX}FRONTIER.md": (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    texts.update(memory["shards"])
    texts.update(projections["DIRECTION"]["shards"])
    texts.update(projections["PANORAMA"]["shards"])
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": (
            "User said 开始加固 for the offered reader-banner hardening: a first-screen banner on every canonical "
            "index, mechanically enforced for all eight indexes, with the manifest rebuild and record re-signing that "
            "the C1-C4 index edits require. Local only; no push; no mathematical change."
        ),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 97,
                      "session_id": SESSION_ID, "repinned": sorted(repinned), "files": len(texts)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
