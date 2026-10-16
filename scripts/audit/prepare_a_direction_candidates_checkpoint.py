#!/usr/bin/env python3
"""Prepare revision 56: record N11 (A-direction candidate generation) and route N12.

S056 generated 13 A-direction candidates across OP01-OP08 with the required
fields (HoTT-specific rule in the critical step, same-task comparison,
machine-checkable discriminating task) and mapped every one of them onto
existing machine results, generic boundaries, or meta/toolchain observations.
Verdict: A_DIRECTION_BOUNDED_NEGATIVE within the fixed candidate space and
toolchain; the only upgrade path is E6 (a real natural-use chain).  The next
work package is N12: the bounded evidence-queue sample review.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-056-A-DIRECTION-CANDIDATES"
PREV_SESSION = "S-RES-20260912-055-W51-RPB01-PROPOSITIONALISATION"
RESULT_ID = "A-A-DIRECTION-CANDIDATES-001"
C10 = "理解章节/C10-N11-A方向候选生成-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [C10]
NEW_STATUS = "A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_a_direction", RUNTIME_PATH)
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
        "KC-000003": ("ALIGNED", "合取前提思想在 C10 中被表述为：边界结论只在特定表示/资格层出现。"),
        "KC-000004": ("ALIGNED", "悖论作为反证在 C10 中保持为研究方向，不把模型选择当作理论失败。"),
        "KC-000005": ("ALIGNED", "先找悖论后归因的顺序在 C10 中保持不变：候选先行、判词后置。"),
        "KC-000006": ("DEEPENED", "时间机制不能收窄为稠密性的警告被 C10 的 A-10 判定直接采用（模型选择而非 HoTT 特有）。"),
        "KC-000010": ("DEEPENED", "‘最优雅结果’的要求在 C10 中被转写为三个必填门槛（规则参与/同一任务/可机器化）。"),
        "KC-000011": ("ALIGNED", "理论推演排除时序的观察在 A-06/A-11 的候选判词中被保留。"),
        "KC-000012": ("DEEPENED", "ASK 预分析在 C10 中体现为：资格越级需要真实使用链（E6）。"),
        "KC-000013": ("ALIGNED", "理论工具性的经济收益在 C10 的候选归约类型中被显式分类。"),
        "KC-000022": ("DEEPENED", "两类现实相对悖论在 C10 中被逐候选检查（A-01–A-09 为边界，A-10 为模型选择，A-13 为通用边界）。"),
        "KC-000024": ("ALIGNED", "时序/过程的可计算性要求在 A-04/A-05/A-06 的机器结果中已被固定。"),
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
            ("NOT_TOUCHED", "本轮是 S056 A 方向候选生成（N11）；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S056/SESSION.md；{C10} | E6 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N11 结题（`A_DIRECTION_BOUNDED_NEGATIVE`）；第一工作包转 N12 证据队列；DIR-U-A 行的陈旧下一动作被原位修正；revision 56/generation 040。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-A-DIRECTION-CANDIDATES`；理解章节 inventory 更新为 35/24（C0–C10）。",
        "- update_decision: `C10 进入 理解章节 与 merge manifest；不新增 claim matrix 行；不把元层/工具链观察写成理论悖论。`",
        "- cross_conflicts: `NONE_OBSERVED` — C10 的归约与 C5–C9、四层审计一致；三条研究线汇合到同一缺口（E6）。",
        "- unresolved: `E6、N12 抽样复核、ERCF-3 P8、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `A_DIRECTION_BOUNDED_NEGATIVE`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S055 路由的第一工作包 N11（A 方向候选生成，要求 HoTT 特有规则参与关键步骤）。",
        "- 产出：`理解章节/C10-N11-A方向候选生成-20260912.md`——13 个候选（A-01–A-13）跨 OP01–OP08，每个候选给出关键 HoTT 规则、同一任务对照、现实侧完成、关键步骤、预测判词与映射；三类归约（表示/资格边界、通用边界、元层/工具链观察）；短名单与逐项复活条件；停止条件。",
        "- 判定：`A_DIRECTION_BOUNDED_NEGATIVE`（限定本轮候选空间与固定工具链）——没有找到同时满足三门槛且需要新增机器证明的 A 方向候选；A-11/A-12 为两个新形态，但判词是元层/工具链观察，不构成理论悖论。",
        "- 统一结论：ERCF 线（C8）、W51 线（C9）与 A 方向（C10）的升级口都是 E6（真实、固定版本、可回查的自然使用链）；继续生成同型候选或同型审计的边际价值已低。",
        "- 治理联动：C10 新增 → merge manifest 重建 35/24（top-level unique 11、nonidentical 20、unresolved 0）；DIR-U-A 行的陈旧下一动作（‘下一步做 N1’）被原位修正。",
        "- 边界：不新增 claim matrix 行；不把工具链行为（编译拒绝、stuck 项）写成对象理论定理。",
        "- 三件套：direction/panorama revision 56/generation 040；core 不变。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT`",
        "状态：`CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 55", "source_state_revision: 56")
    direction = sub_once(direction, "projection_generation: 20260912-direction-039", "projection_generation: 20260912-direction-040")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT",
        "semantic_status: CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT",
    )
    direction = sub_once(
        direction,
        "、`OUT-TOP-ONLINE-CAUSALITY`、`OUT-TOP-C5-PARADOX-DISTANCE` | partiality、guard-erasure、cost、路径证书与在线因果支线已形成完整的正反结构（含表示限制、细化正控制、统一迁移非栖居与在线资格边界），仍未产生现实相对悖论；C5 判定距 `NATURAL_USAGE_MISMATCH` 只差 natural consumer（E6）；下一步做 N1 有界自然消费者审计 |",
        "、`OUT-TOP-ONLINE-CAUSALITY`、`OUT-TOP-C5-PARADOX-DISTANCE`、`OUT-TOP-A-DIRECTION-CANDIDATES` | partiality、guard-erasure、cost、路径证书与在线因果支线已形成完整的正反结构；N11 的 13 个 A 方向候选全部归约为表示/资格边界、通用边界或元层/工具链观察，判 `A_DIRECTION_BOUNDED_NEGATIVE`（限定候选空间与工具链）；升级唯一口 = E6（真实自然使用链） |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N11 新候选生成（A 方向优先）——以 N1–N10、C8、C9 的教训为输入，生成 A 方向（现实可完成、Think in HoTT 呈现额外完成困难）候选矩阵；每个候选必须写明关键步骤由哪条 HoTT 特有规则（`ua`/`Id`/HIT/truncation/高阶相干）承担，以及可机器化的最小判别任务与停止条件；若全部候选只是通用边界/表示限制的重述，记录 `A_DIRECTION_BOUNDED_NEGATIVE` 并转回证据队列。备选（ERCF 线）：T4 第五层 consumer 审计。",
        "4. **当前第一工作包**：N12 证据队列有界推进——按固定规则从 2,396 条 understanding claim 中抽样（含 `univalence`/`HIT`/`truncation`/`Cauchy`/`SIP`/`cost` 关键词者全部入选，另按行号等距补足），逐条给出句级判词（`SUPPORTED` / `UNSUPPORTED` / `SUPERSEDED_BY_MACHINE_RESULT` / `PENDING`）与证据边界；若抽样中发现自然使用链（E6），立即转 F-011 机器化。备选（ERCF 线）：T4 第五层 consumer 审计。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT`",
        "状态：`CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 55", "source_state_revision: 56")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-039", "projection_generation: 20260912-outcome-040")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_W51_PROPOSITIONALISED_N11_A_DIRECTION_CANDIDATES_NEXT",
        "semantic_status: CORE_GENERATION_4_A_DIRECTION_CANDIDATES_BOUNDED_NEGATIVE_EVIDENCE_QUEUE_NEXT",
    )
    row = (
        "| `OUT-TOP-A-DIRECTION-CANDIDATES` | S056 N11 A 方向候选生成——13 个候选（A-01–A-13）跨 OP01–OP08，逐项给出关键 HoTT 规则、同一任务对照、现实侧完成、关键步骤与映射；三类归约（表示/资格边界、通用边界、元层/工具链观察）；短名单与逐项复活条件；判 `A_DIRECTION_BOUNDED_NEGATIVE`（限定候选空间与工具链） |"
        " `DIR-U-A-REALITY-RELATIVE`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工候选生成 + 既有机器结果映射 | `DOCUMENTED / A_DIRECTION_BOUNDED_NEGATIVE` |"
        " 没有找到满足三门槛且需要新增机器证明的 A 方向候选；三条研究线（ERCF/W51/A）汇合到同一缺口 E6 |"
        " 不新增数学 claim；不把元层/工具链观察写成理论悖论；负结论限定在本轮候选空间与固定工具链 |"
        " `理解章节/C10-N11-A方向候选生成-20260912.md`；C5–C9；四层审计 |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "两个理解章节目录当前为 34/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C9 共 10 个独有文件（nonidentical union entries=19）；逐文件处置已生成",
        "两个理解章节目录当前为 35/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C10 共 11 个独有文件（nonidentical union entries=20）；逐文件处置已生成",
    )
    panorama = sub_once(
        panorama,
        "C3/C4/C5/C6/C7/C8/C9 为 top-level current AI strategy/research synthesis",
        "C3/C4/C5/C6/C7/C8/C9/C10 为 top-level current AI strategy/research synthesis",
    )
    panorama = sub_once(
        panorama,
        "S055 完成 W51 命题化与 RP-B01 层映射（C9：W51-1 抽象核有机器证据、W51-2 通用边界、W51-3 保持 OPEN）；R032 回放、",
        "S055 完成 W51 命题化与 RP-B01 层映射（C9：W51-1 抽象核有机器证据、W51-2 通用边界、W51-3 保持 OPEN）；S056 的 N11 把 13 个 A 方向候选归约为三类并判 `A_DIRECTION_BOUNDED_NEGATIVE`；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S055 完成 W51 命题化与 RP-B01 层映射（W51-1 抽象核有机器证据、W51-2 通用边界、W51-3 保持 OPEN）。所有新结论继续执行 F-011。",
        "S055 完成 W51 命题化与 RP-B01 层映射（W51-1 抽象核有机器证据、W51-2 通用边界、W51-3 保持 OPEN）；S056 的 N11 生成 13 个 A 方向候选并把它们归约为三类（表示/资格边界、通用边界、元层/工具链观察），判 `A_DIRECTION_BOUNDED_NEGATIVE`，升级唯一口 = E6。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N11 新候选生成（A 方向优先） | candidate matrix + stop conditions | 每个候选写明 HoTT 特有规则参与的关键步骤与可机器化判别任务；若全是通用边界/表示限制重述则记录 `A_DIRECTION_BOUNDED_NEGATIVE` 并转证据队列 |",
        "| 已闭合工作包 14 | A 方向候选生成（S056，N11） | `A_DIRECTION_BOUNDED_NEGATIVE` | 13 个候选跨 OP01–OP08；三类归约；短名单与逐项复活条件；升级唯一口 = E6 |\n"
        "| 第一工作包 | N12 证据队列有界推进 | fixed-rule sample review | 固定抽样规则（关键词全选 + 行号等距补足）；逐条句级判词与证据边界；发现 E6 即转 F-011；备选 T4 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N11 新候选生成（A 方向优先）：以 N1–N10、C8、C9 的教训为输入，生成 A 方向候选矩阵；每个候选必须写明关键步骤由哪条 HoTT 特有规则（ua/Id/HIT/truncation/高阶相干）承担，以及可机器化的最小判别任务与停止条件；若全部候选只是通用边界/表示限制的重述，记录 `A_DIRECTION_BOUNDED_NEGATIVE` 并转回证据队列。备选（ERCF 线）：T4 第五层 consumer 审计。",
        "2. 当前第一工作包转为 N12 证据队列有界推进：按固定规则从 2,396 条 understanding claim 中抽样（含 univalence/HIT/truncation/Cauchy/SIP/cost 关键词者全部入选，另按行号等距补足），逐条给出句级判词（SUPPORTED / UNSUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / PENDING）与证据边界；若抽样中发现自然使用链（E6），立即转 F-011 机器化。备选（ERCF 线）：T4 第五层 consumer 审计。",
    )
    memory = sub_once(
        memory,
        "- S055 完成 W51 命题化与 RP-B01 层映射：",
        "- S056 完成 N11（A 方向候选生成）：`理解章节/C10-N11-A方向候选生成-20260912.md` 给出 13 个候选（A-01–A-13，跨 OP01–OP08）、三类归约（表示/资格边界、通用边界、元层/工具链观察）、短名单与逐项复活条件；判 `A_DIRECTION_BOUNDED_NEGATIVE`（限定候选空间与固定工具链）；三条研究线（ERCF/W51/A）汇合到同一缺口 E6；merge manifest 重建 35/24；DIR-U-A 行的陈旧下一动作被原位修正；下一工作包转 N12 证据队列。\n"
        "- S055 完成 W51 命题化与 RP-B01 层映射：",
    )
    memory = sub_once(
        memory,
        "`A-W51-RPB01-MAPPING-001`。",
        "`A-W51-RPB01-MAPPING-001`、`A-A-DIRECTION-CANDIDATES-001`。",
    )
    memory = sub_once(
        memory,
        "S055 完成 W51 命题化与 RP-B01 层映射并把 A11.1 保持 PARKED，转 N11（A 方向候选生成），不直接跳 ERCF-3 构造。",
        "S055 完成 W51 命题化与 RP-B01 层映射并把 A11.1 保持 PARKED；S056 完成 N11 并把 A 方向候选收口为 `A_DIRECTION_BOUNDED_NEGATIVE`（升级唯一口 = E6），转 N12 证据队列，不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S056 完成 N11（A 方向候选生成）：`理解章节/C10-N11-A方向候选生成-20260912.md` 给出 13 个候选（A-01–A-13，覆盖 OP01–OP08）与三个必填门槛（HoTT 特有规则参与关键步骤 / 同一任务 / 可机器化判别）；全部候选归约为三类——表示/资格边界（A-01–A-05、A-08、A-09）、通用边界（A-10、A-13）、元层/工具链观察（A-11、A-12）——因此判 `A_DIRECTION_BOUNDED_NEGATIVE`（限定本轮候选空间与固定工具链）。短名单与逐项复活条件已固定；三条研究线（ERCF、W51、A 方向）汇合到同一升级口 E6。merge manifest 重建 35/24；下一工作包为 N12 证据队列有界推进（固定抽样规则 + 句级判词），备选 T4。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "54. 把方向性判断（如 W51“HoTT 对齐程序后继承程序界限”）命题化时，",
        "55. 候选生成要有“必填门槛”和“归约表”：N11 要求每个候选写明 HoTT 特有规则参与的关键步骤、同一任务对照与可机器化判别，然后把 13 个候选逐一映射到已有机器结果/通用边界/元层观察，得到有界负结论而不是无限生成。关键区分：工具链行为（编译拒绝、stuck 项）不等于对象理论定理；模型选择（稠密连续统）不等于 HoTT 特有；只有“真实使用链把弱资格当交付”（E6）才允许升级。三条研究线（自证、继承、A 方向）在同一轮汇合到同一缺口时，应停止生成同型候选、转入证据队列收口。\n"
        "54. 把方向性判断（如 W51“HoTT 对齐程序后继承程序界限”）命题化时，",
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
    if state.get("revision") != 55 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_55_AND_S055")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}
    new_hashes[MERGE_MANIFEST] = sha(root / MERGE_MANIFEST)

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README, MERGE_MANIFEST, C10})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S056 A-direction candidate generation: C10 was added and the understanding-chapter merge manifest "
        "was rebuilt (35/24); no proof source, run or claim-matrix row changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "candidate_generation",
        "path": C10,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "A_DIRECTION_BOUNDED_NEGATIVE",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [C10, MERGE_MANIFEST,
                         "HoTT/CLAIM_EVIDENCE_MATRIX.md",
                         "理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md",
                         "理解章节/C6-新候选生成与派生开发消费者审计-20260912.md",
                         "理解章节/C7-post-N6距离综合与剩余域选择-20260912.md",
                         "理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md",
                         "理解章节/C9-W51命题化与RP-B01层映射-20260912.md",
                         "scripts/audit/prepare_a_direction_candidates_checkpoint.py"],
        "source_hashes": {C10: new_hashes[C10], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST]},
        "resolution": {
            "reason": "13 candidates were generated with the three mandatory gates and mapped onto existing machine results, generic boundaries, or meta/toolchain observations. Verdict: A_DIRECTION_BOUNDED_NEGATIVE within the fixed candidate space and toolchain.",
            "evidence": [C10, MERGE_MANIFEST, "HoTT/CLAIM_EVIDENCE_MATRIX.md"],
        },
        "scope": "A-direction candidate generation (N11): 13 candidates, three reduction classes, shortlist with per-candidate revival conditions, and the bounded-negative verdict. The only upgrade path is E6 (a real natural-use chain). No new mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C10, MERGE_MANIFEST,
                         "scripts/audit/prepare_a_direction_candidates_checkpoint.py"],
        "source_hashes": {C10: new_hashes[C10], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST]},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_A_DIRECTION_CANDIDATES",
        "cognition_status": "A_DIRECTION_BOUNDED_NEGATIVE_AND_N12_ROUTED",
        "scope": "N11 A-direction candidate generation with the bounded-negative verdict and routing of the N12 evidence-queue sample review.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-040" if rid.startswith("I-DIRECTION") else "20260912-outcome-040"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (C10, MERGE_MANIFEST):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N11 A-direction candidate generation: bounded negative; the first work package is the N12 evidence-queue sample review."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the N11 A-direction candidate matrix (A_DIRECTION_BOUNDED_NEGATIVE); the next strand is N12."
    )

    state["revision"] = 56
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N12 evidence queue (bounded): sample the 2,396 understanding claims by a fixed rule (all claims mentioning univalence/HIT/truncation/Cauchy/SIP/cost, plus an equal-spacing fill), "
            "and give each sampled claim a sentence-level verdict (SUPPORTED / UNSUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / PENDING) with evidence boundaries. "
            "If the sample surfaces a natural-use chain (E6), switch immediately to F-011 machine packaging. "
            "Fallback (ERCF line): the T4 fifth-layer consumer audit."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "generation_kind": "a_direction_candidates",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "candidates": {
            "count": 13,
            "ids": ["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-07", "A-08", "A-09", "A-10", "A-11", "A-12", "A-13"],
            "reduction_classes": {
                "representation_boundary": ["A-01", "A-02", "A-03", "A-04", "A-05", "A-08", "A-09"],
                "generic_boundary": ["A-10", "A-13"],
                "meta_or_toolchain": ["A-11", "A-12"],
            },
            "three_gates": ["HoTT-specific rule in the critical step", "same-task comparison", "machine-checkable discriminating task"],
        },
        "verdict": "A_DIRECTION_BOUNDED_NEGATIVE",
        "unified_gap": "E6 (real, fixed-version, retrievable natural-use chain) is the single upgrade path across the ERCF, W51 and A-direction lines",
        "understanding_merge": {"top_level_files": 35, "nested_files": 24, "union_files": 35,
                                "top_level_unique": 11, "nonidentical_union_entries": 20,
                                "unresolved_nontrivial": 0},
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"candidates": C10, "session_evidence": f"{SESSION_REL}/evidence/"},
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
            "This in-scope checkpoint records the N11 A-direction candidate generation (bounded negative with 13 candidates and three reduction classes), "
            "adds C10 to the understanding chapters, rebuilds the merge manifest, fixes the stale DIR-U-A next action, and routes the N12 evidence-queue sample review. "
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
        "revision": 56,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
