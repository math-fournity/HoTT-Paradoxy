#!/usr/bin/env python3
"""Checkpoint the completed H/R/K historical-readiness audit for ABX."""

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
SID = "S-ABX-20260921-ASTRA-HRK-READINESS"
BASE = ".codex/research/hott/sessions/" + SID + "/"
ABX_ID = "R-ABX-ACTION-20260921"
DIALOGUE = "audit/abx-action-20260921/build_hru_readiness_dialogue.py"
VERIFY = "audit/abx-action-20260921/verify_hru_k_readiness.py"
RECEIPT = "audit/abx-action-20260921/HRK-READINESS-VERIFICATION.json"
INDEX = "audit/abx-action-20260921/H-R-K查找思路整备.md"
SHARDS = tuple(
    "audit/abx-action-20260921/H-R-K查找思路整备/" + name
    for name in (
        "001 - 本轮完整问答与分类结论.md",
        "002 - 证据分母、时间线与代码运行资产.md",
        "003 - H、R、U 与操作合同覆盖矩阵.md",
        "004 - K、消费者与社区边界审计.md",
        "005 - 未覆盖义务、禁止重复与重新出发条件.md",
    )
)
SOURCES = (
    "ABX行动.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    INDEX,
    *SHARDS,
    DIALOGUE,
    VERIFY,
    RECEIPT,
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
    deepened = {3, 5, 10, 14, 19, 21, 22, 31, 34, 35, 37, 41, 42, 43, 44, 45, 46}
    corrected = {15, 38, 39, 40}
    body = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: ABX_HRK_READINESS_REGISTERED_WITH_NO_REPEAT_CONSTRAINTS
- panorama_change: H_R_U_OPERATION_AND_K_COVERAGE_REGISTERED_WITH_SCOPE
- essay_change: NO
- update_decision: 未来 ABX 先读取 H/R/K 整备档案和禁止重复清单；只有新 K、更强 R 或旧证据失效才开始新单元
- cross_conflicts: 裸同胚 H、富化关系 R、忘却 U、操作合同、实际消费者 K、对象层矛盾和哲学非现实性均为不同命题；不得互相替代
- unresolved: 完整 OriginTop/R、实际 operation-spec、真实版本固定 K、同任务失配，以及独立非现实性判据；无其一不能交付 HoTT 缺陷结论

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in corrected:
            relation = "CORRECTED"
            judgement = "本轮把第一弹后的历史资产重新归类为 H/R/U/操作/K 的受限证据，撤回把控制或无命中直接写成 HoTT 缺陷的捷径。"
            evidence = f"{INDEX}；{RECEIPT}；出现实际 K 或完整 R 的直接证据才改变范围。"
        elif number in deepened:
            relation = "DEEPENED"
            judgement = "H/R/K 整备把现实同一性、富化信息、操作合同和消费者责任分层，并记录既有正反控制与禁止重复边界。"
            evidence = f"{INDEX}；{RECEIPT}；新版本固定 K、强 R 或旧证据失效才重开。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只完成第一弹相关 H/R/K 的历史整备，不重裁该条独立用户原文。"
            evidence = "goal.md §2；不外推到该独立主题。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：现实对齐可以提出来源—操作—复原敏感的对象，但不能把 H 与 R 混作同一命题。既有原生与经典控制分别给出裸同胚、富化字段、正反操作合同和限定恢复；实际 K 仍未出现。

## 停止裁决

H/R/K 历史整备已完成。它不提供实际 K 或完整 OriginTop，因此 ABX 默认停止；重开只接受外部版本固定 K、用户认可的更强 R/操作合同、明确的新对象理论目标，或直接推翻现有来源、代码、run 或解释边界的证据。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", DIALOGUE, "--check"], cwd=ROOT)
    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    for rel in SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 217
    assert state["latest_session"] == "S-ABX-20260921-ASTRA-COMMUNITY-AWARENESS"
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[ABX_ID])
    assert set(plan["review_required"]) <= {ABX_ID}
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "HRK-READINESS-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    receipt = json.loads((ROOT / RECEIPT).read_text())
    assert receipt["status"] == "PASS_WITH_SCOPE"

    prior_latest = state["latest_session"]
    state["revision"] = 218
    state["latest_session"] = SID
    record = state["records"][ABX_ID]
    record["evidence_status"] = (
        "INITIAL_ABX_BOUNDARY_ESTABLISHED_WITH_SCOPE / HRK_READINESS_COVERAGE_REGISTERED / "
        "KNOWN_TECHNICAL_TRADEOFF_DISTINCTION_VERIFIED / COMMUNITY_BOUNDARIES_SOURCE_REVIEWED / "
        "NO_NEW_HOTT_DEFECT_CLAIM"
    )
    record["status"] = "initial_boundary_hrk_readiness_registered_scoped_no_defect_verdict"
    record["full_sources"] = list(dict.fromkeys(record["full_sources"] + list(SOURCES)))
    record["related_records"] = list(dict.fromkeys(record["related_records"] + [SID]))
    record["source_hashes"].update({rel: sha(ROOT / rel) for rel in SOURCES})
    record["revalidation"] = (
        "Revision218 registers a verbatim user/AI H/R dialogue projection, a file/run inventory, and an audit map from the "
        "first breakpoint report through C-324, Flash, original-four-stage corrigendum, D1/D2/D3 and community sources. "
        "It confirms existing H/R/U and operation-contract controls, preserves their explicit limitations, and finds no actual K. "
        "It does not establish a new topology, semantic completeness of all history, a non-reality predicate, or a HoTT defect."
    )
    record["scope"] = (
        "ABX now has an H/R/K readiness map: H is a bare-space relation, R is a currently limited origin/operation/restoration "
        "proxy, U is explicit forgetting, and K must be a version-pinned real consumer that promotes the weak result to the "
        "same strong task. Existing source/run controls and bounded no-hit denominators must not be repeated as new research."
    )
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_HRK_HISTORICAL_READINESS_AUDITED_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_HRK_READINESS_REGISTERED_STOP_BY_DEFAULT",
        current_phase="PHASE_2_ABX_HRK_READINESS_COMPLETE",
        second_phase_status="ABX_HRK_READINESS_COMPLETE_NO_REPEAT_WITHOUT_NEW_EVIDENCE",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        next_minimal_verification=(
            "STOP_BY_DEFAULT. First read audit/abx-action-20260921/H-R-K查找思路整备.md. Reopen only for a "
            "concrete version-pinned external K call chain, a user-specified stronger R_origin/operation contract, "
            "an explicit independent OriginTop objective, or direct evidence that invalidates the indexed source/run boundary."
        ),
    )
    state["projection"]["status"] = "ABX_HRK_READINESS_REGISTERED_WITH_SCOPE / NO_ACTUAL_K / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation for the ABX H/R/K historical-readiness audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: preserve the complete H/R question-answer record and a non-duplicative map of first-missile-era source, code, run, operation and K evidence
