#!/usr/bin/env python3
"""Register the user's complete continuing objective before its next construction."""
import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SID="S-PLAN-20260919-ASTRA-CONTINUING-GOAL"
BASE=".codex/research/hott/sessions/"+SID+"/"
PLAN="Astra继续尝试/四弹一体完整研究策略.md"
SPEC="Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md"
s=importlib.util.spec_from_file_location("runtime",ROOT/".codex/tools/cognition_runtime.py");R=importlib.util.module_from_spec(s);s.loader.exec_module(R)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--apply",action="store_true");a=ap.parse_args()
    p=R.plan(ROOT,profile="research");assert p["revision"]==174
    state=json.loads((ROOT/R.STATE).read_bytes());old=state["latest_session"]
    state["revision"]=175;state["latest_session"]=SID
    state["records"][SID]={"kind":"session","path":BASE+"SESSION.md","lifecycle_status":"HISTORICAL","evidence_status":"PLAN_INTEGRATED / NO_NEW_MATH_CLAIM","status":"complete","depends_on":[],"related_records":[old],"full_sources":[BASE+"SESSION.md",BASE+"RUNS.json",BASE+"CORE_COGNITION_AUDIT.md"]}
    aid="A-ASTRA-CONTINUING-GOAL-20260919"
    state["records"][aid]={"kind":"activity","path":SPEC,"lifecycle_status":"ACTIVE_WORK","evidence_status":"USER_AUTHORIZED / FULL_OBJECTIVE_UNFINISHED","status":"active","depends_on":[],"related_records":["R-ASTRA-BREAKPOINT-20260919",SID],"full_sources":[PLAN],"scope":"Complete the breakpoint plan, continuously update and then execute the complete four-stage strategy. No substitution of bounded controls for the final outcome."}
    state["active"]=[aid]+state["active"]
    ec=state["execution_control"]
    ec["status"]="ASTRA_CONTINUING_GOAL_PLAN_INTEGRATED"
    ec["last_checkpoint_session"]=SID
    ec["checkpoint_result"]=".codex/cognition/checkpoints/"+SID+"/result.json"
    ec["next_minimal_verification"]="当前用户线程Goal优先：执行BP-GEO-RESTORE-01，检验Puncture C p⊎Unit的自然恢复及逆向分类条件，在QCircle上实例化；不称实数拓扑/物理复原完成。继续补齐断点GEO-01至04与证据门禁后，再执行四弹AST-U00–U09剩余和AST-G01–G06完整验收。旧SUPPLY-010队列保留历史record，不是本线程当前动作。精确规格与全部剩余义务见"+SPEC
    for rec,kind in [("I-DIRECTION-PORTFOLIO-20260912","direction"),("I-OUTCOME-PANORAMA-20260912","outcome")]:state["records"][rec]["projection_generation"]="20260919-"+kind+"-175"
    session=f"""# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；后端路由未认证
- tier: T3 state mutation / research planning
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_GOAL
- user_objective: {SPEC} §1逐字原文；工具Goal仍ACTIVE
- load_receipt: audit/astra-breakpoint-20260919/tracking-recovery/LOAD-RECEIPT-final.json + 本轮hash/KC复认
- status: PLAN_SUPPLEMENT_INTEGRATED / FULL_GOAL_UNFINISHED

上一Goal单元为PROGRESS，有源码、28次运行与174真实事务。本轮先核当前Git40b1ca78、STATE174及tracked=0；core generation7/46KC/hash不变。52文档旧收据差异六处均由172–174已知事务解释，无新未知写者；重新读启动核、九片原策略、最新session与46KC审计、原文KC1–10，并复认其它KC，未触发core变化/升档/用户全文重载。
全量STATE与四件套的上轮全文收据仍适用；本次采用PROTOCOL v3同档复认，不用单纯hash冒充重新全文阅读。task query/plan共61文件，query_first_promoted为空。所读方法包括closure、governance、研究/执行SOP、verification及Git合同。

本轮先把v1.0仅设计的旧owner改为v1.1持续执行，增加010总Goal账本；没有新数学运行。下一构造必须检查实际恢复而不是重复Bool边界。数学证据仍GLOBAL_DELIVERY_GATE_PARTIAL。未宣称断点专题或四弹主目标完成。
用户持续Goal要求遵循项目执行/版本纪律；只保全本专题精确本地提交，不push/tag/发布，不纳入另一AI的审计目录。旧研究record保留；当前next_minimal_verification转为本线程Goal，原控制面保存在checkpoint before副本。

## element_usage

| 元件 | 作用 |
|---|---|
| closure/receipt | 当前HEAD/来源/46KC与既有全文收据复认 |
| 方案owner | 十片保留完整成功范围，逐项接入首轮证据而非缩目标 |
| canonical checkpoint | 新Goal接入先于下一构造；真实result为依据 |
| F-011 | 保持未闭合门禁，不让规划获得数学身份 |
| Sub Agent | 未用，服从用户禁止 |

影响：T01–05新增持续Goal优先级但无新数学哲学裁定；T06–10仅方案接口与验收接入；T11–17无新核运行或工具政策；T18–21不外发；T22–24更新对应唯一当前owner；T25不改AI机制；T26精确本地版本纪律。G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001按PROTOCOL §5使用legacy audit，不声称分片原子写入。
"""
    previous=(ROOT/".codex/research/hott/sessions/S-RES-20260919-ASTRA-BREAKPOINT-01/CORE_COGNITION_AUDIT.md").read_text()
    rows=[line for line in previous.splitlines() if line.startswith("| `KC-")];assert len(rows)==46
    audit=f"""# {SID} 核心认知逐条复认\n\ncore-cognition-generation-7；46条。下表复认既有首轮证据及其反证条件，本单元只据此修订持续策略，未重复运行数学。\n\n- core_change: NO\n- direction_change: CURRENT_GOAL_CONNECTED\n- panorama_change: METADATA_ONLY\n- essay_change: NO\n- update_decision: 保留完整Goal，先接入结果与下一可检构造。\n- cross_conflicts: 旧策略仅设计状态已修；全局证明门禁仍PARTIAL。\n- unresolved: GEO-01至04、完整四层集成、证据门禁与公开验收。\n\n| KC | 主题 | relation | 既有工作姿态复认及本次策略依据 | 证据与反证条件 |
|---|---|---|---|---|\n"""+"\n".join(rows)+"\n\n"
    audit+="""## 扩展认知回评

001问题生成与简化两节：把实际局部结果接回原目标，不以方案字数代替行动；010列下一具体构造。002前提重现节：显式可判定性是待检输入，时间节NOT_TOUCHED，不能用有限步骤替代物理时间。003圆环节：返回原环境/缺点/恢复；ASK及双向目标节：恢复成功能改变候选，不预设失败。004走进HoTT节：保留原生演算和点集区别；自反节NOT_TOUCHED，旧Gödel不复活。005表达界限、文章起点、原文保全：接口未实例化不算几何完成，v1.0由Git保存，Goal逐字保存。006知识谱整片：新的恢复方向是最强反解释，不是知识先验裁决。007助力阻力整片：停止重复同形控制。008现实骨架整片：维持同任务桥梁及真实M/N输入义务。各项若出现完整保真模型/新反例则重评，不修改用户核心原文。

## 已走过的路

首轮完成有界规则控制，尚未闭合现实任务；本单元修复总体策略与实际状态脱节，不把这项准备当数学进展。语义索引由策略拥有，数学事实仍由formal/run/index拥有。旧策略所有U00–U09与G01–G06保留，无被删减目标。

## 即将作出的选择

选择BP-GEO-RESTORE-01，支持KC21/35/37/39/43/44–46：在非平凡QCircle输入实际检查自然恢复与逆向分类条件。拒绝重复旧Bool例子；保留证据门禁独立修复。该恢复若只能在可判定条件下成立，必须登记条件；若同任务恢复成立则撤回相应不可恢复指控。若仅集合层恢复，继续拓扑及动作保真，不能以小结果结束Goal。当前无无限枚举/公平性主张，八轴与未知入口由010固定。
"""
    files=[]
    for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
        b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r"(?m)^source_state_revision: 174$","source_state_revision: 175",body);assert n==1
            kind="direction" if rel==R.DIRECTION else "outcome"
            body,n=re.subn(r"(?m)^projection_generation: .+$","projection_generation: 20260919-"+kind+"-175",body);assert n==1
        if rel=="MEMORY/001 - 当前执行队列.md":
            first=body.index("Astra断点机制第一轮");end=body.index("\n\n",first)
            body=body[:first]+"用户本线程持续Goal已激活：先完成方案补入，再完成断点与证明机制系统检查，并据结果持续更新和执行四弹完整研究策略。首轮11包/9拒绝/60成员/28运行仅为已有控制，完整几何桥梁和证据门禁未完成。总体策略v1.1的010片拥有逐项范围，下一构造BP-GEO-RESTORE-01检查删点后加回指定点的恢复与逆向分类条件。原Goal不缩为有限pass；旧SUPPLY/Gödelrecord保留历史来源，当前动作以此Goal为准。入口：`"+SPEC+"`。"+body[end:]
        if rel=="方向追踪/002 - 治理与用户方向.md":
            lines=body.splitlines()
            for n,line in enumerate(lines):
                if line.startswith("| `DIR-U-ASTRA-BREAKPOINT` |"):
                    lines[n]="| `DIR-U-ASTRA-BREAKPOINT` | 先完成断点检查，再推进持续更新的四弹完整策略 | 用户本线程持续Goal | `ACTIVE_GOAL / FIRST_PASS_ONLY` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01` | BP-GEO-RESTORE-01自然恢复与可判定条件；所有GEO/U/G义务保留 | `"+SPEC+"` |"
            body="\n".join(lines)+"\n"
        files.append({"path":rel,"expected_sha256":R.sha(b),"text":body})
    run={"schema_version":"hott-session-runs/v1","session_id":SID,"mathematical_runs":[],"previous_progress":"R-ASTRA-BREAKPOINT-20260919","plan":PLAN,"validation":"audit/astra-breakpoint-20260919/strategy-v1.1-shards.json"}
    for name,body in [("SESSION.md",session),("RUNS.json",R.dump(run).decode()),("CORE_COGNITION_AUDIT.md",audit)]:files.append({"path":BASE+name,"expected_sha256":None,"text":body})
    payload={"schema_version":"cognition-checkpoint/v1","session_id":SID,"load_profile":"research","task_ids":[],"authorization":"用户持续Goal要求方案补入、持续执行与治理状态维护；不缩小目标。","files":files}
    (OUT/"goal-plan-checkpoint-payload.json").write_bytes(R.dump(payload))
    result=R.checkpoint(ROOT,p["snapshot"],payload,apply=a.apply)
    (OUT/("goal-plan-checkpoint-apply.json" if a.apply else "goal-plan-checkpoint-dry-run.json")).write_bytes(R.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!="paths"},ensure_ascii=False))

if __name__=="__main__":main()
