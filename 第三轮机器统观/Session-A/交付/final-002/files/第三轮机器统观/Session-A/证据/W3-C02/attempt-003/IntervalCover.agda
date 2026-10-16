{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module IntervalCover where

-- C02 intermediate: a rational chain certificate really covers all
-- Dedekind-cut points in the closed unit interval. Not just rational samples.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Unit
open import Cubical.Data.Rationals.Base using (ℚ; [_/_])
import Cubical.Data.Rationals.Order as Q
open import Cubical.Data.Int.Base using (pos; negsuc)
open import Cubical.Data.NatPlusOne using (1+_)
open import Cubical.Relation.Nullary
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
open import CutRealLayer using (DedekindReals)

R : Type₁
R = DedekindReals ℓ-zero

q0 q1 q2 qMinus1 : ℚ
q0 = [ pos 0 / 1+ 0 ]
q1 = [ pos 1 / 1+ 0 ]
q2 = [ pos 2 / 1+ 0 ]
qMinus1 = [ negsuc 0 / 1+ 0 ]

Lower Upper : R → ℚ → Type
Lower x q = fst (fst (fst x) q)
Upper x q = fst (snd (fst x) q)

propLower : (x : R) (q : ℚ) → isProp (Lower x q)
propLower x q = snd (fst (fst x) q)

propUpper : (x : R) (q : ℚ) → isProp (Upper x q)
propUpper x q = snd (snd (fst x) q)

located : (x : R) (q r : ℚ) → q Q.< r → ∥ Lower x q ⊎ Upper x r ∥₁
located ((L , U) , hL , hU , rL , rU , dis , loc) = loc

-- Book's lower-cut inclusion order, specialized to the rational cuts 0/1.
InUnit : R → Type
InUnit x = ((q : ℚ) → q Q.< q0 → Lower x q)
         × ((q : ℚ) → Lower x q → q Q.< q1)

upperBeyondOne : (x : R) → InUnit x → (r : ℚ) → q1 Q.< r → Upper x r
upperBeyondOne x bound r one<r = PT.rec (propUpper x r)
  (λ { (inl l1) → Empty.rec (Q.isIrrefl< q1 (snd bound q1 l1))
     ; (inr ur) → ur }) (located x q1 r one<r)

Interval : Type
Interval = ℚ × ℚ

data _∈_ (i : ℕ) : List ℕ → Type where
  here : {xs : List ℕ} → i ∈ (i ∷ xs)
  there : {j : ℕ} {xs : List ℕ} → i ∈ xs → i ∈ (j ∷ xs)

TailCert : (ℕ → Interval) → ℚ → List ℕ → Type
TailCert F right [] = q1 Q.< right
TailCert F right (j ∷ js) = (fst (F j) Q.< right) × TailCert F (snd (F j)) js

Cert : (ℕ → Interval) → List ℕ → Type
Cert F [] = ⊥
Cert F (i ∷ xs) = (fst (F i) Q.< q0) × TailCert F (snd (F i)) xs

PointCovered : (ℕ → Interval) → List ℕ → R → Type
PointCovered F xs x = ∥ Σ[ i ∈ ℕ ]
  ((i ∈ xs) × (Lower x (fst (F i)) × Upper x (snd (F i)))) ∥₁

Cover : (ℕ → Interval) → List ℕ → Type₁
Cover F xs = (x : R) → InUnit x → PointCovered F xs x

coverFrom : (F : ℕ → Interval) (i : ℕ) (xs : List ℕ) →
  TailCert F (snd (F i)) xs → (x : R) → InUnit x →
  Lower x (fst (F i)) → PointCovered F (i ∷ xs) x
coverFrom F i [] cert x bound li = ∣ (i , here , li ,
  upperBeyondOne x bound (snd (F i)) cert) ∣₁
coverFrom F i (j ∷ js) (overlapEdge , rest) x bound li =
  PT.rec isPropPropTrunc
    (λ { (inl lj) → PT.map (λ { (k , mem , lk , uk) → k , there mem , lk , uk })
                      (coverFrom F j js rest x bound lj)
       ; (inr ui) → ∣ (i , here , li , ui) ∣₁ })
    (located x (fst (F j)) (snd (F i)) overlapEdge)

chainSound : (F : ℕ → Interval) (xs : List ℕ) → Cert F xs → Cover F xs
chainSound F [] ()
chainSound F (i ∷ xs) (start , rest) x bound =
  coverFrom F i xs rest x bound (fst bound (fst (F i)) start)

decPair : {A B : Type} → Dec A → Dec B → Dec (A × B)
decPair (yes a) (yes b) = yes (a , b)
decPair (yes a) (no nb) = no (λ p → nb (snd p))
decPair (no na) _ = no (λ p → na (fst p))

checkTail : (F : ℕ → Interval) (r : ℚ) (xs : List ℕ) → Dec (TailCert F r xs)
checkTail F r [] = Q.<Dec q1 r
checkTail F r (i ∷ xs) = decPair (Q.<Dec (fst (F i)) r) (checkTail F (snd (F i)) xs)

checkCert : (F : ℕ → Interval) (xs : List ℕ) → Dec (Cert F xs)
checkCert F [] = no (λ p → p)
checkCert F (i ∷ xs) = decPair (Q.<Dec (fst (F i)) q0) (checkTail F (snd (F i)) xs)

propTail : (F : ℕ → Interval) (r : ℚ) (xs : List ℕ) → isProp (TailCert F r xs)
propTail F r [] = Q.isProp< q1 r
propTail F r (i ∷ xs) = isProp× (Q.isProp< (fst (F i)) r) (propTail F (snd (F i)) xs)

propCert : (F : ℕ → Interval) (xs : List ℕ) → isProp (Cert F xs)
propCert F [] = isProp⊥
propCert F (i ∷ xs) = isProp× (Q.isProp< (fst (F i)) q0) (propTail F (snd (F i)) xs)

quarter threeQuarters half : ℚ
quarter = [ pos 1 / 1+ 3 ]
threeQuarters = [ pos 3 / 1+ 3 ]
half = [ pos 1 / 1+ 1 ]

overlapping touching : ℕ → Interval
overlapping zero = qMinus1 , threeQuarters
overlapping (suc zero) = quarter , q2
overlapping (suc (suc n)) = q2 , q2
touching zero = qMinus1 , half
touching (suc zero) = half , q2
touching (suc (suc n)) = q2 , q2

Truth : {A : Type} → Dec A → Type
Truth (yes _) = Unit
Truth (no _) = ⊥

decWitness : {A : Type} (d : Dec A) → Truth d → A
decWitness (yes a) _ = a
decWitness (no _) ()

pairIndices : List ℕ
pairIndices = 0 ∷ 1 ∷ []

overlapCert : Cert overlapping pairIndices
overlapCert = decWitness (checkCert overlapping pairIndices) tt

overlapCovers : Cover overlapping pairIndices
overlapCovers = chainSound overlapping pairIndices overlapCert

touchingRejected : Cert touching pairIndices → ⊥
touchingRejected cert = Q.isIrrefl< half (fst (snd cert))
