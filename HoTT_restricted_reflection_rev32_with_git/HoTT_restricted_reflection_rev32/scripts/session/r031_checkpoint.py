#!/usr/bin/env python3
"""Persist R031 through the existing cognition transaction; never recertify old proofs."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-003/'
SID='S-RES-20260911-031-PROOF-REFLECTION'
OUT=ROOT/'artifacts/r031'

def sha(data):return hashlib.sha256(data).hexdigest()
def js(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
def new(rel,data):
    p=ROOT/rel
    if p.exists():raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(data if isinstance(data,str) else js(data),encoding='utf-8')
def backup(rel):new('artifacts/r031/before/'+rel,(ROOT/rel).read_text(encoding='utf-8'))
def hashes(paths):return {p:sha((ROOT/p).read_bytes()) for p in paths}

def main():
    state0=json.loads((ROOT/(P+'STATE.json')).read_text())
    if state0['revision']!=30:raise RuntimeError('Expected revision30')
    for rel in ['MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md']:
        backup(rel)
    owner='HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md'
    backup(owner)
    old=(ROOT/owner).read_text()
    appendix='''
## 10. 2026-09-11 R031：有限校验与同理论反射不能混同

实质记录：`.codex/research/hott/reviews/SELF-REFERENCE-003/PROOF_NOTE.md`。在同一理论T的封闭证明、K、正向内省与目标固定点的明确条件下，已写出Löb变换：从T证明Box P→P得到T证明P；P取空命题且T一致时，排除其同理论一致性反射证书。Box表示编码的T可证明性，不是HoTT的||P||。本轮未完成完整HoTT的证明谓词/固定点/导出条件内化，不能将参数当作已经满足的前提。

有限证书程序实际回放21节点变换，保留FP_forward、FP_backward、Reflection三项“封闭T定理参数”，没有认证它们。局部假设禁止necessitation；不能将T+R或外部元理论中的反射冒充原T的封闭定理。10项单元测试含14类非法证书拒绝。另有P→P、Box(P→P)及Box(P→P)→(P→P)的无参数成功例。不是一遇自指就不可校验，也不是所有反射实例不可证明。

新的过程对照：固定证书校验可有限完成；若额外要求同一T先给出自身全域一致性证书，才准许这个局部动作，则在条件下阻塞来自新增的全域门槛。尚未发现标准HoTT强制该门槛；用户指定全文加载不能与这个数学全域自证混同。

Agda共享条件函数无postulate/sorry但未编译，原生工具本轮PATH未找到。两份核心文档曾11块全文输出，随后实际压缩；333文档动态全集未完成，保持有界局部记录身份。下一步固定一个较小对象片段与其外层解释，跟踪T_in/T_out及版本依赖，不再扩充同一Löb样本或等待Gemini。
'''
    text=old.replace('SCOPED REFLECTION CONSTRUCTION (R030)','CONDITIONAL PROOF REFLECTION (R031)',1)
    text=text.replace('当前问题校准：2026-09-11（§8—9）','当前问题校准：2026-09-11（§8—10）',1)+appendix
    (ROOT/owner).write_text(text,encoding='utf-8')
    backup('scripts/README.md')
    index=(ROOT/'scripts/README.md').read_text()
    (ROOT/'scripts/README.md').write_text(index+'''
## R031 · 有限证书与条件反射

- `research/r031_proof_reflection.py`：显式局部假设/封闭定理参数的有限蕴含-K4证书检查与21节点Löb条件变换；不是HoTT内核。
- `tests/test_r031_proof_reflection.py`：10项单元测试，含14类非法证书。
- `research/r031_positive_control.py`：已可证明公式的单个反射正例，无全局定理参数。
- `research/r031_formal/ConditionalLoeb.agda`：共享MLTT的参数化条件函数，无postulate/sorry；本轮未编译。
- `tools/r031_restore.py`、`r031_context.py`：归档安全恢复、实际全文输出及读取范围。
- `session/r031_checkpoint.py`：保留旧记录并用原治理器交接。
- `tools/r031_verify.py`、`r031_deliver.py`：源码/结果身份、动态路由、Git及归档恢复验证。

运行证据在 `artifacts/r031/`。任何条件BOTTOM结论都保留外部定理参数，不能作为HoTT无前提矛盾。
''',encoding='utf-8')
    spec=importlib.util.spec_from_file_location('r031_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    base=rt.plan(ROOT)
    state=copy.deepcopy(state0);state['revision']=31;state['latest_session']=SID
    impacted=[]
    for rid in base['review_required']:
        record=state['records'][rid]
        if record.get('status')!='review_required':
            impacted.append(rid);record['status']='review_required'
            record['dependency_change_note']='R031 appends explicit conditional proof-reflection scope; original source/evidence retained, not recertified.'
    docs=[R+n for n in ['REQUEST.md','PROOF_NOTE.md','SOURCES.md','PLAN.md','CLAIMS.json']]
    evidence=['scripts/research/r031_proof_reflection.py','scripts/research/r031_positive_control.py',
      'scripts/tests/test_r031_proof_reflection.py','scripts/research/r031_formal/ConditionalLoeb.agda',
      'artifacts/r031/CERTIFICATES.json','artifacts/r031/CERTIFICATE_EXECUTION.json',
      'artifacts/r031/TEST_EXECUTION.json','artifacts/r031/POSITIVE_REFLECTION.json',
      'artifacts/r031/POSITIVE_EXECUTION.json','artifacts/r031/NATIVE_STATUS.json']
    rid='P-PROOF-REFLECTION-031'
    state['records'][rid]={'kind':'scoped_research','path':R+'PLAN.md','status':'review_required',
      'depends_on':['P-SELF-REFLECTION-DOMAIN-030'],
      'full_sources':docs+evidence,'source_hashes':hashes(docs+evidence),
      'scope':'Conditional Loeb derivation with explicit fixed-point/closed-provability parameters; finite rule replay and successful limited reflection',
      'formal_status':'NATIVE_NOT_RUN_CONDITIONAL_CERTIFICATE_REPLAY_ONLY',
      'workflow_status':'FULL_DYNAMIC_COGNITION_INCOMPLETE_ACTUAL_COMPACTION',
      'reality_bridge':'EXPLICIT_EXTRA_GATE_NOT_SHOWN_FORCED_BY_HOTT'}
    sp=P+'sessions/'+SID+'/SESSION.md'
    state['records'][SID]={'kind':'session','path':sp,'status':'review_required',
      'depends_on':[rid,state0['latest_session']],
      'full_sources':docs+evidence,'source_hashes':hashes(docs+evidence),
      'scope':'Bounded local continuation; no external AI interaction; old positive and negative results retained'}
    state['active']=list(dict.fromkeys([rid]+state['active']))
    state['review_due']=list(dict.fromkeys(state['review_due']+[rid,SID]+impacted))
    state['local_git'].update(inherited_head='46a1e27c49cc81e0b43826f2a34fd4502b4fdf0d',
      history_origin='Inherited complete revision30 Git; no reinitialisation',
      pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
      final_head='See R031 delivery receipt and actual repository HEAD')
    mem=f'''# MEMORY · revision31

工作副本 `{ROOT}`，继承revision30完整Git，最新Session {SID}。本轮没有新的Gemini来信/发信/其他AI。

## 连续性
原73项记录继续保留。R001来源缺口、R014/015正反结构、R016/017计算校准、RP-B01、R026规约、R027环境、R028范围以及R029/030实际自指构造均不改。当前推进的是R030明确的下一动作，不重复代码207或Trap枚举。

## 本轮实质差量
在固定理论T、封闭necessitation、K、four和目标固定点条件下，完成纸笔Löb变换：T证明Box P→P则T证明P。取P为空命题并假设T一致，排除同T自一致性反射证书。Box是编码证明谓词而非命题截断；完整HoTT编码、固定点和导出条件尚未实例化。

有限证书检查器逐步回放21节点变换并保留三个外部封闭T定理参数，不为它们出具证明。10项测试通过，14类非法证书拒绝；5份正例中包括无参数的P→P、Box(P→P)及Box(P→P)→(P→P)。不能把局部假设变成T封闭定理再必然化，也不能把外部元理论/T+R的保证无声改成旧T的保证。

## 对原任务的意义
固定证明检查可以有限完成；若加上“先在同一T中证明全部自身可靠/一致才允许局部校验”的门槛，条件下阻塞来自新增全域责任，而非checker不会运行。尚无标准HoTT强制这种门槛的证据；不是新HoTT内部矛盾。已知Löb机制不认领原创。

## 证据和限制
完整论证在reviews/SELF-REFERENCE-003/PROOF_NOTE.md，实际日志在artifacts/r031。Agda共享参数函数未编译；本轮PATH无Agda/Lean/Rocq，未反复安装/伪造日志。第五闭包2416行/三问630行曾11块全文输出，随后真实上下文压缩，333份动态全集未全部加载。本轮仅有界局部接续，不认证完整业务Skill前置。

## 下一动作
选择一个实际受限的语法/解释片段，明确T_in/T_out，检查有限片段保证怎样在加入checker/quote或变更环境后保持/失效。不再增加同一Löb证书样本、不以同行回复为门禁。RP-B01原生模型仍OPEN，R026/027继续参与实际范围问题。
'''
    frontier='''# HoTT前沿 · revision31

## 已推进
R030的评价器覆盖问题已接到证明反射。条件Löb变换完整展开，21节点有限证书回放，局部假设非法必然化等14类错误被拒绝；已证明公式的反射有无参数正例。不是HoTT无前提矛盾或新定理。完整理论编码/固定点/导出条件与原生验证仍缺。

## 当前关键未知
真实HoTT自元理论提案究竟解释哪一片语法、在哪个外层证明可靠、覆盖范围是否被扩大？下一项固定小片段及T_in/T_out，而非再次断言“每个自指都会不返回”。

## 原前沿保留
R026规约忠实性、R027全局环境与版本有效范围继续；RP-B01原生程序模拟为未完成工程。R014/015、R016/017、R029/030的正反结果不能因新理论名称自动重开。没有Gemini回复依赖。全文门禁未通过，范围如记录。
'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''
## R031 · 证明资格也必须带着理论与上下文

- Box_T(A)是编码的T可证明性，不是||A||；唯一选择不能被直接套到Box上。
- Necessitation接受封闭T推导，不接受局部假设；外部元理论或T+R中的结果不是旧T的封闭定理。
- 条件证书的外部定理参数必须保留到最终结论，打印BOTTOM不等于HoTT无前提矛盾。
- 在固定点/K/4/N条件下，反射实例Box P→P可证明只在P可证明时；已知P的反射正例不被禁止。
- 固定有限证书校验不要求完整同理论自一致性证明。额外全域自证门槛可阻塞原任务，但未证明HoTT强制该门槛。
- 已知Löb变换不是原创发现；检验有限推导的程序不是HoTT内核。缺参数导致当前证书失败，不等于全部替代证明都不存在。
- 实际全核心正文输出后发生压缩，记录为有界续接；不把receipt当理解，不借逻辑反射边界修改用户指定的全文加载规则。
'''
    resume=f'''# 接续 revision31

最新Session {SID}。先按原AGENTS/两项Skill恢复；本页不能代替正文。

R031已完成：有限证书与同理论反射的条件Löb证明（SELF-REFERENCE-003/PROOF_NOTE），21节点规则回放，14类非法证书拒绝，已证公式反射正例。依赖FP_forward/FP_backward/Reflection均是外部封闭定理参数，绝不能以CERTIFICATES.json中的accepted当作其HoTT证明。Agda未编译；全333文档加载未完成，后有真实压缩。

接着选一个实际小对象片段的解释与范围继承，标清T_in/T_out与语法/全局环境。若要完整应用Löb于HoTT，须补真实编码与固定点/导出条件，不凭名称跳过。不要继续发信等Gemini；不重复相同评价器/Trap/Löb测试。

R029/030、R026/027以及全部旧records保留。scripts先写再调，本地Git不push。交付恢复与语义认证分别看。
'''
    session=f'''# {SID}

## 输入与恢复
用户“继续”，接续R030下一动作。提供的完整ZIP逐文件恢复，继承46a1e27c49cc81e0b43826f2a34fd4502b4fdf0d。先提交fde005c保全恢复与读取范围；研究代码、推导、原始结果再提交110778b。没有其他AI或外部任务。

## 实际工作
读取现有治理、关键认知、Schema、自指专题及R029/030实质材料。完整核心两份正文实际11块输出，随后上下文真实压缩；333份/2719483字节动态全集未全读，不认证全业务认知。

推导同理论条件Löb变换及Bottom推论，写有限证书规则检查器并真实运行10项测试、14类负例、5份成功证书。Löb的21节点例保留外部封闭定理参数；另有已证明公式反射正例。共享Agda条件函数无postulate/sorry但未编译，PATH无原生工具。外部一手文献仅定位已知结果/真实HoTT自元理论问题，不当成本项目内核证明。

## 结论与证据边界
完成的是固定条件下的推导变换与有限规则回放，不是完整HoTT自可靠性不可能的无条件证明，更不是内部矛盾。额外自证门槛可使局部任务阻塞，但标准HoTT并未被证明强制它。修改owner增加当前入口，旧闭包、三问、Skills、Schema、主张矩阵、源码和记录保持原字节。

## 下一动作
实际受限反射的T_in/T_out和环境依赖；不重做已知对角样本。RP-B01原生内化与R026规约继续保留。
'''
    values={'MEMORY.md':mem,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':js(state),sp:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
      'authorization':'User continues research and prior scripts-first local-Git persistence workflow; bounded record, no external changes',
      'files':[{'path':p,'text':t,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,t in values.items()]}
    new('artifacts/r031/checkpoint/BASE.json',base);new('artifacts/r031/checkpoint/PAYLOAD.json',payload)
    new('artifacts/r031/checkpoint/DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
    result=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True)
    new('artifacts/r031/checkpoint/COMMIT.json',result)
    after=rt.plan(ROOT);new('artifacts/r031/checkpoint/AFTER.json',after)
    required=set(docs+evidence+[sp,'MEMORY.md',P+'reviews/SELF-REFERENCE-002/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'])
    if not required<={d['path'] for d in after['documents']}:raise AssertionError('new or prior dependency absent')
    try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as e:
        if str(e)!='STALE_BASE':raise
        new('artifacts/r031/checkpoint/STALE.json',{'status':'REJECTED','error':str(e)})
    else:raise AssertionError('stale snapshot accepted')
    summary={'status':result['status'],'revision':after['revision'],'snapshot':after['snapshot'],
      'previous_records':len(state0['records']),'current_records':len(state['records']),
      'old_record_ids_retained':set(state0['records'])<=set(state['records']),
      'old_record_statuses_newly_marked_review_required':impacted,'documents':len(after['documents']),
      'required_paths':sorted(required),'full_business_cognition':'INCOMPLETE','native_formal':'NOT_RUN'}
    new('artifacts/r031/CHECKPOINT_SUMMARY.json',summary);print(js(summary))

if __name__=='__main__':main()
