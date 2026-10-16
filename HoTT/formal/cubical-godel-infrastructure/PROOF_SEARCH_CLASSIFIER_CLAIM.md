# Cubical Gödel infrastructure: exhaustive proof/refutation classifier

> Proof ID：`PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001`
> Source：`ProofSearchClassifier.agda`
> Dependencies：the five files from `PF-CUBICAL-GODEL-*` plus `../cubical-synthetic-incompleteness/SyntheticIncompleteness.agda`
> Stage：effective formal-system classifier instantiated; universality and strong separation remain open

## Search interpretation

For a supplied formula `φ`, stage `n` checks natural-number proof code `n` against `φ` and against `negF φ = φ ⇒ bot`:

```agda
proofCore : Fml → ℕ → OptionBool
proofCore φ code with checkProofNat code φ | checkProofNat code (negF φ)
... | true  | negative = some true
... | false | true     = some false
... | false | false    = none
```

One stage checks one code. The step-indexed convergence relation existentially quantifies over stages, so every natural code is eventually considered. The core is not required to retain earlier results at later stages; `PartBool` only requires all successful stages to agree, which is proved from consistency of the object calculus.

## Exact claims

### `MP-CGI-SEMANTIC-CONSISTENCY-001`

`evalF` interprets atoms under any Boolean valuation, `bot` as `false`, and implication by Boolean implication. The K and S axioms are valid for all Boolean inputs and modus ponens preserves truth. Therefore every indexed derivation evaluates to `true` under every valuation, `bot` is not derivable, and no formula and its `negF` are both derivable:

```agda
derivation-valid : ⊢ φ → (valuation : ℕ → Bool) → evalF valuation φ ≡ true
no-bot : ⊢ bot → ⊥
no-proof-and-refutation : ⊢ φ → ⊢ negF φ → ⊥
```

This is a semantic consistency proof for the exact K/S/MP calculus in `MiniProofChecker.agda`.

### `MP-CGI-PROOF-CORE-001`

The stage function is sound and complete in each direction:

```agda
core-true→check     : proofCore φ code ≡ some true
                   → checkProofNat code φ ≡ true
core-false→check-neg : proofCore φ code ≡ some false
                    → checkProofNat code (negF φ) ≡ true
check→core-true     : checkProofNat code φ ≡ true
                   → proofCore φ code ≡ some true
check-neg→core-false : checkProofNat code (negF φ) ≡ true
                    → proofCore φ code ≡ some false
```

The last direction uses semantic consistency to rule out simultaneous positive and negative acceptance when positive checking has precedence.

### `MP-CGI-PROOF-CLASSIFIER-001`

`proofCore-deterministic` proves that successful stages cannot disagree, even when they use different natural-number codes. It therefore supplies a genuine `PartBool`:

```agda
proofClassifier : Fml → PartBool
```

Its successful outcomes correspond exactly to derivability and refutability:

```agda
proof-runs-true          : ⊢ φ → proofClassifier φ ⇓ true
true-runs-proof          : proofClassifier φ ⇓ true → ⊢ φ
refutation-runs-false    : ⊢ negF φ → proofClassifier φ ⇓ false
false-runs-refutation    : proofClassifier φ ⇓ false → ⊢ negF φ
```

### `MP-CGI-FORMAL-SYSTEM-INSTANCE-001`

The small K/S/MP calculus now inhabits the exact effective-system interface used by `PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001`:

```agda
HilbertSystem : FormalSystem Fml negF
```

`hilbert-consistent` is independently recovered through the classifier interface. Thus the `FormalSystem`/classifier parameter of the conditional synthetic theorem has a concrete instance for this calculus.

## Remaining obligations

- `Universal θ` is still not instantiated.
- There is no `r : ℕ → Fml` proving that this K/S/MP calculus strongly separates the two universal self-return predicates. With only K and S axioms, arbitrary atoms are not derivable, so the needed representability is absent.
- The object language has no arithmetic relation symbols or quantifiers and cannot yet express the usual representability theorem.
- No fixed-point sentence or incompleteness theorem for `HilbertSystem` follows from this package alone.
- No exact HoTT calculus or reality-correspondence task is instantiated.

## Prohibited extrapolation

This package proves exhaustive semi-search for proofs and refutations of one supplied formula, not a total theoremhood decider. When neither side is derivable, `proofClassifier φ` has no successful stage; the source does not decide that negative fact by finite search. It removes the effective-classifier parameter from the current small-calculus route but does not remove `Universal` or strong separation. It uses no specifically higher-dimensional theorem. The evidence status is `MACHINE_PROVED_LOCAL_UNCOMMITTED` until version closure is authorized.
