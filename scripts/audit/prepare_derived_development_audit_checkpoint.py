#!/usr/bin/env python3
"""Prepare revision 47: record the N5 derived-development audit and route N6.

N5 audited a fixed set of derived developments (ADK Partiality Revisited,
Chapman-Uustalu-Veltri, Moegelberg-Zwart, CATT, and local Cubical v0.9
derived modules) for self-claims beyond their interfaces.  No FOUND_CANDIDATE:
all audited self-claims carry their assumptions explicitly.  Verdict:
BOUNDED_DEFENSE (scoped).  The next work package is N6:
MP-PARTIAL-DECISION-001, a minimal native Cubical partial-vs-total decision
boundary.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-047-DERIVED-DEVELOPMENT-AUDIT"
PREV_SESSION = "S-RES-20260912-046-NEW-CANDIDATES"
RESULT_ID = "A-DERIVED-DEVELOPMENT-AUDIT-001"
AUDIT = "audit/derived-development-consumer审计-20260912.md"
C6 = "理解章节/C6-新候选生成与派生开发消费者审计-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_n5_audit", RUNTIME_PATH)
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
        "KC-000010": ("ALIGNED", "N5 继续以现实相对资格断层为目标，把“自述是否越过接口”作为审计问题。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题落到派生开发自述：定理级资格是否被写成执行/交付级承诺。"),
        "KC-000013": ("DEEPENED", "理论工具性的经济化自述在 N5 中以“假设是否显式”逐条核对。"),
        "KC-000014": ("ALIGNED", "方向 B 的派生开发自述在固定集合内全部带显式假设；未找到自然升级。"),
        "KC-000021": ("ALIGNED", "本轮为文本/接口审计；不新增机器运行，S043 的 F-011 证据继续作为来源身份。"),
        "KC-000022": ("ALIGNED", "两类现实相对框架保持不变；N5 判定为 scoped bounded defense。"),
        "KC-000024": ("DEEPENED", "partial vs total decision 的时序/完成性差别成为 N6 的机器构造目标。"),
        "KC-000027": ("ALIGNED", "HoTT 继承程序界限的候选在 partiality 自述中表现为 partial 类型，而非被隐藏的总实现。"),
        "KC-000031": ("ALIGNED", "派生开发显式携带 choice/coherence/resource-bounded 假设，继续记为防御而非覆盖失败。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；N5 不启动反射闭包。"),
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
            ("NOT_TOUCHED", "本轮是 N5 派生开发自述审计；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S047/SESSION.md；audit/derived-development-consumer审计-20260912.md | N6、ERCF-3 与其它接口仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N5 在固定集合内判 `BOUNDED_DEFENSE`；第一工作包转 N6 partial/total decision 最小机器边界；revision 47/generation 031。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-DERIVED-DEVELOPMENT-AUDIT`（scoped `BOUNDED_DEFENSE`）。",
        "- update_decision: `N5 审计报告进入 audit/；C6 候选池中的 D1 §5.2 被选为 N6 的机器构造来源；claim matrix 未变。`",
        "- cross_conflicts: `NONE_OBSERVED` — D1–D5 的自述与显式假设一致。",
        "- unresolved: `N6、ERCF-3、R032 回放、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮无新数学结论，状态为 `BOUNDED_DEFENSE_SCOPED`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S046 后的 N5 工作包（派生开发消费者审计）。",
        "- 固定集合：D1 Partiality Revisited（全文）、D2 Chapman–Uustalu–Veltri（摘要）、D3 Møgelberg–Zwart（摘要）、D4 CATT（全文）、D5 本地 Cubical v0.9 派生模块。",
        "- 结果：没有 `FOUND_CANDIDATE`。D1 §5.2 明确区分 `ℝq → 𝟐⊥` 的 partial classifier 与不可定义的 total `ℝq → 𝟐`，并明确区分 propositional 与 definitional equality；D2/D3/D4 显式写出 choice、分配律、resource-bounded 假设；D5 的消费者带类型围栏或显式参数。",
        "- 判定：`BOUNDED_DEFENSE (SCOPED)`。",
        "- 下一工作包：N6 `MP-PARTIAL-DECISION-001`——最小 quotient + partial/total classifier 边界；预期最多 `REPRESENTATION_BOUNDARY`。",
        "- 三件套：direction/panorama revision 47/generation 031；核心认知不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 46", "source_state_revision: 47")
    direction = sub_once(direction, "projection_generation: 20260912-direction-030", "projection_generation: 20260912-direction-031")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N5 派生开发消费者审计——固定论文/库版本与 hash，逐条提取派生开发对自身构造的“可计算/可提取/可序列化/可交付”承诺，核对所需假设（choice、modulus、section、coherence）是否在接口中显式；输出 `FOUND_CANDIDATE` / `BOUNDED_DEFENSE` / `INCONCLUSIVE_SOURCE_UNAVAILABLE`；只有找到候选才进入 F-011 机器化，备选为 `CAND-TYPEQUOT-SECTION`。",
        "4. **当前第一工作包**：N6 `MP-PARTIAL-DECISION-001`——在原生 Cubical Agda 中构造最小 quotient + classifier 模型：不存在与 quotient 相容的 total `Bool` classifier；存在 partial classifier 并给出正控制；任何把 partial 当 total 的消费者要么不返回，要么必须显式添加 modulus/decidability/section；预期最多 `REPRESENTATION_BOUNDARY`。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT`",
        "状态：`CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 46", "source_state_revision: 47")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-030", "projection_generation: 20260912-outcome-031")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT",
        "semantic_status: CORE_GENERATION_4_DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_PARTIAL_DECISION_NEXT",
    )
    row = (
        "| `OUT-TOP-DERIVED-DEVELOPMENT-AUDIT` | N5 派生开发消费者审计：固定集合 D1–D5；没有 `FOUND_CANDIDATE`；D1 §5.2 明确区分 partial `ℝq → 𝟐⊥` 与不可定义的 total `ℝq → 𝟐`；D2/D3/D4 显式写出 choice/分配律/resource-bounded 假设；D5 的消费者带类型围栏或显式参数 |"
        " `DIR-W-RP-B01`、`DIR-W-RACE-TIMEOUT`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工审计 | `BOUNDED_DEFENSE (SCOPED)` |"
        " 每来源给出最接近升级的句子、实际假设/限定与判定；D1 全文与 D2/D3/D4 摘要身份已固定 |"
        " 只覆盖 D1–D5 的版本与所核层级；不证明所有派生开发都安全 |"
        " `audit/derived-development-consumer审计-20260912.md`；S043 evidence/sources；`理解章节/C6-新候选生成与派生开发消费者审计-20260912.md` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "N4 新候选生成已完成（C6，含 `CAND-REGULARITY` 实测排除）；N5 派生开发消费者审计、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N4 新候选生成已完成（C6，含 `CAND-REGULARITY` 实测排除）；N5 派生开发审计已完成（scoped `BOUNDED_DEFENSE`）；N6 partial/total decision 最小机器边界、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N4 生成 DIR×OP 候选矩阵并用 Cubical 探针排除 ua-regularity 候选。所有新结论继续执行 F-011。",
        "N4 生成 DIR×OP 候选矩阵并用 Cubical 探针排除 ua-regularity 候选；N5 审计派生开发自述，固定集合内判 scoped `BOUNDED_DEFENSE`（无自述越过接口）。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N5 派生开发消费者审计 | audit / paper-and-library-evidence | 固定论文/库版本与 hash，逐条核对派生开发对“可计算/可提取/可序列化/可交付”的自述是否超出接口资格；输出 `FOUND_CANDIDATE`/`BOUNDED_DEFENSE`/`INCONCLUSIVE_SOURCE_UNAVAILABLE`；备选 `CAND-TYPEQUOT-SECTION` |",
        "| 第一工作包 | N6 `MP-PARTIAL-DECISION-001` | formal / native Cubical Agda | 最小 quotient + classifier：无相容 total `Bool` classifier；存在 partial classifier 正控制；把 partial 当 total 的消费者必须显式添加 modulus/decidability/section；预期最多 `REPRESENTATION_BOUNDARY` |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N5 派生开发消费者审计：固定论文/库版本与 hash，逐条核对派生开发对“可计算/可提取/可序列化/可交付”的自述是否超出接口资格；输出 `FOUND_CANDIDATE`/`BOUNDED_DEFENSE`/`INCONCLUSIVE_SOURCE_UNAVAILABLE`；备选 `CAND-TYPEQUOT-SECTION`。",
        "2. 当前第一工作包转为 N6 `MP-PARTIAL-DECISION-001`：在原生 Cubical Agda 中构造最小 quotient + classifier 模型，证明不存在相容 total `Bool` classifier、存在 partial classifier（正控制），并记录把 partial 当 total 的消费者必须显式添加 modulus/decidability/section；预期最多 `REPRESENTATION_BOUNDARY`。",
    )
    memory = sub_once(
        memory,
        "- N4 新候选生成（S046）：DIR01–DIR09 × OP01–OP08 候选矩阵与五个短名单；`CAND-REGULARITY` 由 Cubical 2.8.0 探针实测排除；下一工作包转 N5 派生开发消费者审计。",
        "- N4 新候选生成（S046）：DIR01–DIR09 × OP01–OP08 候选矩阵与五个短名单；`CAND-REGULARITY` 由 Cubical 2.8.0 探针实测排除；下一工作包转 N5 派生开发消费者审计。\n"
        "- N5 派生开发消费者审计（S047）：固定集合 D1–D5 内无 `FOUND_CANDIDATE`；D1 §5.2 明确 partial `ℝq → 𝟐⊥` 与不可定义 total `ℝq → 𝟐`，D2–D4 显式携带 choice/分配律/resource-bounded 假设；判定 scoped `BOUNDED_DEFENSE`，转 N6。",
    )
    memory = sub_once(
        memory,
        "`A-TRANSITION-LIFT-FORMAL-001`、`A-NEW-CANDIDATES-001`。六条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选并转 N5 派生开发消费者审计，不直接跳 ERCF-3。",
        "`A-TRANSITION-LIFT-FORMAL-001`、`A-NEW-CANDIDATES-001`、`A-DERIVED-DEVELOPMENT-AUDIT-001`。六条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选，N5 给出 scoped `BOUNDED_DEFENSE` 并转 N6 partial/total decision 机器边界，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S047 完成 N5 派生开发消费者审计：固定集合 D1–D5 内无 `FOUND_CANDIDATE`；D1 §5.2 明确区分 partial `ℝq → 𝟐⊥` 与不可定义 total `ℝq → 𝟐`，D2–D4 显式携带 choice/分配律/resource-bounded 假设；判定 scoped `BOUNDED_DEFENSE`。下一工作包为 N6 `MP-PARTIAL-DECISION-001`（最小 quotient + partial/total classifier 边界）；ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "45. 候选生成必须先用最小探针排除可证伪的机制：`ua` regularity 在 Cubical Agda 2.8.0/Cubical v0.9 中由 `probe-regular = refl` 直接排除，不能靠文献印象保留。N1–N3 表明核心库接口系统性防御；E6 更可能在派生开发对自身构造的承诺中，因此 N5 审计派生开发而不是继续重审核心库。",
        "45. 候选生成必须先用最小探针排除可证伪的机制：`ua` regularity 在 Cubical Agda 2.8.0/Cubical v0.9 中由 `probe-regular = refl` 直接排除，不能靠文献印象保留。N1–N3 表明核心库接口系统性防御；E6 更可能在派生开发对自身构造的承诺中，因此 N5 审计派生开发而不是继续重审核心库。\n"
        "46. 派生开发的“可计算”自述要先看它的**类型**是否已经携带资格：ADK 的 `isPositive : ℝq → 𝟐⊥` 是 partial classifier，作者同时说明 total `ℝq → 𝟐` 不可定义，并把 propositional 与 definitional equality 分开；D2–D4 的 choice/分配律/resource-bounded 假设也都写在接口或正文里。审计的判定单位是“同一任务下是否隐藏假设”，不是文案里是否出现 compute/extract 字样。",
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
    if state.get("revision") != 46 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_46_AND_S046")
    for required in (AUDIT, C6, MATRIX):
        if not (root / required).is_file():
            raise SystemExit(f"REQUIRED_FILE_MISSING:{required}")

    new_hashes = {AUDIT: sha(root / AUDIT), C6: sha(root / C6), MATRIX: sha(root / MATRIX)}
    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    if observed_stale:
        raise SystemExit(f"UNEXPECTED_STALE:{observed_stale[:5]}")

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "derived_development_audit",
        "path": AUDIT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "BOUNDED_DEFENSE_SCOPED",
        "full_sources": [AUDIT, C6, MATRIX,
                         ".codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/full-1610.09254.txt",
                         ".codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/full-2011.03660.txt",
                         ".codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/abstracts.txt",
                         "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"],
        "source_hashes": {AUDIT: new_hashes[AUDIT], C6: new_hashes[C6], MATRIX: new_hashes[MATRIX]},
        "resolution": {
            "reason": "Fixed-set audit D1-D5: no FOUND_CANDIDATE; every audited self-claim carries its assumptions explicitly (countable choice, proposition extensionality, partiality, resource-bounded implementation, explicit satAC parameters).",
            "evidence": [AUDIT, C6],
        },
        "scope": "Audit derived developments for self-claims of computation/extraction/serialization/delivery beyond their interfaces. Result: BOUNDED_DEFENSE (scoped); negative result limited to D1-D5 versions and checked levels. No mathematical claim.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, AUDIT, C6, MATRIX],
        "source_hashes": {AUDIT: new_hashes[AUDIT], C6: new_hashes[C6]},
        "mathematical_status": "NO_NEW_MATHEMATICS_BOUNDED_AUDIT_DEFENSE",
        "cognition_status": "DERIVED_DEVELOPMENT_AUDIT_BOUNDED_DEFENSE_AND_PARTIAL_DECISION_ROUTED",
        "scope": "Run the N5 fixed-set audit, record the scoped bounded defense, route N6; no claim upgrade.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-031" if rid.startswith("I-DIRECTION") else "20260912-outcome-031"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        if AUDIT not in rec["full_sources"]:
            rec["full_sources"].append(AUDIT)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the N5 derived-development audit: scoped BOUNDED_DEFENSE; the first work package is the N6 MP-PARTIAL-DECISION-001 machine boundary."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the scoped bounded defense for derived-development self-claims; the next strand is N6."
    )

    state["revision"] = 47
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N6: build MP-PARTIAL-DECISION-001 in native Cubical Agda. Fix a minimal quotient model with a representative-dependent classifier property; "
            "machine-prove that no total Bool classifier compatible with the quotient exists; construct a partial classifier into a delay/partiality structure as a positive control; "
            "and show that any consumer treating the partial classifier as total either does not return on a specified input or must explicitly add a modulus/decidability/section. "
            "Expected verdict at most REPRESENTATION_BOUNDARY. Do not rename the race/timeout or R036/R038 counterexamples; if the result only reproduces the trivial partial-vs-total fact "
            "without the quotient structure, stop the sub-direction."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "kind": "derived_development_audit",
        "new_machine_proofs": [],
        "proof_sources_changed": False,
        "claim_matrix_sha256": new_hashes[MATRIX],
        "evidence": {"audit": AUDIT, "c6": C6, "sources": ".codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/"},
        "mathematics": "NO_NEW_MATHEMATICS / BOUNDED_DEFENSE_SCOPED",
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
            "This in-scope checkpoint records the N5 derived-development audit (scoped BOUNDED_DEFENSE) and routes N6 MP-PARTIAL-DECISION-001. "
            "No mathematical claim is upgraded. No Git commit, tag or push."
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
        "revision": 47,
        "session_id": SESSION_ID,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
