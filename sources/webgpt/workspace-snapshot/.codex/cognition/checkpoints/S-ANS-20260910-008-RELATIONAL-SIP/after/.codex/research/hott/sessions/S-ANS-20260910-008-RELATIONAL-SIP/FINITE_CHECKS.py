"""Revision 8 finite checks; standard library only.
Enumerations check finite models, not kernel proofs or unlimited mathematical claims.
No uploaded source module or subprocess is executed.
"""
from itertools import product, permutations

def mask_relation(n, pred):
    return sum(1 << (n*x+y) for x in range(n) for y in range(n) if pred(x,y))

def preserves(n, R, S, f):
    return all(not (R >> (n*x+y) & 1) or (S >> (n*f[x]+f[y]) & 1)
               for x in range(n) for y in range(n))

def inverse(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)

def image_relation(n,R,p):
    return sum(1 << (n*p[x]+p[y]) for x in range(n) for y in range(n)
               if R >> (n*x+y) & 1)

def partitions(n):
    if n==0: return [()]
    seq=[(0,)]
    for _ in range(1,n):
        seq=[v+(b,) for v in seq for b in range(max(v)+2)]
    return seq

def class_count(n,R):
    seen=set(); total=0
    for x in range(n):
        if x not in seen:
            seen.update(y for y in range(n) if R >> (n*x+y) & 1)
            total+=1
    return total

