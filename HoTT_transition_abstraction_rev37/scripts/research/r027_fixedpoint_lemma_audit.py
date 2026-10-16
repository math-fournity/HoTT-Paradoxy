"""Finite model audit of IN-006's missing hypotheses. Not a HoTT/Lean kernel.
All functions on labelled state sets of size 1..4 are enumerated.
Orbits terminate on repeated states (finite-model completeness, not a fuel claim).
"""
from itertools import product
from pathlib import Path
import datetime, hashlib, json, time
ROOT=Path(__file__).resolve().parents[2]

def orbit(step, start):
    seen=set(); seq=[]; q=start
    while q not in seen:
        seen.add(q); seq.append(q); q=step[q]
    return seq, q

def local_no_return(step, returned, trap):
    seq,_=orbit(step,trap)
    return not any(returned[q] for q in seq)

def run_checks():
    counts={'labelled_models':0,'fixed_nonreturning_traps':0,
            'local_cases':0,'globally_applicable_cases':0,
            'return_forward_closed_models':0,'exact_return_absorbing_models':0}
    violations=[]
    for size in range(1,5):
        for step in product(range(size),repeat=size):
            for ret in product((False,True),repeat=size):
                counts['labelled_models']+=1
                closed=all(not ret[q] or ret[step[q]] for q in range(size))
                exact=all(not ret[q] or step[q]==q for q in range(size))
                counts['return_forward_closed_models']+=int(closed)
                counts['exact_return_absorbing_models']+=int(exact)
                for trap in range(size):
                    if ret[trap] or step[trap]!=trap: continue
                    counts['fixed_nonreturning_traps']+=1
                    counts['local_cases']+=1
                    if not local_no_return(step,ret,trap):
                        violations.append(['local',step,ret,trap])
                    if not closed: continue
                    for start in range(size):
                        seq,_=orbit(step,start)
                        if trap not in seq: continue
                        counts['globally_applicable_cases']+=1
                        if any(ret[q] for q in seq):
                            violations.append(['global',step,ret,start,trap])
    assert counts['labelled_models']==4330
    assert not violations
    # Reachability is absent: one component returns, another is a fixed trap.
    a={'name':'missing_reachability','step':[0,1],'returned':[True,False], 'start':0,'trap':1}
    a['orbit']=orbit(a['step'],a['start'])[0]
    a['trap_local_no_return']=local_no_return(a['step'],a['returned'],a['trap'])
    a['global_no_return']=not any(a['returned'][q] for q in a['orbit'])
    assert a['trap_local_no_return'] and not a['global_no_return']
    # Reachability is present, but return persistence is absent.
    b={'name':'missing_return_persistence','step':[1,2,2], 'returned':[False,True,False],'start':0,'trap':2}
    b['orbit']=orbit(b['step'],b['start'])[0]
    b['trap_reachable']=b['trap'] in b['orbit']
    b['global_no_return']=not any(b['returned'][q] for q in b['orbit'])
    assert b['trap_reachable'] and not b['global_no_return']
    # Being nonreturning at one step is weaker than being at the fixed point.
    c={'name':'weak_induction_invariant','step':[1,2,2],'returned':[False,False,True],'start':0}
    c['orbit']=orbit(c['step'],c['start'])[0]
    assert not c['returned'][c['step'][0]] and c['returned'][c['step'][c['step'][0]]]
    # Exact state absorption stronger than needed; returning can change store/state.
    d={'name':'return_predicate_persistent_without_state_absorption',
       'step':[1,1,2,2],'returned':[True,True,False,False], 'start':3,'trap':2}
    assert all(not d['returned'][q] or d['returned'][d['step'][q]] for q in range(4))
    assert d['step'][0]!=0 and d['returned'][0]
    assert not any(d['returned'][q] for q in orbit(d['step'],d['start'])[0])
    # Explicit toy H is decidable: a data axiom alone is not proof of noncomputability.
    table=[]
    for p,x in product(range(4),repeat=2):
        H=(p==0); value=H
        assert (value is True)==H
        table.append({'p':p,'x':x,'toy_H':H,'oracle_value':value})
    return {'schema':'r027-targeted/v1','status':'PASS_FINITE_MODEL_SCOPE','counts':counts,
      'violations':violations,'counterexamples':[a,b,c],'positive_control':d,'decidable_toy_oracle':table,
      'groups':['local_fixedpoint','global_reachable_persistent_return','reachability_counterexample',
                'return_persistence_counterexample','induction_strength_counterexample',
                'weaker_persistence_positive_control','toy_oracle_not_intrinsically_uncomputable'],
      'scope':'All labelled deterministic graphs of sizes1..4; not all programs, not kernel checking, no MP independence test',
      'native_Lean':'NOT_RUN_BY_THIS_SCRIPT','native_HoTT':'NOT_RUN'}

def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat(); t=time.perf_counter()
    result=run_checks()
    out=ROOT/'artifacts/r027'; out.mkdir(parents=True,exist_ok=True)
    dst=out/'FINITE_MODEL_RESULTS.json'; dst.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    receipt={'started_utc':start,'duration_seconds':time.perf_counter()-t,
             'code':str(Path(__file__).relative_to(ROOT)),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'result_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'status':'RETURNED_WITH_ALL_ASSERTIONS',
             'proof_level':'Finite exhaustive graph check only'}
    (out/'FINITE_MODEL_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
