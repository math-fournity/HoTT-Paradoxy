#!/usr/bin/env python3
"""Prepare revision 21 for the source-bounded HoTT research-direction proposal."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-PLAN-20260912-021-HOTT-RESEARCH-DIRECTION"
C3_PATH = "理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md"
R041_PATH = "与Web GPT 交流用的文件夹/PROOF_NOTE(20260912-061537) - R401.md"
SPEC = importlib.util.spec_from_file_location("runtime_hott_research_direction", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def replace_count(text: str, old: str, new: str, expected: int) -> str:
    count = text.count(old)
    if count != expected:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}:{expected}")
    return text.replace(old, new)


def replace_line_prefix(text: str, prefix: str, replacement: str) -> str:
    lines = text.splitlines()
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) != 1:
        raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(indexes)}")
    lines[indexes[0]] = replacement
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def replace_span(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"SPAN_MARKER_COUNT:{start}:{text.count(start)}:{end}:{text.count(end)}")
    begin = text.index(start)
    finish = text.index(end, begin) + len(end)
    return text[:begin] + replacement + text[finish:]


def append_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    assessments: dict[str, tuple[str, str, str, str]] = {
        "KC-000001": (
            "ALIGNED",
            "把“找什么、怎么找、凭什么”落实为资格保持性总问题、两个研究包和分级判词。",
            "C3 第0、1、3、10节",
            "具体数学包尚未执行。",
        ),
        "KC-000002": (
            "ALIGNED",
            "每个候选必须先固定 bare/axiomatic、cubical、guarded/clocked 等 Theory Schema 和真实消去规则。",
            "C3 第1、5.1、6.4节",
            "首个 partiality 构造与工具链尚未选定。",
        ),
        "KC-000003": (
            "DEEPENED",
            "把合取前提扩展成 Q0—Q7 资格链，要求逐项指出哪一项被删除、替换或加强。",
            "C3 第1、2节",
            "资格链是审计顺序，不是已证普遍线性蕴含。",
        ),
        "KC-000004": (
            "ALIGNED",
            "保留反证与现实过程前提；不把表示边界直接写成内部矛盾。",
            "C3 第3、5.5节",
            "尚无达到 NATURAL_USAGE_MISMATCH 的实例。",
        ),
        "KC-000005": (
            "ALIGNED",
            "先推进可证伪的 partiality 对照，再按结果判断防御、边界或现实失配，不预设最终归因。",
            "C3 第4.2、10、11节",
            "本轮仅制定方向。",
        ),
        "KC-000006": (
            "DEEPENED",
            "时间机制扩展为完成先后、在线可用性、因果、context 和资源，不再收窄为稠密性。",
            "C3 第1、5.2、7节",
            "物理时间桥梁仍未建立。",
        ),
        "KC-000007": (
            "ALIGNED",
            "历史知识和训练模式只负责生成候选形状，结论必须回到具体 HoTT 接口和直接证据。",
            "C3 第1、9.3节",
            "原创性尚未检索或认证。",
        ),
        "KC-000008": (
            "ALIGNED",
            "历史时间悖论继续作为形态启发，但主攻转为抽象与后续操作的资格保持性。",
            "C3 第0、7节",
            "没有把历史悖论直接翻译成 HoTT 定理。",
        ),
        "KC-000009": (
            "DEEPENED",
            "要求精确定位 quotient、QIIT、guard、提取或 reflection 中发生资格变化的那一步。",
            "C3 第1、5、6节",
            "真实 partiality/QIIT 接口待固定。",
        ),
        "KC-000010": (
            "DEEPENED",
            "用四级判词把现实相对非现实性与 HoTT 内部不一致严格分开，主目标是自然使用失配。",
            "C3 第3节",
            "当前没有 HoTT 内部矛盾证据。",
        ),
        "KC-000011": (
            "DEEPENED",
            "R041 的 bind/race 对照把抽象推演与程序显式时序放进同一 operation-closure 检验。",
            "C3 第4.2、5.2—5.4节",
            "尚未在真实 HoTT 构造中核验。",
        ),
        "KC-000012": (
            "DEEPENED",
            "ASK 被操作化为 Q0—Q7，并在形成、截断、商消去、组合、提取和交付处反复检查。",
            "C3 第1、2节",
            "本轮未执行具体 ASK 审计。",
        ),
        "KC-000013": (
            "DEEPENED",
            "明确 ASK 是动态资格追踪而非禁止研究的总门禁；每个工作单元必须形成可判别结果。",
            "C3 第1、9.5、10节",
            "自然 consumer 尚未选定。",
        ),
        "KC-000014": (
            "DEEPENED",
            "将第二方向落实为数学分类—有效交付—有效自反三级断裂，并与第一方向统一。",
            "C3 第2、4.1、6节",
            "B01-TARGET 仍开放。",
        ),
        "KC-000015": (
            "DEEPENED",
            "把“抽象即否定”改写为可查的遗漏量：结果商删去完成先后后，race/timeout 资格不再保持。",
            "C3 第1、5.3、5.4节",
            "这目前只是 chosen abstraction 的边界候选。",
        ),
        "KC-000016": (
            "ALIGNED",
            "Russell 形成/落定模型保留为支撑方向，不用一般 validator 拒绝冒充主攻 HoTT 悖论。",
            "C3 第9.2节；方向追踪 DIR-L-RUSSELL-FORMATION",
            "本轮未推进 Russell 形式化。",
        ),
        "KC-000017": (
            "ALIGNED",
            "全文使用用户 core 监督训练惯性，并把本结论显式标为 AI proposal 而非用户 ruling。",
            "C3 元数据与第12节",
            "是否采用该排序仍由用户决定。",
        ),
        "KC-000018": (
            "DEEPENED",
            "Z 铁律的否定被落实为 identity/operation/observable 的具体删除，而非抽象口号。",
            "C3 第1、5.4节",
            "真实消费者中的工具性异化尚未发现。",
        ),
        "KC-000019": (
            "ALIGNED",
            "保留合取真值和完成困难，但把稠密空间降为众多可能机制之一。",
            "C3 第1、7、9.4节",
            "稠密连续桥梁本轮未推进。",
        ),
        "KC-000020": (
            "ALIGNED",
            "悖论仍服务反证；运动量子化只作为需物理桥梁的候选，不冒充当前事实。",
            "C3 第9.4节",
            "无现实物理认证。",
        ),
        "KC-000021": (
            "ALIGNED",
            "R041 paper、代码、测试、Git、native HoTT 和现实 consumer 被分成不同证据层。",
            "C3 第10 Gate 0、第13节",
            "R041 执行谱系与 R034 native 均开放。",
        ),
        "KC-000022": (
            "DEEPENED",
            "A/B 两类现实相对悖论被统一为资格保持性断层，同时保留不同责任方向。",
            "C3 第0、2节",
            "两类均未形成最终实例。",
        ),
        "KC-000023": (
            "DEEPENED",
            "要求把时序处理定位到 race/timeout、prefix causality、guard translation 和 exact consumer。",
            "C3 第5、7节",
            "具体 library/version 尚待选择。",
        ),
        "KC-000024": (
            "DEEPENED",
            "两类时序候选被收敛为 partiality contextual adequacy 与在线因果，附带停止条件。",
            "C3 第5、7、11节",
            "在线因果仍为探索位。",
        ),
        "KC-000025": (
            "ALIGNED",
            "解释自指难找是因为必须先有 syntax、quote、substitution、eval、provability 与闭合接口。",
            "C3 第6.3、9.2节",
            "exact calculus 尚未固定。",
        ),
        "KC-000026": (
            "DEEPENED",
            "把“HoTT 不能越过自指”转成有效自我 ASK 的可检验研究包，而非旧哥德尔空间口号。",
            "C3 第6.3、10 Work Unit 5",
            "新的 HoTT 特定不可能定理尚未建立。",
        ),
        "KC-000027": (
            "DEEPENED",
            "将“逻辑+几何+程序继承程序界限”确立为战略主论题，并用 RP-B01 和 reflection 接口分阶段推进。",
            "C3 第4.1、6、14节",
            "自然 HoTT 分类→执行接口仍是关键未知。",
        ),
    }
    units = manifest["units"]
    if set(assessments) != {str(unit["id"]) for unit in units}:
        raise ValueError("AUDIT_ASSESSMENT_DENOMINATOR_MISMATCH")
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(units)}`。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    for unit in units:
        unit_id = str(unit["id"])
        relation, assessment, evidence, unresolved = assessments[unit_id]
        counts[relation] = counts.get(relation, 0) + 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | "
            f"{assessment} | {evidence}; 核心认知.md {unit_id} | {unresolved} |"
        )
    lines.extend(
        [
            "",
            "## 三件套交叉与更新归属",
            "",
            "- core_change: `NO` — 本轮没有新的用户原文或用户明确工作意识变更；generation-3/27 KC 不改。",
            "- direction_change: `YES_AI_PROPOSAL` — 新增资格保持性总方向，明确 B 战略主线与 A 战术先手；不冒充用户已采纳。",
            "- panorama_change: `YES_DOCUMENTED_RESULT` — 登记 C3 研究战略及其证据上限，并同步 28/24 理解章节 inventory。",
            "- update_decision: `C3 进入理解章节 current C 系列；方向/全景/STATE/MEMORY 同步；core 与 rulings 不改。`",
            "- cross_conflicts: `RESOLVED_BY_STRATEGIC_TACTICAL_DISTINCTION` — A11/C1 的 B 优先与 R041 的可执行成熟度不冲突：B 是战略主论题，A 是首个工作包。",
            "- unresolved: `R041 code/25 tests/cf58f27/container；真实 partiality/QIIT consumer；B01-TARGET；exact self-reflection calculus；R034 native；用户是否采纳该 AI 排序。`",
            "",
            "## 汇总",
            "",
            f"`DEEPENED={counts.get('DEEPENED', 0)} / ALIGNED={counts.get('ALIGNED', 0)} / "
            f"CORRECTED={counts.get('CORRECTED', 0)} / TENSION={counts.get('TENSION', 0)} / "
            f"DEVIATED={counts.get('DEVIATED', 0)} / NOT_TOUCHED={counts.get('NOT_TOUCHED', 0)}`。"
            "本回评证明公开文本逐项存在，不认证隐藏模型理解或数学真值。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    # Direct task evidence was hydrated before this preparer runs.  The
    # checkpoint itself uses the research profile without re-hydrating the
    # prior review record, because this transaction deliberately changes two
    # of that historical review's full-source projections.
    task_ids: list[str] = []
    plan = R.plan(root, profile="research", task_ids=task_ids)
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v2" or state.get("revision") != 20:
        raise SystemExit("EXPECTED_STATE_V2_REVISION_20")
    if not (root / C3_PATH).is_file():
        raise SystemExit("C3_DOCUMENT_MISSING")
    merge = json.loads((root / "audit/understanding-chapter-merge-manifest.json").read_text(encoding="utf-8"))
    expected_counts = {
        "top_level_files": 28,
        "nested_files": 24,
        "union_files": 28,
        "same_name_pairs": 24,
        "identical_pairs": 15,
        "different_pairs": 9,
        "nonidentical_union_entries": 13,
        "top_level_unique": 4,
        "nested_unique": 0,
        "unresolved_nontrivial": 0,
    }
    for key, expected in expected_counts.items():
        actual = merge.get("counts", {}).get(key)
        if actual != expected:
            raise SystemExit(f"MERGE_COUNT_NOT_READY:{key}:{actual}:{expected}")

    old_semantic = "CORE_GENERATION_3_R041_PAPER_REVIEWED_EXECUTION_OPEN"
    new_semantic = "CORE_GENERATION_3_QUALIFICATION_PRESERVATION_AI_STRATEGY_PROPOSED"
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(
        direction,
        "integrated-direction-portfolio/v1.1",
        "integrated-direction-portfolio/v1.2",
    )
    direction = replace_once(
        direction,
        "integrated-direction-portfolio:v1.1",
        "integrated-direction-portfolio:v1.2",
    )
    direction = replace_count(direction, old_semantic, new_semantic, 2)
    direction = replace_once(direction, "source_state_revision: 20", "source_state_revision: 21")
    direction = replace_once(
        direction,
        "projection_generation: 20260912-direction-004",
        "projection_generation: 20260912-direction-005",
    )
    divider = "|---|---|---|---|---|---|---|---|"
    umbrella_row = (
        "| `DIR-TOP-QUALIFICATION-PRESERVATION` | ASK／完成资格在 HoTT 抽象、组合、提取与反射中的保持性；"
        "统一 A/B 两类现实相对悖论 | 用户 generation-3 core；当前 AI 的 C3 综合（非用户 ruling） | "
        "`NEXT_CANDIDATE` | `COMPUTATIONAL_LEGITIMACY`, `TIME_AND_TEMPORALITY`, `SELF_REFERENCE`, "
        "`PARADOX_DISCOVERY` | `OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-W-R041-PAPER`、`OUT-W-RP-B01` | "
        "若用户启动数学研究，先执行真实 partiality quotient/QIIT 的 bind×race/timeout 对照；"
        "战略上继续定位数学分类→有效交付→有效自我 ASK 的自然升级点 | "
        "`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md`；`核心认知.md` |"
    )
    direction = replace_once(direction, divider, divider + "\n" + umbrella_row)
    direction = replace_line_prefix(
        direction,
        "| `DIR-U-A-REALITY-RELATIVE`",
        "| `DIR-U-A-REALITY-RELATIVE` | 现实可完成过程被明确 Think in HoTT 设定/解释引入额外完成困难 | "
        "用户原始方向；WebGPT `U-GOAL-20260910-001` | `ACTIVE_USER_DIRECTION` | "
        "`PARADOX_DISCOVERY`, `TIME_AND_TEMPORALITY`, `BEING_AND_BECOMING` | "
        "`OUT-TOP-CORE-FOUNDATION`、`OUT-TOP-HOTT-RESEARCH-STRATEGY`；具体 HoTT 实例未完成 | "
        "按 C3 Q0—Q7 固定同一现实任务和资格跃迁；首个判别对象为 partiality quotient 下可执行 race 与不可下降 race 的反差 | "
        "`核心认知.md`；`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md` |",
    )
    direction = replace_line_prefix(
        direction,
        "| `DIR-U-B-EFFECTIVE-DELIVERY`",
        "| `DIR-U-B-EFFECTIVE-DELIVERY` | 数学上取得分类/存在后被提升为尚未取得的有效求解或实际交付 | "
        "用户原始方向；WebGPT `U-DUAL-DIRECTION-JSON-001` | `ACTIVE_USER_DIRECTION` | "
        "`COMPUTATIONAL_LEGITIMACY`, `BEING_AND_BECOMING`, `EVIDENCE_DISCIPLINE` | "
        "`OUT-L-CORE-MATHEMATICAL`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-W-RP-B01`；自然升级点未形成 | "
        "以 W51×RP-B01 为战略主线，固定数学分类、有效总实现、现实交付与有效自我 ASK 四层，并找到一个真实 HoTT 接口的承诺或拒绝 | "
        "`核心认知.md`；`workspace/.codex/research/hott/candidates/RP-B01/`；`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md` |",
    )
    direction = replace_line_prefix(
        direction,
        "| `DIR-L-SELF-REFLECTION`",
        "| `DIR-L-SELF-REFLECTION` | self-reference、reflection、对象理论—元理论边界；与 W51“程序继承计算界限”合流 | "
        "LocalGPT、WebGPT `P-SELF-*`；KC-000025–000027 | `NEXT_CANDIDATE` | "
        "`SELF_REFERENCE`, `HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY` | "
        "`OUT-W-REFLECTION-FAMILY`、`OUT-W-RP-B01`、`OUT-TOP-HOTT-RESEARCH-STRATEGY` | "
        "作为 B 战略深层：在 Code/quote/substitution/evaluation/provability 固定后构造“有效自我 ASK”最小接口；"
        "不复活 `Map(1,G)` 或把一般 Gödel 口号当 HoTT 实例 | "
        "`HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`；`理解章节/A11-开放问题与悬空接头.md`；"
        "`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md` |",
    )
    direction = replace_line_prefix(
        direction,
        "| `DIR-W-RACE-TIMEOUT`",
        "| `DIR-W-RACE-TIMEOUT` | 部分计算结果等价的操作闭包：代表层 `bind` 相容、`race/timeout` 时序敏感，"
        "以及商/QIIT continuation 与 contextual equivalence 的边界 | WebGPT R039；用户提供的数学 R041 PROOF_NOTE；"
        "一手 partiality 文献 | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, "
        "`PARADOX_DISCOVERY` | `OUT-W-R039`、`OUT-W-R041-PAPER`、`OUT-TOP-HOTT-RESEARCH-STRATEGY` | "
        "这是首个可执行研究包：证据恢复仅为 Gate 0；随后选一个真实 quotient/QIIT/guarded partiality，"
        "证明 bind 正例、race/timeout 负例、上下文等价和最小富化；不再扩充延迟枚举 | "
        "`与Web GPT 交流用的文件夹/PROOF_NOTE(20260912-061537) - R401.md`；"
        "`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md` |",
    )
    direction = replace_line_prefix(
        direction,
        "| `DIR-W-RP-B01`",
        "| `DIR-W-RP-B01` | W51×RP-B01：命题 LEM 下的数学分类、有效总实现、无神谕对角闭包与自然 Think-in-HoTT 交付提升 | "
        "WebGPT `P-RP-B01`；用户 KC-000027；A11.1 | `NEXT_CANDIDATE` | "
        "`COMPUTATIONAL_LEGITIMACY`, `PARADOX_DISCOVERY`, `SELF_REFERENCE` | "
        "`OUT-W-RP-B01`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-TOP-HOTT-RESEARCH-STRATEGY` | "
        "这是战略主线：不再以一般停机定理冒充结果；固定真实 HoTT 计算/提取接口，定位数学分类资格何处被提升为统一有效交付，"
        "再与有效自我 ASK 合流 | `workspace/.codex/research/hott/candidates/RP-B01/`；"
        "`理解章节/A11-开放问题与悬空接头.md`；`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md` |",
    )
    direction = replace_line_prefix(
        direction,
        "| `DIR-G-UNDERSTANDING-RECONCILIATION`",
        "| `DIR-G-UNDERSTANDING-RECONCILIATION` | 两个理解章节的逐文件语义融合和当前 canonical 路由 | "
        "用户当前要求、顶层计划 | `SUPPORTING_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | "
        "`OUT-UNDERSTANDING-MERGE`（设计） | 当前 28/24 inventory 已逐文件处置；继续按 2,396 条历史 claim 的用户选择范围做直接语义/数学复核 | "
        "`理解章节/`；`AI对话录/理解章节/`；`audit/understanding-chapter-merge-manifest.json` |",
    )
    old_priority = (
        "当前优先顺序分成两条队列，防止治理接管任务与数学研究互相冒充：\n\n"
        "1. **当前交接/审计队列**：`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-E-LOCAL-HISTORY-COVERAGE` 与数学 R041 的 source/code/run/Git 谱系补齐；2,396 条 claim 句级裁决仍按用户选中的 stable record 推进。\n"
        "2. **未来恢复数学研究时的 B 主线**：`DIR-W-RP-B01` × `DIR-L-SELF-REFLECTION`，把 W51“逻辑+几何+程序”落实为自然 Think-in-HoTT 接口中的数学分类资格/有效交付资格差异。\n"
        "3. **未来恢复数学研究时的 A 主线**：`DIR-W-RACE-TIMEOUT`。R041 已给代表层 `bind/race` 分离；下一步只推进真实 quotient/QIIT/guarded 接口，不重复延迟图枚举。\n"
        "4. **探索位**：`DIR-L-TIME-WORK-DIMENSION` 的完整流函数/在线因果策略，以及 `DIR-L-GUARD-ERASURE`、`DIR-L-SAME-FUNCTION-DIFFERENT-TIME`；必须给出真实接口和自然任务。\n"
        "5. **验证位**：`DIR-W-PATH-CERTIFICATE` 的 R034 Cubical Agda 原生核查；它提高证据强度，不替代 A/B 两条发现主线。\n"
        "6. 其余历史 `REVIEW_REQUIRED` 分支只在新证据、用户明确重开或当前候选依赖它们时进入。\n\n"
        "不因方向数量增加而自动开始所有方向；不因 WebGPT `active` 列表存在而恢复旧数学研究；不因某方向在 `核心认知` 中被提及就把它提升为当前任务。用户当前目标、`MEMORY` current queue、直接证据和本表的下一判别动作共同决定资格。"
    )
    new_priority = (
        "当前优先顺序区分“用户目标”“AI 战略建议”“首个工作包”和“证据/治理队列”，防止一种优先级冒充另一种：\n\n"
        "1. **总方向建议（尚待用户采纳）**：`DIR-TOP-QUALIFICATION-PRESERVATION`，以 ASK／完成资格在抽象、组合、提取和反射中的保持性统一 A/B 两类目标。\n"
        "2. **战略主论题**：`DIR-W-RP-B01` × `DIR-L-SELF-REFLECTION`。目标是定位数学分类→统一有效交付→有效自我 ASK 的自然资格升级点；其重要性最高，但当前 HoTT 特定接口证据较弱。\n"
        "3. **首个可执行研究包**：`DIR-W-RACE-TIMEOUT`。从数学 R041 的 bind/race 分离推进真实 partiality quotient/QIIT、contextual equivalence 和最小时序富化；它证据最成熟，但不能自动代表最终主论题。\n"
        "4. **探索位**：完整流函数/在线因果、guard 擦除和同函数异时；仅在真实 guarded/clocked 接口与自然任务固定后进入。\n"
        "5. **独立验证位**：R034 Cubical Agda；它提高 path/transport 证据强度，不替代 A/B 发现主线。\n"
        "6. **证据/治理队列**：R041 code/25-test/`cf58f27`/container 谱系、2,396 条 claim、aistudio coverage 和历史因果映射继续按当前用户任务选择；它们不冒充数学进展。\n\n"
        "本轮只形成并落盘研究战略，没有启动任何数学证明、代码模型、证明助手或外部接口审计。未来若用户启动研究，每个自然工作单元只推进一个可检查构造，并按 C3 的四级判词与停止条件收敛。"
    )
    direction = replace_span(
        direction,
        "当前优先顺序分成两条队列，防止治理接管任务与数学研究互相冒充：",
        "不因方向数量增加而自动开始所有方向；不因 WebGPT `active` 列表存在而恢复旧数学研究；不因某方向在 `核心认知` 中被提及就把它提升为当前任务。用户当前目标、`MEMORY` current queue、直接证据和本表的下一判别动作共同决定资格。",
        new_priority,
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(
        panorama,
        "integrated-outcome-panorama/v1.1",
        "integrated-outcome-panorama/v1.2",
    )
    panorama = replace_once(
        panorama,
        "integrated-outcome-panorama:v1.1",
        "integrated-outcome-panorama:v1.2",
    )
    panorama = replace_count(panorama, old_semantic, new_semantic, 2)
    panorama = replace_once(panorama, "source_state_revision: 20", "source_state_revision: 21")
    panorama = replace_once(
        panorama,
        "projection_generation: 20260912-outcome-004",
        "projection_generation: 20260912-outcome-005",
    )
    strategy_result = (
        "| `OUT-TOP-HOTT-RESEARCH-STRATEGY` | C3 将后续研究收敛为 ASK／完成资格保持性，"
        "区分 B 战略主论题 W51×RP-B01×自指与 A 战术先手 partiality quotient×race/timeout，"
        "并给出四级判词、定理阶梯、自然桥梁、执行顺序和停止条件 | "
        "`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY`、"
        "`DIR-W-RACE-TIMEOUT`、`DIR-W-RP-B01`、`DIR-L-SELF-REFLECTION` | 当前顶层 AI 综合 | `DOCUMENTED` | "
        "研究战略已由 generation-3 core、C1/C2、A11、R041、RP-B01 和自指调查逐项支撑；"
        "战略/战术不再混排，所有候选有可证伪判词和停止边界 | "
        "不证明用户已采纳，不证明任何新 HoTT 定理、现实相对悖论或自然 consumer 已找到；本轮未启动数学研究 | "
        "`理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md`；`核心认知.md`；"
        "`workspace/.codex/research/hott/candidates/RP-B01/`；`与Web GPT 交流用的文件夹/PROOF_NOTE(20260912-061537) - R401.md` |"
    )
    panorama = replace_once(
        panorama,
        "| `OUT-UNDERSTANDING-MERGE`",
        strategy_result + "\n| `OUT-UNDERSTANDING-MERGE`",
    )
    panorama = replace_line_prefix(
        panorama,
        "| `OUT-UNDERSTANDING-MERGE`",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 28/24 文件 inventory；"
        "24 个同名对中 15 对字节相同、9 对差异；顶层 C0/C1/C2/C3 共 4 个独有文件"
        "（nonidentical union entries=13）；逐文件处置已生成 | `DIR-G-UNDERSTANDING-RECONCILIATION` | "
        "顶层只读审计 | `VERIFIED_WITH_SCOPE` | 每个 union 文件有 hash、line diff、处置决定、回滚源和非破坏性验证；"
        "C3 为 top-level current AI strategy proposal，nested 历史源仍保留 | "
        "不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；"
        "2,396 条旧 claim 未因 C3 自动裁决 | `audit/understanding-chapter-merge-manifest.json`；"
        "`scripts/audit/verify_understanding_merge.py`；`理解章节/`；`AI对话录/理解章节/` |",
    )
    panorama = replace_once(
        panorama,
        "5. WebGPT 与 LocalGPT 的关键 response→artifact/code→Git 因果映射仍需在具体研究条目上加深；尤其数学 R041 当前只有用户提供的 PROOF_NOTE，源码、25 项测试原始输出、`cf58f27` 与增量容器谱系尚未取得。",
        "5. WebGPT 与 LocalGPT 的关键 response→artifact/code→Git 因果映射仍需在具体研究条目上加深；尤其数学 R041 当前只有用户提供的 PROOF_NOTE，源码、25 项测试原始输出、`cf58f27` 与增量容器谱系尚未取得。\n"
        "6. C3 只是一份证据受限的 AI 研究战略；用户是否采纳、真实 partiality/QIIT consumer、B01-TARGET、有效自我 ASK 演算和相应 native proof 均未完成。",
    )

    memory = """# 当前工作记忆

