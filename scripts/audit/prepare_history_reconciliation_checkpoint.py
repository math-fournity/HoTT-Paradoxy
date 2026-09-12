#!/usr/bin/env python3
"""Prepare/apply the controlled checkpoint for the history reconciliation wave.

This is a small, reproducible adapter around the repository cognition runtime.
It constructs mutable-owner text in memory and lets the runtime perform the
atomic write.  It deliberately keeps the understanding reconciliation record
review_required because the manifest proves file-level disposition, not
mathematical or complete historical semantic equivalence.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "S-GOV-20260912-010-HISTORY-RECONCILIATION"


def load_runtime(root: Path):
    spec = importlib.util.spec_from_file_location("cognition_runtime", root / ".codex/tools/cognition_runtime.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def replace_line_start(text: str, prefix: str, new_line: str) -> str:
    lines = text.splitlines()
    indexes = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(indexes) == 1, (prefix, indexes)
    lines[indexes[0]] = new_line
    return "\n".join(lines) + "\n"


def insert_after_line_start(text: str, prefix: str, additions: list[str]) -> str:
    lines = text.splitlines()
    indexes = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(indexes) == 1, (prefix, indexes)
    i = indexes[0]
    lines[i + 1 : i + 1] = additions
    return "\n".join(lines) + "\n"


def direction_text(root: Path) -> str:
    text = (root / "方向追踪.md").read_text(encoding="utf-8")
    text = text.replace("版本：`integrated-direction-portfolio/v1`", "版本：`integrated-direction-portfolio/v1.1`", 1)
    text = text.replace("状态：`INITIAL_INTEGRATED_PROJECTION / SEMANTIC_FULL_RECONCILIATION_PENDING`", "状态：`EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW`", 1)
    text = text.replace(
        "> 本初始投影已经把 WebGPT 的全部 `P-*` 方向记录、用户双方向、LocalGPT 当前 owner 中明确出现的方向和治理/证据支线纳入覆盖表；LocalGPT 的全历史语义去重、每个 KC 的句子级映射和所有隐含方向仍标 `PENDING_SEMANTIC_RECONCILIATION`，不能用本文件冒充已完成。",
        "> 本投影已经把 WebGPT 的全部 91 条 STATE record 和 LocalGPT 四类历史账本逐项登记到 `audit/cross-source-reconciliation.json`；本文件中的方向表是经过规则/owner 对照的综合视图。关键词/路径规则不能替代对每一条历史句子的人工语义裁决，因此逐句 claim 的 `PENDING_DIRECT_SENTENCE_ADJUDICATION` 仍必须显式保留，不能用本文件冒充数学结论认证。",
        1,
    )
    text = text.replace("<!-- integrated-direction-portfolio:v1", "<!-- integrated-direction-portfolio:v1.1", 1)
    text = text.replace("projection_generation: 20260912-direction-001", "projection_generation: 20260912-direction-002", 1)
    text = text.replace("semantic_status: BOUNDED_INITIAL_NOT_EXHAUSTIVE", "semantic_status: EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW", 1)
    text = text.replace("source_state_revision: 9", "source_state_revision: 10", 1)
    for prefix, old, new in [
        (
            "| `DIR-U-B-EFFECTIVE-DELIVERY`",
            "`OUT-L-CORE-MATHEMATICAL`（表示/证据分层）",
            "`OUT-L-CORE-MATHEMATICAL`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`（表示/证据分层）",
        ),
        (
            "| `DIR-L-TIME-WORK-DIMENSION`",
            "| `OUT-L-TIME-BOUNDARY` |",
            "| `OUT-L-TIME-BOUNDARY`、`OUT-W-TEMPORAL-TRANSPORT` |",
        ),
        (
            "| `DIR-W-RP-B01`",
            "| `OUT-W-RP-B01` |",
            "| `OUT-W-RP-B01`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION` |",
        ),
    ]:
        line = next(line for line in text.splitlines() if line.startswith(prefix))
        assert old in line, (prefix, old)
        text = replace_line_start(text, prefix, line.replace(old, new, 1))
    text = text.replace(
        "这张表是“全部记录身份被纳入综合审计”的机械分母，不把每条记录都压成方向。逐条语义映射由 Wave 2 继续完成。",
        "这张表是“全部记录身份被纳入综合审计”的机械分母；逐项 source mapping 已由 `audit/cross-source-reconciliation.json` 完成，句级语义裁决仍按条目状态显式保留。",
        1,
    )
    text = text.replace(
        "当前初始投影先使用主题级关联，等句子级映射完成后再补 stable KC IDs。",
        "当前方向仍保留主题级 core 关联；`core_refs` 的精确 KC 交叉审视由 register locator 和后续人工句级裁决继续承载，不把规则匹配写成用户语义结论。",
        1,
    )
    section = """## 6.5 全量来源登记与人工复核边界

