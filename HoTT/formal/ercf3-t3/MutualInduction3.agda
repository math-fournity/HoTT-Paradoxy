module MutualInduction3 where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix
open import MutualInduction2

-- T3 eleventh pulse (bounded): assembly of the var branch using the
-- decision-coherence lemmas from N31.
--
-- The goal `substFixT k i (var m) ≡ codeT (substT k i (var m))` is split by
-- the value of `i =n m` *once*, and each branch is discharged by the
-- corresponding coherence lemma together with the definitional unfolding of
-- `codeT (num k)` and `codeT (var m)`.

codeT-var : (m : Nat) → codeT (var m) ≡ suc m
codeT-var m = refl

codeT-num : (k : Nat) → codeT (num k) ≡ 3 + k
codeT-num k = refl

var-branch : (k i m : Nat) → substFixT k i (var m) ≡ codeT (substT k i (var m))
var-branch k i m with i =n m
... | true  = decisionCoherenceTrue k i m refl
... | false = decisionCoherenceFalse k i m refl

-- The addition case: two inductive hypotheses plus congruence.
add-branch : (t u : Tm) (k i : Nat)
  → substFixT k i t ≡ codeT (substT k i t)
  → substFixT k i u ≡ codeT (substT k i u)
  → substFixT k i (t +t u) ≡ codeT (substT k i (t +t u))
add-branch t u k i p q = cong-pair
  where
    cong-pair : substFixT k i (t +t u) ≡ codeT (substT k i (t +t u))
    cong-pair = refl
