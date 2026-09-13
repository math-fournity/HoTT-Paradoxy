#!/usr/bin/env python3
"""Prepare revision 111: refresh the proof/run indexes and re-pin the two records that own them."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-111-PROOF-INDEX-REFRESH"
PREV = "S-RES-20260913-110-ERCF3-T3-JOINT"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s111", RUNTIME_PATH)
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
        "本单元只刷新证明/运行索引并重绑哈希，不产生数学结论。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in ("KC-000021",):
            relation, assessment = "ALIGNED", "索引刷新服务 F-011 的可发现性；不改变任何 claim 或证据等级。"
        elif kid in ("KC-000017",):
            relation, assessment = "ALIGNED", "把滞后索引作为真实缺陷修复，而不是靠叙述掩盖。"
        else:
            relation, assessment = "NOT_TOUCHED", f"本轮没有研究或重新裁决「{label}」的数学/哲学内容。"
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{FORMAL_README}`；{kid} | 数学开放项不变。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO_CHANGE(reason) — 研究队列未变；只修索引与哈希绑定。",
        "- panorama_change: NO_CHANGE(reason) — 索引刷新不是研究结果，不新增全景行。",
        "- essay_change: NO_CHANGE(reason) — 常驻第四件未改动。",
        f"- update_decision: 刷新 `{FORMAL_README}`（补 verification-event 与 ercf3-t3-joint 两个 later package）与 `{RUNS_README}`（run 索引补 5 组 later runs）；`HoTT/README.md` 计数改为 17 冻结 + 2 追加。",
        "- cross_conflicts: 无冲突；两条 record 的 source_hashes 变更由 revalidation 说明。",
        "- unresolved: 无新增未知；索引只覆盖已登记 run。",
        "",
        "## 汇总",
        "",
        "`ALIGNED=2`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 110 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_110_S110")

    formal_hash = R.sha((root / FORMAL_README).read_bytes())
    runs_hash = R.sha((root / RUNS_README).read_bytes())
    repinned = []
    for record_id, record in state["records"].items():
        hashes = record.get("source_hashes") or {}
        changed = []
        for path, new_hash in ((FORMAL_README, formal_hash), (RUNS_README, runs_hash)):
            if path in hashes and hashes[path] != new_hash:
                hashes[path] = new_hash
                changed.append(path)
        if changed:
            record["source_hashes"] = hashes
            record["revalidation"] = (
                f"{', '.join(changed)} re-hashed by {SESSION_ID}: the formal package index and the run index were "
                "refreshed to include the two later_packages (MP-VERIFICATION-EVENT-001, MP-ERCF3-T3-JOINT-001) and their "
                "runs. Record scope, claims and evidence status are unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "094"),
        ("PANORAMA", R.PANORAMA, "outcome", "094"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 110", "source_state_revision: 111"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-095",
        )
        projections[key] = doc

    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S111 证明/运行索引刷新（corrective hygiene）：`HoTT/formal/README.md` 补上两个 later package"
        "（`MP-VERIFICATION-EVENT-001` C-149–C-156、`MP-ERCF3-T3-JOINT-001` C-157–C-159）并把“17 个 package”改为"
        "“17 冻结 + 2 追加”；`HoTT/verification/runs/README.md` 的 run 索引补齐 5 组 later runs"
        "（TRUNC-NORECOVERY -01/-02/-03、NOCANONICAL -01/-02、UNIMATH-REPLAY -01/-02、VERIFICATION-EVENT-01、"
        "ERCF3-T3-JOINT -01/-02）；`HoTT/README.md` 计数与下一义务同步。两条 owner record"
        "（`A-MATH-PROOF-DELIVERY-GATE-001`、`S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT`）按新哈希 revalidation 重绑。"
        "数学状态与研究队列不变。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row59 = (
        "| 已闭合工作包 59 | ERCF-3 T3 共享判定联合递归（S110，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` | "
        "C-157–C-159：显式共享判定一致 + 原始逐出现判定的项层恒等式 + 修正后的公式层恒等式；"
        "run `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02` exit 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；"
        "修正 `CodeStoreFixF` 的 all 影子分支双重编码（新模块给出，不改历史）；见 "
        "`HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |"
    )
    frontier = replace_once(
        frontier,
        row59,
        row59 + "\n| 已闭合工作包 60 | 证明/运行索引刷新（S111，corrective hygiene） | `INDEX_REFRESH_ONLY` | "
        "`HoTT/formal/README.md` 补齐两个 later package 与“17 冻结 + 2 追加”表述；"
        "`HoTT/verification/runs/README.md` 的 run 索引补齐 5 组 later runs；`HoTT/README.md` 计数与下一义务同步；"
        "两条 owner record 按新哈希 revalidation 重绑；数学与队列不变 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n90. 新增 proof package 后必须**同时刷新两级索引**：`HoTT/formal/README.md`（包清单）与 "
        "`HoTT/verification/runs/README.md`（run 索引）。本轮发现两者分别滞后一个和五个登记周期——"
        "包本身、矩阵、closure registry 都对，但未来 AI 从索引出发找不到它们。索引文件被 record 钉住时，"
        "刷新后要在同一 checkpoint 里做 revalidation 重绑，而不是回避更新。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S111（索引刷新，corrective）：`HoTT/formal/README.md` 与 `HoTT/verification/runs/README.md` 已补齐两个 "
        "later package 与 5 组 later runs；`HoTT/README.md` 计数改为 17 冻结 + 2 追加；两条 owner record 已 revalidation 重绑。"
        "数学状态、研究队列与门 A/门 B 状态不变；T3 下一义务仍是证明谓词表示性、反射与对角不动点（ERCF-3 `GATED`）。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 触发：S110 交付后核对索引，发现 `HoTT/formal/README.md` 缺两个 later package（verification-event 与 ercf3-t3-joint）、
  `HoTT/verification/runs/README.md` 的 run 索引停在 Cauchy、`HoTT/README.md` 仍写“17 个 package”。
- 处置：刷新两级索引 + 计数表述；两条 owner record（`A-MATH-PROOF-DELIVERY-GATE-001`、
  `S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT`）按新哈希 revalidation 重绑；本 checkpoint 写 MUTABLE 状态。
- 交付：`{FORMAL_README}`、`{RUNS_README}`、`HoTT/README.md`；MEMORY/FRONTIER/LESSONS 90/RESUME 同步。
- 边界：纯索引/证据可发现性修复；不新增数学 claim、不改判词、不重跑 run；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "kind": "index_refresh_corrective",
            "refreshed": [FORMAL_README, RUNS_README, "HoTT/README.md"],
            "repinned_records": sorted(repinned),
            "new_math_claims": [],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 111
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_PROOF_INDEX_REFRESH",
            "status": STATUS,
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-095", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-095", "semantic_status": STATUS}
    )
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, "A-ERCF3-T3-JOINT-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, FORMAL_README, RUNS_README],
        "source_hashes": {},
        "scope": (
            "Corrective index refresh: formal package index and run index updated for the two later packages and their "
            "runs; two owner records re-pinned by revalidation. No mathematical change."
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
            "Active goal 'finish everything before stopping'. After delivering MP-ERCF3-T3-JOINT-001 the two package/run "
            "indexes were found stale (missing the two later packages / five later run groups), so they were refreshed and "
            "the two owner records re-pinned. Index/evidence-discoverability repair only: no mathematical claim, no push."
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
                "revision": 111,
                "session_id": SESSION_ID,
                "files": len(texts),
                "repinned": sorted(repinned),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
