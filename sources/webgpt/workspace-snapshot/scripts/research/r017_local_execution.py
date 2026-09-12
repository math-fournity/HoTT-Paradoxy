#!/usr/bin/env python3
"""R017: current-input certificates versus all-input totality.

A small deterministic counter-machine syntax plus a bounded-probe wrapper.
Every simulation is fuel bounded. Exhausting fuel is UNKNOWN, never a proof of
nontermination. An explicitly replayed non-halting self-loop is separate evidence.
This is an operational test program, not a HoTT proof assistant or a totality oracle.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path
from typing import Literal

Op = Literal['HALT', 'INC', 'DECJZ', 'JUMP']
Phase = Literal['branch', 'probe', 'spin', 'done']

def natural(value: object, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f'{label} must be a natural number, not bool')
    return value

@dataclass(frozen=True)
class Instruction:
    op: Op
    reg: int = 0
    target: int = 0
    zero: int = 0

@dataclass(frozen=True)
class Machine:
    registers: int
    code: tuple[Instruction, ...]

    def __post_init__(self) -> None:
        natural(self.registers, 'registers')
        if self.registers < 1 or not self.code:
            raise ValueError('Need registers and nonempty code')
        for i in self.code:
            if i.op not in ('HALT','INC','DECJZ','JUMP'):
                raise ValueError('Unknown instruction')
            natural(i.reg, 'register'); natural(i.target, 'target'); natural(i.zero, 'zero')
            if i.reg >= self.registers:
                raise ValueError('Register out of range')
            if i.op in ('INC','JUMP','DECJZ') and i.target >= len(self.code):
                raise ValueError('Jump target out of range')
            if i.op == 'DECJZ' and i.zero >= len(self.code):
                raise ValueError('Zero target out of range')

@dataclass(frozen=True)
class Config:
    pc: int
    registers: tuple[int, ...]
    halted: bool = False
    output: int | None = None

@dataclass(frozen=True)
class BaseRun:
    status: str
    transitions: int
    trace: tuple[Config, ...]

    @property
    def output(self) -> int | None:
        return self.trace[-1].output


def initial(p: Machine, x: int) -> Config:
    natural(x,'input')
    return Config(0, (x,) + (0,)*(p.registers-1))


def well_config(p: Machine, c: Config) -> bool:
    return (type(c.pc) is int and 0 <= c.pc < len(p.code)
            and len(c.registers)==p.registers
            and all(type(x) is int and x>=0 for x in c.registers)
            and type(c.halted) is bool
            and ((c.halted and type(c.output) is int and c.output>=0)
                 or (not c.halted and c.output is None)))


def step(p: Machine, c: Config) -> Config:
    if not well_config(p,c):
        raise ValueError('Invalid configuration')
    if c.halted:
        return c  # absorbing terminal state; allows padded termination witnesses
    ins=p.code[c.pc]; regs=list(c.registers)
    if ins.op=='HALT':
        return Config(c.pc,c.registers,True,regs[ins.reg])
    if ins.op=='JUMP':
        return Config(ins.target,c.registers)
    if ins.op=='INC':
        regs[ins.reg]+=1
        return Config(ins.target,tuple(regs))
    if regs[ins.reg]==0:
        return Config(ins.zero,c.registers)
    regs[ins.reg]-=1
    return Config(ins.target,tuple(regs))


def run_base(p: Machine, x: int, fuel: int) -> BaseRun:
    natural(fuel,'fuel')
    if fuel>100_000:
        raise ValueError('Execution safety bound exceeded')
    c=initial(p,x); trace=[c]
    for _ in range(fuel):
        c=step(p,c);trace.append(c)
        if c.halted:
            return BaseRun('HALTED',len(trace)-1,tuple(trace))
    return BaseRun('FUEL_EXHAUSTED',fuel,tuple(trace))


def check_certificate(p: Machine, x: int, trace: tuple[Config,...]) -> bool:
    """Check finite computation evidence; never try to discover global totality."""
    try:
        return (bool(trace) and trace[0]==initial(p,x)
                and all(well_config(p,c) for c in trace)
                and all(step(p,a)==b for a,b in zip(trace,trace[1:]))
                and trace[-1].halted)
    except (ValueError,TypeError,AttributeError):
        return False


def output_from_certificate(p: Machine,x: int,trace: tuple[Config,...]) -> int:
    if not check_certificate(p,x,trace):
        raise ValueError('Invalid current-input execution certificate')
    assert trace[-1].output is not None
    return trace[-1].output

@dataclass(frozen=True)
class Wrapper:
    base: Machine
    fixed_input: int

    def __post_init__(self):
        natural(self.fixed_input,'fixed input')

@dataclass(frozen=True)
class WrapperState:
    phase: Phase
    remaining: int
    inner: Config | None
    output: int | None = None

@dataclass(frozen=True)
class WrapperRun:
    status: str
    transitions: int
    machine_steps: int
    trace: tuple[WrapperState,...]

    @property
    def output(self):
        return self.trace[-1].output


def wrapper_initial(n: int) -> WrapperState:
    natural(n,'input')
    return WrapperState('branch',n,None)


def wrapper_step(p: Wrapper,n: int,c: WrapperState) -> WrapperState:
    natural(n,'input'); natural(c.remaining,'remaining')
    if c.phase=='branch':
        if c != wrapper_initial(n):
            raise ValueError('Malformed entry')
        if n==0:
            return WrapperState('done',0,None,0)
        return WrapperState('probe',n,initial(p.base,p.fixed_input))
    if c.phase in ('done','spin'):
        if c.phase=='done' and c.output!=0:
            raise ValueError('Wrong wrapper result')
        if c.phase=='spin' and (c.output is not None or c.inner is None or not c.inner.halted):
            raise ValueError('Malformed spin evidence')
        return c
    if c.phase!='probe' or c.inner is None or c.output is not None:
        raise ValueError('Malformed probe')
    if not well_config(p.base,c.inner):
        raise ValueError('Malformed base configuration')
    if c.inner.halted:
        return WrapperState('spin',c.remaining,c.inner)
    if c.remaining==0:
        return WrapperState('done',0,c.inner,0)
    return WrapperState('probe',c.remaining-1,step(p.base,c.inner))


def run_wrapper(p: Wrapper,n: int,fuel: int) -> WrapperRun:
    natural(fuel,'fuel')
    if fuel>100_000:
        raise ValueError('Execution safety bound exceeded')
    c=wrapper_initial(n);trace=[c];count=0
    for _ in range(fuel):
        if c.phase=='probe' and c.inner is not None and not c.inner.halted and c.remaining>0:
            count+=1
        c=wrapper_step(p,n,c);trace.append(c)
        if c.phase=='done':
            return WrapperRun('HALTED',len(trace)-1,count,tuple(trace))
    # No universal divergence claim from finite observation.
    return WrapperRun('FUEL_EXHAUSTED',fuel,count,tuple(trace))


def check_wrapper_prefix(p: Wrapper,n: int,trace: tuple[WrapperState,...]) -> bool:
    try:
        return (bool(trace) and trace[0]==wrapper_initial(n)
                and all(wrapper_step(p,n,a)==b for a,b in zip(trace,trace[1:])))
    except (ValueError,AttributeError,TypeError):
        return False


def check_wrapper_certificate(p: Wrapper,n: int,trace: tuple[WrapperState,...]) -> bool:
    return check_wrapper_prefix(p,n,trace) and trace[-1].phase=='done' and trace[-1].output==0


def spin_certificate(p: Wrapper,n: int,trace: tuple[WrapperState,...]) -> bool:
    """Check a reachable nonterminal fixed configuration, not merely a timeout."""
    return (check_wrapper_prefix(p,n,trace) and trace[-1].phase=='spin'
            and wrapper_step(p,n,trace[-1])==trace[-1])


def local_zero_certificate(p: Wrapper) -> tuple[WrapperState,...]:
    start=wrapper_initial(0)
    return (start,wrapper_step(p,0,start))


def delayed_halt(halt_after: int) -> Machine:
    natural(halt_after,'halt time')
    if halt_after<1:
        raise ValueError('HALT is itself one transition')
    return Machine(1,tuple(Instruction('JUMP',target=i+1) for i in range(halt_after-1))+(Instruction('HALT'),))


def two_instruction_machines() -> tuple[Machine,...]:
    ops=[Instruction('HALT',reg=r) for r in range(2)]
    ops += [Instruction('JUMP',target=j) for j in range(2)]
    ops += [Instruction('INC',reg=r,target=j) for r in range(2) for j in range(2)]
    ops += [Instruction('DECJZ',reg=r,target=j,zero=k) for r in range(2) for j in range(2) for k in range(2)]
    return tuple(Machine(2,tuple(code)) for code in product(ops,repeat=2))


def demonstrate() -> dict:
    machines=two_instruction_machines()
    counts={'base_programs':len(machines),'fixed_inputs':4,'wrapper_inputs':9,
            'wrapper_runs':0,'local_zero_certificates':0,'halted_positive':0,
            'reachable_spins':0,'base_trace_certificates':0}
    for machine in machines:
        for fixed in range(4):
            p=Wrapper(machine,fixed)
            z=local_zero_certificate(p)
            assert check_wrapper_certificate(p,0,z)
            assert len(z)==2
            counts['local_zero_certificates']+=1
            for n in range(9):
                result=run_wrapper(p,n,n+2)
                counts['wrapper_runs']+=1
                assert check_wrapper_prefix(p,n,result.trace)
                if n==0:
                    assert result.status=='HALTED' and result.transitions==1 and result.machine_steps==0
                    continue
                bounded=run_base(machine,fixed,n)
                if bounded.status=='HALTED':
                    assert check_certificate(machine,fixed,bounded.trace)
                    counts['base_trace_certificates']+=1
                    assert spin_certificate(p,n,result.trace)
                    assert not check_wrapper_certificate(p,n,result.trace)
                    counts['reachable_spins']+=1
                else:
                    assert check_wrapper_certificate(p,n,result.trace)
                    assert result.transitions==n+2 and result.machine_steps==n
                    counts['halted_positive']+=1
    assert counts['wrapper_runs']==256*4*9
    prefix_counterexamples=[]
    for k in range(9):
        p=Wrapper(delayed_halt(k+1),0)
        for n in range(k+1):
            assert check_wrapper_certificate(p,n,run_wrapper(p,n,n+2).trace)
        witness=run_wrapper(p,k+1,k+3)
        assert spin_certificate(p,k+1,witness.trace)
        prefix_counterexamples.append({'tested_inputs':[0,k],'all_tests_terminate':True,
                                       'next_input':k+1,'next_input_has_reachable_nonterminal_fixed_state':True})
    examples={
        'halts_immediately':Wrapper(Machine(1,(Instruction('HALT'),)),0),
        'nonterminating_increment':Wrapper(Machine(1,(Instruction('INC',target=0),)),0),
        'halts_after_four_steps':Wrapper(delayed_halt(4),0),
    }
    sample=[]
    for name,p in examples.items():
        for n in (0,1,4):
            run=run_wrapper(p,n,n+3)
            sample.append({'name':name,'base':asdict(p),'wrapper_input':n,'result':asdict(run),
                           'local_certificate':check_wrapper_certificate(p,n,run.trace),
                           'separate_spin_certificate':spin_certificate(p,n,run.trace)})
    return {'schema_version':'hott-r017-results/v1','status':'PASS_FINITE_OPERATIONAL_SCOPE',
            'counts':counts,'finite_prefix_counterexamples':prefix_counterexamples,'examples':sample,
            'checks':['local_zero_short_circuit','finite_trace_verifier','positive_input_bounded_probe',
                      'explicit_nonterminal_cycle','finite_prefix_does_not_certify_totality','whole_source_available'],
            'infinite_theorems':'PAPER_ARGUMENTS_ONLY; enumeration is not a proof of undecidability',
            'machine_universality':'NOT_PROVED_BY_THIS_PROGRAM; metatheorem separately assumes effective universal programming model',
            'proof_assistant':'NOT_RUN','no_totality_oracle':True}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    result=demonstrate()
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':result['counts'],
                      'prefix_counterexamples':len(result['finite_prefix_counterexamples']),
                      'full_result':str(a.output)},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
