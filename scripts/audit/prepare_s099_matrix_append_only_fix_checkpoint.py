#!/usr/bin/env python3
"""Prepare revision 99: keep the claim matrix append-only and record the lesson."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-099-MATRIX-APPEND-ONLY-FIX"
PREV = "S-GOV-20260913-098-EXTERNAL-WORK-IMPORT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/verification-event吸收与独立核验-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V3_5_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V3_5_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
RELEASE_REF = "governance-v3.5.0"

SPEC = importlib.util.spec_from_file_location("runtime_s099", RUNTIME_PATH)
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
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只修矩阵追加纪律与登记教训。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid == "KC-000021":
            relation = "ALIGNED"; assessment = "矩阵的冻结前缀/追加纪律是 proof Gate 版本闭合的一部分；本轮把误插的 9 行移回文末并机械复核。"
        else:
            relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{EVIDENCE}`；{kid} | 数学开放项不变。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只同步 revision 字段（98→99）。",
        "- panorama_change: NO_SEMANTIC_CHANGE — 只同步 revision 字段（98→99）。",
        "- update_decision: 把 `MP-VERIFICATION-EVENT-001` 的 9 行从矩阵中部移到文末追加节；冻结前缀字节不变；`verify_proof_version_closure.py` 与 `verify_formal_proof_run.py --rerun` 复跑通过。",
        "- cross_conflicts: 我最初把新行插在 C-148 之后，破坏 registry 要求的 append-only 前缀；已改为末尾追加并把该纪律写入 LESSONS。",
        "- unresolved: fresh model behavior NOT_RUN；不 push。",
        "", "## 汇总", "", "`ALIGNED=1`；`NOT_TOUCHED=35`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 98 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_98_S098")

    projections = {}
    for key, rel, gen in (("DIRECTION", R.DIRECTION, "direction"), ("PANORAMA", R.PANORAMA, "outcome")):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(doc, "source_state_revision: 98", "source_state_revision: 99")
        projection_edit.replace_in_index(doc, f"projection_generation: 20260913-{gen}-082",
                                         f"projection_generation: 20260913-{gen}-083")
        projections[key] = doc
    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S099 矩阵追加纪律修正：`MP-VERIFICATION-EVENT-001` 的 9 行最初插在 C-148 之后，破坏 "
        "`PROOF_VERSION_CLOSURE` 的 append-only 冻结前缀要求（`CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR`）；"
        "已把 9 行按字节移回文末追加节，冻结前缀保持不变，closure 与 formal-run 校验复跑 PASS。\n",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n78. `HoTT/CLAIM_EVIDENCE_MATRIX.md` 必须**保持冻结前缀 + 末尾追加**：`verify_proof_version_closure.py` 要求当前矩阵"
        "以 d3dfb0e 快照为前缀，中间插入新行会直接 `CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR` BLOCK。新 proof package 的包行与 claim 行"
        "一律追加到文末（可另起追加节 + 自己的表头）；只要行文本不变，旧 run 的 `index-row-manifest` 仍为 `ROW_STABLE_AFTER_INDEX_EVOLUTION`。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"), "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：矩阵追加纪律修正完成（9 行移到文末追加节，冻结前缀不变）；"
        f"`verify_proof_version_closure.py` PASS（frozen 17 + later 1）与 `verify_formal_proof_run --rerun` PASS（ROW_STABLE）。"
        f"下一项回到研究第一线（E6 consumer）或用户指定课题。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 背景：S098 吸收外部工作时把 `MP-VERIFICATION-EVENT-001` 的 9 行插在 C-148 之后；`verify_proof_version_closure.py` 报
  `CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR`（要求当前矩阵以 d3dfb0e 快照为前缀）。
- 修正：把 9 行**按字节原样**移到文末新追加节（不重写任何旧行、不改冻结前缀）；行文本不变使旧 run 的
  `index-row-manifest` 仍判 `ROW_STABLE_AFTER_INDEX_EVOLUTION`。
- 复核：`verify_proof_version_closure.py` → `PASS_WITH_SCOPE`（frozen 17 + later 1 / 8 claims）；
  `verify_formal_proof_run.py --rerun` → `PASS_WITH_SCOPE`、`ROW_STABLE_AFTER_INDEX_EVOLUTION`、`EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 教训写入 LESSONS 第 78 条；本 checkpoint 只同步三件套 revision 字段（98→99）与顺序日志。不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "release_ref": RELEASE_REF,
        "fix": "claim-matrix append-only prefix",
        "mathematics": "NO_CHANGE_TO_ANY_CLAIM",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 99
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_MATRIX_APPEND_ONLY_FIX",
        "status": STATUS,
        "release_ref": RELEASE_REF,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update({"projection_generation": "20260913-direction-083"})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update({"projection_generation": "20260913-outcome-083"})
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-VERIFICATION-EVENT-IMPORT-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         "scripts/audit/verify_proof_version_closure.py"],
        "source_hashes": {},
        "scope": "Keep HoTT/CLAIM_EVIDENCE_MATRIX.md an append-only successor of the frozen d3dfb0e snapshot by moving the imported package rows to an end-of-file section; no claim content changed.",
    }
    texts = {
        R.DIRECTION: projections["DIRECTION"]["index_text"],
        R.PANORAMA: projections["PANORAMA"]["index_text"],
        "MEMORY.md": memory["index_text"],
        f"{R.PREFIX}FRONTIER.md": (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
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
        "authorization": ("Follow-up to the authorized external-work import: restore the claim matrix's append-only contract "
                          "(frozen prefix intact, imported rows moved to an end-of-file section), record the lesson, and sync "
                          "the trio revision fields. No claim content changes; no push."),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 99,
                      "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
