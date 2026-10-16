{-# OPTIONS --safe --cubical --guardedness #-}
module RationalRestoration where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import Cubical.Data.Rationals.Base using (discreteℚ; isSetℚ)
open import Cubical.Data.Sigma using (discreteΣ; discreteΣProp)
open import Cubical.Data.Sum using (inl; inr)
open import Cubical.Data.Unit using (tt)
open import Cubical.Relation.Nullary using (Discrete)
open import RationalPointSet
open import PointRestoration
open Restoration QCircle east

-- This is the existing algebraic rational circle, not a fresh finite surrogate.
discreteQCircle : Discrete QCircle
discreteQCircle = discreteΣ discreteℚ
  (λ x → discreteΣProp discreteℚ (λ y → isSetℚ _ _))

pointDecision : PointDecidable
pointDecision x = discreteQCircle x east

restoreQCircle : Completed ≃ QCircle
restoreQCircle = restorationEquiv pointDecision

punctureInclusionPreserved : (z : Puncture)
  → equivFun restoreQCircle (inl z) ≡ fst z
punctureInclusionPreserved z = refl

specifiedPointPreserved : equivFun restoreQCircle (inr tt) ≡ east
specifiedPointPreserved = refl

restoreAsPath : Completed ≡ QCircle
restoreAsPath = ua restoreQCircle

transportPreservesRestore : (z : Completed)
  → transport restoreAsPath z ≡ extend z
transportPreservesRestore z = uaβ restoreQCircle z

northRestored : equivFun restoreQCircle (inl nonemptyPointSetPuncture) ≡ north
northRestored = refl
