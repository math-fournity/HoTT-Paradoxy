#!/usr/bin/env python3
"""Prepare revision 28 for the machine-proved ERCF factorization core."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN"
RESULT_ID = "A-ERCF-FACTORIZATION-FORMAL-001"
C4 = "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md"
PROOF_SOURCE = "HoTT/formal/ercf-factorization/ERCF.lean"
PROOF_README = "HoTT/formal/ercf-factorization/README.md"
RUN_DIR = "HoTT/verification/runs/20260912-MP-ERCF-001-02"
RUN_JSON = f"{RUN_DIR}/RUN.json"
CLAIM_INDEX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
EVIDENCE = "audit/ERCF-1-2机器证明实施证据-20260912.md"
CAPTURE = "scripts/audit/capture_lean_proof_run.py"
VERIFIER = "scripts/audit/verify_formal_proof_run.py"

EXPECTED = {
    PROOF_SOURCE: "cb3564d348d6503614c6dd771ded172751e948882470f8213a9206d9a303ac8e",
    PROOF_README: "79a1c0373b5752ef1dc0e8259d67599bb772d26d54dacf41672d3e7c12a11edf",
    RUN_JSON: "696d23a3e95400329f0b6ddcf8ee8e573686f6acf3e58858b08d7353e320a0db",
    CLAIM_INDEX: "206635f2b58b2bdbe78e97119ccd2b28cc1fa14b2be1c85c13c526e19e5be444",
    VERIFIER: "1cae299d8ec404e54ed6c5b0a360390ec2d384cdcc3ffe15a97d2e4cc0599e37",
    CAPTURE: "2b949277c4bc2db3ac97601c934c070713d47a2d75cbac9f4ecbcffe1068bcc7",
}

SPEC = importlib.util.spec_from_file_location("runtime_ercf_factorization", RUNTIME_PATH)
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


def file_identity(root: Path, relative: str) -> dict[str, object]:
    data = (root / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": R.sha(data)}


def build_direction(root: Path) -> str:
    body = (root / R.DIRECTION).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-direction-portfolio/v1.4", "integrated-direction-portfolio/v1.5")
    body = replace_once(body, "integrated-direction-portfolio:v1.4", "integrated-direction-portfolio:v1.5")
    body = body.replace(
        "CORE_GENERATION_4_MATH_PROOF_DELIVERY_GATE_ACTIVE",
        "CORE_GENERATION_4_ERCF_FACTORIZATION_MACHINE_PROVED_LOCAL_NATIVE_OPEN",
    )
    body = replace_once(body, "source_state_revision: 27", "source_state_revision: 28")
    body = replace_once(body, "projection_generation: 20260912-direction-011", "projection_generation: 20260912-direction-012")
    body = replace_line_prefix(
        body,
        "| `DIR-G-MATH-PROOF-DELIVERY-GATE`",
        "| `DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 AI 的数学结论在交付前必须由匹配语义的 proof assistant/kernel 机器证明；源码、实际 run 与索引全部留在 repo，`/tmp` 不得成为唯一证据位置 | 用户 ruling §15 / F-011 | `ACTIVE_USER_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-MATH-PROOF-DELIVERY-GATE`、`OUT-TOP-ERCF-FACTORIZATION-LEAN` | 首个真实 package `MP-ERCF-001` 已贯通；今后继续逐 claim 建立 formal source→immutable run→claim matrix 链，缺件时降格 | `AGENTS.md`；`docs/quality/数学结论机器证明与证据留存规范.md`；`audit/ERCF-1-2机器证明实施证据-20260912.md` |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-TOP-QUALIFICATION-PRESERVATION`",
        "| `DIR-TOP-QUALIFICATION-PRESERVATION` | ASK／完成资格在 HoTT 抽象、组合、提取与反射中的保持性；统一 A/B 两类现实相对悖论 | 用户 generation-4 core；当前 AI 的 C3/C4 综合（其中用户新增方向以 KC-000028–000036 为准） | `NEXT_CANDIDATE` | `COMPUTATIONAL_LEGITIMACY`, `TIME_AND_TEMPORALITY`, `SELF_REFERENCE`, `PARADOX_DISCOVERY` | `OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`、`OUT-TOP-ERCF-FACTORIZATION-LEAN`、`OUT-W-R041-PAPER`、`OUT-W-RP-B01` | 通用 factorization 已机器闭合；下一步固定真实 HoTT truncation/quotient/HIT abstraction，先证明受保护 consumer，再检验自然负向 consumer 是被正确拒绝还是发生资格提升失配 | `理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md`；`理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；`HoTT/formal/ercf-factorization/ERCF.lean` |",
    )
    body = replace_line_prefix(
        body,
        "| `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`",
        "| `DIR-U-THEORY-ECONOMY-SELF-VALIDATION` | 理论通过遗忘现实因素取得经济收益后，是否在内部证明其抽象、真理验证器和自身可靠性时形成不可停机、部分性或元层上升；同时审计最小理论覆盖和存在/不存在双视角 | 用户直接新增方向 `KC-000028`–`KC-000036` | `ACTIVE_USER_DIRECTION` | `THEORY_ECONOMY`, `SELF_VALIDATION`, `SELF_REFERENCE`, `ABSTRACTION_AND_NEGATION`, `EXISTENCE_NEGATION_DUALITY` | `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`、`OUT-TOP-ERCF-FACTORIZATION-LEAN` | `MP-ERCF-001` 已闭合一般 ERCF-1/2；现在实例化一个 HoTT 原生信息经济接口与自然 consumer，获得 `DEFENSE_WORKS`/`REPRESENTATION_BOUNDARY`/`NATURAL_USAGE_MISMATCH` 判词后再决定 ERCF-3 exact calculus | `核心认知.md` `KC-000028`–`KC-000036`；`理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；`HoTT/verification/runs/20260912-MP-ERCF-001-02/` |",
    )
    old_priority = """1. **当前用户主方向**：`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` × `DIR-L-SELF-REFLECTION`。先把理论经济、任务相对充分性与反射认证义务写成可证伪构造。
