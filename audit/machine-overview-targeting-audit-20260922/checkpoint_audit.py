#!/usr/bin/env python3
"""Prepare the authorized core-8/targeting audit transaction via canonical runtime."""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
SID='S-AUD-20260922-ASTRA-MACHINE-OVERVIEW-TARGETING'
BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-MACHINE-OVERVIEW-TARGETING-AUDIT-20260922'
REPORT='audit/机器统观目标与针对性策略审计-20260922.md'
TRANS='audit/core-cognition-generation-8-transition-20260922.json'
CUR='scripts/audit/core-cognition-curation-v8.json'
PLAN='R-HOTT-FOUR-TRACK-PLAN-20260921'
SOURCE='sources/prompts/Codex-理论经济与针对性悖论策略-用户原文-20260922.md'
NEWESSAY='扩展认知/009 - 从可疑前提到针对性过程.md'

def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
R=module('runtime','.codex/tools/cognition_runtime.py')
B=module('builder','scripts/audit/build_core_cognition.py')
sys.path.insert(0,str(ROOT/'scripts/audit'))
import projection_edit as E

# Human adjudication: these positions are authored per KC, not inferred by matching words.
ASSESSMENTS=[
 ('ALIGNED','三问回到实际前提与过程，不用工具产量回答'),
 ('DEEPENED','理论地图是来源路由；35条和478项不能冒充全理论'),
 ('DEEPENED','合取条件需在所选过程中起决定作用，模型应承载它'),
 ('ALIGNED','反证方向保留，完整比较与归因仍待证'),
 ('ALIGNED','靶点是可撤回生成假说，最终病因后置'),
 ('ALIGNED','不把多条时间机制全压进Delay Bool'),
 ('ALIGNED','AI可提候选，不能以流畅类比证明原前提'),
 ('ALIGNED','历史悖论启发过程，不能以同名替代保真桥'),
 ('DEEPENED','审计D-01的源内规则到现实解释加强'),
 ('ALIGNED','目标仍为现实相对过程，未改成找类型拒绝'),
 ('ALIGNED','计算次序与物理运动分开；delay不承担所有时间'),
 ('ALIGNED','ASK检查进入推演的资格，具体拒绝不等于理论失败'),
 ('DEEPENED','工具性由真实选择定位；未把一般不可停机叫悖论'),
 ('ALIGNED','B方向需要真实能力提升，delay分离只给形状'),
 ('ALIGNED','Z强律保留为研究起点，不认证全称成立'),
 ('ALIGNED','Russell过程读法作方法启发，未重证或改写原文'),
 ('ALIGNED','先理解用户观察角度，再与源码逐项比较'),
 ('DEEPENED','经济性省略转成敏感过程，不用否定口号越级'),
 ('ALIGNED','判据中保留条件依赖与同任务对照'),
 ('ALIGNED','量子化原话完整保留，不冒充经验事实'),
 ('ALIGNED','本轮源码审计无新数学结论，不重跑无关内核'),
 ('CORRECTED','旧报告把delay分离直接算B覆盖的范围收窄'),
 ('DEEPENED','基础规则先核真实定义，不以类比指认病因'),
 ('ALIGNED','稠密结构与时序两轴保持，A/B不被同一模板穷尽'),
 ('NOT_TOUCHED','本轮不重开自指发现；新同任务自指义务才触及'),
 ('NOT_TOUCHED','未裁决HoTT自身自指极限；新原生任务才重开'),
 ('ALIGNED','共有程序界限的实例不等于HoTT新增失真'),
 ('NOT_TOUCHED','自馈回环具体构造未执行；有精确新义务再启动'),
 ('DEEPENED','用经济收益定位靶前提，拒绝只追求可枚举性'),
 ('ALIGNED','旧C11已有经济账本，承认其历史贡献而不重新发明'),
 ('CORRECTED','两个被拒写法不等于所有观察器不可表达'),
 ('ALIGNED','稠密性怀疑需源内结构和模型身份，不能按名称移植'),
 ('ALIGNED','过程缺席作为独立候选方向保存，未给最终历史归因'),
 ('ALIGNED','省略与新增理想条件分别记录，不混作单一擦除'),
 ('DEEPENED','生成器的表达范围也成为被审对象'),
 ('NOT_TOUCHED','未启动Gödel对象层研究；R3/R4仅历史边界'),
 ('TENSION','容易发现的期待与统观未闭合并存，不保证新方法必胜'),
 ('DEEPENED','作者前提识别必须进入源文，不能只列清单'),
 ('CORRECTED','未奏效的原因定位到代理模型连接和执行选择'),
 ('DEEPENED','知识谱清单不能自证完整；source反观先于枚举'),
 ('ALIGNED','用工具核验与超越既有选题分别判断'),
 ('ALIGNED','熟练工具带来的便利可能影响选题，未作定量因果定律'),
 ('DEEPENED','旧机制重复被写成下一动作限制而非再次披露'),
 ('ALIGNED','现实或假想现实允许作为任务域，先固定合同'),
 ('DEEPENED','现实对齐必须落在具体可观察条件，非类比即结论'),
 ('DEEPENED','机器统观的原始现实问题保留，不限于内部语法'),
 ('DEEPENED','完整保存经济性与普适性—前提—反差的用户原文'),
 ('DEEPENED','每波重读整段，检验靶前提敏感性再扩大实验'),
]

