#!/usr/bin/env python3
"""Prepare OUT-002 and its immutable evidence; do not contact or simulate Gemini."""
from pathlib import Path
import datetime, hashlib, json, re

R = Path(__file__).resolve().parents[2]
D = '.codex/research/hott/dialogues/GEMINI-001/'
N = D + 'rounds/003/'
O = R/'artifacts/r022'

def sha(b): return hashlib.sha256(b).hexdigest()
def dump(x): return json.dumps(x, ensure_ascii=False, sort_keys=True, indent=2)+'\n'
def put(rel, value):
    p=R/rel
    if p.exists(): raise RuntimeError('Refuse overwrite: '+rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(value if isinstance(value,str) else dump(value), encoding='utf-8')
def backup(rel):
    put('.codex/history/r022-before/'+rel, (R/rel).read_text(encoding='utf-8'))

def main():
    if (O/'PREPARED.json').exists(): raise RuntimeError('Already prepared')
    path=R/(D+'TO_GEMINI_002.md')
    body=path.read_bytes()
    # A control character introduced while saving this new draft is editorially removed.
    # No source or incoming correspondence is edited.
    clean=body.replace(b'\x00', b'`TIMEOUT`')
    if clean!=body:
        put('artifacts/r022/DRAFT_EDIT.json', {'change':'Remove inadvertent NUL in own new draft',
            'before_sha256':sha(body), 'after_sha256':sha(clean), 'count':body.count(b'\x00')})
        path.write_bytes(clean)
    text=clean.decode('utf-8')
    assert '\x00' not in text
    assert text.count('\\[')==text.count('\\]')
    assert all(f'H{i:02d}' in text for i in range(1,7))
    assert all(f'G{i:02d}' in text for i in range(1,7))
    put(D+'TO_GEMINI_002.txt',text)
    put(N+'RELAY_NOTE.txt',
        '请完整阅读附件 OUT-002。它回应你的 IN-002，并提出代码分配与有效实现的待审构造。'
        '请优先回答 H03、H04、H05，指出最可能的错误，给出一项最小下一动作；'
        '再简答 H01、H02、H06。不要把双方同意当成证明，不要声称运行了没有运行的代码。\n')
    topics=[
      ('G01','接受撤回；定理适用条件保留','第一节'),
      ('G02','接受几何不自动遍历与卡住/发散区分；限定模型','第一节'),
      ('G03','唯一选择的合法数据提取正例，反对过度否定','第二节'),
      ('G04','不同类型族的运输公式与责任归属','第三节'),
      ('G05','ASK具体资格，不变成万能批准器','第一、五、六节'),
      ('G06','我方和对方共同补齐二元接口、通用代码及一致性范围','第四节')]
    questions=[
      ('H01','残余规则问题'),('H02','程序模型和对角形成'),
      ('H03','数学代码分配与有效可实现性'),('H04','自然使用与目标对应'),
      ('H05','最值当的下一动作'),('H06','主动反对与新的HoTT机制')]
    put(N+'RESPONSE_MAP.json', {'schema_version':'hott-outgoing-response-map/v1',
      'outgoing':'OUT-002','responds_to':'IN-002',
      'coverage':[{'id':i,'response':v,'letter_section':s} for i,v,s in topics],
      'questions':[{'id':i,'topic':t,'reply_status':'NOT_RECEIVED'} for i,t in questions],
      'new_proposal':'Mathematical selector k(z)=c_f(z) versus a realizer for k; explicitly extra AllRealizable principle',
      'proposal_scope':'DRAFT_FOR_CRITICISM_WITH_MODEL_ASSUMPTIONS_NOT_KERNEL_VERIFIED'})
    sources=[
      'AGENTS.md','.codex/skills/hott-session-governance/SKILL.md',
      '.codex/skills/hott-paradox-research/SKILL.md','MEMORY.md',
      '.codex/cognition/PROTOCOL.md','.codex/cognition/LOAD_SET.json',
      D+'TO_GEMINI_001.md',D+'DEBATE_LEDGER.json',D+'README.md',
      D+'rounds/002/IN-002.md',D+'rounds/002/ASSESSMENT.md',D+'rounds/002/SYNTHESIS.md',
      '.codex/research/hott/candidates/RP-B01/PLAN.md',
      '.codex/research/hott/candidates/RP-B01/CONSTRUCTION.md']
    put('artifacts/r022/READ_SCOPE.json',{'scope':'Bounded correspondence drafting and state persistence',
      'primary_basis':'Current user request; real IN-002; OUT-001; R021 assessment and plan',
      'file_identities':[{'path':p,'sha256':sha((R/p).read_bytes()),'bytes':(R/p).stat().st_size} for p in sources],
      'additional_rule_ranges':[
        {'path':'HoTT/theory-schema/upstream/book-578b85cc/logic.tex','ranges':[[358,391],[800,840]]},
        {'path':'HoTT/theory-schema/upstream/book-578b85cc/basics.tex','ranges':[[1625,1638],[1760,1782]]},
        {'path':'HoTT/theory-schema/upstream/book-578b85cc/formal.tex','ranges':[[984,1010],[1172,1193]]}],
      'full_business_cognition':'NOT_CLAIMED; no full closure/dynamic-set reading certification in this bounded drafting task',
      'source_role_note':'Sources describe prior work; newly proposed arguments are labeled as ours and not reconciled into the incoming original.',
      'external_ai_called':False,'response_from_gemini_available_this_turn':False,
      'new_kernel_or_mathematical_experiment':False})
    put(N+'SOURCES.md', '''# OUT-002 来源与读取范围

日期：2026-09-11。直接依据为真实 IN-002、旧 OUT-001 和 revision21 的评估/研究计划；不使用外部AI隐藏推理。

## 本地源

IN-002全文与旧OUT-001已读；ASSESSMENT、SYNTHESIS、RP-B01 PLAN/CONSTRUCTION重新读取。当前来信原文不改。第一轮原文已在先前完整材料与本轮上下文提供；本轮没有再声称重新审计整个JSON或独立认证作者身份。

HoTT Book锁定源码：logic.tex 358—391、800—840；basics.tex 1625—1638、1760—1782；formal.tex 984—1010、1172—1193。源字节与精确范围见 artifacts/r022/READ_SCOPE.json。旧源码中“currently/open”的年代说明不是2026年现状。

## 本次一手web核对

1. https://raw.githubusercontent.com/HoTT/book/master/logic.tex ：命题LEM、唯一选择的条件与唯一答案图。
2. https://raw.githubusercontent.com/HoTT/book/master/basics.tex ：依类型族的运输与命题性UA计算。
3. https://lean-lang.org/doc/reference/latest/Definitions/Modifiers/ ：noncomputable是声明的编译状态；数学上的无算法结论还要独立论证。
4. https://arxiv.org/abs/1611.02108 ：作者摘要和论文身份，构造性单价解释；没有逐证明重审全文。
5. https://arxiv.org/abs/1607.04156 ：作者摘要和规范性结果范围；没有重新运行其证明。

网页通过web读取；没有宣称下载固定版本网页字节或对整篇论文完成审计。信内S3使用本地锁定formal.tex，提供作者URL供接收者核查。

## 本轮新增内容的身份

逐例常量代码、数学选择函数k、Real与AllRealizable的比较，是在已有对角模型前提下提出供讨论的说明。完整原生代码模型、内核证明、新颖性、实际应用桥梁仍未完成。本轮只做规则对应、文稿与文件验证，没有数学试验或其他AI执行。
''')
    # Preserve prior mutable dialogue metadata before changing current routing.
    for rel in (D+'DEBATE_LEDGER.json',D+'README.md','scripts/README.md'):
        backup(rel)
    ledger=json.loads((R/(D+'DEBATE_LEDGER.json')).read_text())
    assert all(x['id']!='OUT-002' for x in ledger['outgoing'])
    ledger['outgoing'].append({'id':'OUT-002','path':D+'TO_GEMINI_002.md',
        'text_path':D+'TO_GEMINI_002.txt','sha256':sha(clean),'bytes':len(clean),
        'responds_to':'IN-002','status':'READY_FOR_USER_RELAY','sent':False,
        'reply_received':False,'reply_id':None,'direct_send_performed':False,
        'source':'Current author, not a simulated Gemini response'})
    ledger['updated_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    ledger['workflow'].update(status='OUT002_READY_RESEARCH_CONTINUES',
        reason='User requested a full reply and collaborative research questions; no direct send or new incoming message.',
        direct_contact_this_round=False, simulated_peer_reply=False, awaiting_peer_to_start_research=False,
        optional_next_peer_action='User may relay OUT-002; H01-H06 have no received answers yet.')
    ledger['round']=2
    ledger['received_rounds']=2
    ledger['outgoing_count']=2
    ledger['followup_questions']=[{'id':i,'topic':t,'introduced_in':'OUT-002',
        'status':'PROPOSED_TO_PEER_NOT_SENT','peer_response':'NOT_RECEIVED',
        'required_to_continue_our_research':False} for i,t in questions]
    (R/(D+'DEBATE_LEDGER.json')).write_text(dump(ledger),encoding='utf-8')
    (R/(D+'README.md')).write_text('''# GEMINI-001 · 时间、ASK与HoTT的真实讨论记录

**当前状态：IN-001与IN-002已经收到；OUT-002已写好供用户转发，尚未直接发送，没有第三轮回复。**

## 可直接转发

[第二封完整回信](TO_GEMINI_002.md) / [同文TXT](TO_GEMINI_002.txt)。可附 [简短转发提示](rounds/003/RELAY_NOTE.txt)。信回应G01—G06，并提出H01—H06，要求具体反例、模型义务和下一步选择，不要求再次宣誓同意。

第五节新增代码分配与可实现性说明标为待审，不是机器证明或Gemini已接受结论。双方同意不作数学认证。

## 不可覆盖的真实历史

首轮000_SOURCE.md与001—005角色切片、ANALYSIS.md、OUT-001均原字节保留。第二轮rounds/002下的USER_MESSAGE、IN-002、ASSESSMENT、SYNTHESIS、SOURCES及INPUT_PROVENANCE保持原文。

旧“没有准备OUT-002”只属于revision21的工作状态；本轮用户明确要求回信，故已经准备。没有回信配额不阻塞研究。外部发送、接收与已证结论分开登记。

## 当前依据与接续

[两轮综合](rounds/002/SYNTHESIS.md)、[完整评估](rounds/002/ASSESSMENT.md)、[当前RP-B01计划](../../candidates/RP-B01/PLAN.md)与[构造](../../candidates/RP-B01/CONSTRUCTION.md)。新文稿范围见 [SOURCES](rounds/003/SOURCES.md) 和 RESPONSE_MAP.json。

下一真实来信追加IN-003并逐项回应H编号，不能覆盖旧稿或伪造已接收。业务研究仍自主从RP-B01模型绑定继续；不会为了等待第三个模型意见暂停。
''',encoding='utf-8')
    sr=R/'scripts/README.md'
    sr.write_text(sr.read_text()+'''\n## R022 · 第二封论辩回信与交接\n\n新增工具均先落盘再调用：`scripts/session/r022_restore.py` 安全恢复原包；`r022_prepare.py` 整理真实文稿与台账；`r022_checkpoint.py` 经原治理器交接；`scripts/tools/r022_verify_package.py` 校验、Git提交与打包。它们不调用Gemini，不运行数学模拟器，不把文件检查当内核证明。\n''',encoding='utf-8')
    put('artifacts/r022/PREPARED.json',{'status':'PREPARED','outgoing':'OUT-002',
        'letter_bytes':len(clean),'unicode_characters':len(text),'lines':len(text.splitlines()),
        'sha256':sha(clean),'md_txt_identical':True,'direct_send':False,'new_peer_reply':False,
        'original_questions_covered':6,'new_questions':6})
    print(dump(json.loads((O/'PREPARED.json').read_text())))

if __name__=='__main__': main()
