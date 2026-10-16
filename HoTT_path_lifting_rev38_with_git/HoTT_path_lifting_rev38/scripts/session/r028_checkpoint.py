"""Save R028 through the existing cognition runtime; retain every earlier record."""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/';D=P+'dialogues/GEMINI-001/';R=D+'rounds/008/'
SID='S-DISC-20260911-028-GEMINI-IN007';OUT=ROOT/'artifacts/r028'
def sha(b):return hashlib.sha256(b).hexdigest()
def jt(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def save(rel,x):
    p=ROOT/rel
    if p.exists():raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(x if isinstance(x,str) else jt(x))
def hs(paths):return {p:sha((ROOT/p).read_bytes()) for p in paths}
def main():
    oldstate=json.loads((ROOT/(P+'STATE.json')).read_text())
    if oldstate['revision']!=27:raise RuntimeError('Expected rev27')
    ledgerpath=ROOT/(D+'DEBATE_LEDGER.json');oldbytes=ledgerpath.read_bytes();ledger=json.loads(oldbytes)
    if ledger['latest_incoming']!='IN-006':raise RuntimeError('Unexpected prior letter')
    save('artifacts/r028/before/'+D+'DEBATE_LEDGER.json',oldbytes.decode())
    ledger.setdefault('question_history',[]).append({'questions':copy.deepcopy(ledger.get('next_questions',[])),
      'reply':'IN-007','assessment':R+'ASSESSMENT.md','note':'No new native run received; prior requests preserved, not reassigned.'})
    ledger.setdefault('incoming',[]).append({'id':'IN-007','path':R+'IN-007.md','responds_to':'OUT-006',
      'status':'RECEIVED_REVIEWED_WITH_SCOPE','source':'Current user-pasted text',
      'sha256':sha((ROOT/(R+'IN-007.md')).read_bytes()),'assessment':R+'ASSESSMENT.md',
      'peer_claims_native_execution':False,'new_native_result_received':False})
    for row in ledger['outgoing']:
        if row['id']=='OUT-006':row.update(reply_received=True,reply_id='IN-007',status='USER_RELAYED_REPLY_RECEIVED',
            delivery_evidence='User supplied actual reply; assistant did not directly send.')
    ledger.setdefault('outgoing',[]).append({'id':'OUT-007','path':D+'TO_GEMINI_007.md','responds_to':'IN-007',
      'status':'PREPARED_NOT_DIRECTLY_SENT','actually_sent':False,'required_to_continue_our_research':False,
      'purpose':'Peer synthesis and bounded closure, not worker task dispatch'})
    ledger['next_questions']=[]
    ledger['latest_incoming']='IN-007';ledger['latest_outgoing']='OUT-007'
    ledger['received_rounds']=len(ledger['incoming']);ledger['outgoing_count']=len(ledger['outgoing']);ledger['round']=7
    ledger.setdefault('answered_question_rounds',[]).append({'incoming':'IN-007','questions':[
      {'id':'M01','verdict':'Improved sketch; universal ReachTrap scope invalid for target machine; no native proof', 'review_path':R+'TECHNICAL_NOTE.md'},
      {'id':'M02','verdict':'Document expectations only; no new versioned output', 'review_path':R+'ASSESSMENT.md'}]})
    ledger.setdefault('workflow_history',[]).append(copy.deepcopy(ledger.get('workflow',{})))
    ledger['workflow'].update(status='IN007_REVIEWED_OUT007_READY_PEER_SYNTHESIS',
        collaboration_mode='PEER_DISCUSSION_NOT_DELEGATION',next_action='Independent scoped research; reopen calibration only on new substantive evidence',
        optional_next_peer_action='None required; genuine new objections or results may be discussed',
        awaiting_peer_to_start_research=False,direct_contact_this_round=False,simulated_peer_reply=False)
    ledger['updated_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    if ledgerpath.read_bytes()!=oldbytes:raise RuntimeError('Concurrent ledger update')
    ledgerpath.write_text(jt(ledger))
    idx=ROOT/'scripts/README.md';text=idx.read_text();save('artifacts/r028/before/scripts/README.md',text)
    idx.write_text(text+'''\n## R028 · IN-007量词审计与同行讨论收束\n\n- `session/r028_restore.py`、`r028_capture.py`：原Git恢复、原文与代码片段保全，不修改旧素材。\n- `session/r028_probe.py`：一次有界原生工具/官方发行地址探测，失败如实记录。\n- `research/r028_scope_checks.py`：234个有限模型和两个R024真实实例，检查全称ReachTrap的过强范围。\n- `research/r028_lean/ScopeAudit.lean`：参数化共享片段，未编译；无新axiom或sorry。\n- `session/r028_checkpoint.py`、`tools/r028_verify.py`：本轮交接与旧字节保护。\n- `tools/package_workspace.py`：复用原本地Git/ZIP/bundle恢复工具；不访问远端。\n''')
    spec=importlib.util.spec_from_file_location('r028_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    base=rt.plan(ROOT)
    state=copy.deepcopy(oldstate);state['revision']=28;state['latest_session']=SID
    head=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,text=True,capture_output=True,check=True).stdout.strip()
    state['local_git'].update(inherited_head='ba227f4e71a1ca4f0ac21dd9cdbf86fb802782d2',pre_checkpoint_head=head,
        final_head='See actual Git HEAD and R028 delivery receipt',history_origin='Inherited complete revision27; no reinitialization')
    for rid in base['review_required']:
        state['records'][rid]['status']='review_required'
        state['records'][rid]['dependency_change_note']='New peer round changes dialogue metadata; no old mathematics re-certified or source hashes silently refreshed.'
    core=[R+f for f in ['IN-007.md','USER_REQUEST.md','ASSESSMENT.md','TECHNICAL_NOTE.md','SOURCES.md']]
    ev=['scripts/research/r028_scope_checks.py','scripts/research/r028_lean/ScopeAudit.lean',
        'artifacts/r028/SCOPE_TEST_RESULTS.json','artifacts/r028/SCOPE_TEST_EXECUTION.json',
        'artifacts/r028/NATIVE_AVAILABILITY.json','artifacts/r028/NATIVE_PROBE_EXECUTION.json',
        'artifacts/r028/INPUT_PROVENANCE.json']
    state['records']['D-GEMINI-007']={'kind':'user_relayed_correspondence_audit','path':core[0],'status':'review_required',
        'depends_on':['D-GEMINI-OUT-006','V-R027-FIXEDPOINT-AUDIT','A-EARLY-GEMINI-001'],
        'full_sources':core[1:],'source_hashes':hs(core),'scope':'Bounded review; universal scope mismatch; peer predictions not execution'}
    state['records']['V-R028-SCOPE-AUDIT']={'kind':'finite_model_audit','path':ev[2],'status':'review_required',
        'depends_on':['D-GEMINI-007'],'full_sources':[x for x in ev if x!=ev[2]]+['scripts/research/r024_diagonal_machine.py'],
        'source_hashes':hs(ev+['scripts/research/r024_diagonal_machine.py']),'native_HoTT':'NOT_RUN','native_Lean_Rocq':'NOT_RUN'}
    state['records']['D-GEMINI-OUT-007']={'kind':'outgoing_letter','path':D+'TO_GEMINI_007.md','status':'review_required',
        'depends_on':['D-GEMINI-007','V-R028-SCOPE-AUDIT'],'full_sources':[D+'TO_GEMINI_007.txt'],
        'source_hashes':hs([D+'TO_GEMINI_007.md',D+'TO_GEMINI_007.txt']),
        'delivery_status':'PREPARED_NOT_DIRECTLY_SENT','directly_sent':False,'dependency_on_reply':False}
    session_path=P+'sessions/'+SID+'/SESSION.md'
    state['records'][SID]={'kind':'session','path':session_path,'status':'review_required',
        'depends_on':['D-GEMINI-007','V-R028-SCOPE-AUDIT','D-GEMINI-OUT-007','S-AUD-20260911-026-EARLY-GEMINI','P-RP-B01'],
        'full_sources':core+ev,'source_hashes':hs(core+ev),'scope':'Bounded peer review; not full business cognition certification'}
    state['review_due']=list(dict.fromkeys(state['review_due']+['D-GEMINI-007','V-R028-SCOPE-AUDIT','D-GEMINI-OUT-007',SID]))
    assert set(oldstate['records'])<=set(state['records'])
    memory=f'''# MEMORY · revision28\n\n当前工作目录`{ROOT}`，继承revision27完整Git，旧HEAD ba227f4e71a1ca4f0ac21dd9cdbf86fb802782d2。先行提交e02ab42保全恢复现场与IN-007。最新Session：{SID}。\n\n## 连续性与范围\nR024/025代码与模拟证据、R026资源/未知/规约忠实性、R027局部/全局不返回和全局环境Σ全部保留。旧R001原证据缺口、历史owner冲突与完整业务认知门禁仍开放。不是只记最新来信，也不把旧NOT_RUN改成通过。\n\n## IN-007吸收与纠正\n接受Trap命题与更强归纳不变量、普通Lean共享范围及明确未编译；M02只是预期而非日志。新错误是reach_trap量化全部State：配合返回保持，推出所有状态都非返回。该假设可描述全不返回模型，但不能对应含Returned(v)的R024，更不适用于D_h常0返回分支。实际ReachTrap仍应由Ret(h,pair(y,y),1)条件化导出。\n\n## 实测\n5组检查通过：234个1..3状态模型；20个满足全称假设的模型全部返回集合为空；相容模型/局部反例/缺返回保持对照；两个原R024编译实例分别10步返回0与11步检测固定点。一般结论为纸笔归纳，不由有限样本证明。原生Lean/Rocq/Agda未找到，一次官方Lean地址请求DNS失败；新ScopeAudit.lean未编译。\n\n## 独立工作与同行讨论\nOUT-007已准备但未直接发送。用户明确双方是共同深化认识的同行，不是相互驱动的悖论发现Worker；不设置新回信派工编号，不等待回复。现有神谕拒绝/Trap逻辑校准如无新证据不重复，不能自动重开R014/R016。\n\nRP-B01原生模型对应仍OPEN；R026规约与证据作用域探索继续。对不变/改变条件、公理签名Σ、局部上下文和实际完成证据分别核查。本文只作路由，论证在rounds/008/。本轮有界来信审计，不声称全动态业务文档已全文加载；没有模型切换、Work、外部AI或远端push。\n'''
    frontier='''# HoTT 研究前沿 · revision28\n\n## 收敛位\nRP-B01原生模型对应尚未完成；保留R024/025真实代码、R027一般条件定理和R028作用域审计。ReachTrap应针对特定编译初态，并携带源返回1前提；全称公理不能代替模型证明。工具不可用时不扩充同类有限样本来冒充认证。\n\n## 探索位：R026及Σ/作用域\n维持任务到规约、规约到执行的忠实性。当前新认识：在形式签名里扩大前提的量词范围，会让正确推导回答另一个问题。先核原输入/结束要求及证据有效范围；不自行添加数据神谕或全局不返回公理后归罪于HoTT。资源状态/epoch支线保持。\n\n## 同行讨论与退出\nIN-007已评估，OUT-007为收束性交流。没有待派工问题；外部新见解可进入，但不作为工作依赖。R014同域Done擦除与R015真像/规范形成功结果并存；R016不透明正常形不等于发散，只有新机制才重开。九方向及双向现实相对目标未收窄。\n'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''\n## R028 · 全称假设与同行讨论\n\n- 名为q_init的变量若类型只是State，仍量化全部状态；注释不提供初态/返回1的限制。全称Reach加返回保持排除全部返回态，不能作为含正常返回的机器性质。\n- 上述假设并非无条件自相矛盾；全不返回模型相容。区分假设过强、不适用与理论内部矛盾。\n- 被共同认可的定理框架仍须检查其具体实例前提；用全称公理替代ReachTrap模拟证明会把关键结论提前放入环境。\n- 未实现数据常量的#reduce/#eval预期不是新日志；oracle_halt的名字没有给出停机规格。官方Rocq诊断/占位条件按版本记录，不预填单一目标代码。\n- 双方讨论用于深化认识，不当相互派工链；短回信可以收束当前校准，不要求不断回应或推动对方发现悖论。无新证据不自动复活Done/opaque ua旧指控。\n'''
    resume=f'''# 接续 revision28\n\n最新{SID}。按治理恢复；本文件不代替指定闭包与三问全文。\n\n先读IN-007、ASSESSMENT、TECHNICAL_NOTE和OUT-007；R026/027继续在动态链中。新问题已定位为全称ReachTrap范围过强，不是新HoTT悖论。234模型及两个实际R024调用是有限审计；新Lean文件NOT_COMPILED。\n\n现有工具缺失与官方请求DNS失败已记，不重复以模拟日志填补。下一步由研究者独立选择实际模型形式化或规约/Σ有效范围实例，不等Gemini完成任务。同行若有新反例再吸收；没有新内容即可封存这一通信支线，旧记录不删除。\n\n维持scripts先保存再执行、本地Git与checkpoint。OUT-007未直接发送，无后台工作。\n'''
    session=f'''# {SID}\n\n日期2026-09-11；本轮为用户请求的有界来信审读与针对性验证。\n\n## 原始输入与保护\n从revision27完整Git包恢复到{ROOT}，实际HEAD与提供历史吻合；新来信原文/请求/两个Lean片段先行保存并提交。没有退回revision25，也没有删除R026/027。\n\n## 实际阅读\n完整读AGENTS、两项Skill、治理协议、README/MEMORY/FRONTIER/RESUME、OUT-006、本轮直接相关R027论证/Lean草稿、R026计划与R024所用机器源码。部分聚合工具输出曾截断；本轮没有宣称全量业务动态集合已全文进入上下文或已通过业务gate。没有为了本次来信启动无限重读循环；保留既有完整加载政策不变。\n\n## 工作与差量\n识别并证明Pres+∀q Reach(q)→∀q ¬Returned(q)；给出相容全非返回模型，避免误判无条件矛盾；实际检查h0/h1编译对照。M02按官方文档只认预期，工具不可用，不填写原生日志。评估新“纯核心”建议与旧R014/R015/R016正反结果的关系。写收束性的OUT-007，不派发新任务。\n\n## 实测与状态\n5组有限检查通过，234个模型、20个全称前提模型均无返回、两个R024实例。ScopeAudit.lean无新axiom或sorry但未编译；HoTT/Lean/Rocq原生验证NOT_RUN。没有新目标悖论或原创性声明，没有代替对方完成的证明。\n\n## 授权与变更\n用户要求跨轮保全、评估、必要程序验证及可选回信。沿已有scripts-first与本地Git授权，新增源码先落盘再执行。只更新台账/脚本索引和当前MEMORY/FRONTIER/LESSONS/RESUME/STATE/HEAD；不改第五闭包、三问、AGENTS、Skills、Schema、矩阵与旧研究。\n\n## 接续\n保留全部旧record及其依赖；R026规约与Σ/有效范围探索继续。RP-B01实际模型内化是独立工作，不让双方通信成为驱动器。没有真实新结果就停止重复校准，等待工具/证据变化不是等待其他AI意见。\n'''
    values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,
            P+'STATE.json':jt(state),session_path:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
             'authorization':'Current user requests preservation, bounded peer-response review, useful programmatic checks and optional reply; standing local scripts-first/Git directions retained.',
             'files':[{'path':p,'text':v,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,v in values.items()]}
    for p in values:
        if (ROOT/p).exists():save('artifacts/r028/before/'+p,(ROOT/p).read_text())
    save('artifacts/r028/checkpoint/BASE_PLAN.json',base);save('artifacts/r028/checkpoint/PAYLOAD.json',payload)
    save('artifacts/r028/checkpoint/DRY_RUN.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
    commit=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('artifacts/r028/checkpoint/COMMIT.json',commit)
    after=rt.plan(ROOT);save('artifacts/r028/checkpoint/AFTER_PLAN.json',after)
    required=set(core+ev+[session_path,D+'TO_GEMINI_007.md',D+'TO_GEMINI_007.txt',D+'TO_GEMINI_006.md',
        P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md',P+'reviews/EARLY-GEMINI-001/PLAN.md','artifacts/r026/CHECK_V1_RESULTS.json',
        D+'rounds/007/TECHNICAL_NOTE.md','artifacts/r027/FINITE_MODEL_RESULTS.json'])
    assert required <= {x['path'] for x in after['documents']}
    try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as e:
        if str(e)!='STALE_BASE':raise
        save('artifacts/r028/checkpoint/STALE_BASE.json',{'status':'REJECTED','error':str(e)})
    else:raise RuntimeError('Old snapshot wrongly accepted')
    summary={'status':commit['status'],'revision':after['revision'],'latest_session':SID,'snapshot':after['snapshot'],
             'old_record_count':len(oldstate['records']),'new_record_count':len(state['records']),
             'all_prior_records_retained':True,'required_paths':sorted(required),
             'dynamic_document_count':len(after['documents']),'full_business_cognition':'NOT_CERTIFIED_BOUNDED_REVIEW',
             'peer_dependency':False,'native_proof':'NOT_RUN'}
    save('artifacts/r028/CHECKPOINT_SUMMARY.json',summary)
    print(jt({k:v for k,v in summary.items() if k!='required_paths'}))
if __name__=='__main__':main()
