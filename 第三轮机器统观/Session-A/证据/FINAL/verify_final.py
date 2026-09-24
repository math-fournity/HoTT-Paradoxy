#!/usr/bin/env python3
"""Capture the bounded final validation without re-running or altering proofs."""
from pathlib import Path
import hashlib,importlib.util,json,re,subprocess,sys,datetime
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    out=HERE/'validation';out.mkdir(exist_ok=False)
    s=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());h=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());core=s['current_core']
    checks=[('three-way',['python3','-B','scripts/audit/verify_three_way_cognition.py']),('shards',['python3','-B','scripts/audit/verify_governance_shards.py']),('core',['python3','-B','scripts/audit/verify_core_cognition.py','--core',core['path'],'--manifest',core['manifest'],'--curation',core['curation'],'--transition',core['transition']])]
    packages=[('MP-MO3-STAGE-COLIMIT-001','20260923-MO3-STAGE-COLIMIT-001-04'),('MP-MO3-BOUQUET-ORDER-001','20260924-MO3-BOUQUET-ORDER-001-02'),('MP-MO3-FINITE-COVER-001','20260924-MO3-FINITE-COVER-001-08'),('MP-MO3-OPEN-COVER-MARGIN-001','20260924-MO3-OPEN-COVER-MARGIN-001-01')]
    for id,run in packages:
        checks += [(id+'-run',['python3','scripts/audit/verify_formal_proof_run.py','--run-dir','HoTT/verification/runs/'+run]),(id+'-version',['python3','scripts/audit/verify_proof_version_closure.py','--proof-id',id])]
    rows=[]
    for n,argv in checks:
        r=subprocess.run(argv,cwd=ROOT,capture_output=True);(out/(n+'.stdout.txt')).write_bytes(r.stdout);(out/(n+'.stderr.txt')).write_bytes(r.stderr);rows.append(dict(name=n,argv=argv,exit=r.returncode))
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt);rt.query_record(ROOT,'MO3-GOVERNED-A');plan=rt.plan(ROOT,profile='research',task_ids=['MO3-GOVERNED-A']);(out/'research-plan.json').write_bytes(rt.dump(plan))
    quotes={};pattern=r'<!-- original:(KC-\d+):begin -->(.*?)<!-- original:\1:end -->'
    for k,p in [('006','第三条发现路径：把知识谱当作被考察对象'),('008','现实对齐：理论是现实的骨架式模仿')]:
        old=(HERE/f'ESSAY-{k}-BEFORE.txt').read_text();new=(ROOT/'扩展认知'/f'{k} - {p}.md').read_text();quotes[k]=dict(unchanged=re.findall(pattern,old,re.S)==re.findall(pattern,new,re.S),ids=[x[0] for x in re.findall(pattern,new,re.S)],applied_proposed=sha(ROOT/'扩展认知'/f'{k} - {p}.md')==sha(HERE/f'ESSAY-{k}-PROPOSED.txt'))
    drift=[p for p,v in h['tracked'].items() if sha(ROOT/p)!=v]
    primary=[]
    for id,run in packages:
        p=ROOT/'HoTT/verification/runs'/run;m=json.loads((p/'source-manifest.json').read_text());receipt=json.loads((p/'RUN.json').read_text());primary.append(dict(proof_id=id,run=run,exit=receipt['exit_code'],local_input_drift=[r['path'] for r in m['files'] if sha(ROOT/r['path'])!=r['sha256']]))
    builtin=json.loads((ROOT/'HoTT/formal/mo3/stage-colimit/BUILTIN-SOURCES.json').read_text())
    # Keep explicit external identities in the result; source validators own their schema checks.
    receipt=json.loads((ROOT/'.codex/cognition/checkpoints/S-RES-20260924-MO3-A-FINAL/result.json').read_text())
    ok=all(x['exit']==0 for x in rows) and not drift and not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'] and all(x['unchanged'] and x['applied_proposed'] for x in quotes.values()) and all(x['exit']==0 and not x['local_input_drift'] for x in primary) and sha(ROOT/core['path'])==core['core_sha256'] and receipt['status']=='CHECKPOINT_COMMITTED' and s['revision']==281
    result=dict(schema='mo3-final-validation/v1',status='PASS_WITH_SCOPE' if ok else 'FAILED',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),revision=s['revision'],canonical_receipt='.codex/cognition/checkpoints/S-RES-20260924-MO3-A-FINAL/result.json',checks=rows,tracked_paths=len(h['tracked']),tracked_drift=drift,review_required=plan['review_required'],query_first_promoted=plan['hydration_diagnostics']['query_first_promoted'],quotes=quotes,core_sha256=sha(ROOT/core['path']),primary_runs=primary,scope='Selected four existing native evidence packages plus state/source/structure, no new kernel replay or independent B audit; full-registry legacy mismatch not repaired')
    (out/'RESULT.json').write_bytes(rt.dump(result));print(json.dumps(result,ensure_ascii=False));return 0 if ok else 1
if __name__=='__main__':sys.exit(main())
