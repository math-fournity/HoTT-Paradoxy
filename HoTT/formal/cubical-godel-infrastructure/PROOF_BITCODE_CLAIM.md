# Cubical Gödel infrastructure: self-delimiting proof bit code

> Proof ID：`PF-CUBICAL-GODEL-PROOF-BITCODE-001`
> Source：`ProofBitCode.agda`
> Dependencies：`MiniProofChecker.agda`、`ProofSerialization.agda`、`FormulaBitCode.agda`
> Stage：finite binary proof coding; natural-number packing remains open

## Code architecture

The package removes formula-valued payloads from the external proof code in four steps:

1. every formula payload is encoded with `FormulaBitCode.bitsF`;
2. K, S and MP tokens receive distinct two-bit tags;
3. each token's formula payloads are concatenated using the self-delimiting formula parser;
4. a unary token-count prefix tells the total decoder how many tokens to read.

The final `proofBits : RawProof → List Bool` contains only Bool values.

## Exact claims

### `MP-CGI-TOKEN-BIT-ROUNDTRIP-001`

Each formula parse and each tagged token parse preserves its suffix:

```agda
parseFormula-roundtrip :
  parseFormula (bitsF φ ++ rest) ≡b just (parsedFormula φ rest)

parseToken-emit :
  parseToken (emitToken tok rest) ≡b just (parsedToken tok rest)
```

### `MP-CGI-PROOF-BIT-ROUNDTRIP-001`

The token-count and token-list parsers satisfy roundtrip laws, leading to the Path-level raw-proof theorem:

```agda
decodeTokenList-roundtrip :
  decodeTokenList (tokenListBits toks)
  ≡b just (decodedTokenList toks [])

decodeProofBits-roundtrip : (p : RawProof)
  → decodeProofBits (proofBits p) ≡ just p
```

`≡b` is Agda's inductive equality for parser computation; `decodeProofBits-roundtrip` converts the parser equality into a Cubical Path and composes it with the postfix proof decoder theorem.

### `MP-CGI-PROOF-BIT-CHECK-001`

The checker on finite Bool code agrees with the raw checker:

```agda
checkProofBits-roundtrip : (p : RawProof) (φ : Fml)
  → checkProofBits (proofBits p) φ ≡ checkAgainst p φ
```

Accepted bit code is sound, and every indexed derivation produces accepted bit code:

```agda
BitChecked φ = Σ[ bits ∈ List Bool ] checkProofBits bits φ ≡ true

bitChecked-sound : BitChecked φ → ⊢ φ
derives→bitChecked : ⊢ φ → BitChecked φ
```

### `MP-CGI-PROOF-BIT-CONTROLS-001`

The encoded K proof is accepted and the encoded ill-matched MP tree is rejected:

```agda
positiveBits-accepted : ... ≡ true
negativeBits-rejected : ... ≡ false
```

## Remaining obligations

- Define `packBits : List Bool → ℕ` and a total `unpackBits : ℕ → List Bool` with a proved roundtrip on encoded lists.
- Define `codeProof = packBits ∘ proofBits`, a total decoder and a checker directly on natural-number codes.
- Prove checker-code commutation and finite-code enumeration coverage.
- Extend the object language to sufficient arithmetic or instantiate a synthetic incompleteness theorem.
- Prove object-level representability of coding, substitution and proof checking.
- Construct the diagonal sentence and prove its unprovability under exact conditions.

## Prohibited extrapolation

This package has a genuine finite binary proof code and total decoder. It does not yet supply a natural-number Gödel numbering, an enumerator that covers all proof codes, object-level representability, a Gödel/Rosser sentence or an incompleteness theorem. The coding and checker use no specifically higher-dimensional theorem.
