"""Run saved tests and finite compiler checks; preserve exact execution evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, random, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.research.r024_diagonal_machine import *
OUT=ROOT/'artifacts/r024'

def main():
    logs=[]
    argv=[sys.executable,'-B',str(ROOT/'scripts/tests/test_r024_diagonal_machine.py')]
    started=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True,timeout=40,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    logs.append({'argv':argv,'cwd':str(ROOT),'started_utc':started,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    (OUT/'TEST_EXECUTION.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
    print(p.stderr)
    if p.returncode: raise RuntimeError('Saved tests failed; see raw log')
    rng=random.Random(20260911)
    instructions=[(SET,r,k,0) for r in range(3) for k in range(3)]
    instructions += [(INC,r,0,0) for r in range(3)]+[(HALT,r,0,0) for r in range(3)]
    instructions += [(COPY,a,b,0) for a in range(3) for b in range(3)]
    instructions += [(DECJZ,r,z,n) for r in range(3) for z in range(5) for n in range(5)]
    instructions += [(JUMP,n,0,0) for n in range(5)]
    hs={tuple(rng.choice(instructions) for _ in range(rng.randint(1,4))) for _ in range(250)}
    cases=[]
    for h in sorted(hs):
        d=compile_diagonal(h)
        assert decode(encode(h))==h and decode(diag(encode(h)))==d
        for y in range(8):
            source=run(h,pair(y,y),120)
            target=run(d,y,300)
            established=source['status'] in ('HALTED','REPEATED_NONTERMINAL')
            if source['status']=='HALTED':
                v=source['value']
                assert target['status']==('REPEATED_NONTERMINAL' if v==1 else 'HALTED'),(h,y,source,target)
                if v!=1: assert target['value']==(0 if v==0 else 2)
            elif source['status']=='REPEATED_NONTERMINAL':
                assert target['status']=='REPEATED_NONTERMINAL'
            cases.append({'code':str(encode(h)),'input':y,'source':source,'diagonal':target,
                          'finite_check_established':established})
    result={'scope':'FINITE_PROGRAM_SEMANTICS_AND_COMPILER_CHECKS_NOT_HOTT_KERNEL',
            'test_framework_exit':p.returncode,'program_count':len(hs),'run_pairs':len(cases),
            'established_pairs':sum(c['finite_check_established'] for c in cases),
            'unknown_pairs':sum(not c['finite_check_established'] for c in cases),
            'code_sha256':hashlib.sha256((ROOT/'scripts/research/r024_diagonal_machine.py').read_bytes()).hexdigest(),
            'predicate_convention':'T holds at-or-before n, returned outputs absorbing',
            'proof_by_enumeration':False,'native_hott_proof':'NOT_RUN','cases':cases}
    (OUT/'COMPILER_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