2. **总方向建议（AI 统筹，尚非用户单独裁定）**：`DIR-TOP-QUALIFICATION-PRESERVATION`，以 ASK／完成资格在抽象、组合、提取和反射中的保持性统一 A/B 与 ERCF。
3. **第一最小可验结果**：C4 的 `ERCF-1/2`，机器证明 `ParadoxWitness(α,J)` 与 factorization 不可能，并给出平凡任务正例；这是进入自反前的 walking skeleton。
4. **战略自反深化**：`DIR-W-RP-B01` × ERCF-3。目标是定位数学分类→统一有效交付→有效自我 ASK→自我可靠性认证的资格升级点。
5. **操作对照包**：`DIR-W-RACE-TIMEOUT`。从 R041 的 bind/race 分离推进真实 partiality quotient/QIIT，作为“局部操作不变性不等于全局上下文充分性”的独立证据。
6. **探索/独立验证位**：完整流函数/在线因果、guard 擦除、同函数异时与 R034 Cubical Agda；只在真实接口固定后进入。
7. **证据/治理队列**：R041 code/25-test/`cf58f27`/container 谱系、2,396 条历史 claim、aistudio coverage 和历史因果映射继续按当前任务选择；C4 不改变这些历史分母。"""
    new_priority = """1. **当前用户主方向**：`DIR-U-THEORY-ECONOMY-SELF-VALIDATION` × `DIR-L-SELF-REFLECTION`。把理论经济、任务相对充分性与反射认证义务推进为 HoTT 原生、可证伪构造。
