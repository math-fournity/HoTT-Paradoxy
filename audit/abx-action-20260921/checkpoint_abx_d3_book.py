#!/usr/bin/env python3
"""Checkpoint the fixed HoTT Book core-rule audit for ABX."""

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
SID = "S-ABX-20260921-ASTRA-D3-BOOK-CORE"
BASE = ".codex/research/hott/sessions/" + SID + "/"
ABX_ID = "R-ABX-ACTION-20260921"
D3_SCRIPT = "audit/abx-action-20260921/verify_abx_d3_book.py"
D3_JSON = "audit/abx-action-20260921/ABX-3-D3-BOOK-CORE.json"
D3_REPORT = "audit/abx-action-20260921/ABX-3-D3-HoTT-Book核心规则审计.md"
SOURCES = (
    "goal.md", "feature-list.md", "ABX行动.md",
    "ABX行动/004 - 执行路径：模型、消费者与失配证明.md",
    "ABX行动/005 - 状态、停止条件与未来交接.md",
    D3_SCRIPT, D3_JSON, D3_REPORT,
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/SOURCES_AND_COVERAGE.md",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/introduction.tex",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/basics.tex",
    "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex",
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
- direction_change: ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE
- panorama_change: BOOK_CORE_RULE_NO_BRIDGE_RECORDED
- essay_change: NO
- update_decision: 固定Book核心规则确认univalence是类型等价/transport且其空间解释非点集拓扑；ABX初始边界完成
- cross_conflicts: 使用“空间”“路径”语言不等于传统点集同胚、闭包或过程完成；Book的规则不能被直接改写为H_top/U→Done_strong
- unresolved: 真实外部K、用户认可的更强R_origin、或新的有版本身份的库/论文消费者；无其一不自动扩搜

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in touched:
            relation = "DEEPENED"
            judgement = "ABX 的现实任务需要一个附加的实际桥；Book的同伦解释和univalence本身不含点集来源/复原完成合同。"
            evidence = f"{D3_REPORT}；{D3_JSON}；出现具体K或更强合同反例才可改变此范围。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只审计ABX相关的Book核心规则分母。"
            evidence = "goal.md §2；不外推到独立主题。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：理论对现实的解释仍可被提出和审查，但它不是从“空间”一词自动得到的定理。当前ABX把这种解释的缺口准确定位为仍缺K，而不把缺口写成已发生的内部矛盾。

## 停止裁决

ABX 的初始合同与三个有界分母已经完成。当前没有新的、能改变判词的实际K或更强来源合同，因此停止自动扩展。后继必须先固定新外部来源/版本/调用链或获得用户对R_origin的精确扩展；重复D1–D3不改变结论。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", D3_SCRIPT], cwd=ROOT)
    for rel in SOURCES:
        assert (ROOT / rel).is_file(), rel
    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 214
    assert state["latest_session"] == "S-ABX-20260921-ASTRA-D2-DIRECT-CONSUMERS"
    assert state["execution_control"]["status"] == "ABX_ACTION_PHASE_2_D1_D2_COMPLETE_WITH_SCOPE"
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[ABX_ID])
    assert set(plan["review_required"]) <= {ABX_ID}
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "D3-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    d3 = json.loads((ROOT / D3_JSON).read_text())
    assert d3["status"] == "PASS_WITH_SCOPE"
    assert d3["source"]["all_tex_file_count"] == 18
    assert d3["source"]["homeomorph_lexical_matches"] == []

    prior_latest = state["latest_session"]
    state["revision"] = 215
    state["latest_session"] = SID
    record = state["records"][ABX_ID]
    record["evidence_status"] = "INITIAL_ABX_BOUNDARY_ESTABLISHED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1_D_ABX_2_D_ABX_3 / NO_NEW_HOTT_DEFECT_CLAIM"
    record["status"] = "initial_abx_boundary_complete_three_bounded_no_k_results"
    record["full_sources"] = list(dict.fromkeys(record["full_sources"] + list(SOURCES)))
    record["related_records"] = list(dict.fromkeys(record["related_records"] + [SID]))
    record["source_hashes"].update({rel: sha(ROOT / rel) for rel in SOURCES})
    record["revalidation"] = (
        "Revision215 audited the hash-pinned Book core source. The Book treats types homotopically rather than through "
        "point-set topology, defines univalence by type equivalence/universe transport, and gives no H_top/U-to-Done_strong "
        "bridge in the selected core or an 18-file homeomorph lexical denominator. This completes the initial ABX boundary, "
        "not a global absence theorem or a HoTT defect verdict."
    )
    record["scope"] = (
        "The initial ABX cycle fixed an actual circle/interval task contract and completed D_ABX_1 (pinned metric sources), "
        "D_ABX_2 (29 local direct consumers), and D_ABX_3 (Book core rules/18 tex lexical denominator). None gives an actual K. "
        "A future defect proof requires a separately frozen external K or a user-accepted stronger R_origin contract."
    )
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_BOOK_CORE_AUDIT_AND_INITIAL_BOUNDARY_CLOSURE_WITH_SCOPE", "status": "complete_with_scope",
        "depends_on": [], "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE",
        current_phase="PHASE_2_ABX_INITIAL_BOUNDARY_COMPLETE",
        second_phase_status="ABX_INITIAL_BOUNDARY_COMPLETE_THREE_DENOMINATORS_NO_K",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        next_minimal_verification=(
            "STOP_BY_DEFAULT. Reopen only for a concrete version-pinned external library/paper/application candidate K with a possible "
            "H_top/U-to-Done_strong call chain, a user-specified stronger R_origin/operation contract, or direct evidence invalidating D_ABX_1–3."
        ),
    )
    state["projection"]["status"] = "ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / THREE_BOUNDED_NO_K_RESULTS / NO_NEW_HOTT_DEFECT_CLAIM"

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation after fixed HoTT Book core-rule audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: determine whether basic univalence/homotopy rules already provide an ABX K bridge
- status: COMPLETED_WITH_SCOPE / INITIAL_ABX_BOUNDARY_ESTABLISHED

