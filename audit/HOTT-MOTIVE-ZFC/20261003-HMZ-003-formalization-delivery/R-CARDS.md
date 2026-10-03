# HMZ-003：R-Cards — 形式化与可计算性的来源动机

## HMZ-R-011 — 类型纪律与 set-theoretic encoding

```text
sources:
  HMZ-S-016 pp. 5–6; HMZ-S-017 pp. 160–161.
claim class:
  REPRESENTATION_COST + CAPABILITY_GOAL.
source-reported content:
  Type theory offers many typed grammatical categories; Rijke/Spitters contrast
  this with an untyped set-theoretic language in which certain errors are harder
  to catch. Grayson explains that ordinary informal types are not directly
  supported by FOL/ZF in the same way.
does not claim:
  Every set-theoretically well-formed statement is meaningless; ZFC cannot be
  formalized; or a type error is a P-shaped formation defect.
linked Z:
  HMZ-Z-011.
```

## HMZ-R-012 — computation, induction and axioms

```text
source:
  HMZ-S-016 pp. 7–8 / derived lines 276–358.
claim class:
  CAPABILITY_GOAL + COMPUTATIONAL_CONTRAST.
source-reported content:
  Reduction of an inductively defined natural-number computation is described
  as complete; an axiom such as excluded middle supplies no effective decision
  procedure even when it is a permissible hypothesis.
does not claim:
  Every classical axiom or every ZFC existential axiom is inconsistent, illegal,
  or an example of a process that uses an unformed object.
linked Z:
  HMZ-Z-012.
```

## HMZ-R-013 — practical formalization has implementation constraints

```text
sources:
  HMZ-S-017 pp. 159–162; HMZ-S-018 pp. 6–10.
claim class:
  CAPABILITY_GOAL + HISTORICAL_CONTEXT.
source-reported content:
  Proof assistants use computation and type discipline to make large
  formalizations practical; actual HoTT libraries have universe/implementation
  constraints and may use axioms that block computation in some proofs.
does not claim:
  HoTT has unqualified computation everywhere, or ZFC is categorically unable
  to support a proof assistant.
linked controls:
  HMZ-C-011, HMZ-C-012.
```
