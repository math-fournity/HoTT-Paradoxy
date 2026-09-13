#!/usr/bin/env python3
"""Prepare revision 22 for generation-4 and the HoTT self-validation/economy study."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-022-SELF-VALIDATION-ECONOMY"
C4 = "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md"
IMPLEMENTATION_EVIDENCE = "audit/核心认知generation-4与自反理论经济研究实施证据-20260912.md"
CORE_TRANSITION = {
    "from_generation": "core-cognition-generation-3",
    "to_generation": "core-cognition-generation-4",
    "manifest": "核心认知.manifest.json",
    "transition": "audit/core-cognition-generation-4-transition-20260912.json",
}
SPEC = importlib.util.spec_from_file_location("runtime_self_validation_economy", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def replace_line_prefix(text: str, prefix: str, replacement: str) -> str:
    lines = text.splitlines()
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) != 1:
        raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(indexes)}")
    lines[indexes[0]] = replacement
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def replace_span(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"SPAN_MARKER_COUNT:{text.count(start)}:{text.count(end)}")
    begin = text.index(start)
    finish = text.index(end, begin) + len(end)
    return text[:begin] + replacement + text[finish:]


def append_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def build_direction(root: Path) -> str:
    body = (root / R.DIRECTION).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-direction-portfolio/v1.2", "integrated-direction-portfolio/v1.3")
    body = replace_once(body, "integrated-direction-portfolio:v1.2", "integrated-direction-portfolio:v1.3")
    body = body.replace(
        "CORE_GENERATION_3_QUALIFICATION_PRESERVATION_AI_STRATEGY_PROPOSED",
        "CORE_GENERATION_4_THEORY_ECONOMY_REFLECTION_USER_DIRECTION_ACTIVE",
    )
    body = replace_once(body, "source_state_revision: 21", "source_state_revision: 22")
    body = replace_once(body, "projection_generation: 20260912-direction-005", "projection_generation: 20260912-direction-006")
    top = (
        "| `DIR-TOP-QUALIFICATION-PRESERVATION` | ASK／完成资格在 HoTT 抽象、组合、提取与反射中的保持性；统一 A/B 两类现实相对悖论 | "
        "用户 generation-4 core；当前 AI 的 C3/C4 综合（其中用户新增方向以 KC-000028–000036 为准） | `NEXT_CANDIDATE` | "
        "`COMPUTATIONAL_LEGITIMACY`, `TIME_AND_TEMPORALITY`, `SELF_REFERENCE`, `PARADOX_DISCOVERY` | "
        "`OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`、`OUT-W-R041-PAPER`、`OUT-W-RP-B01` | "
        "先机器验证 C4 的经济化抽象 factorization 正/反例，再进入包含验证器自身的反射闭包；partiality bind×race 仍保留为并行可执行对照 | "
        "`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md`；`理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；`核心认知.md` |"
    )
    user_direction = (
        "| `DIR-U-THEORY-ECONOMY-SELF-VALIDATION` | 理论通过遗忘现实因素取得经济收益后，是否在内部证明其抽象、真理验证器和自身可靠性时形成不可停机、部分性或元层上升；"
        "同时审计最小理论覆盖和存在/不存在双视角 | 用户直接新增方向 `KC-000028`–`KC-000036` | `ACTIVE_USER_DIRECTION` | "
        "`THEORY_ECONOMY`, `SELF_VALIDATION`, `SELF_REFERENCE`, `ABSTRACTION_AND_NEGATION`, `EXISTENCE_NEGATION_DUALITY` | "
        "`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY` | 先形式化 `R→A` 的任务相对 factorization 与最小反例（ERCF-1/2），再编码反射认证器 ERCF-3；"
        "逐层区分有限 proof checking、proof search、全局 truth 与内部 soundness | `核心认知.md` `KC-000028`–`KC-000036`；"
        "`理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md` |"
    )
    body = replace_line_prefix(body, "| `DIR-TOP-QUALIFICATION-PRESERVATION`", top + "\n" + user_direction)
    body = replace_line_prefix(
        body,
        "| `DIR-L-SELF-REFLECTION`",
        "| `DIR-L-SELF-REFLECTION` | self-reference、reflection、对象理论—元理论边界；与 W51“程序继承计算界限”和当前理论经济—反射自证问题合流 | "
        "LocalGPT、WebGPT `P-SELF-*`；用户 `KC-000025`–`KC-000028`、`KC-000036` | `ACTIVE_USER_DIRECTION` | "
        "`SELF_REFERENCE`, `SELF_VALIDATION`, `HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY` | "
        "`OUT-W-REFLECTION-FAMILY`、`OUT-W-RP-B01`、`OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY` | "
        "在 Code/quote/substitution/evaluation/provability 固定后构造“有效自我 ASK”最小接口；先证明局部检查正例，再检验总停机/健全/完备/内部可证四者不可兼得的精确条件，不把一般 Gödel 口号冒充 HoTT 实例 | "
        "`HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`；`理解章节/A11-开放问题与悬空接头.md`；`理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md` |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-G-UNDERSTANDING-RECONCILIATION`",
        "| `DIR-G-UNDERSTANDING-RECONCILIATION` | 两个理解章节的逐文件语义融合和当前 canonical 路由 | 用户当前要求、顶层计划 | `SUPPORTING_DIRECTION` | "
        "`CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-UNDERSTANDING-MERGE`（设计） | 当前 29/24 inventory 已逐文件处置；继续按 2,396 条历史 claim 的用户选择范围做直接语义/数学复核；"
        "C4 为新增顶层 current synthesis，不改写历史 claim 分母 | `理解章节/`；`AI对话录/理解章节/`；`audit/understanding-chapter-merge-manifest.json` |",
    )
    body = replace_once(body, "当前方向只使用 generation-3 manifest 中实际存在的主题", "当前方向只使用 generation-4 manifest 中实际存在的主题")
    old_start = "1. **总方向建议（尚待用户采纳）**"
    old_end = "本轮只形成并落盘研究战略，没有启动任何数学证明、代码模型、证明助手或外部接口审计。未来若用户启动研究，每个自然工作单元只推进一个可检查构造，并按 C3 的四级判词与停止条件收敛。"
    new_priority = """1. **当前用户主方向**：`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` × `DIR-L-SELF-REFLECTION`。先把理论经济、任务相对充分性与反射认证义务写成可证伪构造。
