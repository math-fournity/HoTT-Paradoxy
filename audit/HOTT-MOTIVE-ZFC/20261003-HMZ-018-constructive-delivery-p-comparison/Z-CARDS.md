# HMZ-018：ZF/ZFC delivery-side还原

## HMZ-Z-023 — ZF sethood and named interfaces do not state a program-delivery contract

```text
source layer:
  Paulson Isabelle/ZF formalization plus prior HMZ-003 formation controls.
u/F:
  ZF axioms/formulas plus named constants and derived rules.
consumer:
  formal proof developments under those named interfaces.
source-supported fact:
  formation/payment interfaces are explicit; no source says that a bare
  existential theorem yields a terminating program for every use.
disposition:
  FORMATION_INTERFACE_CONTROL / NOT_A_CONSTRUCTIVE_DELIVERY_PROMISE.
```

## HMZ-Z-024 — HoTT also has a computation/axiom boundary

```text
source layer:
  Grayson / HoTT Library.
source-supported fact:
  an axiom may block computation even in a type-theoretic formalization.
what it controls:
  “type theory is constructive” cannot be turned into an unconditional
  existence-to-delivery assertion.
disposition:
  SYMMETRIC_COMPUTATION_CONTROL.
```
