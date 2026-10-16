#!/usr/bin/env python3
"""Prepare the revision-90 checkpoint for receipt/hydration/evidence repairs.

The script only prepares a canonical runtime payload.  It does not apply the
checkpoint, create a Git commit/tag, certify model understanding, or make a
mathematical claim.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-090-CHECKPOINT-HYDRATION-REPAIR"
PREV_SESSION = "S-RES-20260913-089-N43-HANDOFF-REPORT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
TRANSACTION_REL = f".codex/cognition/checkpoints/{SESSION_ID}/transaction.json"
GAP_REPORT = "audit/S086至S089-checkpoint收据缺失与治理修复设计-20260913.md"
DESIGN = "docs/design/detailed/认知水合关系与检查点事务合同.md"
SCAN = "audit/agda-unimath-e6-source-scan-20260913.json"

SPEC = importlib.util.spec_from_file_location("runtime_s090", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:100]}:{count}")
    return text.replace(old, new, 1)


def replace_line_prefix(text: str, prefix: str, new: str) -> str:
    lines = text.splitlines()
    hits = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(hits)}")
    lines[hits[0]] = new
    return "\n".join(lines) + "\n"


def line_with_prefix(text: str, prefix: str) -> str:
    hits = [line for line in text.splitlines() if line.startswith(prefix)]
    if len(hits) != 1:
        raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(hits)}")
    return hits[0]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def memory_text(root: Path) -> str:
    text = (root / "MEMORY.md").read_text(encoding="utf-8")
    start = text.index("## 当前执行队列")
    end = text.index("## 当前已验证状态")
    queue = """## 当前执行队列（2026-09-13）

1. S090 当前治理修复：保留 S086–S089 `CHECKPOINT_RECEIPT_MISSING` 历史事实，runtime 3.2 强制 SESSION/RUNS/36-KC audit 同事务并以 canonical result 为应用收据；修正五个 stable record 的水合关系和目录 scope。
2. 数学研究第一线：寻找**真实下游应用或派生开发中的 E6 consumer**。固定版本、调用链、输入与交付承诺，检查截断存在、商类、等价存在或 noncomputable 分类是否被提升成可执行数据。
3. 数学研究第二线：T3 共享判定联合递归。没有自然自验证 consumer 时保持 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不冒充 HoTT 悖论。
4. 第十三批抽样与无差别基础库扫描降优先级；只有出现新判别锚点或具体下游 consumer 才重开。
5. 当前仍未得到 E6、现实桥梁、`NATURAL_USAGE_MISMATCH`、自馈不可停机实例或 HoTT 内部矛盾；17 个 current proof package 仍只支持各自精确范围。
6. 历史交接开放项仍包括 2,396 条 claim、aistudio coverage、历史数学主张、response→artifact/code/Git 因果和 S067–S085 缺 KC audit；缺失历史证据不追溯伪造。
7. 接手现场已由 Git commit `35cace7` 保全；S090 修复提交与 `governance-v3.2.0` 最终版本闭合由本轮用户授权，尚未完成前仍标 pending。

