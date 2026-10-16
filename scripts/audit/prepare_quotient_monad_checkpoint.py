#!/usr/bin/env python3
"""Prepare revision 36: record MP-QUOTIENT-MONAD-001 and route the next package.

The run constructs the quotient-valued continuation monad for the R041 delay
fragment (C-84–C-88): canonical section of the result quotient, bindQQ, unit
laws and associativity, with no choice principle needed. The checkpoint
records the result and session, repairs the twelve stale source hashes caused
by the third claim-matrix growth and the two index README updates, and moves
the projections to revision 36.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-036-QUOTIENT-MONAD"
PREV_SESSION = "S-RES-20260912-035-CONTEXTUAL-EQUIVALENCE"
RESULT_ID = "A-QUOTIENT-MONAD-FORMAL-001"
PROOF_ID = "MP-QUOTIENT-MONAD-001"
RUN_ID = "20260912-MP-QUOTIENT-MONAD-001-01"
SOURCE = "HoTT/formal/partiality-race-timeout/QuotientMonad.agda"
SOURCE_README = "HoTT/formal/partiality-race-timeout/QuotientMonad.README.md"
DEP_SOURCE = "HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
AUDIT_DOC = "audit/quotient-monad机器证明实施证据-20260912.md"
NEW_STATUS = "QUOTIENT_MONAD_CONSTRUCTED_CONTEXT_CHARACTERIZATION_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_quotient_monad", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "本轮以正面结构结果继续深化同一片段，再次没有把表示边界包装成内部矛盾，符合“找现实相对非现实性而非内部矛盾”的航向。"),
        "KC-000012": ("DEEPENED", "ASK 的资格问题被分层：结果商的组合结构本身成立（单子），资格越级只可能发生在自然接口层。"),
        "KC-000013": ("DEEPENED", "理论工具性/异化的边界被再次定位：经济收益（遗忘完成先后）不破坏组合结构，但也不会自动给出 race/deadline 能力。"),
        "KC-000014": ("ALIGNED", "方向 B 再获校准：存在/分类商可以承载单子结构；把“结果类”提升为“含完成先后的交付”仍不可推出。"),
        "KC-000021": ("ALIGNED", "用户要求真实机器运行；本轮同一工具链 final run exit 0 且 exact replay。"),
        "KC-000022": ("ALIGNED", "两类现实相对判别的工具在 partiality 片段进一步精确化；本轮结论是正面结构结果，不是悖论。"),
        "KC-000024": ("DEEPENED", "“以理论内逻辑关系超越时序”被进一步分离：单子结构存在，但上下文等价层次仍要求保留时序，两者不冲突。"),
        "KC-000029": ("DEEPENED", "“理论经济收益的高风险位置”被再次具体化：经济收益可分裂商上仍保持一致组合，说明风险不在商本身而在使用层。"),
        "KC-000031": ("ALIGNED", "HoTT 严格性再次表现为正面结构（商可分裂、单子成立），不是 coverage failure。"),
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
            ("NOT_TOUCHED", "本轮聚焦结果商的 canonical section 与商值 continuation 单子；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S036/SESSION.md；核心认知.md `{unit['id']}` | `≡c` 刻画、更宽上下文语言、natural consumer 与 ERCF-3 仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — 商值 continuation 单子闭合（`C-84`–`C-88`）；第一工作包转为 `≡c` 完整刻画与更宽上下文语言；revision 36/generation 020。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-QUOTIENT-MONAD`（`MACHINE_PROVED_LOCAL_UNCOMMITTED / MONAD_STRUCTURE_CONSTRUCTED`）。",
        "- update_decision: `MP-QUOTIENT-MONAD-001 进入 formal/run/index/STATE；C-84–C-88 进入 claim matrix；五个旧包按 row-stable/exact 重验后更新矩阵哈希。`",
        "- cross_conflicts: `NONE_OBSERVED` — 五个 proof 包在同一矩阵上全部通过验证。",
        "- unresolved: `≡c` 完整刻画、更宽上下文语言、natural consumer、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮数学状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / MONAD_STRUCTURE_CONSTRUCTED`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    lines = [
        f"# {SESSION_ID}",
        "",
        "- 触发：S035 方向更新后的第一工作包（一般商单子的第一部分）。",
        "- 构造：`isSetDelay`（经 `Unit ⊎ (ℕ × A)` Iso）、`canon`/`canon-respects`、`sec : Q A → Delay A`（集合商 rec）、`bindQQ`（商值 continuation bind）、单位律与关联律（代表层模 ≈ + 商层 `≋`）。",
        "- 结果：`MP-QUOTIENT-MONAD-001`（C-84–C-88）通过 kernel：结果商可分裂（canonical section），商值 continuation 单子成立，无需选择公理。判词 `MONAD_STRUCTURE_CONSTRUCTED`（正面结果，非悖论）。",
        "- 运行：final run `20260912-MP-QUOTIENT-MONAD-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。",
        "- 旧证据：矩阵第三次增长后，四个旧包（Lean、truncation、race/timeout、contextual equivalence）均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。",
        "- 失败谱系：本轮按责任点记录 `⊥-rec`/`rec` 命名冲突、Iso 导入格式、关联律 statement 的 level/类型参数、`eq/` 与商类混淆、where 块隐式绑定；命题未削弱。",
        "- 边界：不推广到一般无 section 的商；不证明 `≡c` 完整刻画、更宽上下文语言、现实失配或 HoTT 内部矛盾；不启动 ERCF-3。",
        "- 三件套：direction/panorama revision 36/generation 020；core 不变（无新用户原文）。",
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
    if state.get("revision") != 35 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_35_AND_S035")

    run_dir = root / "HoTT/verification/runs" / RUN_ID
    run = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8"))
    if (
        run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        or run.get("exit_code") != 0
        or run.get("proof_id") != PROOF_ID
        or run.get("claim_ids") != [f"C-{n}" for n in range(84, 89)]
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
        ("A-CONTEXTUAL-EQUIV-FORMAL-001", MATRIX),
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

    row_stable_note = "After C-84 through C-88 were appended (S036), replay returned ROW_STABLE_AFTER_INDEX_EVOLUTION with EXACT_EXIT_STDOUT_STDERR_MATCH; frozen proof/claim rows unchanged."
    for rid in (
        "A-ERCF-FACTORIZATION-FORMAL-001",
        "A-ERCF-TRUNCATION-DEFENSE-001",
        "A-RACE-TIMEOUT-FORMAL-001",
        "A-CONTEXTUAL-EQUIV-FORMAL-001",
        "S-RES-20260912-028-ERCF-FACTORIZATION-LEAN",
        "S-RES-20260912-031-ERCF-TRUNCATION-DEFENSE",
    ):
        rec = state["records"][rid]
        rec.setdefault("source_hashes", {})[MATRIX] = new_hashes[MATRIX]
        rec["revalidation"] = row_stable_note

    economy = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    economy["source_hashes"][MATRIX] = new_hashes[MATRIX]
    economy["revalidation"] = "S036 added the quotient-valued continuation monad (C-84–C-88); the fragment's quotient is split, so the R041 §2.1 choice obstruction does not arise here. C4 text is unchanged and the rest stays open."
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", AUDIT_DOC):
        if rel not in economy["full_sources"]:
            economy["full_sources"].append(rel)
    economy["mathematical_status"] = "FACTORIZATION_TRUNCATION_PARTIALITY_CONTEXT_AND_QUOTIENT_MONAD_PROVED_NATURAL_CONSUMER_OPEN"

    gate = state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"]
    gate["source_hashes"].update({MATRIX: new_hashes[MATRIX], FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    for rel in (SOURCE, SOURCE_README, f"HoTT/verification/runs/{RUN_ID}/RUN.json", f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json", f"HoTT/verification/runs/{RUN_ID}/source-manifest.json", AUDIT_DOC):
        gate["source_hashes"][rel] = new_hashes[rel]
        if rel not in gate["full_sources"]:
            gate["full_sources"].append(rel)
    gate["revalidation"] = "S036 appended the quotient-monad package; all five proof packages re-validated (four row-stable, one exact), and the gate structure is unchanged. Fresh-model behavior still NOT_RUN."
    gate["scope"] = "Require machine proof source/run/index before delivery. Lean, native Cubical truncation, partiality race/timeout, contextual equivalence and quotient-monad packages pass; dependencies are publisher/hash pinned and old index rows remain immutable. Fresh-model behavior and Git version closure remain open."

    s032 = state["records"]["S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"]
    s032["source_hashes"].update({FORMAL_README: new_hashes[FORMAL_README], RUNS_README: new_hashes[RUNS_README]})
    s032["revalidation"] = "S036 appended the quotient-monad package to both human-readable proof indexes; the S032 alignment itself is unchanged."

    direction_rec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_rec["projection_generation"] = "20260912-direction-020"
    direction_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    direction_rec["scope"] = "Portfolio after the quotient-valued continuation monad: the result quotient of the R041 fragment is split and carries a monad; the first work package is the full characterization of ≡c plus a wider context language."
    panorama_rec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_rec["projection_generation"] = "20260912-outcome-020"
    panorama_rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
    panorama_rec["scope"] = "Panorama includes the quotient-monad result C-84–C-88 alongside the partiality boundary and contextual-equivalence hierarchy; natural consumer remains unfound."
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
        "classification": "MONAD_STRUCTURE_CONSTRUCTED",
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(84, 89)],
        "run_id": RUN_ID,
        "mathematical_status": "RESULT_QUOTIENT_SPLIT_AND_QUOTIENT_VALUED_MONAD_CONSTRUCTED",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-MATH-PROOF-DELIVERY-GATE-001", "A-RACE-TIMEOUT-FORMAL-001", "A-CONTEXTUAL-EQUIV-FORMAL-001"],
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
        "scope": "Native Cubical Agda monad structure on the result quotient of the R041 delay fragment: canonical section (C-84), quotient-valued continuation bind (C-85), unit laws (C-86) and associativity (C-87 representative-level up to ≈, C-88 quotient-level). Positive structure result; no general-quotient claim, no HoTT paradox.",
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
            "scripts/audit/prepare_quotient_monad_checkpoint.py",
        ],
        "source_hashes": {
            SOURCE: new_hashes[SOURCE],
            f"HoTT/verification/runs/{RUN_ID}/RUN.json": new_hashes[f"HoTT/verification/runs/{RUN_ID}/RUN.json"],
            AUDIT_DOC: new_hashes[AUDIT_DOC],
        },
        "mathematical_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED_MONAD_STRUCTURE_CONSTRUCTED",
        "cognition_status": "QUOTIENT_MONAD_CONSTRUCTED_AND_CONTEXT_CHARACTERIZATION_ROUTED",
        "scope": "Run the quotient-monad work package natively, produce C-84–C-88 with run/index evidence, revalidate the four older packages row-stable, and route the ≡c characterization plus wider context language as the next package.",
    }

    state["revision"] = 36
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": "In Agda 2.8.0/Cubical v0.9, prove the lt/leb trichotomy and use it to show that on the Bool fragment contextual equivalence ≡c coincides with representational equality (p ≡c q ↔ p ≡ q); then extend the context family with quotient-valued continuations (via bindQQ) and check whether the coarsest respected equivalence still strictly keeps timing.",
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "proof_id": PROOF_ID,
        "claim_ids": [f"C-{n}" for n in range(84, 89)],
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
            "20260912-MP-CONTEXTUAL-EQUIV-001-01": "ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "stale_source_hash_repair": {"observed": 12, "unexpected_remainder": 0},
        "evidence": {"run": f"HoTT/verification/runs/{RUN_ID}/", "audit": AUDIT_DOC, "matrix": MATRIX},
        "post_checkpoint_required": [
            "fresh three-way receipt regenerated at revision 36",
            "projection freshness PASS (27 directions / 32 outcomes)",
            "three-way PASS and core 36 units PASS",
            "checkpoint result CHECKPOINT_COMMITTED revision 36",
            "no write lock / transaction residual",
        ],
        "mathematics": "MACHINE_PROVED_LOCAL_UNCOMMITTED / MONAD_STRUCTURE_CONSTRUCTED",
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
        "authorization": "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. This in-scope checkpoint records the machine-proved quotient-valued continuation monad (C-84–C-88), fixes the twelve stale source hashes created by the third claim-index growth and the two index README updates, and routes the ≡c characterization work package. No Git commit, tag or push.",
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
        "revision": 36,
        "session_id": SESSION_ID,
        "stale_repaired": len(expected_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
