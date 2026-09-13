#!/usr/bin/env python3
"""Prepare revision 31 for the native Cubical Agda truncation-defense result."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE"
RESULT_ID = "A-ERCF-TRUNCATION-DEFENSE-001"
PARENT_RESULT = "A-ERCF-FACTORIZATION-FORMAL-001"
RESEARCH_PARENT = "A-HOTT-SELF-VALIDATION-ECONOMY-001"
PROOF_GATE = "A-MATH-PROOF-DELIVERY-GATE-001"
C4 = "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md"
SOURCE = "HoTT/formal/ercf-truncation-defense/TruncationDefense.agda"
SOURCE_README = "HoTT/formal/ercf-truncation-defense/README.md"
TOOLCHAIN = "HoTT/formal/ercf-truncation-defense/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/ercf-truncation-defense/AGDA_LIBRARIES"
RUN_DIR = "HoTT/verification/runs/20260912-MP-ERCF-TRUNC-001-01"
RUN_JSON = f"{RUN_DIR}/RUN.json"
SOURCE_MANIFEST = f"{RUN_DIR}/source-manifest.json"
INDEX_ROWS = f"{RUN_DIR}/index-row-manifest.json"
OLD_INDEX_ROWS = "HoTT/verification/runs/20260912-MP-ERCF-001-02/index-row-manifest.json"
INDEX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
EVIDENCE = "audit/ERCF-截断防御机器证明实施证据-20260912.md"
CAPTURE = "scripts/audit/capture_agda_proof_run.py"
FREEZE = "scripts/audit/freeze_proof_index_rows.py"
VERIFIER = "scripts/audit/verify_formal_proof_run.py"

EXPECTED = {
    C4: "a1510b9335237bf5c94cbfc28ecc739921863419dc9ecd21a4902e1213e89fb1",
    SOURCE: "f56e97ed93d42ecfaddadc815215c0ad35386389a4b51a265df2edb34156bfa9",
    TOOLCHAIN: "f1810deb16e72d55e8efb0e8316d8ae494eb0acb3867d4f4b103fab63f43e8c2",
    LIBRARIES: "3dc9309430a79c1764bd9a86d29b96a7f7907f8f6f5638207a9cc4f809591c12",
    SOURCE_README: "14ff576cac8bb9490f6482e11dbe6e619aafabb6d70fab2ee624149c04e8e336",
    RUN_JSON: "cf42ef44c1674b6607e992ca9911ac0f0ddb9d63ea9ad62c4cbd4efefcf35376",
    SOURCE_MANIFEST: "747b624f4c62bc0fb16e265ae3f85dedd04d60e58d0fd43700adbc5d416276e1",
    INDEX_ROWS: "865105e8bdfc4cec69a146b8f292f0144d15d4653639c6c930c0a8844eeac917",
    OLD_INDEX_ROWS: "f5dfc378577fa294eb0f4d40462a72cb4fed18d5147f75b89ae51e84b567add9",
    INDEX: "821660749c3a3e13659e0b34753e050f62a9aac4d82db3e4c60fa9ddd08f395b",
    EVIDENCE: "5d5460d374faa9a45b1670b837c412eedaca73b9ef2bc63afcb37c4f632ee888",
    CAPTURE: "7f5dcc8b9343665e554a2d3e7e8a568add1401227d0998a5066ec15cddff43d2",
    FREEZE: "5cf036b0956bb97e9e4a30bab1135823484d60a9d8980a10eb0bbeb16ed10ace",
    VERIFIER: "7dfa8bc7adaa0b3f86f415dcf369c79be409f41e7a0c171bb063fc4102864d17",
}

SPEC = importlib.util.spec_from_file_location("runtime_ercf_truncation", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def replace_line_prefix(text: str, prefix: str, replacement: str) -> str:
    lines = text.splitlines()
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) != 1:
        raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(indexes)}")
    lines[indexes[0]] = replacement
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def append_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def build_direction(root: Path) -> str:
    body = (root / R.DIRECTION).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-direction-portfolio/v1.5", "integrated-direction-portfolio/v1.6")
    body = replace_once(body, "integrated-direction-portfolio:v1.5", "integrated-direction-portfolio:v1.6")
    old_semantic = "CORE_GENERATION_4_ERCF_FACTORIZATION_MACHINE_PROVED_LOCAL_NATIVE_OPEN"
    new_semantic = "CORE_GENERATION_4_NATIVE_TRUNCATION_DEFENSE_PROVED_PARTIALITY_QUOTIENT_NEXT"
    body = body.replace(old_semantic, new_semantic)
    body = replace_once(body, "source_state_revision: 30", "source_state_revision: 31")
    body = replace_once(body, "projection_generation: 20260912-direction-014", "projection_generation: 20260912-direction-015")
    body = replace_line_prefix(
        body,
        "| `DIR-G-MATH-PROOF-DELIVERY-GATE`",
        "| `DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 AI 的数学结论在交付前必须由匹配语义的 proof assistant/kernel 机器证明；源码、实际 run 与索引全部留在 repo，`/tmp` 不得成为唯一证据位置 | 用户 ruling §15 / F-011 | `ACTIVE_USER_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-MATH-PROOF-DELIVERY-GATE`、`OUT-TOP-ERCF-FACTORIZATION-LEAN`、`OUT-TOP-ERCF-TRUNCATION-DEFENSE` | Lean 与原生 Cubical Agda 两条 package 已贯通；逐行索引 manifest 保护旧 proof 免受 append-only matrix 演进误伤；后续仍逐 claim 执行 source→run→index | `AGENTS.md`；数学证明规范；两份 ERCF evidence；两个 final run |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-TOP-QUALIFICATION-PRESERVATION`",
        "| `DIR-TOP-QUALIFICATION-PRESERVATION` | ASK／完成资格在 HoTT 抽象、组合、提取与反射中的保持性；统一 A/B 两类现实相对悖论 | 用户 generation-4 core；当前 AI C3/C4 综合 | `NEXT_CANDIDATE` | `COMPUTATIONAL_LEGITIMACY`, `TIME_AND_TEMPORALITY`, `SELF_REFERENCE`, `PARADOX_DISCOVERY` | `OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`、`OUT-TOP-ERCF-FACTORIZATION-LEAN`、`OUT-TOP-ERCF-TRUNCATION-DEFENSE`、`OUT-W-R041-PAPER` | truncation 的第一原生判别为 `DEFENSE_WORKS`；下一步在 Cubical set quotient/QIIT 上证明 bind 同余与 race/timeout 非同余，再核自然 consumer 是否发生资格提升 | C3；C4；`HoTT/formal/ercf-truncation-defense/`；R041 proof note |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`",
        "| `DIR-U-THEORY-ECONOMY-SELF-VALIDATION` | 理论通过遗忘现实因素取得经济收益后，是否在内部证明其抽象、真理验证器和自身可靠性时形成不可停机、部分性或元层上升；同时审计最小理论覆盖和存在/不存在双视角 | 用户直接新增方向 `KC-000028`–`KC-000036` | `ACTIVE_USER_DIRECTION` | `THEORY_ECONOMY`, `SELF_VALIDATION`, `SELF_REFERENCE`, `ABSTRACTION_AND_NEGATION`, `EXISTENCE_NEGATION_DUALITY` | `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`、`OUT-TOP-ERCF-FACTORIZATION-LEAN`、`OUT-TOP-ERCF-TRUNCATION-DEFENSE` | 命题截断表明 HoTT 可把经济收益与 ASK 防线同时编码；下一步寻找 partiality quotient 的完成先后 consumer，只有自然升级桥梁成立才进入 ERCF-3 | `核心认知.md` KC-000028–000036；C4；两个 ERCF proof packages |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-U-B-EFFECTIVE-DELIVERY`",
        "| `DIR-U-B-EFFECTIVE-DELIVERY` | 数学上取得分类/存在后被提升为尚未取得的有效求解或实际交付 | 用户原始方向；WebGPT `U-DUAL-DIRECTION-JSON-001` | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `BEING_AND_BECOMING`, `EVIDENCE_DISCIPLINE` | `OUT-L-CORE-MATHEMATICAL`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-W-RP-B01`、`OUT-TOP-ERCF-TRUNCATION-DEFENSE` | 截断原生证明排除“mere existence 自动给原 witness”；现在转向结果商是否在自然使用中被提升为可观察完成先后的 race 能力 | core；RP-B01；C3/C4；`TruncationDefense.agda` |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-W-RACE-TIMEOUT`",
        "| `DIR-W-RACE-TIMEOUT` | 部分计算结果等价的操作闭包：代表层 `bind` 相容、`race/timeout` 时序敏感，以及商/QIIT continuation 与 contextual equivalence 的边界 | WebGPT R039；数学 R041 PROOF_NOTE；当前 Cubical toolchain | `NEXT_CANDIDATE` | `TIME_AND_TEMPORALITY`, `COMPUTATIONAL_LEGITIMACY`, `PARADOX_DISCOVERY` | `OUT-W-R039`、`OUT-W-R041-PAPER`、`OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-ERCF-TRUNCATION-DEFENSE` | 复用已资格化 Agda 2.8.0/Cubical v0.9：固定最小 partial computation/result equivalence/set quotient，机器证明 bind 正例、race 负例，再审计实际 consumer；不再停留于 R041 纸笔自述 | R041 proof note；C3/C4；Cubical toolchain manifest |",
    )
    old_priority = """1. **当前用户主方向**：`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` × `DIR-L-SELF-REFLECTION`。把理论经济、任务相对充分性与反射认证义务推进为 HoTT 原生、可证伪构造。
