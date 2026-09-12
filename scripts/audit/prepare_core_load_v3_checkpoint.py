#!/usr/bin/env python3
"""Prepare the revision-13 STATE-v2/core-load-v3 checkpoint payload.

This adapter does not mutate governed state.  It applies explicit, audited
semantic decisions to in-memory copies and writes one payload for the canonical
runtime's dry-run/apply transaction.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-013-CORE-LOAD-V3"
EVIDENCE = "audit/核心认知generation-3与加载治理v3实施证据-20260912.md"
TRANSITION = "audit/core-cognition-generation-3-transition-20260912.json"

SPEC = importlib.util.spec_from_file_location("cognition_runtime_v3", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{label}:{count}")
    return text.replace(old, new, 1)


def direction_text(root: Path) -> str:
    text = (root / "方向追踪.md").read_text(encoding="utf-8")
    text = replace_once(text, "状态：`EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW`",
                        "状态：`CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW`", "direction-status")
    text = replace_once(text, "source_state_revision: 12", "source_state_revision: 13", "direction-revision")
    text = replace_once(text, "projection_generation: 20260912-direction-002",
                        "projection_generation: 20260912-direction-003", "direction-generation")
    text = replace_once(text, "semantic_status: EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW",
                        "semantic_status: CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW", "direction-semantic")
    text = replace_once(text,
        "STATE.json    → 机器状态、开放记录自动发现、依赖闭包和 source hash",
        "STATE.json    → 机器状态、lifecycle/evidence 分离、stable-ID 任务发现和 source hash",
        "direction-state-role")
    text = replace_once(text,
        "3. 将当前方向与 `STATE.json` 的记录身份、`MEMORY.md` current queue 和直接证据对照；",
        "3. 将当前方向与 STATE 的 lifecycle/evidence、`MEMORY.md` current queue 对照；需要直接证据时先 query record，再显式 task hydrate；",
        "direction-start-rule")
    replacements = {
        "`TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `IDENTITY_UNIVALENCE_TRANSPORT`": "`TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `HOTT_OBJECT`",
        "`TIME_AND_TEMPORALITY`, `GUARDED_DIRECTED_VARIANTS`, `PARADOX_DISCOVERY`": "`TIME_AND_TEMPORALITY`, `HOTT_OBJECT`, `PARADOX_DISCOVERY`",
        "`GUARDED_DIRECTED_VARIANTS`, `IDENTITY_UNIVALENCE_TRANSPORT`, `EVIDENCE_DISCIPLINE`": "`SELF_REFERENCE`, `HOTT_OBJECT`, `EVIDENCE_DISCIPLINE`",
        "`THEORY_SCHEMA`, `GUARDED_DIRECTED_VARIANTS`, `EVIDENCE_DISCIPLINE`": "`THEORY_SCHEMA`, `HOTT_OBJECT`, `EVIDENCE_DISCIPLINE`",
        "`IDENTITY_UNIVALENCE_TRANSPORT`, `TIME_AND_TEMPORALITY`": "`HOTT_OBJECT`, `TIME_AND_TEMPORALITY`",
        "`IDENTITY_UNIVALENCE_TRANSPORT`, `COMPUTATIONAL_LEGITIMACY`": "`HOTT_OBJECT`, `COMPUTATIONAL_LEGITIMACY`",
        "`TRUNCATION_QUOTIENT_REFLECTION`, `GUARDED_DIRECTED_VARIANTS`": "`SELF_REFERENCE`, `HOTT_OBJECT`",
        "`TRUNCATION_QUOTIENT_REFLECTION`, `EVIDENCE_DISCIPLINE`": "`SELF_REFERENCE`, `EVIDENCE_DISCIPLINE`",
        "`GUARDED_DIRECTED_VARIANTS`, `TRUNCATION_QUOTIENT_REFLECTION`": "`SELF_REFERENCE`, `TIME_AND_TEMPORALITY`",
        "`GUARDED_DIRECTED_VARIANTS`, `COMPUTATIONAL_LEGITIMACY`": "`SELF_REFERENCE`, `COMPUTATIONAL_LEGITIMACY`",
        "`EVIDENCE_DISCIPLINE`, `HANDOFF_GOVERNANCE`": "`EVIDENCE_DISCIPLINE`；`CORE_UNRELATED/GOVERNANCE_RULING`",
        "`HANDOFF_GOVERNANCE`, `SESSION_CONTINUITY`, `EVIDENCE_DISCIPLINE`": "`CORE_UNRELATED/GOVERNANCE_RULING`",
        "`HANDOFF_GOVERNANCE`, `SESSION_CONTINUITY`": "`CORE_UNRELATED/GOVERNANCE_RULING`",
        "`HANDOFF_GOVERNANCE`, `EVIDENCE_DISCIPLINE`": "`CORE_UNRELATED/GOVERNANCE_RULING`",
    }
    for old, new in replacements.items():
        if old not in text:
            raise ValueError(f"DIRECTION_THEME_REPLACEMENT_MISSING:{old}")
        text = text.replace(old, new)
    text = replace_once(text,
        "当前方向仍保留主题级 core 关联；`core_refs` 的精确 KC 交叉审视由 register locator 和后续人工句级裁决继续承载，不把规则匹配写成用户语义结论。",
        "当前方向只使用 generation-3 manifest 中实际存在的主题；纯治理方向显式标 `CORE_UNRELATED/GOVERNANCE_RULING`。精确 KC 交叉审视仍由当前原文与人工裁决承担，不把规则匹配写成用户语义结论。",
        "direction-core-contract")
    text = replace_once(text,
        "- 用户提出新原文、修正或采纳/撤回：先保存原文输入，再更新 `核心认知` generation 和 `rulings`；",
        "- 用户提出新的悖论/元数学原文或明确修正：先保存 primary 输入，人工更新 curation，再由 manager 生成新 core generation/transition，并同步 `rulings`；",
        "direction-core-update")
    return text


def panorama_text(root: Path) -> str:
    text = (root / "全景视野.md").read_text(encoding="utf-8")
    text = replace_once(text, "状态：`EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW`",
                        "状态：`CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW`", "panorama-status")
    text = replace_once(text, "source_state_revision: 12", "source_state_revision: 13", "panorama-revision")
    text = replace_once(text, "projection_generation: 20260912-outcome-002",
                        "projection_generation: 20260912-outcome-003", "panorama-generation")
    text = replace_once(text, "semantic_status: EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW",
                        "semantic_status: CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW", "panorama-semantic")
    old = "| `OUT-TOP-CORE-FOUNDATION` | 三平台用户提问及本轮治理补充的 chronological core：127 条消息、913 个 `KC-*`、原文/来源 hash/主题/生命周期 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY` | 顶层交接工程 | `VERIFIED_WITH_SCOPE` | core 的机械身份、编号、payload hash、来源文件关系可核验；generation-1 前缀保持不变 | 不证明用户主张为数学真理，不证明模型理解 | `核心认知.md`；`核心认知.manifest.json`；`audit/core-cognition-generation-transition-20260912.json`；`scripts/audit/verify_core_cognition.py` |"
    new = "| `OUT-TOP-CORE-FOUNDATION` | generation-3：三份 primary 共 88 条消息逐项处置，23 条形成 27 个 `USER_OWNED_DIRECT` 原文语义单元；旧 generation-2/913 KC 可恢复 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-U-A-REALITY-RELATIVE`、`DIR-U-B-EFFECTIVE-DELIVERY` | 顶层交接工程 | `VERIFIED_WITH_SCOPE` | source/curation/selector/payload hash、连续编号及 913/913 transition remainder=0 可核验 | 不证明用户主张为数学真理，不证明模型理解；人工 curation 可在新证据下产生下一代 | `核心认知.md`；`核心认知.manifest.json`；`scripts/audit/core-cognition-curation-v3.json`；`audit/core-cognition-generation-3-transition-20260912.json`；`scripts/audit/verify_core_cognition.py` |"
    text = replace_once(text, old, new, "panorama-core-row")
    old = "| `OUT-TOP-THREE-WAY-SKELETON` | 本轮三件套文档、LOAD_SET/runtime/validator 接入、generation-2、merge receipt、source register 和 fresh receipt | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-E-WEB-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION` | 当前顶层本轮升级 | `VERIFIED_WITH_SCOPE` | 三件套固定入口、22,226 行来源登记、25/24 文件处置、fresh load/负向收据和 revision 11 checkpoint 已验证 | 仍不证明 2,396 条 claim 的人工语义、数学认证或模型理解 | `方向追踪.md`；`全景视野.md`；`audit/cross-source-reconciliation.json`；`audit/fresh-three-way-verification-20260912.json`；`.codex/` |"
    new = "| `OUT-TOP-THREE-WAY-SKELETON` | generation-3 + LOAD_SET/runtime v3 + STATE v2：三件套永久全文、governance/research profile、stable task hydration、历史 Session 冷存 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-E-WEB-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION` | 当前顶层治理升级 | `VERIFIED_WITH_SCOPE` | core 7 tests、runtime 27 tests、reader 17 tests、three-way 3 tests；默认 governance/research 均不加载冷资产；revision 13 checkpoint | fresh 模型行为、2,396 条 claim 语义、数学认证仍未完成 | `audit/核心认知generation-3与加载治理v3实施证据-20260912.md`；`audit/fresh-three-way-verification-20260912.json`；`.codex/` |"
    text = replace_once(text, old, new, "panorama-governance-row")
    text = replace_once(text,
        "- 顶层三件套已接入 generation-2、逐文件 merge receipt 和全量 source register；fresh/压缩行为及 2,396 条 claim 的直接句级语义裁决仍不认证，模型上下文仍保持 `NOT_CERTIFIED_BY_TOOL`。",
        "- 顶层三件套已接入 generation-3、STATE/load v3、逐文件 merge receipt 和全量 source register；fresh Python 输入保真与负向行为可核验，fresh 模型/压缩后实际使用和 2,396 条 claim 的句级语义仍未认证。",
        "panorama-current-boundary")
    text = replace_once(text,
        "- 新用户原文/用户工作意识：更新 core generation（先存 source input）和 `rulings`；",
        "- 新用户悖论/元数学原文：先存 primary input、人工更新 curation，再由 manager 生成新 core generation/transition，并同步 `rulings`；一般治理要求只进 ruling/Feature；",
        "panorama-update-rule")
    return text


def memory_text() -> str:
    return """# 当前工作记忆

