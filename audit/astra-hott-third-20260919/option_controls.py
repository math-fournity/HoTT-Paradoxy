#!/usr/bin/env python3
"""Six synthetic Agda option controls for the actual current verifier.

All fixtures are isolated under this audit, labelled SYNTHETIC, and excluded
from the canonical claim matrix. No mathematical theorem is registered.
"""
import importlib.util, json, re
from pathlib import Path
from audit_current import ROOT,OUT,NEW,sha,save,execute

def main():
    spec=importlib.util.spec_from_file_location('verifier',ROOT/'scripts/audit/verify_formal_proof_run.py')
    v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    base=json.loads((ROOT/'HoTT/verification/runs'/NEW[0]/'RUN.json').read_text())['command_argv'][:5]
    cases={
      'SafePositive':'{-# OPTIONS --safe --cubical #-}\nmodule SafePositive where\ndata Token : Set where\n  token : Token\n',
      'UnsafeNegative':'{-# OPTIONS --cubical #-}\nmodule UnsafeNegative where\npostulate witness : Set\n',
      'BlockComment':'{-# OPTIONS --cubical #-}\n{-\n{-# OPTIONS --safe --cubical #-}\n-}\nmodule BlockComment where\npostulate witness : Set\n',
      'LineComment':'{-# OPTIONS --cubical #-}\n-- {-# OPTIONS --safe --cubical #-}\nmodule LineComment where\npostulate witness : Set\n',
      'NestedComment':'{-# OPTIONS --cubical #-}\n{- outer {- inner {-# OPTIONS --safe --cubical #-} -} -}\nmodule NestedComment where\npostulate witness : Set\n',
      'StringLiteral':'{-# OPTIONS --cubical #-}\nmodule StringLiteral where\nopen import Agda.Builtin.String using (String)\ntext : String\ntext = "{-# OPTIONS --safe --cubical #-}"\npostulate witness : Set\n',
    }
    rows=[]
    for name,source in cases.items():
        root=OUT/'synthetic-option-controls'/name;root.mkdir(parents=True,exist_ok=False)
        p=root/(name+'.agda');p.write_text(source)
        rd=Path('HoTT/verification/runs')/('SYNTHETIC-'+name);d=root/rd;d.mkdir(parents=True)
        argv=base+['--ignore-interfaces','--no-libraries','-i',str(root),str(p)]
        rec,r=execute('control-'+name,argv,root)
        manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':'SYNTHETIC-OPTION-CONTROL','run_id':d.name,
                  'files':[{'path':p.name,'bytes':len(p.read_bytes()),'sha256':sha(p.read_bytes())}],'external_dependencies':[]}
        save(d/'source-manifest.json',manifest)
        (d/'stdout.txt').write_bytes(r.stdout);(d/'stderr.txt').write_bytes(r.stderr)
        (d/'environment.txt').write_text('SYNTHETIC OPTION CHECK ONLY; NO MATHEMATICAL CLAIM\n')
        index=root/'HoTT/CLAIM_EVIDENCE_MATRIX.md';index.write_text('Synthetic test only\nSYNTHETIC-OPTION-CONTROL SYNTHETIC-CONTROL '+d.name+'\n')
        run={'schema_version':'formal-proof-run/v1','run_id':d.name,'proof_id':'SYNTHETIC-OPTION-CONTROL','claim_ids':['SYNTHETIC-CONTROL'],
             'status':'KERNEL_ACCEPTED_WITH_SCOPE','exit_code':r.returncode,'index_status':'INDEXED_IN_CLAIM_EVIDENCE_MATRIX',
             'theory_variant':'Cubical Agda synthetic option qualification test','command_argv':argv,
             'index':{'path':'HoTT/CLAIM_EVIDENCE_MATRIX.md','sha256':sha(index.read_bytes())}}
        for key,fn in [('stdout','stdout.txt'),('stderr','stderr.txt'),('environment','environment.txt'),('source_manifest','source-manifest.json')]:
            b=(d/fn).read_bytes();run[key]={'path':fn,'bytes':len(b),'sha256':sha(b)}
        save(d/'RUN.json',run)
        try:result=v.validate(root,rd,True)
        except v.ProofRunError as e:result={'status':'FAIL','error':str(e)}
        entry={'name':name,'kernel_exit':r.returncode,'expected_safe':name=='SafePositive','verifier':result,'source':str(p.relative_to(ROOT))}
        if name=='StringLiteral':
            forced,fr=execute('control-StringLiteral-forced-safe',argv+['--safe'],root)
            entry.update(forced_safe_exit=fr.returncode,forced_safe_diagnostic=(fr.stdout+fr.stderr).decode())
        rows.append(entry);print(name,r.returncode,result['status'],flush=True)
    save(OUT/'OPTION-CONTROLS.json',{'schema_version':'astra-third-option-controls/v1','verifier_sha256':sha((ROOT/'scripts/audit/verify_formal_proof_run.py').read_bytes()),
                                  'scope':'Five claimed lexical cases plus one string-literal holdout; finite executable controls, not a lexer completeness proof.','results':rows})

if __name__=='__main__':main()
