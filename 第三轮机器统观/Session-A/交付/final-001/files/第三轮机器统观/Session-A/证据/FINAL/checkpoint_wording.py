#!/usr/bin/env python3
"""Close final attribution wording without changing proof inputs or acceptance."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
SID='S-RES-20260924-MO3-A-FINAL-WORDING';TASK='MO3-GOVERNED-A';BASE=f'.codex/research/hott/sessions/{SID}/';PREV='S-RES-20260924-MO3-A-FINAL'
CHANGED=['第三轮机器统观/Session-A/'+p for p in ['覆盖与关系/005 - 已接受非叶问题的独立对账.md','结论账本.md','最终报告.md']]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt);sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());h=json.loads((ROOT/rt.HEAD).read_text());assert s['revision']==281 and SID not in s['records'];assert all(sha(p)==v for p,v in h['tracked'].items())
    rt.query_record(ROOT,TASK);plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert not plan['hydration_diagnostics']['query_first_promoted']
    altered=[]
    for id,r in s['records'].items():
        for p,v in list(r.get('source_hashes',{}).items()):
            if p in CHANGED and v!=sha(p):
                assert id==TASK or id.startswith('R-MO3-');r['source_hashes'][p]=sha(p);r['revalidation']='Final wording removes ambiguity that a qualified HoTT instance must have an exclusive mechanism. Shared mechanisms remain eligible; actual missing same-task bridge/commitment still determines no-hit. No proof input, native result, method or acceptance change.';altered.append([id,p])
    s['revision']=282;s['latest_session']=SID;s['execution_control'].update(last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json')
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='ATTRIBUTION_WORDING_REVIEW_NO_NEW_MATHEMATICS',depends_on=[],related_records=[TASK],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';docs['MEMORY.md']['shards'][mp]=docs['MEMORY.md']['shards'][mp].replace('revision281，B未审。','revision282，B未审。')
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：去除G3“特有”造成的专属性歧义，共有机制的HoTT实例仍可研究；原生命题/现实桥判词及交付条件不变，revision282。\n')
    for p,kind,id in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 281','source_state_revision: 282');edit.replace_in_index(docs[p],f'projection_generation: 20260924-{kind}-281',f'projection_generation: 20260924-{kind}-282');s['records'][id]['projection_generation']=f'20260924-{kind}-282'
    files=[row for d in docs.values() for row in edit.payload_rows(d,ROOT)];seen={x['path'] for x in files}
    for p in rt.MUTABLE:
        if p in seen:continue
        text=(ROOT/p).read_text()
        if p==rt.STATE:text=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):text=text.replace('revision281，B未审。','revision282，B未审。')
        files.append(dict(path=p,expected_sha256=sha(p),text=text))
    oldbase=ROOT/'.codex/research/hott/sessions'/PREV
    audit=(oldbase/'CORE_COGNITION_AUDIT.md').read_text().replace(PREV,SID,1)+'\n本次同一综合单元追加D15归属复核：共有机制不因非HoTT独有而失去研究资格；48KC立场不变，KC27直接支持该澄清。原生输入/判断及原文不变。\n'
    session=f'''# {SID}

- host: codex-desktop
- model: Astra（用户指定；非指纹认证）
- tier: T3
- role: RESEARCH_GENERATION / same final synthesis unit
- load_receipt: FINAL/RECOVERY.json及本单元完整core/扩展/最高指示；沿281连续消费，无新理论靶点。
- scope: G3及账本/最终报告消除“特有”歧义，共有机制仍可研究；不改验收/数学或现实桥判词。
- next: 按原最终交付条件完成精确subject commit、seal、verify；B未审。

|element_usage|用途|
|---|---|
|KC27及D15|归属与独有性分开|
|canonical|传播三个当前文件pin，不改旧收据|
|既有验证|native/source不变，复用281四包检查；282状态另核|

reflection=no-plan-change；全量KC兼容审计附本次差分，独占语义分片仍见审计/FINAL。无新增数学声明或权限变化。
'''
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],reused_validation='第三轮机器统观/Session-A/证据/FINAL/validation/RESULT.json',changed_report_paths=CHANGED)
    files += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='同一MO3本轮最终结论纠偏与canonical写回授权，不改验收或证据原件。',files=files)
    (HERE/'wording-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=a.apply);(HERE/('wording-apply.json' if a.apply else 'wording-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps(dict(result={k:v for k,v in res.items() if k!='paths'},refreshed_pins=altered),ensure_ascii=False))
if __name__=='__main__':main()
