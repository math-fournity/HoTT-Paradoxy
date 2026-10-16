{-# OPTIONS --safe --cubical --guardedness #-}

-- GR-1 artificial-equation control (GLM-R1-C03).  Same fragment as
-- RealisticIotaSyntax plus ONE artificial equation art : boolTy ≡ boolTy
-- that declares the nontrivial Boolean self-equivalence `not` to be a
-- definitional identification.  No real type theory has such a computation
-- rule; this is the C-67-style injection, in the fairness contract's sense.
-- Result: the syntax is then NOT a set.  Non-settling must be injected, it
-- is not inherited from real equations.

module ArtificialEquationControl where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (iso ; isoToEquiv)
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Univalence using (ua ; uaβ)
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Data.Bool using (Bool ; true ; false ; not ; true≢false)
open import RealisticIotaSyntax using (BoolElim)

flipNotEquiv : Bool ≃ Bool
flipNotEquiv =
  isoToEquiv (iso not not (λ { false → refl ; true → refl })
                       (λ { false → refl ; true → refl }))

data TmA : Type where
  litA   : Bool → TmA
  boolTy : TmA
  condA  : TmA → TmA → TmA → TmA
  betaTA : (t s : TmA) → condA (litA true)  t s ≡ t
  betaFA : (t s : TmA) → condA (litA false) t s ≡ s
  art    : boolTy ≡ boolTy

valA : TmA → Bool
valA (litA b) = b
valA boolTy = true
valA (condA u v w) = BoolElim (λ _ → Bool) (valA v) (valA w) (valA u)
valA (betaTA t s i) = valA t
valA (betaFA t s i) = valA s
valA (art i) = true

-- Interpretation into the universe: all real equations still go to refl;
-- the artificial one goes to ua of a nontrivial equivalence.
f : TmA → Type
f (litA b) = Bool
f boolTy = Bool
f (condA u v w) = BoolElim (λ _ → Type) (f v) (f w) (valA u)
f (betaTA t s i) = f t
f (betaFA t s i) = f s
f (art i) = ua flipNotEquiv i

uaNotRefl : ¬ (ua flipNotEquiv ≡ refl)
uaNotRefl pr =
  true≢false
    (sym (sym (uaβ flipNotEquiv true) ∙ cong (λ q → transport q true) pr
             ∙ transportRefl true))

-- With the artificial equation, the syntax is no longer a set (GLM-R1-C03).
¬isSetTmA : ¬ isSet TmA
¬isSetTmA S = uaNotRefl (cong (cong f) eq)
  where
  eq : art ≡ refl
  eq = S boolTy boolTy art refl
