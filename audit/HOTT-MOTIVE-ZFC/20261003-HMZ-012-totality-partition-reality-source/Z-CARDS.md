# HMZ-012：Z-side 还原卡

## HMZ-Z-018 — Power Set / subset formation of the class collection

```text
source layers:
  HMZ-S-028 (informal set-theoretic exposition), HMZ-S-010 (ZFC axiom
  taxonomy), HMZ-S-007 (proof-formalization formula).
candidate u:
  a set A, equivalence relation R on A, a class [x]⊆A and the collection E of
  all R-classes.
formation F:
  informal route: form each class by a subset condition and form E as a subset
  of P(A); exact theory sources expose Power Set plus separation/subset rules.
consumer C:
  in HMZ-S-028, use E as a complete partition and its members as mathematical
  objects, including quotient rational numbers.
I/O/Done:
  Input A,R; operation form classes and E; observation each element belongs to
  exactly one class / classes are objects; source-expository Done = complete
  partition or quotient object.
layer warning:
  HMZ-S-028 does not pin an exact ZFC object-language formulation. HMZ-S-010
  and S-007 pin formation resources but do not inherit the paper's cognitive
  Done.
standard formation payment:
  The source itself names subset and Power Set axioms; exact sources make them
  explicit formation rules.
disposition:
  CONSTRUCTION_BRIDGE / P_REQUALIFICATION_REQUIRED.
```

## HMZ-Z-019 — Isabelle/ZF is a nearby actual consumer, with a different F

```text
source layer:
  HMZ-S-027 proof formalization, interpreted with HMZ-S-011.
u/F/C/I/O/Done:
  A,r,A//r; formation by RepFun; quotient I/E and well-defined unary/binary
  operations; Done is a theorem conclusion after equiv/congruence/membership/
  type hypotheses.
competitive reading:
  Z-A: it proves actual consumers can use quotient objects.
  Z-B: it does so only after named formation and guards, and changes the
  Power Set-subset formation route to functional replacement.
standard payment / guard:
  RepFun/Replacement, equiv(A,r), respects/congruent, membership and type
  premises.
disposition:
  ACTUAL_CONSUMER_CONTROL / F_ROUTE_MISMATCH / SOURCE_PAYMENT.
```

## H0 transport status

The proposed Z-side identity here is an equivalence-class quotient. It does not preserve HoTT H0's higher-sameness subject, process, observation or Done: quotient equality is an extensional/class-level relation; the source has no universe-level higher identity completion problem. Therefore `H0→Z0→Q0 = NOT FORMED`, not “ZFC passed” or “H0 is merely a quotient.”