2. **总方向建议（AI 统筹，尚非用户单独裁定）**：`DIR-TOP-QUALIFICATION-PRESERVATION`，以 ASK／完成资格在抽象、组合、提取和反射中的保持性统一 A/B 与 ERCF。
3. **已闭合的基础切片**：`MP-ERCF-001`/`C-59`–`C-66` 机器证明通用 factorization walking skeleton；它排除了把 E₀ 本身当作 HoTT coverage gap 的路径，不再重复这一通用投影模型。
4. **下一最小 HoTT 原生判别**：固定 propositional truncation 或 quotient/HIT 的真实 checker/规则，先证明受保护 consumer 正例，再检验一个自然的 witness/时序/代表元 consumer；正确拒绝记为 `DEFENSE_WORKS`。
5. **战略自反深化**：`DIR-W-RP-B01` × ERCF-3。只在原生信息经济接口闭合后，定位数学分类→统一有效交付→有效自我 ASK→自我可靠性认证的资格升级点。
6. **操作对照包**：`DIR-W-RACE-TIMEOUT`。从 R041 的 bind/race 分离推进真实 partiality quotient/QIIT，作为“局部操作不变性不等于全局上下文充分性”的独立证据。
7. **探索与证据队列**：完整流函数/在线因果、guard 擦除、同函数异时、R034 Cubical Agda，以及 R041 执行谱系、2,396 条历史 claim、aistudio coverage，均按与当前 native consumer 的判别关系调度。"""
    body = replace_once(body, old_priority, new_priority)
    body = replace_once(
        body,
        "C4 仍是 `PAPER_ONLY` 条件性综合，没有 proof assistant 机器证明、具体非停机程序运行或外部接口审计；在新门禁下不能作为当前 AI 已证明的数学结论重新交付。后续每个数学工作单元必须先形成 repo 内 proof source/run/index 链，否则只交付候选和证明义务。",
        "C4 整体仍是 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`：只有 `MP-ERCF-001`/`C-59`–`C-66` 达到 `MACHINE_PROVED_LOCAL_UNCOMMITTED`，没有 HoTT 原生 abstraction/consumer、具体非停机轨迹或 ERCF-3。后续数学单元继续按 F-011 建立 source/run/index 链。",
    )
    return body


def build_panorama(root: Path) -> str:
    body = (root / R.PANORAMA).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-outcome-panorama/v1.4", "integrated-outcome-panorama/v1.5")
    body = replace_once(body, "integrated-outcome-panorama:v1.4", "integrated-outcome-panorama:v1.5")
    body = body.replace(
        "CORE_GENERATION_4_MATH_PROOF_DELIVERY_GATE_ACTIVE",
        "CORE_GENERATION_4_ERCF_FACTORIZATION_MACHINE_PROVED_LOCAL_NATIVE_OPEN",
    )
    body = replace_once(body, "source_state_revision: 27", "source_state_revision: 28")
    body = replace_once(body, "projection_generation: 20260912-outcome-011", "projection_generation: 20260912-outcome-012")
    formal_row = "| `FORMAL_CHECKED_WITH_SCOPE` | 指定 proof assistant、版本、源码和命题通过，不能外推未覆盖规则 |"
    body = replace_once(
        body,
        formal_row,
        formal_row + "\n| `MACHINE_PROVED_LOCAL_UNCOMMITTED` | 精确 claim/source/kernel run/index 链已在当前工作树闭合，但尚未进入获准 Git commit，不能声称 version-closed |",
    )
    gate_row = (
        "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE` | F-011：数学结论交付前机器证明；证明源码、实际 kernel run 和 claim/proof/run 索引分别由 `HoTT/formal/`、"
        "`HoTT/verification/runs/`、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 持有；无证明则强制降格 | `DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前用户裁定与项目本地治理 3.2 candidate | "
        "`VERIFIED_WITH_SCOPE` | 根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范和三类 owner 已接通；4/4 正负向测试通过，首个真实 package `MP-ERCF-001` 又通过 source/run/index/hash/exact replay | "
        "不证明 fresh 模型必然遵循，不把通用 Lean 因子化证明外推为 HoTT 原生结论；当前未 commit/tag | "
        "`docs/quality/数学结论机器证明与证据留存规范.md`；`audit/数学结论机器证明交付门禁实施证据-20260912.md`；`audit/ERCF-1-2机器证明实施证据-20260912.md` |"
    )
    proof_row = (
        "| `OUT-TOP-ERCF-FACTORIZATION-LEAN` | `MP-ERCF-001`：一般 `Type` 值因子化的必要方向、witness no-go、section 充分方向、E₀ 正反控制、subsingleton 反控制、分离观察族与 identity 观察控制（`C-59`–`C-66`） | "
        "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前顶层 Lean 形式化 | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED` | Lean 4.33.1 final run exit 0；source/output/index hashes 完整；独立 `--rerun` 为 `EXACT_EXIT_STDOUT_STDERR_MATCH`；源码无 proof placeholder | "
        "不使用 univalence、cubical Path、HIT、truncation 或 higher coherence；不证明 HoTT coverage gap、HoTT 悖论、现实桥梁、ERCF-3 或原创性 | "
        "`HoTT/formal/ercf-factorization/ERCF.lean`；`HoTT/verification/runs/20260912-MP-ERCF-001-02/`；`HoTT/CLAIM_EVIDENCE_MATRIX.md`；`audit/ERCF-1-2机器证明实施证据-20260912.md` |"
    )
    body = replace_line_prefix(body, "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE`", gate_row + "\n" + proof_row)
    body = replace_line_prefix(
        body,
        "| `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY`",
        "| `OUT-TOP-HOTT-SELF-VALIDATION-ECONOMY` | C4 将 HoTT 自身真理验证拆为有限 proof checking、归一化、证明搜索、整体语义真理和内部总自验证五层；提出 ERCF，并给出 abstraction factorization、存在/不存在四分法、最小 E₀/E₁ 与 Gödel/元层边界 | `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-TOP-QUALIFICATION-PRESERVATION` | 当前用户原文 + 顶层 AI 条件性研究综合 | `PAPER_ONLY` | C4 整体仍是条件性综合；其通用 factorization 子核已分离为 `OUT-TOP-ERCF-FACTORIZATION-LEAN` 并机器证明，证明了 E₀/一般 no-go 骨架而非 HoTT 特定实例 | 不证明 HoTT 内部矛盾、任意 HoTT 实现死循环、物理时空离散、最小 coverage no-go 或 ERCF-3；不得用通用 Lean 结果越级 | `理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；`audit/ERCF-1-2机器证明实施证据-20260912.md`；`核心认知.md` `KC-000028`–`KC-000036` |",
    )
    body = replace_once(
        body,
        "6. C3 是证据受限的 AI 研究战略；真实 partiality/QIIT consumer、B01-TARGET 和有效自我 ASK 演算尚未完成。C4 已响应用户的新自反/理论经济方向，但 ERCF-1/2/3 的 proof-assistant 形式化、具体发散 witness、最小 HoTT coverage no-go 与 Gödel 内部化均未完成。",
        "6. C3 是证据受限的 AI 研究战略；`MP-ERCF-001` 已闭合 ERCF-1/2 的通用因子化子核，但真实 HoTT truncation/quotient/HIT consumer、B01-TARGET、有效自我 ASK、具体发散 witness、最小 HoTT coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )
    return body


def build_memory(root: Path, c4_hash: str, c4_lines: int) -> str:
    body = (root / "MEMORY.md").read_text(encoding="utf-8")
    old_queue = """1. 用户新增项目级硬约束 F-011：当前 AI 的所有数学结论在交付前必须有匹配语义的机器证明；源码、实际 kernel run 和 claim/proof/run 索引必须留在 repo，`/tmp` 不能是唯一证据位置。