`audit/cross-source-reconciliation.json` 对纳入范围的每个来源行保留 `source_class`、稳定 `source_id`、原始 locator、行 hash、候选 direction/result IDs、映射依据和语义状态。当前覆盖分母为 WebGPT STATE 91、AI response ledger 384（LocalGPT 305 + WebGPT 55 + Gemini 24）、tool event 3,146、work product 16,209、understanding claim 2,396，合计 22,226。

这一步的设计理由是把“没有被看板提到”与“已经人工判断过但暂不归类”区分开：所有行都可发现、可回源、可按方向/结果检索；`understanding_claim` 仍标 `PENDING_DIRECT_SENTENCE_ADJUDICATION`，因为路径/关键词路由不能证明句子的真实语义，也不能提高数学证据等级。该 register 是 provenance 导航层，不是第二个数学主张矩阵；原始账本和结果 owner 仍是证据来源。

"""
    assert "## 7. 更新规则\n" in text
    return text.replace("## 7. 更新规则\n", section + "## 7. 更新规则\n", 1)


def panorama_text(root: Path) -> str:
    text = (root / "全景视野.md").read_text(encoding="utf-8")
    text = text.replace("版本：`integrated-outcome-panorama/v1`", "版本：`integrated-outcome-panorama/v1.1`", 1)
    text = text.replace("状态：`INITIAL_INTEGRATED_PROJECTION / SEMANTIC_FULL_RECONCILIATION_PENDING`", "状态：`EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW`", 1)
    text = text.replace(
        "> 本文件是跨 LocalGPT/WebGPT 的成果、正反例、失败、未知和证据边界投影。它不是数学主张矩阵、不是 `STATE.json` 的替代品，也不是把历史 AI 的“完成”措辞重新认证为真。",
        "> 本文件是跨 LocalGPT/WebGPT 的成果、正反例、失败、未知和证据边界投影。逐项来源登记见 `audit/cross-source-reconciliation.json`；它不是数学主张矩阵、不是 `STATE.json` 的替代品，也不是把历史 AI 的“完成”措辞重新认证为真。",
        1,
    )
    text = text.replace("<!-- integrated-outcome-panorama:v1", "<!-- integrated-outcome-panorama:v1.1", 1)
    text = text.replace("projection_generation: 20260912-outcome-001", "projection_generation: 20260912-outcome-002", 1)
    text = text.replace("semantic_status: BOUNDED_INITIAL_NOT_EXHAUSTIVE", "semantic_status: EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW", 1)
    text = text.replace("source_state_revision: 9", "source_state_revision: 10", 1)
    text = replace_line_start(
        text,
        "| `OUT-TOP-CORE-FOUNDATION`",
        "| `OUT-TOP-CORE-FOUNDATION` | 三平台用户提问及本轮治理补充的 chronological core：127 条消息、913 个 `KC-*`、原文/来源 hash/主题/生命周期 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY` | 顶层交接工程 | `VERIFIED_WITH_SCOPE` | core 的机械身份、编号、payload hash、来源文件关系可核验；generation-1 前缀保持不变 | 不证明用户主张为数学真理，不证明模型理解 | `核心认知.md`；`核心认知.manifest.json`；`audit/core-cognition-generation-transition-20260912.json`；`scripts/audit/verify_core_cognition.py` |",
    )
    text = replace_line_start(
        text,
        "| `OUT-UNDERSTANDING-MERGE`",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录的 25/24 文件 inventory；24 个同名，15 对字节相同，9 个同名差异，顶层有 C0 独有文件；逐文件处置已生成 | `DIR-G-UNDERSTANDING-RECONCILIATION` | 顶层只读审计 | `VERIFIED_WITH_SCOPE` | 每个 union 文件有 hash、line diff、处置决定、回滚源和非破坏性验证；顶层目录作为 canonical，nested 源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断 | `audit/understanding-chapter-merge-manifest.json`；`scripts/audit/verify_understanding_merge.py`；`理解章节/`；`AI对话录/理解章节/` |",
    )
    corpus_prefix = "| `OUT-L-CORPUS`"
    outcomes = [
        "| `OUT-W-TEMPORAL-TRANSPORT` | WebGPT C-UA-TIME-001/002/003 与 C-TIME-SCHEDULE-001：同一端函数结构不决定固定时钟可观察性、因果可达性或查询可用性 | `DIR-L-TIME-WORK-DIMENSION`、`DIR-L-SAME-FUNCTION-DIFFERENT-TIME` | WebGPT R006–R008 | `REVIEW_REQUIRED` | 有明确有限 Bool³/关系模型和纸笔边界，说明 extensional equality 不能自动提供 timing/availability | 不证明标准 HoTT 缺少全部时间结构，不证明现实系统的普遍不可交付 | `sources/webgpt/workspace-snapshot/.codex/research/hott/sessions/S-ANS-20260910-006-TEMPORAL-TRANSPORT/`；`.../007-CAUSAL-EQUIVALENCES/`；`.../008-RELATIONAL-SIP/`；`STATE.json` C-UA-TIME-* |",
        "| `OUT-W-EARLY-EFFECTIVE-CONSTRUCTION` | WebGPT C-LABEL-STREAM、C-COMPLETION-CERTIFICATE、C-DONE-OBSERVABILITY、C-QUOTIENT-DESCENT、C-AXIOMATIC-COMPUTATION、C-LOCAL-EXECUTION：有限证书、标签流、商消去和有效交付的条件构造/阻碍 | `DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-W-RP-B01` | WebGPT R010–R017 | `REVIEW_REQUIRED` | 结果区分逐例存在、有限证书、统一有效实现、可观察 Done 与完整 HoTT 编译；历史有限检查/纸笔材料可回源 | 不证明无神谕统一实现已构造，不证明 native HoTT/Lean/Agda 已通过，不证明现实交付 | `sources/webgpt/workspace-snapshot/.codex/research/hott/sessions/S-ANS-20260910-010-LABEL-STREAM/`；`.../011-COMPLETION-CERTIFICATE/`；`.../014-DONE-OBSERVABILITY/`；`.../015-QUOTIENT-DESCENT/`；`.../016-AXIOMATIC-COMPUTATION/`；`.../017-LOCAL-EXECUTION/` |",
    ]
    text = insert_after_line_start(text, corpus_prefix, outcomes)
    section = """## 2.1 全量来源登记与成果投影边界

