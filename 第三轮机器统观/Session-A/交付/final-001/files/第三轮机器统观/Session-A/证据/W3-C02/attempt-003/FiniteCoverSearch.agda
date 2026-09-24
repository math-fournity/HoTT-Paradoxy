{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module FiniteCoverSearch where

-- C02: instantiate least-witness elimination with actual rational chain
-- certificates and return the original indices, plus real-cover evidence.
-- The bridge from an arbitrary original cover to a successful stage is
-- a separate obligation, not assumed to follow just from this module.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.List using (List; []; _∷_; _++_; map; concat)
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.Data.Unit
open import Cubical.Relation.Nullary
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
import Cubical.Data.Nat.Order.Recursive as N
open import IntervalCover

data Result (F : ℕ → Interval) : Type where
  failure : Result F
  found : (xs : List ℕ) → Cert F xs → Result F

Has : {F : ℕ → Interval} → Result F → Type
Has failure = ⊥
Has (found xs cert) = Unit

propHas : {F : ℕ → Interval} (r : Result F) → isProp (Has r)
propHas failure = isProp⊥
propHas (found _ _) = isPropUnit

decHas : {F : ℕ → Interval} (r : Result F) → Dec (Has r)
decHas failure = no (λ p → p)
decHas (found _ _) = yes tt

extract : {F : ℕ → Interval} (r : Result F) → Has r → Σ[ xs ∈ List ℕ ] Cert F xs
extract failure ()
extract (found xs cert) _ = xs , cert

inspect : (F : ℕ → Interval) → List (List ℕ) → Result F
inspect F [] = failure
inspect F (xs ∷ rest) with checkCert F xs
... | yes cert = found xs cert
... | no _ = inspect F rest

upto : ℕ → List ℕ
upto zero = 0 ∷ []
upto (suc n) = upto n ++ (suc n ∷ [])

words : ℕ → List ℕ → List (List ℕ)
words zero alphabet = [] ∷ []
words (suc k) alphabet = [] ∷ concat (map (λ i → map (i ∷_) (words k alphabet)) alphabet)

stage : (F : ℕ → Interval) → ℕ → Result F
stage F n = inspect F (words n (upto n))

SuccessfulStage : (ℕ → Interval) → ℕ → Type
SuccessfulStage F n = Has (stage F n)

leastStage : (F : ℕ → Interval) → ∥ Σ ℕ (SuccessfulStage F) ∥₁ →
  Σ ℕ (N.Minimal.Least (SuccessfulStage F))
leastStage F = PT.rec (N.Minimal.isPropΣLeast (λ n → propHas (stage F n)))
  (N.Minimal.→Least (λ n → decHas (stage F n)))

deliverCert : (F : ℕ → Interval) → ∥ Σ ℕ (SuccessfulStage F) ∥₁ →
  Σ[ xs ∈ List ℕ ] Cert F xs
deliverCert F h = extract (stage F (fst result)) (fst (snd result))
  where
  result = leastStage F h

deliver : (F : ℕ → Interval) → ∥ Σ ℕ (SuccessfulStage F) ∥₁ →
  Σ[ xs ∈ List ℕ ] Cover F xs
deliver F h = fst result , chainSound F (fst result) (snd result)
  where
  result = deliverCert F h

overlapStage : SuccessfulStage overlapping 2
overlapStage = tt

overlapInput : ∥ Σ ℕ (SuccessfulStage overlapping) ∥₁
overlapInput = ∣ (2 , overlapStage) ∣₁

selectedIndices : fst (deliver overlapping overlapInput) ≡ pairIndices
selectedIndices = refl

selectedCoverage : Cover overlapping (fst (deliver overlapping overlapInput))
selectedCoverage = snd (deliver overlapping overlapInput)

touchingStage2 : stage touching 2 ≡ failure
touchingStage2 = refl
