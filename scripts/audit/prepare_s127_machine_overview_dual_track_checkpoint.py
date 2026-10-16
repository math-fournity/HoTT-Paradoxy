#!/usr/bin/env python3
"""Prepare revision 127: adopt dual-track machine-overview coordination."""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-127-MACHINE-OVERVIEW-DUAL-TRACK-DECISION"
PREV = "S-GOV-20260913-126-PROJECTION-STATUS-ALIGNMENT"
RESULT_ID = "A-MACHINE-OVERVIEW-DUAL-TRACK-DECISION-001"
DECISION = "docs/decisions/统观双轨协作与阶段汇合决策-20260913.md"
DECISIONS_INDEX = "docs/decisions/README.md"
FEATURES = "feature-list.md"
RULINGS = "rulings.md"
IMPORT_ROOT = "audit/imports/machine-overview-strategy-20260913"
IMPORT_MANIFEST = f"{IMPORT_ROOT}/IMPORT.json"
IMPORTED_PLAN = f"{IMPORT_ROOT}/HoTT非现实性悖论机器统观完整方案.md"
IMPORTED_METHOD = f"{IMPORT_ROOT}/20260913-机器辅助统观与HoTT候选搜索方法.md"
IMPORTED_HANDOFF = f"{IMPORT_ROOT}/交接说明-机器统观M1-20260913.md"
IMPORTED_AUDIT = f"{IMPORT_ROOT}/20260913-M1自动化统观修复复审.md"
TAKEOVER_REPAIR = "audit/独立审计第二轮整改与接管-20260913.md"
FIRST_REPORT = "audit/统观工作技术报告-20260913.md"
PREP_SCRIPT = "scripts/audit/prepare_s127_machine_overview_dual_track_checkpoint.py"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_MACHINE_OVERVIEW_COORDINATION"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s127", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:100]}:{count}")
    return text.replace(old, new, 1)


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


