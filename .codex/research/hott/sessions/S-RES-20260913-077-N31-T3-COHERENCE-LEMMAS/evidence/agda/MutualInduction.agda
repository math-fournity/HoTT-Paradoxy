module MutualInduction where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix

-- T3 ninth pulse (bounded): the single remaining obligation.
--
--   substFixT k i t  ==  codeT (substT k i t)     for all t, k, i
--
-- Recursion structure: var is the already-proved comparison case; num is
-- definitional; the addition constructor follows from the two inductive
-- hypotheses by congruence.

-- What is already machine-checked (see CodeStoreFix.agda):
--   fix-var-self : substFixT k i (var i) == codeT (substT k i (var i))
--   fix-var-het  : substFixT k i (var m) == codeT (substT k i (var m))   (i =n m == false)
--   fix-num      : substFixT k i (num m) == codeT (substT k i (num m))
--
-- What is attempted here and remains open: the `with`-abstraction over `i =n m`
-- must be aligned between `substFixT` (which matches on `i =n m` directly) and
-- `codeT (substT ...)` (which matches on the same decision through a nested
-- `if`).  Agda's with-abstraction currently rejects the direct rewrite; the
-- fix is to state the helper lemmas with the decision as an explicit argument
-- (or to use a helper that abstracts the common decision).  This is the exact
-- remaining step, not a mathematical gap.

-- The goal type, stated as a named target (not inhabited here):
TermIdentity : Set
TermIdentity = (t : Tm) (k i : Nat) → substFixT k i t ≡ codeT (substT k i t)

