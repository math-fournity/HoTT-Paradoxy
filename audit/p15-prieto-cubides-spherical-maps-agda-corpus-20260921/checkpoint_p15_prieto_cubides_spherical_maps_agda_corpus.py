#!/usr/bin/env python3
"""Checkpoint the bounded P15 source audit and route P16."""
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
SID = "S-RES-20260921-ASTRA-P15-PRIETO-CUBIDES-CORPUS"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN_ID = "R-HOTT-FOUR-TRACK-PLAN-20260921"
ABX_ID = "R-ABX-ACTION-20260921"
P14_ID = "R-P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-20260921"
P15_ID = "R-P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-20260921"
REPORT = "audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-REPORT.md"
FREEZE = "audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SOURCE-FREEZE.json"
VERIFY = "audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/verify_p15_prieto_cubides_spherical_maps_agda_corpus.py"
RECEIPT = "audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-VERIFICATION.json"
CHECKPOINT = "audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/checkpoint_p15_prieto_cubides_spherical_maps_agda_corpus.py"
PLAN_VERIFY = "audit/four-track-plan-20260921/verify_four_track_plan.py"
PLAN_RECEIPT = "audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json"
SOURCES = (REPORT, FREEZE, VERIFY, RECEIPT, CHECKPOINT, PLAN_VERIFY, PLAN_RECEIPT,
           "HoTT后续研究总体方案.md", "HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md",
           "HoTT后续研究总体方案/005 - 当前第一步与交接.md", "goal.md", "goal-3.md",
           "feature-list.md", "rulings.md", "ABX行动.md", "ABX行动/005 - 状态、停止条件与未来交接.md",
           "audit/p14-ambient-operation-k-successor-discovery-20260921/P14-PRIETO-CUBIDES-CANDIDATE-FREEZE.json")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row(text: str, prefix: str, value: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            lines[i] = value
            return "\n".join(lines) + "\n"
    raise AssertionError(prefix)


def audit(core: dict[str, object]) -> str:
    headings = re.findall(r"^### (KC-\d+) · .*? · (.+)$", (ROOT / "核心认知.md").read_text(encoding="utf-8"), re.M)
    assert len(headings) == core["kc_count"] == 46
    top = f"""# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P15_EXPLICIT_STRUCTURE_DEFENSE_P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT
- panorama_change: VERSION_PINNED_PUBLISHED_SOURCE_AUDIT_NOT_A_CONSUMER_WITHIN_FIXED_PAGES
- essay_change: NO
- update_decision: P15 distinguishes an implicit ambient surface from loss of the task-bearing combinatorial Map/Face/Walk data; the fixed source does not instantiate bare-H-to-P13-Done.
- cross_conflicts: P15's use of equivalence compares two spherical specifications at the same explicit Map M; it is not a statement that P13 M/N are an operation-complete task.
- unresolved: P16 candidate selection, an actual K, a theory-rule bridge, a theory–implementation discrepancy, and any HoTT-defect conclusion remain open.
- writer_compatibility: `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`; complete legacy 46-KC single-file audit accepted by current runtime.

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
"""
    touched = {5, 10, 15, 21, 22, 35, 37, 38, 39, 40, 44, 45, 46}
    for n, (kc, topic) in enumerate(headings, 1):
        if n in touched:
            relation = "DEEPENED"
            judgement = "P15以实际发布的Agda模块检验结构是否被忽略；明确Map/Face/Walk/spherical参数阻止把相邻isotopy主题自动读成原圆环K。"
            evidence = f"{REPORT}；P16若找到bare H到P13 Done的真实调用链才改变判词。"
        else:
            relation = "NOT_TOUCHED"
            judgement = "本单元只审计固定P15来源，不新增数学定理。"
            evidence = "无原生核重放、无HoTT缺陷结论。"
        top += f"| `{kc}` | {topic} | {relation} | {judgement} | {evidence} |\n"
    return top + """

## 扩展认知逐片复认

001–008：P15遵循“现实对齐先固定任务”的工作姿态。抽象的surface implicit不能替代输入、操作、观察和Done的逐项比较；结构保留证据必须计入正控制。

## 波次定位

1. **最终目标连接：** P15在实际HoTT相关消费者中检验了P13 operation-sensitive合同，排除了一个具体的bare-H-to-Done候选。
2. **全局坐标：** P3 K_app的固定source-audit；P4未触发。
3. **实际价值：** 将论文标题层的isotopy邻接细化为可见Map/Face/Walk/Spherical输入输出证据。
4. **继续：** P16必须在新来源重新做公开及本地侦察，避免重复此语料。
5. **停止：** 停止P15的五页分母，不停止active goal。
6. **裁决：** `CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P16`。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    subprocess.check_call([sys.executable, "-B", VERIFY, "--write"], cwd=ROOT)
    subprocess.check_call([sys.executable, "-B", PLAN_VERIFY, "--write"], cwd=ROOT)
    assert all((ROOT / p).is_file() for p in SOURCES)
    spec = importlib.util.spec_from_file_location("runtime", ROOT / ".codex/tools/cognition_runtime.py")
    runtime = importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding="utf-8"))
    assert state["revision"] == 234 and state["latest_session"] == "S-RES-20260921-ASTRA-P14-AMBIENT-OPERATION-K-DISCOVERY"
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding="utf-8")); assert all(sha(ROOT / p) == h for p, h in head["tracked"].items())
    plan = runtime.plan(ROOT, profile="research", task_ids=[PLAN_ID]); assert not plan["hydration_diagnostics"]["query_first_promoted"]
    (OUT / "P15-PRIETO-CUBIDES-CHECKPOINT-PLAN.json").write_bytes(runtime.dump(plan))
    previous = state["latest_session"]
    state["revision"] = 235; state["latest_session"] = SID
    for ident in (PLAN_ID, ABX_ID, P14_ID):
        rec = state["records"][ident]
        rec["related_records"] = list(dict.fromkeys(rec.get("related_records", []) + [P15_ID, SID]))
        paths = set(rec.get("full_sources", [])) | set(rec.get("source_hashes", {}))
        rec["source_hashes"].update({p: sha(ROOT / p) for p in paths if (ROOT / p).is_file()})
        rec["revalidation"] = rec.get("revalidation", "") + " Revision235 records P15's fixed-page source audit; prior result scope remains unchanged."
    portfolio = state["records"][PLAN_ID]
    portfolio.update(evidence_status="USER_DIRECTED_PORTFOLIO_PLAN / P15_NOT_A_CONSUMER_WITHIN_FIXED_PAGES / DEFENSE_EXPLICIT_MAP_FACE_WALK_SPHERICAL_DATA / P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT / GOAL_ACTIVE", status="four_track_p15_explicit_structure_defense_p16_next", scope="P15 is a published-source inspection of one version-pinned corpus, not a kernel replay, actual K, or HoTT defect.")
    portfolio["full_sources"] = list(dict.fromkeys(portfolio.get("full_sources", []) + list(SOURCES)))
    portfolio["source_hashes"].update({p: sha(ROOT / p) for p in portfolio["full_sources"] if (ROOT / p).is_file()})
    abx = state["records"][ABX_ID]
    abx.update(revalidation="Revision235: P15 fixed-page audit found explicit Map/Face/Walk/Spherical inputs and task difference; P16 must choose a new denominator.", scope="P15 gives no actual K within its fixed published pages; P16 successor discovery remains required.")
    abx["full_sources"] = list(dict.fromkeys(abx.get("full_sources", []) + list(SOURCES)))
    abx["source_hashes"].update({p: sha(ROOT / p) for p in abx["full_sources"] if (ROOT / p).is_file()})
    state["records"][P15_ID] = {"kind":"result","path":REPORT,"lifecycle_status":"CURRENT","evidence_status":"NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES / DEFENSE_EXPLICIT_MAP_FACE_WALK_SPHERICAL_DATA / TASK_DIFFERENT_FROM_P13_MN_DONE / P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM","status":"complete_with_scope_p16_fourth_successor_discovery_next","depends_on":[],"related_records":[PLAN_ID,ABX_ID,P14_ID,previous],"full_sources":list(SOURCES),"source_hashes":{p:sha(ROOT/p) for p in SOURCES},"scope":"P15 only reads the fixed author-published pages and paper abstract context; it does not prove global absence or replay Agda."}
    state["records"][SID] = {"kind":"session","path":BASE+"SESSION.md","lifecycle_status":"HISTORICAL","evidence_status":"P15_FIXED_PAGE_SOURCE_AUDIT_CHECKPOINTED_WITH_SCOPE","status":"complete_with_scope","depends_on":[],"related_records":[P15_ID,PLAN_ID,ABX_ID,previous],"full_sources":[BASE+n for n in ("SESSION.md","RUNS.json","CORE_COGNITION_AUDIT.md")]}
    state["execution_control"].update(status="FOUR_TRACK_P15_EXPLICIT_MAP_FACE_WALK_DEFENSE_P16_NEXT", current_phase="PHASE_2_P15_FIXED_PAGE_AUDIT_COMPLETE_P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT", second_phase_status="P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_TO_P15_COMPLETE_P16_NEXT", last_checkpoint_session=SID, checkpoint_result=f".codex/cognition/checkpoints/{SID}/result.json", next_minimal_verification="P16-FOURTH-SUCCESSOR-DISCOVERY-001. Perform a fresh bounded public/community and local/historical reconnaissance to select one unreviewed, version-pinned actual HoTT/cubical/related consumer denominator outside P2/P3/P8/P9/P11/P13/P15. Freeze exact input/operation/observation/Done and P7 admission rationale; do not re-audit Prieto-Cubides, compile, clone, or scan a whole site.")
    state["projection"]["status"] = "FOUR_TRACK_FIRST_PASS / P15_EXPLICIT_MAP_FACE_WALK_DEFENSE / NEXT_P16_FOURTH_SUCCESSOR_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM"
    drow = "| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P15实际语料审计与P16新分母发现 | 用户要求每wave做外部与本地侦察 | `P15_EXPLICIT_MAP_FACE_WALK_DEFENSE / NEXT_P16_FOURTH_SUCCESSOR_DISCOVERY / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P15 | P16重选版本冻结实际消费者分母 | `HoTT后续研究总体方案.md`；P15 report；revision235 receipt |"
    arow = "| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P15显式结构防御后的P16发现 | H/R/K、P1–P15 | `NO_K_IN_FIXED_P15_PAGES / NEXT_P16_FOURTH_SUCCESSOR_DISCOVERY` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P15 | P16选择新实际消费者，避免重审 | `ABX行动.md`；P15 report；revision235 receipt |"
    prow = "| `OUT-HOTT-FOUR-TRACK-PLAN` | P15 Prieto-Cubides固定页面实际语料审计 | `DIR-U-HOTT-FOUR-TRACK` | P13 Done、论文与五个发布模块 | `NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES / P16_NEXT` | Map/Face/Walk/Spherical显式，任务不同 | 不证明全局无K、Agda重放或HoTT缺陷 | `audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-REPORT.md`；revision235 receipt |"
    aprow = "| `OUT-ABX-ACTION-INTAKE` | ABX P15固定页面K_app审计 | `DIR-U-ABX-ORIGINAL-CIRCLE` | explicit Map/Face/Walk/Spherical vs P13 bare H/Done | `NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES / P16_NEXT` | 结构保留、任务不同 | 不证明传统同胚错误、真实K或HoTT缺陷 | `ABX行动.md`；P15 report；revision235 receipt |"
    memory = "P15固定 Prieto-Cubides 页面审计已完成：Map/Face/Walk/Spherical数据均显式，且组合图嵌入任务不是P13 M/N operation-sensitive Done；该固定分母是NOT_A_CONSUMER，不是active goal停止条件。当前P16重新做公开/本地侦察，选择一个未审版本冻结实际消费者分母；不重审P15页面。入口：`audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-REPORT.md`；revision235 checkpoint。"
    frontier = "- P15已完成：Prieto-Cubides固定五页显式保留Map/Face/Walk/Spherical，且任务不同于P13 M/N Done；它不是K。当前P16重新选择一个未审版本冻结实际消费者分母，不重审此语料。入口：`audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-REPORT.md`。"
    resume = "当前 active goal 在P15后继续：P15固定页面分母给出显式Map/Face/Walk/Spherical防御和任务不同判词。P16=FOURTH_SUCCESSOR_DISCOVERY：重新做公开/本地侦察，选择一个未审版本冻结实际消费者，固定Input/Operation/Observation/Done与P7准入；不重审Prieto-Cubides、不克隆/编译/全站扫描。入口：`audit/p15-prieto-cubides-spherical-maps-agda-corpus-20260921/P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-REPORT.md`；revision235 checkpoint。"
    files=[]
    for rel in list(runtime.MUTABLE)+list(runtime.mutable_shard_paths(ROOT)):
        raw=(ROOT/rel).read_bytes(); text=raw.decode("utf-8")
        if rel==runtime.STATE: text=runtime.dump(state).decode("utf-8")
        elif rel==runtime.DIRECTION: text=text.replace("source_state_revision: 234","source_state_revision: 235",1).replace("projection_generation: 20260921-direction-234","projection_generation: 20260921-direction-235",1).replace("semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_PRIETO_CUBIDES_CANDIDATE_SELECTED_P15_NEXT","semantic_status: FOUR_TRACK_P15_EXPLICIT_MAP_FACE_WALK_DEFENSE_P16_NEXT",1)
        elif rel==runtime.PANORAMA: text=text.replace("source_state_revision: 234","source_state_revision: 235",1).replace("projection_generation: 20260921-outcome-234","projection_generation: 20260921-outcome-235",1).replace("semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_COQHOTT_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_PRIETO_CUBIDES_CANDIDATE_SELECTED_P15_NEXT","semantic_status: FOUR_TRACK_P15_EXPLICIT_MAP_FACE_WALK_DEFENSE_P16_NEXT",1)
        elif rel=="方向追踪/002 - 治理与用户方向.md": text=row(row(text,"| `DIR-U-HOTT-FOUR-TRACK` |",drow),"| `DIR-U-ABX-ORIGINAL-CIRCLE` |",arow)
        elif rel=="全景视野/003 - 当前机器证明包与原生重放.md": text=row(row(text,"| `OUT-HOTT-FOUR-TRACK-PLAN` |",prow),"| `OUT-ABX-ACTION-INTAKE` |",aprow)
        elif rel=="MEMORY/001 - 当前执行队列.md": text=row(text,"P14实际消费者 successor discovery 已完成：",memory)
        elif rel=="MEMORY/003 - 当前验证状态与顺序日志.md": text += "\nS-RES-20260921-ASTRA-P15-PRIETO-CUBIDES-CORPUS：P15完成。固定页面显式保留Map/Face/Walk/Spherical且任务不同于P13 Done；P16重选新分母；revision235 checkpoint。\n"
        elif rel==runtime.PREFIX+"FRONTIER.md": text=row(text,"- P14已完成：",frontier)
        elif rel==runtime.PREFIX+"RESUME.md": text=row(text,"当前 active goal 在P14后继续：",resume)
        files.append({"path":rel,"expected_sha256":runtime.sha(raw),"text":text})
    session=f"# {SID}\n\n- host: Codex desktop local\n- tier: T3 state mutation for P15 fixed-page source audit\n- status: COMPLETED_WITH_SCOPE / NOT_A_CONSUMER / P16_NEXT\n\nP15 inspected only the frozen author-published pages and paper context. It did not compile Agda or establish a HoTT theorem.\n"
    runs={"schema_version":"hott-session-runs/v1","session_id":SID,"primary_runs":[{"kind":"p15-fixed-page-source-audit","result":"PASS_WITH_SCOPE; explicit structure defense; P16 routed","mathematics":"NO_NEW_KERNEL_RUN"}],"new_math_claims":[],"new_kernel_replay":False}
    for name,text in (("SESSION.md",session),("RUNS.json",runtime.dump(runs).decode("utf-8")),("CORE_COGNITION_AUDIT.md",audit(state["current_core"]))): files.append({"path":BASE+name,"expected_sha256":None,"text":text})
    payload={"schema_version":"cognition-checkpoint/v1","session_id":SID,"load_profile":"research","task_ids":[PLAN_ID],"authorization":"用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。","files":files}
    (OUT/"P15-PRIETO-CUBIDES-checkpoint-payload.json").write_bytes(runtime.dump(payload))
    result=runtime.checkpoint(ROOT,plan["snapshot"],payload,apply=args.apply)
    (OUT/("P15-PRIETO-CUBIDES-checkpoint-apply.json" if args.apply else "P15-PRIETO-CUBIDES-checkpoint-dry-run.json")).write_bytes(runtime.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!="paths"},ensure_ascii=False))


if __name__ == "__main__":
    main()
