{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control MP-CG001-A-UNIVALENCE-B-NEG-003 (CG001-C-430).

  Claim to be refused: the theorem "A and univalence give no finite level"
  applies to the numbered collection, whose code sameness is a fact, if one
  hands it the identity equivalence in place of univalence.  Then ℕ would be
  at no finite h-level.  Expected: rejected at type checking; the identity is
  an equivalence of a ≡ b with itself, not the map from a ≡ b to the
  equivalences of the members that univalence needs.
-}
module WrongBWithoutUnivalence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Relation.Nullary using (¬_)
open import AUnivalenceB using (numbered; numberedAllHeights; module UnivalentCollection)

naturalsHaveNoLevel : (m : ℕ) → ¬ isOfHLevel m ℕ
naturalsHaveNoLevel =
  UnivalentCollection.noFiniteLevel numbered (λ a b → snd (idEquiv (a ≡ b))) numberedAllHeights
