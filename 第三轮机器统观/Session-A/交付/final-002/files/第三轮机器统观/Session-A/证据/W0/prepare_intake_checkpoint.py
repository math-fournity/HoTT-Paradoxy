#!/usr/bin/env python3
"""Prepare the one MO3 intake transaction; canonical runtime alone applies state."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
SID = 'S-RES-20260923-MO3-A-W0'
TASK = 'MO3-GOVERNED-A'
BASE = f'.codex/research/hott/sessions/{SID}/'
OWN = '第三轮机器统观/Session-A/'
REPORT = OWN + '执行记录/002 - W0原典对齐与开工重新呈现.md'
AUDIT = OWN + '审计/W0/CORE_COGNITION_AUDIT.md'

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--apply', action='store_true'); args = ap.parse_args()
    spec = importlib.util.spec_from_file_location('cognition_runtime', ROOT / '.codex/tools/cognition_runtime.py')
    rt = importlib.util.module_from_spec(spec); spec.loader.exec_module(rt)
    sys.path.insert(0, str(ROOT / 'scripts/audit')); import projection_edit as edit
    state = json.loads((ROOT / rt.STATE).read_text())
    assert state['revision'] == 268 and TASK not in state['records'] and SID not in state['records']
    head = json.loads((ROOT / rt.HEAD).read_text())
    assert all(sha(p) == h for p, h in head['tracked'].items()), 'Tracked writer state changed'
    assert state['current_core']['kc_count'] == 48
    plan = rt.plan(ROOT, profile='research'); assert not plan['review_required']
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (HERE / 'intake-plan.json').write_bytes(rt.dump(plan))
    rev = state['revision'] + 1
    next_action = 'W1: establish sourced questions for eight domains and five independent scales; compare formation/Acc/staged composition with Book11.5 cover-to-index delivery, preserve original-circle remainder, and choose a non-existence/delivery holdout. Then execute W2 native thin chain and method controls; no repeated Delay/Godel substitute.'
    message = f'MO3-GOVERNED-A已由用户启动；W0完整加载、原典对齐、十四题/三次呈现、逐KC审计及工具正负控制完成。候选种子未证明，W1–W5未完成，ROUND_INCOMPLETE。下一步为八域五尺度问题/关系首遍，并列形成资格/Acc阶段合成与Book11.5有限交付，另保非存在中心留出；旧P47排名须复审。入口goal-6.md、goal-5.md、第三轮机器统观/Session-A/执行记录.md；revision{rev}。'
    pins = ['goal-6.md', 'goal-5.md', '最高指示.md', REPORT, OWN + '证据/W0/native-qualification-001/RESULT.json']
    state['records'][TASK] = dict(kind='research_task', path=OWN+'执行记录.md', lifecycle_status='ACTIVE_WORK', status='W0_COMPLETE_W1_NEXT', evidence_status='INTAKE_AND_TOOL_QUALIFICATION_WITH_SCOPE / CANDIDATES_UNPROVED / ROUND_INCOMPLETE', depends_on=[], full_sources=['goal-6.md', 'goal-5.md', REPORT, AUDIT], source_hashes={p: sha(p) for p in pins}, related_records=['R-P47-THEORY-SYNTHESIS-20260923'], scope='Goal6/Goal5 full MO3 eight-domain five-scale discovery, actual processes, native verification, reality bridges, four method controls, omissions, claim audits, canonical writeback and final seal for independent B. W0 alone complete; no mathematical result or final handoff.')
    state['records'][SID] = dict(kind='session', path=BASE+'SESSION.md', lifecycle_status='HISTORICAL', status='complete_with_scope', evidence_status='MO3_W0_INTAKE_ONLY', depends_on=[], full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']], related_records=[TASK])
    state['active'] = list(dict.fromkeys(state['active']+[TASK]))
    state['revision'] = rev; state['latest_session'] = SID
    state['execution_control'].update(status='MO3_ACTIVE_ROUND_INCOMPLETE', current_phase='MO3_W1_BREADTH_FIRST_PASS', active_goal_record=TASK, active_goal_path='goal-6.md', domain_sop='goal-5.md', current_role='RESEARCH_GENERATION', app_goal_completion_eligible=False, app_goal_status_observed='active', next_minimal_verification=next_action, last_checkpoint_session=SID, checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json', second_phase_status='MO3_ACTIVE / OLD_006_FIRST_PASS_HISTORICAL', historical_first_pass_status='FIRST_PASS_COMPLETE_WITH_DECLARED_SCOPE; P47 priority REVIEW_REQUIRED by subsequent alignment audit')
    state['projection']['status'] = 'MO3_W0_COMPLETE_W1_NEXT / ROUND_INCOMPLETE / NO_NEW_MATH'
    docs = {p: edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    memory = docs['MEMORY.md']; mp = 'MEMORY/001 - 当前执行队列.md'
    old = memory['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0]
    edit.replace_in_shard(memory,mp,old,message)
    edit.append_to_shard(memory,'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：用户新Goal6正式注册为唯一当前MO3研究；W0完成、W1下一；无新数学claim。旧Goal/ABX不复活。分片审计由{AUDIT}持有，事务内完整单文件兼容，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001未修。revision{rev}。\n')
    for path,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[path],'source_state_revision: 268',f'source_state_revision: {rev}')
        edit.replace_in_index(docs[path],f'projection_generation: 20260923-{kind}-268',f'projection_generation: 20260923-{kind}-{rev}')
        docs[path]['index_text'] = docs[path]['index_text'].replace('THEORY_FIRST_PASS_P47_COMPLETE_WITH_SCOPE','MO3_W0_COMPLETE_W1_NEXT_ROUND_INCOMPLETE')
        state['records'][rid].update(projection_generation=f'20260923-{kind}-{rev}',semantic_status='MO3_W0_COMPLETE_W1_NEXT_ROUND_INCOMPLETE',scope='User-started MO3 W0 intake complete; W1-W5 open; old P47 scope retained, not current completion eligibility.')
    edit.append_to_shard(docs['方向追踪.md'],'方向追踪/002 - 治理与用户方向.md',f'\n| `DIR-U-MO3-GOVERNED` | 第三轮八域五尺度与针对性过程 | 用户Goal6、KC2/11/16/44–48 | `ACTIVE / W1_NEXT / ROUND_INCOMPLETE` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-W0-INTAKE` | 形成资格与覆盖交付同台；完成五尺度首遍后实施薄链与留出 | {REPORT}；goal-6.md；revision{rev} |\n')
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-W0-INTAKE` | 第三轮开工对齐与工具资格 | `DIR-U-MO3-GOVERNED` | 全文输入、原典、重新呈现、工具正负控制 | `INTAKE_COMPLETE / CANDIDATES_UNPROVED` | C01阶段合成与Acc、C02覆盖交付为待核种子 | 无新数学claim、现实桥或final seal；W1–W5未完 | {REPORT}；{AUDIT}；revision{rev} |\n')
    pending='全景视野/008 - 当前未完成.md'
    docs['全景视野.md']['shards'][pending] = re.sub(r'^17\. 统观前提—模型保真连接：.*$', '17. MO3-GOVERNED-A已启动：W0完成，W1–W5未完。前提→原生对象/规则→过程→观察/Done的保真连接仍须实际核证；旧Delay/DM3/I探针不替代本轮。形成资格与Book11.5同台比较，非存在中心留出、四方法控制及最终B封存均未完成。', docs['全景视野.md']['shards'][pending], flags=re.M)
    rows=[]
    for doc in docs.values(): rows += edit.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for path in rt.MUTABLE:
        if path in seen: continue
        text=(ROOT/path).read_text()
        if path==rt.STATE: text=rt.dump(state).decode()
        elif path.endswith('FRONTIER.md'): text=re.sub(r'^- 第006片理论首轮.*$','- '+message,text,flags=re.M)
        elif path.endswith('RESUME.md'):
            text=re.sub(r'^第006片理论首轮.*$',message,text,flags=re.M)
            text=text.replace('当前为 generation-7/46 KC，索引/manifest/旧 receipt 不能替代。','当前身份从STATE.current_core读取；首次全文与压缩复认按PROTOCOL及Goal6，最高指示另须全文重读。')
            text=text.replace('3. 当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001`，全文读 `理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；需战略背景再读 C3/A11/self-reference/RP-B01。','3. 当前用户Goal6为MO3-GOVERNED-A：先query该稳定record，再research task plan；按Goal6恢复执行Skill、最高指示及本轮执行记录。旧C4/Goal/1/3仅在任务真实依赖时读取，不自动复活。')
        rows.append(dict(path=path,expected_sha256=sha(path),text=text))
    audit_doc=edit.load(ROOT,AUDIT)
    # Human-authored arguments remain canonical; this is a complete legacy-format projection for the existing writer.
    legacy=['# '+SID+' 核心认知审计兼容投影','', '- identity: '+state['current_core']['generation']+' / 48 KC']
    legacy += [line for line in audit_doc['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',line)]
    legacy += ['', '语义原件：'+AUDIT+'；嵌套分片不在此事务原子边界内。完整论证如下：','']
    for text in audit_doc['shards'].values(): legacy.append(text)
    legacy_text='\n'.join(legacy)+'\n'
    assert rt._audit_v1_kc_rows(legacy_text)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: Astra（用户选择；不认证后端指纹/effort）\n- tier: T3 research/state intake\n- load_receipt: {OWN}证据/W0/loading-progress-003.json；STATE1–18474已读，当前delta见本事务；最高指示第五稿本单元481行至EOF。\n- role: RESEARCH_GENERATION / sole canonical integrator\n- authorization: 用户Goal6启动词授权本轮research/checkpoint及自身精确本地提交；无Sub Agent、新Session、push/tag/发布或core修改。\n- status: W0_COMPLETE_W1_NEXT / ROUND_INCOMPLETE\n- report: {REPORT}\n- semantic_audit: {AUDIT}\n- next: {next_action}\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；完整单文件审计事务内、分片语义原件事务外。\n\n|element_usage|实际用途/边界|\n|---|---|\n|core/最高指示|原问、十四题/三呈现与候选生成|\n|Goal5/6|八域五尺度、角色、验收与恢复|\n|STATE/投影|唯一当前任务与历史分离|\n|原典/旧报告|形成/Acc/cover核对与查重，不作本轮proof|\n|原生kernel|仅工具资格控制，不是候选证明|\n|审计/事务|48KC与扩展逐节；兼容缺口明示|\n\nreflection=no-plan-change。T01/03/04/13/22/24/26新增开工、来源、工具控制、状态与版本证据；T02/05–12/14–21/23/25无需求、软件、配置、数据schema、部署或AI治理合同修改。\n'
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],tool_qualification=OWN+'证据/W0/native-qualification-001/RESULT.json',load_receipt=OWN+'证据/W0/loading-progress-003.json',report=REPORT,semantic_audit=AUDIT,scope='W0 intake and fixed tool controls; candidate process execution remains pending.')
    rows += [dict(path=BASE+name,expected_sha256=None,text=text) for name,text in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',legacy_text)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[],authorization='用户MO3-GOVERNED-A Goal6启动词：唯一研究integrator，可经canonical checkpoint更新本轮状态并精确本地提交；旧成果/原文保留，不push/tag。',files=rows)
    (HERE/'intake-payload.json').write_bytes(rt.dump(payload))
    result=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (HERE/('intake-apply.json' if args.apply else 'intake-dry-run.json')).write_bytes(rt.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__': main()
