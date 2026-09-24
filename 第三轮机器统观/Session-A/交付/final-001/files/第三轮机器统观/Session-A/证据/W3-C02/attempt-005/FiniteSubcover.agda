{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module FiniteSubcover where

-- Adequacy bridge: a finite pointwise cover supplies a rational overlap
-- chain. Therefore the mere finite-subcover output is enough for Nat indices.
-- This does not assert compactness for arbitrary pointwise covers.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.List using (List; []; _∷_; length)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Unit
open import Cubical.Data.Rationals.Base using (ℚ)
import Cubical.Data.Rationals.Order as Q
import Cubical.Data.Nat.Order.Recursive as N
open import Cubical.Relation.Nullary
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
open import IntervalCover
open import FiniteCoverSearch
open import RationalCuts

RangeCover : (ℕ → Interval) → ℚ → List ℕ → Type₁
RangeCover F left xs = (x : R) → (Above left x × BelowOne x) → PointCovered F xs x

ChainAt : (ℕ → Interval) → ℚ → List ℕ → Type
ChainAt F left [] = ⊥
ChainAt F left (i ∷ xs) = (fst (F i) Q.< left) × TailCert F (snd (F i)) xs

chainTail : (F : ℕ → Interval) (left : ℚ) (xs : List ℕ) →
  ChainAt F left xs → TailCert F left xs
chainTail F left [] ()
chainTail F left (i ∷ xs) p = p

chainZero : (F : ℕ → Interval) (xs : List ℕ) → ChainAt F q0 xs → Cert F xs
chainZero F [] ()
chainZero F (i ∷ xs) p = p

data Remove (i : ℕ) : List ℕ → List ℕ → Type where
  front : {xs : List ℕ} → Remove i (i ∷ xs) xs
  deeper : {j : ℕ} {xs rest : List ℕ} → Remove i xs rest → Remove i (j ∷ xs) (j ∷ rest)

removeOccurrence : {i : ℕ} {xs : List ℕ} → i ∈ xs → Σ[ rest ∈ List ℕ ] Remove i xs rest
removeOccurrence {xs = i ∷ xs} here = xs , front
removeOccurrence {xs = j ∷ xs} (there mem) with removeOccurrence mem
... | rest , rem = (j ∷ rest) , deeper rem

removeLength : {i : ℕ} {xs rest : List ℕ} → Remove i xs rest → length xs ≡ suc (length rest)
removeLength front = refl
removeLength (deeper rem) = cong suc (removeLength rem)

splitMember : {i k : ℕ} {xs rest : List ℕ} → Remove i xs rest →
  k ∈ xs → (k ≡ i) ⊎ (k ∈ rest)
splitMember front here = inl refl
splitMember front (there mem) = inr mem
splitMember (deeper rem) here = inr here
splitMember (deeper rem) (there mem) with splitMember rem mem
... | inl same = inl same
... | inr kept = inr (there kept)

dropPoint : (F : ℕ → Interval) {i : ℕ} {xs rest : List ℕ} →
  Remove i xs rest → (x : R) → Above (snd (F i)) x →
  PointCovered F xs x → PointCovered F rest x
dropPoint F {i} rem x above = PT.rec isPropPropTrunc λ where
  (k , mem , lk , uk) → choose k lk uk (splitMember rem mem)
    where
    choose : (k : ℕ) → Lower x (fst (F k)) → Upper x (snd (F k)) →
      (k ≡ i) ⊎ (k ∈ _) → PointCovered F _ x
    choose k lk uk (inl same) = Empty.rec (aboveExcludesUpper x (snd (F i)) above
      (subst (λ j → Upper x (snd (F j))) same uk))
    choose k lk uk (inr kept) = ∣ (k , kept , lk , uk) ∣₁

dropRange : (F : ℕ → Interval) (left : ℚ) {i : ℕ} {xs rest : List ℕ} →
  left Q.< snd (F i) → Remove i xs rest → RangeCover F left xs →
  RangeCover F (snd (F i)) rest
dropRange F left {i} step rem cover x (above , below) =
  dropPoint F rem x above (cover x
    ((λ q q<left → above q (Q.isTrans< q left (snd (F i)) q<left step)) , below))

emptyPointImpossible : (F : ℕ → Interval) (x : R) → PointCovered F [] x → ⊥
emptyPointImpossible F x = PT.rec isProp⊥ λ { (i , () , li , ui) }

remainingBound : {i fuel : ℕ} {xs rest : List ℕ} → Remove i xs rest →
  length xs N.≤ suc fuel → length rest N.≤ fuel
remainingBound {fuel = fuel} rem bound = subst (λ n → n N.≤ suc fuel) (removeLength rem) bound

buildChain : (F : ℕ → Interval) (fuel : ℕ) (xs : List ℕ) →
  length xs N.≤ fuel → (left : ℚ) → left Q.≤ q1 → RangeCover F left xs →
  ∥ Σ[ ys ∈ List ℕ ] ChainAt F left ys ∥₁
buildChain F zero [] bound left l≤1 cover = Empty.rec
  (emptyPointImpossible F (rationalCut left)
    (cover (rationalCut left) (rationalAboveSelf left , rationalBelowOne left l≤1)))
buildChain F zero (i ∷ xs) () left l≤1 cover
buildChain F (suc fuel) xs bound left l≤1 cover = PT.rec isPropPropTrunc
  extend (cover (rationalCut left) (rationalAboveSelf left , rationalBelowOne left l≤1))
  where
  extend : (Σ[ i ∈ ℕ ] ((i ∈ xs) × ((fst (F i) Q.< left) × (left Q.< snd (F i))))) →
    ∥ Σ[ ys ∈ List ℕ ] ChainAt F left ys ∥₁
  extend (i , mem , start , advance) with Q.<Dec q1 (snd (F i))
  ... | yes finish = ∣ ((i ∷ []) , start , finish) ∣₁
  ... | no notFinish with removeOccurrence mem
  ... | rest , rem = PT.map
    (λ { (ys , cert) → (i ∷ ys) , start , chainTail F (snd (F i)) ys cert })
    (buildChain F fuel rest (remainingBound rem bound) (snd (F i))
      (Q.≮→≥ q1 (snd (F i)) notFinish)
      (dropRange F left advance rem cover))

finiteCoverToChain : (F : ℕ → Interval) (xs : List ℕ) → Cover F xs →
  ∥ Σ[ ys ∈ List ℕ ] Cert F ys ∥₁
finiteCoverToChain F xs cover = PT.map (λ { (ys , cert) → ys , chainZero F ys cert })
  (buildChain F (length xs) xs (N.≤-refl (length xs)) q0
    (Q.<Weaken≤ q0 q1 zero<one) cover)

mereFiniteCoverToChain : (F : ℕ → Interval) → ∥ Σ[ xs ∈ List ℕ ] Cover F xs ∥₁ →
  ∥ Σ[ ys ∈ List ℕ ] Cert F ys ∥₁
mereFiniteCoverToChain F = PT.rec isPropPropTrunc (λ { (xs , cover) → finiteCoverToChain F xs cover })

extractFiniteSubcover : (F : ℕ → Interval) → ∥ Σ[ xs ∈ List ℕ ] Cover F xs ∥₁ →
  Σ[ xs ∈ List ℕ ] Cover F xs
extractFiniteSubcover F h = fromMereChain F (mereFiniteCoverToChain F h)

overlapMereCover : ∥ Σ[ xs ∈ List ℕ ] Cover overlapping xs ∥₁
overlapMereCover = ∣ (pairIndices , overlapCovers) ∣₁

extractedOriginalIndices : fst (extractFiniteSubcover overlapping overlapMereCover) ≡ pairIndices
extractedOriginalIndices =
  cong (λ h → fst (fromMereChain overlapping h))
    (isPropPropTrunc (mereFiniteCoverToChain overlapping overlapMereCover)
      ∣ (pairIndices , overlapCert) ∣₁) ∙ fromMereChainIndices
