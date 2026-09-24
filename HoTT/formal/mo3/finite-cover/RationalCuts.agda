{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module RationalCuts where

-- Actual rational points in the same Dedekind-cut type used by IntervalCover.
-- Density is constructed explicitly; no postulated real point or sample oracle.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (inl; inr)
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Unit
open import Cubical.Data.Rationals.Base using (ℚ; eq/)
import Cubical.Data.Rationals.Properties as A
import Cubical.Data.Rationals.Order as Q
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
open import CutInfra using (·-mono-<-nn)
open import IntervalCover

zero<half : q0 Q.< half
zero<half = decWitness (Q.<Dec q0 half) tt

zero<one : q0 Q.< q1
zero<one = decWitness (Q.<Dec q0 q1) tt

minusOne<zero : qMinus1 Q.< q0
minusOne<zero = decWitness (Q.<Dec qMinus1 q0) tt

halfPlusHalf : half A.+ half ≡ q1
halfPlusHalf = eq/ _ _ refl

halves : (q : ℚ) → (half A.· q) A.+ (half A.· q) ≡ q
halves q = sym (A.·DistR+ half half q) ∙
  cong (A._· q) halfPlusHalf ∙ A.·IdL q

mid : ℚ → ℚ → ℚ
mid q r = (half A.· q) A.+ (half A.· r)

midLeft : (q r : ℚ) → q Q.< r → q Q.< mid q r
midLeft q r qr = subst (Q._< mid q r) (halves q)
  (Q.<-o+ (half A.· q) (half A.· r) (half A.· q)
    (·-mono-<-nn half q r zero<half qr))

midRight : (q r : ℚ) → q Q.< r → mid q r Q.< r
midRight q r qr = subst (mid q r Q.<_) (halves r)
  (Q.<-+o (half A.· q) (half A.· r) (half A.· r)
    (·-mono-<-nn half q r zero<half qr))

lowerInhabited : (q : ℚ) → (q A.+ qMinus1) Q.< q
lowerInhabited q = subst ((q A.+ qMinus1) Q.<_) (A.+IdR q)
  (Q.<-o+ qMinus1 q0 q minusOne<zero)

upperInhabited : (q : ℚ) → q Q.< (q A.+ q1)
upperInhabited q = subst (Q._< (q A.+ q1)) (A.+IdR q)
  (Q.<-o+ q0 q1 q zero<one)

roundedLower : (center q : ℚ) →
  (q Q.< center) ≃ ∥ Σ[ r ∈ ℚ ] ((q Q.< r) × (r Q.< center)) ∥₁
roundedLower center q = propBiimpl→Equiv (Q.isProp< q center) isPropPropTrunc
  (λ qc → ∣ (mid q center , midLeft q center qc , midRight q center qc) ∣₁)
  (PT.rec (Q.isProp< q center) (λ { (r , qr , rc) → Q.isTrans< q r center qr rc }))

roundedUpper : (center r : ℚ) →
  (center Q.< r) ≃ ∥ Σ[ q ∈ ℚ ] ((q Q.< r) × (center Q.< q)) ∥₁
roundedUpper center r = propBiimpl→Equiv (Q.isProp< center r) isPropPropTrunc
  (λ cr → ∣ (mid center r , midRight center r cr , midLeft center r cr) ∣₁)
  (PT.rec (Q.isProp< center r) (λ { (q , qr , cq) → Q.isTrans< center q r cq qr }))

rationalCut : ℚ → R
rationalCut center =
  ((λ q → (q Q.< center) , Q.isProp< q center) ,
   (λ r → (center Q.< r) , Q.isProp< center r)) ,
  ∣ (center A.+ qMinus1 , lowerInhabited center) ∣₁ ,
  ∣ (center A.+ q1 , upperInhabited center) ∣₁ ,
  roundedLower center , roundedUpper center ,
  (λ q (qc , cq) → Q.isAsym< q center qc cq) ,
  (λ q r qr → Q.isWeaklyLinear< q r center qr)

Above : ℚ → R → Type
Above q x = (r : ℚ) → r Q.< q → Lower x r

BelowOne : R → Type
BelowOne x = (r : ℚ) → Lower x r → r Q.< q1

rationalAboveSelf : (q : ℚ) → Above q (rationalCut q)
rationalAboveSelf q r rq = rq

rationalBelowOne : (q : ℚ) → q Q.≤ q1 → BelowOne (rationalCut q)
rationalBelowOne q q≤1 r rq = Q.isTrans<≤ r q q1 rq q≤1

zeroInUnit : InUnit (rationalCut q0)
zeroInUnit = rationalAboveSelf q0 , rationalBelowOne q0 (Q.<Weaken≤ q0 q1 zero<one)

roundedUpperOf : (x : R) (r : ℚ) →
  Upper x r → ∥ Σ[ q ∈ ℚ ] ((q Q.< r) × Upper x q) ∥₁
roundedUpperOf ((L , U) , hL , hU , rL , rU , dis , loc) r = equivFun (rU r)

disjointOf : (x : R) (q : ℚ) → Lower x q → Upper x q → ⊥
disjointOf ((L , U) , hL , hU , rL , rU , dis , loc) q l u = dis q (l , u)

aboveExcludesUpper : (x : R) (r : ℚ) → Above r x → Upper x r → ⊥
aboveExcludesUpper x r above ur = PT.rec isProp⊥
  (λ { (q , qr , uq) → disjointOf x q (above q qr) uq }) (roundedUpperOf x r ur)