def audit(core):
    m=json.loads((ROOT/'核心认知.manifest.json').read_text())
    assert len(m['units'])==len(ASSESSMENTS)==48
    lines=[f'# {SID} 核心认知审计','',f"- identity: {core['generation']} / {core['core_sha256']} / 48 KC",
      '- core_change: YES; 两段完整原文进入KC47/48，旧46段精确保留。',
      '- direction_change: 统观保真连接核对进入P40准入，未执行新的候选搜索。',
      '- panorama_change: 新方法审计与I探针证据收窄；历史运行不改。',
      '- essay_change: YES; 009展开针对性方法；006两处旧引文对齐core原字节。',
      '- update_decision: core manager加canonical checkpoint；App goal实测paused，仅完成本轮用户授权。',
      '- cross_conflicts: 旧投影把代理模型/I探针写得过强，本事务原位收窄。',
      '- unresolved: P40未选择；HoTT必要性/现实同任务桥未闭合；writer新session嵌套分片缺口仍开放。','',
      '| KC | 主题 | relation | 本轮姿态与判断 | 证据 | 下一动作及反证条件 |',
      '|---|---|---|---|---|---|']
    for u,(relation,claim) in zip(m['units'],ASSESSMENTS):
        lines.append(f"| `{u['id']}` | {u['semantic_label']} | `{relation}` | {claim} | {REPORT} §§001–003；原KC原文 | P40先核前提—模型连接；若取得原生保真桥则撤回相应缺口判断；未触及项只在新精确义务下重开 |")
    lines+=['','## 扩展认知逐片回评','',
      '| 片 | 实际使用、偏航与下一动作 |','|---|---|',
      '| 001 | 理论收益与省略都要看；原方案已有这条思路，本轮不抹掉历史。 |',
      '| 002 | 条件变化到结果反差需依赖；稠密与先后分开，D-01解释须复核。 |',
      '| 003 | A/B和ASK保留；旧delay分离不自动算现实B；X₀回接义务未变。 |',
      '| 004 | Schema定位源内规则，未复活自反深支；P40从前提选择。 |',
      '| 005 | 两个探针不足以全称否定表达；机器通过不替代原命题。 |',
      '| 006 | 知识谱是被审对象，发现旧引文39/40与core范围不一致，按core修正引用。 |',
      '| 007 | 便利的delay后端可能使选题重复；核验器不负责选择值得检验的前提。 |',
      '| 008 | 用现实解释理论继续有效；解释不是保真定理。 |',
      '| 009 | 新的完整原文与靶点—敏感过程—保真连接方法相连；允许反证与撤回。 |',
      '', '## 已走路径、未来选择及全部反思', '',
      f'完整逐项回答在 `{REPORT[:-3]}/003 - 原文常驻、方案修订与波次反思.md`：Goal-3 §3九问、§3.1五问、§3.3六问、SOP八项、八轴遗漏与四分支比较。裁决CLOSE_WITH_SCOPE；后继P40保持待执行，App goal仍paused。',
      '', '## 加载与writer边界','',
      '原revision258 canonical receipt及HEAD.tracked全匹配；核心旧46段逐条复认并全文重读。core变化后按core→direction→panorama→essay全文重读，工具截断处补读原行；本轮新增009正文和修改delta再读。STATE既有T3身份依revision258收据复认、hot/受影响records本轮直接查询，不声称本轮重读1.37MB全STATE。工具哈希不认证模型理解。',
      'G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001继续使用完整单文件兼容审计；本轮48项由runtime按current_core动态验证，不伪称嵌套分片原子事务已实现。']
    return '\n'.join(lines)+'\n'

