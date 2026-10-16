#!/usr/bin/env python3
"""One-shot R09 source-scope write-back through the canonical runtime."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OWN = '第三轮机器统观/Session-A/'
TASK = 'MO3-GOVERNED-A'
RID = 'R-MO3-R09-SUBSTITUTION-20260924'
SID = 'S-RES-20260924-MO3-A-R09'
BASE = f'.codex/research/hott/sessions/{SID}/'
REPORT = OWN + '执行记录/011 - 替换接口的来源与实例核对.md'
PROCESS = OWN + '过程与结果/005 - 推导复用与替换侧条件.md'
AUDIT = OWN + '审计/W3-R09/CORE_COGNITION_AUDIT.md'


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('rt', ROOT / '.codex/tools/cognition_runtime.py')
    rt = importlib.util.module_from_spec(spec); spec.loader.exec_module(rt)
    sys.path.insert(0, str(ROOT / 'scripts/audit'))
    import projection_edit as edit
    s = json.loads((ROOT / rt.STATE).read_text())
    assert s['revision'] == 277 and SID not in s['records'] and RID not in s['records']
    h = json.loads((ROOT / rt.HEAD).read_text())
    assert all(sha(p) == value for p, value in h['tracked'].items())
    methods = json.loads((HERE.parent / 'MS01/method-inputs/MANIFEST.json').read_text())
    assert all(sha(x['source']) == x['sha256'] for x in methods['rows'])
    source = json.loads((HERE / 'source/SOURCE-MANIFEST.json').read_text())
    assert all(sha(x['path']) == x['sha256'] for x in source['sources'])
    run = json.loads((HERE / 'software-run-001/RUN.json').read_text())
    observations = json.loads((HERE / 'software-run-001/result.json').read_text())
    assert run['exit_code'] == 0 and observations['all_expected'] and observations['case_count'] == 8
    assert observations == json.loads((HERE / 'rule-instances-001.json').read_text())
    assert sha(OWN + '证据/W3-R09/inspect_rule_instances.py') == run['source_sha256']
    rt.query_record(ROOT, TASK)
    plan = rt.plan(ROOT, profile='research', task_ids=[TASK])
    assert set(plan['review_required']) <= {TASK}
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (HERE / 'checkpoint-plan.json').write_bytes(rt.dump(plan))
    evidence = [PROCESS, REPORT, OWN + '证据/W3-R09/' + 'GENERATION.md',
                OWN + '证据/W3-R09/RULE-REVIEW.md', OWN + '证据/W3-R09/inspect_rule_instances.py',
                OWN + '证据/W3-R09/software-run-001/RUN.json',
                OWN + '证据/W3-R09/software-run-001/result.json',
                OWN + '证据/W3-R09/source/SOURCE-MANIFEST.json'] + [x['path'] for x in source['sources']]
    s['records'][RID] = dict(kind='result', path=PROCESS, lifecycle_status='CLOSED',
        status='SOURCE_SCOPE_REVIEW_COMPLETE', evidence_status='SEMANTICALLY_REVIEWED_WITH_SOURCE_SCOPE / EIGHT_GROUND_OBSERVATIONS / NATIVE_METATHEORY_NOT_REPLAYED',
        depends_on=[], related_records=[TASK], full_sources=evidence,
        source_hashes={p: sha(p) for p in evidence},
        scope='Two distinct calculi, directed background/extension side conditions and QTT usage/phase rules. Three manual directed instances and eight ground QTT reading-aid observations. Source formula precision remains open; no new native theorem, physical bridge, novelty or global consistency claim.')
    task = s['records'][TASK]
    task['depends_on'].append(RID)
    task['dependency_semantics'] = 'verification_staleness'
    task.update(status='R09_SOURCE_SCOPE_COMPLETE_MS05_NEXT',
        evidence_status='C327_TO_C341_SCOPED_NATIVE_RESULTS / R09_SOURCE_REVIEW / NONLEAF_BIAS_SEAL_REMAINDER / ROUND_INCOMPLETE',
        full_sources=['goal-6.md', 'goal-5.md', REPORT, AUDIT],
        scope='Full Goal5 v1.2/Goal6 remains: C01/C04/C02/R13 scoped native packages, MS04 controls and R09 source/instances completed within stated scopes; all remaining non-leaf adjudications, bias regression, omission and final seal remain.',
        revalidation='Current Goal/source route fully re-read; highest503 and core441 re-read. Recovery reattests unchanged core8 and four-set through own canonical277. R09 source text, interpretation, software and native evidence separated. Only known owned report/coverage pins refreshed.')
    for p in [REPORT, AUDIT, OWN + '覆盖与关系/004 - 语义单元与联合条件.md']:
        task['source_hashes'][p] = sha(p)
    rev = s['revision'] + 1
    s['revision'], s['latest_session'] = rev, SID
    message = f'MO3 R09已完成两个演算的source范围替换审查：directed三项背景实例、QTT八项ground用量观察及原件精度余项分列；不新增数学claim或元理论认证。C327–341原有范围保留。下一全部MS02/MS05非叶、R05反馈裁决，再偏差回归及MS06。ROUND_INCOMPLETE；revision{rev}。'
    nxt = 'Complete every accepted MS02/MS05 non-leaf question and relation with its own answer/evidence/scope/remainder/parent impact; explicitly adjudicate R05 feedback rather than substituting static C01. Keep R09 source-formula precision and un-replayed metatheory, C02 producer and R13 margin boundaries. Then perform dedicated bias regression, independent omission and full Goal5/6 completion audit before MS06 seal.'
    s['execution_control'].update(current_phase='MO3_W3_MS05_NONLEAF', status='MO3_ACTIVE_ROUND_INCOMPLETE',
        next_minimal_verification=nxt, last_checkpoint_session=SID,
        checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',
        app_goal_completion_eligible=False, app_goal_status_observed='active')
    s['projection']['status'] = 'MO3_R09_SOURCE_SCOPE / MS05_NEXT / ROUND_INCOMPLETE'
    s['records'][SID] = dict(kind='session', path=BASE + 'SESSION.md', lifecycle_status='HISTORICAL',
        status='complete_with_scope', evidence_status='R09_SOURCE_AND_RULE_INSTANCE_REVIEW', depends_on=[],
        related_records=[TASK, RID], full_sources=[BASE + n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs = {p: edit.load(ROOT, p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp = 'MEMORY/001 - 当前执行队列.md'
    old = docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n', 1)[1].split('\n\n## 既有项目队列', 1)[0]
    edit.replace_in_shard(docs['MEMORY.md'], mp, old, message)
    edit.append_to_shard(docs['MEMORY.md'], 'MEMORY/003 - 当前验证状态与顺序日志.md',
        f'\n{SID}：R09两配置source/侧条件与八项ground控制完成所述范围；无新数学claim，完整元理论及原件精度余项保留。全部非叶/偏差/封存继续；revision{rev}。\n')
    for p, kind, rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'), ('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p], 'source_state_revision: 277', f'source_state_revision: {rev}')
        edit.replace_in_index(docs[p], f'projection_generation: 20260924-{kind}-277', f'projection_generation: 20260924-{kind}-{rev}')
        docs[p]['index_text'] = docs[p]['index_text'].replace('MO3_R13_MARGIN_BOUNDARY_ROUND_INCOMPLETE','MO3_R09_SOURCE_SCOPE_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260924-{kind}-{rev}', semantic_status='MO3_R09_SOURCE_SCOPE_ROUND_INCOMPLETE', scope='R09 source/instances; all non-leaf, bias and seal still incomplete.')
    dp = '方向追踪/002 - 治理与用户方向.md'
    docs['方向追踪.md']['shards'][dp] = re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',
        f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `ACTIVE / MS05_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT`, `OUT-MO3-MS04-CONTROLS`, `OUT-MO3-C04-BOUQUET-ORDER`, `OUT-MO3-C02-FINITE-COVER`, `OUT-MO3-R13-MARGIN`, `OUT-MO3-R09-SUBSTITUTION` | 全部非叶/R05，偏差回归与封存 | {REPORT}；revision{rev} |', docs['方向追踪.md']['shards'][dp], flags=re.M)
    edit.append_to_shard(docs['全景视野.md'], '全景视野/002 - 治理、门禁与骨架结果.md',
        f'\n| `OUT-MO3-R09-SUBSTITUTION` | 推导复用与替换侧条件 | `DIR-U-MO3-GOVERNED` | 两个固定原典、规则实例、8个软件观察 | `SOURCE_SCOPE_REVIEWED / NOT_NATIVE_METATHEORY` | 背景/用量/阶段及原始规则责任具体化 | 无新数学或现实失配；原件精度/完整元理论未认证 | {PROCESS}；{REPORT}；revision{rev} |\n')
    pp = '全景视野/008 - 当前未完成.md'
    docs['全景视野.md']['shards'][pp] = re.sub(r'^17\. MO3-GOVERNED-A.*$',
        '17. MO3-GOVERNED-A：既有native接口及R13余量、MS04控制和R09 source范围已各自完成；全部MS02/MS05非叶与R05反馈裁决、专门偏差回归及MS06仍欠。Book producer、R09原件精度与完整元理论边界保留，不用局部结果抵全轮。', docs['全景视野.md']['shards'][pp], flags=re.M)
    rows = [row for doc in docs.values() for row in edit.payload_rows(doc, ROOT)]
    seen = {x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen: continue
        text = (ROOT / p).read_text()
        if p == rt.STATE: text = rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):
            assert old in text
            text = text.replace(old, message, 1)
        rows.append(dict(path=p, expected_sha256=sha(p), text=text))
    audit_doc = edit.load(ROOT, AUDIT)
    audit = '\n\n'.join(['# '+SID+' 兼容完整审计', '- identity: '+s['current_core']['generation']+' / 48 KC'] +
        [x for x in audit_doc['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):', x)] +
        ['分片语义原件：'+AUDIT+'；嵌套writer缺口保留。'] + list(audit_doc['shards'].values())).rstrip()+'\n'
    assert rt._audit_v1_kc_rows(audit) == [f'KC-{i:06d}' for i in range(1,49)]
    session = f'''# {SID}

- host: codex-desktop
- model: Astra（用户指定；不作后端指纹认证）
- tier: T3
- role: RESEARCH_GENERATION / sole canonical integrator
- thread: 01a0d1bd-c44d-7261-9a37-45bc5fbe87a8
- load_receipt: {OWN}证据/W3-R09/GENERATION.md；最高指示503/core441本轮全文；四件套26路径沿W0全文及本轮自身checkpoint复认；STATE原268全文+自身269–277差分，277受管后像无漂移。非本轮全STATE重新全文认证。
- status: R09_SOURCE_SCOPE_COMPLETE / ROUND_INCOMPLETE
- report: {REPORT}
- semantic_audit: {AUDIT}
- next: {nxt}
- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；旧全registry错配不由本次修复。

|element_usage|实际作用与边界|
|---|---|
|原文/最高指示|先由复用收益生成条件敏感过程|
|原典PDF/视觉核对|完整所选规则与印字/解释分开|
|软件有限实例|8个预给ground观察，不冒充完整QTT核|
|canonical/48KC|当前状态与分片语义审计边界分列|

reflection=no-plan-change。T01/04/13/22/24/26为本轮研究实物与当前态更新；方法、配置、schema、核心原文及其余无变化组保持。无新数学claim、Sub Agent、新Session、push/tag或历史原件改写。
'''
    runs = dict(schema_version='hott-session-runs/v1', session_id=SID, new_math_claims=[],
        software_run=OWN+'证据/W3-R09/software-run-001/RUN.json',
        scope='Eight given ground rule instances only; paper/source scope distinct from native metatheory.',
        source_manifest=OWN+'证据/W3-R09/source/SOURCE-MANIFEST.json')
    rows += [dict(path=BASE+n, expected_sha256=None, text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload = dict(schema_version='cognition-checkpoint/v1', session_id=SID, load_profile='research', task_ids=[TASK],
        authorization='用户当前MO3 Goal5/Goal6唯一integrator与精确本地写回授权；继续同轮研究并保存R09来源范围。', files=rows)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload))
    result = rt.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    (HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))


if __name__ == '__main__': main()
