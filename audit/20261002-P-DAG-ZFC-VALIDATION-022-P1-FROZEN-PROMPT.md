# P-DAG-ZFC-VALIDATION-022：冻结 parent card 的 P1 source-match prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen source card below. Do not
use tools, files, web, project history, prior results, or delegation. Do not provide
hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

This is parent validation, not fresh selection. You MUST keep T/u/F/C/I/O/Done fixed.
You may reject the parent as insufficient or show that no Q exists, but you may not
replace u, F, C, or Q by another object. Test whether the frozen consumer has a
distinct Q that is (a) not immediately paid by F (L6) and (b) a positive obligation
for source-level Done rather than a normal proposition/membership query with a false
branch (L7). Distinguish the formal-model API layer from proof-system or runtime
claims. Compare a nearby reading, give the shortest rule chain, one counterfactual,
and a bounded E7 status.

BEGIN FROZEN SOURCE CARD
Scope: Mathlib4 v4.16.0, commit a6276f4c6097675b1cf5ebd49b1146b735f38c02.
Theory layer: Lean underlying-type-theory ZFC(+Choice) model; not standard ZFC itself.

T = that fixed formal model
u = powerset (prod x y)
F = powerset with mem_powerset: y in powerset x <-> y subseteq x
C = funs x y := ZFSet.sep (IsFunc x y) u
I = x, y, candidate f, u
O = funs x y : ZFSet
Done = mem_funs: f in funs x y <-> IsFunc x y f
Q = UNSET; determine whether any distinct source-supported positive obligation exists.

No operational lifecycle, algorithm, external consumer, real-world task, or additional
source statement is supplied.
END FROZEN SOURCE CARD
```

