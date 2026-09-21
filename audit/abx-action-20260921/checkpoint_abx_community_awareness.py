#!/usr/bin/env python3
"""Checkpoint the bounded ABX review of HoTT community awareness."""

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
SID = "S-ABX-20260921-ASTRA-COMMUNITY-AWARENESS"
BASE = ".codex/research/hott/sessions/" + SID + "/"
ABX_ID = "R-ABX-ACTION-20260921"
VERIFY = "audit/abx-action-20260921/verify_abx_community_awareness.py"
RECEIPT = "audit/abx-action-20260921/ABX-COMMUNITY-AWARENESS-VERIFICATION.json"
REPORT = "audit/abx-action-20260921/ABX-圆环挑战的HoTT社区认识范围审计-20260921.md"
SOURCES = (
    "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    VERIFY,
    RECEIPT,
    REPORT,
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/introduction.tex",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex",
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
    touched = {3, 5, 10, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 44, 45, 46}
    body = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: ABX_COMMUNITY_BOUNDARIES_SOURCE_REVIEWED_NO_CHANGE_TO_K_GATE
- panorama_change: BOOK_PUNCTURED_DISC_AND_COHESIVE_BOUNDARY_RECORDED_WITH_SCOPE
- essay_change: NO
- update_decision: 未来 ABX 水合必须读取社区认识范围审计；它否定“社区完全不知道相关边界”的强叙述，但不提供 K，也不宣判不存在非现实性理论元素
- cross_conflicts: 社区知道抽象层间边界、用户定义的R_origin/Done_strong合同、实际K、数学矛盾和哲学非现实性是不同命题；不得互相替代
- unresolved: 非现实性理论元素的独立判据、实际K、同一现实任务的失败、以及用户认可的更强R_origin；无其一不能交付HoTT缺陷结论

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in touched:
            relation = "DEEPENED" if number not in {15, 38, 39, 40} else "CORRECTED"
            judgement = "公开Book、社区讨论和cohesive HoTT文献显示相关边界已被识别；但未给出用户精确R_origin/Done_strong合同或实际K，故不构成击落也不构成不存在判词。"
            evidence = f"{REPORT}；{RECEIPT}；出现版本固定K、强R_origin合同或直接反例才改变范围。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只审计圆环挑战的社区认识范围与ABX水合入口。"
            evidence = "goal.md §2；不外推到该独立主题。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：现实对齐可将抽象的断裂作为候选来源，但“社区已有分层处理”既不证明抽象完全现实，也不证明它必然产生悖论。未来判断须回到具体任务、理论承诺和可反驳观察。

## 停止裁决

社区认识范围审计已完成。它不提供实际K，因此ABX继续默认停止；重开只接受外部版本固定K、用户认可的更强R_origin/操作合同，或直接推翻现有来源边界的证据。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    for rel in SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 216
    assert state["latest_session"] == "S-ABX-20260921-ASTRA-KNOWN-TRADEOFF"
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[ABX_ID])
    assert set(plan["review_required"]) <= {ABX_ID}
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "COMMUNITY-AWARENESS-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    receipt = json.loads((ROOT / RECEIPT).read_text())
    assert receipt["status"] == "PASS_WITH_SCOPE"

    prior_latest = state["latest_session"]
    state["revision"] = 217
    state["latest_session"] = SID
    record = state["records"][ABX_ID]
    record["evidence_status"] = (
        "INITIAL_ABX_BOUNDARY_ESTABLISHED_WITH_SCOPE / KNOWN_TECHNICAL_TRADEOFF_DISTINCTION_VERIFIED / "
        "COMMUNITY_BOUNDARIES_SOURCE_REVIEWED / NO_NEW_HOTT_DEFECT_CLAIM"
    )
    record["status"] = "initial_boundary_complete_community_awareness_scoped_no_defect_verdict"
    record["full_sources"] = list(dict.fromkeys(record["full_sources"] + list(SOURCES)))
    record["related_records"] = list(dict.fromkeys(record["related_records"] + [SID]))
    record["source_hashes"].update({rel: sha(ROOT / rel) for rel in SOURCES})
    record["revalidation"] = (
        "Revision217 recorded fixed Book passages, public HoTT discussion, and cohesive HoTT sources: visible authors and "
        "participants distinguish pure homotopy types from point-set/complement/ambient-isotopy tasks and make cohesion/shape explicit. "
        "The review found no exact R_origin/Done_strong contract or actual K, establishes no community-wide sociological verdict, "
        "and does not prove or disprove a non-reality element or HoTT defect."
    )
    record["scope"] = (
        "ABX now preserves a source-reviewed community-awareness boundary: known distinctions about topology, geometry, and homotopy "
        "do not substitute for K. Continuation still requires an independently specified reality predicate plus external K, or a more precise "
        "R_origin contract; the report rejects only the strong claim that the relevant boundary was wholly unknown."
    )
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_COMMUNITY_AWARENESS_SOURCE_REVIEWED_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE",
        current_phase="PHASE_2_ABX_INITIAL_BOUNDARY_COMPLETE",
        second_phase_status="ABX_INITIAL_BOUNDARY_COMPLETE_NO_AUTOMATIC_REPEAT_OF_KNOWN_TRADEOFFS",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        next_minimal_verification=(
            "STOP_BY_DEFAULT. Reopen only for a concrete version-pinned external K call chain, a user-specified stronger "
            "R_origin/operation contract, or direct evidence that invalidates the Book/B1a/LEM∞/community-boundary distinctions."
        ),
    )
    state["projection"]["status"] = "ABX_INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation for the ABX community-awareness source review
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: preserve Book/community/cohesive-HoTT awareness evidence without confusing it with an actual K or a defect verdict
- status: COMPLETED_WITH_SCOPE / NO_AUTOMATIC_ABX_CONTINUATION

