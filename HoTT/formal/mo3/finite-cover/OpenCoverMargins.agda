{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module OpenCoverMargins where

-- R13: the same family of strictly internal rational intervals covers the
-- whole open unit interval, but no finite subfamily does. A strict inner
-- closed interval has a one-member positive cover from that same family.
-- Pointwise cut semantics only; not a formalization of the full Book HIT.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Unit
open import Cubical.Data.Rationals.Base using (ℚ)
import Cubical.Data.Rationals.Order as Q
open import Cubical.Relation.Nullary
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
open import IntervalCover
open import RationalCuts

Inner : Type
Inner = Σ[ l ∈ ℚ ] Σ[ r ∈ ℚ ]
  ((q0 Q.< l) × ((l Q.< r) × (r Q.< q1)))

leftEnd rightEnd : Inner → ℚ
leftEnd = fst
rightEnd i = fst (snd i)

leftPositive : (i : Inner) → q0 Q.< leftEnd i
leftPositive (l , r , pos , lr , r1) = pos

leftBelowOne : (i : Inner) → leftEnd i Q.< q1
leftBelowOne (l , r , pos , lr , r1) = Q.isTrans< l r q1 lr r1

OpenUnit : R → Type
OpenUnit x = Lower x q0 × Upper x q1

CoveredBy : Inner → R → Type
CoveredBy i x = Lower x (leftEnd i) × Upper x (rightEnd i)

lowerRoundedIso : (x : R) (q : ℚ) →
  Lower x q ≃ ∥ Σ[ r ∈ ℚ ] ((q Q.< r) × Lower x r) ∥₁
lowerRoundedIso ((L , U) , hL , hU , rL , rU , dis , loc) = rL

lowerClosed : (x : R) (q r : ℚ) → q Q.< r → Lower x r → Lower x q
lowerClosed x q r qr lr = invEq (lowerRoundedIso x q) ∣ (r , qr , lr) ∣₁

lowerBelowUpper : (x : R) (s t : ℚ) → Lower x s → Upper x t → s Q.< t
lowerBelowUpper x s t ls ut with Q.<Dec s t
... | yes st = st
... | no notST = Empty.rec (PT.rec isProp⊥
  (λ { (q , qt , uq) → disjointOf x q
    (lowerClosed x q s (Q.isTrans<≤ q t s qt (Q.≮→≥ s t notST)) ls) uq })
  (roundedUpperOf x t ut))

pointwiseInnerCover : (x : R) → OpenUnit x → ∥ Σ[ i ∈ Inner ] CoveredBy i x ∥₁
pointwiseInnerCover x (l0 , u1) = PT.rec isPropPropTrunc
  (λ { (s , positive , ls) → PT.rec isPropPropTrunc
    (λ { (t , t1 , ut) → ∣ ((s , t , positive , lowerBelowUpper x s t ls ut , t1) , ls , ut) ∣₁ })
    (roundedUpperOf x q1 u1) })
  (equivFun (lowerRoundedIso x q0) l0)

-- Recursive membership uses paths explicitly, avoiding indexed-list matches.
Member : Inner → List Inner → Type
Member i [] = ⊥
Member i (j ∷ xs) = (i ≡ j) ⊎ Member i xs

FiniteCoversOpen : List Inner → Type₁
FiniteCoversOpen xs = (x : R) → OpenUnit x →
  ∥ Σ[ i ∈ Inner ] (Member i xs × CoveredBy i x) ∥₁

AllBound : ℚ → List Inner → Type
AllBound s [] = Unit
AllBound s (i ∷ xs) = (s Q.≤ leftEnd i) × AllBound s xs

rebound : (s r : ℚ) → s Q.≤ r → (xs : List Inner) → AllBound r xs → AllBound s xs
rebound s r sr [] bound = tt
rebound s r sr (i ∷ xs) (ri , rest) = Q.isTrans≤ s r (leftEnd i) sr ri , rebound s r sr xs rest

smallBound : (xs : List Inner) → Σ[ s ∈ ℚ ]
  ((q0 Q.< s) × ((s Q.≤ q1) × AllBound s xs))
smallBound [] = q1 , zero<one , Q.isRefl≤ q1 , tt
smallBound (i ∷ xs) with smallBound xs
... | r , positive , r1 , rest with Q.<Dec (leftEnd i) r
... | yes lr = leftEnd i , leftPositive i ,
  Q.<Weaken≤ (leftEnd i) q1 (leftBelowOne i) , Q.isRefl≤ (leftEnd i) ,
  rebound (leftEnd i) r (Q.<Weaken≤ (leftEnd i) r lr) xs rest
... | no notLR = r , positive , r1 , Q.≮→≥ (leftEnd i) r notLR , rest

lookupBound : (s : ℚ) (xs : List Inner) → AllBound s xs →
  (i : Inner) → Member i xs → s Q.≤ leftEnd i
lookupBound s [] bound i ()
lookupBound s (j ∷ xs) (sj , rest) i (inl same) =
  subst (λ k → s Q.≤ leftEnd k) (sym same) sj
lookupBound s (j ∷ xs) (sj , rest) i (inr mem) = lookupBound s xs rest i mem

noFiniteInnerCover : (xs : List Inner) → FiniteCoversOpen xs → ⊥
noFiniteInnerCover xs cover with smallBound xs
... | s , positive , s1 , bound = PT.rec isProp⊥
  (λ { (i , mem , li , ui) → Q.isAsym< point (leftEnd i)
    (Q.isTrans<≤ point s (leftEnd i) (midRight q0 s positive) (lookupBound s xs bound i mem)) li })
  (cover (rationalCut point)
    (midLeft q0 s positive , Q.isTrans<≤ point s q1 (midRight q0 s positive) s1))
  where
  point : ℚ
  point = mid q0 s

ClosedBetween : ℚ → ℚ → R → Type
ClosedBetween a b x = Above a x × ((q : ℚ) → Lower x q → q Q.< b)

upperBeyond : (x : R) (b : ℚ) → ((q : ℚ) → Lower x q → q Q.< b) →
  (r : ℚ) → b Q.< r → Upper x r
upperBeyond x b below r br = PT.rec (propUpper x r)
  (λ { (inl lb) → Empty.rec (Q.isIrrefl< b (below b lb))
     ; (inr ur) → ur }) (located x b r br)

innerChoice : (a b : ℚ) → q0 Q.< a → a Q.< b → b Q.< q1 → Inner
innerChoice a b posA ab b1 = mid q0 a , mid b q1 , midLeft q0 a posA ,
  Q.isTrans< (mid q0 a) a (mid b q1) (midRight q0 a posA)
    (Q.isTrans< a b (mid b q1) ab (midLeft b q1 b1)) ,
  midRight b q1 b1

innerClosedSingle : (a b : ℚ) → q0 Q.< a → a Q.< b → b Q.< q1 →
  Σ[ i ∈ Inner ] ((x : R) → ClosedBetween a b x → CoveredBy i x)
innerClosedSingle a b posA ab b1 = innerChoice a b posA ab b1 ,
  λ x (above , below) →
    above (mid q0 a) (midRight q0 a posA) ,
    upperBeyond x b below (mid b q1) (midLeft b q1 b1)

closedExample : Σ[ i ∈ Inner ] ((x : R) → ClosedBetween quarter threeQuarters x → CoveredBy i x)
closedExample = innerClosedSingle quarter threeQuarters
  (decWitness (Q.<Dec q0 quarter) tt)
  (decWitness (Q.<Dec quarter threeQuarters) tt)
  (decWitness (Q.<Dec threeQuarters q1) tt)
