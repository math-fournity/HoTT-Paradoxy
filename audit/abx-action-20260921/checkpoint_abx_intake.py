#!/usr/bin/env python3
"""Record the user-opened ABX phase as a bounded state checkpoint.

This checkpoint activates only ABX-0: the frozen user source, the audit of
the GLM/Flash input, and the execution contract.  It does not manufacture an
ABX mathematical theorem, a new kernel run, a real-world restoration result,
or a HoTT defect claim.
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
SID = "S-ABX-20260921-ASTRA-INTAKE"
BASE = ".codex/research/hott/sessions/" + SID + "/"
PLAN_COMMIT = "d7c46403f53607e9145cb63e8ed58eff6cf063b9"
ABX_ID = "R-ABX-ACTION-20260921"
ABX_INDEX = "ABX行动.md"
ABX_SHARDS = tuple(f"ABX行动/{n:03d} - {title}.md" for n, title in (
    (1, "用户任务身份、符号与成功标准"),
    (2, "GLM Flash G4的审计与可复用范围"),
    (3, "原圆环对象、判据与正反控制"),
    (4, "执行路径：模型、消费者与失配证明"),
    (5, "状态、停止条件与未来交接"),
))
USER_SOURCE = "sources/prompts/Codex-ABX行动-用户指令与GLM背景-20260921.md"
IMPORT = "audit/abx-action-20260921/SOURCE-IMPORT.json"
INTAKE = "audit/abx-action-20260921/ABX-0-INTAKE-AUDIT.md"
VERIFY = "audit/abx-action-20260921/INTAKE-VERIFICATION.json"
ZCODE_INDEX = "Astra继续尝试/ZCode-7cb会话成果吸收审查.md"
ZCODE_SHARDS = tuple(
    f"Astra继续尝试/ZCode-7cb会话成果吸收审查/{n:03d} - {title}.md"
    for n, title in (
        (1, "会话覆盖、时间线与完整工作地图"),
        (2, "四个形式模块的重放与命题忠实性"),
        (3, "语料检索、文献解释与证据治理"),
        (4, "吸收决策、后续任务与证据索引"),
    )
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(argv: list[str]) -> str:
    return subprocess.check_output(argv, cwd=ROOT, text=True).strip()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def append_after(body: str, marker: str, addition: str) -> str:
    assert marker in body, marker
    return body.replace(marker, marker + "\n" + addition, 1)


def core_audit(core: dict) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == core["kc_count"] == 46
    touched = {3, 5, 10, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    body = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: ABX_ACTION_PHASE_2_ACTIVE
- panorama_change: ABX_DESIGN_AND_EVIDENCE_INTAKE_REGISTERED
- essay_change: NO
- update_decision: 用户明确开启原圆环 A/B/X 的第二阶段；冻结 ABX-0，不把旧 √2 校准重新命名为第三弹
- cross_conflicts: `H_top`（通常同胚）与旧“实际理论承诺 H”同名，已分成 `H_top` 与 `K`；`RealitySame` 可进规格但不单独推出任务等同或实际 K
- unresolved: ABX-1 的精确原对象/双 Done 控制，随后才是有界实际消费者 K 检索；没有 K 时不得声称 HoTT 缺陷

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    for number, (kc, title) in enumerate(headings, 1):
        if number in touched:
            relation = "DEEPENED"
            judgement = "ABX 将原圆环 A/B/X 作为独立第二阶段候选：来源—复原信息须与通常同胚、任务合同和实际理论使用分开；目前没有 K。"
            evidence = f"{ABX_INDEX}；{INTAKE}；若 ABX-1 的正控制或实际 K 推翻该限定，则更新具体链，不追溯改写第一阶段。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只登记用户开启的 ABX 候选，不扩大到该独立主题。"
            evidence = "goal.md §2；未出现直接反例或实际消费者前保持既有范围。"
        body += f"| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n"
    body += """
## 扩展认知逐片复认

001–008：现实对齐可作为 ABX 的语义锚；它不把 `H_top` 自动升级为来源保持关系或理论内部承诺。ABX 的可反驳工作单位是实际输入、允许操作、观察与 Done，不是“断点”一词本身。

## 停止裁决