`audit/cross-source-reconciliation.json` 将 WebGPT revision 41 的 91 条 STATE record、LocalGPT 384 条 visible response、3,146 条 tool event、16,209 条 work product 和 2,396 条理解章节 claim 逐项登记，共 22,226 条。每条都有 source locator、行 hash、方向/结果候选链接、映射依据和语义状态；`understanding_claim` 的逐句直接语义裁决仍明确标为 `PENDING_DIRECT_SENTENCE_ADJUDICATION`。

因此本全景可以保证“来源行没有静默消失且可发现”，不能保证每个关键词路由就是正确的数学语义归属。详细 JSON register 是按需审计底座；本文件只承载当前结果全景，原始 response/tool/artifact/claim 和 Git 仍是证据源。

"""
    assert "## 3. 两个 GPT 的结果关系\n" in text
    text = text.replace("## 3. 两个 GPT 的结果关系\n", section + "## 3. 两个 GPT 的结果关系\n", 1)
    text = text.replace(
        "顶层当前三件套 projection 是本轮新增，直到 fresh Session、故障注入和 full semantic reconciliation 通过前，状态保持 `IMPLEMENTED_PENDING_FRESH`。",
        "顶层三件套已接入 generation-2、逐文件 merge receipt 和全量 source register；fresh/压缩行为及 2,396 条 claim 的直接句级语义裁决仍不认证，模型上下文仍保持 `NOT_CERTIFIED_BY_TOOL`。",
        1,
    )
    old_tail = """1. WebGPT 91 条记录到 integrated direction/result 的逐条、句子级语义映射；
