"""Persist the bounded IN-005 review through the existing governance manager."""
from __future__ import annotations
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
D=P+'dialogues/GEMINI-001/'
N=D+'rounds/006/'
O=ROOT/'artifacts/r025'
SID='S-DISC-20260911-025-GEMINI-IN005'

def sha(data):return hashlib.sha256(data).hexdigest()
def text(value):return json.dumps(value,ensure_ascii=False,indent=2)+'\n'
def put(rel,value):
    path=ROOT/rel
    if path.exists():raise FileExistsError(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value if isinstance(value,str) else text(value),encoding='utf-8')
def hashes(paths):return {p:sha((ROOT/p).read_bytes()) for p in paths}
def backup(rel):
    path=O/'before'/rel
    if path.exists():raise FileExistsError(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes((ROOT/rel).read_bytes())

def main():
    incoming=(ROOT/(N+'IN-005.md')).read_bytes()
    put(N+'USER_REQUEST.md','评估Gemini的回复，看看有无可以吸收的内容？看看是否需要程序化验证一些东西再回复？\n\n这是Gemini的回复：\n\n```\n'+incoming.decode().rstrip('\n')+'\n```\n\n另外，你需要考虑和评估，是否需要给Gemini再次回信？如果需要，请你给出新的回信。\n')
    put(N+'PROVENANCE.json',{'id':'IN-005','source':'current user message, manually transcribed visible body',
        'sha256':sha(incoming),'bytes':len(incoming),'responds_to':'OUT-004','binding':'K01-K03 and exact compiler mappings',
        'provider_signed_export':False,'peer_actual_tool_execution_observed':False,'math_status_not_upgraded_by_peer_agreement':True})
    letter=(ROOT/(D+'TO_GEMINI_005.md')).read_text()
    put(D+'TO_GEMINI_005.txt',letter)
    decisions=[
        ('K01','ACCEPT_PAPER_SCOPE_NOT_KERNEL_PROOF','ReachTrap、固定点非终态、返回吸收一起支撑D1；非布尔返回2是约定，不是必要条件。'),
        ('K02','USE_AS_DEPENDENCY_PLAN_CORRECT_DECIDABILITY','总step确定不足以保证配置相等可判定；还需程序环境、有限配置、编码与往返及模拟。'),
        ('K03','ACCEPT_EMH_SPLIT_REJECT_ALLREALIZABLE_ROUTING','条件反证无需LEM；实际接口先检查Rep(f)／局部证书，不预设Πf Rep(f)。')]
    put(N+'RESPONSE_MAP.json',{'incoming':'IN-005','outgoing':'OUT-005',
        'items':[{'id':i,'verdict':v,'reason':r} for i,v,r in decisions],
        'kernel_verification':'NOT_RUN','next_optional_questions':['L01','L02'],'peer_reply_required_to_continue':False})
    put(N+'SOURCES.md','''# R025 依据与读取边界

本轮完整读取当前来信IN-005、实际OUT-004、R024编译器/测试/TECHNICAL_NOTE；根AGENTS、两Skill、治理协议、MEMORY用于当前有界任务定位。STATE由原manager解析，未声称2,237,119字节、244份动态正文全部进入上下文。

本地固定原文：HoTT/theory-schema/upstream/book-578b85cc/hits.tex §6.10；logic.tex关于命题截断、唯一选择和构造性否定。未改源码。
公开一手核对（2026-09-11）：
- https://raw.githubusercontent.com/HoTT/book/master/logic.tex ：命题层LEM与证明否定不需LEM，截断消去范围。
- https://raw.githubusercontent.com/HoTT/book/master/hits.tex ：集合商的源函数相容条件，不是AllRealizable。
- https://lean-lang.org/doc/reference/latest/ValidatingProofs/ ：指定decide拒绝、native信任边界。当前文档不是本轮原生执行收据。
- https://lean-lang.org/doc/reference/latest/Type-Classes/Basic-Classes/ ：DecidableEq与Decidable的数据职责。
- https://www.ps.uni-saarland.de/~forster/bachelor.php ：构造性计算理论与代码模拟的既有形式化背景；未导入该Coq工程，不声称独立复现。

本轮没有分析PDF，没有外部AI调用、Lean/Agda/Rocq安装或执行。公开网页仅按上述部分读取，没有为未保存网页字节声称本地SHA快照。原生验证状态来自实际工具探测，不从上一会话继承。

有限结果：TARGETED_RESULTS.json；实际stdout/stderr/退出码：TARGETED_EXECUTION.json；原31测试复现：R024_TEST_REPLAY.json。reference_step是同一作者另写的解释，不是专家独立实现。无界论证见TECHNICAL_NOTE，非由样本数量归纳。
''')
    result=json.loads((O/'TARGETED_RESULTS.json').read_text())
    summary={k:v for k,v in result.items() if k!='certificates'}
    summary.update(raw_path='artifacts/r025/TARGETED_RESULTS.json',raw_sha256=sha((O/'TARGETED_RESULTS.json').read_bytes()))
    put('artifacts/r025/TARGETED_SUMMARY.json',summary)
    ids={}
    for rel in ['scripts/research/r025_diagonal_audit.py','scripts/research/r024_diagonal_machine.py','scripts/tests/test_r024_diagonal_machine.py','scripts/session/run_logged.py']:
        ids[rel]=sha((ROOT/rel).read_bytes())
    put('artifacts/r025/EXECUTION_IDENTITY.json',{'code_sha256':ids,
        'receipts':['artifacts/r025/TARGETED_EXECUTION.json','artifacts/r025/R024_TEST_REPLAY.json'],
        'native_proof':'NOT_RUN','new_code_saved_before_execution':True})
    # Keep both current routing and historical byte evidence.
    ledger_path=D+'DEBATE_LEDGER.json';backup(ledger_path)
    ledger=json.loads((ROOT/ledger_path).read_text())
    ledger['incoming'].append({'id':'IN-005','path':N+'IN-005.md','sha256':sha(incoming),
        'received_via':'current user message','responds_to':'OUT-004','independent_identity_verified':False,
        'assessment':N+'ASSESSMENT.md','new_peer_code_or_native_result':False})
    ledger['received_rounds']=5;ledger['round']=5
    for item in ledger['outgoing']:
        if item['id']=='OUT-004':item.update(reply_received=True,reply_id='IN-005',status='USER_RELAYED_REPLY_RECEIVED')
    ledger['outgoing'].append({'id':'OUT-005','path':D+'TO_GEMINI_005.md','text_path':D+'TO_GEMINI_005.txt',
        'sha256':sha(letter.encode()),'bytes':len(letter.encode()),'responds_to':'IN-005','sent':False,
        'direct_send_performed':False,'reply_received':False,'reply_id':None,'status':'READY_FOR_USER_RELAY'})
    ledger['outgoing_count']=5
    old_questions=ledger.get('next_questions',[])
    ledger.setdefault('question_history',[]).append({'questions':old_questions,'reply':'IN-005','assessment':N+'RESPONSE_MAP.json'})
    ledger['next_questions']=[{'id':i,'introduced_in':'OUT-005','peer_response':'NOT_RECEIVED','required_to_continue_our_research':False} for i in ['L01','L02']]
    ledger['workflow'].update(status='IN005_REVIEWED_OUT005_READY',direct_contact_this_round=False,
        awaiting_peer_to_start_research=False,simulated_peer_reply=False,
        next_action='Internalize ReachTrap and FixedPointNoReturn; inspect specific Rep(f), not a presumed AllRealizable interface.',
        optional_next_peer_action='Review L01/L02 with a concrete proof or counterexample; repeated agreement is not a prerequisite.')
    ledger['updated_at_utc']=datetime.now(timezone.utc).isoformat()
    (ROOT/ledger_path).write_text(text(ledger))
    backup(D+'README.md')
    (ROOT/(D+'README.md')).write_text('''# GEMINI-001 · 当前讨论

IN-001至IN-005均由用户转述收到；OUT-004收到K01—K03的回复。OUT-005已保存待用户转发，未直接发送，没有IN-006。原文、旧信件与旧评估不变。

[本封来信](rounds/006/IN-005.md) · [评估](rounds/006/ASSESSMENT.md) · [D₁技术补充](rounds/006/TECHNICAL_NOTE.md) · [新回信](TO_GEMINI_005.md)

接受条件定理／EM_H依赖分离；原生模型证明未完成，Gemini同意不提升状态。明确T可判定的有限配置依据，非布尔返回政策不影响0/1对角律。下一接口不预设AllRealizable；具体Rep(f)或当前输入证书才是核查对象。

原31测试复现；9组新增针对性检查、8512项块对照、12份trap证书、6项突变均按范围通过。没有HoTT内核运行。讨论不等待对方继续回复，细节见DEBATE_LEDGER.json。
''')
    backup('scripts/README.md')
    with (ROOT/'scripts/README.md').open('a') as f:
        f.write('''\n## R025 · IN-005审计与D₁证据

`research/r025_diagonal_audit.py`提供独立reference_step、块对应、trap有限证书与突变检查，不是HoTT内核。原R024源码未修改。`session/r025_restore.py`、`r025_probe.py`、`r025_checkpoint.py`、`r025_plan_check.py`与`tools/r025_package.py`保存本轮恢复、环境、交接与完整交付流程。所有代码先落盘再调用，原结果不覆盖。\n''')
    spec=importlib.util.spec_from_file_location('r025_cognition',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    before=rt.plan(ROOT)
    assert before['revision']==24
    s=copy.deepcopy(json.loads((ROOT/(P+'STATE.json')).read_text()))
    s.update(revision=25,latest_session=SID)
    s['local_git'].update(inherited_head='4c71883e7c2df60f119a8c40dfb7d9a5676deef7',history_origin='Inherited rev24 full Git',final_head='Actual Git HEAD and external rev25 delivery receipt')
    sr=s['records']['D-GEMINI-001'];sr['source_hashes'].update(hashes([ledger_path]))
    sr.update(revalidation='IN-005 received; ledger updated without upgrading mathematics.',scope='Five user-relayed messages, no peer native proof.',next_action='Independent work not conditional on IN-006.')
    s['records']['D-GEMINI-OUT-004'].update(reply_received=True,reply_id='IN-005',workflow_status='USER_RELAYED_REPLY_RECEIVED')
    core=[N+'IN-005.md',N+'ASSESSMENT.md',N+'TECHNICAL_NOTE.md',N+'RESPONSE_MAP.json',N+'PROVENANCE.json',N+'SOURCES.md']
    s['records']['D-GEMINI-005']={'kind':'incoming_response_review','path':core[0],'status':'review_required','depends_on':['D-GEMINI-OUT-004'],
        'full_sources':core[1:],'source_hashes':hashes(core),'scope':'Bounded source-based review; not independent formal certification.'}
    s['records']['D-GEMINI-OUT-005']={'kind':'outgoing_research_letter','path':D+'TO_GEMINI_005.md','status':'review_required',
        'depends_on':['D-GEMINI-005'],'full_sources':[],'source_hashes':hashes([D+'TO_GEMINI_005.md']),
        'sent':False,'reply_received':False,'peer_wait_is_research_prerequisite':False}
    evidence=['scripts/research/r025_diagonal_audit.py','scripts/research/r024_diagonal_machine.py',
        'artifacts/r025/TARGETED_SUMMARY.json','artifacts/r025/TARGETED_EXECUTION.json',
        'artifacts/r025/R024_TEST_REPLAY.json','artifacts/r025/EXECUTION_IDENTITY.json']
    s['records']['V-R025-D1-AUDIT']={'kind':'targeted_local_model_audit','path':N+'TECHNICAL_NOTE.md','status':'review_required',
        'depends_on':['V-R024-DIAGONAL-COMPILER'],'full_sources':evidence,'source_hashes':hashes(evidence+[N+'TECHNICAL_NOTE.md']),
        'raw_execution_evidence':['artifacts/r025/TARGETED_RESULTS.json'],'native_hott_proof':'NOT_RUN',
        'scope':'Paper fixed-point nonreturn lemma; finite block/trace checks with deliberate mutations, not general kernel proof.'}
    s['records']['P-RP-B01'].update(next_action='First internalize ReachTrap and FixedPointNoReturn in explicit HoTT model; specific Rep(f) interface, not assumed AllRealizable.',
        scope='Conditional theorem and concrete Python prototype retained; R025 targeted audit supports code, native proof remains OPEN.')
    session_path=P+'sessions/'+SID+'/SESSION.md'
    s['records'][SID]={'kind':'session','path':session_path,'status':'review_required','depends_on':['D-GEMINI-OUT-005','V-R025-D1-AUDIT'],
        'full_sources':core+[D+'TO_GEMINI_005.md'],'source_hashes':hashes(core+[D+'TO_GEMINI_005.md']),
        'scope':'Current user-requested review and targeted verification; no full business cognition certification.'}
    s['review_due']=list(dict.fromkeys(s['review_due']+['D-GEMINI-005','D-GEMINI-OUT-005','V-R025-D1-AUDIT',SID]))
    memory=f'''# MEMORY · revision25

实际目录{ROOT}，继承revision24 Git。最新{SID}。用户转述IN-005；K01—K03对应OUT-004。OUT-005准备好未发送，无IN-006，不等待Gemini即可推进。

## 当前结论

吸收EM_H形成分类与无LEM条件反证分离；Gemini认同不等于独立证明。D₁补清有限到达非终态固定点＋返回吸收＋自然数次序的全轨迹论证。“物理层面”没有被证明。T可判定需有限配置表示，不由step确定直接推出。非布尔输出2是约定，改去trap也保持D₀/D₁。

## 本轮真实检查

原R024源码未改，31测试重新通过；新9组针对性检查通过，包括8512指令/赋值对、153前缀、42尾部、12份有限trap证书、6项人为突变识别。无反例；不等于全称HoTT编译正确性。Lean/Agda/Rocq不存在，未安装或运行。原40组燃料未知未重解释为成功。

## 下一动作

先内化ReachTrap与FixedPointNoReturn及T/编码；反射或商接口只查具体Rep(f)/局部证书的承担，不预设AllRealizable，也不重开R015已校准的标准商指控。具体自然理论化仍可自行提出，不以软件事故为普遍前置。

## 证据与范围

本轮是有界来信评估；完整动态业务集合未全文加载，未认证完整认知门禁。原闭包、三问、Skills、Schema、矩阵与旧研究字节不改；代码先scripts后执行；状态通过原checkpoint记录。原R001缺件及其它开放事项不关闭。
'''
    frontier='''# HoTT 前沿 · revision25

收敛：RP-B01条件逻辑与具体编译器已有纸笔及回归，当前缺口是原生HoTT模型对应，优先ReachTrap/FixedPointNoReturn，不再只交换“严格成立”的赞同。
探索：具体反射／提取接口可核当前b的有效依据，不用全局AllRealizable作为搜索前提；R015商规范化成功仍有效，无新证据不重开。
深层：双向现实相对目标和九方向保留。共享计算理论基准不等于HoTT独有悖论，亦不因共享而没有研究价值。

IN-005收到；OUT-005未发送。R025有9组有界检查，原生内核NOT_RUN。新意见不认证旧数学，完整认知加载未声称通过。
'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''
## R025 · 同意结论不能补齐证据；负结果要检查整个轨迹

- 到达trap只能直接约束后来；排除此前返回需要返回吸收或显式前缀论证。确定性三状态控制例显示缺假设的风险。
- 确定的step不使任意State相等可判定；本例靠自然数与有限数据表示、返回标签和有限迭代。
- 非Bool输入的工程处置不是D₀/D₁成立的必要条件，不将规范完整覆盖称为逻辑完备性。
- 具体Rep(f)与AllRealizable的量词不能混同；输入要求证书可能是正确保护，而非先验的时间越界。
- 多模型同意、同作者双解释器、有限测试、纸笔全称证明与原生内核证明分别登记。
'''
    resume=f'''# 接续 revision25

最新{SID}；先按AGENTS恢复，该文件不代替指定全文。IN-005/评估/D₁技术记录在GEMINI-001/rounds/006；OUT-005待转发，不等回信。

先看TECHNICAL_NOTE §2—4：ReachTrap＋返回吸收⇒全轨迹不返回，Config/编码/T的原生依赖。原编译器无本轮反例；新9组检查不构成原生证明。新脚本scripts/research/r025_diagonal_audit.py，原始结果artifacts/r025/TARGETED_RESULTS.json。

下一步做真实模型内化或一条具体规格→执行路径；不要继续要求反射接口声明AllRealizable，不重造全零流或缠绕故事。保留坏模型/坏实现之外的正向对照；数学状态未知项不因新来信而升级。
'''
    session=f'''# {SID}

日期2026-09-11。用户要求评估Gemini K01—K03、吸收价值、必要程序验证和回信。来源为用户当前转述，外部身份与实际阅读附件不可核验。恢复rev24完整包到{ROOT}，继承Git，无远端。

本轮完成：IN-005保全；逐项评估；D₁全轨迹纸笔补全；原31测试重跑；独立参考step与9组有限检查；OUT-005。8512项指令/赋值、12份trap证书、6项突变被识别，旧代码未改。没有新HoTT悖论或原生证明。工具探测确认无Lean/Agda/Rocq，不重复安装。

读取范围：当前来信、上一信、真实代码/测试/技术记录、治理要求与当前MEMORY；核了指定Book及官方文档。动态总集合244份2,237,119字节没有完整加载，未认证业务Skill全套前置。本轮是显式有界评估，不用摘要冒充全文。

结果：K01/K03条件判断有价值，K02依赖表需补，AllRealizable量词错误须撤回。下一动作原生ReachTrap/FixedPointNoReturn或固定函数接口证据，不等待外部回复。旧文件原证据不变，所有新代码先scripts落盘后调用。
'''
    values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':text(s),session_path:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
        'authorization':'User requests evaluation, targeted program verification, and a new reply; standing scripts-first/local Git preservation. No direct external sending.',
        'files':[{'path':k,'text':v,'expected_sha256':sha((ROOT/k).read_bytes()) if (ROOT/k).exists() else None} for k,v in values.items()]}
    put('artifacts/r025/checkpoint/BASE_PLAN.json',before);put('artifacts/r025/checkpoint/PAYLOAD.json',payload)
    put('artifacts/r025/checkpoint/DRY_RUN.json',rt.checkpoint(ROOT,before['snapshot'],payload,apply=False))
    committed=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True)
    put('artifacts/r025/checkpoint/COMMIT.json',committed)
    after=rt.plan(ROOT);put('artifacts/r025/checkpoint/AFTER_PLAN.json',after)
    expected=set(core+evidence+[session_path,D+'TO_GEMINI_005.md'])
    assert after['revision']==25 and expected<={item['path'] for item in after['documents']}
    try:rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as err:
        assert str(err)=='STALE_BASE';put('artifacts/r025/checkpoint/STALE_BASE.json',{'error':str(err),'status':'REJECTED'})
    else:raise AssertionError('Old snapshot unexpectedly accepted')
    summary={'status':committed['status'],'revision':25,'latest_session':SID,'snapshot':after['snapshot'],
        'documents':len(after['documents']),'new_core_paths_loaded_by_plan':True,
        'full_business_cognition':'NOT_CLAIMED','native_kernel':'NOT_RUN','outgoing_sent':False}
    put('artifacts/r025/CHECKPOINT_SUMMARY.json',summary);print(text(summary))
if __name__=='__main__':main()