2. **总方向建议（AI 统筹，尚非用户单独裁定）**：`DIR-TOP-QUALIFICATION-PRESERVATION`，以 ASK／完成资格在抽象、组合、提取和反射中的保持性统一 A/B 与 ERCF。
3. **已闭合的基础切片**：`MP-ERCF-001`/`C-59`–`C-66` 机器证明通用 factorization walking skeleton；它排除了把 E₀ 本身当作 HoTT coverage gap 的路径，不再重复这一通用投影模型。
4. **下一最小 HoTT 原生判别**：固定 propositional truncation 或 quotient/HIT 的真实 checker/规则，先证明受保护 consumer 正例，再检验一个自然的 witness/时序/代表元 consumer；正确拒绝记为 `DEFENSE_WORKS`。
5. **战略自反深化**：`DIR-W-RP-B01` × ERCF-3。只在原生信息经济接口闭合后，定位数学分类→统一有效交付→有效自我 ASK→自我可靠性认证的资格升级点。
6. **操作对照包**：`DIR-W-RACE-TIMEOUT`。从 R041 的 bind/race 分离推进真实 partiality quotient/QIIT，作为“局部操作不变性不等于全局上下文充分性”的独立证据。
7. **探索与证据队列**：完整流函数/在线因果、guard 擦除、同函数异时、R034 Cubical Agda，以及 R041 执行谱系、2,396 条历史 claim、aistudio coverage，均按与当前 native consumer 的判别关系调度。"""
    new_priority = """1. **当前用户主方向**：`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` × `DIR-L-SELF-REFLECTION`。把理论经济、资格保持与反射推进为 HoTT 原生、可证伪构造。
