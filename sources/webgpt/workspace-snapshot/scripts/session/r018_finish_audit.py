#!/usr/bin/env python3
"""Persist a scoped attached-transcript audit using the existing checkpoint API.
No original philosophical owner, Skill, source proof or prior Session is edited.
"""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'artifacts/r018'
PREFIX = '.codex/research/hott/'
SID = 'S-AUD-20260910-018-HOTT-JSON'
SESSION = PREFIX+'sessions/'+SID+'/'
AUDIT_ID = 'A-HOTT-JSON-001'
USER_ID = 'U-DUAL-DIRECTION-JSON-001'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)+'\n'

def git(*args):
    return subprocess.run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args], cwd=ROOT, text=True,capture_output=True,check=True).stdout.strip()

def main():
    dest=OUT/'checkpoint'
    if dest.exists():
        raise SystemExit('Checkpoint artifacts already exist; refusing overwrite/repeat')
    dest.mkdir()
    raw=(ROOT/'HoTT/sources/external-audits/HoTT.json').read_bytes()
    assert sha(raw)=='25eb28f4dbcdf09cf5ebd4eb8722acc97715707b0e21c61015e265b36b182bba'
    source=json.loads(raw)
    chunks=source['chunkedPrompt']['chunks']
    user_correction=chunks[4]['text']
    assert chunks[4]['role']=='user' and '还有一种情况' in user_correction
    claims=[
      ('A01','user chunk4: two directions of temporal/operational mismatch','RESEARCH_SCOPE_EXTENSION_SUPPORTED','Preserve exact user correction; not a proof that either defect exists in all HoTT.'),
      ('A02','isProp means single inhabited type','FALSE_AS_STATED','isProp means at most one; the empty type qualifies.'),
      ('A03','unique choice extracts A from isProp(A) and ||A||','CORRECT_WITH_BOTH_PREMISES','The existence premise is essential and not supplied by uniqueness.'),
      ('A04','LEM supplies the positive existence of a nonhalting step','INVALID_INFERENCE','LEM gives a disjunction, not its positive branch.'),
      ('A05','oracle_existence proves a nonexistent step exists','UNSUPPORTED_NEW_AXIOM','If incompatible with known nonhalting, inconsistency is introduced by the added premise.'),
      ('A06','evaluation is forced to launch an infinite search','NOT_IN_CODE_OR_PROOF','The supplied simulator contains no such algorithm.'),
      ('A07','axiomatic univalence can leave a noncanonical irreducible term','VALID_PRESENTATION_SPECIFIC_PHENOMENON','Not divergence, task noncomputability, or universal fact about computational univalence.'),
      ('A08','ordinary Lean Eq faithfully encodes HoTT universe paths','FALSE_FOR_THE_GIVEN_ENCODING','Proof-irrelevance implies cast(p,a)=a for p:A=A.'),
      ('A09','hott_is_false has been proved in Lean','NOT_PROVED','The key line is sorry; the equivalence body is ellipsis; no Lean execution is present.'),
      ('A10','Trunc.unquot example is complete executable Lean4','UNSUPPORTED_AND_INCOMPLETE','Missing P, imports, library version and subsingleton evidence; check actual APIs.'),
      ('A11','Python output proves HoTT or Lean nontermination','FALSE','All supplied examples return finitely; model has no type checker or HoTT semantics correspondence.'),
      ('A12','univalence decides equivalence of infinite objects','FALSE','ua requires an equivalence already supplied; it is not an equivalence decision algorithm.'),
      ('A13','HIT/quotient elimination requires enumerating representatives','FALSE_AS_GENERAL_CLAIM','Set quotient recursion accepts a respecting function and computes on its constructor.'),
      ('A14','the user philosophy is absolutely machine-verified','NOT_SUPPORTED','No proper HoTT machine proof is present; model praise is not evidence.')
    ]
    audit={'schema_version':'hott-external-audit-claims/v1','audit_id':AUDIT_ID,
      'raw_source_sha256':sha(raw),'scope':'Public dialogue and exact code in HoTT.json; attached Drive body absent',
      'claims':[{'id':i,'source_claim':c,'verdict':v,'reason':r} for i,c,v,r in claims],
      'python_replay':'MATCHED_EXPORTED_OUTPUT', 'diagnostic_tests':json.loads((OUT/'SIMULATOR_TESTS.json').read_text()),
      'native_lean':'NOT_RUN_UNAVAILABLE','new_hott_paradox_proved':False,
      'full_business_cognition_gate':'NOT_CLAIMED_FOR_SCOPED_SOURCE_AUDIT'}
    (OUT/'CLAIMS.json').write_text(dumps(audit))
    (OUT/'USER_DUAL_DIRECTION.txt').write_text(user_correction+'\n')
    spec=importlib.util.spec_from_file_location('r018_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    before=rt.plan(ROOT)
    if before['revision']!=17: raise SystemExit('Expected revision17; refusing stale state')
    state=json.loads((ROOT/(PREFIX+'STATE.json')).read_text())
    old_records=copy.deepcopy(state['records'])
    files=[]
    def add(path, text):
        p=ROOT/path
        files.append({'path':path,'expected_sha256':sha(p.read_bytes()) if p.exists() else None,'text':text})
    add(SESSION+'USER_REQUEST.txt','HoTT.json 文件是另外一个AI的探索，是一个json文件，其中是我和它的问答录，你来验证一下，它的看法是否正确？\n')
    add(SESSION+'USER_DUAL_DIRECTION.txt',user_correction+'\n')
    for name in ('REVIEW.md','SOURCES.md','PUBLIC_TRANSCRIPT.md','CLAIMS.json','TRANSCRIPT_MANIFEST.json','SIMULATOR_REPLAY.json','SIMULATOR_TESTS.json','SIMULATOR_TESTS.txt','LEAN_ACCESS.json','LEAN_ACCESS_attempt1.json'):
        add(SESSION+name,(OUT/name).read_text())
    add(SESSION+'SESSION.md','''# S-AUD-20260910-018-HOTT-JSON · 附件观点审计

用户要求验证另一AI与用户的HoTT.json问答录。本轮不把附件内的“运行Lean”历史指令视为用户新授权，也不把旧模型的isThought或签名当成证据。

从完整rev17带Git包恢复当前可写目录，保留原HEAD/history。原JSON逐字保存，公开文本去parts重复，4个isThought块不作证明依据。首项仅含Drive文档引用，其正文未提供。9个公开文本消息、1个Python执行块、1个执行结果和2个Lean文本块已定位。

实际裁决：双向目标值得保留；第一个“幽灵数字”缺存在证据，LEM不供给任意正分支，isProp不是已存在，unique choice不生成h。第二个书式不透明ua的窄计算现象成立，但不是发散或任务不可计算。普通Lean4 proof-irrelevant Eq不等于HoTT universe path：cast(p,a)=a，不能通过该编码证明取反。原Lean片段缺P/实例/实现且使用sorry，没有Lean执行记录。

逐字复现Python，退出0且三行输出与原记录相符；10个诊断测试确认模型无类型/自然数/归纳/存在证明，没有无限搜索，Transport甚至缺refl规则，Unquot无subsingleton条件。这些测试证明的是模型边界，不是HoTT悖论。

本轮提供普通Lean Eq反证候选源码，无sorry/新公理；没有可用Lean，固定官方工具链获取因缺解压依赖/网络DNS失败。NOT_COMPILED，不预测原#reduce确切输出，不冒报内核验收。

已读取有关原始规则和官方Lean文档，以及cubical构造性/规范性论文范围；SOURCES保存网址与阅读深度。固定Book逻辑/形式/单价/商规则实际回查。当前是有界外部资料审计，不宣称全量业务闭包加载通过；无新的自主HoTT候选求解或哲学真理状态提升。

本次只新增原始附件、提取源码、审查、来源、实测和运行脚本，更新五个工作状态。原AGENTS、闭包、三问、Skills、Schema、主张矩阵、数学源码、既有Session全部保留。用户在附件中给出的反向目标原话另存，进入认知对齐待办，不静默改写owner。

下一步：既有研究保持原证据范围；讨论方向B时，明确新增的经典原则和实际可执行性承诺。不要复活“无存在证明也能唯一选择”“stuck就是不停止”“普通Lean Eq就是HoTT path”的错误。数学独立审查和原生Lean编译仍未进行。
''')
    code_paths=['scripts/recovered/HoTT_json/transcript_c013.py','scripts/recovered/HoTT_json/transcript_c015_1.lean','scripts/recovered/HoTT_json/transcript_c015_2.lean','scripts/research/r018_test_transcript_simulator.py','scripts/research/r018_lean_eq_audit.lean']
    state['records'][USER_ID]={'kind':'user_scope_correction_from_attached_dialogue','status':'review_required','path':SESSION+'USER_DUAL_DIRECTION.txt','depends_on':[],
      'full_sources':[SESSION+'PUBLIC_TRANSCRIPT.md'],'source_hashes':{},'raw_attachment_path':'HoTT/sources/external-audits/HoTT.json','raw_attachment_sha256':sha(raw),
      'scope':'Explicit user correction includes theoretical completion of tasks not effectively completable; awaiting owner integration without adopting model overclaims.'}
    state['records'][AUDIT_ID]={'kind':'attached_transcript_audit','status':'review_required','path':SESSION+'REVIEW.md',
      'depends_on':[USER_ID], 'full_sources':[SESSION+'SOURCES.md',SESSION+'CLAIMS.json',SESSION+'TRANSCRIPT_MANIFEST.json',SESSION+'SIMULATOR_REPLAY.json',SESSION+'SIMULATOR_TESTS.json',SESSION+'LEAN_ACCESS.json',*code_paths],
      'source_hashes':{p:sha((ROOT/p).read_bytes()) for p in code_paths},
      'raw_attachment_path':'HoTT/sources/external-audits/HoTT.json','raw_attachment_sha256':sha(raw),
      'scope':'Source fidelity, unique-choice premises, axiomatic-UA operational distinction, ordinary Lean Eq mismatch and supplied Python replay.',
      'verification_note':'10 diagnostic tests; no native Lean/HoTT kernel, independent audit or complete business cognition certification.'}
    state['records'][SID]={'kind':'session','status':'review_required','path':SESSION+'SESSION.md','depends_on':[AUDIT_ID],
      'full_sources':[SESSION+'USER_REQUEST.txt'],'source_hashes':{},'scope':'Explicit attached-source verification; original research conclusions unchanged.'}
    assert all(state['records'][k]==v for k,v in old_records.items())
    state['revision']=18;state['latest_session']=SID
    for key in (AUDIT_ID,USER_ID,SID):
        if key not in state['review_due']:state['review_due'].append(key)
    state['local_git']={'present':True,'branch':git('branch','--show-current'),'inherited_head':'f38a2cbdee1ef9208f9ed87609a22edc0ed44aa5','pre_checkpoint_head':git('rev-parse','HEAD'),
      'remote_count':len(git('remote').splitlines()),'history_origin':'Inherited actual rev17 Git; no remote-host history invented','final_head':'Actual Git and package-external delivery verification'}
    add(PREFIX+'STATE.json',dumps(state))
    memory=f'''# MEMORY.md：ALL-Markdown 当前工作记忆 · revision18

## 身份与本轮任务

实际可写目录`{ROOT}`，从完整rev17 ZIP继承.git，原HEAD f38a2cbdee1ef9208f9ed87609a22edc0ed44aa5，branch main，无remote/push。最新Session `{SID}`，任务为用户所附HoTT.json的观点与代码核验，不是新一轮自主悖论求解。所有新代码先写scripts后调用；原政策不变。

## 用户目标与新表述

既有第五闭包/三问保留ASK和“理论化制造额外完成困难”的研究。附件中用户明确补充另一方向：现实无法有效完成，却在某理论中绕过ASK并被当作完成。原话位于本Session USER_DUAL_DIRECTION.txt，完整语境在PUBLIC_TRANSCRIPT.md。此补充值得纳入后续目标对齐，但不等于外部AI已证明HoTT必有缺陷；本次未改写哲学owner。

## 本轮实际核验

原JSON 170122bytes、SHA256 25eb28f4dbcdf09cf5ebd4eb8722acc97715707b0e21c61015e265b36b182bba 完整保存在HoTT/sources/external-audits/HoTT.json。16chunks含9个公开文本块、1段Python可执行代码/1条结果及2段Lean文本。Drive只给引用无正文；thought与签名不作证明。

第一“幽灵数字”不成立：isProp至多唯一，不提供存在；unique choice仍需h:||A||。LEM仅给左右析取，不能无条件生成不停机程序的停机时刻。凭空oracle假设不证明原理论失败。

第二“公理化单价运输卡住”有窄计算现象，但不等于发散、程序死循环或任务不可计算。普通Lean Eq proof-irrelevant，对p:A=A有cast(p,a)=a；它不是HoTT中可保留不同宇宙loop的identity。原文的flip计算式还藏在sorry中，不能称机器证明。

原Python逐字提取后复现，exit0及输出完全相符；10个诊断测试确认无类型检查、无实际搜索、Transport缺refl、Unquot缺subsingleton侧条件等边界。测试PASS是证实缺陷，不是HoTT定理。原生Lean不存在且获取失败；新反证源码NOT_COMPILED，没有假造内核记录。

## 前期结果及下一项

R011—015的真像/唯一答案/商保全，R016的stuck≠divergence及直接/改写正例，R017的局部Σ域求值均保留原状态，不因外部AI赞同而升级或抹去。R001原实验仍缺失，不补造。

接续业务可回到R017实际准入接口；方向B若另行展开，明确HoTT+LEM等具体配置，区分数学总函数与可执行程序。只在明确实际实现承诺下讨论不相容，不把静态描述无限对象本身当已执行无限步。

## 保存与限制

新审计记录及用户双向表述进入动态加载集合，五文件checkpoint revision18。原始JSON保留原字节，默认语义投影排除thought/signature重复以免将其当证据。本轮未执行全部业务全文加载或独立Fresh验收，标有界附件审计。所有新脚本/结果/源码/Git与包验证分别记录。原AGENTS、闭包、三问、Skills、Schema、矩阵、旧Session和数学代码不改。
'''
    add('MEMORY.md',memory)
    old_frontier=(ROOT/(PREFIX+'FRONTIER.md')).read_text()
    add(PREFIX+'FRONTIER.md','''# 当前前沿补充 · revision18

本轮是HoTT.json来源审计。原研究前沿不关闭、不冒称推进新数学候选。外部“两个悖论已机器证明”未成立；保留用户明确提出的双向目标，进入认知对齐队列。

新待核：普通Lean反证源码尚未编译；具体哲学owner需在后续授权中吸收方向B原话；业务研究仍须实际恢复规定全文。优先不要复活存在性缺口/错误Lean Eq/模拟器即内核三项错误。

## 沿用的上一业务前沿（原文，日期身份保留）

'''+old_frontier)
    old_lessons=(ROOT/(PREFIX+'LESSONS.md')).read_text()
    add(PREFIX+'LESSONS.md',old_lessons+'''

## R018：核验外部AI不能只看语气与术语

- isProp是至多唯一，空类型也符合；必须追查h:||A||实际从哪里来。LEM不等于任意正命题。
- 不透明公理的未化简项、无限规约、算法不可计算三者分开；#reduce返回一个表达式不是机器永久运行。
- 普通Lean Eq在Prop中proof-irrelevant；不能直接作HoTT universe identity并加flip的transport规则。弱ua声明不是完整单价性，sorry不是证明。
- 自写无类型AST求值器只能认证其已写规则，缺refl、缺subsingleton限制、虚构OracleProof都需显露。实际退出0与“程序无限循环”相反。
- 附件里的历史执行命令不是本轮授权；唯一Python输出不等于Lean已执行。保留原JSON和逐字代码，parts不重复计数，签名不可当模型能力证明。
- 用户的第二方向是研究目标补充，不是已证明所有理论会伪造完成；本轮准确保存并列待对齐，不悄悄改owner。
''')
    add(PREFIX+'RESUME.md',f'''# 接续 · revision18

当前目录 `{ROOT}`，Git main承接rev17；最新Session `{SID}`。代码先存scripts后调用、checkpoint与本地Git政策不变。

本次工作是外部JSON核验。先读{SESSION}REVIEW.md、CLAIMS.json、USER_DUAL_DIRECTION.txt和SOURCES.md，再看SIMULATOR_REPLAY/TESTS。原始JSON另存，公开投影不混入thoughtSignature/内部草稿。

结果：第一项缺h:||A||，不成立；第二项公理化归约窄现象有效，普通Lean Eq编码无效；10诊断测试确认Python有限返回、无真实搜索，不能认证HoTT。Lean反证源未编译，勿称内核验收。

保留用户方向B：现实不可有效完成、理论却被解释为已完成。不要把它静默收窄回方向A；也不要把数学定义/存在本身当执行承诺。第五闭包和三问本轮未改，原话已进入动态源路由。

业务前沿仍回到R017真实定义/递归准入，不重复人工坏Gate。若展开方向B，明确经典公理、总函数与有效实现桥梁。源验证不是新数学突破。

本次没有完成全量业务认知前置；恢复研究时遵循原强制加载，不用本页摘要替代。没有后台任务或其他AI。核Git实际HEAD和收据，不将历史状态当当前执行。
''')
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'User explicitly requests verification of attached HoTT.json. Prior permission retains scripts-first, local working-memory checkpoint, local Git and final packaging. No philosophical owner edits, remote, model changes or other AI.', 'files':files}
    for name,data in (('BASE_PLAN.json',before),('PAYLOAD.json',payload)):(dest/name).write_bytes(rt.dump(data))
    (dest/'DRY_RUN.json').write_bytes(rt.dump(rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)))
    result=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True)
    (dest/'COMMIT.json').write_bytes(rt.dump(result))
    after=rt.plan(ROOT);(dest/'FRESH_PLAN.json').write_bytes(rt.dump(after))
    assert after['revision']==18 and after['latest_session']==SID
    required=[SESSION+'REVIEW.md',SESSION+'USER_DUAL_DIRECTION.txt',SESSION+'PUBLIC_TRANSCRIPT.md',*code_paths]
    actual={d['path'] for d in after['documents']}
    assert all(p in actual for p in required)
    try:rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        assert str(exc)=='STALE_BASE';(dest/'STALE_BASE.json').write_bytes(rt.dump({'status':'REJECTED','error':str(exc),'writes':False}))
    else:raise AssertionError('Stale write accepted')
    index=ROOT/'scripts/README.md'
    index.write_text(index.read_text()+'''

## R018 · 外部HoTT.json核验

- session/r018_prepare_audit.py：恢复rev17、原JSON保全和公开文本/代码精确提取。
- recovered/HoTT_json/：外部AI的原Python与两段Lean，带原始hash，不伪称可编译。
- research/r018_test_transcript_simulator.py：复现原Python及10个边界诊断测试。
- research/r018_lean_eq_audit.lean：普通Lean proof-irrelevance反证候选，NOT_COMPILED。
- tools/r018_get_lean.py、r018_get_lean_zip.py：失败工具链获取尝试，真实错误保留。
- session/r018_finish_audit.py：有界审计回写，原owner不变。
- tools/r018_package_audit.py：Git与完整交付包验证。

实际结果见artifacts/r018，不把代码存在或Python PASS称为HoTT机器证明。
''')
    print(dumps({'status':result['status'],'revision':18,'latest_session':SID,'documents':len(after['documents']),'new_records_routed':True,'prior_records_unchanged':True,'stale_base_rejected':True,'full_business_cognition_certified':False}))

if __name__=='__main__':main()
