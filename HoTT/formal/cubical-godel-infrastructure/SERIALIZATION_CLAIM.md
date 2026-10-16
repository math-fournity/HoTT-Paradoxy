# Cubical Gödel infrastructure: postfix proof serialization

> Proof ID：`PF-CUBICAL-GODEL-PROOF-SERIALIZATION-001`
> Source：`ProofSerialization.agda`
> Dependency：`MiniProofChecker.agda`
> Stage：finite structural serialization; numerical Gödel coding remains open

## Exact claims

### `MP-CGI-SERIALIZE-ROUNDTRIP-001`

`emit` serializes a `RawProof` into a postfix sequence of K/S/MP tokens. The parser `run` uses an explicit proof stack and consumes one token at a time. For every proof, suffix and initial stack:

```agda
run-emit : (p : RawProof) (rest : List Token) (stack : Stack)
         → run (emit p rest) stack ≡ run rest (p ∷ stack)
```

Consequently:

```agda
decode-serialize : (p : RawProof) → decode (serialize p) ≡ just p
```

### `MP-CGI-SERIALIZED-CHECK-001`

Checking a serialized proof agrees with checking the original raw proof:

```agda
checkSerialized-serialize : (p : RawProof) (φ : Fml)
                          → checkSerialized (serialize p) φ
                          ≡ checkAgainst p φ
```

An accepted serialized code yields an indexed derivation; every indexed derivation yields an accepted serialized code:

```agda
checkSerialized-sound : checkSerialized code φ ≡ true → ⊢ φ

SerializedChecked φ = Σ[ code ∈ List Token ] checkSerialized code φ ≡ true

derives→serialized : ⊢ φ → SerializedChecked φ
serialized→derives : SerializedChecked φ → ⊢ φ
```

### `MP-CGI-SERIALIZED-CONTROLS-001`

The serialized K proof is accepted and the serialized ill-matched MP tree is rejected:

```agda
positiveCode-accepted :
  checkSerialized positiveCode (zeroAtom ⇒ (oneAtom ⇒ zeroAtom)) ≡ true

negativeCode-rejected : checkSerialized negativeCode oneAtom ≡ false
```

## Role and remaining obligations

This package replaces a recursive proof tree by a finite sequential representation with a total stack parser and a proved roundtrip. That is one step toward an enumerable proof predicate.

The token type still embeds formulas directly:

```agda
data Token : Type where
  tokK : Fml → Fml → Token
  tokS : Fml → Fml → Fml → Token
  tokMp : Fml → Fml → Token
```

Therefore this is not yet a Gödel numbering. The next package must serialize formula payloads into a self-delimiting finite alphabet or natural numbers, prove token/list decoding, and connect that numeric checker to `checkSerialized`.

## Prohibited extrapolation

- A finite `List Token` whose tokens contain `Fml` is not a natural-number code.
- No enumeration completeness theorem is claimed.
- No proof-search termination or theoremhood decision procedure is claimed.
- No object-level representability, diagonal sentence, Gödel/Rosser theorem, HoTT self-encoding or reality correspondence is claimed.
