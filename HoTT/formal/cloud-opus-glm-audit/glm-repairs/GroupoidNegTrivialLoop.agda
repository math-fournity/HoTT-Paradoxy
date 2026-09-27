{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Near-miss negative control for GLM-R3-C01 (COPUS-GLM-FIX-NEG-02).
  GLM's τ≠refl script, verbatim, applied to the loop built from the
  IDENTITY equivalence instead of the involution a.  Expected: kernel
  rejection (the chain now ends in (true , true), and true != false).
  This shows GLM's non-triviality step depends on a moving (true , true).
-}
module GroupoidNegTrivialLoop where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Foundations.Univalence using (ua ; uaβ)
open import Cubical.Foundations.HLevels using (isPropIsSet)
open import Cubical.Data.Bool using (true ; false ; true≢false)
open import Cubical.Data.Sigma using (fst ; snd)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Relation.Nullary using (¬_)
open import NoHitGroupoidUniverse using (X ; X-isSet ; c₀)

τid : c₀ ≡ c₀
τid = ΣPathP (ua (idEquiv X) ,
              isProp→PathP (λ i → isPropIsSet {A = ua (idEquiv X) i}) X-isSet X-isSet)

wrong : ¬ (τid ≡ refl)
wrong h = true≢false (cong fst chain)
  where
  t1 = uaβ (idEquiv X) (true , true)
  t2 = cong (λ e → transport e (true , true)) (cong (cong fst) h)
  t3 = transportRefl (true , true)
  chain = sym t3 ∙ sym t2 ∙ t1
