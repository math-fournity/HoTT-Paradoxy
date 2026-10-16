#!/usr/bin/env python3
"""Use the original atomic governance runtime; never alter historical proof status."""
from pathlib import Path
import copy,hashlib,importlib.util,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
SID='S-RES-20260911-038-CURRENT-STATE-LIFTING';CID='P-CURRENT-STATE-LIFTING-038'
S=P+'sessions/'+SID+'/';R=P+'reviews/TRANSITION-ABSTRACTION-002/'
OUT=ROOT/'artifacts/r038/checkpoint'
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):
 p=OUT/n;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise FileExistsError(p)
 p.write_text(js(x))
def runtime():
 spec=importlib.util.spec_from_file_location('r038_checkpoint_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
 rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt);return rt
def main():
 old=json.loads((ROOT/(P+'STATE.json')).read_text());assert old['revision']==37
 rt=runtime();base=rt.plan(ROOT);save('BASE.json',base);save('STATE_BASE.json',old)
 state=copy.deepcopy(old);state['revision']=38;state['latest_session']=SID
 # Original owners and old records are not modified in this round.
 need=[k for k in base['review_required'] if old['records'][k]['status']!='review_required']
 if need:raise RuntimeError('unexpected stale prior statuses: '+str(need))
 paths=[R+x for x in ['PROOF_NOTE.md','CLAIMS.json','SOURCES.md','PLAN.md']]+[
  'scripts/research/r038_current_lift.py','scripts/tests/test_r038_current_lift.py',
  'scripts/research/r036_transition_abstraction.py','artifacts/r038/RESULTS.json',
  'artifacts/r038/TEST_EXECUTION.json','artifacts/r038/MODEL_EXECUTION.json',
  'artifacts/r038/RESEARCH_MANIFEST.json','artifacts/r038/SOURCE_EXCERPTS.md']
 state['records'][CID]={'kind':'candidate','path':R+'PROOF_NOTE.md','status':'review_required',
  'depends_on':['P-TRANSITION-ABSTRACTION-036'],'full_sources':paths[1:],
  'source_hashes':{p:sha(ROOT/p) for p in paths},
  'scope':'Exact successor descent/current-state lift; truncated accessibility transfer; incompatible finite-prefix witnesses and a sequential limit counterexample.',
  'mathematical_status':'PAPER_PROOFS_WITH_28_FINITE_TESTS_NOT_NATIVE_VERIFIED',
  'classification':'SPECIFIC_ABSTRACTION_BOUNDARY_WITH_HOTT_POSITIVE_TRANSFER',
  'novelty':'NOT_CLAIMED','HoTT_core_error':False}
 session_sources=[S+'REQUEST.md',S+'RESEARCH_DELTA.md','artifacts/r038/COGNITION_STATUS.json']
 state['records'][SID]={'kind':'session','path':S+'SESSION.md','status':'review_required',
  'depends_on':[old['latest_session'],CID],'full_sources':session_sources,
  'source_hashes':{p:sha(ROOT/p) for p in session_sources},
  'scope':'Bounded local continuation from revision37; all old records retained; no policy rewrite or external AI.',
  'cognition_status':'NOT_CERTIFIED_FULL; ACTUAL_COMPACTION; DYNAMIC_INCOMPLETE','native_status':'NOT_RUN'}
 state['active']=[CID]+old['active'];state['review_due']=list(dict.fromkeys(old['review_due']+[CID,SID]))
 state['execution_control']=copy.deepcopy(old['execution_control']);state['execution_control'].update(
  status='RESUMED_BY_USER',request_path=S+'REQUEST.md',last_research_session=SID,
  reason='User explicitly continues research from the current revision37 handoff.',
  background_work=False,execution_at_delivery='CHECKPOINTED_NOT_RUNNING_BACKGROUND')
 state['local_git'].update(inherited_head='515da9f6143fb5fd545031fa9648a5a002d75c2b',
  pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
  history_origin='Inherited revision37 complete .git; no reinitialization',
  final_head='See actual Git HEAD and external revision38 delivery report')
 memory=f'''# MEMORY · revision38 · 当前态接续与无限组合\n\n当前根`{ROOT}`，继承revision37完整Git；用户“继续”授权有界研究、scripts先存后执行、本地Git与完整交付。无远端push、模型切换、Work、其他AI或后台任务。\n\n## 不变的研究认识\nAGENTS、业务Skill v1.3.4、三问v6及第五闭包§22在R036—37已对齐：HoTT已有的逻辑/同伦/计算能力、共有计算与证明界限、具体理论化新增失真分别说明。原双向现实相对目标和Z原文不被修改；不能因正确拒绝或共有不完备性宣布HoTT错误，也不能因一个正例关闭全部方向。\n\n## 最新实质结果R038\n全文`{R}PROOF_NOTE.md`。固定当前代表的后继谓词C与逐类存在关系E不同。纤维内C双向一致 ⇔ 精确后继下降 ⇔ 每个当前代表有命题性一步提升 ⇔ 全部有限抽象路径有命题性的相容提升。实际商递归需要respect，因此R036坏合并的后继函数不能精确下降，但其may关系仍合法。\n在函数外延性下Acc是命题；对源Acc归纳，用当前提升的截断见证消去到目标Acc，得到Acc_R(s)→Acc_E(αs)。不需先选无限轨迹，不用LEM或依赖选择。终止不等于到达Done；全轨迹提升也不是仅保终止的必要条件。\n新的无限分支倒计时：Root→Count(n)，随后递减到0/Done。每条执行有限结束，但无统一Nat上界；抽象Start,Work,Work,…每个有限前缀都可提升，整条无限路径无提升，因为首步N一旦确定不能不断增大。进一步A_k={{m | k≤m}}、相容映射保持m：Lim A为空，Lim‖A‖有元素。逐阶段忘掉见证再相容化不是先相容化再忘掉见证。已有显式逐层选择，不将其错误归为选择公理缺失。\n\n## 验证与界限\n28项新测试PASS；实际复用未改R036 System。有限提升表、全后继Acc证书和17个前缀有日志。一般定理是纸笔，未经过原生HoTT内核或独立专家；来源查阅不升级为机器证明。不认领原创性或实际库bug。\n\n## 连续性与下一动作\n原{len(old['records'])}项records逐值不变，所有active/unresolved保留。R001缺源、RP-B01原生对应、R026规约、R029—34自指/路径正反成果均在递归记录链里。此族不继续增加图样本。下一探索可转到停顿/弱过程等价：固定有限观察、终止与交付要求，检查特定等价究竟保存什么；不预设弱等价非法，不复活旧Done擦除或不透明ua的错误强断言。\n\n## 加载身份\n完整第五闭包曾输出后发生实际压缩，三问随后完整输出；418份动态材料未完整同窗读取。本轮是受权有界局部接续，NOT_CERTIFIED_FULL_COGNITION。原完整读取政策/引擎未改，字节覆盖不认证理解。\n'''
 frontier=f'''# FRONTIER · revision38\n\n最新`{CID}`。已回答R036后一项关键未知：后继谓词精确下降的respect条件正是当前代表的继续能力；不是商递归免费提供逐类may模型的精确回放。\n\n进一步得到Acc的命题性让“仅命题当前提升”仍足够迁移终止证明。负向反例显示全体有限前缀可行仍不足以全程相容；A_k={{m≥k}}精确说明截断与逆极限不能如此交换。\n\n此族收敛，不增加同类状态表。下一自主候选为停顿/弱过程等价对有限观察与发散的不同处理；先给具体规格与正反例，若只显示合理的抽象界限不冒充核心错误。RP-B01原生对应与R026规约保持开放，工具不可用不阻塞全部纸笔探索。\n'''
 lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''\n## R038 · 当前代表与相容量词\n\n- 逐类存在关系E合法，不代表当前后继谓词C可以精确下降；标准商递归仍要求respect。\n- 各边有见证、每个有限前缀有相容见证、存在同一条无限提升，是三个不同强度。\n- 当前提升见证虽仅截断，目标Acc是命题，仍可用归纳迁移终止证明；不要额外制造无限选择前置。\n- 倒计时树根部无限分支，各次运行有限但无统一界。有限前缀见证已经有显式选择函数；无无限提升的原因是见证不能相容，不是一般选择不可得。\n- A_k={m≥k}的逆极限为空，逐层截断后的极限可缩；不得静默交换这两种操作。\n- Acc不等于指定Done；精确有限轨迹提升不是抽象终止性保持的必要条件。\n- 含未验证arith假公理的参考草稿不作为完整机器证明；原生工具不可用时保留纸笔身份。\n'''
 resume=f'''# RESUME · revision38\n\n最新session `{SID}`，当前根`{ROOT}`；无后台任务。按原全文政策恢复第五闭包、三问和动态状态，不以此摘要替代正文。\n\n最新正文`{R}PROOF_NOTE.md`及CLAIMS/SOURCES/PLAN、artifacts/r038真实检查。优先把握三个差量：exact商respect↔当前代表提升；命题Acc使仅截断提升也能保终止；逐层截断和无限相容极限不交换。\n\n原R036反例仍是合法may模型的虚假路径，非标准HoTT错误。R038正例表明缺陷不能只归给“丢了见证”；必须看量词/当前态。倒计时对每个有限长度有真前缀，不得冒称已有真无限执行。\n\n下一项不继续图样本：具体停顿/弱过程等价对有限观察与发散的合同；若属正确抽象则按正确边界交付。所有旧未决继续保留。新代码先写scripts再调用，保留失败和运行日志，本地Git无push。完整认知与原生证明本轮未认证。\n'''
 session=f'''# {SID}\n\n## 身份与输入\n用户本轮“继续”；从revision37 with_git恢复，真实基线HEAD 515da9f6143fb5fd545031fa9648a5a002d75c2b。恢复收据在artifacts/r038。未改模型/远端/外部AI。\n\n## 实际行动与proof_delta\n读当前AGENTS、治理和业务职责、闭包/三问、当前记忆、R036与固定商/截断规则；原第五闭包读出后发生实际压缩，418份动态未全读，保持有界局部身份。研究差量见RESEARCH_DELTA.md。\n编写并运行28项有限测试与报告，复用原R036模型。写出精确下降定理、仅截断见证的Acc迁移、倒计时和逆极限反例。新材料经原checkpoint进入动态集合，旧结论/依赖不重写、不升级。\n\n## 证据边界\n纸笔证明＋有限程序检查，不是HoTT内核；原生工具在START未发现。网页核对的isPropAcc为作者托管源码，官方raw请求失败未称下载成功；HoTT_Markov含假arith草稿未用作证。没有原创性、物理本体或实际软件错误认领。\n\n## 连续性与授权\n原记录、unresolved及active保留。用户原双向目标和最新已有能力/共享界限/新增失真区分不变。本轮不修改AGENTS/Skill/第五闭包/三问/Schema/矩阵/旧程序。实际变化是新研究文件、scripts索引及当前治理记忆。下一动作见PLAN，不等待Gemini回信。\n'''
 values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':js(state),S+'SESSION.md':session}
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'Explicit continuation with standing scripts-first/local Git/archive authorization; bounded local research only.',
 'files':[{'path':p,'text':t,'expected_sha256':sha(ROOT/p) if (ROOT/p).exists() else None} for p,t in values.items()]}
 save('PAYLOAD.json',payload);save('DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
 result=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('COMMIT.json',result)
 after=rt.plan(ROOT);save('AFTER.json',after)
 try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
 except rt.CognitionError as e:
  if str(e)!='STALE_BASE':raise
  save('STALE.json',{'status':'REJECTED','error':str(e),'writes':False})
 else:raise AssertionError('stale snapshot accepted')
 new=json.loads((ROOT/(P+'STATE.json')).read_text());assert all(new['records'].get(k)==v for k,v in old['records'].items())
 assert new['unresolved']==old['unresolved']
 routes={d['path'] for d in after['documents']};assert set(paths+session_sources+[S+'SESSION.md'])<=routes
 report={'status':result['status'],'revision':38,'old_records':len(old['records']),'old_records_unchanged':len(old['records']),'records':len(new['records']),'all_new_sources_routed':True,'planned_documents':len(after['documents']),'stale_rejected':True,'full_cognition':'NOT_CERTIFIED','native':'NOT_RUN'}
 save('SUMMARY.json',report);print(js(report))
if __name__=='__main__':main()
