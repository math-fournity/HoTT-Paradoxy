#!/usr/bin/env python3
"""Prepare revision 25 for the E0 witness and finite-decidability preconditions."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-025-MINIMAL-WITNESS-PRECONDITIONS"
C4 = "理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md"
OLD_HASH = "369665f6953203d0ffc7d0bbf4f90a5ba9ff02fd8c1a886457d1d69ac36392d2"
NEW_HASH = "8a5a88d9f11569c6bde145ce1944eadf063bb24784732a41c56bf95f8cc15f7a"
SPEC = importlib.util.spec_from_file_location("runtime_minimal_witness_preconditions", RUNTIME_PATH)
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
        "KC-000003": ("CORRECTED", "有限任务族不自动带来 factorization 可判定性；可执行实例还需有限类型/可判定相等等结构。"),
        "KC-000029": ("CORRECTED", "局部理论经济检验的可执行性必须声明数据与相等判定结构，不能由任务数量推出。"),
        "KC-000031": ("DEEPENED", "E₀ 最小见证补齐 `a₀:A` 与可区分 `s₀,s₁:S`，避免空 A 时伪造反例。"),
        "KC-000035": ("DEEPENED", "HoTT 表达 E₀ 时显式携带 inhabitance 和 inequality witnesses。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    for unit in manifest["units"]:
        unit_id = str(unit["id"])
        relation, assessment = touched.get(unit_id, ("NOT_TOUCHED", "本轮只补齐 E₀ inhabitance/inequality 与有限可判定性前提；该用户原文及其既有评估不变。"))
        counts[relation] = counts.get(relation, 0) + 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | C4 §9.1、§12.1、§15；核心认知.md {unit_id} | ERCF-1/2 proof assistant 仍未运行。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变。",
        "- direction_change: `NO_DIRECTION_CHANGE` — 只同步 source revision 25/projection generation 009。",
        "- panorama_change: `YES_RESULT_PRECONDITION_CORRECTION` — C4 形式化候选的前提更精确，状态仍 `PAPER_ONLY`。",
        "- update_decision: `C4/source+merge manifests/STATE source hashes/MEMORY/FRONTIER/LESSONS/RESUME 更新；core 不改。`",
        "- cross_conflicts: `RESOLVED` — 空 A 与不可判定相等的反控制已进入研究合同。",
        "- unresolved: `选定 proof assistant 后仍需决定有限实例和一般构造性命题的精确版本。`",
        "", "## 汇总", "",
        f"`CORRECTED={counts.get('CORRECTED', 0)} / DEEPENED={counts.get('DEEPENED', 0)} / NOT_TOUCHED={counts.get('NOT_TOUCHED', 0)}`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    if R.sha((root / C4).read_bytes()) != NEW_HASH:
        raise SystemExit("C4_PRECONDITION_HASH_MISMATCH")
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 24 or state.get("latest_session") != "S-RES-20260912-024-FACTORIZATION-QUANTIFIER-CORRECTION":
        raise SystemExit("EXPECTED_REVISION_24_S024")

    direction = replace_once((root / R.DIRECTION).read_text(encoding="utf-8"), "source_state_revision: 24", "source_state_revision: 25")
    direction = replace_once(direction, "projection_generation: 20260912-direction-008", "projection_generation: 20260912-direction-009")
    panorama = replace_once((root / R.PANORAMA).read_text(encoding="utf-8"), "source_state_revision: 24", "source_state_revision: 25")
    panorama = replace_once(panorama, "projection_generation: 20260912-outcome-008", "projection_generation: 20260912-outcome-009")
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_once(memory, OLD_HASH, NEW_HASH)
    marker = "- S024 修正 C4 的 factorization 逆向与观察余域量词；ERCF 方向不变，数学状态不升级。"
    memory = replace_once(memory, marker, marker + "\n- S025 补齐 E₀ 的 `a₀:A`/`s₀≠s₁` 见证，并明确有限任务族不自动推出 factorization 可判定。")
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "| 第一最小可验结果 | ERCF-1/2：`α:R→A` 的任务相对 factorization、平凡任务正例与 separating observation 反例 | ready-for-formalization | 先证明无条件方向 `FactorsThrough→FiberConstant` 与 witness no-go；逆向只在明确 quotient/image 消去或 section/choice 条件下证明，并加入 subsingleton-Y 负控制 |",
        "| 第一最小可验结果 | ERCF-1/2：`α:R→A` 的任务相对 factorization、平凡任务正例与 separating observation 反例 | ready-for-formalization | 给定 `a₀:A,s₀≠s₁:S`；先证明 `FactorsThrough→FiberConstant` 与 witness no-go；逆向声明 quotient/image/section 条件，有限执行声明有限类型/可判定相等，并加入 empty-A 与 subsingleton-Y 负控制 |",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "32. 最小反例中的乘积" not in lessons:
        lessons += "\n32. 最小反例中的乘积 `A×S` 需要实际给出 `a₀:A`；仅有 `s₀≠s₁:S` 在 A 为空时不能产生一对现实状态。有限任务族也不使函数相等或 factorization 自动可判定；可执行模型必须另给有限类型、可判定相等或具体枚举器。"
    lessons += "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "S024 已修正 C4 的 factorization 逆向与观察量词：",
        "S025 已补齐 E₀ inhabitance/inequality 与有限可判定性前提；S024 修正 C4 的 factorization 逆向与观察量词：",
    )

    state["revision"] = 25
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "MINIMAL_WITNESS_PRECONDITIONS_CORRECTED_FORMALIZATION_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "next_minimal_verification": "Formalize E0 with explicit a0:A and s0≠s1:S; separate finite decidable executable instance from the general proposition-level factorization theorem.",
    })
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260912-direction-009"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260912-outcome-009"
    for record_id in ("A-HOTT-SELF-VALIDATION-ECONOMY-001", "S-RES-20260912-022-SELF-VALIDATION-ECONOMY", "S-RES-20260912-024-FACTORIZATION-QUANTIFIER-CORRECTION"):
        record = state["records"][record_id]
        record["source_hashes"][C4] = NEW_HASH
        record["revalidation"] = "C4 was reread after S025 added the explicit a0:A, s0≠s1:S witness and separated finite decidable instances from general factorization propositions; historical checkpoint copies preserve earlier versions."
    state["records"]["A-HOTT-SELF-VALIDATION-ECONOMY-001"]["scope"] = "Distinguish finite checking from proof search and global self-truth; formulate ERCF with task-relative factorization, separating-observer assumptions, explicit E0 inhabitants/inequality witnesses, and distinct finite-decidable versus general proposition versions. Formalization and concrete divergence remain open."

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-RES-20260912-024-FACTORIZATION-QUANTIFIER-CORRECTION", "A-HOTT-SELF-VALIDATION-ECONOMY-001"],
        "full_sources": [session_path, audit_path, runs_path, C4, "audit/核心认知generation-4与自反理论经济研究实施证据-20260912.md", "scripts/audit/prepare_minimal_witness_preconditions_checkpoint.py"],
        "source_hashes": {C4: NEW_HASH},
        "mathematical_status": "PAPER_ONLY_PRECONDITIONS_CORRECTED_NOT_NATIVE_VERIFIED",
        "cognition_status": "E0_WITNESS_AND_FINITE_DECIDABILITY_PRECONDITIONS_CORRECTED",
        "scope": "Add the missing A inhabitant and S inequality witnesses to E0, and stop inferring factorization decidability from a finite task family alone; core cognition and ERCF direction remain unchanged.",
    }
    session = f"""# {SESSION_ID}

- 触发：C4 最终复读发现 E₀ 使用 `(a,s₀),(a,s₁)` 却未显式假设 `a:A`，并把有限任务族过快写成可判定。
- 修正：给出 `a₀:A` 与 `s₀≠s₁:S`；一般 factorization 保持 proposition-level，只有额外有限类型/可判定相等等结构时才宣称可执行判定。
- 影响：C4/source+merge manifest/STATE source hashes/恢复入口更新；core generation-4/36 KC 和 ERCF 主方向不变。
- 数学状态：`PAPER_ONLY`；proof assistant 未运行。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "old_c4_sha256": OLD_HASH, "new_c4_sha256": NEW_HASH,
        "correction": ["explicit a0:A", "explicit s0≠s1:S", "finite task family does not imply decidable factorization"],
        "post_checkpoint_required": ["36/36 audit", "C4/source/merge hash checks", "fresh receipt revision 25", "projection freshness", "full regression", "git diff --check"],
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
        "authorization": "The user requested a durable mathematical answer; adding missing witness and decidability preconditions is an in-scope correctness correction governed by the project checkpoint protocol.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 25, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
