#!/usr/bin/env python3
"""Prepare revision 35: record MP-CONTEXTUAL-EQUIV-001 and route the next package.

The run proves the contextual-equivalence hierarchy for the R041 delay
fragment (C-77–C-83): ≡c refines result equivalence and is strictly finer
(timing, divergence and value separation); result equivalence is strictly
coarser. The checkpoint records the result and session, repairs every stale
source hash caused by the second claim-matrix growth and the two index
README updates, and moves the projections to revision 35.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-035-CONTEXTUAL-EQUIVALENCE"
PREV_SESSION = "S-RES-20260912-034-PARTIALITY-RACE-TIMEOUT"
RESULT_ID = "A-CONTEXTUAL-EQUIV-FORMAL-001"
PROOF_ID = "MP-CONTEXTUAL-EQUIV-001"
RUN_ID = "20260912-MP-CONTEXTUAL-EQUIV-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/ContextualEquivalence.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/ContextualEquivalence.README.md"
DEP_SOURCE = "HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/contextual-equivalence机器证明实施证据-20260912.md"
NEW_STATUS = "CONTEXTUAL_EQUIVALENCE_STRICTLY_FINER_PROVED_QUOTIENT_MONAD_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_contextual_equiv", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "本轮继续交付表示/替换边界而非内部矛盾，直接服务“找现实相对非现实性而非内部矛盾”的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题推进到替换原则：在固定上下文族下，结果等价不能作为 race/deadline 语言中的替换依据。"),
        "KC-000013": ("DEEPENED", "理论工具性的边界被再次具体化：结果商的经济收益真实，但更宽的上下文族要求保留时序。"),
        "KC-000014": ("ALIGNED", "方向 B 再获一个具体否证点：结果类不能提升为含完成先后的交付，且该否证在上下文层被加强。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0 且 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别在 partiality 片段达到“上下文等价严格细于结果等价”的层次定理；仍未证实悖论。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”被进一步排除：完整固定上下文族尊重的最粗等价必须保留时序。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”再次被具体化：忘记时序的经济收益在含 race/deadline 的上下文族中不可作为替换原则。"),
        "KC-000031": ("ALIGNED", "HoTT 严格性再一次表现为边界/防御（REPRESENTATION_BOUNDARY），不是 coverage failure。"),
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
            ("NOT_TOUCHED", "本轮聚焦 R041 delay 片段的上下文等价层次；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S035/SESSION.md；核心认知.md `{unit['id']}` | 一般商单子、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — 上下文等价层次闭合（`C-77`–`C-83`）；第一工作包转为一般商单子与更宽上下文语言；revision 35/generation 019。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-CONTEXTUAL-EQUIVALENCE`（`MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`）。",
        "- update_decision: `MP-CONTEXTUAL-EQUIV-001 进入 formal/run/index/STATE；C-77–C-83 进入 claim matrix；四个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 四个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `一般商单子、更宽上下文语言、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`，不是悖论。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S034 方向更新后的第一工作包（操作族下的 contextual equivalence 层次）。",
        "- 构造：上下文族 `hole`/`cbind`/`crace₁`/`crace₂` + `plug`；上下文等价 `p ≡c q` = 全部上下文保持 `≈` 且全部“上下文+deadline k”不可区分；分离工具为 deadline 0、与 ω 的 race、值移动延续 `x ↦ ret 0 (not x)`、时间对齐 race（`leb-refl`/`lt-leb`）。",
        "- 结果：`MP-CONTEXTUAL-EQUIV-001`（C-77–C-83）通过 kernel：`≡c` 为等价关系并精化 `≈`；时序、发散、值差异均被严格分离；结果等价严格粗于上下文等价（`C-83`）。判词 `REPRESENTATION_BOUNDARY`（强化版）。",
        "- 运行：final run `20260912-MP-CONTEXTUAL-EQUIV-001-01`（Agda 2.8.0 + Cubical v0.9；`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）；依赖同目录冻结模块 `PartialityRaceTimeout.agda`（未改写）。",
        "- 旧证据：矩阵第二次增长后，`MP-ERCF-001`、`MP-ERCF-TRUNC-001`、`MP-RACE-TIMEOUT-001` 均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：本包仅两处机械修正（`×` 导入；沿用显式量化/固定 fixity 风格），命题未削弱。",
        "- 边界：不证明所有上下文语言/race 政策下的最粗等价、一般商单子、现实并发失配或 HoTT 内部矛盾；不升级 `NATURAL_USAGE_MISMATCH`，不启动 ERCF-3。",
        "- 三件套：direction/panorama revision 35/generation 019；core 不变（无新用户原文）。",
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
    if state.get("revision") != 34 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_34_AND_S034")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(77, 84)]
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
        DEP_SOURCE: sha(root / DEP_SOURCE),
        f"HoTT/verification/runs/{RUN_ID}/RUN.json": sha(run_dir / "RUN.json"),
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": sha(run_dir / "index-row-manifest.json"),
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": sha(run_dir / "source-manifest.json"),
        AUDIT_DOC: sha(root / AUDIT_DOC),
    }

    expected_stale = {
        ("A-ERCF-FACTORIZATION-FORMAL-001", MATRIX),
        ("A-ERCF-TRUNCATION-DEFENSE-001", MATRIX),
        ("A-HOTT-SELF-VALIDATION-ECONOMY-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", MATRIX),
        ("A-MATH-PROOF-DELIVERY-GATE-001", FORMAL_README),
        ("A-MATH-PROOF-DELIVERY-GATE-001", RUNS_README),
        ("A-RACE-TIMEOUT-FORMAL-001", MATRIX),
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

    row_stable_note = "After C-77 through C-83 were appended (S035), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
        "A-RACE-TIMEOUT-FORMAL-001",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S035 added the contextual-equivalence hierarchy (C-77–C-83); C4 text is unchanged and the paper-only remainder (quotient monad, natural consumer, reality bridge, ERCF-3) stays open."
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
        if rel not in economy["full_sources"]:
            economy["full_sources"].append(rel)
    economy["mathematical_status"] = "GENERAL_FACTORIZATION_TRUNCATION_DEFENSE_PARTIALITY_AND_CONTEXT_BOUNDARY_PROVED_NATURAL_CONSUMER_OPEN"

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, DEP_SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S035 appended the contextual-equivalence package; all four proof packages re-validated (three row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."
    gate["scope"] = "Require machine proof source/run/index before delivery. Lean, native Cubical truncation, native Cubical partiality race/timeout and native Cubical contextual-equivalence packages pass; dependencies are publisher/hash pinned and old index rows remain immutable. Fresh-model behavior and Git version closure remain open."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S035 appended the contextual-equivalence package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-019"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the contextual-equivalence hierarchy: the fixed context family keeps timing; the first work package is the general quotient-valued continuation bind and a wider context language."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-019"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the contextual-equivalence hierarchy C-77–C-83: result equivalence is strictly coarser than the coarsest equivalence respected by the fixed context family; natural consumer remains unfound."
    for rec in (direction_rec, panorama_rec):
        for rel in (SOURCE, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)

    state["records"][RESULT_ID] = {
        "kind": "formal_mathematical_result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "REPRESENTATION_BOUNDARY",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(77, 84)],
        "run_id": RUN_ID,
        "mathematical_status": "CONTEXTUAL_EQUIVALENCE_STRICTLY_FINER_THAN_RESULT_EQUIVALENCE",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001", "A-RACE-TIMEOUT-FORMAL-001"],
        "full_sources": [
            SOURCE,
            SOURCE_README,
            DEP_SOURCE,
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
            SOURCE: new_hashes[SOURCE],
            SOURCE_README: new_hashes[SOURCE_README],
            DEP_SOURCE: new_hashes[DEP_SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            f"HoTT/verification/runs/{RUN_ID}/source-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/source-manifest.json"],
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json"],
            MATRIX: new_hashes[MATRIX],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "resolution": {
            "reason": "Final native Cubical run exited 0; source, dependency, toolchain and index-row hashes match; exact replay passed. Git version closure is not authorized.",
            "evidence": [
                f"HoTT/verification/runs/{RUN_ID}/RUN.json",
                f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
                MATRIX,
                "scripts/audit/verify_formal_proof_run.py",
                AUDIT_DOC,
            ],
        },
        "scope": "Native Cubical Agda contextual equivalence on the R041 delay fragment over the fixed context family (hole, bind, race on either side): ≡c is an equivalence, refines ≈, strictly separates timing/divergence/value differences, and result equivalence is strictly coarser. REPRESENTATION_BOUNDARY; no claim about all context languages, no quotient monad, no HoTT paradox.",
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
            SOURCE,
            f"HoTT/verification/runs/{RUN_ID}/RUN.json",
            f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
            AUDIT_DOC,
            "scripts/audit/prepare_contextual_equivalence_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_REPRESENTATION_BOUNDARY",
        "cognition_status": "CONTEXTUAL_EQUIVALENCE_STRICTNESS_PROVED_AND_QUOTIENT_MONAD_ROUTED",
        "scope": "Run the contextual-equivalence work package natively, produce C-77–C-83 with run/index evidence, revalidate the three older packages row-stable, and route the general quotient-valued continuation bind as the next package.",
    }

    state["revision"] = 35
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, construct the quotient-valued continuation bind Q(A)×(A→Q(B))→Q(B) using the canonical section of the ≈-quotient, or state the exact choice/QIIT boundary if the section fails; then extend the context family to a wider language and check whether the coarsest respected equivalence still keeps timing.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(77, 84)],
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
            "20260912-MP-RACE-TIMEOUT-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "stale_source_hash_repair": {"observed": 11, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 35",
            "projection freshness PASS (27 directions / 31 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 35",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

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
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved contextual-equivalence hierarchy (C-77–C-83), fixes the eleven stale source hashes created by the second claim-index growth and the two index README updates, and routes the quotient-monad work package. No Git commit, tag or push.",
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
        "revision": 35,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
