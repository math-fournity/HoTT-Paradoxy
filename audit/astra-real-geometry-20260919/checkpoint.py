#!/usr/bin/env python3
"""Atomically register C-265 and keep the complete geometry/HoTT goal open."""
import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-REAL-CIRCLE'
BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第四轮执行报告.md'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py')
R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)

TOUCHED={
1:('ALIGNED','精确对象/命题/范围先行；真实实数模型不以历史叙事替代。'),
2:('DEEPENED','固定经典Lean、实数子空间拓扑和原生HoTT的边界，公开三项标准公理。'),
5:('ALIGNED','先构造实际对应并保留正结果，再判断丰富任务是否失配。'),
6:('ALIGNED','不把静态连续函数误报为真实时间或物理完成过程。'),
7:('ALIGNED','依赖固定与实际核验替代模型自述；保存首次失败及占位公理输出。'),
10:('ALIGNED','几何正结果不是内部矛盾或现实悖论；原目标保持现实相对。'),
12:('DEEPENED','删点p作为输入，明确所得只是H关系，不偷换成来源恢复。'),
13:('ALIGNED','连续双逆与有限Trace的资格分离，后继检验真正恢复接口。'),
14:('ALIGNED','对象/表示存在没有升级为原任务所有操作已经完成。'),
15:('TENSION','同胚正结果不能支持抽象必然失败；仍需检查原允许操作与现实对应。'),
17:('ALIGNED','正面同胚接受为证据，不为预定结论屏蔽标准构造。'),
21:('DEEPENED','真实Lean源码、两次正式捕获、23k量级输入pin及双校验，非仅纸面示例。'),
22:('ALIGNED','保留A/B；本次只闭合底层几何，不将两个研究方向提前宣告解决。'),
31:('DEEPENED','从一般参数接口推进到实际非有限实数空间构造。'),
34:('ALIGNED','正构造、负资格控制、工具失败和未触达命题分别记录。'),
35:('DEEPENED','原圆环已有精确底层模型；HoTT保真与完整来源观察仍开放。'),
37:('TENSION','真实几何已有推进但未发现HoTT缺陷，不能改以已得正结果作为父目标成功。'),
38:('TENSION','本轮为关键模型未知提供证据，没有声称已定位理论作者缺陷。'),
39:('DEEPENED','返回圆和区间的基础定义，停止重复恒等函数控制。'),
41:('ALIGNED','工具链和证明助手用于建立真实可复核构造。'),
42:('ALIGNED','固定可信边界，不让库的权威或一次PASS替代任务语义判断。'),
43:('DEEPENED','从长期控制/校验修复回到真正几何模型，后继选择端部和环境。'),
44:('ALIGNED','空间作为假想现实的明确模型处理，不否认其现实诠释可能性。'),
45:('DEEPENED','H已经实例化，下一步核对R的必要条件是否被遗漏。'),
46:('ALIGNED','把现实要求变成环境、端部及操作的下一可检任务，未以能力不足回避。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    assert json.loads((OUT/'DELIVERY.json').read_text())['status']=='DUAL_LOCAL_PASS'
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919'])
    assert plan['revision']==177
    state=json.loads((ROOT/R.STATE).read_text());old=state['latest_session']
    state['revision']=178;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C265_LOCAL_FORMAL_AND_RELATION_CHECKS_PASS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
    state['records']['R-ASTRA-REAL-CIRCLE-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_POINT_SET_GEOMETRY','status':'complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-POINT-RESTORATION-20260919'],'full_sources':[REPORT,'HoTT/formal/astra-real-geometry/PuncturedCircle.lean','HoTT/formal/astra-real-geometry/TOOLCHAIN.json','audit/astra-real-geometry-20260919/DELIVERY.json'],'scope':'C-265: actual real punctured sphere homeomorphism to Ioo(0,1), explicit pole and inverse/continuity. Native HoTT translation, ambient/endpoints and physical Trace remain open.'}
    ec=state['execution_control'];ec.update(status='ASTRA_REAL_INTRINSIC_GEOMETRY_CHECKED',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json')
    ec['next_minimal_verification']='GEO-02/03：在C-265的实际实数点集模型上加入环境嵌入、端部完成/指定缺口和原操作合同；证明端部关联及其保持/不能提升的精确条件，并检查最强保任务恢复。不得以泛型Bool、恒等函数或∀x,x≠p替代真实模型。Lean→HoTT保真、GEO-04、真实GOLD连接、U00–U09与G01–G06其余义务继续保留；ZCode审查已吸收，Goal ACTIVE未完成。'
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端实际路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_GOAL
- load_receipt: audit/astra-real-geometry-20260919/RESUME-20260920.json；延续先前完整T3加载，PROTOCOL v3同档复认；core hash未变、46KC立场已回读与原文抽查，变化来自已知事务/本方计划版本
- status: C265_INTRINSIC_GEOMETRY_CHECKED / FULL_GOAL_ACTIVE

上一单元PROGRESS：ZCode完整可见工作审查、四模块重放及计划v1.4/断点v1.3已提交。本轮回到实际模型，未继续扩大审计。Lean4.34.0/mathlib exact tag与八依赖锁定，官方Cache.Hashing生成2568模块闭包；默认CDN403保留，按上游官方Azure配置下载，aria2≤8路、D盘保留缓存和日志。首次草稿集合外延步骤未闭合，exit1及sorryAx输出保存；修复后过核。正式run-02作为C-265 primary，-01成功捕获和原捕获器副本保留。

当前构造为真实EuclideanSpace ℝ (Fin 2)单位圆的任意指定点补子类型与Ioo(0,1)的Homeomorph；显式pole、满射、双逆和连续性过核。依赖propext/Classical.choice/Quot.sound，无sorryAx；输入/source/artifact哈希固定，官方预编译库可信边界明示。辅助Lean不冒充原生HoTT、物理Trace或环境端部保持。

F与本地包关系双检查PASS；旧28回归PASS；三个隔离compiler绑定错误均被拒。新增Lean精确binary分支服务这个实际消费者，不放行任意wrapper，不改共享Skill/Host/权限。库与源码未为PASS削弱。完整历史版本门禁仍开放。

证据owner={REPORT}；下一动作是实际端部/环境模型及Forget/恢复。原Goal与ZCode追加要求已持久化，未改写其成功标准；不启动Sub Agent，不push/tag/公开。按PROTOCOL§5使用完整46KC legacy单文件审计，已知writer分片原子事务缺口不伪造关闭。

element_usage：closure恢复当前目标；研究Skill区分H/R/Reach；download Skill固定来源/并发/落盘；F-011核精确Lean命题；SOP要求反思/方案版本；checkpoint只登记真实结果。共享治理C01–C05/C07–C09无方法/版本/运行权限变更，C06仅项目内Lean证据支持与3负控制、C10保存失败与可信边界；T11–17/22–26受影响，其余当前需求未改。
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: NEXT_AMBIENT_ENDPOINTS\n- panorama_change: ADD_C265_REAL_GEOMETRY\n- essay_change: NO\n- update_decision: 记录真实底层几何，继续R与HoTT连接。\n- cross_conflicts: 内在同胚成立与原操作未决不可合并。\n- unresolved: 端部/环境、Trace、HoTT保真、四层集成。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
    for n,(kc,title) in enumerate(headings,1):
        rel,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未研究该具体时间、自指或元理论命题；几何同胚不回答该问题。'))
        ev='C-265源码/run-02与第四轮报告；如原任务不允许所给参数或需要不同观察，修改对应关系而非扩大本定理；哈希/类型失败则撤回资格。' if n in TOUCHED else '第四轮报告003未触达范围；出现该主题具名规格或新直接证据再进入。'
        audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001问题发生/简化：真实模型校准原M/N，不改变目标。002前提改变：当前经典选择、实数与子空间假设显式；时间连续性未检验。003圆环/ASK/A-B：给内在对应，不宣称过程完成；原阶段条件仍开放。004HoTT形态：Lean模型与原生HoTT分开，归因后置；自反未触达。005表达界限/原文/文章起点：经典数学正构造被保留，当前成果写回而非改原用户表述。006知识谱：从具体Sphere/interval API获得模型，非模型自评。007助力阻力：结束泛型控制重复，返回真实端部环境。008现实骨架：数学空间是明确假想现实模型，实际允许操作须另给，不以静态函数抹除该要求。

## 已走过的路

上一阶段只有原生路径排除、有理点集及一般恢复。本轮取得真实实数拓扑模型和实际双逆，关键未知减少。环境准备服务2568模块的单一所需闭包，非全库重构；失败、classical axioms和预编译可信边界保存。未得到HoTT失配。

## 即将作出的选择与完备性

选择实际端部/环境及Forget恢复，对应KC35/37/39/43/44–46；拒绝再做泛型恒等函数。八轴为结构化点集×删点/呈现×原M/N底层×立体投影/双逆×内在拓扑×表示完成×Lean核×固定经典mathlib。未触达物理Trace、全库消费者、native HoTT或无限候选空间，无穷举/公平性声称。独立后继对照为嵌入/闭包/端部语义；若保任务恢复成功则撤回对应候选，若只关系不同则不升级为理论矛盾。原Goal全部剩余义务保留。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_run':'HoTT/verification/runs/20260920-MP-ASTRA-REAL-CIRCLE-001-02','historical_capture':'HoTT/verification/runs/20260920-MP-ASTRA-REAL-CIRCLE-001-01','validation':'audit/astra-real-geometry-20260919/DELIVERY.json','claim_ids':['C-265'],'parent_goal':'ACTIVE_NOT_COMPLETE'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-178'
    files=[]
    for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
        b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 177$','source_state_revision: 178',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-178',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户本线程持续Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户本线程持续Goal ACTIVE，ZCode 7cb审查已完成并接入策略v1.4。第四轮C-265已构造真实二维实数单位圆去点到Ioo(0,1)的Homeomorph，显式点/双逆/连续性经Lean4.34.0/mathlib核验及本地双检查。经典三公理与官方缓存可信边界明示，不是native HoTT或物理Trace。下一步GEO-02/03实际端部/环境、Forget与原允许操作；GEO-04、真实GOLD连接及完整U00–U09/G01–G06继续开放。入口：`'+REPORT+'`。旧SUPPLY/Gödel与全历史修复不自动替代当前动作。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]='| `DIR-U-ASTRA-BREAKPOINT` | 完成断点检查并持续推进完整四弹策略 | 用户线程Goal | `ACTIVE_GOAL / REAL_INTRINSIC_GEOMETRY_CHECKED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02`、`OUT-ASTRA-PROOF-WIRING-03`、`OUT-ASTRA-REAL-CIRCLE-04` | 实际端部/环境与原操作保真，Lean模型不冒充native HoTT | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |'
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-REAL-CIRCLE-04` | C-265真实实数去点圆与开区间的内在同胚 | `DIR-U-ASTRA-BREAKPOINT` | Lean4.34.0/mathlib固定版本、源与22923外部文件哈希、实际run-02、双校验 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN` | 首次实际实数拓扑对应及显式点/逆律/连续性 | 环境端部、物理Trace、native HoTT保真或缺陷 | `'+REPORT+'`；`audit/astra-real-geometry-20260919/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(b),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户持续Goal授权完成断点与四弹策略及相应治理；登记C-265实际范围，后继继续同一实际模型，不宣称总目标完成。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
