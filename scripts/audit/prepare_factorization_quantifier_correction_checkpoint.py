#!/usr/bin/env python3
"""Prepare revision 24 for the C4 factorization/observer quantifier correction."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-024-FACTORIZATION-QUANTIFIER-CORRECTION"
C4 = "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md"
NEW_C4_HASH = "369665f6953203d0ffc7d0bbf4f90a5ba9ff02fd8c1a886457d1d69ac36392d2"
SPEC = importlib.util.spec_from_file_location("runtime_factorization_correction", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000003": ("DEEPENED", "把 factorization 与纤维常值的关系收紧为无条件必要性；逆向需商/像泛性质、截面或选择。"),
        "KC-000015": ("CORRECTED", "非单射抽象并非对任意固定余域自动失败；必须给出实际能分离被合并状态的任务。"),
        "KC-000018": ("CORRECTED", "理论工具性/否定现实的普遍攻击被明确限定到足够分离的观察类。"),
        "KC-000029": ("CORRECTED", "理论经济 no-go 的量词改为分离观察族；固定 subsingleton 余域构成反控制。"),
        "KC-000031": ("DEEPENED", "最小覆盖反例必须显式给出 observables 与 interpretation criterion，不能只凭非单射。"),
        "KC-000032": ("DEEPENED", "存在性攻击需要指定能观察理论新增/遗漏差异的 context，而非从模型差异直接跳到失败。"),
        "KC-000035": ("DEEPENED", "HoTT 表达 factorization 骨架时需区分必要方向与依赖 quotient/image elimination 的充分方向。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    for unit in manifest["units"]:
        unit_id = str(unit["id"])
        relation, assessment = touched.get(unit_id, ("NOT_TOUCHED", "本轮只修正 C4 中 factorization/观察量词；该用户原文及其 S022 语义评估不变。"))
        counts[relation] = counts.get(relation, 0) + 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        unresolved = "ERCF-1/2 机器证明仍待执行。" if unit_id in touched else "既有数学未决保持。"
        lines.append(
            f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | C4 §6、§12.1；核心认知.md {unit_id} | {unresolved} |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — 用户原文、generation-4/36 KC、curation/manifest/transition 均不变。",
        "- direction_change: `NO_DIRECTION_CHANGE` — ERCF 主方向不变；只同步 source revision 24/projection generation 008。",
        "- panorama_change: `YES_RESULT_CORRECTION` — C4 的 paper-only 结论被收紧；结果状态不升级。",
        "- update_decision: `C4/implementation evidence/source+merge manifests/STATE source hash/MEMORY/LESSONS/RESUME 更新；core 不改。`",
        "- cross_conflicts: `RESOLVED` — 任意固定 Y 的过强结论由 subsingleton 反控制排除；正确命题要求 separating observation family，或允许 Y=R,J=id_R。",
        "- unresolved: `ERCF-1/2 的构造性条件、quotient/image elimination、proof-assistant 实现和 ERCF-3 仍开放。`",
        "", "## 汇总", "",
        f"`DEEPENED={counts.get('DEEPENED', 0)} / CORRECTED={counts.get('CORRECTED', 0)} / NOT_TOUCHED={counts.get('NOT_TOUCHED', 0)} / DEVIATED={counts.get('DEVIATED', 0)}`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    if R.sha((root / C4).read_bytes()) != NEW_C4_HASH:
        raise SystemExit("C4_CORRECTED_HASH_MISMATCH")
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 23 or state.get("latest_session") != "S-GOV-20260912-023-SELF-VALIDATION-FINAL-ALIGNMENT":
        raise SystemExit("EXPECTED_REVISION_23_S023")

    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"), "source_state_revision: 23", "source_state_revision: 24")
    direction = replace_once(direction, "projection_generation: 20260912-direction-007", "projection_generation: 20260912-direction-008")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"), "source_state_revision: 23", "source_state_revision: 24")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-007", "projection_generation: 20260912-outcome-008")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(
        memory,
        "- C4 共 724 行，SHA-256 `2116492f9ba6ba3426cee16e2f09a4267f733fca8bf8b5e9d20cb137119b29e4`；它将验证任务分五层，提出 ERCF、factorization 充分性、存在/不存在四分法、E₀/E₁ 与 Gödel/元层边界；状态为 `PAPER_ONLY`。",
        f"- C4 经量词纠偏后共 733 行，SHA-256 `{NEW_C4_HASH}`；它将验证任务分五层，提出 ERCF、任务相对 factorization、存在/不存在四分法、E₀/E₁ 与 Gödel/元层边界；状态仍为 `PAPER_ONLY`。纤维常值只无条件给出必要性，逆向需 quotient/image 泛性质、截面或选择；全局 no-go 需 separating observation family。",
    )
    marker = "- S023 只完成 post-verification/EOF 格式收尾：core 7/7、runtime 28/28、reader 17/17、three-way 4/4、36-KC audit、merge/register/history/fresh/projection 均通过；不改变 C4 数学状态。"
    memory = replace_once(memory, marker, marker + "\n- S024 修正 C4 的 factorization 逆向与观察余域量词；ERCF 方向不变，数学状态不升级。")

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "| 第一最小可验结果 | ERCF-1/2：`α:R→A` 的任务相对 factorization、平凡任务正例与观察敏感反例 | ready-for-formalization | 选定 Lean/Agda/HoTT 片段，证明 `ParadoxWitness(α,J) → ¬FactorsThrough(α,J)`，保存源码与真实运行 |",
        "| 第一最小可验结果 | ERCF-1/2：`α:R→A` 的任务相对 factorization、平凡任务正例与 separating observation 反例 | ready-for-formalization | 先证明无条件方向 `FactorsThrough→FiberConstant` 与 witness no-go；逆向只在明确 quotient/image 消去或 section/choice 条件下证明，并加入 subsingleton-Y 负控制 |",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "31. `FactorsThrough`" not in lessons:
        lessons += "\n31. `FactorsThrough(α,J)` 无条件推出 `FiberConstant(α,J)`，逆向却依赖像/商的消去泛性质、截面或选择；非单射也不保证对任意固定余域 Y 都有区分观察（subsingleton Y 是立即反例）。全局经济 no-go 必须显式量化 separating observation family，或允许 Y=R 与 J=id。"
    lessons += "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "S023 已完成 S022 的验证/EOF 格式收尾；S022 把用户当前原文纳入 generation-4 的 KC-000028–000036，并完成 C4 论证：",
        "S024 已修正 C4 的 factorization 逆向与观察量词：纤维常值只是无条件必要条件，全局 no-go 需要 separating observations；S023 完成验证/EOF 收尾，S022 把用户当前原文纳入 generation-4 的 KC-000028–000036，并完成 C4 主论证：",
    )

    state["revision"] = 24
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "FACTORIZATION_QUANTIFIER_CORRECTED_ERCF_FORMALIZATION_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "next_minimal_verification": "Formalize FactorsThrough→FiberConstant and ParadoxWitness no-go first; test converse only with explicit quotient/image/section assumptions and include a subsingleton-codomain negative control.",
    })
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-008"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-008"

    core_record = state["records"]["A-CORE-GENERATION-4-001"]
    core_record["source_hashes"] = {"核心认知.md": state["current_core"]["core_sha256"]}
    core_record["revalidation"] = "Removed the unrelated C4 research-document hash from the core-generation identity; core source/manifest/curation/transition were reverified unchanged."
    result_record = state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]
    result_record["source_hashes"][C4] = NEW_C4_HASH
    result_record["revalidation"] = "C4 was directly reread and corrected: factorization implies fiber constancy; the converse and global noninjectivity no-go now state their quotient/section and separating-observer assumptions."
    result_record["scope"] = "Distinguish finite checking from proof search and global self-truth; formulate ERCF with task-relative factorization and explicit separating-observer assumptions, existence/nonexistence distinctions, minimum-theory coverage criteria and Gödel/self-metatheory boundaries. Formalization and concrete divergence remain open."
    s022 = state["records"]["S-RES-20260912-022-SELF-VALIDATION-ECONOMY"]
    s022["source_hashes"][C4] = NEW_C4_HASH
    s022["revalidation"] = "The session's C4 output was corrected in S024 and rehashed; the original S022 checkpoint copies preserve the pre-correction version for audit."

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-GOV-20260912-023-SELF-VALIDATION-FINAL-ALIGNMENT", "A-HOTT-SELF-VALIDATION-ECONOMY-001"],
        "full_sources": [session_path, audit_path, runs_path, C4, "audit/核心认知generation-4与自反理论经济研究实施证据-20260912.md", "scripts/audit/prepare_factorization_quantifier_correction_checkpoint.py"],
        "source_hashes": {C4: NEW_C4_HASH},
        "mathematical_status": "PAPER_ONLY_QUANTIFIERS_CORRECTED_NOT_NATIVE_VERIFIED",
        "cognition_status": "FACTORIZATION_AND_OBSERVER_ASSUMPTIONS_CORRECTED",
        "scope": "Correct the unconditional fiber-constancy converse and fixed-codomain observer overclaim in C4; preserve ERCF direction and all core cognition while updating source hashes and verification routing.",
    }
    session = f"""# {SESSION_ID}

