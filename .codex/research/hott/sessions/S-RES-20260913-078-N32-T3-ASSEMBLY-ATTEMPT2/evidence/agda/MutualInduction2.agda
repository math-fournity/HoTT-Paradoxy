module MutualInduction2 where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix

-- T3 tenth pulse (bounded): continue the with-abstraction alignment.
--
-- The blocker recorded in N30 is that `substFixT` matches `i =n m` directly,
-- while `codeT (substT ...)` matches the same decision through a nested `if`.
-- This pulse pins the *exact* coherence condition that would close the gap:
-- the code-level function must place, in the substituted position, the value
-- that the syntax-level function's numeral produces.  We record that as a
-- single named equation about the two functions' treatment of the decision.

decisionCoherenceTrue : (k i m : Nat) → i =n m ≡ true → substFixT k i (var m) ≡ 3 + k
decisionCoherenceTrue k i m with i =n m
... | true  = λ _ → refl
... | false = λ ()

decisionCoherenceFalse : (k i m : Nat) → i =n m ≡ false → substFixT k i (var m) ≡ suc m
decisionCoherenceFalse k i m with i =n m
... | true  = λ ()
... | false = λ _ → refl
