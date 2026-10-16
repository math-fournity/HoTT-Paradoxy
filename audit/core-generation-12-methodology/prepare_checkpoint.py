#!/usr/bin/env python3
"""Prepare, but do not apply, the core-generation-12 checkpoint.

The user asked that their later theory-selection and Russell-pattern guidance be
part of the permanently loaded core cognition.  This script composes the
required T3 checkpoint payload after the curation manager has generated the
new core/manifest/transition.  It intentionally does not make a mathematical
claim, start a new research Goal, or publish a branch.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "S-GOV-20261002-CORE-GENERATION-12-METHODOLOGY"
PREVIOUS_SESSION = "S-GOV-20261001-MAIN-DOCS-ALIGNMENT"
BASE_REVISION = 295
NEXT_REVISION = 296
OLD_GENERATION = "core-cognition-generation-11"
NEW_GENERATION = "core-cognition-generation-12"
OLD_CORE_RECORD = "A-CODEX-CORE-GENERATION-11-001"
CORE_RECORD = "A-CODEX-CORE-GENERATION-12-001"
CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION = "scripts/audit/core-cognition-curation-v12.json"
TRANSITION = "audit/core-cognition-generation-12-transition-20261002.json"
SOURCE = "sources/prompts/Codex-后续理论靶与罗素模式P-用户原文-20261002.md"
PREPARE = "audit/core-generation-12-methodology/prepare_checkpoint.py"
STATE = ".codex/research/hott/STATE.json"
DIRECTION = "方向追踪.md"
PANORAMA = "全景视野.md"
ESSAY = "扩展认知.md"
MEMORY = "MEMORY.md"
MEMORY_001 = "MEMORY/001 - 当前执行队列.md"
MEMORY_003 = "MEMORY/003 - 当前验证状态与顺序日志.md"
RESUME = ".codex/research/hott/RESUME.md"
RESULT = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_ROOT = f".codex/research/hott/sessions/{SESSION_ID}"
DIRECTION_RECORD = "I-DIRECTION-PORTFOLIO-20260912"
PANORAMA_RECORD = "I-OUTCOME-PANORAMA-20260912"
CORE_TRANSITION = {
    "from_generation": OLD_GENERATION,
    "to_generation": NEW_GENERATION,
    "manifest": MANIFEST,
    "transition": TRANSITION,
}


def load_module(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    if not spec or not spec.loader:
        raise SystemExit(f"MODULE_NOT_LOADABLE:{rel}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R = load_module("runtime_core12", ".codex/tools/cognition_runtime.py")
if str(ROOT / "scripts/audit") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts/audit"))
import build_core_cognition as core_builder  # noqa: E402
import projection_edit  # noqa: E402


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(rel: str) -> str:
    return sha((ROOT / rel).read_bytes())


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:80]}:{count}")
    return text.replace(old, new, 1)


def add_once(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def quote(payload: str, kid: str) -> str:
    body = "\n".join("> " + line if line else ">" for line in payload.splitlines())
    return f"<!-- original:{kid}:begin -->\n{body}\n<!-- original:{kid}:end -->"


def update_projection_metadata(doc: dict, version_before: str, version_after: str, suffix: str) -> None:
    projection_edit.replace_in_index(doc, version_before, version_after)
    projection_edit.replace_in_index(doc, "日期：2026-10-01", "日期：2026-10-02")
    projection_edit.replace_in_index(doc, "source_state_revision: 295", "source_state_revision: 296")
    old = re.search(r"projection_generation: ([^\n]+)", doc["index_text"])
    if not old:
        raise ValueError("PROJECTION_GENERATION_MISSING")
    projection_edit.replace_in_index(doc, old.group(0), f"projection_generation: {suffix}-296")


def methodology_essay(payloads: dict[str, str]) -> str:
    return f'''<!-- governance-shard:v2
logical_id: CORE-ESSAY
shard_id: 012
index: ../扩展认知.md
-->

# 后续理论靶、罗素模式 P 与工作意识

本片是对 generation-12 新增六条用户原文的 AI 阐释。它把它们放进此前“理论经济—现实对齐—针对性过程”的连续方法里，但不把阐释、路线图中的具体候选或任何数学判断回写成用户原文。本片尤其区分两种不同身份：用户规定的是**如何找到应该审视的理论位置**；Power Set、P0–P6、ETCS、forcing 等是当前 AI 提出的、仍待来源与控制检验的研究设计。

## 靶不是醒目的结果，而是理论的骨架

{quote(payloads["KC-000056"], "KC-000056")}

[原文出处](../{SOURCE}#L9)

这条纠正把选题层级固定下来。芝诺和圆环并非为了反驳一个算术级数；它们让数轴、连续和极限怎样规定“到达”成为可审问题。罗素也并非只制造一个怪集合，而是使把条件当作已形成集合的朴素集合论暴露。由此，后续工作需要问：某理论在多大范围内提供共同对象、共同语言或基础设施？它为得到这种能力抽象了什么？过程必须使这一承诺重新变成决定性条件。

这不是贬低定理、论文或具体现象。它们可以成为原典、消费者、正控制或反控制；只是它们本身不自动等于理论靶。一个候选还须保住同一对象、输入、操作、观察和完成条件，避免把“理论回答不了”建立在悄悄换题上。

## 资料入口不能支配理论选择

{quote(payloads["KC-000057"], "KC-000057")}

[原文出处](../{SOURCE}#L13)

菲尔兹奖论文库仍是极有价值的资料库，但它只能提高进入原典与消费者的机会。它不能取代理论级资格，也不能令一个本来不合格的结果成为靶。未来如果用户把范围明确限定在菲尔兹奖工作内，这一限定当然仍须遵守；在没有该限定时，理论的基础位置、具体抽象和同一任务优先。

## 用已有数学知识生成候选，但不能把它当作证据

{quote(payloads["KC-000058"], "KC-000058")}

[原文出处](../{SOURCE}#L17)

这延续了 KC-000007、KC-000040 的发现路径：已学习的数学图式可以帮助提出多种候选，而不应只是把熟悉的教科书答案当作终局。实际可执行的动作是先从理论收益、被压缩的条件和现实或假想现实任务生成种子，再回到原典、真实消费者、标准回答和反控制筛选。模型不能直接读取自己的权重、单个训练样本或所谓神经网络中的某一条数据；因此它们也不构成可审计来源。

## 罗素模式 P：先把放大镜磨清楚

{quote(payloads["KC-000059"], "KC-000059")}

[原文出处](../{SOURCE}#L21)

这里的顺序很重要。模式 P 不是“看见自指就宣布悖论”，也不是把所有不可计算、所有非构造存在或所有独立性揉成一个问题。它要求把规则读成形成、依赖、停止和使用的过程：理论不能不面对的对象怎样取得可用资格；对其存在或合法身份的追问是否形成直接回环或无终点上升；追问尚未结束时，理论是否已经把该对象交给算符、判断或实际使用；最后是否在同一任务中出现 UR。P 的具体形式可以继续修订，但它的职责是把罗素的“最后一跃”变成可审计的发现方法。

用户关于 Pre-HoTT 社区的判断在这里仍是研究先验，而不是数学史定理。每个理论都有自己的守卫、层级、证书和完成规则；它们可能真正阻断 P 的某一环，也可能只阻断最表面的形状。审计的价值在于允许这两种结果。

## P 不替代正确起点

{quote(payloads["KC-000060"], "KC-000060")}

[原文出处](../{SOURCE}#L25)

P 是放大镜，不能替代先看见理论最显眼、最中心的承诺。芝诺对准稠密性，罗素对准无界条件形成，HoTT 的现有罗素线对准宇宙与相同的形成位置。由此，面对 ZFC 或其它理论，先选一个理论自身不能绕开的显眼承诺，再以 P 深读它；不要把多条公理、模型语义、工具实现和一般困难并列为“到处碰碰看”的搜索表。

当前把 Power Set 作为 ZFC 的第一个来源卡是 AI 的应用选择，不是本条用户原话的替换。它必须仍然从 Power Set 自身的形成承诺导出问题，接受有限集合、明示子集、层级与模型相对语义等控制，并通过 P 的各项义务后才能称为候选。

## 工作意识是输入，不是自我认证

{quote(payloads["KC-000061"], "KC-000061")}

[原文出处](../{SOURCE}#L29)

把这些指导纳入核心认知，意味着后续会话在规定的完整加载中先看到它们，而不是只在路线图或近期聊天里偶然遇到。它不意味着文件存在就能证明模型理解、保证每次都照做，或自动产生正确的数学发现。真正的使用仍要在每个理论局部表现为：找对理论层级和明显承诺；把既有知识当作启发而非裁决；构造保住同一任务的敏感过程；再用来源、控制和必要时机器证明检查结果。
'''


def audit_entry(kid: str, label: str, relation: str, assessment: str, evidence: str, next_step: str) -> str:
    return f'''### {kid}

- relation: {relation}
- 该条要求的工作姿态：{assessment}
- 已走过的路与证据：{evidence}
- 为什么是该 relation：本轮只在所列范围内把该用户原文接入 current core；未把它提升为数学结论或替代其它 KC 的语义。
- 下一选择与反证条件：{next_step}
'''


def build_audit(manifest: dict) -> tuple[str, dict[str, str]]:
    focus = {
        "KC-000007": ("DEEPENED", "内在知识可作为启发式候选生成，而非训练数据读取或数学证据。", "KC-000058 原文；curation v12。", "若后续候选无法回到原典、消费者和控制，撤回其证据升级。"),
        "KC-000017": ("ALIGNED", "先理解用户的悖论视角再使用既有解释；新增原文继续要求抵抗训练惯性。", "KC-000017、KC-000058；扩展认知 001、012。", "若新的展开把用户方法缩为标准教材问题，回到原文纠正。"),
        "KC-000039": ("DEEPENED", "基础问题应先在基础位置寻找；新增 KC-000060 明确“显而易见的位置”不是广搜。", "KC-000039、KC-000060；扩展认知 006、012。", "若具体理论无法显示一个中心承诺，停止把 P 当作遍历许可。"),
        "KC-000040": ("DEEPENED", "把模型已有知识谱当作被考察对象，新增原文限定为启发式而非读取权重。", "KC-000040、KC-000058；扩展认知 006、012。", "若把启发式种子说成来源或证明，降格并补来源。"),
        "KC-000047": ("DEEPENED", "理论经济与普适性须落实到理论层级的靶和具体过程，不能停在耀眼结论。", "KC-000047、KC-000056；扩展认知 009、012。", "若候选只有定理而无理论承诺与同一任务，不能升级。"),
        "KC-000048": ("DEEPENED", "针对性策略既要求目标前提，也要求从正确的显眼承诺起步。", "KC-000048、KC-000059、KC-000060；路线图 007。", "若 P 被当作无边界搜索清单，撤回该搜索路径。"),
        "KC-000050": ("DEEPENED", "论域元素的存在性追问是 P 的核心材料之一，但不把新理论预判为命中。", "KC-000050、KC-000059；扩展认知 010、012。", "若不存在不可另账对象、未落定追问或预支使用，P 候选失败。"),
        "KC-000051": ("DEEPENED", "算符先于存在性落定的次序提供 P 的‘最后一跃’；新原文要求先刻画这一结构。", "KC-000051、KC-000059；扩展认知 010、012。", "若理论的守卫、分层或证书在对象使用前已完成，不能称预支使用。"),
        "KC-000054": ("ALIGNED", "UR 仍规定候选的最终可理解性；本轮没有把 P 或 ZFC 候选直接叫作 UR。", "KC-000054；路线图 007；扩展认知 011、012。", "若同一任务的对象、操作、观察或 Done 改变，不能用 UR 宣称命中。"),
        "KC-000055": ("NOT_TOUCHED", "圆环对芝诺幽灵的所指保持原有裁定；本轮没有重新归因。", "KC-000055；generation-11 transition。", "若新用户澄清圆环线，再回源更新。"),
        "KC-000056": ("ALIGNED", "后续靶是支撑数学大厦的理论；过程用于令其承诺显形。", "generation-12 source/curation；扩展认知 012。", "若用户修正理论层级或指向，追加新原文而不改写本条。"),
        "KC-000057": ("ALIGNED", "菲尔兹奖只是可能的来源入口，不是理论选择硬门。", "generation-12 source/curation；rulings；扩展认知 012。", "若用户在某一任务重新限定菲尔兹范围，只在该任务内应用限定。"),
        "KC-000058": ("ALIGNED", "利用已学知识生成种子，但来源、控制和证明必须独立提供。", "generation-12 source/curation；扩展认知 012。", "若声称读取权重或将启发式种子当证据，立即降格。"),
        "KC-000059": ("ALIGNED", "先刻画罗素模式 P，再审视 ZFC、HoTT 和更早理论。", "generation-12 source/curation；路线图 007；扩展认知 012。", "若 P 被简化为任意自指或不可计算，重新回到完整原文。"),
        "KC-000060": ("ALIGNED", "先找到极其明显的核心承诺，P 仅用于深读，不作无边界枚举。", "generation-12 source/curation；扩展认知 012。", "若起点不再是理论自身显眼承诺，说明其理由或停止。"),
        "KC-000061": ("ALIGNED", "这批理念性指导须随 core 在规定情形完整加载。", "generation-12 source/curation；STATE.current_core；LOAD_SET。", "文件加载不认证理解；未来实际使用仍需 source-first 与行为证据。"),
    }
    units = manifest["units"]
    shards: dict[str, str] = {}
    for shard_id, subset, title in (
        ("001", units[:30], "KC-000001 至 KC-000030"),
        ("002", units[30:], "KC-000031 至 KC-000061"),
    ):
        lines = [
            "<!-- governance-shard:v2", "logical_id: CORE-AUDIT", f"shard_id: {shard_id}",
            "index: ../CORE_COGNITION_AUDIT.md", "-->", "", f"# {title}", "",
        ]
        for unit in subset:
            kid = unit["id"]
            if kid in focus:
                relation, assessment, evidence, next_step = focus[kid]
            else:
                relation = "NOT_TOUCHED"
                assessment = "本轮只完成 core generation-12 的方法论原文接入；未重新裁决本 KC 的数学、现实或哲学内容。"
                evidence = f"`核心认知.md` {kid}；`核心认知.manifest.json`。"
                next_step = "只有后续任务直接使用本条或新证据改变其适用性时才重审。"
            lines.append(audit_entry(kid, str(unit["semantic_label"]), relation, assessment, evidence, next_step))
        shards[f"{SESSION_ROOT}/CORE_COGNITION_AUDIT/{shard_id} - {title}.md"] = "\n".join(lines)

    core_index = f'''<!-- governance-shard-index:v2
logical_id: CORE-AUDIT
mode: topical
shard_root: CORE_COGNITION_AUDIT
last_shard: CORE_COGNITION_AUDIT/003 - 四件套交叉审视与裁定.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 3 个分片；缺一片即未完成，按表顺序读取。

# 核心认知逐编号回评：{SESSION_ID}

> generation：`{NEW_GENERATION}`；KC 总数：61；角色：`GOVERNANCE_ALIGNMENT`。本审计记录用户原文怎样进入持续加载链；它不认证模型理解，也不交付数学结论。

- core_change: `YES_ADDITIVE_PRESERVING` — generation-11/55 → generation-12/61；55/55 旧 KC 由 transition 精确映射，新增 KC-000056–KC-000061。
- direction_change: `METADATA_AND_METHOD_ALIGNMENT` — 方向投影只刷新 current STATE revision/生成标识；新的理论级路线图仍是候选设计，不启动 Goal。
- panorama_change: `METADATA_ONLY` — 不新增或升级数学结果、证明范围、候选命中或现实结论。
- essay_change: `YES` — 扩展认知新增第 012 片，解释理论级靶、来源入口、启发式、模式 P、显眼承诺与持续加载的关系；它仍是 AI 阐释层。
- update_decision: 新的直接用户方法论进入 core；AI 的 Power Set 首点、P0–P6 细化与候选排序保留为带身份的研究设计。
- cross_conflicts: 过去将菲尔兹奖入口、模型启发式或 ZFC 首点说成硬门/用户原话的表述必须让位于 KC-000056–KC-000061 与本轮 ruling；没有将旧路线图历史删除。
- unresolved: 模式 P 的形式、Power Set 是否产生 P 问题、任何 ZFC/ETCS/topos 等候选是否形成 UR，均未在本轮解决；核心更新也不认证未来模型会实际遵循加载内容。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [KC-000001 至 KC-000030](<CORE_COGNITION_AUDIT/001 - KC-000001 至 KC-000030.md>) | 历史起点、时间/ASK、理论经济 | current |
| 002 | [KC-000031 至 KC-000061](<CORE_COGNITION_AUDIT/002 - KC-000031 至 KC-000061.md>) | 自反、现实对齐、罗素线与本轮六条方法论 | current |
| 003 | [四件套交叉审视与裁定](<CORE_COGNITION_AUDIT/003 - 四件套交叉审视与裁定.md>) | 扩展认知、方向、全景、来源与停止边界 | current |
<!-- governance-shard-table:end -->
'''
    cross = f'''<!-- governance-shard:v2
logical_id: CORE-AUDIT
shard_id: 003
index: ../CORE_COGNITION_AUDIT.md
-->

# 四件套交叉审视与裁定

## 最高指示的角色复核

- 本轮角色是 `GOVERNANCE_ALIGNMENT`：保护的发现动作是使用户关于理论层级、显眼承诺和罗素模式 P 的后续指导在未来每次规定加载时先于 AI 的便利选靶惯性出现。
- 最危险的偏差是把用户方法误写成 ZFC 已命中、把 AI 的 Power Set 或 P0–P6 设计回灌为用户原话，或把菲尔兹奖入口重新升级成硬门。
- 这次更新让 core 成为长期输入；“写入”“读取”“理解”“按其行动”和“得到数学结论”仍是不同的证据层。
- 若后续实际研究不能指出理论的基础位置、显眼承诺、同一任务和敏感过程，则本轮文档接入没有发挥发现作用，应回到 KC-000056–KC-000061 而非补造结论。

## 扩展认知逐段落复核

- 001–011：`ALIGNED` — 已有阐释继续保留理论经济、现实对齐、ASK、罗素存在性追问与 UR 的边界；本轮不改写其历史引文身份。
- 012：`DEEPENED` — 新增解释片只展开本轮六条直接用户原文，并明确 Power Set/P0–P6/候选排序不是用户原话或数学结论。
- 反证条件：若引用块不再逐字对应 generation-12 的 KC-000056–KC-000061，或阐释把候选升级为结论，则重新核对 source、curation 与本片。
- 未决：扩展认知是 AI 阐释层，文件更新不证明未来会话的语义使用；需由以后的 source-first 回源和实际候选工作检验。

## 方向、全景与当前状态

- 方向：`RETAINED_WITH_METADATA_REFRESH` — 当前 HoTT/Goal7 状态未变；未来理论级路线图保持候选/开发文档身份。
- 全景：`NO_NEW_MATHEMATICAL_RESULT` — 本轮只更新 core/essay 的方法论输入，不把任何理论候选加入结果面板。
- STATE：`CURRENT_CORE_ADVANCED` — generation、curation、manifest、transition、KC count、core record 与本 session 记录在同一 canonical checkpoint 更新。
- 反证条件：若 STATE.current_core 与 core/manifest/transition 的字节身份不一致，或 checkpoint 无 `CHECKPOINT_COMMITTED` receipt，则不得宣称本代已应用。
'''
    shards[f"{SESSION_ROOT}/CORE_COGNITION_AUDIT/003 - 四件套交叉审视与裁定.md"] = cross
    return core_index, shards


def build_legacy_audit(manifest: dict) -> str:
    """Build the runtime-compatible full-KC table.

    cognition_runtime v3.6.1 verifies v2 audit shards when they already exist,
    but its write allowlist cannot atomically create child files below a session
    audit directory.  The project records that limitation as an open writer
    gap.  This legacy table preserves exact coverage and the full written
    reasoning rather than creating an out-of-band shard tree.
    """
    focused = {
        "KC-000007": ("DEEPENED", "已有数学知识用于启发式候选生成，不是可审计证据。"),
        "KC-000017": ("ALIGNED", "先按用户的悖论观理解，再审视熟悉解释；新增方法论继续抵抗训练惯性。"),
        "KC-000039": ("DEEPENED", "基础问题应先在基础位置寻找；P 不能替代正确起点。"),
        "KC-000040": ("DEEPENED", "知识谱是被考察对象；新增原文明确其只能产生启发式种子。"),
        "KC-000047": ("DEEPENED", "理论经济和普适性要落实在理论级靶与同一任务的过程上。"),
        "KC-000048": ("DEEPENED", "针对性策略还要求显眼中心承诺先行，反对无边界枚举。"),
        "KC-000050": ("DEEPENED", "论域元素的存在性追问是罗素模式 P 的核心材料。"),
        "KC-000051": ("DEEPENED", "算符先于存在性落定的次序是 P 的最后一跃。"),
        "KC-000054": ("ALIGNED", "UR 仍是最终同一任务的不合理性判据；本轮没有宣布任何新 UR 命中。"),
        "KC-000056": ("ALIGNED", "后续靶是理论骨架而非醒目结果，过程用来显形理论承诺。"),
        "KC-000057": ("ALIGNED", "菲尔兹奖是可选入口而不是候选硬门。"),
        "KC-000058": ("ALIGNED", "内在知识可启发候选，不能被说成读取权重或证明。"),
        "KC-000059": ("ALIGNED", "先刻画罗素模式 P，再审视 ZFC、HoTT 和其他理论。"),
        "KC-000060": ("ALIGNED", "从极其明显的核心承诺起步，P 不是无边界搜索。"),
        "KC-000061": ("ALIGNED", "本批理念性指导是每次规定 core 加载中的长期输入。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{NEW_GENERATION}`；KC 总数：61。当前 runtime 的 session-child 写入限制使本次使用 single-file legacy audit；这是结构兼容边界，不冒称 v2 audit shards 已原子写入。", "",
        "- core_change: YES_ADDITIVE_PRESERVING — generation-11/55 → generation-12/61；55/55 旧 KC 有完整 transition mapping，新增 KC-000056–KC-000061。",
        "- direction_change: METADATA_AND_METHOD_ALIGNMENT — 仅刷新 STATE revision/生成标识，未来理论级路线图保持候选设计。",
        "- panorama_change: METADATA_ONLY — 不新增或升级数学结果、候选命中或现实结论。",
        "- essay_change: YES — 扩展认知新增第 012 片，解释新六条原文；其身份仍为 AI 阐释层。",
        "- update_decision: 新方法论进入 core；Power Set、P0–P6 和候选排序保持 AI 研究设计身份。",
        "- cross_conflicts: 任何把 Fields、模型启发式或 AI 的 ZFC 首点误报为硬门/用户数学结论的旧表述均须降级。",
        "- unresolved: P 的具体规格、Power Set 的审计、所有未来理论候选和未来模型实际使用仍开放。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决与反证条件 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = str(unit["id"])
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focused.get(kid, ("NOT_TOUCHED", "本轮只将新增方法论原文接入 core，未重新裁决本 KC 的数学、现实或哲学内容。"))
        evidence = f"`核心认知.md` {kid}；`核心认知.manifest.json`；本轮 core transition。"
        unresolved = "未来直接使用本条或出现新用户原文/证据时重审；本轮不替代其既有边界。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | {evidence} | {unresolved} |")
    lines.extend([
        "", "## 四件套交叉审视", "",
        "- 最高指示角色复核：本轮为 GOVERNANCE_ALIGNMENT；保护的发现动作是让理论级靶、显眼承诺与 P-first 的指导在未来加载中先于方便的旧路径出现。",
        "- 扩展认知：001–011 保持原有边界；012 对 KC-000056–KC-000061 作 AI 阐释，明确不把 Power Set、P0–P6 或任何候选回写成用户原话。",
        "- 方向与全景：只刷新 current STATE metadata，不改 Goal7、既有 HoTT 罗素线或任何数学结果。",
        "- 反证条件：若 current_core、manifest、transition 或 canonical result 不一致，或未来实际工作未回到新 KC 原文，则本轮不能被说成持续理解已获认证。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit(f"OUTPUT_EXISTS:{args.output}")

    state = json.loads((ROOT / STATE).read_text(encoding="utf-8"))
    if state.get("revision") != BASE_REVISION or state.get("latest_session") != PREVIOUS_SESSION:
        raise SystemExit("STATE_BASE_MISMATCH")
    if state.get("current_core", {}).get("generation") != OLD_GENERATION:
        raise SystemExit("STATE_CORE_BASE_MISMATCH")
    if CORE_RECORD in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("RECORD_ALREADY_EXISTS")
    if not all((ROOT / rel).is_file() for rel in (CORE, MANIFEST, CURATION, TRANSITION, SOURCE)):
        raise SystemExit("CORE_GENERATION_INPUT_MISSING")

    manifest = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    if manifest.get("generation") != NEW_GENERATION or manifest.get("counts", {}).get("core_units") != 61:
        raise SystemExit("CORE_GENERATION_NOT_BUILT")
    payloads = core_builder.parse_core_payloads((ROOT / CORE).read_text(encoding="utf-8"))
    if list(payloads)[-6:] != [f"KC-{n:06d}" for n in range(56, 62)]:
        raise SystemExit("CORE_NEW_UNIT_ORDER_INVALID")

    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)
    if plan["revision"] != BASE_REVISION or plan["latest_session"] != PREVIOUS_SESSION:
        raise SystemExit("PLAN_BASE_MISMATCH")

    direction = projection_edit.load(ROOT, DIRECTION)
    update_projection_metadata(direction, "版本：`integrated-direction-portfolio/v1.16`", "版本：`integrated-direction-portfolio/v1.17`", "20261002-direction-core")
    panorama = projection_edit.load(ROOT, PANORAMA)
    update_projection_metadata(panorama, "版本：`integrated-outcome-panorama/v1.17`", "版本：`integrated-outcome-panorama/v1.18`", "20261002-outcome-core")

    essay = projection_edit.load(ROOT, ESSAY)
    essay["index_text"] = replace_once(essay["index_text"], "last_shard: 扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md", "last_shard: 扩展认知/012 - 后续理论靶、罗素模式 P 与工作意识.md")
    essay["index_text"] = replace_once(essay["index_text"], "baseline: core-cognition-generation-11", "baseline: core-cognition-generation-12")
    essay["index_text"] = replace_once(essay["index_text"], "本文根据《核心认知.md》generation-11 的全部 55 段原文综合写成。", "本文根据《核心认知.md》generation-12 的全部 61 段原文持续综合；第 012 片专门展开本轮新增的六条方法论原文。")
    essay["index_text"] = replace_once(essay["index_text"], "| 011 | [本来应该很简单的事：UR 与芝诺的模式匹配](<扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md>) | 用户 2026-09-30 的三段原文（KC-000052–KC-000054）及其上下文：四句证据链被读作非现实性悖论；项目目标不加“存在性”限定；UR 的定义与芝诺的模式匹配；对照表、两副面孔、教科书消解的对位、“相同可以无限细分”、A／B 两向分工与“找到了”的身份分层 | current |", "| 011 | [本来应该很简单的事：UR 与芝诺的模式匹配](<扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md>) | 用户 2026-09-30 的三段原文（KC-000052–KC-000054）及其上下文：四句证据链被读作非现实性悖论；项目目标不加“存在性”限定；UR 的定义与芝诺的模式匹配；对照表、两副面孔、教科书消解的对位、“相同可以无限细分”、A／B 两向分工与“找到了”的身份分层 | current |\n| 012 | [后续理论靶、罗素模式 P 与工作意识](<扩展认知/012 - 后续理论靶、罗素模式 P 与工作意识.md>) | 理论级靶、菲尔兹入口可选、受控启发式、罗素模式 P、明显核心承诺与持续加载（KC-000056–KC-000061） | current |")
    essay["shards"]["扩展认知/012 - 后续理论靶、罗素模式 P 与工作意识.md"] = methodology_essay(payloads)
    old_note = "本文的主题顺序属于解释性创作，文中 40 处标记为 original 的原文引文逐字来自《核心认知.md》generation-5；其中 KC-000037–KC-000040（用户 2026-09-16 提出的第三条发现路径）见第 006 片。"
    new_note = "本文最初的主题顺序与最早 40 处 original 引文来自 generation-5；后续第 006–011 片逐步纳入 generation-6 至 generation-11 的新原文，本轮第 012 片逐字展开 generation-12 的 KC-000056–KC-000061。当前全文基线是 generation-12，但 AI 阐释不替代每条 KC 的原文权威。"
    essay["shards"]["扩展认知/005 - 表达界限、文章作为起点与编写说明.md"] = replace_once(essay["shards"]["扩展认知/005 - 表达界限、文章作为起点与编写说明.md"], old_note, new_note)

    memory = projection_edit.load(ROOT, MEMORY)
    insertion = """## 后续理论靶与罗素模式 P 的核心方法（2026-10-02）

