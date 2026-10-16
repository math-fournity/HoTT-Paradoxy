#!/usr/bin/env python3
"""R030: finite, explicitly staged reflection language. NOT a HoTT kernel.

Code=Nat. Nodes use Cantor pairs; subexpression codes strictly decrease.
An old_eval(j,a,b) node is admissible at stage k only if j<k.
Raw evaluators return False for invalid codes BY DEFINITION; this default is
never presented as certified semantics of an admissible program.
The paper termination argument is lexicographic in (stage, code), not the
finite tests and not a claim about unlimited Python stack/memory resources.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from math import isqrt
from typing import Optional


def natural(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError('Expected an actual nonnegative integer')
    return n


def pair(a: int, b: int) -> int:
    natural(a); natural(b)
    return (a+b)*(a+b+1)//2+b


def unpair(n: int) -> tuple[int, int]:
    natural(n)
    w=(isqrt(8*n+1)-1)//2
    b=n-w*(w+1)//2
    return w-b,b


def node(tag: int, payload: int=0) -> int:
    return 1+pair(tag,payload)


def nat_lit(n: int) -> int:
    return natural(n)+1


VAR=0
FALSE=node(0)
TRUE=node(1)

def eq(a: int,b: int) -> int: return node(2,pair(a,b))
def neg(a: int) -> int: return node(3,natural(a))
def conj(a: int,b: int) -> int: return node(4,pair(a,b))
def old_eval(j: int,a: int,b: int) -> int:
    return node(5,pair(natural(j),pair(a,b)))

def nat_value(code: int,x: int) -> int:
    natural(code);natural(x)
    return x if code==VAR else code-1


@lru_cache(maxsize=100000, typed=True)
def well(stage: int,code: int) -> bool:
    natural(stage);natural(code)
    if code==0:return False
    tag,payload=unpair(code-1)
    if tag in (0,1):return payload==0
    if tag==2:return True
    if tag==3:return well(stage,payload)
    if tag==4:
        a,b=unpair(payload)
        return well(stage,a) and well(stage,b)
    if tag==5:
        j,_=unpair(payload)
        return j<stage
    return False


@lru_cache(maxsize=100000, typed=True)
def raw_eval(stage: int,code: int,x: int) -> bool:
    natural(stage);natural(code);natural(x)
    if not well(stage,code):return False
    tag,payload=unpair(code-1)
    if tag==0:return False
    if tag==1:return True
    if tag==2:
        a,b=unpair(payload)
        return nat_value(a,x)==nat_value(b,x)
    if tag==3:return not raw_eval(stage,payload,x)
    if tag==4:
        a,b=unpair(payload)
        av,bv=raw_eval(stage,a,x),raw_eval(stage,b,x)
        return av and bv
    j,args=unpair(payload);a,b=unpair(args)
    return raw_eval(j,nat_value(a,x),nat_value(b,x))


def checked_eval(stage: int,code: int,x: int) -> dict:
    if not well(stage,code):
        return {'status':'REJECTED_NOT_IN_LANGUAGE','value':None}
    return {'status':'RETURNED','value':raw_eval(stage,code,x)}


def diagonal_code(j: int) -> int:
    return neg(old_eval(j,VAR,VAR))


@dataclass(frozen=True)
class Config:
    """Deliberately non-staged current-evaluator experiment, not safe language."""
    code: int
    input: int
    pending_not: int=0
    result: Optional[bool]=None
    rejected: bool=False


def unstratified_step(q: Config) -> Config:
    """Exact partial-language step: constants, not, and a current-eval call.
    old_eval(0,...) is REINTERPRETED as current-eval only in this experiment.
    This is an explicit semantic change, never claimed to be a HoTT rule.
    """
    if q.result is not None or q.rejected:return q
    if q.code==0:return Config(q.code,q.input,q.pending_not,rejected=True)
    tag,payload=unpair(q.code-1)
    if tag in (0,1) and payload==0:
        b=(tag==1) != bool(q.pending_not%2)
        return Config(q.code,q.input,q.pending_not,result=b)
    if tag==3:return Config(payload,q.input,q.pending_not+1)
    if tag==5:
        j,args=unpair(payload)
        if j==0:
            a,b=unpair(args)
            return Config(nat_value(a,q.input),nat_value(b,q.input),q.pending_not)
    return Config(q.code,q.input,q.pending_not,rejected=True)


def trace(steps: int) -> list[dict]:
    natural(steps)
    d=diagonal_code(0);q=Config(d,d);out=[]
    for t in range(steps+1):
        out.append({'time':t,'code':q.code,'input':q.input,'pending_not':q.pending_not,'result':q.result,'rejected':q.rejected})
        q=unstratified_step(q)
    return out
