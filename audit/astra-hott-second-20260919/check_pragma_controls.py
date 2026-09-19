#!/usr/bin/env python3
"""Bounded verifier-correctness controls, not mathematical proof claims.

Generate transparent synthetic receipts under this audit directory. Test whether
comment text is mistaken for an effective Agda option. Actual project proof
sources, matrix and historical receipts are read-only. No external target.
"""
from pathlib import Path
import importlib.util, json, subprocess, sys
from audit_repairs import ROOT, OUT, NEW, sha, save, execute

def main():
    spec=importlib.util.spec_from_file_location('canonical_verifier',ROOT/'scripts/audit/verify_formal_proof_run.py')
    verifier=importlib.util.module_from_spec(spec);spec.loader.exec_module(verifier)
    base=json.loads((ROOT/'HoTT/verification/runs'/NEW[0]/'RUN.json').read_text())['command_argv'][:5]
    cases={
        'SafePositive':'{-# OPTIONS --safe --cubical #-}\nmodule SafePositive where\ndata Token : Set where\n  token : Token\n',
        'UnsafeNegative':'{-# OPTIONS --cubical #-}\nmodule UnsafeNegative where\npostulate witness : Set\n',
        'CommentPragma':'{-# OPTIONS --cubical #-}\n{-\n{-# OPTIONS --safe --cubical #-}\n-}\nmodule CommentPragma where\npostulate witness : Set\n',
    }
    results=[]
    for name,source in cases.items():
        # v1 used reserved Agda keyword "opaque" as an identifier and failed
        # parsing. Preserve that failed setup; v2 fixes only the identifier.
        fixture=OUT/'synthetic-verifier-controls-v2'/name
        fixture.mkdir(parents=True,exist_ok=False)
        p=fixture/(name+'.agda');p.write_text(source)
        relative=Path('HoTT/verification/runs')/('SYNTHETIC-'+name)
        d=fixture/relative;d.mkdir(parents=True)
        argv=base+['--ignore-interfaces','--no-libraries','-i',str(fixture),str(p)]
        receipt,r=execute('control-v2-'+name,argv,fixture)
        manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':'SYNTHETIC-OPTION-TEST',
                  'run_id':d.name,'files':[{'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}],
                  'external_dependencies':[]}
        save(d/'source-manifest.json',manifest)
        (d/'stdout.txt').write_bytes(r.stdout);(d/'stderr.txt').write_bytes(r.stderr)
        (d/'environment.txt').write_text('SYNTHETIC VERIFIER CONTROL; NOT A MATHEMATICAL RESULT\n'+sys.version+'\n')
        index=fixture/'HoTT/CLAIM_EVIDENCE_MATRIX.md'
        index.write_text('Synthetic test only. No project claim.\nSYNTHETIC-OPTION-TEST '+d.name+' SYNTHETIC-CONTROL\n')
        run={'schema_version':'formal-proof-run/v1','run_id':d.name,'proof_id':'SYNTHETIC-OPTION-TEST',
             'claim_ids':['SYNTHETIC-CONTROL'],'status':'KERNEL_ACCEPTED_WITH_SCOPE',
             'exit_code':r.returncode,'index_status':'INDEXED_IN_CLAIM_EVIDENCE_MATRIX',
             'theory_variant':'Cubical Agda synthetic option qualification control',
             'command_argv':argv,'scope':'Synthetic option test, no theorem claim',
             'index':{'path':'HoTT/CLAIM_EVIDENCE_MATRIX.md','sha256':sha(index.read_bytes())}}
        for field,fn in [('stdout','stdout.txt'),('stderr','stderr.txt'),('environment','environment.txt'),('source_manifest','source-manifest.json')]:
            data=(d/fn).read_bytes();run[field]={'path':fn,'bytes':len(data),'sha256':sha(data)}
        save(d/'RUN.json',run)
        try:
            checked=verifier.validate(fixture,relative,True)
        except verifier.ProofRunError as e:
            checked={'status':'FAIL','error':str(e)}
        row={'case':name,'kernel_exit':r.returncode,'verification':checked,
             'effective_safe_expected':name=='SafePositive',
             'fixture':str(fixture.relative_to(ROOT))}
        if name=='CommentPragma':
            forced,fr=execute('control-v2-CommentPragma-forced-safe',argv+['--safe'],fixture)
            row['forced_safe_exit']=fr.returncode
            row['forced_safe_diagnostic']=(fr.stdout+fr.stderr).decode()
        results.append(row);print(name,checked['status'],flush=True)
    save(OUT/'PRAGMA-CONTROLS-v2.json',{'verifier_source_sha256':sha((ROOT/'scripts/audit/verify_formal_proof_run.py').read_bytes()),
                                  'scope':'Three synthetic option controls. No global parser completeness claim.',
                                  'results':results})

if __name__=='__main__':main()