def git_head(root: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": ("ALIGNED", "用目标、方法、证据和验收分别比较两条统观线，并形成可执行分工。"),
        "KC-000002": ("ALIGNED", "机器线继续使用来源锁定的 profile/理论片段；主库保留 Theory Schema 与规则判断责任。"),
        "KC-000005": ("ALIGNED", "双轨允许探索先产生候选，最终归因和现实桥梁仍分层处理。"),
        "KC-000006": ("DEEPENED", "任务分区保留时间/运动、时序、量词、B 方向与自反，不让 L1 校准吞掉其它机制。"),
        "KC-000007": ("DEEPENED", "机器统观承担有类型生成与反例反馈，语义统观保留 LLM 的问题生成和独立审查。"),
        "KC-000009": ("ALIGNED", "交换包要求每个候选绑定具体 profile、规则、TaskSpec、运行和失败位置。"),
        "KC-000010": ("ALIGNED", "校准器与目标悖论分开验收，正常 Agda ground instance 不被误写成现实相对发现。"),
        "KC-000011": ("ALIGNED", "S 轨优先时间/运动与 B 方向，M 轨先修证据链后扩展 L2/L6，避免把时间缩成 delay。"),
        "KC-000012": ("DEEPENED", "Gate A/B 把 ASK 落到执行输入、任务对应、数学命题和结果晋升的不同检查点。"),
        "KC-000013": ("DEEPENED", "最新复审证明声明有 validator 不等于 ASK 已可靠执行；双轨保留独立反证。"),
        "KC-000014": ("ALIGNED", "B 方向保留为 S 轨独立探索面，不被机器线 L1 校准替代。"),
        "KC-000015": ("ALIGNED", "C11 继续提供理论经济启发，但不成为两轨共享的排他剪枝规则。"),
        "KC-000017": ("DEEPENED", "保留不同生成机制和独立汇合者，避免一条线的 PASS、自评或偏见自动传播。"),
        "KC-000021": ("ALIGNED", "机器候选与正式数学结论分两层收据；主库 F-011 仍是数学交付门禁。"),
        "KC-000022": ("ALIGNED", "两条现实相对方向均保持；不同工作线只改变探索职责，不改变目标。"),
        "KC-000024": ("DEEPENED", "研究分区显式保留时间/运动、量词/完成顺序和 B 方向，防止有限时序模型冒充全覆盖。"),
        "KC-000027": ("ALIGNED", "机器系统的通用软件缺陷与 HoTT 特定数学问题分开记录。"),
        "KC-000029": ("DEEPENED", "把两种统观各自获得的经济收益和转移的验证责任作为架构选择依据。"),
        "KC-000030": ("DEEPENED", "第一次理论经济账本与第二次机器搜索形成互补接口，不互相改写真值。"),
        "KC-000031": ("ALIGNED", "机器线有限 grammar 未覆盖不能证明 HoTT 不覆盖；表达问题仍由可修订任务驱动。"),
        "KC-000035": ("DEEPENED", "TaskSpec 忠实性由 S 轨独立审查，避免方便编码的部分反向替代完整研究理论。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本轮只决定第一次统观线与机器统观线的职责和汇合方式，不启动新数学研究。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(
            kid,
            ("NOT_TOUCHED", f"本轮没有重新研究或裁决“{label}”的数学或物理内容。"),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{DECISION}`；{kid} | "
            "目标悖论、现实桥梁与未证明数学义务保持原状态。 |"
        )
    counts: dict[str, int] = {}
    for relation, _ in focus.values():
        counts[relation] = counts.get(relation, 0) + 1
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 没有新的用户悖论或元数学原文；generation-4/36 KC 保持。",
        "- direction_change: YES_IN_PLACE — 新增双轨协作方向，并把近期动作分为 S 轨探索与 M 轨修复/扩展。",
        "- panorama_change: YES_IN_PLACE — 登记机器方案、M1 实现、最新 REQUEST_CHANGES 与当前不集成判断。",
        "- essay_change: NO — AI 阐释层的思想关系没有变化。",
        "- update_decision: CURRENT_PROJECT_DECISION — 受控双轨、冻结交换、阶段汇合；不整体交接或直接合并。",
        "- cross_conflicts: 旧 M1 handoff 的完整接受措辞由较晚独立复审否定；当前状态使用 REQUEST_CHANGES。",
        "- unresolved: M 轨 P1/P2、M2–M5、首个非 L1 任务；S 轨下一候选；Gate A/B/C 均未通过。",
        "",
        "## 汇总",
        "",
        f"`ALIGNED={counts.get('ALIGNED', 0)}`；`DEEPENED={counts.get('DEEPENED', 0)}`；"
        f"其余 `NOT_TOUCHED={len(manifest['units']) - len(focus)}`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        DECISION,
        DECISIONS_INDEX,
        FEATURES,
        RULINGS,
        IMPORT_MANIFEST,
        IMPORTED_PLAN,
        IMPORTED_METHOD,
        IMPORTED_HANDOFF,
        IMPORTED_AUDIT,
        TAKEOVER_REPAIR,
        FIRST_REPORT,
        PREP_SCRIPT,
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 126 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_126_S126")
    if RESULT_ID in state["records"]:
        raise SystemExit("RESULT_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    projection_edit.append_to_shard(
        direction,
        direction_shard,
        "| `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK` | 第一次语义/研究统观与第二次机器统观保持独立生成，通过冻结 TaskSpec、候选与证据包阶段汇合；主库拥有唯一 current truth | 用户本轮要求评估合并/接管/独立策略；ruling §20 | `ACTIVE_USER_DIRECTION` | `PARADOX_DISCOVERY`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY` | `OUT-TOP-MACHINE-OVERVIEW-DUAL-TRACK-DECISION` | S 轨在主库选择 L3 时间/运动、B 方向或真实 consumer 的可反驳候选；M 轨先关闭最新复审 P1/P2，独立复审接受后再优先扩展 L2/L6；两边不共写 worktree/current truth | `docs/decisions/统观双轨协作与阶段汇合决策-20260913.md`；`audit/imports/machine-overview-strategy-20260913/` |",
    )
    priority_shard = "方向追踪/005 - 交叉审视、优先级与更新规则.md"
    direction["shards"][priority_shard] = replace_line(
        direction["shards"][priority_shard],
        "4. **当前第一工作包",
        "4. **当前统观双轨与第一工作包**：S 轨留在主库，继续用 C11 v2 但不设排他 Gate，优先选择时间/运动结构、B 方向或固定真实 consumer 的同任务可反驳候选；M 轨留在独立 worktree，先关闭最新复审的 P1/P2 并取得独立接受，再优先把机器搜索扩展到 L2 或 L6。两轨通过冻结 TaskSpec/输入/候选/run 包阶段汇合，不直接共写 current owners。T3 剩余表示性/反射义务仍需明确 consumer；第十三批抽样与无差别基础库扫描保持低优先级。",
    )
    for old, new in (
        ("source_state_revision: 126", "source_state_revision: 127"),
        ("projection_generation: 20260913-direction-108", "projection_generation: 20260913-direction-109"),
        (
            "semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_ROUND2_AUDIT_REPAIR_TAKEOVER",
            f"semantic_status: {STATUS}",
        ),
        (
            "状态：`CORE_GENERATION_4_GOVERNANCE_V4_ROUND2_AUDIT_REPAIR_TAKEOVER`",
            f"状态：`{STATUS}`",
        ),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_shard = "全景视野/002 - 治理、门禁与骨架结果.md"
    projection_edit.append_to_shard(
        panorama,
        panorama_shard,
        "| `OUT-TOP-MACHINE-OVERVIEW-DUAL-TRACK-DECISION` | 比较第一次统观 current workline 与 M0–M5 机器方案/M1 实现/两轮实现审计后，采用受控双轨与阶段汇合 | `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK`、`DIR-TOP-THEORY-ECONOMY-LEDGER` | 用户委托本轮评估与当前 AI 架构决策 | `DOCUMENTED / CURRENT_PROJECT_DECISION / MACHINE_INTEGRATION_NOT_ACCEPTED` | 两线能力互补；机器方案完整但实际 M0/M1 最新复审仍 `REQUEST_CHANGES`，且活动 worktree 有未提交修复；因此不整体交接、不直接合并，使用 Gate A/B/C 分别验收工具、候选和职责变化 | 不证明机器搜索有效性、M0/M1 已接受、M2–M5 已实现、目标悖论存在或不存在；不把活动 dirty 字节当已验收实现 | `docs/decisions/统观双轨协作与阶段汇合决策-20260913.md`；`audit/imports/machine-overview-strategy-20260913/IMPORT.json` |",
    )
    for old, new in (
        ("source_state_revision: 126", "source_state_revision: 127"),
        ("projection_generation: 20260913-outcome-108", "projection_generation: 20260913-outcome-109"),
        (
            "semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_ROUND2_AUDIT_REPAIR_TAKEOVER",
            f"semantic_status: {STATUS}",
        ),
        (
            "状态：`CORE_GENERATION_4_GOVERNANCE_V4_ROUND2_AUDIT_REPAIR_TAKEOVER`",
            f"状态：`{STATUS}`",
        ),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    lines = memory["shards"][memory_shard].splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("2. 数学研究第一线"))
    end = start
    while end < len(lines) and (end == start or lines[end].startswith(tuple(f"{n}. " for n in range(3, 10)))):
        end += 1
    queue = [
        "2. 当前统观采用**受控双轨、阶段汇合**（S127；用户裁定 §20）：S 轨留在主库，负责语义/研究统观、同任务与现实对应、候选反解释和正式数学门禁；下一项从 L3 时间/运动结构、B 方向或固定真实 consumer 中选择一个可反驳工作包。C11 v2 继续作启发与审查账本，不是准入或穷尽 Gate。",
        "3. M 轨留在 `/Volumes/D/HoTT-machine-overview`，由另一 AI 继续：稳定实现为 `56c4306`、文档 HEAD 为 `2705847`；最新独立复审仍 `REQUEST_CHANGES`，2026-09-13T16:34:11Z 又观察到 6 个 tracked 实现文件与 v2 profile/task/grammar/legacy 资产在途。先关闭 P1/P2、形成 clean commit 并取得独立接受，再优先扩展 L2/L6；当前不合并、不写主库 current owners。",
        "4. T3 编码线的自足部分仍由 C-157–C-187 支持。C-168 只证明 `double` 下 1 无原像；`codeAtom` 实际满射（C-184/C-185）；`codeT'`/`codeF'` 像不含 1（C-186/C-187）。编码/解码/替换/引用已闭合到精确范围；对象层可表示性、证明谓词 `P` 的表示性、反射与对角不动点仍需明确 consumer。ERCF-3 保持 `GATED`。",
        "5. 第十三批抽样与无差别基础库扫描降优先级；只有出现新判别锚点或具体下游 consumer 才重开。",
        "6. 当前仍未得到 E6、现实桥梁、`NATURAL_USAGE_MISMATCH`、自馈不可停机实例或 HoTT 内部矛盾；17 个 current proof package 仍只支持各自精确范围。",
        "7. 历史交接开放项仍包括 2,396 条 claim、aistudio coverage、历史数学主张、response→artifact/code/Git 因果和 S067–S085 缺 KC audit；缺失历史证据不追溯伪造。",
        "8. 版本闭合：主库当前 base `22cb363…`；S127 决策、外部文档导入与 checkpoint 待本轮提交；不 push、不 tag、不合并机器分支。",
    ]
    lines[start:end] = queue
    memory["shards"][memory_shard] = "\n".join(lines) + "\n"
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S127 统观双轨决策：比较主库第一次统观与 `/Volumes/D/HoTT-machine-overview` 的 M0–M5 方案、M1 实现及最新独立复审后，决定不整体交接、不直接合并，也不永久隔绝。S 轨留在主库做语义/研究统观；M 轨在独立 worktree 先关闭 `REQUEST_CHANGES` 的 P1/P2，再扩展 L2/L6；两轨以冻结 TaskSpec/候选/run 证据包阶段汇合，Gate A/B/C 分别控制工具集成、结果吸收与职责变化。外部 16 份文档按字节导入；活动 dirty 代码未导入、未验收。未新增数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "# HoTT 研究前沿（S125 接管修复后）\n\nS125 接管修复只改变当前研究资格与证明证据关系，不新增数学 claim：C-184–C-187 仍有效；ERCF-3 仍 `GATED`；T3 剩余义务不变。\n\n当前首要动作从纠正后的 C11 v2 全候选面选择一个具体、可反驳工作包；门 A/门 B 是暂选路线，时间/运动、量词/完成顺序、B 方向独立行、开放 triage consumer 均可竞争。不得消费 S107–S109 的历史关闭结论。",
        "# HoTT 研究前沿（S127 统观双轨）\n\nS127 只改变统观工作线的职责、交换和汇合方式，不新增数学 claim：C-184–C-187 仍有效；ERCF-3 仍 `GATED`；T3 剩余义务不变。\n\n当前采用受控双轨。S 轨在主库从 L3 时间/运动结构、B 方向或固定真实 consumer 中选择一个同任务可反驳工作包；C11 v2 只作启发和审查，不作穷尽 Gate。M 轨在独立 machine-overview worktree 先关闭最新复审 P1/P2，取得 clean commit 与独立接受后，再优先扩展 L2/L6。两轨只通过冻结 TaskSpec、候选和 run 证据包阶段汇合；不得消费 S107–S109 的历史关闭结论，也不得把当前 M1 `REQUEST_CHANGES` 写成已接受。",
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\nS125：",
        "## 当前停止点\n\nS127：统观工作组织已定为受控双轨与阶段汇合。S 轨留在主库继续语义/研究统观，下一项优先 L3 时间/运动、B 方向或固定真实 consumer；M 轨留在独立 worktree，当前以最新 `REQUEST_CHANGES` 复审为基线先修 P1/P2，Gate A 通过后优先扩展 L2/L6。两轨不共写 current truth，以冻结 TaskSpec/候选/run 包经 Gate B 汇合；Gate C 前不讨论整体接管。外部设计、handoff 和复审已按字节导入 `audit/imports/machine-overview-strategy-20260913/`。无新数学 claim。\n\nS125：",
    )

    state["revision"] = 127
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_DUAL_TRACK_COORDINATION_DECISION"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "S track: freeze one same-task falsifiable package from L3 time/motion, B-direction delivery, or a concrete consumer. "
        "M track remains external: close the latest M1 P1/P2 findings, produce a clean commit and independent acceptance before L2/L6 expansion. "
        "No machine candidate enters current truth before Gate B; ERCF-3 remains GATED."
    )
    state["projection"]["status"] = STATUS

    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260913-direction-109"
    direction_record["semantic_status"] = STATUS
    direction_record["scope"] = (
        "Dual-track portfolio after S127: S track owns semantic/research overview in main; M track owns the external machine-overview instrument. "
        "They exchange frozen task/evidence packets and converge through Gate A/B/C. C11 coordinates remain non-gating; ERCF-3 remains gated."
    )
    add_once(direction_record["full_sources"], DECISION)
    add_once(direction_record["full_sources"], IMPORT_MANIFEST)

    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record["projection_generation"] = "20260913-outcome-109"
    panorama_record["semantic_status"] = STATUS
    panorama_record["scope"] = (
        "Panorama after S127 records the dual-track decision and the machine-overview evidence boundary: complete M0-M5 proposal, real L1 M0/M1 calibration, "
        "latest independent REQUEST_CHANGES, active uncommitted repair, no integration and no new mathematical claim."
    )
    add_once(panorama_record["full_sources"], DECISION)
    add_once(panorama_record["full_sources"], IMPORT_MANIFEST)

    state["records"][RESULT_ID] = {
        "classification": "DUAL_TRACK_STAGED_CONVERGENCE",
        "decision_status": "USER_DELEGATED_CURRENT_DECISION",
        "depends_on": [],
        "evidence_status": "DOCUMENTED",
        "full_sources": [
            DECISION,
            IMPORT_MANIFEST,
            IMPORTED_PLAN,
            IMPORTED_METHOD,
            IMPORTED_HANDOFF,
            IMPORTED_AUDIT,
            FIRST_REPORT,
            TAKEOVER_REPAIR,
        ],
        "kind": "coordination_decision",
        "lifecycle_status": "CURRENT",
        "path": DECISION,
        "related_records": [
            "A-THEORY-ECONOMY-LEDGER-001",
            "A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001",
            SESSION_ID,
        ],
        "scope": (
            "Current organization of the first semantic/research overview and the second machine-overview workline. "
            "Keep independent generation and worktree ownership; exchange immutable task/evidence packets; Gate A controls tool integration, Gate B result promotion, "
            "and Gate C any reconsideration of broad takeover. Machine M0/M1 is not accepted at the audited 2705847 snapshot; active dirty repairs are not evidence. No new math claim."
        ),
        "source_hashes": {
            rel: R.sha((ROOT / rel).read_bytes())
            for rel in [DECISION, IMPORT_MANIFEST, IMPORTED_PLAN, IMPORTED_METHOD, IMPORTED_HANDOFF, IMPORTED_AUDIT]
        },
        "status": "complete",
    }
    for record_id in ["A-THEORY-ECONOMY-LEDGER-001", "A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001"]:
        add_once(state["records"][record_id].setdefault("related_records", []), RESULT_ID)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    main_head = git_head(ROOT)
    session = f"""# {SESSION_ID}

- 触发：用户要求评估第一次统观线与另一个 AI 的第二次系统化机器统观应整体交接、合并还是独立推进。
- 对象：主库 `{main_head}` / revision 126；机器 worktree 稳定 HEAD `2705847`、实现 commit `56c4306`；外部 M0–M5 方案、M1 handoff 和最新复审。
- 现场：2026-09-13T16:34:11Z 机器 worktree 有 6 个 tracked 实现文件修改及 untracked v2 profile/task/grammar/legacy；未写入、未运行、未把 dirty 当证据。
- 结论：受控双轨、阶段汇合。S 轨留主库；M 轨留独立 worktree；冻结 TaskSpec/候选/run 包交换；Gate A/B/C 分别控制工具集成、结果吸收和职责变化。
- 导入：外部 16 份 Markdown 按字节复制到 `{IMPORT_ROOT}/`，`IMPORT.json` 固定来源、字节和 SHA-256。
- 没有：不修改机器 worktree、不合并分支、不 push/tag、不启动数学研究、不新增数学 claim。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "main_baseline": main_head,
            "machine_stable_head": "2705847db5893bbbdfae21abb58c5a01beff6e27",
            "machine_implementation_commit": "56c4306",
            "machine_audit_status": "REQUEST_CHANGES",
            "machine_dirty_observed_at_utc": "2026-09-13T16:34:11Z",
            "external_import": {
                "manifest": IMPORT_MANIFEST,
                "files": 16,
                "byte_comparison": "PASS_BEFORE_CHECKPOINT",
            },
            "decision": "DUAL_TRACK_STAGED_CONVERGENCE",
            "new_math_claims": [],
            "machine_worktree_mutation": "NONE",
            "merge": "NOT_PERFORMED_GATE_A_NOT_MET",
            "push": "NOT_AUTHORIZED",
            "tag": "NOT_CREATED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "DOCUMENTED",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, DECISION, IMPORT_MANIFEST],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, RESULT_ID],
        "scope": "Evaluation and persistent coordination decision for the two overview worklines; no machine-worktree mutation and no mathematical research.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text(ROOT)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "The user delegated the decision whether the first overview workline and the second machine-overview workline should merge, hand off, or remain separate. "
            "Record the selected dual-track staged-convergence decision and its evidence, without mutating or merging the active machine worktree."
        ),
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
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 127,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