def run_checks():
    results=[]
    n=2; eq=mask_relation(n,lambda x,y:x==y); full=(1<<(n*n))-1
    ident=(0,1)
    assert preserves(n,eq,full,ident) and not preserves(n,full,eq,ident)
    results.append({"id":"T01","status":"PASS_FINITE_SCOPE",
                    "claim":"Bijection plus forward relation hom is not structured iso",
                    "forward":True,"inverse":False})

    count=one=two=0
    for n in (1,2):
        rels=range(1<<(n*n))
        for p in permutations(range(n)):
            d=inverse(p)
            for a in rels:
                im=image_relation(n,a,p)
                for b in rels:
                    fwd=preserves(n,a,b,p)
                    back=preserves(n,b,a,d)
                    assert fwd == ((im & ~b)==0)
                    assert (fwd and back)==(im==b)
                    count+=1;one+=int(fwd);two+=int(fwd and back)
    assert count==516
    results.append({"id":"T02","status":"PASS_FINITE_SCOPE",
                    "arbitrary_relation_bijection_cases":count,
                    "forward_hom_cases":one,"two_way_iso_cases":two})

    count=one=two=0
    for n in range(1,5):
        rels=[mask_relation(n,lambda x,y,v=v:v[x]==v[y]) for v in partitions(n)]
        for p in permutations(range(n)):
            d=inverse(p)
            for a in rels:
                im=image_relation(n,a,p)
                for b in rels:
                    fwd=preserves(n,a,b,p);back=preserves(n,b,a,d)
                    assert (fwd and back)==(im==b)
                    count+=1;one+=int(fwd);two+=int(fwd and back)
    assert count==5559
    results.append({"id":"T03","status":"PASS_FINITE_SCOPE",
                    "equivalence_relation_bijection_cases":count,
                    "forward_hom_cases":one,"two_way_iso_cases":two})

    X=tuple(product((0,1),repeat=3));N=len(X)
    K=[mask_relation(N,lambda x,y,k=k:X[x][:k]==X[y][:k]) for k in (1,2,3)]
    late=(K[0],K[0],K[1],K[2])
    early=(K[0],K[1],K[1],K[2])
    assert all((fine & ~coarse)==0 for seq in (late,early) for coarse,fine in zip(seq,seq[1:]))
    counts_l=[class_count(N,r) for r in late]
    counts_e=[class_count(N,r) for r in early]
    assert counts_l==[2,2,4,8] and counts_e==[2,4,4,8]
    assert set(late)==set(early)
    results.append({"id":"T04","status":"PASS_FINITE_SCOPE",
                    "late_observation_classes":counts_l,
                    "early_observation_classes":counts_e,
                    "same_unindexed_relation_family":True})

    # Enumerate every triangular map, using a proved mathematical
    # characterization; NOT an exhaustive loop through 8^8 raw maps.
    by_tuple={x:i for i,x in enumerate(X)}
    triangular=set()
    for g1 in product((0,1),repeat=2):
        for g2 in product((0,1),repeat=4):
            for g3 in product((0,1),repeat=8):
                f=tuple(by_tuple[(g1[a],g2[2*a+b],g3[i])]
                        for i,(a,b,c) in enumerate(X))
                assert all(preserves(N,r,r,f) for r in late)
                assert all(preserves(N,r,r,f) for r in early)
                triangular.add(f)
    assert len(triangular)==16384
    results.append({"id":"T05","status":"PASS_FINITE_SCOPE",
                    "triangular_maps_checked":len(triangular),
                    "all_raw_maps":8**8,
                    "raw_exhaustive_enumeration":False,
                    "completeness_basis":"Separate paper characterization, not assumed from enumeration"})

    permutation_count=iso_count=0
    for p in permutations(range(N)):
        permutation_count+=1
        all_layers=all(image_relation(N,a,p)==b for a,b in zip(late,early))
        iso_count+=int(all_layers)
    assert permutation_count==40320 and iso_count==0
    results.append({"id":"T06","status":"PASS_FINITE_SCOPE",
                    "all_carrier_bijections_checked":permutation_count,
                    "time_preserving_structural_isomorphisms":iso_count})

    q=tuple(b for a,b,c in X)
    out_eq=mask_relation(2,lambda x,y:x==y)
    def available(rel,obs):
        return all(not(rel>>(N*x+y)&1) or obs[x]==obs[y]
                   for x in range(N) for y in range(N))
    assert available(early[1],q) and not available(late[1],q)
    ix=X.index((0,0,0));iy=X.index((0,1,0))
    assert late[1]>>(N*ix+iy)&1 and q[ix]!=q[iy]
    ident=tuple(range(N))
    assert all(preserves(N,a,b,ident) for a,b in zip(early,late))
    assert not all(preserves(N,a,b,ident) for a,b in zip(late,early))
    results.append({"id":"T07","status":"PASS_FINITE_SCOPE",
                    "question":"Return b at clock 1",
                    "early_available":True,"late_available":False,
                    "counterexample_inputs":[list(X[ix]),list(X[iy])],
                    "early_to_late_identity_hom":True,"late_to_early_identity_hom":False})

    probes=tuple(product((0,1),repeat=N))
    families_l=[[p for p in probes if available(r,p)] for r in late]
    families_e=[[p for p in probes if available(r,p)] for r in early]
    sizes_l=[len(v) for v in families_l];sizes_e=[len(v) for v in families_e]
    assert sizes_l==[4,4,16,256] and sizes_e==[4,16,16,256]
    results.append({"id":"T08","status":"PASS_FINITE_SCOPE",
                    "bool_probes_enumerated":len(probes),
                    "late_per_clock":sizes_l,"early_per_clock":sizes_e})

    restored=0
    for rel,family in zip(late+early,families_l+families_e):
        rec=mask_relation(N,lambda x,y,fs=family:all(p[x]==p[y] for p in fs))
        assert rec==rel
        restored+=1
    results.append({"id":"T09","status":"PASS_FINITE_SCOPE",
                    "relations_reconstructed_from_all_stage_bool_probes":restored})
    return {"schema_version":"hott-r8-finite-checks/v1","status":"PASS_FINITE_SCOPE",
            "test_groups":len(results),"results":results,
            "proof_assistant":"NOT_RUN","independent_review":"NOT_RUN",
            "governance_full_cognition":"NOT_CERTIFIED",
            "limits":"Finite checks and exact counts only; general statements rely on paper proofs."}
