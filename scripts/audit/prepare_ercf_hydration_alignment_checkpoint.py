#!/usr/bin/env python3
"""Prepare revision 29 to make the ERCF result task hydratable without treating empty stderr as prose."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-029-ERCF-PROOF-HYDRATION-ALIGNMENT"
RESULT_ID = "A-ERCF-FACTORIZATION-FORMAL-001"
EMPTY_STDERR = "HoTT/verification/runs/20260912-MP-ERCF-001-02/stderr.txt"
RUN_JSON = "HoTT/verification/runs/20260912-MP-ERCF-001-02/RUN.json"

SPEC = importlib.util.spec_from_file_location("runtime_ercf_hydration_alignment", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `NOT_TOUCHED` | "
            "本轮只修复 proof stable record 的认知水合路由：零字节 raw stderr 继续留存并由 RUN.json/hash/verifier 认证，但不再作为必须有正文的 full-source；不改变、证明或反驳该用户原文。 | "
            f"S028 proof package；S029/SESSION.md；核心认知.md {unit['id']} | HoTT 原生 consumer 与 fresh model behavior 仍开放。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变。",
        "- direction_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 29/projection generation 013。",
        "- panorama_change: `NO_SEMANTIC_CHANGE` — 只同步 source revision 29/projection generation 013。",
        "- update_decision: `STATE stable-record hydration route、MEMORY/LESSONS/RESUME 和 session receipt 更新；空 stderr 原件不修改。`",
        "- cross_conflicts: `RESOLVED_BY_SOURCE_CLASSIFICATION` — raw empty output 是运行证据，不是可加载正文；RUN.json 保留其 bytes/hash。",
        "- unresolved: `fresh model behavior 与下一 HoTT 原生数学构造仍开放。`",
        "", "## 汇总", "", "`NOT_TOUCHED=36`；本轮不改变数学命题或证明状态。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 28 or state.get("latest_session") != "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN":
        raise SystemExit("EXPECTED_REVISION_28_S028")
    if (root / EMPTY_STDERR).stat().st_size != 0:
        raise SystemExit("EXPECTED_ZERO_BYTE_STDERR")
    run = json.loads((root / RUN_JSON).read_text(encoding="utf-8"))
    if run.get("stderr", {}).get("bytes") != 0 or run.get("stderr", {}).get("sha256") != "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        raise SystemExit("RUN_STDERR_IDENTITY_MISMATCH")
    record = state["records"][RESULT_ID]
    if record["full_sources"].count(EMPTY_STDERR) != 1 or record["resolution"]["evidence"].count(EMPTY_STDERR) != 1:
        raise SystemExit("EXPECTED_EXACT_EMPTY_STDERR_HYDRATION_REFS")

    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"), "source_state_revision: 28", "source_state_revision: 29")
    direction = replace_once(direction, "projection_generation: 20260912-direction-012", "projection_generation: 20260912-direction-013")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"), "source_state_revision: 28", "source_state_revision: 29")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-012", "projection_generation: 20260912-outcome-013")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    anchor = "- `MP-ERCF-001` 是 F-011 下首个真实数学 package：Lean 4.33.1 final run/index/hash/exact replay PASS；源码和运行原件均在 repo；未提交，且只证明一般 `Type` 值因子化。"
    memory = replace_once(
        memory,
        anchor,
        anchor + "\n- S029 修复 `A-ERCF-FACTORIZATION-FORMAL-001` 的 task hydration：空 `stderr.txt` 仍原样保留并由 RUN.json/hash/verifier 认证，但不再被错误要求作为非空认知正文加载。",
    )
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "35. proof run 的零字节" not in lessons:
        lessons += "\n35. proof run 的零字节 stdout/stderr 是需要原样留存并用 hash 认证的运行证据，但不是认知 loader 要求的非空正文；stable record 应通过 RUN.json/source manifest/verifier 路由它，避免 `EMPTY_REQUIRED_FILE` 在跨 Session 水合时误阻塞。"
    lessons += "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\nS028 已完成",
        "## 当前停止点\n\nS029 已修复 `A-ERCF-FACTORIZATION-FORMAL-001` 的 research task hydration：空 stderr 作为 raw evidence 原样保留在 run，并由 RUN.json/hash/verifier 路由，不再进入要求非空正文的 `full_sources`。\n\nS028 已完成",
    )

    record["full_sources"].remove(EMPTY_STDERR)
    record["resolution"]["evidence"].remove(EMPTY_STDERR)
    record["revalidation"] = "A research task plan initially failed with EMPTY_REQUIRED_FILE on the correctly empty raw stderr. The file remains immutable evidence and hash-pinned by RUN.json; hydration now reads RUN.json/source manifest/verifier instead of treating zero-byte stderr as prose."
    state["revision"] = 29
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "ERCF_GENERAL_FACTORIZATION_MACHINE_PROVED_LOCAL_TASK_HYDRATION_ALIGNED_HOTT_NATIVE_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
    })
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-013"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-013"

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-RES-20260912-028-ERCF-FACTORIZATION-LEAN", RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, RUN_JSON, "scripts/audit/prepare_ercf_hydration_alignment_checkpoint.py"],
        "source_hashes": {RUN_JSON: R.sha((root / RUN_JSON).read_bytes())},
        "mathematical_status": "UNCHANGED_FROM_MP_ERCF_001",
        "cognition_status": "EMPTY_RAW_STDERR_ROUTED_WITHOUT_BLOCKING_TASK_HYDRATION",
        "scope": "Preserve the zero-byte raw stderr as immutable run evidence while removing it from non-empty cognition full_sources; no mathematical or research-direction change.",
    }
    session = f"""# {SESSION_ID}

- 触发：`plan --profile research --task {RESULT_ID}` 返回 `EMPTY_REQUIRED_FILE: {EMPTY_STDERR}`。
- 根因：零字节 stderr 是正确、必须保留的 raw run evidence；runtime 的 `full_sources` 面向可读认知正文，拒绝空文件也是正确行为。stable record 把两类资产混在同一加载列表。
- 修复：空 stderr 原件、其 SHA-256 和 RUN.json 均不修改；仅从 result record 的 `full_sources`/`resolution.evidence` 删除直接正文水合，继续通过 RUN.json、source manifest 和 verifier 路由。
- 数学状态：`MP-ERCF-001`/`C-59`–`C-66` 不变；仍是一般 Lean 结果、未提交、非 HoTT 悖论。
- 三件套：无语义变化；只同步 revision 29/generation 013。core 不变。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "observed_failure": {
            "command": f"python3 -B .codex/tools/cognition_runtime.py plan --profile research --task {RESULT_ID}",
            "result": f"BLOCKED EMPTY_REQUIRED_FILE: {EMPTY_STDERR}",
        },
        "preserved_evidence": {
            "path": EMPTY_STDERR,
            "bytes": 0,
            "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "run_json": RUN_JSON,
        },
        "post_checkpoint_required": ["research task plan succeeds", "proof exact replay", "29-direction/28-outcome three-way", "36/36 KC audit", "fresh revision 29", "projection freshness", "full regression", "git diff --check"],
        "mathematics": "UNCHANGED_FROM_MP_ERCF_001",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

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
        "authorization": "This in-scope alignment repairs a cross-session recovery failure discovered while verifying the user-authorized proof package; it preserves all raw evidence and changes no mathematical claim.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": relative, "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None, "text": value}
            for relative, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 29, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
