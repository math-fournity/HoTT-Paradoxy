{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Where the "blind observer" boundary of CG001-C-44 stops (Claude, session
  91a6cdaa, 2026-09-25), in reply to Terra's audit 007 (question O-019).

  proof id : MP-CG001-PATH-OBSERVERS-001
  claims   : CG001-C-46 (full statement in CLAIM.md)

  Terra 007 points out that winding : Omega S1 -> Z is an internal function
  on a loop space that tells loop from refl, so C-44 cannot be read as "every
  internal observation of the identified type is blind".  This file fixes the
  exact line between the two:

  C-46 (a) winding sees the loop: winding loop is not winding refl; a
           fixed-endpoint observer can see the net effect of a step.
       (b) winding is not endpoint-uniform: no t : (a b : S1) -> a = b -> Z
           agrees with winding on the loops at base (by C-44 (a)).
       (c) on a contractible type every fixed-endpoint path observer is
           constant, whatever its result type.
       (d) on the history-indexed context HIT of Homotopical Patch Theory
           (contractible, CG001-C-31) every observer of the patches between
           two fixed contexts is constant: winding-like detectors do not exist
           there.

  Bridge labels (step, patch, context, observer) prove no fact about any
  version control system.
-}
module PathObservers where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; snotz)
open import Cubical.Data.Int using (ℤ; pos; negsuc)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Bool using (Bool; true; false)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.HITs.S1 using (S¹; base; loop; ΩS¹; winding)
open import Cubical.Relation.Nullary using (¬_)

private
  variable
    ℓ ℓ' : Level

-- C-44 (a), restated locally: uniform transition observers are blind
transitionBlind : {A : Type ℓ} {B : Type ℓ'} (t : (a b : A) → a ≡ b → B)
  {a b : A} (p : a ≡ b) → t a b p ≡ t a a refl
transitionBlind t {a} p = J (λ b' p' → t a b' p' ≡ t a a refl) refl p

------------------------------------------------------------------------
-- (a) a fixed-endpoint observer sees the net effect of a step

windingSeesLoop : ¬ (winding loop ≡ winding refl)
windingSeesLoop p = snotz (injPos p)

------------------------------------------------------------------------
-- (b) ... but it cannot be made uniform in the endpoints

windingNotUniform :
  ¬ (Σ[ t ∈ ((a b : S¹) → a ≡ b → ℤ) ] ((q : ΩS¹) → t base base q ≡ winding q))
windingNotUniform (t , agrees) =
  windingSeesLoop (sym (agrees loop) ∙ transitionBlind t loop ∙ agrees refl)

------------------------------------------------------------------------
-- (c) on a contractible type, every fixed-endpoint path observer is constant

contractiblePathBlind : {C : Type ℓ} {B : Type ℓ'} → isContr C
  → {a b : C} (f : a ≡ b → B) (p q : a ≡ b) → f p ≡ f q
contractiblePathBlind h f p q = cong f (isProp→isSet (isContr→isProp h) _ _ p q)

------------------------------------------------------------------------
-- (d) the history-indexed contexts of Homotopical Patch Theory (C-31)

data HistCtx : Type where
  hdoc : List Bool → HistCtx
  hadd : (b : Bool) (h : List Bool) → hdoc h ≡ hdoc (b ∷ h)

histToPath : (h : List Bool) → hdoc [] ≡ hdoc h
histToPath [] = refl
histToPath (b ∷ h) = histToPath h ∙ hadd b h

histContraction : (x : HistCtx) → hdoc [] ≡ x
histContraction (hdoc h) = histToPath h
histContraction (hadd b h i) = compPath-filler (histToPath h) (hadd b h) i

isContrHistCtx : isContr HistCtx
isContrHistCtx = hdoc [] , histContraction

patchObserverBlind : {B : Type ℓ} {x y : HistCtx} (f : x ≡ y → B) (p q : x ≡ y) → f p ≡ f q
patchObserverBlind = contractiblePathBlind isContrHistCtx

-- e.g. no observer of patches from the empty context back to itself tells
-- "add a line, then take it back" from "do nothing"
noUndoDetector : {B : Type ℓ} (f : hdoc [] ≡ hdoc [] → B)
  → f (hadd true [] ∙ sym (hadd true [])) ≡ f refl
noUndoDetector f = patchObserverBlind f _ _