> Owner：顶层 `AGENTS.md`、Feature/rulings 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态/队列，不复制三件套或历史长文。

## 当前执行队列（2026-09-12）

1. 用户要求判断后续 HoTT 悖论方向并写入新文档；C3 已完成。当前 AI 建议以“ASK／完成资格在抽象、组合、提取与反射中的保持性”统一 A/B 两类目标；这是 AI proposal，不是用户已采纳 ruling，也不是新数学结果。
2. 若用户启动数学研究：战略主论题为 W51×RP-B01×self-reference；首个可执行研究包为真实 partiality quotient/QIIT 上的 bind×race/timeout、contextual equivalence 与最小时序富化。在线因果/guard 擦除为探索位，R034 Cubical Agda 为独立验证位。
3. 数学 R041 的 code、25-test 原始输出、`cf58f27` 和增量容器谱系仍是证据 Gate 0；若不可得，可按已固定正文重新实现一个明确标注新 provenance 的模型，不得冒充原源码。证据恢复不等于数学研究本身。
4. 历史交接主线仍开放：2,396 条 understanding claim 的直接句级裁决、aistudio coverage、历史数学主张和关键 response→artifact/code/Git 因果；只按用户/current task 选中的 stable ID 显式 hydrate。
5. 治理独立验证仍开放：固定 model/host/version 的 fresh Session/真实压缩后行为验收；Python EOF/hash 不替代模型行为。

