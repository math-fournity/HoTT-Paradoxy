#!/usr/bin/env python3
"""Serialize W1's authored state delta; only the canonical runtime applies it."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
SID = 'S-RES-20260923-MO3-A-W1'
TASK = 'MO3-GOVERNED-A'
OWN = '第三轮机器统观/Session-A/'
BASE = '.codex/research/hott/sessions/' + SID + '/'
REPORT = OWN + '覆盖与关系/003 - 首遍语义裁决与实际验证选择.md'
AUDIT = OWN + '审计/W1/CORE_COGNITION_AUDIT.md'

def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location('rt', ROOT / '.codex/tools/cognition_runtime.py')
    rt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rt)
    sys.path.insert(0, str(ROOT / 'scripts/audit'))
    import projection_edit as edit
    s = json.loads((ROOT / rt.STATE).read_text())
    assert s['revision'] == 269 and s['latest_session'] == 'S-RES-20260923-MO3-A-W0'
    assert SID not in s['records'] and s['current_core']['kc_count'] == 48
    head = json.loads((ROOT / rt.HEAD).read_text())
    assert all(sha(p) == h for p, h in head['tracked'].items()), 'canonical owner drift'
    plan = rt.plan(ROOT, profile='research', task_ids=[TASK])
    assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted']
    (HERE / 'checkpoint-plan.json').write_bytes(rt.dump(plan))
    rev = s['revision'] + 1
    next_action = 'W2: implement C01 with native SeqColim and stage-induced edges, finite-stage Acc and the exact aggregate consumer, plus same-task frozen-stage/qualification controls. Execute four method controls; then C04 double-loop order holdout and W3 C02 enumerable cover delivery. Preserve original-circle metric/process remainder and R09 extension-substitution review; W2-W5 mandatory and no final seal yet.'
    message = f'MO3-GOVERNED-A的W1语义首遍完成：八域32个S1–S4问题、3个整体问题有范围回答；七扩展原典接口已回核，关系新增R09。来源报告与候选规格，不是数学证明。下一步W2原生C01直接合成/Acc及控制；C02覆盖列表、C04异机制留出、原圆环余项与R09组合审查仍必做。ROUND_INCOMPLETE，revision{rev}；入口goal-6.md及第三轮机器统观/Session-A/执行记录.md。'
    rec = s['records'][TASK]
    rec.update(status='W1_SOURCE_PASS_COMPLETE_W2_NEXT', evidence_status='SOURCED_SEMANTIC_FIRST_PASS / PROCESS_SPECS_UNPROVED / ROUND_INCOMPLETE', full_sources=['goal-6.md','goal-5.md',REPORT,AUDIT], scope='MO3 W0 and W1 complete with scope: eight-domain five-scale sourced first pass, relation omission and candidate selection. W2-W5 actual processes, controls, native proofs, reality bridges and final B seal remain mandatory.')
    rec['source_hashes'].update({p:sha(p) for p in [REPORT,AUDIT,OWN+'证据/W1/extension-source-read.json']})
    rec['revalidation'] = 'W1 reread current Goal6/Goal5/role/Highest Directive and primary rule scopes; original W0 pins unchanged. Add exact W1 sourced first-pass report, semantic audit and source-reading receipt. This extends evidence routing only; no candidate is promoted to mathematical proof or round completion.'
    s['records'][SID] = dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='MO3_W1_SOURCE_PASS_NOT_MATH_PROOF',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[TASK])
    s['revision'] = rev
    s['latest_session'] = SID
    s['execution_control'].update(current_phase='MO3_W2_NATIVE_THIN_CHAIN',next_minimal_verification=next_action,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False)
    s['projection']['status'] = 'MO3_W1_COMPLETE_W2_NEXT / ROUND_INCOMPLETE / NO_NEW_MATH'
    docs = {p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    memory = docs['MEMORY.md']
    mp = 'MEMORY/001 - 当前执行队列.md'
    old = memory['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0]
    edit.replace_in_shard(memory,mp,old,message)
    edit.append_to_shard(memory,'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：MO3 W1八域五尺度source pass与九条关系实例完成，C01优先且C02/C04及原圆环余项未删。无数学claim/run/final seal。审计{AUDIT}，事务内完整单文件兼容，分片writer缺口仍在。revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 269',f'source_state_revision: {rev}')
        edit.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-269',f'projection_generation: 20260923-{kind}-{rev}')
        docs[p]['index_text'] = docs[p]['index_text'].replace('MO3_W0_COMPLETE_W1_NEXT_ROUND_INCOMPLETE','MO3_W1_COMPLETE_W2_NEXT_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260923-{kind}-{rev}',semantic_status='MO3_W1_COMPLETE_W2_NEXT_ROUND_INCOMPLETE',scope='MO3 W1 sourced semantic first pass complete; W2-W5 open; no new mathematical claim or round completion.')
    dp='方向追踪/002 - 治理与用户方向.md'
    docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮八域五尺度与针对性过程 | 用户Goal6、KC2/11/16/44–48 | `ACTIVE / W2_NEXT / ROUND_INCOMPLETE` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-W0-INTAKE`, `OUT-MO3-W1-SOURCE-PASS` | 原生C01直接合成/Acc先行；C02/C04/原圆环余项/R09与四控制保留 | {REPORT}；goal-6.md；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-W1-SOURCE-PASS` | 八域五尺度首遍与关系补漏 | `DIR-U-MO3-GOVERNED` | 固定Book/七扩展接口、32+3问题、九条关系实例 | `SOURCE_REPORTED / PROCESS_SPECS_UNPROVED` | C01原生直接合成/Acc为下一实际链，C04异机制留出 | 不是全理论完备、数学证明或现实桥；W2–W5未完 | {REPORT}；{AUDIT}；revision{rev} |\n')
    pending='全景视野/008 - 当前未完成.md'
    docs['全景视野.md']['shards'][pending]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：W0/W1有范围完成，W2–W5未完。下一步原生C01直接合成/Acc及控制，C02覆盖列表、C04异机制留出、原圆环运动/逼近余项、R09扩展推导组合、四方法控制与B封存仍必做。来源判词不冒数学证明或全理论无悖论。',docs['全景视野.md']['shards'][pending],flags=re.M)
    rows=[]
    for d in docs.values(): rows += edit.payload_rows(d,ROOT)
    seen={r['path'] for r in rows}
    for p in rt.MUTABLE:
        if p in seen: continue
        content=(ROOT/p).read_text()
        if p==rt.STATE: content=rt.dump(s).decode()
        elif p.endswith('FRONTIER.md'): content=re.sub(r'^- MO3-GOVERNED-A.*$','- '+message,content,flags=re.M)
        elif p.endswith('RESUME.md'): content=re.sub(r'^MO3-GOVERNED-A.*$',message,content,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=content))
    aud=edit.load(ROOT,AUDIT)
    legacy=['# '+SID+' 核心认知审计兼容投影','', '- identity: '+s['current_core']['generation']+' / 48 KC']
    legacy += [line for line in aud['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',line)]
    legacy += ['', '语义原件：'+AUDIT+'；嵌套分片仍不在canonical事务内。','']
    # The legacy writer expects relation in column three and spaces after '|'.
    # Reorder the already-authored cells; no semantic assessment is generated.
    for body in aud['shards'].values():
        converted=[]
        for line in body.splitlines():
            if line.startswith('|`KC-') or line.startswith('|KC|relation|'):
                cells=[c.strip() for c in line.strip('|').split('|')]
                cells[1],cells[2]=cells[2],cells[1]
                line='| '+' | '.join(cells)+' |'
            converted.append(line)
        legacy.append('\n'.join(converted))
    legacy_text='\n'.join(legacy)+'\n'
    assert rt._audit_v1_kc_rows(legacy_text)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'''# {SID}

- host: codex-desktop
- model: Astra（用户选择，不认证后端指纹/effort）
- tier: T3 research/state
- role: RESEARCH_GENERATION / sole canonical integrator
- load_receipt: {OWN}证据/W0/loading-progress-003.json；STATE268全文+自身269已读事务差分；37个269后像无漂移；本轮恢复及最高指示481 EOF/48KC复认见执行记录003。
- source_receipt: {OWN}证据/W1/extension-source-read.json
- status: W1_SOURCE_PASS_COMPLETE_W2_NEXT / ROUND_INCOMPLETE
- report: {REPORT}
- semantic_audit: {AUDIT}
- next: {next_action}
- authorization: 用户Goal6已授本轮精确checkpoint/本地commit；无Sub Agent、新Session、push/tag/发布或core改动。
- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；完整单文件在事务内，独占分片事务外。

|element_usage|用途/边界|
|---|---|
|core/最高指示|源先行、14题/三呈现、原问余项与过程选择|
|Goal5/6|五尺度、全轮义务和角色恢复|
|原典/源码|有范围语义审查与查重，非当前机器证明|
|STATE/投影|唯一队列，旧Goal不复活|
|KC/扩展审计|逐条理由及下一选择，非理解自动认证|
|原生工具|沿用W0资格；本单元无candidate run|

reflection=no-plan-change。T01/03/04/13/22/24/26变更为来源判断/研究选择/证据/当前态；T02/05–12/14–21/23/25无需求、软件产品、配置、schema、部署、AI治理合同变化。R09是研究分类补漏，不是SOP验收降低。
'''
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],source_receipt=OWN+'证据/W1/extension-source-read.json',report=REPORT,semantic_audit=AUDIT,scope='W1 sourced semantic first pass and process selection; no mathematical verification or final handoff.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',legacy_text)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户MO3-GOVERNED-A Goal6授权唯一integrator执行本轮canonical写回与精确本地commit；不push/tag、不改core或他人修改。',files=rows)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload))
    result=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__': main()