The fixed HoTT Book source distinguishes its homotopical treatment of types from point-set topology, describes univalence as an equivalence between universe paths and type equivalences with family transport, and defines equivalence using maps/homotopies/inverse or fiber data. The declared 18-file tex denominator has no homeomorph lexical match. It supplies no H_top/U-to-Done_strong bridge for the circle task.

This is a source interpretation with pinned hashes, not a proof that no later application can introduce K. Together with D_ABX_1 and D_ABX_2 it closes the initial ABX boundary. No new mathematical theorem, kernel replay, global safety/defect conclusion, external message or Sub Agent occurred.
"""
    runs = {
        "schema_version": "hott-session-runs/v1", "session_id": SID,
        "primary_runs": [{"kind": "pinned-book-source-audit", "command": f"python3 -B {D3_SCRIPT}", "result": "PASS_WITH_SCOPE; 18 tex files and three core sources qualified; no core bridge", "mathematics": "NOT_A_KERNEL_RUN"}],
        "new_math_claims": [], "new_kernel_replay": False,
        "scope": "Book source scope, not a theorem about all HoTT applications.",
    }

    old_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `ACTIVE_WORK / D_ABX_1_D_ABX_2_NO_K` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、两有界K分母 | 29个本地direct consumers已穷尽且无K；下一步仅冻结外部Book/库/论文分母或更强R_origin | `ABX行动.md`；ABX-1-3/D2收据；revision214 receipt |"
    new_direction = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / D1_D2_D3_NO_K` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；C261–296/C320、D1/D2/Book D3 | 初始合同与三分母完成；只有新外部K候选或用户更强R_origin才重开 | `ABX行动.md`；ABX-1-3/D2/D3收据；revision215 receipt |"
    old_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环合同、两有界K分母与本地direct-consumer分类 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320、D_ABX_1、D_ABX_2 29/29源码 | `FORMAL_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1_AND_D_ABX_2` | 当前原生消费者保留强任务、显式原则或分开操作；两分母均无K | 不证明完整来源复原不可能、外部全库无K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；ABX-1-3/D2收据；revision214 receipt |"
    new_panorama = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环合同与三个有界K分母 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C261–296/C320、D1、D2=29/29、Book D3=18 tex | `INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / NO_K_WITHIN_D1_D2_D3` | 本地消费者保留强任务；Book核心不把点集同胚/忘却规定为强完成 | 不证明完整来源复原不可能、外部全库无K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；ABX-1-3/D2/D3收据；revision215 receipt |"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 214", "source_state_revision: 215")
            body = replace_once(body, "projection_generation: 20260921-direction-214", "projection_generation: 20260921-direction-215")
            body = replace_once(body, "semantic_status: ABX_1_2_QUALIFIED / D_ABX_1_D_ABX_2_NO_K_WITH_SCOPE", "semantic_status: ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / D_ABX_1_D_ABX_2_D_ABX_3_NO_K")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 214", "source_state_revision: 215")
            body = replace_once(body, "projection_generation: 20260921-outcome-214", "projection_generation: 20260921-outcome-215")
            body = replace_once(body, "semantic_status: ABX_1_2_QUALIFIED / D_ABX_1_D_ABX_2_NO_K_WITH_SCOPE", "semantic_status: ABX_INITIAL_BOUNDARY_ESTABLISHED_WITH_SCOPE / D_ABX_1_D_ABX_2_D_ABX_3_NO_K")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            body = replace_once(body, old_direction, new_direction)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            body = replace_once(body, old_panorama, new_panorama)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            old = "ABX 已完成两个有限K分母。`D_ABX_1` 检查三项pinned agda-unimath统一同胚源码、两项本地反向控制和Cubical字面扫描；`D_ABX_2` 穷尽29个直接import六个ABX根模块的本地 `hott-z` 文件。两者均为 `NO_K_WITHIN_DECLARED_DENOMINATOR`：最接近代码保留字段、显式要求Lift/原则，或区分操作/Done。它们不证明外部全库无K或HoTT无缺陷。下一步只能冻结一个外部Book/库/论文分母，或由用户定义更强R_origin；原四弹第一阶段仍不被追溯改写，旧机器统观/PREMISE/R4继续不自动排队。入口：`ABX行动.md`、ABX-1-3/D2收据；revision214 checkpoint。"
            new = "ABX 初始边界已完成。实际圆/双Done合同、D_ABX_1、D_ABX_2=29本地direct消费者以及Book D_ABX_3=18 tex核心规则均未提供实际K；Book明确将空间语言限于纯同伦理解而非点集拓扑。当前结论是`INITIAL_ABX_BOUNDARY_ESTABLISHED_WITH_SCOPE`，不是HoTT缺陷或全局安全结论。默认停止自动扩展；只有新版本冻结的外部K调用链、用户认可的更强R_origin/操作合同，或现有证据失效才重开。原四弹第一阶段仍不被追溯改写，旧机器统观/PREMISE/R4继续不自动排队。入口：`ABX行动.md`及ABX-1-3/D2/D3收据；revision215 checkpoint。"
            body = replace_once(body, old, new)
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = """# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 第一阶段四弹 redo 保持 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`；ABX 不追溯改写它。
- ABX 的初始边界已经以实际圆/双Done合同、D_ABX_1、D_ABX_2（29本地direct consumers）和D_ABX_3（Book核心/18 tex）闭合。三个分母都没有K。
- Book把类型空间解释限定为纯同伦而非点集拓扑；本地实际消费者保留强字段、显式原则或操作区别。当前可支持的结论是表示/任务边界。
- 默认停止自动扩展。只有新版本固定的外部K候选、用户认可的更强R_origin/操作合同，或现有证据失效可以重开ABX。
"""
        elif rel == runtime.PREFIX + "RESUME.md":
            pattern = r"## 当前阶段（2026-09-21）\n\n.*?\n\n## 历史停止点"
            replacement = "## 当前阶段（2026-09-21）\n\nABX 初始边界已闭合：实际圆/去点/开区间与双Done合同、D_ABX_1、D_ABX_2的29个本地direct consumers、D_ABX_3的固定HoTT Book核心规则都没有找到K。Book的univalence是类型等价和类型族transport，且明确不把其空间语言当点集拓扑。当前是有界表示/任务边界，不是HoTT缺陷或全局安全结论。默认停止；新外部K调用链、用户认可的更强R_origin合同或证据失效才重开。\n\n## 历史停止点"
            body, count = re.subn(pattern, replacement, body, count=1, flags=re.S)
            assert count == 1
        files.append({"path": rel, "expected_sha256": runtime.sha(raw), "text": body})

    for name, body in (("SESSION.md", session), ("RUNS.json", runtime.dump(runs).decode()), ("CORE_COGNITION_AUDIT.md", core_audit(state["current_core"]))):
        files.append({"path": BASE + name, "expected_sha256": None, "text": body})
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SID, "load_profile": "research", "task_ids": [ABX_ID],
        "authorization": "用户2026-09-21明确启动并要求继续ABX；当前唯一工作AI获授权保存Book核心审计、初始ABX边界判词与必要checkpoint。", "files": files,
    }
    (OUT / "D3-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("D3-checkpoint-apply.json" if args.apply else "D3-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