> Owner：顶层 `AGENTS.md`、Feature/rulings 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态/队列，不复制三件套或历史长文。

## 当前执行队列（2026-09-12）

1. 本轮用户授权的 core 重建与本地治理 v3 已完成代码/文档实现，正由 `S-GOV-20260912-013-CORE-LOAD-V3` revision 13 checkpoint 封存；本轮不启动数学研究。
2. 交付后若用户要求继续验证治理，下一独立结果是固定 model/host/version 的 fresh Session/真实压缩后行为验收；没有该运行时只能保持 `FRESH_MODEL_BEHAVIOR=NOT_RUN`，不能用 Python EOF 代替。
3. 历史交接主线仍开放：2,396 条 understanding claim 的直接句级裁决、aistudio coverage、历史数学主张、关键 response→artifact/code/Git 因果。它们只在用户/current task 选中 stable ID 后显式 hydrate，不自动复活全部历史 Session。

## 当前已验证状态

- `核心认知.md` 当前为 `core-cognition-generation-3`：三份 primary 共 88 条消息逐项人工处置，23 条形成 27 个按 UTC 排序的直接用户原文语义单元；core SHA-256 `8aa005505c68d20eb11c48b946fa61e68b03013d56926ca2b9c928d06c5a7dfb`。
- `governance-v2.1.0` 保存 generation-2/913 KC；generation-3 transition 覆盖 913/913、remainder=0。退出当前 core 的 AI relay/supplemental/治理/重复内容仍在 source/Git，不是删除。
- `LOAD_SET v3` 固定 core→direction→panorama 全文，并区分 governance/research/query-first/task-expand/archive。STATE v2 将 lifecycle 与 evidence status 分开，历史治理 Session 不因 review_required 自动加载。
- checkpoint 前实测 governance=15 documents/159,882 bytes，research=20/228,396 bytes；最终 revision 13 精确值见 `audit/fresh-three-way-verification-20260912.json`。
- 已执行 core 7/7、runtime 27/27、single-core reader 17/17、three-way 3/3；旧命令入口错误、旧 2115 行 oracle 和 transition exact-identity 误判均保留在本 Session RUNS。
- `/Volumes/D/ALL-Markdown` 与 WebGPT workspace 均未修改；共享治理主库和全局 Codex runtime 有其它 dirty 工作，本轮不触碰、不发布共享版本。