2. 当前数学主方向仍是 HoTT 自反真理验证/理论经济；下一最小研究结果 ERCF-1/2 只有在 `HoTT/formal/`、`HoTT/verification/runs/` 和 claim matrix 形成完整 proof package 后，才可作为数学结论交付。
3. C4 保持 `PAPER_ONLY`，新规则不追认或伪造历史证明；未来重用其命题时必须逐项形式化和重放。
4. C3 的资格保持性、W51×RP-B01、自指与 R041 partiality 对照继续在全局视野；同样受 F-011 约束。"""
    new_queue = """1. `MP-ERCF-001` 已完成 F-011 生效后的首个真实 proof package：`C-59`–`C-66` 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`；下一轮不得重复通用 E₀ 投影模型。
2. 当前数学主方向仍是 HoTT 自反真理验证/理论经济；下一最小结果改为一个 HoTT 原生 truncation 或 quotient/HIT abstraction，先证明受保护 consumer，再检验自然负向 consumer。
3. C4 整体保持 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`；只有通用子核升级，HoTT 特定 coverage/self-reflection/ERCF-3 均未证明。
4. C3 的资格保持性、W51×RP-B01、自指与 R041 partiality 对照继续在全局视野；进入任何数学结论前仍逐 claim 执行 F-011。"""
    body = replace_once(body, old_queue, new_queue)
    old_c4 = "- C4 经量词纠偏后共 733 行，SHA-256 `8a5a88d9f11569c6bde145ce1944eadf063bb24784732a41c56bf95f8cc15f7a`；它将验证任务分五层，提出 ERCF、任务相对 factorization、存在/不存在四分法、E₀/E₁ 与 Gödel/元层边界；状态仍为 `PAPER_ONLY`。纤维常值只无条件给出必要性，逆向需 quotient/image 泛性质、截面或选择；全局 no-go 需 separating observation family。"
    new_c4 = f"- C4 当前共 {c4_lines} 行，SHA-256 `{c4_hash}`；整体为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`。它将验证任务分五层，并把 `MP-ERCF-001`/`C-59`–`C-66` 的通用机器证明与 HoTT 原生未决边界分开。"
    body = replace_once(body, old_c4, new_c4)
    gate_line = "- F-011 proof-delivery Gate 已在根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范、formal/run/index owner 中实现；4/4 正负向 static tests PASS。它只证明治理结构，不证明未来模型行为或任何数学命题。"
    body = replace_once(
        body,
        gate_line,
        gate_line + "\n- `MP-ERCF-001` 是 F-011 下首个真实数学 package：Lean 4.33.1 final run/index/hash/exact replay PASS；源码和运行原件均在 repo；未提交，且只证明一般 `Type` 值因子化。",
    )
    body = replace_once(
        body,
        "- 本轮 core/curation/transition、C4、方向/全景和治理机制可机器检查；C4 本身尚无 proof-assistant 证明或具体发散运行轨迹。",
        "- 本轮 core/curation/transition、C4、方向/全景和治理机制可机器检查；C4 的通用 factorization 子核有 `MP-ERCF-001` proof-assistant 证明，但 C4 的 HoTT 特定、自反与具体发散主张仍无机器证明/运行轨迹。",
    )
    body = replace_once(
        body,
        "当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001` 并读 C4；进入机器证明时再读 C3、Theory Schema 和选定 proof assistant 接口。不要直接跳到 ERCF-3：先完成 ERCF-1/2 的正反对照。",
        "当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001` 与 `A-ERCF-FACTORIZATION-FORMAL-001` 并读 C4/proof package。ERCF-1/2 通用正反对照已完成；不要直接跳到 ERCF-3，先固定一个 HoTT 原生 truncation 或 quotient/HIT 接口及自然 consumer。",
    )
    return body


def build_frontier(root: Path) -> str:
    return """# HoTT 研究前沿（S028 ERCF 通用因子化机器证明）