2. **总方向建议（AI 统筹，尚非用户单独裁定）**：`DIR-TOP-QUALIFICATION-PRESERVATION`，以 ASK／完成资格在抽象、组合、提取和反射中的保持性统一 A/B 与 ERCF。
3. **第一最小可验结果**：C4 的 `ERCF-1/2`，机器证明 `ParadoxWitness(α,J)` 与 factorization 不可能，并给出平凡任务正例；这是进入自反前的 walking skeleton。
4. **战略自反深化**：`DIR-W-RP-B01` × ERCF-3。目标是定位数学分类→统一有效交付→有效自我 ASK→自我可靠性认证的资格升级点。
5. **操作对照包**：`DIR-W-RACE-TIMEOUT`。从 R041 的 bind/race 分离推进真实 partiality quotient/QIIT，作为“局部操作不变性不等于全局上下文充分性”的独立证据。
6. **探索/独立验证位**：完整流函数/在线因果、guard 擦除、同函数异时与 R034 Cubical Agda；只在真实接口固定后进入。
7. **证据/治理队列**：R041 code/25-test/`cf58f27`/container 谱系、2,396 条历史 claim、aistudio coverage 和历史因果映射继续按当前任务选择；C4 不改变这些历史分母。

本轮已按用户要求形成 C4 条件性数学论证并更新研究航向，但没有启动 proof assistant 机器证明、具体非停机程序运行或外部接口审计。后续每个自然工作单元只推进一个可检查构造，并按 C3/C4 的判词与停止条件收敛。"""
    return replace_span(body, old_start, old_end, new_priority)


def build_panorama(root: Path) -> str:
    body = (root / R.PANORAMA).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-outcome-panorama/v1.2", "integrated-outcome-panorama/v1.3")
    body = replace_once(body, "integrated-outcome-panorama:v1.2", "integrated-outcome-panorama:v1.3")
    body = body.replace(
        "CORE_GENERATION_3_QUALIFICATION_PRESERVATION_AI_STRATEGY_PROPOSED",
        "CORE_GENERATION_4_THEORY_ECONOMY_REFLECTION_USER_DIRECTION_ACTIVE",
    )
    body = replace_once(body, "source_state_revision: 21", "source_state_revision: 22")
    body = replace_once(body, "projection_generation: 20260912-outcome-005", "projection_generation: 20260912-outcome-006")
    body = replace_line_prefix(
        body,
        "| `OUT-TOP-CORE-FOUNDATION`",
        "| `OUT-TOP-CORE-FOUNDATION` | generation-4：保留三份历史 primary，并加入一份当前 Codex 直接用户原文；89 条登记消息中 24 条形成 36 个 `USER_OWNED_DIRECT` 原文语义单元；"
        "generation-3 的 27 KC 全部 byte-identical 保留 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` | "
        "顶层交接工程 | `VERIFIED_WITH_SCOPE` | source/curation lineage/selector/payload hash、连续编号及 generation-3→4 的 27/27 `PRESERVED_EXACT`、remainder=0 可核验 | "
        "不证明用户主张为数学真理，不证明模型理解；新增捕获时间不是用户写作时间 | `核心认知.md`；`核心认知.manifest.json`；`scripts/audit/core-cognition-curation-v4.json`；"
        "`audit/core-cognition-generation-4-transition-20260912.json`；`scripts/audit/verify_core_cognition.py` |",
    )
    result = (
        "| `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY` | C4 将 HoTT 自身真理验证拆为有限 proof checking、归一化、证明搜索、整体语义真理和内部总自验证五层；"
        "提出 ERCF（理论经济—反射自证回环），给出 abstraction factorization、存在/不存在四分法、最小 E₀/E₁ 与 Gödel/元层边界 | "
        "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-TOP-QUALIFICATION-PRESERVATION` | 当前用户原文 + 顶层 AI 条件性研究综合 | `PAPER_ONLY` | "
        "支持“局部验证可停机而全局同层健全完备总真理判定不可兼得”的分层结论；证明目标已被改写成 ERCF-1/2/3 的可证伪阶梯，并由 HoTT Book、cubical normalization、2LTT、内部元理论与 Gödel 形式化资料交叉 | "
        "不证明 HoTT 内部矛盾，不证明任意 HoTT 实现实际死循环，不证明物理时空离散，不证明已存在一个一致而 HoTT 无法保真覆盖的最小理论；尚无本轮 proof-assistant run | "
        "`理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；`核心认知.md` `KC-000028`–`KC-000036`；`HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md` |"
    )
    merge = (
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 29/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0/C1/C2/C3/C4 共 5 个独有文件"
        "（nonidentical union entries=14）；逐文件处置已生成 | `DIR-G-UNDERSTANDING-RECONCILIATION` | 顶层只读审计 | `VERIFIED_WITH_SCOPE` | "
        "每个 union 文件有 hash、line diff、处置决定、回滚源和非破坏性验证；C3/C4 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | "
        "不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4 自动裁决 | "
        "`audit/understanding-chapter-merge-manifest.json`；`scripts/audit/verify_understanding_merge.py`；`理解章节/`；`AI对话录/理解章节/` |"
    )
    body = replace_line_prefix(body, "| `OUT-UNDERSTANDING-MERGE`", result + "\n" + merge)
    body = replace_line_prefix(
        body,
        "| `OUT-TOP-THREE-WAY-SKELETON`",
        "| `OUT-TOP-THREE-WAY-SKELETON` | generation-4 + LOAD_SET/runtime v3 + STATE v2：三件套永久全文、governance/research profile、stable task hydration、历史 Session 冷存；"
        "incremental curation v2 允许 hash-pinned 后续用户原文追加 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-E-WEB-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION` | "
        "当前顶层治理升级 | `VERIFIED_WITH_SCOPE` | core 7 tests、runtime/reader/three-way/fresh checks 按当前 generation 动态核验；旧 27 KC 全保留，新 9 KC 可逐字重建 | "
        "fresh 模型行为、2,396 条历史 claim 语义、C4 数学结论的机器证明仍未完成；本轮治理候选尚未 commit/tag | "
        "`audit/核心认知generation-4与自反理论经济研究实施证据-20260912.md`；`audit/fresh-three-way-verification-20260912.json`；`.codex/` |",
    )
    body = replace_once(body, "顶层三件套已接入 generation-3、STATE/load v3、逐文件 merge receipt 和全量 source register", "顶层三件套已接入 generation-4、STATE/load v3、逐文件 merge receipt 和全量历史 source register")
    old = "6. C3 只是一份证据受限的 AI 研究战略；用户是否采纳、真实 partiality/QIIT consumer、B01-TARGET、有效自我 ASK 演算和相应 native proof 均未完成。"
    new = "6. C3 是证据受限的 AI 研究战略；真实 partiality/QIIT consumer、B01-TARGET 和有效自我 ASK 演算尚未完成。C4 已响应用户的新自反/理论经济方向，但 ERCF-1/2/3 的 proof-assistant 形式化、具体发散 witness、最小 HoTT coverage no-go 与 Gödel 内部化均未完成。"
    return replace_once(body, old, new)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    rows = {
        1: ("DEEPENED", "三问被 C4 落实为五类验证任务、ERCF 三阶候选和明确证据边界。", "C4 §0–§3、§12", "ERCF 尚未机器证明。"),
        2: ("ALIGNED", "坚持先区分 HoTT 变体、宇宙、消去、正性与终止规则。", "C4 §2、§9", "首个 proof assistant/variant 尚未选定。"),
        3: ("DEEPENED", "合取前提被写成 abstraction factorization 与任务族充分性。", "C4 §6", "现实任务类仍需实例化。"),
        4: ("TENSION", "保留反证用途，同时指出表示失真、形成拒绝和内部矛盾不能自动等同。", "C4 §8–§9", "具体矛盾到现实前提的桥梁待证。"),
        5: ("ALIGNED", "先给可证伪候选和边界，不预设最终 HoTT 归因。", "C4 §12–§15", "no-go witness 未形成。"),
        6: ("ALIGNED", "自反、元层、任务充分性扩展了时间问题，没有收窄为稠密性。", "C4 §4、§6", "物理时间仍外部。"),
        7: ("ALIGNED", "利用已有理论知识生成候选，但回到一手论文与精确构造。", "C4 参考资料与证据边界", "原创性检索未完成。"),
        8: ("ALIGNED", "历史悖论作为形态启发，未被直接冒充 HoTT 定理。", "C4 §8", "历史到 HoTT 的保真翻译仍开放。"),
        9: ("DEEPENED", "将 HoTT 时间维度定位到 proof search、反射义务和元层上升。", "C4 §1、§4", "具体内核 witness 未运行。"),
        10: ("ALIGNED", "明确不以内部矛盾为默认目标，并保留现实相对/表示边界判词。", "C4 §0、§13", "NATURAL_USAGE_MISMATCH 实例待证。"),
        11: ("DEEPENED", "把程序顺序与无界搜索、有限检查、元理论义务分层。", "C4 §1、§3", "操作成本模型尚未形式化。"),
        12: ("DEEPENED", "ASK 被区分为证书检查、问题可判定性和全局真理资格。", "C4 §1、§3", "ERCF-3 的 ASK 接口待编码。"),
        13: ("DEEPENED", "理论工具性被系统化为五类理论经济与任务相对充分性。", "C4 §5–§7", "HoTT 具体经济收益的量化指标未设定。"),
        14: ("ALIGNED", "数学分类与有效交付断裂继续作为 ERCF 自反线的输入。", "C4 §3、§12", "RP-B01 自然接口仍开放。"),
        15: ("TENSION", "将抽象必然悖论收紧为：非单射抽象必对某些观察失败，但不必对所有任务失败。", "C4 §6", "Z 铁律强式仍是研究立场而非已证全称定理。"),
        16: ("TENSION", "动态不可停机重释被保留，但与 Russell 的标准无约束概括来源并列。", "C4 §8.2", "两种语义的等价未证。"),
        17: ("ALIGNED", "用户原文进入 core，AI 结论保持 paper-only 并回到外部证据。", "核心认知 generation-4；C4 元数据", "模型理解不由工具认证。"),
        18: ("TENSION", "承认工具性/否定现实的研究价值，同时要求指定任务、观察与 factorization。", "C4 §5–§7", "无条件 Z 铁律未被证明。"),
        19: ("TENSION", "稠密性作为模型正结构保留，但无限描述、极限和物理执行被严格区分。", "C4 §8.1", "现实离散性未认证。"),
        20: ("TENSION", "保留反证路线，但不从悖论直接推出物理时空连续性为假。", "C4 §8.1、§15", "现实桥梁待物理证据。"),
        21: ("ALIGNED", "给出下一 proof-assistant walking skeleton，并明确本轮尚未运行。", "C4 §12、§15", "机器证明为下一工作单元。"),
        22: ("ALIGNED", "两类现实相对目标由资格保持性与 ERCF 联通。", "C4 §6、§12", "具体双向 HoTT 实例未完成。"),
        23: ("DEEPENED", "明确最可能的问题点是经济化抽象与反射性全局认证的交叉。", "C4 §4–§6", "真实 HoTT consumer 待固定。"),
        24: ("DEEPENED", "时序成本论被正式命名为理论经济，并写成任务族相对的信息压缩。", "C4 §5–§7", "经济指标尚未经验化。"),
        25: ("DEEPENED", "解释自指候选难点在于 syntax/quote/eval/provability 与可靠性条件。", "C4 §3–§4、§11", "exact calculus 待选。"),
        26: ("DEEPENED", "把不可越过自身转成同层总健全完备自验证不可兼得的条件命题。", "C4 §0、§3", "尚非 HoTT 特有不一致性。"),
        27: ("DEEPENED", "区分 proof checking 可停机与 theoremhood/全局 self-truth 无总判定器。", "C4 §1–§3", "Gödel 条件需在选定 HoTT 中内部化。"),
        28: ("DEEPENED", "直接回答：可能出现 proof-search 发散或认证义务不闭合，但不是所有验证死循环。", "C4 §0–§4、§14.1", "无具体运行发散轨迹。"),
        29: ("DEEPENED", "把经济收益高风险点写成 `α:R→A`、任务族与全局认证回路。", "C4 §5–§6", "ERCF-2/3 尚未机器证明。"),
        30: ("DEEPENED", "核实旧 KC-13/18/24 已含经济思想，并补充 HoTT 的五类经济性。", "C4 §5、§7", "历史用语未被 AI 改写进 core。"),
        31: ("DEEPENED", "给出覆盖失败四分法、E₀/E₁ 和真正 no-go 所需六项合同。", "C4 §9", "一致且不可保真解释的最小理论尚未找到。"),
        32: ("DEEPENED", "将否定现实与存在性攻击改写为模型添加、遗漏、商去和观察充分性。", "C4 §6、§8", "稠密物理解释待证。"),
        33: ("TENSION", "保留无时序动态重释，但不把它冒充 Russell 标准形式原因。", "C4 §8.2", "程序语义映射待构造。"),
        34: ("CORRECTED", "把关系性双视角细分为省略、商去、否定公理和理想化添加，明确省略不等于逻辑否定。", "C4 §8", "对偶视角仍可作为现实相对语义使用。"),
        35: ("DEEPENED", "给出 Reality/abstract/observe/ASK/ParadoxWitness 的 HoTT 表达骨架。", "C4 §10", "现实语义和全局自应用需外部/更高层。"),
        36: ("DEEPENED", "回答 HoTT 可研究 Gödel，并区分研究弱理论、研究自身、证明搜索发散和反射阶梯。", "C4 §11", "HoTT 内部完整形式化尚未完成。"),
    }
    units = manifest["units"]
    if set(rows) != set(range(1, len(units) + 1)):
        raise ValueError("AUDIT_ASSESSMENT_DENOMINATOR_MISMATCH")
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(units)}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    for index, unit in enumerate(units, 1):
        relation, assessment, evidence, unresolved = rows[index]
        counts[relation] = counts.get(relation, 0) + 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | {evidence}; 核心认知.md {unit['id']} | {unresolved} |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `YES_USER_DIRECT_INPUT` — 用户明确要求记录；建立 generation-4，旧 27 KC 全部逐字保留并新增 KC-000028–000036。",
        "- direction_change: `YES_ACTIVE_USER_DIRECTION` — 新增理论经济—反射自证方向并把 self-reflection 升为当前用户方向；ERCF-1/2 为下一最小可验结果。",
        "- panorama_change: `YES_PAPER_ONLY_RESULT` — 登记 C4 的分层回答、正向 normalization 控制、no-go 条件、未决机器证明与现实边界。",
        "- update_decision: `用户原文只进入 core/source/ruling；AI 论证进入 C4/方向/全景/STATE；历史 claim register 分母不被追写。`",
        "- cross_conflicts: `RESOLVED_BY_LAYERING` — 旧“程序不可停机”直觉与 cubical proof checking 可判定性不矛盾：前者适用于无界搜索/总真理自证，后者是有限判断。省略现实因素与逻辑否定也被分层。",
        "- unresolved: `ERCF-1/2/3 proof assistant；具体发散 witness；一致而 HoTT 无法保真覆盖的最小理论；内部 Gödel 编码；物理与 Russell 动态桥梁。`",
        "", "## 汇总", "",
        f"`DEEPENED={counts.get('DEEPENED', 0)} / ALIGNED={counts.get('ALIGNED', 0)} / CORRECTED={counts.get('CORRECTED', 0)} / TENSION={counts.get('TENSION', 0)} / DEVIATED={counts.get('DEVIATED', 0)} / NOT_TOUCHED={counts.get('NOT_TOUCHED', 0)}`。本回评只证明公开逐项判断存在，不认证隐藏模型状态或数学真值。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="research", task_ids=(), _allow_core_transition=CORE_TRANSITION)
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 21:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_21")
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    if manifest.get("generation") != "core-cognition-generation-4" or manifest.get("counts", {}).get("core_units") != 36:
        raise SystemExit("CORE_GENERATION_4_NOT_READY")
    transition = json.loads((root / CORE_TRANSITION["transition"]).read_text(encoding="utf-8"))
    if transition.get("mapping_count") != 27 or transition.get("mapping_remainder") != 0 or transition.get("relation_counts") != {"PRESERVED_EXACT": 27}:
        raise SystemExit("CORE_TRANSITION_NOT_PRESERVING")
    merge = json.loads((root / "audit/understanding-chapter-merge-manifest.json").read_text(encoding="utf-8"))
    expected_merge = {
        "top_level_files": 29, "nested_files": 24, "union_files": 29,
        "same_name_pairs": 24, "identical_pairs": 15, "different_pairs": 9,
        "nonidentical_union_entries": 14, "top_level_unique": 5,
        "nested_unique": 0, "unresolved_nontrivial": 0,
    }
    if merge.get("counts") != expected_merge:
        raise SystemExit("UNDERSTANDING_MERGE_NOT_READY")

    direction = build_direction(root)
    panorama = build_panorama(root)
    c4_hash = R.sha((root / C4).read_bytes())
    core_hash = R.sha((root / "核心认知.md").read_bytes())
    manifest_hash = R.sha((root / "核心认知.manifest.json").read_bytes())
    curation_hash = R.sha((root / "scripts/audit/core-cognition-curation-v4.json").read_bytes())

    memory = f"""# 当前工作记忆

