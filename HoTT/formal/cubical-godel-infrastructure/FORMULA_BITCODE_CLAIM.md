# Cubical Gödel infrastructure: self-delimiting formula bit code

> Proof ID：`PF-CUBICAL-GODEL-FORMULA-BITCODE-001`
> Source：`FormulaBitCode.agda`
> Dependencies：`MiniProofChecker.agda`、`ProofSerialization.agda`
> Stage：finite-alphabet formula coding; token/proof numerical coding remains open

## Code

The formula code uses a finite Bool alphabet:

```text
atom n  ↦  false · trueⁿ · false
bot     ↦  true · false
φ ⇒ ψ   ↦  true · true · bitsF(φ) · bitsF(ψ)
```

The atom payload is self-delimiting unary. The implication children are parseable sequentially because each formula code is self-delimiting.

## Exact claims

### `MP-CGI-FML-BIT-LENGTH-001`

`STEPS` is exactly the bit length of the code:

```agda
bits-length : (φ : Fml) → LEN (bitsF φ) ≡b STEPS φ
```

The file also proves the list-append and arithmetic identities used by the parser.

### `MP-CGI-FML-PARSER-001`

The parser is a total finite-fuel state machine. `close` uses an explicit continuation stack for the right child of implication. For every formula, pending stack, suffix and remaining fuel:

```agda
parse-run :
  (φ : Fml) (stk : Stack) (rest : List Bool) (fuel : ℕ)
  → run (wantFml stk) (STEPS φ + fuel) (bitsF φ ++ rest)
  ≡b resume (close φ stk) rest fuel
```

The atom-index submachine has its own accumulator theorem `index-run`.

### `MP-CGI-FML-BIT-ROUNDTRIP-001`

Prefix parsing preserves any suffix, and exact decoding returns the original formula:

```agda
parsePrefix-roundtrip : (φ : Fml) (rest : List Bool)
                      → parsePrefix (bitsF φ ++ rest)
                      ≡b res φ rest true

decodeF-roundtrip : (φ : Fml) → decodeF (bitsF φ) ≡b φ
decodeF-ok : (φ : Fml) → rOk (parsePrefix (bitsF φ)) ≡b true
```

Here `≡b` is Agda's inductive equality used for the parser's computation laws; the surrounding module is checked in the same Cubical Agda environment as the Path-based proof checker.

## Remaining obligations

- `Token` still carries `Fml` payloads directly.
- Token tags and formula payloads must be encoded into Bool lists and parsed.
- A proof sequence needs a self-delimiting token count or equivalent termination discipline.
- The resulting finite Bool list must be connected to a natural-number code with a total decoder.
- Checker-on-code commutation and proof-code enumeration remain open.
- Object-level arithmetic representability, diagonalization and incompleteness remain open.

## Prohibited extrapolation

This package proves a finite, prefix-decodable formula representation. It does not prove a Gödel numbering into ℕ, proof coding, enumerability of theoremhood, representability in the object theory, a fixed-point sentence or any incompleteness result.
