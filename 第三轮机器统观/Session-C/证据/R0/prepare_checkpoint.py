#!/usr/bin/env python3
"""Build this one R0 payload; only cognition_runtime may apply current state.

This is a one-time task artifact, not a second registry/writer. Existing current
files are read-only here; the output uses exclusive creation and exact hashes.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / '.codex/tools'))
sys.path.insert(0, str(ROOT / 'scripts/audit'))
import cognition_runtime as cr
import projection_edit as pe

SID = 'S-RES-20260924-MO3-C-R0'
TASK = 'MO3-COVERAGE-C'
BASE_HEAD = '4cc4f6ea4cf30864e911b63b45b5c038ba4f50eb'
BASE_STATE = '18fc033da7e2453872eb01d461b83dccda6ac1d6fcf7cb6218b43a7524917b3b'
C = '第三轮机器统观/Session-C/'
OUT = ROOT / C / '证据/R0/checkpoint-payload-002.json'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def replace_once(body, old, new):
    assert body.count(old) == 1, ('REPLACE_COUNT', old[:80], body.count(old))
    return body.replace(old, new, 1)

def main():
    assert subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=ROOT, text=True).strip() == str(ROOT)
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip() == BASE_HEAD
    assert not subprocess.check_output(['git', 'diff', '--cached', '--name-only'], cwd=ROOT)
    assert sha((ROOT / cr.STATE).read_bytes()) == BASE_STATE
    assert not (ROOT / cr.PREFIX / 'sessions' / SID).exists()
    state = json.loads((ROOT / cr.STATE).read_text())
    assert TASK not in state['records'] and SID not in state['records']
    plan = cr.plan(ROOT, profile='research')
    rev = state['revision'] + 1
    docs = {p: pe.load(ROOT, p) for p in ('MEMORY.md', cr.DIRECTION, cr.PANORAMA, cr.ESSAY)}
    texts = {p: (ROOT / p).read_text() for p in cr.MUTABLE if p not in docs}
    old_current = 'MO3研究义务已按执行014逐项结案，C327–341与source/有限运行各保范围；本轮无合格现实相对命中。006/008解释纠偏保原文。交付末步由第三轮机器统观/Session-A/交付/final-002/SEAL.json及verify拥有：若有效则交用户B独立审计；若缺失/失败则继续封存，不重开旧研究队列。revision283，B未审；final-001及副本命令失败保留，新代次修正说明。'
    current = ('当前用户启动Goal7 / MO3-COVERAGE-C，Session C为本续做阶段唯一研究integrator。R0已完成启动读取、独立父范围入口、旧A固定输入和初次精确复用；父范围仍PARENT_SCOPE_INCOMPLETE。105编号节/54 Schema入口不等已审，A01.W/B05.03只有有范围来源审查。旧A四包C327–341按精确命题复用，不继承其整体完成判词；未重跑kernel。下一步按Session-C父范围owner推进Book正文与扩展配置实审；最高指示在新理论单元/压缩后全文重读。W全树执行种子与旧C03同题，不再新造同义proof；Book5.5内部化/计算接口保留待审。C无最终seal、命中未定、D未审。旧A final-002作为只读阶段成果；当前revision由STATE与本次canonical result决定。')
    pe.replace_in_shard(docs['MEMORY.md'], 'MEMORY/001 - 当前执行队列.md', old_current, current)
    pe.replace_in_shard(docs['MEMORY.md'], 'MEMORY/001 - 当前执行队列.md', '## 用户当前专题（2026-09-19）', '## 用户当前专题（2026-09-24）')
    pe.append_to_shard(docs['MEMORY.md'], 'MEMORY/003 - 当前验证状态与顺序日志.md', f'\n{SID}：Goal7的C首次注册；父来源入口与W来源查重、四包selected证据/Git核验，未新跑kernel；全registry旧Coq错配仍在。R1/R2继续，父范围未完成；revision{rev}，canonical结果另核。\n')
    texts[cr.PREFIX+'FRONTIER.md'] = replace_once(texts[cr.PREFIX+'FRONTIER.md'], old_current, current)
    texts[cr.PREFIX+'RESUME.md'] = replace_once(texts[cr.PREFIX+'RESUME.md'], old_current, current)
    texts[cr.PREFIX+'RESUME.md'] = replace_once(texts[cr.PREFIX+'RESUME.md'], '3. 当前用户Goal6为MO3-GOVERNED-A：先query该稳定record，再research task plan；按Goal6恢复执行Skill、最高指示及本轮执行记录。旧C4/Goal/1/3仅在任务真实依赖时读取，不自动复活。', '3. 当前用户Goal7为MO3-COVERAGE-C：先query真实record，再research task plan；按Goal7恢复执行Skill、最高指示、Session-C父范围/复用/过程/执行记录。旧A final-002只读复用，不继承整体完成。旧Goal/1/3不复活。')
    for p in (cr.DIRECTION, cr.PANORAMA):
        doc = docs[p]
        pe.replace_in_index(doc, '状态：`MO3_RESEARCH_CLOSED_SEAL_RECEIPT_REQUIRED`', '状态：`MO3_C_PARENT_SCOPE_INCOMPLETE`')
        pe.replace_in_index(doc, 'semantic_status: MO3_RESEARCH_CLOSED_SEAL_RECEIPT_REQUIRED', 'semantic_status: MO3_C_PARENT_SCOPE_INCOMPLETE')
        pe.replace_in_index(doc, 'source_state_revision: 283', f'source_state_revision: {rev}')
        word = 'direction' if p == cr.DIRECTION else 'outcome'
        pe.replace_in_index(doc, f'projection_generation: 20260924-{word}-283', f'projection_generation: 20260924-{word}-{rev}')
    ds = '方向追踪/002 - 治理与用户方向.md'
    old_row = next(x for x in docs[cr.DIRECTION]['shards'][ds].splitlines() if x.startswith('| `DIR-U-MO3-GOVERNED`'))
    new_row = old_row.replace('第三轮递归多尺度与针对性过程', '第三轮旧A阶段：递归多尺度与针对性过程').replace('`RESEARCH_CLOSED / SEAL_RECEIPT_REQUIRED`', '`HISTORICAL_STAGE / PARENT_COMPLETION_NOT_ESTABLISHED`').replace('核实际新seal；有效后交用户B，不自动新开研究', 'final-002保只读阶段证据；接续父任务由Goal7/C承担')
    pe.replace_in_shard(docs[cr.DIRECTION], ds, old_row, new_row)
    pe.append_to_shard(docs[cr.DIRECTION], ds, '| `DIR-U-MO3-COVERAGE-C` | 第三轮父范围充分性与研究义务续做 | 用户Goal7、KC2/40/44–48 | `ACTIVE / PARENT_SCOPE_INCOMPLETE` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C-R0` | 从固定父范围逐项实审、精确复用与独立充分性挑战 | 第三轮机器统观/Session-C/父范围与覆盖.md；MO3-COVERAGE-C |\n')
    ps = '全景视野/002 - 治理、门禁与骨架结果.md'
    old_row = next(x for x in docs[cr.PANORAMA]['shards'][ps].splitlines() if x.startswith('| `OUT-MO3-FINAL-SYNTHESIS`'))
    new_row = old_row.replace('第三轮研究综合及交付条件', '旧A阶段研究综合及交付条件').replace('`RESEARCH_COMPLETE_WITH_SCOPE`', '`OLD_A_STAGE_DELIVERY / PARENT_COMPLETION_NOT_ESTABLISHED`')
    pe.replace_in_shard(docs[cr.PANORAMA], ps, old_row, new_row)
    pe.append_to_shard(docs[cr.PANORAMA], ps, '| `OUT-MO3-C-R0` | C独立父范围入口与旧成果精确复用 | `DIR-U-MO3-COVERAGE-C` | 全文认知、原典/Schema、105/54入口、W源审查、四包证据关系/Git及seal字节核验 | `R0_INTAKE_AND_SOURCE_SLICE / PARENT_SCOPE_INCOMPLETE` | W种子复用旧C03来源边界；新增5.5内部规格/计算待审入口 | 入口计数非充分性；无新kernel run；旧Coq错配与C02警告函数名错位保留；D未审 | 第三轮机器统观/Session-C/旧成果复用与缺口.md；第三轮机器统观/Session-C/审计/R0/CORE_COGNITION_AUDIT.md |\n')
    us = '全景视野/008 - 当前未完成.md'
    old17 = next(x for x in docs[cr.PANORAMA]['shards'][us].splitlines() if x.startswith('17. MO3-GOVERNED-A'))
    pe.replace_in_shard(docs[cr.PANORAMA], us, old17, '17. MO3-COVERAGE-C按Goal7接续同一第三轮；当前父范围PARENT_SCOPE_INCOMPLETE。旧A final-002只读，四包精确复用不关闭Book/全部C/D/S/E及内部路线；C须完成来源处置、多层关系、独立充分性挑战和范围内研究义务，再给新seal交用户D。当前没有C最终封存或D通过。')
    next_action = 'R1/R2：按Session-C父范围与覆盖逐章读取Book正文并完成语义处置，先从第1章与附录基础接口的对应开始；保留Book5.5内部化/计算问题及全部扩展未审项。新理论单元先全文重读最高指示和KC47/48、公开生成。禁止将旧A整体完成或四proof复用当父范围充分。'
    state['revision'] = rev
    state['latest_session'] = SID
    state['active'] = [x for x in state['active'] if x != 'MO3-GOVERNED-A'] + [TASK]
    control = state['execution_control']
    control.update(active_goal_path='goal-7.md', active_goal_record=TASK,
                   app_goal_status_observed='active', app_goal_completion_eligible=False,
                   current_phase='MO3_C_R1_PARENT_SCOPE_AND_SEMANTIC_REVIEW',
                   status='MO3_C_PARENT_SCOPE_INCOMPLETE', domain_sop='goal-7.md; compatible discipline goal-5.md',
                   current_role='RESEARCH_GENERATION', last_checkpoint_session=SID,
                   checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',
                   completion_eligibility_scope='All six Goal7 gates remain required; parent scope not sufficient yet; no C final seal or D pass.',
                   next_minimal_verification=next_action,
                   previous_delivery_seal_path=control.get('delivery_seal_path'), delivery_seal_path=None,
                   second_phase_status='MO3_C_PARENT_SCOPE_INCOMPLETE; OLD_A_STAGE_HISTORICAL')
    state['projection']['status'] = 'MO3_C_PARENT_SCOPE_INCOMPLETE / HIT_UNDETERMINED / D_NOT_AUDITED'
    for rid,word in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:
        rec=state['records'][rid]
        rec['projection_generation']=f'20260924-{word}-{rev}'
        rec['semantic_status']='MO3_C_PARENT_SCOPE_INCOMPLETE'
        rec['scope']='Goal7 continuation C; initial parent entries and scoped source/proof reuse, no parent completion or new kernel run.'
    sources=['goal-7.md','.codex/skills/hott-machine-overview-execution/SKILL.md','最高指示.md',
             'audit/第三轮机器统观全面覆盖与完成资格专项复核-20260924.md',
             C+'父范围与覆盖.md',C+'过程与结果.md',C+'旧成果复用与缺口.md',
             C+'审计/R0/CORE_COGNITION_AUDIT.md',C+'证据/R0/旧证明包检查-001.json',
             C+'证据/R0/旧证明与封存比较.json',C+'证据/R0/旧A封存字节核验.json']
    for d in ['父范围与覆盖','过程与结果','审计/R0/CORE_COGNITION_AUDIT']:
        sources.extend(str(p.relative_to(ROOT)) for p in sorted((ROOT/C/d).glob('*.md')))
    state['records'][TASK]={'kind':'research_task','path':C+'执行记录.md','lifecycle_status':'ACTIVE_WORK',
        'evidence_status':'IN_PROGRESS_PARENT_SCOPE_NOT_ESTABLISHED','status':'active',
        'scope':'Goal7 fixed Book/appendix, all C/D/S/E and named branches plus relevant configurations/interfaces; parent sufficiency and research obligations both required.',
        'depends_on':[],'related_records':['MO3-GOVERNED-A'],'full_sources':sources,
        'source_hashes':{p:sha((ROOT/p).read_bytes()) for p in sources},
        'execution_control':{'phase':'R1_PARENT_SCOPE_AND_R2_REVIEW','next_minimal_verification':next_action,
                             'coverage_status':'PARENT_SCOPE_INCOMPLETE','hit_status':'UNDETERMINED','audit_status':'NOT_AUDITED'}}
    sb=cr.PREFIX+'sessions/'+SID+'/'
    state['records'][SID]={'kind':'session','path':sb+'SESSION.md','lifecycle_status':'HISTORICAL',
        'status':'complete_with_scope','evidence_status':'INTAKE_SOURCE_REVIEW_AND_EXISTING_PROOF_EVIDENCE_CHECKED',
        'depends_on':[],'related_records':[TASK],'full_sources':[sb+x for x in cr.SESSION_REQUIRED_FILES],
        'source_hashes':{},'scope':'First C intake registration only; parent scope and Goal remain incomplete.'}
    texts[cr.STATE]=cr.dump(state).decode()
    session=f'''# {SID}：Goal7接手、父范围入口与精确复用

HoTT固定父范围的覆盖充分性与研究完成义务为父目标。本单元以全文认知、原典/Schema、独立入口表、W生成及查重、旧四包源码/run/index/Git核验形成R0接手依据；不交付新数学定理或父范围完成。

- host: Codex desktop
- model: 用户选择的Astra会话；不以自述认证后端路由
- tier: T3
- role: RESEARCH_GENERATION / sole continuation research integrator
- load_receipt: 初始research snapshot {plan['snapshot']}；证据/R0/INPUT-IDENTITY.json及执行记录001的实际范围
- core: {state['current_core']['generation']} / {state['current_core']['kc_count']} KC
- scope: Goal7；COMPOSE_FROM_OWNERS / OWNER_UPDATE；原典入口先于旧A案例
- authorization: 当前用户/goal明确允许C独占研究、必要current owners、canonical checkpoint与精确本地提交；禁止事项保持。
- baseline: main {BASE_HEAD}，index为空；其它既存dirty不属于C。

初次四件套严格顺序全文；压缩后最高指示/Goal7/role/common全文恢复，26文件逐项hash复认、core全文、008/009原文抽查与逐KC立场均在执行记录。STATE1–19326连续完成。research三问、references、规划六片、Goal5/四依据/Schema全文及原始main/formal已读；Book其余正文未冒已读。

产物：{C}父范围与覆盖.md（初始105/54入口，非充分性）；过程与结果001（W来源薄层，复用旧C03，不另写同义proof）；旧成果复用与缺口.md（四包exact范围，SOURCE/有限运行分轴）；审计/R0完整48KC与阐释/反思。

运行：四primary raw evidence检查exit0；selected evidence与Git检查exit0；全registry exit2旧Coq错配保留；seal字节通过；53个所选非缓存文件与固定seal匹配，11个再生接口不在seal。没有新kernel run。C02 warning名错位在C报告说明，不改A。

状态：本事务仅注册C并接续current queue；R1–R5及六门未完成，PARENT_SCOPE_INCOMPLETE，命中未定，D未审，无C最终seal。事务成功只认canonical result.json，本文不自证apply。

下一动作：{next_action}

writer兼容：G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001未修。事务内完整单文件legacy audit由已人工审查的48项与阐释正文确定性转排；Session-C独占分片不声称由本事务原子写入。历史A/core/proof/run/sources不改。

## element_usage
|元件|实际用途/边界|
|---|---|
|closure/Goal7/common/最高指示|范围与角色、实际生成和恢复；不以hash自证理解|
|四件套|首次全文、同档复认；用户原文与AI阐释分开|
|Schema/原典|父范围入口、W实际规则；不以目录算实审|
|F-011/两个verifier|旧精确数学证据复用；不作新kernel或全局PASS|
|checkpoint/projection helper|唯一当前状态事务及全逻辑分片；不改旧收据|
|SOP反思|停止重复W种子，返回父范围；no-plan-change|
|Sub Agent/发布/全局配置|未使用，当前用户明确禁止|

T01–05执行既定目标/授权；T06–12无演算/架构/配置变更；T13–17新增精确证据核验及保留失败；T18–21无外发/部署；T22–24只接续C current与历史分层；T25不改AI治理合同；T26精确本地提交，不push/tag。reflection=no-plan-change。
'''
    auditroot=ROOT/C/'审计/R0/CORE_COGNITION_AUDIT'
    kc=(auditroot/'001 - 核心认知逐项回评.md').read_text()
    blocks=re.split(r'^### (KC-\d{6})\n',kc,flags=re.M)
    legacy=f'# {SID} 完整兼容审计\n\ncore-cognition-generation-8；48 KC；本单文件只因writer第一层兼容限制而生成。人审分片见{C}审计/R0/CORE_COGNITION_AUDIT.md；不认证嵌套分片已原子提交。\n\n'
    legacy+='core_change: NO\ndirection_change: YES\npanorama_change: YES\nessay_change: NO\nupdate_decision: register C and current queue only; no parent completion\ncross_conflicts: old A administrative closure is not Goal7 parent closure; old Coq mismatch retained\nunresolved: parent source/semantic/relations sufficiency and C final delivery; writer nested-shard gap\n\n|KC ID|姿态|relation|assessment and evidence|next and falsifier|\n|---|---|---|---|---|\n'
    for i in range(1,len(blocks),2):
        kid,body=blocks[i:i+2]
        fields={}
        for line in body.splitlines():
            if line.startswith('- ') and ': ' in line:
                k,v=line[2:].split(': ',1);fields[k]=v
        legacy+=f"| `{kid}` | {fields['工作姿态']} | {fields['relation']} | {fields['实际证据与关系理由']} | {fields['下一选择及反证条件']} |\n"
    assert len(cr._audit_v1_kc_rows(legacy))==48
    essay=(auditroot/'002 - 阐释消费与航向反思.md').read_text()
    legacy+='\n'+essay[essay.index('# 阐释消费与航向反思'):]
    legacy+='\n## 注册前证据增量\n旧账本318行及四包全部本地数学源码已读；七命令结果在旧证明包检查-001.json，四包精确复用不改变KC证据/现实边界；无新kernel。C02警告名纠正与原件保留体现KC21/48的证据纪律。下一队列按Goal7回父范围，旧A整体完成不被继承。\n'
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'kernel_runs':[],
          'evidence':[C+'证据/R0/旧证明包检查-001.json',C+'证据/R0/旧证明与封存比较.json',C+'证据/R0/旧A封存字节核验.json',C+'证据/R0/shards-check-003.json'],
          'status':'EXISTING_EVIDENCE_CHECKED_WITH_SCOPE','global_registry':'BLOCKED_OLD_COQ_COMMAND_SOURCE_MISMATCH',
          'model_understanding':'NOT_CERTIFIED_BY_TOOL','parent_coverage':'PARENT_SCOPE_INCOMPLETE'}
    rows=[]
    for doc in docs.values():rows+=pe.payload_rows(doc,ROOT)
    for p,t in texts.items():rows.append({'path':p,'expected_sha256':sha((ROOT/p).read_bytes()),'text':t})
    for name,t in [('SESSION.md',session),('CORE_COGNITION_AUDIT.md',legacy),('RUNS.json',cr.dump(runs).decode())]:
        rows.append({'path':sb+name,'expected_sha256':None,'text':t})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[],
        'authorization':'User Goal7 launch authorizes sole Session C integrator to register own record and necessary current owners through canonical checkpoint, retaining A/D/sources read-only and preserving unrelated dirty/index.',
        'files':rows}
    with OUT.open('xb') as f:f.write(cr.dump(payload))
    print(json.dumps({'snapshot':plan['snapshot'],'session_id':SID,'proposed_revision':rev,'payload':str(OUT.relative_to(ROOT)),'row_count':len(rows),'state_applied':False},ensure_ascii=False))

if __name__=='__main__':
    main()
