#!/usr/bin/env python3
"""Record R039 through the unchanged atomic governance engine."""
from pathlib import Path
import copy,hashlib,json,subprocess,sys
from r039_context import ROOT,runtime,dump
P='.codex/research/hott/'
R=P+'reviews/SILENT-STEPS-001/'
SID='S-RES-20260911-039-SILENT-STEPS-CHECKPOINT';CID='P-SILENT-STEPS-039';S=P+'sessions/'+SID+'/'
ORIG=P+'sessions/S-RES-20260911-039-SILENT-STEPS/'
OUT=ROOT/'artifacts/r039/checkpoint_retry'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):
 p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise FileExistsError(p)
 p.write_text(dump(x))
def main():
 old=json.loads((ROOT/(P+'STATE.json')).read_text())
 if old['revision']!=38:raise ValueError('Expected revision38')
 rt=runtime();base=rt.plan(ROOT);save('BASE.json',base)
 stale=[k for k in base['review_required'] if old['records'][k]['status']!='review_required']
 if stale:raise ValueError('Unresolved changed dependencies '+repr(stale))
 state=copy.deepcopy(old);state['revision']=39;state['latest_session']=SID
 paths=[R+x for x in ['PROOF_NOTE.md','CLAIMS.json','SOURCES.md','PLAN.md']]+[
 'scripts/research/r039_silent_steps.py','scripts/tests/test_r039_silent_steps.py',
 'artifacts/r039/RESULTS.json','artifacts/r039/TEST_EXECUTION.json','artifacts/r039/MODEL_EXECUTION.json','artifacts/r039/RESEARCH_MANIFEST.json','artifacts/r039/sources/FETCH_RECEIPT.json']
 state['records'][CID]={'kind':'candidate','path':paths[0],'status':'review_required','depends_on':['P-CURRENT-STATE-LIFTING-038'],'full_sources':paths[1:],'source_hashes':{p:sha(ROOT/p) for p in paths},'scope':'Divergence-blind weak bisimulation preserves may but not must; erroneous greatest one-sided stutter relation fails transitivity; termination-sensitive delay equivalence and finite-skip protection.','mathematical_status':'PAPER_PROOFS_WITH_31_FINITE_TESTS_NOT_NATIVE_VERIFIED','classification':'PROCESS_EQUIVALENCE_BOUNDARY_WITH_POSITIVE_CONTROLS','novelty':'KNOWN_CORE_NOT_CLAIMED','HoTT_core_error':False}
 session_sources=[ORIG+'REQUEST.md',ORIG+'RESEARCH_DELTA.md',ORIG+'SESSION.md','artifacts/r039/COGNITION_STATUS.json','artifacts/r039/START.json','artifacts/r039/checkpoint/FAILURE.json']
 session=(ROOT/(ORIG+'SESSION.md')).read_text()+'\n## 原子交接\n\n此独立checkpoint Session保留先行研究SESSION原字节；首轮dry-run因未包含新SESSION被拒，未写状态；本次按原引擎新建此不可覆盖记录。\n'
 state['records'][SID]={'kind':'session','path':S+'SESSION.md','status':'review_required','depends_on':[old['latest_session'],CID],'full_sources':session_sources,'source_hashes':{**{p:sha(ROOT/p) for p in session_sources},S+'SESSION.md':hashlib.sha256(session.encode()).hexdigest()},'scope':'Bounded continuation of revision38; no full cognition certification, no invented compaction event.','cognition_status':'BLOCKED_FULL_COGNITION_DYNAMIC_INCOMPLETE','native_status':'NOT_RUN'}
 state['active']=[CID]+old['active'];state['review_due']=list(dict.fromkeys(old['review_due']+[CID,SID]))
 state['execution_control'].update(status='RESUMED_BY_USER',request_path=ORIG+'REQUEST.md',last_research_session=SID,reason='User continues from R038; concrete silent-step equivalence investigation.',background_work=False,execution_at_delivery='CHECKPOINTED_NOT_RUNNING_BACKGROUND')
 state['local_git'].update(inherited_head='149767b70bd102fa4b16b28922bf7bb3dd64682c',pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),history_origin='Inherited complete revision38 Git archive; not reinitialized',final_head='See actual Git HEAD and external revision39 delivery report')
 memory=f'''# MEMORY · revision39 · 停顿等价与完成量词

当前根`{ROOT}`，继承revision38完整Git；实际研究R039。授权为当前沙箱有界研究、scripts先写后调用、本地Git与打包。无Work、模型切换、其他AI、push或后台。

## 共同认识不变
HoTT已有能力、共有计算界限、具体理论化新增失真分开；双向现实相对目标及Z原话保留。正确拒绝/保全是正例，不能把所有不可能性归给缺时间。

## 最新R039
全文`{R}PROOF_NOTE.md`。F --done--> Z；S --tau--> S且S --done--> Z。普通发散不敏感弱互模拟F~S，两者MayDone但只有F满足所有最大运行最终done（不加公平性）。Done仍显式保留，无限tau由另一侧连续零步匹配；因此MustDone不尊重这个等价，不能保持原规格下降到其HoTT集合商。不是声称标准商规则会免费发放这种下降。
确定性Delay的保结果等价可以忘掉有限停顿且仍区分omega和now。相反，若把单边跳过全部解释为最大不动点，Bad将omega关联到任何now，甚至不传递；其等价闭包会合并0/1，因此不能保标签提取。Bad是明示的错误比较定义，不是标准HoTT身份或已查实际库bug。
一手作者源码明确使用归纳收敛/双边进度，或有限单边预算；这些保护保留。不能把产生无限的关系证明节点当成待证程序已经返回。

## 证据
31项有限测试通过，含144个1—3状态确定性Delay图与错误证书；一般结论为纸笔，非原生内核。web实际查阅作者源码及论文摘要；三份容器下载DNS失败，未假称原始文件已下载。原生工具未找到，本轮没有补一个未经编译的“完成形式化”。

## 接续
原87项records逐值保留；R038的Acc正例、无限前缀反例，RP-B01原生对应、R026规约、各轮自指/路径结果都在旧链中。下一项可检查结果等价与race/timeout组合：顺序bind可保什么，竞争操作又需要什么；不要继续放大同一自环样本，不等待Gemini。

## 认知边界
本轮原计划433份/3,218,894字节没有全文加载；闭包和三问仅部分实际读取。BLOCKED_FULL_COGNITION / bounded local continuation，不宣称完整Skill已执行，不虚构压缩。原政策、运行器、原文与数学状态不改。
'''
 frontier=f'''# FRONTIER · revision39

当前`{CID}`：完成R038约定的silent-step检查。精确结果：发散不敏感弱互模拟保本例may、不保must；有限跳过与无限单边余归纳不同，后者Bad甚至非传递；正确Delay关系有终止/结果保护。

该族停止追加同类图穷举。下一有判别力的候选：确定性部分结果等价与race/timeout操作的组合，核真实操作类型及quotient respect，不把共用“等价”名称当成同一合同。RP-B01原生对应和R026规约/环境有效范围仍开放，不因工具缺失清空。没有发给其他AI的依赖任务。
'''
 lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''\n## R039 · 空匹配与有限跳过\n\n- R038的每条边有当前一步提升不能无声削弱成允许零步的弱匹配；无限多个零步匹配不提供进度。\n- MayDone与MustDone不同，公平性不得默认为真；保留Done标签仍可丢掉must保证。\n- 定义为最大不动点的任意单边跳过，会把omega关联到每个结果且不传递；这不是标准弱互模拟。商可合并这些点，但结果读取必须证明respect。\n- 有限跳过/双边余归纳与无限单边跳过分开。正确Delay关系可同时遗忘有限耗时并保收敛/发散，不能以“weak”一词判定失败。\n- 工具通过某个关系的局部规则，不等于该关系符合预期的完成语义。\n- 容器源下载失败和web读源成功分别记录；不用文件hash或输出量替代全文认知。\n'''
 resume=f'''# RESUME · revision39

最新`{SID}`，当前根`{ROOT}`，无后台任务。按原入口/全文政策恢复；本摘要不替代433份实际依赖。

先回源`{R}PROOF_NOTE.md`、CLAIMS/SOURCES/PLAN与artifacts/r039结果。F/S反例是普通弱互模拟不保must；Bad是刻意核查的错误定义，不是库实际实现；真实Leroy Delay源码的有限单边预算与归纳收敛是正向控制，未本地编译。

保留R038当前态Acc迁移，不能因为这次zero-match失败就撤回旧的一步正定理。所有87项旧记录/未决保留。

下一不重复工作：结果等价上的顺序组合与竞争/超时的不同观察责任。只有明确操作、规约和真正的新连接时再展开，不继续更换自环标签。脚本先存，本地Git/实际日志/原checkpoint回读再打包；不宣称完整认知或原生证明通过。
'''
 values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':dump(state),S+'SESSION.md':session}
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'User continues; standing scripts-first local Git/archive authorization. Bounded local research, no remote or other AI.', 'files':[{'path':p,'text':t,'expected_sha256':sha(ROOT/p) if (ROOT/p).exists() else None} for p,t in values.items()]}
 save('PAYLOAD.json',payload);save('DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False));commit=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('COMMIT.json',commit)
 after=rt.plan(ROOT);save('AFTER.json',after)
 try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
 except rt.CognitionError as e:
  if str(e)!='STALE_BASE':raise
  save('STALE.json',{'status':'REJECTED','error':str(e),'writes':False})
 else:raise AssertionError('Stale base accepted')
 new=json.loads((ROOT/(P+'STATE.json')).read_text());assert all(new['records'][k]==v for k,v in old['records'].items())
 assert new['unresolved']==old['unresolved']
 routes={d['path'] for d in after['documents']};assert set(paths+session_sources+[S+'SESSION.md'])<=routes
 index=ROOT/'scripts/README.md'
 index.write_text(index.read_text()+'''\n## R039 · silent-step等价与完成量词\n\n研究：`research/r039_silent_steps.py`；31项测试：`tests/test_r039_silent_steps.py`。运行日志和结果在`artifacts/r039/`；有限模型不是HoTT内核。治理/读源/制包脚本在`session/r039_*`，全部先存后执行。旧源码原位置保留。\n''')
 save('SUMMARY.json',dict(status=commit['status'],revision=39,old_records_preserved=len(old['records']),current_records=len(new['records']),planned_documents=len(after['documents']),all_new_sources_routed=True,stale_rejected=True,full_cognition='NOT_CERTIFIED',native='NOT_RUN'))
 print((OUT/'SUMMARY.json').read_text())
if __name__=='__main__':main()