## 当前证据上限

- 三件套字节/EOF、curation/transition、profile/task 与 checkpoint 可以机械验证；模型实际理解始终 `NOT_CERTIFIED_BY_TOOL`。
- 本轮没有新增 HoTT 推导、Lean/Agda 内核证明或现实物理认证。Z 铁律、量子化时空和 HoTT 自指仍按用户研究立场/开放命题使用。
- source register 22,226 行与理解章节 25/24 文件处置保持原范围；core 重建不改变历史 AI 审计分母，也不自动完成 2,396 条语义裁决。

## 恢复入口

按根 AGENTS 全文加载三件套；治理任务用 governance profile，数学研究用 research profile；选定记录先 `query --record ID`，再 `plan --profile research --task ID`。当前实现与 C01–C10 见 `audit/核心认知generation-3与加载治理v3实施证据-20260912.md`。
"""


def frontier_text() -> str:
    return """# HoTT 研究前沿（当前治理 v3 交接阶段）

本文件是当前注意力槽，不是数学结论数据库。三件套已成为完整常驻研究视野；底层历史证据只按 stable ID 水合。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 收敛 | generation-3 core + LOAD_SET/runtime v3 + STATE v2 checkpoint | completing | 完成 revision 13、fresh Python receipt、全套回归与 Git/tag；fresh model behavior 仍独立 NOT_RUN |
| 探索 | 2,396 条 understanding claim 与关键 response→artifact/code/Git 因果 | open_issue | 用户选择后按 record/task hydrate，逐句回源，不把 register 路由当语义结论 |
| 深层 | HoTT 时间/ASK/现实相对候选 | historical-review | 用户明确恢复数学研究后，先全文加载 research profile，再选择一项真实构造/反例 |

