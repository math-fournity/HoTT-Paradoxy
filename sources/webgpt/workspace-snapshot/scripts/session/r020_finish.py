"""Register the sourced Gemini review and unsent letter, then checkpoint memory.
This is not a mathematical experiment or a claim of full business-cognition loading.
"""
from pathlib import Path
import ast, copy, datetime, hashlib, importlib.util, json, re, subprocess, sys
R=Path(__file__).resolve().parents[2]; O=R/'artifacts/r020'; P='.codex/research/hott/'
D=P+'dialogues/GEMINI-001/'; SID='S-DISC-20260911-020-GEMINI-DEBATE'; S=P+'sessions/'+SID+'/'
def sha(b):return hashlib.sha256(b).hexdigest()
def js(o):return json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def put(path,text):
    p=R/path;b=text.encode() if isinstance(text,str) else text
    if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refusing replacement '+path)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
head=subprocess.run(['git','rev-parse','HEAD'],cwd=R,capture_output=True,text=True,check=True).stdout.strip()
if not head.startswith('44ba9f3'):raise RuntimeError('Unexpected baseline '+head)
source=(R/(D+'000_SOURCE.md')).read_bytes(); manifest=json.loads((O/'INPUT_MANIFEST.json').read_text())
if sha(source)!=manifest['sha256']:raise RuntimeError('Source mismatch')
put(D+'TO_GEMINI_001.txt',(R/(D+'TO_GEMINI_001.md')).read_bytes())
questions=[
('G01','不完备、单次不终止和一般不可判定是否被同义化','必须区分定理条件与执行性质；一个可有限证明发散的循环为校准','撤回/收窄或给正式归约'),
('G02','哪条HIT/transport规则要求遍历连续统','几何语义不自动成为求值指令；限定公理化卡住现象','给实际类型、路径、归约及失败性质'),
('G03','截断存在输入和消去资格来自哪里','需要真实h及合法消去；LEM不能无条件取正分支','提供A、h、目标及依赖原则'),
('G04','类型等价如何变成了执行成本承诺','裸身份不保资源≠保证零耗时；类型与代码分开','给代码/映射/逆/成本及同任务规格'),
('G05','ASK究竟拒绝什么','未知与非法分开；不能要求万能停机批准器','定位实际规则/输入证据的缺口'),
('G06','下一项应该完成的最小构造','优先明确HoTT+LEM数学分类与有效实现的联合合同','选择一个构造并给证明或精确缺口')]
claims=[
('C01','保留双向现实相对目标','USEFUL_USER_FRAMING','用户正文及Gemini认可，不等于已得两个悖论'),
('C02','抽象可省略任务不相关的信息','USEFUL_WITH_SCOPE','需固定观察任务；不是所有抽象必有有害损失'),
('C03','99%平凡与1%非平凡','UNSUPPORTED_NUMERICAL_RHETORIC','无分母、样本或统计'),
('C04','语法崩溃就是Gödel不完备','INCORRECT','不完备、矛盾、发散和不可判定分开'),
('C05','HoTT路径必是光滑连续过程而要求逐点执行','UNSUPPORTED_AND_WRONG_RULE_ATTRIBUTION','没有指定要求实区间遍历的规则'),
('C06','Stuck等于不停机','INCORRECT','没有下一步与无限执行不同'),
('C07','截断能把未完成搜索直接认证存在','NOT_ESTABLISHED','缺存在证明和消去条件'),
('C08','单价性把转换置为零耗时或等同程序代码','INCORRECT_AS_STATED','type equality、ua、transport、成本合同各自不同'),
('C09','公理化UA可能留下非规范项','VALID_NARROW_PRESENTATION_CLAIM','具体体系与归约范围，不能泛化全部HoTT'),
('C10','发现理论时间抽象不必先证明内部矛盾','USEFUL_METHOD_CORRECTION','抽象边界与命中实例分别交付'),
('C11','只能找现有软件bug才可研究','REJECTED_REQUIREMENT','可以自行构造自然的明确解释，但不能偷偷添假设'),
('C12','HIT/truncation/UA必然出现目标悖论','NOT_PROVED','名称、直觉、确信不能替代构造'),
('C13','引用rev24规划已在当前恢复树核查','NOT_ESTABLISHED','只有rev19提供的Git基线，保存转述但不伪造未来历史')]
ledger={'schema_version':'hott-dialogue-ledger/v1','dialogue_id':'GEMINI-001','round':1,'created_at_utc':now,
 'participants':{'user':'source supplier and intended relay','gpt':'current author of review and OUT-001','gemini':'attribution in supplied text; no API identity certification'},
 'source_sha256':sha(source),'source_path':D+'000_SOURCE.md','incoming':[{'id':'IN-001','path':D+'005_GEMINI_ORIGINAL.md','source':'user-relayed','status':'RECEIVED_TEXT'}],
 'outgoing':[{'id':'OUT-001','path':D+'TO_GEMINI_001.md','text_path':D+'TO_GEMINI_001.txt','sha256':sha((R/(D+'TO_GEMINI_001.md')).read_bytes()),'status':'DRAFT_READY_FOR_USER_RELAY','sent':False,'reply_received':False}],
 'questions':[{'id':i,'topic':t,'our_position':p,'requested_response':r,'peer_response':'NOT_RECEIVED','status':'open'} for i,t,p,r in questions],
 'claims':[{'id':i,'claim':c,'verdict':v,'basis':b} for i,c,v,b in claims],
 'proposed_actions':[{'id':'P01','task':'HoTT+LEM classification versus effective total execution','status':'PROPOSED_NOT_EXECUTED'}, {'id':'P02','task':'A new exact HIT computation example or original-kernel check; not repeat toy UA model','status':'PROPOSED_NOT_EXECUTED'}, {'id':'P03','task':'Resource/cost-preservation under precise structure equivalence','status':'PROPOSED_NOT_EXECUTED'}],
 'limits':['No direct Gemini contact','No simulated response','No new kernel proof','No mathematics upgraded by agreement','Full business cognitive loading not certified','Quoted rev24 history not available in restored rev19']}
