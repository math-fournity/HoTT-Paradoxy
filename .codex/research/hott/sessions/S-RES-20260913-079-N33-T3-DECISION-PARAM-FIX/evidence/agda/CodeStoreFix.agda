module CodeStoreFix where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma

-- T3 seventh pulse (bounded): the *corrected* code-level substitution, per the
-- N27 finding.  In the corrected reading the substitution stores the *code* of
-- the numeral rather than the numeral itself, so that the code level and the
-- syntax level agree.  We implement the corrected term-level function and
-- machine-check the cases that are definitional.

-- codeT (num n) = 5 + n in the DiagonalCore coding; make that transparent.
code-num : (n : Nat) → codeT (num n) ≡ 3 + n
code-num n = refl

-- Corrected substitution on term codes: for the matching variable we store the
-- code of the numeral (i.e. 5 + k), which is exactly what the syntax does.
substFixT : Nat → Nat → Tm → Nat
substFixT k i (var m) with i =n m
... | true = 3 + k
... | false = suc m
substFixT k i (num m) = suc (suc (suc m))
substFixT k i (t +t u) = 1 + (1 + (suc (suc (suc (substFixT k i t + substFixT k i u)))))

-- The matching-variable case now agrees with the syntax level, definitionally.
fix-var-self : (k i : Nat)
  → substFixT k i (var i) ≡ codeT (substT k i (var i))
fix-var-self k i rewrite =n-refl i = refl

-- The non-matching case keeps the original variable on both sides.
fix-var-het : (k i m : Nat) (p : i =n m ≡ false)
  → substFixT k i (var m) ≡ codeT (substT k i (var m))
fix-var-het k i m p rewrite p = refl

-- The numeral case: both sides leave the numeral untouched.
fix-num : (k i m : Nat) → substFixT k i (num m) ≡ codeT (substT k i (num m))
fix-num k i m = refl
