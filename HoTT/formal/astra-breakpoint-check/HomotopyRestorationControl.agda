{-# OPTIONS --safe --cubical --guardedness #-}
module HomotopyRestorationControl where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels hiding (extend)
open import Cubical.Data.Empty as Empty using (⊥)
open import Cubical.Data.Sum using (inl; inr)
open import Cubical.Data.Unit using (tt)
open import Cubical.HITs.S1.Base using (S¹; base)
open import PointRestoration
open import PathExclusion using (circleExclusion)
open import UpstreamLoopHoldout using (notAllProofsEqual)
open Restoration S¹ base

-- A control for the exact path-exclusion representation; it is not a theorem
-- about removing one geometric point of an embedded topological circle.
allExtendedAtBase : (r : Completed) → extend r ≡ base
allExtendedAtBase (inl z) = Empty.rec (circleExclusion z)
allExtendedAtBase (inr tt) = refl

splitWouldContract : SplitRestore → isContr S¹
splitWouldContract (decode , law) = base , λ x →
  sym (sym (law x) ∙ allExtendedAtBase (decode x))

noHomotopySplit : SplitRestore → ⊥
noHomotopySplit split = notAllProofsEqual
  (isProp→isSet (isContr→isProp (splitWouldContract split)) base base)

noPointDecision : PointDecidable → ⊥
noPointDecision decision = noHomotopySplit (decisionToSplit decision)
