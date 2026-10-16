# Cubical synthetic incompleteness: explicit conditional Gödel–Rosser core

> Proof ID：`PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001`
> Source：`SyntheticIncompleteness.agda`
> Theory：Cubical Agda 2.8.0 with Cubical library v0.9
> Status：conditional abstract theorem; no concrete HoTT calculus is instantiated

## Source relationship

The construction is a Cubical Agda adaptation of the synthetic computational route in Dominik Kirst and Benjamin Peters, *Gödel’s Theorem Without Tears: Essential Incompleteness in Synthetic Computability*, CSL 2023, especially Definitions 7, 17, 18, Fact 19 and Theorem 20. The accompanying Coq implementation was inspected at `uds-psl/coq-synthetic-incompleteness`, commit `cd7d8490f8542bfe85658c465bcb26b2ed163f53`, principally `utils.v`, `epf.v`, `formal_systems.v`, and `abstract_incompleteness.v`.

No originality claim is made for the mathematical diagonal argument. This package makes its assumptions and completion behavior explicit in the current Cubical Agda evidence system.

## Computational interface

`PartBool` is a deterministic, step-indexed partial Boolean computation:

```agda
record PartBool : Type₁ where
  field
    core : ℕ → OptionBool
    deterministic : (b₁ b₂ : Bool) (k₁ k₂ : ℕ)
      → core k₁ ≡ some b₁ → core k₂ ≡ some b₂ → b₁ ≡ b₂

p ⇓ b = Σ[ k ∈ ℕ ] core p k ≡ some b
Diverges p = (b : Bool) → ¬ (p ⇓ b)
```

This is deliberately not an arbitrary convergence relation. A successful computation has a finite stage witness, matching the step-indexed partial-function representation used in the cited Coq development.

`Universal θ` is an explicit Church-thesis-style hypothesis:

```agda
Universal θ =
  (f : ℕ → PartBool) →
  Σ[ c ∈ ℕ ] ((x : ℕ) (b : Bool) → (f x ⇓ b) ↔ (θ c x ⇓ b))
```

The source does not construct a term of `Universal θ`. Every theorem taking it as an argument is conditional on that exact assumption.

## Exact claims

### `MP-CSI-PARTIAL-BOOL-001`

`flipPart` interchanges successful `true` and `false` outcomes while preserving deterministic partial computation. The derived `runs-deterministic` proves that one `PartBool` cannot converge to two different Boolean values.

### `MP-CSI-SEPARATOR-DIVERGENCE-001`

For `SelfReturns θ b x = θ x x ⇓ b`, any partial computation family that returns `b` whenever the universal machine with code/input `x` returns `b` must diverge at a specifically constructed index:

```agda
separator-diverges :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → (f : ℕ → PartBool)
  → SeparatesSelfReturns θ f
  → Σ[ c ∈ ℕ ] Diverges (f c)
```

The proof applies universality to the Boolean-flipped family, obtains its code `c`, and diagonalizes at input `c`. `no-total-separator` derives the corresponding impossibility of a total separating family.

### `MP-CSI-EFFECTIVE-SYSTEM-001`

`FormalSystem S neg` carries an object-level derivability family and a deterministic partial classifier. Convergence to `true` corresponds in both directions to a proof of `s`; convergence to `false` corresponds in both directions to a proof of `neg s`. `classifier-consistent` therefore derives that `s` and `neg s` cannot both be derivable.

### `MP-CSI-INDEPENDENT-SENTENCE-001`

If a formal system strongly separates the universal self-return-`true` and self-return-`false` predicates, the diagonal divergence theorem yields a concrete index whose represented sentence has neither a proof nor a proof of its negation:

```agda
synthetic-incompleteness :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → (fs : FormalSystem S neg)
  → (r : ℕ → S)
  → StronglySeparates fs (SelfReturns θ true) (SelfReturns θ false) r
  → Σ[ c ∈ ℕ ] Independent fs (r c)
```

`synthetic-not-complete` additionally proves that the system cannot satisfy the data-bearing constructive completeness interface `Complete fs`.

### `MP-CSI-ESSENTIAL-INCOMPLETENESS-001`

Strong separation transports from a base system to every extension on the same sentence type and negation operation. Consequently:

```agda
synthetic-essential-incompleteness :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → (base extension : FormalSystem S neg)
  → Extends base extension
  → (r : ℕ → S)
  → StronglySeparates base (SelfReturns θ true) (SelfReturns θ false) r
  → Σ[ c ∈ ℕ ] Independent extension (r c)
```

The result is “essential” only relative to these explicit extension and strong-separation hypotheses.

## What the constructed non-completion means

The package does more than refute a total Boolean decider abstractly. Given the universal-code hypothesis and a proposed separating classifier, `separator-diverges` returns an index `c` and proves that the classifier has neither Boolean result at `c`. When that classifier is the proof/refutation classifier of a strongly separating formal system, `r c` is independent. This is the exact point at which a completion claim becomes a non-completing classification process.

## Remaining instantiation obligations

- Construct or assume a model-specific `θ` and prove `Universal θ`. The current file only quantifies over it.
- Instantiate `FormalSystem` with an exact, effectively presented object calculus.
- Build its proof/refutation classifier from a proof-code enumeration and prove both classifier correspondences.
- Prove strong separation for the two self-return predicates. For arithmetic, this is the representability burden; for a HoTT claim, it must be proved for an exact HoTT calculus.
- Relate the represented sentence and classification task to the user’s reality-relative task without changing input, observation, or completion criterion.

## Prohibited extrapolation

This package does not construct Church’s thesis, prove that it holds in ordinary Cubical Agda, instantiate Robinson arithmetic, produce a self-coded HoTT syntax, or prove HoTT itself incomplete. It uses no univalence theorem, higher inductive type, truncation, or specifically higher-dimensional argument. Its significance for HoTT is that the conditional theorem type-checks in a Cubical setting and exposes the exact missing instantiation interfaces. The package does not establish a contradiction, a HoTT-specific cause, or a reality-relative nonreality paradox. Until committed under separate authorization, its evidence status is `MACHINE_PROVED_LOCAL_UNCOMMITTED`.
