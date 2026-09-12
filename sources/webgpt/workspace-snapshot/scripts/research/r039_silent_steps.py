#!/usr/bin/env python3
"""Exact finite-state checks for delay relations and divergence-blind weak bisimulation.
Not a HoTT kernel. Cyclic certificates prove a post-fixed relation in a declared
finite graph; no execution timeout is interpreted as divergence.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from collections import deque
from itertools import product
from typing import Mapping, Iterable
import argparse, json

@dataclass(frozen=True)
class Now:
    value: int
    def __post_init__(self):
        if type(self.value) is not int: raise TypeError('Return label must be an integer, not bool')
@dataclass(frozen=True)
class Later:
    target: str
    def __post_init__(self):
        if type(self.target) is not str: raise TypeError('Target must be a state name')
Node = Now | Later
Pair = tuple[str,str]

class DelayGraph:
    def __init__(self, nodes: Mapping[str, Node]):
        self.nodes=dict(nodes)
        if not self.nodes: raise ValueError('Empty graph')
        for k,v in self.nodes.items():
            if type(k) is not str or type(v) not in (Now,Later): raise TypeError('Invalid state syntax')
            if isinstance(v,Later) and v.target not in self.nodes: raise ValueError('Missing successor')
    def outcome(self,start: str) -> dict:
        if start not in self.nodes: raise ValueError('Unknown state')
        seen={}; path=[]; s=start
        while s not in seen:
            seen[s]=len(path);path.append(s);node=self.nodes[s]
            if isinstance(node,Now):
                return dict(kind='RETURN',value=node.value,delay_steps=len(path)-1,path=path)
            s=node.target
        return dict(kind='DIVERGENCE_LASSO',prefix=path[:seen[s]],cycle=path[seen[s]:],repeated_state=s)
    def operator(self,relation: set[Pair],mode: str) -> set[Pair]:
        if mode not in ('bad','good'): raise ValueError('Unknown relation')
        result=set(); outcomes={x:self.outcome(x) for x in self.nodes}
        for p,q in product(self.nodes,repeat=2):
            a,b=self.nodes[p],self.nodes[q]
            if mode=='bad':
                holds=(isinstance(a,Now) and isinstance(b,Now) and a.value==b.value)
                holds=holds or (isinstance(a,Later) and (a.target,q) in relation)
                holds=holds or (isinstance(b,Later) and (p,b.target) in relation)
            else:
                op,oq=outcomes[p],outcomes[q]
                holds=(op['kind']==oq['kind']=='RETURN' and op['value']==oq['value'])
                holds=holds or (isinstance(a,Later) and isinstance(b,Later) and (a.target,b.target) in relation)
            if holds: result.add((p,q))
        return result
    def fixed_point(self,mode: str, greatest: bool=True) -> tuple[set[Pair],int]:
        r=set(product(self.nodes,repeat=2)) if greatest else set(); rounds=0
        while True:
            nxt=self.operator(r,mode);rounds+=1
            if nxt==r: return r,rounds
            if greatest and not nxt<=r: raise AssertionError('Not descending')
            if not greatest and not r<=nxt: raise AssertionError('Not ascending')
            r=nxt
    def postfixed(self,relation: Iterable[Pair],mode: str) -> bool:
        r=set(relation)
        if not r<=set(product(self.nodes,repeat=2)):return False
        return r<=self.operator(r,mode)

def equiv_closure(states: Iterable[str], relation: set[Pair]) -> set[Pair]:
    ss=tuple(states); r=set(relation)|{(q,p) for p,q in relation}|{(p,p) for p in ss}
    for k in ss:
        for i in ss:
            for j in ss:
                if (i,k) in r and (k,j) in r:r.add((i,j))
    return r

def respects(relation: set[Pair], values: Mapping[str,int]) -> bool:
    return all(values[p]==values[q] for p,q in relation if p in values and q in values)

def check_credit_certificate(g: DelayGraph, cert: dict, root: str) -> bool:
    """Finite graph of indexed bisimulation obligations. Cycles allowed only by rules.
    Both: consumes a later on each side, may reset a finite credit.
    Left/right: consumes one later and STRICTLY decrements the credit by one.
    """
    if root not in cert:return False
    pending=[root]; visited=set()
    while pending:
        name=pending.pop()
        if name in visited:continue
        visited.add(name);n=cert.get(name)
        if not isinstance(n,dict) or not {'pair','credit','rule'}<=n.keys():return False
        pair=n['pair'];k=n['credit']
        if not isinstance(pair,(tuple,list)) or len(pair)!=2 or type(k) is not int or k<0:return False
        p,q=pair
        if p not in g.nodes or q not in g.nodes:return False
        a,b=g.nodes[p],g.nodes[q];rule=n['rule']
        if rule=='now':
            if not (isinstance(a,Now) and isinstance(b,Now) and a.value==b.value):return False
            if 'next' in n:return False
            continue
        child=cert.get(n.get('next'))
        if not isinstance(child,dict) or 'pair' not in child or 'credit' not in child:return False
        cp=tuple(child['pair']);ck=child['credit']
        if type(ck) is not int or ck<0:return False
        if rule=='both':
            if not (isinstance(a,Later) and isinstance(b,Later) and cp==(a.target,b.target)):return False
        elif rule=='left':
            if not (isinstance(a,Later) and cp==(a.target,q) and k==ck+1):return False
        elif rule=='right':
            if not (isinstance(b,Later) and cp==(p,b.target) and k==ck+1):return False
        else:return False
        pending.append(n['next'])
    return True

class LTS:
    def __init__(self,states: Iterable[str],edges: Iterable[tuple[str,str,str]]):
        self.states=tuple(states);self.edges=tuple(edges)
        if len(set(self.states))!=len(self.states):raise ValueError('Duplicate state')
        for s,l,t in self.edges:
            if s not in self.states or t not in self.states or type(l) is not str:raise ValueError('Invalid edge')
    def out(self,s):return [(l,t) for a,l,t in self.edges if a==s]
    def tau_closure(self,s):
        reach={s};todo=[s]
        while todo:
            p=todo.pop()
            for l,q in self.out(p):
                if l=='tau' and q not in reach:reach.add(q);todo.append(q)
        return reach
    def weak_targets(self,s,label):
        if label=='tau':return self.tau_closure(s)
        return {v for p in self.tau_closure(s) for l,q in self.out(p) if l==label for v in self.tau_closure(q)}
    def weak_condition(self,p,q,r):
        return all(any((t,u) in r for u in self.weak_targets(q,l)) for l,t in self.out(p))
    def weak_bisim(self,preserve_divergence=False):
        r=set(product(self.states,repeat=2));div={s:self.tau_diverges(s) for s in self.states}
        if preserve_divergence:r={(p,q) for p,q in r if div[p]==div[q]}
        rounds=0
        while True:
            nr={(p,q) for p,q in r if self.weak_condition(p,q,r) and self.weak_condition(q,p,{(b,a) for a,b in r})}
            rounds+=1
            if nr==r:return r,rounds
            r=nr
    def tau_diverges(self,s):
        def visit(q,grey,black):
            if q in grey:return True
            if q in black:return False
            grey.add(q)
            for l,t in self.out(q):
                if l=='tau' and visit(t,grey,black):return True
            grey.remove(q);black.add(q);return False
        return visit(s,set(),set())
    def may_done(self,s):return bool(self.weak_targets(s,'done'))
    def must_done_states(self):
        """All maximal paths eventually emit done, with no fairness assumption.
        A deadlock before done is failure. Done is a visible edge, not stuttering.
        """
        r=set()
        while True:
            nr=r|{s for s in self.states if self.out(s) and all(l=='done' or t in r for l,t in self.out(s))}
            if nr==r:return r
            r=nr

def minimal_delay():return DelayGraph({'ret0':Now(0),'ret1':Now(1),'spin':Later('spin'),'wait0':Later('ret0'),'wait1':Later('ret1'),'two0':Later('wait0')})
def completion_lts():return LTS(['fast','retry','end','wait'],[('fast','done','end'),('retry','tau','retry'),('retry','done','end'),('wait','tau','fast')])
def results():
    g=minimal_delay();bad,br=g.fixed_point('bad');good,gr=g.fixed_point('good');least,lr=g.fixed_point('bad',False)
    lts=completion_lts();weak,wr=lts.weak_bisim();sensitive,_=lts.weak_bisim(True)
    strong={('ret0','ret0'):True}
    out=dict(scope='EXACT_FINITE_MODELS_NOT_HOTT_KERNEL',
      delay=dict(nodes={k:({'now':v.value} if isinstance(v,Now) else {'later':v.target}) for k,v in g.nodes.items()},outcomes={p:g.outcome(p) for p in g.nodes},
        bad_pairs=[list(p) for p in sorted(bad)],good_pairs=[list(p) for p in sorted(good)],iterations=dict(bad=br,good=gr,least_bad=lr),
        bad_spin_ret0=('spin','ret0') in bad,bad_spin_ret1=('spin','ret1') in bad,bad_ret0_ret1=('ret0','ret1') in bad,
        bad_transitivity_counterexample=['ret0','spin','ret1'],least_rejects_spin_ret0=('spin','ret0') not in least,
        good_rejects_spin_ret0=('spin','ret0') not in good,good_identifies_finite_delay=('wait0','ret0') in good,
        bad_equivalence_closure_merges_values=('ret0','ret1') in equiv_closure(g.nodes,bad)),
      nondeterminism=dict(edges=lts.edges,weak_pairs=[list(p) for p in sorted(weak)],weak_rounds=wr,fast_retry_weak=('fast','retry') in weak,
        fast_retry_divergence_preserving=('fast','retry') in sensitive,
        may={s:lts.may_done(s) for s in lts.states},must={s:s in lts.must_done_states() for s in lts.states},tau_divergence={s:lts.tau_diverges(s) for s in lts.states},fairness_assumed=False),
      general_proofs='PAPER_ONLY',native_kernel='NOT_RUN',HoTT_core_error=False,novelty='KNOWN_CORE_NOT_CLAIMED')
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    a.output.parent.mkdir(parents=True,exist_ok=True);r=results();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