2. **总方向建议（AI 统筹）**：`DIR-TOP-QUALIFICATION-PRESERVATION`，统一 A/B 与 ERCF，但不把防御结果包装成目标完成。
3. **已闭合基础**：`MP-ERCF-001` 机器证明通用 factorization；`MP-ERCF-TRUNC-001` 原生证明 truncation 正向 consumer 与 point-preserving witness extraction no-go，判 `DEFENSE_WORKS`。
4. **当前第一工作包**：`DIR-W-RACE-TIMEOUT`。用已资格化 Cubical toolchain 形式化 partiality result quotient/QIIT，成对证明 bind 同余正例和 race/timeout 非同余负例。
5. **自然桥梁 Gate**：查明实际 HoTT consumer 是否把结果商提升成含完成先后的交付能力；没有桥梁就停在 `DEFENSE_WORKS/REPRESENTATION_BOUNDARY`。
6. **战略自反深化**：`DIR-W-RP-B01` × ERCF-3 继续等待自然 consumer；不以一般 Gödel 口号提前启动。
7. **探索与证据队列**：在线因果、guard 擦除、同函数异时、R034，以及 R041 执行谱系、历史 claim/aistudio coverage，按对当前 consumer 的判别价值调度。"""
    body = replace_once(body, old_priority, new_priority)
    body = replace_once(
        body,
        "C4 整体仍是 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`：只有 `MP-ERCF-001`/`C-59`–`C-66` 达到 `MACHINE_PROVED_LOCAL_UNCOMMITTED`，没有 HoTT 原生 abstraction/consumer、具体非停机轨迹或 ERCF-3。后续数学单元继续按 F-011 建立 source/run/index 链。",
        "C4 整体仍是 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE`：C-59–C-66 与 C-67–C-70 分别机器闭合，但截断结论是 `DEFENSE_WORKS`；现实桥梁、partiality natural consumer、具体非停机与 ERCF-3 仍开放。",
    )
    return body


def build_panorama(root: Path) -> str:
    body = (root / R.PANORAMA).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-outcome-panorama/v1.5", "integrated-outcome-panorama/v1.6")
    body = replace_once(body, "integrated-outcome-panorama:v1.5", "integrated-outcome-panorama:v1.6")
    body = body.replace(
        "CORE_GENERATION_4_ERCF_FACTORIZATION_MACHINE_PROVED_LOCAL_NATIVE_OPEN",
        "CORE_GENERATION_4_NATIVE_TRUNCATION_DEFENSE_PROVED_PARTIALITY_QUOTIENT_NEXT",
    )
    body = replace_once(body, "source_state_revision: 30", "source_state_revision: 31")
    body = replace_once(body, "projection_generation: 20260912-outcome-014", "projection_generation: 20260912-outcome-015")
    body = replace_line_prefix(
        body,
        "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE`",
        "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE` | F-011 source/run/index 门禁与 repo 内留存 | `DIR-G-MATH-PROOF-DELIVERY-GATE` | 用户裁定与本地治理 | `VERIFIED_WITH_SCOPE` | Lean 通用与 Cubical Agda 原生两种 package 均通过 kernel/dependency/index/exact replay；逐行 index manifest 支持 append-only 索引演进 | 不证明 fresh 模型永久遵循，不把 `DEFENSE_WORKS` 外推成悖论；未 commit/tag | 数学证明规范；两个 final run；两份 ERCF evidence；proof verifier |",
    )
    native_row = (
        "| `OUT-TOP-ERCF-TRUNCATION-DEFENSE` | `MP-ERCF-TRUNC-001`：Cubical propositional truncation 的 proposition recursor、二重截断压平、Bool 输出恒定性和 point-preserving extraction no-go（C-67–C-70） | "
        "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-W-RACE-TIMEOUT`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前原生 Cubical Agda 形式化 | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS` | Agda 2.8.0 + Cubical v0.9、`--safe --cubical --ignore-interfaces`、官方 release/tree hashes、exit 0、exact replay；截断允许 proposition consumer 并阻断逐点恢复 Bool witness | "
        "不证明 HoTT 内部矛盾、现实相对悖论、所有 choice/所有 `∥A∥→A` 不存在、非停机或 ERCF-3 | `HoTT/formal/ercf-truncation-defense/TruncationDefense.agda`；final run；claim matrix；`audit/ERCF-截断防御机器证明实施证据-20260912.md` |"
    )
    lean_prefix = "| `OUT-TOP-ERCF-FACTORIZATION-LEAN`"
    lines = body.splitlines()
    positions = [i for i, line in enumerate(lines) if line.startswith(lean_prefix)]
    if len(positions) != 1:
        raise ValueError(f"LEAN_OUTCOME_COUNT:{len(positions)}")
    lines.insert(positions[0] + 1, native_row)
    body = "\n".join(lines) + ("\n" if body.endswith("\n") else "")
    body = replace_line_prefix(
        body,
        "| `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`",
        "| `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY` | C4 的 V1–V5、ERCF、存在/不存在与覆盖边界综合 | `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-TOP-QUALIFICATION-PRESERVATION` | 用户原文 + 当前 AI 综合 | `PAPER_ONLY` | 通用 factorization 与原生 truncation defense 已分离为两个机器结果；截断实例显示 HoTT 在此处执行 ASK 防御 | 不证明自然现实失配、任意实现死循环、coverage no-go 或 ERCF-3 | C4；两个 ERCF evidence；核心认知 KC-000028–000036 |",
    )
    body = replace_line_prefix(
        body,
        "| `OUT-TOP-THREE-WAY-SKELETON`",
        "| `OUT-TOP-THREE-WAY-SKELETON` | generation-4 + LOAD_SET/runtime v3 + STATE v2 的跨 Session 认知骨架 | `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-E-WEB-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION` | 当前顶层治理 | `VERIFIED_WITH_SCOPE` | core/runtime/reader/three-way/fresh 按当前 generation 核验；两类 proof package 可由 stable record 水合 | fresh 模型行为、2,396 条历史语义、C4 未机器化余项和 Git version-close 仍开放 | generation-4 evidence；fresh receipt；`.codex/` |",
    )
    body = replace_once(
        body,
        "6. C3 是证据受限的 AI 研究战略；`MP-ERCF-001` 已闭合 ERCF-1/2 的通用因子化子核，但真实 HoTT truncation/quotient/HIT consumer、B01-TARGET、有效自我 ASK、具体发散 witness、最小 HoTT coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "6. C3 是证据受限的 AI 研究战略；通用 factorization 与原生 truncation defense 已机器闭合，后者判 `DEFENSE_WORKS`。真实 partiality quotient/QIIT 的 bind/race operation closure、自然 consumer、B01-TARGET、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )
    return body


def build_memory(root: Path) -> str:
    body = (root / "MEMORY.md").read_text(encoding="utf-8")
    old_queue = """1. `MP-ERCF-001` 已完成 F-011 生效后的首个真实 proof package：`C-59`–`C-66` 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`；下一轮不得重复通用 E₀ 投影模型。
2. 当前数学主方向仍是 HoTT 自反真理验证/理论经济；下一最小结果改为一个 HoTT 原生 truncation 或 quotient/HIT abstraction，先证明受保护 consumer，再检验自然负向 consumer。
3. C4 整体保持 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`；只有通用子核升级，HoTT 特定 coverage/self-reflection/ERCF-3 均未证明。
4. C3 的资格保持性、W51×RP-B01、自指与 R041 partiality 对照继续在全局视野；进入任何数学结论前仍逐 claim 执行 F-011。"""
    new_queue = """1. `MP-ERCF-TRUNC-001` 已完成首个 HoTT 原生信息经济判别：C-67–C-70 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS`；命题截断正确阻断逐点 witness 恢复，不是悖论。
2. 当前第一数学工作包转为 `DIR-W-RACE-TIMEOUT`：在 Agda 2.8.0/Cubical v0.9 中形式化 partiality result quotient/QIIT，成对证明 bind 同余与 race/timeout 非同余，再核自然 consumer。
3. C4 整体为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE`；现实桥梁、自反/ERCF-3 和 HoTT 悖论仍未证明。
4. W51×RP-B01、自指、guard/在线因果和 R034 继续在全局视野；任何新数学结论仍逐 claim 执行 F-011。"""
    body = replace_once(body, old_queue, new_queue)
    body = replace_once(
        body,
        "- C4 当前共 755 行，SHA-256 `6cc6ce029f9a0516a5a0fc769ab65623a26f6edbb09a706484779814a6f446ec`；整体为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`。它将验证任务分五层，并把 `MP-ERCF-001`/`C-59`–`C-66` 的通用机器证明与 HoTT 原生未决边界分开。",
        "- C4 当前共 773 行，SHA-256 `a1510b9335237bf5c94cbfc28ecc739921863419dc9ecd21a4902e1213e89fb1`；整体为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE`，明确区分两组机器子结果与现实/反射未决。",
    )
    proof_anchor = "- `MP-ERCF-001` 是 F-011 下首个真实数学 package：Lean 4.33.1 final run/index/hash/exact replay PASS；源码和运行原件均在 repo；未提交，且只证明一般 `Type` 值因子化。"
    body = replace_once(
        body,
        proof_anchor,
        proof_anchor + "\n- `MP-ERCF-TRUNC-001` 是首个原生 Cubical package：Agda 2.8.0/Cubical v0.9 final run、5 类外部依赖 hash、index row manifest 和 exact replay PASS；判词 `DEFENSE_WORKS`。",
    )
    body = replace_once(
        body,
        "- 本轮 core/curation/transition、C4、方向/全景和治理机制可机器检查；C4 的通用 factorization 子核有 `MP-ERCF-001` proof-assistant 证明，但 C4 的 HoTT 特定、自反与具体发散主张仍无机器证明/运行轨迹。",
        "- C4 的通用 factorization 子核和原生 truncation defense 分别有 Lean/Cubical Agda proof package；截断结果是理论防御，不是现实失配。C4 的 partiality natural consumer、自反与具体发散仍无机器证明/运行轨迹。",
    )
    body = replace_once(
        body,
        "当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001` 与 `A-ERCF-FACTORIZATION-FORMAL-001` 并读 C4/proof package。ERCF-1/2 通用正反对照已完成；不要直接跳到 ERCF-3，先固定一个 HoTT 原生 truncation 或 quotient/HIT 接口及自然 consumer。",
        "当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001`、`A-ERCF-FACTORIZATION-FORMAL-001`、`A-ERCF-TRUNCATION-DEFENSE-001`。truncation Gate 已闭合为防御；下一步 query `DIR-W-RACE-TIMEOUT` 相关来源并形式化 quotient/QIIT operation closure，不直接跳 ERCF-3。",
    )
    return body


def build_frontier() -> str:
    return """# HoTT 研究前沿（S031 原生命题截断防御）

