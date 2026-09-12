"""Audit exact R024 transitions with a separately written reference stepper.

Certificates are finite executable evidence, not HoTT proof terms. The general
fixed-point non-return lemma and the compiler simulation are stated separately.
No installation, external service, or proof-assistant emulation is performed.
"""
from __future__ import annotations
from dataclasses import asdict
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.research import r024_diagonal_machine as m

def canonical(pc: int, regs: dict[int, int]) -> m.State:
    return m.State(pc, tuple(sorted((k,v) for k,v in regs.items() if v != 0)))

def reference_step(p: m.Program, state: m.Config) -> m.Config:
    """Independent implementation of the declared transition table."""
    if isinstance(state, m.Returned):
        return state
    pc = state.pc
    if pc < 0 or pc >= len(p):
        return state
    op, a, b, c = p[pc]
    old = dict(state.registers)
    new = old.copy()
    if op == m.HALT:
        return m.Returned(old.get(a, 0))
    if op == m.JUMP:
        return canonical(a, new)
    if op == m.DECJZ:
        if old.get(a, 0) == 0:
            return canonical(b, new)
        new[a] = old[a]-1
        return canonical(c, new)
    if op == m.SET:
        new[a] = b
    elif op == m.COPY:
        new[a] = old.get(b, 0)
    elif op == m.ADD:
        new[a] = old.get(b, 0)+old.get(c, 0)
    elif op == m.MUL:
        new[a] = old.get(b, 0)*old.get(c, 0)
    elif op == m.INC:
        new[a] = old.get(a, 0)+1
    else:
        raise ValueError('Invalid opcode')
    return canonical(pc+1, new)

def iterate(p: m.Program, s: m.Config, n: int, stepper=m.step) -> m.Config:
    for _ in range(n):
        s=stepper(p,s)
    return s

def encode_state(s: m.Config) -> dict:
    if isinstance(s,m.Returned):
        return {'tag':'Returned','value':s.value}
    return {'tag':'State','pc':s.pc,'registers':[list(kv) for kv in s.registers]}

def decode_state(data: dict) -> m.Config:
    if data.get('tag')=='Returned':
        return m.Returned(m.nat(data['value']))
    if data.get('tag')!='State':
        raise ValueError('Unknown configuration tag')
    regs=[(m.nat(k),m.nat(v)) for k,v in data['registers']]
    if regs!=sorted(set(regs)) or len({k for k,v in regs})!=len(regs) or any(v==0 for k,v in regs):
        raise ValueError('Noncanonical finite register support')
    return m.State(m.nat(data['pc']),tuple(regs))

def make_certificate(p:m.Program,x:int,limit:int=200) -> dict:
    p=m.program(p)
    s=m.State.initial(x)
    states=[encode_state(s)]
    for _ in range(limit):
        nxt=m.step(p,s)
        states.append(encode_state(nxt))
        if isinstance(nxt,m.Returned) or (nxt==s and isinstance(nxt,m.State)):
            break
        s=nxt
    return {'program':[list(i) for i in p],'input':x,'trace':states,
            'scope':'finite trace plus independently checked nonterminal fixed-point equation'}

def check_certificate(cert:dict) -> bool:
    """Check start, every transition, no returned prefix, final fixed point."""
    try:
        p=m.program(cert['program']);x=m.nat(cert['input'])
        states=[decode_state(s) for s in cert['trace']]
        if not states or states[0]!=m.State.initial(x):return False
        if any(isinstance(s,m.Returned) for s in states):return False
        if any(reference_step(p,s)!=t for s,t in zip(states,states[1:])):return False
        return reference_step(p,states[-1])==states[-1]
    except (KeyError,ValueError,TypeError):
        return False

