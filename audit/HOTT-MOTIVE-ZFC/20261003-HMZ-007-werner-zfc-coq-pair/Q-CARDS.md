# HMZ-007：Q-Cards — 配对来源的资格结论

## HMZ-Q-009 — “ZFC-based Coq formalization 必然把未交付对象当作已交付”

```text
same-task test:
  FAIL.  WoLLIC gives a historical/motivational sentence; Werner supplies a
  specific CIC model and proof task.  Voevodsky does not identify Werner as
  one of the attempts, and “unnatural” has no shared source-defined Done.
payment:
  Werner explicitly adds EM + TTDA/TTCA non-computational choice principles for full ZFC.
P1/P2/P3:
  P1 only at proof-formalization/model layer; no same-object reentry or pending
  admission is supplied.
disposition:
  CANDIDATE_PAIRING_NOT_ATTRIBUTED + SOURCE_PAYMENT / Q-R REJECTED_WITH_SCOPE.
```

## HMZ-Q-010 — `Power` as a possible second Russell opening

```text
same-task test:
  FAIL.  Power is a CIC definition on an already formed Ens, not evidence that
  bare ZFC's P(A) is used before formation is settled.
P2/P3:
  NOT SUPPLIED.  Type-level predicates and impredicative Prop are visible host
  assumptions; no self-reentry appears.
H0 transport T0–T5:
  FAIL AT T2/T4/T5.  Extensional EQ : Ens -> Ens -> Prop changes the high
  identity subject and the source contains no HoTT-style “which level settles?”
  process or Done.
disposition:
  ANTI_ANALOGY_CONTROL / P_REQUALIFICATION_REQUIRED.
```

## HMZ-Q-011 — Russell.v as P-positive candidate

```text
surface resemblance:
  Comp U (fun x => IN x x -> False) occurs and the file is named Russell.
control:
  the theorem begins from a hypothesized universal U : Ens and proves False;
  U is never formed by the comprehension itself.  Thus it blocks the naive
  formation, instead of using an unformed same object.
disposition:
  RUSSELL_GUARD_CONTROL / Q-R REJECTED_WITH_SCOPE.
```