本文件是注意力槽，不是数学结论数据库。`MP-ERCF-TRUNC-001` 以原生 Cubical Agda 把命题截断候选判为 `DEFENSE_WORKS`；它不是 HoTT 悖论。所有新结论继续执行 F-011。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 当前用户主方向 | ERCF：理论经济与资格/反射边界 | active-user-direction / mixed-paper-and-two-formal-subresults | 保持 V1–V5；把防御与现实失配分开 |
| 已闭合通用基础 | `MP-ERCF-001` factorization C-59–C-66 | machine-proved-local-uncommitted / general | 不再重复任意 E₀ |
| 已闭合原生防御 | `MP-ERCF-TRUNC-001` C-67–C-70 | machine-proved-local-uncommitted / DEFENSE_WORKS | truncation 允许 proposition consumer，拒绝 point-preserving Bool extraction；不重开同一指控 |
| 第一工作包 | Cubical partiality result quotient/QIIT 的 bind×race/timeout | next-candidate / R041-paper-plus-native-toolchain-ready | 固定最小类型、结果等价和商；机器证明 bind 同余、race 非同余；再核自然 consumer |
| 战略自反深化 | ERCF-3 × W51/RP-B01 | blocked-on-natural-consumer-and-exact-calculus | 只有资格提升桥梁成立才构造 diagonal |
| 对照支线 | guard/online causality、同函数异时、R034 | retained | 用于反驳过强外推与选择下一 consumer |