研究发起人已经要求将本日后续理论工作的理念性指导完整纳入核心认知第 12 代（KC-000056–KC-000061），未来按既有四件套规则加载。它规定：靶须是支撑数学大厦的理论，而非单一定理；菲尔兹奖只是可选资料入口；模型已有数学知识只能作启发式种子；先深刻刻画罗素的计算—存在—自指模式 P；先从极其明显的核心承诺起步，P 不授权无边界枚举。该输入不把 ZFC、Power Set、ETCS、topos 或任何候选升级为数学结论或已选 Goal。当前具体路线卡仍由 `dev-docs/菲尔兹奖后续理论级目标路线图/` 持有。

"""
    memory["shards"][MEMORY_001] = replace_once(memory["shards"][MEMORY_001], "## 用户当前专题（2026-09-24）", insertion + "## 用户当前专题（2026-09-24）")
    memory["shards"][MEMORY_003] = memory["shards"][MEMORY_003].rstrip() + f"\n\n{SESSION_ID}：用户要求把 2026-10-02 的后续理论级方法论作为工作意识入 core。generation-11/55→generation-12/61；55/55 旧 KC 由 transition 映射，新 KC-000056–000061 分别固定理论级靶、菲尔兹入口可选、受控启发式、罗素模式 P、明显核心承诺与持续加载。更新只改变长期输入、AI 阐释和当前恢复信息；不创建 Goal、不宣称 ZFC 命中、不交付数学结论。\n"

    resume = (ROOT / RESUME).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 历史停止点\n\n", "## 历史停止点\n\n" + f"{SESSION_ID}：core generation-12 将用户 2026-10-02 的后续理论级方法论纳入固定加载输入（KC-000056–KC-000061）。这改变未来选靶/发现的工作意识，不改变 Goal7、HoTT 阶段收尾或任何数学结论。\n\n")

    state["revision"] = NEXT_REVISION
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "core_sha256": sha_file(CORE),
        "curation": CURATION,
        "curation_sha256": sha_file(CURATION),
        "generation": NEW_GENERATION,
        "kc_count": 61,
        "manifest": MANIFEST,
        "manifest_sha256": sha_file(MANIFEST),
        "path": CORE,
        "transition": TRANSITION,
    }
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = RESULT
    state["records"][DIRECTION_RECORD]["projection_generation"] = "20261002-direction-core-296"
    state["records"][PANORAMA_RECORD]["projection_generation"] = "20261002-outcome-core-296"

    old_core = state["records"][OLD_CORE_RECORD]
    old_core["lifecycle_status"] = "HISTORICAL"
    old_core["status"] = "superseded_by_generation_12"
    old_core["resolution"] = {
        "evidence": [TRANSITION, CORE, MANIFEST],
        "reason": "Generation-12 preserves all generation-11 units and advances STATE.current_core to the new curation, manifest and transition. The generation-11 migration remains historical evidence.",
    }
    old_core["revalidation"] = str(old_core.get("revalidation", "")).strip() + f" {SESSION_ID}: superseded as current core by generation-12; source payloads remain preserved through the generation-12 transition."

    core_sources = [CORE, MANIFEST, CURATION, TRANSITION, SOURCE, "scripts/audit/build_core_cognition.py", "scripts/audit/verify_core_cognition.py", PREPARE]
    state["records"][CORE_RECORD] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / COMPLETE_ADDITIVE_PRESERVING",
        "full_sources": core_sources,
        "kind": "core_generation_migration",
        "lifecycle_status": "CURRENT",
        "path": TRANSITION,
        "related_records": [OLD_CORE_RECORD, SESSION_ID],
        "scope": "Incrementally preserve all 55 generation-11 direct-user units exactly and append KC-000056–KC-000061: theory-level target selection, non-mandatory Fields entrance, controlled learned-knowledge heuristics, Russell pattern P first, obvious central commitment first, and permanent core loading. No mathematical theorem, ZFC hit, or new Goal is added.",
        "source_hashes": {rel: sha_file(rel) for rel in core_sources},
        "status": "closed",
    }

    session_path = f"{SESSION_ROOT}/SESSION.md"
    audit_text = build_legacy_audit(manifest)
    audit_path = f"{SESSION_ROOT}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_ROOT}/RUNS.json"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, audit_path, runs_path, RESULT, SOURCE, CURATION, TRANSITION, PREPARE, CORE_RECORD, OLD_CORE_RECORD],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREVIOUS_SESSION, CORE_RECORD, OLD_CORE_RECORD, DIRECTION_RECORD, PANORAMA_RECORD],
        "scope": "Apply core generation-12 and its explanatory/current-state integration. The work records methodology as enduring input; it does not start a new theory investigation, alter Goal7, or claim a mathematical result.",
        "source_hashes": {},
        "status": "complete",
    }

    session = f'''# {SESSION_ID}

- tier: T3 — core generation, fourth-document alignment and canonical current-state update; no mathematical conclusion.
- role: GOVERNANCE_ALIGNMENT.
- authorization: the user directly required that their later theory-work guidance be fully recorded as core cognition and loaded every time. This covers the necessary source, curation, generated core/transition, explanatory fourth-document, recovery, audit and checkpoint work.
- protected discovery action: future work must begin with a theory-level target and an obvious core commitment, use learned knowledge only to generate candidates, and apply Russell pattern P before claiming a new target.
- critical boundary: Power Set, P0–P6, ETCS, forcing and all ZFC candidates are AI research designs or source cards; they are not inserted as user claims or mathematical results.
- core: {OLD_GENERATION}/55 → {NEW_GENERATION}/61; transition must preserve the old 55 units and append the six direct user messages.
- unchanged work: Goal7 / MO3-COVERAGE-C, the phase-closed HoTT Russell line, existing proof packages and all mathematical statuses remain unchanged.
- temporary state hygiene: the previously uncheckpointed MEMORY/001 additions are replayed verbatim inside this checkpoint payload after restoring the tracked base required by cognition_runtime. No user content is discarded.
- audit boundary: the current runtime cannot atomically create child files inside a session audit shard directory, so this transaction uses a complete legacy single-file KC audit and records the known writer limitation rather than bypassing the checkpoint path.

## source and use boundary

The source file contains only direct user messages. Curation and the new core preserve them verbatim. The extension is explicitly AI exposition. Machine checks can establish byte identity, source selection, transition coverage and checkpoint atomicity; they cannot establish that a model will understand or use the guidance correctly in every future session.
'''
    runs = {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "GOVERNANCE_CORE_GENERATION_METHOD_CONSOLIDATION",
        "checkpoint_result": RESULT,
        "base_snapshot": plan["snapshot"],
        "formal_runs": [],
        "governance_runs": [
            {"tool": "scripts/audit/build_core_cognition.py", "status": "generation-12 built before payload preparation; no mathematical claim"},
            {"tool": "scripts/audit/verify_core_cognition.py", "status": "must pass against curation-v12 and generation-12 transition before checkpoint"},
            {"tool": PREPARE, "status": "payload constructed and cognition_runtime dry-run must pass"},
            {"tool": ".codex/tools/cognition_runtime.py", "status": "only CHECKPOINT_COMMITTED result proves application"},
        ],
        "new_math_claims": [],
        "open": ["future semantic use of core", "P specification validation", "all ZFC and other theory candidates", "Goal7 / MO3-COVERAGE-C"],
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for doc in (direction, panorama, essay, memory):
        texts[doc["index_path"]] = doc["index_text"]
        texts.update(doc["shards"])
    texts[RESUME] = resume
    texts[STATE] = json_text(state)
    texts[session_path] = session
    texts[audit_path] = audit_text
    texts[runs_path] = json_text(runs)

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "The user explicitly required the later theory-work guidance to be fully recorded as core cognition and loaded every time. This checkpoint applies only the necessary core-generation, explanatory, recovery and current-state updates; it does not create a Goal, publish, push, or assert a mathematical result.",
        "load_profile": "governance",
        "task_ids": [],
        "core_transition": CORE_TRANSITION,
        "files": [
            {"path": rel, "expected_sha256": sha((ROOT / rel).read_bytes()) if (ROOT / rel).is_file() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    R.prepare(ROOT, plan["snapshot"], payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json_text(payload), encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "session_id": SESSION_ID,
        "snapshot": plan["snapshot"],
        "revision": NEXT_REVISION,
        "files": len(texts),
        "core_units": len(manifest["units"]),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
