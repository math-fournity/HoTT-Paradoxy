#!/usr/bin/env python3
"""Prepare revision 48: record MP-PARTIAL-DECISION-001 and route N7.

N6 built the minimal native Cubical boundary between a strict classifier and a
partial classifier definable only up to weak bisimilarity (C-118-C-123).
Verdict: PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL.  The next work
package is N7: a post-N6 distance synthesis over the twelve machine packages.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-048-PARTIAL-DECISION"
PREV_SESSION = "S-RES-20260912-047-DERIVED-DEVELOPMENT-AUDIT"
RESULT_ID = "A-PARTIAL-DECISION-FORMAL-001"
PROOF_ID = "MP-PARTIAL-DECISION-001"
RUN_ID = "20260912-MP-PARTIAL-DECISION-001-01"
SOURCE = "HoTT/formal/partial-decision/PartialDecision.agda"
SOURCE_README = "HoTT/formal/partial-decision/README.md"
TOOLCHAIN = "HoTT/formal/partial-decision/TOOLCHAIN.json"
LIBRARIES = "HoTT/formal/partial-decision/AGDA_LIBRARIES"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/partial-decision机器证明实施证据-20260912.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_partial_decision", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N6 把现实相对资格断层缩到 strict vs partial 分类器，并保持边界判词。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 N6 中具体化为“商层只能交付 up-to-≈ 的 partial classifier”。"),
        "KC-000013": ("DEEPENED", "理论工具性的遗忘（商掉严格展示）在 N6 中得到机器化的正反控制。"),
        "KC-000014": ("ALIGNED", "方向 B 的“交付资格”在 partial/total 二分中再获一个边界实例。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮 Agda 2.8.0/Cubical v0.9 final run exit 0、零 warning、exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对框架保持不变；N6 仍是表示/资格边界而非内部矛盾。"),
        "KC-000024": ("DEEPENED", "完成时刻/严格展示的差别成为 N6 的核心：strict 消费者无法下降到商。"),
        "KC-000029": ("DEEPENED", "理论经济在此处表现为“商掉完成时刻”；正控制给出 up-to-≈ 的 partial 交付。"),
        "KC-000031": ("ALIGNED", "商消去规则拒绝 strict 扩展，继续记为防御/边界而非覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N6 不涉及自指反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是 N6 partial/strict classifier 机器边界；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S048/SESSION.md；HoTT/formal/partial-decision/PartialDecision.agda | N7、ERCF-3 与其它接口仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N6 完成并判 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`；第一工作包转 N7 post-N6 距离综合；revision 48/generation 032。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-PARTIAL-DECISION`。",
        "- update_decision: `MP-PARTIAL-DECISION-001 进入 formal/run/index/STATE；C-118–C-123 进入 claim matrix；十一个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 十二个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `N7、ERCF-3、R032、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S047 后的 N6 工作包（最小 quotient + partial/strict classifier 边界）。",
        "- 构造：`A={a,b,c}`、`R_A` 识别 `a,b`；`Q = A/R_A`；`Delay Bool = now/later`；`R_D (now x) (later (now y)) = (x≡y)`；`D≈ = Delay Bool/R_D`；`P0 a=now true`、`P0 b=later (now true)`、`P0 c=now false`；`strict (now _)=true`、`strict (later _)=false`。",
        "- 结果：`MP-PARTIAL-DECISION-001`（C-118–C-123）通过 kernel：代表层 strict 分类器存在；无 strict `Q→Delay Bool` 扩展；存在 up-to-≈ partial classifier `Q→D≈`（正控制）；无 strict `Q→Bool` 消费者；代表层消费者区分 a,b。判词 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`（非悖论）。",
        "- 运行：final run `20260912-MP-PARTIAL-DECISION-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`），零 warning。",
        "- 旧证据：矩阵第十次增长后，十一个旧包全部重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：`true≢false` 重名、`rec` 歧义、路径复合方向、`isSet/` 与商注入的隐式参数；均按责任点修复，命题未削弱。",
        "- 边界：只覆盖最小 delay 片段；不构造完整 partiality monad，不形式化 `ℝq → 𝟐⊥`，不主张原创性。",
        "- 三件套：direction/panorama revision 48/generation 032；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT`",
        "状态：`CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 47", "source_state_revision: 48")
    direction = sub_once(direction, "projection_generation: 20260912-direction-031", "projection_generation: 20260912-direction-032")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT",
        "semantic_status: CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT",
    )
    direction = sub_once(
        direction,
        "；`MP-TRANSITION-LIFT-001` 原生证明 R036/R038 核心边界（`C-110`–`C-117`：过渡抽象/极限）。",
        "；`MP-TRANSITION-LIFT-001` 原生证明 R036/R038 核心边界（`C-110`–`C-117`：过渡抽象/极限）；`MP-PARTIAL-DECISION-001` 原生给出 strict vs partial classifier 的最小边界（`C-118`–`C-123`）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N6 `MP-PARTIAL-DECISION-001`——在原生 Cubical Agda 中构造最小 quotient + classifier 模型：不存在与 quotient 相容的 total `Bool` classifier；存在 partial classifier 并给出正控制；任何把 partial 当 total 的消费者要么不返回，要么必须显式添加 modulus/decidability/section；预期最多 `REPRESENTATION_BOUNDARY`。",
        "4. **当前第一工作包**：N7 post-N6 距离综合——汇总十二个机器包（C-59–C-123）的判词分布，重新评估离 `NATURAL_USAGE_MISMATCH` 的距离，明确剩余未触达域（SIP/表示消费者机器化、Cauchy modulus 外部库、工具链/应用层消费者），并选择下一机器构造或审计；不得升级任何未证命题。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT`",
        "状态：`CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 47", "source_state_revision: 48")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-031", "projection_generation: 20260912-outcome-032")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT",
        "semantic_status: CORE_GENERATION_4_PARTIAL_DECISION_PROVED_POST_N6_DISTANCE_SYNTHESIS_NEXT",
    )
    row = (
        "| `OUT-TOP-PARTIAL-DECISION` | `MP-PARTIAL-DECISION-001`：strict 与 partial classifier 的最小原生边界——代表层 strict 分类器存在（`C-118`）、strict 区分 `now/later`（`C-119`）、无 strict `Q → Delay Bool` 扩展（`C-120`）、存在 up-to-≈ partial classifier `Q → D≈`（`C-121`，正控制）、无 strict `Q → Bool` 消费者（`C-122`）、代表层消费者区分 `a,b`（`C-123`） |"
        " `DIR-W-RACE-TIMEOUT`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL` |"
        " 同一 Agda 2.8.0 + Cubical v0.9 工具链、官方 release/tree hashes、exit 0（零 warning）、`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`；十一个旧包 row-stable + exact replay |"
        " 只覆盖最小 delay 片段；不构造完整 partiality monad、不形式化 `ℝq → 𝟐⊥`、不证明真实库误用或 HoTT 内部矛盾 |"
        " `HoTT/formal/partial-decision/`；final run `20260912-MP-PARTIAL-DECISION-001-01`；claim matrix C-118–C-123；`audit/partial-decision机器证明实施证据-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N6 partial/total decision 最小机器边界、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N6 partial/total decision 最小机器边界已机器闭合（C-118–C-123）；N7 post-N6 距离综合、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N5 审计派生开发自述，固定集合内判 scoped `BOUNDED_DEFENSE`（无自述越过接口）。所有新结论继续执行 F-011。",
        "N5 审计派生开发自述，固定集合内判 scoped `BOUNDED_DEFENSE`（无自述越过接口）；N6 把 strict vs partial classifier 做成最小原生机器边界（C-118–C-123，零 warning），判 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N6 `MP-PARTIAL-DECISION-001` | formal / native Cubical Agda | 最小 quotient + classifier：无相容 total `Bool` classifier；存在 partial classifier 正控制；把 partial 当 total 的消费者必须显式添加 modulus/decidability/section；预期最多 `REPRESENTATION_BOUNDARY` |",
        "| 第一工作包 | N7 post-N6 距离综合 | synthesis / paper-only | 汇总十二个机器包（C-59–C-123）判词分布，重估 `NATURAL_USAGE_MISMATCH` 距离，列出剩余未触达域并选择下一机器构造/审计；不升级任何命题 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N6 `MP-PARTIAL-DECISION-001`：在原生 Cubical Agda 中构造最小 quotient + classifier 模型，证明不存在相容 total `Bool` classifier、存在 partial classifier（正控制），并记录把 partial 当 total 的消费者必须显式添加 modulus/decidability/section；预期最多 `REPRESENTATION_BOUNDARY`。",
        "2. 当前第一工作包转为 N7 post-N6 距离综合：汇总十二个机器包（C-59–C-123）的判词分布，重估离 `NATURAL_USAGE_MISMATCH` 的距离，列出剩余未触达域（SIP/表示消费者、Cauchy modulus、工具链/应用层消费者）并选择下一机器构造或审计；不升级任何命题。",
    )
    memory = sub_once(
        memory,
        "- N5 派生开发消费者审计（S047）：固定集合 D1–D5 内无 `FOUND_CANDIDATE`；D1 §5.2 明确 partial `ℝq → 𝟐⊥` 与不可定义 total `ℝq → 𝟐`，D2–D4 显式携带 choice/分配律/resource-bounded 假设；判定 scoped `BOUNDED_DEFENSE`，转 N6。",
        "- N5 派生开发消费者审计（S047）：固定集合 D1–D5 内无 `FOUND_CANDIDATE`；D1 §5.2 明确 partial `ℝq → 𝟐⊥` 与不可定义 total `ℝq → 𝟐`，D2–D4 显式携带 choice/分配律/resource-bounded 假设；判定 scoped `BOUNDED_DEFENSE`，转 N6。\n"
        "- N6 partial/total classifier 边界（S048）已由 `MP-PARTIAL-DECISION-001` 原生机器化：C-118–C-123，零 warning、exact replay；十一个旧包在矩阵增长后全部 row-stable；判词 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。",
    )
    memory = sub_once(
        memory,
        "`A-NEW-CANDIDATES-001`、`A-DERIVED-DEVELOPMENT-AUDIT-001`。六条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE` 并转 N6 partial/total decision 机器边界，不直接跳 ERCF-3。",
        "`A-NEW-CANDIDATES-001`、`A-DERIVED-DEVELOPMENT-AUDIT-001`、`A-PARTIAL-DECISION-FORMAL-001`。七条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限、partial/total decision）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE`，N6 关闭 partial/total 边界并转 N7 距离综合，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S048 完成 N6：`MP-PARTIAL-DECISION-001`（C-118–C-123）在 Agda 2.8.0/Cubical v0.9 下原生机器化 strict vs partial classifier 边界，零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay；十一个旧包在矩阵增长后全部 row-stable。判词 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。下一工作包为 N7 post-N6 距离综合；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "46. 派生开发的“可计算”自述要先看它的**类型**是否已经携带资格：ADK 的 `isPositive : ℝq → 𝟐⊥` 是 partial classifier，作者同时说明 total `ℝq → 𝟐` 不可定义，并把 propositional 与 definitional equality 分开；D2–D4 的 choice/分配律/resource-bounded 假设也都写在接口或正文里。审计的判定单位是“同一任务下是否隐藏假设”，不是文案里是否出现 compute/extract 字样。",
        "46. 派生开发的“可计算”自述要先看它的**类型**是否已经携带资格：ADK 的 `isPositive : ℝq → 𝟐⊥` 是 partial classifier，作者同时说明 total `ℝq → 𝟐` 不可定义，并把 propositional 与 definitional equality 分开；D2–D4 的 choice/分配律/resource-bounded 假设也都写在接口或正文里。审计的判定单位是“同一任务下是否隐藏假设”，不是文案里是否出现 compute/extract 字样。\n"
        "47. 最小的 strict-vs-partial 机器边界不需要完整 partiality monad：`Q = A/R_A`（a~b）、`D≈ = Delay Bool/R_D`（now x ~ later (now x)）、代表层 `P0 a = now true`、`P0 b = later (now true)` 就足以证明「strict 扩展不存在、up-to-≈ partial classifier 存在、strict 消费者不能下降、代表层消费者仍可区分」。先做最小片段再决定是否升级到完整单子。",
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
    if state.get("revision") != 47 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_47_AND_S047")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(118, 124)]
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
    note = "After C-118 through C-123 were appended (S048), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH for the eleven older packages."
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
        "classification": "PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(118, 124)],
        "run_id": RUN_ID,
        "mathematical_status": "MINIMAL_NATIVE_STRICT_VS_PARTIAL_CLASSIFIER_BOUNDARY",
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
        "scope": "Minimal native boundary between a strict classifier and a partial classifier definable only up to weak bisimilarity: no strict Q -> Delay Bool extension (C-120), no strict Q -> Bool consumer (C-122), partial classifier Q -> D-approximate exists (C-121), representative-level strict classifier exists and separates a,b (C-118, C-119, C-123). Boundary result with positive control; not a HoTT paradox.",
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
                         "scripts/audit/prepare_partial_decision_checkpoint.py"],
        "source_hashes": {SOURCE: new_hashes[SOURCE],
                          f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
                          AUDIT_DOC: new_hashes[AUDIT_DOC]},
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_PARTIAL_DECISION",
        "cognition_status": "PARTIAL_DECISION_BOUNDARY_PROVED_AND_POST_N6_SYNTHESIS_ROUTED",
        "scope": "Native Cubical partial/strict classifier boundary (C-118–C-123), revalidation of eleven older packages, and routing of the N7 post-N6 distance synthesis.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-032" if rid.startswith("I-DIRECTION") else "20260912-outcome-032"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                    f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the native partial-decision result: the partial/strict boundary is machine-proved; the first work package is the N7 post-N6 distance synthesis."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the native partial-decision boundary (C-118-C-123); the next strand is N7."
    )

    state["revision"] = 48
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N7: post-N6 distance synthesis. Read the twelve machine packages (C-59-C-123), the C5 synthesis and the N1-N5 audits; "
            "tally the verdict distribution, reassess the distance to NATURAL_USAGE_MISMATCH, and enumerate the remaining untouched domains "
            "(SIP/representation consumers, Cauchy modulus with an external Real library, toolchain/application-level consumers, ERCF-3 prerequisites). "
            "Select the next machine construction or bounded audit with explicit evidence boundaries. No claim upgrade."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(118, 124)],
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
                "20260912-MP-TRANSITION-LIFT-001-01",
            )
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL",
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
            "This in-scope checkpoint records the native partial-decision package MP-PARTIAL-DECISION-001 (C-118-C-123), "
            "repairs the source hashes changed by the claim-matrix growth, and routes the N7 post-N6 distance synthesis. "
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
        "revision": 48,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