## 当前已验证状态

- `核心认知.md` 仍为 generation-3/27 KC，SHA-256 `8aa005505c68d20eb11c48b946fa61e68b03013d56926ca2b9c928d06c5a7dfb`；本轮全文读取并完成 27/27 人工回评，core 未改。
- C3 共 522 行，明确区分战略主线与战术先手，给出 Q0—Q7 资格链、四级判词、partiality 定理阶梯、RP-B01/反射研究包、探索/验证位和停止条件；它的最强状态是 source-bounded AI strategy。
- 数学 R041 正文支持代表层 bind 相容、race 不相容、组合完成性反差和条件性黑箱不可能三角；当前顶层/workspace Git 均无 `cf58f27`，源码与运行未取得。
- 理解章节 merge manifest 已按 C3 和 README 的当前文件集重建并验证：top-level 28、nested 24、union 28、same-name 24、identical 15、different pairs 9、top-only 4、nonidentical union 13、unresolved nontrivial 0。
- 项目治理基线仍是 `governance-v3.0.0`；S021 是本地 runtime checkpoint，尚未获得 Git commit，不 push、不发布。

## 当前证据上限

- 本轮证明 C3 文档、公开逐 KC 回评、三件套投影和 checkpoint 的机械一致性；不证明研究排序最优、用户已采纳、任何新 HoTT 定理或现实相对悖论成立。
- R041 为 `PAPER_SOURCE_ACQUIRED / CODE_RUN_GIT_LINEAGE_OPEN`；其 25 项测试是来源自述。RP-B01 的 native formalization/experiment/independent review 均未运行，`B01-TARGET` 仍开放。
- R034 原生 HoTT/Cubical Agda 仍 `NOT_RUN`；当前 PATH 有 Lean 4.33.1、无 Agda，普通 Lean Eq 不替代单价 Path。
- fresh Python 输入保真与负向行为可核验；模型对三件套的实际理解仍不由工具认证。

