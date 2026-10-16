#!/usr/bin/env python3
"""Checkpoint the user's premise-targeted candidate-generation correction."""
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
SID = "S-PLAN-20260922-ASTRA-P40-PREMISE-TARGETING"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P39 = "R-P39-ORIGIN-EVENT-CONTRACT-GATE-20260922"
CHANGED_SOURCES = (
    "rulings.md",
    "goal-3.md",
    "goal-3-工作路径树/001 - 原初目标与当前工作树.md",
    "goal.md",
    "HoTT后续研究总体方案.md",
    "HoTT后续研究总体方案/004 - 令牌经济、反漂移与每单元复核.md",
    "HoTT后续研究总体方案/005 - 当前第一步与交接.md",
    "feature-list.md",
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
    3: ("DEEPENED", "合取前提要成为可检验靶点", "先选可能被省略的条件，再设计令其决定完成的过程", "不能从类比直接推出前提错误"),
    4: ("DEEPENED", "以具体过程向前提发问", "用户以芝诺稠密性和罗素形成过程说明定向攻击", "两例是方法提示不是HoTT定理"),
    5: ("CORRECTED", "先发现后定最终病因", "前提现在只是可撤回靶点，最终归因仍后置", "兼容用户原研究顺序"),
   10: ("ALIGNED", "寻找现实相对过程而非形式爆炸", "P40先设计针对过程并预注册Done", "尚无HoTT失配"),
   15: ("DEEPENED", "研究抽象否定的具体位置", "P40要求规则出处、经济收益、条件和过程成对登记", "Z强律仍不是已证元定理"),
   16: ("ALIGNED", "形成过程可以成为压力测试", "罗素比方只用于生成目标，不移植矛盾", "须找到HoTT自身规则"),
   18: ("DEEPENED", "追问理论经济如何处理时间", "把过程压力先于随机消费者检索", "不把缺时间当已证病因"),
   19: ("DEEPENED", "合取条件中定位可疑前提", "针对过程要使条件改变可观察Done", "不能仅因条件被省略判矛盾"),
   20: ("ALIGNED", "运动领域作候选母域", "P40的D-01候选仍须现实模型与反解释", "物理量子化不作已证输入"),
   21: ("ALIGNED", "机器结论需相称运行", "本轮只修研究次序，无新数学claim/run", "后续候选需原生核"),
   22: ("ALIGNED", "A/B两类方向并存", "靶点过程可产生额外困难或虚假完成的候选", "不预判哪类成立"),
   37: ("ALIGNED", "圆环直觉启发定向发现", "原圆环X₀保留回接基准", "一般任务X_T不自动等于原X₀"),
   38: ("DEEPENED", "捕捉作者设计决策", "先核经济收益与被省略条件", "不随机搜相邻论文"),
   39: ("CORRECTED", "基础问题应从基础前提出发", "P40从经济前提而非消费者标题选择", "候选不足则如实换分母"),
   40: ("DEEPENED", "把知识谱当审查对象", "PREMISE-001/C11只作查重与候选地图", "AI旧判断不作证据"),
   43: ("CORRECTED", "防路径依赖", "随机K扫描降为针对过程后验证", "再无靶点则不继续相邻关键词"),
   44: ("ALIGNED", "现实骨架可用于提出过程", "X_T需有任务与完成标准", "现实类比不自动成为经验事实"),
   45: ("DEEPENED", "在诠释断裂处找前提", "前提、经济收益、过程和反解释成对固定", "不能见结果后选病因"),
   46: ("DEEPENED", "用现实理解HoTT的动作", "先做针对过程，再决定理论/应用/实现层", "不以代码量替代发现"),
}


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == 46
    out = [
        f"# {SID} 核心认知与靶点策略审计", "",
        f"- core_identity: {core['generation']} / {core['core_sha256']} / 46 KC",
        "- tier: T3 plan mutation; single-file compatibility under G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.",
        "- core_change: NO; 用户本轮重述既有 KC-000003/004/005/015/018/019/020/045，新增的是执行次序裁定，原文完整存 rulings/dev-notes。",
        "- direction_change: P40从随机队列消费者审计改为靶前提—过程候选准入。",
        "- panorama_change: 只登记策略修正，不新增数学命题或证明。",
        "- essay_change: NO; 当前阐释层已讨论现实对齐、理论经济、AI路径依赖。",
        "- update_decision: canonical checkpoint 登记 P40 新 TaskSpec；变更前不得执行旧队列扫描。",
        "- cross_conflicts: 旧 STATE 指向队列审计，新 goal-3/总体方案已按用户裁定改为靶点先行；本事务消除冲突。",
        "- unresolved: P40尚未选出合格靶前提或针对过程；实际K、HoTT必要性、现实桥和审计分片writer gap仍开放。", "",
        "## 核心认知逐条立场", "",
        "| KC | 主题 | relation | 要求姿态 | 本轮实际与证据 | 为什么 | 下一选择与反证条件 |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, (kc, title) in enumerate(headings, 1):
        if i in TOUCHED:
            relation, posture, actual, why = TOUCHED[i]
            next_step = "P40只选一张靶前提—过程卡；若已有控制完全覆盖或过程不敏感，撤回候选并换分母。"
        else:
            relation, posture, actual, why = (
                "NOT_TOUCHED", f"保留「{title}」原文义务", "本轮只改候选生成顺序；rulings/goal-3", "该主题不决定本轮 P40 准入",
            )
            next_step = "相关新分母或直接反证出现时重开；本轮不由未触及推断。"
        out.append(f"| `{kc}` | {title} | `{relation}` | {posture} | {actual}；见本轮 ruling 与 goal-3 | {why} | {next_step} |")
    out.extend([
        "", "## 扩展认知逐片回评", "",
        "| 分片 | 已走过的路、偏航诊断与下一选择 |", "|---|---|",
        "| 001 理论简化 | 以省略/理想化带来经济收益为候选来源；不把抽象存在直接叫矛盾。 |",
        "| 002 前提与时间 | 用户的针对性过程让被改变条件重新出现；物理时间仍需独立桥梁。 |",
        "| 003 芝诺/圆环/ASK | 事前选靶前提与过程；原X₀是回接基准，未把X_T冒充X₀。 |",
        "| 004 HoTT与自反 | 之后才查规则与自反义务；当前不复活已闭合反射分母。 |",
        "| 005 表达界限 | 形式化不能偷换任务；先问过程真正观察什么。 |",
        "| 006 知识谱反观 | PREMISE-001作为被审对象，不是AI已判非现实的权威。 |",
        "| 007 AI助力与阻力 | P40旧队列来源先行显出熟悉通道；及时改道而非追加K扫描。 |",
        "| 008 现实对齐 | 定位某抽象前提在现实过程中的断裂，先作为可撤回假说。 |", "",
        "## 已走过的路", "",
        "`G0 → P1/P2/P3/P4 首次通路 → P23–P33反射边界 → P34–P39圆环合同 → P40旧队列来源候选`。P39关闭同义事件字段；用户本轮指出P40继续随机消费者来源检索没有靶点。新裁定是靶前提→针对过程→分支验证，不回写或删除旧运行。证据是rulings原文、goal-3及工作树、历史P39报告、plan-revise commit。", "",
        "## 即将作出的选择：全树比较", "",
        "| 候选 | 支持、张力、反证和回退 |", "|---|---|",
        "| P40靶前提—过程准入 | 服务KC-003/004/015/045。固定G-04、D-01、Book§11.2三类既有来源；只选一张非重复候选卡。若全已覆盖或过程对靶条件不敏感，判NO_ELIGIBLE_TARGET_WITHIN_THREE并换前提分母。 |",
        "| P1继续圆环字段 | P39已关闭同义事件扩展；只有新的独立Operation/Observation/Done才重开。 |",
        "| P2规则级挑战 | 需P40先提出针对特定经济前提的可检验过程；否则重扫SIP/反射仅重复。 |",
        "| P3实际消费者 | 队列论文是已发现但低优先级线索；没有靶过程不随机找K；若真实强声明出现可重开。 |",
        "| P4实现忠实性 | 仍无规则—实现差异；普通拒签不触发。 |", "",
        "## 波次反思与边界", "",
        "Goal-3 §3：新增事实为用户明确裁定的针对性发现顺序；旧P39数学判词不变。Input/Operation/Done未改，下一波才设计X_T。正控制是旧理论保结构/保成本字段时任务可恢复；最强反解释是理想前提仅属于数学对象或可选模型。旧P40队列审计若继续会重复同类防线，故本轮停止它；P40候选准入获得资格，P1/P2/P3/P4仍为验证分支。没有新数学事实时停止本轮规划并执行一张卡，而非继续写规则。Goal-3 §3.1：总体价值是纠正候选产生机制、减少无靶来源扫描；坐标为G0→P39→P40计划修正；裁决SWITCH_BRANCH。Goal-3 §3.2–3.3：完整路径和四支比较见上；若新X_T无保任务桥，不称原X₀命中；`TARGETING_DRIFT`与`SPEC_SUBSTITUTION_DRIFT`分别监控。旧SOP八项：PREMISE-001原35条与GEN-001不在本轮重跑；P3/P4未做，scoped negative未外推，新的靶策略来自用户而非AI自证。当前writer仅能原子保存单文件46KC audit，分片缺口保留。",
    ])
    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rt, ed = runtime(), editor()
    state = json.loads((ROOT / rt.STATE).read_text())
    assert state["revision"] == 257 and state["latest_session"] == "S-RES-20260922-ASTRA-P39-ORIGIN-EVENT-CONTRACT-GATE"
    tracked = json.loads((ROOT / rt.HEAD).read_text())["tracked"]
    assert all(sha(ROOT / p) == digest for p, digest in tracked.items())
    plan = rt.plan(ROOT, profile="governance")
    assert not plan["review_required"] and not plan["hydration_diagnostics"]["query_first_promoted"]
    (HERE / "P40-PLAN-SNAPSHOT.json").write_bytes(rt.dump(plan))
    owner = state["records"][PLAN]
    actual_changed = {p for p, old in owner.get("source_hashes", {}).items() if (ROOT / p).is_file() and sha(ROOT / p) != old}
    assert actual_changed == set(CHANGED_SOURCES), actual_changed

    state["revision"], state["latest_session"] = 258, SID
    owner["related_records"] = list(dict.fromkeys(owner.get("related_records", []) + [SID]))
    owner["status"] = "p40_premise_targeted_candidate_discovery_next"
    owner["evidence_status"] = "PLAN_REVISED_BY_USER / P40_TARGET_PREMISE_BEFORE_PROCESS_BEFORE_K / NO_NEW_MATH_CLAIM / GOAL_ACTIVE"
    for p in CHANGED_SOURCES:
        owner["source_hashes"][p] = sha(ROOT / p)
    owner["revalidation"] = owner.get("revalidation", "") + " Revision258 incorporates the user's premise-targeted paradox-construction correction; old P40 queue-consumer task was a plan only and is superseded before execution."
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL", "status": "complete_with_scope",
        "evidence_status": "P40_TARGETING_PLAN_CORRECTION_CHECKPOINTED / NO_NEW_MATH_CLAIM", "depends_on": [],
        "related_records": [PLAN, P39],
        "full_sources": [BASE + x for x in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P40_PREMISE_TARGETED_CANDIDATE_NEXT",
        "current_phase": "PHASE_2_P40_PREMISE_TARGETED_CANDIDATE_DISCOVERY_NEXT",
        "second_phase_status": "P1_P39_EVENT_EXTENSION_CLOSED_P40_TARGETED_GENERATION_NEXT_P2P3_FOLLOW_TARGET_P4_NOT_TRIGGERED",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": "P40-PREMISE-TARGETED-CANDIDATE-DISCOVERY-001. In one bounded selection pass compare source-pinned PREMISE-G-04 (univalence equivalence-as-identity), PREMISE-D-01 (cubical interval/connections), and HoTT Book §11.2 real/Ω simplification. Use existing PREMISE-001/C11 and C250–C326 coverage before new search. For each record exact rule/optional-axiom identity, economic or universality benefit, omitted/idealized condition, a pre-registered process X_T specifically sensitive to that condition with Input/Operation/Observation/Done, strongest defense and positive control. Select exactly one non-duplicative target card or NO_ELIGIBLE_TARGET_WITHIN_THREE, then choose a new premise denominator. Do not run a kernel, scan random consumers, predeclare a HoTT defect, or count an X_T result as original circle X0 without a separate task-preserving bridge. Queue representation-independence source remains a candidate/defense control, not the current task.",
    })
    state["projection"]["status"] = "FOUR_TRACK_P40_TARGETED_PREMISE_CANDIDATE_NEXT / P39_CLOSED / P2P3_AFTER_TARGET / P4_NOT_TRIGGERED / GOAL_ACTIVE / NO_HOTT_DEFECT_CLAIM"

    memory = ed.load(ROOT, "MEMORY.md")
    direction = ed.load(ROOT, "方向追踪.md")
    panorama = ed.load(ROOT, "全景视野.md")
    essay = ed.load(ROOT, "扩展认知.md")
    ed.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md",
        "P39 已关闭P1同义历史事件字段延伸：原X可检查的端部、闭图与已登记过程已有P7/ABX及实际源码覆盖；额外历史事件的独立`Done_s`尚未规定。总航向审计承认第一弹/原M3与P31/P34–P38的局部偏航，但保留已核边界。下一=P40固定官方Cubical队列表示独立性源码版本，审其真实证明运输承诺；尚无K或HoTT缺陷。入口：`audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md`；revision257。",
        "用户纠正P40的来源先行顺序：候选发现须先固定HoTT的具体经济性前提及其省略/理想化条件，再设计专门针对该条件的过程；P1–P4和真实K是后续验收层。P39的原X范围判词不变。下一=P40一次有界靶前提—过程准入，比较G-04、D-01、Book§11.2三处已登记来源，最多选一张非重复卡；队列论文仅候选/防线对照。尚无K或HoTT缺陷。入口：`goal-3.md`、`HoTT后续研究总体方案/005 - 当前第一步与交接.md`；revision258。")
    ed.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\nS-PLAN-20260922-ASTRA-P40-PREMISE-TARGETING：按用户靶点先行纠正更新goal-3/总体方案与STATE，旧P40队列来源任务执行前被替代；revision258。无新数学claim或kernel run。\n")
    for doc, kind in ((direction, "direction"), (panorama, "outcome")):
        ed.replace_in_index(doc, "source_state_revision: 257", "source_state_revision: 258")
        ed.replace_in_index(doc, f"projection_generation: 20260922-{kind}-257", f"projection_generation: 20260922-{kind}-258")
        ed.replace_in_index(doc, "semantic_status: FOUR_TRACK_P39_P1_EXTENSION_CLOSED_P40_NEW_P3_SOURCE_NEXT",
            "semantic_status: FOUR_TRACK_P40_PREMISE_TARGETED_CANDIDATE_NEXT")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-HOTT-FOUR-TRACK` | P39：P1事件字段延伸关闭，P40新消费者来源待审 | P38/P39 | `P1_EXTENSION_CLOSED / P40_P3_NEW_SOURCE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN`、`OUT-P39-ORIGIN-EVENT-CONTRACT-GATE` | pin官方Cubical队列示例的源码commit，核真实K承诺；无强Done则防御收尾 | P39 report；revision257 |",
        "| `DIR-U-HOTT-FOUR-TRACK` | P40：靶前提—针对过程先于分支验收 | 用户2026-09-22纠正/P39 | `P40_TARGETED_CANDIDATE_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY`、`THEORY_ECONOMY` | `OUT-HOTT-FOUR-TRACK-PLAN`、`OUT-P39-ORIGIN-EVENT-CONTRACT-GATE` | 在G-04/D-01/Book§11.2中最多选一张新靶前提—过程卡；已有控制全覆盖即换分母 | goal-3/总体方案005；revision258 |")
    ed.replace_in_shard(direction, "方向追踪/002 - 治理与用户方向.md",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX原圆环K仍未找到；P40仅检一般证明使用机制 | P21/P39 | `P3_CIRCLE_PAUSED / P40_GENERAL_CONSUMER_GATE` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | P40若命中一般机制，仍须另证保真接回原X | P21/P39 reports；revision257 |",
        "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX原圆环K仍未找到；P40先生成靶前提—过程 | P21/P39/用户纠正 | `P3_CIRCLE_PAUSED / P40_TARGETED_DISCOVERY` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 一般X_T只有保任务回接后才可称原X₀命中；有靶过程后才找K | goal-3/P39；revision258 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-P39-ORIGIN-EVENT-CONTRACT-GATE` | 原X事件合同准入与全树偏航审计 | `DIR-U-HOTT-FOUR-TRACK` | 原用户原文、P7/ABX/P13/P38和实际源码 | `CONTRACT_INSPECTED_WITH_SCOPE / P1_EXTENSION_CLOSED / P40_NEXT` | 可检查的端部/闭图/过程字段已覆盖，独立历史事件Done未定；换新消费者来源 | 不证明用户历史直觉为假、任何HoTT规则误用、现实失配或全局无问题 | P39 report；revision257 |",
        "| `OUT-P39-ORIGIN-EVENT-CONTRACT-GATE` | 原X事件合同准入与全树偏航审计 | `DIR-U-HOTT-FOUR-TRACK` | 原用户原文、P7/ABX/P13/P38和实际源码 | `CONTRACT_INSPECTED_WITH_SCOPE / P1_EXTENSION_CLOSED / P40_TARGETED_NEXT` | 可检查的端部/闭图/过程字段已覆盖，独立历史事件Done未定；后续先选前提靶点 | 不证明用户历史直觉为假、任何HoTT规则误用、现实失配或全局无问题 | P39 report；revision257 |")
    ed.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md",
        "| `OUT-ABX-ACTION-INTAKE` | 原圆环P3仍待K；P40另查一般证明运输使用 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P21/P39的准入与范围裁决 | `P3_CIRCLE_PAUSED / P40_GENERAL_GATE_NEXT` | 一般机制如命中仍须另证回接原X | 不证明原M/N桥、HoTT缺陷或P40已找到K | P21/P39 reports；revision257 |",
        "| `OUT-ABX-ACTION-INTAKE` | 原圆环P3仍待K；P40先生成前提—过程候选 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P21/P39/用户靶点裁定 | `P3_CIRCLE_PAUSED / P40_TARGETED_DISCOVERY_NEXT` | 一般过程X_T若命中须另证回接原X₀ | 不证明原M/N桥、HoTT缺陷或P40已找到K | goal-3/P39；revision258 |")
    ed.replace_in_shard(panorama, "全景视野/008 - 当前未完成.md",
        "16. `P40-P3-REPRESENTATION-INDEPENDENCE-QUEUE-CONSUMER-001`：先固定论文v2与官方Cubical Agda队列示例的源码commit，再核真实输入、保操作关系、输出与强任务承诺；无实际强Done即防御关闭。",
        "16. `P40-PREMISE-TARGETED-CANDIDATE-DISCOVERY-001`：从G-04、D-01、Book§11.2三处有出处的理论经济决策中，先查重并设计针对省略条件的过程，最多选一张新候选卡；无合格靶点则换前提分母，不随机扫描K。")
    simple = {p: (ROOT / p).read_text() for p in rt.MUTABLE if p not in {rt.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    old_frontier = "- P39确认原X可检查的端部/过程字段已覆盖，历史事件Done未独立规定；关闭同义P1延伸。P40先pin官方Cubical队列表示独立性源码版本，再核真实证明使用承诺。入口：`audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md`。"
    new_frontier = "- 用户纠正P40候选生成顺序：先选HoTT具体经济性前提及其被省略条件，再设计针对过程；P40在G-04/D-01/Book§11.2中只选一张非重复候选卡。队列论文暂为防线对照。入口：`goal-3.md`、`HoTT后续研究总体方案/005 - 当前第一步与交接.md`。"
    assert old_frontier in simple[rt.PREFIX + "FRONTIER.md"]
    simple[rt.PREFIX + "FRONTIER.md"] = simple[rt.PREFIX + "FRONTIER.md"].replace(old_frontier, new_frontier, 1)
    old_resume = "当前 active goal 已完成P39的Goal-3逐项反思：现有字段覆盖原X可检查的端部/闭图/过程，额外历史事件Done未独立规定；P1这条延伸关闭。P40先固定官方Cubical队列表示独立性论文v2与源码commit，审真实证明使用承诺；仍无圆环K、HoTT缺陷或P4触发。入口：`audit/p39-origin-event-contract-gate-20260922/P39-ORIGIN-EVENT-CONTRACT-GATE-REPORT.md`；revision257。"
    new_resume = "当前 active goal 已按用户靶点先行裁定纠正P40：P39原X合同结论不变；P40先从G-04/D-01/Book§11.2有出处前提中选一项并设计针对性过程，再进入P1/P2/P3/P4验证。旧队列来源审计执行前被替代，队列论文仅保留候选/防线对照；仍无实际K、HoTT缺陷或P4触发。入口：`goal-3.md`、`HoTT后续研究总体方案/005 - 当前第一步与交接.md`；revision258。"
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
        "- tier: T3 plan mutation\n- status: `P40_TARGETED_PREMISE_DISCOVERY_NEXT / NO_NEW_MATH_CLAIM`\n"
        f"- load_receipt: governance plan snapshot `{plan['snapshot']}`; current core generation-7/46, goal-3 and P39 path reviewed.\n"
        "- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001; single-file 46-KC audit, not atomically written shards.\n"
        "- authorization: user's target-first correction and active goal permit plan/current-state write-back; no subagent, push, release, or publication.\n"
        "- element_usage: core=question anchor; direction/panorama=current scope; STATE=next action; proof gate=prevents theorem claim; historical ledgers=not used.\n"
    )
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID,
            "primary_runs": [{"kind": "plan/shard validation", "result": "PASS_WITH_SCOPE", "receipt": "goal-3.md"}],
            "new_math_claims": [], "new_kernel_replay": False}
    rows.extend([
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": rt.dump(runs).decode()},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": core_audit(state["current_core"])},
    ])
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID,
               "load_profile": "governance", "task_ids": [],
               "authorization": "用户明确纠正悖论候选生成策略，授权active goal计划与当前状态同步；不启动Sub Agent、不push、不发布。",
               "files": rows}
    (HERE / "P40-CHECKPOINT-PAYLOAD.json").write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (HERE / ("P40-CHECKPOINT-APPLY.json" if args.apply else "P40-CHECKPOINT-DRY-RUN.json")).write_bytes(rt.dump(result))
    print(json.dumps({k: v for k, v in result.items() if k != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
