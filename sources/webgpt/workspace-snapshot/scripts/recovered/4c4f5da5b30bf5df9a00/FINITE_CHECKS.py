"""Finite checks for the rev7 provisional causal-equivalence proof.
Standard library only. This program is not a Lean/Agda kernel or a test of the
governance loading gate. General claims are proved separately in PROOF_NOTE.md.
"""
from itertools import product, permutations
from collections import Counter
import json

def partitions(n):
    if n == 0:
        yield ()
        return
    def extend(xs):
        if len(xs) == n:
            yield tuple(xs)
            return
        for value in range(max(xs)+2):
            yield from extend(xs+[value])
    yield from extend([0])

def preserves(f, labels):
    n=len(labels)
    return all(labels[i]!=labels[j] or labels[f[i]]==labels[f[j]]
               for i in range(n) for j in range(n))

def conjugate(e, f):
    inv=tuple(e.index(i) for i in range(len(e)))
    return tuple(e[f[inv[i]]] for i in range(len(e)))

def relation_equal_under(e, labels):
    return all((labels[i]==labels[j]) == (labels[e[i]]==labels[e[j]])
               for i in range(len(e)) for j in range(len(e)))

def encode(pair):
    a,b=pair
    return a//2, 2*b+a%2

def decode(pair):
    u,v=pair
    return 2*u+v%2, v//2

def double_current(pair):
    a,b=pair
    return 2*a,b

def run_checks():
    checks=[]
    V=tuple(product((0,1),repeat=2))
    labels=tuple(v[0] for v in V)
    maps=tuple(product(range(4),repeat=4))
    good=tuple(f for f in maps if preserves(f,labels))
    e_swap=(0,2,1,3)
    D=tuple(V.index((0,a)) for a,b in V)
    Dp=conjugate(e_swap,D)
    assert preserves(D,labels) and not preserves(Dp,labels)
    assert Dp == tuple(V.index((b,0)) for a,b in V)
    o_prime=tuple(v[1] for v in V)
    assert preserves(Dp,o_prime)
    checks.append({"id":"T01","status":"PASS","scope":"old swap and transported-observation control"})

    per_e=[]
    for e in permutations(range(4)):
        kept=sum(preserves(conjugate(e,f),labels) for f in good)
        structural=relation_equal_under(e,labels)
        assert (kept==len(good))==structural
        per_e.append({"e":list(e),"kept":kept,"bicausal":structural})
    histogram=dict(Counter(str(x["kept"]) for x in per_e))
    assert len(maps)==256 and len(good)==64 and histogram=={"64":8,"16":16}
    checks.append({"id":"T02","status":"PASS","scope":"all 24 Boolean permutations × all 64 causal maps",
                   "conjugations_checked":1536,"histogram":histogram})

    triangular=set()
    for c,h0,h1 in product((0,1),repeat=3):
        table=tuple(V.index((a^c,b^(h0 if a==0 else h1))) for a,b in V)
        triangular.add(table)
    actual={tuple(x["e"]) for x in per_e if x["bicausal"]}
    assert len(triangular)==8 and actual==triangular
    checks.append({"id":"T03","status":"PASS","scope":"exact triangular description of the eight permutations"})

    relation_pairs=0
    permutation_cases=0
    sizes=[]
    for n in range(1,5):
        ps=tuple(partitions(n))
        fs=tuple(product(range(n),repeat=n))
        end={p:frozenset(f for f in fs if preserves(f,p)) for p in ps}
        sizes.append({"n":n,"partitions":len(ps),"functions":len(fs)})
        for p in ps:
            for s in ps:
                inclusion=end[p] <= end[s]
                lemma = s in (tuple(range(n)),p,(0,)*n)
                assert inclusion == lemma
                relation_pairs+=1
            for e in permutations(range(n)):
                carried=frozenset(conjugate(e,f) for f in end[p])
                assert (carried<=end[p])==relation_equal_under(e,p)
                permutation_cases+=1
    assert relation_pairs==255 and permutation_cases==395
    checks.append({"id":"T04","status":"PASS","scope":"invariant-equivalence lemma for all n≤4",
                   "relation_pairs_checked":relation_pairs,"sizes":sizes})
    checks.append({"id":"T05","status":"PASS","scope":"one-way conjugation criterion for all n≤4",
                   "partition_permutation_cases":permutation_cases})

    for a,b in product(range(64),repeat=2):
        x=(a,b)
        assert decode(encode(x))==x
        assert encode(decode(x))==x
        assert encode(double_current(decode(x)))==(2*a+b%2,2*(b//2))
    checks.append({"id":"T06","status":"PASS","scope":"Nat model, each coordinate 0..63",
                   "points":4096,"inverse_equations_per_point":2,"conjugation_formula_per_point":1})

    for a,b,c in product(range(32),repeat=3):
        assert encode((a,b))[0]==encode((a,c))[0]
        assert double_current((a,b))[0]==double_current((a,c))[0]
    checks.append({"id":"T07","status":"PASS","scope":"forward-causality samples",
                   "input_pairs":32768,"maps_checked":2})

    x,y=(0,0),(0,1)
    assert x[0]==y[0]
    assert decode(x)[0]!=decode(y)[0]
    assert encode(double_current(decode(x)))[0]!=encode(double_current(decode(y)))[0]
    checks.append({"id":"T08","status":"PASS","scope":"exact witnesses refuting inverse and transported causality",
                   "x":x,"y":y,"inverse_images":[decode(x),decode(y)]})

    # This tests prefix preservation only, not every endomorphism conjugation on B^3.
    V3=tuple(product((0,1),repeat=3))
    num_preserving=0
    for e in permutations(range(8)):
        if all((V3[i][:t]==V3[j][:t])==(V3[e[i]][:t]==V3[e[j]][:t])
               for t in (1,2) for i in range(8) for j in range(8)):
            num_preserving+=1
    assert num_preserving==128
    checks.append({"id":"T09","status":"PASS","scope":"all 40320 permutations of three-bit strings; prefix relation only",
                   "prefix_preserving_permutations":num_preserving,
                   "all_function_transport_on_B3":"NOT_TESTED"})

    return {"schema_version":"hott-causal-equiv-finite/v1",
            "status":"PASS_FINITE_SCOPE","checks":checks,"boolean_permutations":per_e,
            "general_proof":"SEPARATE_PAPER_ARGUMENT",
            "proof_assistant":"NOT_RUN","novelty":"NOT_ESTABLISHED",
            "full_cognition_gate":"NOT_CERTIFIED"}

if __name__=="__main__":
    print(json.dumps(run_checks(),ensure_ascii=False,indent=2))
