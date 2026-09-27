{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Declaration/proof repair for GLM-R1-C02 (claim COPUS-GLM-FIX-C02).

  GLM's declared content: "the standard interpretation sends each ι path
  constructor to refl, definitionally".  GLM's formal witness
      valReflT : (t s : Tm) → Path (Path Bool (val (cond (lit true) t s)) (val t)) refl refl
  never mentions the path constructor betaT: it only needs the two
  endpoints to agree definitionally, after which `refl ≡ refl` is trivial.

  (1) The faithful statement, machine-checked here:
        cong val (betaT t s) ≡ refl      (by refl)
  (2) The rupture, machine-exhibited: GLM's statement FORM also holds for
      the ARTIFICIAL equation `art`, whose interpretation is ua not ≠ refl,
      whereas the faithful form fails for it.  So the original witness does
      not discriminate real from artificial equations; the faithful one does.
-}
module IotaC02Faithful where

open import Cubical.Foundations.Prelude
open import Cubical.Relation.Nullary using (¬_)
open import RealisticIotaSyntax using (Tm ; betaT ; betaF ; val)
open import ArtificialEquationControl using (TmA ; boolTy ; art ; f ; uaNotRefl)

-- (1) faithful C02
valBetaT-refl : (t s : Tm) → cong val (betaT t s) ≡ refl
valBetaT-refl t s = refl

valBetaF-refl : (t s : Tm) → cong val (betaF t s) ≡ refl
valBetaF-refl t s = refl

-- (2a) GLM's statement form, instantiated at the artificial equation: holds.
glmFormHoldsAtArt : Path (Path Type (f boolTy) (f boolTy)) refl refl
glmFormHoldsAtArt = refl

-- (2b) the faithful form at the artificial equation: refuted.
faithfulFormFailsAtArt : ¬ (cong f art ≡ refl)
faithfulFormFailsAtArt = uaNotRefl