2. LocalGPT response/tool/trajectory/artifact/Git 到所有方向/结果的完整语义闭合；
3. core 主题级链接升级为每个当前方向的精确 KC ID；
4. `verify_projection_freshness` 的全量 source-manifest/STATE/三件套 hash 闭环和新 Session 真实行为验收；
5. 两个理解章节的最终语义合并和 canonical cutover；
6. 所有历史研究结果的数学/形式化/现实桥梁复核。"""
    new_tail = """1. 2,396 条 understanding claim 的直接句级语义裁决；当前已逐行登记，但规则路由仍不等于人工判断；
2. `verify_projection_freshness` 的全量 source-manifest/STATE/三件套 hash 闭环和新 Session/压缩恢复的宿主行为验收；
3. `A-AISTUDIO-COVERAGE-001`：`aistudio-docs` 与 `HoTT_is_GONE_COMPLETE.md` 的覆盖关系；
4. `A-HISTORICAL-MATH-CLAIMS-001`：历史数学主张的逐项数学/形式化/现实桥梁复核；
5. WebGPT 与 LocalGPT 的关键 response→artifact/code→Git 因果映射仍需在具体研究条目上加深，而不是仅凭 register 归类。"""
    assert old_tail in text
    text = text.replace(old_tail, new_tail, 1)
    return text.replace("这些未完成项是当前全景的一部分，不能被“初始投影已存在”覆盖。", "这些未完成项是当前全景的一部分，不能被“全量来源已登记”覆盖；登记完成与语义/数学认证仍是不同状态。", 1)


def memory_text() -> str:
    return """# 当前工作记忆

> Owner：顶层综合 repo 的 `AGENTS.md` 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态，不复制 `核心认知.md` 或历史长文。

## 当前状态（2026-09-12）

- 顶层 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 已初始化为新 Git repo；当前治理 checkpoint 将由 `S-GOV-20260912-010-HISTORY-RECONCILIATION` 封存。
- `核心认知.md` 已从 generation-1 迁移到 `core-cognition-generation-2`：127 条登记消息、94 条含核心单元消息、913 个连续 `KC-*`；generation-1 的 903 个 KC 前缀逐项保持一致。新增输入是用户关于三件套、压缩恢复、跨 GPT 综观和理解章节逐文件融合的原文。
- 三件套当前固定顺序为 `核心认知.md` → `方向追踪.md` → `全景视野.md`；两个 projection 已从有界初始投影升级为“全量 source register + scoped manual review”。这不证明模型上下文实际保有全文。
- `audit/understanding-chapter-merge-manifest.json` 已覆盖顶层 25 文件与 nested 24 文件；顶层 `理解章节/` 是 canonical，nested `/AI对话录/理解章节/` 仍保留为历史源，没有删除。
- `audit/cross-source-reconciliation.json` 已登记 WebGPT 91、AI response ledger 384（LocalGPT 305 + WebGPT 55 + Gemini 24）、tool event 3,146、work product 16,209、understanding claim 2,396，共 22,226 个来源行；每行有 locator 和方向/结果链接或理由。2,396 条 claim 仍是 `PENDING_DIRECT_SENTENCE_ADJUDICATION`，不把规则匹配写成语义结论。
- `/Volumes/D/ALL-Markdown` 的当前工作树仍 dirty、HEAD `8470721a07f28f842895a67f5fd885ab12c1ee33`；WebGPT workspace snapshot HEAD `26fcecfbfecf6db66a70c1bf3e067159bce3eb6a`、revision 41；二者都没有被本轮修改。

## 当前仍开放 / 未完成

