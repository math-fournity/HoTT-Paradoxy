#!/usr/bin/env python3
"""Pin secondary audit sources and capture scoped current-state checks."""
from pathlib import Path
import json, subprocess, sys
from audit_repairs import ROOT, OUT, save, file_row, execute

def main():
    paths=[]
    for folder in ['Astra对击落HoTT工作的第一次审计','Terra的第一次审计',
                   'Astra继续尝试/四弹一体完整研究策略']:
        paths.extend((ROOT/folder).glob('*.md'))
    for folder in ['Atria的方案/修订片']:
        for prefix in ['027','030']:
            paths.extend((ROOT/folder).glob(prefix+'*.md'))
    paths.extend(ROOT/p for p in ['HoTT/theory-schema/upstream/book-578b85cc/logic.tex',
             'HoTT/theory-schema/upstream/book-578b85cc/reals.tex',
             'HoTT/formal/dedekind-omega-missile/CLAIM-PACKAGE-REAL-LAYER.md',
             'Astra继续尝试/四弹一体完整研究策略.md','GLM的审计报告.md',
             'HoTT/verification/PROOF_VERSION_CLOSURE.json',
             'scripts/audit/verify_proof_version_closure.py',
             'scripts/audit/verify_math_proof_delivery_governance.py'])
    save(OUT/'CONTEXT-SOURCES.json',[file_row(p) for p in sorted(set(paths))])
    rows=[]
    for label,argv in [
        ('math-governance',[sys.executable,'-B','scripts/audit/verify_math_proof_delivery_governance.py','--project-root','.']),
        ('version-closure',[sys.executable,'-B','scripts/audit/verify_proof_version_closure.py','--project-root','.']),
        ('repair-diff',['git','diff','19d45ce','d304994','--','HoTT/formal/dedekind-omega-missile/CutRealLayer.agda','scripts/audit/verify_formal_proof_run.py','HoTT/CLAIM_EVIDENCE_MATRIX.md']),
        ('repair-files',['git','show','--format=fuller','--stat','59cc2a2']),
    ]:
        row,r=execute(label,argv);rows.append(row)
        print(label,r.returncode,flush=True)
    # Evidence quotes at an exact historical identity, not the moving checkout.
    old=subprocess.check_output(['git','show','8a334e0:HoTT/CLAIM_EVIDENCE_MATRIX.md'],cwd=ROOT,text=True)
    selected=[]
    for i,line in enumerate(old.splitlines(),1):
        if line.startswith(('| CAND-F2-7-M3 |','| CAND-F2-7-M3-UNC |','| CAND-F2-7-REBOUND-DISARM |','| CAND-F2-7-NECESSITY-LEM |','| **B2 ')):
            selected.append({'line':i,'text':line})
    save(OUT/'BASELINE-MATRIX-EXCERPTS.json',{'ref':'8a334e0','path':'HoTT/CLAIM_EVIDENCE_MATRIX.md','rows':selected})
    save(OUT/'CONTEXT-CHECKS.json',rows)

if __name__=='__main__':main()
