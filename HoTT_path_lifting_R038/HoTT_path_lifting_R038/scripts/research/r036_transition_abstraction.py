#!/usr/bin/env python3
"""Exact finite transition analysis; NOT a HoTT kernel or unbounded simulator.

The default model terminates in two steps. Its existential quotient has a
checkable self-loop without a compatible concrete lift of a two-edge prefix.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import argparse,hashlib,itertools,json


def nat(x: object) -> bool:
    return type(x) is int and x >= 0


@dataclass(frozen=True)
class System:
    size: int
    edges: frozenset[tuple[int, int]]
    initial: int
    done: frozenset[int]

    def __post_init__(self) -> None:
        if not nat(self.size) or self.size < 1:
            raise ValueError('nonempty explicit finite domain required')
        if not nat(self.initial) or self.initial >= self.size:
            raise ValueError('invalid initial state')
        if not isinstance(self.edges, frozenset) or not isinstance(self.done, frozenset):
            raise TypeError('immutable explicit edges and done set required')
        for x in self.done:
            if not nat(x) or x >= self.size: raise ValueError('invalid done state')
        for e in self.edges:
            if type(e) is not tuple or len(e) != 2: raise ValueError('invalid edge')
            if any(not nat(x) or x >= self.size for x in e): raise ValueError('edge endpoint out of range')
            if e[0] in self.done: raise ValueError('Done is terminal, not an absorbing execution edge')

    def successors(self, x: int) -> tuple[int,...]:
        return tuple(sorted(y for u,y in self.edges if u == x))

    def reachable(self) -> frozenset[int]:
        seen={self.initial};work=[self.initial]
        while work:
            for y in self.successors(work.pop()):
                if y not in seen: seen.add(y);work.append(y)
        return frozenset(seen)

    def cycle(self, reachable_only: bool = True) -> tuple[int,...] | None:
        """Return a finite cycle certificate (first == last), not a timeout guess."""
        allowed=self.reachable() if reachable_only else frozenset(range(self.size))
        grey:list[int]=[];black:set[int]=set()
        def dfs(x:int):
            if x in grey:
                i=grey.index(x);return tuple(grey[i:]+[x])
            if x in black:return None
            grey.append(x)
            for y in self.successors(x):
                if y in allowed:
                    result=dfs(y)
                    if result is not None:return result
            grey.pop();black.add(x);return None
        for x in sorted(allowed):
            result=dfs(x)
            if result is not None:return result
        return None

    def check_cycle(self, cycle:tuple[int,...]) -> bool:
        return (len(cycle)>=2 and cycle[0]==cycle[-1]
                and all((x,y) in self.edges for x,y in zip(cycle,cycle[1:])))

    def rank(self) -> tuple[int,...] | None:
        """Longest finite path length, only when the WHOLE graph is a DAG."""
        if self.cycle(False) is not None:return None
        cache:dict[int,int]={}
        def go(x:int)->int:
            if x not in cache:cache[x]=max((go(y)+1 for y in self.successors(x)),default=0)
            return cache[x]
        return tuple(go(x) for x in range(self.size))

    def all_runs_complete(self) -> bool:
        reachable=self.reachable()
        return (self.cycle() is None and all(x in self.done or self.successors(x) for x in reachable))

    def traces(self, max_edges:int) -> tuple[tuple[int,...],...]:
        if not nat(max_edges):raise ValueError('nonnegative finite bound required')
        traces=[(self.initial,)]
        for _ in range(max_edges):
            traces += [p+(y,) for p in tuple(traces) if len(p)==_+1 for y in self.successors(p[-1])]
        return tuple(traces)


@dataclass(frozen=True)
class Abstraction:
    source: System
    alpha: tuple[int,...]

    def __post_init__(self)->None:
        if type(self.alpha) is not tuple or len(self.alpha)!=self.source.size:
            raise ValueError('one label per state required')
        if any(not nat(x) for x in self.alpha):raise ValueError('labels must be natural numbers')
        if set(self.alpha)!=set(range(max(self.alpha)+1)):
            raise ValueError('labels must cover a contiguous quotient domain')
        for x,y in itertools.product(range(self.source.size),repeat=2):
            if self.alpha[x]==self.alpha[y] and ((x in self.source.done)!=(y in self.source.done)):
                raise ValueError('Done observability may not be erased in this experiment')

    @property
    def target(self)->System:
        return System(max(self.alpha)+1,
            frozenset((self.alpha[x],self.alpha[y]) for x,y in self.source.edges),
            self.alpha[self.source.initial],frozenset(self.alpha[x] for x in self.source.done))

    def edge_witnesses(self,u:int,v:int)->tuple[tuple[int,int],...]:
        return tuple(sorted((x,y) for x,y in self.source.edges if (self.alpha[x],self.alpha[y])==(u,v)))

    def abstract_walk_valid(self,path:tuple[int,...])->bool:
        return bool(path) and path[0]==self.target.initial and all((x,y) in self.target.edges for x,y in zip(path,path[1:]))

    def lift_sets(self,path:tuple[int,...])->tuple[frozenset[int],...]:
        if not self.abstract_walk_valid(path):raise ValueError('not an abstract path from initial observation')
        current=frozenset([self.source.initial]);result=[current]
        for label in path[1:]:
            current=frozenset(y for x in current for y in self.source.successors(x) if self.alpha[y]==label)
            result.append(current)
        return tuple(result)

    def backward_failures(self)->tuple[tuple[int,int],...]:
        """Missing uniform one-step lifting from an ACTUAL current representative."""
        return tuple((s,v) for s in range(self.source.size)
            for v in self.target.successors(self.alpha[s])
            if not any(self.alpha[t]==v for t in self.source.successors(s)))

    def factor_rank(self,rank:tuple[int,...])->tuple[int,...] | None:
        if len(rank)!=self.source.size or any(not nat(r) for r in rank):raise ValueError('invalid rank')
        if not all(rank[y]<rank[x] for x,y in self.source.edges):raise ValueError('not a source ranking')
        out=[]
        for u in range(self.target.size):
            values={rank[s] for s in range(self.source.size) if self.alpha[s]==u}
            if len(values)!=1:return None
            out.append(next(iter(values)))
        return tuple(out)


def partitions(n:int):
    """Restricted growth strings: each set partition exactly once."""
    if n<1:raise ValueError('positive size')
    def go(a):
        if len(a)==n:yield a;return
        for x in range(max(a)+2):yield from go(a+(x,))
    yield from go((0,))


def specimen()->Abstraction:
    return Abstraction(System(3,frozenset([(0,1),(1,2)]),0,frozenset([2])),(0,0,1))


def report()->dict:
    a=specimen();src=a.source;dst=a.target;cycle=dst.cycle()
    assert cycle is not None and dst.check_cycle(cycle)
    abstract_prefix=(0,0,0)
    identity=Abstraction(src,(0,1,2))
    classified=[]
    for n in range(2,7):
        system=System(n,frozenset((i,i+1) for i in range(n-1)),0,frozenset([n-1]))
        rows=[]
        for labels in partitions(n):
            try:b=Abstraction(system,labels)
            except ValueError:continue
            ranking=b.target.rank()
            if ranking is not None:
                lifted=tuple(ranking[labels[s]] for s in range(n))
                assert all(lifted[y]<lifted[x] for x,y in system.edges)
            rows.append({'labels':labels,'all_runs_complete':b.target.all_runs_complete(),
                         'cycle':b.target.cycle(),'source_rank_factors':b.factor_rank(system.rank()) is not None})
        classified.append({'chain_states':n,'Done_preserving_partitions':len(rows),
                           'terminating_quotients':sum(r['all_runs_complete'] for r in rows),'rows':rows})
    return {'kind':'FINITE_MODEL_AND_CERTIFICATE_CHECK_NOT_HOTT_KERNEL',
        'source':{'states':['a','b','done'],'edges':sorted(src.edges),'initial':src.initial,'done':sorted(src.done),
                  'strict_rank':src.rank(),'all_runs_complete':src.all_runs_complete(),
                  'all_prefixes':src.traces(3),'exact_longest_run_edges':2},
        'quotient':{'alpha':a.alpha,'labels':['working','Done'],'edges':sorted(dst.edges),'done':sorted(dst.done),
                    'edge_witnesses':{f'{u}->{v}':a.edge_witnesses(u,v) for u,v in sorted(dst.edges)},
                    'all_runs_complete':dst.all_runs_complete(),'reachable_cycle_certificate':cycle,
                    'infinite_run_definition':'beta(n)=working for every natural n; reuse the proved abstract edge, not a concrete run'},
        'finite_obstruction':{'abstract_prefix':abstract_prefix,'abstract_valid':True,
                              'compatible_concrete_representatives':[sorted(x) for x in a.lift_sets(abstract_prefix)],
                              'independent_edge_witnesses_accept':True,'compatible_full_lift_exists':False},
        'missing_back_conditions':a.backward_failures(),
        'positive_control':{'alpha':identity.alpha,'rank':identity.target.rank(),'all_runs_complete':identity.target.all_runs_complete(),
                            'valid_trace':(0,1,2),'lift':[sorted(x) for x in identity.lift_sets((0,1,2))]},
        'chain_partition_classification':classified,
        'scope':{'finite_samples_do_not_prove_general_theorems':True,'same_concrete_domain':True,
                 'Done_preserved':True,'fairness_assumption':False,'LEM_or_oracle':False,'HoTT_core_failure_claim':False,
                 'native_formal_validation':'NOT_RUN','novelty':'KNOWN_ABSTRACTION_MECHANISM; NEW_PROJECT_INSTANTIATION'}}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    result=report();result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['source','quotient','finite_obstruction','missing_back_conditions','positive_control']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