## 恢复入口

按根 AGENTS 全文加载 core→direction→panorama。后续方向先读 `理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md`；追溯判断依据再读 C1/C2/A11、数学 R041 与 RP-B01。若启动首个研究包，先 query `A-HOTT-RESEARCH-DIRECTION-001` 和 `A-WEBGPT-R041-PAPER-001`，再显式 research task hydrate。
"""

    frontier = """# HoTT 研究前沿（S021 研究战略提案后）

本文件是当前注意力槽，不是数学结论数据库。C3 是 source-bounded AI proposal；用户是否采纳仍未定，本轮没有启动数学研究。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 战略主论题 | W51×RP-B01×self-reference：数学分类→统一有效交付→有效自我 ASK | AI-proposed / target-interface-open | 固定一个真实 HoTT 计算/提取接口；若无自然资格升级点，则保存防御或一般计算边界，不冒充 HoTT 特定悖论 |
| 首个可执行研究包 | partiality quotient/QIIT 的 bind×race/timeout、contextual equivalence 与最小富化 | AI-proposed / paper-skeleton-ready / native-not-run | 选一个真实构造，先做 bind 正例、race 负例、商下降与上下文等价；按四级判词收敛 |
| 探索 | 完整流函数/在线因果、guard 擦除、同函数异时 | parked-until-exact-interface | 只在 guarded/clocked source、target、observable 和自然现实任务都固定后进入 |
| 验证/证据 | R034 Cubical Agda；数学 R041 code/25-test/`cf58f27`/container | open | native 环境可得时验证 R034；R041 执行谱系缺失时可按正文另建新 provenance 对照，不冒充原源码 |