1. `A-UNDERSTANDING-RECONCILIATION-001`：文件级 manifest 已通过，但历史章节的逐句语义等价和数学主张复核仍不认证。
2. `A-AISTUDIO-COVERAGE-001`：不能凭 `HoTT_is_GONE_COMPLETE.md` 文件存在证明已覆盖用户移走的 `aistudio-docs`。
3. `A-HISTORICAL-MATH-CLAIMS-001`：历史数学主张仍按纸笔/有限测试/native/现实桥梁分层，未被本治理 Session 重新证明。
4. `A-HISTORY-LEDGERS-001` 与 `A-CROSS-SOURCE-RECONCILIATION-001`：来源逐行登记完成，但 understanding claim 的直接句级语义裁决和关键 response→artifact/Git 因果仍需人工加深。
5. `Q-CONTEXT`/`Q-FRESH` 等 WebGPT 原始治理未知仍作为历史来源保留；新 Session/压缩恢复的宿主级模型实际消费不能由工具认证。

## 下一最小可验结果

先按固定顺序全文读取 generation-2 三件套，运行 `verify_core_cognition.py`、`verify_three_way_cognition.py`、`verify_understanding_merge.py` 和 `verify_cross_source_reconciliation.py`；随后做 source/hash freshness 与缺件/错序/孤儿的负向演练。数学研究保持暂停，直到用户明确恢复或交接证据链完成。
"""


def frontier_text() -> str:
    return """# HoTT 研究前沿（当前交接与三件套升级阶段）

本文件是当前注意力槽，不是新的数学结论数据库。历史来源已经完成逐项 register；下一优先级仍是把可发现性与直接证据语义裁决分开，再决定是否开始新的候选构造。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 收敛 | 22,226 条跨来源 register + 理解章节 merge receipt | active | 抽样核对关键 response→artifact/code/Git 因果，并保留 claim 句级待审状态 |
| 探索 | `理解章节/A11-开放问题与悬空接头.md` 的未闭合接头 | active | 将精确 KC、方向、结果和 source locator 逐项连回，不把主题匹配当结论 |
| 深层 | HoTT 时间/ASK/现实相对候选 | historical-review | 先完成历史数学主张范围复核，再选择一项真正构造/反例 |

当前不宣称任何历史候选为 `HoTT ⊢ ⊥`，也不宣称已完成现实桥梁、Lean/Agda 内核认证或 aistudio-docs 全覆盖。`new_math_research_started=false`。
"""


def resume_text() -> str:
    return """# 接续指针

## 当前可恢复入口

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`。
2. 按固定前三项全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`，再读取 `.codex/cognition/LOAD_SET.json` 指定的其余固定文件。
3. 运行 `rtk python3 scripts/audit/verify_core_cognition.py`，确认 generation-2 的 913 KC 和 generation-1 前缀迁移收据。
4. 运行 `rtk python3 scripts/audit/verify_understanding_merge.py` 和 `rtk python3 scripts/audit/verify_cross_source_reconciliation.py`，确认双目录 25/24 文件和 22,226 条 source-row register。
5. 运行 `rtk python3 scripts/audit/verify_three_way_cognition.py`，再用 `cognition_runtime.py plan/read/check` 记录三件套真实 EOF/hash 收据。
6. 按需打开 `audit/cross-source-reconciliation.json` 的具体 locator，优先处理 2,396 条 understanding claim 的句级语义裁决和历史数学主张 review。

## 当前停止点

来源覆盖登记、逐文件 merge receipt 和 core generation-2 已完成并 checkpoint；模型实际上下文、压缩后的保有、数学正确性、aistudio-docs 覆盖和 claim 的人工语义闭合仍不能由当前工具宣称完成。
"""


def lessons_text() -> str:
    return """# 交接阶段经验

