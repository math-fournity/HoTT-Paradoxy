# P-DAG-ZFC-VALIDATION-020：Mathlib ZFSet card的 P1 冻结 source-match prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen source card and P1 method.
Do not use tools, files, web, project history, prior results, or delegation. Do not
provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

P1 requires a concrete first-class subject u, native formation F, a same-layer source
consumer C with input/output/Done, and a Q demanded by that consumer. Then test: Q
must not be immediately paid by F (L6) and must be a positive obligation for task Done,
not a normal yes/no or membership query that can finish by false (L7). Do not promote a
proof-system contract into another layer. Compare a nearby reading, give the shortest
rule chain/normalization, a counterfactual, and choose a bounded status in E7.

BEGIN FROZEN SOURCE CARD
Scope: Mathlib4 v4.16.0, commit a6276f4c6097675b1cf5ebd49b1146b735f38c02.
The source header describes ZFSet as a ZFC (+ Choice) model in Lean's underlying type theory.

def powerset : ZFSet -> ZFSet
theorem mem_powerset : y in powerset x <-> y subseteq x

def funs (x y : ZFSet) : ZFSet :=
  ZFSet.sep (IsFunc x y) (powerset (prod x y))

theorem mem_funs : f in funs x y <-> IsFunc x y f

No operational lifecycle, algorithm, real-world task, external consumer, or extra
source statement is supplied.
END FROZEN SOURCE CARD
```

