#!/usr/bin/env python3
"""Write P23/P24 results and the P25 successor into the canonical checkpoint."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-RES-20260921-ASTRA-P24-ERCF3-QUALIFICATION"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P23 = "R-P23-INDEPENDENT-INGRESS-DISCOVERY-20260921"
P24 = "R-P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-20260921"
P23_DIR = "audit/p23-independent-ingress-discovery-20260921"
P24_DIR = "audit/p24-ercf3-proof-predicate-qualification-20260921"
P23_SOURCES = (
    f"{P23_DIR}/P23-INDEPENDENT-INGRESS-DISCOVERY-REPORT.md",
    f"{P23_DIR}/verify_p23_independent_ingress_discovery.py",
    f"{P23_DIR}/P23-INDEPENDENT-INGRESS-DISCOVERY-VERIFICATION.json",
)
P24_SOURCES = (
    f"{P24_DIR}/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md",
    f"{P24_DIR}/P24-ERCF3-SOURCE-FREEZE.json",
    f"{P24_DIR}/verify_p24_ercf3_proof_predicate_qualification.py",
    f"{P24_DIR}/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-VERIFICATION.json",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_runtime():
    spec = importlib.util.spec_from_file_location("cognition_runtime", ROOT / ".codex/tools/cognition_runtime.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_projection_edit():
    sys.path.insert(0, str(ROOT / "scripts/audit"))
    import projection_edit  # noqa: PLC0415
    return projection_edit


def core_headings() -> list[tuple[str, str]]:
    text = (ROOT / "核心认知.md").read_text(encoding="utf-8")
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", text, re.MULTILINE)
    assert len(headings) == 46
    return headings


def audit(core: dict) -> str:
    touched = {
        "KC-000025": ("DEEPENED", "自指问题被拆为对象语法、可表述性、反射、对角与自然消费者六桥。", "P24 report §3；若找到已闭合 S3–S6 的目标系统则改判。"),
        "KC-000026": ("DEEPENED", "P24 没有假定 HoTT 可越过自身自指；只检查该问题在固定代码中尚未被对象化。", "P24 report §§3、8；实际对象层反射定理或 consumer 是反证条件。"),
        "KC-000027": ("TENSION", "一般 Gödel/程序界限有外部正控制，但 P24 没有找到 HoTT 的实际同层消费者。", "P24 report §§4、8；P25 的真实调用链或其缺失决定后续。"),
        "KC-000028": ("DEEPENED", "有限检查、proof predicate、整体自证和可能的不闭合被逐桥区分，避免把其中任何一项说成运行回环。", "P24 report §§1–3；P25 需检查版本固定实现。"),
        "KC-000029": ("DEEPENED", "理论经济只作为可能的解释坐标；本轮没有把它当成实际 consumer 的证据。", "P24 report §§5、8；出现同任务经济化承诺才可加强。"),
        "KC-000035": ("DEEPENED", "HoTTLean 是语法—检查器—模型的相邻工程，显示表达研究与同层自证是不同任务。", "P24 report §4.2；P25 审计其源码与层级。"),
        "KC-000036": ("DEEPENED", "研究 Gödel需对象编码、可证明性条件与层级；P24 精确登记这些尚未闭合。", "P24 report §§3–4；不能由普通对角化跳到 HoTT 结论。"),
        "KC-000041": ("ALIGNED", "本单元把 AI 的检索能力同本地源码、保存 run 与一手资料交叉，未把语言模型生成当作判词。", "P24 source freeze；外部报告和源码可推翻。"),
        "KC-000043": ("CORRECTED", "以当前来源和固定规格反抗训练先验：不把名称为 repr 的构造子当作可证明性定理。", "P24 report §3；完整语义桥或实际 consumer 会改变。"),
        "KC-000044": ("DEEPENED", "本轮没有否认理论的现实解释可能性；只保留现实/同任务桥尚未建立的状态。", "P24 report §8；P25 的真实任务承诺是反证条件。"),
        "KC-000045": ("DEEPENED", "理论—现实对齐需要实际 Input/Operation/Observation/Done；P24 未将元理论层级差异误称现实失配。", "P24 report §§2、5；同任务调用链可改变。"),
        "KC-000046": ("DEEPENED", "本轮将全局自证和有限检查区分，并把 P25 设计为现实可解释的实际系统审计，而非仅停留于口号。", "P24 report §§5–6；未来实际 consumer 是反证条件。"),
    }
    body = f"# {SID} 核心认知回评\n\n{core['generation']}；46 条。兼容单文件格式：`G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001` 仍登记，不能冒充分片审计已原子化。\n\n"
    body += "- core_change: NO\n- direction_change: P23/P24 completed; P25 HoTTLean source denominator selected.\n- panorama_change: P24 object-level proof-predicate bridge and natural-consumer boundary recorded.\n- essay_change: NO\n- update_decision: close the exact ERCF3 source denominator and advance to P25 without reopening parked branches.\n- cross_conflicts: no actual HoTT self-verification consumer or HoTT defect established.\n- unresolved: P25 source audit; S3–S6 bridge and reality-task connection remain open.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n"
    body += "| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc, title in core_headings():
        relation, assessment, evidence = touched.get(
            kc,
            ("NOT_TOUCHED", "P24 没有直接检验这条用户原文；不以本地 bridge 审计替代它。", "P25 的不同源/任务或新的用户直接原文才触及。"),
        )
        body += f"| `{kc}` | {title} | `{relation}` | {assessment} | {evidence} |\n"
    body += "\n## 波次定位\n\nP24 在 P2/ERCF3 规则—对象理论桥上，拆开证明谓词、反射与自然消费者；其价值是阻止把编码正控制误报为同层自证。P25 将检验外层化的 HoTTLean 真实 syntax/checker/model 路径；若它仍保持层级边界，则关闭该分母并生成新的 successor。\n"
    return body


def result_record(path: str, evidence: str, related: list[str], scope: str, sources: tuple[str, ...]) -> dict:
    return {
        "kind": "result",
        "path": path,
        "lifecycle_status": "CURRENT",
        "evidence_status": evidence,
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": related,
        "full_sources": list(sources),
        "source_hashes": {source: sha256(ROOT / source) for source in sources},
        "scope": scope,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    runtime = load_runtime()
    edit = load_projection_edit()
    required = [*P23_SOURCES, *P24_SOURCES, "goal-3.md"]
    assert all((ROOT / item).is_file() for item in required)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 239
    assert state["latest_session"] == "S-RES-20260921-ASTRA-P21-CROSS-BRANCH-SYNTHESIS"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8"))
    assert all(sha256(ROOT / path) == expected for path, expected in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN])
    (OUT / "P24-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))

    state["revision"] = 240
    state["latest_session"] = SID
    portfolio = state["records"][PLAN]
    portfolio["related_records"] = list(dict.fromkeys(portfolio.get("related_records", []) + [P23, P24, SID]))
    portfolio["status"] = "four_track_p3_paused_p1_expression_p4_not_triggered_p22_parked_p25_hottlean_next"
    portfolio["evidence_status"] = (
        "P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / "
        "P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / P22_GUARDED_BRIDGE_PARKED / "
        "P24_OBJECT_LEVEL_PROVABILITY_BRIDGE_NOT_ESTABLISHED / "
        "P25_HOTTLEAN_MLTT_SYNTAX_SEMANTICS_CANDIDATE_NEXT / GOAL_ACTIVE"
    )
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(P23_SOURCES) + list(P24_SOURCES)))
    portfolio["source_hashes"].update({source: sha256(ROOT / source) for source in portfolio["full_sources"] if (ROOT / source).is_file()})
    portfolio["revalidation"] = (portfolio.get("revalidation", "") +
        " Revision240 records P23/P24 ERCF3 bridge qualification and selects version-pinned HoTTLean P25; prior P19–P22 scopes unchanged.")
    state["records"][P23] = result_record(
        P23_SOURCES[0],
        "SUCCESSOR_SELECTED / ERCF3_PROOF_PREDICATE_REPRESENTABILITY_AND_NATURAL_CONSUMER_CANDIDATE / P24_COMPLETED / NO_NEW_HOTT_DEFECT_CLAIM",
        [PLAN, P24, SID],
        "P23 selects the ERCF3 qualification task; it is not a HoTT theorem or defect.",
        P23_SOURCES,
    )
    state["records"][P24] = result_record(
        P24_SOURCES[0],
        "CLOSE_WITH_SCOPE / OBJECT_LEVEL_PROVABILITY_BRIDGE_NOT_ESTABLISHED / NATURAL_SELF_VERIFICATION_CONSUMER_NOT_ESTABLISHED_WITHIN_P24_DENOMINATOR / EXTERNAL_KNOWN_ANALOGUES_IDENTIFIED / P25_HOTTLEAN_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM",
        [PLAN, P23, SID],
        "P24 is a source-level qualification of fixed ERCF3 assets and selected public sources; it makes no mathematical or HoTT-defect conclusion.",
        P24_SOURCES,
    )
    state["records"][SID] = {
        "kind": "session",
        "path": BASE + "SESSION.md",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "P23_P24_CHECKPOINTED_WITH_SCOPE",
        "status": "complete_with_scope",
        "depends_on": [],
        "related_records": [PLAN, P23, P24],
        "full_sources": [BASE + name for name in ("SESSION.md", "RUNS.json", "CORE_COGNITION_AUDIT.md")],
    }
    state["execution_control"].update({
        "status": "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_P22_PARKED_P25_HOTTLEAN_NEXT",
        "current_phase": "PHASE_2_P24_ERC3_QUALIFIED_P25_HOTTLEAN_SOURCE_AUDIT_NEXT",
        "second_phase_status": "P3_PAUSED_P1_POSITIVE_CONTROL_P4_NOT_TRIGGERED_GUARD_PARKED_P25_NEXT",
        "last_checkpoint_session": SID,
        "checkpoint_result": f".codex/cognition/checkpoints/{SID}/result.json",
        "next_minimal_verification": (
            "P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-001. At fixed HoTTLean master "
            "31133dd5b25226ea897f8aa5e2e43b61392459eb, inspect the actual Syntax, Typechecker and Model "
            "entry points. Freeze Input/Operation/Observation/Done; determine whether a real object-level "
            "proof-predicate/reflection chain and a same-layer global self-verification consumer exist. "
            "Retain Lean-vs-object layering and current HIT scope; do not re-audit parked P3/P1/P4 branches."
        ),
    })
    state["projection"]["status"] = (
        "FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_GUARD_PARKED / "
        "P24_ERC3_BRIDGE_SCOPED / NEXT_P25_HOTTLEAN_SOURCE_AUDIT / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"
    )

    memory = edit.load(ROOT, "MEMORY.md")
    directions = edit.load(ROOT, "方向追踪.md")
    panorama = edit.load(ROOT, "全景视野.md")
    essay = edit.load(ROOT, "扩展认知.md")
    old_queue = (
        "P21已将P19–P22同步：P1最小结构可表达，P3同类consumer暂停，P4不因缺翻译触发，"
        "Guarded→bare桥停放待实际target。当前P23需选独立新入口并做公开/本地侦察；不重审停放分支。"
        "入口：`audit/p21-cross-branch-synthesis-20260921/P21-CROSS-BRANCH-SYNTHESIS-REPORT.md`；revision239。"
    )
    new_queue = (
        "P23/P24 已完成 ERCF3 独立入口与对象层 bridge qualification：修复编码是正控制，"
        "但 `Prov`→对象可表述性→反射→对角不动点及自然自验证消费者仍未建立。"
        "下一=P25：固定 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 审计 Syntax/Typechecker/Model 的实际层级与调用链；"
        "不重审 P3/P1/P4/Guard 停放分支。入口：`audit/p24-ercf3-proof-predicate-qualification-20260921/"
        "P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md`；revision240。"
    )
    edit.replace_in_shard(memory, "MEMORY/001 - 当前执行队列.md", old_queue, new_queue)
    edit.append_to_shard(memory, "MEMORY/003 - 当前验证状态与顺序日志.md", (
        "\nS-RES-20260921-ASTRA-P24-ERCF3-QUALIFICATION：P23/P24 已 checkpoint；固定 ERCF3 源码未建立对象层可证明性桥或自然同层自验证 consumer，"
        "Coquand 2026 为规格正控制，HoTTLean@31133dd5 为 P25 版本冻结候选；revision240。\n"
    ))

    edit.replace_in_index(directions, "source_state_revision: 239", "source_state_revision: 240")
    edit.replace_in_index(directions, "projection_generation: 20260921-direction-239", "projection_generation: 20260921-direction-240")
    edit.replace_in_index(directions, "semantic_status: FOUR_TRACK_P21_CONSOLIDATED_P23_NEXT", "semantic_status: FOUR_TRACK_P24_ERC3_BRIDGE_SCOPED_P25_HOTTLEAN_NEXT")
    old_direction = "| `DIR-U-HOTT-FOUR-TRACK` | P21综合：P3停放/P1正控制/P4未触发/Guard停放 | 反漂移综合 | `P23_INDEPENDENT_INGRESS_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | P19–P22 | P23选独立入口 | P21 report；revision239 |"
    new_direction = "| `DIR-U-HOTT-FOUR-TRACK` | P24：ERCF3对象层桥资格审计 | P23/P24独立入口 | `P25_HOTTLEAN_SOURCE_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | P19–P24 | P24局部缺口关闭，P25查真实层级/consumer | P24 report；revision240 |"
    edit.replace_in_shard(directions, "方向追踪/002 - 治理与用户方向.md", old_direction, new_direction)

    edit.replace_in_index(panorama, "source_state_revision: 239", "source_state_revision: 240")
    edit.replace_in_index(panorama, "projection_generation: 20260921-outcome-239", "projection_generation: 20260921-outcome-240")
    edit.replace_in_index(panorama, "semantic_status: FOUR_TRACK_P21_CONSOLIDATED_P23_NEXT", "semantic_status: FOUR_TRACK_P24_ERC3_BRIDGE_SCOPED_P25_HOTTLEAN_NEXT")
    old_outcome = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P21跨支综合 | `DIR-U-HOTT-FOUR-TRACK` | P19–P22 | `P3_PAUSED / P23_NEXT` | 表达性/桥缺口/guard分层 | 不证明缺陷 | P21 report；revision239 |"
    new_outcome = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P24 ERCF3对象层桥资格审计 | `DIR-U-HOTT-FOUR-TRACK` | P23/P24 | `P24_SCOPED / P25_NEXT` | 语法编码不等于对象可证明性/反射/consumer | 不证明HoTT缺陷 | P24 report；revision240 |"
    edit.replace_in_shard(panorama, "全景视野/003 - 当前机器证明包与原生重放.md", old_outcome, new_outcome)
    edit.append_to_shard(panorama, "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md", (
        "\n## P24：ERCF3 对象层证明谓词资格审计（revision240）\n\n"
        "P24 复用 C-181–C-183 的编码正控制，逐桥核对 `Prov`、`repr`、`Reflect`。固定源中没有从原 `Prov` 到对象层可表示性、反射或对角不动点的已证桥，也未见自然同层自验证 consumer。"
        "Coquand 2026 的 BRA 形式化是可证明性规格的正控制；HoTTLean 是 P25 的相邻版本冻结 syntax/checker/model 候选。"
        "判词 `CLOSE_WITH_SCOPE / NO_NEW_HOTT_DEFECT_CLAIM`。\n"
    ))
    edit.append_to_shard(panorama, "全景视野/008 - 当前未完成.md", (
        "\n7. `P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-001`：固定 HoTTLean 版本的对象 syntax、certifying typechecker、模型语义与同层自验证调用链审计；P24 只选择该候选，未重放其源码。\n"
    ))

    simple = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in runtime.MUTABLE if rel not in {runtime.STATE, "MEMORY.md", "方向追踪.md", "全景视野.md", "扩展认知.md"}}
    simple[runtime.PREFIX + "FRONTIER.md"] = simple[runtime.PREFIX + "FRONTIER.md"].replace(
        "- P21已同步：P3暂停、P1表达性正控制、P4未触发、Guard桥停放。P23选择独立新入口；不重审停放分支。入口：`audit/p21-cross-branch-synthesis-20260921/P21-CROSS-BRANCH-SYNTHESIS-REPORT.md`。",
        "- P24已关闭 ERCF3 本地对象层 bridge 分母：编码正控制存在，但 `Prov` 表示性、反射、对角不动点和自然同层自验证 consumer 均未建立。下一 P25 审计 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 的 Syntax/Typechecker/Model 层级；不重审停放分支。入口：`audit/p24-ercf3-proof-predicate-qualification-20260921/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md`。",
        1,
    )
    simple[runtime.PREFIX + "RESUME.md"] = simple[runtime.PREFIX + "RESUME.md"].replace(
        "当前 active goal 在P21后继续：P23选择一个独立版本冻结入口，做公开/本地侦察并固定Input/Operation/Observation/Done；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p21-cross-branch-synthesis-20260921/P21-CROSS-BRANCH-SYNTHESIS-REPORT.md`；revision239。",
        "当前 active goal 在P24后继续：P23/P24 已把 ERCF3 的对象语法、可证明性表示、反射、对角与 natural consumer 分开资格化；固定源码未闭合对象层 bridge。P25 审计 HoTTLean@`31133dd5b25226ea897f8aa5e2e43b61392459eb` 的 Syntax/Typechecker/Model 实际层级与调用链；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p24-ercf3-proof-predicate-qualification-20260921/P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md`；revision240。",
        1,
    )

    rows: list[dict] = []
    for doc in (memory, directions, panorama, essay):
        rows.extend(edit.payload_rows(doc, ROOT))
    seen = {row["path"] for row in rows}
    for rel in runtime.MUTABLE:
        if rel in seen:
            continue
        text = runtime.dump(state).decode("utf-8") if rel == runtime.STATE else simple[rel]
        rows.append({"path": rel, "expected_sha256": sha256(ROOT / rel), "text": text})

    session_text = f"""# {SID}