判词顺序不变：`DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`。当前只达到第一类。
"""


def build_resume(root: Path) -> str:
    body = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    start = "## 当前停止点\n\n"
    before, sep, _ = body.partition(start)
    if not sep:
        raise ValueError("RESUME_STOP_MARKER_MISSING")
    stop = """S031 已完成第一个 HoTT 原生信息经济判别。`MP-ERCF-TRUNC-001` 在 Agda 2.8.0/Cubical v0.9 的 native Path+squash-HIT 下机器证明 C-67–C-70；final run、官方 release/tree hash、stdout/stderr、环境、索引和 exact replay 均在 repo。当前未 commit，状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

判词是 `DEFENSE_WORKS`，不是 HoTT 悖论：命题截断允许 proposition-valued consumer 和二重截断压平；任意 `∥Bool∥₁→Bool` 对两个 canonical point 输出 path-equal，因此逐点恢复原 Bool witness 的合同不可能。HoTT 在这里没有绕过 ASK，而是阻断了资格提升。

工具链已资格化并外置到 D 盘。失败谱系包括错误 source path、未加载 library flags、混合 option cache 和缺 infective `--guardedness`；均保留且未被冒充数学拒绝。claim matrix 追加还触发 index-row manifest 修复，使旧 Lean proof 在索引演进后继续逐行验证。

