#!/usr/bin/env python3
"""Prepare revision 45: record MP-TRANSITION-LIFT-001 and route N4.

N3 upgraded the R036/R038 core to native Cubical Agda (C-110-C-117):
the finite transition quotient/lift boundary and the R038-D
truncation-limit non-commutation.  Verdict is a boundary result with
positive controls (TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS).
The R036/R038 sub-direction is therefore closed with scope and the next
work package is N4: new-candidate generation (DIR01-DIR09 x OP01-OP08).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-045-TRANSITION-LIFT"
PREV_SESSION = "S-RES-20260912-044-RP-B01-EXTRACTION-AUDIT"
RESULT_ID = "A-TRANSITION-LIFT-FORMAL-001"
PROOF_ID = "MP-TRANSITION-LIFT-001"
RUN_ID = "20260912-MP-TRANSITION-LIFT-001-01"
SOURCE = "HoTT/formal/transition-lift/TransitionLift.agda"
SOURCE_README = "HoTT/formal/transition-lift/README.md"
TOOLCHAIN = "HoTT/formal/transition-lift/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/transition-lift/AGDA_LIBRARIES"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/transition-lift机器证明实施证据-20260912.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_transition_lift", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N3 交付的是过渡抽象边界与正控制，不把抽象无限路径升级成现实相对悖论。"),
        "KC-000011": ("DEEPENED", "次序/分支在 R036 的逐步执行与抽象自由拼接的差别中被机器化。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题具体化为“固定当前代表的后继 C”与“只固定抽象端点的存在像 E”的差别。"),
        "KC-000013": ("ALIGNED", "理论工具性的遗忘（状态合并）在 N3 中被形式化为 α、C、E 与 lift no-go。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮为 Agda 2.8.0/Cubical v0.9 实际 kernel 运行、exit 0、零 warning。"),
        "KC-000022": ("ALIGNED", "两类现实相对框架保持不变；机器结论是边界而非 HoTT 内部矛盾。"),
        "KC-000024": ("DEEPENED", "时序/过程条件的保持性在 C-112/C-113 与 C-114–C-116 中被机器检验。"),
        "KC-000029": ("DEEPENED", "理论经济的“忘掉状态”在 N3 中给出 C/E 分离与精确极限不可提升的机器证据。"),
        "KC-000031": ("ALIGNED", "严格规则/结构约束继续被记录为边界与正控制，不判为覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N3 不涉及自指反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是 R036/R038 核心边界的原生 Cubical 升级；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S045/SESSION.md；HoTT/formal/transition-lift/TransitionLift.agda | N4、ERCF-3 与其它接口仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — `DIR-W-TRANSITION-ABSTRACTION` 与 `DIR-W-CURRENT-STATE-LIFT` 转 `CLOSED_WITH_SCOPE`；第一工作包转 N4 新候选生成；revision 45/generation 029。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-TRANSITION-LIFT`（`TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`）。",
        "- update_decision: `MP-TRANSITION-LIFT-001 进入 formal/run/index/STATE；C-110–C-117 进入 claim matrix；十个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十一个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `N4 新候选生成、R038-A/B Acc 迁移、R032 回放、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S044 后的 N3 工作包（R036/R038 原生 Cubical 升级）。",
        "- 构造：有限模型 `S={a,b,d}`、`Q={w,W}`、`α` 合并 `a,b`；`R` 为 `step : S → Maybe S` 的图；`C`/`E` 用命题截断定义；R038-D 塔 `A k = Σ m, k ≤ m`。",
        "- 结果：`MP-TRANSITION-LIFT-001`（C-110–C-117）通过 kernel：终止正控制、存在像自环、`w,w,w` 无具体两步提升、无当前态提升函数、精确极限空、截断极限有元素、无逆、无纤维恒定下降等级。判词 `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`（非悖论）。",
        "- 运行：final run `20260912-MP-TRANSITION-LIFT-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`），零 warning。",
        "- 旧证据：矩阵第九次增长后，十个旧包全部重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：`_≤_`/`¬`/`⊤` 作用域、`rec` 歧义、`just-inj` 重名、`≤` 辅助引理 UnequalTerms 与 `j` 的 UnsolvedConstraints；均按责任点修复，命题未削弱。",
        "- 边界：不主张一般图 lift/limit 定理、R038-A/B Acc 迁移、实际系统误用、物理时间或原创性。",
        "- 三件套：direction/panorama revision 45/generation 029；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT`",
        "状态：`CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 44", "source_state_revision: 45")
    direction = sub_once(direction, "projection_generation: 20260912-direction-028", "projection_generation: 20260912-direction-029")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT",
        "semantic_status: CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-CURRENT-STATE-LIFT` | 当前态提升/截断可达性/不相容有限前缀 | WebGPT `P-CURRENT-STATE-LIFTING-038` | `NEXT_CANDIDATE` | `BEING_AND_BECOMING`, `TIME_AND_TEMPORALITY` | `OUT-W-R038` | N3 原生 Cubical 升级：固定当前态 lift/截断可达性/有限前缀接口，机器证明或反驳 lift no-go 并保留正控制 |",
        "| `DIR-W-CURRENT-STATE-LIFT` | 当前态提升/截断可达性/不相容有限前缀 | WebGPT `P-CURRENT-STATE-LIFTING-038` | `CLOSED_WITH_SCOPE` | `BEING_AND_BECOMING`, `TIME_AND_TEMPORALITY` | `OUT-W-R038`、`OUT-TOP-TRANSITION-LIFT`（C-114–C-116） | R038-D 的截断—极限核心已原生机器化：精确极限空、截断极限有元素、比较映射无逆；R038-A/B 的 Acc 迁移仍为 paper；重开条件为 Acc 迁移原生化或出现真实 consumer |",
    )
    direction = sub_once(
        direction,
        "| `DIR-W-TRANSITION-ABSTRACTION` | Done-preserving state quotient 导致 spurious infinite path 和 lift obstruction | WebGPT `P-TRANSITION-ABSTRACTION-036` | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT` | `OUT-W-R036` | N3 原生 Cubical 升级：固定 Done 保真商、具体/抽象反例与 lift obstruction 接口，不把抽象反例回传成 HoTT 核心错误 |",
        "| `DIR-W-TRANSITION-ABSTRACTION` | Done-preserving state quotient 导致 spurious infinite path 和 lift obstruction | WebGPT `P-TRANSITION-ABSTRACTION-036` | `CLOSED_WITH_SCOPE` | `TIME_AND_TEMPORALITY`, `HOTT_OBJECT` | `OUT-W-R036`、`OUT-TOP-TRANSITION-LIFT`（C-110–C-113、C-117） | R036 的有限商/提升核心已原生机器化：自环存在像、无两步具体提升、无当前态提升函数、无纤维恒定下降等级；不再重证同一有限模型；重开条件为新机制或新接口 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N3 R036/R038 原生 Cubical 升级——固定状态商、Done 保真、当前态 lift 与 limit 比较接口，机器证明（或反驳）相应 lift/limit no-go 并保留正向控制；预期最多 `REPRESENTATION_BOUNDARY`；若只重证有限模型且无新机制则停止该子方向，回到新候选生成。",
        "4. **当前第一工作包**：N4 新候选生成——按 `hott-paradox-research` 的 OP01–OP08 与 DIR01–DIR09 对未触达方向（先后/依赖、形成资格、历史/来源、方向/不可逆、运动/连续、自指）系统生成候选；每个候选必须固定 HoTT 配置、任务、抽象与后续操作，关键步骤必须让 UA/Id/HIT/Π 或 truncation 真正参与，并直接指向 E6（natural consumer）；不得改名重述 R036/R038/R034/race-timeout 的既有反例。",
    )
    direction = sub_once(
        direction,
        "C4 整体仍是 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE_AND_PARTIALITY_CONTEXT_MONAD_AND_CHARACTERIZATION_BOUNDARY`：C-59–C-66、C-67–C-70、C-71–C-76、C-77–C-83、C-84–C-88 与 C-89–C-91 分别机器闭合；截断是 `DEFENSE_WORKS`、partiality 边界是 `REPRESENTATION_BOUNDARY`、商值单子是 `MONAD_STRUCTURE_CONSTRUCTED`；现实桥梁、natural consumer、具体非停机与 ERCF-3 仍开放。",
        "C4 整体仍是 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_DEFENSES_AND_BOUNDARIES`：C-59–C-66（通用因子化）、C-67–C-70（截断防御）、C-71–C-91（partiality/上下文/商单子/完整刻画）、C-92–C-95（guard-erasure）、C-96–C-99（cost）、C-100–C-105（路径证书）、C-106–C-109（在线因果）与 C-110–C-117（过渡抽象/极限）分别机器闭合；判词覆盖 `DEFENSE_WORKS`、`REPRESENTATION_BOUNDARY`、`MONAD_STRUCTURE_CONSTRUCTED`、`TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS` 等；现实桥梁、natural consumer、具体非停机与 ERCF-3 仍开放。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT`",
        "状态：`CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 44", "source_state_revision: 45")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-028", "projection_generation: 20260912-outcome-029")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_RP_B01_EXTRACTION_AUDIT_DEFENSE_WORKS_R036_R038_NATIVE_NEXT",
        "semantic_status: CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT",
    )
    row = (
        "| `OUT-TOP-TRANSITION-LIFT` | `MP-TRANSITION-LIFT-001`：R036/R038 核心边界原生升级——三状态终止正控制（`C-110`）、存在像自环与抽象无限路径（`C-111`）、`w,w,w` 无具体两步提升（`C-112`）、无当前态提升函数（`C-113`）、精确相容极限为空（`C-114`）、截断极限有元素（`C-115`）、比较映射无逆（`C-116`）、无严格下降纤维恒定等级（`C-117`） |"
        " `DIR-W-TRANSITION-ABSTRACTION`、`DIR-W-CURRENT-STATE-LIFT`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0（零 warning）、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；十个旧包在矩阵增长后全部 row-stable + exact replay |"
        " 不证明一般图 lift/limit 定理、R038-A/B 的 Acc 迁移、任何实际系统误用或 HoTT 内部矛盾 |"
        " `HoTT/formal/transition-lift/`；final run `20260912-MP-TRANSITION-LIFT-001-01`；claim matrix C-110–C-117；`audit/transition-lift机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N3 R036/R038 原生升级、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N3 R036/R038 原生升级已机器闭合（C-110–C-117）；N4 新候选生成、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N2 在 Agda/Lean 提取接口上判 scoped `DEFENSE_WORKS`（postulate 错误桩、noncomputable 拒绝）。所有新结论继续执行 F-011。",
        "N2 在 Agda/Lean 提取接口上判 scoped `DEFENSE_WORKS`（postulate 错误桩、noncomputable 拒绝）；N3 把 R036/R038 核心边界原生机器化（C-110–C-117，零 warning），判 `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N3 R036/R038 原生 Cubical 升级 | formal / native Cubical Agda | 固定状态商、Done 保真、当前态 lift 与 limit 比较接口；证明（或反驳）lift/limit no-go 并保留正控制；预期最多 `REPRESENTATION_BOUNDARY` |",
        "| 第一工作包 | N4 新候选生成（DIR01–DIR09 × OP01–OP08） | generation / paper-first | 对未触达方向系统生成候选；每个候选固定 HoTT 配置/任务/抽象/后续操作，关键步骤必须使用 UA/Id/HIT/Π 或 truncation，并直接指向 E6；不得改名重述既有反例 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N3 R036/R038 原生 Cubical 升级：固定状态商、Done 保真、当前态 lift 与 limit 比较接口，机器证明或反驳 lift/limit no-go 并保留正控制；预期最多 `REPRESENTATION_BOUNDARY`。",
        "2. 当前第一工作包转为 N4 新候选生成：按 OP01–OP08 × DIR01–DIR09 对未触达方向系统生成候选；每个候选固定 HoTT 配置/任务/抽象/后续操作，关键步骤必须让 UA/Id/HIT/Π 或 truncation 真正参与，并直接指向 E6（natural consumer）；不得改名重述既有反例。",
    )
    memory = sub_once(
        memory,
        "- N2 提取接口审计（S044）在 Agda 2.8.0/MAlonzo 与 Lean 4.33.1 上判 scoped `DEFENSE_WORKS`：postulate 生成 `error \"postulate evaluated\"`，noncomputable 分类器被 `#eval`/`#eval!` 拒绝，`Prop → Bool` 大消去被内核拒绝；`DIR-W-RP-B01` 转 `PARKED` 并保留重开条件。",
        "- N2 提取接口审计（S044）在 Agda 2.8.0/MAlonzo 与 Lean 4.33.1 上判 scoped `DEFENSE_WORKS`：postulate 生成 `error \"postulate evaluated\"`，noncomputable 分类器被 `#eval`/`#eval!` 拒绝，`Prop → Bool` 大消去被内核拒绝；`DIR-W-RP-B01` 转 `PARKED` 并保留重开条件。\n"
        "- N3 过渡抽象/极限边界（S045）已由 `MP-TRANSITION-LIFT-001` 原生机器化：C-110–C-117，零 warning、exact replay；十个旧包在矩阵增长后全部 row-stable；`DIR-W-TRANSITION-ABSTRACTION` 与 `DIR-W-CURRENT-STATE-LIFT` 转 `CLOSED_WITH_SCOPE`。",
    )
    memory = sub_once(
        memory,
        "`A-NATURAL-CONSUMER-AUDIT-001`、`A-RP-B01-EXTRACTION-AUDIT-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 在提取接口上给出 scoped `DEFENSE_WORKS` 并转 N3 R036/R038 原生升级，不直接跳 ERCF-3。",
        "`A-NATURAL-CONSUMER-AUDIT-001`、`A-RP-B01-EXTRACTION-AUDIT-001`、`A-TRANSITION-LIFT-FORMAL-001`。六条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 把 R036/R038 核心边界原生机器化并转 N4 新候选生成，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S045 完成 N3：`MP-TRANSITION-LIFT-001`（C-110–C-117）在 Agda 2.8.0/Cubical v0.9 下原生机器化 R036/R038 核心边界，零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay；十个旧包在矩阵增长后全部 row-stable。判词 `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`；`DIR-W-TRANSITION-ABSTRACTION` 与 `DIR-W-CURRENT-STATE-LIFT` 转 `CLOSED_WITH_SCOPE`。下一工作包为 N4 新候选生成（DIR01–DIR09 × OP01–OP08）；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "43. 提取接口审计必须有真实运行证据：Agda postulate 在 MAlonzo 中被编译为 `error \"postulate evaluated\"`，Lean 4.33.1 对 `Prop → Bool` 大消去与 noncomputable 求值分别拒绝。类型层“可定义”与执行层“可交付”是两个独立验收面；接口的默认拒绝是 DEFENSE_WORKS，而不是悖论，也不是“理论已经解决问题”。",
        "43. 提取接口审计必须有真实运行证据：Agda postulate 在 MAlonzo 中被编译为 `error \"postulate evaluated\"`，Lean 4.33.1 对 `Prop → Bool` 大消去与 noncomputable 求值分别拒绝。类型层“可定义”与执行层“可交付”是两个独立验收面；接口的默认拒绝是 DEFENSE_WORKS，而不是悖论，也不是“理论已经解决问题”。\n"
        "44. 原生升级旧的有限检查边界时，先固定 claim 映射与禁止外推，再处理实现警告：把索引归纳族改成构造子递归的函数定义（如 `_≤_`）可消除 `UnsupportedIndexedMatch` 而不改变命题；矩阵追加新 proof 后必须重放全部旧包并保持 row-stable，不能只验证新包。",
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
    if state.get("revision") != 44 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_44_AND_S044")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(110, 118)]
    ):
        raise SystemExit("FINAL_RUN_NOT_ACCEPTED_AND_INDEXED")
    for required in ("index-row-manifest.json", "source-manifest.json", "stdout.txt", "stderr.txt", "environment.txt"):
        if not (run_dir / required).is_file():
            raise SystemExit(f"RUN_FILE_MISSING:{required}")

    new_hashes = {
        MATRIX: sha(root / MATRIX),
        FORMAL_README: sha(root / FORMAL_README),
        RUNS_README: sha(root / RUNS_README),
        SOURCE: sha(root / SOURCE),
        SOURCE_README: sha(root / SOURCE_README),
        TOOLCHAIN: sha(root / TOOLCHAIN),
        LIBRARIES: sha(root / LIBRARIES),
        f"HoTT/verification/runs/{RUN_ID}/RUN.json": sha(run_dir / "RUN.json"),
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": sha(run_dir / "index-row-manifest.json"),
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": sha(run_dir / "source-manifest.json"),
        AUDIT_DOC: sha(root / AUDIT_DOC),
    }

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
    note = "After C-110 through C-117 were appended (S045), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH for the ten older packages."
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes[rel]
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(110, 118)],
        "run_id": RUN_ID,
        "mathematical_status": "NATIVE_R036_R038_CORE_BOUNDARY_MACHINE_PROVED",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [
            SOURCE, SOURCE_README, TOOLCHAIN, LIBRARIES,
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/stdout.txt",
            f"HoTT/verification/runs/{RUN_ID}/stderr.txt",
            f"HoTT/verification/runs/{RUN_ID}/environment.txt",
            MATRIX, "scripts/audit/capture_agda_proof_run.py",
            "scripts/audit/mark_proof_run_indexed.py",
            "scripts/audit/freeze_proof_index_rows.py",
            "scripts/audit/verify_formal_proof_run.py", AUDIT_DOC,
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE], SOURCE_README: new_hashes[SOURCE_README],
            TOOLCHAIN: new_hashes[TOOLCHAIN], LIBRARIES: new_hashes[LIBRARIES],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX], AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0 with zero warnings; source, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX, "scripts/audit/verify_formal_proof_run.py", AUDIT_DOC,
            ],
        },
        "scope": "Native Cubical Agda upgrade of the R036/R038 core: finite transition quotient with terminal d; spurious existential-image self-loop; no concrete two-step lift of w,w,w from a; no exact current-state successor lift; no strictly descending fibre-constant rank; R038-D exact limit empty, truncated limit inhabited, no inverse. Boundary result with positive controls; not a HoTT paradox.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, SOURCE, SOURCE_README,
                         f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                         f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC,
                         "scripts/audit/prepare_transition_lift_checkpoint.py"],
        "source_hashes": {SOURCE: new_hashes[SOURCE],
                          f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
                          AUDIT_DOC: new_hashes[AUDIT_DOC]},
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_TRANSITION_LIFT",
        "cognition_status": "TRANSITION_LIFT_BOUNDARY_PROVED_AND_NEW_CANDIDATE_GENERATION_ROUTED",
        "scope": "Native Cubical upgrade of the R036/R038 core (C-110–C-117), revalidation of ten older packages, and routing of the N4 new-candidate generation.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-029" if rid.startswith("I-DIRECTION") else "20260912-outcome-029"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                    f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the native transition-lift result: the R036/R038 core is machine-proved and closed with scope; "
        "the first work package is the N4 new-candidate generation over DIR01-DIR09 and OP01-OP08."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the native transition-lift boundary (C-110-C-117); the next strand is N4 new-candidate generation."
    )

    state["revision"] = 45
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N4: generate new paradox candidates by systematically applying OP01-OP08 to the least-touched DIR01-DIR09 directions "
            "(order/dependency, formation qualification, history/provenance, direction/irreversibility, motion/continuity, self-reference). "
            "Each candidate must fix the HoTT configuration, the real/programmatic task, the abstraction and the downstream operation; "
            "the key step must genuinely involve UA/Id/HIT/Pi or truncation, and the candidate must aim at E6 (a natural consumer that upgrades a weaker qualification). "
            "Do not rename the existing R036/R038/R034/race-timeout counterexamples; record failed or non-natural candidates with reopen conditions."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(110, 118)],
        "final_run": {
            "run_id": RUN_ID,
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "older_proofs_after_matrix_growth": {
            rid: "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH"
            for rid in (
                "20260912-MP-ERCF-001-02", "20260912-MP-ERCF-TRUNC-001-01",
                "20260912-MP-RACE-TIMEOUT-001-01", "20260912-MP-CONTEXTUAL-EQUIV-001-01",
                "20260912-MP-QUOTIENT-MONAD-001-01", "20260912-MP-CONTEXT-CHARACTERIZATION-001-01",
                "20260912-MP-GUARD-ERASURE-001-01", "20260912-MP-COST-FACTORIZATION-001-01",
                "20260912-MP-PATH-CERTIFICATE-001-01", "20260912-MP-ONLINE-CAUSALITY-001-01",
            )
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 45",
            "projection freshness PASS",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 45",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS",
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
            "This in-scope checkpoint records the native Cubical transition-lift package MP-TRANSITION-LIFT-001 (C-110–C-117), "
            "repairs the source hashes changed by the claim-matrix growth, closes the R036/R038 core with scope, and routes the N4 new-candidate generation. "
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
        "revision": 45,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
