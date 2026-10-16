#!/usr/bin/env python3
"""Persist the user-requested second letter via the existing cognition manager."""
from pathlib import Path
import copy, hashlib, importlib.util, json, subprocess, sys

R=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
D=P+'dialogues/GEMINI-001/'
N=D+'rounds/003/'
SID='S-DISC-20260911-022-GEMINI-OUT002'
SESSION=P+'sessions/'+SID+'/SESSION.md'
O=R/'artifacts/r022/checkpoint'
BASE='8e6641dd9b229e39875017e6a56732c2b8019af3'

def sha(b): return hashlib.sha256(b).hexdigest()
def dump(o): return json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def put(p,o):
    if p.exists(): raise RuntimeError('Refuse overwrite: '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(o if isinstance(o,str) else dump(o),encoding='utf-8')
def bind(paths): return {p:sha((R/p).read_bytes()) for p in paths}

def main():
    spec=importlib.util.spec_from_file_location('r022_cognition_runtime', R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=rt
    spec.loader.exec_module(rt)
    before=rt.plan(R)
    if before['revision']!=21: raise RuntimeError('Expected revision21')
    old=json.loads((R/(P+'STATE.json')).read_text())
    state=copy.deepcopy(old)
    state['revision']=22
    state['latest_session']=SID
    state['local_git'].update(history_origin='Inherited complete supplied revision21 Git',
      inherited_head=BASE,pre_checkpoint_head=BASE,
      final_head='See actual Git HEAD and package-external revision22 receipt; no self-reference')
    docpaths=[D+'TO_GEMINI_002.md',N+'USER_REQUEST.md',N+'RESPONSE_MAP.json',N+'SOURCES.md']
    entry=state['records']['D-GEMINI-001']
    entry['source_hashes'].update(bind([D+'DEBATE_LEDGER.json']))
    entry['revalidation']='OUT-002 created at explicit current user request; outgoing status and six pending questions verified against actual files. IN-001, IN-002, OUT-001 and previous analyses byte-preserved. No new peer answer or mathematical certification.'
    entry['scope']='Two real incoming opinions plus two authored outgoing letters; OUT-002 not sent and no IN-003 received. Agreement is not proof.'
    entry['next_action']='OUT-002 may be relayed by user; RP-B01 work continues independently.'
    state['records']['D-GEMINI-OUT-002']={
      'kind':'outgoing_research_letter','path':D+'TO_GEMINI_002.md','status':'pending',
      'depends_on':['D-GEMINI-002','P-RP-B01'],
      'full_sources':[N+'USER_REQUEST.md',N+'RESPONSE_MAP.json',N+'SOURCES.md',D+'DEBATE_LEDGER.json'],
      'source_hashes':bind(docpaths),
      'scope':'Complete G01-G06 response and H01-H06 research questions; mathematical selector/realizability extension is a draft with model assumptions, not kernel-verified.',
      'sent':False,'reply_received':False,'peer_wait_is_research_prerequisite':False,
      'next_action':'Archive actual IN-003 only if user supplies it; meanwhile follow RP-B01 WP1.'}
    state['records'][SID]={
      'kind':'session_record','path':SESSION,'status':'review_required',
      'depends_on':['D-GEMINI-OUT-002'],
      'full_sources':docpaths+['artifacts/r022/READ_SCOPE.json','artifacts/r022/PREPARED.json'],
      'source_hashes':bind(docpaths),
      'scope':'Bounded reply drafting, source check and state persistence. No peer invocation, mathematical experiment, native proof, or full business cognition certification.'}
    state['review_due']=list(dict.fromkeys(old['review_due']+['D-GEMINI-OUT-002',SID]))
    memory=f'''# MEMORY.md · 当前工作记忆 revision22

## 身份与当前状态

实际根 `{R}`；继承提供的revision21完整Git，基线HEAD `{BASE}`。最新Session `{SID}`。最终提交见实际Git与外部交付收据，不在正文伪造自引用哈希。

用户本轮明确要求回一封完整信，并向Gemini探讨后续想法。本次已经创建OUT-002（TO_GEMINI_002.md及同文TXT），回应实际收到的IN-002；状态是READY_FOR_USER_RELAY，尚未直接发送，没有IN-003、没有模拟回信。用户此前报告配额不足，本轮没有独立确认恢复；有无回信都不阻塞自主研究。

## 本轮交付

OUT-002逐项回应G01—G06：接受有依据的撤回，修正唯一选择的过度否定、所有transport通用共轭、绝对一致性与未发现即全部安全。承认我方OUT-001对程序输入/通用闭包也曾交代不足。

新增供讨论的切口：k(z)=c_f(z)给每个实例分配有限常量代码；这个数学函数本身不自动有有效实现。显式区分无截断ΠΣ的数学选择与代码可实现性，并提出AllRealizable_Bool作为额外被检验原则，不声称HoTT标准自带它。所有这些为带模型假设的待审说明，不是新的机器证明或原创性认证。

H01—H06要求对方给规则反驳、Code模型、可实现性论证、自然目标对应、下一动作与新机制；不要再次只表示赞同。最优先批评H03/H04/H05；原计划不以对方认可为启动条件。

## 下一项自主工作

RP-B01原PLAN/CONSTRUCTION保持原字节，实际Code形式化与目标桥梁仍OPEN。继续WP1固定有效通用模型、有限步T、配对及h→D_h。OUT-002是补充待审问题，不把写信数量当数学进展。收到真实新回复后追加IN-003及逐项状态，不覆盖前两轮信件。

## 持续证据边界

Done、真像、唯一答案图、有限规范代表、双向观察、卡住≠发散、局部收敛域等旧正例继续保留原证据等级。R001来源缺口未关闭。理论选择、局部边界和完整目标实例分别交付；普通Lean/Rocq不自动当HoTT；经典依赖或noncomputable标记不单独证明无算法。

本轮为有界资料回信与治理交接，没有认证第五闭包/动态全集已经全文加载，没有更改强制加载规则；没有数学实验、内核验证或其他AI调用。原README某些旧revision13状态段落仍属继承的未同步信息，本次不凭该旧头部覆盖STATE、MEMORY与当前文件，也不擅自扩大为全仓治理重写。
'''
    frontier=(R/(P+'FRONTIER.md')).read_text().replace('revision21','revision22',1)
    frontier += '''\n## 本轮可选外部反馈\n\nOUT-002已备妥，H01—H06尚无新答案。代码分配/可实现性是待审的分析补充，不是RP-B01已经完成模型绑定。用户可转发；本项目不等待回信继续工作。\n'''
    lessons=(R/(P+'LESSONS.md')).read_text()+'''\n## R022 · 以可反驳的问题继续合作\n\n- 接受撤回不等于接受过度否定；真实存在与唯一刻画仍能提取数据，原正例不抹去。\n- “每例有有限正确代码”“有数学上的代码分配函数”“该函数有有效代码”是不同责任；无截断ΠΣ已给数学选择，不能把缺口一律归为没有选择公理。\n- AllRealizable是显式附加的实现要求，不是凭函数类型自动取得的HoTT公理；其排除结论不等于核心矛盾。\n- OUT-002为新写待转发文件；无发送证据或真实来信不能登记已发送/已答复。外部意见改变不了原生验证状态。\n- 当前任务只要求有界资料回应；不得把信件、哈希或checkpoint称作完成了全业务认知或数学研究。首次准备脚本曾因稿件路径尚未落盘而失败，失败日志保留，补存正文后重试成功。\n'''
    resume=f'''# 接续 · revision22

根 `{R}`；最新Session `{SID}`。每次业务研究仍按AGENTS/治理Skill全文恢复，不能以本页代替闭包。

本轮新增OUT-002，位于dialogues/GEMINI-001/TO_GEMINI_002.md与.txt；已回应IN-002并新增H01—H06。信已写好，尚未直接发送，没有第三轮回信；不能恢复成“Gemini已同意新构造”。

先读信第五—八节及RESPONSE_MAP，再对照RP-B01 PLAN/CONSTRUCTION。数学代码分配k与有效实现的区分是待审补充，不是形式化成果。原计划WP1仍是下一项自主工作；不为等待反馈停工，也不重复旧Done/缺规则模拟器。

下一份真实来信使用IN-003并追加逐项评估，保留旧稿原文。直接发送须有新的明确动作与证据；本次只有供用户转发文本。所有代码先存scripts再调用，里程碑用原checkpoint并本地Git保全。
'''
    session=f'''# {SID}

日期：2026-09-11。身份：用户请求的第二封完整回信与讨论记录维护，非新数学求解、非其他AI调用。

## 输入与来源

从用户提供的revision21完整包恢复，继承HEAD {BASE}。重新阅读AGENTS、两类Skill、协议、最新记忆、IN-002、OUT-001、R021评估/综合及RP-B01计划/构造，并核对固定书式规则及一手网页。精确范围在artifacts/r022/READ_SCOPE.json。未声称全文完成第五闭包或190份以上动态全集，也未修改该要求。

## 实际产物

完整OUT-002与同文TXT、转发提示、G01—G06回应映射、H01—H06新问题、来源边界。提出逐例常量代码/数学选择/有效实现的进一步讨论，明确模型假设、额外AllRealizable要求和未形式化部分。接收者可只凭信与参考入口理解；不必先恢复本机治理。

## 证据与状态

OUT-002 READY_FOR_USER_RELAY；sent=false；reply_received=false；没有IN-003或外部身份认证。无新数学实验、Lean/Agda编译或独立专家审查。原CLAIMS/PLAN和所有历史数学仍原状态。

## 变更与故障

新增文稿、来源/覆盖/验证与scripts工具；更新当前对话README/DEBATE_LEDGER和脚本索引，改前字节已备份；本checkpoint同步MEMORY/FRONTIER/LESSONS/RESUME/STATE。首轮准备因文稿路径缺失返回FileNotFoundError，补存正文后新日志重试；没有将失败说成通过。

保持不变：第五闭包、三问、AGENTS、两类Skill、治理引擎、LOAD_SET、Theory Schema、主张矩阵、所有原来信、OUT-001、旧sessions与RP-B01原计划/构造。继承README旧状态段落的不同步单独披露，本次不擅自改全仓。

## 下一动作

用户可转发OUT-002；无实际回信不作共同结论。内部自主工作仍从RP-B01模型绑定开始，新的可实现性区分仅作待审补充。任何后续同意都不能替代实际规则、证明或运行证据。
'''
    texts={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,
        P+'RESUME.md':resume,P+'STATE.json':dump(state),SESSION:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
      'authorization':'Current user requests a full reply and continued discussion; established scripts-first, local Git and persistence requirements. No external send authorized or performed.',
      'files':[{'path':p,'expected_sha256':sha((R/p).read_bytes()) if (R/p).exists() else None,'text':t} for p,t in texts.items()]}
    put(O/'BASE_PLAN.json',before)
    put(O/'PAYLOAD.json',payload)
    put(O/'DRY_RUN.json',rt.checkpoint(R,before['snapshot'],payload,apply=False))
    result=rt.checkpoint(R,before['snapshot'],payload,apply=True)
    put(O/'COMMIT.json',result)
    after=rt.plan(R)
    put(O/'AFTER_PLAN.json',after)
    required=set(docpaths+[SESSION,'MEMORY.md'])
    assert required<={x['path'] for x in after['documents']}
    assert after['revision']==22
    try:
        rt.checkpoint(R,before['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        assert str(exc)=='STALE_BASE'
        put(O/'STALE_BASE.json',{'status':'REJECTED','error':str(exc)})
    else:
        raise RuntimeError('Stale-base rejection failed')
    actual=json.loads((R/(P+'STATE.json')).read_text())
    assert all(actual['records'][k]==v for k,v in old['records'].items() if k!='D-GEMINI-001')
    summary={'status':result['status'],'revision':22,'latest_session':SID,
        'new_letter_in_load_set':True,'dynamic_documents':len(after['documents']),
        'stale_base_rejected':True,'old_record_identities_preserved':True,
        'direct_send':False,'peer_reply_received':False,'full_business_cognition':'NOT_CLAIMED'}
    put(R/'artifacts/r022/CHECKPOINT_SUMMARY.json',summary)
    print(dump(summary))

if __name__=='__main__': main()
