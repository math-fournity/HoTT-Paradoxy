#!/usr/bin/env python3
"""Prepare revision 130: make main the sole work surface and persist the computability/literature audit."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260914-130-COMPUTABILITY-CONTINUITY-LITERATURE-AUDIT"
PREV = "S-GOV-20260913-129-DUAL-TRACK-COMMUNICATION-CONTRACT"
STATUS = "CORE_GENERATION_4_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY"
PLAN = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md"
PLAN_SHARD = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
IMPORT = "audit/imports/machine-overview-computability-20260914/IMPORT.json"
DECISION = "docs/decisions/统观单工作面与主库连续性决策-20260914.md"
OLD_DECISION = "docs/decisions/统观双轨协作与阶段汇合决策-20260913.md"
CONTRACT = "docs/design/detailed/统观双轨AI通信与证据交换合同-20260913.md"
EXTERNAL_PLAN = "外部资料/在 HoTT 中寻找“不可停机—不完备性边界”的研究方案：从计算性限制到 Gödel 型自指的可执行路线.md"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
AUDIT_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
DECISION_ID = "A-MACHINE-OVERVIEW-SINGLE-WORK-SURFACE-DECISION-001"
OLD_DECISION_ID = "A-MACHINE-OVERVIEW-DUAL-TRACK-DECISION-001"
OLD_CONTRACT_ID = "A-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT-001"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s130", RUNTIME_PATH)
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


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": ("DEEPENED", "三问中的‘怎么找/凭什么’已落为可计算性实现阶梯、文献分母和有界完备性审计。"),
        "KC-000002": ("DEEPENED", "Theory Schema 通过八轴规划和 exact HoTT calculus 缺口进入当前队列。"),
        "KC-000007": ("DEEPENED", "AI 提案与一手全文、机器 oracle、holdout 分离；不能用模型记忆冒充学术覆盖。"),
        "KC-000010": ("ALIGNED", "R0–R5 分层保持现实相对目标与内部矛盾不同；现实桥梁仍 OPEN。"),
        "KC-000012": ("DEEPENED", "ASK 被具体化为 proof checking、proof search、halting、decidability 与 representability 的资格链。"),
        "KC-000013": ("DEEPENED", "理论对象到总求解能力的提升由 R2/R3/R4 分开，不以 timeout 替代。"),
        "KC-000014": ("ALIGNED", "方向 B 保留为 proof-to-solver、partial-to-total 等能力越级；本轮没有宣称实例已找到。"),
        "KC-000017": ("DEEPENED", "发现现有 41 条文献地图的训练先验/作者聚类盲区，并以 2024–2026 一手来源反查。"),
        "KC-000021": ("ALIGNED", "worktree proof 仅作为 contributor evidence 导入身份；main 数学结论仍须 F-011。"),
        "KC-000022": ("ALIGNED", "A/B 与计算/不完备分层继续保留，未把一般不可判定性写成目标悖论。"),
        "KC-000024": ("DEEPENED", "固定程序发散、统一不可判定、proof-search 半判定和 Gödel 独立句进入不同程序工作包。"),
        "KC-000025": ("DEEPENED", "自指线的慢点被定位为 universal code、strong separation 与 exact syntax，而非继续造小循环。"),
        "KC-000026": ("DEEPENED", "Groupoid-Syntax/2LTT/Extension Types 被列为 HoTT 自身语法与元层边界的必要新输入。"),
        "KC-000027": ("DEEPENED", "R1 已有候选机器证据；R2 通用计算与公平归约仍明确开放。"),
        "KC-000028": ("DEEPENED", "证明检查、证明搜索、反射和同层自担保被分成 R0–R4；没有把回环观察升级为发散定理。"),
        "KC-000029": ("DEEPENED", "理论经济高风险位置现在与 partiality、oracle modality、synthetic computability 文献交叉。"),
        "KC-000030": ("DEEPENED", "学术谱系成为理论经济与计算合法性共同的外部校准，而不是外部 worktree 私有记忆。"),
        "KC-000031": ("DEEPENED", "exact HoTT calculus 的覆盖/拒绝要用 syntax、conservativity 与 inner/outer 文献核验。"),
        "KC-000035": ("DEEPENED", "HoTT 能否表达本研究被拆为对象机、synthetic core、exact syntax 与现实 bridge 四层。"),
        "KC-000036": ("DEEPENED", "Gödel/不完备主线的已完成与未完成前提、最新学术缺口和下一机器节点已进入 main owner。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮回收计算合法性计划并审计学术覆盖，不新增数学 claim。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(kid, ("NOT_TOUCHED", f"本轮没有重新裁决“{label}”的数学、物理或哲学内容。"))
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{PLAN_SHARD}`；{kid} | "
            "R2、exact HoTT、现实桥梁与全面文献覆盖按本轮范围保持开放。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 本轮是项目治理/研究路线与来源覆盖裁定，不把一般操作指令加入 core。",
        "- direction_change: YES_IN_PLACE — 历史双轨关闭为 superseded；新增 main 单工作面计算合法性方向。",
        "- panorama_change: YES_IN_PLACE — 登记候选证据回收与文献覆盖不完整的有界审计结果。",
        "- essay_change: NO — AI 阐释层未改。",
        "- update_decision: main 为唯一 active write root；外部 machine worktree 为只读 contributor evidence source。",
        "- cross_conflicts: worktree 中有更晚数学候选，但尚未通过 main proof/source/run/index 集成；保持 candidate。",
        "- unresolved: 19 个 FULL_TEXT_TO_READ、2024–2026 漏项、R2、exact HoTT syntax/representability、现实桥梁、代码集成与 Git version closure。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [PLAN, PLAN_SHARD, IMPORT, DECISION, OLD_DECISION, CONTRACT, EXTERNAL_PLAN, "feature-list.md", "rulings.md"]
    for rel in required:
        if not (ROOT / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 129 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_129_S129")
    for record_id in [PLAN_ID, AUDIT_ID, DECISION_ID, SESSION_ID]:
        if record_id in state["records"]:
            raise SystemExit(f"RECORD_ALREADY_EXISTS:{record_id}")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK`",
        "| `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK` | 历史双轨统观：两个 active writer 分处主库与 machine worktree，以冻结 TaskSpec/证据包阶段汇合 | 用户 2026-09-13 的双 AI 现场；rulings §20–§21 | `CLOSED_WITH_SCOPE / SUPERSEDED_BY_SINGLE_WORK_SURFACE` | `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-MACHINE-OVERVIEW-DUAL-TRACK-DECISION`、`OUT-TOP-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT` | 只有再次出现多个 active writer 时，按 2026-09-14 新决定重核后才复活旧合同；旧 task/ACK/HEAD 不自动有效 | `docs/decisions/统观双轨协作与阶段汇合决策-20260913.md`；`docs/decisions/统观单工作面与主库连续性决策-20260914.md` |",
    )
    projection_edit.append_to_shard(
        direction,
        direction_shard,
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 为唯一工作面推进基于计算合法性/不可停机代码的 HoTT 悖论探索；把文献、计划和候选证据先回收到项目治理，再完成 R2、exact HoTT Gödel 与现实桥梁 | 用户 2026-09-14 当前指令；rulings §22；F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-COMPUTABILITY-CONTINUITY-AUDIT` | 先完成 `LIT-DENOMINATOR-001` 与 19 条全文缺口，和 `R2-PROGRAMCODE-001`/`R2-FAIR-001` 交替推进；再用最新 HoTT syntax/modalities 文献固定 `G-HOTT-SYNTAX-001` | 项目程序化探索规划第 006 片；`audit/imports/machine-overview-computability-20260914/IMPORT.json`；单工作面决定 |",
    )
    for old, new in (
        ("版本：`integrated-direction-portfolio/v1.7`", "版本：`integrated-direction-portfolio/v1.8`"),
        ("状态：`CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT`", f"状态：`{STATUS}`"),
        ("source_state_revision: 129", "source_state_revision: 130"),
        ("projection_generation: 20260913-direction-111", "projection_generation: 20260914-direction-112"),
        ("semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_shard = "全景视野/002 - 治理、门禁与骨架结果.md"
    panorama["shards"][panorama_shard] = replace_line(
        panorama["shards"][panorama_shard],
        "| `OUT-TOP-MACHINE-OVERVIEW-DUAL-TRACK-DECISION`",
        "| `OUT-TOP-MACHINE-OVERVIEW-DUAL-TRACK-DECISION` | 历史双轨与阶段汇合决定 | `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK`、`DIR-TOP-THEORY-ECONOMY-LEDGER` | 2026-09-13 双 AI 现场 | `DOCUMENTED / HISTORICAL / SUPERSEDED_FOR_CURRENT_TOPOLOGY` | 保留多 writer 时的职责、冻结交换包与 Gate A/B/C | 不能继续说明 2026-09-14 当前执行拓扑；不证明 machine 实现或数学被 main 接受 | `docs/decisions/统观双轨协作与阶段汇合决策-20260913.md`；单工作面决定 |",
    )
    panorama["shards"][panorama_shard] = replace_line(
        panorama["shards"][panorama_shard],
        "| `OUT-TOP-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT`",
        "| `OUT-TOP-MACHINE-OVERVIEW-COMMUNICATION-CONTRACT` | 历史三 worktree 双通道通信合同 | `DIR-TOP-MACHINE-OVERVIEW-DUAL-TRACK` | 2026-09-13 Git/Codex App 现场 | `DOCUMENTED / HISTORICAL / NO_CURRENT_HANDSHAKE_REQUIRED` | 多 writer 再出现时可重核后复用控制/证据分离 | 旧 task ID、ACK 与 HEAD 不自动有效；当前单 writer 不需握手 | `docs/design/detailed/统观双轨AI通信与证据交换合同-20260913.md`；单工作面决定 |",
    )
    projection_edit.append_to_shard(
        panorama,
        panorama_shard,
        "| `OUT-TOP-COMPUTABILITY-CONTINUITY-AUDIT` | 主项目回收 machine-overview 的不可停机/Gödel计划、文献地图、完备性审计与 handoff，并审计从经典到 2026 的实际覆盖 | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-TOP-THEORY-ECONOMY-LEDGER` | 用户当前指令 + main/worktree直接证据 + 2026-09-14 一手来源检索 | `DOCUMENTED / CANDIDATE_EVIDENCE_IMPORTED / LITERATURE_COVERAGE_INCOMPLETE` | byte-identical import 使未来 Session 不依赖外部 worktree；41 条文献状态重算为 19 `FULL_TEXT_TO_READ`、5 primary PDF topics、10 experiment-mapped；R1 contributor proof、R2/R4/现实桥梁分层明确；2024–2026 关键漏项已具名 | 不把 import 升格为 main 数学证明；不证明文献全覆盖；不证明 HoTT 不完备或非现实性悖论 | 项目程序化探索规划第 006 片；`audit/imports/machine-overview-computability-20260914/IMPORT.json`；外部方案 |",
    )
    for old, new in (
        ("版本：`integrated-outcome-panorama/v1.7`", "版本：`integrated-outcome-panorama/v1.8`"),
        ("状态：`CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT`", f"状态：`{STATUS}`"),
        ("source_state_revision: 129", "source_state_revision: 130"),
        ("projection_generation: 20260913-outcome-111", "projection_generation: 20260914-outcome-112"),
        ("semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory["index_text"] = replace_once(memory["index_text"], "当前执行队列（2026-09-13）", "当前执行队列（2026-09-14）")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][memory_shard] = replace_once(memory["shards"][memory_shard], "## 当前执行队列（2026-09-13）", "## 当前执行队列（2026-09-14）")
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "2. 当前统观采用",
        "2. 用户已明确当前只有本 AI 在主项目工作；统观从历史双轨切换为**主项目单工作面**。`/Volumes/D/HoTT_AI_HANDOFF_20260911` main 是唯一 active write root/current-truth owner；`/Volumes/D/HoTT-machine-overview` 降为只读候选实现/证据来源。旧双轨决定和通信合同保留为历史与未来多 writer 复用条件，不再进入 current queue。",
    )
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "3. M 轨任务",
        "3. 项目级程序化探索规划现为 v2 index + 6 shards；第 006 片把不可停机/Gödel动态状态、用户指定 1115 行外部方案、41 条文献分母和 2024–2026 已确认遗漏带回主项目。当前判词：R1 固定对象程序发散有 contributor 机器证据；R2 通用不可判定未完成；conditional synthetic incompleteness core 与作者 Coq `Q` 重放不等于 exact HoTT calculus；学术文献 U0 `IN_PROGRESS`，不能声称从 Turing 到最近研究全面覆盖。",
    )
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "8. 版本链以",
        "8. 当前优先顺序：`LIT-DENOMINATOR-001`（冻结 1931–2026 文献检索分母）→ `LIT-CLASSICS-001`/`LIT-HOTT-COMPUTABILITY-001`（全文补齐）与 `R2-PROGRAMCODE-001`/`R2-FAIR-001`（通用对象机）交替推进 → `G-HOTT-SYNTAX-001`。外部分支代码/proof/run 只有经 main 独立核验和正式集成才改变数学状态；不 push、不 tag。",
    )
    evidence_shard = "MEMORY/002 - 当前证据上限与恢复入口.md"
    memory["shards"][evidence_shard] = replace_once(memory["shards"][evidence_shard], "模型对三件套的实际理解", "模型对四件套的实际理解")
    memory["shards"][evidence_shard] = replace_once(
        memory["shards"][evidence_shard],
        "- 数学结论若没有 repo 内匹配语义的 proof source、kernel run 和 claim index，只能保持 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/COUNTEREXAMPLE_CANDIDATE/SOURCE_REPORTED_NOT_REPLAYED`。",
        "- 数学结论若没有 repo 内匹配语义的 proof source、kernel run 和 claim index，只能保持 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/COUNTEREXAMPLE_CANDIDATE/SOURCE_REPORTED_NOT_REPLAYED`。\n- 可计算性主线目前只有 R1 固定程序发散的 contributor proof、条件性 synthetic incompleteness core 与外部 Coq `Q` 重放；R2 universal halting undecidability、R4 exact HoTT calculus、HoTT essentiality 和现实桥梁均开放。机器统观 41 条文献表中 19 条待全文，深读 cache 仅五个主题，且遗漏 2024–2026 的 Oracle Modalities、Post hierarchy、ordinal decidability、groupoid-syntax 等直接相关工作；学术全面覆盖未成立。",
    )
    memory["shards"][evidence_shard] = replace_once(
        memory["shards"][evidence_shard],
        "## 恢复入口\n\n",
        "## 恢复入口\n\n按根 AGENTS 全文加载 core→direction→panorama→思想展开四件套。机器统观/完备性/计算合法性任务还要全文读取 `.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md` 的 index 与全部 shards，优先读第 006 片和 `audit/imports/machine-overview-computability-20260914/IMPORT.json`；不依赖外部 worktree 才能恢复当前判词。下段既有 stable-record 路由继续有效，但不能覆盖这项新入口。\n\n",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S130 计算合法性主线回收与学术覆盖审计：用户确认 main 是唯一 active work surface；外部 machine worktree 降为只读候选来源。按字节导入动态计划、完备性审计、literature README/PDF manifest 与 handoff；项目程序化探索规划增至 6 片。41 条 LIT 分母中 19 条仍待全文、5 个 primary PDF 主题已深读、10 条 experiment-mapped；本轮确认 2017 Dominances、2024 Oracle Modalities/Post hierarchy、2025 synthetic computability 总览/cubical cofibration complexity、2026 ordinal decidability/groupoid-syntax/Extension Types 及 Agda Gödel 等关键漏项。R1 仅为 contributor evidence；R2、exact HoTT、现实桥梁和文献全面覆盖保持 OPEN。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    marker = "本文件是注意力槽"
    if marker not in frontier:
        raise SystemExit("FRONTIER_MARKER_MISSING")
    tail = marker + frontier.split(marker, 1)[1]
    frontier = (
        "# HoTT 研究前沿（S130 主项目单工作面与计算合法性）\n\n"
        "S130 改变工作面与研究准备状态，不新增数学 claim。main 现在是唯一 active write root/current-truth owner；外部 machine-overview 只作候选实现与证据来源。\n\n"
        "当前第一工作包为 `LIT-DENOMINATOR-001`：冻结 1931–2026 的经典、类型论、HoTT/cubical 和机器化文献分母；随后让 `LIT-CLASSICS-001`/`LIT-HOTT-COMPUTABILITY-001` 与 `R2-PROGRAMCODE-001`/`R2-FAIR-001` 交替推进。R1 固定程序发散仅有 contributor 证据；R2 universal halting undecidability、exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。\n\n"
        + tail
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS130：用户确认 main 是唯一 active work surface；外部 machine worktree 降为只读候选来源。主项目已导入不可停机/Gödel计划、完备性审计、文献 manifest 与 handoff，并在项目程序化探索规划第 006 片记录 R0–R5、41 条文献分母、19 条待全文及 2024–2026 关键漏项。当前下一步=`LIT-DENOMINATOR-001`，与 R2 ProgramCode/fairness 交替推进。分支数学仍是 candidate，未进入 main F-011。\n\n",
    )

    state["revision"] = 130
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_SINGLE_WORK_SURFACE_COMPUTABILITY_CONTINUITY"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Run LIT-DENOMINATOR-001 in main: freeze the 1931-2026 source/venue/query denominator, then close current FULL_TEXT_TO_READ items while R2-PROGRAMCODE-001 and R2-FAIR-001 form the universal-machine thin path."
    )
    state["projection"]["status"] = STATUS

    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260914-direction-112"
    direction_record["semantic_status"] = STATUS
    for rel in [PLAN, PLAN_SHARD, IMPORT, DECISION]:
        add_once(direction_record["full_sources"], rel)
    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record["projection_generation"] = "20260914-outcome-112"
    panorama_record["semantic_status"] = STATUS
    for rel in [PLAN, PLAN_SHARD, IMPORT, DECISION]:
        add_once(panorama_record["full_sources"], rel)

    old_decision = state["records"][OLD_DECISION_ID]
    old_decision["lifecycle_status"] = "HISTORICAL"
    old_decision["evidence_status"] = "DOCUMENTED / SUPERSEDED_FOR_CURRENT_TOPOLOGY"
    old_decision["resolution"] = {
        "reason": "The user confirmed on 2026-09-14 that only one active writer remains and directed main-project governance to own continuity; the two-writer topology is superseded, while its historical gates remain available if multiple writers recur.",
        "evidence": [DECISION, "rulings.md", IMPORT],
    }
    old_decision["source_hashes"][OLD_DECISION] = R.sha((ROOT / OLD_DECISION).read_bytes())
    add_once(old_decision.setdefault("related_records", []), DECISION_ID)
    old_decision["revalidation"] = (old_decision.get("revalidation", "") + f" {SESSION_ID} records that the two-active-writer premise ended; the decision remains historical and is superseded by {DECISION} for current topology.").strip()
    old_contract = state["records"][OLD_CONTRACT_ID]
    old_contract["lifecycle_status"] = "HISTORICAL"
    old_contract["evidence_status"] = "DOCUMENTED / NO_CURRENT_HANDSHAKE_REQUIRED"
    old_contract["resolution"] = {
        "reason": "No inter-agent handshake is needed while main has the only active writer. The contract remains historical and can be re-qualified if multiple active worktrees recur.",
        "evidence": [DECISION, "rulings.md"],
    }
    old_contract["source_hashes"][OLD_DECISION] = R.sha((ROOT / OLD_DECISION).read_bytes())
    add_once(old_contract.setdefault("related_records", []), DECISION_ID)
    old_contract["revalidation"] = (
        f"{SESSION_ID} reclassified this contract as historical because the user confirmed a single active writer; no SENT/ACKED state is carried forward, and reuse requires fresh worktree/task qualification."
    )

    plan_shards = [
        f".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/{n:03d} - {name}.md"
        for n, name in [
            (1, "完备性目标、边界与覆盖包络"),
            (2, "HoTT构造与程序化激发算子全景"),
            (3, "生成器、执行器与判据组合"),
            (4, "开放世界未知、反遗漏与自扩展机制"),
            (5, "阶段路线、验收与当前缺口"),
            (6, "计算合法性主线与学术谱系覆盖审计"),
        ]
    ]
    plan_sources = [PLAN] + plan_shards + [IMPORT, DECISION, "scripts/audit/test_hott_programmatic_exploration_completeness.py"]
    state["records"][PLAN_ID] = {
        "classification": "PROGRAMMATIC_EXPLORATION_COMPLETENESS_ENVELOPE",
        "depends_on": [],
        "evidence_status": "DOCUMENTED / MECHANICALLY_VERIFIED_WITH_SCOPE",
        "full_sources": plan_sources,
        "kind": "research_governance_plan",
        "lifecycle_status": "CURRENT",
        "path": PLAN,
        "related_records": [AUDIT_ID, DECISION_ID, SESSION_ID],
        "scope": "Project-local eight-axis, 14-construct, 14-operator, six-generator and seven-ingress exploration envelope with bounded/fair/reduction completeness semantics. It is a research method, not proof that a HoTT paradox exists.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in plan_sources if (ROOT / rel).is_file()},
        "status": "active",
    }
    state["records"][AUDIT_ID] = {
        "classification": "COMPUTABILITY_AND_LITERATURE_COVERAGE_INCOMPLETE",
        "depends_on": [],
        "evidence_status": "DOCUMENTED / BOUNDED_AUDIT",
        "full_sources": [PLAN_SHARD, IMPORT, EXTERNAL_PLAN, DECISION],
        "kind": "research_coverage_audit",
        "lifecycle_status": "OPEN_ISSUE",
        "path": PLAN_SHARD,
        "related_records": [PLAN_ID, DECISION_ID, SESSION_ID],
        "scope": "Current R0-R5 computability status and literature denominator audit: 41 mapped entries, 19 FULL_TEXT_TO_READ, five downloaded primary-paper topics, ten experiment mappings, and named 2017/2024-2026 omissions. R2, exact HoTT, reality bridge and comprehensive literature coverage remain open.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in [PLAN_SHARD, IMPORT, EXTERNAL_PLAN, DECISION]},
        "status": "review_required",
    }
    state["records"][DECISION_ID] = {
        "classification": "SINGLE_MAIN_WORK_SURFACE_WITH_IMPORTED_CANDIDATE_EVIDENCE",
        "depends_on": [],
        "evidence_status": "DOCUMENTED / IMPORT_HASH_VERIFIED",
        "full_sources": [DECISION, IMPORT, PLAN, PLAN_SHARD, "feature-list.md", "rulings.md"],
        "kind": "coordination_decision",
        "lifecycle_status": "CURRENT",
        "path": DECISION,
        "related_records": [OLD_DECISION_ID, OLD_CONTRACT_ID, PLAN_ID, AUDIT_ID, SESSION_ID],
        "scope": "Main is the only active write root/current-truth owner; the machine-overview worktree is a read-only contributor evidence source. Candidate documents are imported byte-identically, while code/math acceptance remains separate.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in [DECISION, IMPORT, PLAN, PLAN_SHARD, "feature-list.md", "rulings.md"]},
        "status": "complete",
    }
    for list_name in ["review_due", "unresolved"]:
        add_once(state[list_name], AUDIT_ID)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户问题：可计算性/计算合法性机器统观准备到什么程度，是否全面覆盖 Turing 至当前学术研究，且是否吸收指定 1115 行外部方案。
- 用户后续裁定：现在只有本 AI 在主项目工作；连续性必须由 main 的治理资产承担，不能把决定性内容只留在外部 worktree。
- 结论：外部方案已实际吸收；R1 有 contributor 机器证据，R2/精确 HoTT/现实桥梁开放；41 条文献表有 19 条待全文、五个 primary-paper 主题深读、十个 experiment mapping，未达到全面覆盖。
- 新发现：2017 Dominances、2021 Parametric CT、2024 Oracle Modalities/Post hierarchy、2025 synthetic computability overview/cubical cofibration complexity、2026 ordinal decidability/groupoid-syntax/Extension Types，以及 Agda Gödel/Lean Foundation 等未进入 current LIT 表。
- 连续性：按字节导入五份 machine-overview current documents；项目规划新增第 006 片；Feature/MEMORY/rulings/decision/direction/panorama/STATE 原位收敛。
- 证据边界：worktree formal/run 未合并；无新数学 claim；不 push/tag。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "main": {"root": str(ROOT), "branch": "main", "starting_head": "2bbf5c873dfa3ac1d512955301b163b2b6f311b0"},
        "source_worktree": {"root": "/Volumes/D/HoTT-machine-overview", "branch": "feat/machine-overview-m1", "head": "1aa1a6e32c0f59459f79ebc76f74e8f2b5be97a5", "role": "READ_ONLY_CANDIDATE_SOURCE"},
        "import": {"manifest": IMPORT, "files": 5, "cmp": "PASS", "evidence_boundary": "CANDIDATE_NOT_CURRENT_MATHEMATICS"},
        "literature_denominator": {"rows": 41, "full_text_to_read": 19, "primary_pdf_topics": 5, "experiment_mapped": 10, "formal_dependencies": 7, "coverage": "INCOMPLETE"},
        "computability": {"R1": "CONTRIBUTOR_MACHINE_EVIDENCE", "R2": "OPEN", "R3": "CONDITIONAL_CORE_PLUS_EXTERNAL_Q_REPLAY", "R4": "OPEN", "R5": "NO_EVIDENCE"},
        "new_math_claims": [],
        "push": "NOT_PERFORMED",
        "tag": "NOT_CREATED"
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "DOCUMENTED / BOUNDED_AUDIT",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, PLAN, PLAN_SHARD, IMPORT, DECISION],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, PLAN_ID, AUDIT_ID, DECISION_ID],
        "scope": "Single-work-surface transition, computability readiness audit, literature coverage audit and main-project cognition import; no mathematical claim acceptance.",
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
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "The user stated that only this AI now works in the main project and directed the project governance framework to own cross-session continuity instead of leaving decisive content only in the external worktree.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 130, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