统一判词：`DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`，不得跳级。`new_math_research_started=false`。
"""

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    lessons += (
        "\n25. “战略上最重要”与“下一个最可执行”不是同一排序：W51×RP-B01×自指更接近最终理论目标，"
        "而 R041 partiality 操作闭包的证据链更成熟，适合先建立完整研究样板；必须显式区分，避免用成熟度覆盖目标价值或用目标价值掩盖证据缺口。"
        "\n26. 后续候选应按资格保持性判别，并分成 `DEFENSE_WORKS`、`REPRESENTATION_BOUNDARY`、"
        "`NATURAL_USAGE_MISMATCH`、`INTERNAL_INCONSISTENCY`；商拒绝非同余 race、截断拒绝取见证或提取器拒绝经典项时，"
        "这是理论防御证据，不能绕过规则制造悖论。\n"
    )

    resume = """# 接续指针

## 每个新 Session/压缩后的固定恢复

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md` 和本地治理 Skill/PROTOCOL/LOAD_SET/STATE。
2. 严格全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`；manifest/旧 receipt 不能替代。
3. 当前方向先读 `理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md`；追溯依据再读 C1/C2/A11。
4. 数学 R041 回源文件名 R401 的 PROOF_NOTE，不与 workspace 的 ZCode-governance R041 合并；RP-B01 回源 `workspace/.codex/research/hott/candidates/RP-B01/`。
5. 数学研究使用 research profile，先 query stable record 再显式 task hydrate；结束为当前 generation 全部 KC 写人工回评，并交叉更新 core/direction/panorama 的正确 owner。

