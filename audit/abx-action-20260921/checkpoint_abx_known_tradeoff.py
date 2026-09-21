#!/usr/bin/env python3
"""Checkpoint the ABX distinction between known technical tradeoffs and defects."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-ABX-20260921-ASTRA-KNOWN-TRADEOFF"
BASE = ".codex/research/hott/sessions/" + SID + "/"
ABX_ID = "R-ABX-ACTION-20260921"
VERIFY = "audit/abx-action-20260921/verify_abx_known_tradeoff.py"
RECEIPT = "audit/abx-action-20260921/ABX-KNOWN-TRADEOFF-VERIFICATION.json"
REPORT = "audit/abx-action-20260921/ABX-已知技术取舍与非现实性解释审计.md"
SOURCES = (
    "goal.md", "feature-list.md",
    "ABX行动/002 - GLM Flash G4的审计与可复用范围.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    VERIFY, RECEIPT, REPORT,
    "HoTT/formal/dedekind-omega-missile/CLAIM-PACKAGE-REAL-LAYER.md",
    "Astra继续尝试/ZCode-7cb会话成果吸收审查/003 - 语料检索、文献解释与证据治理.md",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/reals.tex",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/logic.tex",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/introduction.tex",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def replace_line(body: str, prefix: str, replacement: str) -> str:
    lines = body.splitlines()
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    lines[hits[0]] = replacement
    return "\n".join(lines) + "\n"


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == 46
    touched = {3, 5, 10, 14, 15, 19, 21, 22, 28, 29, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    body = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: ABX_KNOWN_TECHNICAL_TRADEOFF_DISTINCTION_RECORDED
- panorama_change: BOOK_OPTIONS_B1A_SCOPE_LEMINFTY_AND_CUBICAL_CANONICITY_SEPARATED
- essay_change: NO
- update_decision: 不把Book已知技术取舍、B1a充分性、被拒的LEM∞或cubical canonicity研究改写为“非现实危机已被共同体承认”
- cross_conflicts: 技术选择/形式限制、哲学非现实性、社区知情、实际未披露使用和内部缺陷是不同命题；GLM曾将它们混合
- unresolved: 现实对应的独立判据、外部实际K和更强R_origin；没有这些不能把ABX写成击落工程

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in touched:
            relation = "CORRECTED" if number in {15, 28, 29, 38, 43} else "DEEPENED"
            judgement = "Book 的技术选项和引擎的性质应按其精确数学范围理解；它们不自动证明或反驳非现实性哲学判断，也不替代实际K。"
            evidence = f"{REPORT}；{RECEIPT}；出现明确K、完整必要性证明或独立现实判据才可重开。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只纠正ABX与已知技术取舍的证据层级。"
            evidence = "goal.md §2；不外推到该独立主题。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：现实对齐是一项需要独立判据的解释工作。Book 的公开取舍可作为研究材料，但公开、知情、选择或实现优化本身均不足以等同于“非现实性悖论”。

## 停止裁决

ABX 不因重复已知技术取舍而继续。当前只接受三个重开入口：外部版本固定的K、用户认可的更强R_origin/操作合同、或直接推翻D_ABX_1–3/本审计范围的证据。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", VERIFY], cwd=ROOT)
    for rel in SOURCES:
        assert (ROOT / rel).is_file(), rel
    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 215
    assert state["latest_session"] == "S-ABX-20260921-ASTRA-D3-BOOK-CORE"
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[ABX_ID])
    assert set(plan["review_required"]) <= {ABX_ID}
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "KNOWN-TRADEOFF-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    receipt = json.loads((ROOT / RECEIPT).read_text())
    assert receipt["status"] == "PASS_WITH_SCOPE"

    prior_latest = state["latest_session"]
    state["revision"] = 216
    state["latest_session"] = SID
    record = state["records"][ABX_ID]
    record["evidence_status"] = "INITIAL_ABX_BOUNDARY_ESTABLISHED_WITH_SCOPE / KNOWN_TECHNICAL_TRADEOFF_DISTINCTION_VERIFIED / NO_NEW_HOTT_DEFECT_CLAIM"
    record["status"] = "initial_boundary_complete_known_tradeoff_not_a_defect_verdict"
    record["full_sources"] = list(dict.fromkeys(record["full_sources"] + list(SOURCES)))
    record["related_records"] = list(dict.fromkeys(record["related_records"] + [SID]))
    record["source_hashes"].update({rel: sha(ROOT / rel) for rel in SOURCES})
    record["revalidation"] = (
        "Revision216 distinguished Book §11.2's explicit universe-management options from philosophical non-reality claims, "
        "separated LEM∞ from hProp-LEM, and rechecked that B1a is sufficient while Necessity remains conjectural. "
        "It also records the source scope of Huber/cubical canonicity. No actual K, defect, inconsistency or community-wide "
        "knowledge verdict follows."
    )
    record["scope"] = (
        "ABX's initial boundary now includes the distinction between known technical tradeoffs and an alleged non-reality crisis. "
        "A future continuation needs an independently specified reality predicate plus external K, or a more precise R_origin contract; "
        "Book awareness and B1a sufficiency alone are not such evidence."
    )
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_KNOWN_TRADEOFF_AUDIT_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE",
        current_phase="PHASE_2_ABX_INITIAL_BOUNDARY_COMPLETE",
        second_phase_status="ABX_INITIAL_BOUNDARY_COMPLETE_NO_AUTOMATIC_REPEAT_OF_KNOWN_TRADEOFFS",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        next_minimal_verification=(
            "STOP_BY_DEFAULT. Reopen only for a concrete version-pinned external K call chain, a user-specified stronger R_origin/operation contract, "
            "or direct evidence that invalidates the Book/B1a/LEM∞/D_ABX source distinctions."
        ),
    )
    state["projection"]["status"] = "ABX_INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation after known-technical-tradeoff audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: distinguish Book/cubical technical knowledge from a non-reality or defect verdict
- status: COMPLETED_WITH_SCOPE / NO_AUTOMATIC_ABX_CONTINUATION

Book §11.2 openly presents alternative universe-management routes for Dedekind reals. It does not label them non-real or establish a community misuse. The current B1a proof is a conditional sufficient construction; Necessity is conjectural. The Book distinguishes rejected all-types LEM∞ from hProp-LEM that may consistently be assumed. Huber's cubical canonicity paper proves canonicity for a specified calculus, not a general confession that univalence destroys it.

This unit corrects GLM's over-strong interpretation. ABX remains meaningful only as an independently specified task/usage audit; it is not justified as a repetition of known Book tradeoffs. No new kernel theorem, external application audit, mathematical defect claim, message or Sub Agent occurred.
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{"kind": "book-and-local-scope-verification", "command": f"python3 -B {VERIFY}", "result": "PASS_WITH_SCOPE; three Book files and two local scope owners match anchors/hashes", "mathematics": "NOT_A_KERNEL_RUN"}],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "Source-scope distinction only; no mathematical or philosophical theorem.",
    }

    old_direction_prefix = "| `DIR-U-ABX-ORIGINAL-CIRCLE` |"
    new_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21明确开启；已知取舍审计 | `INITIAL_BOUNDARY / KNOWN_TRADEOFFS_NOT_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、D1/D2/D3与Book/B1a范围 | 默认停止；仅真实外部K、更强R_origin或直接证据失效可重开 | `ABX行动.md`；已知取舍审计；revision216 receipt |"
    old_panorama_prefix = "| `OUT-ABX-ACTION-INTAKE` |"
    new_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环合同、三分母与已知技术取舍边界 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320、D1/D2/D3、Book §11.2/logic、B1a范围 | `INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE` | Book技术选项、B1a充分性、LEM∞拒绝和cubical研究均不替代K | 不证明非现实、社区未披露、外部全库无K、HoTT缺陷或公开结论 | `ABX行动.md`；已知取舍审计；revision216 receipt |"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 215", "source_state_revision: 216")
            body = replace_once(body, "projection_generation: 20260921-direction-215", "projection_generation: 20260921-direction-216")
            body = replace_once(body, "semantic_status: ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / D_ABX_1_D_ABX_2_D_ABX_3_NO_K", "semantic_status: ABX_INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 215", "source_state_revision: 216")
            body = replace_once(body, "projection_generation: 20260921-outcome-215", "projection_generation: 20260921-outcome-216")
            body = replace_once(body, "semantic_status: ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / D_ABX_1_D_ABX_2_D_ABX_3_NO_K", "semantic_status: ABX_INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            body = replace_line(body, old_direction_prefix, new_direction)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            body = replace_line(body, old_panorama_prefix, new_panorama)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            body = replace_line(body, "ABX 初始边界已完成。", "ABX 初始边界及“已知技术取舍≠非现实性危机”审计已完成。Book §11.2 的四种Ω/宇宙处理路线是公开技术选择；B1a只证SingleOmega到项目代理实数层的充分性，Necessity仍是conjecture；Book区分被拒的全类型LEM∞与可一致假定的hProp-LEM；Huber cubical论文证明指定演算的canonicity。这些都不等于社区承认非现实危机，也不构成ABX所需K。ABX默认停止；只在外部版本固定K、用户认可更强R_origin/操作合同或直接证据失效时重开。入口：`audit/abx-action-20260921/ABX-已知技术取舍与非现实性解释审计.md`；revision216 checkpoint。")
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = """# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 第一阶段四弹 redo 保持 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`；ABX 不追溯改写它。
- ABX初始合同及D1/D2/D3均未出现K；Book的空间解释是纯同伦理解，不能代替点集来源/复原任务。
- Book §11.2的Ω、resizing、hProp-LEM、σ-frame是已公开技术选项；B1a为充分性、Necessity为conjecture。把它们叫作非现实危机或共同体已承认缺陷没有当前证据。
- 默认停止自动扩展。只有外部版本固定K、用户认可的更强R_origin/操作合同，或直接证据失效能重开ABX。
"""
        elif rel == runtime.PREFIX + "RESUME.md":
            pattern = r"## 当前阶段（2026-09-21）\n\n.*?\n\n## 历史停止点"
            replacement = "## 当前阶段（2026-09-21）\n\nABX初始边界和已知技术取舍审计均已完成。Book §11.2是宇宙管理选项而非非现实危机判词；B1a仅为充分性，必要性未证；LEM∞和hProp-LEM必须分开；Huber的cubical论文证明指定演算canonicity。ABX未找到K，默认停止。仅外部K、更强R_origin/操作合同或直接证据失效可重开。\n\n## 历史停止点"
            body, count = re.subn(pattern, replacement, body, count=1, flags=re.S)
            assert count == 1
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": body})

    for name, body in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode()), ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"]))):
        files.append({"path": BASE + name, "expected_sha256": None, "text": body})
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [ABX_ID],
        "authorization": "用户2026-09-21要求审计ABX与GLM对Book、cubical和非现实性问题的关系；当前唯一工作AI获授权更新ABX证据边界和checkpoint。", "files": files,
    }
    (OUT / "KNOWN-TRADEOFF-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("KNOWN-TRADEOFF-checkpoint-apply.json" if args.apply else "KNOWN-TRADEOFF-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
