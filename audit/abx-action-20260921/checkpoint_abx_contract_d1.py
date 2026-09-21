#!/usr/bin/env python3
"""Checkpoint the qualified ABX-1/2 contract and first bounded K scan.

No new theorem is generated here.  The only mathematical inputs are existing
saved proof packages whose current source/run/index identities are verified by
``verify_abx1_contract.py`` before this state mutation is prepared.
"""

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
SID = "S-ABX-20260921-ASTRA-CONTRACT-D1"
BASE = ".codex/research/hott/sessions/" + SID + "/"
ABX_ID = "R-ABX-ACTION-20260921"
REPORT = "audit/abx-action-20260921/ABX-1-3-原对象任务合同与首个K分母.md"
QUALIFIER = "audit/abx-action-20260921/verify_abx1_contract.py"
QUALIFICATION = "audit/abx-action-20260921/ABX-1-FORMAL-QUALIFICATION.json"
ABX_SOURCES = (
    "ABX行动.md",
    "ABX行动/003 - 原圆环对象、判据与正反控制.md",
    "ABX行动/004 - 执行路径：模型、消费者与失配证明.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    REPORT,
    QUALIFIER,
    QUALIFICATION,
    "HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda",
    "HoTT/formal/agda-unimath/hott-z/PunctureApartness.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeOpenInterval.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeCompletion.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda",
    "HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == 46
    touched = {3, 5, 10, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    body = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: ABX_1_2_COMPONENTS_QUALIFIED_AND_D_ABX_1_CLOSED
- panorama_change: ACTUAL_CIRCLE_TASK_CONTRACT_AND_BOUNDED_NO_K_RESULT
- essay_change: NO
- update_decision: 用既有实际圆、闭图、任务和复原正反控制完成 ABX-1/2 的首个可检验合同；D_ABX_1 未见 K
- cross_conflicts: 直接弱删点/强删点、通常同胚/来源代理、静态 Done/过程 Done 已分开；任何一项都不能单独推出 HoTT 缺陷
- unresolved: 更强 R_origin 的用户可接受定义、扩大后的 K 分母，或一个实际 K 调用链；无新证据不重跑同一分母

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in touched:
            relation = "DEEPENED"
            judgement = "ABX 的现实语义锚被落实为实际圆—闭图任务合同；富化数据、操作合同和 K 的实际使用仍须逐项证明，不能由同胚替代。"
            evidence = f"{REPORT}；{QUALIFICATION}；新的实际 K 或强 Done 的反例将改变此处范围。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只资格化原圆环 A/B/X 的当前合同，不扩张到该独立主题。"
            evidence = "goal.md §2；无新判词改变凭据时保持停止。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：ABX 的现实对齐坚持同一对象与过程的语义锚，但当前可机器检查部分只到 `RichCurve` 的闭图代理。显式 U、双 Done 和操作合同使“理论抽象是否遗漏信息”成为可检验问题，而不把直觉直接宣告成对象层矛盾。

## 停止裁决

`D_ABX_1` 已完成且无 K。它结束这个分母，不结束 ABX。下一步只能是新的、明确版本与入口的消费者分母，或用户认可的更强 `R_origin` 合同；重复同一十个 proof-run 或把无命中外推为全库不存在均不改变判词。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    subprocess.check_call([sys.executable, "-B", QUALIFIER], cwd=ROOT)
    for rel in ABX_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 212
    assert state["latest_session"] == "S-ABX-20260921-ASTRA-INTAKE"
    assert state["execution_control"]["status"] == "ABX_ACTION_PHASE_2_ACTIVE"
    assert ABX_ID in state["records"]
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[ABX_ID])
    # The ABX record is intentionally stale while this unit adds its current
    # contract/report sources.  No unrelated record may become stale.
    assert set(plan["review_required"]) <= {ABX_ID}
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "CONTRACT-D1-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    qualification = json.loads((ROOT / QUALIFICATION).read_text())
    assert qualification["status"] == "PASS_WITH_SCOPE"
    assert qualification["K_denominator_D_ABX_1"]["verdict"] == "NO_K_WITHIN_DECLARED_DENOMINATOR"
    prior_latest = state["latest_session"]
    state["revision"] = 213
    state["latest_session"] = SID
    record = state["records"][ABX_ID]
    record["evidence_status"] = "ABX_1_2_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1 / NO_NEW_HOTT_DEFECT_CLAIM"
    record["status"] = "abx_1_2_contract_qualified_d_abx_1_complete_no_k"
    record["full_sources"] = list(dict.fromkeys(record["full_sources"] + list(ABX_SOURCES)))
    record["related_records"] = list(dict.fromkeys(record["related_records"] + [SID]))
    record["source_hashes"].update({rel: sha(ROOT / rel) for rel in ABX_SOURCES})
    record["revalidation"] = (
        "Revision213 re-qualified ten existing source/run/index packages against their current source hashes. "
        "It fixed the first actual C,p,M,N,H_top,U,Done contract and completed D_ABX_1. "
        "The result is a bounded no-K finding and representation/task boundary, not a HoTT defect or absence theorem."
    )
    record["scope"] = (
        "ABX-1 fixes an actual Dedekind circle/east, weak and strong puncture, original open interval, type-level "
        "homeomorphism, RichCurve source/closed-diagram surrogate, U=Bare and weak/strong Done. ABX-2 uses only the "
        "existing selected-rich-data and supplied-source no-go forms. D_ABX_1 audits three pinned agda-unimath "
        "uniform-homeomorphism sources, two local controls and a literal Cubical scan; it found no actual K. "
        "No unrestricted restoration theorem, real provenance theorem, actual misuse, HoTT inconsistency, defect or "
        "global absence claim is made."
    )
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_CONTRACT_AND_D1_COMPLETION_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_ACTION_PHASE_2_ABX_1_2_D1_COMPLETE",
        current_phase="PHASE_2_ABX",
        second_phase_status="ABX_1_2_COMPONENTS_QUALIFIED_D1_COMPLETE",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        next_minimal_verification=(
            "ABX-3 D_ABX_2: before any new mathematical theorem, freeze and inspect the direct consumers of the actual "
            "hott-z circle/open-interval symbols, recording whether each preserves the rich contract, changes the task, "
            "or constitutes a genuine K. New libraries/papers require a separate denominator."
        ),
    )
    state["projection"]["status"] = "ABX_1_2_COMPONENTS_QUALIFIED / D_ABX_1_NO_K_WITH_SCOPE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation after ABX-1/2 task-contract qualification and D_ABX_1 source audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: bind the original circle A/B/X contract to current formal evidence and record the first finite K scan