- host: codex-desktop
- model: runtime-model-not-certified-by-tool
- tier: T3
- status: `P23_P24_CHECKPOINTED_WITH_SCOPE / P25_HOTTLEAN_SOURCE_AUDIT_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`
- load_receipt: research plan snapshot `{plan['snapshot']}`; four-piece closure and P23/P24 sources rechecked before the checkpoint.
- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察与 checkpoint；不启动 Sub Agent、不 push、不发布。

## element_usage

| 元件 | 实际使用 | 未使用会拦住什么 | 未使用且无影响 |
|---|---|---|---|
| Goal 3 §2.1 | 是：P24 公开一手资料与版本 pin | 会把已知可证明性规格遗漏为“新发现” | — |
| Goal 3 §2.2 | 是：重用 ERCF3/P23/C-181–183 资产 | 会重复编码脉冲 | — |
| 四件套 | 是：P24 触及自反、理论经济、现实对齐主题 | 会失去用户目标边界 | — |
| F-011 | 是：没有升级任何数学命题 | 会混淆静态审计与数学证明 | — |
| P3/P4 audit trail | 未触发：P24不是前提实质判定 | 若执行P3/P4才需要 | 无影响于本次bridge资格审计 |
| Sub Agent | 未使用：项目明确禁止 | 禁止保护单写者与来源边界 | — |
"""
    runs = {
        "schema_version": "hott-session-runs/v1",
        "session_id": SID,
        "primary_runs": [
            {
                "kind": "P24 report verifier",
                "command": "python3 -B audit/p24-ercf3-proof-predicate-qualification-20260921/verify_p24_ercf3_proof_predicate_qualification.py",
                "result": "PASS_WITH_SCOPE",
            },
            {
                "kind": "public source pin read",
                "command": "git ls-remote https://github.com/sinhp/HoTTLean.git HEAD refs/heads/master and git ls-remote https://github.com/coquand/agda-godel-tree.git HEAD refs/heads/main",
                "result": "P25 and positive-control commits recorded in P24 source freeze",
            },
        ],
        "new_math_claims": [],
        "new_kernel_replay": False,
        "scope": "P24 is a source/consumer qualification, not a new proof package.",
    }
    rows.extend([
        {"path": BASE + "SESSION.md", "expected_sha256": None, "text": session_text},
        {"path": BASE + "RUNS.json", "expected_sha256": None, "text": runtime.dump(runs).decode("utf-8")},
        {"path": BASE + "CORE_COGNITION_AUDIT.md", "expected_sha256": None, "text": audit(state["current_core"])},
    ])
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SID,
        "load_profile": "research",
        "task_ids": [PLAN],
        "authorization": "用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。",
        "files": rows,
    }
    payload_path = OUT / "P24-CHECKPOINT-PAYLOAD.json"
    payload_path.write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan["snapshot"], payload, apply=args.apply)
    output = OUT / ("P24-CHECKPOINT-APPLY.json" if args.apply else "P24-CHECKPOINT-DRY-RUN.json")
    output.write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != "paths"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