> Owner：顶层 `AGENTS.md`、Feature/rulings 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态/队列，不复制三件套或历史长文。

## 当前执行队列（2026-09-12）

1. 用户新增并已写入 core 的主方向：HoTT 自反真理验证是否在理论经济化与自我认证相交处产生不可停机、部分性或持续元层上升；同时考察存在/不存在双视角、最小理论覆盖、本项目悖论理论表达和 Gödel 研究。
2. 下一最小可验结果是 C4 的 `ERCF-1/2`：在选定 proof assistant 中定义 `R=A×S`、`α=π₁`、`FactorsThrough` 与 `ParadoxWitness`，同时给出平凡任务正例和观察敏感任务反例；完成后才进入 ERCF-3 自反编码。
3. C3 的资格保持性总方向、W51×RP-B01、自指与 R041 partiality 对照仍在全局视野中；当前新用户方向优先，不把旧 AI 排序覆盖用户新指令。
4. 历史交接开放项仍为 2,396 条 understanding claim 直接语义裁决、aistudio coverage、历史数学主张和关键 response→artifact/code/Git 因果；C4 不改变 22,226 条历史 register 分母。
5. 治理独立验证仍开放：固定 model/host/version 的 fresh Session/真实压缩后行为验收；Python EOF/hash 不替代模型行为。

