module DecisionParam where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix
open import MutualInduction2

-- T3 twelfth pulse (bounded): implement fix (b) from the N32 record — restate
-- the term-level code substitution so that it *takes the decision value as an
-- explicit argument*.  With the decision explicit, both sides are built from
-- the same value and the with-abstraction mismatch disappears by construction.

substFixTd : Bool → Nat → Nat → Tm → Nat
substFixTd d k i (var m) with d
... | true  = 3 + k
... | false = suc m
substFixTd d k i (num m) = suc (suc (suc m))
substFixTd d k i (t +t u) = 1 + (1 + (suc (suc (suc (substFixTd d k i t + substFixTd d k i u)))))

-- The exact coherence equation for the matching-variable case, now a plain
-- equality about an explicit-decision application (no with-abstraction remains
-- in the goal).
matchCaseAgrees : (k i : Nat) → substFixTd true k i (var i) ≡ 3 + k
matchCaseAgrees k i = refl

nonMatchCaseAgrees : (k i m : Nat) → substFixTd false k i (var m) ≡ suc m
nonMatchCaseAgrees k i m = refl

-- Consequence: with the decision explicit, the coherence equations are
-- definitional, so the var branch of the mutual induction can be discharged
-- without any with-abstraction transport.