1. “用户提问已提取”不等于“AI 回答、工具事件、代码和 Git 已审计”；必须分开建立 ledger。
2. LocalGPT 的父线程和 HoTT-2 子线程不能用一个文件的数量替代 38-turn lineage；同一用户内容的重复和补充要显式标识。
3. WebGPT 的 workspace 快照是历史来源；其 `STATE`、R、SESSION 和 Git 需要重新绑定到顶层 repo，不能直接当作当前状态。
4. Gemini 的 `inlineFile` 是代码载荷，不能因为旧报告的摘要而分类成空记录；Drive 文档正文缺失必须保留缺口。
5. `/Volumes/D/ALL-Markdown/aistudio-docs/` 被用户移走是有效边界；替代文件是否覆盖原目录是待证事实，不是文件名可以解决的语义问题。
6. 核心认知的编号/hash/定位可以机械验证；是否深化、纠偏或偏航仍需当前 AI 写逐编号公开评估。
7. 22,226 条来源行可以全部登记而不等于 22,226 条语义已经人工判定；register 的 locator/ID/规则依据必须与 `PENDING_DIRECT_SENTENCE_ADJUDICATION` 同时保留。
8. 理解章节的逐文件“合并”可以安全地先形成 canonical 选择和 rollback receipt；保留 nested 源比未经授权删除更重要，line diff 也不等于数学内容等价。
9. core generation-2 只能通过新增用户原文输入和生成器重建；generation-1 前缀 identity check 是迁移证据，不能手工编辑旧 KC。
10. full EOF/hash、checkpoint、Git commit 和测试都不能认证模型理解；`model_context=NOT_CERTIFIED_BY_TOOL` 是必须保留的真实边界。
"""


def new_state(root: Path) -> dict[str, object]:
    state = json.loads((root / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))
    state["revision"] = 10
    state["latest_session"] = SESSION_ID
    state["execution_control"] = {
        "background_work": False,
        "checkpoint_result": "CHECKPOINT_COMMITTED",
        "last_checkpoint_session": SESSION_ID,
        "new_math_research_started": False,
        "next_minimal_verification": "fresh three-way EOF/hash and negative fault rehearsal; then direct sentence review of 2396 understanding claims",
        "source_policy": "preserve historical snapshots; do not restore user-removed aistudio-docs",
        "status": "EXHAUSTIVE_SOURCE_REGISTER_AND_UNDERSTANDING_MERGE_VALIDATED_WITH_SCOPED_MANUAL_REVIEW",
    }
    state["projection"]["status"] = "EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update({
        "scope": "Cross-LocalGPT/WebGPT direction portfolio; all source rows are registered, while sentence-level semantic adjudication remains explicitly scoped.",
        "full_sources": ["核心认知.md", "sources/SOURCE_MANIFEST.json", "sources/webgpt/workspace-snapshot/.codex/research/hott/STATE.json", "HoTT/README.md", "HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md", "理解章节/C0-当前整合审计与证据边界-20260912.md", "audit/cross-source-reconciliation-report.md"],
        "projection_generation": "20260912-direction-002",
        "semantic_status": "EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW",
    })
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update({
        "scope": "Cross-LocalGPT/WebGPT outcome and evidence panorama; all source rows are registered, while sentence-level semantic adjudication and mathematical certification remain explicitly scoped.",
        "full_sources": ["方向追踪.md", "sources/SOURCE_MANIFEST.json", "sources/webgpt/workspace-snapshot/.codex/research/hott/STATE.json", "HoTT/CLAIM_EVIDENCE_MATRIX.md", "audit/ledger-summary.json", "audit/coverage-summary.json", "audit/verification-report.json", "audit/cross-source-reconciliation-report.md", "audit/understanding-chapter-merge-manifest.json"],
        "projection_generation": "20260912-outcome-002",
        "semantic_status": "EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW",
    })
    state["records"]["A-UNDERSTANDING-RECONCILIATION-001"].update({
        "status": "review_required",
        "scope": "File-level reconciliation is complete and non-destructive; semantic equivalence and mathematical claim review remain explicitly open.",
        "full_sources": ["理解章节/README.md", "理解章节/读遍账本.md", "理解章节/B0-工作史总览.md", "理解章节/B1-本地GPT工作史.md", "理解章节/B2-网页GPT工作史-I.md", "理解章节/B3-网页GPT工作史-II.md", "理解章节/B4-Gemini工作史.md", "理解章节/B5-成果总账.md", "核心认知.md", "audit/understanding-chapter-merge-manifest.json", "scripts/audit/verify_understanding_merge.py"],
    })
    state["records"]["A-HISTORY-LEDGERS-001"].update({
        "scope": "Visible AI responses, canonical trajectory events, WebGPT sections, Gemini executable/inline records, artifacts and claims; exhaustive cross-source row register is now built, with direct semantic review remaining scoped.",
        "full_sources": ["sources/SOURCE_MANIFEST.json", "sources/prompts/Codex-HoTT-2-用户消息提取-20260911.md", "sources/prompts/ChatGPT-HoTT-Main-用户消息提取-20260911.md", "sources/prompts/Gemini-AI对话录-用户消息提取-20260911.md", "audit/cross-source-reconciliation-report.md"],
    })
    state["records"]["A-HISTORICAL-MATH-CLAIMS-001"]["full_sources"] = ["理解章节/B5-成果总账.md", "HoTT/CLAIM_EVIDENCE_MATRIX.md", "sources/webgpt/workspace-snapshot/.codex/research/hott/STATE.json", "全景视野.md", "audit/cross-source-reconciliation-report.md"]
    state["records"]["A-CORE-GENERATION-2-001"] = {
        "kind": "core_generation_migration",
        "path": "audit/core-cognition-generation-transition-20260912.json",
        "status": "closed",
        "scope": "Append only user-authored governance/handoff requirements through a registered source input; preserve generation-1 prefix identity.",
        "full_sources": ["audit/core-cognition-generation-transition-20260912.json", "核心认知.manifest.json", "scripts/audit/verify_core_cognition.py"],
        "resolution": {
            "reason": "Generation-2 was generated by the canonical builder and verified; the first 903 KC metadata and payloads equal the generation-1 Git recovery prefix.",
            "evidence": ["audit/core-cognition-generation-transition-20260912.json", "核心认知.manifest.json", "scripts/audit/verify_core_cognition.py"],
        },
    }
    state["records"]["A-CROSS-SOURCE-RECONCILIATION-001"] = {
        "kind": "cross_source_reconciliation",
        "path": "audit/cross-source-reconciliation-report.md",
        "status": "review_required",
        "scope": "Exhaustively register WebGPT STATE and four top-level historical ledgers with stable locators and candidate direction/result links; direct sentence semantics remain review_required.",
        "depends_on": ["A-HISTORY-LEDGERS-001", "I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"],
        "full_sources": ["audit/cross-source-reconciliation-report.md", "audit/coverage-summary.json", "方向追踪.md", "全景视野.md"],
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "status": "review_required",
        "scope": "Exhaustive source-row registration, understanding-directory merge receipt, core generation-2 migration and post-change governance checkpoint; no new mathematics.",
        "cognition_status": "EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW",
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "depends_on": ["S-GOV-20260912-009-MEMORY-ALIGNMENT"],
        "full_sources": [
            f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
            f".codex/research/hott/sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md",
            f".codex/research/hott/sessions/{SESSION_ID}/RUNS.json",
            "audit/core-cognition-generation-transition-20260912.json",
            "audit/understanding-chapter-merge-manifest.json",
            "audit/cross-source-reconciliation-report.md",
            "scripts/audit/verify_core_cognition.py",
            "scripts/audit/verify_understanding_merge.py",
            "scripts/audit/verify_cross_source_reconciliation.py",
        ],
    }
    state["review_due"] = ["A-AISTUDIO-COVERAGE-001", "A-HISTORICAL-MATH-CLAIMS-001", "A-HISTORY-LEDGERS-001", "A-UNDERSTANDING-RECONCILIATION-001", "A-CROSS-SOURCE-RECONCILIATION-001"]
    state["unresolved"] = ["A-AISTUDIO-COVERAGE-001", "A-HISTORY-LEDGERS-001", "A-UNDERSTANDING-RECONCILIATION-001", "A-CROSS-SOURCE-RECONCILIATION-001", "A-HISTORICAL-MATH-CLAIMS-001"]
    return state


def session_text() -> str:
    return """# 历史覆盖登记、理解章节合并与核心 generation-2 Session