## 当前已验证状态

- `核心认知.md` 为 generation-4/36 KC，SHA-256 `{core_hash}`；4 个登记来源、89 条消息、24 条纳入消息。generation-3 的 27/27 单元全部 `PRESERVED_EXACT`，新增 `KC-000028`–`KC-000036`。
- C4 共 724 行，SHA-256 `{c4_hash}`；它将验证任务分五层，提出 ERCF、factorization 充分性、存在/不存在四分法、E₀/E₁ 与 Gödel/元层边界；状态为 `PAPER_ONLY`。
- 当前最强数学判断：某些 cubical HoTT 风格系统的有限判断可归一化/判定；足够强有效理论不能同时拥有同层内部、总停机、健全、完备的全局真理自验证。二者不矛盾。
- 理解章节 merge manifest 当前为 top-level 29、nested 24、union 29、same-name 24、identical 15、different 9、top-only 5、nonidentical 14、unresolved nontrivial 0。
- project-local governance 3.1 是未提交 candidate；最近已封存 tag 仍为 `governance-v3.0.0`。本轮未获 commit/tag/push 授权。

## 当前证据上限

- 本轮 core/curation/transition、C4、方向/全景和治理机制可机器检查；C4 本身尚无 proof-assistant 证明或具体发散运行轨迹。
- 没有证明 HoTT 内部不一致、所有验证都会死循环、物理时空离散、Russell 标准悖论等价于无时序程序，或存在一个一致而 HoTT 完全无法保真解释的最小理论。
- 2LTT/QIIT/QIIRT/内部模型资料支持“自我元理论困难且常需分层/表示变化”，不自动证明 HoTT coverage failure。
- fresh Python 输入保真可验证；模型对三件套的实际理解仍不由工具认证。