def all_cases() -> dict:
    checks={};certificate_rows=[]
    # Every primitive including aliases, zero tests, boundary/large jump targets.
    instructions=set()
    registers=(0,1,5)
    for a in registers:
        for value in (0,1,2,19):instructions.add((m.SET,a,value,0))
        for b in registers:instructions.add((m.COPY,a,b,0))
        instructions.add((m.INC,a,0,0));instructions.add((m.HALT,a,0,0))
        for b,c in product(registers,repeat=2):
            instructions.add((m.ADD,a,b,c));instructions.add((m.MUL,a,b,c))
        for b,c in product((0,1,2,999),repeat=2):instructions.add((m.DECJZ,a,b,c))
    for dest in (0,1,2,999):instructions.add((m.JUMP,dest,0,0))
    pairs=0;normal_blocks=0;halt_blocks=0
    for ins in sorted(instructions):
        p=m.program((ins,(m.HALT,0,0,0)))
        d=m.compile_diagonal(p);trap=4+2*len(p);post=trap+1
        for values in product((0,1,2,7),repeat=3):
            rho=dict(zip(registers,values));source=canonical(0,rho)
            expected=reference_step(p,source)
            assert m.step(p,source)==expected
            target=canonical(4,{0:17,1:23,2:31,**{r+3:v for r,v in rho.items()}})
            op=ins[0];micro=1 if op in (m.JUMP,m.DECJZ) else 2
            evolved=iterate(d,target,micro)
            reference=iterate(d,target,micro,reference_step)
            assert evolved==reference
            if isinstance(expected,m.Returned):
                assert isinstance(evolved,m.State) and evolved.pc==post
                assert dict(evolved.registers).get(0,0)==expected.value
                for r in registers:assert dict(evolved.registers).get(r+3,0)==rho.get(r,0)
                halt_blocks+=1
            else:
                address=4+2*expected.pc if expected.pc<len(p) else trap
                wanted={0:17,1:23,2:31,**{r+3:v for r,v in expected.registers}}
                assert evolved==canonical(address,wanted),(ins,values,evolved,expected)
                normal_blocks+=1
            pairs+=1
    checks['instruction_and_block_agreement']={'instructions':len(instructions),'register_assignments':64,
        'cases':pairs,'nonhalt_blocks':normal_blocks,'halt_blocks':halt_blocks}
    # The four-instruction prologue does not depend on candidate behavior.
    preamble=0
    for h in (m.program(()),m.LOOP,m.program(((m.HALT,5,0,0),))):
        d=m.compile_diagonal(h)
        for y in list(range(50))+[10**30]:
            actual=iterate(d,m.State.initial(y),4)
            assert isinstance(actual,m.State) and actual.pc==4
            regs=dict(actual.registers)
            assert regs.get(3,0)==m.pair(y,y)
            assert all(regs.get(k,0)==0 for k in (4,5,8,100))
            preamble+=1
    checks['prologue']={'cases':preamble}
    # Branch table: prove by paper for v=0, v=1 and v>=2; test boundaries and huge naturals.
    suffix=0
    for n in range(7):
        h=m.program(tuple((m.INC,5,0,0) for _ in range(n)))
        d=m.compile_diagonal(h);trap=4+2*n;post=trap+1
        for v in [0,1,2,3,7,10**30]:
            s=canonical(post,{0:v,1:19,2:31,3:8})
            out=iterate(d,s,4)
            if v==1:
                assert isinstance(out,m.State) and out.pc==trap and m.step(d,out)==out
            else:assert out==m.Returned(0 if v==0 else 2)
            suffix+=1
    checks['postlude']={'cases':suffix}
    # Actual D1 traces, all prefixes checked by a second interpreter.
    const1=m.program(((m.SET,0,1,0),(m.HALT,0,0,0)))
    histories=[const1,
       m.program(((m.COPY,5,0,0),(m.DECJZ,5,4,2),(m.INC,6,0,0),(m.JUMP,1,0,0),(m.SET,2,1,0),(m.HALT,2,0,0))),
       m.program(((m.JUMP,2,0,0),(m.HALT,0,0,0),(m.SET,7,1,0),(m.HALT,7,0,0)))]
    for i,h in enumerate(histories):
        for x in (0,1,2,3):
            c=make_certificate(m.compile_diagonal(h),x,500)
            assert check_certificate(c)
            c['source_program_index']=i;certificate_rows.append(c)
    checks['nonreturn_trace_certificates']={'accepted':len(certificate_rows),'checked_with':'reference_step, not run status strings'}
    # T convention: absorbing return means at-or-before, not exact first halt.
    code=m.encode(const1)
    observed=[m.T(code,0,n,1) for n in range(6)]
    assert observed==[False,False,True,True,True,True]
    checks['T_convention']={'n_0_to_5':observed}
    # Control: a deterministic system can return and subsequently trap if return is not absorbing.
    control={'start':'returned','returned':'trap','trap':'trap'}
    trace=['start']
    for _ in range(4):trace.append(control[trace[-1]])
    assert 'returned' in trace and trace[-1]=='trap'
    checks['drop_terminal_absorption_countermodel']={'trace':trace,
       'conclusion':'eventually a nonterminal fixed point alone does not exclude an earlier return'}
    # Rejection of fabricated proofs and deliberate compiler mutations.
    mutations=[]
    valid=certificate_rows[0]
    tampered=json.loads(json.dumps(valid));tampered['trace'].insert(1,{'tag':'Returned','value':0})
    assert not check_certificate(tampered);mutations.append('inserted_return_in_trace')
    tampered=json.loads(json.dumps(valid));tampered['trace'][-1]['pc']+=1
    assert not check_certificate(tampered);mutations.append('wrong_final_pc')
    tampered=json.loads(json.dumps(valid));tampered['input']=2
    assert not check_certificate(tampered);mutations.append('changed_input')
    d=list(m.compile_diagonal(const1));trap=4+2*len(const1)
    d[trap]=(m.HALT,0,0,0)
    cert=make_certificate(m.program(d),0)
    assert not check_certificate(cert)
    assert m.run(m.program(d),0,100)['status']=='HALTED'
    mutations.append('trap_replaced_by_halt')
    h=m.program(((m.JUMP,99,0,0),));d=list(m.compile_diagonal(h));post=4+2*len(h)+1
    d[4]=(m.JUMP,post,0,0)
    assert m.run(m.program(d),0,100)['status']=='HALTED'
    assert m.run(m.compile_diagonal(h),0,100)['status']=='REPEATED_NONTERMINAL'
    mutations.append('invalid_jump_redirected_to_return_postlude')
    # Incorrect register shift loads outer scratch R2 rather than candidate R0.
    h=m.program(((m.HALT,0,0,0),));d=list(m.compile_diagonal(h));d[4]=(m.COPY,0,2,0)
    bad=iterate(m.program(d),m.State.initial(2),6)
    assert isinstance(bad,m.State) and dict(bad.registers)[0]!=m.pair(2,2)
    mutations.append('return_register_shift_plus2_instead_of_plus3')
    checks['mutations_rejected']={'count':len(mutations),'names':mutations}
    # A growing computation is not a fixed point and must remain unknown.
    grow=m.program(((m.INC,0,0,0),(m.JUMP,0,0,0)))
    c=make_certificate(grow,0,30)
    assert not check_certificate(c)
    assert m.run(grow,0,30)['status']=='FUEL_EXHAUSTED_UNKNOWN'
    checks['unknown_not_nonreturn_certificate']={'status':'FUEL_EXHAUSTED_UNKNOWN'}
    # Nonboolean policy can be altered without changing the two Bool-case obligations.
    alternate=[]
    for v in (0,1,2,3):
        h=m.program(((m.SET,0,v,0),(m.HALT,0,0,0)))
        d=list(m.compile_diagonal(h));trap=4+2*len(h);post=trap+1
        d[post+2]=(m.JUMP,trap,0,0)
        result=m.run(m.program(d),0,100)
        assert result['status']==('HALTED' if v==0 else 'REPEATED_NONTERMINAL')
        alternate.append({'source_output':v,'status':result['status']})
    checks['nonboolean_policy_not_necessary']={'alternative':'non-Bool output goes to trap','cases':alternate}
    return {'schema_version':'r025-targeted-audit/v1','status':'PASS_FINITE_SCOPE','checks':checks,
        'check_groups':len(checks),'certificates':certificate_rows,
        'original_r024_source_sha256':hashlib.sha256((ROOT/'scripts/research/r024_diagonal_machine.py').read_bytes()).hexdigest(),
        'proof_assistant':'NOT_RUN','original_compiler_modified':False,
        'claim_scope':'finite transition tests and checked concrete trap certificates; general simulation is paper only'}

def main():
    result=all_cases();out=ROOT/'artifacts/r025/TARGETED_RESULTS.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='certificates'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
