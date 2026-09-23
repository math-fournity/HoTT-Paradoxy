#!/usr/bin/env python3
"""Apply the P39 scoped contract verdict through the canonical checkpoint writer."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SID = "S-RES-20260922-ASTRA-P39-ORIGIN-EVENT-CONTRACT-GATE"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P38 = "R-P38-REAL-ORIGIN-EVENT-BRIDGE-20260922"
P39 = "R-P39-ORIGIN-EVENT-CONTRACT-GATE-20260922"
REPORT = "audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md"
SOURCES = (
    REPORT,
    "goal-3-工作路径树/001 - 原初目标与当前工作树.md",
    "Astra继续尝试/断点与证明机制系统检查/对话原文/007 - 归档交付与指定缺口的新问题.md",
    "ABX行动/003 - 原圆环对象、判据与正反控制.md",
    "audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md",
    "audit/p13-ambient-pair-rmin-requalification-20260921/P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md",
    "audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md",
    "HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime():
    spec = importlib.util.spec_from_file_location("cognition_runtime", ROOT / ".codex/tools/cognition_runtime.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def editor():
    sys.path.insert(0, str(ROOT / "scripts/audit"))
    import projection_edit
    return projection_edit


TOUCHED = {
    1: ("DEEPENED", "三问约束原X", "P39只判断历史事件规格是否能改变Done", "没有把合同裁决称为悖论"),
    5: ("ALIGNED", "先找现象再归因", "以静态与历史事件分开记录", "没有凭字段缺席指控HoTT"),
    7: ("CORRECTED", "AI模式匹配需受反证约束", "P7旧字段覆盖让新record无资格", "不因熟悉概念继续包装"),
   10: ("DEEPENED", "现实相对同任务过程", "原X与三种操作类未混淆", "缺强桥时不判非现实"),
   11: ("DEEPENED", "时序可用性独立检查", "历史删除若有时序意义仍未定义Done", "静态去点不等于事件历史"),
   14: ("ALIGNED", "保留B方向", "本波未用P1边界否定B方向", "P3新来源将检实际承诺"),
   15: ("ALIGNED", "理论抽象负责任地检验", "忘却来源是候选而非已证Z铁律实例", "未来需真实K与同任务失配"),
   17: ("DEEPENED", "先用用户视角看旧知识", "先读原文再核P7与实际源码", "没有让教科书等价遮蔽来源任务"),
   21: ("ALIGNED", "数学结论要机器证明", "本波只有合同覆盖判断无新定理", "不作kernel升级"),
   22: ("ALIGNED", "A/B双向目标", "保留两类任务但本波不声称命中", "消费者与现实桥仍开放"),
   23: ("TENSION", "应定位HoTT时间处理", "P39只完成P1准入，仍无规则桥", "下一来源必须检真实声明"),
   35: ("ALIGNED", "查理论表达范围", "P7能承载可检查字段", "历史事件未定不能称不可表达"),
   37: ("CORRECTED", "圆环直觉驱动而非自证", "C269/C270的曲线正例保留", "N不能变M不得无条件使用"),
   38: ("TENSION", "审HoTT作者基础选择", "P39未找到其遗漏原任务的实际K", "P40查真实定理运输使用处"),
   39: ("TENSION", "基础问题不应无限延期", "第39波仍未形成强见证链", "停止P1同义工作换分母"),
   40: ("DEEPENED", "知识谱是被审对象", "选择官方Cubical真实使用处而非凭记忆", "P40先固定版本和调用链"),
   41: ("ALIGNED", "用AI并超越惯性", "正反控制与源文共同约束裁决", "不把本轮文本量当发现"),
   42: ("DEEPENED", "助力可变成阻力", "连续P1字段细化已显边际递减", "换真实消费者来源"),
   43: ("CORRECTED", "防路径依赖", "P39关闭历史event wrapper", "P40若只见弱声明也立即关闭"),
   44: ("DEEPENED", "理论是现实骨架式模仿", "保留圆环来源作为解释任务", "未把物理历史伪造成静态类型事实"),
   45: ("DEEPENED", "在现实对齐断裂处找前提", "断裂落在历史事件Done未规定", "只有实际承诺才能定位理论失配"),
   46: ("DEEPENED", "从现实过程进理论", "原X限定P1，P40寻找一般机制后才回接", "不以队列任务取代圆环"),
}


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == 46
    out = [
        f"# {SID} 核心认知与波次审计", "",
        f"- core_identity: {core['generation']} / {core['core_sha256']} / 46 KC",
        "- tier: T3 research mutation; single-file compatibility under G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.",
        "- core_change: NO; 本波没有用户新的直接悖论原文。",
        "- direction_change: P1历史事件延伸关闭；P3新来源一次消费者准入。",
        "- panorama_change: P39合同范围裁决，无新数学证明。",
        "- essay_change: NO; 以下对八片阐释层逐片复核。",
        "- update_decision: 以canonical checkpoint关闭P1延伸并登记P40为下一项有界来源审计。",
        "- cross_conflicts: goal.md和总体方案005曾仍指P18/P19，plan-revise(b67a4d3c)已原位修复；Feature F021/F022需同波更新。",
        "- unresolved: 历史事件独立Done、actual K、现实同任务桥及分片writer gap。", "",
        "## 核心认知逐条立场", "",
        "| KC | 主题 | relation | 该条要求的姿态 | P39实际与证据 | 为什么 | 下一选择与反证条件 |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, (kc, title) in enumerate(headings, 1):
        if i in TOUCHED:
            relation, posture, actual, why = TOUCHED[i]
            next_step = "P40核新真实使用处；若出现保任务强承诺或反例，重评P39。"
        else:
            relation, posture, actual, why = (
                "NOT_TOUCHED", f"按原文重新检验「{title}」", "P39只审圆环历史事件合同；报告§1–§8", "该主题不决定本波规格准入",
            )
            next_step = "进入与该主题直接相关的新分母或出现反证时再触及；本波不推断。"
        out.append(f"| `{kc}` | {title} | `{relation}` | {posture} | {actual}；P39报告§1–§8 | {why} | {next_step} |")
    out.extend([
        "", "## 扩展认知逐片回评", "",
        "| 分片 | 姿态、已经做过什么、偏航与下一选择 |", "|---|---|",
        "| 001 理论简化 | 看抽象省略了什么；P39确认省略候选需独立Done；P40查真实使用。 |",
        "| 002 前提与时间 | 保留时序和运动结构之别；P39未新增物理或稠密性结论。 |",
        "| 003 圆环与ASK | 原X作为根，三操作类不可混；P40只找一般机制，回接X另证。 |",
        "| 004 HoTT与自反 | 本波没有对象反射或规则级桥；旧P2子线不因P40自动复活。 |",
        "| 005 表达界限 | 现有P7表达可检查字段；未定历史事件不等于不可表达。 |",
        "| 006 知识谱反观 | 官方源码作为待核对象，而非训练记忆的权威。 |",
        "| 007 AI助力与阻力 | P34–P39连续P1的熟路已终止；P40负结果也必须及时结束。 |",
        "| 008 现实对齐 | 历史事件解释断在独立Done；保留断裂，不向HoTT硬贴错误。 |", "",
        "## 已走过的路", "",
        "`G0 → P1 → P7 → P34/C-326 → P35 → P36 → P37 → P38 → P39`。静态去点、闭图、曲线过程和两种操作的控制均已有定位。P38的宽否定已降级；P39没有找到独立改变Done的历史事件字段，关闭同义延伸。P31曾离开HoTT本体做modal/Löb校准，P32/P33将其范围收回。证据见P39报告及各前序报告，不因路径节点多而增加数学结论。", "",
        "## 即将作出的选择：全树比较", "",
        "| 入口 | 当前资格、反解释、回退 |", "|---|---|",
        "| 新P2规则/模型 | 已审SIP与反射来源仅给边界；无不同且真实承诺的定点，暂不重开。 |",
        "| P3实际消费者 | 官方Cubical队列表示独立性是新真实证明使用处；P40先pin源码、核五项K；若只承诺抽象正确性即防御。 |",
        "| P1另一对象任务 | 历史事件Done尚未独立规定；新操作/观察/Done出现才回航，不再添同义record。 |",
        "| P4实现差异 | 无同规则可重放差异；拒签/超时不是入口。 |", "",
        "## 波次反思、遗漏与局限", "",
        "Goal-3 §3七项、§3.1五项、§3.2 successor和§3.3六项完整见P39报告§5–§7。裁决`CLOSE_WITH_SCOPE / SWITCH_BRANCH`。P40是来源准入而非已找到K，最强反解释为源自身只承诺保操作的抽象正确性。遗漏轴：其它理论、其它实际消费者、物理实施和实现语义均未穷尽。P39无新claim/run；checkpoint只登记有界研究状态，不能证明HoTT非现实或全局无问题。writer不支持同事务写审计分片，依PROTOCOL§5使用单文件46-KC兼容形式并保留G-V5缺口。",
    ])
    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rt, ed = runtime(), editor()
    assert all((ROOT / p).is_file() for p in SOURCES)
    state = json.loads((ROOT / rt.STATE).read_text())
    assert state["revision"] == 256 and state["latest_session"] == "S-RES-20260922-ASTRA-P38-REAL-ORIGIN-EVENT-BRIDGE"
    tracked = json.loads((ROOT / rt.HEAD).read_text())["tracked"]
    assert all(sha(ROOT / p) == digest for p, digest in tracked.items())
    plan = rt.plan(ROOT, profile="research", task_ids=[P38])
    assert not plan["review_required"] and not plan["hydration_diagnostics"]["query_first_promoted"]
    (HERE / "P39-CHECKPOINT-PLAN.json").write_bytes(rt.dump(plan))

    state["revision"], state["latest_session"] = 257, SID
    owner = state["records"][PLAN]
    owner["related_records"] = list(dict.fromkeys(owner.get("related_records", []) + [P39, SID]))
    owner["status"] = "p1_event_extension_closed_p40_new_consumer_gate_next"
    owner["evidence_status"] = "P39_REGISTERED_FIELDS_COVERED_HISTORICAL_EVENT_SPEC_UNDERDETERMINED / P1_EXTENSION_CLOSED / P3_P40_NEW_CONSUMER_SOURCE_NEXT / P4_NOT_TRIGGERED / GOAL_ACTIVE"
    owner["full_sources"] = list(dict.fromkeys(owner.get("full_sources", []) + list(SOURCES)))
    owner.setdefault("source_hashes", {}).update({p: sha(ROOT / p) for p in SOURCES})
    for path in ("goal.md", "HoTT后续研究总体方案/005 - 当前第一步与交接.md"):
        assert path in owner["source_hashes"]
        owner["source_hashes"][path] = sha(ROOT / path)
    owner["revalidation"] = owner.get("revalidation", "") + " Revision257 closes P39's duplicate event-field path and selects a distinct official representation-independence consumer source for P40; no K is established."
    state["records"][P39] = {
        "kind": "result", "path": REPORT, "lifecycle_status": "CURRENT", "status": "complete_with_scope",
        "evidence_status": "CONTRACT_INSPECTED_WITH_SCOPE / REGISTERED_FIELDS_COVERED / HISTORICAL_EVENT_SPEC_UNDERDETERMINED / P1_EXTENSION_CLOSED / NO_NEW_MATH_CLAIM",
        "depends_on": [], "related_records": [PLAN, P38, SID],
        "full_sources": list(SOURCES), "source_hashes": {p: sha(ROOT / p) for p in SOURCES},
        "scope": "The original endpoints/process obligations are represented by P7/ABX and fixed models; no independently specified historical-event Done changes the registered task. This does not refute user intuition, prove global expressibility, or establish any HoTT K or reality mismatch.",
    }
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL", "status": "complete_with_scope",
        "evidence_status": "P39_SCOPED_CONTRACT_GATE_REFLECTED_AND_CHECKPOINTED", "depends_on": [],
        "related_records": [PLAN, P38, P39],
        "full_sources": [BASE + x for x in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P39_P1_EXTENSION_CLOSED_P40_NEW_P3_SOURCE_NEXT",
        "current_phase": "PHASE_2_P39_REFLECTED_WITH_SCOPE_P40_CONSUMER_GATE_NEXT",
        "second_phase_status": "P1_P39_EVENT_EXTENSION_CLOSED_P2_OLD_DENOMINATORS_CLOSED_P3_P40_NEW_SOURCE_NEXT_P4_NOT_TRIGGERED",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P40-P3-REPRESENTATION-INDEPENDENCE-QUEUE-CONSUMER-001. Freeze Angiuli et al. arXiv:2009.05547v2 and the exact Cubical Agda commit for RepresentationIndependence.agda §4.2, Queue and Truncated2List. Audit actual Input (two queue representations), Operation (queue operations and theorem transport), Observation (what source claims is preserved), Done_w (operation-preserving abstract correctness) and Done_s only if that source itself claims process, cost, timing, or provenance preservation. Apply P7 K-input/output/claim/forgetting/version with explicit positive control and strongest defense. Stop after one fixed corpus verdict K/DEFENSE/TASK_DISTINCT/EXACT_COVERAGE; do not infer the original circle X or a HoTT defect from a queue result. If no K, generate a different successor.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P39_P1_EXTENSION_CLOSED / P40_NEW_P3_SOURCE_NEXT / P2_OLD_BOUNDARIES_CLOSED / P4_NOT_TRIGGERED / GOAL_ACTIVE / NO_HOTT_DEFECT_CLAIM"

    memory = ed.load(ROOT, "MEMORY.md")
    direction = ed.load(ROOT, "方向追踪.md")
    panorama = ed.load(ROOT, "全景视野.md")
    essay = ed.load(ROOT, "扩展认知.md")
    ed.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md",
        "P38 已完成六模块有界审计与逐项反思：静态去点已定义；历史来源事件没有在已查实际模型接口中显式登记。旧宽否定已降级。下一=P39一次合同准入门，仅在独立改变`Done_s`的缺字段存在时继续P1形式化；P3仍等待实际K，P4未触发。入口：`audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md`；revision256。",
        "P39 已关闭P1同义历史事件字段延伸：原X可检查的端部、闭图与已登记过程已有P7/ABX及实际源码覆盖；额外历史事件的独立`Done_s`尚未规定。总航向审计承认第一弹/原M3与P31/P34–P38的局部偏航，但保留已核边界。下一=P40固定官方Cubical队列表示独立性源码版本，审其真实证明运输承诺；尚无K或HoTT缺陷。入口：`audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md`；revision257。")
    ed.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\nS-RES-20260922-ASTRA-P39-ORIGIN-EVENT-CONTRACT-GATE：P1历史事件Done未独立规定，已有字段覆盖可检查原X；P39按Goal-3§3/3.1/3.2/3.3关闭并换真实消费者分母P40；revision257，无新数学claim。\n")
    for doc, kind in ((direction, "direction"), (panorama, "outcome")):
        ed.replace_in_index(doc, "source_state_revision: 256", "source_state_revision: 257")
        ed.replace_in_index(doc, f"projection_generation: 20260922-{kind}-256", f"projection_generation: 20260922-{kind}-257")
        ed.replace_in_index(doc, "semantic_status: FOUR_TRACK_P38_SIX_MODULE_BOUNDARY_P39_CONTRACT_GATE_NEXT",
            "semantic_status: FOUR_TRACK_P39_P1_EXTENSION_CLOSED_P40_NEW_P3_SOURCE_NEXT")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P38：六模块来源事件范围审计 | P37/P38 | `P39_ONE_BOUNDED_CONTRACT_GATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、`OUT-P38-ORIGIN-EVENT-BOUNDARY` | 静态去点已定义；先检验P39是否有独立影响Done的义务 | P38 report；revision256 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P39：P1事件字段延伸关闭，P40新消费者来源待审 | P38/P39 | `P1_EXTENSION_CLOSED / P40_P3_NEW_SOURCE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、`OUT-P39-ORIGIN-EVENT-CONTRACT-GATE` | pin官方Cubical队列示例的源码commit，核真实K承诺；无强Done则防御收尾 | P39 report；revision257 |")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P38 | `P3_PAUSED / P39_P1_CONTRACT_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P38 reports；revision256 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX原圆环K仍未找到；P40仅检一般证明使用机制 | P21/P39 | `P3_CIRCLE_PAUSED / P40_GENERAL_CONSUMER_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | P40若命中一般机制，仍须另证保真接回原X | P21/P39 reports；revision257 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-P38-ORIGIN-EVENT-BOUNDARY` | 六模块来源事件有界覆盖与旧宽判词纠正 | `DIR-U-HOTT-FOUR-TRACK` | frozen local source + reflection | `SOURCE_INSPECTED_WITH_SCOPE / P39_ONE_GATE_NEXT` | 静态去点已定义；六模块未显式给历史事件合同 | 不证明全库无桥、不可表达、实际K或HoTT缺陷 | P38 report/verification；revision256 |",
        "| `OUT-P38-ORIGIN-EVENT-BOUNDARY` | 六模块来源事件有界覆盖与旧宽判词纠正 | `DIR-U-HOTT-FOUR-TRACK` | frozen local source + reflection | `SOURCE_INSPECTED_WITH_SCOPE / P39_COMPLETED` | 静态去点已定义；六模块未显式给历史事件合同 | 不证明全库无桥、不可表达、实际K或HoTT缺陷 | P38 report/verification；revision256 |\n| `OUT-P39-ORIGIN-EVENT-CONTRACT-GATE` | 原X事件合同准入与全树偏航审计 | `DIR-U-HOTT-FOUR-TRACK` | 原用户原文、P7/ABX/P13/P38和实际源码 | `CONTRACT_INSPECTED_WITH_SCOPE / P1_EXTENSION_CLOSED / P40_NEXT` | 可检查的端部/闭图/过程字段已覆盖，独立历史事件Done未定；换新消费者来源 | 不证明用户历史直觉为假、任何HoTT规则误用、现实失配或全局无问题 | P39 report；revision257 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P38转入P39一次合同准入门 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34/P35/P36/P37/P38 | `P3_PAUSED / P39_P1_CONTRACT_GATE` | 仅新实际K可重开P3 | 不证明原M/N桥 | P21/P38 reports；revision256 |",
        "| `OUT-ABX-ACTION-INTAKE` | 原圆环P3仍待K；P40另查一般证明运输使用 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P21/P39的准入与范围裁决 | `P3_CIRCLE_PAUSED / P40_GENERAL_GATE_NEXT` | 一般机制如命中仍须另证回接原X | 不证明原M/N桥、HoTT缺陷或P40已找到K | P21/P39 reports；revision257 |")
    ed.replace_in_shard(panorama, "全景视野/008 - 当前未完成.md",
        "16. `P39-P1-ORIGIN-EVENT-CONTRACT-GATE-001`：只核一次既有P7/ABX与原X的operation/observation/Done是否缺独立字段；无缺口即关闭这条P1延伸。",
        "16. `P40-P3-REPRESENTATION-INDEPENDENCE-QUEUE-CONSUMER-001`：先固定论文v2与官方Cubical Agda队列示例的源码commit，再核真实输入、保操作关系、输出与强任务承诺；无实际强Done即防御关闭。")
    simple = {p: (ROOT / p).read_text() for p in rt.MUTABLE if p not in {rt.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    old_frontier = "- P38确认六模块已定义静态去点而无显式历史事件合同；旧全资产否定已降级。P39只准一次独立Done合同核对。入口：`audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md`。"
    new_frontier = "- P39确认原X可检查的端部/过程字段已覆盖，历史事件Done未独立规定；关闭同义P1延伸。P40先pin官方Cubical队列表示独立性源码版本，再核真实证明使用承诺。入口：`audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md`。"
    assert old_frontier in simple[rt.PREFIX + "FRONTIER.md"]
    simple[rt.PREFIX + "FRONTIER.md"] = simple[rt.PREFIX + "FRONTIER.md"].replace(old_frontier, new_frontier, 1)
    old_resume = "当前 active goal 已完成P38有界范围与Goal-3逐项反思：静态去点已定义；六模块未显式保存历史事件合同，不能外推全库。P39只核一次独立Done缺口；P3等实际K，P4未触发。入口：`audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md`；revision256。"
    new_resume = "当前 active goal 已完成P39的Goal-3逐项反思：现有字段覆盖原X可检查的端部/闭图/过程，额外历史事件Done未独立规定；P1这条延伸关闭。P40先固定官方Cubical队列表示独立性论文v2与源码commit，审真实证明使用承诺；仍无圆环K、HoTT缺陷或P4触发。入口：`audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md`；revision257。"
    assert old_resume in simple[rt.PREFIX + "RESUME.md"]
    simple[rt.PREFIX + "RESUME.md"] = simple[rt.PREFIX + "RESUME.md"].replace(old_resume, new_resume, 1)
    rows = []
    for doc in (memory, direction, panorama, essay):
        rows.extend(ed.payload_rows(doc, ROOT))
    seen = {row["path"] for row in rows}
    for path in rt.MUTABLE:
        if path not in seen:
            rows.append({"path": path, "expected_sha256": sha(ROOT / path),
                         "text": rt.dump(state).decode() if path == rt.STATE else simple[path]})
    session = (
        f"# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n"
        "- tier: T3 research mutation\n- status: `P39_P1_EXTENSION_CLOSED / P40_P3_SOURCE_GATE_NEXT`\n"
        f"- load_receipt: research plan snapshot `{plan['snapshot']}`; goal-3 and core→direction→panorama→essay were read to EOF in order.\n"
        "- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001; complete single-file 46-KC audit, not atomically written shards.\n"
        "- authorization: user active goal permits the scoped research-state checkpoint; no subagent, push, release, or publication.\n"
    )
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID,
            "primary_runs": [{"kind": "P39 contract/source inspection", "result": "SOURCE_INSPECTED_WITH_SCOPE", "receipt": REPORT}],
            "new_math_claims": [], "new_kernel_replay": False}
    rows.extend([
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": rt.dump(runs).decode()},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": core_audit(state["current_core"])},
    ])
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID,
               "load_profile": "research", "task_ids": [P38],
               "authorization": "用户active goal授权P39合同准入、Goal-3逐项反思和canonical checkpoint；不启动Sub Agent、不push、不发布。",
               "files": rows}
    (HERE / "P39-CHECKPOINT-PAYLOAD.json").write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (HERE / ("P39-CHECKPOINT-APPLY.json" if args.apply else "P39-CHECKPOINT-DRY-RUN.json")).write_bytes(rt.dump(result))
    print(json.dumps({k: v for k, v in result.items() if k != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
