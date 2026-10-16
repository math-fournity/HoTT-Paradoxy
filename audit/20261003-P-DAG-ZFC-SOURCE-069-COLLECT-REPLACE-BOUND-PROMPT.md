# P-DAG-ZFC-SOURCE-069：Collect / Replace domain-guard source-match payload

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
Source: Lawrence C. Paulson, Isabelle's Logics: FOL and ZF, official Isabelle PDF, SHA-256 4ce0ae256cb7506832fdc5d3605ff752c932c3c5721e3140c4658d84e56b0fcb.

Frozen source facts:
1. Collect constructs a set by separation: {x:A . P[x]} abbreviates Collect(A, lambda x. P[x]) and consists of all x in A satisfying P[x].
2. Replace constructs {y . x:A, Q[x,y]}, consisting of y for some x in A satisfying Q[x,y]. Replacement requires Q to be single-valued over A.
3. RepFun is a special case of replacement: it produces all b[x] for x in A; the document says a function's domain A must be given in order for the result to be a set.
4. The source lists Pow(B) membership as A in Pow(B) iff A is a subset of B, and lists Collect/Replace/RepFun as ZF set operations.
END FROZEN SOURCE CARD

## Frozen parent TaskCard — echo these exact fields in E3

T = Isabelle documented ZF separation/replacement formation interfaces
u = Collect(A,P), contrasted with Replace(A,Q) and RepFun(A,f)
F = set formation only over the supplied set domain A
C = documented formation interface; no separate runtime consumer supplied
I = A,P or A,Q/f with A explicitly a set domain
O = bounded subset/image/replacement set
Done = source-layer formation result subject to the stated bound/single-value condition; no runtime completion asserted
Q? = whether an arbitrary predicate/class-function formation becomes an active, unpaid same-object formation/identity/operator obligation after the domain guard is retained

## Required analysis

E0 scope; E1 source identity; E2 source facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 ledger; E6 PowerSetDefenseLedger; E7 bounded verdict and altered fact.

At E5 distinguish the bounded binder x in A from unrestricted comprehension, source formation from active demand, and source syntax from runtime lifecycle. Do not invent a consumer or a same-object reentry.

At E6 use this exact semantic table:

| field | question |
| PS0 source/variant | Which Collect/Replace/RepFun/Pow source variant and layer are examined? |
| PS1 defended Russell feature | Which source-stated unrestricted predicate/class-function boundary is constrained? |
| PS2 actual guard | What exact given-domain/single-valued or subset condition applies? |
| PS3 guard scope | Which documented formation task/layer is covered? |
| PS4 candidate surplus | With guard retained, what active same-task Q, negative reentry, lifecycle or unpaid remainder is source-supported? |
| PS5 same-task control | What does the source say changes if the required domain/bound is absent or altered? |
| PS6 verdict | Give one bounded verdict from DEFENSE_IDENTIFIED, CANDIDATE_GUARD_BLOCKED, BEYOND_DEFENSE_CANDIDATE, SOURCE_GUARD_SCOPE_UNSET or NOT_ENOUGH_EVIDENCE. |

Use ABSENT/UNSUPPORTED or UNKNOWN for source gaps. A documented formation operation does not by itself establish a runtime construction process, a theory defect, a real task, or a ZFC result.
```
