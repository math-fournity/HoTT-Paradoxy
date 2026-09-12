"""Save R027 via the existing governance transaction, preserving R026 and all old records."""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
D=P+'dialogues/GEMINI-001/'
R=D+'rounds/007/'
O=ROOT/'artifacts/r027'
SID='S-DISC-20260911-027-GEMINI-IN006'
def sha(b): return hashlib.sha256(b).hexdigest()
def text(o): return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
def put(rel,o):
    p=ROOT/rel
    if p.exists(): raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(o if isinstance(o,str) else text(o))
def hashes(paths): return {p:sha((ROOT/p).read_bytes()) for p in paths}
def main():
    # Only the governance ledger/index is revised; old letters and R026 stay byte-identical.
    ledgerpath=D+'DEBATE_LEDGER.json'
    ledger=json.loads((ROOT/ledgerpath).read_text())
    put('artifacts/r027/before/'+ledgerpath,(ROOT/ledgerpath).read_text())
    ledger.setdefault('incoming',[]).append({'id':'IN-006','path':R+'IN-006.md',
        'source':'Current user-relayed visible text','responds_to':'OUT-005','status':'RECEIVED_REVIEWED_WITH_SCOPE',
        'sha256':sha((ROOT/(R+'IN-006.md')).read_bytes()),'assessment':R+'ASSESSMENT.md',
        'peer_claims_native_execution':False,'new_native_result_received':False})
    ledger.setdefault('outgoing',[]).append({'id':'OUT-006','path':D+'TO_GEMINI_006.md',
        'responds_to':'IN-006','status':'PREPARED_NOT_DIRECTLY_SENT','actually_sent':False,
        'required_to_continue_our_research':False})
    ledger.setdefault('answered_question_rounds',[]).append({'incoming':'IN-006','questions':[
      {'id':'L01','introduced_in':'OUT-005','peer_response':'IN-006','verdict':'USEFUL_SKETCH_NOT_COMPLETED; missing reachability / proof-as-type / weak IH',
       'review_path':R+'TECHNICAL_NOTE.md','required_to_continue_our_research':False},
      {'id':'L02','introduced_in':'OUT-005','peer_response':'IN-006','verdict':'EXPLICIT_INTERFACE_PROPOSAL; oracle not MP; native behavior untested',
       'review_path':R+'TECHNICAL_NOTE.md','required_to_continue_our_research':False}]})
    ledger.setdefault('r027_followup',[]).extend([
      {'id':'M01','question':'Complete source and actual native execution, with ReachTrap connected or a precise counterexample','status':'PROPOSED_NOT_DIRECTLY_SENT'},
      {'id':'M02','question':'Version-pinned actual #reduce/#eval/Extraction results, not another opaque oracle story','status':'PROPOSED_NOT_DIRECTLY_SENT'}])
    # Update descriptive latest fields if they already exist; retain historical arrays.
    ledger['latest_incoming']='IN-006'; ledger['latest_outgoing']='OUT-006'
    ledger['updated_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    ledger['direct_ai_communication']=False
    (ROOT/ledgerpath).write_text(text(ledger))
    index=ROOT/'scripts/README.md'; old=index.read_text(); put('artifacts/r027/before/scripts/README.md',old)
    index.write_text(old+'\n## R027 · IN-006, fixed-point scope and extraction\n\n- `research/r027_fixedpoint_lemma_audit.py`: seven finite-model groups; no HoTT simulation.\n- `research/r027_lean/`: ordinary Lean proof draft and isolated positive/negative interface probes; native status in `artifacts/r027/NATIVE_RUN.json`.\n- `research/r027_coq/OracleExtraction.v`: actual Rocq/Coq test source, not executed when tool unavailable.\n- `tools/r027_run_checks.py`: execute saved sources and preserve result/skip records.\n- `recovered/Gemini_IN006/`: six verbatim peer snippets, separate from corrections.\n- `session/r027_checkpoint.py`, `tools/r027_restore.py`: provenance and transactional continuity.\n')
    spec=importlib.util.spec_from_file_location('r027_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec); sys.modules[spec.name]=rt; spec.loader.exec_module(rt)
    before=rt.plan(ROOT)
    if before['revision']!=26: raise RuntimeError('Expected revision26')
    state=copy.deepcopy(json.loads((ROOT/(P+'STATE.json')).read_text()))
    old_record_ids=set(state['records'])
    state.update(revision=27,latest_session=SID)
    state['local_git'].update(inherited_head='298ebb0861358f25ff850bafb207d72ae4eccfb6',
      history_origin='Inherited complete revision26; no reinitialization',pre_checkpoint_head='07ee915',
      final_head='See actual Git HEAD and R027 external delivery receipt')
    impacted=[]
    for key in before['review_required']:
        rec=state['records'][key]
        if rec.get('status')!='review_required':
            impacted.append(key); rec['status']='review_required'
            rec['dependency_change_note']='IN-006 appended to debate ledger; original mathematical source and state not re-certified.'
    core=[R+n for n in ['IN-006.md','USER_REQUEST.md','PROVENANCE.json','ASSESSMENT.md','TECHNICAL_NOTE.md','SOURCES.md']]
    native=[str(p.relative_to(ROOT)) for p in sorted((ROOT/'scripts/research/r027_lean').glob('*.lean'))]
    native+=['scripts/research/r027_coq/OracleExtraction.v']
    evidence=['scripts/research/r027_fixedpoint_lemma_audit.py','scripts/tools/r027_run_checks.py',
      'artifacts/r027/FINITE_MODEL_RESULTS.json','artifacts/r027/FINITE_EXECUTION.json',
      'artifacts/r027/FINITE_MODEL_RECEIPT.json','artifacts/r027/NATIVE_RUN.json','artifacts/r027/TOOLCHAIN_PROBE.json']+native
    state['records']['D-GEMINI-006']={'kind':'user_relayed_correspondence_audit','path':core[0], 'status':'review_required',
      'depends_on':['D-GEMINI-OUT-005','V-R025-D1-AUDIT','A-EARLY-GEMINI-001'],
      'full_sources':core[1:]+[D+'TO_GEMINI_006.md'],'source_hashes':hashes(core+[D+'TO_GEMINI_006.md']),
      'scope':'Peer sketch acknowledged, no native proof; bounded corrections and finite controls; R026 remains active context'}
    state['records']['V-R027-FIXEDPOINT-AUDIT']={'kind':'finite_model_audit_and_native_probe_material',
      'path':'artifacts/r027/FINITE_MODEL_RESULTS.json','status':'review_required','depends_on':['D-GEMINI-006'],
      'full_sources':[p for p in evidence if p!='artifacts/r027/FINITE_MODEL_RESULTS.json'],
      'source_hashes':hashes(evidence),'native_HoTT':'NOT_RUN','native_Lean_Rocq':'NOT_RUN_TOOL_UNAVAILABLE'}
    state['records']['D-GEMINI-OUT-006']={'kind':'outgoing_letter','path':D+'TO_GEMINI_006.md','status':'pending',
      'depends_on':['D-GEMINI-006','V-R027-FIXEDPOINT-AUDIT'], 'full_sources':[D+'TO_GEMINI_006.txt'],
      'source_hashes':hashes([D+'TO_GEMINI_006.md',D+'TO_GEMINI_006.txt']), 'directly_sent':False,'dependency_on_reply':False}
    sp=P+'sessions/'+SID+'/SESSION.md'
    state['records'][SID]={'kind':'session','path':sp,'status':'review_required',
      'depends_on':['D-GEMINI-006','V-R027-FIXEDPOINT-AUDIT','D-GEMINI-OUT-006','S-AUD-20260911-026-EARLY-GEMINI','P-RP-B01'],
      'full_sources':core+evidence,'source_hashes':hashes(core+evidence), 'scope':'Bounded correspondence audit; full business cognition not certified'}
    assert old_record_ids <= set(state['records'])
    state['review_due']=list(dict.fromkeys(state['review_due']+['D-GEMINI-006','V-R027-FIXEDPOINT-AUDIT',SID]+impacted))
    memory=f'''# MEMORY · revision27

当前可写目录 `{ROOT}`。继承revision26完整Git，基线298ebb0861358f25ff850bafb207d72ae4eccfb6；先行提交07ee915已保全新来信与恢复证据。最新Session：{SID}。

## 连续性：没有退回revision25或丢弃R026

OUT-001—005、IN-001—005、R024/025代码与证明、R026早期稿件评估及六组检查全部保持原字节。R026在HoTT/AUDIT_AND_RECONSTRUCTION §3.5—3.7、C-12—C-16中的纠错和“规约忠实性/时序澄清”探索继续有效；新来信不覆盖它们。最新Gemini来信为用户真实转述IN-006，回应OUT-005；已写OUT-006但未直接发送，不等待对方回复才研究。

## 本轮结论

L01：有限Config、显式step参数有帮助，但原草图把定理证明项当作箭头左侧命题，trap参数未限制，IH需要先加强为run=q。局部从trap不返回不需要返回吸收；从真实初态全程不返回仍需ReachTrap及返回保持，不能只证明尾部。普通Lean不是原生HoTT。

L02：oracle_halt加正确性对应EM_H，不是仅MP。MP的双重否定稳定性与判定H+¬H分开。无自由局部变量不等于没有未实现全局常量；扩大公理环境后不能沿用较小计算环境的执行保证。Lean定义编译/#reduce/#eval/sorry和Rocq Extraction分别审查。官方明确拒绝/需要实现不是已经越界；没有实际原生日志就不声称VM卡住。

## 实际验证

7组有限检查通过：1..4状态的4330个确定性带返回标签模型；2165个局部固定点与1324个满足全局假设实例；两个缺前提反例、弱IH反例、较弱返回保持正例、简单可判定H的对照。模型有限不表示无界机器证明。Lean/Rocq/Agda工具不存在，官方地址访问DNS失败；7个Lean源文件与1个Coq源文件已保存但NOT_RUN。没有用Python仿造它们的预期输出。

## 当前工作

收敛仍是RP-B01：完成实际编译器ReachTrap与一般全轨迹不返回的原生对应，当前草图不认证完成。探索继续R026的真实需求到规约忠实性；新视角是规约的全局环境Σ也可能改变，闭项只是局部Γ为空，不代表所有依赖已实现。资源票号/兑现/epoch作为独立备选，两个独立线性资源可各用一次，不复活旧反例。

## 证据与未知

主入口 `{R}`；回信 `{D}TO_GEMINI_006.md`；实测 `artifacts/r027/`。R001缺原实验、历史owner冲突、上下文容量和Fresh理解问题仍开放。所有旧记录继续路由，不因新摘要升级证明状态。本轮为有界材料审计；全动态业务全集未完整加载，不声明全套Skill认知验收。无远端、无push、无其他AI。
'''
    frontier='''# HoTT 研究前沿 · revision27

## 收敛位
RP-B01保留。R024/025实现、一般纸笔反证与R027有限图检查各按原范围使用；原生ReachTrap尚缺。局部trap闭包不替代原始执行结论。共享Lean片段即便以后编译，也不自动等于HoTT全集认证。

## 探索位：延续R026
保留真实任务→规约→实际执行的忠实性探索。当前增加全局依赖环境Σ的记录：Γ为空的闭项仍可能使用数据公理。要找真实接口何时改变完成依据，不人为添加神谕再指控原构造性核心。良构、数学规格、代码实现和实际运行分轴。

## 备选与退出
资源兑现的状态/epoch与有限线性对照不丢弃。神谕拒编若只复现官方保护，就结束校准，不再换名重复；没有新证据不重开商类型/圈覆盖旧指控。九方向与双向现实相对目标不变。
'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''
## R027 · 局部证明与全局环境

- 定理的证明项不是其命题类型；用Trap定义与htrap分开表达。归纳需匹配实际不变量，不能凭“不返回”直接假设配置相等。
- 从陷阱出发不返回不需要返回吸收；要证明初态全程不返回，需ReachTrap及返回性质保持，或独立前缀证据。精确状态吸收是充分而非唯一条件。
- 普通Lean不是原生HoTT，未编译草稿不是内核证明。有限图穷举不认证全部寄存器机代码。
- 马尔可夫实例¬¬H→H不等于H+¬H；停机Bool神谕加正确性已经装入EM_H，不是没有经典原则的新来源。
- 局部闭项与可执行闭合分开：全局签名中的数据公理也必须实现。定义、编译、#reduce、#eval、Extraction的输出不同；sorry不实现神谕，默认#eval拒绝不能称无限执行。
- 新通信不能抹去R026规约探索；恢复最新完整Git及既有动态依赖，比重复新摘要更可靠。环境缺工具诚实写NOT_RUN，不再模拟原生输出。
'''
    resume=f'''# 接续 revision27

最新{SID}。先按治理恢复，本文件不是第五闭包或原论证替代。

先读IN-006、ASSESSMENT、TECHNICAL_NOTE、OUT-006及NATIVE_RUN。L01仍缺真实ReachTrap；L02只是官方边界的待原生测试校准。不要把“Gemini提供签名”写成已完成HoTT证明。普通Lean共享片段文件已保存，工具不可用未编译。

延续R026：资源、发现、规约忠实性三个问题保留，优先一个真实时序需求的两种规约及其全局环境变更。既不只搜软件bug，也不反复添加无实现公理再宣称悖论。R024/025/026原代码和结果保持字节。

OUT-006未直接发送；无需等待M01/M02答复才继续。源码均先scripts再运行。原始文件和校验详情见artifacts/r027/BASELINE.json及最终验证。所有开放问题与旧状态原样保留。
'''
    session=f'''# {SID}

日期2026-09-11。用户要求先保全既有工作再审查OUT-005的新回复，必要时程序验证并回信。

## 输入恢复
从完整R026 ZIP恢复到{ROOT}，验证包SHA与Git HEAD，未回退R025。先行本地提交07ee915保全新IN-006与原始代码，原R026独立审读继续保留。用户转述是来源身份，没有供应商签名验证。

## 实际工作
回查R025技术说明与OUT-005，完整阅读R026评估及计划。对原草图作类型/命题及归纳检查，写出局部和全初态两个论证；区分MP与EM_H，核官方Lean/Rocq执行边界。保存修正草稿和隔离测试；原生工具未找到、下载失败，未编译。实际执行7组有限图校准，不模拟Lean/Coq输出。写OUT-006回应，未直接发送。

## 结果与差量
来信方向可吸收，但尚未达到原生证明或接口实测。新增差量是把局部trap/全初态结论严格分开，指出返回谓词保持足够，以及闭项的全局环境仍可能包含未实现数据公理。这些不认证新的HoTT悖论、原子性或物理结论。

## 保全与影响
更新讨论台账及当前MEMORY/FRONTIER/LESSONS/RESUME/STATE；原文、第五闭包、三问、Skills、Schema、主张矩阵、R026审计owner与所有旧代码/证据不改。旧source_hash不以刷新掩盖影响，相关状态继续review_required。

## 读取及授权边界
本轮是有界用户材料审计与针对性程序检查。已读本任务路由、当前记忆和直接论证；全动态业务集合未全文注入，不认证完整业务认知。没有其他AI、远端提交或原主机访问；脚本先落盘后调用。

## 下一步
原生完成共享引理及实际ReachTrap对应，或执行原生接口探针获得版本日志；获得官方拒绝正例后结束同族校准。R026规约忠实性探索继续，外部AI回复不是依赖。
'''
    values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':text(state),sp:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
      'authorization':'Current user explicitly requests preservation, audit of actual IN-006, programmatic checks if useful and a reply; scripts-first and local Git standing directions retained.',
      'files':[{'path':p,'text':v,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,v in values.items()]}
    for p in values:
        if (ROOT/p).exists(): put('artifacts/r027/before/'+p,(ROOT/p).read_text())
    put('artifacts/r027/checkpoint/BASE_PLAN.json',before)
    put('artifacts/r027/checkpoint/PAYLOAD.json',payload)
    put('artifacts/r027/checkpoint/DRY_RUN.json',rt.checkpoint(ROOT,before['snapshot'],payload,apply=False))
    committed=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True)
    put('artifacts/r027/checkpoint/COMMIT.json',committed)
    after=rt.plan(ROOT); put('artifacts/r027/checkpoint/AFTER_PLAN.json',after)
    required=set(core+evidence+[sp,D+'TO_GEMINI_006.md',D+'TO_GEMINI_006.txt',
       P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md',P+'reviews/EARLY-GEMINI-001/PLAN.md',
       'artifacts/r026/CHECK_V1_RESULTS.json',D+'TO_GEMINI_005.md'])
    assert required <= {d['path'] for d in after['documents']}
    try: rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as e:
        if str(e)!='STALE_BASE': raise
        put('artifacts/r027/checkpoint/STALE_BASE.json',{'status':'REJECTED','error':str(e)})
    else: raise RuntimeError('Stale base accepted')
    summary={'status':committed['status'],'revision':after['revision'],'latest_session':SID,'snapshot':after['snapshot'],
      'old_record_count':len(old_record_ids),'new_record_count':len(state['records']),
      'no_old_records_removed':True,'r026_and_out005_in_dynamic_set':True,'required_paths':sorted(required),
      'documents':len(after['documents']),'total_bytes':after['total_bytes'],'full_business_cognition':'NOT_CERTIFIED',
      'native_HoTT':'NOT_RUN','native_Lean_Rocq':'NOT_RUN','directly_sent':False,'dependency_impacts':impacted}
    put('artifacts/r027/CHECKPOINT_SUMMARY.json',summary)
    print(text({k:v for k,v in summary.items() if k!='required_paths'}))
if __name__=='__main__': main()
