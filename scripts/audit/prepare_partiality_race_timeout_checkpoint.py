#!/usr/bin/env python3
"""Prepare revision 34: record MP-RACE-TIMEOUT-001 and route the next package.

The native Cubical Agda run proves the R041 operation-closure boundary
(C-71–C-76): bind congruence and set-quotient descent, race/deadline
non-descent and no quotient-level race selector. This checkpoint records the
formal result and session, updates every stale source hash touched by the
claim-matrix growth and the two human-readable proof indexes, and moves the
projections to revision 34.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-034-PARTIALITY-RACE-TIMEOUT"
PREV_SESSION = "S-GOV-20260912-033-HANDOVER-VERIFICATION"
RESULT_ID = "A-RACE-TIMEOUT-FORMAL-001"
PROOF_ID = "MP-RACE-TIMEOUT-001"
RUN_ID = "20260912-MP-RACE-TIMEOUT-001-01"
PACKAGE = "HoTT/formal/partiality-race-timeout"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/partiality-race-timeout机器证明实施证据-20260912.md"
NEW_STATUS = "PARTIALITY_RACE_TIMEOUT_REPRESENTATION_BOUNDARY_PROVED_CONTEXTUAL_EQUIVALENCE_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_partiality_race", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "本轮再次交付表示边界而非内部矛盾，直接服务“找现实相对非现实性而非内部矛盾”的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题在 partiality 商上被机器化：结果类不携带完成先后资格，race/deadline 不能下降。"),
        "KC-000013": ("DEEPENED", "理论工具性/异化在 partiality 片段出现具体边界：忘记时序的经济收益真实存在，但竞争 consumer 被机器逻辑阻断。"),
        "KC-000014": ("ALIGNED", "方向 B（数学上取得存在/分类后被提升为有效交付）获得一个具体否证点：结果类不能提升为含完成先后的交付。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮原生 Cubical Agda final run exit 0 且有 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在 partiality 片段推进：第一类与第二类都没有被证实，边界被精确化为 REPRESENTATION_BOUNDARY。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”获得机器化边界实例：结果商遗忘完成先后，理论也不从商上给出该能力。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”被具体化：忘记时序正是经济收益，race/deadline 是不可下降的消费方。"),
        "KC-000031": ("ALIGNED", "HoTT 严格性再次表现为边界/防御（REPRESENTATION_BOUNDARY），不是 coverage failure。"),
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
            ("NOT_TOUCHED", "本轮聚焦 R041 partiality 结果商的 bind/race/deadline 操作闭包；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S034/SESSION.md；核心认知.md `{unit['id']}` | natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — `DIR-W-RACE-TIMEOUT` 由 `NEXT_CANDIDATE` 变为 `CLOSED_WITH_SCOPE`（`REPRESENTATION_BOUNDARY`）；第一工作包转为 contextual equivalence 层次；revision 34/generation 018。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-PARTIALITY-RACE-TIMEOUT`（`MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`）；R041 行注明已有原生机器对应。",
        "- update_decision: `MP-RACE-TIMEOUT-001 进入 formal/run/index/STATE；C-71–C-76 进入 claim matrix；两个旧 proof 的 matrix hash 按 row-stable 重验后更新。`",
        "- cross_conflicts: `NONE_OBSERVED` — 新旧 proof 在同一矩阵上均通过验证（新 run exact snapshot；旧 run row-stable exact replay）。",
        "- unresolved: `contextual equivalence、一般商单子、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`，不是悖论。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：方向追踪 §6 第 4 项第一工作包 `DIR-W-RACE-TIMEOUT`；R041 纸笔原型（`PAPER_ONLY`）的核心操作闭包在原生 Cubical Agda 中重做。",
        "- 构造：`Delay A = ω | ret n a`（R041 单次返回族与 ω 的忠实表示）；`≈` 为 R041 §1 收敛行为等价；`bind`/`race` 逐子句采用 R041 §1；`deadline` 为 R041 §6 截止期观察的有限形式；商用 Cubical `SetQuotients` 与 `effective`。",
        "- 结果：`MP-RACE-TIMEOUT-001` 通过 kernel；C-71 bind 同余、C-72 固定 continuation 的商下降、C-73 race 非同余、C-74 完成性差异、C-75 截止期分离、C-76 商上无 race 选择子。判词 `REPRESENTATION_BOUNDARY`。",
        "- 运行：final run `20260912-MP-RACE-TIMEOUT-001-01`（Agda 2.8.0 + Cubical v0.9；`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。",
        "- 旧证据：矩阵增长后 `MP-ERCF-001` 与 `MP-ERCF-TRUNC-001` 均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay，冻结行未被改写。",
        "- 失败谱系：编译迭代中的层级/解析/商元素类型问题全部按责任点修复，命题未削弱（见 audit 证据文档 §5）。",
        "- 自然 consumer：在已核证据内未找到把结果商提升为含完成先后交付能力的实际 HoTT consumer；不升级为 `NATURAL_USAGE_MISMATCH`，不提前启动 ERCF-3。",
        "- 三件套：direction/panorama revision 34/generation 018；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 33 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_33_AND_S033")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(71, 77)]
    ):
        raise SystemExit("FINAL_RUN_NOT_ACCEPTED_AND_INDEXED")
    for required in ("index-row-manifest.json", "source-manifest.json", "stdout.txt", "stderr.txt", "environment.txt"):
        if not (run_dir / required).is_file():
            raise SystemExit(f"RUN_FILE_MISSING:{required}")

    new_hashes = {
        MATRIX: sha(root / MATRIX),
        FORMAL_README: sha(root / FORMAL_README),
        RUNS_README: sha(root / RUNS_README),
        f"{PACKAGE}/PartialityRaceTimeout.agda": sha(root / f"{PACKAGE}/PartialityRaceTimeout.agda"),
        f"{PACKAGE}/README.md": sha(root / f"{PACKAGE}/README.md"),
        f"{PACKAGE}/TOOLCHAIN.json": sha(root / f"{PACKAGE}/TOOLCHAIN.json"),
        f"{PACKAGE}/AGDA_LIBRARIES": sha(root / f"{PACKAGE}/AGDA_LIBRARIES"),
        f"HoTT/verification/runs/{RUN_ID}/RUN.json": sha(run_dir / "RUN.json"),
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": sha(run_dir / "index-row-manifest.json"),
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": sha(run_dir / "source-manifest.json"),
        "scripts/audit/mark_proof_run_indexed.py": sha(root / "scripts/audit/mark_proof_run_indexed.py"),
        AUDIT_DOC: sha(root / AUDIT_DOC),
    }

    expected_stale = {
        ("A-ERCF-FACTORIZATION-FORMAL-001", MATRIX),
        ("A-ERCF-TRUNCATION-DEFENSE-001", MATRIX),
        ("A-HOTT-SELF-VALIDATION-ECONOMY-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", FORMAL_README),
        ("A-MATH-PROOF-DELIVERY-GATE-001", RUNS_README),
        ("S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT", FORMAL_README),
        ("S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT", RUNS_README),
        ("S-RES-20260912-028-ERCF-FACTORIZATION-LEAN", MATRIX),
        ("S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE", MATRIX),
    }
    observed_stale = set()
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            if not path.is_file() or sha(path) != exp:
                observed_stale.add((rid, rel))
    if observed_stale != expected_stale:
        raise SystemExit(f"UNEXPECTED_STALE_SET:{sorted(observed_stale)}")

    row_stable_note = "After C-71 through C-76 were appended (S034), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S034 added the native partiality boundary result (C-71–C-76); C4 text is unchanged and the paper-only remainder (natural consumer, reality bridge, ERCF-3) stays open."
    for rel in (
        f"{PACKAGE}/PartialityRaceTimeout.agda",
        f"{PACKAGE}/README.md",
        f"HoTT/verification/runs/{RUN_ID}/RUN.json",
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
        AUDIT_DOC,
    ):
        if rel not in economy["full_sources"]:
            economy["full_sources"].append(rel)
    economy["mathematical_status"] = "GENERAL_FACTORIZATION_TRUNCATION_DEFENSE_AND_PARTIALITY_BOUNDARY_PROVED_NATURAL_CONSUMER_OPEN"

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"][MATRIX] = new_hashes[MATRIX]
    gate["source_hashes"][FORMAL_README] = new_hashes[FORMAL_README]
    gate["source_hashes"][RUNS_README] = new_hashes[RUNS_README]
    for rel, value in new_hashes.items():
        if rel.startswith(PACKAGE) or rel.startswith("HoTT/verification/runs") or rel.endswith("mark_proof_run_indexed.py") or rel == AUDIT_DOC:
            gate["source_hashes"][rel] = value
            if rel not in gate["full_sources"]:
                gate["full_sources"].append(rel)
    gate["revalidation"] = "S034 appended the partiality race/timeout package; both older proof packages re-validated row-stable and the new native run is exact-index-matched. Gate structure unchanged; fresh-model behavior still NOT_RUN."
    gate["scope"] = "Require machine proof source/run/index before delivery. Lean, native Cubical truncation and native Cubical partiality packages pass; external toolchains are publisher/hash pinned and old index rows remain immutable. Fresh-model behavior and Git version closure remain open."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"][FORMAL_README] = new_hashes[FORMAL_README]
    s032["source_hashes"][RUNS_README] = new_hashes[RUNS_README]
    s032["revalidation"] = "S034 appended the partiality race/timeout package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-018"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_PARTIALITY_RACE_TIMEOUT_REPRESENTATION_BOUNDARY_PROVED_CONTEXTUAL_EQUIVALENCE_NEXT"
    direction_rec["scope"] = "Portfolio after the native partiality race/timeout boundary: DIR-W-RACE-TIMEOUT is closed with scope (REPRESENTATION_BOUNDARY); the first work package is the contextual-equivalence hierarchy and the general quotient monad question."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-018"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_PARTIALITY_RACE_TIMEOUT_REPRESENTATION_BOUNDARY_PROVED_CONTEXTUAL_EQUIVALENCE_NEXT"
    panorama_rec["scope"] = "Panorama includes the machine-proved partiality quotient boundary C-71–C-76 alongside the truncation defense; natural consumer remains unfound and ERCF-3 stays deferred."
    for rec in (direction_rec, panorama_rec):
        for rel in (
            f"{PACKAGE}/PartialityRaceTimeout.agda",
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            AUDIT_DOC,
        ):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)

    source_rel = f"{PACKAGE}/PartialityRaceTimeout.agda"
    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": source_rel,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "REPRESENTATION_BOUNDARY",
        "proof_id": PROOF_ID,
        "claim_ids": ["C-71", "C-72", "C-73", "C-74", "C-75", "C-76"],
        "run_id": RUN_ID,
        "mathematical_status": "PARTIALITY_QUOTIENT_OPERATION_BOUNDARY_NOT_PARADOX",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [
            source_rel,
            f"{PACKAGE}/README.md",
            f"{PACKAGE}/TOOLCHAIN.json",
            f"{PACKAGE}/AGDA_LIBRARIES",
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            f"HoTT/verification/runs/{RUN_ID}/stdout.txt",
            f"HoTT/verification/runs/{RUN_ID}/stderr.txt",
            f"HoTT/verification/runs/{RUN_ID}/environment.txt",
            MATRIX,
            "scripts/audit/capture_agda_proof_run.py",
            "scripts/audit/mark_proof_run_indexed.py",
            "scripts/audit/freeze_proof_index_rows.py",
            "scripts/audit/verify_formal_proof_run.py",
            AUDIT_DOC,
        ],
        "source_hashes": {
            source_rel: new_hashes[source_rel],
            f"{PACKAGE}/README.md": new_hashes[f"{PACKAGE}/README.md"],
            f"{PACKAGE}/TOOLCHAIN.json": new_hashes[f"{PACKAGE}/TOOLCHAIN.json"],
            f"{PACKAGE}/AGDA_LIBRARIES": new_hashes[f"{PACKAGE}/AGDA_LIBRARIES"],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX],
            "scripts/audit/mark_proof_run_indexed.py": new_hashes["scripts/audit/mark_proof_run_indexed.py"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0; source, toolchain, external dependency and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX,
                "scripts/audit/verify_formal_proof_run.py",
                AUDIT_DOC,
            ],
        },
        "scope": "Native Cubical Agda over the R041 deterministic delay model: bind congruence and fixed-continuation set-quotient descent (C-71, C-72); race non-congruence, completion gap and deadline separation (C-73 to C-75); no quotient-level race selector (C-76). REPRESENTATION_BOUNDARY, not a HoTT paradox; no reality bridge or originality claim.",
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [
            session_path,
            audit_path,
            runs_path,
            source_rel,
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            AUDIT_DOC,
            "scripts/audit/prepare_partiality_race_timeout_checkpoint.py",
        ],
        "source_hashes": {
            source_rel: new_hashes[source_rel],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_REPRESENTATION_BOUNDARY",
        "cognition_status": "PARTIALITY_RACE_TIMEOUT_BOUNDARY_MACHINE_PROVED_AND_CONTEXTUAL_EQUIVALENCE_ROUTED",
        "scope": "Run the first DIR-W-RACE-TIMEOUT work package natively, produce C-71–C-76 with run/index evidence, revalidate both older proof packages row-stable, and route the contextual-equivalence hierarchy as the next package.",
    }

    state["revision"] = 34
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, define the fixed context family (bind, race, deadline and composites) on the R041 delay model; define the coarsest equivalence respected by every context; prove result equivalence is strictly coarser than it; then evaluate the general quotient monad Q(A)×(A→Q(B))→Q(B) and its choice/weak-bisimulation requirements.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-71", "C-72", "C-73", "C-74", "C-75", "C-76"],
        "final_run": {
            "run_id": RUN_ID,
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "older_proofs_after_matrix_growth": {
            "20260912-MP-ERCF-001-02": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
            "20260912-MP-ERCF-TRUNC-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "stale_source_hash_repair": {"observed": 10, "unexpected_remainder": 0},
        "evidence": {
            "run": f"HoTT/verification/runs/{RUN_ID}/",
            "audit": AUDIT_DOC,
            "matrix": MATRIX,
        },
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 34",
            "projection freshness PASS (27 directions / 30 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 34",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    # The trio/FRONTIER/RESUME edits were drafted in this session; they are held
    # under the session evidence directory and only written to the working tree
    # by the checkpoint transaction (state files must not change outside it).
    pending = root / SESSION_REL / "evidence/pending-edits"
    memory = (pending / "MEMORY.md").read_text(encoding="utf-8")
    direction = (pending / R.DIRECTION).read_text(encoding="utf-8")
    panorama = (pending / R.PANORAMA).read_text(encoding="utf-8")
    frontier = (pending / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    resume = (pending / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")

    texts = {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved partiality race/timeout boundary (C-71–C-76), fixes the ten stale source hashes created by the append-only claim index, and routes the contextual-equivalence work package. No Git commit, tag or push.",
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
        "revision": 34,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