- status: COMPLETED_WITH_SCOPE / STOP_BY_DEFAULT_UNTIL_NEW_EVIDENCE

The readiness audit copies the visible user question and answer verbatim, inventories the first-missile-era document/code/run families, and maps their actual conclusions to H (bare topology), R (a limited origin/operation/restoration proxy), U (forgetting) and K (a real consumer). It confirms that the project already has strong bounded controls for the first four axes but no version-pinned consumer that promotes H or U to the same Done_strong task. It neither establishes a new topology nor a HoTT defect.

No new kernel theorem, external application audit, mathematical defect claim, message or Sub Agent occurred. The only executions are projection/receipt/inventory and governance validation; pre-existing proof receipts are indexed but not rerun.
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{
            "kind": "hrk-dialogue-projection-and-history-inventory-verification",
            "command": f"python3 -B {DIALOGUE} --check && python3 -B {VERIFY} --write",
            "result": "PASS_WITH_SCOPE; verbatim projection, declared source/code anchors, fixed Git-history counts and file/run inventory match",
            "mathematics": "NOT_A_KERNEL_RUN",
        }],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "Historical evidence mapping and routing change only; no new mathematical, sociological, or HoTT-defect theorem.",
    }

    new_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的 H/R/K 查找整备 | 用户 2026-09-21要求完整保存问答并审计第一弹后的全部相关工作 | `INITIAL_BOUNDARY / HRK_READINESS_REGISTERED / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C250–324、Flash、第一阶段redo、D1/D2/D3、Book/社区来源 | 默认停止；先读整备档案。仅真实外部K、更强R/操作合同、独立对象理论目标或直接证据失效可重开 | `ABX行动.md`；H/R/K整备；revision218 receipt |"
    new_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环 H/R/K 历史覆盖与重新出发边界 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、第一阶段redo、D1/D2/D3、Book/社区来源 | `H_R_K_READINESS_AUDITED_WITH_SCOPE / NO_ACTUAL_K` | H、R、U与三种操作合同已有控制；有界K分母无命中；社区边界不替代K | 不证明新拓扑、所有历史的语义完整性、外部全库无K、非现实、HoTT缺陷或公开结论 | `ABX行动.md`；H/R/K整备；revision218 receipt |"
    new_memory = "ABX 的 H/R/K 历史整备完成：本轮完整问答已逐字投影；第一弹专题 308 个追踪文件、C250–324 的 68 份关联运行收据、Flash、Lean/原生 Agda 控制、第一阶段 redo 和 D1/D2/D3 均有索引。已知：H 是裸空间关系，R 仍是受限来源—操作—复原代理，U 是忘却，既有 `RichCurve`/`SourceContract`/`TaskIntegration` 已证明若干边界；未找到将 H/U 当同一 `Done_strong` 任务的真实版本固定 K。默认停止，未来先读 `audit/abx-action-20260921/H-R-K查找思路整备.md`；只在外部 K、更强 R/操作合同、独立对象理论目标或直接证据失效时重开。revision218 checkpoint。"
    new_frontier = "- ABX H/R/K 历史整备已完成：前四轴已有有界控制和禁止重复清单，但没有实际 K；下一步只能基于新版本固定消费者、更强 R/operation-spec、独立对象理论目标或直接证据失效。入口：`audit/abx-action-20260921/H-R-K查找思路整备.md`。"
    new_resume = "ABX H/R/K 历史整备已完成：完整本轮问答、308 个断点专题追踪文件、C250–324 的 68 份关联 run、Flash、Lean/原生 Agda控制、第一阶段 redo 和 D1/D2/D3 均已建立索引。H 是裸空间关系；R 仍只是受限来源—操作—复原代理；U 是忘却；现有 SourceContract/TaskIntegration 显式保住字段和操作差异。未找到实际版本固定 K 将 H/U 升格为同一 Done_strong 任务。默认停止：未来先读 `audit/abx-action-20260921/H-R-K查找思路整备.md`；仅外部K、更强R/操作合同、独立对象理论目标或直接证据失效可重开。"
    memory_log = "\nS-ABX-20260921-ASTRA-HRK-READINESS：完整 H/R 问答逐字投影、第一弹以后文档/代码/run/消费者来源的有界历史审计与无重复清单已写入 `audit/abx-action-20260921/H-R-K查找思路整备.md`。基线：断点专题308追踪文件；C250–324关联RUN.json为68（52接受、16预期拒绝）。判词 `HRK_PREPARATION_COVERAGE_REGISTERED_NO_REPEAT_WITHOUT_NEW_EVIDENCE`：H/R/U和操作合同已有控制，但没有版本固定的实际K；不证明新拓扑或HoTT缺陷。验证器 PASS_WITH_SCOPE；revision218 checkpoint。\n"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 217", "source_state_revision: 218")
            body = replace_once(body, "projection_generation: 20260921-direction-217", "projection_generation: 20260921-direction-218")
            body = replace_once(body, "semantic_status: ABX_INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE", "semantic_status: ABX_HRK_READINESS_REGISTERED_WITH_SCOPE")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 217", "source_state_revision: 218")
            body = replace_once(body, "projection_generation: 20260921-outcome-217", "projection_generation: 20260921-outcome-218")
            body = replace_once(body, "semantic_status: ABX_INITIAL_BOUNDARY_KNOWN_TRADEOFF_AND_COMMUNITY_SCOPE_AUDITED_WITH_SCOPE", "semantic_status: ABX_HRK_READINESS_REGISTERED_WITH_SCOPE")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            body = replace_line(body, "| `DIR-U-ABX-ORIGINAL-CIRCLE` |", new_direction)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            body = replace_line(body, "| `OUT-ABX-ACTION-INTAKE` |", new_panorama)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            body = replace_line(body, "ABX 初始边界、已知技术取舍与社区认识范围审计均已完成。", new_memory)
        elif rel == "MEMORY/003 - 当前验证状态与顺序日志.md":
            body += memory_log
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = replace_once(body, "- ABX 的社区认识范围已审计：Book、公开讨论与cohesive HoTT知道普通同伦型与补空间/几何过程的边界，但不提供R_origin/Done_strong的实际K；默认停止条件不变。", new_frontier)
        elif rel == runtime.PREFIX + "RESUME.md":
            body = replace_once(body, "ABX初始边界、已知技术取舍和社区认识范围审计均已完成。Book/公开HoTT讨论/cohesive HoTT将普通同伦型与点集补空间、环境同痕和几何结构分层，故不能以“社区完全不知道”作为攻击前提；它们也没有给出用户精确R_origin/Done_strong合同或实际K。Book §11.2是宇宙管理选项而非非现实危机判词；B1a仅为充分性，必要性未证；LEM∞和hProp-LEM必须分开；Huber的cubical论文证明指定演算canonicity。ABX未找到K，默认停止。仅外部K、更强R_origin/操作合同或直接证据失效可重开。", new_resume)
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
        "authorization": "用户2026-09-21要求完整保存其关于第一弹、新拓扑学与HoTT查找思路的提问和AI回答，并彻底审计第一弹后相关文档、代码、运行和消费者搜索的广度/深度，使未来AI避免重复劳动；当前唯一工作AI获授权更新ABX证据边界和checkpoint。",
        "files": files,
    }
    (OUT / "HRK-READINESS-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    suffix = "HRK-READINESS-checkpoint-apply.json" if args.apply else "HRK-READINESS-checkpoint-dry-run.json"
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
