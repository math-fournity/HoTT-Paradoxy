#!/usr/bin/env python3
"""Read-only identities and source locators for a bounded historical-source review."""
from pathlib import Path
import hashlib, importlib.util, json, shutil, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r026'

def main():
    env={'python':sys.version,'executables':{x:shutil.which(x) for x in ['lean','agda','rocq','coqc','z3','cvc5']},
         'modules':{x:bool(importlib.util.find_spec(x)) for x in ['z3','sympy','pytest']}}
    (OUT/'ENVIRONMENT.json').write_text(json.dumps(env,indent=2)+'\n')
    print(json.dumps(env,indent=2))
    paths=['HoTT/CLAIM_EVIDENCE_MATRIX.md','HoTT/AUDIT_AND_RECONSTRUCTION.md','HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md','HoTT/THEORY_SCHEMA.md']
    terms=['有限','未知','模糊','linear','C12','C13','translat','鉴定','探索','时间','归约']
    rows=[]
    for rel in paths:
        p=ROOT/rel
        data=p.read_bytes();lines=data.decode().splitlines()
        print('\n###',rel,'lines',len(lines),'sha256',hashlib.sha256(data).hexdigest())
        chosen=set()
        for i,line in enumerate(lines):
            if any(t.lower() in line.lower() for t in terms):
                chosen.update(range(max(0,i-1),min(len(lines),i+2)))
        for i in sorted(chosen): print(f'{i+1}|{lines[i]}')
        rows.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'selected_lines':[i+1 for i in sorted(chosen)]})
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    print('\nSTATE TOP',list(state),'revision',state.get('current_version'))
    print('OPEN ROOTS',state.get('active'),state.get('review_due'),state.get('unresolved'))
    print('LAST RECORDS',json.dumps(list(state['records'].items())[-3:],ensure_ascii=False,indent=2) if isinstance(state['records'],dict) else json.dumps(state['records'][-3:],ensure_ascii=False,indent=2))
    (OUT/'SOURCE_LOCATORS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
