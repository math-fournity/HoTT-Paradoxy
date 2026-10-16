# P-DAG-ZFC-SOURCE-066：Vrec／rank／Power Set ledger-field repair

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
This is an Isabelle/ZF proof-theory card. It is not a full standard-ZFC semantic consumer, a runtime lifecycle, a history claim, or a real-world task.

Source A: Univ.thy, Isabelle mirror commit 5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256 67f77f66e1892afefdb76b17d058d7d88792aefef2dce56d5f1211c09e785213.
Source B: Epsilon.thy, same commit, SHA-256 9f0a4f8340a96df9ae9c7086349f04e9f61967af6ab35d6425465f744b4b8fbc.

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
END FROZEN SOURCE CARD

## Frozen parent TaskCard — echo these exact fields in E3

T = Isabelle/ZF cumulative-hierarchy and Vrec proof theory
u = Vrec(a,H), indexed by the object a and rank(a)
F = Vrec/Vfrom formation through transrec and Vset(rank(a))
C = source Vrec recurrence/recursor proof use
I = a,H and lower-rank x in Vset(rank(a))
O = H(a, lambda x in Vset(rank(a)). Vrec(x,H))
Done = source-defined recursive equation / proof use under the stated lower-rank domain only
Q? = whether the source provides an active, unpaid same-object formation/identity/operator obligation after its rank and stage guards, rather than merely a guarded lower-rank recursion

## Required analysis

E0 scope; E1 source identity; E2 source-bearing facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 ledger; E6 PowerSetDefenseLedger; E7 bounded verdict and changed fact that would alter it.

At E5 separately state P1 active-Q/payment, P2 Bind/Form + Bridge/Reenter + polarity + rank relation, and P3 lifecycle/build evidence. A source equation, proof acceptance, rank, stage, or elapsed time cannot substitute for a lifecycle state.

At E6 use exactly this semantic table and no alternate meaning for the labels:

| field | question you must answer |
| PS0 source/variant | Which version-fixed Power Set / Vfrom / rank rule and which proof-layer consumer are being examined? |
| PS1 defended Russell feature | Which Russell-style feature, if any, is actually constrained: unrestricted binder, negative self-reentry, rank/stage ascent, self-membership, or formation payment? State UNKNOWN if the source does not establish one. |
| PS2 actual guard | Which exact source condition limits recursive inputs or Power Set use? |
| PS3 guard scope | Which theory layer and task does that guard cover? |
| PS4 candidate surplus | With the guard retained, what active same-task Q, negative reentry, lifecycle, or other unpaid remainder is source-supported? State ABSENT/UNSUPPORTED if none. |
| PS5 same-task control | What changes if the guard is removed or altered? If no such counterfactual is a source fact, say COUNTERFACTUAL_UNKNOWN and describe only the actual positive guard control. |
| PS6 verdict | Give one bounded verdict from DEFENSE_IDENTIFIED, CANDIDATE_GUARD_BLOCKED, BEYOND_DEFENSE_CANDIDATE, SOURCE_GUARD_SCOPE_UNSET, or NOT_ENOUGH_EVIDENCE, plus a reason. |

Do not relabel raw source excerpts as PS0–PS6. A source gap is UNKNOWN, not evidence of a defect. Do not call recursion, a rank, a stage, or an output elapsed time theory time. Use the fixed card only.
```
