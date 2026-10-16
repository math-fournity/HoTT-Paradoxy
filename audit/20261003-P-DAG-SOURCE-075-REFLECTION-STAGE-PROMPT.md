# P-DAG-SOURCE-075：ClEx reflection stage source-match payload

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
Source: isabelle-prover/mirror-isabelle `src/ZF/Constructible/Reflection.thy`, commit 5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256 c6f53b48e78e3683d8e78fd6c72d203aeef2fed13f7fba9b7f421bdf7561f27f.

Frozen source facts:
1. M(x) is defined as existence of an ordinal a with x in Mset(a). Reflects(Cl,P,Q) requires closed/unbounded Cl and, for stages a in Cl and x in Mset(a), P(x) iff Q(a,x).
2. F0(P,y) selects a least witness-bound; FF(P,a) is the union of F0(P,y) over y in Mset(a); ClEx(P,a) is Limit(a) and normalize(FF(P),a)=a.
3. The source proves ZF_ClEx_iff: under stated Mset/Cl/ClEx conditions, a global existential P fact is equivalent to a local existential Q fact in Mset(a).
4. The source proves ZF_Closed_Unbounded_ClEx: Closed_Unbounded(ClEx(P)). The source is a proof-theory development and supplies no runtime lifecycle or real-world task.
END FROZEN SOURCE CARD

## Frozen parent TaskCard — echo these exact fields in E3

T = Isabelle/ZF Constructible Reflection proof theory
u = ClEx(P,a), a stage-selection condition for existential reflection
F = F0/FF/ClEx/Reflects definitions over Mset, M, P, Q and Cl
C = ZF_ClEx_iff and ZF_Closed_Unbounded_ClEx proof-theoretic use
I = P,Q,Cl,a,x,Mset(a) and formula/stage conditions
O = global/local existential reflection equivalence and closed-unbounded reflecting-stage result
Done = source theorem/proof result at the stated proof-theory layer
Q? = whether this source leaves a current active unpaid same-stage/formula reflection task after its own source packet is considered

## Required analysis

E0 scope; E1 source identity; E2 source facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 ledger; E6 nearest guard/payment and bounded verdict; E7 altered fact.

At E5 separately answer:
1. P1 active task/payment: are the stated theorems direct packet payment of the candidate task?
2. P2: is P(x) iff Q(a,x) a same-object reentry/feedback bridge, or a guarded global/local formula relation? Do not invent self-reference.
3. P3: are any Draft/NeedBuild/NeedEval/Admitted/OperatorUse/BuildDone transitions stated?

Do not claim global truth, ZFC inconsistency, a runtime process, a real task, UR, or a new knife.
```
