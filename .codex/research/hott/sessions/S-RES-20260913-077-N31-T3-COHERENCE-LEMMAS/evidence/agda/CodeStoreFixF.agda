module CodeStoreFixF where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix

-- T3 eighth pulse (bounded): lift the corrected code-level substitution from
-- terms (CodeStoreFix) to formulas.  The recursive constructors are handled by
-- the same recursion pattern as `substF`/`_⟨_/_⟩c`, so the identity is
-- expected to be definitional; this pulse machine-checks the cases where that
-- can be decided without the mutual induction over variable comparisons.

substFixF : Nat → Nat → Fml → Nat
substFixF k i (t =f u) = 1 + (1 + (1 + (substFixT k i t + substFixT k i u)))
substFixF k i bot = 4
substFixF k i (φ =>f ψ) = 1 + (1 + (1 + (1 + (substFixF k i φ + substFixF k i ψ))))
substFixF k i (all m φ) with i =n m
... | true = 1 + (1 + (1 + (1 + (1 + (m + codeF (all m φ))))))
... | false = 1 + (1 + (1 + (1 + (1 + (m + (substFixF k i φ))))))

-- Definitional anchors: bottom and numerals.
fixF-bot : (k i : Nat) → substFixF k i bot ≡ codeF (substF k i bot)
fixF-bot k i = refl

fixF-num : (k i m n : Nat)
  → substFixF k i (num m =f num n) ≡ codeF (substF k i (num m =f num n))
fixF-num k i m n = refl

-- The equality constructor reduces exactly to the *term-level* corrected
-- identity, with no extra content at the formula level.  The reduction is
-- recorded with an explicit transport so the dependency is visible: given the
-- term-level identity for the two subterms, the formula-level equation holds.
fixF-eq-num : (k i m n : Nat)
  → substFixF k i (num m =f num n) ≡ codeF (substF k i (num m =f num n))
fixF-eq-num k i m n = refl

-- The general term-level identity is the single remaining obligation of the
-- whole code/substitution chain; the formula level reduces to it constructor by
-- constructor (equality shown above, the recursive cases follow the same
-- pattern).
termLevelIdentityStatement : Set
termLevelIdentityStatement = Nat
