"""Finite sanity checks for DONE-OBS/v1, not an unbounded/HoTT proof.
Pure Python stdlib. All executed samples have finite certified bounds.
The monitor returns on an event or observable DONE. No previous project code imported.
"""
from itertools import product
import json

DONE, IDLE = 2, 3

def words_at_most(n):
    for k in range(n+1):
        yield from product((0, 1), repeat=k)

def marked(w, i):
    if i < len(w):
        return w[i]
    return DONE if i == len(w) else IDLE

def erased(w, i):
    return w[i] if i < len(w) else 0

def q(w):
    return int(1 in w)

def trim(w):
    k=len(w)
    while k and w[k-1] == 0:
        k-=1
    return w[:k]

def monitor_with_done(oracle):
    # No provided bound or length: on genuinely finite marked traces,
    # this loop stops because DONE is part of the actual observation.
    i=0
    while True:
        v=oracle(i)
        if v == 1:
            return 1, i+1
        if v == DONE:
            return 0, i+1
        if v != 0:
            raise ValueError("unexpected protocol input")
        i+=1

def nth_binary_word(j):
    length=0
    while j >= (1 << length):
        j -= 1 << length
        length+=1
    return tuple((j >> (length-i-1)) & 1 for i in range(length))

def certificate_decoder(oracle, search_limit):
    # A bounded test harness for the infinite fair enumeration in the proof.
    # Returns no guessed value if the witness has not been enumerated.
    for j in range(search_limit):
        w=nth_binary_word(j)
        cert=w+(DONE,)
        if all(oracle(i)==a for i,a in enumerate(cert)):
            return q(w), j+1
    return None

def run_checks():
    tests=[]
    sample=list(words_at_most(12))
    seen=[]
    for w in sample:
        answer, queries=monitor_with_done(lambda i: marked(w,i))
        assert answer==q(w) and queries<=len(w)+1
        seen.append(queries)
    tests.append(dict(id="G1",claim="DONE monitor returns on every sampled finite trace",
                      traces=len(sample),max_queries=max(seen),pass_=True))

    classes={}
    for w in sample:
        normal=trim(w)
        signature=tuple(erased(w,i) for i in range(13))
        if signature in classes:
            old_normal,old_q=classes[signature]
            assert old_q==q(w) and old_normal==normal
        else:
            classes[signature]=(normal,q(w))
    tests.append(dict(id="G2",claim="erasure fibers agree on task value",
                      inputs=len(sample),padded_classes=len(classes),pass_=True))

    canonical=[w for w in sample if not w or w[-1]==1]
    signatures={tuple(erased(w,i) for i in range(13)) for w in canonical}
    assert len(signatures)==len(canonical)==4096
    tests.append(dict(id="G3",claim="canonical finite traces have distinct padded behaviors",
                      canonical_traces=len(canonical),pass_=True))

    query_sets=0
    for mask in range(1<<10):
        Q=[i for i in range(10) if mask & (1<<i)]
        r=max(Q)+1 if Q else 0
        empty=()
        later=(0,)*r+(1,)
        assert all(erased(empty,i)==erased(later,i) for i in Q)
        assert q(empty)==0 and q(later)==1
        assert trim(later)==later
        query_sets+=1
    tests.append(dict(id="G4",claim="for every sampled finite query set a same-domain counterexample",
                      query_sets=query_sets,pass_=True))

    certificates=0
    for n in range(129):
        prefix=(0,)*n
        later=prefix+(1,)
        assert all(erased((),i)==erased(later,i) for i in range(n))
        assert q(later)==1
        for k in (n+1,n+2):
            assert 1 in tuple(erased(later,i) for i in range(k))
            certificates+=1
    tests.append(dict(id="G5",claim="silence never certifies no event at tested lengths; seeing 1 does",
                      silence_lengths=129,positive_prefix_checks=certificates,pass_=True))

    searches=0;max_checked=0
    for w in words_at_most(8):
        result=certificate_decoder(lambda i:marked(w,i),search_limit=512)
        assert result is not None and result[0]==q(w)
        max_checked=max(max_checked,result[1]); searches+=1
    tests.append(dict(id="G6",claim="enumerated finite certificates recover marked-trace task",
                      traces=searches,max_certificates_tested=max_checked,pass_=True))

    return dict(schema_version="hott-done-observability-finite/v1",
                status="PASS_FINITE_SCOPE",groups=tests,group_count=len(tests),
                scope="Finite regression only. Infinite impossibility and certificate iff theorem have separate paper proofs.",
                full_cognition_gate="NOT_PASSED",
                proof_assistant="NOT_RUN",independent_review="NOT_RUN",
                totality_of_all_hott_terms="NOT_CLAIMED")

if __name__=="__main__":
    print(json.dumps(run_checks(),ensure_ascii=False,indent=2))
