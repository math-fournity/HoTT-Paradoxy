#!/usr/bin/env python3
"""Reconcile the actual proof packages used by the four-stage same-task audit."""
from pathlib import Path
import concurrent.futures,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
IDS=['MP-ASTRA-NATIVE-SOURCE-CONTRACT-001','MP-ASTRA-NATIVE-RICH-TASK-001',
     'MP-ASTRA-NATIVE-COMPLETION-001','MP-ASTRA-NATIVE-INTERVAL-001',
     'MP-ASTRA-WEAK-LIFT-PRINCIPLE-001','MP-ASTRA-SQRT2-TASK-COMPARISON-001',
     'MP-ASTRA-CURVE-DEFORMATION-001','MP-ASTRA-ENDPOINT-CLOSURE-001']


def check(row):
    results=[]
    for label,args in [('formal',['scripts/audit/verify_formal_proof_run.py','--run-dir',row['run']]),
                       ('version',['scripts/audit/verify_proof_version_closure.py','--proof-id',row['proof_id']])]:
        p=subprocess.run(['python3','-B',*args],cwd=ROOT,capture_output=True)
        prefix=row['proof_id']+'.'+label
        (OUT/(prefix+'.stdout.json')).write_bytes(p.stdout)
        (OUT/(prefix+'.stderr.txt')).write_bytes(p.stderr)
        results.append({'kind':label,'argv':args,'exit':p.returncode})
    return {'proof_id':row['proof_id'],'claims':row['claim_ids'],'source':row['source'],
            'run':row['run'],'checks':results,'scope':'current source/run/option/index and selected HEAD bytes; no kernel replay'}


def main():
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())
    assert state['revision']==198
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in head['tracked'].items())
    sources=json.loads((ROOT/'audit/astra-case-contract-20260920/SOURCE-INPUTS.json').read_text())
    source_rows=sources['messages']+sources['export_manifests']+sources['historical_plan_sources']
    for row in source_rows:
        b=(ROOT/row['path']).read_bytes();assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
    registry=json.loads((ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text())
    packages={r['proof_id']:r for r in registry['packages']+registry['later_packages']}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(check,[packages[i] for i in IDS]))
    receipt={'status':'SCOPED_INPUT_CHECKS_COMPLETED','head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),
             'revision':198,'source_rows_hash_matched':len(source_rows),'selected_packages':len(results),
             'results':results,'not_passed':[r['proof_id'] for r in results if any(c['exit'] for c in r['checks'])],
             'math_scope':'Existing package qualification only; same-task and physical/source semantics require explicit audit.',
             'new_kernel_replay':False}
    (OUT/'INPUT-VERIFICATION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='results'},ensure_ascii=False))


if __name__=='__main__':main()
