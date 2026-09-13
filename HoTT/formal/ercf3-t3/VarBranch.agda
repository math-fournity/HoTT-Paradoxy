module VarBranch where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix
open import MutualInduction2

-- T3 eleventh pulse, second attempt (bounded): discharge the var branch by
-- rewriting the *goal* with the definitional unfolding of `codeT (num k)`
-- before splitting, so that both sides present the same expression shape.
--
-- The first attempt failed because Agda's with-abstraction kept the internal
-- `if` un-reduced.  This attempt instead proceeds by cases on the *value* of
-- the decision, using the coherence lemmas to rewrite, in the order that makes
-- the two sides definitionally equal.

codeT-num-unfold : (k : Nat) → codeT (num k) ≡ 3 + k
codeT-num-unfold k = refl

-- Direct call to the coherence lemmas still leaves the with-abstraction
-- mismatch: the goal after splitting presents the *internal* match expression
-- `substFixT ... | true`, while the coherence lemma speaks about the
-- *un-split* application.  Closing this requires either
--
--   (a) a lemma that transports the coherence result along the with-unfolding
--       (i.e. an equation `(substFixT k i (var m) | true) ≡ 3 + k` stated as a
--       plain equality, provable by `refl` once the decision is known), or
--   (b) restating the substitution functions to take the decision value as an
--       explicit argument.
--
-- Both are mechanical; neither changes the mathematics.

varBranchDirection : Set
varBranchDirection = Nat
