#!/usr/bin/env python3
"""Checkpoint the finite D_ABX_2 direct-consumer audit."""

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
SID = "S-ABX-20260921-ASTRA-D2-DIRECT-CONSUMERS"
BASE = ".codex/research/hott/sessions/" + SID + "/"
ABX_ID = "R-ABX-ACTION-20260921"
D2_SCRIPT = "audit/abx-action-20260921/verify_abx_d2_direct_consumers.py"
D2_JSON = "audit/abx-action-20260921/ABX-3-D2-DIRECT-CONSUMERS.json"
D2_REPORT = "audit/abx-action-20260921/ABX-3-D2-原生直接消费者审计.md"
SOURCES = (
    "ABX行动.md",
    "ABX行动/004 - 执行路径：模型、消费者与失配证明.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    D2_SCRIPT,
    D2_JSON,
    D2_REPORT,
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
- direction_change: D_ABX_2_DIRECT_CONSUMERS_CLOSED_WITH_SCOPE
- panorama_change: SECOND_BOUNDED_NO_K_RESULT_AND_EXPLICIT_DEFENSE_CLASSIFICATION
- essay_change: NO
- update_decision: 29个直接 import 的原生消费者分母以remainder=0完成；最接近模块保留/要求强任务，未见K
- cross_conflicts: “有import/有同胚”不等于“把同胚作为强Done”；本地项目代码也不自动成为外部自然消费者
- unresolved: 外部库/论文的独立K分母或更强R_origin合同；D_ABX_2不得被当作全库扫描

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in touched:
            relation = "DEEPENED"
            judgement = "ABX 以实际代码而非词汇判断理论使用：直接消费者若保留字段、显式要求原则或分开操作，即是反向控制而非K。"
            evidence = f"{D2_REPORT}；{D2_JSON}；发现同时满足H_top/U、忽略R、宣称Done_strong的调用链才改判。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只完成ABX的第二个有限消费者分母。"
            evidence = "goal.md §2；新外部分母须单独预注册。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：现实对齐要求理论使用和实际任务之间有真实调用桥。D_ABX_2 显示当前最贴近的本地源码没有略过这座桥；这是有界证据，不是对理论或现实的最终判词。

## 停止裁决

D_ABX_2 完成后停止该本地直接-import分母。下一动作需选择一个版本固定的外部教材/库/论文来源，或先由用户定义更强R_origin；不能把第二次无命中转写为全局无风险。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    subprocess.check_call([sys.executable, "-B", D2_SCRIPT], cwd=ROOT)
    for rel in SOURCES:
        assert (ROOT / rel).is_file(), rel
    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 213
    assert state["latest_session"] == "S-ABX-20260921-ASTRA-CONTRACT-D1"
    assert state["execution_control"]["status"] == "ABX_ACTION_PHASE_2_ABX_1_2_D1_COMPLETE"
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[ABX_ID])
    assert set(plan["review_required"]) <= {ABX_ID}
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "D2-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    d2 = json.loads((ROOT / D2_JSON).read_text())
    assert d2["status"] == "PASS_WITH_SCOPE"
    assert d2["denominator"]["remainder"] == 0
    assert d2["verdict"] == "NO_K_WITHIN_D_ABX_2"

    prior_latest = state["latest_session"]
    state["revision"] = 214
    state["latest_session"] = SID
    record = state["records"][ABX_ID]
    record["evidence_status"] = "ABX_1_2_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1_AND_D_ABX_2 / NO_NEW_HOTT_DEFECT_CLAIM"
    record["status"] = "abx_1_2_contract_qualified_d1_d2_complete_no_k"
    record["full_sources"] = list(dict.fromkeys(record["full_sources"] + list(SOURCES)))
    record["related_records"] = list(dict.fromkeys(record["related_records"] + [SID]))
    record["source_hashes"].update({rel: sha(ROOT / rel) for rel in SOURCES})
    record["revalidation"] = (
        "Revision214 enumerated every direct local import of six ABX roots (29/29, remainder=0), "
        "classified the closest consumers by code anchors, and found no K. This is a local direct-consumer "
        "audit; it does not generalize to external libraries, the Book, or all HoTT uses."
    )
    record["scope"] = (
        "ABX has two bounded no-K results. D_ABX_1 covers three pinned agda-unimath uniform-homeomorphism files, "
        "two local controls and a Cubical literal scan. D_ABX_2 covers the 29 project-local hott-z files directly "
        "importing one of six circle/interval roots. Neither is a global absence theorem or a HoTT defect claim."
    )
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_D2_DIRECT_CONSUMER_AUDIT_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_ACTION_PHASE_2_D1_D2_COMPLETE_WITH_SCOPE",
        current_phase="PHASE_2_ABX",
        second_phase_status="ABX_1_2_QUALIFIED_D1_D2_COMPLETE",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        next_minimal_verification=(
            "ABX-3 D_ABX_3: freeze exact HoTT Book source sections on type equivalence, univalence and homotopy interpretation; "
            "test whether they assert any H_top/U-to-Done_strong bridge. This is a source-reading audit, not a proof of global absence."
        ),
    )
    state["projection"]["status"] = "ABX_1_2_QUALIFIED / D_ABX_1_D_ABX_2_NO_K_WITH_SCOPE / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation after D_ABX_2 direct-consumer audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: enumerate and classify the local direct consumers of the ABX circle roots