- 触发：最终数学复读发现 C4 把 `FiberConstant→FactorsThrough` 写成无条件等价，并对任意固定余域 Y 过快断言可构造区分观察。
- 修正：只保留 `FactorsThrough→FiberConstant` 的无条件方向；逆向要求 quotient/image elimination、section 或 choice。非单射 no-go 要求 task family 包含 separating observation；subsingleton Y 是负控制，允许 Y=R,J=id 是强控制。
- 影响：C4 hash、source/merge manifest、STATE source hash、MEMORY/FRONTIER/LESSONS/RESUME 和 projection revision 更新；core generation-4/36 KC 不变。
- 数学状态：ERCF 仍 `PAPER_ONLY`，未运行 proof assistant。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "old_c4_sha256": "2116492f9ba6ba3426cee16e2f09a4267f733fca8bf8b5e9d20cb137119b29e4",
        "new_c4_sha256": NEW_C4_HASH,
        "correction": [
            "FactorsThrough implies FiberConstant unconditionally",
            "FiberConstant converse requires explicit quotient/image elimination, section or choice assumptions",
            "noninjectivity needs a separating observer in the allowed task family; fixed subsingleton codomain is a negative control",
        ],
        "post_checkpoint_required": ["36/36 audit", "C4/source/merge hash checks", "fresh receipt revision 24", "projection freshness", "full regression", "git diff --check"],
        "mathematics": "PAPER_ONLY_NOT_NATIVE_VERIFIED", "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume, R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "The user requested a durable mathematical answer; correcting an overstrong quantifier claim and synchronizing its evidence hashes is an in-scope correctness action governed by the project checkpoint protocol.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 24, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
