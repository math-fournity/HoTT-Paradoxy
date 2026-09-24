#!/usr/bin/env python3
"""Execute fixed rational-interval searches; native soundness is separate evidence."""
from fractions import Fraction
from pathlib import Path
import hashlib, itertools, json, platform, sys
HERE=Path(__file__).resolve().parent

def words(fuel, alphabet):
    if fuel==0:return [[]]
    smaller=words(fuel-1, alphabet)
    return [[]]+[[x,*xs] for x in alphabet for xs in smaller]

def certificate(family, indices):
    if not indices:return False
    left,right=family(indices[0])
    if not left<0:return False
    for i in indices[1:]:
        next_left,next_right=family(i)
        if not next_left<right:return False
        right=next_right
    return 1<right

def main():
    fixture=json.loads((HERE/'families.json').read_text());results=[]
    for case in fixture['cases']:
        prefix=[tuple(map(Fraction,p)) for p in case['prefix']];tail=tuple(map(Fraction,case['tail']))
        def family(i):return prefix[i] if i<len(prefix) else tail
        stages=[];found=None
        for n in range(case['last_observed_stage']+1):
            candidates=words(n,list(range(n+1)))
            independent={p for k in range(n+1) for p in itertools.product(range(n+1),repeat=k)}
            assert len(candidates)==len(independent) and set(map(tuple,candidates))==independent
            answer=next((xs for xs in candidates if certificate(family,xs)),None)
            stages.append({'stage':n,'candidate_denominator':len(candidates),'independent_set_equal':True,'remainder':0,'first_valid_indices':answer})
            if answer is not None:
                found={'stage':n,'indices':answer,'intervals':[[str(q) for q in family(i)] for i in answer]};break
        assert (None if found is None else found['stage'])==case['expected_first_stage']
        if case.get('expected_indices') is not None:assert found['indices']==case['expected_indices']
        if 'required_original_indices' in case:assert set(case['required_original_indices']).issubset(found['indices'])
        results.append({'id':case['id'],'stages':stages,'output':found,'no_output_boundary':None if found else 'Only the recorded stages; no unbounded no-cover or nontermination claim.'})
    out={'schema':'mo3-c02-rational-search-run/v1','status':'FIXED_INPUTS_MATCHED','python':sys.version,'platform':platform.platform(),'source_hashes':{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in ['families.json','run_rational_search.py']},'results':results,'boundary':'Software observations on four fixed families; exact Fractions, not real sampling. Native certificate soundness and source-cover adequacy are separate obligations.'}
    with (HERE/'rational-search-result.json').open('x') as f:f.write(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'outputs':{r['id']:r['output'] for r in results}},ensure_ascii=False))

if __name__=='__main__':main()
