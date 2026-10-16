# Cubical Gödel infrastructure: a checkable proof relation

> Proof ID：`PF-CUBICAL-GODEL-PROOF-CHECKER-001`
> Theory：Cubical Agda 2.8.0 with Cubical library v0.9
> Source：`MiniProofChecker.agda`
> Stage：Gödel infrastructure only; no incompleteness sentence is claimed

## Object language and derivability

The file defines a small propositional object language:

```agda
data Fml : Type where
  atom : ℕ → Fml
  bot : Fml
  _⇒_ : Fml → Fml → Fml
```

and an indexed Hilbert derivation relation with K, S and modus ponens. `RawProof` is an unindexed proof tree. Its modus-ponens node stores the intended antecedent and consequent; the total Bool function `check` verifies recursively that both subtrees check and that their computed conclusions have the required shapes.

## Exact claims

### `MP-CGI-EQUALITY-001`

`eqNat` and `eqF` are reflexive and sound:

```agda
eqNat-refl  : (n : ℕ) → eqNat n n ≡ true
eqNat-sound : (m n : ℕ) → eqNat m n ≡ true → m ≡ n
eqF-refl    : (φ : Fml) → eqF φ φ ≡ true
eqF-sound   : (φ ψ : Fml) → eqF φ ψ ≡ true → φ ≡ ψ
```

### `MP-CGI-CHECK-SOUND-001`

Every accepted raw proof yields an indexed object derivation of its computed conclusion:

```agda
check-sound : (p : RawProof) → check p ≡ true → ⊢ conclusion p

checkAgainst-sound : (p : RawProof) (φ : Fml)
                   → checkAgainst p φ ≡ true → ⊢ φ
```

### `MP-CGI-CHECK-COMPLETE-001`

Every indexed derivation can be erased to an accepted raw proof with the same conclusion:

```agda
erase : {φ : Fml} → ⊢ φ → RawProof
conclusion-erase : {φ : Fml} (d : ⊢ φ) → conclusion (erase d) ≡ φ
check-erase : {φ : Fml} (d : ⊢ φ) → check (erase d) ≡ true
checkAgainst-erase : {φ : Fml} (d : ⊢ φ)
                   → checkAgainst (erase d) φ ≡ true
```

Consequently there are total maps in both directions between `⊢ φ` and the checked proof package:

```agda
Checked φ = Σ[ p ∈ RawProof ] checkAgainst p φ ≡ true

derives→checked : ⊢ φ → Checked φ
checked→derives : Checked φ → ⊢ φ
```

No claim of path-level equivalence between the two proof types is made.

### `MP-CGI-TRUNCATED-PROVABILITY-001`

Provability is represented as mere existence of a checked proof:

```agda
Provable φ = ∥ Checked φ ∥₁

derives→provable : ⊢ φ → Provable φ
provable→mereDerives : Provable φ → ∥ ⊢ φ ∥₁
```

This fixes the relationship between proof-relevant derivations, decidable checking of one supplied raw proof, and propositionally truncated existence of some proof.

### `MP-CGI-CONTROLS-001`

One K-axiom raw proof is accepted, while an ill-matched modus-ponens tree is rejected:

```agda
kRaw-checks : checkAgainst kRaw (zeroAtom ⇒ (oneAtom ⇒ zeroAtom)) ≡ true
badMp-rejected : check badMp ≡ false
```

## Why this matters for the Gödel route

Gödel/Rosser needs a proof predicate whose *individual proof relation* is effectively checkable. This package supplies that layer for a small object logic and proves soundness/completeness relative to its indexed derivations. It also preserves the HoTT distinction between a concrete proof object and the mere proposition that some proof exists.

The next obligations are separate:

1. a finite, decodable code for `Fml` and `RawProof`;
2. a proof that the checker on codes represents the same relation;
3. an object language with enough arithmetic or another proved incompleteness hypothesis;
4. internal representability of coding, substitution and proof checking;
5. a diagonal/fixed-point sentence;
6. consistency or Rosser conditions and the actual unprovability theorem;
7. a later instantiation to an exact effective HoTT calculus if the claim is about HoTT itself.

## Assumptions and prohibited extrapolation

- The source introduces no postulate.
- It uses Cubical library propositional truncation, but no univalence theorem or higher path computation is needed for the proof-checker mechanism.
- The result does not prove that `Provable φ` is decidable. Deciding `checkAgainst p φ` for a supplied `p` is different from finding some `p`.
- It does not prove theoremhood undecidable, theory incomplete, a Gödel sentence independent, or HoTT inconsistent.
- It does not encode the proof assistant's own syntax or checking relation.
- It does not establish a reality correspondence or a HoTT-specific nonreality mechanism.
