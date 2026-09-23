#!/usr/bin/env python3
"""Checkpoint P38's bounded source audit and its explicit wave reflection."""
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
SID = "S-RES-20260922-ASTRA-P38-REAL-ORIGIN-EVENT-BRIDGE"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P37 = "R-P37-WEAK-PUNCTURE-FIDELITY-20260922"
P38 = "R-P38-REAL-ORIGIN-EVENT-BRIDGE-20260922"
AUDIT = "audit/p38-real-origin-event-bridge-20260922/"
SOURCES = (
    AUDIT + "P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md",
    AUDIT + "P38-REAL-ORIGIN-EVENT-BRIDGE-SOURCE-FREEZE.json",
    AUDIT + "verify_p38_real_origin_event_bridge.py",
    AUDIT + "P38-REAL-ORIGIN-EVENT-BRIDGE-VERIFICATION.json",
    "HoTT/formal/astra-breakpoint-check/OriginDirectedDiagram.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda",
    "HoTT/formal/agda-unimath/hott-z/PunctureApartness.agda",
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


# Each tuple gives the posture requested by the named KC and this wave's
# specific contact with it. These are research judgments, not mathematical facts.
KC_NOTES = {
  1: ("DEEPENED", "以三问约束发现", "P38只裁决原X来源桥的六文件覆盖", "范围判断不等于找到悖论"),
  2: ("NOT_TOUCHED", "固定HoTT规则分母", "未修订Theory Schema", "本波只读固定模型源码"),
  3: ("NOT_TOUCHED", "核合取前提与稠密过程", "未检验稠密性或物理时间", "静态去点不能替代物理前提"),
  4: ("NOT_TOUCHED", "检验运动反证", "未构造运动与现实的矛盾", "源码字段观察不足以作物理归因"),
  5: ("ALIGNED", "先寻找具体失配再归因", "P38把宽否定降为六文件边界", "尚无HoTT实际承诺"),
  6: ("NOT_TOUCHED", "保留多类时间机制", "未将来源事件化约为稠密性", "本波未比较其它时间机制"),
  7: ("CORRECTED", "将模型知识作候选而非证明", "P38旧词汇式PASS被降级", "锚点/哈希不证明语义缺席"),
  8: ("NOT_TOUCHED", "用历史悖论启发", "未审历史案例", "六文件分母不包含它们"),
  9: ("NOT_TOUCHED", "定位HoTT时间设定", "未识别HoTT规则级时间前提", "P38是P1对象审计"),
 10: ("DEEPENED", "以同一现实过程比较理论", "静态去点与历史事件被明确分开", "没有同任务HoTT失配"),
 11: ("DEEPENED", "检查时序是否被省略", "六模块只有静态操作及另立CurveRun", "缺事件语义不等于理论拒绝时序"),
 12: ("NOT_TOUCHED", "先问ASK资格", "未定义或执行ASK", "P38没有有效求解任务"),
 13: ("NOT_TOUCHED", "检查抽象是否绕过ASK", "未找到真实HoTT消费者", "不能从source字段缺口推出绕过"),
 14: ("NOT_TOUCHED", "保留现实不可完成而理论宣称完成", "未检验方向B", "P38的Done_s尚未桥接"),
 15: ("ALIGNED", "以抽象遗漏提出候选", "P38提出来源历史可能遗漏", "未把Z铁律当已证元定理"),
 16: ("NOT_TOUCHED", "区分Russell形成与程序运行", "未构造Russell模型", "圆去点来源任务不同"),
 17: ("DEEPENED", "先依用户问题再读现有知识", "静态去点正控制与事件疑问并列", "既有拓扑术语未替代原X"),
 18: ("NOT_TOUCHED", "核理论经济的时间舍弃", "未识别HoTT必要前提", "单个record缺字段不是前提否定"),
 19: ("NOT_TOUCHED", "核合取与稠密过程", "未测量现实运动", "六文件覆盖与物理稠密性不同层"),
 20: ("NOT_TOUCHED", "核运动量子化归因", "未引入Planck尺度前提", "原任务对应尚未建立"),
 21: ("ALIGNED", "数学结论交付需原生运行", "P38不登记新定理或新kernel run", "源码审计只获范围结论"),
 22: ("NOT_TOUCHED", "保留双向现实相对目标", "P38没有证明A/B任一方向", "仍缺K与现实桥"),
 23: ("TENSION", "寻找HoTT时间问题", "P38只定位对象规格缺口", "不能将其当HoTT时间前提"),
 24: ("NOT_TOUCHED", "比较两类时序悖论", "未构造不可停机或虚假完成", "Done_s尚未独立固定历史事件"),
 25: ("NOT_TOUCHED", "审自指候选", "本波没有对象语言自指", "来源事件与自指不同"),
 26: ("NOT_TOUCHED", "查HoTT自身自指", "未触及该分支", "P2反射旧分母已范围关闭"),
 27: ("NOT_TOUCHED", "区分程序共有界限", "未测通用计算界限", "P38只是来源模型"),
 28: ("NOT_TOUCHED", "精确化自验证停机任务", "未运行自反验证", "无对象证明谓词进入本波"),
 29: ("NOT_TOUCHED", "检理论经济回环", "未建立经济收益或自馈", "不能由字段缺席推回环"),
 30: ("NOT_TOUCHED", "考察HoTT经济学", "未比较理论设计选择", "P38只审固定源码"),
 31: ("NOT_TOUCHED", "检最小理想理论覆盖", "未造新理论范型", "P39仅准入合同"),
 32: ("NOT_TOUCHED", "区分稠密性新存在", "未研究稠密数轴", "此分母是实际圆来源"),
 33: ("NOT_TOUCHED", "查无时序不存在性", "未作Russell式形成检验", "静态/历史区分尚非悖论"),
 34: ("NOT_TOUCHED", "保持存在/不存在双视角", "未建立对应逻辑变换", "P38没有全称抽象定理"),
 35: ("ALIGNED", "审HoTT表达力", "OriginDirectedDiagram提供有限正控制", "不能把缺实际事件接口说成不可表达"),
 36: ("NOT_TOUCHED", "检查不完备性研究的自馈", "本波未进入Gödel/反射", "一般限制不能代替原X"),
 37: ("CORRECTED", "以圆环直觉驱动发现", "P38承认静态去点已经定义", "直觉不能压倒正控制"),
 38: ("CORRECTED", "捕捉作者出发点的遗漏", "六模块缺历史事件仍只是规格候选", "没有作者承诺或理论缺陷"),
 39: ("TENSION", "在基础处寻找", "P38为第38波仍未找到K", "下一步仅准入一次避免无穷延长"),
 40: ("DEEPENED", "把知识谱当被审对象", "现有声明被逐字段检验", "训练记忆不作负结论证据"),
 41: ("ALIGNED", "用AI辅助核查并超越惯性", "P38使用固定源码与反解释", "结论仍待独立事件标准"),
 42: ("TENSION", "识别AI助力与阻力", "旧P38过宽措辞显出惯性", "本次降级并限制P39"),
 43: ("CORRECTED", "检查路径依赖", "连续P1波后给P39一次门槛", "没有新Done即回到全树"),
 44: ("DEEPENED", "用现实骨架理解抽象", "静态去点与历史生成分开", "本波不判断现实标准已完成"),
 45: ("DEEPENED", "在对齐断裂处定位省略", "source由输入供应而非历史事件输出", "断裂可能是规格选择非理论错误"),
 46: ("DEEPENED", "从现实过程提问并交机器核", "P38固定原X但不伪造新proof", "P39需独立观察和Done才准形式化"),
}


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == len(KC_NOTES)
    out = [
        f"# {SID} 核心认知与波次审计",
        "",
        f"- core_identity: {core['generation']} / {core['core_sha256']} / 46 KC",
        "- tier: T3 research mutation; single-file compatibility under G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.",
        "- core_change: NO; P38没有新的用户原文。",
        "- direction_change: P38范围降级；P39仅一次合同准入门。",
        "- panorama_change: 新增六模块有界源码覆盖结果，不新增数学命题。",
        "- essay_change: NO; 下方逐主题回评现有AI阐释。",
        "- update_decision: 先经canonical checkpoint更新STATE到P39，未完成前不执行P39。",
        "- cross_conflicts: 旧P38宽判词与六文件证据不相称，已在报告原位纠正；P7与P39可能同义重复。",
        "- unresolved: 历史事件的独立Operation/Observation/Done、实际K、现实同任务桥及分片审计writer gap。",
        "",
        "## 核心认知逐条五元组",
        "",
        "| KC | 主题 | relation | 要求姿态 | P38实际与证据 | relation理由 | 下一选择与反证条件 |",
        "|---|---|---|---|---|---|---|",
    ]
    for index, (kc, title) in enumerate(headings, 1):
        relation, posture, actual, why = KC_NOTES[index]
        next_step = "P39仅核原X独立Done；若实际K或相反源码出现，复评。" if relation != "NOT_TOUCHED" else "该主题进入新分母或用户补规格时重开；本波不推断。"
        out.append(f"| `{kc}` | {title} | `{relation}` | {posture} | {actual}；P38报告§1–§7 | {why} | {next_step} |")
    out.extend([
        "",
        "## 扩展认知逐主题回评",
        "",
        "| 分片/章节 | 姿态、已走过的路、偏航与下一选择 |",
        "|---|---|",
        "| 001 问题意识与简化 | P38先固定原X再读模型；旧‘无桥’宽判词已降级；P39需独立任务。 |",
        "| 002 前提改变与时间 | 本波区分静态子类型和历史事件，但没有时间连续性模型；P39不能据此作物理结论。 |",
        "| 003 芝诺与圆环 | 圆、east、弱M、N、闭图仍是对象；只凭静态去点不推出过程复原。 |",
        "| 003 ASK与两种方向 | 没有ASK或A/B失配见证；P39只问强Done规格资格。 |",
        "| 004 走进HoTT与自反 | C-325是可表达性正控制，P38无规则级桥；P2入口须另立。 |",
        "| 005 表达界限与文章起点 | 缺显式接口只限定六模块；以反解释阻断‘HoTT不可表达’误判。 |",
        "| 006 知识谱反观 | 直接检查源码而非把熟悉的术语当权威；P39复核P7旧规格。 |",
        "| 007 助力与阻力 | 连续P1波有路径依赖风险；P39只许一次准入审计。 |",
        "| 008 现实对齐 | 解释在历史来源处断开；可能是解释规格尚未固定，下一步先定观察与Done。 |",
        "",
        "## 已走过的路",
        "",
        "`G0 → P1 → P7/C-325 → P34/C-326 → P35 → P36/P37 → P38`。P38沿六模块确认静态去点已存在；原报告的仓库级否定被纠正为六模块边界。证据是P38报告、freeze、verifier与Git修订。P23–P33反射支线在既有分母内关闭；它不是P38定理依赖。",
        "",
        "## 即将作出的选择",
        "",
        "| 候选 | 支持与张力 | 裁决、反证与退路 |",
        "|---|---|---|",
        "| P39一次P1合同准入 | 服务KC-10/44–46；连续P1投入触发KC-43路径依赖风险 | 只检查一个独立改变Done_s的字段；若P7已覆盖或语义未定，关闭并转其它根支。 |",
        "| 新P2规则/模型入口 | 服务理论自身之问；已有反射子线无原X桥 | 没有不同理论分母前不复活；新来源须通过同任务准入。 |",
        "| P3实际消费者 | 最接近用户对HoTT使用者的疑问 | 只在版本固定K出现时重开，禁止重复旧扫描。 |",
        "| P4实现忠实性 | 可查规则与证明器一致 | 需可重放语义差异；普通拒签不准入。 |",
        "",
        "## 波次反思与局限",
        "",
        "P38的Goal-3 §3七问、§3.1五项和§3.3六项已逐项记于P38报告§4–§7。结论为`CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_ONE_BOUNDED_P39_CONTRACT_GATE`。本单元没有新数学证明；脚本的PASS只核固定源码身份与正锚点。当前checkpoint writer不支持同事务写入嵌套审计分片，按PROTOCOL §5使用单文件46-KC兼容形式并保留G-V5缺口，不冒充分片审计集已完成。",
    ])
    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rt, ed = runtime(), editor()
    assert all((ROOT / item).is_file() for item in SOURCES)
    assert json.loads((ROOT / SOURCES[3]).read_text())["status"] == "PASS_WITH_SCOPE"
    state = json.loads((ROOT / rt.STATE).read_text())
    assert state["revision"] == 255 and state["latest_session"] == "S-RES-20260922-ASTRA-P37-WEAK-PUNCTURE-FIDELITY"
    tracked = json.loads((ROOT / rt.HEAD).read_text())["tracked"]
    assert all(sha(ROOT / path) == digest for path, digest in tracked.items())
    plan = rt.plan(ROOT, profile="research", task_ids=[PLAN])
    (HERE / "P38-CHECKPOINT-PLAN.json").write_bytes(rt.dump(plan))
    state["revision"], state["latest_session"] = 256, SID
    owner = state["records"][PLAN]
    owner["related_records"] = list(dict.fromkeys(owner.get("related_records", []) + [P38, SID]))
    owner["status"] = "p1_six_module_event_scope_bounded_p39_contract_gate_next"
    owner["evidence_status"] = "P1_STATIC_PUNCTURE_DEFINED / P38_SIX_MODULE_EVENT_BOUNDARY_ONLY / P2_REFLECTION_SUBLINE_CLOSED / P3_PAUSED_NO_K / P4_NOT_TRIGGERED / P39_ONE_BOUNDED_CONTRACT_GATE_NEXT / GOAL_ACTIVE"
    owner["full_sources"] = list(dict.fromkeys(owner.get("full_sources", []) + list(SOURCES)))
    owner.setdefault("source_hashes", {}).update({p: sha(ROOT / p) for p in owner["full_sources"] if (ROOT / p).is_file()})
    owner["revalidation"] = owner.get("revalidation", "") + " Revision256 corrects P38's overbroad negative, rebinds the revised path-tree and exact P38 sources, and gates P39 on an independent Done obligation."
    state["records"][P38] = {
        "kind": "result", "path": SOURCES[0], "lifecycle_status": "CURRENT",
        "evidence_status": "SOURCE_INSPECTED_WITH_SCOPE / STATIC_PUNCTURE_OPERATION_DEFINED / NO_EXPLICIT_HISTORICAL_EVENT_BRIDGE_IN_SIX_CHECKED_MODULES / P39_ONE_BOUNDED_CONTRACT_GATE / NO_NEW_MATH_CLAIM",
        "status": "complete_with_scope", "depends_on": [], "related_records": [PLAN, P37, SID],
        "full_sources": list(SOURCES), "source_hashes": {p: sha(ROOT / p) for p in SOURCES},
        "scope": "Only six fixed model modules were inspected. Static puncture is defined; a historical event and source certificate are not explicit in these modules. No repo-wide absence, inability theorem, HoTT defect, actual K, or reality bridge is claimed.",
    }
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "P38_SCOPED_REFLECTION_AND_CHECKPOINT", "status": "complete_with_scope",
        "depends_on": [], "related_records": [PLAN, P37, P38],
        "full_sources": [BASE + x for x in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P38_SIX_MODULE_BOUNDARY_P39_CONTRACT_GATE_NEXT",
        "current_phase": "PHASE_2_P38_REFLECTED_WITH_SCOPE_P39_ONE_CONTRACT_GATE_NEXT",
        "second_phase_status": "P1_P39_ONE_BOUNDED_GATE_P2_REFLECTION_CLOSED_P3_PAUSED_P4_NOT_TRIGGERED",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P39-P1-ORIGIN-EVENT-CONTRACT-GATE-001. In one bounded pass compare original X and its independently supplied Operation/Observation/Done_s with P7 OriginPresentation, ABX/003, actual RealCircle/east/PuncturedRealCircle, RichCurve, SourceContract and CurveRun. Identify one field that changes Done_s and is not already represented; if none, classify EXACT_COVERAGE or SPEC_UNDERDETERMINED, close this P1 extension, and generate a different successor. Do not add a record or math claim before that gate; no HoTT defect or actual K is established.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P38_SIX_MODULE_BOUNDARY / P39_ONE_BOUNDED_CONTRACT_GATE_NEXT / P2_REFLECTION_CLOSED / P3_PAUSED / P4_NOT_TRIGGERED / GOAL_ACTIVE / NO_HOTT_DEFECT_CLAIM"

    memory = ed.load(ROOT, "MEMORY.md")
    direction = ed.load(ROOT, "方向追踪.md")
    panorama = ed.load(ROOT, "全景视野.md")
    essay = ed.load(ROOT, "扩展认知.md")
    ed.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md",
        "P37 已由C-283–C-290/C-307–C-308确认：普通弱M到开区间的相关正构造显式带`Lift`，强域结果不能无条件替代原M。下一=P38审计现有资产是否已共同给出真实来源event bridge。P3仍等待实际K，P4未触发。入口：`audit/p37-weak-puncture-fidelity-20260922/P37-WEAK-PUNCTURE-FIDELITY-REPORT.md`；revision255。",
        "P38 已完成六模块有界审计与逐项反思：静态去点已定义；历史来源事件没有在已查实际模型接口中显式登记。旧宽否定已降级。下一=P39一次合同准入门，仅在独立改变`Done_s`的缺字段存在时继续P1形式化；P3仍等待实际K，P4未触发。入口：`audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md`；revision256。")
    ed.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\nS-RES-20260922-ASTRA-P38-REAL-ORIGIN-EVENT-BRIDGE：六模块局部来源事件覆盖审计；旧宽否定降级；Goal-3 §3/3.1/3.3逐项反思，P39一次合同准入门；revision256。\n")
    for doc, kind in ((direction, "direction"), (panorama, "outcome")):
        ed.replace_in_index(doc, "source_state_revision: 255", "source_state_revision: 256")
        ed.replace_in_index(doc, f"projection_generation: 20260922-{kind}-255", f"projection_generation: 20260922-{kind}-256")
        ed.replace_in_index(doc, "semantic_status: FOUR_TRACK_P37_WEAK_STRONG_FIDELITY_COVERED_P38_EVENT_BRIDGE_NEXT",
            "semantic_status: FOUR_TRACK_P38_SIX_MODULE_BOUNDARY_P39_CONTRACT_GATE_NEXT")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P37：弱/强M任务忠实性复资格化 | P36/P37 | `P38_REAL_ORIGIN_EVENT_BRIDGE_DISCOVERY_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、C-283–C-290/C-307–C-308 | 条件性已覆盖，审计是否有真实来源event桥 | P37 report；revision255 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P38：六模块来源事件范围审计 | P37/P38 | `P39_ONE_BOUNDED_CONTRACT_GATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、`OUT-P38-ORIGIN-EVENT-BOUNDARY` | 静态去点已定义；先检验P39是否有独立影响Done的义务 | P38 report；revision256 |")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P37 | `P3_PAUSED / P38_P1_EVENT_BRIDGE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P37 reports；revision255 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P38 | `P3_PAUSED / P39_P1_CONTRACT_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P38 reports；revision256 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-P37-WEAK-PUNCTURE-FIDELITY` | 原弱M与强域模型的任务忠实性复资格化 | `DIR-U-HOTT-FOUR-TRACK` | existing C-283–C-290/C-307–C-308 sources/runs | `EXACT_COVERAGE_WITH_SCOPE / P38_NEXT` | 强域到N无条件、弱域正构造显式带Lift；不许强域替代原弱M | 不证明任何无条件弱同胚不可能、HoTT缺陷或现实桥 | P37 report/verification；revision255 |",
        "| `OUT-P37-WEAK-PUNCTURE-FIDELITY` | 原弱M与强域模型的任务忠实性复资格化 | `DIR-U-HOTT-FOUR-TRACK` | existing C-283–C-290/C-307–C-308 sources/runs | `EXACT_COVERAGE_WITH_SCOPE / P38_COMPLETED` | 强域到N无条件、弱域正构造显式带Lift；不许强域替代原弱M | 不证明任何无条件弱同胚不可能、HoTT缺陷或现实桥 | P37 report/verification；revision255 |\n| `OUT-P38-ORIGIN-EVENT-BOUNDARY` | 六模块来源事件有界覆盖与旧宽判词纠正 | `DIR-U-HOTT-FOUR-TRACK` | frozen local source + reflection | `SOURCE_INSPECTED_WITH_SCOPE / P39_ONE_GATE_NEXT` | 静态去点已定义；六模块未显式给历史事件合同 | 不证明全库无桥、不可表达、实际K或HoTT缺陷 | P38 report/verification；revision256 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P37转入P38事件桥审计 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34/P35/P36/P37 | `P3_PAUSED / P38_P1_EVENT_BRIDGE` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P37 reports；revision255 |",
        "| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，P38转入P39一次合同准入门 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27/P28/P29/P30/P31/P32/P33/P34/P35/P36/P37/P38 | `P3_PAUSED / P39_P1_CONTRACT_GATE` | 仅新实际K可重开P3 | 不证明原M/N桥 | P21/P38 reports；revision256 |")
    ed.replace_in_shard(panorama, "全景视野/008 - 当前未完成.md",
        "16. `P38-P1-REAL-ORIGIN-EVENT-BRIDGE-DISCOVERY-001`：审计完整圆、点、去点source、operation、观察和Done是否已有真实origin-event bridge；全覆盖即停止。",
        "16. `P39-P1-ORIGIN-EVENT-CONTRACT-GATE-001`：只核一次既有P7/ABX与原X的operation/observation/Done是否缺独立字段；无缺口即关闭这条P1延伸。")
    simple = {p: (ROOT / p).read_text() for p in rt.MUTABLE if p not in {rt.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[rt.PREFIX + "FRONTIER.md"] = simple[rt.PREFIX + "FRONTIER.md"].replace(
        "- P37确认弱/强关系已有条件性机器覆盖，强域不替代无条件原M；P38审计是否存在真实origin-event bridge。入口：`audit/p37-weak-puncture-fidelity-20260922/P37-WEAK-PUNCTURE-FIDELITY-REPORT.md`。",
        "- P38确认六模块已定义静态去点而无显式历史事件合同；旧全资产否定已降级。P39只准一次独立Done合同核对。入口：`audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md`。", 1)
    simple[rt.PREFIX + "RESUME.md"] = simple[rt.PREFIX + "RESUME.md"].replace(
        "当前 active goal 已完成P37：既有C-283–C-290/C-307–C-308已覆盖弱/强边界，强域结果不能无条件替代原弱M。P38审计现有资产是否已共同形成真实来源event bridge；P3仍等待实际K、P4未触发。入口：`audit/p37-weak-puncture-fidelity-20260922/P37-WEAK-PUNCTURE-FIDELITY-REPORT.md`；revision255。",
        "当前 active goal 已完成P38有界范围与Goal-3逐项反思：静态去点已定义；六模块未显式保存历史事件合同，不能外推全库。P39只核一次独立Done缺口；P3等实际K，P4未触发。入口：`audit/p38-real-origin-event-bridge-20260922/P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md`；revision256。", 1)
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
        f"- tier: T3 research mutation\n- status: `P38_SCOPED_REFLECTION_COMPLETE / P39_ONE_GATE_NEXT`\n"
        f"- load_receipt: research plan snapshot `{plan['snapshot']}`; goal-3 full text and P38 fixed source/report reviewed.\n"
        "- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001; canonical runtime accepts complete single-file 46-KC audit.\n"
        "- authorization: user active goal permits the research-state checkpoint; no subagent, push, release, or publication.\n"
    )
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID,
            "primary_runs": [{"kind": "P38 fixed-source verifier", "result": "PASS_WITH_SCOPE", "receipt": SOURCES[3]}],
            "new_math_claims": [], "new_kernel_replay": False}
    rows += [
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": rt.dump(runs).decode()},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None,
         "text": core_audit(state["current_core"])},
    ]
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID,
               "load_profile": "research", "task_ids": [PLAN],
               "authorization": "用户active goal允许P38范围纠正、逐项反思与canonical checkpoint；不启动Sub Agent、不push、不发布。",
               "files": rows}
    (HERE / "P38-CHECKPOINT-PAYLOAD.json").write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (HERE / ("P38-CHECKPOINT-APPLY.json" if args.apply else "P38-CHECKPOINT-DRY-RUN.json")).write_bytes(rt.dump(result))
    print(json.dumps({k: v for k, v in result.items() if k != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
