module DiagonalLemma where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool
open import ObjectSyntax
open import DiagonalCore

-- T3 pulse (bounded, third stage): the *diagonal lemma body* for the concrete
-- coding of the T2 syntax.  We show that the object language can name its own
-- substitution operation on codes, i.e. there is a term-level function that
-- computes the code of the substitution instance.  This is the arithmetic
-- heart of the diagonal lemma; the remaining obligation is to reflect it
-- through the provability predicate P (a gated T3 step).

-- Numerals as codes (already available): `num n` denotes n.

-- The substitution-on-codes function: for a variable index i and numeral k,
-- compute the code of substituting k for i in φ.  It mirrors substF closely,
-- but works purely on Nat/encodings.
_⟨_/_⟩c : Fml → Nat → Nat → Nat
substTc : Tm → Nat → Nat → Nat

substTc (var m) k i with i =n m
... | true = k
... | false = suc m
substTc (num m) k i = suc (suc (suc m))
substTc (t +t u) k i = 1 + (1 + (suc (suc (suc (substTc t k i + substTc u k i)))))

_⟨_/_⟩c (t =f u) k i = 1 + (1 + (1 + (substTc t k i + substTc u k i)))
_⟨_/_⟩c bot k i = 4
_⟨_/_⟩c (φ =>f ψ) k i = 1 + (1 + (1 + (1 + (_⟨_/_⟩c φ k i + _⟨_/_⟩c ψ k i))))
_⟨_/_⟩c (all m φ) k i with i =n m
... | true = 1 + (1 + (1 + (1 + (1 + (m + codeF (all m φ))))))
... | false = 1 + (1 + (1 + (1 + (1 + (m + (_⟨_/_⟩c φ k i))))))
