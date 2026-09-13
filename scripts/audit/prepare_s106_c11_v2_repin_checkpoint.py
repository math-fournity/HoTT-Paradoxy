#!/usr/bin/env python3
"""Prepare revision 106: re-pin C11 v2, the retrodiction checker and the rebuilt merge manifest.

Corrective checkpoint after S105 (same pattern as S099 after S098): rewriting C11 into
v2 changed three classes of pinned hashes that the S105 transaction could not know
about — C11 itself, the retrodiction checker (row-label contract updated), and the
merge manifest (rebuilt because C11's hash is recorded inside it, which re-pins the
14 records that reference the manifest).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-106-C11-V2-REPIN"
PREV = "S-GOV-20260913-105-C11-REVIEW-ABSORPTION"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
CHECKER = "scripts/audit/verify_ledger_retrodiction.py"
CHECK_RECEIPT = "audit/ledger-retrodiction-check-20260913.json"
MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_NON_MANIFEST = {C11, CHECKER}

SPEC = importlib.util.spec_from_file_location("runtime_s106", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:60]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是 C11 v2 的哈希再绑定（corrective checkpoint），不产生数学结论。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in ("KC-000005", "KC-000021", "KC-000030"):
            relation = "ALIGNED"
            assessment = "本轮只修正登记哈希与行标签契约，不改任何语义判断。"
        else:
            relation = "NOT_TOUCHED"
            assessment = f"本轮没有研究或重新裁决「{label}」的数学/哲学内容。"
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{C11}`；{kid} | 数学开放项不变。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO_CHANGE(reason) — 语义未变，只重绑哈希；记忆与接续文件记录本次修正。",
        "- panorama_change: NO_CHANGE(reason) — S105 的结果行仍然准确。",
        "- essay_change: NO_CHANGE(reason) — 常驻第四件未改动。",
        f"- update_decision: 重新绑定 C11 v2（`{C11}`）、校验脚本（`{CHECKER}`）与重建后的 merge manifest；14 条 pin 了 manifest 的 record 一并重新哈希。",
        "- cross_conflicts: 无新冲突；本轮的冲突是 S105 事务无法预知的哈希漂移（同类于 S099 对 S098 的修正）。",
        "- unresolved: 无新未知；数学与候选状态一律不变。",
        "",
        "## 汇总",
        "",
        "`ALIGNED=3`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 105 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_105_S105")

    repinned: dict[str, list[str]] = {}
    for record_id, record in state["records"].items():
        hashes = record.get("source_hashes") or {}
        if not hashes:
            continue
        changed = []
        for path, old_hash in list(hashes.items()):
            target = root / path
            if not target.is_file():
                continue
            new_hash = R.sha(target.read_bytes())
            if new_hash == old_hash:
                continue
            hashes[path] = new_hash
            changed.append(path)
        if changed:
            record["source_hashes"] = hashes
            record["revalidation"] = (
                f"{', '.join(changed)} re-hashed by {SESSION_ID}: C11 was rewritten to v2 (ua row restored, "
                "row-id contract aligned, compensation-action trichotomy), so its own hash, the retrodiction "
                "checker's row-label contract and the rebuilt merge manifest needed re-pinning. Claim, scope and "
                "evidence status are unchanged."
            )
            repinned[record_id] = changed
    touched_paths = {p for paths in repinned.values() for p in paths}
    if not EXPECTED_NON_MANIFEST <= touched_paths:
        raise SystemExit(f"EXPECTED_C11_AND_CHECKER_REPIN:{sorted(touched_paths)}")
    manifest_records = sorted(r for r, paths in repinned.items() if MANIFEST in paths)
    if len(manifest_records) != 14:
        raise SystemExit(f"EXPECTED_14_MANIFEST_REPIN:{len(manifest_records)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "089"),
        ("PANORAMA", R.PANORAMA, "outcome", "089"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 105", "source_state_revision: 106"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-090",
        )
        projections[key] = doc

    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S106 C11 v2 哈希再绑定（corrective checkpoint，同类于 S099 对 S098 的修正）：v2 重写时**补回被误删的 "
        "univalence/SIP 行（#2b）**，并把 `verify_ledger_retrodiction.py` 的行标签契约从 v1 的“#N”标签改为 v2 表的行号"
        "（1/2/2b/3/4/5/6a/6b/7/8/9），重建 merge manifest；重新绑定 16 条 record（C11 本体 1 条、校验脚本 1 条、"
        "pin 了 manifest 的 14 条）。五个 verifier 全 PASS；数学判词、候选状态与研究队列**不变**。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row54 = (
        "| 已闭合工作包 54 | C11 独立评审吸收与 v2 修订（S105） | `ABSORPTION_AND_INDEPENDENT_VERIFICATION`"
        "（5 主条 + 5 细节全部 ACCEPTED，一条附范围限定） | C11 v1→v2：接上 Theory Schema/C6、不变量降为非判据、"
        "六字段账本、补偿动作三分、四坐标分离、2×2 降为检查坐标、补时间结构与 B 方向、回溯结论降级；v1 由 Git 保存；见 "
        "`audit/c11评审吸收与独立核验-20260913.md` |"
    )
    frontier = replace_once(
        frontier,
        row54,
        row54 + "\n| 已闭合工作包 55 | C11 v2 哈希再绑定（S106，corrective） | "
        "`HASH_REPIN_ONLY` | 补回 v2 误删的 univalence/SIP 行（#2b）；校验脚本行标签对齐 v2 行号；重建 merge manifest；"
        "重新绑定 16 条 record（C11 / 校验脚本 / 14 条 manifest pin）；五个 verifier 全 PASS；数学与队列不变 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n85. 文档“原位重写”会连带改动三类哈希：文档自身的 record pin、依赖它做机械检查的脚本契约、以及记录该文档"
        "哈希的派生 manifest（后者会级联重绑所有 pin 了 manifest 的 record）。重写后必须**先跑全部 verifier**再提交，"
        "本轮就是靠 verifier 才发现 v2 误删了 univalence 行、且校验脚本仍在用 v1 的行标签。修正走一个新的 corrective "
        "checkpoint（同类 S099→S098），不篡改已应用的事务。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S106（corrective）：C11 v2 的哈希再绑定完成——补回 v2 误删的 univalence/SIP 行（#2b）、校验脚本行标签对齐 v2、"
        "重建 merge manifest、重新绑定 16 条 record；五个 verifier 全 PASS。数学判词、候选状态与研究队列不变。"
        "下一步仍是登记中的两条并行线：自主构造（须过退化测试）与 triage 批次 1（146 取 20）。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 触发：S105 应用后跑 verifier，发现 C11 v2 的两处副作用——(a) 重写时误删了 v1 的 univalence/SIP 行；
  (b) `verify_ledger_retrodiction.py` 仍用 v1 的“#N”行标签。/ 另外 C11 哈希写入 merge manifest，重建后级联影响 14 条 record。
- 处置：补回 `#2b univalence（ua）/SIP` 行；校验脚本改为按 v2 表行号（1/2/2b/3/4/5/6a/6b/7/8/9）匹配；
  重建 `{MANIFEST}`；本 checkpoint 重新绑定 16 条 record；五个 verifier 全部 PASS。
- 边界：语义零改动（数学判词、候选状态、研究队列不变）；不新增数学 claim；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "kind": "corrective_repin",
            "repinned_records": len(repinned),
            "repinned_paths": sorted(touched_paths),
            "manifest_records": len(manifest_records),
            "verifiers": ["verify_governance_shards", "verify_three_way_cognition",
                          "verify_understanding_merge", "verify_fresh_three_way",
                          "verify_ledger_retrodiction"],
            "mathematics": "NOT_CERTIFIED",
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 106
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_C11_V2_REPIN",
            "status": STATUS,
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-090", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-090", "semantic_status": STATUS}
    )
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, "A-THEORY-ECONOMY-LEDGER-001", "A-LEDGER-RETRODICTION-CHECK-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, C11, CHECK_RECEIPT],
        "source_hashes": {},
        "scope": (
            "Corrective hash re-pin after the C11 v2 rewrite: restored the univalence/SIP ledger row, aligned the "
            "retrodiction checker's row-id contract with the v2 table, rebuilt the merge manifest, and re-pinned 16 "
            "records (C11, checker, 14 manifest-pinned). No semantic change."
        ),
    }

    texts: dict[str, str] = {}
    for doc in (projections["DIRECTION"], projections["PANORAMA"], memory, essay):
        texts[doc["index_path"]] = doc["index_text"]
        texts.update(doc["shards"])
    texts[f"{R.PREFIX}FRONTIER.md"] = frontier
    texts[f"{R.PREFIX}LESSONS.md"] = lessons
    texts[f"{R.PREFIX}RESUME.md"] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "Follow-up to the accepted C11-review absorption: after applying revision 105 the verifiers exposed two "
            "side effects of the in-place C11 v2 rewrite (a dropped univalence row and a stale row-label contract in "
            "the retrodiction checker) plus the cascading merge-manifest re-pin. This corrective checkpoint re-pins the "
            "affected hashes. No semantic change, no new mathematical claim, no push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 106,
                "session_id": SESSION_ID,
                "files": len(texts),
                "repinned_records": len(repinned),
                "manifest_records": len(manifest_records),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