def replace_row(doc,path,identity,new):
    lines=doc['shards'][path].splitlines(keepends=True)
    matches=[i for i,l in enumerate(lines) if l.startswith(f'| `{identity}` |')]
    assert len(matches)==1,(identity,matches)
    lines[matches[0]]=new+'\n';doc['shards'][path]=''.join(lines)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==258
    oldcore=state['current_core']
    head=json.loads((ROOT/R.HEAD).read_text())
    assert all(sha(p)==h for p,h in head['tracked'].items())
    transition=dict(from_generation=oldcore['generation'],to_generation='core-cognition-generation-8',manifest='核心认知.manifest.json',transition=TRANS)
    p=R.plan(ROOT,profile='governance',_allow_core_transition=transition)
    assert not p['review_required'] and not p['hydration_diagnostics']['query_first_promoted']
    (HERE/'PLAN.json').write_bytes(R.dump(p))
    core=dict(path='核心认知.md',manifest='核心认知.manifest.json',curation=CUR,transition=TRANS,
              generation='core-cognition-generation-8',kc_count=48,core_sha256=sha('核心认知.md'),
              manifest_sha256=sha('核心认知.manifest.json'),curation_sha256=sha(CUR))
    state['current_core']=core;state['revision']=259;state['latest_session']=SID
    refs=[REPORT]+[str(x.relative_to(ROOT)) for x in sorted((ROOT/REPORT[:-3]).glob('*.md'))]
    refs += [str((HERE/'EVIDENCE.json').relative_to(ROOT)),SOURCE,CUR,TRANS]
    state['records'][RID]=dict(kind='result',path=REPORT,lifecycle_status='CLOSED',status='source_audited_with_scope',
      evidence_status='SOURCE_AND_RECEIPT_AUDIT_WITH_SCOPE / NO_NEW_MATH_CLAIM',depends_on=[],
      full_sources=refs,source_hashes={x:sha(x) for x in refs},related_records=[PLAN,'A-PREMISE-001'],
      scope='Machine-overview premise-to-model fidelity audit; exact core additions; two specific I rejections do not establish universal undefinability or a faithful translation.')
    state['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',
      evidence_status='CORE8_REGISTERED_AND_TARGETING_AUDIT_COMPLETE',depends_on=[],related_records=[RID,PLAN],
      full_sources=[BASE+x for x in ('SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md')])
    # Rebind only the current plan's explicitly reviewed, changed source owners.
    changed=['goal-3.md','rulings.md','feature-list.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md']
    owner=state['records'][PLAN]
    actual={x for x,h in owner['source_hashes'].items() if (ROOT/x).is_file() and sha(x)!=h}
    assert actual==set(changed),actual
    for x in changed:owner['source_hashes'][x]=sha(x)
    owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,SID]))
    owner['revalidation']+=' Revision259: source-reviewed targeting audit and KC47/48 inclusion; P40 still not executed. App goal observed paused.'
    owner['evidence_status']='PLAN_REVISED_BY_USER / P40_TARGET_FIDELITY_NEXT / APP_GOAL_OBSERVED_PAUSED / NO_NEW_MATH_CLAIM'
    state['execution_control'].update(status='MACHINE_OVERVIEW_TARGETING_AUDIT_COMPLETE_P40_PENDING',last_checkpoint_session=SID,
      checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='paused',
      next_minimal_verification=state['execution_control']['next_minimal_verification']+' Before that selection, read KC-000047/048 in full and this audit. Requalify D-01 density interpretation; establish target sensitivity and representation fidelity before expanding any generator. Execute only under renewed research authorization or resumed goal.')
    state['projection']['status']='CORE8_MACHINE_OVERVIEW_AUDIT / P40_PENDING / APP_GOAL_OBSERVED_PAUSED / NO_NEW_MATH'
    memory=E.load(ROOT,'MEMORY.md');direction=E.load(ROOT,'方向追踪.md');panorama=E.load(ROOT,'全景视野.md');essay=E.load(ROOT,'扩展认知.md')
    mp='MEMORY/001 - 当前执行队列.md'
    old=memory['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0]
    msg='机器统观目标忠实性回顾完成：理论前提→代理模型连接不足、D-01稠密解释需资格化、I探针范围已收窄。用户两段完整原文进入core generation-8的KC47/48；goal-3要求每波/压缩恢复整段重读并检验靶前提敏感性。P40三项选择尚未执行，原后继保留；本轮App goal实测paused，不自动恢复。入口：`audit/机器统观目标与针对性策略审计-20260922.md`；revision259。'
    E.replace_in_shard(memory,mp,old,msg)
    E.append_to_shard(memory,'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：core8/48、旧46逐字保留；统观源文/模型/收据审计与goal-3原文常驻要求；无新数学claim或内核运行，P40待执行。revision259。\n')
    for doc,kind in [(direction,'direction'),(panorama,'outcome')]:
        E.replace_in_index(doc,'source_state_revision: 258','source_state_revision: 259')
        E.replace_in_index(doc,f'projection_generation: 20260922-{kind}-258',f'projection_generation: 20260922-{kind}-259')
        E.replace_in_index(doc,'semantic_status: FOUR_TRACK_P40_PREMISE_TARGETED_CANDIDATE_NEXT','semantic_status: CORE8_MACHINE_OVERVIEW_AUDIT_P40_PENDING')
        E.replace_in_index(doc,'状态：`INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE`','状态：`CORE8_MACHINE_OVERVIEW_AUDIT_P40_PENDING`')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(direction,d,'DIR-TOP-PREMISE-INVENTORY','| `DIR-TOP-PREMISE-INVENTORY` | HoTT前提清单及现实对齐候选 | KC44–48、PREMISE-001 | `HISTORICAL_INVENTORY_REUSED / FIDELITY_REVIEW_REQUIRED` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-TOP-PREMISE-001-REGISTRATION`、`OUT-MACHINE-OVERVIEW-TARGETING-AUDIT` | A–G35条仅范围内清单，9条AI非现实判断待审；D-01密度解释与GEN代理须重核。I三探针只支持给定形式接受/拒绝，未证完整保真翻译或全称不可定义 | PREMISE-001原件；本轮统观审计；revision259 |')
    replace_row(direction,d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | P40靶前提—针对过程的保真准入 | KC47–48、本轮统观审计 | `P40_PENDING / APP_GOAL_OBSERVED_PAUSED` | `PARADOX_DISCOVERY`, `THEORY_ECONOMY` | `OUT-HOTT-FOUR-TRACK-PLAN`、`OUT-MACHINE-OVERVIEW-TARGETING-AUDIT` | 后续从G-04/D-01/Book§11.2最多选一张卡，先核前提身份及模型敏感性；不重跑旧delay枚举 | goal-3 §0B；统观审计；revision259 |')
    out='全景视野/002 - 治理、门禁与骨架结果.md'
    replace_row(panorama,out,'OUT-TOP-PREMISE-001-REGISTRATION','| `OUT-TOP-PREMISE-001-REGISTRATION` | A–G35条前提登记与P2/P3P4候选分析 | `DIR-TOP-PREMISE-INVENTORY` | PREMISE-001 001–008与旧审计 | `HISTORICAL_INVENTORY_WITH_SCOPE / AI_VERDICTS_PENDING_AUDIT` | 35条登记、9条候选和5族供给可回源；结构层/可选原则遗漏已有登记 | 不证明全HoTT前提穷尽或9条非现实；GEN链不补原生前提保真；D-01解释须重新资格化 | PREMISE-001；本轮统观审计002 |')
    E.append_to_shard(panorama,out,f'\n| `OUT-MACHINE-OVERVIEW-TARGETING-AUDIT` | 原统观目标、前提识别和代理模型连接审计；core8原文纳入 | `DIR-TOP-PREMISE-INVENTORY`、`DIR-U-HOTT-FOUR-TRACK` | 原方案、生成目标、源码及保存run | `SOURCE_AND_RECEIPT_AUDIT_WITH_SCOPE / NO_NEW_MATH_CLAIM` | 原方案已有针对性；代理连接未闭合，I探针叙述需收窄；KC47/48整段保存 | 不证明HoTT有或无悖论、新方法必胜、全历史语义审计或未来永久注意力 | {REPORT}；revision259 |\n')
    # Remove wording that suggests the native premises were actually tested by the analogue.
    for old,new in [('A-03 方向 B 的机器化','A-03相关Delay Bool类比的机器化'),('B-01 的机器化','B-01相关Delay Bool类比的机器化'),('三联的机器化','三联相关Delay Bool类比的机器化'),('双成员的机器化','双成员相关Delay Bool类比的机器化')]:
        assert old in panorama['shards'][out];panorama['shards'][out]=panorama['shards'][out].replace(old,new,1)
    pp='全景视野/008 - 当前未完成.md'
    E.append_to_shard(panorama,pp,'\n17. 统观前提—模型保真连接：旧Delay Bool/DM3仅按代理模型范围使用；I探针不提供全称不可定义或完整翻译。下一P40先核源内靶点与敏感过程，不重复旧枚举。\n')
    # Add one coherent exposition shard through the same canonical transaction.
    E.replace_in_index(essay,'last_shard: 扩展认知/008 - 现实对齐：理论是现实的骨架式模仿.md',f'last_shard: {NEWESSAY}')
    E.replace_in_index(essay,'下方 8 个分片','下方 9 个分片')
    E.replace_in_index(essay,'baseline: core-cognition-generation-7','baseline: core-cognition-generation-8')
    E.replace_in_index(essay,'generation-7 的全部 46 段原文','generation-8 的全部 48 段原文')
    E.replace_in_index(essay,'<!-- governance-shard-table:end -->',f'| 009 | [从可疑前提到针对性过程](<{NEWESSAY}>) | KC47–48完整原文、敏感过程、模型保真及机器统观教训 | current |\n<!-- governance-shard-table:end -->')
    raw=B.parse_core_payloads((ROOT/'核心认知.md').read_text())
    def quote(k):return f'<!-- original:{k}:begin -->\n'+ '\n'.join('> '+l for l in raw[k].splitlines())+f'\n<!-- original:{k}:end -->'
    essay['shards'][NEWESSAY]='''<!-- governance-shard:v2
logical_id: CORE-ESSAY
shard_id: 009
index: ../扩展认知.md
-->

# 从可疑前提到针对性过程

本片展开HoTT现实相对研究中的候选发现方法。它保留用户的强研究立场，说明如何使这份立场进入具体过程的选择；不把哲学判断或物理前提转换为已证定理。

## 理论经济与普适性需要被一起考察

'''+quote('KC-000047')+'''

理论为了简洁而省略什么，为了普适而理想化什么，是两个相关但不完全相同的提问。前者可能放下来源、等待或成本；后者可能把有限情形推广成统一结构。这里必须让整个过程回到视野中：原来要完成什么，哪些条件在通常情形里似乎无关，在哪个特殊情形里又成为决定因素。

原文把这种反差放进反证视角。进入具体研究时，应当分别追踪理论前提、解释关系、观察与完成条件；仅仅看到现实与模型不同，还没有定位是哪一项假设造成了差异。用户原话中的必然性、量子化及历史归因保持原文身份；严肃检验要求允许具体候选失败。

## 有靶点还不够：过程要对它敏感

'''+quote('KC-000048')+'''

这次修正说明，精彩的过程并非从任意枚举中等待出现。它要让某项平常被省略的条件重新决定结果。研究者先提出可撤回的靶点，构思专门过程，同时尝试保条件的正控制；最后再讨论理论、公理、使用与实现的归因。这样的顺序与“先找到现象、后定最终病因”相容。

机器统观的教训是：把不同前提都映到同一个方便计算的模型，容易使模型代替原问题。原生证明器接受一个Delay Bool命题，验证的是这个命题；它不会自动验证“该模型忠实代表区间稠密性或高阶相等迭代”。在扩大搜索前，要先看靶前提是否确实由模型承载，改变它能否改变推导或观察。只有名字改变、实际目标未变，不能算检验了新前提。

## 原文怎样真正影响下一步

每波与压缩恢复时，按goal-3 §0B完整重读这两段；随后用当前对象回答经济收益、省略条件、针对过程和反解释。反思时再看新增的是靶点、保真连接、过程反差还是辅助能力。旧缺口必须改变下一选择，不能仅在报告尾部重复。

本片不是另一份当前队列。具体状态仍由STATE与方向／全景拥有；本次源文、代码及收据索引见 `audit/机器统观目标与针对性策略审计-20260922.md`。加载原文是必要输入，持续理解与合理选题仍需用实际行为检验。
'''
    e6='扩展认知/006 - 第三条发现路径：把知识谱当作被考察对象.md'
    for k in ('KC-000039','KC-000040'):
        essay['shards'][e6],n=re.subn(r'<!-- original:'+k+r':begin -->.*?<!-- original:'+k+r':end -->',lambda m:quote(k),essay['shards'][e6],flags=re.S);assert n==1
    for key,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:
        state['records'][key].update(projection_generation=f'20260922-{kind}-259',semantic_status='CORE8_MACHINE_OVERVIEW_AUDIT_P40_PENDING',scope='Current targeting audit and core8; historical entries retain their scoped evidence; P40 pending.')
    rows=[]
    for doc in (memory,direction,panorama,essay):rows+=E.payload_rows(doc,ROOT)
    done={r['path'] for r in rows}
    for path in R.MUTABLE:
        if path in done:continue
        text=(ROOT/path).read_text()
        if path==R.STATE:text=R.dump(state).decode()
        elif path.endswith('FRONTIER.md'):
            text=re.sub(r'^- 用户纠正P40候选生成顺序：.*$', '- '+msg,text,flags=re.M)
        elif path.endswith('RESUME.md'):
            text=re.sub(r'^当前 active goal 已按用户靶点先行裁定纠正P40：.*$',msg,text,flags=re.M)
        rows.append(dict(path=path,expected_sha256=sha(path),text=text))
    session=f'''# {SID}

- host: codex-desktop
- model: runtime-model-not-certified-by-tool
- tier: T3
- status: SOURCE_AUDIT_COMPLETE / CORE8_48 / P40_PENDING
- load_receipt: PLAN.json snapshot {p['snapshot']}; full four-set reread on core change, recovery reattestation for unchanged prior T3 state.
- scope: 用户要求的机器统观回顾、两段原文纳入、Goal-3方法修订；无新数学研究或kernel replay。
- authorization: 本轮明确要求及已有本地方案/检查点维护授权；不push/tag，不修改外部worktree，不启动Sub Agent。
- app_goal: observed paused; not resumed by this audit.
- writer_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001; full48-KC legacy single-file compatibility, no new nested-writer claim.

## element_usage

| 元件 | 用途或边界 |
|---|---|
| core/essay | 两段原文完整保存并展开；不是定理 |
| direction/panorama | 模型连接缺口、范围收窄与下次选择 |
| STATE/checkpoint | 唯一当前状态与原子收据 |
| original plan/code/run | 区分意图、实际目标与历史检查结果 |
| web primary | 核区间解释来源，不作新机器证明 |
| proof gate | 不把探针拒绝升级全称结论 |
| Goal-3 | 全部反思见报告003；不重造平台 |

影响与反思：{REPORT[:-3]}/003 - 原文常驻、方案修订与波次反思.md。
'''
    bundle={'SESSION.md':session,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,
      audit_evidence=str((HERE/'EVIDENCE.json').relative_to(ROOT)),new_math_claims=[],new_kernel_runs=[],app_goal_observed='paused')).decode(),
      'CORE_COGNITION_AUDIT.md':audit(core)}
    rows += [dict(path=BASE+k,expected_sha256=None,text=v) for k,v in bundle.items()]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],core_transition=transition,
      authorization='用户明确要求评估机器统观、完整纳入两段原文并审查goal-3；沿用本地方案版本化和canonical checkpoint授权。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(payload))
    res=R.checkpoint(ROOT,p['snapshot'],payload,apply=args.apply)
    (HERE/('APPLY.json' if args.apply else 'DRY-RUN.json')).write_bytes(R.dump(res))
    print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