"""
    text = text[:start] + queue + text[end:]
    text = replace_line_prefix(
        text,
        "- project-local governance 3.2",
        "- project-local governance 3.2 正在按用户授权闭合：修复前现场由 commit `35cace7` 保全；runtime 3.2 / PROTOCOL 2.3 / business Skill 1.8 已实现候选，S090 canonical checkpoint、修复提交与 `governance-v3.2.0` tag 仍待本轮完成；不 push。",
    )
    s086 = (
        "- S086 的 `MP-NOCANONICAL-001`（C-142–C-148）仍由独立重放支持；当前索引状态为 "
        "`ROW_STABLE_AFTER_INDEX_EVOLUTION`，不是 STATE 旧写法 exact。它是独立 Cubical/Type₀ 构造，与 agda-unimath 定理只作非正式对照；"
        "`NoCanonicalFinite.agda` 未被 final command 导入。N38 旧常量目标的 `s=id` 纠偏没有独立 claim/run/index，降为 paper-level 反例候选。"
    )
    text = replace_line_prefix(text, "- S086 完成 N40（第一项）", s086)
    text = replace_line_prefix(
        text,
        "- `MP-NOCANONICAL-001` 是第十一个 F-011 proof package",
        "- `MP-NOCANONICAL-001`（C-142–C-148）是独立 Cubical/Type₀ proof package：final run exit 0、stderr 0、零 warning，当前 `ROW_STABLE_AFTER_INDEX_EVOLUTION`、exact replay；判词 `UNLABELED_FINITE_NO_CANONICAL_POINT`。它不是 agda-unimath 源码重放；bridge 未由 final command 导入；N38 旧目标纠偏没有独立 claim/run/index，保持 paper-level。",
    )
    text = replace_line_prefix(
        text,
        "- S084 完成 N38",
        "- S084 是已被后续纠偏的历史尝试：旧常量目标和 eliminator 阻塞归因不再作为当前命题；原探针保留，精确否定在未另建 claim/run/index 前保持 paper-level。",
    )
    s088 = (
        "- S088 的 `MP-UNIMATH-NOSECTION-REPLAY-001` / C-05 固定 agda-unimath@`7b81411d` 并真实重放 486 条 Checking（1 项目目标 + 485 外部模块），"
        "exit 0、stderr 0、exact replay；该机器结果保留。外部 E6 结论已纠正为 `SOURCE_INSPECTED_BOUNDED_NEGATIVE`："
        "`foundation.global-choice` 不在保存 run 闭包；literate-aware 公设清点为 20 postulate / 9 primitive / 22 union，"
        "实际 run 闭包含 7 个声明文件；机器清单见 `audit/agda-unimath-e6-source-scan-20260913.json`。"
    )
    text = replace_line_prefix(text, "- S088 完成 N42(a)", s088)
    insertion = (
        "- S090 治理修复已进入 canonical checkpoint：S086–S089 缺事务收据被独立登记；runtime 32/32 单测覆盖 Session evidence Gate、目录 scope、related-record 非递归水合与依赖语义；task plan 的前后实测和 canonical result 由 S090 evidence 持有。\n"
    )
    text = replace_once(text, "## 当前已验证状态\n\n", "## 当前已验证状态\n\n" + insertion)
    return text


def direction_text(root: Path) -> str:
    text = (root / R.DIRECTION).read_text(encoding="utf-8")
    text = replace_once(text, "版本：`integrated-direction-portfolio/v1.6`", "版本：`integrated-direction-portfolio/v1.7`")
    text = replace_once(text, "状态：`N43_HANDOFF_REPORT_REVIEWED_QUEUE_CONTINUES`", "状态：`GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST`")
    text = replace_once(text, "<!-- integrated-direction-portfolio:v1.6", "<!-- integrated-direction-portfolio:v1.7")
    text = replace_once(text, "source_state_revision: 89", "source_state_revision: 90")
    text = replace_once(text, "projection_generation: 20260913-direction-073", "projection_generation: 20260913-direction-074")
    text = replace_once(text, "semantic_status: N43_HANDOFF_REPORT_REVIEWED_QUEUE_CONTINUES", "semantic_status: GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST")
    gate = line_with_prefix(text, "| `DIR-G-MATH-PROOF-DELIVERY-GATE`")
    new_gate = (
        "| `DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 AI 的数学结论交付前必须由匹配语义的 proof assistant/kernel 机器证明；"
        "源码、实际 run、索引和 external-replay 公设/闭包边界均留在 repo | 用户 ruling §15–§16 / F-011 | `ACTIVE_USER_DIRECTION` | "
        "`CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-MATH-PROOF-DELIVERY-GATE`、17 个 current proof package、3 个 legacy proof 行 | "
        "继续逐 claim 执行 source→run→index；外部源码审读不得冒充保存 run 检查 | `AGENTS.md`；数学证明规范；claim matrix；proof verifier |"
    )
    text = replace_once(text, gate, new_gate)
    governance = (
        "| `DIR-G-CHECKPOINT-HYDRATION-INTEGRITY` | applied checkpoint 必须有 canonical transaction/result，"
        "Session evidence 与 36-KC audit 同事务；叙事关系不递归污染 task hydration | 用户 ruling §16 / F-012 | `ACTIVE_USER_DIRECTION` | "
        "`CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-GOVERNANCE-CHECKPOINT-HYDRATION` | 以 S090 result、五个 task plan 和 release tag 闭合；历史 S086–S089 缺口不伪造 | "
        f"`{DESIGN}`；`{GAP_REPORT}`；runtime 3.2 |"
    )
    text = replace_once(text, new_gate, new_gate + "\n" + governance)
    work = (
        "4. **当前第一工作包**：从 N43 三选一收敛为真实下游 consumer 的 E6 定向审计。固定具体应用/派生开发、版本、调用链与交付承诺，"
        "只在它把截断存在、商类、等价存在或 noncomputable 分类提升成可执行数据时考虑 `NATURAL_USAGE_MISMATCH`。"
        "T3 共享判定联合递归为第二线；没有自然自验证 consumer 时保持通用 Gödel/对角边界。第十三批抽样与无差别基础库扫描降优先级。"
        "S088 的 C-05 外部重放仍有效；其 E6 扫描已降为 `SOURCE_INSPECTED_BOUNDED_NEGATIVE`，`foundation.global-choice` 不在保存 run 闭包。"
    )
    text = replace_line_prefix(text, "4. **当前第一工作包**", work)
    text = text.replace("；下一步按 N43 继续", "；下一步优先审计固定下游应用/派生开发的真实 consumer")
    text = text.replace("N42 在真实 agda-unimath 中复核同一分离（`count → ε-operator` 正控制、`no-global-choice` 反证）", "N42 在固定 agda-unimath 源码中 source-inspect 同一分离（`count → ε-operator` 正控制、`no-global-choice` 源码；后者不在 C-05 run 闭包）")
    return text


def panorama_text(root: Path) -> str:
    text = (root / R.PANORAMA).read_text(encoding="utf-8")
    text = replace_once(text, "版本：`integrated-outcome-panorama/v1.6`", "版本：`integrated-outcome-panorama/v1.7`")
    text = replace_once(text, "状态：`N43_HANDOFF_REPORT_REVIEWED_QUEUE_CONTINUES`", "状态：`GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST`")
    text = replace_once(text, "<!-- integrated-outcome-panorama:v1.6", "<!-- integrated-outcome-panorama:v1.7")
    text = replace_once(text, "source_state_revision: 89", "source_state_revision: 90")
    text = replace_once(text, "projection_generation: 20260913-outcome-073", "projection_generation: 20260913-outcome-074")
    text = replace_once(text, "semantic_status: N43_HANDOFF_REPORT_REVIEWED_QUEUE_CONTINUES", "semantic_status: GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST")
    verified = "| `VERIFIED_WITH_SCOPE` | 证据包、实现/来源和相称验证在明确范围内闭合 |"
    text = replace_once(text, verified, verified + "\n| `SOURCE_INSPECTED_WITH_SCOPE` | 固定源码和 lexical/结构锚点已核；没有进入保存 kernel run 的模块不得称为机器重放 |")
    gate = line_with_prefix(text, "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE`")
    text = replace_once(
        text,
        gate,
        "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE` | F-011 source/run/index 门禁与 external replay 分层 | `DIR-G-MATH-PROOF-DELIVERY-GATE` | 用户裁定与本地治理 | `VERIFIED_WITH_SCOPE` | 17 个 current package 与 3 个 legacy proof 行可按各自 run 核验；外部源码审读、外部重放和当前项目证明已分层 | 不证明 fresh 模型永久遵循，不把 defense/boundary 外推成悖论；version-close 仍待最终 tag | 数学证明规范；claim matrix；proof verifier |",
    )
    new_gate = line_with_prefix(text, "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE`")
    governance = (
        "| `OUT-TOP-GOVERNANCE-CHECKPOINT-HYDRATION` | S090 修复 checkpoint 收据、Session evidence Gate、目录 scope 与错误依赖水合 | "
        "`DIR-G-CHECKPOINT-HYDRATION-INTEGRITY` | 当前项目治理 | `VERIFIED_WITH_SCOPE` | runtime 3.2 单测 32/32；S086–S089 缺口有基线与独立审计；"
        "S090 只有在 canonical result 写成 `CHECKPOINT_COMMITTED` 时才会成为 current | 不恢复历史事务，不认证 KC 语义或模型理解，不证明数学 | "
        f"`{DESIGN}`；`{GAP_REPORT}`；`{RESULT_REL}` |"
    )
    text = replace_once(text, new_gate, new_gate + "\n" + governance)
    text = replace_line_prefix(
        text,
        "| `OUT-TOP-UNIMATH-E6-SCAN`",
        "| `OUT-TOP-UNIMATH-E6-SCAN` | 固定 agda-unimath@`7b81411d` 的 E6 源码/闭包审计：命名提升接口、`no-global-choice` 源码和带前提正控制可定位；保存 C-05 run 不含 `foundation.global-choice`；literate-aware 公设口径 20/9/22，实际外部闭包 485 模块、7 个声明文件 | `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-W-RP-B01`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前外部语料审计 | `SOURCE_INSPECTED_WITH_SCOPE / SOURCE_INSPECTED_BOUNDED_NEGATIVE` | 可复现 script/JSON 固定扫描规则、命中清单、树身份和 run 闭包 | 不证明全库语义上不存在 E6；不把 `no-global-choice` 称为 S088 已重放；不证明下游无误用 | `audit/unimath-e6-scan-and-nosection-replay-20260913.md` §3；`audit/agda-unimath-e6-source-scan-20260913.json` |",
    )
    text = replace_line_prefix(
        text,
        "| `OUT-TOP-NOCANONICAL-NATIVE-REPLAY`",
        "| `OUT-TOP-NOCANONICAL-NATIVE-REPLAY` | `MP-NOCANONICAL-001`：独立 Cubical/Type₀ 证明 unlabeled 二元素呈现无统一选点（C-142–C-148）；与 agda-unimath no-section 现象只作非正式对照 | `DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / UNLABELED_FINITE_NO_CANONICAL_POINT` | exit 0、stderr 0、零 warning、当前 `ROW_STABLE_AFTER_INDEX_EVOLUTION`、exact replay | 不证明两个外部/本地规格等价；final command 未导入 bridge；N38 旧目标纠偏仍是 paper-level；不证明 E6/悖论 | `NoCanonicalPoint.agda`；run `20260913-MP-NOCANONICAL-001-02`；C-142–C-148；N40 审计 |",
    )
    text = replace_line_prefix(
        text,
        "| `OUT-TOP-THREE-WAY-SKELETON`",
        "| `OUT-TOP-THREE-WAY-SKELETON` | generation-4 + LOAD_SET v3 + runtime 3.2 / STATE v2 的跨 Session 认知骨架 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-E-WEB-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-CHECKPOINT-HYDRATION-INTEGRITY` | 当前顶层治理 | `VERIFIED_WITH_SCOPE` | 三件套固定全文、profile/task hydration、Session evidence Gate 与 canonical checkpoint receipt 可机械核验 | 不证明模型理解、2,396 条历史语义或数学结论 | generation-4 evidence；S090 result；`.codex/` |",
    )
    text = text.replace("同轮外部 E6 扫描判 `BOUNDED_NEGATIVE_WITH_STRONGEST_COUNTEREXAMPLE`（`no-global-choice` 用 `no-section` 反证全局提升；`count` 等显式假设下才有 ε 算子）", "同轮外部 E6 源码扫描后经独立复审降为 `SOURCE_INSPECTED_BOUNDED_NEGATIVE`（`no-global-choice` 不在保存 run 闭包；literate-aware 20/9/22 公设口径）")
    text = text.replace("原生机器化 unlabeled 二元素无统一选点、纠偏 N38 假“常量陈述”", "独立机器化 unlabeled 二元素无统一选点；N38 旧目标纠偏保持 paper-level")
    return text


def frontier_text(root: Path) -> str:
    text = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    text = replace_once(text, "# HoTT 研究前沿（S031 原生命题截断防御）", "# HoTT 研究前沿（S090 治理修复后）")
    intro = (
        "本轮 S090 不新增数学结论：它把 S086–S089 标为缺 canonical checkpoint receipt，修复 task hydration 关系，"
        "把 S088 外部 E6 强说法降为 source-inspected，并把研究首选收敛到真实下游 consumer；T3 为第二线，batch 13/无差别基础库扫描降优先级。\n\n"
    )
    text = replace_once(text, "\n本文件是注意力槽", "\n" + intro + "本文件是注意力槽")
    text = replace_line_prefix(
        text,
        "| 已闭合工作包 47 |",
        "| 已闭合工作包 47 | unlabeled 无规范选点独立 Cubical/Type₀ 证明（S086，C-142–C-148） | `MACHINE_PROVED_LOCAL_UNCOMMITTED / UNLABELED_FINITE_NO_CANONICAL_POINT` | 当前 row-stable + exact replay；不是 agda-unimath 源码重放；bridge 未被 final command 导入；N38 旧目标纠偏 paper-only |",
    )
    text = replace_line_prefix(
        text,
        "| 已闭合工作包 50 |",
        "| 已闭合工作包 50 | agda-unimath E6 源码/闭包扫描（S088 后复审） | `SOURCE_INSPECTED_BOUNDED_NEGATIVE` | `foundation.global-choice` 不在 C-05 run；20 postulate / 9 primitive / 22 union；run 闭包 7 声明文件；E6 仍开放 |",
    )
    text = replace_line_prefix(
        text,
        "| 第一工作包 |",
        "| 第一工作包 | 固定下游应用/派生开发的真实 E6 consumer | active | 固定版本、调用链、输入和交付承诺；只有真实资格越级才升格 |",
    )
    text = text.replace("原生机器化 unlabeled 二元素呈现无统一选点（与 agda-unimath `no-section-type-2-Element-Type` 同内容）", "独立机器化 unlabeled 二元素呈现无统一选点（与 agda-unimath 现象仅作非正式对照）")
    text = text.replace("并纠正 N38 的假“常量陈述”", "；N38 旧目标纠偏保持 paper-level")
    text = text.replace("同轮外部 E6 扫描判 `BOUNDED_NEGATIVE_WITH_STRONGEST_COUNTEREXAMPLE`（`no-global-choice` 用 `no-section` 反证全局提升；`count`/`is-decidable`/DN-elim 等显式假设下才有 ε 算子）", "同轮外部 E6 扫描经复审降为 `SOURCE_INSPECTED_BOUNDED_NEGATIVE`（`foundation.global-choice` 不在保存 run 闭包；20/9/22 literate-aware 公设口径）")
    return text


def lessons_text(root: Path) -> str:
    text = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    text = replace_line_prefix(
        text,
        "62. 不要为错误命题寻找证明机制。",
        "62. 不要为疑似错误目标继续调证明机制。N38 的常量目标有 `s=id` 纸笔反例候选，但该精确否定没有独立 claim/run/index，按 F-011 必须降为 paper-level；机器已闭合的是 C-142–C-148 的自识别相干/无统一选点命题。先分开“目标纠偏”和“已机器证明内容”。",
    )
    text = replace_line_prefix(
        text,
        "66. 外部库的『自然提升消费者』",
        "66. 外部库源码中的定理不因位于同一仓库就自动成为保存 run 的已重放结论。agda-unimath 固定源码含 `no-global-choice` 与正控制，但 C-05 run 不导入 `foundation.global-choice`；当前只能称 source-inspected。literate-aware 扫描必须排除 Markdown prose，得到 20 postulate / 9 primitive / 22 union，实际 run 闭包 7 个声明文件。",
    )
    additions = (
        "\n68. `POST-CHECKPOINT.json` 是 AI 派生摘要，不能证明 checkpoint 已应用；唯一证据是 canonical runtime 生成的 transaction、before/after 与 `result.json.status=CHECKPOINT_COMMITTED`。历史缺收据必须登记，不能追溯补造。\n"
        "69. `depends_on` 不是时间线。只有会传播 stale 的验证依赖才递归水合；批次先后、报告概括、研究归属和相似现象必须用 `research_parent`/`related_records`，否则 query-first 原件会被重新拉成数十 MB 启动正文。\n"
        "70. task plan 的 `review_required=[]` 只说明已选 record 没有当前 stale 标记，不证明计划可装配。必须同时检查总 bytes/lines、document count、largest documents、query-first promotion，并实际完成 snapshot coverage。\n"
    )
    if not text.endswith("\n"):
        text += "\n"
    return text + additions


def resume_text(root: Path) -> str:
    text = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    text = replace_line_prefix(
        text,
        "4. 数学研究使用 research profile",
        "4. 数学研究使用 research profile，先 query stable record 再显式 task hydrate，并检查 hydration diagnostics；结束时把 SESSION/RUNS/当前全部 KC 回评放入同一 checkpoint，只有 canonical result 能证明应用。",
    )
    current = (
        "S090 治理修复：S086–S089 四轮缺 canonical checkpoint receipt 的事实已独立登记，禁止追溯伪造；runtime 3.2 强制 SESSION/RUNS/36-KC audit 同事务，"
        "并区分 `depends_on` 与非递归 `research_parent`/`related_records`。S088 的外部 E6 强说法降为 `SOURCE_INSPECTED_BOUNDED_NEGATIVE`；"
        "C-05 重放仍有效。下一数学主线是固定下游应用/派生开发的真实 E6 consumer；T3 第二线；batch 13/无差别基础库扫描降优先级。\n\n"
    )
    text = replace_once(text, "## 当前停止点\n", "## 当前停止点\n" + current)
    text = replace_line_prefix(
        text,
        "S088 完成 N42(a)",
        "S088 历史工作：C-05 外部派生文件重放在固定 agda-unimath@`7b81411d` 下 exit 0、stderr 0、486 条 Checking、exact replay，继续有效。其 E6 扫描经 S090 独立复审降为 source-inspected：`foundation.global-choice` 不在保存 run 闭包；20/9/22 literate-aware 公设口径，run 闭包 7 声明文件。",
    )
    text = replace_line_prefix(
        text,
        "S086 完成 N40（第一项）",
        "S086 历史工作：`MP-NOCANONICAL-001` / C-142–C-148 是独立 Cubical/Type₀ 证明，当前 row-stable + exact replay；不是外部源码重放，bridge 未被 final command 导入。N38 的 `s=id` 纠偏没有独立 claim/run/index，保持 paper-level。",
    )
    text = replace_line_prefix(
        text,
        "S084 完成 N38",
        "S084 历史尝试已被 S086/S090 纠偏：其常量目标与 eliminator 阻塞归因不得作为当前命题；原文件保留为历史失败证据。",
    )
    return text


def session_audit(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000001": "本轮把‘凭什么’落实到可复现治理收据：缺 checkpoint 不能由 POST 自证，task 水合必须有规模和来源边界。",
        "KC-000005": "本轮没有宣布悖论；先修交接真实性与证据边界，再恢复数学搜索。",
        "KC-000010": "保持现实相对悖论与内部矛盾分离；治理修复不把任何 defense/boundary 升格。",
        "KC-000012": "Checkpoint 和 task hydration 现在都有先行合法性检查，相当于对研究过程本身执行 ASK。",
        "KC-000013": "阻止 query-first 原件因叙事依赖回灌，保护理论工具性不掩盖执行/上下文资格。",
        "KC-000017": "三件套在压缩后已重新全文加载；修复目标正是降低训练惯性与局部摘要替代完整用户认知的风险。",
        "KC-000021": "两个受影响 proof run 被真实重放；S088 的未运行源码命题主动降级，符合机器证明要求。",
        "KC-000022": "两类现实相对悖论仍未建立；本轮只修证据和下一搜索入口，不用治理 PASS 冒充数学结果。",
        "KC-000027": "T3 被明确置为第二线并保留通用 Gödel/程序边界，不把一般计算限制冒充 HoTT 特有结果。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮是治理/证据修复，不新增数学结论。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned:
            relation = "ALIGNED"
            assessment = aligned[kid]
            evidence = f"`{DESIGN}`；`{GAP_REPORT}`；runtime 3.2 tests；{kid}"
        else:
            relation = "NOT_TOUCHED"
            assessment = f"本轮只修复治理与证据合同，没有研究或重新裁决“{label}”的数学/哲学内容。"
            evidence = f"`{GAP_REPORT}` §4；本轮 scope；{kid}"
        unresolved = "对应数学方向保持既有状态；E6、现实桥梁与 HoTT 悖论仍未建立。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | {evidence} | {unresolved} |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 没有新的用户悖论/元数学原文，generation-4/36 KC 保持逐字不变。",
        "- direction_change: YES — 增加 checkpoint/hydration 治理方向，并把数学首选从 N43 三选一收敛到真实下游 E6 consumer；T3 为第二线。",
        "- panorama_change: YES — 记录历史 checkpoint 缺口、runtime 3.2 修复、S086/S088 证据降级与 scan 收据。",
        "- update_decision: STATE revision 90；错误叙事依赖改 related_records；A-KC-AUDIT-GAP 使用 scope locator；新增 F-012 对应治理记录。",
        "- cross_conflicts: S086–S089 POST 自述与缺失 transaction/result 冲突；S088 强 E6 文字与实际 C-05 run 闭包冲突；均以直接证据纠正。",
        "- unresolved: fresh 模型行为仍 NOT_RUN；S067–S085 的缺失语义回评不可重建；最终 Git version-close 尚待后续提交/tag；数学目标仍开放。",
        "", "## 汇总", "", "`ALIGNED=9`；`NOT_TOUCHED=27`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return f"""# {SESSION_ID}

