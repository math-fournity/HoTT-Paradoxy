"""Targeted audit of IN-007's universal ReachTrap. Finite models, not a HoTT kernel.
The unbounded implication is proved separately. No simulated Lean output.
"""
from pathlib import Path
from itertools import product
import argparse, hashlib, importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]

def orbit(step, start):
    seen=set(); trace=[]; q=start
    while q not in seen:
        seen.add(q);trace.append(q);q=step[q]
    return trace

def preserves(step,ret):
    return all(not ret[q] or ret[step[q]] for q in range(len(step)))

def reaches_trap(step,ret,start):
    return any(step[q]==q and not ret[q] for q in orbit(step,start))

def check():
    counts=[]; accepted=[]
    for n in range(1,4):
        examined=ok=0
        for delta in product(range(n),repeat=n):
            for ret in product((False,True),repeat=n):
                examined+=1
                if preserves(delta,ret) and all(reaches_trap(delta,ret,q) for q in range(n)):
                    ok+=1
                    assert not any(ret), (delta,ret)
        counts.append({'states':n,'models':examined,'satisfy_universal_reach_and_preservation':ok})
    # Legal two-state machine: a trap and an absorbing returned state coexist.
    delta=(0,1);ret=(False,True)
    assert preserves(delta,ret) and reaches_trap(delta,ret,0)
    assert not reaches_trap(delta,ret,1) and ret[1]
    local={'step':delta,'returned':ret,'valid_local_initial':0,'counterexample_to_universal_initial':1}
    # The peer assumptions are not intrinsically inconsistent: all states may be non-returned.
    delta0=(0,0,0);ret0=(False,False,False)
    assert preserves(delta0,ret0) and all(reaches_trap(delta0,ret0,q) for q in range(3))
    consistent={'step':delta0,'returned':ret0,'satisfies_peer_universal_hypothesis':True}
    # Remove preservation: all states reach a non-returned trap although a state is returned.
    delta1=(0,0);ret1=(False,True)
    assert all(reaches_trap(delta1,ret1,q) for q in range(2))
    assert not preserves(delta1,ret1) and any(ret1)
    missing={'step':delta1,'returned':ret1,'trace_from_returned':orbit(delta1,1)}

    module_path=ROOT/'scripts/research/r024_diagonal_machine.py'
    sp=importlib.util.spec_from_file_location('r028_original_r024',module_path)
    machine=importlib.util.module_from_spec(sp);sys.modules[sp.name]=machine;sp.loader.exec_module(machine)
    def replay(p,x):
        s=machine.State.initial(x);trace=[repr(s)];seen=set()
        for n in range(100):
            if isinstance(s,machine.Returned):
                assert machine.step(p,s)==s
                return {'status':'RETURNED','steps':n,'value':s.value,'trace':trace}
            if s in seen:
                assert machine.step(p,s)==s  # these two chosen cases have fixed, not general, cycles
                return {'status':'NONRETURN_FIXED_POINT','steps':n,'trace':trace}
            seen.add(s);s=machine.step(p,s);trace.append(repr(s))
        raise AssertionError('Unexpected fuel exhaustion; not treated as divergence')
    actual=[]
    for b in (0,1):
        h=machine.program(((machine.SET,0,b,0),(machine.HALT,0,0,0)))
        p=machine.compile_diagonal(h);r=replay(p,0)
        assert r['status']==('RETURNED' if b==0 else 'NONRETURN_FIXED_POINT')
        if b==0: assert r['value']==0
        # Every compiled program's whole Config type still contains Returned(0).
        returned=machine.Returned(0)
        assert machine.step(p,returned)==returned
        actual.append({'candidate_constant':b,'program':[list(i) for i in p],'result':r,
                       'arbitrary_returned_state_is_absorbing':True})
    return {'scope':'234 finite systems plus two explicit R024 runs; general theorem is paper proof',
            'check_groups':5,'groups_passed':5,'finite_models':counts,'model_total':sum(c['models'] for c in counts),
            'satisfying_total':sum(c['satisfy_universal_reach_and_preservation'] for c in counts),
            'local_success_universal_failure':local,'consistent_all_nonreturn_model':consistent,
            'preservation_needed_countermodel':missing,'original_r024_examples':actual,
            'r024_sha256':hashlib.sha256(module_path.read_bytes()).hexdigest(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'native_Lean_or_HoTT':'NOT_RUN','unbounded_proof_by_this_program':False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);a=ap.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    result=check();a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='original_r024_examples'},ensure_ascii=False,indent=2))
    print('Actual R024 cases:',[(x['candidate_constant'],x['result']['status'],x['result']['steps']) for x in result['original_r024_examples']])
if __name__=='__main__':main()