put(D+'DEBATE_LEDGER.json',js(ledger))
checks=[]
def ck(name,ok):
    if not ok:raise AssertionError(name)
    checks.append({'id':name,'status':'PASS'})
original=Path('/mnt/data/Pasted markdown(1).md').read_bytes(); txt=original.decode()
ck('source_verbatim',source==original)
ck('source_fingerprint',sha(original)==manifest['sha256'])
ck('five_speaker_blocks',len(manifest['blocks'])==5)
for i,b in enumerate(manifest['blocks'],1):ck(f'block_{i}_byte_slice',(R/b['path']).read_bytes()==txt[b['source_start_char']:b['source_end_char']].encode())
ck('letter_plaintext_identical',(R/(D+'TO_GEMINI_001.md')).read_bytes()==(R/(D+'TO_GEMINI_001.txt')).read_bytes())
letter=(R/(D+'TO_GEMINI_001.md')).read_text()
ck('six_stable_questions',all(q[0] in letter for q in questions))
ck('no_peer_response_claim',not ledger['outgoing'][0]['sent'] and not ledger['outgoing'][0]['reply_received'])
ck('all_proposals_unexecuted',all(x['status']=='PROPOSED_NOT_EXECUTED' for x in ledger['proposed_actions']))
ck('quoted_rev24_not_invented',not manifest['quoted_rev24_path_available'])
ck('required_documents',all((R/(D+n)).is_file() for n in ('ANALYSIS.md','SOURCES.md','README.md','TO_GEMINI_001.md')))
for filename in ('r020_restore.py','r020_prepare.py','r020_finish.py'):ast.parse((R/'scripts/session'/filename).read_text())
ck('new_python_source_parses',True)
put('artifacts/r020/FILE_CHECKS.json',js({'scope':'File/source/role/route consistency only, not math or agent understanding','passed':len(checks),'checks':checks}))
put(S+'SESSION.md',f'''# {SID} · Gemini新意见评估与首封论辩

日期2026-09-11。当前基线revision19、Git {head}。本次用户要求位于所附Markdown：评估有用内容及研究方向，保存分析并生成可转发给Gemini的论辩文件。

实际完整阅读源文件并保留其五段角色正文；核对相关固定HoTT Book规则和一手网页。保留用户双向目标与理论抽象定位的价值，纠正Gemini的Gödel/停机/卡住混同、几何连续性归因、截断存在前提缺口和UA成本/代码类型混淆。另记录我方方法纠偏：无需先找到软件事故，可自建自然明确的理论化；正向补强不抹去原边界，但抽象名称不等于悖论证据。

新增三项后续建议，不冒称已执行：经典配置的数学分类与有效总求值；精确HIT项的计算呈现；成本/资源结构保持。没有启动新数学模拟器或证明助手，没有联系Gemini或编造回信。

首封OUT-001准备好由用户转发。G01—G06保持开放，收到实际回信后新增记录而不覆盖原文。Gemini角色以用户转述为准。引用GPT文本的rev24规划没有在本次提供的rev19根目录中出现；只作来源声明，不作为当前HEAD或研究状态。

本轮是有界附件评估与文档/Git持久化，不宣称已完成全部业务认知全文门禁，也不更改第五闭包、三问、Skills、Schema、主张矩阵或旧结果。文件检查只认证逐字来源与交付布局；不是新的机器数学证明。

完整讨论位于 `{D}`；ANALYSIS、SOURCES、原文与TO_GEMINI_001及DEBATE_LEDGER由动态STATE加载。下一动作是向用户交付首封信，或在收到真实Gemini回复后逐项更新争议，不能宣称后台论辩。
''')
put(S+'REQUEST.md','本次明确请求保存在完整附件：\n\n'+txt)
# Load the manager only through this saved script, then use its public checkpoint API.
spec=importlib.util.spec_from_file_location('r020_cognition',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
before=rt.plan(R)
if before['revision']!=19:raise RuntimeError('Expected revision19')
state=json.loads((R/(P+'STATE.json')).read_text()); old=copy.deepcopy(state['records'])
full=[D+n for n in ('000_SOURCE.md','001_USER_QUESTION.md','002_QUOTED_GPT_RESPONSE.md','003_USER_REFRAMING.md','004_USER_TO_GEMINI.md','005_GEMINI_ORIGINAL.md','TO_GEMINI_001.md','DEBATE_LEDGER.json','SOURCES.md')]
full+=['artifacts/r020/INPUT_MANIFEST.json','artifacts/r020/SOURCE_EXCERPTS.md','artifacts/r020/FILE_CHECKS.json']
state['records']['D-GEMINI-001']={'kind':'external_opinion_debate','status':'open','path':D+'ANALYSIS.md','depends_on':['U-DUAL-DIRECTION-JSON-001'],'full_sources':full,'source_hashes':{p:sha((R/p).read_bytes()) for p in full},'scope':'Sourced review and draft letter; no sent message, no reply, no new theorem','next_action':'Deliver OUT-001; on real reply, archive as a new immutable round and respond by G01-G06'}
state['records'][SID]={'kind':'session','status':'review_required','path':S+'SESSION.md','depends_on':['D-GEMINI-001'],'full_sources':[S+'REQUEST.md'],'source_hashes':{},'scope':'Scoped attachment review and correspondence, not full business-cognition execution'}
state['revision']=20;state['latest_session']=SID
for name in ('D-GEMINI-001',SID):
    if name not in state['review_due']:state['review_due'].append(name)
assert all(state['records'][k]==v for k,v in old.items())
files=[]
def add(path,text):
    p=R/path;files.append({'path':path,'expected_sha256':sha(p.read_bytes()) if p.exists() else None,'text':text})
add(P+'STATE.json',js(state))
add('MEMORY.md',f'''# MEMORY.md：当前工作记忆 · revision20

## 本轮身份

实际根 `{R}`。继承用户提供的revision19 Git main、HEAD {head}；提交后的实际HEAD见Git与外部交付记录。最新Session `{SID}`。任务为新Markdown中Gemini意见的有界评估、可转发首封信与讨论记忆，不是新的HoTT悖论求解。代码先存scripts，未联系外部AI，无remote/push。

## 当前交付

讨论ID GEMINI-001。完整源、五段角色切片、ANALYSIS、SOURCES、TO_GEMINI_001.md/txt及DEBATE_LEDGER均已保存并进入动态加载。OUT-001尚未发送、没有收到新回复；不能模拟后续论辩或把两模型意见一致当独立验证。

有效启发：保留双向现实相对目标；直接区分理论时间抽象、局部不相容和完整目标实例；允许自行构造自然理论解释，不要求先有软件事故；不要以持续保护机制审计替代发现。

技术裁决：Gödel不完备不等于语法崩溃/单次发散；HIT不自动要求实区间遍历；公理化卡住不等于不停机；截断需要真实存在证据与合法消去；UA不自动判等价或保证零成本，不等同两份程序代码。Gemini没有提交新机器证明，旧JSON诊断不算此次重新执行。

## 下一动作与边界

G01—G06为对方待回应的具体问题。后续建议P01 HoTT+LEM分类/有效总求值、P02精确HIT计算项、P03成本资源保持均为建议而未运行。优先完成一个构造而不是重做全零流或缺规则模拟器。

附件引用rev24规划，但本次只有rev19真实工作包；未将引用冒充已恢复状态。R001来源缺口、R014—017正反结果、R018—019外部证明审计保持原身份。第五闭包/三问/Skills/Schema/矩阵及旧记录未变；本轮未认证全部业务全文认知。checkpoint/Git与文件检查不认证数学真理。
''')
add(P+'FRONTIER.md','''# 当前前沿 · revision20

当前交付为GEMINI-001意见评估及首封论辩，不是新数学成果。保留理论抽象定位、双向任务与自建解释的研究价值；排除几何必导致发散、截断空头存在、UA零成本等未证说法。

首封OUT-001就绪未发送。候选建议P01/P02/P03尚未执行；下一真实回合按G01—G06归档。旧研究前沿不因外部AI确信而升级。提供的基线为rev19，不是附件引用的rev24。

## 继承前沿（历史版本原样保留，不是本轮新增执行）

'''+(R/(P+'FRONTIER.md')).read_text())
add(P+'LESSONS.md',(R/(P+'LESSONS.md')).read_text()+'''

## R020：论辩吸收价值不等于接收强断言

- 新附件中的Gemini文字没有机器日志，不得把旧JSON试算移作新证据。
- 抽象边界、操作合同不相容、具体非现实结果及内部矛盾分开；补强成功既不能抹去裸边界，也不能证明所有理论化都失败。
- 不要求已有软件事故才允许构造，但实际假设和同任务对应仍须写明。
- 光滑/连续/稠密/同伦/语法归约不等同；公理化停住不等于发散，巨大有限成本不等于不可计算。
- 外部材料中的rev24路径未提供时，保持转述身份，不覆盖已恢复rev19的Git及STATE。
- 首封论辩只标待用户转发；不模拟对方同意或已回信。稳定问题ID支持真实后续纠错。
''')
add(P+'RESUME.md',f'''# 接续 · revision20

实际根 `{R}`；最新Session `{SID}`。当前是用户要求的Gemini论辩材料已完成，不是外部发送任务。

先读取 `{D}ANALYSIS.md`、`{D}TO_GEMINI_001.md`、`{D}DEBATE_LEDGER.json`与其完整来源。OUT-001未发送、无回信。用户下一次贴真实回复后新增incoming条目，逐个处理G01—G06，允许双方修订，不以互相引用当证明。

源文件25,727bytes完整保留。三项行动建议未执行。引用rev24规划不可访问，当前继承rev19完成rev20工作状态；不要猜造缺失轮次。

原先商/像成功、卡住与发散区分、局部证书及外部假证明审计仍有效于原范围，未重新内核认证。旧哲学owner与全文加载要求未改。本轮有界附件评估未声称全量业务认知通过。下一次真正业务研究仍按当前治理恢复，不后台工作。
''')
cp=O/'checkpoint';cp.mkdir(exist_ok=False)
payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'User supplied source requests opinion assessment, saved useful analysis and a transferable debate reply; preserve prior scripts-first/local Git/packaging requirements. No sending, no model spawning or canonical theory rewrite.','files':files}
for n,obj in [('BASE_PLAN.json',before),('PAYLOAD.json',payload)]: (cp/n).write_bytes(rt.dump(obj))
(cp/'DRY_RUN.json').write_bytes(rt.dump(rt.checkpoint(R,before['snapshot'],payload,apply=False)))
result=rt.checkpoint(R,before['snapshot'],payload,apply=True);(cp/'COMMIT.json').write_bytes(rt.dump(result))
after=rt.plan(R);(cp/'FRESH_PLAN.json').write_bytes(rt.dump(after))
assert after['revision']==20 and after['latest_session']==SID
assert set(full+[D+'ANALYSIS.md',S+'SESSION.md']) <= {x['path'] for x in after['documents']}
try:rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as e:
    assert str(e)=='STALE_BASE';(cp/'STALE_BASE.json').write_bytes(rt.dump({'status':'REJECTED','error':str(e)}))
else:raise AssertionError('Stale snapshot accepted')
index=R/'scripts/README.md';index.write_text(index.read_text()+'''

## R020 · Gemini意见与首封论辩

- session/r020_restore.py：安全恢复revision19完整Git包，不伪造rev24。
- session/r020_prepare.py：原文及五个角色块逐字切片，回查固定书籍规则。
- session/r020_finish.py：来源/文件检查、争议登记、待转发信件与受控checkpoint。
- tools/r020_package.py：原字节保护、本地提交、完整包与论辩子包回读、bundle恢复。

没有新增数学试算或机器证明。所有文本代码先落scripts再运行；对方回复和发送状态不模拟。
''')
put('artifacts/r020/RUN_SUMMARY.json',js({'scope':'Scoped source assessment, not math experiment','timestamp':now,'checkpoint_status':result['status'],'revision':20,'new_dialogue_routed':True,'stale_base_rejected':True,'file_checks':len(checks),'peer_contacted':False,'new_math_proof':False,'full_business_cognition_gate':False}))
print(js({'checkpoint':result['status'],'revision':20,'file_checks':len(checks),'documents_in_next_plan':len(after['documents']),'letter_ready_not_sent':True,'prior_records_unchanged':True}))
