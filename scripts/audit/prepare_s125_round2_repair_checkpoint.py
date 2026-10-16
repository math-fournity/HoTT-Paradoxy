#!/usr/bin/env python3
"""Prepare revision 125: repair the second-audit findings and take over the workline."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-125-ROUND2-AUDIT-REPAIR-TAKEOVER"
PREV = "S-GOV-20260913-124-INDEPENDENT-AUDIT-ABSORPTION"
RESULT_ID = "A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001"
REPORT = "audit/独立审计第二轮整改与接管-20260913.md"
IMPORTED_AUDIT = (
    "audit/imports/audit-absorption-round2-20260913/"
    "独立审计吸收-第二轮审计-20260913.md"
)
IMPORT_MANIFEST = "audit/imports/audit-absorption-round2-20260913/IMPORT.json"
OLD_ABSORPTION = "audit/独立审计吸收与独立核验-20260913.md"
TECH_REPORT = "audit/统观工作技术报告-20260913.md"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
VERIFIER = "scripts/audit/verify_proof_version_closure.py"
MARK = "scripts/audit/mark_proof_run_indexed.py"
FREEZE = "scripts/audit/freeze_proof_index_rows.py"
TESTS = "scripts/audit/test_proof_evidence_links.py"
PROOF_CONTRACT = "docs/quality/数学结论机器证明与证据留存规范.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_ROUND2_AUDIT_REPAIR_TAKEOVER"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s125", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:80]}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_line(text: str, marker: str, replacement: str, *, starts: bool = False) -> str:
    lines = text.splitlines()
    matches = [
        index
        for index, line in enumerate(lines)
        if (line.startswith(marker) if starts else marker in line)
    ]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


AUDIT_FOCUS = {
    "KC-000005": (
        "CORRECTED",
        "撤回“已穷尽收口”的当前叙述；发现优先不等于可以用有界样本关闭未检查方向。",
    ),
    "KC-000014": (
        "TENSION",
        "S109 曾把 B 方向压入单一门 B；本轮恢复 B 方向独立行与其它未落账轴的资格。",
    ),
    "KC-000015": (
        "TENSION",
        "理论经济分析继续保留，但支付装置坐标不再被当作候选准入或穷尽 Gate。",
    ),
    "KC-000017": (
        "ALIGNED",
        "接管以独立审计反例纠正旧 AI 的自评，不以原 AI 的完成声明替代直接证据。",
    ),
    "KC-000021": (
        "ALIGNED",
        "证明证据链增加 proof/run/source/claim 身份与 replay 关系回归；不新增数学 claim。",
    ),
    "KC-000024": (
        "ALIGNED",
        "时间/运动结构与量词/完成顺序重新进入可执行候选面，不再被两条暂选路线排除。",
    ),
    "KC-000030": (
        "CORRECTED",
        "当前 owner 原位收敛第一轮吸收的覆盖不足；理论经济账本保持可证伪方法而非完成定理。",
    ),
    "KC-000035": (
        "ALIGNED",
        "表达/覆盖只保留为三个已检查样本；没有把未证的全域否定继续写进当前状态。",
    ),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元接管被审计 AI 的工作线并修复第二轮审计 R2-1～R2-5，不启动新数学研究。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = AUDIT_FOCUS.get(
            kid,
            ("NOT_TOUCHED", f"本轮没有重新研究或裁决“{label}”的数学/哲学内容。"),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{REPORT}`；{kid} | "
            "既有数学开放项保持。 |"
        )
    corrected = sum(1 for relation, _ in AUDIT_FOCUS.values() if relation == "CORRECTED")
    aligned = sum(1 for relation, _ in AUDIT_FOCUS.values() if relation == "ALIGNED")
    tension = sum(1 for relation, _ in AUDIT_FOCUS.values() if relation == "TENSION")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文，generation-4/36 KC 保持。",
        "- direction_change: YES_IN_PLACE — 研究方向行与优先级撤回穷尽关闭，保留暂选路线和其它轴资格。",
        "- panorama_change: YES_IN_PLACE — triage、S108/S109、C-168 与第一轮吸收结果均原位收敛；新增接管修复行。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: R2-1～R2-5 全部修复；数学 claim/ERCF-3 判词不变。",
        "- cross_conflicts: S107–S109 历史文档/回评与当前结论不同；保留历史，CURRENT owners 使用本轮处置。",
        "- unresolved: F3 广义数学问题、C11 未落账轴、triage 语义队列、T3 表示性/反射/不动点与 fresh model 行为仍开放。",
        "",
        "## 汇总",
        "",
        f"`ALIGNED={aligned}`；`CORRECTED={corrected}`；`TENSION={tension}`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def append_revalidation(record: dict, note: str) -> None:
    previous = str(record.get("revalidation", "")).strip()
    record["revalidation"] = (previous + " " + note).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    for rel in (
        REPORT,
        IMPORTED_AUDIT,
        IMPORT_MANIFEST,
        OLD_ABSORPTION,
        TECH_REPORT,
        REGISTRY,
        VERIFIER,
        MARK,
        FREEZE,
        TESTS,
        PROOF_CONTRACT,
    ):
        if not (root / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 124 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_124_S124")

    direction = projection_edit.load(root, R.DIRECTION)
    direction["shards"]["方向追踪/002 - 治理与用户方向.md"] = replace_line(
        direction["shards"]["方向追踪/002 - 治理与用户方向.md"],
        "`DIR-TOP-THEORY-ECONOMY-LEDGER`",
        "| `DIR-TOP-THEORY-ECONOMY-LEDGER` | HoTT 理论经济账本与悖论位置判别：六字段账本、补偿动作三分与多坐标检查；坐标用于提出和审查候选，不是准入或穷尽 Gate | 用户 2026-09-13 要求系统化统观；C11 v2；两轮独立审计 | `ACTIVE_USER_DIRECTION` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY`, `TIME_AND_TEMPORALITY`, `SELF_REFERENCE` | `OUT-TOP-THEORY-ECONOMY-LEDGER`、`OUT-TOP-TRIAGE-AND-OBLIGATION-ROUND1`、`OUT-TOP-AUTONOMOUS-ROUND2-INVARIANT-CLOSURE`、`OUT-TOP-SEARCH-SPACE-TWO-DOORS`、`OUT-TOP-INDEPENDENT-AUDIT-ROUND2-REPAIR` | P1/P2/P3 只保留各自有界判词；词汇 triage 因收益/成本暂停，43 条队列开放且至少两条是真实消费者；S108 的“自动同余/空集”有论证缺口；S109 的身份/表达检查不穷尽。门 A/门 B 是暂选路线；时间/运动结构、量词与完成顺序、B 方向独立行及其它未构造形状均可产生下一工作包。下一步应固定一个具体轴、版本、任务与判据，或核一个真实 consumer；不得从旧关闭结论筛掉候选 | `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md`；`audit/独立审计第二轮整改与接管-20260913.md` |",
    )
    direction["shards"]["方向追踪/005 - 交叉审视、优先级与更新规则.md"] = replace_line(
        direction["shards"]["方向追踪/005 - 交叉审视、优先级与更新规则.md"],
        "4. **当前第一工作包",
        "4. **当前第一工作包（接管修复后的可选入口）**：继续用 C11 v2 的六字段与多坐标审查候选，但任何坐标都不是准入 Gate。P1/P2/P3 是有界历史结果；triage 队列开放；S108/S109 不再关闭不敏感、身份或表达形状；门 A/门 B 只是两条暂选路线。下一工作包可以来自时间/运动结构、量词与完成顺序、B 方向独立行、其它新构造或固定真实 consumer；选定后必须固定任务、版本、调用链、承诺与可反驳判据。T3 自足编码线已闭合，剩余表示性/反射工作只有在明确 consumer 下启动；第十三批抽样与无差别基础库扫描保持低优先级。",
        starts=True,
    )
    for old, new in (
        ("source_state_revision: 124", "source_state_revision: 125"),
        ("projection_generation: 20260913-direction-106", "projection_generation: 20260913-direction-107"),
        (
            "semantic_status: GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST",
            f"semantic_status: {STATUS}",
        ),
        (
            "状态：`GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST`",
            f"状态：`{STATUS}`",
        ),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(root, R.PANORAMA)
    panorama_shard = "全景视野/004 - 距离综合与消费者审计.md"
    panorama["shards"][panorama_shard] = replace_line(
        panorama["shards"][panorama_shard],
        "`OUT-TOP-TRIAGE-AND-OBLIGATION-ROUND1`",
        "| `OUT-TOP-TRIAGE-AND-OBLIGATION-ROUND1` | C11 v2 §6 第一轮：两批各 20 条词汇 triage 样本均非候选；自主候选 #1 退化到 C-142–C-148。独立审计随后确认未读队列至少含两条真实截断消费者 | `DIR-TOP-THEORY-ECONOMY-LEDGER` | S107 历史工作 + 两轮独立审计 | `DOCUMENTED / TRIAGE_PAUSED_COST_BENEFIT_QUEUE_OPEN` | 40 条已读样本的分类与候选 #1 的退化结论保留；词汇方法边际收益不足，43 条队列继续开放；真实消费者、条件合法与资格越级分开判断 | 不新增数学 claim；不证明队列其余项是假阳性，不建立 E6，不关闭 consumer 搜索 | `audit/triage批次与自主构造第一轮-20260913.md`；`audit/独立审计第二轮整改与接管-20260913.md` |",
    )
    panorama["shards"][panorama_shard] = replace_line(
        panorama["shards"][panorama_shard],
        "`OUT-TOP-AUTONOMOUS-ROUND2-INVARIANT-CLOSURE`",
        "| `OUT-TOP-AUTONOMOUS-ROUND2-INVARIANT-CLOSURE` | S108 对 `UnlabeledTwoElement` 的六个观察量做了有界纸笔检查；第二轮审计指出从“识别不敏感”到 recursor 所需函数、集合余域和同余证明均已构造存在缺口 | `DIR-TOP-THEORY-ECONOMY-LEDGER` | S108 历史工作 + 独立审计 F3 | `DOCUMENTED / PAPER_ONLY_ARGUMENT_GAP_RESEARCH_OPEN` | 五类命题值观察量和统一选点案例可作为该家族的已检查样本；“统一选点不敏感”不成立这一局部观察保留 | 不能推出“不敏感 + 不可满足义务”为空集，不能关闭该任务形状，也不新增数学 claim | `audit/自主构造第二轮-识别不敏感与相干义务-20260913.md`；`audit/独立审计第二轮整改与接管-20260913.md` |",
    )
    panorama["shards"][panorama_shard] = replace_line(
        panorama["shards"][panorama_shard],
        "`OUT-TOP-SEARCH-SPACE-TWO-DOORS`",
        "| `OUT-TOP-SEARCH-SPACE-TWO-DOORS` | S109 检查了三种身份差异使用位置与三个表达候选，并提出门 A/门 B；独立审计撤回其穷尽收口 | `DIR-TOP-THEORY-ECONOMY-LEDGER` | S109 历史工作 + 独立审计 F3/F4 | `DOCUMENTED / BOUNDED_AXIS_CHECKS_NON_EXHAUSTIVE / PROVISIONAL_ROUTES` | 已检查样本与两条路线仍可用于生成候选；路线各有明确输入条件 | 不证明身份轴、表达轴或整个搜索空间关闭；不证明只剩两条路线，也不证明路线之外必有成功候选 | `audit/自主构造第三轮-表达与身份两轴-20260913.md`；`audit/独立审计第二轮整改与接管-20260913.md` |",
    )

    t3_shard = "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md"
    panorama["shards"][t3_shard] = replace_line(
        panorama["shards"][t3_shard],
        "`OUT-TOP-ERCF3-T3-ARITHMETIC-TAGS`",
        "| `OUT-TOP-ERCF3-T3-ARITHMETIC-TAGS` | `MP-ERCF3-T3-ARITH-TAGS-001`（C-166–C-168）：偶/奇标签算术与 `codeAtom` 单射；C-168 的精确对象是 `double`，不是 `codeAtom` | `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | T3 第十七脉冲 + F1 更正 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / NARRATIVE_CORRECTED` | C-166/C-167 与 C-168 的 `double` 命题由原 run 支持；C-184/C-185 另证 `codeAtom` 满射；C-186/C-187 另证 `codeT'`/`codeF'` 像不含 1，因此全 `Nat` 解码规格须定义像外行为，当前缺省分支在 1 上可达 | 原冻结 C-168 行保留为历史错误叙述，不再作为 CURRENT 语义；不量化所有解码器实现；不涉及 P 表示性/反射/不动点 | `HoTT/formal/ercf3-t3/README.md`；`C-166`–`C-168`；`C-184`–`C-187`；`audit/独立审计第二轮整改与接管-20260913.md` |",
    )
    panorama["shards"][t3_shard] = replace_line(
        panorama["shards"][t3_shard],
        "`OUT-TOP-INDEPENDENT-AUDIT-ABSORPTION`",
        "| `OUT-TOP-INDEPENDENT-AUDIT-ABSORPTION` | 第一轮独立审计吸收：建立 C-184–C-187、三类文件完整性检查与部分语义修订；第二轮确认其“完整吸收/F2 已闭合”判断过强 | `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | S124 | `HISTORICAL_FIRST_ROUND / SUPERSEDED_BY_ROUND2_REPAIR` | 第一轮机器证明和历史保全继续有效 | 不证明当前入口或 proof/run/index 身份在 S124 已闭合 | `audit/独立审计吸收与独立核验-20260913.md`；`audit/独立审计第二轮整改与接管-20260913.md` |",
    )
    projection_edit.append_to_shard(
        panorama,
        t3_shard,
        "| `OUT-TOP-INDEPENDENT-AUDIT-ROUND2-REPAIR` | 接管被审计 AI 的工作线并闭合第二轮 R2-1～R2-5：current owner 原位收敛、C-168 叙述纠正、v2 proof/run/index 身份检查、精确 run 依赖例外、显式 replay 关系 | `DIR-TOP-THEORY-ECONOMY-LEDGER`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前接管工作包 | `VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM` | 九项受控回归覆盖 run 交换、漏/重 claim、RUN 身份/命令、文件漂移、计数、例外外溢与 replay register→mark→freeze；原 proof/run/matrix 历史不改 | 不重新证明数学，不认证 fresh model 理解，不关闭 F3 广义问题或 HoTT 研究方向 | `audit/独立审计第二轮整改与接管-20260913.md`；`scripts/audit/test_proof_evidence_links.py`；`HoTT/verification/PROOF_VERSION_CLOSURE.json` |",
    )
    for old, new in (
        ("source_state_revision: 124", "source_state_revision: 125"),
        ("projection_generation: 20260913-outcome-106", "projection_generation: 20260913-outcome-107"),
        (
            "semantic_status: GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST",
            f"semantic_status: {STATUS}",
        ),
        (
            "状态：`GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST`",
            f"状态：`{STATUS}`",
        ),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(root, "MEMORY.md")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "2. 数学研究第一线",
        "2. 数学研究第一线（S125 接管修复后）：C11 v2 的六字段与多坐标继续用于提出、比较和反驳候选，但不是准入或穷尽 Gate。P1/P2/P3 只保留有界判词；两批 40 条词汇 triage 因收益/成本暂停，43 条队列开放且至少两条为真实截断消费者；S108 的“不敏感 ⇒ 自动给出同余证明/空集”有论证缺口；S109 的身份与表达检查只是样本。门 A/门 B 是两条暂选路线，时间/运动结构、量词与完成顺序、B 方向独立行及其它未构造形状均有研究资格。下一工作包须固定一个具体轴或真实 consumer、版本、同一任务和可反驳判据；当前仍无 E6、`NATURAL_USAGE_MISMATCH` 或 HoTT 内部矛盾。",
        starts=True,
    )
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "3. 数学研究第二线",
        "3. 数学研究第二线：T3 编码线的自足部分仍由 C-157–C-187 支持。C-168 只证明 `double` 下 1 无原像；`codeAtom` 实际满射（C-184/C-185）；`codeT'`/`codeF'` 像不含 1（C-186/C-187），所以全 `Nat` 解码规格须定义像外行为，当前缺省分支在 1 上可达。编码/解码/替换/引用已闭合到其精确范围；对象层可表示性、证明谓词 `P` 的表示性、反射与对角不动点仍需明确 consumer。ERCF-3 保持 `GATED`，不从通用 Gödel 机制外推 HoTT 悖论。",
        starts=True,
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S125 第二轮审计整改与接管（`A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001`）：以逐字节导入的第二轮审计为基线，原位修正全部 CURRENT 研究入口与 C-168 叙述；`PROOF_VERSION_CLOSURE.json` 升 v2，verifier 新增 registry/RUN/source/row/matrix 身份、唯一行与完整 claim 集检查；6 条历史依赖例外绑定精确 run 与哈希；新 replay 必须 register→mark→freeze。聚焦回归 9/9 PASS；未新增数学 claim，ERCF-3 保持 `GATED`，未落账轴与 triage 队列继续开放。\n",
    )

    frontier = (root / ".codex/research/hott/FRONTIER.md").read_text(encoding="utf-8")
    frontier = replace_line(frontier, "# HoTT 研究前沿", "# HoTT 研究前沿（S125 接管修复后）", starts=True)
    frontier = replace_line(
        frontier,
        "S092 只更新 Git 可恢复性",
        "S125 接管修复只改变当前研究资格与证明证据关系，不新增数学 claim：C-184–C-187 仍有效；ERCF-3 仍 `GATED`；T3 剩余义务不变。",
        starts=True,
    )
    frontier = replace_line(
        frontier,
        "本轮 S090 不新增数学结论",
        "当前首要动作从纠正后的 C11 v2 全候选面选择一个具体、可反驳工作包；门 A/门 B 是暂选路线，时间/运动、量词/完成顺序、B 方向独立行、开放 triage consumer 均可竞争。不得消费 S107–S109 的历史关闭结论。",
        starts=True,
    )
    frontier = replace_line(
        frontier,
        "| 已闭合工作包 56 |",
        "| 已完成历史工作包 56 | triage 两批与自主候选 #1（S107） | `TRIAGE_PAUSED_COST_BENEFIT_QUEUE_OPEN / DEGENERATION_TEST_FAILED_KNOWN_PACKAGE` | 40 个已读样本的分类与候选 #1 退化结论保留；43 条队列开放，至少两条为真实消费者；不作精度极限或不存在性结论 |",
        starts=True,
    )
    frontier = replace_line(
        frontier,
        "| 已闭合工作包 57 |",
        "| 已完成历史工作包 57 | S108 `UnlabeledTwoElement` 六观察量检查 | `PAPER_ONLY_ARGUMENT_GAP / RESEARCH_OPEN` | 具体样本保留；不敏感并不自动构造 recursor 的函数、集合余域与同余证明，不能宣称形状为空集 |",
        starts=True,
    )
    frontier = replace_line(
        frontier,
        "| 已闭合工作包 58 |",
        "| 已完成历史工作包 58 | S109 身份/表达样本与门 A/门 B 提议 | `BOUNDED_CHECKS / PROVISIONAL_ROUTES_NON_EXHAUSTIVE` | 三种身份位置与三个表达候选只是样本；两条路线不排除其它轴或新构造 |",
        starts=True,
    )
    frontier = replace_line(
        frontier,
        "| 第一工作包 |",
        "| 当前第一工作包 | 从未落账轴、开放 triage consumer、门 A/门 B 或其它新构造中选择一个具体候选 | `READY_FOR_BOUNDED_SELECTION` | 固定理论版本、同一任务、输入/承诺、反解释与停止条件；有明确 consumer 才启动 T3 表示性/反射；不得以旧“只剩两门”过滤候选 |",
        starts=True,
    )

    lessons = (root / ".codex/research/hott/LESSONS.md").read_text(encoding="utf-8")
    lesson_updates = {
        "81.": "81. 理论经济账本应先于具体候选，帮助显式写出收入、悬置/加入因子、补偿与复活条件；支付装置的可用/昂贵/不存在只是描述坐标，不是候选准入或搜索穷尽 Gate。现有包的归类一致性不能证明账本完备。",
        "82.": "82. 商/截断消去器把同余或目标层级义务写进类型，能拒绝一类直接资格越级；但真实截断消费者确实存在。后续必须分别检查消费者真实性、条件是否合法、是否把弱资格提升为更强交付，不能把 E6 预设成只会出现在文档措辞里。",
        "83.": "83. 粗域接口检索可先用词汇 triage 建立有界队列，再人工实读；两批低精度样本只支持收益/成本暂停，不能证明剩余命中都是假阳性。队列保持可复算和开放，真实消费者不自动等于 E6。",
        "86.": "86. 词汇级扫描的两批 40 条样本说明命名造成严重噪音，继续调词表的边际收益低；它不构成“精度极限”定理。未读队列中至少两条是真实截断消费者，因此停止必须写成成本决定并保留重开与逐条语义检查。",
        "87.": "87. 对一个已经给出 `isSet B`、`f : A → B` 与关系 `R` 的具体 recursor 问题，“对识别不敏感”可以被精确写成所需同余证明；但规格可形式化或口头不敏感不会自动构造这些输入。S108 的空集结论因此撤回，具体 `UnlabeledTwoElement` 样本继续保留。",
        "88.": "88. 门 A（形式化规格）与门 B（同层自我担保）是两条可操作路线，不是穷尽结论。时间/运动结构、量词与完成顺序、B 方向独立行及新规则组合持续有研究资格；停止重复同型枚举不等于证明没有其它候选。",
        "93.": "93. 算术标签层的精确结果必须按对象分开：C-166/C-168 约束 `double`/`odd`，C-167 证明 `codeAtom` 单射，而 C-184/C-185 证明 `codeAtom` 满射。修复后 `codeT'`/`codeF'` 像不含 1 由 C-186/C-187 支持；这说明全 `Nat` 解码规格需定义像外行为，并证明当前缺省分支可达，不强制所有实现采用同一语法结构。",
    }
    for prefix, replacement in lesson_updates.items():
        lessons = replace_line(lessons, prefix, replacement, starts=True)

    resume = (root / ".codex/research/hott/RESUME.md").read_text(encoding="utf-8")
    resume = replace_line(
        resume,
        "2. 严格全文读取",
        "2. 严格全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md` → `从抽象到悖论——HoTT研究的核心问题意识与思想展开.md`；当前为 generation-4/36 KC，索引/manifest/旧 receipt 不能替代。",
        starts=True,
    )
    resume = replace_once(
        resume,
        "## 当前停止点\n",
        "## 当前停止点\n"
        "\nS125：已接管被审计 AI 的工作线并闭合第二轮整改。CURRENT owners 不再交付 triage 精度关闭、S108 空集、S109 两轴/两门穷尽或 `codeAtom` 非满射；proof registry/verifier 使用 v2 身份合同，历史依赖例外限于精确 run，新 replay 必须显式登记。聚焦回归 9/9 PASS。下一数学工作从开放候选面选择具体轴/consumer；ERCF-3 仍 `GATED`，无新数学 claim。\n",
    )
    resume = replace_line(
        resume,
        "S114：",
        "S114（历史结果，经 F1/S125 更正）：C-166–C-168 的内核运行有效，但 C-168 只谈 `double` 下 1 无原像；`codeAtom` 满射由 C-184/C-185 证明。修复后 `codeT'`/`codeF'` 像不含 1 由 C-186/C-187 证明。不得再用 S114 的旧中文叙述推导全解码器形态。",
        starts=True,
    )
    resume = replace_line(
        resume,
        "S109：",
        "S109（历史纸笔检查，经 F3/F4/S125 降级）：三种身份使用位置与三个表达候选是有界样本；门 A/门 B 只作暂选路线。它们不关闭身份轴、表达轴或其它搜索形状；C11 v2 未落账轴保持资格。",
        starts=True,
    )
    resume = replace_line(
        resume,
        "S108：",
        "S108（历史纸笔检查，经 F3/S125 降级）：`UnlabeledTwoElement` 的六个观察量保留；从“不敏感”到完整 recursor 输入的构造有缺口，`INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION` 不再是当前判词，该形状开放。",
        starts=True,
    )
    resume = replace_line(
        resume,
        "S107：",
        "S107（历史样本，经 F5/S125 降级）：两批 40 条分类与候选 #1 退化结论保留；词汇 triage 因收益/成本暂停，43 条队列开放，至少两条是真实消费者。不得再写“精度极限已关闭”。",
        starts=True,
    )

    # STATE current records.
    triage = state["records"]["A-TRIAGE-AND-OBLIGATION-ROUND1-001"]
    triage["classification"] = "TRIAGE_PAUSED_COST_BENEFIT_QUEUE_OPEN"
    triage["scope"] = (
        "S107 historical round: two lexical-triage batches (40 inspected hits) were all non-candidates, and autonomous "
        "candidate #1 reduced to C-142-C-148. Current disposition after F5/R2-1: lexical triage is paused for cost-benefit "
        "reasons; the 43-item queue remains open and contains at least two real truncation consumers. A real consumer, a "
        "legally conditioned consumer and a qualification overreach are distinct. No E6 and no new mathematical claim."
    )
    triage["revalidation"] = f"Current scope corrected in place by {SESSION_ID}; historical source and hashes unchanged."

    round2 = state["records"]["A-AUTONOMOUS-ROUND2-001"]
    round2["classification"] = "PAPER_ONLY_ARGUMENT_GAP_RESEARCH_OPEN"
    round2["scope"] = (
        "S108 bounded paper inspection of six observables on the owned UnlabeledTwoElement family. The inspected "
        "proposition-valued observables and the fact that uniform choice is not identification-insensitive remain useful "
        "samples. The step from an informally insensitive/formalisable specification to constructed recursor inputs "
        "(isSet B, f and congruence proof) was not established. INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION is withdrawn "
        "as a current closure verdict; the shape remains research-eligible. No new mathematical claim."
    )
    round2["revalidation"] = f"Current scope corrected in place by {SESSION_ID} after F3/R2-1."

    round3 = state["records"]["A-AUTONOMOUS-ROUND3-001"]
    round3["classification"] = "BOUNDED_AXIS_CHECKS_NON_EXHAUSTIVE_PROVISIONAL_ROUTES"
    round3["scope"] = (
        "S109 bounded paper checks of three uses of an erased distinction and three expressibility candidates. These "
        "examples remain historical observations. They do not close the identity axis, expressibility axis or the whole "
        "search space. Door A and door B are provisional routes, not an exhaustive classification; C11 v2's unledgered "
        "axes and other new constructions remain eligible. No new mathematical claim."
    )
    round3["revalidation"] = f"Current scope corrected in place by {SESSION_ID} after F3/F4/R2-1."

    arith = state["records"]["A-ERCF3-T3-ARITH-TAGS-001"]
    arith["scope"] = (
        "MP-ERCF3-T3-ARITH-TAGS-001 (C-166-C-168): C-166 double/odd arithmetic and disjointness; C-167 codeAtom "
        "injectivity; C-168 only states that double has no preimage of 1. codeAtom is surjective (C-184/C-185). The "
        "repaired coders codeT'/codeF' miss 1 (C-186/C-187), so a total Nat-domain decoding specification must define "
        "out-of-image behaviour; the current default branches are reachable at 1. No claim about every decoder's source "
        "syntax. ERCF-3 remains gated."
    )
    append_revalidation(arith, f"CURRENT scope corrected by {SESSION_ID}; formal C-166-C-168 and receipts unchanged.")

    coding_image = state["records"]["A-ERCF3-T3-CODING-IMAGE-001"]
    coding_image["scope"] = (
        "C-186 codeT' misses 1 and C-187 codeF' misses 1. Consequently a total Nat-domain decoder specification must "
        "define behaviour outside the image; the current dec/decF default branches are reachable at input 1. This does "
        "not quantify every decoder implementation or prescribe a particular source-code construct."
    )
    append_revalidation(coding_image, f"Natural-language scope tightened by {SESSION_ID}; proof and run unchanged.")

    old_absorption = state["records"]["A-INDEPENDENT-AUDIT-ABSORPTION-001"]
    old_absorption["lifecycle_status"] = "HISTORICAL"
    old_absorption["superseded_by"] = RESULT_ID
    old_absorption["scope"] = (
        "Historical first-round absorption. Its C-184-C-187 proof results, import preservation and three file-integrity "
        "mutation checks remain valid. The former claim that all seven findings and F2 were fully closed was disproved by "
        "the second audit and is superseded by A-INDEPENDENT-AUDIT-ROUND2-REPAIR-001."
    )
    old_absorption["resolution"] = {
        "reason": "Second audit found incomplete current-truth propagation, proof/run/index identity gaps, proof-scoped "
        "dependency exceptions and replay-indexing false success; S125 repairs them.",
        "evidence": [REPORT, IMPORTED_AUDIT],
    }

    proof_closure = state["records"]["A-PROOF-VERSION-CLOSURE-001"]
    proof_closure["classification"] = "17_FROZEN_PLUS_11_LATER_V2_EVIDENCE_RELATIONS"
    proof_closure["scope"] = (
        "Git recoverability of the original 17-package snapshot plus v2 evidence-integrity and relationship checks for "
        "11 later packages and registered replay runs. Checks registry/RUN/source/row/matrix identities, complete claim "
        "sets, unique rows, command/source/tool linkage, exact historical-run dependency exceptions and replay "
        "registration. Does not re-run or expand mathematics."
    )
    for rel in (MARK, FREEZE, TESTS, PROOF_CONTRACT, REPORT):
        add_once(proof_closure["full_sources"], rel)

    proof_gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    proof_gate["scope"] = (
        "Require exact mathematical statement, proof source, kernel run and claim/proof index before delivery. The v1.1 "
        "project contract additionally requires v2 proof/run/source/row/matrix identity closure, exact-run dependency "
        "exceptions and an explicit replay relation. Existing 17-package version closure remains; later package claims "
        "retain their recorded mathematical scope. Fresh-model behaviour remains NOT_RUN."
    )
    for rel in (TESTS, REPORT, IMPORTED_AUDIT, IMPORT_MANIFEST):
        add_once(proof_gate["full_sources"], rel)

    report_record = state["records"]["A-AUDIT-REPORT-TONGGUAN-001"]
    report_record["scope"] = (
        "Current technical audit report for the panoramic workline, revised after two independent audits. Historical "
        "S107-S109 judgments are labelled bounded/superseded; door A/B are provisional non-exhaustive routes; C-168 and "
        "the v2 proof evidence/replay contract are stated precisely. It introduces no mathematical claim."
    )

    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [
            SESSION_ID,
            "A-INDEPENDENT-AUDIT-ABSORPTION-001",
            "A-AUTONOMOUS-ROUND2-001",
            "A-AUTONOMOUS-ROUND3-001",
            "A-TRIAGE-AND-OBLIGATION-ROUND1-001",
            "A-PROOF-VERSION-CLOSURE-001",
        ],
        "full_sources": [
            REPORT,
            IMPORTED_AUDIT,
            IMPORT_MANIFEST,
            REGISTRY,
            VERIFIER,
            MARK,
            FREEZE,
            TESTS,
            PROOF_CONTRACT,
            TECH_REPORT,
            RESULT_REL,
        ],
        "source_hashes": {
            REPORT: R.sha((root / REPORT).read_bytes()),
            IMPORTED_AUDIT: R.sha((root / IMPORTED_AUDIT).read_bytes()),
            IMPORT_MANIFEST: R.sha((root / IMPORT_MANIFEST).read_bytes()),
            REGISTRY: R.sha((root / REGISTRY).read_bytes()),
            VERIFIER: R.sha((root / VERIFIER).read_bytes()),
            MARK: R.sha((root / MARK).read_bytes()),
            FREEZE: R.sha((root / FREEZE).read_bytes()),
            TESTS: R.sha((root / TESTS).read_bytes()),
            PROOF_CONTRACT: R.sha((root / PROOF_CONTRACT).read_bytes()),
        },
        "scope": (
            "Takeover repair for second-audit findings R2-1 through R2-5: converge all current research owners; correct "
            "the C-168 narrative; validate proof/run/source/claim identities and exact row sets; bind historical gaps to "
            "exact runs; require replay registration before mark/freeze. Nine focused regressions pass. No new math claim."
        ),
    }

    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260913-direction-107"
    direction_record["scope"] = (
        "Portfolio after S125 takeover repair: C11 v2 coordinates are non-gating; triage queue and unledgered axes are "
        "open; door A/B are provisional routes; T3 representability/reflection requires a concrete consumer."
    )
    direction_record["semantic_status"] = STATUS

    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record["projection_generation"] = "20260913-outcome-107"
    panorama_record["scope"] = (
        "Panorama after S125: historical S107-S109 conclusions are bounded/superseded, C-168 is precise, and v2 proof "
        "evidence relationship checks are verified with scope."
    )
    panorama_record["semantic_status"] = STATUS

    # Re-pin every existing record that explicitly hashes a changed non-MUTABLE asset.
    changed_paths = (
        REPORT,
        IMPORTED_AUDIT,
        IMPORT_MANIFEST,
        OLD_ABSORPTION,
        TECH_REPORT,
        REGISTRY,
        VERIFIER,
        MARK,
        FREEZE,
        TESTS,
        PROOF_CONTRACT,
        "HoTT/formal/README.md",
        "HoTT/formal/ercf3-t3/README.md",
        "HoTT/verification/runs/README.md",
    )
    for record_id, record in state["records"].items():
        hashes = record.get("source_hashes")
        if not isinstance(hashes, dict):
            continue
        touched = []
        for rel in changed_paths:
            if rel in hashes:
                hashes[rel] = R.sha((root / rel).read_bytes())
                touched.append(rel)
        if touched:
            append_revalidation(
                record,
                f"{SESSION_ID} re-pinned changed project evidence: {', '.join(touched)}.",
            )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户目标：接手被第二轮审计的 AI 工作线；以 `{IMPORTED_AUDIT}` 为整改基线。
- 接管基线：`0dd4596f38343562334e499bca6eed1ab065066b`；接管前 tracked tree clean，两个既有未跟踪 dev-notes 原样保留；未发现仍操作该根的进程。
- R2-1/R2-2：CURRENT 方向、全景、STATE、MEMORY、FRONTIER、LESSONS、RESUME 与 formal/run 入口原位收敛；历史 session/run/matrix rows 不改写。
- R2-3：proof closure v2 交叉核验 registry/RUN/source/row/matrix、claim 完整集合、唯一 ID 与 command/source/tool。
- R2-4：六条历史依赖例外绑定精确 run 与哈希；同 proof 新 run 不继承。
- R2-5：replay 先登记关系再 mark/freeze；primary 矩阵行不覆盖。
- 验证：`python3 -B -m unittest scripts.audit.test_proof_evidence_links` = 9/9 PASS；canonical verifier 在 checkpoint 后复跑。
- 数学边界：无新 claim；C-184–C-187 不重证、不扩大；ERCF-3 保持 `GATED`。
- Git：本轮不 push、不打 tag；是否本地提交由接管收尾的精确 Git 状态决定。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "takeover_baseline": "0dd4596f38343562334e499bca6eed1ab065066b",
            "imported_second_audit": {
                "path": IMPORTED_AUDIT,
                "sha256": "5b133815ab4ebd7f9e59ed0880f76d6f6e508f0482c7db545f52607d729e0ecf",
            },
            "focused_regression": {
                "command": "python3 -B -m unittest scripts.audit.test_proof_evidence_links",
                "tests": 9,
                "failures": 0,
                "errors": 0,
                "status": "PASS",
            },
            "proof_closure_pre_checkpoint": {
                "status": "PASS_WITH_SCOPE",
                "later_packages": 11,
                "later_claims": 39,
                "source_manifest_rows": 85,
                "unique_source_files": 21,
                "index_rows": 50,
                "exact_historical_gaps": 6,
                "registered_replays": 0,
            },
            "new_math_claims": [],
            "math_status_change": "NONE",
            "push": "NOT_AUTHORIZED",
            "tag": "NOT_CREATED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 125
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ROUND2_AUDIT_REPAIR_TAKEOVER",
            "status": STATUS,
            "next_minimal_verification": (
                "Select one concrete, falsifiable research package from the full corrected candidate surface: an "
                "unledgered C11 v2 axis (time/motion structure, quantifier/completion order, independent B-direction), "
                "an open triage consumer, provisional door A/B, or a genuinely new construction. Bind the theory version, "
                "same task, input/claim, counterinterpretation and stop condition before proof work. T3 representability "
                "and reflection remain gated on a concrete consumer; ERCF-3 stays GATED."
            ),
        }
    )
    state["projection"]["status"] = STATUS
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            RESULT_REL,
            REPORT,
            IMPORTED_AUDIT,
            IMPORT_MANIFEST,
        ],
        "source_hashes": {},
        "scope": "Second-audit remediation and takeover of the audited AI workline; no new mathematics.",
    }

    essay = projection_edit.load(root, R.ESSAY)
    texts: dict[str, str] = {
        rel: (root / rel).read_text(encoding="utf-8") for rel in R.MUTABLE
    }
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[".codex/research/hott/FRONTIER.md"] = frontier
    texts[".codex/research/hott/LESSONS.md"] = lessons
    texts[".codex/research/hott/RESUME.md"] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "The user explicitly asked this agent to take over the audited AI's work and identified the second-audit "
            "report as the takeover baseline. Apply R2-1 through R2-5 inside the top-level HoTT repository, preserve "
            "historical proof/session/transaction evidence, run focused and canonical checks, and do not push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes())
                if (root / rel).exists()
                else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 125,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