The review found direct Book evidence that ordinary HoTT is purely homotopical rather than point-set topological, a punctured-disc example distinguishing fixed endpoints from a movable endpoint, a public HoTT discussion that routes complement/ambient-isotopy questions to cohesive HoTT, and cohesive literature that separates geometric/topological structure from a shape homotopy type. These sources refute the strong narrative that the community wholly missed the relevant boundary. They do not establish that the community stated the user's exact R_origin/Done_strong contract, that any consumer K makes an invalid promotion, or that a non-real element/HoTT defect exists or does not exist.

No new kernel theorem, external application audit, mathematical defect claim, message or Sub Agent occurred.
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{
            "kind": "community-awareness-local-anchor-verification",
            "command": f"python3 -B {VERIFY} --write",
            "result": "PASS_WITH_SCOPE; report anchors, modified ABX hydration entry, and pinned Book excerpts match",
            "mathematics": "NOT_A_KERNEL_RUN",
        }],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "Source-review and routing change only; no mathematical or sociological theorem.",
    }

    new_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21明确开启；已知取舍与社区认识范围审计 | `INITIAL_BOUNDARY / KNOWN_TRADEOFFS_AND_COMMUNITY_BOUNDARIES_NOT_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、D1/D2/D3、Book/B1a与社区/凝聚来源范围 | 默认停止；仅真实外部K、更强R_origin或直接证据失效可重开 | `ABX行动.md`；已知取舍与社区认识范围审计；revision217 receipt |"
    new_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环合同、三分母、已知技术取舍与社区认识范围 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320、D1/D2/D3、Book §11.2/logic、B1a、Book/社区/cohesive来源 | `INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE` | Book技术选项、B1a充分性、LEM∞拒绝、cubical研究和社区已知边界均不替代K | 不证明非现实、社区完全不知道或已解决精确合同、外部全库无K、HoTT缺陷或公开结论 | `ABX行动.md`；社区认识范围审计；revision217 receipt |"
    new_memory = "ABX 初始边界、已知技术取舍与社区认识范围审计均已完成。Book §11.2 的四种Ω/宇宙处理路线是公开技术选择；B1a只证SingleOmega到项目代理实数层的充分性，Necessity仍是conjecture；Book区分被拒的全类型LEM∞与可一致假定的hProp-LEM；Huber cubical论文证明指定演算的canonicity。Book、公开HoTT讨论和cohesive HoTT文献还表明，点集补空间／端点操作／几何结构与同伦型的差异已被明确认识和分层；这不等于用户的R_origin/Done_strong合同已被解决，也不构成ABX所需K。ABX默认停止；只在外部版本固定K、用户认可更强R_origin/操作合同或直接证据失效时重开。入口：`audit/abx-action-20260921/ABX-圆环挑战的HoTT社区认识范围审计-20260921.md`；revision217 checkpoint。"
    new_frontier = "- ABX 的社区认识范围已审计：Book、公开讨论与cohesive HoTT知道普通同伦型与补空间/几何过程的边界，但不提供R_origin/Done_strong的实际K；默认停止条件不变。"
    new_resume = "ABX初始边界、已知技术取舍和社区认识范围审计均已完成。Book/公开HoTT讨论/cohesive HoTT将普通同伦型与点集补空间、环境同痕和几何结构分层，故不能以“社区完全不知道”作为攻击前提；它们也没有给出用户精确R_origin/Done_strong合同或实际K。Book §11.2是宇宙管理选项而非非现实危机判词；B1a仅为充分性，必要性未证；LEM∞和hProp-LEM必须分开；Huber的cubical论文证明指定演算canonicity。ABX未找到K，默认停止。仅外部K、更强R_origin/操作合同或直接证据失效可重开。"
    memory_log = "\nS-ABX-20260921-ASTRA-COMMUNITY-AWARENESS：Book、公开HoTT讨论与cohesive HoTT的有界来源审计完成并进入ABX水合链。判词 `COMMUNITY_RELEVANT_BOUNDARIES_SOURCE_REVIEWED_NO_EXACT_ABX_CONTRACT_OR_K_FOUND`：社区已公开区分普通同伦型与点集补空间/端点操作/几何过程，cohesive HoTT显式区分几何结构和shape；未发现用户精确 `R_origin/Done_strong` 合同或实际K。该结果否定“社区完全不知道”但不证明非现实元素不存在，也不改变K门槛。验证器 PASS_WITH_SCOPE；revision217 checkpoint。\n"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 216", "source_state_revision: 217")
            body = replace_once(body, "projection_generation: 20260921-direction-216", "projection_generation: 20260921-direction-217")
            body = replace_once(body, "semantic_status: ABX_INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE", "semantic_status: ABX_INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 216", "source_state_revision: 217")
            body = replace_once(body, "projection_generation: 20260921-outcome-216", "projection_generation: 20260921-outcome-217")
            body = replace_once(body, "semantic_status: ABX_INITIAL_BOUNDARY_AND_KNOWN_TRADEOFF_AUDITED_WITH_SCOPE", "semantic_status: ABX_INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            body = replace_line(body, "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", new_direction)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            body = replace_line(body, "| `OUT-ABX-ACTION-INTAKE` |", new_panorama)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            body = replace_line(body, "ABX 初始边界及“已知技术取舍≠非现实性危机”审计已完成。", new_memory)
        elif rel == "MEMORY/003 - 当前验证状态与顺序日志.md":
            body += memory_log
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = replace_once(body, "- Book §11.2的Ω、resizing、hProp-LEM、σ-frame是已公开技术选项；B1a为充分性、Necessity为conjecture。把它们叫作非现实危机或共同体已承认缺陷没有当前证据。", "- Book §11.2的Ω、resizing、hProp-LEM、σ-frame是已公开技术选项；B1a为充分性、Necessity为conjecture。把它们叫作非现实危机或共同体已承认缺陷没有当前证据。\n" + new_frontier)
        elif rel == runtime.PREFIX + "RESUME.md":
            body = replace_once(body, "ABX初始边界和已知技术取舍审计均已完成。Book §11.2是宇宙管理选项而非非现实危机判词；B1a仅为充分性，必要性未证；LEM∞和hProp-LEM必须分开；Huber的cubical论文证明指定演算canonicity。ABX未找到K，默认停止。仅外部K、更强R_origin/操作合同或直接证据失效可重开。", new_resume)
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": body})

    for name, body in (
        ("SESSION.md", session),
        ("RUNS.json", runtime.dump(runs).decode()),
        ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"])),
    ):
        files.append({"path": BASE + name, "expected_sha256": None, "text": body})

    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID,
        "load_profile": "research", "task_ids": [ABX_ID],
        "authorization": "用户2026-09-21要求调查HoTT Book与公开网页中对圆环挑战相关边界的认识，并明确要求将调查结果落盘供未来AI水合；当前唯一工作AI获授权更新ABX证据边界和checkpoint。",
        "files": files,
    }
    (OUT / "COMMUNITY-AWARENESS-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    suffix = "COMMUNITY-AWARENESS-checkpoint-apply.json" if args.apply else "COMMUNITY-AWARENESS-checkpoint-dry-run.json"
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
