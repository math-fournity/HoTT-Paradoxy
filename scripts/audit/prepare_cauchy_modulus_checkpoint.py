#!/usr/bin/env python3
"""Prepare revision 51: record MP-CAUCHY-MODULUS-001 and route the N10 application-layer audit.

N9 built the minimal native Cubical Cauchy-modulus boundary: a quotient by the
eventual value keeps the limit but forgets the modulus carried by the
representation, and no function out of the quotient recovers that modulus
(C-129-C-133).  Verdict: CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS.  The
secondary fixed item (external Real-library interface audit of agda-unimath)
is recorded in the audit document.  The next work package is N10: the
application-layer consumer audit (toolchain plugins / real HoTT application
code delivery-and-computation claims).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-051-CAUCHY-MODULUS"
PREV_SESSION = "S-RES-20260912-050-SIP-REPRESENTATION"
RESULT_ID = "A-CAUCHY-MODULUS-FORMAL-001"
PROOF_ID = "MP-CAUCHY-MODULUS-001"
RUN_ID = "20260912-MP-CAUCHY-MODULUS-001-01"
SOURCE = "HoTT/formal/cauchy-modulus/CauchyModulus.agda"
SOURCE_README = "HoTT/formal/cauchy-modulus/README.md"
TOOLCHAIN = "HoTT/formal/cauchy-modulus/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/cauchy-modulus/AGDA_LIBRARIES"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/cauchy-modulus机器证明实施证据-20260912.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EXTERNAL_SOURCES = [
    f"{SESSION_REL}/evidence/sources/cauchy-sequences-real-numbers.lagda.md",
    f"{SESSION_REL}/evidence/sources/modulated-cauchy-sequences-real-numbers.lagda.md",
    f"{SESSION_REL}/evidence/sources/convergent-sequences-metric-spaces.lagda.md",
    f"{SESSION_REL}/evidence/sources/real-numbers-listing.json",
    f"{SESSION_REL}/evidence/sources/master-commit.json",
]
OLD_RUNS = (
    "20260912-MP-ERCF-001-02", "20260912-MP-ERCF-TRUNC-001-01",
    "20260912-MP-RACE-TIMEOUT-001-01", "20260912-MP-CONTEXTUAL-EQUIV-001-01",
    "20260912-MP-QUOTIENT-MONAD-001-01", "20260912-MP-CONTEXT-CHARACTERIZATION-001-01",
    "20260912-MP-GUARD-ERASURE-001-01", "20260912-MP-COST-FACTORIZATION-001-01",
    "20260912-MP-PATH-CERTIFICATE-001-01", "20260912-MP-ONLINE-CAUSALITY-001-01",
    "20260912-MP-TRANSITION-LIFT-001-01", "20260912-MP-PARTIAL-DECISION-001-01",
    "20260912-MP-SIP-REPRESENTATION-001-01",
)
NEW_STATUS = "CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_cauchy_modulus", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N9 是表示/资格边界而非内部矛盾，符合‘找理论非现实性’而非‘找 HoTT 自相矛盾’的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 N9 中具体化为：按极限值取商的表示是否仍携带 modulus 资格。"),
        "KC-000013": ("DEEPENED", "理论工具性在 N9 中表现为‘取商保留极限值、忘掉 modulus’；细化表示即恢复被删去的区分。"),
        "KC-000014": ("ALIGNED", "方向 B 的交付资格在 Cauchy modulus 表示边界中再获一个机器化实例。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮 Agda 2.8.0/Cubical v0.9 final run exit 0、零 warning、exact replay。"),
        "KC-000024": ("DEEPENED", "Cauchy 常量性 modulus 是‘何时已落定’的表征数据；按极限值取商会忘掉该完成/落定数据。"),
        "KC-000029": ("ALIGNED", "理论经济在表示层的机器化实例：只保留极限值的最小表示丢失 modulus，细化表示可恢复（正控制）。"),
        "KC-000035": ("ALIGNED", "N9 表明 HoTT 能精确表达‘表示丢弃了什么’这一区分；可表达性与覆盖性问题继续保持分开。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N9 不涉及自指反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是 N9 Cauchy modulus 机器边界 + 外部 Real 库接口审计；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S051/SESSION.md；HoTT/formal/cauchy-modulus/CauchyModulus.agda | N10、ERCF-3 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N9 完成并判 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`；第一工作包转 N10 应用层消费者审计；revision 51/generation 035。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-CAUCHY-MODULUS`。",
        "- update_decision: `MP-CAUCHY-MODULUS-001 进入 formal/run/index/STATE；C-129–C-133 进入 claim matrix；十三个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十四个 proof 包在同一矩阵上全部通过验证；外部 Real 库接口与本地边界方向一致。",
        "- unresolved: `N10 应用层审计、ERCF-3 前置、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S050 后的 N9 工作包（Cauchy modulus 边界 + 外部 Real 库接口固定审计子项）。",
        "- 构造：`Seq = ℕ → Bool`；`Cauchy = Σ s, Σ N, (∀ n → le N n → s n ≡ s N)`；`mod c`、`lim c = seq c (mod c)`；`c0=(constTrue,0,·)`、`c1=(constTrue,1,·)`；`Q = Cauchy / (lim c ≡ lim d)`；细化 `Q' = Cauchy / ((mod c ≡ mod d) × (lim c ≡ lim d))`。",
        "- 结果：`MP-CAUCHY-MODULUS-001`（C-129–C-133）通过 kernel：limit 下降到商（C-129）；两表示被识别而 modulus 不同（C-130）；无统一 modulus 恢复函数（C-131）；细化同一性后 modulus 下降（C-132，正控制）；细化关系不再识别两表示（C-133）。判词 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`（非悖论）。",
        "- 运行：final run `20260912-MP-CAUCHY-MODULUS-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`），零 warning，stdout 11,347 bytes、stderr 0 bytes。",
        "- 旧证据：矩阵第十二次增长后，十三个旧包全部重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH`（其中 ERCF-001、ERCF-TRUNC-001、RACE-TIMEOUT-001 在批量输出不可完整捕获后按单包补证）。",
        "- 外部审计：UniMath/agda-unimath `master` @ `6dc2d58a35d256978aeccb987eb92b9b11ed613a`；`cauchy-sequences-real-numbers.lagda.md`（blob `2974eb40…`，7,498 bytes）Idea 明确 convergence modulus ⇔ Cauchy，完备性定理 `opaque`，夹逼定理从显式 `c-a→0` 析出 modulus；另有 `modulated-cauchy-sequences-real-numbers.lagda.md`（blob `b9f448dc…`）把 modulus 作为结构数据。原件与哈希存于本 Session `evidence/sources/`。",
        "- 失败谱系：`_≤_` 与 `Cubical.Data.Bool.Properties` 的 Bool 序同名（库第 243 行）→ 界谓词改名 `le`；`SQ-rec` 第一参数是目标 set-ness（库签名 `rec : isSet B → …`）→ 改用 `isSetBool`/`isSetℕ`；命题未削弱。",
        "- 边界：不构造完整 Cauchy reals/Real 库、不形式化十进制展开、不主张真实库误用、不主张原创性。",
        "- 三件套：direction/panorama revision 51/generation 035；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT`",
        "状态：`CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 50", "source_state_revision: 51")
    direction = sub_once(direction, "projection_generation: 20260912-direction-034", "projection_generation: 20260912-direction-035")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT",
        "semantic_status: CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT",
    )
    direction = sub_once(
        direction,
        "；`MP-SIP-REPRESENTATION-001` 原生给出 SIP/UA 替换许可的最小边界（`C-124`–`C-128`）。",
        "；`MP-SIP-REPRESENTATION-001` 原生给出 SIP/UA 替换许可的最小边界（`C-124`–`C-128`）；`MP-CAUCHY-MODULUS-001` 原生给出 Cauchy modulus 表示边界与细化正控制（`C-129`–`C-133`）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N9 Cauchy modulus 边界——在同一工具链中固定 Cauchy 序列/等价的最小模型；证明商层不能统一恢复 modulus（或在无 modulus 数据时不能输出指定的界/十进制观察量）；给出携带 modulus 的细化表示正控制；并把可得的外部 Real 库接口作为固定审计子项；预期最多 `REPRESENTATION_BOUNDARY`；若只是重述 N6 partial/strict 形状则停止并转应用层审计。",
        "4. **当前第一工作包**：N10 应用层消费者审计——在固定集合与版本内审计真实 HoTT/类型论应用代码或工具链插件，检查是否存在把较弱资格（商、截断、等价存在、表示数据缺失）当作交付/计算承诺的 natural consumer；给出每个来源的实际假设、类型围栏与承诺面；预期最多维持 `REPRESENTATION_BOUNDARY`；若只重述已有 defense/boundary 则停止并转 ERCF-3 前置评估。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT`",
        "状态：`CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 50", "source_state_revision: 51")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-034", "projection_generation: 20260912-outcome-035")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_SIP_REPRESENTATION_PROVED_CAUCHY_MODULUS_NEXT",
        "semantic_status: CORE_GENERATION_4_CAUCHY_MODULUS_PROVED_APPLICATION_LAYER_AUDIT_NEXT",
    )
    row = (
        "| `OUT-TOP-CAUCHY-MODULUS` | `MP-CAUCHY-MODULUS-001`：Cauchy modulus 表示边界——按极限值取商保留 limit（`C-129`）；两个 modulus 不同的常量真序列表示被识别（`C-130`）；不存在从商统一恢复给定 modulus 的函数（`C-131`）；把 modulus 纳入同一性判据后可以下降（`C-132`，正控制）；细化关系不再识别两表示（`C-133`） |"
        " `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 + 外部 Real 库接口审计 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0（零 warning）、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；十三个旧包 row-stable + exact replay；agda-unimath master 固定审计显示 modulus 为显式结构数据 |"
        " 不构造完整 Cauchy reals/Real 库、不形式化十进制展开、不证明真实库误用、不主张原创性或 HoTT 内部矛盾 |"
        " `HoTT/formal/cauchy-modulus/`；final run `20260912-MP-CAUCHY-MODULUS-001-01`；claim matrix C-129–C-133；`audit/cauchy-modulus机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N8 SIP/表示消费者机器构造已机器闭合（C-124–C-128）；N9 Cauchy modulus 边界、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N8 SIP/表示消费者机器构造（C-124–C-128）与 N9 Cauchy modulus 表示边界（C-129–C-133，含外部 Real 库接口审计）均已机器闭合；R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N8 把 SIP/UA 替换许可做成最小机器边界（C-124–C-128，零 warning），判 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。所有新结论继续执行 F-011。",
        "N8 把 SIP/UA 替换许可做成最小机器边界（C-124–C-128，零 warning），判 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`；N9 把 Cauchy modulus 表示边界做成最小机器构造（C-129–C-133，零 warning，附外部 Real 库接口审计），判 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N9 Cauchy modulus 边界 | formal / native Cubical Agda + external-library audit | 最小 Cauchy 序列/等价模型；商层不能统一恢复 modulus；携带 modulus 的细化表示正控制；外部 Real 库接口审计；预期最多 `REPRESENTATION_BOUNDARY` |",
        "| 已闭合工作包 9 | Cauchy modulus 表示边界（`C-129`–`C-133`） | machine-proved-local-uncommitted / `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS` | 按极限值取商保留 limit、忘掉 modulus；统一恢复不存在；把 modulus 纳入同一性即可下降（正控制）；外部 agda-unimath 接口审计一致 |\n"
        "| 第一工作包 | N10 应用层消费者审计 | audit / fixed-set application-layer scan | 固定集合与版本内审计真实应用代码/工具链插件的交付与计算承诺；预期最多维持 `REPRESENTATION_BOUNDARY`；只重述已有 defense 则停止并转 ERCF-3 前置评估 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N9 Cauchy modulus 边界：在同一工具链中固定 Cauchy 序列/等价的最小模型；证明商层不能统一恢复 modulus（或无 modulus 数据时不能输出指定界/十进制观察量）；给出携带 modulus 的细化表示正控制；并把可得的 Real 库接口作为固定审计子项；预期最多 `REPRESENTATION_BOUNDARY`。",
        "2. 当前第一工作包转为 N10 应用层消费者审计：在固定集合与版本内审计真实 HoTT/类型论应用代码或工具链插件，检查是否存在把较弱资格（商、截断、等价存在、表示数据缺失）当作交付/计算承诺的 natural consumer；记录每个来源的实际假设与类型围栏；预期最多维持 `REPRESENTATION_BOUNDARY`；若只重述已有 defense/boundary 则停止并转 ERCF-3 前置评估。",
    )
    memory = sub_once(
        memory,
        "- N8 SIP/UA 替换许可边界（S050）已由 `MP-SIP-REPRESENTATION-001` 原生机器化：C-124–C-128，零 warning、exact replay；十二个旧包在矩阵增长后全部 row-stable；判词 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。",
        "- N8 SIP/UA 替换许可边界（S050）已由 `MP-SIP-REPRESENTATION-001` 原生机器化：C-124–C-128，零 warning、exact replay；十二个旧包在矩阵增长后全部 row-stable；判词 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。\n"
        "- N9 Cauchy modulus 表示边界（S051）已由 `MP-CAUCHY-MODULUS-001` 原生机器化：C-129–C-133，零 warning、exact replay；十三个旧包在矩阵增长后全部 row-stable；外部 agda-unimath 接口审计与边界方向一致；判词 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。",
    )
    memory = sub_once(
        memory,
        "`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`、`A-SIP-REPRESENTATION-FORMAL-001`。八条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision、SIP/表示）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成距离综合，N8 关闭 SIP/表示边界并转 N9 Cauchy modulus，不直接跳 ERCF-3。",
        "`A-PARTIAL-DECISION-FORMAL-001`、`A-POST-N6-DISTANCE-001`、`A-SIP-REPRESENTATION-FORMAL-001`、`A-CAUCHY-MODULUS-FORMAL-001`。九条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision、SIP/表示、Cauchy modulus）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界，N7 完成距离综合，N8 关闭 SIP/表示边界，N9 关闭 Cauchy modulus 表示边界并转 N10 应用层消费者审计，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S051 完成 N9：`MP-CAUCHY-MODULUS-001`（C-129–C-133）在 Agda 2.8.0/Cubical v0.9 下原生机器化 Cauchy modulus 表示边界，零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay；十三个旧包在矩阵增长后全部 row-stable；外部 agda-unimath 接口审计（master @ `6dc2d58a…`）显示 convergence modulus/modulated Cauchy 序列为显式结构数据，与 C-131/C-132 方向一致。判词 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。下一工作包为 N10 应用层消费者审计；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "49. 最小 SIP 边界可以用 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 手写，不需要完整 SIP 模块；关键是把“签名外观察量”写成需要额外表示数据（carrier 是 Bool）的值，而不是伪装成 `Str → Bool` 全函数。正控制则是把观察量加入签名，使识别不再成立。",
        "49. 最小 SIP 边界可以用 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 手写，不需要完整 SIP 模块；关键是把“签名外观察量”写成需要额外表示数据（carrier 是 Bool）的值，而不是伪装成 `Str → Bool` 全函数。正控制则是把观察量加入签名，使识别不再成立。\n"
        "50. 最小 Cauchy modulus 边界显示“按极限值取商”与“保留给定 modulus”是两个不同承诺：`ℕ → Bool` 序列加 `Σ N` 常量性数据就足以证明商层识别 `(constTrue,0)`/`(constTrue,1)` 而 modulus 不可统一恢复；把 modulus 纳入同一性关系即得正控制。外部 agda-unimath 把 convergence modulus 与 modulated Cauchy 序列写成显式结构、完备性定理 `opaque`，与该边界方向一致；引用外部接口时必须绑定抓取提交与 blob hash，且不得由接口形状推断某个具体使用已经出错。",
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
    if state.get("revision") != 50 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_50_AND_S050")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(129, 134)]
    ):
        raise SystemExit("FINAL_RUN_NOT_ACCEPTED_AND_INDEXED")
    for required in ("index-row-manifest.json", "source-manifest.json", "stdout.txt", "stderr.txt", "environment.txt"):
        if not (run_dir / required).is_file():
            raise SystemExit(f"RUN_FILE_MISSING:{required}")
    for rel in EXTERNAL_SOURCES:
        if not (root / rel).is_file():
            raise SystemExit(f"EXTERNAL_SOURCE_MISSING:{rel}")

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
    note = (
        "After C-129 through C-133 were appended (S051), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with "
        "EXACT_EXIT_STDOUT_STDERR_MATCH for the thirteen older packages."
    )
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
        "classification": "CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(129, 134)],
        "run_id": RUN_ID,
        "mathematical_status": "MINIMAL_NATIVE_CAUCHY_MODULUS_REPRESENTATION_BOUNDARY",
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
            *EXTERNAL_SOURCES,
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE], SOURCE_README: new_hashes[SOURCE_README],
            TOOLCHAIN: new_hashes[TOOLCHAIN], LIBRARIES: new_hashes[LIBRARIES],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX], AUDIT_DOC: new_hashes[AUDIT_DOC],
            **{rel: sha(root / rel) for rel in EXTERNAL_SOURCES},
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0 with zero warnings; source, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX, "scripts/audit/verify_formal_proof_run.py", AUDIT_DOC,
            ],
        },
        "scope": "Minimal native Cubical Cauchy-modulus boundary: the quotient by equality of the limit admits a limit function (C-129); (constTrue,0) and (constTrue,1) are identified while their moduli differ (C-130); no function out of the quotient uniformly recovers the given modulus (C-131); refining the identity relation to include the modulus yields a modulus function on the refined quotient (C-132) and the two representations are not related (C-133). Boundary result with positive controls plus a bounded external agda-unimath interface audit; not a HoTT paradox.",
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
                         "scripts/audit/prepare_cauchy_modulus_checkpoint.py", *EXTERNAL_SOURCES],
        "source_hashes": {SOURCE: new_hashes[SOURCE],
                          f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
                          AUDIT_DOC: new_hashes[AUDIT_DOC],
                          **{rel: sha(root / rel) for rel in EXTERNAL_SOURCES}},
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_CAUCHY_MODULUS",
        "cognition_status": "CAUCHY_MODULUS_BOUNDARY_PROVED_AND_APPLICATION_LAYER_AUDIT_ROUTED",
        "scope": "Native Cubical Cauchy-modulus boundary (C-129-C-133), revalidation of thirteen older packages, bounded external agda-unimath interface audit, and routing of the N10 application-layer audit.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-035" if rid.startswith("I-DIRECTION") else "20260912-outcome-035"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                    f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the native Cauchy-modulus boundary: the modulus-representation boundary is machine-proved; the first work package is the N10 application-layer consumer audit."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the native Cauchy-modulus boundary (C-129-C-133) with a bounded external Real-library interface audit; the next strand is N10."
    )

    state["revision"] = 51
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N10: application-layer consumer audit. In a fixed set of versions, scan real HoTT/type-theory application code or toolchain plugins for natural consumers "
            "that turn a weaker qualification (quotient, truncation, mere existence, missing representation data) into a delivery-or-computation claim; record each source's actual assumptions, "
            "type fences and promise surface. Expected verdict at most REPRESENTATION_BOUNDARY. If the audit only re-derives existing defense/boundary shapes, stop and move to the ERCF-3 prerequisite assessment."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(129, 134)],
        "final_run": {
            "run_id": RUN_ID,
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
            "warnings": 0,
            "stdout_bytes": 11347,
            "stderr_bytes": 0,
        },
        "older_proofs_after_matrix_growth": {
            rid: "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH"
            for rid in OLD_RUNS
        },
        "older_proofs_verification_note": (
            "Ten row-stable lines were captured in the batch replay session; ERCF-001, ERCF-TRUNC-001 and RACE-TIMEOUT-001 were re-verified individually "
            "with the same result after the batch session output could not be fully captured."
        ),
        "external_audit": {
            "repository": "UniMath/agda-unimath",
            "ref": "master",
            "commit": "6dc2d58a35d256978aeccb987eb92b9b11ed613a",
            "files": {
                "src/real-numbers/cauchy-sequences-real-numbers.lagda.md": {
                    "blob": "2974eb40a9cbaf804405588d4650fd2ecb43b65e",
                    "bytes": 7498,
                },
                "src/real-numbers/modulated-cauchy-sequences-real-numbers.lagda.md": {
                    "blob": "b9f448dc1f1c5c160f3021607d37bba7fcd47c8d",
                    "bytes": 1128,
                },
                "src/metric-spaces/convergent-sequences-metric-spaces.lagda.md": {
                    "blob": "474a9c7325f31349eefad2d5a2b16e170377acc4",
                    "bytes": 2848,
                },
            },
            "scope": "Bounded interface-shape audit; the moving master ref is pinned by the recorded commit; no claim about any concrete library misuse.",
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX,
                     "external_sources": EXTERNAL_SOURCES},
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS",
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
            "This in-scope checkpoint records the native Cauchy-modulus package MP-CAUCHY-MODULUS-001 (C-129-C-133), "
            "repairs the source hashes changed by the claim-matrix growth, and routes the N10 application-layer audit. "
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
        "revision": 51,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
