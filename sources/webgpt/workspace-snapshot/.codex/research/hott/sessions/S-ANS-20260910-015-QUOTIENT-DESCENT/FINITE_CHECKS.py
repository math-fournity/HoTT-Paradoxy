"""Finite checks for R015; not a proof assistant or an unbounded theorem.
All mathematical definitions here act on completed finite words, not raw infinite oracles.
Standard library only, no subprocess or network.
"""
from itertools import product

def words_upto(bound):
    for n in range(bound+1):
        yield from product((0,1), repeat=n)

def normal(w):
    w=tuple(w)
    if any(b not in (0,1) for b in w):
        raise ValueError("binary word required")
    end=len(w)
    while end and w[end-1]==0:
        end-=1
    return w[:end]

def bit(w,i):
    if i<0: raise ValueError("nonnegative position required")
    return w[i] if i<len(w) else 0

def same_pad_finite_words(w,v):
    return all(bit(w,i)==bit(v,i) for i in range(max(len(w),len(v))))

def answer(w):
    return int(any(w))

def class_membership(representative,query_word):
    return int(same_pad_finite_words(representative,query_word))

def run():
    groups=[]
    W=list(words_upto(10))  # 2047 finite words
    counts={}
    for w in W:
        n=normal(w)
        assert normal(n)==n
        assert n==() or n[-1]==1
        assert same_pad_finite_words(w,n)
        assert answer(w)==answer(n)==int(bool(n))
        counts[n]=counts.get(n,0)+1
    assert len(W)==2047 and len(counts)==1024
    groups.append({"id":"G1","name":"normal_form_idempotence_padding_answer",
                   "words":len(W),"normal_classes":len(counts),"status":"PASS"})

    small=list(words_upto(7))
    related=0
    for w in small:
        for v in small:
            equal=normal(w)==normal(v)
            assert equal==same_pad_finite_words(w,v)
            if equal:
                related+=1
                assert answer(w)==answer(v)
    groups.append({"id":"G2","name":"kernel_equals_normal_form_equality",
                   "words":len(small),"ordered_pairs":len(small)**2,
                   "related_pairs":related,"status":"PASS"})

    # Independently enumerate all Boolean tables on 15 source representatives,
    # select invariant tables, and check their induced quotient tables.
    W3=list(words_upto(3))
    K3=sorted({normal(w) for w in W3})
    evaluated=0
    tables_examined=0
    invariant_tables=0
    quotient_tables=set()
    for labels in product((0,1),repeat=len(W3)):
        tables_examined+=1
        source_task=dict(zip(W3,labels))
        if not all(source_task[w]==source_task[normal(w)] for w in W3):
            continue
        invariant_tables+=1
        task={k:source_task[k] for k in K3}
        quotient_tables.add(tuple(task[k] for k in K3))
        for w in W3:
            assert task[normal(w)]==source_task[w]
            evaluated+=1
    assert len(K3)==8 and tables_examined==32768
    assert invariant_tables==256 and len(quotient_tables)==256 and evaluated==3840
    groups.append({"id":"G3","name":"all_small_invariant_tasks_descend",
                   "classes":len(K3),"source_tables_examined":tables_examined,
                   "invariant_tasks":invariant_tables,"distinct_quotient_tasks":len(quotient_tables),
                   "representatives":len(W3),"evaluations":evaluated,"status":"PASS"})

    # Membership of the empty word detects whether the class is the all-zero class.
    for w in W:
        assert answer(w)==1-class_membership(w,())
    groups.append({"id":"G4","name":"class_membership_query_solves_OR",
                   "representatives":len(W),"queries_per_task":1,"status":"PASS"})

    # Positive search can recover some finite representative from a total membership oracle.
    # Search is not bounded in the general paper argument; these are finite samples.
    tests=list(words_upto(8))
    catalogue=list(words_upto(8))
    max_queries=0
    for w in tests:
        queries=0
        found=None
        for candidate in catalogue:
            queries+=1
            if class_membership(w,candidate):
                found=candidate
                break
        assert found is not None
        assert found==normal(w)  # length-lex search yields canonical representative here
        assert answer(found)==answer(w)
        max_queries=max(max_queries,queries)
    groups.append({"id":"G5","name":"nonempty_decidable_class_search_samples",
                   "inputs":len(tests),"catalogue":len(catalogue),
                   "max_queries":max_queries,"status":"PASS"})

    # Finite representatives of true-image fibres: all representatives give the same canonical data.
    by_signature={}
    for w in W:
        sig=tuple(bit(w,i) for i in range(11))  # longer than every sampled word
        by_signature.setdefault(sig,[]).append(w)
    for reps in by_signature.values():
        ns={normal(w) for w in reps}
        assert len(ns)==1
    groups.append({"id":"G6","name":"unique_canonical_image_witness_samples",
                   "words":len(W),"finite_signatures":len(by_signature),
                   "signature_length":11,"status":"PASS"})

    # The bound is observable in these signatures; never conclude a finite signature
    # distinguishes all infinite streams. These are regression witnesses only.
    for q in [(),(0,),(0,2),(1,3,7),tuple(range(10))]:
        k=max(q)+1 if q else 0
        late=(0,)*k+(1,)
        assert all(bit((),i)==bit(late,i) for i in q)
        assert class_membership((),())!=class_membership(late,())
    groups.append({"id":"G7","name":"component_queries_are_not_membership_queries",
                   "query_sets":5,"status":"PASS_FINITE_EXAMPLES_ONLY"})

    return {
      "schema_version":"hott-r015-finite-checks/v1",
      "status":"PASS_FINITE_SCOPE","groups":groups,"group_count":len(groups),
      "proof_assistant":"NOT_RUN",
      "scope":"Finite-word normal-form model; not HIT implementation, not infinite-oracle exhaustive verification.",
      "general_proofs":"Separate PROOF_NOTE.md; no unbounded theorem certified by these counts.",
      "source_hash_proves_authenticity":False
    }