- status: COMPLETED_WITH_SCOPE / 29_OF_29 / NO_K_WITHIN_D_ABX_2

`D_ABX_2` selects exactly every `hott-z/*.agda` directly importing one of NativeOpenInterval, NativeRichCurve, NativeSourceContract, NativeTaskIntegration, PunctureApartness or NativeCompletion. The script found 29 files, all classified with hashes and direct-import anchors. The nearest modules explicitly forbid BareStep→AmbientStep lifting, preserve full-field transport, require Lift/RealNonzeroApartness for weak coverage or homeomorphism, or distinguish Done/operation contracts.

The result is no K in this declared local denominator. It does not treat project-local code as community practice, does not prove any external absence, and does not claim a HoTT defect. No new theorem, kernel replay, physical result, external message or Sub Agent occurred.
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{
            "kind": "bounded-direct-source-enumeration", "command": f"python3 -B {D2_SCRIPT}",
            "result": "PASS_WITH_SCOPE; 29 records, remainder=0, no K in declared denominator", "mathematics": "NOT_A_KERNEL_RUN",
        }],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "A local source denominator and classification audit, not a mathematical theorem.",
    }

    old_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `ACTIVE_WORK / ABX_1_2_QUALIFIED / D_ABX_1_NO_K` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、Flash/G4窄控制与D_ABX_1 | 实际模型/双Done/首个窄恢复候选已定；下一步仅冻结D_ABX_2 direct-consumer分母 | `ABX行动.md`；ABX-1-3收据；revision213 receipt |"
    new_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `ACTIVE_WORK / D_ABX_1_D_ABX_2_NO_K` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、两有界K分母 | 29个本地direct consumers已穷尽且无K；下一步仅冻结外部Book/库/论文分母或更强R_origin | `ABX行动.md`；ABX-1-3/D2收据；revision214 receipt |"
    old_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环任务合同、现有形式控制与D_ABX_1 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320当前source/run/index、pinned agda-unimath、Cubical字面扫描 | `FORMAL_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1` | 实际C,p,M,N、U、双Done和窄恢复边界已明确；D_ABX_1无K | 不证明完整来源复原不可能、全库无K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；`audit/abx-action-20260921/ABX-1-3-原对象任务合同与首个K分母.md`；revision213 receipt |"
    new_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环合同、两有界K分母与本地direct-consumer分类 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320、D_ABX_1、D_ABX_2 29/29源码 | `FORMAL_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1_AND_D_ABX_2` | 当前原生消费者保留强任务、显式原则或分开操作；两分母均无K | 不证明完整来源复原不可能、外部全库无K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；ABX-1-3/D2收据；revision214 receipt |"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 213", "source_state_revision: 214")
            body = replace_once(body, "projection_generation: 20260921-direction-213", "projection_generation: 20260921-direction-214")
            body = replace_once(body, "semantic_status: ABX_1_2_COMPONENTS_QUALIFIED / D_ABX_1_NO_K_WITH_SCOPE", "semantic_status: ABX_1_2_QUALIFIED / D_ABX_1_D_ABX_2_NO_K_WITH_SCOPE")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 213", "source_state_revision: 214")
            body = replace_once(body, "projection_generation: 20260921-outcome-213", "projection_generation: 20260921-outcome-214")
            body = replace_once(body, "semantic_status: ABX_1_2_COMPONENTS_QUALIFIED / D_ABX_1_NO_K_WITH_SCOPE", "semantic_status: ABX_1_2_QUALIFIED / D_ABX_1_D_ABX_2_NO_K_WITH_SCOPE")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            body = replace_once(body, old_direction, new_direction)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            body = replace_once(body, old_panorama, new_panorama)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            old = "ABX 已完成首个实际任务合同和消费者分母 `D_ABX_1`。实际 `RealCircle/east`、弱/强删点、原开区间、`U=Bare`、弱/强 Done 与现有正反控制被绑定到 C261–296/C320；`D_ABX_1` 对三项 pinned agda-unimath 统一同胚源码、两项本地反向控制及 Cubical 字面扫描得到 `NO_K_WITHIN_D_ABX_1`。它只证明该分母内没有把静态同胚/忘却当作强完成的实际 K；不证明全HoTT无K或有缺陷。下一步只能冻结 `D_ABX_2` 的 direct-consumer 集，或由用户指定更强来源/操作合同。原四弹第一阶段仍为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，不被追溯改写；旧机器统观、PREMISE-001、R4 等继续不自动排队。入口：`ABX行动.md`、`audit/abx-action-20260921/ABX-1-3-原对象任务合同与首个K分母.md`；revision213 checkpoint。"
            new = "ABX 已完成两个有限K分母。`D_ABX_1` 检查三项pinned agda-unimath统一同胚源码、两项本地反向控制和Cubical字面扫描；`D_ABX_2` 穷尽29个直接import六个ABX根模块的本地 `hott-z` 文件。两者均为 `NO_K_WITHIN_DECLARED_DENOMINATOR`：最接近代码保留字段、显式要求Lift/原则，或区分操作/Done。它们不证明外部全库无K或HoTT无缺陷。下一步只能冻结一个外部Book/库/论文分母，或由用户定义更强R_origin；原四弹第一阶段仍不被追溯改写，旧机器统观/PREMISE/R4继续不自动排队。入口：`ABX行动.md`、ABX-1-3/D2收据；revision214 checkpoint。"
            body = replace_once(body, old, new)
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = """# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 第一阶段四弹 redo 保持 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`；ABX 不追溯改写它。
- ABX-1/2 已固定实际圆、弱/强删点、开区间、RichCurve、U与双Done。D_ABX_1 与 D_ABX_2 都没有发现实际K：前者是小型外部/本地分母，后者是29/29本地direct consumers。
- 最近消费者要么保留完整字段、要么显式要求Lift/RealNonzeroApartness、要么把操作合同分开。因此当前是有界表示/任务边界，而非HoTT缺陷。
- 下一最小单元：冻结Book或独立外部库的精确源码分母，检查其是否有H_top/U→Done_strong桥；不能重跑D1/D2或把无命中外推。
"""
        elif rel == runtime.PREFIX + "RESUME.md":
            pattern = r"## 当前阶段（2026-09-21）\n\n.*?\n\n## 历史停止点"
            replacement = "## 当前阶段（2026-09-21）\n\nABX 已完成实际任务合同和两个有界消费者分母。D_ABX_1（pinned agda-unimath/本地控制/Cubical字面）与D_ABX_2（29个本地direct imports）均未出现K；closest consumers显式保留强任务或要求额外原则。当前结论仍是表示/任务边界。下一步只能冻结外部Book/库/论文的精确来源分母，检查是否存在H_top/U→Done_strong桥；旧机器统观/PREMISE/R4不自动接续。\n\n## 历史停止点"
            body, count = re.subn(pattern, replacement, body, count=1, flags=re.S)
            assert count == 1
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": body})

    for name, body in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode()), ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"]))):
        files.append({"path": BASE + name, "expected_sha256": None, "text": body})
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [ABX_ID],
        "authorization": "用户2026-09-21明确启动ABX并要求继续尝试；当前唯一工作AI获授权保存D_ABX_2消费者审计及必要current-state/checkpoint。",
        "files": files,
    }
    (OUT / "D2-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("D2-checkpoint-apply.json" if args.apply else "D2-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
