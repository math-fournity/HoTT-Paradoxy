#!/usr/bin/env python3
"""Persist R032 via unchanged cognition manager; no old math re-certification."""
from pathlib import Path
import copy,hashlib,importlib.util,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-004/'
SID='S-RES-20260911-032-RESTRICTED-REFLECTION'
RID='P-RESTRICTED-REFLECTION-032'
OUT=ROOT/'artifacts/r032'
def sha(b):return hashlib.sha256(b).hexdigest()
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def new(rel,t):
    p=ROOT/rel
    if p.exists():raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(t if isinstance(t,str) else js(t),encoding='utf-8')
def backup(rel):new('artifacts/r032/before/'+rel,(ROOT/rel).read_text())
def get_rt():
    spec=importlib.util.spec_from_file_location('r032_checkpoint_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m

def main():
    state0=json.loads((ROOT/(P+'STATE.json')).read_text())
    if state0['revision']!=31:raise RuntimeError('Expected revision31')
    inherited='be37ac2b5d79cebd793daff05916c7bee21c80c4'
    for rel in ['MEMORY.md',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md',P+'STATE.json',
                'HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md']:
        backup(rel)
    owner='HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md'
    prior=(ROOT/owner).read_text()
    (ROOT/owner).write_text(prior+'''
## 11. 2026-09-11 R032：受限反射、环境桥接与实际证据

实质记录：`.codex/research/hott/reviews/SELF-REFERENCE-004/PROOF_NOTE.md`。本轮选择原子/蕴含/空类型的小对象演算，构造Der的外层解释；语义函数必须取得实际公理和局部假设的实现，未把整个外层HoTT编码回对象语言。proof-producing宏带真实有限证书，展开为目标环境的普通推导，可保守；不是同一T的全域真反射或Löb前提已内化。

同逻辑签名/规则下，每项源公理的目标闭证明足以递归迁移全部源推导；任一全推导迁移反过来在单叶公理上给出这些桥接。这是两个构造性蕴含，不声称证明相关数据的互逆等价。单个证书只需used-support桥接；支持集不是原结论所有替代证明的必要条件。

安全实现拒绝将permit:P改成permit:Q以后继续返回P。两个环境各自相容；P解释为空、Q为单位给出目标不证明P的构造性反模型。但删除id:P→P后可以以λx.x桥接，未使用的公理改变不要求全部旧证明失效。故不能只靠旧accepted字段，也不能只凭整个环境哈希变化停止全部复用。

33项最终有限检查通过；初版30项也通过，主例随后移除不必要的false公理并保留版本。独立Agda共享Der/interpret/migrate/expand/noTargetP源码未编译，Python解析到Der的机器对应也未证明。官方Agda TC文档仅作真实接口对照，不作为本项目执行或全部系统安全认证。

本轮不产生新HoTT悖论，未证明标准规则强迫BAD缓存策略。下一项进入一个真正含依赖上下文/替换的最小解释，检查桥接如何需要依赖翻译和相干，不再扩大相同标签变换或对角样本。核心两文实际12块全文输出后出现压缩，349文档动态集未完整加载，保持有界局部续接身份。
''',encoding='utf-8')
    index=(ROOT/'scripts/README.md').read_text()
    (ROOT/'scripts/README.md').write_text(index+'''
## R032 · 受限反射与证书迁移

- `research/r032_restricted_reflection.py`：显式对象演算、quote/检查、依赖桥接、proof-producing展开、有限语义执行与JSON证书回读；不是HoTT内核。
- `tests/test_r032_restricted_reflection.py`：33项正反检查，保留声明域、当前目标类型和桥接闭合性。
- `research/r032_formal/RestrictedReflection.agda`：共享MLTT的Der/interpret/migrate/expand/noTargetP，无postulate/sorry；未编译。
- `tools/r032_context.py`、`r032_repair_context.py`：完整核心输出与恢复检查，.git/index运行缓存差异不被当作内容丢失；初失败原样保存。
- `tools/r032_refine.py`、`r032_finalize_note.py`：版本保全、实质例子修订和主张清单。
- `tools/r032_native_status.py`：本机工具发现，不伪造编译结果。
- `session/r032_checkpoint.py`、`tools/r032_verify.py`、`tools/r032_deliver.py`：原治理器交接与Git/ZIP恢复验证。

原始执行收据在artifacts/r032。一般迁移引理来源于结构归纳，不来源于测试量。
''',encoding='utf-8')
    rt=get_rt();base=rt.plan(ROOT);state=copy.deepcopy(state0)
    state['revision']=32;state['latest_session']=SID
    impacted=[]
    for oldrid in base['review_required']:
        rec=state['records'][oldrid]
        if rec.get('status')!='review_required':
            rec['status']='review_required';impacted.append(oldrid)
            rec['dependency_change_note']='R032 appends scoped restricted-reflection interpretation; old statements and evidence retained, not recertified.'
    sources=[R+n for n in ['REQUEST.md','PROOF_NOTE.md','SOURCES.md','PLAN.md','CLAIMS.json']]+[
        'scripts/research/r032_restricted_reflection.py','scripts/tests/test_r032_restricted_reflection.py',
        'scripts/research/r032_formal/RestrictedReflection.agda','artifacts/r032/RESULTS_V1.json',
        'artifacts/r032/TEST_V1_EXECUTION.json','artifacts/r032/CONSTRUCTION_V1_EXECUTION.json',
        'artifacts/r032/REFINEMENT.json','artifacts/r032/NATIVE_STATUS.json']
    hashes={rel:sha((ROOT/rel).read_bytes()) for rel in sources}
    state['records'][RID]={'kind':'scoped_research','path':R+'PLAN.md','status':'review_required',
       'depends_on':['P-PROOF-REFLECTION-031'],'full_sources':sources,'source_hashes':hashes,
       'scope':'Concrete implicational derivation interpretation, proof-producing reflection, exact axiom-bridge transfer criterion, scoped countermodels',
       'formal_status':'SCOPED_PAPER_AND_PYTHON_REPLAY_NATIVE_AGDA_NOT_RUN',
       'workflow_status':'FULL_DYNAMIC_COGNITION_INCOMPLETE_ACTUAL_COMPACTION',
       'reality_bridge':'UNSAFE_RECEIPT_POLICY_EXPLICIT_COUNTER_DESIGN_NOT_ATTRIBUTED_TO_HOTT'}
    sp=P+'sessions/'+SID+'/SESSION.md'
    state['records'][SID]={'kind':'session','path':sp,'status':'review_required',
      'depends_on':[RID,state0['latest_session']], 'full_sources':sources,'source_hashes':hashes,
      'scope':'User continues R031; prior R026/R027/R030/R031 records remain dependencies; no new external AI message.'}
    state['active']=list(dict.fromkeys([RID]+state['active']))
    state['review_due']=list(dict.fromkeys(state['review_due']+[RID,SID]+impacted))
    state['local_git'].update(inherited_head=inherited,history_origin='Inherited full revision31 Git; no reinitialization',
      pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
      final_head='See actual repository HEAD and R032 delivery verification')
    memory=f'''# MEMORY · revision32

当前工作副本 `{ROOT}`，继承revision31完整Git。最新Session：{SID}。没有新Gemini来信/发信、外部AI或Work任务。

## 问题身份和连续性
用户要求“继续”，实际推进R031留下的受限对象解释而非重做Löb。双向现实相对目标不变；不将小片段正例当成HoTT全部问题已解决，也不将自行定义的坏接口伪装成HoTT核心。原75项记录保留，R001来源缺口、R014/015正反例、R016/017、RP-B01、R026规约、R027环境、R028范围、R029/030评价覆盖与R031条件反射均保持原身份。

## R032实质差量
已构造蕴含/空类型小对象演算的Der，外层按结构递归解释，输入包含实际公理/上下文语义实现。proof-producing反射宏带真实有限证书并展开为目标普通证明，不引入全域自可靠性。固定公式语言/规则下，源公理逐项有目标闭证明⇄存在全部源推导的保公式迁移；这里是两个构造性蕴含，不是数据空间等价。

单份证书只需实际使用公理的桥接，环境变更不要求全部重做；但迁移该证书失败也不证明原结论无法另证。permit:P换为permit:Q的旧批准失配有构造性反模型；删除id:P→P后用λx.x桥接成功。没有证明标准HoTT或Agda使用“只信accepted”的BAD策略。

## 证据
完整论证在reviews/SELF-REFERENCE-004/。最终33项测试通过，初版30项亦通过，两次源码/原始日志保留；初版反例包含未使用false假设，已改成两边均有模型的示例，未改变迁移规则。Agda共享源码有Der/interpret/migrate/expand/noTargetP，原生NOT_RUN，非Python已验证整个类型论。一般结论来自纸笔归纳，不是测试计数。

## 认知范围
349份动态文档/2800802字节。第五闭包2416行与三问630行实际12块全文输出；随后真实压缩，动态全集未读完，保持有界局部续接，不认证完整业务Skill前置。不改全文加载要求，收据不等于理解。

## 下一动作
停止增加同类桥接样本。选一个最小依赖上下文/替换，将本轮非依赖公式迁移推进到实际的依赖翻译或相干责任。工具可用时编译现有共享Agda并核解析器对应，不虚构已运行。RP-B01原生程序模型仍OPEN；不等待Gemini。
'''
    frontier='''# HoTT前沿 · revision32

## 当前进展
R031问题已落实到具体有限对象演算和外层解释。proof-producing宏保守；环境源公理的目标证明与全证明迁移存在两个构造性转换。单证书支持依赖充分，但不是所有替代证明的必要条件。旧批准不能代替当前证据；环境哈希变化也不自动使所有旧认识失效。

## 未完成
共享Agda源码未编译；Python解析/Der对应未原生证明；完整HoTT依赖语法与反射不在本模型内。BAD receipt反设计未被归属于任何实际HoTT核心接口，无新悖论认证。

## 下一最小问题
选择x:A,y:B(x)之类的受限依赖环境，固定替换σ及语义赋值，核证书迁移需什么transport/相干。已有桥接定理不能不经检查推广到改变原子/签名/依赖形成的系统。

## 旧前沿继续有效
R026规约与R027环境继续，RP-B01原生内化OPEN；R014/015、R016/017、R029—031既有正反边界不重开。不再扩大同一对角线、trap或accepted标签样本。
'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''
## R032 · 反射可以返回证明，迁移必须带适用环境

- Der是实际有限推导数据；编码provability、截断存在和Boolean accepted不是同一输入。
- 小对象理论在外层的结构解释不要求同一完整理论的全域自反射；具体语义实现α必须进入类型。
- 全证明迁移等价于逐项提供源公理的目标证明（这里只证明两个蕴含）；单证书用过的公理就够，不强加全局自证。
- used-support是该树的结构迁移充分条件，不是所有替代证明的必要条件；拒绝当前迁移不能宣布目标不可证明。
- 全环境hash是版本身份不是语义证据。不同版本可能安全复用，同名证书也可能范围已变。
- 反设计只信旧accepted字段可以失真，但未发现标准HoTT强迫此反设计。正向解释和不保真边界同时保存。
- 33项有限测试/未编译Agda不构成完整HoTT内核证明；外部Agda反射文档不作为本机执行收据。
'''
    resume=f'''# 接续 revision32

最新Session {SID}。完整恢复仍依AGENTS/两项Skill，本页不替代正文。

R032完整论证：reviews/SELF-REFERENCE-004/PROOF_NOTE.md。核心是受限Der解释、proof-producing宏展开以及环境公理桥接⇄全证明迁移；并给出used-support足够但非最小必要的区别。正反例和33项运行记录在artifacts/r032。Agda共享稿未编译，完整业务认知未通过，实际压缩/动态集合缺项已明确。

下一步固定一个依赖上下文/替换问题，查非依赖迁移定理何处需要新的依赖翻译条件；不要再次只交换公理标签或复述Löb。工具可用后核验现有Agda，严禁把源码存在作内核通过。RP-B01/R026/R027与原75项记录保留。scripts先保存后调用，本地Git不push，外部AI不是依赖。
'''
    session=f'''# {SID}

## 身份与输入
用户“继续”。继承真实revision31工作包及Git {inherited}。未调用本机WebCodex、未更改模型、未启动外部AI、未发送新信。全部新代码先保存scripts后运行。

## 实际认知恢复
已读当前AGENTS/治理Skill/业务Skill/协议/关键记忆与R031实质证明、计划、Schema。核心两文2416+630行实际分12块输出，随后实际压缩；349份动态全集未全部读入。本轮有界局部接续，不认证全业务前置。

## 已执行
恢复检查首次因git status刷新.git/index字节而失败，失败源码/记录保全；修复仅排除该运行缓存后复查1807份非Git原文件。构造受限推导解释、桥接迁移、proof-producing宏，初版30测试与最终33测试均通过，保存两个版本。最终反例源/目标分别相容；实际过滤了错类型、局部假设封装、假结论/支持集/哈希、循环语法等输入。

## 数学状态
纸笔证明完整展开小片段结构解释、宏保守性、逐公理桥接与全迁移的两个方向。没有新增HoTT内部矛盾或现实悖论。未证明所有反射实现安全，也未称标准HoTT采用BAD缓存。Agda源码无postulate/sorry但未编译，当前PATH无相关工具。Python值的任意语义类型不由本检查器认证。

## 持久化和下一步
本session经原治理checkpoint保存。只更新owner追加、scripts索引与当前五状态文件；原闭包/三问/Skills/Schema/主张矩阵/旧源码和证据不变。下一项是最小依赖上下文/替换的实质解释，不重复当前例子，不等同伴确认。
'''
    values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,
            P+'RESUME.md':resume,P+'STATE.json':js(state),sp:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
      'authorization':'User continues project research and prior scripts-first local Git persistence; bounded scope, no external mutation',
      'files':[{'path':rel,'text':text,'expected_sha256':sha((ROOT/rel).read_bytes()) if (ROOT/rel).exists() else None} for rel,text in values.items()]}
    new('artifacts/r032/checkpoint/BASE.json',base);new('artifacts/r032/checkpoint/PAYLOAD.json',payload)
    new('artifacts/r032/checkpoint/DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
    result=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True)
    new('artifacts/r032/checkpoint/COMMIT.json',result)
    after=rt.plan(ROOT);new('artifacts/r032/checkpoint/AFTER.json',after)
    actual={d['path'] for d in after['documents']}
    required=set(sources+[sp,'MEMORY.md',P+'reviews/SELF-REFERENCE-003/PROOF_NOTE.md',
                         P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'])
    if not required<=actual:raise AssertionError('Missing dependency: '+repr(required-actual))
    try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as e:
        if str(e)!='STALE_BASE':raise
        new('artifacts/r032/checkpoint/STALE.json',{'status':'REJECTED','error':str(e)})
    else:raise AssertionError('stale snapshot accepted')
    summary={'status':result['status'],'revision':after['revision'],'snapshot':after['snapshot'],
      'previous_records':len(state0['records']),'current_records':len(state['records']),
      'old_record_ids_retained':set(state0['records'])<=set(state['records']),
      'newly_flagged_old_records':impacted,'documents':len(after['documents']),
      'required_paths':sorted(required),'full_business_cognition':'INCOMPLETE','native_formal':'NOT_RUN'}
    new('artifacts/r032/CHECKPOINT_SUMMARY.json',summary);print(js(summary))

if __name__=='__main__':main()
