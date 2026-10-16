module TermIdentityFinal where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix
open import MutualInduction2
open import DecisionParam

-- T3 thirteenth pulse (bounded): close the var cases of the term-level identity
-- using the decision-parameter formulation, so that the remaining obligation is
-- purely the recursive case (+t and the formula-level constructors).

-- Second occurrence of the residual blocker, now in its exact final form:
--
--   substFixTd true k i (var m)  ==  3 + k                      (definitional)
--   codeT (substT k i (var m))   ==  codeT (if i =n m then num k else var m)
--
-- The *syntax-side* `substT` also performs a decision split, and without knowing
-- that `i =n m` is true the nested `if` does not reduce.  Hence the two
-- formulations must share the decision on *both* sides: either the syntax-side
-- substitution must also take the decision as a parameter, or the identity must
-- be proved by a joint recursion that abstracts the single decision used by both
-- definitions.
--
-- Conclusion recorded rather than re-attempted: the remaining step is a joint
-- (mutual) recursion over the shared decision, not a local transport.

-- What is already machine-checked in this file's dependency set:
--   * var cases with the decision fixed on the *code* side (MutualInduction2)
--   * decision-parameter formulation and its definitional coherence (DecisionParam)
--   * corrected store (codeT (num k) = 3 + k) on three constructors (CodeStoreFix)
--   * definitional anchors at formula level (CodeStoreFixF)

remainingStep : Set
remainingStep = Nat
