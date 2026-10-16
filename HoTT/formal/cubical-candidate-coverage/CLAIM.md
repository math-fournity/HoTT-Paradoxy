# PF-CUBICAL-CANDIDATE-COVERAGE-001

> Status before canonical capture: `FORMAL_SOURCE_CANDIDATE`  
> Theory: Cubical Agda with native Path, using the existing R041 `Delay Bool` semantics  
> Intended run: `20260914-CUBICAL-CANDIDATE-COVERAGE-001`

## Exact scope

This package gives a class-relative completeness certificate for a fixed
bounded completion-search language. For every natural-number bound `n`, the
indexed type `Raw n` contains precisely the following declared grammar:

```text
never
now false
now true
laterR r, where r : Raw n-1
```

The finite list `allRaw n` enumerates every inhabitant of `Raw n`. A
normalization function maps this explicit syntax to the canonical R041
representation `Delay Bool = ω | ret k b`. The raw and canonical semantics are
stated independently for convergence and deadline observation, and their
equality/equivalence is proved with Cubical Path.

For a fixed task horizon and expected observation, `candidateSpace` enumerates
all raw candidates. `reduceCandidate` retains the horizon and expected result,
normalizes only the program, preserves the deadline observation, and every
reduced candidate occurs in `canonicalSpace`.

## Claims

### MP-CCC-RAW-ENUMERATION-001

```text
(r : Raw n) → r ∈ allRaw n
```

The structural recursion is a coverage proof for this exact indexed grammar.
Cubical Agda accepts this theorem and emits its standard
`UnsupportedIndexedMatch` warning because the definition pattern-matches on
the `ℕ` index. Consequently, the package does not claim judgemental reduction
of `allRaw-complete` when its argument is hidden behind a transported indexed
value; the logical coverage theorem and all constructor-generated controls are
kernel accepted.

### MP-CCC-NORMALIZATION-SEMANTICS-001

For every bounded raw program, Boolean value and deadline:

```text
RawConv r b ⇔ Conv (normalize r) b
rawDeadline k r ≡ deadline k (normalize r)
```

Thus normalization preserves both eventual result evidence and the declared
finite completion observation.

### MP-CCC-TASK-PRESERVATION-001

For every candidate, reduction preserves its task horizon, expected
observation and actual deadline observation:

```text
canonicalHorizon (reduceCandidate c) ≡ rawHorizon c
canonicalExpected (reduceCandidate c) ≡ rawExpected c
rawObservation c ≡ canonicalObservation (reduceCandidate c)
```

### MP-CCC-REDUCED-COVERAGE-001

For every fixed horizon/expected pair and every `r : Raw n`:

```text
reduceCandidate (candidate k expected r)
  ∈ canonicalSpace n k expected
```

This is the exact denominator-relative link between normalization and the
generated canonical search space.

### MP-CCC-CONTROLS-001

The package checks membership of immediate and one-step-delayed returns,
distinguishes too-early from on-time deadline observations, checks divergence,
and confirms that `laterR never` normalizes to canonical `ω`.

## Prohibited extrapolation

- The theorem covers the declared `Raw n` grammar only. It does not cover all
  HoTT terms, all partial programs, arbitrary consumers, unbounded syntax or
  future grammar extensions.
- The fixed consumer is `deadline`; no theorem states that normalization
  preserves every context, race, quotient, higher inductive eliminator or
  proof-search behavior.
- The proofs use native Cubical Path and the existing Cubical partiality model,
  but they do not establish that the phenomenon is caused by univalence, HITs,
  higher paths or HoTT rather than ordinary typed computation.
- The accepted indexed coverage proof carries one retained
  `UnsupportedIndexedMatch` diagnostic. No consumer in this package evaluates
  it on a transported `Raw` value, and no computational claim about that case
  is made.
- The preserved task fields are a formal TaskSpec identity. They are not an
  empirical or philosophical proof that this task models physical reality.
- This package is a first machine-checked `COMP-2` and task-preserving reduction
  slice. It does not establish `COMP-4` for the full HoTT paradox candidate
  class, `COMP-5` for an exact HoTT-to-reality mechanism chain, or `COMP-6`
  global discovery completeness.
