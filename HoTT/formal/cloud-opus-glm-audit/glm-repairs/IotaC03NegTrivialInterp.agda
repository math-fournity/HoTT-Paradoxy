{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Near-miss negative control for GLM-R1-C03 (COPUS-GLM-FIX-NEG-03).
  GLM's ¬isSetTmA proof, verbatim, with the interpretation of `art`
  replaced by the constant path (f' (art i) = Bool).  Expected: kernel
  rejection (cong f' art is refl, not ua flipNotEquiv).  This shows C03
  rests on the non-trivial interpretation of the injected equation, which
  GLM's own negative control (art ≢ refl definitionally) does not test.
-}
module IotaC03NegTrivialInterp where

open import Cubical.Foundations.Prelude
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Data.Bool using (Bool)
open import RealisticIotaSyntax using (BoolElim)
open import ArtificialEquationControl
  using (TmA ; litA ; boolTy ; condA ; betaTA ; betaFA ; art ; valA ; uaNotRefl)

f' : TmA → Type
f' (litA b) = Bool
f' boolTy = Bool
f' (condA u v w) = BoolElim (λ _ → Type) (f' v) (f' w) (valA u)
f' (betaTA t s i) = f' t
f' (betaFA t s i) = f' s
f' (art i) = Bool

wrong : ¬ isSet TmA
wrong S = uaNotRefl (cong (cong f') (S boolTy boolTy art refl))