本 checkpoint 只完成 `ABX-0`。下一最小行动是 `ABX-1`：固定实际圆/去点/开区间模型和 `Done_weak`/`Done_strong` 正控制；在此之前不搜索全库、不申请缺陷结论，也不把 Flash/G4 的窄控制当作 K。
"""
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    assert command(["git", "rev-parse", "HEAD"]) == PLAN_COMMIT
    source_files = (ABX_INDEX, *ABX_SHARDS, USER_SOURCE, IMPORT, INTAKE, VERIFY, ZCODE_INDEX, *ZCODE_SHARDS)
    for rel in source_files:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)

    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state["revision"] == 211
    assert state["latest_session"] == "S-COR-20260921-ASTRA-ORIGINAL-X-TASK-FIDELITY"
    assert state["execution_control"]["second_phase_status"] == "NOT_OPENED"
    assert ABX_ID not in state["records"]
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[])
    assert not plan["review_required"]
    assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    prior_latest = state["latest_session"]
    state["revision"] = 212
    state["latest_session"] = SID
    state["active"] = [item for item in state["active"] if item in {"I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"}]
    state["projection"]["status"] = "ABX_ACTION_PHASE_2_ACTIVE / DESIGN_AND_EVIDENCE_INTAKE / NO_MATHEMATICAL_CLAIM"
    state["records"][ABX_ID] = {
        "kind": "candidate",
        "classification": "ORIGINAL_ABX_TASK_FIDELITY_CANDIDATE",
        "path": ABX_INDEX,
        "lifecycle_status": "ACTIVE_WORK",
        "evidence_status": "DESIGN_AND_EVIDENCE_INTAKE_ACTIVE / NO_NEW_MATHEMATICAL_CLAIM",
        "status": "abx_0_source_and_historical_control_intake_complete",
        "depends_on": [],
        "related_records": [
            "R-ASTRA-ASSUMPTION-INTEGRATION-20260921",
            "R-ASTRA-TASK-FIDELITY-CORRIGENDUM-20260921",
            SID,
        ],
        "full_sources": list(source_files),
        "scope": (
            "ABX is the user-opened second-phase candidate about the original circle/puncture/open-interval/"
            "restoration process. ABX-0 freezes the user source, audits GLM Flash/G4 as narrow controls, and fixes the "
            "H_top/R_origin/K/U vocabulary. It has not fixed an OriginPresentation, a strong completion theorem, or an "
            "actual HoTT consumer K; it asserts no HoTT defect, inconsistency, physical result, or global absence theorem."
        ),
        "source_hashes": {rel: sha(ROOT / rel) for rel in source_files},
    }
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "ABX_PHASE_2_INTAKE_CHECKPOINT_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [ABX_ID, prior_latest],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update(
        status="ABX_ACTION_PHASE_2_ACTIVE",
        current_phase="PHASE_2_ABX",
        second_phase_status="ABX_DESIGN_AND_EVIDENCE_INTAKE_ACTIVE",
        last_checkpoint_session=SID,
        checkpoint_result=".codex/cognition/checkpoints/" + SID + "/result.json",
        abx_record=ABX_ID,
        next_minimal_verification=(
            "ABX-1: fix one actual circle/puncture/open-interval OriginPresentation, a declared U, Done_weak and "
            "Done_strong with positive controls; then freeze a finite actual-consumer K denominator. Do not claim a "
            "defect unless an actual K treats H_top/U as completing Done_strong."
        ),
    )

    session = f"""# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 state mutation after user-authorized ABX source and plan intake
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: register the user-opened ABX second phase without changing the completed first-phase verdict
- plan_commit: {PLAN_COMMIT}
- status: COMPLETED_WITH_SCOPE / ABX_0_INTAKE / ABX_1_NEXT

用户明确拒绝把旧 `√2` 的 `Spec_A`/`Spec_B` 校准当成原圆环第三弹的失败。ABX 因而固定为独立候选：原圆 C、指定去点 p、去点呈现 M、开区间 N、两端闭合/复原过程 X，以及静态处理 A 与过程完成 B。`H_top` 是通常同胚，`R_origin` 是待精确化的来源—复原关系，`K` 是实际 HoTT 使用事实，`U` 是明确忘却映射；这些不能互相偷换。

本 checkpoint 保存用户原文的精确快照、GLM Flash/G4 的范围审计、ZCode 7cb 的可见轨迹审查和 ABX 五片设计。Flash 四模块仅是富化数据/排除证据的窄控制；`Σ x:C, x≠p`、恒等 bridge 或逻辑过强命题都不等于原圆环任务。没有新证明源码、内核运行、实际 K、来源恢复不可能性或 HoTT 缺陷结论。

