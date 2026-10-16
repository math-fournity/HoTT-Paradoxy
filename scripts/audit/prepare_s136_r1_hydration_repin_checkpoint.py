#!/usr/bin/env python3
"""Prepare revision 136: remove an empty receipt from R1 full-text hydration."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260914-136-R1-HYDRATION-REPIN"
PREV = "S-RES-20260914-135-R1-FIXED-MACHINE-MAIN"
R1_ID = "A-CUBICAL-MACHINE-HALTING-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
EMPTY_STDERR = "HoTT/verification/runs/20260914-MP-CUBICAL-MACHINE-HALTING-001-01/stderr.txt"
RUN = "HoTT/verification/runs/20260914-MP-CUBICAL-MACHINE-HALTING-001-01/RUN.json"
STATUS = "CORE_GENERATION_4_R1_FIXED_MACHINE_MAIN_PROVED_R2_PROGRAMCODE_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s136", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只修复 R1 task hydration 与规划测试锚点，不改变 C-188–C-190。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "ALIGNED" if kid in {"KC-000007", "KC-000021"} else "NOT_TOUCHED"
        assessment = (
            "空 stderr 继续由 RUN.json 的零字节/hash 收据证明，但不再作为必须全文水合的文档；规划测试改核当前语义。"
            if relation == "ALIGNED" else f"本轮没有重新裁决“{label}”的内容。"
        )
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{RUN}`；{kid} | R2 及 S135 的全部开放义务不变。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO。",
        "- direction_change: NO_SEMANTIC_CHANGE。",
        "- panorama_change: NO_SEMANTIC_CHANGE。",
        "- essay_change: NO。",
        "- update_decision: empty stderr 由 RUN receipt 间接水合；programmatic test 重绑当前措辞。",
        "- cross_conflicts: runtime 拒绝零字节 full-source；证明证据本身仍完整且未修改。",
        "- unresolved: 与 S135 相同。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 135 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_135_S135")
    if SESSION_ID in state["records"]:
        raise SystemExit("SESSION_ALREADY_EXISTS")
    if (ROOT / EMPTY_STDERR).stat().st_size != 0:
        raise SystemExit("R1_STDERR_NOT_EMPTY")
    if EMPTY_STDERR not in state["records"][R1_ID]["full_sources"]:
        raise SystemExit("R1_EMPTY_STDERR_NOT_HYDRATED")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    projection_edit.replace_in_index(direction, "source_state_revision: 135", "source_state_revision: 136")
    projection_edit.replace_in_index(direction, "projection_generation: 20260914-direction-117", "projection_generation: 20260914-direction-118")
    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.replace_in_index(panorama, "source_state_revision: 135", "source_state_revision: 136")
    projection_edit.replace_in_index(panorama, "projection_generation: 20260914-outcome-117", "projection_generation: 20260914-outcome-118")
    memory = projection_edit.load(ROOT, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S136 R1 水合重绑定：S135 的数学证据未变。显式 R1 task plan 因零字节 `stderr.txt` 被 runtime 的非空正文约束拒绝；现从 `full_sources/source_hashes` 移除该空文件，零字节与 SHA-256 仍由 `RUN.json` 固定。程序化规划测试从 S130 旧句更新为 S135 当前语义，5/5 PASS。下一步仍是 R2 ProgramCode。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS136：R1 task hydration 已修复。空 `stderr.txt` 不再作为全文输入，零字节/hash 仍由 RUN.json 固定；规划测试 5/5。S135 数学证据与下一 `R2-PROGRAMCODE-001` 不变。\n\n",
    )

    state["revision"] = 136
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_R1_HYDRATION_REPIN"
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-118"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-118"

    r1 = state["records"][R1_ID]
    r1["full_sources"] = [rel for rel in r1["full_sources"] if rel != EMPTY_STDERR]
    r1["source_hashes"].pop(EMPTY_STDERR, None)
    r1["revalidation"] = f"{SESSION_ID}: empty stderr remains hash-bound through RUN.json but is not promoted as a full-text hydration document; mathematical evidence unchanged."
    plan_record = state["records"][PLAN_ID]
    plan_record["source_hashes"][TEST] = R.sha((ROOT / TEST).read_bytes())
    plan_record["revalidation"] = f"{SESSION_ID}: test anchors updated from the S130 wording to the S135 R1-main status; plan semantics unchanged."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 发现：显式 `A-CUBICAL-MACHINE-HALTING-001` hydration 把零字节 `{EMPTY_STDERR}` 当作必读正文，runtime 返回 `EMPTY_REQUIRED_FILE`。
- 修复：空文件从 stable record 的 `full_sources/source_hashes` 移除；其 bytes/hash 仍由 `{RUN}` 保存。
- 同步：`{TEST}` 更新为 R1 main 当前语义，5/5 PASS。
- 边界：C-188–C-190、run、索引与 S135 判词均未修改；下一 R2 不变。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "trigger": "EMPTY_REQUIRED_FILE:R1 stderr.txt",
        "stderr_evidence_route": RUN,
        "programmatic_tests": "5/5 PASS",
        "new_math_claims": [],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "MECHANICALLY_VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, RUN, TEST],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, R1_ID, PLAN_ID],
        "scope": "Repair R1 full-text hydration and re-pin the current programmatic-plan test; no mathematical change.",
        "source_hashes": {}, "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Preserve the active R1 evidence while making explicit task hydration executable and continuing to R2.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 136, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