当前不宣称任何历史候选为 `HoTT ⊢ ⊥`，不宣称完成现实桥梁、Lean/Agda 内核认证、fresh 模型行为或 aistudio-docs 全覆盖。`new_math_research_started=false`。
"""


def lessons_text(root: Path) -> str:
    text = (root / ".codex/research/hott/LESSONS.md").read_text(encoding="utf-8").rstrip()
    text = replace_once(text,
        "9. core generation-2 只能通过新增用户原文输入和生成器重建；generation-1 前缀 identity check 是迁移证据，不能手工编辑旧 KC。",
        "9. core 当前代必须由人工 curation + canonical manager 生成；任何用户新悖论/元数学原文进入新 generation，旧代由 tag/transition 保留，不能手工编辑生成物。",
        "lessons-core-generation")
    return text + """
11. `role=user` 只证明消息由用户通道发送，不证明其中每段都是用户原创；Response annotations、转发信件、复合 briefing 必须逐项区分，不能把 AI 文字注入 core。
12. “core 必须全文加载”保护的是用户定义的当前逻辑文档，不保护旧生成器的错误边界；重建可缩小当前输入，但必须精确原文、逐消息 disposition、完整迁移和可回滚历史。
13. `evidence_status=REVIEW_REQUIRED` 不等于 `lifecycle_status=ACTIVE_WORK`。把二者混成一个 status 会让历史 Session/逐-KC表永久复活并形成自激压缩循环。
14. 失败要按责任点记录：错误 unittest 入口不是测试失败；旧 2115 行下限是坏 oracle；旧 payload 含 `---` 使“完全相等”预期错误。修命令/规格后复跑，不能改数据求绿。
15. 一个 compatibility runtime 副本若可直接路由到 canonical 实现，就不应长期维护第二份独立代码；路径兼容和真值唯一可以同时成立。
"""


def resume_text() -> str:
    return """# 接续指针