## 当前停止点

S021 已把用户本轮问题回答为一份新的 C3：总方向是 ASK／完成资格保持性；B 线 W51×RP-B01×自指是战略主论题，A 线真实 partiality quotient×race/timeout 是首个可执行研究包，在线因果/guard 擦除是探索位，R034 是验证位。理解章节 inventory 已刷新为 28/24。本轮没有执行新数学、代码模型、证明助手或外部 consumer 审计；该排序仍是 AI proposal，未冒充用户 ruling。下一成果必须是用户启动后的单个可检查构造，或现有证据缺口的明确补齐。
"""

    state["revision"] = 21
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "status": "HOTT_QUALIFICATION_PRESERVATION_AI_STRATEGY_PROPOSED_NOT_EXECUTED",
            "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
            "new_math_research_started": False,
            "next_minimal_verification": (
                "If the user starts mathematics: select one real HoTT partiality quotient/QIIT and decide bind/race "
                "operation closure with contextual equivalence; independently recover R041 execution lineage when available."
            ),
        }
    )
    state["projection"]["status"] = new_semantic
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record.update(
        {
            "projection_generation": "20260912-direction-005",
            "semantic_status": new_semantic,
            "scope": (
                "Cross-LocalGPT/WebGPT portfolio with a source-bounded qualification-preservation umbrella, "
                "strategic W51×RP-B01×reflection line, tactical partiality-context line and explicit proposal/non-execution boundary."
            ),
        }
    )
    append_unique(direction_record["full_sources"], C3_PATH)
    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record.update(
        {
            "projection_generation": "20260912-outcome-005",
            "semantic_status": new_semantic,
            "scope": (
                "Cross-source outcome panorama including the documented C3 AI research strategy and current 28/24 "
                "understanding inventory; no new mathematical theorem, native proof or user adoption is claimed."
            ),
        }
    )
    append_unique(panorama_record["full_sources"], C3_PATH)
    state["records"]["A-UNDERSTANDING-RECONCILIATION-001"]["scope"] = (
        "File-level reconciliation is complete and non-destructive for the current 28/24 inventory "
        "(24 same-name pairs, 15 identical, 9 different, 4 top-only); semantic equivalence and mathematical claim review remain explicitly open."
    )
    c3_hash = R.sha((root / C3_PATH).read_bytes())
    r041_hash = R.sha((root / R041_PATH).read_bytes())
    state["records"]["A-HOTT-RESEARCH-DIRECTION-001"] = {
        "kind": "research_strategy",
        "path": C3_PATH,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "decision_status": "AI_PROPOSAL_NOT_USER_RULING",
        "depends_on": [
            "A-DIRECTION-PARADOX-REVIEW-001",
            "A-PARADOX-HOTT-SYNTHESIS-001",
            "A-WEBGPT-R041-PAPER-001",
        ],
        "full_sources": [
            C3_PATH,
            "核心认知.md",
            "方向追踪.md",
            "全景视野.md",
            "理解章节/C1-后续研究方向独立复审-20260912.md",
            "理解章节/C2-历史悖论谱与HoTT处理机制全解-20260912.md",
            "理解章节/A11-开放问题与悬空接头.md",
            R041_PATH,
            "workspace/.codex/research/hott/candidates/RP-B01/PLAN.md",
            "workspace/.codex/research/hott/candidates/RP-B01/CONSTRUCTION.md",
            "workspace/.codex/research/hott/candidates/RP-B01/CLAIMS.json",
            "HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md",
        ],
        "source_hashes": {
            C3_PATH: c3_hash,
            R041_PATH: r041_hash,
        },
        "mathematical_status": "NO_NEW_THEOREM_STRATEGY_ONLY",
        "scope": (
            "Source-bounded recommendation: qualification preservation is the umbrella; W51×RP-B01×reflection is the strategic line; "
            "real partiality quotient/QIIT bind-versus-race contextual adequacy is the first executable work package."
        ),
    }
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [
            "S-GOV-20260912-020-UNDERSTANDING-INVENTORY-REFRESH",
            "A-HOTT-RESEARCH-DIRECTION-001",
        ],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            C3_PATH,
            "方向追踪.md",
            "全景视野.md",
            "audit/understanding-chapter-merge-manifest.json",
            "scripts/audit/prepare_hott_research_direction_checkpoint.py",
        ],
        "source_hashes": {C3_PATH: c3_hash},
        "mathematical_status": "NO_NEW_MATHEMATICS_STRATEGY_AND_ROUTING_ONLY",
        "cognition_status": "QUALIFICATION_PRESERVATION_STRATEGY_DOCUMENTED_AND_ROUTED",
        "scope": (
            "Answer the user's direction question in a new document, reconcile strategic versus tactical priority, "
            "update current projections and audit all 27 core units; no research execution or user adoption claimed."
        ),
    }

    session = f"""# {SESSION_ID}

