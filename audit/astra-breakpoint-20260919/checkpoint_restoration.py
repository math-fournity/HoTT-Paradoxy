#!/usr/bin/env python3
"""Checkpoint the restoration evidence and remaining full-goal obligations."""
import argparse
import importlib.util
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SID="S-RES-20260919-ASTRA-POINT-RESTORATION"
BASE=".codex/research/hott/sessions/"+SID+"/"
REPORT="Astra继续尝试/断点与证明机制系统检查/第二轮执行报告.md"
spec=importlib.util.spec_from_file_location("r",ROOT/".codex/tools/cognition_runtime.py");R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)

# Semantic choices are authored here, not inferred from text similarity.
TOUCHED={
1:("ALIGNED","问题固定为自然恢复及其输入条件；不以新公式替代研究目标。"),
2:("DEEPENED","任意Type、QCircle集合层与HIT圆分别检查；不混用删点语义。"),
5:("ALIGNED","同时构造恢复与反向控制，由实际结果决定解释。"),
6:("ALIGNED","函数构造未被提升为物理时间或运动的完成。"),
7:("ALIGNED","知识提出候选，原生内核核其精确类型，未由模型自述认证。"),
10:("ALIGNED","保留现实相对目标；既不强迫内部矛盾，也不把表示差异当完成。"),
12:("DEEPENED","从实际decode分支反推出PointDecidable，而非随意附加前提。"),
13:("DEEPENED","指定点已知与任意点可分类分开；检查所需实际输出。"),
14:("ALIGNED","类型对象、逆函数和可执行物理交付仍分层。"),
15:("TENSION","本轮展示一个原生合法恢复，不能支持抽象必然失败的全称读法；回到实际拓扑/动作合同。"),
17:("ALIGNED","最强恢复作为真实实现进入，未因期待否定HoTT而排除。"),
21:("ALIGNED","三个主包、显式safe聚合和一份失败均落盘；F-011全局失败保持公开。"),
22:("ALIGNED","A/B都保留；Q恢复不直接消除实际过程问题，HIT拒绝不直接证明B越级。"),
31:("DEEPENED","条件接口和具体非有限QCircle实例接通，HIT实例的否定具有精确类型。"),
34:("ALIGNED","正构造、否定规格、实现名冲突与门禁失败分别报告。"),
35:("DEEPENED","表达了自然恢复及其完整读出条件，但没有宣称完整表达用户的现实复原理论。"),
37:("TENSION","圆环直觉尚未成为目标反例；已离开纯Bool控制，但实数拓扑与操作仍OPEN。"),
38:("TENSION","未定位作者的同规格错误；恢复和HIT控制不构成对基础HoTT的否定。"),
39:("TENSION","发现侧仍未命中；下轮必须修证据连接/具体几何，不能重复同形小命题。"),
40:("ALIGNED","从先前结果产生恢复逆向分类这一新义务，并用实际源码核验。"),
41:("ALIGNED","AI形式化能力用于实际构造，名冲突失败完整记录。"),
42:("ALIGNED","不把容易实现的Q模型当用户真实圆环模型。"),
43:("ALIGNED","停止追加同形Boolean控制，将下一步转向证据接线及真实拓扑。"),
44:("ALIGNED","保留现实/假想现实的模型意义；缺少现成实数库不作为问题无效的理由。"),
45:("DEEPENED","自然包含与原指定点实际被使用；同任务所需拓扑没有被名字抹去。"),
46:("ALIGNED","实际执行恢复构造，但未将函数返回当物理操作；继续具名拓扑任务。"),
}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--apply",action="store_true");a=ap.parse_args()
    p=R.plan(ROOT,profile="research");assert p["revision"]==175
    state=json.loads((ROOT/R.STATE).read_bytes());state["revision"]=176;state["latest_session"]=SID
    state["records"][SID]={"kind":"session","path":BASE+"SESSION.md","lifecycle_status":"HISTORICAL","evidence_status":"KERNEL_RUNS_ACCEPTED / FULL_MATH_DELIVERY_PARTIAL","status":"complete","depends_on":[],"related_records":["S-PLAN-20260919-ASTRA-CONTINUING-GOAL"],"full_sources":[BASE+"SESSION.md",BASE+"RUNS.json",BASE+"CORE_COGNITION_AUDIT.md"]}
    state["records"]["R-ASTRA-POINT-RESTORATION-20260919"]={"kind":"result","path":REPORT,"lifecycle_status":"CURRENT","evidence_status":"NATIVE_RUNS_ACCEPTED / GEOMETRY_AND_GLOBAL_GATE_OPEN","status":"unit_executed_with_scope","depends_on":[],"related_records":[SID,"R-ASTRA-BREAKPOINT-20260919"],"full_sources":[REPORT,"audit/astra-breakpoint-20260919/restoration-delivery-verification.json"],"scope":"Natural point restoration and pointwise decision criterion; concrete rational point-set instance; HIT path-complement countercontrol. No topology or physical-operation completion."}
    issue="G-ASTRA-PROOF-EVIDENCE-WIRING-001"
    state["records"][issue]={"kind":"issue","path":"Astra继续尝试/断点与证明机制系统检查/第二轮执行报告/003 - 源码、运行、校验与失败索引.md","lifecycle_status":"OPEN_ISSUE","evidence_status":"REPRODUCED","status":"open","depends_on":[],"related_records":[SID],"full_sources":["audit/astra-breakpoint-20260919/restoration-delivery-verification.json"],"scope":"Frozen-prefix insertion, legacy CAND registry parsing, and external Cubical tree coverage in package-relation verifier. Keep failures; fix without weakening identity/hash/import checks."}
    ec=state["execution_control"];ec["status"]="ASTRA_POINT_RESTORATION_EXECUTED_FULL_GOAL_ACTIVE";ec["last_checkpoint_session"]=SID;ec["checkpoint_result"]=".codex/cognition/checkpoints/"+SID+"/result.json"
    ec["next_minimal_verification"]="先按治理自维护闭包修复G-ASTRA-PROOF-EVIDENCE-WIRING-001的精确三处证据关系，并回归正负样例，不改数学命题或历史失败；随后资格化实际实数拓扑圆/开区间与端部模型，补GEO-01至04。断点检查未整体完成；继续完整四弹U00–U09与G01–G06，线程Goal保持ACTIVE。自然恢复单元的具体结果见"+REPORT
    for rec,kind in [("I-DIRECTION-PORTFOLIO-20260912","direction"),("I-OUTCOME-PANORAMA-20260912","outcome")]:state["records"][rec]["projection_generation"]="20260919-"+kind+"-176"
    session=f"""# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证后端路由
- tier: T3 research and state mutation
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_GOAL
- load_receipt: audit/astra-breakpoint-20260919/tracking-recovery/LOAD-RECEIPT-final.json；本轮175计划事务后的同档复认
- status: BP-GEO-RESTORE-01_EXECUTED / FULL_GOAL_ACTIVE / GLOBAL_DELIVERY_GATE_PARTIAL

当前Goal完整原文在四弹策略010且与get_goal逐字一致。先完成策略v1.1补入、本地精确commit7900d644及175真实checkpoint，随后执行本构造；未push/tag。首次完整T3加载与本轮hash/KC/原文抽查连续，core generation7/46KC不变。新Goal优先于旧SUPPLY队列；不使用Sub Agent。

## 具体构造

PointRestoration检查对任意C,p的自然extend之右逆与pointDecision两方向，以及给定decision构造Iso；没有额外isSet C假设。RationalRestoration实际从discreteℚ构造QCircle的decision，并检查包含、指定点与ua运输。HomotopyRestorationControl对HIT S¹的内部路径排除检查noSplit/noDecision。三个主run接受且formal verifier通过；显式safe聚合142源码通过；一次extend名冲突失败及修复前源码保留。C-261–C-264、三个包、五次运行分别计数。
本单元未构造实数拓扑、同胚或物理Trace。不能把和类型自动赋不相交并拓扑，也不能默认为从C运输的拓扑。原始M/N任务与完整四弹仍未完成。新结果是运行事实与精确规格，不越过仍失败的完整交付门禁。

## 证据与下一动作

owner={REPORT}；catalogue=restoration-claim-catalogue.json；verify=restoration-delivery-verification.json。数学/说明/依赖源文件不改旧run；内核失败不是理论反例。下一动作先处理已反复复现的证据关系实现问题，再接真实拓扑模型；保持当前Goal全部范围，不标complete或blocked。

## 影响与元件

closure/receipt复认保持当前来源；研究Skill驱动双向构造与实际实例；verification保留失败、safe资格与导入哈希；SOP要求前一方案版本先记录再执行；canonical checkpoint只登记事实。T01–10是具体任务/接口澄清，不更改用户哲学；T11–17为三原生源与五run及验证；T18–21不部署；T22–24更新对应owner；T25不改AI机制；T26精确本地版本纪律、保留其他AI路径。按PROTOCOL §5兼容legacy完整KC审计，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001未被假称关闭。
"""
    headings=re.findall(r"^### (KC-\d+) · .*? · .*? · (.+)$",(ROOT/"核心认知.md").read_text(),re.M);assert len(headings)==46
    audit=f"# {SID} 核心认知审计\n\ncore-cognition-generation-7；46条，沿原顺序。\n\n- core_change: NO\n- direction_change: NATURAL_RESTORE_EXECUTED_NEXT_GATE_AND_GEOMETRY\n- panorama_change: ADD_RESTORATION_RUN_FACTS\n- essay_change: NO\n- update_decision: 更新实际构造，保持完整Goal未完成。\n- cross_conflicts: 数学run接受与包关系/全局gate失败分别记录。\n- unresolved: 实数拓扑、允许动作、同任务桥梁与证据关系。\n\n| KC | 主题 | relation | 姿态、实际动作及理由 | 证据、下一选择与反证条件 |\n|---|---|---|---|---|\n"
    for n,(kc,title) in enumerate(headings,1):
        rel,why=TOUCHED.get(n,("NOT_TOUCHED","本轮未处理该具体时间、自指、计算或元理论问题；自然恢复构造不能代替它。"))
        nxt="第二轮报告001–004、三源码及五run；如拓扑/原动作模型出现保真恢复或同规格反例则重评；任何哈希/类型不符先撤回对应证据。" if n in TOUCHED else "第二轮报告004的覆盖范围；取得该主题具名形式规格或新直接证据时再进入，不据当前未触及作否定。"
        audit+=f"| `{kc}` | {title} | {rel} | {why} | {nxt} |\n"
    audit+="""
## 扩展认知逐节回评

001问题发生/简化：从原指定点恢复提出可执行问题，取得逆向判定条件；未预定否定。002改变前提：实际decode消费条件；时间节NOT_TOUCHED物理模型。003圆环：QCircle恢复真实接通但拓扑OPEN；ASK：源、点、决策区分；A/B：函数取得不代替物理完成。004走进HoTT：原生类型与HIT分层；自反NOT_TOUCHED。005表达界限：实际实例比接口前进一步；文章起点：把结果回写策略；原文保全：保持44条历史快照与Goal原文，未补造当前final。006知识谱：自然恢复的反向必要条件是新unknown入口；007助力阻力：不因实现顺利便把有理对象当实圆；008现实骨架：继续拓扑/环境/动作/Done，理论结构与现实解释分开。任何保真反例或恢复都会改变候选，不改用户原文。

## 已走过的路

新增自然恢复的两个方向及实际Q实例，区别于首轮仅给删点后的一个元素；HIT对照沿原定义复用非平凡路径，并保留一次实现失败。父目标的模型连接有所推进，原现实任务仍未被完整表达，未命中HoTT缺陷。证据gate保持三处已复现阻塞，不掩盖。

## 即将作出的选择

继续增加一般恢复玩具例子收益低，拒绝。选择先修精确证据接线，再资格化实际拓扑；这支持KC21/35/37/39/43/44–46，并防止无最终可交付证明的堆积。风险是治理替代发现，因此修复只限三处直接失败及必要负对照，结束立即回GEO。通用“所有set都可分类”的逻辑强度可作为unknown ingress，但不能取代当前实际圆环义务。无无限穷举/无全理论负结论；原Goal保持ACTIVE。
"""
    runs={"schema_version":"hott-session-runs/v1","session_id":SID,"packages":"audit/astra-breakpoint-20260919/restoration-claim-catalogue.json","validation":"audit/astra-breakpoint-20260919/restoration-delivery-verification.json","kernel_accepted_primary_packages":3,"claim_specifications":4,"new_runs":5,"full_delivery_gate":"PARTIAL","parent_goal":"ACTIVE_NOT_COMPLETE"}
    files=[]
    for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
        b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r"(?m)^source_state_revision: 175$","source_state_revision: 176",body);assert n==1
            kind="direction" if rel==R.DIRECTION else "outcome"
            body,n=re.subn(r"(?m)^projection_generation: .+$","projection_generation: 20260919-"+kind+"-176",body);assert n==1
        if rel=="MEMORY/001 - 当前执行队列.md":
            start=body.index("用户本线程持续Goal");end=body.index("\n\n",start)
            body=body[:start]+"用户本线程持续Goal仍ACTIVE，先完成断点检查，再完成不断更新的四弹策略，禁止缩为小控制。第二轮BP-GEO-RESTORE-01已运行：自然恢复/可判定条件、QCircle实例、HIT对照，3主包/4规格/5运行；C-261–C-264及报告 `"+REPORT+"` 可复核。实数拓扑、动作许可、同任务桥梁及完整proof gate均未完成。当前下一项是G-ASTRA-PROOF-EVIDENCE-WIRING-001三处精确证据关系修复，随即回GEO真实拓扑；旧SUPPLY/Gödelrecord保留但非本线程当前动作。"+body[end:]
        if rel=="方向追踪/002 - 治理与用户方向.md":
            ls=body.splitlines()
            for n,line in enumerate(ls):
                if line.startswith("| `DIR-U-ASTRA-BREAKPOINT` |"):
                    ls[n]="| `DIR-U-ASTRA-BREAKPOINT` | 先完成断点检查，再推进持续更新的四弹完整策略 | 用户本线程持续Goal | `ACTIVE_GOAL / RESTORATION_UNIT_EXECUTED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02` | 修复精确证据关系后回真实拓扑/动作保真，所有GEO/U/G义务保留 | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |"
            body="\n".join(ls)+"\n"
        if rel=="全景视野/003 - 当前机器证明包与原生重放.md":body=body.rstrip()+"\n| `OUT-ASTRA-RESTORATION-02` | 自然指定点恢复、逆向可判定条件、QCircle实例和HIT对照 | `DIR-U-ASTRA-BREAKPOINT` | 三个原生源码包与五运行 | `KERNEL_RUNS_ACCEPTED / GLOBAL_GATE_PARTIAL` | 固定规格的内核接受、原包含及ua运输检查 | 实数拓扑、同胚、物理复原、HoTT缺陷或总Goal完成 | `"+REPORT+"`；`audit/astra-breakpoint-20260919/restoration-delivery-verification.json` |\n"
        files.append({"path":rel,"expected_sha256":R.sha(b),"text":body})
    for name,body in [("SESSION.md",session),("RUNS.json",R.dump(runs).decode()),("CORE_COGNITION_AUDIT.md",audit)]:files.append({"path":BASE+name,"expected_sha256":None,"text":body})
    payload={"schema_version":"cognition-checkpoint/v1","session_id":SID,"load_profile":"research","task_ids":[],"authorization":"用户持续Goal：据结果更新策略、持续执行完整范围并维护治理状态。","files":files}
    (OUT/"restoration-checkpoint-payload.json").write_bytes(R.dump(payload))
    result=R.checkpoint(ROOT,p["snapshot"],payload,apply=a.apply)
    (OUT/("restoration-checkpoint-apply.json" if a.apply else "restoration-checkpoint-dry-run.json")).write_bytes(R.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!="paths"},ensure_ascii=False))

if __name__=="__main__":main()
