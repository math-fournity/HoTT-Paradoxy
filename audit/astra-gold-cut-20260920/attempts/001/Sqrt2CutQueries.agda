{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module Sqrt2CutQueries where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Empty as Empty
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.Data.Rationals.Order using (_<_; Trichotomy; _≟_; lt; eq; gt; isAsym<; isIrrefl<)
open import CutInfra using (<-≤)
import CutGoldForm as G
import MissileTwoUniversalIrrationality as M2
import MissileThreeUnconditional as Old
open import StandardDedekind
open import Sqrt2CutBridge

zeroLower : G.L zeroQ
zeroLower = inr ((0 , refl) , (1 , refl))

classify : (q : ℚ) → G.L q ⊎ G.U q
classify q with q ≟ zeroQ
... | lt q<0 = inl (inl q<0)
... | eq q=0 = inl (subst G.L (sym q=0) zeroLower)
... | gt 0<q with (q ·ℚ q) ≟ twoQ
...   | lt sq<2 = inl (inr (<-≤ zeroQ q 0<q , sq<2))
...   | eq sq=2 = Empty.rec (M2.√2-irrational q sq=2)
...   | gt 2<sq = inr (0<q , 2<sq)

lowerQuery : (q : ℚ) → Dec (G.L q)
lowerQuery q with classify q
... | inl l = yes l
... | inr u = no (λ l → isIrrefl< q (G.disjoint q q l u))

upperQuery : (q : ℚ) → Dec (G.U q)
upperQuery q with classify q
... | inl l = no (λ u → isIrrefl< q (G.disjoint q q l u))
... | inr u = yes u

packedLowerQuery : (q : ℚ) → Dec (fst (lowerPredicate goldReal q))
packedLowerQuery = lowerQuery

packedUpperQuery : (q : ℚ) → Dec (fst (upperPredicate goldReal q))
packedUpperQuery = upperQuery

decisionTag : {A : Type₀} → Dec A → Bool
decisionTag (yes _) = true
decisionTag (no _) = false

minusThreeIsLower : G.L minusThreeQ
minusThreeIsLower = inl (2 , refl)

minusThreeLowerTag : decisionTag (lowerQuery minusThreeQ) ≡ true
minusThreeLowerTag = refl

oldSquareTableRejectsMinusThree : fst Old.specA-inhabited-unc minusThreeQ ≡ false
oldSquareTableRejectsMinusThree = refl

RationalRootTask : Type₀
RationalRootTask = Σ[ q ∈ ℚ ] q ·ℚ q ≡ twoQ

noRationalRootOutput : RationalRootTask → ⊥
noRationalRootOutput (q , root) = M2.√2-irrational q root
