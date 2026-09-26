{-# OPTIONS --safe --cubical --guardedness #-}

-- GR-1 C01 completion (GLM-R1-C01): the realistic iota-syntax from
-- RealisticIotaSyntax IS a set.  Route: peer-review Q3 suggestion, third
-- attempt, landed; see REVISIONS.md for the two failed attempts.
--
-- Key step: write q's cond-clause with an EXPLICIT triple composite
-- (cong-part ∙∙ betaι-part ∙∙ branch-part).  At a literal head the
-- cong-part reduces to refl definitionally (cong f refl ≡ refl,
-- machine-tested), so the clause value is definitionally
--   refl ∙∙ betaT t s ∙∙ q t
-- which is exactly the unfolding of `betaT t s ∙ q t` (_∙_ is defined as
-- refl ∙∙ p ∙∙ q) — the left edge of squareLeft.  No lUnit paste needed.

module RealisticIotaSyntaxSet where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isSetRetract)
open import Cubical.Data.Bool using (Bool ; true ; false)
open import Cubical.Data.Bool.Properties using (isSetBool)
open import RealisticIotaSyntax
  using (Tm ; lit ; cond ; betaT ; betaF ; val ; BoolElim ; squareLeft)

mutual
  unlift : (c : Bool) (v w : Tm)
         → cond (lit c) v w ≡ BoolElim (λ _ → Tm) v w c
  unlift true  v w = betaT v w
  unlift false v w = betaF v w

  liftq : (c : Bool) (v w : Tm)
        → BoolElim (λ _ → Tm) v w c
          ≡ lit (BoolElim (λ _ → Bool) (val v) (val w) c)
  liftq true  v w = q v
  liftq false v w = q w

  q : (t : Tm) → t ≡ lit (val t)
  q (lit b) = refl
  q (cond u v w) =
    cong (λ x → cond x v w) (q u) ∙∙ unlift (val u) v w ∙∙ liftq (val u) v w
  q (betaT t s i) j = squareLeft (betaT t s) (q t) i j
  q (betaF t s i) j = squareLeft (betaF t s) (q s) i j

-- GLM-R1-C01: the realistic-equation syntax settles, at set level.
realisticIotaSyntaxIsASet : isSet Tm
realisticIotaSyntaxIsASet = isSetRetract val lit (λ t → sym (q t)) isSetBool
