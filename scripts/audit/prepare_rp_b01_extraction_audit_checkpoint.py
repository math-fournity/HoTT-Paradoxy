#!/usr/bin/env python3
"""Prepare revision 44: record the N2 RP-B01 extraction-interface audit.

N2 fixes real object-layer to execution-layer interfaces (Agda MAlonzo,
Lean evaluation/compilation) and tests whether they promise a uniform
effective implementation for the propositional-LEM classifier chi.  The
audited interfaces refuse: Agda emits a "postulate evaluated" runtime-error
stub and Lean refuses to compile noncomputable definitions.  Verdict:
DEFENSE_WORKS (scoped).  The next work package is the R036/R038 native
Cubical upgrade (N3).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-044-RP-B01-EXTRACTION-AUDIT"
PREV_SESSION = "S-RES-20260912-043-NATURAL-CONSUMER-AUDIT"
RESULT_ID = "A-RP-B01-EXTRACTION-AUDIT-001"
AUDIT = "audit/rp-b01-extraction-interface审计-20260912.md"
N1_AUDIT = "audit/natural-consumer审计-20260912.md"
C5 = "理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
AGDA_SRC = f"{SESSION_REL}/evidence/agda/LemClassifier.agda"
AGDA_HS = f"{SESSION_REL}/evidence/agda/out/MAlonzo/Code/LemClassifier.hs"
LEAN_SRC = f"{SESSION_REL}/evidence/lean/LemClassifier.lean"
NEW_STATUS = "RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_n2_audit", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N2 把提取接口的拒绝写成防御证据，不把 B01 分离包装成已完成悖论。"),
        "KC-000012": ("DEEPENED", "N2 把 ASK 的资格问题落到对象层→执行层：类型层可定义不等于执行层可交付。"),
        "KC-000013": ("DEEPENED", "理论工具性在提取接口上表现为显式的 postulate/noncomputable 代价，而非免费实现。"),
        "KC-000014": ("ALIGNED", "方向 B 的有效交付问题在 N2 中得到接口级拒绝证据；B01-TARGET 仍未被自然接口满足。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮 Agda/Lean 行为均为实际运行，Coq/GHC 缺源如实标记。"),
        "KC-000022": ("ALIGNED", "两类现实相对悖论框架保持不变；N2 没有升级任何未证命题。"),
        "KC-000027": ("DEEPENED", "HoTT/类型论继承程序界限在 N2 中被具体化：公理与 noncomputable 定义没有默认执行实现。"),
        "KC-000031": ("ALIGNED", "接口拒绝继续记为 DEFENSE_WORKS，不判为覆盖失败。"),
        "KC-000035": ("ALIGNED", "HoTT 表达能力与执行交付能力被分开；N2 只审计后者。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N2 的 scoped defense 不支持提前启动反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是固定接口集合内的 N2 提取行为审计；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S044/SESSION.md；audit/rp-b01-extraction-interface审计-20260912.md | N3、B01-TARGET 其它接口、ERCF-3 与 R036/R038 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N2 在被审计提取接口上判 scoped `DEFENSE_WORKS`；`DIR-W-RP-B01` 转 `PARKED` 并保留重开条件；`DIR-W-TRANSITION-ABSTRACTION`/`DIR-W-CURRENT-STATE-LIFT` 转 `NEXT_CANDIDATE`；第一工作包转 N3；revision 44/generation 028。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-RP-B01-EXTRACTION-AUDIT`（scoped `DEFENSE_WORKS`）。",
        "- update_decision: `N2 审计报告进入 audit/；十包 claim 状态不变；N3 进入第一工作包；ERCF-3 继续 gated。`",
        "- cross_conflicts: `NONE_OBSERVED` — claim matrix 未变；Coq/GHC 不可用已如实记为 NOT_AVAILABLE。",
        "- unresolved: `N3、B01-TARGET 其它接口、ERCF-3、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮无新数学结论，状态为 `DEFENSE_WORKS_SCOPED`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：N1 bounded negative 后，STATE 路由 N2 W51×RP-B01 对象层→执行层提取接口审计。",
        "- 接口：Agda 2.8.0 type check + MAlonzo 编译；Lean 4.33.1 求值与 `#eval!`；Coq/Rocq 与 GHC 不可用（NOT_AVAILABLE）。",
        "- 结果：Agda 类型层接受 LEM 分类器，但 MAlonzo 把 postulate 编译为 `error \"postulate evaluated\"`；Lean 内核拒绝 `Prop → Bool` 大消去，`Classical` 版分类器被 `#eval` 与 `#eval!` 以 `dependsOnNoncomputable` 拒绝。",
        "- 判定：`DEFENSE_WORKS_SCOPED` —— 被审计接口不把命题 LEM 下的数学分类承诺为同规格统一有效交付。",
        "- 下一工作包：N3 R036/R038 原生 Cubical 升级（固定状态商/Done 保真/当前态 lift/limit 比较接口；预期最多 `REPRESENTATION_BOUNDARY`；只重证有限模型则停止该子方向）。",
        "- 三件套：direction/panorama revision 44/generation 028；核心认知不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 43", "source_state_revision: 44")
    direction = sub_once(direction, "projection_generation: 20260912-direction-027", "projection_generation: 20260912-direction-028")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-RP-B01` | W51×RP-B01：命题 LEM 下的数学分类、有效总实现、无神谕对角闭包与自然 Think-in-HoTT 交付提升 | WebGPT `P-RP-B01`；用户 KC-000027；A11.1 | `NEXT_CANDIDATE` | `COMPUTATIONAL_LEGITIMACY`, `PARADOX_DISCOVERY`, `SELF_REFERENCE` | `OUT-W-RP-B01`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-NATURAL-CONSUMER-AUDIT` | 这是战略主线：不再以一般停机定理冒充结果；N1 的有界负结论把下一步固定为 N2 提取接口审计——固定真实对象层→执行层接口，判定它是否把命题 LEM 下的数学分类承诺为统一有效交付，再与有效自我 ASK 合流 |",
        "| `DIR-W-RP-B01` | W51×RP-B01：命题 LEM 下的数学分类、有效总实现、无神谕对角闭包与自然 Think-in-HoTT 交付提升 | WebGPT `P-RP-B01`；用户 KC-000027；A11.1 | `PARKED` | `COMPUTATIONAL_LEGITIMACY`, `PARADOX_DISCOVERY`, `SELF_REFERENCE` | `OUT-W-RP-B01`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-NATURAL-CONSUMER-AUDIT`、`OUT-TOP-RP-B01-EXTRACTION-AUDIT` | N2 在被审计接口（Agda MAlonzo、Lean 求值/编译）上判 scoped `DEFENSE_WORKS`：postulate 生成 `error \"postulate evaluated\"`，noncomputable 定义被求值拒绝，Prop→Bool 大消去被内核拒绝；未找到把 LEM 分类承诺为统一有效交付的自然接口；重开条件为新版本/后端默认交付实现或出现实际消费者 |",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-CURRENT-STATE-LIFT` | 当前态提升/截断可达性/不相容有限前缀 | WebGPT `P-CURRENT-STATE-LIFTING-038` | `REVIEW_REQUIRED` | `BEING_AND_BECOMING`, `TIME_AND_TEMPORALITY` | `OUT-W-R038` | 复核截断 accessibility、有限相容性和 sequential limit 反例 |",
        "| `DIR-W-CURRENT-STATE-LIFT` | 当前态提升/截断可达性/不相容有限前缀 | WebGPT `P-CURRENT-STATE-LIFTING-038` | `NEXT_CANDIDATE` | `BEING_AND_BECOMING`, `TIME_AND_TEMPORALITY` | `OUT-W-R038` | N3 原生 Cubical 升级：固定当前态 lift/截断可达性/有限前缀接口，机器证明或反驳 lift no-go 并保留正控制 |",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-TRANSITION-ABSTRACTION` | Done-preserving state quotient 导致 spurious infinite path 和 lift obstruction | WebGPT `P-TRANSITION-ABSTRACTION-036` | `REVIEW_REQUIRED` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT` | `OUT-W-R036` | 固定抽象关系、保持量和具体/抽象反例，不把抽象反例回传成 HoTT 核心错误 |",
        "| `DIR-W-TRANSITION-ABSTRACTION` | Done-preserving state quotient 导致 spurious infinite path 和 lift obstruction | WebGPT `P-TRANSITION-ABSTRACTION-036` | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT` | `OUT-W-R036` | N3 原生 Cubical 升级：固定 Done 保真商、具体/抽象反例与 lift obstruction 接口，不把抽象反例回传成 HoTT 核心错误 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N2 W51×RP-B01 提取接口审计——固定真实对象层→执行层接口（证明助手/编译/提取入口），核对它是否把命题 LEM 下的数学分类承诺为同规格统一有效交付；四组控制：有限步停机检测、经典分支常量、真正停机分类、显式神谕/用户实现；找到候选则进入 F-011 机器化，明确拒绝则记 `DEFENSE_WORKS`，缺源则记 `INCONCLUSIVE_SOURCE_UNAVAILABLE`。",
        "4. **当前第一工作包**：N3 R036/R038 原生 Cubical 升级——固定状态商、Done 保真、当前态 lift 与 limit 比较接口，机器证明（或反驳）相应 lift/limit no-go 并保留正向控制；预期最多 `REPRESENTATION_BOUNDARY`；若只重证有限模型且无新机制则停止该子方向，回到新候选生成。",
    )
    direction = sub_once(
        direction,
        "6. **战略自反深化**：N2 先审计 `DIR-W-RP-B01` 的真实对象层→执行层接口（`B01-TARGET`）；ERCF-3 继续等待精确演算与自然 consumer，不以一般 Gödel 口号提前启动。",
        "6. **战略自反深化**：`DIR-W-RP-B01` 在被审计提取接口上判 scoped `DEFENSE_WORKS` 并转 `PARKED`（重开条件见 N2 审计 §5）；ERCF-3 继续等待精确演算与自然 consumer，不以一般 Gödel 口号提前启动。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 43", "source_state_revision: 44")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-027", "projection_generation: 20260912-outcome-028")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT",
    )
    audit_row = (
        "| `OUT-TOP-RP-B01-EXTRACTION-AUDIT` | N2 对象层→执行层提取接口审计——Agda MAlonzo 把 LEM postulate 编译为 `error \"postulate evaluated\"`；Lean 内核拒绝 `Prop → Bool` 大消去，`Classical` 版分类器被 `#eval`/`#eval!` 以 `dependsOnNoncomputable` 拒绝；Coq/GHC 不可用 |"
        " `DIR-W-RP-B01`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前实测审计 | `DEFENSE_WORKS_SCOPED` |"
        " 两套真实工具链实际运行；生成 Haskell 与 Lean 输出留档；四组控制逐项记录（第 4 组未构建，标 NOT_RUN） |"
        " 不证明任何接口/版本都不可能作出统一有效交付承诺；不把 B01 分离升级为 HoTT 悖论 |"
        " `audit/rp-b01-extraction-interface审计-20260912.md`；S044 evidence/agda 与 evidence/lean |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", audit_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N2 W51×RP-B01 提取接口审计、R036/R038 原生升级、R032 回放、B01-TARGET、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N2 提取接口审计已完成并在被审计接口上判 scoped `DEFENSE_WORKS`；N3 R036/R038 原生升级、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N1 在固定审计集合内给出 bounded negative，最近候选均被显式围栏挡住。",
        "N1 在固定审计集合内给出 bounded negative，最近候选均被显式围栏挡住；N2 在 Agda/Lean 提取接口上判 scoped `DEFENSE_WORKS`（postulate 错误桩、noncomputable 拒绝）。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N2 W51×RP-B01 提取接口审计 | audit / proof-assistant-and-extraction-evidence | 固定真实对象层→执行层接口，核对它是否把命题 LEM 下的数学分类承诺为同规格统一有效交付；四组控制；找到候选进入 F-011，明确拒绝记 `DEFENSE_WORKS`，缺源记 `INCONCLUSIVE_SOURCE_UNAVAILABLE` |",
        "| 第一工作包 | N3 R036/R038 原生 Cubical 升级 | formal / native Cubical Agda | 固定状态商、Done 保真、当前态 lift 与 limit 比较接口；证明（或反驳）lift/limit no-go 并保留正控制；预期最多 `REPRESENTATION_BOUNDARY` |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N2 W51×RP-B01 提取接口审计：固定真实对象层→执行层接口，核对它是否把命题 LEM 下的数学分类承诺为同规格统一有效交付；找到候选进入 F-011，明确拒绝记 `DEFENSE_WORKS`，缺源记 `INCONCLUSIVE_SOURCE_UNAVAILABLE`。",
        "2. 当前第一工作包转为 N3 R036/R038 原生 Cubical 升级：固定状态商、Done 保真、当前态 lift 与 limit 比较接口，机器证明或反驳 lift/limit no-go 并保留正控制；预期最多 `REPRESENTATION_BOUNDARY`。",
    )
    memory = sub_once(
        memory,
        "- N1 有界自然消费者审计（S043）在固定集合（Cubical v0.9 全库 + 四份一手入口）内未找到 E6：最近候选（`MagicTrick.recover`、`SplitSupport`、`satAC`、delay 商、delay×effects、`uaβ`/SIP、CATT）均被显式假设、相干数据或类型围栏挡住；判定 `BOUNDED_NEGATIVE_MOVE_TO_RP_B01`。",
        "- N1 有界自然消费者审计（S043）在固定集合（Cubical v0.9 全库 + 四份一手入口）内未找到 E6：最近候选（`MagicTrick.recover`、`SplitSupport`、`satAC`、delay 商、delay×effects、`uaβ`/SIP、CATT）均被显式假设、相干数据或类型围栏挡住；判定 `BOUNDED_NEGATIVE_MOVE_TO_RP_B01`。\n"
        "- N2 提取接口审计（S044）在 Agda 2.8.0/MAlonzo 与 Lean 4.33.1 上判 scoped `DEFENSE_WORKS`：postulate 生成 `error \"postulate evaluated\"`，noncomputable 分类器被 `#eval`/`#eval!` 拒绝，`Prop → Bool` 大消去被内核拒绝；`DIR-W-RP-B01` 转 `PARKED` 并保留重开条件。",
    )
    memory = sub_once(
        memory,
        "`A-C5-PARADOX-DISTANCE-001`、`A-NATURAL-CONSUMER-AUDIT-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；C5 固定第二级距离，N1 已给出 bounded negative 并转 N2 提取接口审计，不直接跳 ERCF-3。",
        "`A-C5-PARADOX-DISTANCE-001`、`A-NATURAL-CONSUMER-AUDIT-001`、`A-RP-B01-EXTRACTION-AUDIT-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 在提取接口上给出 scoped `DEFENSE_WORKS` 并转 N3 R036/R038 原生升级，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S044 完成 N2 提取接口审计：Agda 2.8.0 类型层接受 LEM 分类器，但 MAlonzo 把 postulate 编译为 `error \"postulate evaluated\"`；Lean 4.33.1 内核拒绝 `Prop → Bool` 大消去，`Classical` 版分类器被 `#eval`/`#eval!` 拒绝；Coq/GHC 不可用。判定 scoped `DEFENSE_WORKS`，`DIR-W-RP-B01` 转 PARKED。下一工作包为 N3 R036/R038 原生 Cubical 升级；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "42. N1 的有界审计表明，E6 的缺失既可能来自“没有 consumer”，也可能来自“consumer 被显式围栏”：`SplitSupport`/`satAC` 是显式假设，`MagicTrick.recover` 受依赖余域与类型检查围栏，delay 商受 choice/QIIT 条件约束，效应组合的失败被写成不可分配定理，CATT 是 refinement 而非裸函数恢复。审计必须区分 documented boundary / explicit assumption / type-level fence / refinement interface，并把负结论限定在被审计版本与集合内。",
        "42. N1 的有界审计表明，E6 的缺失既可能来自“没有 consumer”，也可能来自“consumer 被显式围栏”：`SplitSupport`/`satAC` 是显式假设，`MagicTrick.recover` 受依赖余域与类型检查围栏，delay 商受 choice/QIIT 条件约束，效应组合的失败被写成不可分配定理，CATT 是 refinement 而非裸函数恢复。审计必须区分 documented boundary / explicit assumption / type-level fence / refinement interface，并把负结论限定在被审计版本与集合内。\n"
        "43. 提取接口审计必须有真实运行证据：Agda postulate 在 MAlonzo 中被编译为 `error \"postulate evaluated\"`，Lean 4.33.1 对 `Prop → Bool` 大消去与 noncomputable 求值分别拒绝。类型层“可定义”与执行层“可交付”是两个独立验收面；接口的默认拒绝是 DEFENSE_WORKS，而不是悖论，也不是“理论已经解决问题”。",
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
    if state.get("revision") != 43 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_43_AND_S043")
    for required in (AUDIT, N1_AUDIT, C5, MATRIX, AGDA_SRC, AGDA_HS, LEAN_SRC):
        if not (root / required).is_file():
            raise SystemExit(f"REQUIRED_FILE_MISSING:{required}")

    new_hashes = {
        AUDIT: sha(root / AUDIT),
        N1_AUDIT: sha(root / N1_AUDIT),
        C5: sha(root / C5),
        MATRIX: sha(root / MATRIX),
        AGDA_SRC: sha(root / AGDA_SRC),
        AGDA_HS: sha(root / AGDA_HS),
        LEAN_SRC: sha(root / LEAN_SRC),
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "extraction_interface_audit",
        "path": AUDIT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "DEFENSE_WORKS_SCOPED",
        "full_sources": [AUDIT, N1_AUDIT, C5, MATRIX, AGDA_SRC, AGDA_HS, LEAN_SRC],
        "source_hashes": {
            AUDIT: new_hashes[AUDIT],
            N1_AUDIT: new_hashes[N1_AUDIT],
            C5: new_hashes[C5],
            MATRIX: new_hashes[MATRIX],
            AGDA_SRC: new_hashes[AGDA_SRC],
            AGDA_HS: new_hashes[AGDA_HS],
            LEAN_SRC: new_hashes[LEAN_SRC],
        },
        "resolution": {
            "reason": "Real runs on Agda 2.8.0 and Lean 4.33.1: the audited extraction interfaces refuse a default effective implementation for the LEM classifier (postulate runtime-error stub; noncomputable evaluation refusal; Prop large-elimination restriction). Coq/GHC unavailable.",
            "evidence": [AUDIT, AGDA_SRC, AGDA_HS, LEAN_SRC],
        },
        "scope": "Audit real object-layer to execution-layer interfaces for W51xRP-B01: does any audited interface promise a uniform effective implementation for the propositional-LEM classifier chi? Result: DEFENSE_WORKS (scoped); no mathematical claim upgraded.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, AUDIT, AGDA_SRC, AGDA_HS, LEAN_SRC, MATRIX],
        "source_hashes": {AUDIT: new_hashes[AUDIT], AGDA_SRC: new_hashes[AGDA_SRC], LEAN_SRC: new_hashes[LEAN_SRC]},
        "mathematical_status": "NO_NEW_MATHEMATICS_DEFENSE_WORKS_SCOPED",
        "cognition_status": "RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_AND_R036_R038_NATIVE_ROUTED",
        "scope": "Run the N2 extraction-interface experiments, record raw evidence, judge DEFENSE_WORKS (scoped), route N3; no claim upgrade.",
    }

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["revalidation"] = "S043/S044 closed the A-line result-quotient consumer and the B-line extraction interface as bounded negative / scoped DEFENSE_WORKS; no E6 consumer found. ERCF-3 stays gated."

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-028" if rid.startswith("I-DIRECTION") else "20260912-outcome-028"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (AUDIT, N1_AUDIT):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N2 extraction-interface audit: DEFENSE_WORKS (scoped); DIR-W-RP-B01 is PARKED with reopen conditions; "
        "the first work package is the N3 R036/R038 native Cubical upgrade."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the scoped DEFENSE_WORKS result for the audited extraction interfaces; the next strand is N3."
    )

    state["revision"] = 44
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N3: upgrade the R036/R038 transition-abstraction/current-state-lift boundary to native Cubical Agda. "
            "Fix the state quotient, Done preservation, current-state lift and limit-comparison interfaces; machine-prove or refute the corresponding lift/limit no-go "
            "with positive controls. Expected verdict at most REPRESENTATION_BOUNDARY. If the native formalization only re-derives the finite model with no new mechanism or interface, "
            "record that and stop the sub-direction, then return to new-candidate generation (DIR01-DIR09 and OP01-OP08) rather than renaming the same counterexample."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "kind": "extraction_interface_audit",
        "new_machine_proofs": [],
        "proof_sources_changed": False,
        "claim_matrix_sha256": new_hashes[MATRIX],
        "interface_runs": {
            "agda_type_check": {"exit_code": 0, "tool": "Agda 2.8.0-3d04bac"},
            "agda_malzano_compile": {"exit_code": 42, "completed": False, "reason": "ghc not available; generated Haskell retained"},
            "lean_eval": {"exit_code": 1, "tool": "Lean 4.33.1", "result": "noncomputable evaluation refused; #eval! also refused"},
            "coq": "NOT_AVAILABLE",
            "ghc": "NOT_AVAILABLE",
        },
        "evidence": {"audit": AUDIT, "agda": f"{SESSION_REL}/evidence/agda/", "lean": f"{SESSION_REL}/evidence/lean/"},
        "mathematics": "NO_NEW_MATHEMATICS / DEFENSE_WORKS_SCOPED",
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
            "This in-scope checkpoint records the N2 RP-B01 extraction-interface audit (revision 44), its real Agda/Lean run evidence, "
            "the scoped DEFENSE_WORKS verdict and the N3 R036/R038 native-Cubical route. No mathematical claim is upgraded. "
            "No Git commit, tag or push."
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
        "revision": 44,
        "session_id": SESSION_ID,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
