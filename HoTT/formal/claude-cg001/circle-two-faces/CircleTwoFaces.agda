{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A1 follow-up (Claude, session 6fd0312a, 2026-09-24): the two faces of the
  circle in HoTT, used to read the user's circle paradox by dual-expression
  collision (method M).

  proof id : MP-CG001-CIRCLE-TWO-FACES-001
  claims   : CG001-C-21 .. CG001-C-22 (full statements in CLAIM.md)

  C-21  a type whose points carry an injective set-valued coordinate is a set
        (Book Theorem 7.2.2 applied to "same coordinate"), so every loop in it
        is trivial: no type has both coordinatized points and a non-trivial
        loop.
  C-22  the synthetic circle S1 has a non-trivial loop, admits no injective
        coordinate into any set, and taking a point away from it (by
        "not equal to base") leaves nothing.

  Read together: the circle whose points can be removed and measured, and the
  circle that is a loop, are two different objects in HoTT.  The point-set
  side of the user's story is covered by Astra's native results C-283..C-324
  (shared matrix), which this file does not re-prove.

  Bridge labels (coordinate, circle, taking a point away) are interpretation;
  this file proves no physical fact and not HoTT inconsistency.
-}
module CircleTwoFaces where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Data.Empty using (⊥; isProp⊥)
open import Cubical.Data.Nat using (znots)
open import Cubical.Data.Int using (injPos)
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Relation.Binary.Properties using (reflPropRelImpliesIdentity→isSet)
open import Cubical.HITs.PropositionalTruncation as PT using (∥_∥₁)
open import Cubical.HITs.S1 using (S¹; base; loop; winding)
open import Cubical.HITs.S1.Properties using (isConnectedS¹)

------------------------------------------------------------------------
-- CG001-C-21  Coordinatized points leave no room for a loop

module Coordinatized {ℓ ℓ'} {A : Type ℓ} {P : Type ℓ'} (setP : isSet P)
  (f : A → P) (inj : (x y : A) → f x ≡ f y → x ≡ y) where

  coordinatizedIsSet : isSet A
  coordinatizedIsSet =
    reflPropRelImpliesIdentity→isSet (λ x y → f x ≡ f y)
      (λ _ → refl) (λ _ _ → setP _ _) (λ {x} {y} → inj x y)

  loopsTrivial : (a : A) (p : a ≡ a) → p ≡ refl
  loopsTrivial a p = coordinatizedIsSet a a p refl

  noNontrivialLoop : ¬ (Σ[ a ∈ A ] Σ[ p ∈ (a ≡ a) ] ¬ (p ≡ refl))
  noNontrivialLoop (a , p , nontrivial) = nontrivial (loopsTrivial a p)

------------------------------------------------------------------------
-- CG001-C-22  The synthetic circle: a loop, no coordinates, no removable point

loopNontrivial : ¬ (loop ≡ refl)
loopNontrivial q = znots (injPos (sym (cong winding q)))

noCoordinateOnS¹ : ∀ {ℓ'} {P : Type ℓ'} → isSet P
  → ¬ (Σ[ f ∈ (S¹ → P) ] ((x y : S¹) → f x ≡ f y → x ≡ y))
noCoordinateOnS¹ setP (f , inj) =
  Coordinatized.noNontrivialLoop setP f inj (base , loop , loopNontrivial)

puncturedS¹Empty : ¬ (Σ[ x ∈ S¹ ] ¬ (base ≡ x))
puncturedS¹Empty (x , away) = PT.rec isProp⊥ away (isConnectedS¹ x)
