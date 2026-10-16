#!/usr/bin/env python3
"""Capture exact repair diff, source references and negative-run integrity."""
import importlib.util,json,sys
from pathlib import Path
from audit_current import ROOT,OUT,NEW,row,sha,save,execute

def main():
    paths=[ROOT/'Astra对击落HoTT工作的第一次审计/007 - 修订顺序、送审条件与可保留成果.md',
           ROOT/'数学危机工程/003 - 六缺口与被排除的门.md',
           ROOT/'HoTT/theory-schema/upstream/book-578b85cc/logic.tex',
           ROOT/'HoTT/theory-schema/upstream/book-578b85cc/reals.tex']
    save(OUT/'CONTEXT-SOURCES.json',[row(p) for p in paths])
    rec,r=execute('repair-diff',['git','diff','8fcb900','f958be9','--','scripts/audit/verify_formal_proof_run.py','HoTT/CLAIM_EVIDENCE_MATRIX.md','HoTT/formal/dedekind-omega-missile','Atria的方案/修订片/030 - B线收官（B1a过核+B1b败因登记+B1b′降格+B2降格+B3基准）.md'])
    spec=importlib.util.spec_from_file_location('verifier',ROOT/'scripts/audit/verify_formal_proof_run.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    rows=[]
    for rid in NEW[1:]:
        d=ROOT/'HoTT/verification/runs'/rid;run=json.loads((d/'RUN.json').read_text())
        for key in ('stdout','stderr','environment','source_manifest'):v.check_artifact(d,run[key],key)
        manifest=json.loads((d/'source-manifest.json').read_text())
        labels=[v.check_external_dependency(x) for x in manifest['external_dependencies']]
        rows.append({'run_id':rid,'artifact_hashes':'PASS','external_dependency_labels_verified':labels,
                     'scope':'Negative control integrity only; not generic positive-proof verifier acceptance.'})
    save(OUT/'NEGATIVE-RUN-INTEGRITY.json',rows)
    rec,r=execute('glm-shards',[sys.executable,'-B','scripts/audit/validate_governance_shards.py','GLM的第二次审计.md'])
    print('negative integrity',len(rows),'shards',r.returncode)

if __name__=='__main__':main()