- session_id: `S-GOV-20260912-010-HISTORY-RECONCILIATION`
- scope: 完成双 GPT 历史来源的逐行 reconciliation register、两个理解章节的逐文件非破坏性合并收据、核心认知 generation-1→2 用户原文增补，以及对应 runtime checkpoint
- authorization: 用户已明确要求在完整审计方案后继续执行；不修改 `/Volumes/D/ALL-Markdown`、WebGPT 原 workspace、已移走的 `aistudio-docs` 或 nested 历史源
- mathematical_status: `UNCHANGED_FROM_R039_HISTORICAL_SCOPE`
- cognition_status: `EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW`

## 实际执行

1. 生成 `audit/understanding-chapter-merge-manifest.json`：顶层目录 25 文件、nested 目录 24 文件、24 个同名，其中 15 对字节相同，9 个同名差异，顶层独有 C0；所有文件均有 hash、line diff、处置理由、rollback source。顶层 `理解章节/` 作为 canonical，nested 物理源保留，未执行删除。
2. 生成 `audit/cross-source-reconciliation.json` 和人读报告：WebGPT revision 41 的 91 条 STATE record、AI response ledger 384（LocalGPT 305 + WebGPT 55 + Gemini 24）、3,146 tool event、16,209 work product、2,396 understanding claim，共 22,226 条逐项登记；每项均有 locator、方向/成果候选链接和显式语义状态。
3. 将 WebGPT R006–R017 的时间/有效交付结果族补入全景入口；保留 `REVIEW_REQUIRED` 和 `NOT_PERFORMED_BY_THIS_REGISTER` 边界。
4. 将用户关于三件套、压缩恢复、跨 LocalGPT/WebGPT 综观和逐文件融合的原文保存到新的 `sources/prompts/` 输入，由生成器生成 `core-cognition-generation-2`；旧 903 个 KC 的 payload/metadata 前缀逐项保持一致，新版本为 913 个 KC。

