#!/usr/bin/env python3
"""Prepare revision 55: record the W51xRP-B01 propositionalisation and route N11.

S055 (A11.1) fixed the W51 proposition in three strengths (W51-1 local
classical separation, W51-2 generic inheritance boundary, W51-3 HoTT-specific
natural-lift mismatch) and mapped RP-B01's B01-M/B01-E/B01-TARGET onto the
repo's machine evidence.  Verdict: W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT;
A11.1 and DIR-W-RP-B01 stay PARKED with exact reopen conditions.  The next
work package is N11: A-direction candidate generation.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-055-W51-RPB01-PROPOSITIONALISATION"
PREV_SESSION = "S-RES-20260912-054-ERCF3-T2-ENCODING-ROUTE"
RESULT_ID = "A-W51-RPB01-MAPPING-001"
C9 = "理解章节/C9-W51命题化与RP-B01层映射-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RP_CONSTRUCTION = f"{SESSION_REL}/evidence/rp-b01/CONSTRUCTION.md"
RP_PLAN = f"{SESSION_REL}/evidence/rp-b01/PLAN.md"
RP_CLAIMS = f"{SESSION_REL}/evidence/rp-b01/CLAIMS.json"
EVIDENCE = [RP_CONSTRUCTION, RP_PLAN, RP_CLAIMS]
NEW_STATUS = "W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_w51_rpb01", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "C9 继续区分理论非现实性与内部矛盾，不把通用边界写成 HoTT 悖论。"),
        "KC-000012": ("DEEPENED", "ASK 的资格预分析在 C9 中落到 chi/Rep 的具体词表上。"),
        "KC-000013": ("ALIGNED", "理论工具性经济在 C9 中体现为 M 层分类与 E 层交付的分离。"),
        "KC-000022": ("DEEPENED", "用户的两类现实相对悖论在 C9 中被重新表述为 W51-1/W51-2/W51-3 三个强度。"),
        "KC-000023": ("ALIGNED", "‘HoTT 的问题应该不难定位’由 C9 给出精确回答：定位到 B01-TARGET 这一唯一开放层。"),
        "KC-000026": ("ALIGNED", "自指怀疑与 W51 继承读法在 C9 中被区分为不同层，不互相冒充。"),
        "KC-000027": ("DEEPENED", "W51 原文在 C9 中完成命题化：三个强度、层映射与第三层验收四条件。"),
        "KC-000030": ("ALIGNED", "理论经济学的问题在 C9 中保持为方向，不冒充已证结论。"),
        "KC-000035": ("ALIGNED", "HoTT 能否表达本项目理论的问题保持开放；C9 只映射 RP-B01 层与证据。"),
        "KC-000036": ("ALIGNED", "哥德尔/自馈问题在 C9 中保持通用边界判定，ERCF-3 与 W51-3 继续 gated。"),
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
            ("NOT_TOUCHED", "本轮是 S055 W51 命题化与 RP-B01 层映射；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S055/SESSION.md；{C9} | N11 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — A11.1 命题化完成；第一工作包转 N11（A 方向候选生成）；DIR-W-RP-B01 保持 PARKED 且重开条件精确化；revision 55/generation 039。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-W51-RPB01-MAPPING`；理解章节 inventory 更新为 34/24（C0–C9）。",
        "- update_decision: `C9 进入 理解章节 与 merge manifest；RP-B01 三份原件归档到 session evidence；不新增 claim matrix 行。`",
        "- cross_conflicts: `NONE_OBSERVED` — C9 与 C4 §13、C8、RP-B01 §7 一致（通用边界 + 缺 natural consumer）；A11 正文保持历史快照，当前状态由本文与三件套/STATE 承担。",
        "- unresolved: `N11 候选矩阵、B01-TARGET、ERCF-3 P8、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S054 路由的第一工作包 A11.1（W51×RP-B01 命题化）。",
        "- 产出：`理解章节/C9-W51命题化与RP-B01层映射-20260912.md`——W51 三强度命题化（W51-1 局部分离 / W51-2 一般继承边界 / W51-3 HoTT 特有自然使用失配）、RP-B01 三层（B01-M/B01-E/B01-TARGET）与本 repo 机器证据的逐项映射、第三层验收四条件与判词阶梯、重开条件。",
        "- 判定：`W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT`；A11.1 与 DIR-W-RP-B01 保持 PARKED（重开条件按 C9 §4 四条件）；W51-1 的抽象核由 S053 T1 探针与 MP-ERCF-001（C-59–C-66）机器证据支撑，chi/Rep 具体实例仍为纸笔（RP-B01 PLAN WP1/WP2）。",
        "- 证据：RP-B01 三份原件（CONSTRUCTION.md/PLAN.md/CLAIMS.json）归档副本进 session evidence；原件 hash 与副本一致。",
        "- 治理联动：C9 新增 → merge manifest 重建 34/24（top-level unique 10、nonidentical 19、unresolved 0）；A11 正文保持历史快照（分类器对非 B 系列文件的差异 fail closed），当前状态由 C9/三件套/STATE 承担。",
        "- 边界：不新增数学 claim；不追认 RP-B01 历史自述为机器结果；W51-2 只作为标准结果读法记录。",
        "- 三件套：direction/panorama revision 55/generation 039；core 不变。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT`",
        "状态：`CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 54", "source_state_revision: 55")
    direction = sub_once(direction, "projection_generation: 20260912-direction-038", "projection_generation: 20260912-direction-039")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT",
        "semantic_status: CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT",
    )
    direction = sub_once(
        direction,
        "`OUT-TOP-NATURAL-CONSUMER-AUDIT`、`OUT-TOP-RP-B01-EXTRACTION-AUDIT` | N2 在被审计接口（Agda MAlonzo、Lean 求值/编译）上判 scoped `DEFENSE_WORKS`：postulate 生成 `error \"postulate evaluated\"`，noncomputable 定义被求值拒绝，Prop→Bool 大消去被内核拒绝；未找到把 LEM 分类承诺为统一有效交付的自然接口；重开条件为新版本/后端默认交付实现或出现实际消费者 |",
        "`OUT-TOP-NATURAL-CONSUMER-AUDIT`、`OUT-TOP-RP-B01-EXTRACTION-AUDIT`、`OUT-TOP-W51-RPB01-MAPPING` | N2 在被审计接口（Agda MAlonzo、Lean 求值/编译）上判 scoped `DEFENSE_WORKS`：postulate 生成 `error \"postulate evaluated\"`，noncomputable 定义被求值拒绝，Prop→Bool 大消去被内核拒绝；S055 完成 W51 命题化与 RP-B01 层映射（C9）：W51-1 抽象核有机器证据、W51-2 为通用边界、W51-3（`B01-TARGET`）保持 OPEN；第三层验收四条件与重开条件已固定 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：A11.1 W51×RP-B01 命题化——把 W51 命题（“HoTT 作为逻辑+几何+程序的系统继承而非豁免程序的计算界限”）写成精确命题，与 RP-B01 的已证/未证层（含 `MP-ERCF-001` 骨架与 N2 提取接口审计）逐项对应，并固定第三层（自然 Think-in-HoTT 交付提升）的缺口与验收判据；若只是通用边界重述则保持 `PARKED`。备选（ERCF 线）：T4 第五层 consumer 审计。",
        "4. **当前第一工作包**：N11 新候选生成（A 方向优先）——以 N1–N10、C8、C9 的教训为输入，生成 A 方向（现实可完成、Think in HoTT 呈现额外完成困难）候选矩阵；每个候选必须写明关键步骤由哪条 HoTT 特有规则（`ua`/`Id`/HIT/truncation/高阶相干）承担，以及可机器化的最小判别任务与停止条件；若全部候选只是通用边界/表示限制的重述，记录 `A_DIRECTION_BOUNDED_NEGATIVE` 并转回证据队列。备选（ERCF 线）：T4 第五层 consumer 审计。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT`",
        "状态：`CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 54", "source_state_revision: 55")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-038", "projection_generation: 20260912-outcome-039")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT",
        "semantic_status: CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT",
    )
    row = (
        "| `OUT-TOP-W51-RPB01-MAPPING` | S055 W51 命题化与 RP-B01 层映射——W51 三强度（W51-1 局部分离；W51-2 一般继承边界；W51-3 HoTT 特有自然使用失配）；RP-B01 的 `B01-M`/`B01-E`/`B01-TARGET` 与 `MP-ERCF-001`（C-59–C-66）、S053 T1 对角核、N2 提取接口审计逐项映射；第三层验收四条件与判词阶梯固定 |"
        " `DIR-W-RP-B01`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工综合 + RP-B01 源记录重读 | `DOCUMENTED / W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT` |"
        " W51-1 抽象核有机器证据；W51-2 为通用边界；W51-3（=E6）保持 OPEN；A11.1/DIR-W-RP-B01 保持 PARKED 且重开条件精确 |"
        " 不新增数学 claim；不追认 RP-B01 历史纸笔推导为机器结果；不把通用边界写作 HoTT 特有悖论 |"
        " `理解章节/C9-W51命题化与RP-B01层映射-20260912.md`；S055 evidence/rp-b01；C4 §13；N2 审计 |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "两个理解章节目录当前为 33/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C8 共 9 个独有文件（nonidentical union entries=18）；逐文件处置已生成",
        "两个理解章节目录当前为 34/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C9 共 10 个独有文件（nonidentical union entries=19）；逐文件处置已生成",
    )
    panorama = sub_once(
        panorama,
        "C3/C4/C5/C6/C7/C8 为 top-level current AI strategy/research synthesis",
        "C3/C4/C5/C6/C7/C8/C9 为 top-level current AI strategy/research synthesis",
    )
    panorama = sub_once(
        panorama,
        "S054 完成 T2 编码路线实验（路线 (a)，纯 Agda builtins，无新增层级）并转 A11.1 命题化；R032 回放、",
        "S054 完成 T2 编码路线实验（路线 (a)，纯 Agda builtins，无新增层级）；S055 完成 W51 命题化与 RP-B01 层映射（C9：W51-1 抽象核有机器证据、W51-2 通用边界、W51-3 保持 OPEN）；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S054 完成 T2 编码路线实验（路线 (a)，纯 Agda builtins，无 cubical 特征），P2/P3 语法层不需要新增层级。所有新结论继续执行 F-011。",
        "S054 完成 T2 编码路线实验（路线 (a)，纯 Agda builtins，无 cubical 特征），P2/P3 语法层不需要新增层级；S055 完成 W51 命题化与 RP-B01 层映射（W51-1 抽象核有机器证据、W51-2 通用边界、W51-3 保持 OPEN）。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | A11.1 W51×RP-B01 命题化 | paper + 证据映射 | W51 写成精确命题并与 RP-B01 已证/未证层逐项对应；固定第三层缺口与验收判据；无进展则保持 PARKED；备选 T4 |",
        "| 已闭合工作包 13 | W51×RP-B01 命题化（S055） | synthesis + source remap | 三强度命题化（W51-1/2/3）；B01-M/E/TARGET 与本 repo 机器证据逐项映射；第三层验收四条件固定；A11.1 保持 PARKED |\n"
        "| 第一工作包 | N11 新候选生成（A 方向优先） | candidate matrix + stop conditions | 每个候选写明 HoTT 特有规则参与的关键步骤与可机器化判别任务；若全是通用边界/表示限制重述则记录 `A_DIRECTION_BOUNDED_NEGATIVE` 并转证据队列 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 A11.1 W51×RP-B01 命题化：把 W51 命题写成精确命题，与 RP-B01 的已证/未证层逐项对应，并固定第三层（自然 Think-in-HoTT 交付提升）的缺口与验收判据；若只是通用边界重述则保持 `PARKED`。备选（ERCF 线）：T4 第五层 consumer 审计。",
        "2. 当前第一工作包转为 N11 新候选生成（A 方向优先）：以 N1–N10、C8、C9 的教训为输入，生成 A 方向候选矩阵；每个候选必须写明关键步骤由哪条 HoTT 特有规则（ua/Id/HIT/truncation/高阶相干）承担，以及可机器化的最小判别任务与停止条件；若全部候选只是通用边界/表示限制的重述，记录 `A_DIRECTION_BOUNDED_NEGATIVE` 并转回证据队列。备选（ERCF 线）：T4 第五层 consumer 审计。",
    )
    memory = sub_once(
        memory,
        "- S054 完成 T2 编码路线实验：",
        "- S055 完成 W51 命题化与 RP-B01 层映射：`理解章节/C9-W51命题化与RP-B01层映射-20260912.md` 给出 W51 三强度（W51-1 局部分离 / W51-2 一般继承边界 / W51-3 HoTT 特有自然使用失配）、RP-B01 的 B01-M/B01-E/B01-TARGET 与本 repo 机器证据的逐项映射、第三层验收四条件与判词阶梯；判词 `W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT`；A11.1 与 DIR-W-RP-B01 保持 PARKED；merge manifest 重建 34/24；下一工作包转 N11（A 方向候选生成）。\n"
        "- S054 完成 T2 编码路线实验：",
    )
    memory = sub_once(
        memory,
        "`A-ERCF3-T2-ENCODING-ROUTE-001`。",
        "`A-ERCF3-T2-ENCODING-ROUTE-001`、`A-W51-RPB01-MAPPING-001`。",
    )
    memory = sub_once(
        memory,
        "S054 完成 T2 编码路线实验（路线 (a) 可行，语法层不需要新增层级）并转 A11.1 命题化，不直接跳 ERCF-3 构造。",
        "S054 完成 T2 编码路线实验（路线 (a) 可行，语法层不需要新增层级）；S055 完成 W51 命题化与 RP-B01 层映射并把 A11.1 保持 PARKED，转 N11（A 方向候选生成），不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S055 完成 A11.1：`理解章节/C9-W51命题化与RP-B01层映射-20260912.md` 把 W51 拆成三强度（W51-1 局部分离、W51-2 一般继承边界、W51-3 HoTT 特有自然使用失配），把 RP-B01 的 B01-M/B01-E/B01-TARGET 映射到 `MP-ERCF-001`（C-59–C-66）、S053 T1 对角核与 N2 提取接口审计，并固定第三层验收四条件与判词阶梯。判词 `W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT`；A11.1 与 DIR-W-RP-B01 保持 PARKED；merge manifest 重建 34/24。下一工作包为 N11（A 方向候选生成，要求 HoTT 特有规则参与关键步骤）；备选 T4。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "53. 前置任务的“同层可行性”应先用最弱载体检验：",
        "54. 把方向性判断（如 W51“HoTT 对齐程序后继承程序界限”）命题化时，必须拆成可分别判定的强度：局部分离（有机器抽象核）、一般继承边界（通用 Turing/Gödel 型，不依赖目标理论特有规则）、以及特有使用失配（需要真实接口）。前两者成立不构成悖论候选；只有第三层（=E6/B01-TARGET）满足四条件（真实性、资格越级、无新增假设、可核查性）才允许升级。历史上的“双方都同意”或“纸笔推导”不能被追认为机器结果；源记录重读时同时给出 hash 与归档副本。\n"
        "53. 前置任务的“同层可行性”应先用最弱载体检验：",
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
    if state.get("revision") != 54 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_54_AND_S054")
    if not (root / C9).is_file():
        raise SystemExit(f"C9_MISSING:{C9}")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}
    new_hashes[C9] = sha(root / C9)
    new_hashes[MERGE_MANIFEST] = sha(root / MERGE_MANIFEST)

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README, MERGE_MANIFEST, C9})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S055 W51xRP-B01 propositionalisation: C9 was added and the understanding-chapter merge manifest "
        "was rebuilt (34/24); no proof source, run or claim-matrix row changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "research_synthesis",
        "path": C9,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-HOTT-SELF-VALIDATION-ECONOMY-001", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [C9, *EVIDENCE, MERGE_MANIFEST,
                         "HoTT/formal/ercf-factorization/ERCF.lean",
                         "audit/rp-b01-extraction-interface审计-20260912.md",
                         "scripts/audit/prepare_w51_rpb01_checkpoint.py"],
        "source_hashes": {C9: new_hashes[C9], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "resolution": {
            "reason": "W51 was propositionalised in three strengths and RP-B01's layers were mapped onto the repo's machine evidence; third-layer acceptance conditions fixed. Verdict: W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT; A11.1 stays PARKED.",
            "evidence": [C9, RP_CONSTRUCTION, MERGE_MANIFEST],
        },
        "scope": "W51xRP-B01 propositionalisation: three strengths (W51-1 local classical separation with machine-backed abstract core; W51-2 generic inheritance boundary; W51-3 HoTT-specific natural-lift mismatch, open), layer mapping B01-M/B01-E/B01-TARGET, and the four acceptance conditions plus verdict ladder for the third layer. No new mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C9, *EVIDENCE,
                         MERGE_MANIFEST, "scripts/audit/prepare_w51_rpb01_checkpoint.py"],
        "source_hashes": {C9: new_hashes[C9], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_W51_PROPOSITIONALISATION",
        "cognition_status": "W51_PROPOSITIONALISED_AND_N11_ROUTED",
        "scope": "W51xRP-B01 propositionalisation with RP-B01 source remap and routing of the N11 A-direction candidate generation.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-039" if rid.startswith("I-DIRECTION") else "20260912-outcome-039"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (C9, MERGE_MANIFEST):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the W51xRP-B01 propositionalisation: A11.1 stays PARKED with exact reopen conditions; the first work package is the N11 A-direction candidate generation."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the W51xRP-B01 propositionalisation (W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT); the next strand is N11."
    )

    state["revision"] = 55
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N11: A-direction candidate generation. Using the lessons of N1-N10, C8 and C9, generate a candidate matrix for direction A (reality can complete; Think-in-HoTT introduces an extra completion difficulty). "
            "Each candidate must state which HoTT-specific rule (ua/Id/HIT/truncation/higher coherence) carries the critical step, plus a minimal machine-checkable discriminating task and stop condition. "
            "If every candidate merely re-states a generic boundary or a representation limit, record A_DIRECTION_BOUNDED_NEGATIVE and return to the evidence queue. Fallback (ERCF line): T4 fifth-layer consumer audit."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "synthesis_kind": "w51_rpb01_propositionalisation",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "strengths": {
            "W51-1": "local classical separation: chi has a mathematical specification and no oracle-free effective total implementation; abstract core machine-backed (S053 T1 probe, MP-ERCF-001 C-59-C-66); concrete chi/Rep formalisation NOT_RUN",
            "W51-2": "generic inheritance boundary (Turing/Goedel-type reading; not a new theorem of this repo; does not depend on HoTT-specific rules)",
            "W51-3": "HoTT-specific natural-lift mismatch (= B01-TARGET = E6); OPEN, no candidate found in N1/N2/N5/N10",
        },
        "layer_mapping": {"B01-M": "paper + general factorisation core machine-proved", "B01-E": "paper diagonal + abstract diagonal core machine-proved", "B01-TARGET": "OPEN"},
        "acceptance_conditions_fixed": 4,
        "verdict": "W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT",
        "understanding_merge": {"top_level_files": 34, "nested_files": 24, "union_files": 34,
                                "top_level_unique": 10, "nonidentical_union_entries": 19,
                                "unresolved_nontrivial": 0},
        "source_remap": {"CONSTRUCTION.md": new_hashes[RP_CONSTRUCTION], "PLAN.md": new_hashes[RP_PLAN], "CLAIMS.json": new_hashes[RP_CLAIMS]},
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"synthesis": C9, "session_evidence": f"{SESSION_REL}/evidence/"},
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
            "This in-scope checkpoint records the W51xRP-B01 propositionalisation (three strengths, layer mapping, third-layer acceptance conditions), "
            "adds C9 to the understanding chapters, rebuilds the merge manifest, and routes the N11 A-direction candidate generation. "
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
        "revision": 55,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
