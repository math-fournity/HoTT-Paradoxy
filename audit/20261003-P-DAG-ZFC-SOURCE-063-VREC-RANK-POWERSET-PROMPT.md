You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

## Frozen source identity and scope

This is an Isabelle/ZF proof-theory card. It is not a full standard-ZFC semantic consumer, a runtime lifecycle, a history claim, or a real-world task.

- **Source A:** `Univ.thy`, Isabelle mirror commit `5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8`, SHA-256 `67f77f66e1892afefdb76b17d058d7d88792aefef2dce56d5f1211c09e785213`.
- **Source B:** `Epsilon.thy`, same commit, SHA-256 `9f0a4f8340a96df9ae9c7086349f04e9f61967af6ab35d6425465f744b4b8fbc`.

Frozen source excerpts, rendered only for this card:

```text
Vfrom(A,i) == transrec(i, lambda x f. A union (Union y in x. Pow(f`y)))
Vfrom(A,succ(i)) = A union Pow(Vfrom(A,i))
Limit(i) -> Vfrom(A,i) = Union y in i. Vfrom(A,y)

Vrec(a,H) == transrec(rank(a), lambda x g.
  (lambda z in Vset(succ(x)).
     H(z, lambda w in Vset(x). g`rank(w)`w)) ` a)
Vrec(a,H) = H(a, lambda x in Vset(rank(a)). Vrec(x,H))

b in Vset(a) <-> rank(b) < rank(a)
rank(a) < rank(b) when a in b
rank(Pow(a)) = succ(rank(a))
Pow(a) in Vfrom(A,succ(succ(j))) when a in Vfrom(A,j) and Transset(A)
```

## Frozen parent TaskCard — echo these exact fields in E3

```text
T = Isabelle/ZF cumulative-hierarchy and Vrec proof theory
u = Vrec(a,H), indexed by the object a and rank(a)
F = Vrec/Vfrom formation through transrec and Vset(rank(a))
C = source Vrec recurrence/recursor proof use
I = a,H and lower-rank x in Vset(rank(a))
O = H(a, lambda x in Vset(rank(a)). Vrec(x,H))
Done = source-defined recursive equation / proof use under the stated lower-rank domain only
Q? = whether the source provides an active, unpaid same-object formation/identity/operator obligation after its rank and stage guards, rather than merely a guarded lower-rank recursion
```

## Required analysis

E0 scope; E1 source identity; E2 source-bearing facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 ledger; E6 `PowerSetDefenseLedger`; E7 bounded verdict and changed fact that would alter it.

For E5, separately state:

1. P1: whether a source-defined active Q exists and whether any definition, source equation, supplied guard, or witnessed rule directly pays it.
2. P2: Bind/Form, Bridge/Reenter, polarity, and whether the relation strictly lowers rank or returns to the same `a`.
3. P3: whether the source actually gives `Draft`, `NeedBuild`, `NeedEval`, `Admitted`, `OperatorUse`, or `BuildDone`; source equations and proof acceptance alone do not count.

For E6, fill PS0–PS6. Treat `Vfrom` successor/limit and `rank` as source facts. If a remove-guard counterfactual is not in the source, label it `UNKNOWN`; do not invent one. A source gap is `UNKNOWN`, not evidence of a defect. Do not call recursion, a rank, a stage, or an output elapsed time “theory time.”

Use the fixed card only. Do not introduce another object, consumer, theory variant, real task, or hypothesis.