## 恢复入口

按根 AGENTS 全文加载 core→direction→panorama。当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001` 并读 C4；进入机器证明时再读 C3、Theory Schema 和选定 proof assistant 接口。不要直接跳到 ERCF-3：先完成 ERCF-1/2 的正反对照。
"""
    frontier = """# HoTT 研究前沿（S022 自反真理验证与理论经济）

本文件是当前注意力槽，不是数学结论数据库。C4 已回答用户问题但证据等级为 `PAPER_ONLY`；本轮没有 proof-assistant 或具体发散运行。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 当前用户主方向 | ERCF：理论经济化抽象与反射性自我认证何时迫使部分性、不完备或元层上升 | active-user-direction / paper-only | 明确区分 V1 proof checking、V2 normalization、V3 proof search、V4 truth/soundness、V5 internal total self-verifier |
| 第一最小可验结果 | ERCF-1/2：`α:R→A` 的任务相对 factorization、平凡任务正例与观察敏感反例 | ready-for-formalization | 选定 Lean/Agda/HoTT 片段，证明 `ParadoxWitness(α,J) → ¬FactorsThrough(α,J)`，保存源码与真实运行 |
| 战略自反深化 | ERCF-3 × W51/RP-B01：Code/quote/eval/provability/ASK 与验证器自身 | blocked-on-walking-skeleton-and-calculus | 只在 exact calculus、宇宙和 derivability 条件固定后构造 diagonal；不以一般 Gödel 口号冒充 HoTT 特有结论 |
| 最小覆盖边界 | 一致、操作语义清楚、观察规格明确而 HoTT 无法保真解释的最小理论 | open / no-witness | 区分语法可写、内部模型、保真解释和正确拒绝；非法 `U:U`/非正递归只计 `DEFENSE_WORKS` |
| 对照与历史支线 | cubical normalization 正控制、R041 bind/race、R034 native、guard/online causality | retained / not-current-first | 用于反驳过强结论和比较局部不变性；不覆盖当前用户主方向 |

判词保持：`DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`。新增 ERCF 结论也必须区分实际 divergence、无总判定器和元理论不可闭合。
"""
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    additions = """
27. “一个有限证明可检查/一个系统有归一化”与“所有命题可自动决定/理论能证明自身整体可靠”属于不同层次；若不先拆 V1–V5，会把正面元理论结果和哥德尔边界写成伪矛盾。
28. 理论经济必须相对于任务族定义：`J` 通过 `α` 分解才是抽象对该任务充分；非单射抽象并非对所有任务失败，但必有观察能击穿其全局无损声明。
29. 省略、商去、逻辑否定和理想化添加是四种不同理论操作；“理论中不存在 F”与“理论断言 ¬F”不能互换。用户的存在/不存在双视角应作为现实相对语义保留，而非无条件对象逻辑等价。
30. core generation 更新和 STATE checkpoint 存在双资源过渡：先生成新 core 会让旧 STATE 的动态 generation 校验失败。runtime 3.1 只在给出 manifest+transition、旧/新 generation 和零 remainder 的窄迁移声明时允许 checkpoint 建立基线；普通 Session 仍 fail closed。
"""
    if "27. “一个有限证明可检查" not in lessons:
        lessons += additions
    resume = """# 接续指针

## 每个新 Session/压缩后的固定恢复

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md` 和本地治理 Skill/PROTOCOL/LOAD_SET/STATE。
2. 严格全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`；当前为 generation-4/36 KC，manifest/旧 receipt 不能替代。
3. 当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001`，全文读 `理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；需战略背景再读 C3/A11/self-reference/RP-B01。
4. 数学研究使用 research profile，先 query stable record 再显式 task hydrate；结束按当前 manifest 全部 KC 人工回评，并交叉更新 core/direction/panorama 的正确 owner。

## 当前停止点

S022 已把用户当前原文纳入 generation-4 的 KC-000028–000036，并完成 C4 论证：HoTT 的有限 proof checking 不必循环；无界证明搜索和同层全局自验证在标准条件下会失去总停机、完备、健全或内部可证之一；最准确候选是理论经济—反射自证回环 ERCF。下一步不是重复泛泛自指讨论，而是先机器证明 ERCF-1/2 的 factorization 正/反例，再决定 ERCF-3 的 exact calculus。当前没有 HoTT 内部矛盾、具体发散轨迹或最小 coverage no-go。
"""

    state["revision"] = 22
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "generation": "core-cognition-generation-4",
        "path": "核心认知.md",
        "manifest": "核心认知.manifest.json",
        "curation": "scripts/audit/core-cognition-curation-v4.json",
        "transition": CORE_TRANSITION["transition"],
        "kc_count": 36,
        "core_sha256": core_hash,
        "manifest_sha256": manifest_hash,
        "curation_sha256": curation_hash,
    }
    state["load_policy"]["runtime_version"] = "3.1.0"
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "HOTT_SELF_VALIDATION_ECONOMY_PAPER_SYNTHESIS_COMPLETE_FORMALIZATION_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "new_math_research_started": True,
        "next_minimal_verification": "Formalize ERCF-1/2 factorization positive and negative controls in one selected proof assistant before attempting reflective ERCF-3.",
    })
    semantic = "CORE_GENERATION_4_THEORY_ECONOMY_REFLECTION_USER_DIRECTION_ACTIVE"
    state["projection"]["status"] = semantic
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record.update({
        "projection_generation": "20260912-direction-006",
        "semantic_status": semantic,
        "scope": "Cross-source portfolio with the active user ERCF/theory-economy/self-validation direction, qualification-preservation umbrella and retained historical branches.",
    })
    append_unique(direction_record["full_sources"], C4)
    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record.update({
        "projection_generation": "20260912-outcome-006",
        "semantic_status": semantic,
        "scope": "Cross-source panorama including generation-4 core and the paper-only C4 self-validation/economy result; no native proof or HoTT inconsistency claimed.",
    })
    append_unique(panorama_record["full_sources"], C4)
    gen3 = state["records"]["A-CORE-GENERATION-3-001"]
    gen3["lifecycle_status"] = "HISTORICAL"
    gen3["resolution"] = {
        "reason": "Generation-3 remains the exact 27-KC historical baseline; generation-4 preserves all 27 payloads and adds nine direct-user units.",
        "evidence": ["audit/core-cognition-generation-4-transition-20260912.json", "核心认知.manifest.json"],
    }
    state["records"]["A-CORE-GENERATION-4-001"] = {
        "kind": "core_generation_migration",
        "path": CORE_TRANSITION["transition"],
        "status": "closed",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["A-CORE-GENERATION-3-001"],
        "full_sources": [
            "核心认知.md", "核心认知.manifest.json",
            "scripts/audit/core-cognition-curation-v4.json",
            "sources/prompts/Codex-自反真理验证与理论经济学-用户原文-20260912.md",
            CORE_TRANSITION["transition"], "scripts/audit/verify_core_cognition.py", IMPLEMENTATION_EVIDENCE,
        ],
        "source_hashes": {"核心认知.md": core_hash, C4: c4_hash},
        "scope": "Incrementally add nine exact direct-user self-validation/economy units while preserving every generation-3 KC byte-for-byte; current denominator 36 KC across four sources and 89 registered messages.",
    }
    state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"] = {
        "kind": "research_direction_result",
        "path": C4,
        "status": "review_required",
        "lifecycle_status": "OPEN_ISSUE",
        "evidence_status": "PAPER_ONLY",
        "depends_on": ["A-CORE-GENERATION-4-001", "A-HOTT-RESEARCH-DIRECTION-001"],
        "full_sources": [
            C4, "核心认知.md", "方向追踪.md", "全景视野.md",
            "HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md", IMPLEMENTATION_EVIDENCE,
        ],
        "source_hashes": {C4: c4_hash},
        "mathematical_status": "CONDITIONAL_METAMATHEMATICAL_SYNTHESIS_NOT_NATIVE_VERIFIED",
        "scope": "Distinguish finite checking from proof search and global self-truth; formulate ERCF, task-relative factorization, existence/nonexistence distinctions, minimum-theory coverage criteria and Gödel/self-metatheory boundaries. Formalization and concrete divergence remain open.",
    }
    for group in ("review_due", "unresolved"):
        append_unique(state[group], "A-HOTT-SELF-VALIDATION-ECONOMY-001")
    state["records"]["A-UNDERSTANDING-RECONCILIATION-001"]["scope"] = (
        "File-level reconciliation is complete and non-destructive for the current 29/24 inventory "
        "(24 same-name pairs, 15 identical, 9 different, 5 top-only); C4 is a new top-level synthesis, while semantic equivalence and 2,396 historical claim review remain open."
    )
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-PLAN-20260912-021-HOTT-RESEARCH-DIRECTION", "A-HOTT-SELF-VALIDATION-ECONOMY-001"],
        "full_sources": [session_path, audit_path, runs_path, C4, "核心认知.md", "方向追踪.md", "全景视野.md", IMPLEMENTATION_EVIDENCE, "scripts/audit/prepare_self_validation_economy_checkpoint.py"],
        "source_hashes": {C4: c4_hash, "核心认知.md": core_hash},
        "mathematical_status": "PAPER_ONLY_CONDITIONAL_SYNTHESIS_NO_PROOF_ASSISTANT_RUN",
        "cognition_status": "GENERATION_4_AND_ERCF_DIRECTION_DOCUMENTED_AND_ROUTED",
        "scope": "Record the user's new direct cognition, answer the HoTT self-validation/economy/Gödel questions in C4, update the three-way projections and audit all 36 KC; no internal inconsistency or native proof claimed.",
    }
    session = f"""# {SESSION_ID}

- 触发：用户要求把当前思想原文记录到 core，并论述 HoTT 自反真理验证、理论经济、最小覆盖、存在/不存在双视角和 Gödel 研究。
- 认知输入：本轮按固定顺序全文读取 generation-3 三件套后，查阅 C3/A11/RP-B01/自指调查，并核验 HoTT Book、cubical normalization、2LTT、内部元理论与 Gödel 形式化一手资料。
- 核心变更：generation-4 保留旧 27 KC，新增 KC-000028–000036；source/curation/transition 可逐字重建。
- 数学结论：有限 proof checking 不等于全局真理判定；ERCF 描述经济化抽象与反射性全局认证相交时的部分性/不完备/元层上升候选。
- 产物：`{C4}`；同步 direction v1.3、panorama v1.3、STATE revision 22、MEMORY/FRONTIER/LESSONS/RESUME、29/24 merge inventory 和 36-KC 回评。
- 证据边界：`PAPER_ONLY`；没有 proof-assistant、具体发散轨迹、HoTT 内部矛盾、物理离散性或最小 coverage no-go。
- Git：checkpoint applied locally；未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "cognition": {
            "core_generation": "core-cognition-generation-4", "core_units_read": 36,
            "three_way_order": ["核心认知.md", "方向追踪.md", "全景视野.md"],
            "core_transition": {"old_units": 27, "preserved_exact": 27, "new_units": 9, "remainder": 0},
        },
        "artifacts": {"c4_lines": 724, "c4_sha256": c4_hash, "merge_counts": expected_merge},
        "pre_checkpoint_verification": {
            "core_tests": "7/7 PASS", "core_verifier": "PASS_WITH_SCOPE",
            "runtime_tests": "28/28 PASS including core-transition positive/negative",
            "understanding_merge": "PASS 29/24/29",
        },
        "research_status": {
            "result": "PAPER_ONLY", "proof_assistant": "NOT_RUN",
            "concrete_divergence": "NOT_PRODUCED", "internal_inconsistency": "NOT_ESTABLISHED",
        },
        "post_checkpoint_required": [
            "KC audit 36/36 verify", "three-way verify", "fresh full-trio receipt revision 22",
            "projection freshness", "source/merge/history/core full regression", "JSON parse and git diff --check",
        ],
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    texts = {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons + "\n",
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session,
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly requested durable core recording and a new document answering the HoTT self-validation, theory-economy, minimum-coverage and Gödel questions; project governance requires atomic projection/state/memory and per-KC audit alignment.",
        "load_profile": "research", "task_ids": [], "core_transition": CORE_TRANSITION,
        "files": [
            {"path": relative, "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None, "text": value}
            for relative, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "session_id": SESSION_ID, "revision": 22, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
