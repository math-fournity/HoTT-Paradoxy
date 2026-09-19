#!/usr/bin/env python3
"""Verify the bounded new engineering observations in Terra's audit.

This only writes its own evidence directory and a disposable copy of M1.
No proof source, historical receipt, release target, or registry is changed.
"""
from pathlib import Path
import hashlib, json, shutil, subprocess, tempfile

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]

def digest(b):
    return hashlib.sha256(b).hexdigest()

def execute(name, argv, cwd=ROOT):
    r = subprocess.run(argv, cwd=cwd, capture_output=True, check=False)
    (OUT/(name+'-stdout.txt')).write_bytes(r.stdout)
    (OUT/(name+'-stderr.txt')).write_bytes(r.stderr)
    return {'argv':argv,'cwd':str(cwd),'exit_code':r.returncode,
            'stdout_sha256':digest(r.stdout),'stderr_sha256':digest(r.stderr),
            'stdout_bytes':len(r.stdout),'stderr_bytes':len(r.stderr)}

def main():
    results={}
    results['math_governance']=execute('math-governance',['python3','-B','scripts/audit/verify_math_proof_delivery_governance.py','--project-root','.'])
    registry=json.loads((ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text())
    baseline=registry['proof_asset_commit']
    old=subprocess.check_output(['git','show',baseline+':HoTT/CLAIM_EVIDENCE_MATRIX.md'],cwd=ROOT)
    now=(ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md').read_bytes()
    first=next((i for i,(a,b) in enumerate(zip(old.splitlines(),now.splitlines())) if a!=b),None)
    results['closure_baseline']={'commit':baseline,'current_has_frozen_prefix':now.startswith(old),'first_different_line_1based':None if first is None else first+1,
        'frozen_line':None if first is None else old.splitlines()[first].decode(),
        'current_line':None if first is None else now.splitlines()[first].decode(),
        'dedekind_registered_later_packages':[x['proof_id'] for x in registry['later_packages'] if 'DEDEKIND' in x['proof_id']]}
    results['matrix_diff']=execute('matrix-diff',['git','diff','--unified=3',baseline,'HEAD','--','HoTT/CLAIM_EVIDENCE_MATRIX.md'])
    run=json.loads((ROOT/'HoTT/verification/runs/20260917-MP-DEDEKIND-OMEGA-M1-04/RUN.json').read_text())
    with tempfile.TemporaryDirectory(prefix='astra-terra-path-probe-',dir='/Volumes/D/HoTT-toolchain-cache') as temp:
        dest=Path(temp)/run['command_argv'][-1]
        dest.parent.mkdir(parents=True)
        shutil.copyfile(ROOT/run['command_argv'][-1],dest)
        results['relocated_m1']=execute('relocated-m1',run['command_argv'],Path(temp))
        results['relocated_m1']['source_sha256']=digest(dest.read_bytes())
        results['relocated_m1']['diagnostic_matched']='ModuleDefinedInOtherFile' in ((OUT/'relocated-m1-stdout.txt').read_text()+(OUT/'relocated-m1-stderr.txt').read_text())
        results['relocated_m1']['scope']='Same entrypoint bytes, historical argv unchanged, different cwd with relative entrypoint; a path-coupling check, not a full portable release build.'
    paths=[ROOT/'Terra的第一次审计.md',*sorted((ROOT/'Terra的第一次审计').glob('*.md'))]
    results['terra_sources']=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in paths]
    frozen=json.loads((OUT.parent/'source-snapshot-before.json').read_text())
    results['prior_proof_scope_drift']=[row['path'] for row in frozen if digest((ROOT/row['path']).read_bytes())!=row['sha256']]
    receipt=json.loads((OUT.parent/'FOUR-SET-IDENTITY.json').read_text())
    results['four_set_drift']=[row['path'] for row in receipt if digest((ROOT/row['path']).read_bytes())!=row['sha256']]
    results['head']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    (OUT/'VERIFICATION.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'head':results['head'],'first_matrix_diff':results['closure_baseline'],'governance_exit':results['math_governance']['exit_code'],'relocation_exit':results['relocated_m1']['exit_code'],'relocation_diagnostic':results['relocated_m1']['diagnostic_matched'],'proof_drift':results['prior_proof_scope_drift'],'four_set_drift':results['four_set_drift']},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
