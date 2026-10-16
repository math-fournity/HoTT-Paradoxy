# Cubical Gödel infrastructure: natural-number proof codes

> Proof ID：`PF-CUBICAL-GODEL-NAT-PROOF-CODE-001`
> Source：`NatProofCode.agda`
> Dependencies：`MiniProofChecker.agda`、`ProofSerialization.agda`、`FormulaBitCode.agda`、`ProofBitCode.agda`
> Stage：external natural-number coding of the finite proof relation; object-level arithmetic representability remains open

## Code architecture

The package turns the self-delimiting proof bit stream into a natural-number code without assuming an abstract Gödel numbering. It defines the representation explicitly:

```text
codeBits []          = 1
codeBits (false ∷ s) = 2 · codeBits(s)
codeBits (true  ∷ s) = 2 · codeBits(s) + 1
```

The implementation uses primitive recursive `twice`, `pack`, `parity`, `half`, and a fuel-bounded `unbits`. The terminal value `1` distinguishes the end of the finite list. For decoding a candidate natural number `c`, `unbits c c` is always finite; the earlier self-delimiting proof parser consumes the proof prefix and may leave an irrelevant suffix.

## Exact claims

### `MP-CGI-PROOF-PREFIX-001`

The proof-bit format remains decodable when arbitrary bits follow a well-formed proof code. Token emission distributes over an appended suffix, and token-list, proof, and checker decoding preserve the intended prefix:

```agda
decodeTokenList-prefix : (toks : List Token) (rest : List Bool)
  → decodeTokenList (tokenListBits toks ++ rest)
  ≡b just (decodedTokenList toks rest)

decodeProofBits-prefix : (p : RawProof) (rest : List Bool)
  → decodeProofBits (proofBits p ++ rest) ≡ just p

checkProofBits-prefix : (p : RawProof) (rest : List Bool) (φ : Fml)
  → checkProofBits (proofBits p ++ rest) φ ≡ checkAgainst p φ
```

### `MP-CGI-BIT-NAT-ROUNDTRIP-001`

The parity and halving operations invert one `pack` step. Reading exactly the length of an encoded finite bit string recovers that string, while the numerical code strictly dominates its bit length:

```agda
unbits-code : (bs : List Bool)
  → unbits (LEN bs) (codeBits bs) ≡ bs

codeBits-dominates : (bs : List Bool)
  → suc (LEN bs) ≤ codeBits bs

unbits-split : (i j c : ℕ)
  → unbits (i + j) c
  ≡ unbits i c ++ unbits j (halfs i c)
```

These facts justify using the code itself as a terminating decoding bound: it contains the original bit string as a prefix, followed by a finite suffix.

### `MP-CGI-NAT-PROOF-ROUNDTRIP-001`

Every raw proof has an explicit natural-number code. The total decoder recovers every encoded proof, and the coding function is injective:

```agda
codeProof : RawProof → ℕ
decodeProofNat : ℕ → Maybe RawProof

codeProof-roundtrip : (p : RawProof)
  → decodeProofNat (codeProof p) ≡ just p

codeProof-injective : (p q : RawProof)
  → codeProof p ≡ codeProof q → p ≡ q
```

The decoder is total on every natural number, although arbitrary numbers need not be canonical images of `codeProof`.

### `MP-CGI-NAT-PROOF-CHECK-001`

The proof checker on natural-number codes agrees with the raw checker on every encoded proof:

```agda
checkProofNat-code : (p : RawProof) (φ : Fml)
  → checkProofNat (codeProof p) φ ≡ checkAgainst p φ
```

Accepted natural-number codes are sound for the indexed derivation relation, and every indexed derivation yields an accepted natural-number code:

```agda
NatChecked φ = Σ[ c ∈ ℕ ] checkProofNat c φ ≡ true

natChecked-sound : NatChecked φ → ⊢ φ
derives→natChecked : ⊢ φ → NatChecked φ
```

Thus this particular external metatheory now has a concrete total relation `checkProofNat : ℕ → Fml → Bool` whose existential acceptance corresponds in both directions to its derivability relation.

### `MP-CGI-NAT-PROOF-CONTROLS-001`

The natural-number code of a minimal K proof is accepted, while natural number `0`, which does not decode to a proof, is rejected:

```agda
positiveNatCode-accepted : ... ≡ true
negativeNatCode-rejected : ... ≡ false
```

## Remaining obligations

- Extend or instantiate an object language with enough arithmetic to express the relevant coding functions and proof relation.
- Prove object-level representability of formula coding, substitution, proof checking, and the existential provability predicate.
- Establish the exact substitution-on-code operation needed by diagonalization.
- Construct and verify a fixed-point sentence.
- State and prove the final Gödel or Rosser theorem under exact consistency, soundness, effective axiomatizability, and strength assumptions.
- If the intended conclusion concerns HoTT itself, identify an exact effective HoTT calculus and prove that the metatheoretic coding and theorem apply to it.
- Separately build the reality-correspondence argument required for a reality-relative nonreality claim.

## Prohibited extrapolation

This package supplies a genuine natural-number representation and total checker for one small Hilbert proof system. The negative control checks malformed numeric input; rejection of an encoded ill-matched modus-ponens proof was already established at the preceding bit-code layer. It does not prove that the object language internally represents that checker, that theoremhood is decidable, that the theory is incomplete, that a Gödel sentence exists, or that HoTT has a contradiction or a theory-specific defect. Its coding and checker use no specifically higher-dimensional theorem. The result remains `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` until the project branch is versioned under separate authorization.
