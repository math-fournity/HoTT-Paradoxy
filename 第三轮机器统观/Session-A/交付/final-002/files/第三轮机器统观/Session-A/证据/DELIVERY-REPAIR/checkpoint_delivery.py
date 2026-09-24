#!/usr/bin/env python3
"""Record the observed delivery-interface correction; preserve all research proofs."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
SID='S-RES-20260924-MO3-A-DELIVERY-REPAIR';PREV='S-RES-20260924-MO3-A-FINAL-WORDING';TASK='MO3-GOVERNED-A';BASE=f'.codex/research/hott/sessions/{SID}/';OWN='第三轮机器统观/Session-A/'
CHANGED=[OWN+p for p in ['执行记录.md','交付说明.md','最终报告.md','结论账本.md']];REPAIR=OWN+'证据/DELIVERY-REPAIR/REPAIR.md'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt);sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());h=json.loads((ROOT/rt.HEAD).read_text());assert s['revision']==282 and SID not in s['records'];assert all(sha(p)==v for p,v in h['tracked'].items())
    rt.query_record(ROOT,TASK);plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert not plan['hydration_diagnostics']['query_first_promoted']
    evidence=json.loads((ROOT/OWN/'交付/final-001-verification/diagnostic-003/RESULT.json').read_text());assert len(evidence['checks'])==4 and all(x['exit']==0 for x in evidence['checks'])
    for id,r in s['records'].items():
        for p,v in list(r.get('source_hashes',{}).items()):
            if p in CHANGED and v!=sha(p):
                assert id==TASK or id.startswith('R-MO3-');r['source_hashes'][p]=sha(p);r['revalidation']='Observed copied-checker CLI failure corrected; raw run-dir is relative, Git closure verifier remains tied to original historical repo. Four copied raw evidence checks passed; no native proof/source/run or research acceptance change. New immutable final-002 follows.'
    task=s['records'][TASK];task['full_sources'].append(REPAIR);task['source_hashes'][REPAIR]=sha(REPAIR);task['delivery_seal_path']=OWN+'交付/final-002';task['scope']=task['scope'].replace('final-001','final-002')
    s['revision']=283;s['latest_session']=SID;s['execution_control'].update(last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',delivery_seal_path=OWN+'交付/final-002')
    s['execution_control']['next_minimal_verification']=s['execution_control']['next_minimal_verification'].replace('final-001','final-002')
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='DELIVERY_CLI_CORRECTION_WITH_COPIED_RAW_EVIDENCE_CHECKS',depends_on=[],related_records=[TASK],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';docs['MEMORY.md']['shards'][mp]=docs['MEMORY.md']['shards'][mp].replace('第三轮机器统观/Session-A/交付/final-001/SEAL.json','第三轮机器统观/Session-A/交付/final-002/SEAL.json').replace('revision282，B未审。','revision283，B未审；final-001及副本命令失败保留，新代次修正说明。')
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：final-001字节正确但副本命令假设错误，保留旧代次与失败；相对run-dir的四raw包副本检查通过，当前交付改用新final-002，研究命题不变；revision283。\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=docs['全景视野.md']['shards'][pp].replace('Session-A/交付/final-001/SEAL.json','Session-A/交付/final-002/SEAL.json')
    for p,kind,id in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 282','source_state_revision: 283');edit.replace_in_index(docs[p],f'projection_generation: 20260924-{kind}-282',f'projection_generation: 20260924-{kind}-283');s['records'][id]['projection_generation']=f'20260924-{kind}-283'
    files=[row for d in docs.values() for row in edit.payload_rows(d,ROOT)];seen={x['path'] for x in files}
    for p in rt.MUTABLE:
        if p in seen:continue
        body=(ROOT/p).read_text()
        if p==rt.STATE:body=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):body=body.replace('第三轮机器统观/Session-A/交付/final-001/SEAL.json','第三轮机器统观/Session-A/交付/final-002/SEAL.json').replace('revision282，B未审。','revision283，B未审；final-001及副本命令失败保留，新代次修正说明。')
        files.append(dict(path=p,expected_sha256=sha(p),text=body))
    prev=ROOT/'.codex/research/hott/sessions'/PREV
    audit=(prev/'CORE_COGNITION_AUDIT.md').read_text().replace(PREV,SID,1)+'\n同一最终交付单元：KC21机器证据要求促成副本实查，KC17/41–43与D07/12/21约束不能相信CLI名字。本次实测纠正两项接口读法；48KC的研究立场不变，证明/原文不变，新增证据见DELIVERY-REPAIR。\n'
    session=f'''# {SID}

- host: codex-desktop
- model: Astra（用户选择；不认证后端指纹）
- tier: T3
- role: RESEARCH_GENERATION / final delivery verification
- load_receipt: FINAL/RECOVERY.json及同单元281–282连续source-first复核；无新理论靶前提。
- report: {REPAIR}
- status: RESEARCH_UNCHANGED / FINAL002_SEAL_PENDING
- next: 精确提交修正与当前态，生成新final-002，实际seal/live/四raw包副本核验；B未审。

|element_usage|用途|
|---|---|
|实际副本命令|发现Git/全局例外与run-dir限制|
|固定失败|final001和三个诊断原件保留|
|canonical/48KC|只传播交付合同和代次，不改数学/验收|

reflection=no-plan-change；全量兼容审计复用已回读原文及本次差分；独占语义分片仍见审计/FINAL。无新数学定理或权限扩大。
'''
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],repair=REPAIR,diagnostics=OWN+'交付/final-001-verification',corrected_raw_evidence=OWN+'交付/final-001-verification/diagnostic-003/RESULT.json')
    files += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='同一MO3交付验证/纠错/canonical写回与新代次封存授权，保留旧seal/失败，不改研究验收。',files=files)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply);(HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
