#!/usr/bin/env python3
"""Prepare revision 53: record the ERCF-3 prerequisite assessment and route T2.

S053 fixed the ERCF-3 prerequisites (P1-P8), the minimal proxy tasks (T1-T5)
and their stop conditions, and machine-checked the abstract diagonal core
(Lawvere fixed point, no fixed-point-free Bool endomorphism, no exact
self-encoding A -> (A -> Bool), constant-fragment positive control) as a probe.
Verdict: ERCF3_GATED_WITH_MACHINE_CHECKED_DIAGONAL_CORE.  The next work
package is T2: the bounded encoding-route experiment.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-053-ERCF3-PREREQUISITE-AUDIT"
PREV_SESSION = "S-RES-20260912-052-APPLICATION-LAYER-AUDIT"
RESULT_ID = "A-ERCF3-PREREQUISITE-ASSESSMENT-001"
C8 = "理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [
    f"{SESSION_REL}/evidence/agda/DiagonalCore.agda",
    f"{SESSION_REL}/evidence/agda/DiagonalCore.check.stdout.txt",
    f"{SESSION_REL}/evidence/agda/DiagonalCore.check.stderr.txt",
    f"{SESSION_REL}/evidence/agda/AGDA_LIBRARIES",
]
NEW_STATUS = "ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_ercf3_prereq", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:80]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "S053 明确 ERCF-3 的强读法被通用对角核反驳，继续区分‘理论非现实性’与‘理论内部矛盾’。"),
        "KC-000012": ("DEEPENED", "ASK 的预分析在 S053 中具体化为：自证要求必须先通过 P1–P8 前置条件检查。"),
        "KC-000013": ("DEEPENED", "理论工具性的经济收益在 S053 中被形式化为‘编码精确性 vs 有限片段表示’的取舍。"),
        "KC-000021": ("ALIGNED", "S053 的对角核探针在固定 Agda 工具链实际运行，kernel 通过、零 warning。"),
        "KC-000025": ("ALIGNED", "自指型构造慢的疑问在 S053 得到结构性回答：前置条件（尤其 P8）不足时升级会失败。"),
        "KC-000026": ("DEEPENED", "‘HoTT 能否越过自身自指’在 S053 中被拆为强/弱/分层三种读法与它们各自的义务。"),
        "KC-000028": ("DEEPENED", "自反真理验证回环在 S053 中被精确化为 P1–P8 前置条件表与 T1–T5 代理任务。"),
        "KC-000029": ("ALIGNED", "理论经济在 S053 中表现为编码精确性与有限片段表示之间的取舍，而不是自动循环。"),
        "KC-000031": ("ALIGNED", "‘最小理想理论是否被 HoTT 拒绝’在 S053 中保持为需要 P8 natural consumer 的开放问题。"),
        "KC-000035": ("ALIGNED", "HoTT 能否表达本项目理论的问题被 S053 拆为 L0/L1/L2 层级纪律，继续要求显式分层。"),
        "KC-000036": ("DEEPENED", "HoTT 研究哥德尔不完备性的循环风险在 S053 中被判定为通用边界 + 内部化表示代价；ERCF-3 本体保持 gated。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(
            unit["id"],
            ("NOT_TOUCHED", "本轮是 S053 ERCF-3 前置评估与对角核机器核查；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S053/SESSION.md；{C8} | T2/T3/T4 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — S053 完成 ERCF-3 前置评估（P1–P8/T1–T5 + 对角核机器核查）；ERCF-3 本体保持 `GATED`；第一工作包转 T2 编码路线实验；revision 53/generation 037。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-ERCF3-PREREQUISITE-ASSESSMENT`；理解章节 inventory 更新为 33/24（C0–C8）。",
        "- update_decision: `C8 进入 理解章节 与 merge manifest；探针证据进入 session evidence；不新增 claim matrix 行（探针非 claim 包）。`",
        "- cross_conflicts: `NONE_OBSERVED` — C4 §13 的通用边界判定与 T1 的机器核查一致；ERCF-3 的三种读法义务已在 C8 §6 分离。",
        "- unresolved: `T2 编码路线、T3/T4、P8 natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `ERCF3_GATED_WITH_MACHINE_CHECKED_DIAGONAL_CORE`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S052 把第一工作包路由为 ERCF-3 前置评估（N1–N10 未找到 natural consumer 后的决策点）。",
        "- 产出：`理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md`——P1–P8 前置条件表、T1–T5 最小代理任务（含假设与停止条件）、三种读法分析（强/弱/分层）、判定与重开条件。",
        "- 机器核查（T1，探针非 claim 包）：`evidence/agda/DiagonalCore.agda` 在 Agda 2.8.0-3d04bac + Cubical v0.9、`--safe --cubical --guardedness --ignore-interfaces` 下 `CHECK EXIT=0`、零 warning、stderr 0 字节；内容为 Lawvere 不动点、`not` 无不动点、无精确自编码 `A → (A → Bool)`、常值片段精确表示正控制。",
        "- 关键判定：ERCF-3 保持 `GATED`；强读法（带 section 的精确自编码）在编码层被通用对角核反驳；弱读法不自动触发；分层读法是通用 Gödel–Tarski 边界 + 内部化表示代价。升级为项目悖论候选的唯一路径是 P8（natural consumer），N1–N10 未发现。",
        "- 治理联动：理解章节 merge manifest 重建为 33/24（top-level unique 9、nonidentical 18、unresolved 0），`verify_understanding_merge.py` PASS；MEMORY 中的旧 merge 计数（29/14）被原位修正。",
        "- 边界：探针不是 F-011 claim 包；不新增 claim matrix 行；不主张 Lawvere 结果的原创性或 HoTT 特有性。",
        "- 三件套：direction/panorama revision 53/generation 037；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT`",
        "状态：`CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 52", "source_state_revision: 53")
    direction = sub_once(direction, "projection_generation: 20260912-direction-036", "projection_generation: 20260912-direction-037")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT",
        "semantic_status: CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-ONLINE-CAUSALITY` | partiality、guard-erasure、cost、路径证书与在线因果支线的正反结构已完全闭合（商可分裂、单子成立、`≡c` = 代表相等）；经济收益的边界（race/deadline 不可下降）保持；只有自然升级桥梁成立才进入 ERCF-3 |",
        "、`OUT-TOP-ONLINE-CAUSALITY`、`OUT-TOP-ERCF3-PREREQUISITE-ASSESSMENT` | partiality、guard-erasure、cost、路径证书与在线因果支线的正反结构已完全闭合（商可分裂、单子成立、`≡c` = 代表相等）；经济收益的边界（race/deadline 不可下降）保持；S053 把 ERCF-3 的 8 个前置条件、5 个代理任务与停止条件固定，并完成对角核机器核查；ERCF-3 本体保持 gated，下一步做 T2 编码路线实验 |",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY` | 在 Code/quote/substitution/evaluation/provability 固定后构造“有效自我 ASK”最小接口；先证明局部检查正例，再检验总停机/健全/完备/内部可证四者不可兼得的精确条件，不把一般 Gödel 口号冒充 HoTT 实例 |",
        "`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`、`OUT-TOP-ERCF3-PREREQUISITE-ASSESSMENT` | Code/quote/substitution/evaluation/provability 的固定工作已按 S053 的 P1–P8 前置表推进（L0 已资格化；L1 路线由 T2 决定）；抽象对角核（Lawvere + 无精确自编码）已机器核查；继续按 T2/T3 停止条件检验总停机/健全/完备/内部可证四者不可兼得的精确条件，不把一般 Gödel 口号冒充 HoTT 实例 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：ERCF-3 前置评估——N1–N10 的 defense/boundary 审计已覆盖核心库、论文层、提取接口、派生开发与编译后端，E6（natural consumer）仍未找到；不再新增同型审计，改为固定 ERCF-3 的精确演算、反射闭包与 diagonal 前置条件，逐项列出可机器化的最小代理任务、所需假设与停止条件；若前置条件仍要求不存在的 natural consumer，则把 ERCF-3 保持 gated 并转回用户主方向的其它可判别动作。",
        "4. **当前第一工作包**：T2 编码路线实验——在 (a) 普通归纳编码 + 算术化、(b) QIIT、(c) 2LTT 三条路线中确定哪条能在固定工具链中给出“语法 + 替换 + 证明谓词接口”的最小可通过片段；只做可行性，不写 Gödel 句；若 (a) 无法在无新增层级下完成而 (b)/(c) 需要分层，则记录 `SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION` 并停止在该结论；ERCF-3 本体与 T3/T4 保持 gated，备选为 A11.1 W51×RP-B01 命题化。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT`",
        "状态：`CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 52", "source_state_revision: 53")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-036", "projection_generation: 20260912-outcome-037")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT",
        "semantic_status: CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT",
    )
    row = (
        "| `OUT-TOP-ERCF3-PREREQUISITE-ASSESSMENT` | S053 ERCF-3 前置评估——8 个前置条件（P1–P8）与 5 个最小代理任务（T1–T5，含假设与停止条件）；三种读法分析（强/弱/分层）；T1 抽象对角核（Lawvere 不动点、`not` 无不动点、无精确自编码 `A → (A → Bool)`、常值片段精确表示正控制）在固定工具链完成机器核查（探针，零 warning）；强读法在编码层被通用对角核反驳；ERCF-3 本体保持 `GATED` |"
        " `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工评估 + 机器核查探针 | `DOCUMENTED / ERCF3_GATED_WITH_MACHINE_CHECKED_DIAGONAL_CORE` |"
        " 前置条件与代理任务可逐项检查；对角核在 Agda 2.8.0/Cubical v0.9 下 kernel 通过；升级路径唯一为 P8（natural consumer） |"
        " 不新增数学 claim（探针非 claim 包）；不主张 Lawvere 结果的原创性或 HoTT 特有性；不证明 ERCF-3 本体 |"
        " `理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md`；S053 evidence/agda；`audit/understanding-chapter-merge-manifest.json`（33/24） |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 32/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C7 共 8 个独有文件（nonidentical union entries=17）；逐文件处置已生成 |",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 33/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C8 共 9 个独有文件（nonidentical union entries=18）；逐文件处置已生成 |",
    )
    panorama = sub_once(
        panorama,
        "C3/C4/C5/C6/C7 为 top-level current AI strategy/research synthesis",
        "C3/C4/C5/C6/C7/C8 为 top-level current AI strategy/research synthesis",
    )
    panorama = sub_once(
        panorama,
        "N10 工具链/应用层交付审计在固定版本集合内给出 scoped `DEFENSE_WORKS`（cubical 内容无可交付执行路径）；R032 回放、",
        "N10 工具链/应用层交付审计在固定版本集合内给出 scoped `DEFENSE_WORKS`（cubical 内容无可交付执行路径）；S053 把 ERCF-3 拆成 P1–P8/T1–T5 并完成对角核机器核查，判定其本体保持 gated；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "判 scoped `DEFENSE_WORKS`。所有新结论继续执行 F-011。",
        "判 scoped `DEFENSE_WORKS`；S053 完成 ERCF-3 前置评估（P1–P8/T1–T5）与抽象对角核的机器核查（探针，零 warning），判定 ERCF-3 本体保持 gated、强读法在编码层被通用对角核反驳。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | ERCF-3 前置评估 | paper + 最小代理任务设计 | 固定精确演算、反射闭包与 diagonal 前置条件；列出可机器化最小任务与停止条件；仍缺 natural consumer 则保持 gated 并转回用户主方向其它动作 |",
        "| 已闭合工作包 11 | ERCF-3 前置评估（S053） | assessment + machine-checked diagonal core probe | P1–P8/T1–T5 固定；T1 探针 kernel 通过（Lawvere + 无精确自编码 + 正控制）；强读法在编码层被通用对角核反驳；ERCF-3 保持 gated，重开条件见 C8 §9 |\n"
        "| 第一工作包 | T2 编码路线实验 | 有界可行性（语法 + 替换 + 证明谓词接口） | 三路线选一；若需分层则记录 `SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION` 并停止；T3/T4 保持 gated；备选 A11.1 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 ERCF-3 前置评估：固定 ERCF-3 的精确演算、反射闭包与 diagonal 前置条件，逐项列出可机器化的最小代理任务、所需假设与停止条件；若前置条件仍要求不存在的 natural consumer，则把 ERCF-3 保持 gated 并转回用户主方向的其它可判别动作。",
        "2. 当前第一工作包转为 T2 编码路线实验：在 (a) 普通归纳编码 + 算术化、(b) QIIT、(c) 2LTT 中选一条，做出可通过 kernel 的最小片段（语法 + 替换 + 一个证明谓词接口）；只做可行性，不写 Gödel 句；若需分层则记录 `SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION` 并停止；ERCF-3 本体与 T3/T4 保持 gated，备选 A11.1。",
    )
    memory = sub_once(
        memory,
        "- N10 工具链/应用层交付审计（S052）：",
        "- S053 完成 ERCF-3 前置评估：`理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md` 固定 P1–P8 前置条件与 T1–T5 代理任务；T1 抽象对角核（Lawvere 不动点、`not` 无不动点、无精确自编码 `A → (A → Bool)`、常值片段正控制）在 Agda 2.8.0/Cubical v0.9 下探针 kernel 通过（零 warning）；强读法在编码层被通用对角核反驳，ERCF-3 本体保持 gated；理解章节 inventory 重建为 33/24。\n"
        "- N10 工具链/应用层交付审计（S052）：",
    )
    memory = sub_once(
        memory,
        "- 理解章节 merge manifest 当前为 top-level 29、nested 24、union 29、same-name 24、identical 15、different 9、top-only 5、nonidentical 14、unresolved nontrivial 0。",
        "- 理解章节 merge manifest 当前为 top-level 33、nested 24、union 33、same-name 24、identical 15、different 9、top-level unique 9、nonidentical 18、unresolved nontrivial 0（S053 加入 C8 后重建）。",
    )
    memory = sub_once(
        memory,
        "`A-CAUCHY-MODULUS-FORMAL-001`、`A-APPLICATION-LAYER-AUDIT-001`。",
        "`A-CAUCHY-MODULUS-FORMAL-001`、`A-APPLICATION-LAYER-AUDIT-001`、`A-ERCF3-PREREQUISITE-ASSESSMENT-001`。",
    )
    memory = sub_once(
        memory,
        "N10 在固定工具链集合内给出 scoped `DEFENSE_WORKS`（cubical 内容无编译路径）并转 ERCF-3 前置评估，不直接跳 ERCF-3 构造。",
        "N10 在固定工具链集合内给出 scoped `DEFENSE_WORKS`（cubical 内容无编译路径）；S053 完成 ERCF-3 前置评估（P1–P8/T1–T5 + 对角核机器核查）并把 ERCF-3 本体保持 gated，转 T2 编码路线实验，不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S053 完成 ERCF-3 前置评估：`理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md` 固定 P1–P8、T1–T5 与停止条件；T1 抽象对角核探针（Lawvere 不动点、`not` 无不动点、无精确自编码 `A → (A → Bool)`、常值片段正控制）在固定工具链 kernel 通过（零 warning）；判定 ERCF-3 本体保持 `GATED`（强读法在编码层被通用对角核反驳；升级唯一路径是 P8 natural consumer，N1–N10 未发现）。理解章节 merge manifest 重建为 33/24；下一工作包为 T2 编码路线实验，备选 A11.1。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "51. 交付层的资格分离可以先于运行时发生：",
        "52. ERCF-3 一类“理论为自身认证器开总完备证明”的要求，其最强读法可以在**编码层**就被对角核反驳：带 section 的精确自编码 `A → (A → Bool)` 不存在（Lawvere 不动点 + `not` 无不动点）。该论证与 HoTT 无关，因此不能当作 HoTT 特有悖论；有意义的机器化应停在“前置条件 + 探针”层，只有出现真实 natural consumer 或 HoTT 特有规则的不可替代使用才继续升级。评估必须显式区分强/弱/分层三种读法，否则会把“前提不可满足”误读成“理论失败”。\n"
        "51. 交付层的资格分离可以先于运行时发生：",
    )
    return {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 52 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_52_AND_S052")
    if not (root / C8).is_file():
        raise SystemExit(f"C8_MISSING:{C8}")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}
    new_hashes[C8] = sha(root / C8)
    new_hashes[MERGE_MANIFEST] = sha(root / MERGE_MANIFEST)

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README, MERGE_MANIFEST})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S053 ERCF-3 prerequisite assessment: the understanding-chapter merge manifest was rebuilt (33/24) "
        "because C8 was added; no proof source, run or claim-matrix row changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "research_synthesis",
        "path": C8,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "ERCF3_GATED_WITH_MACHINE_CHECKED_DIAGONAL_CORE",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-HOTT-SELF-VALIDATION-ECONOMY-001", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [C8, *EVIDENCE, MERGE_MANIFEST,
                         "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md",
                         "理解章节/C7-post-N6距离综合与剩余域选择-20260912.md",
                         "audit/application-layer-consumer审计-20260912.md",
                         "scripts/audit/prepare_ercf3_prerequisite_checkpoint.py"],
        "source_hashes": {C8: new_hashes[C8], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "resolution": {
            "reason": "ERCF-3 prerequisites were decomposed (P1-P8) and proxy tasks fixed (T1-T5); T1 (abstract diagonal core) type-checked in the fixed toolchain with zero warnings. Verdict: ERCF-3 body remains GATED.",
            "evidence": [C8, f"{SESSION_REL}/evidence/agda/DiagonalCore.agda",
                         f"{SESSION_REL}/evidence/agda/DiagonalCore.check.stdout.txt",
                         MERGE_MANIFEST, "scripts/audit/verify_understanding_merge.py"],
        },
        "scope": "ERCF-3 prerequisite assessment: P1-P8 prerequisites, T1-T5 minimal proxy tasks with assumptions and stop conditions, three readings (strong/weak/stratified), and a machine-checked abstract diagonal core probe (Lawvere fixed point; no exact self-encoding A -> (A -> Bool); constant-fragment positive control). No new mathematical claim; ERCF-3 body stays gated.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C8, *EVIDENCE,
                         MERGE_MANIFEST, "scripts/audit/prepare_ercf3_prerequisite_checkpoint.py"],
        "source_hashes": {C8: new_hashes[C8], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_ERCF3_PREREQUISITE_DIAGONAL_CORE_PROBE",
        "cognition_status": "ERCF3_PREREQUISITE_ASSESSED_AND_T2_ENCODING_ROUTE_ROUTED",
        "scope": "ERCF-3 prerequisite assessment with a machine-checked abstract diagonal core probe and the routing of the T2 encoding-route experiment.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-037" if rid.startswith("I-DIRECTION") else "20260912-outcome-037"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (C8, MERGE_MANIFEST):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the ERCF-3 prerequisite assessment: ERCF-3 body stays gated; the first work package is the bounded T2 encoding-route experiment."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the ERCF-3 prerequisite assessment and the machine-checked diagonal-core probe; the next strand is T2."
    )

    state["revision"] = 53
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "T2 encoding-route experiment (bounded feasibility only): choose one of (a) ordinary inductive encoding + arithmetisation, (b) QIIT, (c) 2LTT/two-level, "
            "and produce a minimal kernel-accepted fragment with syntax, substitution and one proof-predicate interface. Do not write the Goedel sentence. "
            "If (a) cannot be done without an extra level while (b)/(c) require stratification, record SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION and stop there. "
            "T3/T4 and the ERCF-3 body stay gated; the fallback is the A11.1 W51xRP-B01 propositionalisation."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "assessment_kind": "ercf3_prerequisite",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "diagonal_core_probe": {
            "path": f"{SESSION_REL}/evidence/agda/DiagonalCore.agda",
            "sha256": new_hashes[f"{SESSION_REL}/evidence/agda/DiagonalCore.agda"],
            "check_exit": 0,
            "warnings": 0,
            "stderr_bytes": 0,
            "toolchain": "Agda 2.8.0-3d04bac + Cubical v0.9, --safe --cubical --guardedness --ignore-interfaces",
            "contents": [
                "Lawvere fixed point (section forces fixed points of every endomorphism)",
                "not is fixed-point-free on Bool",
                "no exact self-encoding A -> (A -> Bool) with a section",
                "positive control: constant-predicate fragment is exactly representable (injective, hits)",
            ],
            "not_a_claim_package": True,
        },
        "understanding_merge": {"top_level_files": 33, "nested_files": 24, "union_files": 33,
                                "top_level_unique": 9, "nonidentical_union_entries": 18,
                                "unresolved_nontrivial": 0},
        "verdict": "ERCF3_GATED_WITH_MACHINE_CHECKED_DIAGONAL_CORE",
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"assessment": C8, "session_evidence": f"{SESSION_REL}/evidence/"},
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    edited = apply_projection_edits(root)
    texts = {
        **edited,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. "
            "This in-scope checkpoint records the ERCF-3 prerequisite assessment (P1-P8/T1-T5) with a machine-checked diagonal-core probe, "
            "rebuilds the understanding-chapter merge manifest for C8, and routes the bounded T2 encoding-route experiment. "
            "No new mathematical claim, no Git commit, tag or push."
        ),
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
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 53,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
