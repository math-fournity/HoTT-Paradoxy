# P-DAG-ZFC-SOURCE-024：修复 marker 的 relative-powerset P1 prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card. Do not
use tools, files, web, project history, prior results, or delegation. Do not provide
hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

For P1, identify theory scope, layer, subject, formation, consumer, input/output/Done,
and Q if any. Do not promote an external metatheoretic comparison into an internal
consumer. Test L6/L7: a Q must not be directly paid and must be a positive obligation,
not a normal false-branch predicate. State a nearby reading, shortest rule chain,
counterfactual, and bounded status.

BEGIN FROZEN SOURCE CARD
Source: Isabelle2013-1, ZF-Constructible/Relative.thy rendered at
https://isabelle.in.tum.de/website-Isabelle2013-1/dist/library/ZF/ZF-Constructible/Relative.html
Scope shown in source: locale M_trivial, a relative/transitive model M.

definition power_ax(M) == forall x[M]. exists z[M]. powerset(M,x,z)

The source comments: “Powerset is NOT absolute! This result is one direction of
absoluteness.” It then proves:
  powerset(M, x, Pow(x))
and comments that it cannot prove that the powerset in M includes the real powerset.
It also proves:
  [powerset(M,x,y); M(y)] ==> y subseteq Pow(x)

No source line states that M's internal powerset equals the external powerset, no
runtime process is supplied, and no external consumer/Done is supplied.
END FROZEN SOURCE CARD
```

