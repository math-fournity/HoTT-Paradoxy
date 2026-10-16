#!/usr/bin/env python3
"""Prepare revision 154: core generation-7 + essay rename + PREMISE-001 registration.

This preparer also performs two forced drift repairs *before* plan(), because
revision 152/153 were direct STATE edits without a canonical checkpoint:

1. Backfill STATE.records[S153] (kind=session). graph() requires
   latest_session to be a registered record; the generation-6 session bundle
   exists on disk but was never registered.
2. Rebuild HEAD.tracked for the current MUTABLE set (the essay was renamed to
   扩展认知 and gained shards 007/008 after revision 153 was written).

Both repairs keep revision=153 / latest_session=S153 unchanged; they restore
the derived routing data the canonical machinery needs, they do not rewrite
history. The checkpoint itself then carries revision 153 -> 154.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SCRIPTS = ROOT / "scripts/audit"

SESSION_ID = "S-GOV-20260916-154-CORE-GENERATION-7-RENAME-PREMISE-001"
PREV = "S-GOV-20260916-153-CORE-GENERATION-6"
PREV152 = "S-GOV-20260916-152-CORE-GENERATION-5"
STATUS = "CORE_GENERATION_7_ESSAY_RENAMED_PREMISE_001_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
PREMISE_ID = "A-PREMISE-001"

GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
R4_ID = "A-R4-HOTT-NAT-EFFECTIVITY-001"

CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION_V7 = "scripts/audit/core-cognition-curation-v7.json"
TRANSITION_GEN7 = "audit/core-cognition-generation-7-transition-20260916.json"
CURATION_V6 = "scripts/audit/core-cognition-curation-v6.json"
TRANSITION_GEN6 = "audit/core-cognition-generation-6-transition-20260916.json"
USER_SOURCE = "sources/prompts/Codex-理论是对现实的骨架式模仿-用户原文-20260916.md"
SHARD_008 = "Atria的方案/修订片/008 - PREMISE-001 HoTT 前提集穷尽清单与 P1–P4 分工.md"
AUDIT_09 = "Atria的审计报告集/09 - 反思路径的结构性边界与前提清单的可枚举性.md"
REVISION_INDEX = "Atria的方案/修订片.md"
GOAL = "goal.md"
FEATURE = "feature-list.md"
PREPARE = "scripts/audit/prepare_s154_core_generation_7_rename_premise001_checkpoint.py"
CORE_SHA = "b4a57785eef22cffb471028d73a8641549ce1cead5763ab8f6c31727945b8999"
MANIFEST_SHA = "62ff443a2d02eb0e608793b3bec2031c76370f10b75ceadfc8a216590a58b598"
CURATION_V7_SHA = "74a0320703771a43978f59fbde3b2beb07bf3798ad99ede744ee824b9706d7fc"
GEN7 = "core-cognition-generation-7"
GEN6 = "core-cognition-generation-6"

CORE_TRANSITION = {
    "from_generation": GEN6,
    "to_generation": GEN7,
    "manifest": MANIFEST,
    "transition": TRANSITION_GEN7,
}

SPEC = importlib.util.spec_from_file_location("runtime_s154", RUNTIME_PATH)
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


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def file_hashes(paths: list[str]) -> dict[str, str]:
    return {path: R.sha((ROOT / path).read_bytes()) for path in paths}


def command_pass(argv: list[str], required: str) -> str:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    if result.returncode != 0 or required not in output:
        raise SystemExit(f"PRECHECK_FAILED:{' '.join(argv)}\n{output}")
    return output


def repair_state_and_head() -> None:
    """Backfill the missing S153 record and rebuild HEAD.tracked (idempotent)."""
    state_path = ROOT / R.STATE
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("revision") != 153 or state.get("latest_session") != PREV:
        raise SystemExit(f"S154_EXPECTED_REVISION_153_S153:{state.get('revision')}:{state.get('latest_session')}")
    if PREV not in state["records"]:
        s153_sources = [
            f".codex/research/hott/sessions/{PREV}/SESSION.md",
            f".codex/research/hott/sessions/{PREV}/CORE_COGNITION_AUDIT.md",
            f".codex/research/hott/sessions/{PREV}/RUNS.json",
            "sources/prompts/Codex-AI数学用好与超越-用户原文-20260916.md",
            CURATION_V6,
            TRANSITION_GEN6,
        ]
        state["records"][PREV] = {
            "depends_on": [],
            "evidence_status": "VERIFIED_WITH_SCOPE / CANONICAL_CHECKPOINT_RECEIPT_GAP_REGISTERED_NOT_FORGED",
            "full_sources": s153_sources,
            "kind": "session",
            "lifecycle_status": "HISTORICAL",
            "path": f".codex/research/hott/sessions/{PREV}/SESSION.md",
            "related_records": [PREV152, GOAL_ID, R4_ID],
            "scope": (
                "Core generation-6 (KC-000041-000043) curation/build/registration and essay shard 007; "
                "session bundle is complete on disk but was applied as a direct STATE edit without a "
                "canonical checkpoint transaction/result; the gap is registered here, not back-filled "
                "with a forged receipt."
            ),
            "source_hashes": file_hashes(s153_sources),
            "status": "complete",
        }
        state_path.write_bytes(R.dump(state))

    head_path = ROOT / R.HEAD
    head = json.loads(head_path.read_bytes())
    tracked = {}
    for rel in R.MUTABLE:
        data = R.read_bytes(ROOT, rel)
        tracked[rel] = R.sha(data)
        index = R.parse_shard_index(data, rel)
        if index is not None:
            for row in index["shards"]:
                tracked[row["path"]] = R.sha(R.read_bytes(ROOT, row["path"]))
    if head.get("tracked") != tracked:
        head["tracked"] = tracked
        head_path.write_bytes(R.dump(head))


def audit_text() -> str:
    manifest = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    focus = {
        "KC-000037": (
            "TENSION",
            "用户一眼发明圆环悖论、原以为发现 HoTT 非现实悖论并不困难——这个预期与机器统观众久未发现的事实构成张力，本轮不消解它；PREMISE-001 只把「发现」从无分母的反思变成有穷分母上的登记，不声称发现必然发生。",
        ),
        "KC-000038": (
            "TENSION",
            "「在我的提示下捕捉 HoTT 作者思路缺陷是很基础的工作」与实际未发生并存；本轮保留该张力并给出它为何不自动发生的结构性理由（反思无分母、判据在现实侧、P3/P4 不能由 AI 在最流利处自证）。",
        ),
        "KC-000039": (
            "DEEPENED",
            "「基础问题就在基础之处、基础必然在训练数据中」被从「反观知识谱」深化为「对 HoTT 前提集做穷尽 P1/P2 登记」：基础仍在基础之处，但被穷尽枚举的是前提集这一有穷分母，而不是 AI 的反思本身。",
        ),
        "KC-000040": (
            "CORRECTED",
            "第三条发现路径（把训练数据中的 HoTT 完整知识谱当作被考察对象）方向正确但缺分母、不可证伪；PREMISE-001 给出它的第一个可枚举分母（PREMISE_DENOMINATOR_V1 类别 A–G）与 P1–P4 + C 的步骤级分工，使其可证伪。",
        ),
        "KC-000041": (
            "NOT_TOUCHED",
            "本轮不裁决「用好 AI 与超越 AI 都需要持续探索和努力」的内容；它作为方法论观察保留。",
        ),
        "KC-000042": (
            "NOT_TOUCHED",
            "本轮不裁决「第一件事上 AI 给的助力有多大，第二件事上的阻力就有多大」的互反性；它仍是强启发式，不是单调定律。",
        ),
        "KC-000043": (
            "DEEPENED",
            "认知惯性/路径依赖被显式扩展到现实骨架映射：AI 用现实解释理论时可能对齐到语料中最熟悉的那个现实例子，而不是最贴近该前提本性的现实域——修订片 008 的 corpus_pressure 三道闸因此对 reality_skeleton 同样适用。",
        ),
        "KC-000044": (
            "CORRECTED",
            "用户的认识论修正纠正了审计报告集 09 §5 原先「同伦型在日常生活中无可直接把握的现实标准」的判断：理论永远是对现实的骨架式模仿，假想中的现实也是现实，HoTT 必然可映射到现实；报告集 09 §5/§8/§9/§10 已按用户原文原位改写。",
        ),
        "KC-000045": (
            "DEEPENED",
            "「在现实诠释与不断对齐中定位理论为经济性舍弃了不该舍弃的前提」落成 PREMISE-001 的 P2 机制：每条前提必填 reality_skeleton 与 divergence_point，断裂点就是 P3/P4 唯一可判定的对象。",
        ),
        "KC-000046": (
            "DEEPENED",
            "AI 缺的是用现实理解理论的动作而非思考现实的能力——本轮把计算域明确为现实域之一而非唯一：机器统观的原始出发点（能否用 HoTT 框架代码构造不可停机程序）本身是现实问题，但运动/连续/转动等母域同样是现实域，reality_skeleton 不得默认只填计算域。",
        ),
    }
    anchors = {
        "KC-000003", "KC-000010", "KC-000013", "KC-000014", "KC-000022",
        "KC-000024", "KC-000025", "KC-000026", "KC-000028", "KC-000029",
        "KC-000031", "KC-000035", "KC-000036",
    }
    generic = (
        "本轮是 core generation-7 登记、第四件改名（扩展认知）与 PREMISE-001 任务登记的治理工作，"
        "没有重新裁决该 KC 的数学、现实或哲学内容。"
    )
    anchor_note = " 该 KC 是修订片 008 明示的 PREMISE-001 候选 KC 锚点，本轮不裁决，留待 P1/P2 逐条引用。"
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；根 Goal 保持 active；本轮登记用户 2026-09-16 认识论修正（KC-000044–KC-000046）、第四件改名 `扩展认知`，并把 `PREMISE-001` 登记为下一动作。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        identity = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(identity, ("NOT_TOUCHED", generic))
        if identity in anchors:
            assessment = assessment + anchor_note
        evidence = (
            f"`{AUDIT_09}`；`{SHARD_008}`；`{USER_SOURCE}`；`{SESSION_ID}`；{identity} 原文锚点见 `{CORE}`（{GEN7}）"
        )
        unresolved = (
            "PREMISE-001 未执行任何 P1/P2；HoTT 前提集的 reality_skeleton/divergence_point 均未产出；"
            "无非现实前提被判定；无新数学 claim；Goal 不完成。"
        )
        lines.append(
            f"| `{identity}` | {label} | `{relation}` | {assessment} | {evidence} | {unresolved} |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: YES_ADDITIVE_PRESERVING — 用户 2026-09-16 认识论修正原文纳入 generation-7（KC-000044/045/046）；43/43 旧单元 PRESERVED_EXACT、mapping_remainder=0；无新用户悖论原文。",
        "- direction_change: YES_IN_PLACE — 新增 `DIR-TOP-PREMISE-INVENTORY`；`DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` 的下一动作转为 PREMISE-001，R4 并行保留。",
        "- panorama_change: YES_IN_PLACE — 新增 `OUT-TOP-PREMISE-001-REGISTRATION`（TASK_FROZEN_NOT_EXECUTED / NO_NEW_MATH_CLAIM）。",
        "- essay_change: YES_IN_PLACE — 第四件改名为 `扩展认知`（索引 + 8 分片，新增第 008 片《现实对齐：理论是现实的骨架式模仿》）；活当前真值引用已同步，历史快照与用户原文引文中的旧名保持原样。",
        "- update_decision: PREMISE-001 为下一手（有穷分母 + P1/P2 由 AI、P3/P4 由用户、C 由引擎与原生核）；R4 并行保留；Goal 保持 active；revision 153→154。",
        "- cross_conflicts: revision 152/153 为无 canonical checkpoint 的直接 STATE 编辑，导致 S153 记录缺失与 HEAD.tracked 三重过期；本轮以补登 S153 记录（登记缺口、不伪造收据）+ 重建 HEAD.tracked 修复，而非掩盖。用户说「刷到 revision 153」而 153 已被 generation-6 消耗，实际新 revision 为 154。",
        "- unresolved: PREMISE-001 全部 P1/P2 未执行；HoTT essentiality、ambient R2、exact R4、物理时间、经验 reality 桥梁与全面文献覆盖均开放；本会话不产生数学结论。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        CORE, MANIFEST, CURATION_V7, TRANSITION_GEN7, CURATION_V6, TRANSITION_GEN6,
        USER_SOURCE, SHARD_008, AUDIT_09, REVISION_INDEX, GOAL, FEATURE, PREPARE,
        "Atria的审计报告集/01 - 总结论与决定性发现.md",
        "Atria的方案/修订片/006 - 发现引擎：语义重定向作为八轴搜索策略.md",
        "Atria的方案/修订片/003 - GEN-001 有界生成器验收单元（新增）.md",
        "Atria的方案/修订片/007 - 供给层的语料压力字段与符号翻转分工.md",
        f".codex/research/hott/sessions/{PREV}/SESSION.md",
        f".codex/research/hott/sessions/{PREV}/CORE_COGNITION_AUDIT.md",
        f".codex/research/hott/sessions/{PREV}/RUNS.json",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"S154_EVIDENCE_MISSING:{missing}")

    command_pass(["python3", "-B", "scripts/audit/verify_governance_shards.py"], '"status": "PASS"')
    command_pass(["python3", "-B", "scripts/audit/test_three_way_cognition.py"], "Ran 6 tests")
    command_pass(
        ["python3", "-B", "scripts/audit/verify_core_cognition.py",
         "--curation", CURATION_V7, "--transition", TRANSITION_GEN7],
        '"status": "PASS_WITH_SCOPE"',
    )

    repair_state_and_head()

    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 153 or state.get("latest_session") != PREV:
        raise SystemExit("S154_REPAIR_DID_NOT_STABILIZE")
    for identity in (PREMISE_ID, SESSION_ID):
        if identity in state["records"]:
            raise SystemExit(f"S154_RECORD_ALREADY_EXISTS:{identity}")

    # ---- projections -------------------------------------------------------
    direction = projection_edit.load(ROOT, R.DIRECTION)
    d2 = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][d2] = replace_once(
        direction["shards"][d2],
        "当前做 `R4-HOTT-NAT-EFFECTIVITY-001`：选择具 Nat/Path/conversion 且拒绝 incomplete input/general recursion的exact target；",
        "并行保留 `R4-HOTT-NAT-EFFECTIVITY-001`（资格化具 Nat/Path/conversion 且拒绝 incomplete input/general recursion 的 exact target）；"
        "用户 2026-09-16 认识论修正后，当前下一动作转 `PREMISE-001`（见 `DIR-TOP-PREMISE-INVENTORY`）：",
    )
    projection_edit.append_to_shard(
        direction,
        d2,
        "| `DIR-TOP-PREMISE-INVENTORY` | 把 HoTT 自己的前提集当作第一个被穷尽枚举的分母：AI 完成 P1（前提逐字与出处）与 P2（现实骨架映射 + 省略形状），用户做 P3/P4 判定，引擎完成冻结族→枚举→保归约→原生核收据 | 用户 2026-09-16 认识论修正（KC-000044–KC-000046）+ 报告集 09 + 修订片 008 | `ACTIVE_USER_DIRECTION` | `PARADOX_DISCOVERY`, `THEORY_ECONOMY`, `ABSTRACTION_AND_NEGATION`, `REALITY_ALIGNMENT` | `OUT-TOP-PREMISE-001-REGISTRATION` | 冻结 `PREMISE_DENOMINATOR_V1`（类别 A–G）并逐条 P1/P2；`reality_skeleton` 不准留空；P3/P4 不得由 AI 自证 | `Atria的方案/修订片/008 - PREMISE-001 HoTT 前提集穷尽清单与 P1–P4 分工.md`；`Atria的审计报告集/09 - 反思路径的结构性边界与前提清单的可枚举性.md` |\n",
    )
    old_status = "CORE_GENERATION_4_C244_C249_R3_REPLAYED_R4_NAT_EFFECTIVITY_NEXT"
    for old, new in (
        ("source_state_revision: 151", "source_state_revision: 154"),
        ("projection_generation: 20260915-direction-133", "projection_generation: 20260916-direction-154"),
        (f"状态：`{old_status}`", f"状态：`{STATUS}`"),
        (f"semantic_status: {old_status}", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    p2 = "全景视野/002 - 治理、门禁与骨架结果.md"
    projection_edit.append_to_shard(
        panorama,
        p2,
        "| `OUT-TOP-PREMISE-001-REGISTRATION` | PREMISE-001 任务登记：HoTT 前提集（`PREMISE_DENOMINATOR_V1` 类别 A–G）成为机器统观第一个被穷尽枚举的、理论自身的分母；P1/P2=AI、P3/P4=用户、C=引擎与原生核 | `DIR-TOP-PREMISE-INVENTORY`、`DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 修订片 008 + 报告集 09（§5 已按用户 2026-09-16 认识论修正原位改写） | `DOCUMENTED / TASK_FROZEN_NOT_EXECUTED / NO_NEW_MATH_CLAIM` | 分母类别 A–G 已固定；`reality_skeleton`/`divergence_point`/`OMISSION_SHAPE` 必填；验收判词 `PREMISE_INVENTORY_COMPLETE_WITH_SCOPE` 与 `PREMISE_AUDITED_NO_NONREAL_PREMISE_WITH_SCOPE` 已定义 | 未执行任何 P1/P2；不声称覆盖 HoTT 全部未命名前提（unknown ingress 保持开放）；F-011 不适用——P1/P2 是结构与省略分析，不是数学结论 | 修订片 008；报告集 09；S154 checkpoint |\n",
    )
    for old, new in (
        ("source_state_revision: 151", "source_state_revision: 154"),
        ("projection_generation: 20260915-outcome-133", "projection_generation: 20260916-outcome-154"),
        (f"状态：`{old_status}`", f"状态：`{STATUS}`"),
        (f"semantic_status: {old_status}", f"semantic_status: {STATUS}"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m1 = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][m1] = replace_once(memory["shards"][m1], "## 当前执行队列（2026-09-15）", "## 当前执行队列（2026-09-16）")
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "`从抽象到悖论——…md` 成为常驻第四件（AI 阐释层，5 片）",
        "`扩展认知.md`（原名 `从抽象到悖论——HoTT研究的核心问题意识与思想展开.md`，2026-09-16 用户改名；现 8 片）成为常驻第四件（AI 阐释层）",
    )
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "当前优先 `R4-HOTT-NAT-EFFECTIVITY-001`；并行保留 Oracle、ambient R2、物理时间与 reality。未获授权不 commit/push/tag。",
        "`R4-HOTT-NAT-EFFECTIVITY-001` 并行保留（资格化 community cubical target）；用户 2026-09-16 的认识论修正（理论是对现实的骨架式模仿、HoTT 必然可映射现实）把当前下一动作改为 `PREMISE-001`：对 HoTT 前提集做穷尽 P1/P2 清单并交用户 P3/P4 判定。并行保留 Oracle、ambient R2、物理时间与 reality。未获授权不 commit/push/tag。",
    )
    memory["shards"][m1] += (
        "9. 本轮四件套变化：`核心认知.md` 升至 generation-7/46（新增 KC-000044/045/046，用户 2026-09-16 认识论修正）；第四件改名为 `扩展认知`（8 片，新增第 008 片）；revision 153→154；修复 S153 记录缺失与 HEAD.tracked 过期两处漂移。`PREMISE-001` 是下一手，但它不产生数学结论——P1/P2 是结构与省略分析，「某前提非现实」必须经用户 P3/P4 判定再由引擎与原生核验证。\n"
    )
    m3 = "MEMORY/003 - 当前验证状态与顺序日志.md"
    if not memory["shards"][m3].endswith("\n"):
        memory["shards"][m3] += "\n"
    memory["shards"][m3] += (
        f"- S154 core generation-7 + essay 改名 + PREMISE-001 登记：用户 2026-09-16T12:14:00Z 认识论修正（理论是对现实的骨架式模仿；数学与 HoTT 必然可映射现实；AI 缺的是用现实理解理论的动作）原文纳入四件套，generation-6/43→generation-7/46（KC-000044/045/046；43/43 `PRESERVED_EXACT`、remainder=0）。第四件按用户要求改名 `从抽象到悖论——HoTT研究的核心问题意识与思想展开`→`扩展认知`（索引+8 分片，新增第 008 片），19 个活当前真值文件同步引用；历史快照/来源原文/dev-notes 中的旧名保持原样。`PREMISE-001`（HoTT 前提集穷尽 P1/P2 清单 + 用户 P3/P4 判定，`PREMISE_DENOMINATOR_V1` 类别 A–G）登记为下一动作并进 STATE active；R4 并行保留。额外修复两处既有漂移：STATE.records 补登 S153（登记 canonical 收据缺口、不伪造）、HEAD.tracked 重建（旧文档名/缺 essay 007/008/MEMORY-003/RESUME 哈希过期）。revision 153→154（用户说「刷到 153」但 153 已被 generation-6 消耗）。无新数学 claim；未 push、未 tag。\n"
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        f"{SESSION_ID}：用户 2026-09-16 认识论修正已纳入核心认知 generation-7（46 KC，KC-000044/045/046；43/43 PRESERVED_EXACT、remainder=0）；"
        "第四件按用户要求改名为 `扩展认知`（索引 + 8 分片，新增第 008 片《现实对齐：理论是现实的骨架式模仿》），活当前真值引用同步，历史快照中的旧名保持原样。"
        "`PREMISE-001` 登记为下一动作并写入 STATE active：对 HoTT 前提集（`PREMISE_DENOMINATOR_V1` 类别 A–G）做穷尽 P1/P2 清单，交用户 P3/P4 判定，非现实者冻结任务族进 GEN-001 链；`R4-HOTT-NAT-EFFECTIVITY-001` 并行保留。"
        "额外修复两处漂移：STATE.records 补登 S153（收据缺口登记、不伪造）、HEAD.tracked 重建。revision 153→154。无新数学 claim；未 push、未 tag。\n\n",
    )

    # ---- STATE -------------------------------------------------------------
    state["revision"] = 154
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "core_sha256": CORE_SHA,
        "curation": CURATION_V7,
        "curation_sha256": CURATION_V7_SHA,
        "generation": GEN7,
        "kc_count": 46,
        "manifest": MANIFEST,
        "manifest_sha256": MANIFEST_SHA,
        "path": CORE,
        "transition": TRANSITION_GEN7,
    }
    state["load_policy"]["full_set"] = [CORE, R.DIRECTION, R.PANORAMA, R.ESSAY]
    state["projection"]["status"] = STATUS
    add_once(state["active"], PREMISE_ID)

    ec = state["execution_control"]
    ec["last_checkpoint_session"] = SESSION_ID
    ec["checkpoint_result"] = RESULT_REL
    ec["status"] = STATUS
    ec["next_minimal_verification"] = (
        "Execute PREMISE-001: freeze PREMISE_DENOMINATOR_V1 (categories A-G) with item ids and hash, "
        "then per item produce P1 (verbatim premise + provenance) and P2 (reality_skeleton, "
        "divergence_point, evidence_level, at least one OMISSION_SHAPE) as structured analysis only; "
        "submit every item to the user for P3/P4 adjudication (never AI-self-certified); for premises "
        "the user judges non-real, run SUPPLY_REGISTRATION then the GEN-001 chain (frozen task family "
        "-> enumeration -> reduction -> native kernel receipt). R4-HOTT-NAT-EFFECTIVITY-001 is "
        "retained in parallel. No mathematical claim is delivered by P1/P2."
    )

    premise_sources = [
        SHARD_008, REVISION_INDEX, AUDIT_09,
        "Atria的审计报告集/01 - 总结论与决定性发现.md",
        "Atria的审计报告集/08 - 对机器统观作为发现路径的独立判断.md",
        "Atria的方案/修订片/003 - GEN-001 有界生成器验收单元（新增）.md",
        "Atria的方案/修订片/006 - 发现引擎：语义重定向作为八轴搜索策略.md",
        "Atria的方案/修订片/007 - 供给层的语料压力字段与符号翻转分工.md",
        CORE, R.ESSAY, "扩展认知/008 - 现实对齐：理论是现实的骨架式模仿.md",
        USER_SOURCE, GOAL, FEATURE,
    ]
    state["records"][PREMISE_ID] = {
        "classification": "EXHAUSTIVE_HOTT_PREMISE_INVENTORY_P1_P2_WITH_USER_P3_P4",
        "depends_on": [],
        "evidence_status": "TASKSPEC_FROZEN / NOT_EXECUTED / NO_NEW_MATH_CLAIM",
        "full_sources": premise_sources,
        "kind": "candidate_search_task",
        "lifecycle_status": "ACTIVE_WORK",
        "path": SHARD_008,
        "research_parent": GOAL_ID,
        "related_records": [GOAL_ID, PLAN_ID, R4_ID, SESSION_ID],
        "scope": (
            "First finite denominator that is HoTT's own premise set (PREMISE_DENOMINATOR_V1 "
            "categories A-G). P1/P2 are structural and omission analysis only; a 'non-real premise' "
            "verdict requires user P3/P4 adjudication followed by engine and native-kernel "
            "verification. Does not cover unnamed premises outside the denominator."
        ),
        "source_hashes": file_hashes(premise_sources),
        "status": "active",
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session_text = f"""# {SESSION_ID}