本文件是当前注意力槽，不是数学结论数据库。`MP-ERCF-001` 只把通用因子化 `C-59`–`C-66` 升为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`；C4 整体和 HoTT 原生悖论仍开放。所有新数学结论继续执行 F-011。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 当前用户主方向 | ERCF：理论经济化抽象与反射性自我认证何时迫使部分性、不完备或元层上升 | active-user-direction / mixed-paper-and-general-formal-core | 保持 V1–V5 分层；不把通用因子化结果外推成自反/非停机结论 |
| 已闭合基础切片 | `MP-ERCF-001`：一般 `Type` 值 factorization、E₀ 正反控制、分离观察与 identity 控制 | machine-proved-local-uncommitted / not-HoTT-specific | 作为后续实例的接口合同；不再重复任意投影 E₀，不在未授权时声称 version-closed |
| 第一 HoTT 原生判别 | propositional truncation 或 quotient/HIT 的真实信息经济接口及 consumer | next-candidate / checker-and-exact-rules-not-yet-fixed | 固定原生系统；先证明受保护消去/同余正例，再选择自然 witness/代表元/时序 consumer；正确拒绝记 `DEFENSE_WORKS` |
| 战略自反深化 | ERCF-3 × W51/RP-B01：Code/quote/eval/provability/ASK 与验证器自身 | blocked-on-native-abstraction-consumer-and-calculus | 只在 exact calculus、宇宙和 derivability 条件固定后构造 diagonal；不以一般 Gödel 口号冒充 HoTT 特有结论 |
| 最小覆盖边界 | 一致、操作语义清楚、观察规格明确而 HoTT 无法保真解释的最小理论 | open / E0-eliminated-as-coverage-gap | E₀ 已可表达；下一对象必须依赖真实 HoTT 规则，且区分 `DEFENSE_WORKS`、表示边界与自然使用失配 |
| 对照与历史支线 | cubical normalization 正控制、R041 bind/race、R034 native、guard/online causality | retained / not-current-first | 用于选择 native consumer 和反驳过强结论；不覆盖当前用户主方向 |

判词保持：`DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`。新原生尝试必须同时保存通过与拒绝结果。
"""


def build_resume(root: Path) -> str:
    body = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    start = "## 当前停止点\n\n"
    before, sep, _ = body.partition(start)
    if not sep:
        raise ValueError("RESUME_STOP_MARKER_MISSING")
    stop = """S028 已完成 ERCF-1/2 的通用机器证明：`MP-ERCF-001`/`C-59`–`C-66` 由 Lean 4.33.1 kernel 接受，final run `20260912-MP-ERCF-001-02` 已索引且 exact replay 一致；源码、stdout/stderr、环境与 source manifest 都在 repo。当前未 commit，所以只能称 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

这个结果不是 HoTT 悖论。源码只用普通 `Type` 和 Lean equality；它证明 E₀/因子化 walking skeleton 可表达，并排除把 E₀ 本身当作 HoTT coverage gap。C4 整体仍为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`。