下一单元只做 ABX-1 的模型与双 Done 正控制；之后才可冻结 K 的有限检索分母。无 Sub Agent、push、tag、公开或外部消息。
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {
                "kind": "user-source-import-verification",
                "command": "python3 -B audit/abx-action-20260921/verify_abx_intake.py",
                "result": "PASS_WITH_SCOPE; source snapshot and 13 historical Flash/ZCode identities qualified",
                "mathematics": "NOT_A_KERNEL_RUN",
            }
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "scope": "State and evidence intake only; no new mathematical proof or consumer result.",
    }

    direction_row = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环 A/B/X 的来源—复原任务保真候选 | 用户 2026-09-21 明确开启；`goal.md` §2 | `ACTIVE_WORK / DESIGN_AND_EVIDENCE_INTAKE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-ABX-ACTION-20260921`；Flash/G4 窄控制及现有原生正控制 | ABX-1 固定模型与双 Done；随后有界检索实际 K；未发现 K 前不得提出 HoTT 缺陷 | `ABX行动.md`；ABX-0 intake；revision212 receipt |"
    panorama_row = "| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环第三弹的用户来源、GLM/Flash审计与执行合同 | `DIR-U-ABX-ORIGINAL-CIRCLE` | 用户精确来源、ZCode 7cb 审查、现有 Flash receipts | `DESIGN_AND_EVIDENCE_INTAKE_ACTIVE / NO_NEW_MATHEMATICAL_CLAIM` | `H_top`、`R_origin`、`K`、`U` 已消歧；GLM 模块可作控制但不能代替原任务 | 不证明来源复原不可能、实际 K、HoTT误用、理论缺陷或公开结论 | `ABX行动.md`；`audit/abx-action-20260921/ABX-0-INTAKE-AUDIT.md`；revision212 receipt |"

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, "source_state_revision: 211", "source_state_revision: 212")
            body = replace_once(body, "projection_generation: 20260921-direction-211", "projection_generation: 20260921-direction-212")
            body = replace_once(body, "semantic_status: FOUR_STAGE_REDO_PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM", "semantic_status: ABX_ACTION_PHASE_2_ACTIVE / DESIGN_AND_EVIDENCE_INTAKE")
        elif rel == runtime.PANORAMA:
            body = replace_once(body, "source_state_revision: 211", "source_state_revision: 212")
            body = replace_once(body, "projection_generation: 20260921-outcome-211", "projection_generation: 20260921-outcome-212")
            body = replace_once(body, "semantic_status: FOUR_STAGE_REDO_PHASE_1_RECLOSED_AFTER_TASK_FIDELITY_CORRIGENDUM", "semantic_status: ABX_ACTION_PHASE_2_ACTIVE / DESIGN_AND_EVIDENCE_INTAKE")
        elif rel == "方向追踪/002 - 治理与用户方向.md":
            marker = "| `DIR-U-ASTRA-BREAKPOINT` | 原四弹 redo：原X/任务忠实性勘误后的范围判词 | 用户两阶段 goal；`goal.md` §1.1 | `CLOSED_WITH_SCOPE / PHASE_1_RECLOSED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-ASSUMPTION-INTEGRATION-35`、`R-ASTRA-TASK-FIDELITY-CORRIGENDUM-20260921`及C250–324 | 原整体击落论证未建立；固定来源未找到实际H；第二阶段未开启 | `goal.md`；第三十五轮第007片；H审计；revision211 receipt |"
            body = append_after(body, marker, direction_row)
        elif rel == "全景视野/003 - 当前机器证明包与原生重放.md":
            marker = "| `OUT-ASTRA-ASSUMPTION-INTEGRATION-35` | 原四弹 redo 的修正范围判词 | `DIR-U-ASTRA-BREAKPOINT` | 六原文/五方案、C250–324、9包18资格、14固定Coq源、原X/H十源审计 | `PHASE_1_RECLOSED_WITH_SCOPE / ORIGINAL_TARGET_NOT_ESTABLISHED / NO_H_IN_FIXED_SCOPE` | 原圆环X、R/C/H与√2校准分开；精确局部结果保留 | 不证明全HoTT无问题、全局不存在H、物理实现、Coq全库有效或已击落；第二阶段未开启 | `goal.md`；第三十五轮第007片；H审计；revision211 receipt |"
            body = append_after(body, marker, panorama_row)
        elif rel == "MEMORY/001 - 当前执行队列.md":
            old = "用户当前 `/goal` 的两阶段四弹 redo 第一阶段已在原X/任务忠实性勘误后重新关闭。原主过程是圆去点、开区间呈现与两端闭合/复原；`RealitySame` 可作语义锚，却不等于任务合同 C 或实际 HoTT 承诺 H。固定十源审计未找到 H；原 `√2` M3 只保留为校准。当前判词仍为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，精确局部证明保留。第二阶段未开启；旧机器统观、PREMISE-001、R4、一般反向、独立性、更多消费者与新版包不再自动排队。只在用户明确开启或出现具体 H、反例、来源/运行失效等合格凭据时重开。revision211 checkpoint 写入此状态。入口：`goal.md`、第三十五轮第007片、`audit/astra-task-fidelity-corrigendum-20260921/H-COMMITMENT-AUDIT.md`。"
            new = "用户已明确启动第二阶段 `ABX`。ABX 观察原圆 C、指定去点 p、去点呈现 M、开区间 N 与闭合/复原过程 X；`√2` M3 保留为校准而非 ABX 失败。当前仅完成 ABX-0：用户来源冻结、GLM/Flash范围审计、H_top/R_origin/K/U 消歧与执行合同。下一步是 ABX-1 的精确模型、`Done_weak`/`Done_strong` 双正控制；之后才冻结实际 HoTT 消费者 K 的有限检索分母。原四弹第一阶段仍为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，不被追溯改写；旧机器统观、PREMISE-001、R4 等继续不自动排队。入口：`goal.md` §2、`ABX行动.md`、`audit/abx-action-20260921/ABX-0-INTAKE-AUDIT.md`；revision212 checkpoint。"
            body = replace_once(body, old, new)
        elif rel == runtime.PREFIX + "FRONTIER.md":
            body = """# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 四弹一体原方案 redo 的第一阶段保持 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`；它没有被 ABX 追溯性改写。
- 用户已明确开启第二阶段 `ABX`：原圆/去点/开区间/闭合—复原的 A/B/X 候选。ABX-0 已冻结来源，区分 `H_top`、`R_origin`、实际使用事实 `K` 和忘却 `U`，并将 Flash/G4 降为窄控制。
- 当前下一最小单元是 ABX-1：固定一个实际模型及 `Done_weak`/`Done_strong` 的双正控制。没有实际 K 把 `H_top` 或 U 当作强完成前，不可声称 HoTT 缺陷。
- 旧机器统观、PREMISE-001、R4、文献和其它候选仍不自动恢复；每次扩展分母或进入新数学命题都须有单独的判词改变凭据。
"""
        elif rel == runtime.PREFIX + "RESUME.md":
            old = "四弹一体原方案 redo 已在原 X／数学现实同一性／第三弹任务忠实性勘误后重新关闭。固定十源审计未找到把静态 A 当作原圆环过程性 B 完成的实际 H；`√2` M3 继续仅是校准。`goal.md` 是唯一 current owner；第二阶段未开启。新工作必须先满足具体 H、反例、来源失效或用户明确授权的判词改变凭据，旧机器统观/PREMISE/R4 不再自动接续。"
            new = "四弹一体原方案 redo 第一阶段已在原 X／数学现实同一性／第三弹任务忠实性勘误后关闭；固定十源未找到把静态 A 当原过程 B 完成的实际 H，`√2` 只保留为校准。用户已明确授权独立第二阶段 ABX，current owner 为 `ABX行动.md`。现在只做 ABX-1 的实际模型、`Done_weak`/`Done_strong` 正控制；之后才以已冻结的有限分母寻找实际 K。ABX 不得因为设计或富化表示存在就被报为 HoTT 缺陷。旧机器统观/PREMISE/R4 不自动接续。"
            body = replace_once(body, old, new)
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
        "task_ids": [],
        "authorization": "用户于2026-09-21明确启动ABX第二阶段，并要求当前唯一工作AI继续、更新相关文档；授权将ABX-0来源和计划状态写入当前repo与canonical checkpoint。",
        "files": files,
    }
    (OUT / "checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    (OUT / ("checkpoint-apply.json" if args.apply else "checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
