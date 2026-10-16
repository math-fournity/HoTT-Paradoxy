#!/usr/bin/env python3
"""Prepare revision 52: record the N10 application-layer audit and route the ERCF-3 prerequisite.

N10 audited the delivery side of the toolchain: Agda 2.8.0's JS and GHC
backends refuse every --cubical module; --erased-cubical only allows erased
use (computational transport and library functions are refused); a plain
module cannot even import the cubical library.  Lean 4.33.1 evaluates
relation-respecting quotient eliminators and refuses representative-dependent
and noncomputable consumers.  Verdict: DEFENSE_WORKS (scoped); no natural
consumer (E6) found in the fixed set.  The next work package is the ERCF-3
prerequisite assessment.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-052-APPLICATION-LAYER-AUDIT"
PREV_SESSION = "S-RES-20260912-051-CAUCHY-MODULUS"
RESULT_ID = "A-APPLICATION-LAYER-AUDIT-001"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/application-layer-consumer审计-20260912.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [
    f"{SESSION_REL}/evidence/agda-js/AGDA_LIBRARIES",
    f"{SESSION_REL}/evidence/agda-js/JsBaseline.agda",
    f"{SESSION_REL}/evidence/agda-js/JsUaTransport.agda",
    f"{SESSION_REL}/evidence/agda-js/JsHit.agda",
    f"{SESSION_REL}/evidence/agda-js/JsQuotient.agda",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalPositive.agda",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalNegative.agda",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalImport.agda",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalLibraryFunction.agda",
    f"{SESSION_REL}/evidence/agda-js/PlainCubicalImport.agda",
    f"{SESSION_REL}/evidence/lean/QuotConsumer.lean",
    f"{SESSION_REL}/evidence/lean/QuotRespect.lean",
    f"{SESSION_REL}/evidence/lean/QuotNoncomputable.lean",
    f"{SESSION_REL}/evidence/agda-js/baseline.node.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/JsUaTransport.js2.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/JsHit.js2.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/JsQuotient.js2.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalPositive.check2.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalNegative.check2.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalLibraryFunction.check.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/ErasedCubicalImport.ghc.stdout.txt",
    f"{SESSION_REL}/evidence/agda-js/PlainCubicalImport.js2.stdout.txt",
    f"{SESSION_REL}/evidence/lean/QuotConsumer.stdout.txt",
    f"{SESSION_REL}/evidence/lean/QuotRespect.stdout.txt",
    f"{SESSION_REL}/evidence/lean/QuotNoncomputable.stdout.txt",
]
NEW_STATUS = "APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_application_layer", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N10 是交付资格边界的防御审计，不升级为内部矛盾，符合‘找理论非现实性’的航向。"),
        "KC-000011": ("DEEPENED", "“思考过程/结果不想让时间参与”在交付层获得新实例：编译后端整体拒绝承载 cubical 计算。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 N10 中具体化为：编译/执行交付面是否接受被擦除的表示数据当作计算依据。"),
        "KC-000013": ("ALIGNED", "理论工具性在交付层的落实：工具链用擦除/拒绝保证计算不依赖被遗忘的 cubical 内容。"),
        "KC-000014": ("ALIGNED", "方向 B 的交付资格在编译后端审计中再获防御性证据。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮 Agda/JS/node 与 Lean 均实际运行并保留原始输出。"),
        "KC-000024": ("ALIGNED", "交付/完成资格的分离在工具链层被执行：可检查不等于可交付执行。"),
        "KC-000027": ("ALIGNED", "HoTT 与程序界限的观察在 N10 中体现为“cubical 内容在 2.8.0 无编译路径”。"),
        "KC-000029": ("DEEPENED", "理论经济在交付层：擦除证明内容换取可编译性，任何计算性依赖被明确拒绝。"),
        "KC-000035": ("ALIGNED", "HoTT 可表达与工具链可交付继续被分开记录，不把防御写成覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 仍 gated；N10 只把前置评估排为下一工作包。"),
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
            ("NOT_TOUCHED", "本轮是 N10 工具链/应用层交付审计；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S052/SESSION.md；{AUDIT_DOC} | ERCF-3 前置与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N10 完成并判 scoped `DEFENSE_WORKS`；第一工作包转 ERCF-3 前置评估；revision 52/generation 036。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-APPLICATION-LAYER-AUDIT`。",
        "- update_decision: `N10 审计证据进入 session evidence、audit 文档与 STATE；不新增数学 claim，claim matrix 不变。`",
        "- cross_conflicts: `NONE_OBSERVED` — Agda 与 Lean 两个方向都执行资格分离；与 N1/N2/N5 的 bounded 结论一致。",
        "- unresolved: `ERCF-3 前置、GHC 实际执行、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `DEFENSE_WORKS (SCOPED)`，E6 未发现。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S051 后的 N10 工作包（工具链/应用层交付消费者审计）。",
        "- 审计集合：Agda 2.8.0-3d04bac 的 JS 与 GHC/MAlonzo 后端、Cubical v0.9 导入面（node v26.7.0 实际执行）、Lean 4.33.1 求值器；GHC 不可用，Haskell 只做源码级检查。",
        "- 结果（scoped `DEFENSE_WORKS`）：`--cubical` 模块被两个后端整体拒绝（`CubicalCompilationNotSupported`）；`--erased-cubical` 只允许擦除使用（计算性 `transport` 与库函数 `not` 均报 `DefinitionIsErased`），GHC 后端接受擦除模块但生成的 Haskell 中不含 cubical 内容；无选项模块导入 cubical 库报三连 `InfectiveImport`；非 cubical 基线经 JS 后端实际运行打印 `BASELINE_OK`。",
        "- Lean 侧：`Quot.lift` 消费者 `#eval` 输出 `true/true`（尊重识别），代表元依赖消去被类型检查拒绝，`noncomputable` 被求值器以 `dependsOnNoncomputable` 拒绝。",
        "- 判定：固定版本集合内没有找到把较弱资格当执行/交付承诺的 natural consumer；E6 未发现，判词维持第二级 `REPRESENTATION_BOUNDARY`。",
        "- 过程披露：探针迭代中的 `--safe`/COMPILE 冲突、library 文件用法、infective `--guardedness`、`_++_` fixity、`@0` 需要 `--erasure` 等按责任点修复，全部中间错误保留在 evidence 输出中。",
        "- 边界：不新增数学 claim；不证明全局不存在 E6；Coq 等后端 NOT_AVAILABLE。",
        "- 三件套：direction/panorama revision 52/generation 036；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 51", "source_state_revision: 52")
    direction = sub_once(direction, "projection_generation: 20260912-direction-035", "projection_generation: 20260912-direction-036")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT",
    )
    direction = sub_once(
        direction,
        "；`MP-CAUCHY-MODULUS-001` 原生给出 Cauchy modulus 表示边界与细化正控制（`C-129`–`C-133`）。",
        "；`MP-CAUCHY-MODULUS-001` 原生给出 Cauchy modulus 表示边界与细化正控制（`C-129`–`C-133`）；N10 工具链/应用层交付审计（S052）在固定版本集合内判 scoped `DEFENSE_WORKS`：cubical 内容在 Agda 2.8.0 两个编译后端均无交付路径，Lean 商消去在类型/求值两层执行资格分离。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N10 应用层消费者审计——在固定集合与版本内审计真实 HoTT/类型论应用代码或工具链插件，检查是否存在把较弱资格（商、截断、等价存在、表示数据缺失）当作交付/计算承诺的 natural consumer；给出每个来源的实际假设、类型围栏与承诺面；预期最多维持 `REPRESENTATION_BOUNDARY`；若只重述已有 defense/boundary 则停止并转 ERCF-3 前置评估。",
        "4. **当前第一工作包**：ERCF-3 前置评估——N1–N10 的 defense/boundary 审计已覆盖核心库、论文层、提取接口、派生开发与编译后端，E6（natural consumer）仍未找到；不再新增同型审计，改为固定 ERCF-3 的精确演算、反射闭包与 diagonal 前置条件，逐项列出可机器化的最小代理任务、所需假设与停止条件；若前置条件仍要求不存在的 natural consumer，则把 ERCF-3 保持 gated 并转回用户主方向的其它可判别动作。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 51", "source_state_revision: 52")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-035", "projection_generation: 20260912-outcome-036")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_ERCF3_PREREQUISITE_NEXT",
    )
    row = (
        "| `OUT-TOP-APPLICATION-LAYER-AUDIT` | N10 工具链/应用层交付审计——Agda 2.8.0 的 JS/GHC 后端整体拒绝 `--cubical` 模块；`--erased-cubical` 只允许擦除使用（计算性 `transport` 与库函数 `not` 报 `DefinitionIsErased`），GHC 后端接受的擦除模块生成物不含 cubical 内容；无选项模块导入 cubical 库报 `InfectiveImport`；非 cubical 基线经 JS 后端实际运行成功；Lean 4.33.1 商消去 `#eval` 正确，代表元依赖消去与 `noncomputable` 消费者被拒绝 |"
        " `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-W-RP-B01`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前工具链实测审计（Agda JS/node + GHC 源码生成 + Lean 求值） | `DEFENSE_WORKS (SCOPED)` |"
        " 固定版本集合内没有把较弱资格当执行/交付承诺的 natural consumer；四层围栏（编译拒绝、导入 infective、erasure 检查、求值拒绝）均有原始输出 |"
        " 不证明全局不存在 E6、不证明其它后端/版本无缺口、不新增数学 claim；GHC 实际执行 NOT_RUN |"
        " `audit/application-layer-consumer审计-20260912.md`；S052 evidence/agda-js 与 evidence/lean；`HoTT/CLAIM_EVIDENCE_MATRIX.md`（本包不新增行） |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N8 SIP/表示消费者机器构造（C-124–C-128）与 N9 Cauchy modulus 表示边界（C-129–C-133，含外部 Real 库接口审计）均已机器闭合；R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N8 SIP/表示消费者机器构造（C-124–C-128）与 N9 Cauchy modulus 表示边界（C-129–C-133，含外部 Real 库接口审计）均已机器闭合；N10 工具链/应用层交付审计在固定版本集合内给出 scoped `DEFENSE_WORKS`（cubical 内容无可交付执行路径）；R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N9 把 Cauchy modulus 表示边界做成最小机器构造（C-129–C-133，零 warning，附外部 Real 库接口审计），判 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。所有新结论继续执行 F-011。",
        "N9 把 Cauchy modulus 表示边界做成最小机器构造（C-129–C-133，零 warning，附外部 Real 库接口审计），判 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`；N10 审计 Agda 2.8.0 的 JS/GHC 编译后端与 Lean 4.33.1 求值：cubical 内容没有可交付执行路径（`--cubical` 全拒、`--erased-cubical` 仅擦除、普通模块无法导入），判 scoped `DEFENSE_WORKS`。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N10 应用层消费者审计 | audit / fixed-set application-layer scan | 固定集合与版本内审计真实应用代码/工具链插件的交付与计算承诺；预期最多维持 `REPRESENTATION_BOUNDARY`；只重述已有 defense 则停止并转 ERCF-3 前置评估 |",
        "| 已闭合工作包 10 | 工具链/应用层交付审计（`S052`） | scoped `DEFENSE_WORKS` | Agda 2.8.0 两后端拒绝 `--cubical`、`--erased-cubical` 仅擦除、普通模块无法导入；Lean 商消去类型/求值双层分离；E6 未发现，重开条件见审计 §4 |\n"
        "| 第一工作包 | ERCF-3 前置评估 | paper + 最小代理任务设计 | 固定精确演算、反射闭包与 diagonal 前置条件；列出可机器化最小任务与停止条件；仍缺 natural consumer 则保持 gated 并转回用户主方向其它动作 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N10 应用层消费者审计：在固定集合与版本内审计真实 HoTT/类型论应用代码或工具链插件，检查是否存在把较弱资格（商、截断、等价存在、表示数据缺失）当作交付/计算承诺的 natural consumer；记录每个来源的实际假设与类型围栏；预期最多维持 `REPRESENTATION_BOUNDARY`；若只重述已有 defense/boundary 则停止并转 ERCF-3 前置评估。",
        "2. 当前第一工作包转为 ERCF-3 前置评估：固定 ERCF-3 的精确演算、反射闭包与 diagonal 前置条件，逐项列出可机器化的最小代理任务、所需假设与停止条件；若前置条件仍要求不存在的 natural consumer，则把 ERCF-3 保持 gated 并转回用户主方向的其它可判别动作。",
    )
    memory = sub_once(
        memory,
        "- N9 Cauchy modulus 表示边界（S051）已由 `MP-CAUCHY-MODULUS-001` 原生机器化：C-129–C-133，零 warning、exact replay；十三个旧包在矩阵增长后全部 row-stable；外部 agda-unimath 接口审计与边界方向一致；判词 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。",
        "- N9 Cauchy modulus 表示边界（S051）已由 `MP-CAUCHY-MODULUS-001` 原生机器化：C-129–C-133，零 warning、exact replay；十三个旧包在矩阵增长后全部 row-stable；外部 agda-unimath 接口审计与边界方向一致；判词 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。\n"
        "- N10 工具链/应用层交付审计（S052）：Agda 2.8.0 的 JS/GHC 后端拒绝全部 `--cubical` 模块（`CubicalCompilationNotSupported`）；`--erased-cubical` 只允许擦除使用（计算性 `transport` 与库函数 `not` 均报 `DefinitionIsErased`）；无选项模块导入 cubical 库报 `InfectiveImport`；非 cubical 基线经 JS 后端实际运行；Lean 4.33.1 商消去 `#eval` 正确且尊重识别，代表元依赖消去被类型检查拒绝、`noncomputable` 被求值器拒绝；判 scoped `DEFENSE_WORKS`，E6 未发现。",
    )
    memory = sub_once(
        memory,
        "`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`、`A-SIP-REPRESENTATION-FORMAL-001`、`A-CAUCHY-MODULUS-FORMAL-001`。九条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision、SIP/表示、Cauchy modulus）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成距离综合，N8 关闭 SIP/表示边界，N9 关闭 Cauchy modulus 表示边界并转 N10 应用层消费者审计，不直接跳 ERCF-3。",
        "`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`、`A-SIP-REPRESENTATION-FORMAL-001`、`A-CAUCHY-MODULUS-FORMAL-001`、`A-APPLICATION-LAYER-AUDIT-001`。九条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision、SIP/表示、Cauchy modulus）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成距离综合，N8 关闭 SIP/表示边界，N9 关闭 Cauchy modulus 表示边界，N10 在固定工具链集合内给出 scoped `DEFENSE_WORKS`（cubical 内容无编译路径）并转 ERCF-3 前置评估，不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S052 完成 N10：工具链/应用层交付审计在 Agda 2.8.0-3d04bac（JS 后端实际运行到 node v26.7.0；GHC 源码生成，无 ghc 执行）与 Lean 4.33.1 上完成实测。结论 scoped `DEFENSE_WORKS`：`--cubical` 模块被两个编译后端整体拒绝；`--erased-cubical` 只允许擦除使用（计算性 `transport`、库函数 `not` 报 `DefinitionIsErased`）；无选项模块导入 cubical 库报 `InfectiveImport`；非 cubical 基线实际运行成功；Lean 商消去尊重识别、代表元依赖与 `noncomputable` 消费者被拒绝。E6 未发现，判词仍为第二级 `REPRESENTATION_BOUNDARY`。下一工作包为 ERCF-3 前置评估；ERCF-3 构造继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "50. 最小 Cauchy modulus 边界显示“按极限值取商”与“保留给定 modulus”是两个不同承诺：`ℕ → Bool` 序列加 `Σ N` 常量性数据就足以证明商层识别 `(constTrue,0)`/`(constTrue,1)` 而 modulus 不可统一恢复；把 modulus 纳入同一性关系即得正控制。外部 agda-unimath 把 convergence modulus 与 modulated Cauchy 序列写成显式结构、完备性定理 `opaque`，与该边界方向一致；引用外部接口时必须绑定抓取提交与 blob hash，且不得由接口形状推断某个具体使用已经出错。",
        "50. 最小 Cauchy modulus 边界显示“按极限值取商”与“保留给定 modulus”是两个不同承诺：`ℕ → Bool` 序列加 `Σ N` 常量性数据就足以证明商层识别 `(constTrue,0)`/`(constTrue,1)` 而 modulus 不可统一恢复；把 modulus 纳入同一性关系即得正控制。外部 agda-unimath 把 convergence modulus 与 modulated Cauchy 序列写成显式结构、完备性定理 `opaque`，与该边界方向一致；引用外部接口时必须绑定抓取提交与 blob hash，且不得由接口形状推断某个具体使用已经出错。\n"
        "51. 交付层的资格分离可以先于运行时发生：Agda 2.8.0 的两个编译后端整体拒绝 `--cubical` 模块，`--erased-cubical` 只允许与计算无关的擦除使用（计算性 `transport` 与 cubical 库函数 `not` 都报 `DefinitionIsErased`），cubical 选项是 infective 的（普通模块导入即 `InfectiveImport`），因此“理论检查通过”与“可编译执行”是两层不同验收面。审计交付链必须区分 type check、编译接受、生成物检查与实际运行四种证据；无 GHC 时只能到“生成物检查”，不能声称已执行。",
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
    if state.get("revision") != 51 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_51_AND_S051")
    if not (root / AUDIT_DOC).is_file():
        raise SystemExit(f"AUDIT_DOC_MISSING:{AUDIT_DOC}")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}
    new_hashes[AUDIT_DOC] = sha(root / AUDIT_DOC)

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S052 application-layer audit; no proof source, run or claim-matrix row changed in this session."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes[rel] if rel in new_hashes else sha(root / rel)
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "application_layer_audit",
        "path": AUDIT_DOC,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "DEFENSE_WORKS_SCOPED",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [AUDIT_DOC, *EVIDENCE, MATRIX,
                         "HoTT/formal/cauchy-modulus/TOOLCHAIN.json",
                         "scripts/audit/prepare_application_layer_audit_checkpoint.py"],
        "source_hashes": {AUDIT_DOC: new_hashes[AUDIT_DOC], MATRIX: sha(root / MATRIX),
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "resolution": {
            "reason": "Fixed-version toolchain probes were actually run (Agda JS backend executed with node; GHC backend generated Haskell sources; Lean 4.33.1 evaluated quotient programs). No natural consumer found; verdict DEFENSE_WORKS (scoped).",
            "evidence": [AUDIT_DOC,
                         f"{SESSION_REL}/evidence/agda-js/baseline.node.stdout.txt",
                         f"{SESSION_REL}/evidence/agda-js/JsUaTransport.js2.stdout.txt",
                         f"{SESSION_REL}/evidence/agda-js/ErasedCubicalNegative.check2.stdout.txt",
                         f"{SESSION_REL}/evidence/lean/QuotConsumer.stdout.txt",
                         f"{SESSION_REL}/evidence/lean/QuotNoncomputable.stdout.txt"],
        },
        "scope": "Application-layer/toolchain delivery audit in a fixed version set: Agda 2.8.0-3d04bac (JS backend executed via node v26.7.0; GHC/MAlonzo source generation only, no ghc) with Cubical v0.9, and Lean 4.33.1 evaluation. Cubical content has no compilable delivery path; erased-cubical only permits erased use; Lean quotients separate qualification at type and evaluation layers. No natural consumer (E6) found; verdict DEFENSE_WORKS (SCOPED); not a mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, AUDIT_DOC,
                         "scripts/audit/prepare_application_layer_audit_checkpoint.py", *EVIDENCE],
        "source_hashes": {AUDIT_DOC: new_hashes[AUDIT_DOC],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_APP_Layer_DEFENSE_WORKS_SCOPED",
        "cognition_status": "APPLICATION_LAYER_AUDIT_DEFENSE_WORKS_AND_ERCF3_PREREQUISITE_ROUTED",
        "scope": "Toolchain/application-layer delivery audit (N10) with raw probe outputs, and routing of the ERCF-3 prerequisite assessment.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-036" if rid.startswith("I-DIRECTION") else "20260912-outcome-036"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (AUDIT_DOC,):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N10 application-layer audit: delivery backends perform qualification separation (scoped DEFENSE_WORKS); the first work package is the ERCF-3 prerequisite assessment."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the N10 application-layer audit (scoped DEFENSE_WORKS, no new mathematical claim); the next strand is the ERCF-3 prerequisite assessment."
    )

    state["revision"] = 52
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "ERCF-3 prerequisite assessment: fix the exact calculus, the reflection closure and the diagonal prerequisites; list the minimal machine-checkable proxy tasks with their assumptions and stop conditions. "
            "Do not build the ERCF-3 diagonal itself. If the prerequisites still require a natural consumer that N1-N10 did not find, keep ERCF-3 gated and return to other decidable actions of the user's main direction."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "audit_kind": "application_layer_delivery",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "environment": {
            "agda": "2.8.0-3d04bac (binary sha256 ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e)",
            "cubical": "v0.9 (tag commit b150186d2544e7efeddd31e5d14a8b9ecbb100f7, tree sha256 73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81)",
            "node": "v26.7.0",
            "lean": "4.33.1 (commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6)",
            "ghc": "NOT_AVAILABLE",
        },
        "probes": {
            "JsBaseline": {"check": 0, "js": 0, "node": 0, "stdout": "BASELINE_OK"},
            "JsUaTransport": {"check": 0, "js": 42, "ghc_source": 42, "error": "CubicalCompilationNotSupported"},
            "JsHit": {"check": 0, "js": 42, "ghc_source": 42, "error": "CubicalCompilationNotSupported"},
            "JsQuotient": {"check": 0, "js": 42, "ghc_source": 42, "error": "CubicalCompilationNotSupported"},
            "ErasedCubicalPositive": {"check": 0, "js": 42, "ghc_source": 0, "erased_content_dropped": True},
            "ErasedCubicalNegative": {"check": 42, "error": "DefinitionIsErased"},
            "ErasedCubicalLibraryFunction": {"check": 42, "error": "DefinitionIsErased"},
            "ErasedCubicalImport": {"check": 0, "js": 42, "ghc_source": 0},
            "PlainCubicalImport": {"check": 42, "error": "InfectiveImport"},
            "LeanQuotConsumer": {"exit": 0, "stdout": ["true", "true"]},
            "LeanQuotRespect": {"exit": 1, "error": "type_error_rfl_a_b"},
            "LeanQuotNoncomputable": {"exit": 1, "error": "dependsOnNoncomputable"},
        },
        "verdict": "DEFENSE_WORKS_SCOPED",
        "e6_found": False,
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"audit": AUDIT_DOC, "session_evidence": f"{SESSION_REL}/evidence/"},
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
            "This in-scope checkpoint records the N10 application-layer/toolchain audit (scoped DEFENSE_WORKS, no new mathematical claim), "
            "keeps the claim matrix unchanged, and routes the ERCF-3 prerequisite assessment. No Git commit, tag or push."
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
        "revision": 52,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
