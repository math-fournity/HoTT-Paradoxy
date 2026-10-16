#!/usr/bin/env python3
"""Apply the bounded original-X task-fidelity correction checkpoint.

This is a state/projection checkpoint only.  It records a source audit and a
negative result within that fixed source set; it does not execute a proof
assistant or create a mathematical claim.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-COR-20260921-ASTRA-ORIGINAL-X-TASK-FIDELITY"
BASE = ".codex/research/hott/sessions/" + SID + "/"
PLAN_COMMIT = "7c71b9ba7f1c0110d7eec2857c25b5465acf28d1"
RESULT_ID = "R-ASTRA-ASSUMPTION-INTEGRATION-20260921"
CORRECTION_ID = "R-ASTRA-TASK-FIDELITY-CORRIGENDUM-20260921"
REPORT = "Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md"
REPORT_SHARD = "Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告/007 - 原X、数学现实同一性与第三弹校正.md"
AUDIT = "audit/astra-task-fidelity-corrigendum-20260921/H-COMMITMENT-AUDIT.md"
MANIFEST = "audit/astra-task-fidelity-corrigendum-20260921/SOURCE-MANIFEST.json"
VERIFY = "audit/astra-task-fidelity-corrigendum-20260921/VERIFICATION.json"
DIALOGUE = "Astra继续尝试/断点与证明机制系统检查/对话原文.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(argv: list[str]) -> str:
    return subprocess.check_output(argv, cwd=ROOT, text=True).strip()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == 46
    directly_touched = {3, 5, 10, 12, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    body = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: FOUR_STAGE_REDO_PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM
- panorama_change: ORIGINAL_TARGET_NOT_ESTABLISHED_WITH_ORIGINAL_X_AND_H_SCOPE_CORRECTED
- essay_change: NO
- update_decision: 原 X／数学现实同一性勘误完成；固定来源未发现实际 H，第一阶段重新关闭
- cross_conflicts: 旧 `√2` M3 解释与原圆环过程的混同已由策略/第三十五轮第007片分开；未将语义 R 偷换为 C 或 H
- unresolved: 新的实际 H、精确反例、来源失效或用户明确第二阶段指令才可重开

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in directly_touched:
            relation = "CORRECTED" if number in {3, 15, 19, 38, 43} else "DEEPENED"
            judgement = "将共同数学现实过程保留为显式语义锚，但不把共同指称加强为任务合同或理论承诺；固定来源审计未发现 H。"
            evidence = f"{AUDIT}；{REPORT_SHARD}；发现实际 H、来源失效或用户开启第二阶段才可重开。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元不扩张到该独立候选；只完成原四弹范围判词的任务忠实性校正。"
            evidence = "goal.md §1.1；无新的合格判词改变凭据前保持停止。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：现实对齐仍是研究方向，不能把 R 的语义地位当作理论内部同一性。此次勘误避免了将算术校准误称为原过程；没有新增 HoTT 缺陷或物理完成的结论。

## 停止裁决

`R-ASTRA-TASK-FIDELITY-CORRIGENDUM-20260921` 已完成固定来源审计，结果为 `NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`。它支持重述第一阶段的范围判词，不支持全局不存在结论；第二阶段仍未开启。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    assert command(["git", "rev-parse", "HEAD"]) == PLAN_COMMIT
    for rel in (REPORT, REPORT_SHARD, AUDIT, MANIFEST, VERIFY, DIALOGUE):
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)

    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 210
    assert state["latest_session"] == "S-COM-20260921-ASTRA-FOUR-STAGE-REDO-COMPLETE"
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[RESULT_ID])
    assert not plan["review_required"]
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    prior_latest = state["latest_session"]
    state["revision"] = 211
    state["latest_session"] = SID
    state["active"] = [item for item in state["active"] if item in {"I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"}]

    result = state["records"][RESULT_ID]
    result["evidence_status"] = "PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM / SOURCE_CONTRACT_AUDITED_NOT_COQ_REPLAY"
    result["status"] = "original_four_stage_redo_reclosed_with_scope_target_not_established"
    result["scope"] = (
        "The original arguments, geometry/arithmetic controls and fixed natural-consumer source were reconciled. "
        "The original circle process was then distinguished from the sqrt2 calibration. In the fixed correction "
        "source set no actual HoTT rule, theorem, library interface or consumer H was found that treats static A "
        "as completion of process B. The original whole target remains not established; exact local results remain. "
        "This is not a global HoTT safety theorem, global absence theorem, Coq replay, physical realization result, or phase-two proof."
    )
    result["full_sources"] = list(dict.fromkeys(result["full_sources"] + [REPORT_SHARD, AUDIT, MANIFEST, VERIFY, DIALOGUE]))
    result["related_records"] = list(dict.fromkeys(result["related_records"] + [CORRECTION_ID, SID]))
    result["source_hashes"].update(
        {
            REPORT_SHARD: sha(ROOT / REPORT_SHARD),
            AUDIT: sha(ROOT / AUDIT),
            MANIFEST: sha(ROOT / MANIFEST),
            VERIFY: sha(ROOT / VERIFY),
        }
    )
    result["revalidation"] = (
        "Revision211 task-fidelity corrigendum reread the original process proposals and fixed sources. "
        "The correction adds a bounded H audit, distinguishes RealitySame from C/H, and does not alter prior mathematical scopes."
    )

    state["records"][CORRECTION_ID] = {
        "kind": "result",
        "path": AUDIT,
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "FIXED_SOURCE_AUDIT_NO_H_WITH_SCOPE",
        "status": "complete_with_scope_no_actual_h_commitment",
        "depends_on": [],
        "related_records": [RESULT_ID, SID],
        "full_sources": [AUDIT, MANIFEST, VERIFY, REPORT_SHARD, DIALOGUE],
        "scope": (
            "Bounded audit of the original punctured-circle closure/restoration task. It found no actual H commitment "
            "in the ten fixed sources. This is not exhaustive over HoTT or its consumers, and makes no mathematical absence theorem."
        ),
        "source_hashes": {rel: sha(ROOT / rel) for rel in (AUDIT, MANIFEST, VERIFY, REPORT_SHARD)},
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "TASK_FIDELITY_CORRIGENDUM_COMPLETION_AUDIT_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [RESULT_ID, CORRECTION_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="FOUR_STAGE_REDO_PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM",
        current_phase="PHASE_1_COMPLETE_WITH_SCOPE",
        second_phase_status="NOT_OPENED",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        phase_1_result_record=RESULT_ID,
        next_minimal_verification=(
            "NONE_BY_DEFAULT. Reopen only if a concrete actual H commitment for the fixed original-X task, a source/run invalidation, "
            "a counterexample to the fixed audit, an unmet fixed six-obligation question, or explicit user authorization appears."
        ),
    )

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation after a bounded source audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: 原 X／数学现实同一性／第三弹任务忠实性勘误
- plan_commit: {PLAN_COMMIT}
- status: COMPLETED_WITH_SCOPE / PHASE_1_RECLOSED / SECOND_PHASE_NOT_OPENED

用户澄清原 A、B、X 所观察的是圆去点、开区间呈现与两端闭合/复原过程，`√2` 的 `Spec_A`／`Spec_B` 只是校准。于是本单元把 `RealitySame(A,B,X)`、任务合同 C 和理论侧实际承诺 H 分开。R 可作为语义/规格前提，不能自己推出 C 或 H。

本轮固定十个来源并保留 hash/锚点。项目的 `NativeSourceContract` 实际使用 univalence/同胚运输，却要求闭图 `Denotes` 并否定裸 `N`；`NativeTaskIntegration` 显式把同一对象对放在不同操作合同中；`Sqrt2TaskComparison` 分开 Request/Output/Done；S¹ loop consumer与固定 Coq locator也不提供原闭合任务的 H。结果是 `NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`，不是全局不存在或 HoTT 内部安全定理。

不新增数学命题、证明源码、内核运行或外部网络来源。未重跑未变内核输入。第一阶段以修正理由重新关闭；第二阶段未开启。无 Sub Agent、push、tag、公开或外部消息。
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {
                "kind": "bounded-source-audit",
                "command": "python3 -B audit/astra-task-fidelity-corrigendum-20260921/verify_h_commitment_scope.py",
                "result": "PASS; 10 source identities/anchors and zero target vocabulary matches in 3 fixed locator files",
                "mathematics": "NOT_A_KERNEL_RUN",
            },
            {
                "kind": "visible-dialogue-archive",
                "command": "python3 -B Astra继续尝试/断点与证明机制系统检查/tools/append_reality_identity_corrigendum.py --verify",
                "result": "PASS; 13 increment messages and 57 cumulative messages exact against canonical reader",
                "mathematics": "NOT_A_KERNEL_RUN",
            },
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "existing_evidence": [AUDIT, MANIFEST, VERIFY, REPORT_SHARD],
        "scope": "Task-fidelity source audit and state reconciliation only; no mathematical re-execution.",
    }

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 210", "source_state_revision: 211")
            body = replace_once(body, "projection_generation: 20260921-direction-210", "projection_generation: 20260921-direction-211")
            body = replace_once(body, "semantic_status: FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE", "semantic_status: FOUR_STAGE_REDO_PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 210", "source_state_revision: 211")
            body = replace_once(body, "projection_generation: 20260921-outcome-210", "projection_generation: 20260921-outcome-211")
            body = replace_once(body, "semantic_status: FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE", "semantic_status: FOUR_STAGE_REDO_PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            lines = body.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("| `DIR-U-ASTRA-BREAKPOINT` |"):
                    lines[i] = "| `DIR-U-ASTRA-BREAKPOINT` | 原四弹 redo：原X/任务忠实性勘误后的范围判词 | 用户两阶段 goal；`goal.md` §1.1 | `CLOSED_WITH_SCOPE / PHASE_1_RECLOSED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-ASSUMPTION-INTEGRATION-35`、`R-ASTRA-TASK-FIDELITY-CORRIGENDUM-20260921`及C250–324 | 原整体击落论证未建立；固定来源未找到实际H；第二阶段未开启 | `goal.md`；第三十五轮第007片；H审计；revision211 receipt |"
            body = "\n".join(lines) + "\n"
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            lines = body.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("| `OUT-ASTRA-ASSUMPTION-INTEGRATION-35` |"):
                    lines[i] = "| `OUT-ASTRA-ASSUMPTION-INTEGRATION-35` | 原四弹 redo 的修正范围判词 | `DIR-U-ASTRA-BREAKPOINT` | 六原文/五方案、C250–324、9包18资格、14固定Coq源、原X/H十源审计 | `PHASE_1_RECLOSED_WITH_SCOPE / ORIGINAL_TARGET_NOT_ESTABLISHED / NO_H_IN_FIXED_SCOPE` | 原圆环X、R/C/H与√2校准分开；精确局部结果保留 | 不证明全HoTT无问题、全局不存在H、物理实现、Coq全库有效或已击落；第二阶段未开启 | `goal.md`；第三十五轮第007片；H审计；revision211 receipt |"
            body = "\n".join(lines) + "\n"
        elif rel == "MEMORY/001 - 当前执行队列.md":
            old = "用户当前 `/goal` 是两阶段的四弹一体 redo。第一阶段已经完成：第三十五轮逐层对账、九包十八资格项、固定 Coq 源码合同和 revision209 收据支持范围判词 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / ASSUMPTIONS_AND_TASKS_RECONCILED_WITH_SCOPE`。原整体击落结论未建立，精确局部证明保留。第二阶段未开启；旧机器统观、PREMISE-001、R4、一般反向、独立性、更多消费者与新版包不再自动排队。只在用户明确开启或新事实满足 `goal.md` 的判词改变凭据时重开。当前 checkpoint revision210 将该完成状态写入 STATE；feature-list.md 有另一写者的 dirty 修改，本单元未覆盖。入口：`goal.md`、`Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md`。"
            new = "用户当前 `/goal` 的两阶段四弹 redo 第一阶段已在原X/任务忠实性勘误后重新关闭。原主过程是圆去点、开区间呈现与两端闭合/复原；`RealitySame` 可作语义锚，却不等于任务合同 C 或实际 HoTT 承诺 H。固定十源审计未找到 H；原 `√2` M3 只保留为校准。当前判词仍为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，精确局部证明保留。第二阶段未开启；旧机器统观、PREMISE-001、R4、一般反向、独立性、更多消费者与新版包不再自动排队。只在用户明确开启或出现具体 H、反例、来源/运行失效等合格凭据时重开。revision211 checkpoint 写入此状态。入口：`goal.md`、第三十五轮第007片、`audit/astra-task-fidelity-corrigendum-20260921/H-COMMITMENT-AUDIT.md`。"
            body = replace_once(body, old, new)
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = """# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 四弹一体原方案 redo 第一阶段已在原 X／数学现实同一性勘误后重新关闭：`ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`；精确局部结果、原始运行、固定源码和边界保留。
- `RealitySame(A,B,X)` 作为语义锚不推出同任务 C 或实际理论承诺 H。固定来源中最接近的 univalence/同胚运输控制保留 `Denotes` 与 Done，未把裸 `N` 当作完成。
- 第二阶段未开启。旧机器统观、PREMISE-001、R4、文献和其它候选只作历史/潜在研究材料；不得因仍开放自动恢复。
- 唯一重开条件：用户明确开启，或一个已记录的判词改变凭据给出具体实际 H、反例、证据失效或未回答的固定六义务。
"""
        elif rel == runtime.PREFIX + "RESUME.md":
            pattern = r"## 当前阶段（2026-09-21）\n\n.*?\n\n## 历史停止点"
            replacement = "## 当前阶段（2026-09-21）\n\n四弹一体原方案 redo 已在原 X／数学现实同一性／第三弹任务忠实性勘误后重新关闭。固定十源审计未找到把静态 A 当作原圆环过程性 B 完成的实际 H；`√2` M3 继续仅是校准。`goal.md` 是唯一 current owner；第二阶段未开启。新工作必须先满足具体 H、反例、来源失效或用户明确授权的判词改变凭据，旧机器统观/PREMISE/R4 不再自动接续。\n\n## 历史停止点"
            body, count = re.subn(pattern, replacement, body, count=1, flags=re.S)
            assert count == 1
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": body})

    for name, body in (
        ("SESSION.md", session),
        ("RUNS.json", runtime.dump(runs).decode()),
        ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"])),
    ):
        files.append({"path": BASE + name, "expected_sha256": None, "text": body})

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SID,
        "load_profile": "research",
        "task_ids": [RESULT_ID],
        "authorization": "用户2026-09-21要求直接执行原X/第三弹任务忠实性勘误，并已授权当前repo的唯一工作AI完成必要状态与证据留存；不启动第二阶段。",
        "files": files,
    }
    (OUT / "checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("checkpoint-apply.json" if args.apply else "checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