## 三方判定

- `core_change`: `APPEND_USER_UNIT`；只追加用户原文工作意识/交接要求，不写入 AI 结果或 audit 推断。
- `direction_change`: `STATUS_AND_RESULT_COVERAGE`；从有界初始投影升级为“全量来源登记、保留句级人工复核”的当前状态。
- `panorama_change`: `ADD_RESULT_FAMILIES_AND_MERGE_RECEIPT`；补入 WebGPT 早期结果族和理解章节可追溯合并结果。
- `update_decision`: `MULTIPLE_WITH_REASON`；core、direction、panorama、audit manifest 各自承担唯一职责，不能互相覆盖。
- `cross_conflicts`: `WEBGPT_REVISION_40_41`、`WEBGPT_SKILL_MANIFEST_1.3.3_ACTUAL_1.3.4`、`LOCALGPT_DIRTY_VS_SNAPSHOT`、`SENTENCE_SEMANTIC_REVIEW_PENDING`。
- `unresolved`: `A-AISTUDIO-COVERAGE-001`、`A-UNDERSTANDING-RECONCILIATION-001`、`A-HISTORICAL-MATH-CLAIMS-001`、`A-HISTORY-LEDGERS-001` 的人工句级/数学复核边界、模型实际理解认证。

## 结果边界

本 Session 完成的是来源覆盖登记、当前投影扩展、逐文件 merge receipt 和 core generation migration；规则/owner 路由不是人工数学语义判决，22,226 项的存在和链接不等于模型理解或数学证明。原始源、Git、tool、artifact 和 claim 必须沿 locator 回源；LocalGPT dirty 工作树、aistudio-docs 缺失和 WebGPT 版本漂移继续作为负证据保留。
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    runtime = load_runtime(root)
    base = runtime.plan(root)
    state = new_state(root)
    files = [
        ("MEMORY.md", memory_text()),
        ("方向追踪.md", direction_text(root)),
        ("全景视野.md", panorama_text(root)),
        (".codex/research/hott/FRONTIER.md", frontier_text()),
        (".codex/research/hott/LESSONS.md", lessons_text()),
        (".codex/research/hott/RESUME.md", resume_text()),
        (".codex/research/hott/STATE.json", json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"),
        (f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md", session_text()),
    ]
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly requested full plan audit, rationale completion, and execution; scope excludes external source mutation, restoration of aistudio-docs, and deletion of historical nested source.",
        "files": [],
    }
    for rel, text in files:
        path = root / rel
        payload["files"].append({
            "path": rel,
            "expected_sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None,
            "text": text,
        })
    result = runtime.checkpoint(root, base["snapshot"], payload, apply=args.apply)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