- 用户授权：`rulings.md` §16，“按照你的建议处理”；范围含本地治理修复、证据修正、精确 commit/tag，不含 push。
- 历史保全：修复前 1,915 路径现场已提交为 `35cace7`；旧 S086–S089 POST 未改写。
- 历史缺口：四轮均缺 canonical checkpoint 目录，登记为 `CHECKPOINT_RECEIPT_MISSING / DIRECT_STATE_WRITE_NOT_ATOMICALLY_ATTESTED`；不补造。
- Runtime 3.2：`depends_on` 只表示 verification staleness；`related_records` 不水合；目录 scope locator；plan hydration diagnostics；SESSION/RUNS/全量 KC audit 同事务 Gate。
- 证据修正：S086 保留 C-142–C-148，但改称独立 Cubical/Type₀ 构造，当前 row-stable；N38 旧目标纠偏 paper-only，bridge 未由 final command 检查。S088 保留 C-05 external replay；E6 扫描降为 source-inspected，20/9/22 与 7-file closure 有 JSON 收据。
- 研究统筹：第一线改为真实下游应用/派生开发的 E6 consumer；T3 第二线；batch 13 与无差别基础库扫描降优先级。
- 本轮不新增数学 claim；core generation-4/36 不变。只有 `{RESULT_REL}` 实际出现且 status 为 CHECKPOINT_COMMITTED，才可称 S090 checkpoint applied。
"""


def runs_text() -> str:
    value = {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "work_kind": "governance_checkpoint_hydration_and_evidence_repair",
        "baseline_commit": "35cace735a58",
        "pre_checkpoint_checks": {
            "runtime_tests": "32/32 PASS",
            "scan_unit_tests": "2/2 PASS",
            "scan_receipt": SCAN,
            "n40_replay": "PASS_WITH_SCOPE / ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
            "n42_replay": "PASS_WITH_SCOPE / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "checkpoint_contract": {
            "transaction": TRANSACTION_REL,
            "result": RESULT_REL,
            "required_result_status": "CHECKPOINT_COMMITTED",
            "post_checkpoint_summary_cannot_self_attest": True,
        },
        "mathematics": "NO_NEW_MATHEMATICAL_CLAIM",
        "model_understanding": "NOT_CERTIFIED_BY_TOOL",
        "git_release": "PENDING_REPAIR_COMMIT_AND_GOVERNANCE_V3_2_0_TAG",
    }
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def add_related(record: dict, values: list[str]) -> None:
    record["related_records"] = sorted(set(record.get("related_records", [])) | set(values))


def mutate_state(root: Path, state: dict, texts: dict[str, str]) -> dict:
    records = state["records"]
    n40 = records["A-NOCANONICAL-POINT-001"]
    add_related(n40, ["A-LIBRARY-INTERFACE-NO-RECOVERY-001", "A-UNIMATH-NOSECTION-REPLAY-001"])
    n40["depends_on"] = []
    n40["formal"]["index_validation"] = "ROW_STABLE_AFTER_INDEX_EVOLUTION"
    n40["terminology"] = "INDEPENDENT_CUBICAL_TYPE0_ANALOGUE_NOT_EXTERNAL_SOURCE_REPLAY"
    n40["n38_correction_status"] = "PAPER_ONLY_WITH_EXPLICIT_COUNTEREXAMPLE_CANDIDATE"
    n40["bridge_kernel_status"] = "SOURCE_PINNED_NOT_IMPORTED_BY_FINAL_COMMAND"
    n40["resolution"]["reason"] = "C-142–C-148 remain kernel-accepted and exact-replayable in the pinned Cubical toolchain; after matrix evolution the current index verdict is ROW_STABLE_AFTER_INDEX_EVOLUTION. This is an independent Cubical/Type0 analogue, not a proved equivalence to or replay of the agda-unimath source theorem. The N38 s=id correction is paper-level unless separately indexed, and the bridge file was source-pinned but not imported by the final command."

    batch = records["A-BATCH12-001"]
    add_related(batch, ["A-BATCH11-001"]); batch["depends_on"] = []

    replay = records["A-UNIMATH-NOSECTION-REPLAY-001"]
    add_related(replay, ["A-E6-DERIVED-SCAN-001", "A-NOCANONICAL-POINT-001"])
    replay["depends_on"] = []
    replay["research_parent"] = "A-NATURAL-CONSUMER-AUDIT-001"

    scan = records["A-UNIMATH-E6-SCAN-001"]
    add_related(scan, ["A-UNIMATH-NOSECTION-REPLAY-001", "A-NATURAL-CONSUMER-AUDIT-001"])
    scan["depends_on"] = []
    scan["classification"] = "SOURCE_INSPECTED_BOUNDED_NEGATIVE"
    scan["evidence_status"] = "SOURCE_INSPECTED_WITH_SCOPE"
    for rel in [SCAN, "scripts/audit/scan_agda_unimath_e6.py", "scripts/audit/test_scan_agda_unimath_e6.py"]:
        if rel not in scan["full_sources"]: scan["full_sources"].append(rel)
    scan["resolution"] = {
        "reason": "Pinned-source audit reproduces named epsilon/global-choice/positive-control anchors, a literate-aware 20 postulate / 9 primitive / 22 union count, and the actual C-05 replay closure (485 external modules; 7 declaration files). foundation.global-choice is not in that saved run, so no-global-choice is SOURCE_INSPECTED_NOT_REPLAYED_BY_THIS_RUN. No E6 was established in the bounded named-interface scan.",
        "evidence": ["audit/unimath-e6-scan-and-nosection-replay-20260913.md", SCAN, "scripts/audit/scan_agda_unimath_e6.py"],
    }
    scan["scope"] = "Lexical/source and saved-run-closure audit of pinned agda-unimath 7b81411d. No full-library semantic absence theorem, no downstream-consumer absence theorem, and no replay of foundation.global-choice."

    handoff = records["A-HANDOFF-REPORT-S086-S088-001"]
    add_related(handoff, ["A-UNIMATH-NOSECTION-REPLAY-001", "A-UNIMATH-E6-SCAN-001", "A-BATCH12-001", "A-NOCANONICAL-POINT-001"])
    handoff["depends_on"] = []
    handoff["classification"] = "HANDOFF_REPORT_CORRECTED_WITH_SCOPE"
    handoff["resolution"]["reason"] = "The report remains navigation but is corrected against direct evidence: S086 is row-stable and an independent Cubical/Type0 analogue; N38 correction is paper-level and the bridge was not imported; machine-backed claims are 83 -> 90 plus one external replay; S088 E6 scan is source-inspected; startup order and historical checkpoint receipt gaps are explicit."

    kc_gap = records["A-KC-AUDIT-GAP-001"]
    kc_gap["path_mode"] = "scope_locator"
    if GAP_REPORT not in kc_gap["full_sources"]: kc_gap["full_sources"].append(GAP_REPORT)
    if GAP_REPORT not in kc_gap["resolution"]["evidence"]: kc_gap["resolution"]["evidence"].append(GAP_REPORT)
    kc_gap["scope"] = "S067–S085 lack semantic 36-KC audits and are not retroactively reconstructed. The directory path is a scope locator; explicit hydration loads direct evidence files rather than the directory as text."

    affected = [
        "S-RES-20260913-086-N40-NOCANONICAL-NATIVE",
        "S-RES-20260913-087-N41-BATCH12",
        "S-RES-20260913-088-N42-UNIMATH-REPLAY",
        "S-RES-20260913-089-N43-HANDOFF-REPORT",
    ]
    for sid in affected:
        records[sid]["checkpoint_attestation"] = {
            "status": "CHECKPOINT_RECEIPT_MISSING",
            "post_checkpoint_self_attestation": "UNSUPPORTED_AS_APPLICATION_RECEIPT",
            "canonical_checkpoint_directory": f".codex/cognition/checkpoints/{sid}",
            "audit": GAP_REPORT,
            "historical_session_not_rewritten": True,
        }

    records["A-CHECKPOINT-RECEIPT-GAP-S086-S089-001"] = {
        "kind": "historical_governance_evidence_gap",
        "path": GAP_REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "CHECKPOINT_RECEIPT_MISSING_DIRECT_STATE_WRITE_NOT_ATOMICALLY_ATTESTED",
        "depends_on": [],
        "related_records": affected,
        "full_sources": [GAP_REPORT] + [f".codex/research/hott/sessions/{sid}/POST-CHECKPOINT.json" for sid in affected],
        "source_hashes": {},
        "resolution": {"reason": "All four POST files self-report checkpoint_applied=true, but all four canonical checkpoint directories are absent. The gap is preserved, not retroactively fabricated; future checkpoints use runtime 3.2.", "evidence": [GAP_REPORT]},
        "scope": "Historical checkpoint-process attestation only; does not invalidate independently retained mathematical proof runs.",
    }
    records["A-GOVERNANCE-REPAIR-S090-001"] = {
        "kind": "governance_repair",
        "path": DESIGN,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "CHECKPOINT_AND_HYDRATION_INTEGRITY_REPAIRED",
        "depends_on": [],
        "related_records": ["A-CHECKPOINT-RECEIPT-GAP-S086-S089-001", "A-KC-AUDIT-GAP-001", "A-HANDOFF-REPORT-S086-S088-001"],
        "full_sources": [DESIGN, GAP_REPORT, ".codex/tools/cognition_runtime.py", ".codex/skills/hott-paradox-research/checks/test_cognition_runtime.py", SCAN, RESULT_REL],
        "source_hashes": {},
        "resolution": {"reason": "Runtime 3.2 separates verification dependencies from lineage, supports directory scope locators, emits hydration diagnostics, and requires SESSION/RUNS/full ordered KC audit in every applied checkpoint. S090 itself is accepted only through its canonical result.", "evidence": [DESIGN, GAP_REPORT, ".codex/skills/hott-paradox-research/checks/test_cognition_runtime.py", RESULT_REL]},
        "scope": "Project-local cognition runtime and governance contract only; no model-comprehension or mathematics certification.",
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    records[SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete", "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE", "depends_on": [],
        "related_records": [PREV_SESSION, "A-GOVERNANCE-REPAIR-S090-001", "A-CHECKPOINT-RECEIPT-GAP-S086-S089-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, TRANSACTION_REL, DESIGN, GAP_REPORT, SCAN],
        "source_hashes": {},
        "scope": "S090 project-local governance and evidence repair; no new mathematical claim.",
    }

    state["revision"] = 90
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": "GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST",
        "next_minimal_verification": "First line: a pinned downstream application/derived-development consumer with a concrete qualification-to-delivery call chain. Second line: T3 shared-decision joint recursion. Batch 13 and undirected foundational scans are deprioritized.",
    })
    state["load_policy"]["runtime_version"] = "3.2.0"
    state["projection"]["status"] = "CORE_GENERATION_4_GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update({
        "projection_generation": "20260913-direction-074",
        "semantic_status": "CORE_GENERATION_4_GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST",
        "scope": "Portfolio after S090 governance/evidence repair: downstream natural consumers are the first research line; T3 is second; batch 13 and undirected foundational scans are deprioritized.",
    })
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update({
        "projection_generation": "20260913-outcome-074",
        "semantic_status": "CORE_GENERATION_4_GOVERNANCE_REPAIR_APPLIED_DOWNSTREAM_E6_CONSUMER_FIRST",
        "scope": "Panorama after S090: historical checkpoint gaps, compact task hydration, S086/S088 evidence corrections, and source-inspected E6 status are current.",
    })

    def proposed_bytes(rel: str) -> bytes:
        if rel in texts:
            return texts[rel].encode("utf-8")
        path = root / rel
        if not path.is_file():
            raise ValueError(f"SOURCE_HASH_TARGET_MISSING:{rel}")
        return path.read_bytes()

    for key, record in records.items():
        hashes = record.get("source_hashes")
        if not isinstance(hashes, dict):
            continue
        changed = False
        for rel, old_hash in list(hashes.items()):
            new_hash = sha_bytes(proposed_bytes(rel))
            if new_hash != old_hash:
                hashes[rel] = new_hash; changed = True
        if changed:
            record["revalidation"] = "S090 refreshed changed governance/audit projection hashes after direct evidence correction; mathematical proof sources and retained kernel run bodies were not rewritten. Final validators and affected proof replays remain required after checkpoint."

    for key in ("A-CHECKPOINT-RECEIPT-GAP-S086-S089-001", "A-GOVERNANCE-REPAIR-S090-001"):
        record = records[key]
        for rel in record["resolution"]["evidence"]:
            if rel == RESULT_REL: continue
            record["source_hashes"][rel] = sha_bytes(proposed_bytes(rel))
    for rel in [SCAN, "scripts/audit/scan_agda_unimath_e6.py", "scripts/audit/test_scan_agda_unimath_e6.py"]:
        scan["source_hashes"][rel] = sha_bytes(proposed_bytes(rel))
    for sid in affected:
        rel = f".codex/research/hott/sessions/{sid}/POST-CHECKPOINT.json"
        records["A-CHECKPOINT-RECEIPT-GAP-S086-S089-001"]["source_hashes"][rel] = sha_bytes(proposed_bytes(rel))
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 89 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_89_AND_S089")

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    texts = {
        "MEMORY.md": memory_text(root),
        R.DIRECTION: direction_text(root),
        R.PANORAMA: panorama_text(root),
        f"{R.PREFIX}FRONTIER.md": frontier_text(root),
        f"{R.PREFIX}LESSONS.md": lessons_text(root),
        f"{R.PREFIX}RESUME.md": resume_text(root),
        session_path: session_text(),
        audit_path: session_audit(root),
        runs_path: runs_text(),
    }
    state = mutate_state(root, state, texts)
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly accepted the six recommended S086-S088 repairs ('按照你的建议处理'), including project-local governance/evidence edits and exact local commit/tag. This checkpoint writes only the authorized in-repo cognition owners and new S090 session evidence; it does not push, publish, restore removed sources, or create mathematical claims.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 90, "session_id": SESSION_ID, "files": len(payload["files"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
