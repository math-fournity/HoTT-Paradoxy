"""New revision-11 finite sanity checks; NOT a proof of LPO or undecidability.
Stdlib only. Every finite word has a known end, unlike an arbitrary infinite stream.
Bound certificates below are checked only on explicit known pulse/zero examples.
No user mathematical programs or proof assistants are imported.
"""
from itertools import product
import json

def pulse(n, k):
    return 0 if n is None else int(k == n)

def first_pulse(word):
    seen = False
    out = []
    for bit in word:
        if bit not in (0, 1):
            raise ValueError("Not a binary word")
        out.append(int(bit == 1 and not seen))
        seen = seen or bit == 1
    return tuple(out)

def finite_report(word):
    where = [i for i, v in enumerate(word) if v == 1]
    if len(where) > 1:
        raise ValueError("Not at most one")
    return None if not where else where[0]

def bounded_report(stream, horizon):
    # Correct only when an actual certificate establishes zero for all k >= horizon.
    if horizon < 0:
        raise ValueError("negative horizon")
    for k in range(horizon):
        if stream(k):
            return k
    return None

def validate_program(prog):
    if not prog:
        raise ValueError("empty program")
    for op in prog:
        if op[0] == "halt":
            if len(op) != 1: raise ValueError("halt arity")
        elif op[0] == "inc":
            if len(op) != 3 or op[1] not in (0, 1) or not 0 <= op[2] < len(prog):
                raise ValueError("bad inc")
        elif op[0] == "dec":
            if len(op) != 4 or op[1] not in (0, 1) or not all(0 <= t < len(prog) for t in op[2:]):
                raise ValueError("bad dec")
        else:
            raise ValueError("bad opcode")

def halted(prog, conf):
    return prog[conf[0]][0] == "halt"

def step(prog, conf):
    pc, a, b = conf
    regs = [a, b]
    op = prog[pc]
    if op[0] == "halt":
        return conf
    if op[0] == "inc":
        regs[op[1]] += 1
        return (op[2], *regs)
    if regs[op[1]] == 0:
        return (op[2], *regs)
    regs[op[1]] -= 1
    return (op[3], *regs)

def state_at(prog, initial, n):
    conf = initial
    for _ in range(n):
        conf = step(prog, conf)
    return conf

def first_halt_bit(prog, initial, n):
    # Always finite: n transitions and optionally n-1 transitions.
    now = halted(prog, state_at(prog, initial, n))
    previous = False if n == 0 else halted(prog, state_at(prog, initial, n-1))
    return int(now and not previous)

def run():
    groups = []
    # Concrete finite returned reports; no-event given as a constructor.
    for n in [None] + list(range(128)):
        N = 0 if n is None else n+1
        assert bounded_report(lambda k, n=n: pulse(n,k), N) == n
    groups.append({"id":"G1","name":"explicit completed reports encode and recover with certificates",
                   "cases":129,"scope":"explicit zero/pulse streams with known horizon"})

    amo_count, all_words = 0, 0
    by_length = []
    for length in range(13):
        count=0
        for w in product((0,1),repeat=length):
            all_words+=1
            if sum(w)>1: continue
            count+=1; amo_count+=1
            r=finite_report(w)
            assert tuple(pulse(r,k) for k in range(length))==w
        assert count==length+1
        by_length.append({"length":length,"at_most_one":count})
    groups.append({"id":"G2","name":"finite at-most-one fibers have exactly one report",
                   "all_words":all_words,"accepted":amo_count,"by_length":by_length,
                   "scope":"finite image fibers only; not HoTT truncation execution"})

    cases=0
    for length in range(12):
        for w in product((0,1),repeat=length):
            p=first_pulse(w); cases+=1
            assert sum(p)<=1
            assert sum(p)==int(any(w))
            if any(w):
                assert finite_report(p)==w.index(1)
    groups.append({"id":"G3","name":"bounded first-event masking","cases":cases,
                   "scope":"finite prefixes; arbitrary-stream logical principle separately proved"})

    bound_cases=0
    for n in [None]+list(range(24)):
        for N in range(25):
            valid=(n is None or n < N)
            if valid:
                assert bounded_report(lambda k,n=n:pulse(n,k),N)==n
                bound_cases+=1
    groups.append({"id":"G4","name":"actual end-horizon suffices on explicit streams",
                   "cases":bound_cases,"scope":"uses a true horizon, never infers one from finite zeros"})

    queries=0
    for mask in range(1<<10):
        Q=[i for i in range(10) if mask & (1<<i)]
        m=max(Q)+1 if Q else 0
        assert all(pulse(None,q)==pulse(m,q) for q in Q)
        assert pulse(None,m)!=pulse(m,m)
        queries+=1
    groups.append({"id":"G5","name":"finite-query transcripts do not certify zero forever",
                   "cases":queries,"scope":"finite sanity of the separate adversarial argument"})

    program_cases = [
        ("halt_now", (("halt",),), (0,0,0), 0),
        ("increment_forever", (("inc",0,0),), (0,0,0), None),
    ]
    for a in range(16):
        program_cases.append(("countdown_"+str(a),
                              (("dec",0,1,0),("halt",)),(0,a,0), a+1))
    details=[]
    evaluations=0
    for name,prog,initial,known_halt in program_cases:
        validate_program(prog)
        bits=tuple(first_halt_bit(prog,initial,n) for n in range(65))
        evaluations+=len(bits)
        assert sum(bits)<=1
        assert bits==tuple(pulse(known_halt,n) for n in range(65))
        assert finite_report(bits)==known_halt
        details.append({"program":name,"code":prog,"initial":initial,
                        "first_halt_in_checked_range":finite_report(bits)})
    groups.append({"id":"G6","name":"source-code-visible total first-halt generators",
                   "programs":len(details),"bounded_bit_evaluations":evaluations,
                   "examples":details,
                   "scope":"each bit computed by bounded simulation; no universal decidability claim"})

    failed_certificates=0
    for N in range(64):
        late=N+1
        assert bounded_report(lambda k:pulse(None,k),N) is None
        assert bounded_report(lambda k,late=late:pulse(late,k),N) is None
        assert pulse(late,late)==1
        failed_certificates+=1
    groups.append({"id":"G7","name":"unjustified cutoff misclassifies a later event",
                   "cases":failed_certificates,
                   "scope":"a checked prefix is not a bound certificate"})
    return {"schema_version":"hott-finite-checks/rev11-v1","status":"PASS_FINITE_SCOPE",
            "groups":groups, "group_count":len(groups),
            "not_proved_by_program":["HoTT typing","unbounded termination","LPO independence",
                                    "double-negation or truncation principles",
                                    "absence of a general code classifier"],
            "kernel_run":False,"external_search":False,
            "mathematical_general_proofs":"separate PROOF_NOTE.md"}
if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