下一步不是 ERCF-3，也不是再造一个任意投影：先固定一个原生支持 propositional truncation 或 quotient/HIT 的 HoTT/cubical 系统，机器证明受保护 consumer 正例，再检验一个来自实际用法的 witness/代表元/时序 consumer。若系统正确拒绝，结论是 `DEFENSE_WORKS`；只有合法自然接口与同任务桥梁都闭合，才可能升级为 HoTT 特定候选。
"""
    return before + start + stop


def build_audit(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000003": ("DEEPENED", "把‘前提/因素是否影响结果’落实为任务相对因子化与同纤维观察条件，并由 C-59/C-60 机器核验。"),
        "KC-000015": ("DEEPENED", "理论抽象删除区分后的悖论潜势获得通用 `ParadoxWitness→¬FactorsThrough` 机器证明；HoTT 实例仍开放。"),
        "KC-000018": ("DEEPENED", "理论工具性/经济性被收敛为对任务族的充分性，而不是无条件把省略等同逻辑否定。"),
        "KC-000021": ("ALIGNED", "本轮确实运行 Lean 4.33.1，并把证明源码、kernel 原始结果、环境、哈希和索引留在当前 repo。"),
        "KC-000022": ("DEEPENED", "机器证明了两类方向共用的表示因子化骨架，但没有冒充两类 HoTT 悖论均已找到。"),
        "KC-000029": ("DEEPENED", "理论经济收益的任务相对边界由正控制、subsingleton 反控制和 separating family 同时固定。"),
        "KC-000031": ("CORRECTED", "E₀ 在普通依值类型论/Lean 中可表达，因此不能充当 HoTT 范型过严导致的 coverage gap；下一候选必须使用 HoTT 原生规则。"),
        "KC-000032": ("DEEPENED", "‘删除因素后产生否定性存在/缺席’被窄化为明确抽象与观察的非因子化命题，避免无条件存在论外推。"),
        "KC-000035": ("DEEPENED", "本项目悖论理论的最小 E₀ 骨架已机器表达；完整 HoTT 原生表达、现实桥梁与自反层仍待证。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    for unit in manifest["units"]:
        unit_id = str(unit["id"])
        relation, assessment = touched.get(
            unit_id,
            ("NOT_TOUCHED", "本轮只闭合 ERCF 的通用因子化机器证明并调整下一 HoTT 原生目标；该用户原文及既有研究判断不变。"),
        )
        counts[relation] = counts.get(relation, 0) + 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        evidence = (
            "HoTT/formal/ercf-factorization/ERCF.lean；HoTT/verification/runs/20260912-MP-ERCF-001-02/；"
            f"audit/ERCF-1-2机器证明实施证据-20260912.md；核心认知.md {unit_id}"
        )
        lines.append(
            f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | {evidence} | HoTT 原生 abstraction/consumer 与 ERCF-3 仍未闭合。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — 本轮没有新的用户原文；generation-4/36 KC 与 hash 均不变。",
        "- direction_change: `YES` — 通用 ERCF-1/2 从下一候选改为已闭合基础；下一动作切换到 HoTT 原生 truncation/quotient/HIT consumer。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-ERCF-FACTORIZATION-LEAN`，并把 C4 分成通用已证子核与 HoTT/self-reflection paper-only 余项。",
        "- update_decision: `C4/proof evidence/README/Feature/STATE/MEMORY/FRONTIER/LESSONS/RESUME/方向/全景更新；core 不改。`",
        "- cross_conflicts: `NONE_AFTER_SCOPE_SPLIT` — claim matrix、final run、C4 与三件套都禁止把普通 Lean equality 外推为 HoTT 原生结果。",
        "- unresolved: `原生 checker/变体、真实 abstraction、受保护 consumer 与自然负向 consumer 尚待固定；ERCF-3 暂不启动。`",
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
    if state.get("revision") != 27 or state.get("latest_session") != "S-GOV-20260912-027-MATH-PROOF-GATE-FINAL-ALIGNMENT":
        raise SystemExit("EXPECTED_REVISION_27_S027")
    for relative, expected_hash in EXPECTED.items():
        if R.sha((root / relative).read_bytes()) != expected_hash:
            raise SystemExit(f"PRECONDITION_HASH_MISMATCH:{relative}")
    run = json.loads((root / RUN_JSON).read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX" or run.get("exit_code") != 0:
        raise SystemExit("FINAL_RUN_NOT_ACCEPTED_AND_INDEXED")
    if run.get("claim_ids") != [f"C-{n}" for n in range(59, 67)]:
        raise SystemExit("FINAL_RUN_CLAIM_SET_MISMATCH")

    c4_data = (root / C4).read_bytes()
    c4_hash = R.sha(c4_data)
    c4_lines = len(c4_data.decode("utf-8").splitlines())
    direction = build_direction(root)
    panorama = build_panorama(root)
    memory = build_memory(root, c4_hash, c4_lines)
    frontier = build_frontier(root)
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "34. `MP-ERCF-001`" not in lessons:
        lessons += "\n34. `MP-ERCF-001` 机器证明了通用因子化 walking skeleton，并以 subsingleton、section、separating family 和 identity 观察提供正反控制；这使 E₀ 从 coverage-gap 候选降为可表达的通用基础。下一步必须引入真实 HoTT abstraction/consumer，不能以普通 Lean `Eq` 重命名为 HoTT 悖论。"
    lessons += "\n"
    resume = build_resume(root)

    semantic = "CORE_GENERATION_4_ERCF_FACTORIZATION_MACHINE_PROVED_LOCAL_NATIVE_OPEN"
    state["revision"] = 28
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "ERCF_GENERAL_FACTORIZATION_MACHINE_PROVED_LOCAL_HOTT_NATIVE_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "next_minimal_verification": "Fix a native HoTT/cubical truncation or quotient/HIT abstraction and prove its protected consumer first; then test a natural witness/representative/temporal consumer and classify rejection as DEFENSE_WORKS rather than paradox.",
    })
    state["projection"]["status"] = semantic
    drec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    drec.update({
        "projection_generation": "20260912-direction-012",
        "semantic_status": semantic,
        "scope": "Cross-source portfolio after MP-ERCF-001 machine-proved the general factorization walking skeleton; next research is a native HoTT information-economy interface and natural consumer, while F-011 remains mandatory.",
    })
    for path in (PROOF_SOURCE, RUN_JSON, EVIDENCE):
        append_unique(drec["full_sources"], path)
    prec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    prec.update({
        "projection_generation": "20260912-outcome-012",
        "semantic_status": semantic,
        "scope": "Cross-source outcome panorama with the first F-011 mathematical package: C-59 through C-66 are machine-proved locally, while HoTT-native abstraction/consumer, reflection and paradox remain open.",
    })
    for path in (PROOF_SOURCE, RUN_JSON, EVIDENCE):
        append_unique(prec["full_sources"], path)

    revalidation = (
        "C4 was reread after S028 separated the Lean-machine-proved general factorization core C-59 through C-66 from the still paper-only HoTT-native, reality-bridge and ERCF-3 claims; historical checkpoint copies preserve earlier versions."
    )
    for record_id, record in state["records"].items():
        source_hashes = record.get("source_hashes")
        if isinstance(source_hashes, dict) and C4 in source_hashes:
            source_hashes[C4] = c4_hash
            record["revalidation"] = revalidation

    hott_record = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    hott_record.update({
        "evidence_status": "PAPER_ONLY_WITH_MACHINE_PROVED_SUBRESULT",
        "mathematical_status": "GENERAL_FACTORIZATION_CORE_MACHINE_PROVED_HOTT_NATIVE_REFLECTION_OPEN",
        "scope": "C4 separates V1-V5 and ERCF. MP-ERCF-001 machine-proves the general Type-valued factorization subcore C-59 through C-66; native HoTT abstraction/consumer, reality bridge, concrete divergence, coverage no-go and ERCF-3 remain open.",
    })
    for path in (PROOF_SOURCE, PROOF_README, RUN_JSON, CLAIM_INDEX, EVIDENCE):
        append_unique(hott_record["full_sources"], path)
    hott_record["source_hashes"].update({
        C4: c4_hash,
        PROOF_SOURCE: EXPECTED[PROOF_SOURCE],
        RUN_JSON: EXPECTED[RUN_JSON],
        CLAIM_INDEX: EXPECTED[CLAIM_INDEX],
    })

    gate_record = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    for path in (CAPTURE, VERIFIER, PROOF_SOURCE, PROOF_README, f"{RUN_DIR}/source-manifest.json", RUN_JSON, EVIDENCE):
        append_unique(gate_record["full_sources"], path)
    gate_record["source_hashes"].update({
        "AGENTS.md": R.sha((root / "AGENTS.md").read_bytes()),
        CLAIM_INDEX: EXPECTED[CLAIM_INDEX],
        "HoTT/formal/README.md": R.sha((root / "HoTT/formal/README.md").read_bytes()),
        "HoTT/verification/runs/README.md": R.sha((root / "HoTT/verification/runs/README.md").read_bytes()),
        CAPTURE: EXPECTED[CAPTURE],
        VERIFIER: EXPECTED[VERIFIER],
        PROOF_SOURCE: EXPECTED[PROOF_SOURCE],
        RUN_JSON: EXPECTED[RUN_JSON],
    })
    gate_record["revalidation"] = "The first real proof package MP-ERCF-001 passed Lean kernel, immutable run/index/hash checks and exact replay; fresh-model compliance behavior remains NOT_RUN."
    gate_record["scope"] = "Require every current-AI mathematical conclusion to have a semantically matching machine proof persisted as source/run/index. MP-ERCF-001 exercises the real path for C-59 through C-66; fresh-model behavior and Git version closure remain open."

    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": PROOF_SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "mathematical_status": "GENERAL_TYPE_FACTORIZATION_PROVED_HOTT_NATIVE_NOT_CLAIMED",
        "depends_on": ["A-HOTT-SELF-VALIDATION-ECONOMY-001", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [PROOF_SOURCE, PROOF_README, RUN_JSON, f"{RUN_DIR}/source-manifest.json", f"{RUN_DIR}/stdout.txt", f"{RUN_DIR}/stderr.txt", f"{RUN_DIR}/environment.txt", CLAIM_INDEX, VERIFIER, EVIDENCE, C4],
        "source_hashes": {
            PROOF_SOURCE: EXPECTED[PROOF_SOURCE],
            PROOF_README: EXPECTED[PROOF_README],
            RUN_JSON: EXPECTED[RUN_JSON],
            CLAIM_INDEX: EXPECTED[CLAIM_INDEX],
            VERIFIER: EXPECTED[VERIFIER],
            C4: c4_hash,
        },
        "claim_ids": [f"C-{n}" for n in range(59, 67)],
        "proof_id": "MP-ERCF-001",
        "run_id": "20260912-MP-ERCF-001-02",
        "scope": "Lean 4.33.1 proves the exact general Type-valued factorization controls in ERCF.lean. No univalence, cubical Path, HIT, truncation, HoTT-specific paradox, physical bridge or originality is claimed.",
        "resolution": {
            "evidence": [RUN_JSON, f"{RUN_DIR}/source-manifest.json", f"{RUN_DIR}/stdout.txt", f"{RUN_DIR}/stderr.txt", CLAIM_INDEX, VERIFIER, EVIDENCE],
            "reason": "Final indexed run exited 0 and exact replay matched stdout/stderr; all source and index hashes match. Git version closure is not authorized, so status remains local-uncommitted.",
        },
    }

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-027-MATH-PROOF-GATE-FINAL-ALIGNMENT", RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, PROOF_SOURCE, PROOF_README, RUN_JSON, CLAIM_INDEX, VERIFIER, EVIDENCE, C4, "scripts/audit/prepare_ercf_factorization_checkpoint.py"],
        "source_hashes": {PROOF_SOURCE: EXPECTED[PROOF_SOURCE], RUN_JSON: EXPECTED[RUN_JSON], CLAIM_INDEX: EXPECTED[CLAIM_INDEX], C4: c4_hash},
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_GENERAL_FACTORIZATION_HOTT_NATIVE_OPEN",
        "cognition_status": "ERCF_GENERAL_WALKING_SKELETON_PROVED_AND_NATIVE_NEXT_ROUTED",
        "scope": "Machine-prove and persist the general ERCF-1/2 factorization core, separate it from HoTT-specific claims, update the trio and audit all 36 KC.",
    }
    session = f"""# {SESSION_ID}