下一步转到 `DIR-W-RACE-TIMEOUT`：用同一 Cubical toolchain 形式化 partiality result quotient/QIIT 的 bind 同余正例与 race/timeout 非同余负例，再寻找实际 consumer 的自然资格提升桥梁。没有桥梁就保持 `DEFENSE_WORKS/REPRESENTATION_BOUNDARY`，不进入 ERCF-3。
"""
    return before + start + stop


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000013": ("DEEPENED", "命题截断把 ASK 具体落实为消去目标的 h-level 资格；unsafe witness consumer 被原生规则阻断。"),
        "KC-000015": ("DEEPENED", "抽象确实遗忘 witness 差异，但本轮显示遗忘不自动制造悖论：理论可明确限制 consumer。"),
        "KC-000018": ("DEEPENED", "理论经济收益与安全成本同时可见：squash 简化存在信息，消去/路径约束支付防御成本。"),
        "KC-000021": ("ALIGNED", "使用 Agda 2.8.0/Cubical v0.9 原生 checker 实际运行，并把 source/run/dependency/index 全部留存。"),
        "KC-000022": ("DEEPENED", "原生截断判别没有找到 A/B 悖论，而是证明 B 类的直接 witness 提升被正确拒绝。"),
        "KC-000024": ("DEEPENED", "非平凡 consumer 的时序/完成观察必须先通过商/截断的合法消去或同余 Gate；当前截断 Gate 返回拒绝。"),
        "KC-000029": ("DEEPENED", "命题截断是明确的理论经济样本：保留 inhabitance、删除 witness 身份，并以规则限定可用收益。"),
        "KC-000030": ("DEEPENED", "HoTT 的一项理论经济已由原生 HIT、受保护 recursor 和失败 consumer 具体化。"),
        "KC-000031": ("CORRECTED", "HoTT 对 point-preserving untruncation 的严格拒绝在本实例中是可机器证明的防御，不是范型覆盖失败。"),
        "KC-000034": ("DEEPENED", "witness 差异在截断中被同一化，但该缺席没有被对象语言冒充 `¬A`；存在/不存在视角继续分层。"),
        "KC-000035": ("DEEPENED", "本项目的‘抽象—consumer—资格’骨架已进入原生 HoTT HIT；完整现实桥梁仍未表达。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    for unit in manifest["units"]:
        unit_id = str(unit["id"])
        relation, assessment = touched.get(unit_id, ("NOT_TOUCHED", "本轮只审查原生命题截断的 consumer 资格；该用户原文及既有判断不变。"))
        counts[relation] = counts.get(relation, 0) + 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | TruncationDefense.agda；final run；audit/ERCF-截断防御机器证明实施证据-20260912.md；核心认知.md {unit_id} | partiality quotient natural consumer 与 ERCF-3 仍开放。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — 没有新的用户原文；generation-4/36 KC 不变。",
        "- direction_change: `YES` — truncation 原生候选关闭为 `DEFENSE_WORKS`；第一工作包转到 partiality quotient/QIIT bind×race。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-ERCF-TRUNCATION-DEFENSE`，更新 F-011 与 C4 分层。",
        "- update_decision: `proof source/toolchain/run/index/evidence/C4/README/Feature/manifests/STATE/MEMORY/FRONTIER/LESSONS/RESUME 更新；core 不改。`",
        "- cross_conflicts: `NONE_AFTER_DEFENSE_CLASSIFICATION` — 原生规则拒绝 unsafe consumer 与用户 ASK 航向一致，但不冒充悖论。",
        "- unresolved: `partiality quotient 的 operation closure 与自然 consumer 桥梁；ERCF-3 暂缓。`",
        "", "## 汇总", "",
        f"`ALIGNED={counts.get('ALIGNED', 0)} / DEEPENED={counts.get('DEEPENED', 0)} / CORRECTED={counts.get('CORRECTED', 0)} / NOT_TOUCHED={counts.get('NOT_TOUCHED', 0)}`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 30 or state.get("latest_session") != "S-GOV-20260912-030-ERCF-DEPENDENCY-SEMANTICS-ALIGNMENT":
        raise SystemExit("EXPECTED_REVISION_30_S030")
    for relative, expected_hash in EXPECTED.items():
        if R.sha((root / relative).read_bytes()) != expected_hash:
            raise SystemExit(f"PRECONDITION_HASH_MISMATCH:{relative}")
    run = json.loads((root / RUN_JSON).read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX" or run.get("exit_code") != 0:
        raise SystemExit("NATIVE_RUN_NOT_ACCEPTED_AND_INDEXED")

    direction = build_direction(root)
    panorama = build_panorama(root)
    memory = build_memory(root)
    frontier = build_frontier()
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    additions = [
        "37. 原生 propositional truncation 证明显示理论经济与 ASK 防御可同时存在：向 mere proposition 的 consumer 合法，point-preserving Bool witness extraction 因 squash path 不可能。正确拒绝是 `DEFENSE_WORKS`，不能为了目标把它改名成悖论。",
        "38. Cubical checker 的证据身份包含 library infective options 与 XDG cache generation；错误 source path、漏 library flags、混合 option cache 和缺 `--guardedness` 是四类不同失败。先按责任点修复再重跑，不能改命题求绿。",
        "39. 不断增长的 claim matrix 不能以 whole-file hash 永久绑定每个旧 run。先冻结 proof/claim 精确行 hash；未来 append 时逐行保持，改写旧行仍 fail closed，才兼顾不可覆盖证据与可增长索引。",
    ]
    for addition in additions:
        if addition.split(". ", 1)[1][:25] not in lessons:
            lessons += "\n" + addition
    lessons += "\n"
    resume = build_resume(root)

    semantic = "CORE_GENERATION_4_NATIVE_TRUNCATION_DEFENSE_PROVED_PARTIALITY_QUOTIENT_NEXT"
    state["revision"] = 31
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "NATIVE_TRUNCATION_DEFENSE_MACHINE_PROVED_PARTIALITY_QUOTIENT_NEXT",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, formalize a minimal partial-computation result quotient or QIIT; prove bind congruence and race/timeout noncongruence, then audit whether a natural HoTT consumer promotes quotient data to timing-sensitive delivery.",
    })
    state["projection"]["status"] = semantic
    drec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    drec.update({"projection_generation": "20260912-direction-015", "semantic_status": semantic, "scope": "Portfolio after native Cubical truncation returned DEFENSE_WORKS; current first package is partiality quotient/QIIT bind-versus-race plus a natural-consumer bridge."})
    prec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    prec.update({"projection_generation": "20260912-outcome-015", "semantic_status": semantic, "scope": "Panorama includes native Cubical truncation C-67 through C-70 as machine-proved defense, while the HoTT paradox and natural timing consumer remain open."})
    for record in (drec, prec):
        for path in (SOURCE, RUN_JSON, EVIDENCE):
            append_unique(record["full_sources"], path)

    revalidation = "C4 was reread after S031 added machine-proved native Cubical truncation C-67 through C-70 as DEFENSE_WORKS and moved the next target to partiality quotient/QIIT; historical checkpoints preserve earlier text."
    for record in state["records"].values():
        hashes = record.get("source_hashes")
        if isinstance(hashes, dict):
            if C4 in hashes:
                hashes[C4] = EXPECTED[C4]
                record["revalidation"] = revalidation
            if INDEX in hashes:
                hashes[INDEX] = EXPECTED[INDEX]
                record["revalidation"] = (str(record.get("revalidation", "")) + " Claim-matrix evolution was checked by stable proof/claim row manifests; no previously indexed claim row changed.").strip()
            if VERIFIER in hashes:
                hashes[VERIFIER] = EXPECTED[VERIFIER]

    old_result = state["records"][PARENT_RESULT]
    for path in (OLD_INDEX_ROWS, FREEZE):
        append_unique(old_result["full_sources"], path)
    old_result["source_hashes"].update({INDEX: EXPECTED[INDEX], VERIFIER: EXPECTED[VERIFIER], OLD_INDEX_ROWS: EXPECTED[OLD_INDEX_ROWS]})
    old_result["revalidation"] = "After C-67 through C-70 were appended, the old Lean proof passed ROW_STABLE_AFTER_INDEX_EVOLUTION and exact replay; its proof/claim lines are frozen in index-row-manifest.json."

    hott = state["records"][RESEARCH_PARENT]
    hott.update({
        "evidence_status": "PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_AND_NATIVE_DEFENSE_SUBRESULTS",
        "mathematical_status": "GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE_PROVED_NATURAL_CONSUMER_REFLECTION_OPEN",
        "scope": "C4 separates V1-V5 and ERCF. General factorization C-59 through C-66 and native Cubical truncation defense C-67 through C-70 are machine-proved; partiality natural consumer, reality bridge, divergence, coverage no-go and ERCF-3 remain open.",
        "revalidation": revalidation,
    })
    for path in (SOURCE, SOURCE_README, TOOLCHAIN, RUN_JSON, INDEX_ROWS, EVIDENCE):
        append_unique(hott["full_sources"], path)
    hott["source_hashes"].update({C4: EXPECTED[C4], SOURCE: EXPECTED[SOURCE], RUN_JSON: EXPECTED[RUN_JSON], INDEX: EXPECTED[INDEX]})

    gate = state["records"][PROOF_GATE]
    for path in (CAPTURE, FREEZE, SOURCE, TOOLCHAIN, LIBRARIES, RUN_JSON, SOURCE_MANIFEST, INDEX_ROWS, OLD_INDEX_ROWS, EVIDENCE):
        append_unique(gate["full_sources"], path)
    gate["source_hashes"].update({
        INDEX: EXPECTED[INDEX], VERIFIER: EXPECTED[VERIFIER], CAPTURE: EXPECTED[CAPTURE], FREEZE: EXPECTED[FREEZE],
        SOURCE: EXPECTED[SOURCE], TOOLCHAIN: EXPECTED[TOOLCHAIN], LIBRARIES: EXPECTED[LIBRARIES], RUN_JSON: EXPECTED[RUN_JSON],
        "HoTT/formal/README.md": "f0af95cef2821255758e0f2c07e3cf134be1e3f739e7becd1e669b631fd0a4b1",
        "HoTT/verification/runs/README.md": "a3dd7871007895efe98bfa128496af7015562ee56f3585f8a9959b7581467bde",
    })
    gate["revalidation"] = "MP-ERCF-TRUNC-001 exercised native Cubical source/run/external-dependency/index/exact-replay verification. Row manifests now preserve old claims across append-only index evolution; fresh-model compliance remains NOT_RUN."
    gate["scope"] = "Require machine proof source/run/index before delivery. Both Lean and native Cubical Agda packages now pass; external toolchains are publisher/hash pinned and old index rows remain immutable. Fresh-model behavior and Git version closure remain open."

    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "mathematical_status": "NATIVE_CUBICAL_TRUNCATION_DEFENSE_NOT_PARADOX",
        "depends_on": [PROOF_GATE],
        "research_parent": RESEARCH_PARENT,
        "proof_id": "MP-ERCF-TRUNC-001",
        "claim_ids": [f"C-{n}" for n in range(67, 71)],
        "run_id": "20260912-MP-ERCF-TRUNC-001-01",
        "classification": "DEFENSE_WORKS",
        "full_sources": [SOURCE, SOURCE_README, TOOLCHAIN, LIBRARIES, RUN_JSON, SOURCE_MANIFEST, f"{RUN_DIR}/stdout.txt", f"{RUN_DIR}/environment.txt", INDEX_ROWS, INDEX, CAPTURE, FREEZE, VERIFIER, EVIDENCE, C4],
        "source_hashes": {SOURCE: EXPECTED[SOURCE], SOURCE_README: EXPECTED[SOURCE_README], TOOLCHAIN: EXPECTED[TOOLCHAIN], LIBRARIES: EXPECTED[LIBRARIES], RUN_JSON: EXPECTED[RUN_JSON], SOURCE_MANIFEST: EXPECTED[SOURCE_MANIFEST], INDEX_ROWS: EXPECTED[INDEX_ROWS], INDEX: EXPECTED[INDEX], VERIFIER: EXPECTED[VERIFIER], EVIDENCE: EXPECTED[EVIDENCE], C4: EXPECTED[C4]},
        "scope": "Agda 2.8.0/Cubical v0.9 native Path and squash-HIT prove proposition-valued elimination, truncation flattening, Bool-output constancy and no point-preserving Bool extraction. This is a defense result, not a HoTT paradox or reality bridge.",
        "resolution": {
            "evidence": [RUN_JSON, SOURCE_MANIFEST, f"{RUN_DIR}/stdout.txt", INDEX_ROWS, INDEX, VERIFIER, EVIDENCE],
            "reason": "Final native Cubical run exited 0; repo sources, official release assets, binary and 1111-file source tree hashes match; index rows and exact replay pass. Git version closure is not authorized.",
        },
    }

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete", "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-030-ERCF-DEPENDENCY-SEMANTICS-ALIGNMENT", RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, SOURCE, TOOLCHAIN, RUN_JSON, INDEX, VERIFIER, EVIDENCE, C4, "scripts/audit/prepare_ercf_truncation_checkpoint.py"],
        "source_hashes": {SOURCE: EXPECTED[SOURCE], RUN_JSON: EXPECTED[RUN_JSON], INDEX: EXPECTED[INDEX], C4: EXPECTED[C4]},
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_NATIVE_TRUNCATION_DEFENSE_HOTT_PARADOX_OPEN",
        "cognition_status": "NATIVE_TRUNCATION_DEFENSE_PROVED_AND_PARTIALITY_QUOTIENT_NEXT_ROUTED",
        "scope": "Qualify a native Cubical toolchain, prove the truncation consumer defense, preserve all failure/evidence boundaries, update the trio and audit all 36 KC.",
    }
    session = f"""# {SESSION_ID}