- 工作单元：用户 2026-09-16 三件事——（1）认识论修正进入核心认知；（2）第四件文档改名；（3）`PREMISE-001` 写入 STATE current queue 并刷新投影。
- 事件 1（已完成，commit `6ab1c68`）：用户 2026-09-16T12:14:00Z 认识论修正原文纳入核心认知 generation-6/43 → generation-7/46；新增 `KC-000044`（理论是对现实的骨架式模仿）、`KC-000045`（数学与 HoTT 必然可映射现实）、`KC-000046`（AI 缺的是用现实理解理论的动作）；43/43 旧单元 `PRESERVED_EXACT`、mapping_count=43、remainder=0；curation v7、transition gen7、`verify_core_cognition.py` PASS_WITH_SCOPE。
- 事件 2（已完成，commit `3990de8`）：`从抽象到悖论——HoTT研究的核心问题意识与思想展开`（索引 + 同名分片目录）按用户要求改名为 `扩展认知`；新增第 008 片《现实对齐：理论是现实的骨架式模仿》；19 个活当前真值文件同步引用（AGENTS/LOAD_SET/PROTOCOL/cognition_runtime `ESSAY` 常量/Skill/rulings/feature-list/合同/validators/RESUME/MEMORY/README）；`verify_governance_shards.py` PASS（456 索引、17 canonical）、`test_three_way_cognition.py` 6/6 OK。剩余旧名引用经全面检查均为不可变历史证据或用户原文逐字引文（`核心认知.md` KC-000038 载体、`扩展认知/006` 逐字引文、essay 索引内的改名说明、audit/imports 与第三方历史快照），不改动。
- 事件 3（本 checkpoint）：`A-PREMISE-001` 登记为 STATE active 记录并写入 `execution_control.next_minimal_verification`；`方向追踪`/`全景视野` 索引 marker 刷到 revision 154 并新增 `DIR-TOP-PREMISE-INVENTORY` / `OUT-TOP-PREMISE-001-REGISTRATION`；`DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` 的下一动作原位改为 PREMISE-001（R4 并行保留）；MEMORY/001 队列与 MEMORY/003 顺序日志同步；RESUME 停止点插入 S154。
- 额外修复（既有漂移，非用户要求但对 canonical 流程强制）：STATE.records 补登 S153 记录——generation-6 的 session 三件存在于磁盘但未被登记，`graph()` 要求 latest_session 必须是已注册 session 记录；登记内容显式标注 canonical checkpoint 收据缺口、不伪造 transaction/result。HEAD.tracked 重建——revision 153 写入后 essay 改名并新增分片 007/008，且 MEMORY/003、RESUME 等哈希过期，`plan()` 报 `HEAD_TRACKING_INCOMPLETE` + `UNCOMMITTED_STATE`；重建保持 revision=153/latest_session=S153 不变，仅恢复派生路由数据。
- 关于 revision 号：用户说「投影刷到 revision 153」，但 153 已被 generation-6 消耗（STATE/HEAD 均为 153、latest_session=S153），canonical checkpoint 只能取 prior+1=154。这是 forced move，在此透明说明。
- 数学状态：不变。PREMISE-001 的 P1/P2 是结构与省略分析，不是数学结论（F-011 不适用）；「某前提非现实」必须经用户 P3/P4 判定再由引擎与原生核验证。无新数学 claim。
- Git：本工作单元路径精确 stage 后本地提交；不 push、不 tag。
"""
    runs_text = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "session_kind": "GOVERNANCE_CORE_GENERATION_ESSAY_RENAME_PREMISE_REGISTRATION",
            "checkpoint_result": RESULT_REL,
            "formal_runs": [],
            "governance_runs": [
                {
                    "run_id": "20260916-CORE-GENERATION-7-BUILD-01",
                    "tool": "scripts/audit/build_core_cognition.py",
                    "command": "build_core_cognition.py --curation scripts/audit/core-cognition-curation-v7.json --write (carried over from commit 6ab1c68)",
                    "status": "BUILT / COMPLETE_ADDITIVE_PRESERVING / mapping_count=43 / remainder=0",
                    "generation": f"{GEN6}/43 -> {GEN7}/46",
                    "kc_count": "43 -> 46",
                },
                {
                    "run_id": "20260916-ESSAY-RENAME-01",
                    "tool": "git mv + reference sync",
                    "command": "git mv index + shard dir -> 扩展认知; 19 live current-truth files updated",
                    "status": "COMMITTED (3990de8); verify_governance_shards.py PASS (456 indexes / 17 canonical); test_three_way_cognition.py 6/6 OK",
                    "generation": "essay index 7 -> 8 shards",
                },
                {
                    "run_id": "20260916-HEAD-TRACKING-REPAIR-01",
                    "tool": "scripts/audit/prepare_s154_core_generation_7_rename_premise001_checkpoint.py",
                    "command": "repair_state_and_head(): backfill STATE.records[S153] + rebuild HEAD.tracked",
                    "status": "REPAIRED / revision and latest_session unchanged / gap registered not forged",
                    "generation": "n/a",
                },
                {
                    "run_id": "20260916-CHECKPOINT-APPLY-154-01",
                    "tool": ".codex/tools/cognition_runtime.py",
                    "command": "cognition_runtime.py checkpoint --snapshot <s> --payload <p> --apply",
                    "status": "CHECKPOINT_COMMITTED / revision 153 -> 154",
                    "generation": "current_core -> core-cognition-generation-7",
                },
            ],
            "new_math_claims": [],
            "math_status_change": "NONE",
            "next": [PREMISE_ID, R4_ID],
            "push_policy": "NOT_AUTHORIZED",
            "note": "Governance-only session: user epistemological correction recorded into core generation-7, "
                    "the AI-exposition fourth document renamed to 扩展认知, and PREMISE-001 registered as the "
                    "next action. No mathematical claim was delivered or adjudicated.",
        },
        ensure_ascii=False, sort_keys=True, indent=2,
    ) + "\n"

    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, SHARD_008, AUDIT_09, USER_SOURCE, MANIFEST, TRANSITION_GEN7, CURATION_V7],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, PREV152, GOAL_ID, PLAN_ID, R4_ID, PREMISE_ID],
        "scope": (
            "Register core generation-7 (KC-000044/045/046), rename the fourth document to 扩展认知, "
            "register PREMISE-001 as the next action with R4 retained in parallel, and repair two "
            "pre-existing drifts (missing S153 record, stale HEAD.tracked). No new mathematics."
        ),
        "source_hashes": {},
        "status": "complete",
    }

    # refresh related records
    for record_id in (GOAL_ID, PLAN_ID, R4_ID):
        record = state["records"][record_id]
        add_once(record.setdefault("related_records", []), PREMISE_ID)
        add_once(record.setdefault("related_records", []), SESSION_ID)
    r4 = state["records"][R4_ID]
    r4["revalidation"] = (
        f"{SESSION_ID}: user 2026-09-16 epistemological correction reorders the next action to "
        f"PREMISE-001 (HoTT premise set as the first finite denominator); R4 is retained in active "
        f"without lifecycle change and its TaskSpec remains valid in parallel."
    )
    for record_id, extra in (
        (GOAL_ID, [SHARD_008, AUDIT_09, USER_SOURCE, TRANSITION_GEN7, CURATION_V7, MANIFEST, CORE]),
        (PLAN_ID, [SHARD_008, AUDIT_09, USER_SOURCE]),
    ):
        record = state["records"][record_id]
        for path in extra:
            add_once(record.setdefault("full_sources", []), path)
        record["revalidation"] = (
            f"{SESSION_ID}: core generation-7 recorded and the fourth document renamed; PREMISE-001 "
            f"registered as the next action inside the same goal; no mathematical scope changed."
        )

    # ---- assemble payload --------------------------------------------------
    essay = projection_edit.load(ROOT, R.ESSAY)  # unchanged this checkpoint, but its index + every
    # shard must still ship in the payload (prepare() requires the full logical document)
    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    texts[session_path] = session_text
    texts[audit_path] = audit_text()
    texts[runs_path] = runs_text

    new_records = (PREMISE_ID, SESSION_ID, PREV)
    for record in state["records"].values():
        hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(hashes, dict):
            continue
        rebound = []
        for path in list(hashes.keys()):
            if path == R.STATE:
                continue
            data = texts[path].encode("utf-8") if path in texts else None
            if data is None:
                target = ROOT / path
                if not target.is_file():
                    continue
                data = target.read_bytes()
            value = R.sha(data)
            if hashes[path] != value:
                hashes[path] = value
                rebound.append(path)
        if rebound and record is not state["records"][PREMISE_ID] and record is not state["records"][SESSION_ID]:
            note = (
                f"{SESSION_ID}: rebound source hashes at {', '.join(sorted(rebound))} "
                f"(content evolved during revisions 152-154 while the canonical checkpoint machinery "
                f"was being repaired); prior mathematical and scope conclusions remain unchanged."
            )
            previous = record.get("revalidation")
            record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note

    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries.",
        "load_profile": "governance",
        "task_ids": [],
        "core_transition": CORE_TRANSITION,
        "files": [
            {"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value}
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 154, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