- 触发：MEMORY/方向/C4 把 ERCF-1/2 设为 F-011 下第一最小可验结果。
- 构造：在 `{PROOF_SOURCE}` 固定一般 `Type` 值 `FactorsThrough`、`FiberConstant`、`ParadoxWitness`、E₀ 正反控制、subsingleton、分离观察族和 identity 控制。
- 运行：Lean 4.33.1 final run `20260912-MP-ERCF-001-02` exit 0；source/output/index hashes 通过；`verify_formal_proof_run.py --rerun` 为 `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 数学状态：`C-59`–`C-66 = MACHINE_PROVED_LOCAL_UNCOMMITTED`。没有 univalence/cubical Path/HIT/truncation，因此不是 HoTT 悖论；C4 整体仍 paper-only。
- 研究转向：E₀ 被排除为 coverage-gap 候选；下一步固定 HoTT 原生 truncation 或 quotient/HIT abstraction 及正/负 consumer，不直接跳 ERCF-3。
- 三件套：core `NO_CHANGE`；direction/panorama 更新到 revision 28，并新增 `OUT-TOP-ERCF-FACTORIZATION-LEAN`。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof": {
            "proof_id": "MP-ERCF-001",
            "claim_ids": [f"C-{n}" for n in range(59, 67)],
            "source": file_identity(root, PROOF_SOURCE),
            "final_run": file_identity(root, RUN_JSON),
            "claim_index": file_identity(root, CLAIM_INDEX),
            "kernel": "Lean 4.33.1 exit 0",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
            "status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        },
        "scope": "GENERAL_TYPE_FACTORIZATION_ONLY_NOT_HOTT_NATIVE",
        "pre_index_run": "20260912-MP-ERCF-001-01 retained as non-current lineage",
        "post_checkpoint_required": ["36/36 KC audit", "proof exact replay", "core/runtime/reader/three-way regression", "source and merge manifests", "fresh revision 28", "projection freshness", "git diff --check"],
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    texts = {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session,
        audit_path: build_audit(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "The active user goal authorizes continued HoTT paradox research and requires every new result to be evaluated against and written to the trio. This checkpoint persists the machine-proved ERCF factorization increment without commit/tag/push.",
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": relative,
                "expected_sha256": R.sha((root / relative).read_bytes()) if (root / relative).exists() else None,
                "text": value,
            }
            for relative, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 28,
        "session_id": SESSION_ID,
        "files": len(texts),
        "c4_sha256": c4_hash,
        "c4_lines": c4_lines,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
