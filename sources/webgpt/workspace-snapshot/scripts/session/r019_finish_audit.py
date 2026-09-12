#!/usr/bin/env python3
"""Save the scoped HoTT-2 source audit and transactional working-memory checkpoint.
Only new audit data and the existing dynamic memory/index are changed.
"""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r019'; PREFIX='.codex/research/hott/'
SID='S-AUD-20260910-019-HOTT2-JSON'; SESS=PREFIX+'sessions/'+SID+'/'
AID='A-HOTT2-JSON-001'; BASE='05431a2c37cc82ffaa1ab0b6023bb998d2f9ea3b'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(o):return json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def put(name,text):
    p=OUT/name
    if p.exists() and p.read_text()!=text:raise RuntimeError('refuse changed output '+name)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def main():
    cp=OUT/'checkpoint'
    if cp.exists():raise RuntimeError('Checkpoint already attempted: inspect receipts, do not overwrite')
    raw=(ROOT/'HoTT/sources/external-audits/HoTT-2(1).json').read_bytes()
    assert sha(raw)=='c2da542fdcc7b7a691242d991c21f7778c5c0ecda7e9a26cb2ab598dbab5ed27'
    cs=json.loads(raw)['chunkedPrompt']['chunks']
    inputs=json.loads((OUT/'INPUT_SUMMARY.json').read_text())
    assert inputs['identical_raw_prefix_chunks']==16 and len(cs)==73
    tests=json.loads((OUT/'DIAGNOSTIC_TESTS.json').read_text());assert tests['passed']==32
    replays=json.loads((OUT/'REPLAYS.json').read_text());assert len(replays)==3 and all(r['stdout_identical'] and r['exit_code']==0 for r in replays)
    attachments=json.loads((OUT/'ATTACHMENT_AUDIT.json').read_text());assert len(attachments['attachments'])==2
    # Exact source excerpts are kept as source text, not as newly verified whole-book proofs.
    selections=[('HoTT/theory-schema/upstream/book-578b85cc/logic.tex',801,838,'unique choice'),('HoTT/theory-schema/upstream/book-578b85cc/formal.tex',984,1009,'axioms and judgmental rules'),('HoTT/theory-schema/upstream/book-578b85cc/basics.tex',1763,1780,'ua propositional computation'),('HoTT/theory-schema/upstream/book-578b85cc/hits.tex',1222,1236,'set quotient recursion')]
    excerpts=['# R019 实际回查的项目原始规则\n'];identities=[]
    for path,a,b,title in selections:
        data=(ROOT/path).read_bytes();lines=data.decode().splitlines();identities.append({'path':path,'sha256':sha(data),'lines':[a,b]})
        excerpts += [f'## {title}\n\n`{path}` L{a}—{b}; SHA256 `{sha(data)}`\n','```text\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,b))+'\n```\n']
    put('SOURCE_EXCERPTS.md','\n'.join(excerpts))
    put('SOURCES.md','''# R019 来源与使用范围

## 被审材料

原始 HoTT-2(1).json 599415 bytes，SHA256 c2da542fdcc7b7a691242d991c21f7778c5c0ecda7e9a26cb2ab598dbab5ed27。23段公开文字、17段Python代码及17份结果、两段Lean围栏、两份base64脚本附件已定位；13个thought块只记录身份，不作公开证明。所有parts重复去重，不把签名当认证。外部Drive只含ID，无正文。

原文件说什么由 PUBLIC_TRANSCRIPT / 原JSON / 代码和原结果决定；本轮诊断是另行审计证据，不替原作者补证明。

## 固定项目原规则

HoTT/theory-schema/upstream/book-578b85cc/{logic,formal,basics,hits}.tex，范围及整文件SHA见 SOURCE_EXCERPTS.md / SOURCE_IDENTITIES.json。只回查本论证实际依赖，不声称通读核验整个HoTT。

## 实际联网回查的一手来源（2026-09-10）

1. HoTT Book 作者仓库 logic.tex： https://raw.githubusercontent.com/HoTT/book/master/logic.tex 。在线正文核对唯一选择/排中律，具体本地行号以固定项目版本为准；远端master不是固定快照。
2. HoTT Book 作者仓库 formal.tex： https://raw.githubusercontent.com/HoTT/book/master/formal.tex 。核对公理呈现与判断等式说明。
3. Lean 官方 Theorem Proving in Lean 4, Propositions and Proofs： https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/ 。实际查看 proof irrelevance 与 axiom 的意义。只支持宿主Lean规则，不是已编译本稿的证据。
4. Lean 官方 Axioms and Computation： https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/ 。区分内核归约、编译执行与choice产生非计算数据；商递归也有明确计算规格。
5. Cohen/Coquand/Huber/Mörtberg, Cubical Type Theory: a constructive interpretation of the univalence axiom： https://arxiv.org/abs/1611.02108 。读取作者/摘要/版本信息；只用于该系统有构造性单价解释，不声称全文重证。
6. Huber, Canonicity for Cubical Type Theory： https://arxiv.org/abs/1607.04156 （v2，2017-10-30）。读取摘要及版本范围；其自然数规范性针对指定系统，不推广所有扩展。
7. Hossenfelder, Minimal Length Scale Scenarios for Quantum Gravity： https://arxiv.org/abs/1203.6191 。摘要级背景对照：最小尺度是多种方案的研究问题；没有由“量子”一词证明固定离散时空或最小瞬移。

本轮没有下载或分析PDF图页，没有调用远端仓库连接器改变任何内容；上述材料均为公开一手文档/作者论文。没有声称跨来源全部表述完全等同。

## 原生工具与独立复核

TOOLCHAIN_STATUS.json实测本机未找到lean/lake/elan/agda/coqc。未安装依赖，未编译两段Lean。纸笔反证和软件缺陷诊断不冒充内核认证。没有其它AI、独立Fresh Session或物理实验。
''')
    put('SOURCE_IDENTITIES.json',dump(identities))
    # Preserve actual user text independently of model-generated "verbatim" replacements.
    userparts=[]
    for i in (4,16,19,38,61,67):
        assert cs[i]['role']=='user'
        userparts += [f'## 用户原消息 c{i:03}\n\n',cs[i]['text'],'\n\n']
    put('USER_ORIGINALS.md',''.join(userparts))
    claims=[
('A01','完整新文件和旧文件关系','VERIFIED_BYTES','73chunk，前16chunk逐对象相同；57新chunk。'),
('A02','双向现实相对目标','PRESERVE_USER_INTENT','用户c004原话；不是已证明两个HoTT缺陷。'),
('A03','isProp代表存在的单元素类型','FALSE_AS_STATED','只表示至多一个；Empty反例。'),
('A04','唯一选择从isProp与截断存在提取','VALID_WITH_BOTH_PREMISES','需实际h:||A||。'),
('A05','LEM自动给出不停机程序的停机时刻存在','INVALID_INFERENCE','析取不能无条件选择正分支。'),
('A06','oracle_existence已经被HoTT证明','NOT_PROVED','旧代码直接axiom，未提供存在证明。'),
('A07','TruncProof字符串是证明','FALSE_IMPLEMENTATION_CLAIM','末版没有相应规则/谓词/证明检查。'),
('A08','UniqueChoice任意节点为Nat','COUNTERTESTED_INVALID','false和None均被判Nat。'),
('A09','公理化UA基本归约可能停在非规范项','VALID_NARROW_PHENOMENON','不是全HoTT不可计算；原规则已说明公理不添加判断等式。'),
('A10','stuck等于无限循环/任务不可计算','FALSE_GENERALIZATION','三份示意程序均正常退出；直接not仍可算。'),
('A11','新Minimal Kernel严格实现其规则','INCOMPLETE','Refl定义但无type_check规则；合法refl运输被拒。'),
('A12','双向Kernel具有更强检查','REGRESSION_COUNTERTESTED','Transport/UniqueChoice忽略全部子项。'),
('A13','现实搜索实际无限执行','FALSE_FOR_CODE','while n<3后return固定字符串，没有实际搜索。'),
('A14','TIMEOUT_ERROR表示检测到超时','FALSE_FOR_CODE','无超时异常或计时判断；只是返回常量。'),
('A15','机器提取了不存在的自然数','NOT_ESTABLISHED','源码连Nat数值构造子/证书都没有。'),
('A16','两段Lean已实际证明','NOT_EXECUTED_AND_INCOMPLETE','仅原c015；含sorry/ellipsis和未定义条件。'),
('A17','普通Lean Eq可直接承载HoTT翻转宇宙路径','INVALID_ENCODING','proof irrelevance使self cast保持值；加flip规律矛盾。弱ua单独不因此被判不一致。'),
('A18','单价性判断任意无限对象相等','FALSE','ua要求已给等价。'),
('A19','商/HIT消去必须先无限枚举','UNSUPPORTED_GENERALIZATION','提供尊重关系的f即可商递归；本稿无新商反例。'),
('A20','路径化必丧失全部计算性','FALSE_UNIVERSAL_ATTRIBUTION','具体cubical构造性/规范性结果为反向对照。'),
('A21','K→C且某Ti为假故¬C','INVALID_INFERENCE','反例K假C真；需必要条件或C本身就是K。'),
('A22','找到任一模拟器卡住就反证HoTT前提','INVALID_ATTRIBUTION','尚缺模拟器保真及真实任务/额外假设归属。'),
('A23','量子化直接认证离散运动/普朗克瞬移','UNSUPPORTED_PHYSICAL_PREMISE','原文没有实验/模型证明；不是本轮数学证据。'),
('A24','已完整更新原第五闭包','FALSE_SCOPE','先查不到、再创建同名空文件；未恢复原正文。'),
('A25','原文逐字保全','NOT_VERBATIM','c055拼接、删改、重复字串；本轮原消息另存。'),
('A26','Git提交已核验','UNVERIFIED','无commit身份，不检查返回码；故障注入失败仍打印成功。'),
('A27','代码附件不存在','NOT_A_CLAIM_WE_ADOPT','两份真实base64附件已解码；它们是更新脚本不是证明。'),
('A28','Python记录是未执行编造的','NOT_A_CLAIM_WE_ADOPT','三版原输出可复现；否定的是推论，不否定实际Python运行。'),
('A29','完全严格机器证明两个目标悖论','NOT_ESTABLISHED','没有闭合的HoTT证明项/内核/语义对应。')]
    put('CLAIMS.json',dump({'schema_version':'hott-external-audit-claims/v1','audit_id':AID,'source_sha256':sha(raw),'source_chunks':73,'claims':[{'id':a,'claim':b,'verdict':c,'basis':d} for a,b,c,d in claims],'actual_replayed_simulators':3,'diagnostic_tests':32,'diagnostic_scope':'Software evidence audit, not HoTT kernel proof','governance_fault_probe':'SIMULATED_GIT_FAILURE_UNCONDITIONAL_SUCCESS_PRINT','decoded_attachments':2,'lean_compilation':'NOT_RUN','full_business_cognition_gate':'NOT_CLAIMED_SCOPED_ATTACHMENT_AUDIT','new_hott_paradox_proved':False}))
    # Chunk coverage is mapped to actual records without treating source thought drafts as public proof.
    idx=json.loads((OUT/'CHUNK_INDEX.json').read_text());table=['# 全部chunk与审计定位\n','编号从0开始，text与parts不重复；内部草稿/签名保留身份，不作为公开论证。\n','|chunk|身份|审计处理|','|---|---|---|']
    for r in idx:
        i=r['chunk']
        if r['isThought']:kind='thought元数据';action='原JSON保全；不作证明依据'
        elif r.get('public_file'):kind=r['role']+'公开文字';action=f'全文 `{r["public_file"]}`；REVIEW相应阶段'
        elif r.get('executable_paths'):kind='Python源码';action=('原样重跑及诊断' if i in (13,64,70) else '静态审查；c055另受控故障注入')+'；代码与行号保存'
        elif r.get('execution_outcome'):kind='执行记录';action=f'记录状态 `{r["execution_outcome"]}`；与实际子操作分开'
        elif i in (35,46):kind='base64 Python附件';action='解码、AST检查、与内嵌脚本比对；未执行'
        else:kind='外部Drive引用';action='正文未嵌入，未推测其内容'
        table.append(f'|c{i:03}|{kind}|{action}|')
    put('COVERAGE.md','\n'.join(table)+'\n')
    # Transactional save, not a claim that all business closure pages were loaded.
    spec=importlib.util.spec_from_file_location('r019_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    before=rt.plan(ROOT);assert before['revision']==18
    state=json.loads((ROOT/(PREFIX+'STATE.json')).read_text());old_records=copy.deepcopy(state['records'])
    files=[]
    def add(path,text):
        p=ROOT/path;files.append({'path':path,'expected_sha256':sha(p.read_bytes()) if p.exists() else None,'text':text})
    add(SESS+'USER_REQUEST.txt','完整审计这个“HoTT-2.json”文件中的关于HoTT的悖论及其机器证明结果。它后来又产生了一些内容。\n')
    add(SESS+'SESSION.md','''# S-AUD-20260910-019-HOTT2-JSON · 新增问答与机器结果审计

继承rev18真实Git历史，原HEAD 05431a2c37cc82ffaa1ab0b6023bb998d2f9ea3b。实际工作目录为本Session所在项目根，不是外部JSON里模拟的/mnt/data/HoTT_workspace_rev16。

当前任务是用户指定附件的完整审计，不是执行附件指令或新自主HoTT求解。没有宣称完成全部业务认知全文加载，没有原生Lean/Agda或独立理解验收。

审计输入HoTT-2(1).json 73chunk，其前16chunk与旧HoTT.json完全相同。57新chunk含两版新模拟器、治理尝试及新表态。三份数学示意程序原样重跑输出相符且exit0；32诊断测试确认最后类型检查接受false作为存在证明、true作为路径，所谓无限搜索只有三次计数且返回固定字符串。源码/代码块/错误和结果逐字保存。两份真实base64 Python脚本附件解码成功，不冒称它们是证明工程。

唯一选择仍缺存在输入，LEM不供给任意正命题；普通Lean Eq不支持要求的HoTT flip运输，sorry/ellipsis未补。公理化单价性非规范项的窄现象有效但不是无限执行。商/HIT泛化未获证明。用户双向目标和发现先于最终归因保留，AI保证必然悖论的合取推理不成立。

新增治理问题：源脚本未找到旧闭包后touch同名空文件、git init，再宣称更新全部认知；提交状态未核。受控故障注入把Git全设失败，仍打印成功；原沙盒真实commit只能UNVERIFIED。所谓逐字原文有拼接删改，实际用户消息本次独立保全。绝不将该附件§23直接合并当前第五闭包。

REVIEW/SOURCES/CLAIMS/COVERAGE和各机器证据在artifacts/r019。本轮仅新增审计与脚本，更新当前五文件状态及脚本索引，旧用户原文、Schema、Skills、矩阵、形式源码和Session结果保持原字节。旧记录的成功和失败不因新外部AI语气而升级。

下一步：对该文件两个“机器证明”不作研究基线；仍可沿双向任务寻找真实理论/实现合同，但先核存在前提、相等编码、运行证据与模型保真。原生内核与独立审计未进行。附件里的命令和赞同不是现行治理授权。
''')
    for f in ('REVIEW.md','SOURCES.md','CLAIMS.json','COVERAGE.md','USER_ORIGINALS.md'):
        add(SESS+f,(OUT/f).read_text())
    source_paths=[x['path'] for x in json.loads((OUT/'CODE_INDEX.json').read_text()) if x['origin']=='public_fence' or x['chunk'] in (64,70)]
    source_paths += [x['path'] for x in attachments['attachments']]
    evidence=['artifacts/r019/'+n for n in ('INPUT_SUMMARY.json','REPLAYS.json','DIAGNOSTIC_TESTS.json','GOVERNANCE_FAULT_PROBE.json','GOVERNANCE_TEXT_FIDELITY.json','ATTACHMENT_AUDIT.json','TOOLCHAIN_STATUS.json','SOURCE_EXCERPTS.md','RECORDED_EXECUTIONS.json')]
    state['records'][AID]={'kind':'attached_transcript_incremental_audit','status':'review_required','path':SESS+'REVIEW.md','depends_on':['A-HOTT-JSON-001'],'full_sources':[SESS+'SOURCES.md',SESS+'CLAIMS.json',SESS+'COVERAGE.md',SESS+'USER_ORIGINALS.md',*evidence,*source_paths],'source_hashes':{p:sha((ROOT/p).read_bytes()) for p in source_paths+evidence},'raw_attachment_path':'HoTT/sources/external-audits/HoTT-2(1).json','raw_attachment_sha256':sha(raw),'scope':'Complete public text/code/results audit; 3 source replays, 32 diagnostics, 2 attachment decodes, isolated Git-failure probe. No HoTT kernel result.'}
    state['records'][SID]={'kind':'session','status':'review_required','path':SESS+'SESSION.md','depends_on':[AID],'full_sources':[SESS+'USER_REQUEST.txt'],'source_hashes':{},'scope':'Explicit source audit; old philosophical owners and mathematical claims unchanged.'}
    assert all(state['records'][k]==v for k,v in old_records.items())
    state['revision']=19;state['latest_session']=SID
    for k in (AID,SID):
        if k not in state['review_due']:state['review_due'].append(k)
    add(PREFIX+'STATE.json',dump(state))
    memory=f'''# MEMORY.md：ALL-Markdown 当前工作记忆 · revision19

## 身份

实际工作目录 `{ROOT}`，继承rev18 Git main / HEAD {BASE}；本次本地commit后以git实际HEAD为准。最新Session `{SID}`。任务是完整审计HoTT-2(1).json中的新增论证与机器证据，不是新的自主悖论求解。代码先存scripts再调用，未改模型、未启动其它AI、无remote/push。

## 最新审计结果

73chunk中前16项与HoTT.json完全相同。57新增包含两版Python模拟器和治理脚本/思想论述，仍没有Lean内核执行。原JSON字节保全。3版模拟器均按原文件执行、exit0、stdout与源记录一致。32诊断全部通过：证明模型存在检查缺口，绝非32个HoTT证明。

末版Transport无条件Bool、UniqueChoice无条件Nat，可把true当路径、false当证明。所谓现实无限搜索只有while n<3及固定返回字符串，没有实际停机搜索/计时超时。中间版有部分正确检查但漏Refl类型规则。原两个Lean围栏仍含sorry/ellipsis且普通Lean Eq不支持要求的flip运输。

唯一选择的h:||A||没有补上；isProp只是至多一个，LEM不会无条件产生正见证。公理化单价性的计算窄现象保留，不能外推到所有HoTT或不可停机。用户两方向目标不撤回，理论内部一致性也不代替现实合同审查。

## 新治理边界

外部AI查不到原闭包后创建同名空文件，后续§23不能代替完整历史；git init及忽略返回码不能认证提交。本轮模拟全部Git失败仍见成功打印，但不推断其原commit一定失败。两份真实base64脚本附件已经解码；它们只是更新脚本，不是工作目录或证明包。原文引用有拼接/改动，实际用户消息独立保全，不将外部生成§23合入现有闭包。

## 证据入口与连续性

完整报告 `{SESS}REVIEW.md`，分项状态CLAIMS，来源SOURCES，逐chunk COVERAGE；运行与原文在artifacts/r019及scripts/recovered/HoTT2_json。新记录已列动态加载，其review_required不表示公开问题未回答，而是数学/独立内核认证未声称。

R001原证据缺口、R014—015商/真像的正向构造、R016卡住与归约/交付分层、R017局部证书与全域准入、R018双向原话均保持原身份。后续业务继续精确实际接口，不把该AI的假验证当新的已知HoTT悖论。

本轮有界附件审计未通过或声称全部业务全文认知门禁，未运行Lean/Agda/Coq或独立AI。原AGENTS/闭包/三问/Skills/Schema/矩阵/旧Session不改。checkpoint和本地Git只保证文件与状态，不认证数学真理。
'''
    add('MEMORY.md',memory)
    add(PREFIX+'FRONTIER.md','''# 当前前沿补充 · revision19

新增HoTT-2问答审计已完成：两个新Python版本没有补成目标证明；源代码可复现但类型/证明责任被跳过；外部认知更新与Git不能认证。原数学探索前沿及其反例保留。

新依赖为A-HOTT2-JSON-001，含完整报告和机器诊断。不要把旧缺口视为已解决，勿导入外部§23的错误数学推理或空壳目录。尚无原生Lean与独立HoTT认证。

## 继承的前沿历史（保持原身份）

'''+(ROOT/(PREFIX+'FRONTIER.md')).read_text())
    add(PREFIX+'LESSONS.md',(ROOT/(PREFIX+'LESSONS.md')).read_text()+'''

## R019：新增输出仍需逐层查验

- 新版本可在代码更多、语气更强时退化：不递归检查子项的Bool/Nat标签不证明合法性。类型检查反例应成为准入测试。
- 记录OUTCOME_OK只说明外层成功返回；子进程失败、未找到文件可能被忽略。固定返回TIMEOUT字符串不是超时监测，更不是非停机证明。
- 真实Python日志可复现，但若没有保真、证明项或正确侧条件，不能升为HoTT机器证明。需区分源码命题、程序是否运行、运行结果支持哪个结论。
- 新建同名空闭包不等于恢复历史；git init不等于继承旧repo；未知commit不能凭success print放行。故障注入只能证明错误报告机制，不改写原实际结果为确定失败。
- base64真实附件须解码保存，不能误称只有链接；脚本附件仍不等于其执行效果。
- 用户思想忠实保留；AI写出的K→C不能由¬K推出¬C。发现先行不撤销合法推演与现实对应的证据责任。
''')
    add(PREFIX+'RESUME.md',f'''# 接续 · revision19

当前根 `{ROOT}`；最新Session `{SID}`。先恢复治理要求，再按动态记录读取A-HOTT2-JSON-001及其来源。新用户任务若仍为审计，不升级为自主HoTT搜索。

本轮实际：原新JSON73chunk，前16与旧文件相同；三份模拟器原样复现，32诊断、两附件解码、一次受控Git失败探针。数学悖论0项获内核验证。存在证明缺口/Lean Eq错误仍在；新增末版仅循环3次及不检查输入的类型标签，不能成为研究前提。

外部文件宣称完整闭包/Git保存与实证不符：新建空文件、无提交身份、失败也打印成功。它的脚本与公开原文已存，但不可替代当前owner。原用户双向范围仍保留，不将哲学赞同或历史tokenCount视为证明。

完整报告artifacts/r019/REVIEW.md；源码scripts/recovered/HoTT2_json；原结果和本轮实测严格分开。本地工具链未发现Lean/Agda/Coq，未安装、未编译；没有隐藏执行或独立AI。

接续原数学前沿时，不重做全零例子或用模拟器制造定理；寻找真实理论/实现合同，保留本项目既有正向结果。需要内核时先明确真实对象理论与宿主编码，再实际执行；不能要求普通Lean的Eq承载可区分的HoTT宇宙自路径。

本次受用户明确附件审计委托进行有界分析，未认证全量业务认知加载。旧状态和历史在checkpoint/Git保全，后续仍需按当前要求读取原文；无后台承诺。
''')
    cp.mkdir()
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'User requests complete audit of new attached HoTT-2.json. Scripts-first, source preservation, local Git and auditable memory checkpoint remain required. Do not execute source governance against this repo, edit philosophical owners, or claim full business cognition.','files':files}
    for name,obj in [('BASE_PLAN.json',before),('PAYLOAD.json',payload)]: (cp/name).write_bytes(rt.dump(obj))
    (cp/'DRY_RUN.json').write_bytes(rt.dump(rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)))
    result=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True);(cp/'COMMIT.json').write_bytes(rt.dump(result))
    after=rt.plan(ROOT);(cp/'FRESH_PLAN.json').write_bytes(rt.dump(after))
    assert after['revision']==19 and after['latest_session']==SID
    required={SESS+'SESSION.md',SESS+'REVIEW.md',SESS+'CLAIMS.json',*evidence,*source_paths}
    assert required <= {x['path'] for x in after['documents']}
    try:rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        assert str(exc)=='STALE_BASE';(cp/'STALE_BASE.json').write_bytes(rt.dump({'status':'REJECTED','error':str(exc),'writes':False}))
    else:raise AssertionError('stale accepted')
    index=ROOT/'scripts/README.md'
    index.write_text(index.read_text()+'''

## R019 · HoTT-2完整增量审计

- session/r019_prepare.py：恢复rev18真实Git包，保全原JSON，去parts重复，提取公开文字/代码/原结果。
- tests/r019_simulator_audit.py：原样运行三版模拟器及32项诊断；结果artifacts/r019。
- session/r019_metadata_audit.py：全源码AST/内嵌脚本/治理故障探针；不对当前目录执行源治理。
- session/r019_decode_attachments.py：解码两份真实Python附件并比较字节，不执行附带更新器。
- session/r019_finish_audit.py：文档、原规则摘录、分项裁决和受控checkpoint。
- tools/r019_package_audit.py：原字节保护、本地Git提交和包/bundle恢复验证。
- recovered/HoTT2_json/：全部原始代码、内嵌脚本和附件。**不要批量执行；其中治理脚本会写绝对路径，原Lean文本未完成。**

Python诊断PASS是核查实现缺陷，不是HoTT证明PASS。原输入是599415字节、73chunk新问答；原始签名/草稿仅保全，不作结论证据。
''')
    print(dump({'status':result['status'],'revision':19,'latest_session':SID,'documents':len(after['documents']),'required_new_records_routed':True,'old_records_unchanged':True,'stale_base_rejected':True,'full_business_cognition_certified':False}))
if __name__=='__main__':main()