## 每个新 Session/压缩后的固定恢复

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md` 和本地治理 Skill/PROTOCOL/LOAD_SET/STATE。
2. 严格全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`；当前 core 是 generation-3/27 KC，manifest/旧 receipt 不能替代。
3. 纯治理用 `cognition_runtime.py plan --profile governance`；数学研究用 `--profile research`。
4. 先 `query --record <ID>` 判断 lifecycle/evidence，再用 `plan --profile research --task <ID>` 水合本轮证据；不要自动读取所有 historical/review_required Session。
5. 运行 `scripts/audit/verify_core_cognition.py`、`verify_three_way_cognition.py` 和 `verify_projection_freshness.py`；实现审计再读 validator/runtime 源码。
6. 结束时为当前 generation 全部 KC 写人工回评，并经原子 checkpoint 更新真正变化的 owner。

## 当前停止点

generation-3、六层 LOAD_SET、runtime 3.0、STATE v2、27-KC回评和 revision 13 checkpoint 构成本轮交付。fresh Python receipt 只证明输入/工具行为；fresh 模型行为、数学正确性、aistudio coverage 和 2,396 条 claim 语义仍未由本轮完成。
"""


def core_audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    special = {
        "KC-000001": ("ALIGNED", "本轮把‘找什么/怎么找/凭什么’落实为 core 内容边界、来源处置、加载与验证合同；没有回答新的数学三问。"),
        "KC-000007": ("ALIGNED", "分层加载让 LLM 在每次恢复先获得用户问题意识，再按任务调用既有知识和证据；本轮未执行 HoTT 模式匹配研究。"),
        "KC-000017": ("DEEPENED", "本轮直接按该反训练先验要求重建 27 单元 core，并真实全文加载三件套；AI relay 和训练惯性材料不再反向污染用户原文。"),
        "KC-000021": ("ALIGNED", "生成器、迁移、runtime 和负向测试均真实运行且严格标明只属治理机械证据；没有冒充 Lean/Agda 数学证明。"),
        "KC-000022": ("ALIGNED", "方向/全景继续同时保留现实可完成→理论困难与现实不可完成→理论假装完成两条用户方向；本轮未证明任何实例。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        unit_id = unit["id"]
        relation, assessment = special.get(unit_id, (
            "NOT_TOUCHED",
            "本轮只核定并保全该用户原文的当前 core 身份，没有对其中的 HoTT/悖论/物理或元数学主张作新推导、反例或形式化。"
        ))
        evidence = (f"核心认知.md#{unit_id}; scripts/audit/core-cognition-curation-v3.json; "
                    f"{TRANSITION}; {EVIDENCE}")
        unresolved = "该 KC 的数学真值、HoTT 规则对应与现实桥梁仍按方向/成果/底层证据独立研究。"
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | {evidence} | {unresolved} |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `YES` — 用户明确授权按最初定义重建；generation-3 精确收窄为三份 primary 的 27 个直接用户单元。",
        "- direction_change: `YES` — 保留 24 方向；将已不存在的 generation-2 主题映射替换为当前主题或 `CORE_UNRELATED/GOVERNANCE_RULING`，加载语义改为 lifecycle + explicit hydration。",
        "- panorama_change: `YES` — 更新 core/治理结果为 generation-3、STATE/load v3 和 revision 13；历史数学结果不变。",
        "- update_decision: `core 只因本轮用户原文修正而换代；方向/全景只更新认知路由与实施结果；不写入新数学结论。`",
        "- cross_conflicts: `NONE_AFTER_OWNER_UPDATES` — generation-2 当前措辞已在 owner 原位收敛，旧状态由 tag/Git/transition 保留。",
        "- unresolved: `fresh model behavior、2,396 claim 句级语义、历史数学认证、aistudio coverage。`", "",
        "## 汇总", "",
        "`DEEPENED=1 / ALIGNED=4 / NOT_TOUCHED=22 / CORRECTED=0 / TENSION=0 / DEVIATED=0`。这里的完成是公开逐项回评完成，不是模型隐藏理解或数学证明认证。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return f"""# {SESSION_ID}