- 触发：用户要求回答后续 HoTT 悖论分析/查找方向及理由，并写入一份新文档。
- 认知输入：本轮固定顺序全文读取 generation-3 三件套；显式 query 当前方向和 R041 record；直接复核 C1/C2/A11、数学 R041、RP-B01 三文件和自指/反射调查。
- 核心判断：总方向收敛为 ASK／完成资格保持性；W51×RP-B01×self-reference 是战略主论题，真实 partiality quotient/QIIT 的 bind×race/timeout 是首个可执行研究包。
- 产物：`{C3_PATH}`；同步 direction v1.2、panorama v1.2、STATE revision 21、MEMORY/FRONTIER/LESSONS/RESUME，以及 28/24 merge inventory。
- 决策边界：C3 是 AI proposal，不是用户 ruling；本轮没有新数学、代码模型、proof assistant、外部 consumer 审计、原创性或现实物理认证。
- Git：runtime checkpoint applied locally；未 commit、未 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "cognition": {
                "core_units_read": 27,
                "three_way_order": ["核心认知.md", "方向追踪.md", "全景视野.md"],
                "queried_records": [
                    "I-DIRECTION-PORTFOLIO-20260912",
                    "A-DIRECTION-PARADOX-REVIEW-001",
                    "A-WEBGPT-R041-PAPER-001",
                ],
                "direct_sources": [
                    C3_PATH,
                    "理解章节/C1-后续研究方向独立复审-20260912.md",
                    "理解章节/C2-历史悖论谱与HoTT处理机制全解-20260912.md",
                    "理解章节/A11-开放问题与悬空接头.md",
                    R041_PATH,
                    "workspace/.codex/research/hott/candidates/RP-B01/PLAN.md",
                    "workspace/.codex/research/hott/candidates/RP-B01/CONSTRUCTION.md",
                    "workspace/.codex/research/hott/candidates/RP-B01/CLAIMS.json",
                    "HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md",
                ],
            },
            "artifacts": {
                "c3_lines": 522,
                "c3_sha256": c3_hash,
                "merge_counts": expected_counts,
            },
            "research_status": {
                "umbrella": "QUALIFICATION_PRESERVATION_UNDER_ABSTRACTION_AND_COMPOSITION",
                "strategic": "W51_RP_B01_SELF_REFLECTION",
                "first_executable": "PARTIALITY_CONTEXTUAL_ADEQUACY",
                "new_math_research_started": False,
                "mathematics": "NOT_CERTIFIED",
                "user_adoption": "NOT_CLAIMED",
            },
            "post_checkpoint_required": [
                "KC audit 27/27 verify",
                "understanding merge verify",
                "three-way cognition verify",
                "fresh three-way receipt revision 21",
                "projection freshness",
                "full regression",
                "JSON parse and git diff --check",
            ],
            "git_commit": "NOT_AUTHORIZED_THIS_TURN",
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n"

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
        "authorization": (
            "User explicitly requested a new durable document answering the future HoTT paradox direction question; "
            "project governance requires the resulting AI proposal, current direction, panorama, memory and per-KC audit to remain mutually consistent."
        ),
        "load_profile": "research",
        "task_ids": task_ids,
        "files": [
            {
                "path": relative,
                "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None,
                "text": value,
            }
            for relative, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "session_id": SESSION_ID,
                "revision": 21,
                "files": len(texts),
                "c3_sha256": c3_hash,
                "merge_counts": expected_counts,
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
