{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module GenericFiniteCover where

-- Contrast with the Nat-indexed positive theorem: a selector uniformly
-- polymorphic in every index type would choose an unlabeled point.
-- No claim that every fixed index type lacks choices or algorithms.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (invEq)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (true)
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Unit
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
import Cubical.Data.Rationals.Order as Q
open import IntervalCover
open import RationalCuts
open import FiniteCoverSearch
open import FiniteSubcover
open import NoCanonicalPoint using (UnlabeledTwoElement; noUniformChoice)

GenericPoint : (I : Type) → (I → Interval) → List I → R → Type
GenericPoint I F xs x = ∥ Σ[ i ∈ I ]
  (Mem i xs × (Lower x (fst (F i)) × Upper x (snd (F i)))) ∥₁

GenericCover : (I : Type) → (I → Interval) → List I → Type₁
GenericCover I F xs = (x : R) → InUnit x → GenericPoint I F xs x

UniformSelector : Type₁
UniformSelector = (I : Type) (F : I → Interval) →
  ∥ Σ[ xs ∈ List I ] GenericCover I F xs ∥₁ →
  Σ[ xs ∈ List I ] GenericCover I F xs

constantFamily : {I : Type} → I → Interval
constantFamily i = qMinus1 , q2

one<two : q1 Q.< q2
one<two = decWitness (Q.<Dec q1 q2) tt

singleCover : {I : Type} (i : I) → GenericCover I constantFamily (i ∷ [])
singleCover i x bound = ∣ (i , memHere ,
  fst bound qMinus1 minusOne<zero , upperBeyondOne x bound q2 one<two) ∣₁

mereCarrier : (X : UnlabeledTwoElement) → ∥ fst X ∥₁
mereCarrier X = PT.map (λ e → invEq e true) (snd X)

mereConstantCover : (X : UnlabeledTwoElement) →
  ∥ Σ[ xs ∈ List (fst X) ] GenericCover (fst X) constantFamily xs ∥₁
mereConstantCover X = PT.map (λ i → (i ∷ []) , singleCover i) (mereCarrier X)

coverHead : {I : Type} (F : I → Interval) (xs : List I) → GenericCover I F xs → I
coverHead F [] cover = Empty.rec
  (PT.rec isProp⊥ (λ { (i , () , li , ui) }) (cover (rationalCut q0) zeroInUnit))
coverHead F (i ∷ xs) cover = i

choiceFromSelector : UniformSelector → (X : UnlabeledTwoElement) → fst X
choiceFromSelector select X = coverHead constantFamily (fst result) (snd result)
  where
  result = select (fst X) constantFamily (mereConstantCover X)

noUniformSelector : UniformSelector → ⊥
noUniformSelector select = noUniformChoice (choiceFromSelector select)