## 目的与用户授权

实施用户已采纳的 core/跨压缩治理升级，并服从最新纠偏：可以按最初定义从三份 primary 重建 core，不必继续从 generation-2 怪物中打捞。授权范围为当前顶层 repo 的文档、生成器、runtime、测试、STATE checkpoint、Git commit/tag；不修改外部 repo、不启动数学研究、不 push。

## 实际完成

- `governance-v2.1.0` 封存旧 913-KC/105-document 模式；
- generation-3：88 条逐消息 disposition、23 条纳入、27 个直接用户语义单元、913/913 transition；
- LOAD_SET/runtime 3.0：三件套全文、governance/research profile、query/task hydration、历史 Session 冷存、单一 canonical runtime；
- STATE v2：lifecycle/evidence 分离，五个开放 issue 保持，005–012 等 Session 为 historical；
- 当前方向/全景/MEMORY/FRONTIER/LESSONS/RESUME 同一 checkpoint 原位对齐；
- 当前 27 KC 已逐项公开回评。

## 验证与限制

core tests 7/7、runtime 27/27、reader 17/17、three-way 3/3 及 pre-checkpoint fresh Python profile/negative rehearsal 通过；实际命令与失败见 `RUNS.json`。checkpoint 结果由 `.codex/cognition/checkpoints/{SESSION_ID}/result.json` 持有。

