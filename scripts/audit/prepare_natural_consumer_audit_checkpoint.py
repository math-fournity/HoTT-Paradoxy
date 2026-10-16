#!/usr/bin/env python3
"""Prepare revision 43: record the bounded N1 natural-consumer audit.

N1 audits a fixed set (Cubical library v0.9 plus four primary external
sources) for an E6 consumer that upgrades a weaker qualification to a
stronger one.  No such consumer was found; the closest candidates are fenced
by explicit assumptions, coherence data or the type checker.  The result is a
bounded negative and routes the W51xRP-B01 extraction-interface audit (N2).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-043-NATURAL-CONSUMER-AUDIT"
PREV_SESSION = "S-RES-20260912-042-C5-PARADOX-DISTANCE"
RESULT_ID = "A-NATURAL-CONSUMER-AUDIT-001"
AUDIT = "audit/natural-consumer审计-20260912.md"
C5 = "理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md"
TOOLCHAIN = "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SOURCES = f".codex/research/hott/sessions/{SESSION_ID}/evidence/sources"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_n1_audit", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N1 继续以现实相对非现实性为目标，把未找到 consumer 记为有界负结论而非悖论。"),
        "KC-000012": ("DEEPENED", "N1 把 ASK 的资格问题落成 E6 四条件检查，并逐个核对真实接口的假设与围栏。"),
        "KC-000013": ("DEEPENED", "理论工具性的“遗忘”在审计中以接口承诺与显式假设的形式被区分，不再停留在直觉。"),
        "KC-000014": ("ALIGNED", "方向 B 的有效交付仍未越级；N2 将直接审计 RP-B01 的对象层→执行层接口。"),
        "KC-000022": ("ALIGNED", "两类现实相对悖论框架保持不变；N1 没有把 documented boundary 写成目标完成。"),
        "KC-000024": ("ALIGNED", "时序相关资格在 partiality/delay 审计中被逐项检查；审计集合内没有把时序差异偷偷提升的接口。"),
        "KC-000027": ("DEEPENED", "HoTT/类型论库把选择、证明存在与计算提取分开；N2 将审查程序界限在真实接口中的表现。"),
        "KC-000031": ("ALIGNED", "严格范型/消去限制在审计中继续记为防御与显式假设，不判为覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N1 的负结论不支持提前启动反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是固定审计集合内的 N1 consumer 审计；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S043/SESSION.md；audit/natural-consumer审计-20260912.md | N2、B01-TARGET、ERCF-3 与 R036/R038 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N1 在固定审计集合内给出 bounded negative；第一工作包从 N1 转为 N2 W51×RP-B01 提取接口审计；revision 43/generation 027。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-NATURAL-CONSUMER-AUDIT`（bounded negative / documented boundary）。",
        "- update_decision: `N1 审计报告进入 audit/；十包 claim 状态不变；DIR-W-RACE-TIMEOUT 保持 CLOSED_WITH_SCOPE；DIR-W-RP-B01 的下一动作固定为 N2。`",
        "- cross_conflicts: `NONE_OBSERVED` — 审计集合与机器证明使用同一 Cubical v0.9 身份；claim matrix 未变。",
        "- unresolved: `N2、B01-TARGET、ERCF-3、R036/R038 原生升级、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮无新数学结论，状态为 `BOUNDED_NEGATIVE_MOVE_TO_RP_B01`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：C5 判定唯一决定性缺环是 E6（natural consumer）；执行 N1 有界自然消费者审计。",
        "- 审计集合：Cubical library v0.9 全库（tag commit b150186d、tree SHA 73ccfbaf、1111 files/7,511,145 bytes）＋四份一手外部入口（Chapman–Uustalu–Veltri、Altenkirch–Danielsson–Kraus、Møgelberg–Zwart、Cost-Aware Type Theory）。",
        "- 结果：未找到同时满足 E6 四条件的 consumer。最近候选（`MagicTrick.recover`、`SplitSupport`、`satAC`、delay 商、delay×effects、`uaβ`/SIP、CATT）全部被显式假设、相干数据或类型围栏挡住。",
        "- 判定：`BOUNDED_NEGATIVE_MOVE_TO_RP_B01`；负结论严格限定在本次审计集合与版本内，重开条件见审计报告 §6。",
        "- 下一工作包：N2 W51×RP-B01 提取接口审计（固定真实对象层→执行层接口，四组控制；找到候选则 F-011 机器化，明确防御则记 DEFENSE_WORKS，缺源则 INCONCLUSIVE_SOURCE_UNAVAILABLE）。",
        "- 三件套：direction/panorama revision 43/generation 027；核心认知不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 42", "source_state_revision: 43")
    direction = sub_once(direction, "projection_generation: 20260912-direction-026", "projection_generation: 20260912-direction-027")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-QUOTIENT-MONAD` | R041 固定模型的操作闭包（C-71–C-76）、上下文等价层次（C-77–C-83）、商值 continuation 单子（C-84–C-88）与上下文等价完整刻画（C-89–C-91）均已机器闭合；R041 §2.1 在本片段被正面解决（商可分裂）；natural consumer 未找到，保留为重开条件 |",
        "`OUT-TOP-QUOTIENT-MONAD`、`OUT-TOP-NATURAL-CONSUMER-AUDIT` | R041 固定模型的操作闭包（C-71–C-76）、上下文等价层次（C-77–C-83）、商值 continuation 单子（C-84–C-88）与上下文等价完整刻画（C-89–C-91）均已机器闭合；R041 §2.1 在本片段被正面解决（商可分裂）；N1 在有界审计集合内未找到把结果商用于 race/timeout/scheduling 的 natural consumer，重开条件保留为出现未声明该假设的真实接口 |",
    )
    direction = sub_once(
        direction,
        "| `OUT-W-RP-B01`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-TOP-HOTT-RESEARCH-STRATEGY` | 这是战略主线：不再以一般停机定理冒充结果；固定真实 HoTT 计算/提取接口，定位数学分类资格何处被提升为统一有效交付，再与有效自我 ASK 合流 |",
        "| `OUT-W-RP-B01`、`OUT-W-EARLY-EFFECTIVE-CONSTRUCTION`、`OUT-TOP-HOTT-RESEARCH-STRATEGY`、`OUT-TOP-NATURAL-CONSUMER-AUDIT` | 这是战略主线：不再以一般停机定理冒充结果；N1 的有界负结论把下一步固定为 N2 提取接口审计——固定真实对象层→执行层接口，判定它是否把命题 LEM 下的数学分类承诺为统一有效交付，再与有效自我 ASK 合流 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N1 有界自然消费者审计——固定真实 partiality/delay、truncation、univalent transport 与 cost 接口的版本、签名、承诺与调用链，逐条判定是否存在把较弱资格当较强资格的 consumer；找到则进入 F-011 机器化，未找到则给出有界负结论并转 W51×RP-B01 接口构造或 R036/R038 原生升级。",
        "4. **当前第一工作包**：N2 W51×RP-B01 提取接口审计——固定真实对象层→执行层接口（证明助手/编译/提取入口），核对它是否把命题 LEM 下的数学分类承诺为同规格统一有效交付；四组控制：有限步停机检测、经典分支常量、真正停机分类、显式神谕/用户实现；找到候选则进入 F-011 机器化，明确拒绝则记 `DEFENSE_WORKS`，缺源则记 `INCONCLUSIVE_SOURCE_UNAVAILABLE`。",
    )
    direction = sub_once(
        direction,
        "5. **自然桥梁 Gate**：N1 审计实际 HoTT/类型论 consumer 是否把结果商、截断、裸函数、等价存在或在线限制提升成更强资格；已核证据内尚未找到桥梁，继续停在 `DEFENSE_WORKS/REPRESENTATION_BOUNDARY`，找到固定接口再开。",
        "5. **自然桥梁 Gate**：N1 已在固定审计集合内完成（Cubical v0.9 全库 + 四份一手入口），未找到把结果商、截断、裸函数、等价存在或在线限制提升成更强资格的 natural consumer；最近候选均被显式假设、相干数据或类型围栏挡住，保持 `DEFENSE_WORKS/REPRESENTATION_BOUNDARY`，重开条件见审计报告 §6。",
    )
    direction = sub_once(
        direction,
        "6. **战略自反深化**：`DIR-W-RP-B01` × ERCF-3 继续等待自然 consumer；不以一般 Gödel 口号提前启动。",
        "6. **战略自反深化**：N2 先审计 `DIR-W-RP-B01` 的真实对象层→执行层接口（`B01-TARGET`）；ERCF-3 继续等待精确演算与自然 consumer，不以一般 Gödel 口号提前启动。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 42", "source_state_revision: 43")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-026", "projection_generation: 20260912-outcome-027")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_C5_PARADOX_DISTANCE_ASSESSED_NATURAL_CONSUMER_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_RP_B01_EXTRACTION_AUDIT_NEXT",
    )
    audit_row = (
        "| `OUT-TOP-NATURAL-CONSUMER-AUDIT` | N1 有界自然消费者审计——固定审计集合：Cubical v0.9 全库 + Chapman–Uustalu–Veltri / Altenkirch–Danielsson–Kraus / Møgelberg–Zwart / CATT；未找到 E6 consumer；最近候选均被显式假设、相干数据或类型围栏挡住 |"
        " `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-W-RACE-TIMEOUT`、`DIR-W-RP-B01`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工审计 | `DOCUMENTED` / `BOUNDED_NEGATIVE` |"
        " Cubical 身份与十个机器证明相同（tree `73ccfbaf…`）；四份外部入口有 URL/字节/SHA-256；T1–T4 的分类、candidate 表、负结论范围与重开条件已固定 |"
        " 负结论只覆盖本次审计集合与版本；不证明全局不存在 natural consumer；不新增数学 claim |"
        " `audit/natural-consumer审计-20260912.md`；S043 evidence/sources；`理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", audit_row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "C5 综合已完成并判定当前距离为第二级；N1 自然消费者审计、R036/R038 原生升级、R032 回放、B01-TARGET、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "C5 综合已完成并判定当前距离为第二级；N1 已在固定审计集合内给出 bounded negative（未找到 E6 consumer）；N2 W51×RP-B01 提取接口审计、R036/R038 原生升级、R032 回放、B01-TARGET、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "C5 综合评估把当前判词固定在第二级 `REPRESENTATION_BOUNDARY`，并指出唯一决定性缺环是 natural consumer（E6）。",
        "C5 综合评估把当前判词固定在第二级 `REPRESENTATION_BOUNDARY`，并指出唯一决定性缺环是 natural consumer（E6）；N1 在固定审计集合内给出 bounded negative，最近候选均被显式围栏挡住。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N1 有界自然消费者审计 | audit / paper-and-library-evidence | 固定真实 partiality/delay、truncation、univalent transport 与 cost 接口的版本/签名/承诺/调用链；逐条判定是否存在 E6 升级；找到则 F-011 机器化，未找到则有界负结论转 RP-B01/R036-R038 |",
        "| 第一工作包 | N2 W51×RP-B01 提取接口审计 | audit / proof-assistant-and-extraction-evidence | 固定真实对象层→执行层接口，核对它是否把命题 LEM 下的数学分类承诺为同规格统一有效交付；四组控制；找到候选进入 F-011，明确拒绝记 `DEFENSE_WORKS`，缺源记 `INCONCLUSIVE_SOURCE_UNAVAILABLE` |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N1 有界自然消费者审计：固定真实 partiality/delay、truncation、univalent transport 与 cost 接口的版本/签名/承诺/调用链，逐条判定是否存在把较弱资格当较强资格的 consumer；找到则进入 F-011 机器化，未找到则给出有界负结论。",
        "2. 当前第一工作包转为 N2 W51×RP-B01 提取接口审计：固定真实对象层→执行层接口，核对它是否把命题 LEM 下的数学分类承诺为同规格统一有效交付；找到候选进入 F-011，明确拒绝记 `DEFENSE_WORKS`，缺源记 `INCONCLUSIVE_SOURCE_UNAVAILABLE`。",
    )
    memory = sub_once(
        memory,
        "- C5 综合（S042）已评估十包后的悖论距离：仍在 `REPRESENTATION_BOUNDARY`（第二级），唯一决定性缺环是 natural consumer（E6）；下一工作包转为 N1 有界自然消费者审计（paper + 库/论文证据）。",
        "- C5 综合（S042）已评估十包后的悖论距离：仍在 `REPRESENTATION_BOUNDARY`（第二级），唯一决定性缺环是 natural consumer（E6）；下一工作包转为 N1 有界自然消费者审计（paper + 库/论文证据）。\n"
        "- N1 有界自然消费者审计（S043）在固定集合（Cubical v0.9 全库 + 四份一手入口）内未找到 E6：最近候选（`MagicTrick.recover`、`SplitSupport`、`satAC`、delay 商、delay×effects、`uaβ`/SIP、CATT）均被显式假设、相干数据或类型围栏挡住；判定 `BOUNDED_NEGATIVE_MOVE_TO_RP_B01`。",
    )
    memory = sub_once(
        memory,
        "`A-ONLINE-CAUSALITY-FORMAL-001`、`A-C5-PARADOX-DISTANCE-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；C5 已把距离固定在第二级并转 N1 自然消费者审计，不直接跳 ERCF-3。",
        "`A-ONLINE-CAUSALITY-FORMAL-001`、`A-C5-PARADOX-DISTANCE-001`、`A-NATURAL-CONSUMER-AUDIT-001`。五条机器支线（partiality、guard-erasure、cost、路径证书、在线因果）均已闭合；C5 固定第二级距离，N1 已给出 bounded negative 并转 N2 提取接口审计，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S043 完成 N1 有界自然消费者审计：固定集合为 Cubical v0.9 全库 + 四份一手入口；未找到把较弱资格当较强资格的 E6 consumer，最近候选均被显式假设/相干数据/类型围栏挡住；判定 `BOUNDED_NEGATIVE_MOVE_TO_RP_B01`。下一工作包为 N2 W51×RP-B01 提取接口审计；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "41. 十个机器包之后的距离评估把 `NATURAL_USAGE_MISMATCH` 的六要素收敛为 E1–E6：E1–E5 已在固定模型中成立，E6（真实、固定版本、可回查的 natural consumer）是唯一决定性缺环。没有 E6 时只能停在 `REPRESENTATION_BOUNDARY`；审计负结论必须写成“在本次固定的审计集合内未发现”，不得写成“系统中不存在”。",
        "41. 十个机器包之后的距离评估把 `NATURAL_USAGE_MISMATCH` 的六要素收敛为 E1–E6：E1–E5 已在固定模型中成立，E6（真实、固定版本、可回查的 natural consumer）是唯一决定性缺环。没有 E6 时只能停在 `REPRESENTATION_BOUNDARY`；审计负结论必须写成“在本次固定的审计集合内未发现”，不得写成“系统中不存在”。\n"
        "42. N1 的有界审计表明，E6 的缺失既可能来自“没有 consumer”，也可能来自“consumer 被显式围栏”：`SplitSupport`/`satAC` 是显式假设，`MagicTrick.recover` 受依赖余域与类型检查围栏，delay 商受 choice/QIIT 条件约束，效应组合的失败被写成不可分配定理，CATT 是 refinement 而非裸函数恢复。审计必须区分 documented boundary / explicit assumption / type-level fence / refinement interface，并把负结论限定在被审计版本与集合内。",
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
    if state.get("revision") != 42 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_42_AND_S042")
    for required in (AUDIT, C5, TOOLCHAIN, MATRIX, f"{SOURCES}/abstracts.txt"):
        if not (root / required).is_file():
            raise SystemExit(f"REQUIRED_FILE_MISSING:{required}")

    source_files = [
        "abstracts.txt",
        "partiality-revisited.html",
        "monads-extra-pages.html",
        "cost-aware-tt.html",
        "quotienting-delay-monad.html",
        "full-1610.09254.html",
        "full-2011.03660.html",
    ]
    source_hashes = {f"{SOURCES}/{name}": sha(root / SOURCES / name) for name in source_files}
    new_hashes = {
        AUDIT: sha(root / AUDIT),
        C5: sha(root / C5),
        TOOLCHAIN: sha(root / TOOLCHAIN),
        MATRIX: sha(root / MATRIX),
        **source_hashes,
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "natural_consumer_audit",
        "path": AUDIT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "BOUNDED_NEGATIVE_MOVE_TO_RP_B01",
        "full_sources": [AUDIT, C5, TOOLCHAIN, MATRIX] + [f"{SOURCES}/{name}" for name in source_files],
        "source_hashes": {
            AUDIT: new_hashes[AUDIT],
            TOOLCHAIN: new_hashes[TOOLCHAIN],
            MATRIX: new_hashes[MATRIX],
            **source_hashes,
        },
        "resolution": {
            "reason": "Bounded audit over a fixed set: no E6 consumer found; the closest candidates are fenced by explicit assumptions, coherence data or the type checker.",
            "evidence": [AUDIT] + [f"{SOURCES}/{name}" for name in source_files],
        },
        "scope": "Audit Cubical v0.9 plus four primary external sources for a natural consumer that upgrades a weaker qualification to a stronger one. Result: bounded negative (no E6 in the audited set); reopen conditions in the audit report §6. No mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, AUDIT, C5, TOOLCHAIN, MATRIX],
        "source_hashes": {AUDIT: new_hashes[AUDIT], TOOLCHAIN: new_hashes[TOOLCHAIN]},
        "mathematical_status": "NO_NEW_MATHEMATICS_BOUNDED_AUDIT_NEGATIVE",
        "cognition_status": "NATURAL_CONSUMER_AUDIT_BOUNDED_NEGATIVE_AND_RP_B01_INTERFACE_AUDIT_ROUTED",
        "scope": "Run the bounded N1 natural-consumer audit over the fixed set; record the bounded negative and route N2; no claim upgrade.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-027" if rid.startswith("I-DIRECTION") else "20260912-outcome-027"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (AUDIT, f"{SOURCES}/abstracts.txt"):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the bounded N1 natural-consumer audit: no E6 consumer found in the fixed set; "
        "the next work package is the N2 W51xRP-B01 extraction-interface audit."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the bounded N1 natural-consumer audit (no E6 in the audited set); the next strand is N2."
    )

    state["revision"] = 43
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N2: audit the W51xRP-B01 object-layer to execution-layer interfaces. Fix real proof-assistant/compile/extraction entry points, "
            "check whether any of them promises a uniform effective implementation for the propositional-LEM mathematical classifier chi, "
            "and run the four controls from RP-B01 PLAN WP3: bounded-step halt detection, classical branches with equal constants, "
            "the genuinely halting-dependent classifier, and an explicit oracle/user implementation. "
            "If a candidate interface is found, machine-formalize it under F-011; if the interface explicitly refuses or requires an oracle, record DEFENSE_WORKS; "
            "if sources are unavailable, record INCONCLUSIVE_SOURCE_UNAVAILABLE."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "kind": "natural_consumer_audit",
        "new_machine_proofs": [],
        "proof_sources_changed": False,
        "claim_matrix_sha256": new_hashes[MATRIX],
        "older_proof_replays": "NOT_RERUN_IN_S043_NO_PROOF_SOURCE_OR_MATRIX_CHANGE; S041 post-check replays remain authoritative for unchanged hashes",
        "evidence": {"audit": AUDIT, "sources": f"{SOURCES}/", "absolute_paths": ["/Volumes/D/HoTT-toolchain-cache/cubical-v0.9/cubical/"], "relative_paths": [TOOLCHAIN]},
        "mathematics": "NO_NEW_MATHEMATICS / BOUNDED_NEGATIVE_MOVE_TO_RP_B01",
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
            "This in-scope checkpoint records the bounded N1 natural-consumer audit (revision 43), its fixed evidence set, "
            "the bounded negative verdict and the N2 W51xRP-B01 extraction-interface audit route. No mathematical claim is upgraded. "
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
        "revision": 43,
        "session_id": SESSION_ID,
        "audit_sources": len(source_files),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
