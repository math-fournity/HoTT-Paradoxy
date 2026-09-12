"""Record R021 source synthesis through the existing atomic cognition manager."""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, sys

R=Path(__file__).resolve().parents[2]
O=R/'artifacts/r021'; CP=O/'checkpoint'
P='.codex/research/hott/'
D=P+'dialogues/GEMINI-001/'
N=D+'rounds/002/'
C=P+'candidates/RP-B01/'
SID='S-DISC-20260911-021-GEMINI-SYNTHESIS'
SESSION=P+'sessions/'+SID+'/SESSION.md'

def sha(b):return hashlib.sha256(b).hexdigest()
def dump(obj):return json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def put(p,obj):
    if p.exists():raise RuntimeError('Refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(dump(obj),encoding='utf-8')

def bind(paths):
    return {p:sha((R/p).read_bytes()) for p in paths}

spec=importlib.util.spec_from_file_location('r021_runtime',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
before=rt.plan(R)
if before['revision']!=20:raise RuntimeError('Expected revision20, got '+str(before['revision']))
old=json.loads((R/(P+'STATE.json')).read_text())
state=copy.deepcopy(old)
state['revision']=21
state['latest_session']=SID
state['local_git'].update(history_origin='Inherited full provided revision20 Git history',
    inherited_head='3e529cd4ea00124347afa1195aaa3ccc1619b46e',
    pre_checkpoint_head='3e529cd4ea00124347afa1195aaa3ccc1619b46e',
    final_head='Actual Git and package-external revision21 delivery receipt; not a self-referential claim')

current=[N+x for x in ('USER_MESSAGE.md','IN-002.md','USER_DIRECTIVE.txt','INPUT_PROVENANCE.json',
                       'ASSESSMENT.md','SYNTHESIS.md','SOURCES.md')]
olddeb=state['records']['D-GEMINI-001']
olddeb['full_sources']=list(dict.fromkeys(olddeb['full_sources']+current))
olddeb['source_hashes'].update(bind([D+'DEBATE_LEDGER.json']+current))
olddeb['revalidation']='Source-state update only: actual user-relayed IN-002 archived without correction; compared G01-G06 with first source and fixed rule excerpts. Historic ANALYSIS/OUT-001 unchanged. No machine theorem/absolute consistency/full cognition certification.'
olddeb['next_action']='Use current RP-B01 plan autonomously; do not wait for additional Gemini quota or reply.'
olddeb['scope']='Two actual user-relayed opinions received; old first review kept, current conclusions in rounds/002. No direct sending action or new machine proof.'
olddeb['status']='review_required'

ud=state['records']['U-DUAL-DIRECTION-JSON-001']
ud['integration']={'revision':21,'status':'CURRENT_GOAL_TEXT_ALIGNED_NOT_A_MATH_VERDICT',
    'owners':['AGENTS.md','HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md',
              'HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md',
              '.codex/skills/hott-paradox-research/SKILL.md'],
    'source_note':'Existing actual user scope correction and first-source user reframing; not authority from Gemini agreement.'}
ud['scope']='User dual-direction correction preserved and now reflected in current goal owners. Source/historical review status not upgraded to theorem or complete cognitive gate.'

state['records']['D-GEMINI-002']={
    'kind':'relayed_opinion_synthesis','path':N+'SYNTHESIS.md','status':'review_required',
    'depends_on':['D-GEMINI-001'], 'full_sources':current+[D+'DEBATE_LEDGER.json','artifacts/r021/SOURCE_EXCERPTS.md'],
    'source_hashes':bind(current+['artifacts/r021/SOURCE_EXCERPTS.md']),
    'scope':'Both opinions compared; remaining errors recorded separately from originals; no simulated reply or kernel certification.',
    'next_action':C+'PLAN.md', 'awaiting_peer':False}
state['records']['P-RP-B01']={
    'kind':'research_plan_and_expository_construction','path':C+'PLAN.md','status':'review_required',
    'depends_on':['D-GEMINI-002'],
    'full_sources':[C+'CONSTRUCTION.md',C+'CLAIMS.json',N+'ASSESSMENT.md',N+'SOURCES.md',
                    'artifacts/r021/SOURCE_EXCERPTS.md'],
    'source_hashes':bind([C+'PLAN.md',C+'CONSTRUCTION.md',C+'CLAIMS.json']),
    'scope':'Known classical separation under explicit effective-model premises; native Code implementation and actual interface bridge OPEN.',
    'next_action':'WP1: choose a universal effective Code representation; bind bounded T and effective construction of D_h.',
    'formal_verification':'NOT_RUN','originality':'KNOWN_CLASSICAL_CORE_NOT_CLAIMED_NEW'}
state['records'][SID]={
    'kind':'session_record','path':SESSION,'status':'review_required',
    'depends_on':['D-GEMINI-002','P-RP-B01'],
    'full_sources':current+[C+'PLAN.md',C+'CONSTRUCTION.md',C+'CLAIMS.json',
                           'artifacts/r021/READ_SCOPE.json','artifacts/r021/INTEGRATION.json',
                           'artifacts/r021/SOURCE_IDENTITIES.json','artifacts/r021/web/MANIFEST.json'],
    'source_hashes':bind(current+[C+'PLAN.md',C+'CONSTRUCTION.md',C+'CLAIMS.json']),
    'scope':'User-authorized two-source synthesis, precise corrections, plan and current owner maintenance; not full business cognition/native mathematical validation.'}
state['active']=list(dict.fromkeys(['U-GOAL-20260910-001','U-ASK-20260910-001',
                                  'U-DUAL-DIRECTION-JSON-001','P-RP-B01']))
state['review_due']=list(dict.fromkeys(old['review_due']+['D-GEMINI-002','P-RP-B01',SID]))

memory='''# MEMORY.md · 当前工作记忆 revision21

## 身份与当前状态

实际根 `/mnt/data/HoTT_Gemini_synthesis_rev21/`；继承提供的revision20完整Git，基线HEAD `3e529cd4ea00124347afa1195aaa3ccc1619b46e`。最终提交以实际Git和外部交付收据为准。最新Session `S-DISC-20260911-021-GEMINI-SYNTHESIS`。

本轮用户已转回Gemini真实回复IN-002，要求综合两次意见并全部落盘，当前没有Gemini配额。没有等待第三封信、没有模拟回复、没有直接联系其他AI。旧OUT-001保持原字节，当前状态不再是“尚无回信”。

## 已完成的交付与不能外推之处

GEMINI-001/rounds/002保存本轮完整用户消息、原回复、逐项评估、综合认识和来源。DEBATE_LEDGER记录真实撤回与残余错误。第一轮的发现性提醒和第二轮的条件化构造一起吸收，不凭道歉或意见一致认证数学。

残余修正：唯一选择在真实存在且目标为命题时能提取数据；共轭只是End族运输公式，不是全部transport的判断执行；χ从一元改成明确二元Code模型；通用性/有效编码/对角程序闭包必须补齐；未推翻内部一致性不等于证明绝对一致性；没查到工程越界不证明全系统安全。普通Lean/Rocq不能自动当作HoTT。

当前目标owner、三问v5、业务Skill v1.3.3已对齐双向研究与三层成果。第五闭包历史、治理Skill/引擎、全文加载要求、Theory Schema、主张矩阵及旧研究均未改。

## 下一项自主工作

主攻 `P-RP-B01`：`.codex/research/hott/candidates/RP-B01/PLAN.md`。当前有修订后的完整条件式解释CONSTRUCTION.md和精确CLAIMS.json，但实际原生Code形式化、数学实验和独立审查都NOT_RUN。

优先WP1：固定有效通用程序模型、有限步T、输入配对以及h→D_h的代码构造。随后建立HoTT+命题LEM的χ规格与Rep(χ)不可成立的分离，核心属于已知经典机制，不冒充HoTT独有或原创。

实现审查是互补路径：自行构造自然解释不需先有软件bug；核查具体版本/公理/编译链时保留正例。经典语法、noncomputable标记不单独证明数学函数没有算法。新结果必须有相对既有工作的差量。

## 继承的重要边界

Done/真像/唯一答案/规范代表的成功构造、双向观察结构、卡住与发散的区别、局部证书与全域总性区别仍按旧证据状态保留。R001缺原始证据和其他待复核项不因本次综合被关闭。无新数学机制时不再重复全零流、缺规则模拟器或旧商指控；成本、历史、生成、自指、运动等方向保持开放。

本轮是有界来源综合与计划/治理文档维护；没有通过全部190份以上必读的业务认知gate，也没有重新声称已全文恢复第五闭包。文件/Git/checkpoint检查只认证所检查的字节、引用与状态，不能替代语义或内核证明。
'''
frontier='''# HoTT 当前研究前沿 · revision21

本文件是当前安排；旧版完整内容在Git与r021-before备份中，不把多份“当前”累加成互相矛盾的说明。

| 位置 | 本次选定对象 | 已有内容 | 下一项有判别力的动作 |
|---|---|---|---|
| 收敛 | RP-B01 数学分类与有效总交付 | 两轮来源综合；统一二元接口；条件式纸笔解释 | 完成一个实际通用Code模型及D_h构造的精确绑定 |
| 探索 | 规范→编译/提取→运行的接口 | 官方文档有保护与外部实现责任；未调查完整库 | 选择一个精确接口，检查计算相关依赖与规格；不以软件bug为唯一入口 |
| 深层 | 时间/资源/历史/形成及自指 | 旧正反结果与开放问题均保留 | 仅在有新机制/新证据时推进，不被经典停机基准永久占据 |

## 双向目标与成果层次

A：已有完成依据是否被理论化消掉；B：数学资格是否被提升为无依据的有效交付。当前优先B，但未撤销A或九类方向。
先交付理论选择，再交付局部限制，最后核目标实例。前两层不因第三层开放而无价值，也不冒充第三层已经完成。没有新增“必须先找到已有库漏洞”的前置。

## 不复活的旧入口

- R014—015：商/真像可以保业务答案与有限规范轨迹；不重复指控所有商消去无限搜索。
- R016：非规范正常形不等于无穷归约；同值证明可支持其他正确交付途径。
- R017：局部收敛域与证书可行，未找到强迫坏全域Gate的原规则。
- R018—019：外部模拟器、sorry、公理和成功字符串均不能代替实际证明。
- R020—021：外部AI承认错误是讨论状态；唯一选择的正例不能因“彻底撤回”而丢失。

## 本轮没有做的工作

RP-B01还没有可用的原生Code实现或机器证明；候选目标桥梁OPEN。没有重新核验旧数学结果，也没有全库排除全部越界。Gemini当前配额不足不成为暂停业务研究的理由。
'''
resume='''# 接续 · revision21

当前工作根 `/mnt/data/HoTT_Gemini_synthesis_rev21/`，最新Session `S-DISC-20260911-021-GEMINI-SYNTHESIS`。先按AGENTS与治理Skill恢复规定的全部正文，不能把本页替代第五闭包、三问或动态来源。

已收到IN-002。实际来信在 `.codex/research/hott/dialogues/GEMINI-001/rounds/002/IN-002.md`；读ASSESSMENT与SYNTHESIS、当前DEBATE_LEDGER，并保留第一轮原意见和OUT-001。不要再写“等待Gemini回复”，也不要模拟新对手。

本次重要修正：G03绝对禁止提取过强；G04共轭公式和归约层级要限定；G06必须二元输入、有效通用Code与对角闭包。绝对一致性和全工程无漏洞未被证明。

下一步自行执行RP-B01计划WP1的最小未闭合环节：在一套具体有效程序模型中绑定Code、T(p,x,n,v)、配对、程序调用与h→D_h的构造。再证明χ规格与¬Rep，不将经典数学分类当作已编译总算法。程序域不得在对角步骤悄悄变换。已有CONSTRUCTION仅为带明示模型前提的完整纸笔说明，不当作kernel结果。

原生HoTT工具不可用时，继续明确的纸笔/代码语义工作并报告范围；不要用普通Lean Eq冒充HoTT身份。对真实提取接口的检查是互补支线，不能取代自主数学构造。经典两支同值、有限步判定、真实像恢复等正例必须保留。

所有新增代码先写scripts再调用；过程原证据保存，里程碑走checkpoint并本地Git提交。未完成全文gate不能靠旧收据补PASS。本轮没有通过完整业务加载、没有新数学执行或外部AI调用。
'''
lessons=(R/(P+'LESSONS.md')).read_text()+'''

## R021 · 接受纠偏不能接受过度纠偏

- 原文撤回“截断凭空存在”后，若改成“绝不能提取数据”，仍须拒绝；真实h和唯一答案图可合法提取，不因对方道歉跳过正例。
- LEM数学分类与有效算法分开，但对角模型必须包含统一的输入参数、通用编码、组合与自输入闭包。Code可判定相等不够；一元χ和二元eval不能混接。
- 运输共轭只对End族；命题等式不是自动归约规则。数学函数总定义不等于每个闭项已求值。
- 没有内部矛盾的这段推演不证明全理论绝对一致；没有搜索到实际越界也不证明所有实现完整隔离。
- 普通Lean/Mathlib、Rocq模式与HoTT分别识别。noncomputable不等于无算法，经典分支两边同值可有常值实现。用户实现替换需独立规格责任。
- 真实来信只归档已收到内容；已接收就更新状态，不让旧“等待回信”阻塞。没有外部配额也不影响本项目研究者自选路径。
- 理论选择、局部边界、目标实例分层交付。已知基准可用但不包装原创；数学构造不必等待软件事故，工具审查也不能无限扩张。
- 原始思想与旧证明保持身份。当前MEMORY不累加多个冲突的“当前版本”，旧文完整由Git及历史字节备份保全。
'''
session='''# S-DISC-20260911-021-GEMINI-SYNTHESIS

日期：2026-09-11。任务：综合用户最近两次提供的Gemini意见，保存原文、评估、研究计划与当前治理认识。不是向Gemini发送信息或启动新求解批次。

## 身份与输入

恢复提供的revision20完整Git包，继承HEAD 3e529cd4ea00124347afa1195aaa3ccc1619b46e。第一轮000_SOURCE/OUT-001和既有ANALYSIS原字节保留；本轮用户消息手工保全可见正文，随后精确切片IN-002。不声称独立平台原始字节导出或外部模型身份认证。

读取范围为本轮实际两源、有关治理、当前状态、三问、Schema入口与固定原规则；完整动态业务加载未认证。任务按用户明确请求完成有界来源综合及相应维护，不冒充HoTT悖论求解或全量认识恢复。

## Claims / Evidence

双方在反对混淆Gödel/发散/卡住、反对无证据存在、区分经典分类与算法方面已有有用对齐。仍需修正唯一选择过度否定、所有transport通用共轭、绝对一致性、一元/二元接口及全系统隔离推论。ASSESSMENT逐项记录，原回复不改。

RP-B01以命题LEM构造χ(p,x)，以同一个通用有效模型的D_h说明无相应无神谕总实现；CONSTRUCTION是经典机制的带明示前提纸笔解释。实际Code形式化、机器执行和目标应用桥梁未完成。PLAN把下一步分为模型绑定、规格/有效性分离、自然解释与实际接口的正反对照，不等待第三封信。

## Mutations

人工作用域：根AGENTS、Z研究owner当前目标、三问v5、业务Skill v1.3.3及manifest、scripts索引、当前对话README/ledger。新增原文、裁决、综合、来源、RP-B01计划与构造、检查脚本和证据。修改前字节在.codex/history/r021-before保存。

本checkpoint同步MEMORY、FRONTIER、LESSONS、RESUME、STATE和本不可覆盖Session；旧记录不删除、不变更path/kind，已有数学状态不升级。D-GEMINI-001仅变更真实来信、来源身份与当前动作，保留待复核状态及说明。

不变：第五闭包、原用户文、理论Schema、固定书式源码、主张矩阵、原形式化源码、治理Skill/引擎/全文加载集合政策、旧sessions、旧论辩信与第一轮意见。

## Verification / Limits

只检查文件身份、原文切片、引用、版本、动态路由、checkpoint事务和Git交付。原文哈希保护当前转录，不证明作者身份或数学。原论文/官方文档用web读取，容器HTML下载DNS失败已记录，未假称完整网页存档。没有数学样本测试、Lean/Agda或独立AI审查。

全文业务认知gate NOT_CLAIMED；不以输出字节、测试数或双方同意代替。没有把当前源中的rev24引用当可取得的真实历史。

## Next Action

恢复本轮源与RP-B01，先补有效通用Code模型及D_h的实际形成，再把定理按真实理论环境核查。保留研究者自由选择新机制，不自动将全部探索缩为经典LEM或软件漏洞查找；成功保护要记录，重复旧机制要退出。
'''
texts={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,
       P+'RESUME.md':resume,P+'STATE.json':dump(state),SESSION:session}
payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
 'authorization':'Current explicit user request to synthesize both Gemini opinions, maintain appropriate project files; prior scripts-first and local Git directives remain in force.',
 'files':[]}
for path,text in texts.items():
    f=R/path
    b=f.read_bytes() if f.exists() else None
    if b is not None:
        bak=R/'.codex/history/r021-before'/path
        if bak.exists():raise RuntimeError('Checkpoint backup exists '+path)
        bak.parent.mkdir(parents=True,exist_ok=True);bak.write_bytes(b)
    payload['files'].append({'path':path,'expected_sha256':sha(b) if b is not None else None,'text':text})
put(CP/'BASE_PLAN.json',before)
put(CP/'PAYLOAD.json',payload)
try:
    dry=rt.checkpoint(R,before['snapshot'],payload,apply=False)
    put(CP/'DRY_RUN.json',dry)
    result=rt.checkpoint(R,before['snapshot'],payload,apply=True)
    put(CP/'COMMIT.json',result)
except Exception as exc:
    put(CP/'FAILURE.json',{'type':type(exc).__name__,'error':str(exc)})
    raise

after=rt.plan(R);put(CP/'FRESH_PLAN.json',after)
assert after['revision']==21 and after['latest_session']==SID
must=set(current+[C+'PLAN.md',C+'CONSTRUCTION.md',C+'CLAIMS.json',SESSION])
assert must <= {x['path'] for x in after['documents']}
newstate=json.loads((R/(P+'STATE.json')).read_text())
assert set(old['records'])<=set(newstate['records'])
allowed_changes={'D-GEMINI-001','U-DUAL-DIRECTION-JSON-001'}
assert all(newstate['records'][k]==v for k,v in old['records'].items() if k not in allowed_changes)
try:rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as exc:
    assert str(exc)=='STALE_BASE'
    put(CP/'STALE_BASE.json',{'status':'REJECTED','error':str(exc)})
else:raise AssertionError('Stale checkpoint accepted')
put(O/'CHECKPOINT_SUMMARY.json',{'status':result['status'],'revision':21,'latest_session':SID,
    'dynamic_documents':len(after['documents']),'new_sources_and_plan_routed':True,
    'prior_records_removed':False,'prior_record_metadata_updated':sorted(allowed_changes),
    'stale_base_rejected':True,'business_gate':'NOT_CLAIMED','new_math_machine_run':False})
print(dump({'status':result['status'],'revision':21,'documents':len(after['documents']),
            'all_new_sources_routed':True,'stale_base_rejected':True}))