- 目标：把通用 ERCF factorization 推进到第一个真正使用 HoTT native Path/HIT 的信息经济接口。
- 工具链：Agda 2.8.0/Cubical v0.9；官方 release SHA、binary SHA、tag/tree SHA、D 盘 XDG/TMP 全部固定。
- 证明：`MP-ERCF-TRUNC-001`/C-67–C-70；proposition recursor、二重截断压平、Bool 输出恒定、point-preserving extraction no-go。
- 判词：`DEFENSE_WORKS`。系统阻断 mere existence→原 witness 的资格提升；不是 HoTT 悖论。
- 失败：错误 source path、漏 library flags、混合 option cache、缺 infective guardedness 均保存并按责任点修复；命题未削弱。
- 索引：为新旧 run 冻结 row manifests；旧 Lean proof 在 matrix 追加后通过 row-stable exact replay。
- 三件套：core 不变；direction/panorama 更新，下一工作包为 Cubical partiality quotient/QIIT bind×race natural-consumer Gate。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "proof": {"proof_id": "MP-ERCF-TRUNC-001", "claim_ids": [f"C-{n}" for n in range(67, 71)], "source_sha256": EXPECTED[SOURCE], "run_sha256": EXPECTED[RUN_JSON], "index_sha256": EXPECTED[INDEX], "kernel": "Agda 2.8.0/Cubical v0.9 exit 0", "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH", "classification": "DEFENSE_WORKS", "status": "MACHINE_PROVED_LOCAL_UNCOMMITTED"},
        "toolchain": {"agda_asset_sha256": "9a35071eb9747f984177f48e1ba7008a9cebccfc259a40a0a84b29ffc2ec2db6", "cubical_asset_sha256": "003f9c57c134e4a9401a4b339b3773be667aa169ff929ca3dfb9c8abefc225c5", "cubical_tag_commit": "b150186d2544e7efeddd31e5d14a8b9ecbb100f7", "external_cache": "/Volumes/D/HoTT-toolchain-cache"},
        "preflight_failures": ["source path invocation", "library flags not applied", "mixed global-option XDG cache", "missing infective guardedness"],
        "index_evolution": {"old_lean": "ROW_STABLE_AFTER_INDEX_EVOLUTION", "native": "EXACT_INDEX_SNAPSHOT_MATCH"},
        "post_checkpoint_required": ["native and Lean exact replay", "36/36 KC audit", "27 directions/29 outcomes", "fresh revision 31", "projection freshness", "source/merge manifests", "full regression", "git diff --check"],
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "The active user goal authorizes continued HoTT paradox research and requires each new result to be assessed against and written to the trio. This checkpoint persists the native truncation defense and routes the next quotient/race experiment without commit/tag/push.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 31, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
