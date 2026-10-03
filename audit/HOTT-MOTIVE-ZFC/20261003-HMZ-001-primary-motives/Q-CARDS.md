# HMZ-001：Q-Cards — 资格与控制处置

> 这里记录的不是“已发现的问题清单”。每项要么是来源充分的控制，要么是明确指出哪一道 P／同一任务门还没有通过。

## HMZ-Q-001 — 结构分类不会自动变成自然的 universal family

```text
Target-Q:
  是否有一个 set-theoretic / structuralist consumer 把按同构给出的分类，
  当作已经交付具体、自然、可拉回的 family？
Candidate-Q:
  The classification is used as though it itself supplied the required family.
Control-Q:
  Mumford 1965 explicitly distinguishes the coarse moduli object from a
  universal family and retains automorphisms and maps as data.
same T/u/F/C/Q/I/O/Done:
  T = classification versus represented family; u/F/C/Done are pinned in
  HMZ-Z-001. The alleged Candidate-Q would change Done only if it added a
  naturality requirement not present in the source.
P1:
  Position/formation/consumer present at mathematical-practice layer;
  no active positive obligation that a coarse classification by itself deliver
  the stronger family.
P2:
  No source-supported same-object reentry or pending existence question.
P3:
  Done is made explicit by the source rather than preempted.
X_i / Op / O / Done:
  Input family/moduli data; construct a universal family; inspect the stated
  pullback/mapping property; finish only with that property.
C+:
  The source reports a universal family in the automorphism-free restriction.
C−:
  With nontrivial automorphisms, the source requires particular maps; it does
  not call a coarse object completed delivery.
state:
  Q-R REJECTED_WITH_SCOPE / REAL_CONSUMER_CONTROL.
falsifier/reopen:
  Reopen only with a version-fixed source where the same consumer omits the
  map/marking/coherence data but claims the same Done.
```

## HMZ-Q-002 — Power Set / directness mismatch

```text
Target-Q:
  A genuine R-derived formation question about a ZFC object.
Candidate-Q:
  “Power Set gives all subsets at once, therefore it is the ZFC counterpart of
  a HoTT direct-higher-object motive.”
Control-Q:
  HMZ-S-007 gives a formal formation assertion but no R→Power Set bridge,
  consumer, I/O or Done; HMZ-S-001 uses “directly” with a different scope.
P1:
  L0/L1 (A and P(A) formation) are visible in a proof-formalization source;
  L2 consumer is absent.
P2/P3:
  No source-supported Bind/Form/Bridge/Reenter or admission/Done structure.
same-task:
  FAIL — a claim about direct descriptions of higher objects has been changed
  into a generic all-subsets formation question.
state:
  P_REQUALIFICATION_REQUIRED / NOT_A_Q.
falsifier/reopen:
  A primary source mapping a specified HoTT motive to a specified Power Set
  consumer and preserving the same formation/Done question.
```

## HMZ-Q-003 — `H0 → Z0 → Q0` 首轮传输审计

```text
H0 identity:
  Existing HoTT-side “sameness / universe / higher structure” completion
  phenomenon remains owned by its evidence package; it is not re-proved here.
T0, ZFC first-order object u_Z:
  UNKNOWN. Neither a proper-class slogan nor the phrase “all structures” is a
  permitted object-language replacement.
T1, formation/interface into same-layer use:
  UNKNOWN. Metamath ax-ext/ax-pow supplies formulae, not an H0-analogous interface.
T2, subject/process/observation/Done preservation:
  FAIL/UNFORMED. Structure classification and Power Set questions each alter
  the original higher-sameness completion task.
T3, unpaid completion:
  UNKNOWN. Existing source guards/payments cannot be universalized.
T4, P2/P3 reentry/admission structure:
  UNKNOWN. No source in this denominator provides one.
T5, controls:
  PARTIAL. Mumford and the Book's V construction are anti-analogy controls,
  not a positive transport control.
state:
  TRANSPORT_UNDER_SPECIFIED / Z0=UNKNOWN / Q0=UNFORMED.
reopen:
  Only after a source-defined ZFC consumer preserves H0's subject, process,
  observation and Done through T0–T5.
```

## HMZ-Q-004 — 机器验证不把存在升级为可执行交付

```text
Target-Q:
  A source-defined ZFC use that moves from a proof/existence to a same-agent,
  executable delivery without paying the relevant construction/verification cost.
Candidate-Q:
  “Existing foundations are not suited to proof assistants, so ZFC must make
  this promotion for free.”
Control-Q:
  Voevodsky's motive is a design goal; the source packet does not identify a
  ZFC object, formation or consumer that performs the alleged promotion.
P1/P2/P3:
  Not eligible: C/I/O/Done are absent at the ZFC object level.
state:
  Z_SIDE_UNDER_SPECIFIED / NOT_A_Q.
reopen:
  HMZ-MF-003 must supply a fixed formalization and actual consumer with the
  alleged promotion in its source contract.
```

## HMZ-Q-005 — “任何大范畴”在 ZFC 内不能被陈述

```text
Target-Q:
  Formally state/prove a theorem quantified over a large category in the
  object language of ZFC.
Candidate-Q:
  The foundational theory lacks a first-order class quantifier, so the intended
  statement cannot be formed internally.
Control-Q:
  Shulman gives the exact meta-theorem workaround and a NBG extension with
  class quantification; these are explicit language/scope changes, not hidden
  completion payments.
same T/u/F/C/Q/I/O/Done:
  The target's subject is a formula-defined class / large category. But the
  source says it is not a ZFC object. Replacing it by a meta-level variable or
  an NBG class changes the theory/language at issue.
P1:
  L0 fails for an internal class object; L2 is a theorem-statement use, but it
  lies at the meta-language boundary.
P2/P3:
  No source-supported same-object reentry or formation-before-existence use.
state:
  REPRESENTATION_BOUNDARY / Q-R REJECTED_WITH_SCOPE_AS_P.
reopen:
  A source-defined ZFC-internal consumer must treat the same unformed class
  object as available to a later operator while retaining the same Done.
```

## Round disposition

```text
CANDIDATE_SEED: 0
Q-1/Q-2/Q-3/Q-4: 0
Q-R REJECTED_WITH_SCOPE: 2 (HMZ-Q-001, HMZ-Q-005)
P_REQUALIFICATION_REQUIRED: 1 (HMZ-Q-002)
TRANSPORT_UNDER_SPECIFIED: 1 (HMZ-Q-003)
Z_SIDE_UNDER_SPECIFIED: 1 (HMZ-Q-004)
```

This is a source-bounded result. It does not support “ZFC has no Q”; it only says the frozen first corpus has not
yet paid the conditions needed to put one in the Q lane.
