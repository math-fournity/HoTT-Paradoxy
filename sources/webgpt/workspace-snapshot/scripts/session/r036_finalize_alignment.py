#!/usr/bin/env python3
"""Finish current-section consistency, retaining committed checkpoint36 and old originals."""
from pathlib import Path
import copy,hashlib,importlib.util,json,sys,subprocess
ROOT=Path(__file__).resolve().parents[2];P='.codex/research/hott/'
SID='S-GOV-20260911-037-OWNER-ALIGNMENT-FINAL';S=P+'sessions/'+SID+'/'
OUT=ROOT/'artifacts/r036/final_alignment'
C='认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md'
K='.codex/skills/hott-paradox-research/SKILL.md';Q='HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
def js(o):return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise FileExistsError(p)
 p.write_text(text,encoding='utf-8')
def out(name,o):save('artifacts/r036/final_alignment/'+name,js(o))
def rep(t,a,b):
 if t.count(a)!=1:raise ValueError('expected one occurrence: '+a[:80])
 return t.replace(a,b,1)
def main():
 old=json.loads((ROOT/(P+'STATE.json')).read_text());assert old['revision']==36
 changes={}
 def update(rel,text):
  p=ROOT/rel;before=p.read_bytes();save('.codex/history/r037-before/'+rel,before.decode());p.write_text(text)
  changes[rel]={'before':sha(before),'after':sha(p.read_bytes())}
 t=(ROOT/C).read_text()
 t=rep(t,'完整最新原文见[§20]','完成困难目标的原文见[§20]')
 t=rep(t,'三问当前在v3中同步§20目标；Z owner相应现行段落已校准为多形态发现、确认与最终归因分离。','三问当前为v6，双向目标、ASK及R035认识同时同步；Z/时间owner相应区分已有能力、共享界限和新增失真。')
 start=t.index('## 十四、当前结论与 Verdict');end=t.index('## 十五、',start)
 t=t[:start]+'''## 十四、当前结论与 Verdict

### 14.1 当前认识

依据R035用户怀疑及R036明确恢复请求，以“逻辑＋同伦结构＋计算/依赖”审视HoTT。区分已有能力、有效系统共有的限制，以及指定理论化新增的失真；不能仅凭停机不可判定、Löb界限或类型非栖居就宣布理论不现实。

双向现实相对目标、用户Z哲学来源、ASK与九类方向保持。§20—21仍保存原始目标与ASK原话；§22新增R035请求和助手完整评估。用户判断、助手解释、数学结论及物理假说分层，旧原文不得静默改写。

R036实际有限研究已进行：源a→b→d两步完成，Done保真状态商有虚假无限路径。其两步前缀不能提升；正确may过近似不宣称源发散。这是指定抽象的行为边界，不是新的HoTT内核矛盾。正文在reviews/TRANSITION-ABSTRACTION-001，不以本节概述替代证明。

### 14.2 尚未闭合

完整实际HoTT应用的现实对应、原生形式化、独立审查及新颖性均按具体记录保留。R001原证据、RP-B01原生对应、R026规约、R029—34正反结果未被抹去或重新认证。当前没有“所有旧owner/全部语料已终审”的结论。

完整动态认知读取仍未通过；未读文档不能以索引或哈希代替理解。一般研究未知不是新的全域前置门槛。

### 14.3 当前执行与保全

本轮用户已解除R035暂停并授权对齐后继续探索。当前工作副本继承完整Git，所有代码先写scripts；实际研究保存于checkpoint36，旧current段指针复核后再保存checkpoint37。旧版本由Git、r036-before/r037-before及不可覆盖Session保留，不回滚或改写已经提交的checkpoint。

无Work、模型切换、其它AI、push或后台。两核心全文曾读出后真实压缩；本轮只认证当前owner对齐及有界局部研究，不认证完整业务Skill。全文政策与治理引擎未改。

'''+t[end:]
 t=rep(t,'> 本次档案与解释对齐不提高数学、物理、原创性或外审状态。全部动态依赖的全文gate在本轮读取过程中仍发生压缩，未宣称完整业务Skill验收；本轮只交付明确授权的原文保全、文档对齐和治理回写。','> 当前owner对齐不升级旧数学、物理、原创性或外审状态。R036新研究有独立正文与有限执行证据；当前动态全集未全部加载且有真实压缩，故不认证完整业务Skill。最新具体状态以STATE和MEMORY为准。')
 update(C,t)
 t=(ROOT/K).read_text();t=t.replace('## 13. v1.3.2：','## 13. 历史v1.3.2：',1).replace('## 14. v1.3.3：','## 14. 历史v1.3.3：',1)
 t=rep(t,'当前计划和证据状态以 `.codex/research/hott/candidates/RP-B01/` 为起点，后续按新成果调度。','该历史轮计划曾以 `.codex/research/hott/candidates/RP-B01/` 为起点；当前计划及证据状态以最新STATE/FRONTIER为准。')
 update(K,t)
 t=(ROOT/Q).read_text().replace('### 2026-09-11 v5：双向目标与两轮Gemini材料的正确地位','### 2026-09-11 v5历史：双向目标与两轮Gemini材料的正确地位',1)
 t=rep(t,'当前由本项目选定RP-B01：','当时由本项目选定RP-B01：');update(Q,t)
 t=(ROOT/'AGENTS.md').read_text()
 t=rep(t,'预算；当前常规项目规模远非会触及。若未来接近真实预算，先提升配置、改善路由或去真正重复，\n不得删除会改变 AI 判断的 always-on 认知。','预算；当前历史动态集合已很大，不能预设全部容纳或声称可控制宿主预算。可以改善路由、去真正重复并如实标记未加载，\n不得删除会改变 AI 判断的 always-on 认知，也不得改清单来伪认证全文完成。')
 update('AGENTS.md',t)
 # Root pointer uses latest actual checkpoint; no mathematical new round is implied.
 t=(ROOT/'README.md').read_text();t=t.replace('当前状态与恢复入口（2026-09-11，revision36）','当前状态与恢复入口（2026-09-11，revision37；最后实际研究R036）',1);update('README.md',t)
 old=(json.loads((ROOT/(P+'STATE.json')).read_text()))
 audit={'reason':'Final current-owner review found closure §14 still asserted historical no-Git/no-research, and old current-plan references.',
 'changes':changes,'checkpoint36_retained':True,'new_math':False,'load_policy_changed':False}
 out('OWNER_REVIEW.json',audit)
 save(S+'OWNER_REVIEW.md','''# 当前owner最终交叉核查

R036已经完成认识同步与数学研究。最终逐current section复核发现第五闭包§14仍是revision9的无Git/无新研究状态，§7.5仍引用三问v3，Skill历史v1.3.3仍称RP-B01当前起点。此次原位修复这些过期current指针，而不是再追加一段相反现状。

保留checkpoint36与其源码/载荷，不修改旧SESSION或旧STATE记录；新增checkpoint37，仅完成治理一致性核查。最后实质研究仍R036，28测试不重复计数。§17—21历史原文、所有旧数学/实验/用户源仍保留。全部加载政策/运行器未改。
''')
 spec=importlib.util.spec_from_file_location('r037_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
 base=rt.plan(ROOT);out('BASE.json',base)
 state=copy.deepcopy(old);state['revision']=37;state['latest_session']=SID
 full=[S+'OWNER_REVIEW.md','artifacts/r036/final_alignment/OWNER_REVIEW.json']+list(changes)
 state['records'][SID]={'kind':'session','path':S+'SESSION.md','status':'review_required','depends_on':[old['latest_session']],
 'full_sources':full,'source_hashes':{p:sha((ROOT/p).read_bytes()) for p in full},
 'scope':'Final current-owner pointer correction after actual R036 research; no new math experiment.',
 'cognition_status':'NOT_CERTIFIED_FULL_LOAD','native_status':'NOT_RUN'}
 state['review_due']=old['review_due']+[SID]
 state['local_git']['final_head']='See actual Git HEAD and external revision37 delivery report; research round remains R036'
 # Keep actual last-research pointer, active queue, all old records and all unresolved items unchanged.
 memory=(ROOT/'MEMORY.md').read_text().replace('# MEMORY · revision36 · RESUMED_BY_USER','# MEMORY · revision37 · RESUMED_BY_USER；最后实质研究R036',1)
 memory=memory.replace('## 当前认识的唯一使用方式',f'最新治理Session `{SID}`，完成最后一次current段交叉核查；实际研究仍R036。所有旧checkpoint保留。\n\n## 当前认识的唯一使用方式',1)
 frontier=(ROOT/(P+'FRONTIER.md')).read_text().replace('# FRONTIER · revision36','# FRONTIER · revision37（研究R036）',1)
 resume=(ROOT/(P+'RESUME.md')).read_text().replace('# RESUME · revision36','# RESUME · revision37',1)
 resume=resume.replace('最新session `S-RES-20260911-036-TRANSITION-ABSTRACTION`',f'最新治理session `{SID}`，最后实际研究 `S-RES-20260911-036-TRANSITION-ABSTRACTION`',1)
 lessons=(ROOT/(P+'LESSONS.md')).read_text()+'\n## R037 · current段必须真正同步\n\n初次入口更新后仍须回读旧current Verdict与历史版本段落；不依靠顶部新摘要覆盖相反指令。已提交checkpoint不改写，后续修正另存新版本；本次37只是治理复核，不计作新数学成果。\n'
 session=f'''# {SID}

沿同一用户恢复请求完成最终current-owner交叉核查。精确修正见OWNER_REVIEW.md与OWNER_REVIEW.json，改前全文在r037-before。

checkpoint36已真实提交，保留原Session/STATE/代码/测试；本轮37没有新增数学实验或证明，最后实际研究仍R036。原{len(old['records'])}项记录逐值不变，新增本Session。load政策与引擎不变；不认证全业务认知或原生HoTT。

后续继续依MEMORY/FRONTIER及R036完整论文，不再执行R035的历史暂停，也不把旧三问v3或RP-B01历史优先级当当前指令。
'''
 vals={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':js(state),S+'SESSION.md':session}
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'Same explicit user request to align current cognition and resume; final consistency pass, no additional mathematical claim.',
 'files':[{'path':p,'text':t,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,t in vals.items()]}
 out('PAYLOAD.json',payload);out('DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False));out('COMMIT.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=True))
 after=rt.plan(ROOT);out('AFTER.json',after)
 try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
 except rt.CognitionError as e:
  assert str(e)=='STALE_BASE';out('STALE.json',{'error':str(e),'writes':False})
 else:raise AssertionError('stale accepted')
 assert all(state['records'][k]==v for k,v in old['records'].items())
 out('SUMMARY.json',{'revision':37,'last_research':'R036','old_records_unchanged':len(old['records']),'records':len(state['records']),
 'current_owner_review_completed':True,'core_historical_sources_unchanged':True,'full_cognition':'NOT_CERTIFIED',
 'documents':len(after['documents']),'bytes':after['total_bytes']})
 print(js({'revision':37,'last_research':'R036','records':len(state['records']),'changed_owners':list(changes),'checkpoint':'COMMITTED'}))
if __name__=='__main__':main()
