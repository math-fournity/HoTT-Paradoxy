#!/usr/bin/env python3
"""Prepare revision 129: register the dual-track communication contract."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-129-DUAL-TRACK-COMMUNICATION-CONTRACT"
PREV = "S-GOV-20260913-128-DUAL-TRACK-FORMAT-ALIGNMENT"
DECISION_ID = "A-MACHINE-OVERVIEW-DUAL-TRACK-DECISION-001"
RESULT_ID = "A-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT-001"
DECISION = "docs/decisions/统观双轨协作与阶段汇合决策-20260913.md"
CONTRACT = "docs/design/detailed/统观双轨AI通信与证据交换合同-20260913.md"
DETAILED_INDEX = "docs/design/detailed/README.md"
FEATURES = "feature-list.md"
RULINGS = "rulings.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s129", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [index for index, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def append_revalidation(record: dict, note: str) -> None:
    old = str(record.get("revalidation", "")).strip()
    record["revalidation"] = (old + " " + note).strip()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": ("ALIGNED", "把两个 AI 的身份、通信方法和证据依据分别写成可执行合同。"),
        "KC-000007": ("DEEPENED", "Codex 任务消息使两个 LLM 工作线可以交换有界控制信息，Git/证据包仍承担可复核事实。"),
        "KC-000012": ("DEEPENED", "通信握手要求 source OID、packet hash、write root、动作和回执，ASK 落到任务入口。"),
        "KC-000017": ("ALIGNED", "保留独立 worktree 与独立审查，不让直接消息把一方自评升级为共同真值。"),
        "KC-000021": ("ALIGNED", "数学结论继续走主库 F-011；控制消息和机器探索收据不能替代 proof/run/index。"),
        "KC-000022": ("ALIGNED", "通信只组织双轨工作，不改变 A/B 两类目标或宣称任一已经完成。"),
        "KC-000029": ("DEEPENED", "控制/证据双通道减少重复搬运，同时保留每次抽象与验证责任。"),
        "KC-000030": ("DEEPENED", "把理论经济统观和机器统观连接为可追踪消息与证据反馈，而不合并真值 owner。"),
        "KC-000035": ("ALIGNED", "TaskSpec/现实对应的语义判断仍由 S 轨审查，消息只传 locator 与动作。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本轮明确三个 worktree、项目治理接受状态与两个 AI 的通信合同，不启动数学研究。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(
            kid,
            ("NOT_TOUCHED", f"本轮没有重新研究或裁决“{label}”的数学、物理或哲学内容。"),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{CONTRACT}`；{kid} | "
            "目标悖论与既有数学义务不变。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户悖论或元数学原文。",
        "- direction_change: YES_IN_PLACE — 双轨方向补上任务消息与 Git/证据双通道，以及明确 write root。",
        "- panorama_change: YES_IN_PLACE — 登记通信合同已设计、task 已发现、握手尚未发送。",
        "- essay_change: NO — 第四件不变。",
        "- update_decision: S 轨 current 写入根=主库 main；M 轨写入根=machine worktree；控制消息与证据通道分离。",
        "- cross_conflicts: Codex task cwd 与实际 write root 不同，已在合同中显式区分。",
        "- unresolved: 尚无用户发送授权、SENT/ACKED 收据或 M 轨对合同的接受；Gate A/B/C 不变。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    for rel in [DECISION, CONTRACT, DETAILED_INDEX, FEATURES, RULINGS]:
        if not (ROOT / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 128 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_128_S128")
    if RESULT_ID in state["records"]:
        raise SystemExit("RESULT_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK`",
        "| `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK` | 第一次语义/研究统观与第二次机器统观保持独立生成，通过冻结 TaskSpec、候选与证据包阶段汇合；Codex task message 传控制意图，exact Git commit/不可变 packet 传可审计事实；主库拥有唯一 current truth | 用户本轮要求评估合并/接管/独立策略并追问 worktree、治理与通信；rulings §20–§21 | `ACTIVE_USER_DIRECTION` | `PARADOX_DISCOVERY`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY` | `OUT-TOP-MACHINE-OVERVIEW-DUAL-TRACK-DECISION`、`OUT-TOP-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT` | S 轨 current 写入根为主库 main；M 轨写 machine worktree。当前已发现 `机器统观` task ID，但未获发送授权、未建立 ACK；S 轨继续 L3/B/consumer，M 轨继续 P1/P2 修复，Gate A 后扩展 L2/L6 | `docs/decisions/统观双轨协作与阶段汇合决策-20260913.md`；`docs/design/detailed/统观双轨AI通信与证据交换合同-20260913.md` |",
    )
    for old, new in (
        ("source_state_revision: 128", "source_state_revision: 129"),
        ("projection_generation: 20260913-direction-110", "projection_generation: 20260913-direction-111"),
        (
            "semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_MACHINE_OVERVIEW_COORDINATION",
            f"semantic_status: {STATUS}",
        ),
        (
            "状态：`CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_MACHINE_OVERVIEW_COORDINATION`",
            f"状态：`{STATUS}`",
        ),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_shard = "全景视野/002 - 治理、门禁与骨架结果.md"
    projection_edit.append_to_shard(
        panorama,
        panorama_shard,
        "| `OUT-TOP-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT` | 三 worktree 身份与双轨 AI 通信合同：控制消息、Git/证据包、授权、握手、状态机、并发与失败恢复 | `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK` | 用户追问 + 本轮 Git/Codex App 只读核对 | `DOCUMENTED / CONTROL_CHANNEL_DISCOVERED_NOT_HANDSHAKEN / RUNTIME_OBSERVED_WITH_SCOPE` | 当前任务启动 cwd=detached `eb7b`，S 轨 current 写入根=主库 main，M 轨写入根=machine worktree；三者共享 common-dir；Codex 已发现 `机器统观` task ID，可用 task message 作控制通道，exact commit/packet 作证据通道 | 不证明另一 AI 已收到或接受合同；未发送消息；task summary 不是证据；不授权 merge/push/tag 或跨 worktree 写入 | `docs/design/detailed/统观双轨AI通信与证据交换合同-20260913.md`；`.codex/research/hott/sessions/S-GOV-20260913-129-DUAL-TRACK-COMMUNICATION-CONTRACT/` |",
    )
    panorama["shards"][panorama_shard] = panorama["shards"][panorama_shard].rstrip("\n") + "\n"
    for old, new in (
        ("source_state_revision: 128", "source_state_revision: 129"),
        ("projection_generation: 20260913-outcome-110", "projection_generation: 20260913-outcome-111"),
        (
            "semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_MACHINE_OVERVIEW_COORDINATION",
            f"semantic_status: {STATUS}",
        ),
        (
            "状态：`CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_MACHINE_OVERVIEW_COORDINATION`",
            f"状态：`{STATUS}`",
        ),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "2. 当前统观采用",
        "2. 当前统观采用**受控双轨、阶段汇合**。本 Codex task 启动 cwd 是 detached `eb7b` 审计 worktree（`fc79094a…`），但 S 轨 current 项目写入根是 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 的 `main`；所有 current 修改均以显式 workdir 执行原项目治理。S 轨继续负责语义/研究统观，下一项仍从 L3 时间/运动、B 方向或固定真实 consumer 选择可反驳工作包。",
    )
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "3. M 轨留在",
        "3. M 轨任务 `机器统观`（task ID `01a09a72-aeb6-7a50-81d6-d24f43c5e912`）只写 `/Volumes/D/HoTT-machine-overview`。控制通道使用 Codex task message，证据通道使用 exact commit/不可变 packet；当前仅发现任务，尚未获发送授权或取得 ACK。M 轨继续 P1/P2 修复，clean commit + 独立接受前不合并，Gate A 后优先扩展 L2/L6。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S129 双轨通信合同：机械确认本任务启动 cwd 是 detached `eb7b`，实际 S 轨 current 写入根是主库 `main`，M 轨写入根是 `/Volumes/D/HoTT-machine-overview`；三者共享 Git common-dir 但 index/工作文件隔离。Codex App 已发现活动任务 `机器统观` 及其 task ID。通信分为 task message 控制通道与 exact commit/不可变 packet 证据通道，并定义授权、握手、回执、并发、失败和恢复。当前状态 `DISCOVERED / LIVE_HANDSHAKE_NOT_STARTED`：未发送消息、未取得 ACK、未合并。无新数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = resume.replace(
        "## 当前停止点\n\nS127：",
        "## 当前停止点\n\nS129：双轨通信合同已落盘。当前 task 启动于 detached `eb7b`，S 轨 current 写入根为主库 main，M 轨写 machine worktree；Codex 已发现 `机器统观` task ID。控制=task message，证据=exact commit/不可变 packet；尚未获发送授权、未发送握手、未取得 ACK。S/M 的研究和修复队列、Gate A/B/C、ERCF-3 `GATED` 与数学状态不变。\n\nS127：",
        1,
    )

    state["revision"] = 129
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_DUAL_TRACK_COMMUNICATION_CONTRACT"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Communication: live handshake remains pending explicit user authorization; if authorized, send the v1 handshake to task 01a09a72-aeb6-7a50-81d6-d24f43c5e912 and require ACK with exact refs. "
        "Research remains unchanged: S track freezes one L3/B/concrete-consumer package; M track closes P1/P2 in its own worktree before Gate A."
    )
    state["projection"]["status"] = STATUS
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260913-direction-111"
    direction_record["semantic_status"] = STATUS
    add_once(direction_record["full_sources"], CONTRACT)
    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record["projection_generation"] = "20260913-outcome-111"
    panorama_record["semantic_status"] = STATUS
    add_once(panorama_record["full_sources"], CONTRACT)

    decision_record = state["records"][DECISION_ID]
    add_once(decision_record["full_sources"], CONTRACT)
    decision_record["source_hashes"][DECISION] = R.sha((ROOT / DECISION).read_bytes())
    decision_record["source_hashes"][CONTRACT] = R.sha((ROOT / CONTRACT).read_bytes())
    add_once(decision_record["related_records"], RESULT_ID)
    append_revalidation(
        decision_record,
        f"{SESSION_ID} clarified the launch-cwd/write-root distinction and added the v1 control-message plus Git/evidence communication contract; dual-track gates and research allocation are unchanged.",
    )

    state["records"][RESULT_ID] = {
        "classification": "DUAL_CHANNEL_CONTROL_AND_EVIDENCE_COMMUNICATION",
        "depends_on": [],
        "evidence_status": "DOCUMENTED / RUNTIME_OBSERVED_WITH_SCOPE",
        "full_sources": [CONTRACT, DECISION, FEATURES, RULINGS],
        "kind": "ai_communication_contract",
        "lifecycle_status": "CURRENT",
        "path": CONTRACT,
        "related_records": [DECISION_ID, SESSION_ID],
        "scope": (
            "Versioned v1 contract for two Codex tasks and three shared-common-dir worktrees. Control plane uses task messages; evidence plane uses exact Git commits and immutable packets. "
            "The machine task was discovered read-only, but no message has been sent and no ACK exists. S writes main; M writes the machine worktree; the detached eb7b launch worktree is not a current owner."
        ),
        "source_hashes": {
            CONTRACT: R.sha((ROOT / CONTRACT).read_bytes()),
            DECISION: R.sha((ROOT / DECISION).read_bytes()),
        },
        "status": "complete",
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户问题：本 AI 在哪个 Git worktree 工作、是否执行原项目治理、两个 AI 未来怎样通信。
- worktree：task launch=`/Users/aurolafly/.codex/worktrees/eb7b/HoTT_AI_HANDOFF_20260911` detached `fc79094a…`；S current write root=`/Volumes/D/HoTT_AI_HANDOFF_20260911` main `510466c…`；M write root=`/Volumes/D/HoTT-machine-overview` branch `feat/machine-overview-m1` HEAD `2705847…`；common-dir 相同。
- 治理：S current 操作实际加载并执行主库 AGENTS、本地治理 Skill、四件套、STATE/profile/hydration、36-KC audit 与 checkpoint。
- task discovery：`非自动化统观`=`01a09b1e-c809-7453-89fa-7b5f01115d35`；`机器统观`=`01a09a72-aeb6-7a50-81d6-d24f43c5e912`，发现时 active。
- 合同：control plane=Codex task message；evidence plane=exact commit + immutable packet；每条消息固定 write root/ref/hash/action/prohibitions/reply。
- 当前边界：只读发现完成；未获跨任务发送授权，故没有 SENT/ACKED 收据；未修改 M worktree、未合并/push/tag、未新增数学 claim。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "git_worktrees": {
                "launch_audit": {"path": "/Users/aurolafly/.codex/worktrees/eb7b/HoTT_AI_HANDOFF_20260911", "head": "fc79094a79ceeeb3a19fa76b03f263d52538a918", "branch": "DETACHED"},
                "s_current": {"path": "/Volumes/D/HoTT_AI_HANDOFF_20260911", "head_before_change": "510466c1be18ed6363b6098b5a51210d1bc2fff0", "branch": "main"},
                "m_current": {"path": "/Volumes/D/HoTT-machine-overview", "head": "2705847db5893bbbdfae21abb58c5a01beff6e27", "branch": "feat/machine-overview-m1", "dirty": True},
                "common_dir": "/Volumes/D/HoTT_AI_HANDOFF_20260911/.git",
            },
            "codex_tasks": {
                "s": "01a09b1e-c809-7453-89fa-7b5f01115d35",
                "m": "01a09a72-aeb6-7a50-81d6-d24f43c5e912",
                "discovery": "READ_ONLY_LIST_THREADS",
            },
            "communication_status": "DISCOVERED_LIVE_HANDSHAKE_NOT_STARTED",
            "outbound_messages": 0,
            "new_math_claims": [],
            "machine_worktree_mutation": "NONE",
            "merge": "NOT_PERFORMED",
            "push": "NOT_AUTHORIZED",
            "tag": "NOT_CREATED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "DOCUMENTED / RUNTIME_OBSERVED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, CONTRACT, DECISION],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, RESULT_ID, DECISION_ID],
        "scope": "Worktree/governance clarification and v1 control/evidence communication contract; no outbound message and no mathematical change.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text(ROOT)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Record the user-requested clarification of actual worktree identity, project-local governance acceptance, and the designed future communication mechanism. Do not send a cross-task message or mutate the machine worktree.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 129, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
