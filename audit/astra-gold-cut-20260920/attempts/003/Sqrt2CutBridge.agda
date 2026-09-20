{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module Sqrt2CutBridge where

-- Pack the unchanged GOLD predicates into standard and corrected legacy carriers.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Equiv using (_≃_; propBiimpl→Equiv; equivFun; invEq)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import Cubical.Data.Sum.Properties as Sum
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Data.Nat.Base using (zero)
open import Cubical.Data.Int.Base using (pos; negsuc)
open import Cubical.Data.NatPlusOne.Base using (1+_)
open import Cubical.Data.Rationals.Base using (ℚ; [_/_])
open import Cubical.Data.Rationals.Order using (_<_; isIrrefl<)
open import StandardDedekind
import CutGoldForm as G
import CutRealLayer as Legacy

zeroQ oneQ twoQ minusThreeQ : ℚ
zeroQ = [ pos 0 / 1+ zero ]
oneQ = [ pos 1 / 1+ zero ]
twoQ = [ pos 2 / 1+ zero ]
minusThreeQ = [ negsuc 2 / 1+ zero ]

stdToLegacy : {ℓ : Level} (L U : ℚ → hProp ℓ) → dcutStd L U → Legacy.dcut L U
stdToLegacy L U (a , b , rl , ru , dj , loc) = a , b ,
  (λ q → propBiimpl→Equiv (snd (L q)) isPropPropTrunc (fst (rl q)) (snd (rl q))) ,
  (λ r → propBiimpl→Equiv (snd (U r)) isPropPropTrunc (fst (ru r)) (snd (ru r))) , dj , loc

legacyToStd : {ℓ : Level} (L U : ℚ → hProp ℓ) → Legacy.dcut L U → dcutStd L U
legacyToStd L U (a , b , rl , ru , dj , loc) = a , b ,
  (λ q → equivFun (rl q) , invEq (rl q)) ,
  (λ r → equivFun (ru r) , invEq (ru r)) , dj , loc

stdLegacyEquiv : {ℓ : Level} (L U : ℚ → hProp ℓ) → dcutStd L U ≃ Legacy.dcut L U
stdLegacyEquiv L U = propBiimpl→Equiv (isPropDcutStd L U) (Legacy.isPropDCut L U)
  (stdToLegacy L U) (legacyToStd L U)

goldStd : dcutStd G.Lₚ G.Uₚ
goldStd = ∣ oneQ , G.inhabL ∣₁ , ∣ twoQ , G.inhabU ∣₁ ,
  (λ q → (λ l → ∣ G.roundedL← q l ∣₁) ,
    PT.rec (snd (G.Lₚ q)) (λ { (r , q<r , lr) → G.roundedL→ q r q<r lr })) ,
  (λ r → (λ u → ∣ G.roundedU← r u ∣₁) ,
    PT.rec (snd (G.Uₚ r)) (λ { (q , q<r , uq) → G.roundedU→ q r q<r uq })) ,
  (λ q lu → isIrrefl< q (G.disjoint q q (fst lu) (snd lu))) ,
  (λ q r q<r → ∣ G.located q r q<r ∣₁)

goldBook : dcutBook G.Lₚ G.Uₚ
goldBook = stdToBook G.Lₚ G.Uₚ goldStd

goldLegacy : Legacy.dcut G.Lₚ G.Uₚ
goldLegacy = stdToLegacy G.Lₚ G.Uₚ goldStd

goldReal : StandardReals ℓ-zero
goldReal = (G.Lₚ , G.Uₚ) , goldStd

goldLegacyReal : Legacy.DedekindReals ℓ-zero
goldLegacyReal = (G.Lₚ , G.Uₚ) , goldLegacy

goldLowerIdentity : lowerPredicate goldReal ≡ G.Lₚ
goldLowerIdentity = refl

goldUpperIdentity : upperPredicate goldReal ≡ G.Uₚ
goldUpperIdentity = refl

oneLessTwo : oneQ < twoQ
oneLessTwo = 0 , refl

untruncatedLocatedValueNotProp : isProp (G.L oneQ ⊎ G.U twoQ) → ⊥
untruncatedLocatedValueNotProp h = lower
  (Sum.⊎Path.encode (inl G.inhabL) (inr G.inhabU) (h (inl G.inhabL) (inr G.inhabU)))