`FRESH_MODEL_BEHAVIOR=NOT_RUN`、`MODEL_CONTEXT=NOT_CERTIFIED_BY_TOOL`、`MATHEMATICS=UNCHANGED_NOT_CERTIFIED`。本 Session 不证明 Z 铁律、量子时空、HoTT 自指或任何 `HoTT ⊢ ⊥`。
"""


def runs_text() -> str:
    value = {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "successful_runs": [
            {"command": "python3 -B scripts/audit/test_core_cognition.py", "result": "7/7 PASS"},
            {"command": "python3 -B scripts/audit/verify_core_cognition.py", "result": "PASS; 88 messages; 27 KC; 913/913 transition"},
            {"command": "python3 -B scripts/audit/test_three_way_cognition.py", "result": "3/3 PASS"},
            {"command": "python3 -B scripts/audit/verify_three_way_cognition.py", "result": "PASS at revision 12 pre-checkpoint"},
            {"command": "python3 -B .codex/skills/hott-paradox-research/checks/test_cognition_runtime.py", "result": "27/27 PASS"},
            {"command": "python3 -B .codex/skills/hott-paradox-research/checks/test_full_closure_loading.py", "result": "17/17 PASS after oracle correction"},
            {"command": "python3 -B scripts/audit/verify_fresh_three_way.py", "result": "PASS_WITH_SCOPE at revision 12 pre-checkpoint"}
        ],
        "preserved_failures_and_corrections": [
            {"failure": "unittest -m received a path beginning with .codex and raised ValueError: Empty module name", "classification": "COMMAND_ENTRY_ERROR_NOT_TEST_FAILURE", "correction": "execute the test files directly; 56/56 and 17/17 old baseline passed"},
            {"failure": "generation transition test expected PRESERVED_EXACT", "classification": "BAD_EXPECTATION", "correction": "old payloads contained message separator ---; verify CURATED_EXACT_SUBRANGE; 913/913 passed"},
            {"failure": "reader test required current core line count > 2115", "classification": "HISTORICAL_SIZE_ORACLE", "correction": "compare growth to current EOF; 17/17 passed"},
            {"failure": "apply_patch rejected Delete+Add for one path in one patch", "classification": "PATCH_TOOL_CONTRACT", "correction": "split into two recoverable patch operations; no user content lost"}
        ],
        "pre_checkpoint_plans": {
            "governance": {"documents": 15, "bytes": 159882, "lines": 1711},
            "research": {"documents": 20, "bytes": 228396, "lines": 2562}
        },
        "fresh_model_behavior": "NOT_RUN_NO_FRESH_MODEL_INVOCATION_AUTHORIZED",
        "mathematics": "NOT_RUN_OR_CHANGED"
    }
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def migrate_state(root: Path) -> dict:
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("schema_version") != "hott-working-state/v1" or state.get("revision") != 12:
        raise ValueError("EXPECTED_STATE_V1_REVISION_12")
    for key, record in state["records"].items():
        if key in state["active"]:
            lifecycle = "ACTIVE_WORK"
        elif record.get("kind") == "session":
            lifecycle = "HISTORICAL"
        elif record.get("status") in {"closed", "complete"}:
            lifecycle = "CLOSED"
        elif record.get("status") in {"open", "active", "pending", "blocked", "in_progress", "review_required"}:
            lifecycle = "OPEN_ISSUE"
        else:
            lifecycle = "HISTORICAL"
        if record.get("kind") == "session" or record.get("status") in {"closed", "complete"}:
            evidence = "VERIFIED_WITH_SCOPE"
        else:
            evidence = "REVIEW_REQUIRED" if record.get("status") == "review_required" or key in state["review_due"] else "VERIFIED_WITH_SCOPE"
        record["lifecycle_status"] = lifecycle
        record["evidence_status"] = evidence
    state["records"]["A-FRESH-THREE-WAY-001"]["scope"] = "Fresh Python process verifies layered governance/research plans, complete trio bytes, explicit task hydration and fail-closed negatives; no model behavior or mathematics."
    state["records"]["A-FRESH-THREE-WAY-001"]["resolution"]["reason"] = "Fresh Python processes verify exact trio bytes and layered loader behavior; model ingestion/comprehension remains NOT_RUN."
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-003"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = "CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["evidence_status"] = "REVIEW_REQUIRED"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-003"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = "CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["evidence_status"] = "REVIEW_REQUIRED"
    state["records"]["A-CORE-GENERATION-3-001"] = {
        "kind": "core_generation_migration", "path": TRANSITION, "status": "closed",
        "lifecycle_status": "CURRENT", "evidence_status": "VERIFIED_WITH_SCOPE", "depends_on": [],
        "full_sources": ["核心认知.md", "核心认知.manifest.json", "scripts/audit/core-cognition-curation-v3.json", "scripts/audit/verify_core_cognition.py", EVIDENCE],
        "source_hashes": {},
        "scope": "Rebuild current core from exactly three primary extracts with explicit 88-message disposition and total 913-KC migration lineage.",
        "resolution": {"reason": "Canonical builder/verifier produced 27 direct-user units and a 913/913 transition with zero remainder.",
                       "evidence": [TRANSITION, EVIDENCE]}
    }
    state["records"]["A-LOAD-GOVERNANCE-V3-001"] = {
        "kind": "governance_upgrade", "path": EVIDENCE, "status": "closed",
        "lifecycle_status": "CURRENT", "evidence_status": "VERIFIED_WITH_SCOPE", "depends_on": ["A-CORE-GENERATION-3-001"],
        "full_sources": [".codex/cognition/LOAD_SET.json", ".codex/tools/cognition_runtime.py", ".codex/cognition/PROTOCOL.md", ".codex/skills/hott-local-session-governance/SKILL.md", ".codex/skills/hott-paradox-research/SKILL.md", "audit/fresh-three-way-verification-20260912.json"],
        "source_hashes": {},
        "scope": "Layer full-trio/boot/research/query/task/archive cognition and separate lifecycle from evidence status without deleting history.",
        "resolution": {"reason": "Layered runtime and negative tests pass; fresh model behavior remains explicitly NOT_RUN.",
                       "evidence": [EVIDENCE, "audit/fresh-three-way-verification-20260912.json"]}
    }
    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["A-CORE-GENERATION-3-001", "A-LOAD-GOVERNANCE-V3-001"],
        "full_sources": [session_path, audit_path, runs_path, EVIDENCE, TRANSITION, "audit/fresh-three-way-verification-20260912.json", f".codex/cognition/checkpoints/{SESSION_ID}/result.json"],
        "source_hashes": {},
        "mathematical_status": "UNCHANGED_FROM_R039_HISTORICAL_SCOPE",
        "cognition_status": "CORE_GENERATION_3_AND_LAYERED_LOAD_V3_MECHANICALLY_VERIFIED",
        "scope": "Rebuild the user core and implement project-local layered cognition governance; no new mathematics."
    }
    state["schema_version"] = "hott-working-state/v2"
    state["schema_migration"] = {
        "from": "hott-working-state/v1", "to": "hott-working-state/v2",
        "rollback_ref": "governance-v2.1.0", "receipt": EVIDENCE
    }
    state["current_core"] = {
        "generation": "core-cognition-generation-3", "path": "核心认知.md",
        "manifest": "核心认知.manifest.json", "curation": "scripts/audit/core-cognition-curation-v3.json",
        "transition": TRANSITION, "kc_count": 27
    }
    state["load_policy"] = {
        "schema_version": "cognition-load-set/v3", "runtime_version": "3.0.0",
        "full_trio": ["核心认知.md", "方向追踪.md", "全景视野.md"],
        "profiles": ["governance", "research"], "historical_session_auto_load": False,
        "fresh_model_behavior": "NOT_RUN"
    }
    state["revision"] = 13
    state["latest_session"] = SESSION_ID
    state["execution_control"] = {
        "background_work": False, "checkpoint_result": "CHECKPOINT_COMMITTED",
        "last_checkpoint_session": SESSION_ID, "new_math_research_started": False,
        "next_minimal_verification": "fresh model/real compaction behavior if separately authorized; otherwise hydrate one selected open issue",
        "source_policy": "preserve all historical snapshots; do not restore user-removed aistudio-docs",
        "status": "CORE_GENERATION_3_AND_LAYERED_LOAD_V3_MECHANICALLY_VERIFIED"
    }
    state["projection"]["status"] = "CORE_GENERATION_3_LAYERED_LOAD_V3_WITH_SCOPED_MANUAL_REVIEW"
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = migrate_state(root)
    files = {
        "MEMORY.md": memory_text(),
        "方向追踪.md": direction_text(root),
        "全景视野.md": panorama_text(root),
        f"{R.PREFIX}FRONTIER.md": frontier_text(),
        f"{R.PREFIX}LESSONS.md": lessons_text(root),
        f"{R.PREFIX}RESUME.md": resume_text(),
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md": session_text(),
        f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md": core_audit_text(root),
        f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json": runs_text(),
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "User explicitly said to start implementation of the accepted project-local governance/core rebuild; no external repo, push or new mathematics.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": text}
            for rel, text in files.items()
        ]
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 13,
                      "session_id": SESSION_ID, "files": len(files), "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
