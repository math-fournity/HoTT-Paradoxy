"""Apply bounded, source-grounded R021 documentation changes; no research execution.

All old bytes are backed up. STATE/MEMORY are updated later through the existing
checkpoint manager. Historical dialogue and source texts remain immutable.
"""
from pathlib import Path
import datetime, hashlib, json

R = Path(__file__).resolve().parents[2]
A = R / 'artifacts/r021'
D = R / '.codex/research/hott/dialogues/GEMINI-001'
N = D / 'rounds/002'
C = R / '.codex/research/hott/candidates/RP-B01'
B = R / '.codex/history/r021-before'
changes = []

def sha(b):
    return hashlib.sha256(b).hexdigest()

def dump(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode()

def update(rel, data):
    p = R / rel
    old = p.read_bytes()
    data = data.encode('utf-8') if isinstance(data, str) else data
    if old == data:
        return
    bak = B / rel
    if bak.exists():
        raise RuntimeError('Backup already exists: ' + str(bak))
    bak.parent.mkdir(parents=True, exist_ok=True)
    bak.write_bytes(old)
    p.write_bytes(data)
    changes.append({'path': rel, 'old_sha256': sha(old), 'new_sha256': sha(data),
                    'backup': str(bak.relative_to(R))})

def replace_once(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError('Expected unique text: ' + old[:140])
    return text.replace(old, new, 1)

def new(rel, text):
    p = R / rel
    if p.exists():
        raise RuntimeError('New path already exists: ' + rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(text.encode() if isinstance(text, str) else text)

# Correct our own new document's relative navigation, not any original quotation.
p = N / 'ASSESSMENT.md'
s = p.read_text()
s = replace_once(s, '../../../candidates/RP-B01/CONSTRUCTION.md',
                 '../../../../candidates/RP-B01/CONSTRUCTION.md')
p.write_text(s)

ledger_rel = str((D/'DEBATE_LEDGER.json').relative_to(R))
ledger = json.loads((R/ledger_rel).read_text())
ledger['round'] = 2
ledger['updated_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger['workflow'] = {
    'status': 'AUTONOMOUS_SYNTHESIS_NO_PEER_WAIT',
    'reason': 'User reports current Gemini quota exhaustion and requests synthesis plus persistence.',
    'direct_contact_this_round': False, 'simulated_peer_reply': False,
    'awaiting_peer_to_start_research': False,
    'next_action': '.codex/research/hott/candidates/RP-B01/PLAN.md#WP1',
    'authority': 'Source agreements do not certify mathematics; current researcher owns next action.'
}
ledger['incoming'].append({
    'id': 'IN-002', 'path': str((N/'IN-002.md').relative_to(R)),
    'source': 'Actual current user-relayed visible text',
    'status': 'RECEIVED_AND_CRITICALLY_REVIEWED',
    'bytes': (N/'IN-002.md').stat().st_size,
    'sha256': sha((N/'IN-002.md').read_bytes()),
    'identity': 'Attributed to Gemini by user; not independently API-authenticated',
    'new_machine_proof_or_execution_receipt': False
})
for outgoing in ledger['outgoing']:
    if outgoing['id'] == 'OUT-001':
        outgoing['reply_received'] = True
        outgoing['status'] = 'USER_RELAYED_REPLY_RECEIVED'
        outgoing['sent'] = False
        outgoing['sent_field_scope'] = 'No direct assistant sending action; not a claim that user did not relay it.'
        outgoing['delivery_evidence'] = 'User supplied a reply acknowledging OUT-001; exact external delivery was not instrumented.'
        outgoing['reply_id'] = 'IN-002'
q_updates = {
    'G01': ('RETRACTED_BY_PEER_WITH_SCOPE', '原混同明确撤回；有效公理化、一致性和算术条件仍须补齐。'),
    'G02': ('NARROWED_NOT_UNIVERSAL', '撤回连续统遍历与发散；具体族、归约及cubical定理范围仍须限定。'),
    'G03': ('PARTIAL_RETRACTION_RESIDUAL_ERROR', '撤回凭空存在；绝对禁止提取为过度纠偏，唯一选择正例保留。'),
    'G04': ('NARROWED_FORMULA_CORRECTION_REQUIRED', '裸身份不保成本正确；共轭仅适用End族，命题等式不自动是执行规则。'),
    'G05': ('ALIGNED_WITH_EVIDENCE_BOUNDARIES', 'ASK为资格责任；不要求万能批准器或先得统一时间界限。'),
    'G06': ('ACCEPTED_DIRECTION_REPAIRED_EXPOSITORY_ARGUMENT', '二元Code接口与有效对角闭包补明；无新内核结果、绝对一致性或原创性认证。')
}
for q in ledger['questions']:
    status, decision = q_updates[q['id']]
    q['history'] = [{'round': 1, 'status': q['status'], 'peer_response': q['peer_response']}]
    q['peer_response'] = 'IN-002'
    q['status'] = status
    q['current_decision'] = decision
    q['review_path'] = str((N/'ASSESSMENT.md').relative_to(R))
    q['further_peer_reply_required'] = False
ledger['claim_transitions'] = [
    {'claim_id': 'C04', 'round': 2, 'peer_action': 'explicit retraction', 'original_verdict_retained': True},
    {'claim_id': 'C05', 'round': 2, 'peer_action': 'explicit retraction', 'original_verdict_retained': True},
    {'claim_id': 'C06', 'round': 2, 'peer_action': 'explicit retraction', 'original_verdict_retained': True},
    {'claim_id': 'C07', 'round': 2, 'peer_action': 'retraction plus new overcorrection', 'new_issue': 'G03 unique-choice exception'},
    {'claim_id': 'C08', 'round': 2, 'peer_action': 'narrowed', 'new_issue': 'G04 family/equality scope'},
]
ledger['new_claims'] = [
    {'id': 'C14', 'claim': '截断绝不允许提取具体数据', 'verdict': 'OVERSTRONG_UNIQUE_CHOICE_COUNTEREXAMPLE'},
    {'id': 'C15', 'claim': 'HoTT+LEM的数学χ与有效总实现分离', 'verdict': 'VALID_CLASSICAL_DIRECTION_WITH_MODEL_ASSUMPTIONS'},
    {'id': 'C16', 'claim': '此论证证明HoTT+LEM完全自洽', 'verdict': 'NOT_ESTABLISHED_BY_THIS_ARGUMENT'},
    {'id': 'C17', 'claim': '查不到越界意味着所有系统已经完整隔离', 'verdict': 'INVALID_GLOBAL_INFERENCE'},
    {'id': 'C18', 'claim': 'Lean/Coq使用经典逻辑就成为HoTT', 'verdict': 'THEORY_IDENTIFICATION_REQUIRED'},
    {'id': 'C19', 'claim': '以后只需等待对方或只找软件bug', 'verdict': 'NOT_A_RESEARCH_REQUIREMENT'},
]
ledger['proposed_actions'][0].update(status='SELECTED_PLAN_EXPOSITORY_CONSTRUCTION_SAVED_NATIVE_NOT_RUN',
    plan=str((C/'PLAN.md').relative_to(R)), construction=str((C/'CONSTRUCTION.md').relative_to(R)))
ledger['proposed_actions'][1]['status'] = 'RESERVE_NEW_MECHANISM_ONLY_NOT_EXECUTED'
ledger['proposed_actions'][2]['status'] = 'RESERVE_OPEN_NOT_EXECUTED'
ledger['synthesis_path'] = str((N/'SYNTHESIS.md').relative_to(R))
update(ledger_rel, dump(ledger))
update(str((D/'README.md').relative_to(R)), '''# GEMINI-001 · 时间、ASK与HoTT的真实讨论记录

**当前状态：已收到用户转述的 IN-002；两轮综合分析已保存，研究无需等待下一封回信。**

用户目前没有Gemini使用配额。此为当前条件，不预判恢复日期。未直接联系Gemini、没有模拟回复、没有通过两模型赞同认证数学。

## 不可覆盖的历史

- `000_SOURCE.md`：首轮完整附件；`001`—`005`保留角色切片。
- `ANALYSIS.md`：第一轮评估，不改成第二轮观点。
- `TO_GEMINI_001.md` / `.txt`：OUT-001原文，字节不变。用户已转回一份明确回应它的文本；本助手没有直接发送日志。

## 当前来信与综合

- [第二轮完整用户消息](rounds/002/USER_MESSAGE.md)、[IN-002原文](rounds/002/IN-002.md)：手工保全可见消息后精确切片，不校订其错误。
- [逐项评估](rounds/002/ASSESSMENT.md)：区分撤回、仍过强之处、我方补正及官方资料。
- [研究综合](rounds/002/SYNTHESIS.md)：吸收双向目标、三层成果和自主探索。
- [来源与范围](rounds/002/SOURCES.md)、`INPUT_PROVENANCE.json`。
- [当前行动方案](../../candidates/RP-B01/PLAN.md)与[修订后的构造](../../candidates/RP-B01/CONSTRUCTION.md)。

DEBATE_LEDGER记录G01—G06的具体转变；“讨论中撤回”不等于“新数学定理已经机器证明”。不再写一份等待发送的OUT-002作为研究前置。以后确实收到新材料，再新增真实回合。
''')

# Current governance and business entry; no new gating or change of full-load rules.
ag = (R/'AGENTS.md').read_text()
old = '- 当前第一主题是“Z铁律下的HoTT现实相对时间悖论”：主要目标不是内部 `HoTT ⊢ ⊥`，而是理论时间前提把握的非现实性。按第五闭包§20，优先构造一个过程：现实对应本无该完成困难，Think in HoTT的明确设定／解释却引出了它。其它现实相对形状保留；不以一般no-go、任意加强合同或信息损失冒充目标完成。'
newgoal = '- 当前第一主题是“Z铁律下的HoTT现实相对时间悖论”，不是以内部 `HoTT ⊢ ⊥` 为主要目标。双向目标同时保留：A，现实对应原可完成，明确Think in HoTT设定／解释引入额外完成困难（第五闭包§20）；B，数学分类／存在被提升为尚未取得的有效交付能力（用户双向原文记录 `U-DUAL-DIRECTION-JSON-001` 与 GEMINI-001/000_SOURCE.md）。当前优先级按真实前沿，不再永久绑定A或Done编码；两方向都须核同任务、规则及证据，不以一般no-go或任意加强合同冒充目标完成。'
ag = replace_once(ag, old, newgoal)
anchor = '## 最高目的与第一动作\n'
section = '''## 外部论辩吸收与自主接续（2026-09-11，revision21）

外部意见原文、其作者撤回、我方校正、已确认规则及待执行研究分别记录。实际用户转回的来信才算收到，不模拟其他AI；配额或对方停止回复不是本项目选题和推进的依赖。当前GEMINI-001已接收IN-002，旧OUT-001留作历史，不能再从旧“待回信”状态阻塞研究。

可独立交付三层结果：理论选择、局部不相容／表示边界、完整目标实例。前层有价值但不冒充后层；正确保全结构的例子限定指控，不取消原抽象边界。允许自行构造自然、精确的理论化，不以已有软件漏洞为唯一入口。

普通Lean/Mathlib、Rocq/Coq与HoTT的理论环境须分别固定。`noncomputable`或源码出现经典原则，不单独证明任务不可计算；没有查到坏提取也不证明所有系统隔离完备。实现审查回到具体依赖、编译/提取入口和规格，不能只按关键词判决。

本轮仅维护来源评估与行动规则，不改第五闭包历史、不重新认证旧数学或全文认知门禁。详见 `.codex/research/hott/dialogues/GEMINI-001/rounds/002/` 和 `.codex/research/hott/candidates/RP-B01/`。

'''
ag = replace_once(ag, anchor, section+anchor)
update('AGENTS.md', ag)

skill_rel = '.codex/skills/hott-paradox-research/SKILL.md'
s = (R/skill_rel).read_text()
s = replace_once(s, 'version: "1.3.2"', 'version: "1.3.3"')
s = replace_once(s, '当前主要目标不是HoTT内部矛盾，而是其时间前提的把握所引出的理论非现实性。按第五闭包§20和最新原文，优先希望构造一个过程：现实对应本无某种完成困难，而明确的Think in HoTT设定／解释引入了它，表现为无法完成、不落定或其他经过定义的障碍。完整原文路径为 `HoTT/sources/user-originals/HoTT目标再澄清-非现实性困难与无法完成-20260910.md`，由STATE和第五闭包全文进入当前加载。',
'''当前主要目标不是HoTT内部矛盾，而是其时间前提与交付资格的现实相对问题。保留两个方向：A，现实对应原可完成，明确Think in HoTT设定／解释使之出现额外完成困难；B，数学上取得分类或存在，随后被提升为尚未获得的有效求解／实际交付。A的完整原文与思想演化见第五闭包§20及 `HoTT/sources/user-originals/HoTT目标再澄清-非现实性困难与无法完成-20260910.md`；B的用户原文由 `U-DUAL-DIRECTION-JSON-001` 与 `D-GEMINI-001` 动态路由。原文均不被本段代替。当前主攻按MEMORY／FRONTIER，不能每次重启都回到同一Done例子。''')
s = replace_once(s, '下一步继承revision11的实际问题：从有Done的有限轨迹或完成报告出发，固定擦除/变换及原输入域，追踪结束依据是否真的被删除或误认为已完成。不扩大域、不换完成任务来制造悖论；若证书/字面来源使过程仍可完成，就保留正向结果，转查实际放宽准入或非计算消去的接口。',
'''每次下一动作以最新真实前沿为准，不将revision11的Done问题设为永久首选。R014—017已保存其正反结果；只有新机制、新实际接口或新证据才重开相同指控。不扩大域、不换完成任务来制造悖论；证书／来源使过程仍可完成时应保留正向结果。''')
s += '''

## 14. v1.3.3：两轮外部意见的研究吸收

本次维护依据用户2026-09-11要求，GEMINI-001已真实收到用户转述的IN-002。来源撤回不是定理证明；第一轮和第二轮原文均保留。没有新的外部AI调用，不等待对方配额恢复；本项目研究者自主承担计划和反向检查。

按三层交付：直接定位理论选择；证明指定要求的局部边界；再核自然理论化对同任务的实际非现实性。没有第三层时仍交付前两层，但明确范围。数学构造与现有实现审查互补，任何一个都不成为另一个的普遍前置。

当前RP-B01聚焦命题LEM下的数学停机分类与无神谕有效总实现。Code模型须固定有效通用性、配对、有限步关系及对角闭包；二元χ(p,x)不能中途改成一元。单价性／HIT未被核心推导使用时明确说明，不包装成HoTT独有新定理。纸笔经典归约不当作本次已运行的机器验证，模型未形式化之处显式保留。

关键反向校准：真实h:||P||且P为命题时可以唯一选择再投影数据；不把一般禁止消去误写成绝对禁止。运输共轭公式只用于End族，命题计算不自动变归约规则。源码依赖LEM、`noncomputable`标记与函数没有任何有效算法分别判断；两支同值可有常值实现。检查到的局部保护不证明所有库完全隔离。

三类资格F（形成）、M（数学规格）、E（有效交付）只是可用分析视角，不新增强制表单或万能ASK。旧Skill方法仍可自主扩展。当前计划和证据状态以 `.codex/research/hott/candidates/RP-B01/` 为起点，后续按新成果调度。全文加载规则、治理Skill与运行器均不因这一维护而改变。
'''
update(skill_rel, s)

qrel = 'HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
q = (R/qrel).read_text()
q = replace_once(q, '> 初稿：2026-09-09；当前认识对齐：2026-09-10，v4（revision13；目标见第五闭包§20，ASK原文与完整理解见§21）。',
''' > 初稿：2026-09-09；当前认识对齐：2026-09-11，v5（revision21；第五闭包§20—21保留原字节，双向用户来源及两轮论辩由STATE带入）。'''.lstrip())
q = replace_once(q, '当前v4对齐ASK；本次改前文件保存在 `.codex/history/ASK-before-rev13/`，第五闭包旧§17—20全部不改。',
'''v4对齐ASK的改前文件保存在 `.codex/history/ASK-before-rev13/`；本次v5改前全文保存于 `.codex/history/r021-before/` 与Git。v5吸收已记录的双向目标及来源批判，不改第五闭包或其历史附件。''')
q = replace_once(q, '**第一，寻找HoTT的理论设定或明确的Think in HoTT解释对时间前提把握所带来的非现实性。优先构造一个过程：现实对应本无这种完成困难，而理论化使它陷入无法完成或无法落定。不是以内部矛盾为主要目标，也不以任意no-go或信息差异代替该实例；九类方向与其它现实相对表现继续保留。**',
'''**第一，寻找HoTT的理论设定或明确Think in HoTT解释对时间、求解及交付资格把握所带来的非现实性。双向保留：A，原可完成的现实任务被理论化引入额外完成困难；B，数学上的分类或存在，被提升为尚未取得的有效完成能力。不是以内部矛盾为主要目标，也不以任意no-go或信息差异替代目标实例；九类方向继续保留，实际优先级由当前证据与前沿决定。**''')
q = replace_once(q, '### 2. 所谓“非现实性”，尤其包括理论制造的完成困难',
                   '### 2. 所谓“非现实性”：完成依据丧失与完成能力被过度认领两个方向')
q = replace_once(q, '最新原文强调的不只是理论“多许诺了一种现实中做不到的能力”，还包括相反方向：现实对应本无某种完成困难，而一种具体理论化引出了这种困难。优先希望像芝诺或圆环一样，给出一个能让人清楚看见反差的过程，而不是只宣布某类抽象不完整。',
'''第五闭包§20原文突出方向A：现实对应本无某种完成困难，某种理论化却引出困难。后续用户明确补充方向B：“现实中，比如使用程序，无法完成，但是却在某个理论中，绕过了ASK过程，然后完成了？”两方向都要以可检查的过程与资格对应展开，不把A设成永久的唯一主线。B的用户原文保存于[双向纠偏记录](../.codex/research/hott/sessions/S-AUD-20260910-018-HOTT-JSON/USER_DUAL_DIRECTION.txt)和[完整论辩输入](../.codex/research/hott/dialogues/GEMINI-001/000_SOURCE.md)。Gemini认可不是这项用户目标的权威来源，也不证明目标实例已成立。''')
q = replace_once(q, '**我们优先希望交付的，不是一句“HoTT有缺失”或又一个假设合同no-go，而是一个可逐步核查的过程：某种HoTT理论化把现实对应本无的完成困难引出来了。理论过程在哪里不能完成，与现实过程怎样对应，要具体展示；最终应修改哪项前提仍可继续研究。**',
'''**应分层交付：先明确理论实际选择了什么，再证明它与哪些具体过程要求不能共存，进一步构造同任务的非现实性实例。方向A展示新增完成困难，方向B展示数学分类被提升为并未取得的有效交付。前两层不能冒充最终实例，也不能因最终实例未闭合就拒绝承认前两层成果；最终归因与修复仍可后置。**''')
q = replace_once(q, '**找什么？**找Think in HoTT后出现的理论非现实性，优先追踪具体过程中的无法完成／不落定与现实对应的反差；不是把内部矛盾、一般信息损失或条件合同不相容替代为最终目标。',
'''**找什么？**找Think in HoTT的现实相对问题，既追踪原完成依据怎样丧失，也追踪数学资格怎样被提升成无依据的有效能力。内部矛盾不是唯一目标，信息损失与合同不相容不自动等于最终命中。''')
q += '''

### 2026-09-11 v5：双向目标与两轮Gemini材料的正确地位

用户当前要求综合两轮外部意见并落盘，暂时无Gemini配额；研究不等待第三封信。第一轮提供直接定位时间抽象的方法提醒，第二轮撤回若干过强主张并采用HoTT+命题LEM的分类例子。新的绝对禁止截断提取、无条件一致性结论和“未发现问题即所有库安全”的推断仍须纠正。原文和校正分别保存在 `.codex/research/hott/dialogues/GEMINI-001/rounds/002/`。

当前由本项目选定RP-B01：固定通用有效Code模型及二元输入，分别建立数学χ的规格与不存在同规格无神谕总算法的论证，再审一个自然解释或真实实现接口。该核心是经典分离，不声称HoTT独有；普通Lean/Rocq的比较不能冒充HoTT身份类型。有限有界判断、可提取的唯一答案、经典语法但两支同值等正例必须保留。

可以自行构造自然、精确的理论化，不以已有软件事故为唯一入口。库审查只在具体版本/定义/公理/提取/运行链上判断；关键词、道歉、两AI一致和文件测试不代替证明。未发现越界只能限制已查范围，不能概括所有系统。

本次是来源综合及行动规则维护，未完成新的Code原生形式化、数学实验、独立外审或完整业务认知加载。第五闭包、原用户正文、固定规则源码、既有证明和主张矩阵均未变；计划与方法可以更新，数学真值须另依证据。
'''
update(qrel, q)

zrel = 'HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md'
z = (R/zrel).read_text()
z = replace_once(z, '建立日期：2026-09-01；当前认识对齐：2026-09-10（第五闭包§20—21／revision13）。',
                  '建立日期：2026-09-01；当前目标对齐：2026-09-11（双向用户原文／revision21；第五闭包§20—21原文不改）。')
z = replace_once(z, '> **寻找HoTT的理论设定或明确的Think in HoTT解释在时间前提的把握上引出的非现实性。优先构造一个具体过程：现实对应本无这种完成困难，而理论化使它陷入无法完成或无法落定。**',
'''> **寻找HoTT理论设定或明确Think in HoTT解释对时间／求解资格的现实相对问题，双向保留：A，原能完成的任务被引入额外完成困难；B，数学分类或存在被解释为已经取得无相应有效依据的完成能力。当前优先级由实际前沿决定，不永久限定Done、截断或单一方向。**''')
z = replace_once(z, '最新原文和完整理解见第五闭包§20及 `sources/user-originals/HoTT目标再澄清-非现实性困难与无法完成-20260910.md`。',
'''A的原文与完整理解见第五闭包§20及 `sources/user-originals/HoTT目标再澄清-非现实性困难与无法完成-20260910.md`；B的用户明确补充见 `.codex/research/hott/sessions/S-AUD-20260910-018-HOTT-JSON/USER_DUAL_DIRECTION.txt`（相对于项目根）及 GEMINI-001/000_SOURCE.md 中的用户再论述。外部AI的认可不是数学证据；本轮只对齐当前研究目标，不改历史原文。''')
z = replace_once(z, '当前最强、已具标准数学和文献支撑的 HoTT 候选是：',
'''历史已登记、具有局部规则与文献支撑的候选之一是（当前是否主攻及证据强度见最新前沿与主张矩阵，本文不按旧登记自动排序）：''')
z = replace_once(z, '最接近芝诺、圆环、Russell 与 Better Best 共同结构的开放目标是：',
'''历史按芝诺、圆环、Russell 与 Better Best 启发登记的一条开放目标是（不排除不同机制或预设共同病因）：''')
update(zrel, z)

# Recompute only this skill's current manifest. Old top-level delivery manifests
# remain immutable historical snapshots, not claims about the new release.
mrel = '.codex/skills/hott-paradox-research/MANIFEST.json'
m = json.loads((R/mrel).read_text())
m['version'] = '1.3.3'
m['revision_note'] = 'Source synthesis and dual-goal methodology only; runtime/full-text gate unchanged; no new math certification.'
for row in m['files']:
    b = (R/'.codex/skills/hott-paradox-research'/row['path']).read_bytes()
    row['bytes'], row['sha256'] = len(b), sha(b)
update(mrel, dump(m))

new(str((C/'CLAIMS.json').relative_to(R)), dump({
    'schema_version': 'hott-rp-b01-claim-status/v1', 'candidate_id': 'RP-B01',
    'status': 'PLAN_SELECTED_AND_EXPOSITORY_ARGUMENT_SAVED',
    'claims': [
        {'id': 'B01-M', 'statement': 'HoTT+命题LEM下构造二元χ及停机规格',
         'status': 'PAPER_EXPLANATION_WITH_MODEL_DEFINITIONS_PENDING', 'uses_univalence': False},
        {'id': 'B01-E', 'statement': '无神谕通用模型不存在同规格有效总实现',
         'status': 'KNOWN_DIAGONAL_ARGUMENT_WITH_EXPLICIT_MODEL_ASSUMPTIONS'},
        {'id': 'B01-TARGET', 'statement': '特定HoTT使用方式把数学分类许诺为有效交付',
         'status': 'OPEN_ACTUAL_INTERFACE_NOT_IDENTIFIED'}],
    'native_formalization': 'NOT_RUN', 'mathematical_experiments': 'NOT_RUN',
    'independent_review': 'NOT_RUN', 'originality': 'KNOWN_CLASSICAL_CORE_NOT_CLAIMED_NEW',
    'complete_business_cognition': 'NOT_CLAIMED_SCOPED_DOCUMENT_SYNTHESIS',
    'no_false_claim_of_absolute_consistency': True,
    'next_action': 'WP1: Code model, bounded execution, effective diagonal code construction'
}))

index = (R/'scripts/README.md').read_text()
index += '''

## R021 · Gemini两轮综合与研究计划保全

新增脚本在 `scripts/session/r021_*.py` 与 `scripts/tools/r021_*.py`，均先落盘再调用。
`restore`恢复真实rev20仓库；`prepare`原文切片/来源指纹；`sources`记录远端快照尝试（DNS失败如实保留）；`integrate`维护来源裁决与当前目标；`checkpoint`经既有manager同步状态；`verify`只查文件/路由/边界；`package`实际提交、Git/ZIP/bundle恢复验证。
本轮没有运行HoTT数学模拟器或证明助手。机械检查不是数学定理证明。旧回收源码和历史脚本不被改写。
'''
update('scripts/README.md', index)
new('artifacts/r021/INTEGRATION.json', dump({
    'schema_version': 'hott-r021-integration/v1', 'changes': changes,
    'old_originals_preserved': True, 'fifth_closure_modified': False,
    'theory_schema_modified': False, 'claim_matrix_modified': False,
    'native_mathematics_executed': False, 'business_version': '1.3.3', 'three_questions_version': 'v5',
    'governance_runtime_modified': False,
    'legacy_delivery_manifests': 'Preserved as historical records; final R021 delivery receipt covers current files.'
}))
print(json.dumps({'updated_files': len(changes), 'business_skill': '1.3.3',
                  'source_reply_unchanged': True, 'state_checkpoint': 'NOT_YET_EXECUTED'}, ensure_ascii=False))
