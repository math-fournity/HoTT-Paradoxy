{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control COPUS-KS-NEG-01 for KSUniverseTower (near miss).
  The non-triviality script of `base` (uaβ on swap) is applied to the
  TRIVIAL loop refl at (Bool , isSetBool).  Expected: kernel rejection,
  because transport along refl does not compute to `not`
  (the endpoint of `uaβ notEquiv true` is `transport (ua notEquiv) true`).
  This shows the KS base case genuinely rests on the non-trivial loop.
-}
module KSNegTrivialBase where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence using (ua ; uaβ)
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool ; true ; false)
open import Cubical.Data.Bool.Properties using (notEquiv ; isSetBool ; true≢false)
open import Cubical.Relation.Nullary using (¬_)
open import KSUniverseTower using (T)

W₀ : T ℓ-zero 0
W₀ = Bool , isSetBool

wrong : ¬ (refl {x = W₀} ≡ refl)
wrong r = true≢false (sym (transportRefl true)
                      ∙ sym (cong (λ p → transport p true) (cong (cong fst) r))
                      ∙ uaβ notEquiv true)