- status: COMPLETED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1 / NEXT_D_ABX_2

本单元不新造“圆环悖论”代码。它核对十个已有 proof run 的 source/run/index identity，固定实际 `RealCircle/east`、弱/强删点、`OpenRealInterval`、强同胚/类型路径、`RichCurve` 闭图代理、`U=Bare`、`Done_weak` 和 `Done_strong`。已有正控制表明：完整字段运输可保持强 Done；裸 `nRich` 仅过弱检查；有理点集有指定点恢复；同一 pair 可在连续曲线合同成功而在环境同胚合同失败。

`D_ABX_1` 检查 pinned agda-unimath 的 uniform-homeomorphism/closed-interval consumers、两项实际本地 M/N 控制与 Cubical literal tree。无实际 K 命中：外部代码只传递声明的度量性质，本地代码保留或区分强任务，Cubical `homeomorphism` 字面为零。这是已声明分母内的无命中，不是全库、全理论或未来代码的否定。

没有新增 kernel replay、数学 claim、HoTT 缺陷、物理恢复、外部消息或 Sub Agent。下一单元如继续，必须先冻结 D_ABX_2 的 direct-consumer 分母。
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {
                "kind": "persisted-proof-run-qualification",
                "command": "python3 -B audit/abx-action-20260921/verify_abx1_contract.py",
                "result": "PASS_WITH_SCOPE; 10 current source/run/index identities qualified, no proof command replayed",
                "mathematics": "EXISTING_KERNEL_EVIDENCE_REQUALIFIED_NOT_NEW_PROOF",
            },
            {
                "kind": "bounded-consumer-source-scan",
                "command": "included in verify_abx1_contract.py: pinned agda-unimath D_ABX_1 plus Cubical literal scan",
                "result": "NO_K_WITHIN_D_ABX_1; Cubical literal matches=0",
                "mathematics": "NOT_A_KERNEL_RUN",
            },
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "scope": "Qualification and bounded source audit only; no new theorem or defect claim.",
    }

    old_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `ACTIVE_WORK / DESIGN_AND_EVIDENCE_INTAKE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；Flash/G4 窄控制及现有原生正控制 | ABX-1 固定模型与双 Done；随后有界检索实际 K；未发现 K 前不得提出 HoTT 缺陷 | `ABX行动.md`；ABX-0 intake；revision212 receipt |"
    new_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `ACTIVE_WORK / ABX_1_2_QUALIFIED / D_ABX_1_NO_K` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、Flash/G4窄控制与D_ABX_1 | 实际模型/双Done/首个窄恢复候选已定；下一步仅冻结D_ABX_2 direct-consumer分母 | `ABX行动.md`；ABX-1-3收据；revision213 receipt |"
    old_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环第三弹的用户来源、GLM/Flash审计与执行合同 | `DIR-U-ABX-ORIGINAL-CIRCLE` | 用户精确来源、ZCode 7cb 审查、现有 Flash receipts | `DESIGN_AND_EVIDENCE_INTAKE_ACTIVE / NO_NEW_MATHEMATICAL_CLAIM` | `H_top`、`R_origin`、`K`、`U` 已消歧；GLM 模块可作控制但不能代替原任务 | 不证明来源复原不可能、实际 K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；`audit/abx-action-20260921/ABX-0-INTAKE-AUDIT.md`；revision212 receipt |"
    new_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环任务合同、现有形式控制与D_ABX_1 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320当前source/run/index、pinned agda-unimath、Cubical字面扫描 | `FORMAL_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1` | 实际C,p,M,N、U、双Done和窄恢复边界已明确；D_ABX_1无K | 不证明完整来源复原不可能、全库无K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；`audit/abx-action-20260921/ABX-1-3-原对象任务合同与首个K分母.md`；revision213 receipt |"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 212", "source_state_revision: 213")
            body = replace_once(body, "projection_generation: 20260921-direction-212", "projection_generation: 20260921-direction-213")
            body = replace_once(body, "semantic_status: ABX_ACTION_PHASE_2_ACTIVE / DESIGN_AND_EVIDENCE_INTAKE", "semantic_status: ABX_1_2_COMPONENTS_QUALIFIED / D_ABX_1_NO_K_WITH_SCOPE")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 212", "source_state_revision: 213")
            body = replace_once(body, "projection_generation: 20260921-outcome-212", "projection_generation: 20260921-outcome-213")
            body = replace_once(body, "semantic_status: ABX_ACTION_PHASE_2_ACTIVE / DESIGN_AND_EVIDENCE_INTAKE", "semantic_status: ABX_1_2_COMPONENTS_QUALIFIED / D_ABX_1_NO_K_WITH_SCOPE")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            body = replace_once(body, old_direction, new_direction)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            body = replace_once(body, old_panorama, new_panorama)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            old = "用户已明确启动第二阶段 `ABX`。ABX 观察原圆 C、指定去点 p、去点呈现 M、开区间 N 与闭合/复原过程 X；`√2` M3 保留为校准而非 ABX 失败。当前仅完成 ABX-0：用户来源冻结、GLM/Flash范围审计、H_top/R_origin/K/U 消歧与执行合同。下一步是 ABX-1 的精确模型、`Done_weak`/`Done_strong` 双正控制；之后才冻结实际 HoTT 消费者 K 的有限检索分母。原四弹第一阶段仍为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，不被追溯改写；旧机器统观、PREMISE-001、R4 等继续不自动排队。入口：`goal.md` §2、`ABX行动.md`、`audit/abx-action-20260921/ABX-0-INTAKE-AUDIT.md`；revision212 checkpoint。"
            new = "ABX 已完成首个实际任务合同和消费者分母 `D_ABX_1`。实际 `RealCircle/east`、弱/强删点、原开区间、`U=Bare`、弱/强 Done 与现有正反控制被绑定到 C261–296/C320；`D_ABX_1` 对三项 pinned agda-unimath 统一同胚源码、两项本地反向控制及 Cubical 字面扫描得到 `NO_K_WITHIN_D_ABX_1`。它只证明该分母内没有把静态同胚/忘却当作强完成的实际 K；不证明全HoTT无K或有缺陷。下一步只能冻结 `D_ABX_2` 的 direct-consumer 集，或由用户指定更强来源/操作合同。原四弹第一阶段仍为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，不被追溯改写；旧机器统观、PREMISE-001、R4 等继续不自动排队。入口：`ABX行动.md`、`audit/abx-action-20260921/ABX-1-3-原对象任务合同与首个K分母.md`；revision213 checkpoint。"
            body = replace_once(body, old, new)
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = """# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 第一阶段四弹 redo 保持 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`；ABX 不追溯改写它。
- ABX-1/2 已以实际 `RealCircle/east`、弱/强删点、原开区间、`RichCurve`、`U=Bare` 和双 Done 资格化；既有内核证据表明完整字段运输能保住强合同，而裸 `nRich` 不足。这个结论是表示/任务边界。
- `D_ABX_1` 在明确分母内得到 `NO_K_WITHIN_D_ABX_1`：没有实际消费者把静态同胚/忘却当作该强 Done。它不是全库或全 HoTT 的结论。
- 下一最小单元：预先冻结 `D_ABX_2` 的 direct consumers，逐个判定为保留强任务、改变任务或实际 K。没有新分母/实际 K，不继续重跑已资格化输入。
"""
        elif rel == runtime.PREFIX + "RESUME.md":
            pattern = r"## 当前阶段（2026-09-21）\n\n.*?\n\n## 历史停止点"
            replacement = "## 当前阶段（2026-09-21）\n\nABX 已完成首个可执行合同：实际 `RealCircle/east`、弱/强删点、原开区间、通常同胚、`RichCurve` 闭图代理、`U=Bare`、`Done_weak`/`Done_strong`。十个既有 proof package 的 source/run/index 已重新资格化；D_ABX_1 在小的明确消费者分母内未发现 K。当前是 `NO_K_WITHIN_D_ABX_1`，不是缺陷或全局结论。下一步只能预注册 D_ABX_2 的 direct consumers 或由用户补充更强来源合同；旧机器统观/PREMISE/R4 不自动接续。\n\n## 历史停止点"
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
        "task_ids": [ABX_ID],
        "authorization": "用户2026-09-21明确启动ABX并要求继续尝试；当前唯一工作AI获授权保存必要ABX模型、消费者审计、状态和checkpoint证据。",
        "files": files,
    }
    (OUT / "contract-d1-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("contract-d1-checkpoint-apply.json" if args.apply else "contract-d1-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
