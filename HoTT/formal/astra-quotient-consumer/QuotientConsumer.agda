{-# OPTIONS --safe --cubical --guardedness #-}
module QuotientConsumer where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Int.Base using (ℤ; pos)
import Cubical.Data.Int.Properties as Z
import Cubical.Data.Nat.Properties as N
open import Cubical.Data.NatPlusOne.Base using (ℕ₊₁; 1+_)
open import Cubical.Data.Rationals.Base using (ℚ; isSetℚ)
import Cubical.Data.Rationals.Base as Q
import Cubical.Data.Rationals.Properties as R
import Cubical.HITs.SetQuotients.Properties as SQ
import Cubical.HITs.PropositionalTruncation as PT
open PT using (∥_∥₁; ∣_∣₁; squash₁)
import CutGoldForm as GOLD

Frac : Type₀
Frac = ℤ × ℕ₊₁

pack : Frac → ℚ
pack = Q.[_]

oneRep twoRep zeroRep : Frac
oneRep = pos 1 , 1+ 0
twoRep = pos 2 , 1+ 1
zeroRep = pos 0 , 1+ 0

oneQ : ℚ
oneQ = pack oneRep

sameRational : pack oneRep ≡ pack twoRep
sameRational = Q.eq/ oneRep twoRep refl

differentNumerators : fst oneRep ≡ fst twoRep → ⊥
differentNumerators p = N.znots (N.injSuc (Z.injPos p))

-- Only the contract that preserves *every original* numerator is excluded.
OriginalNumerator : Type₀
OriginalNumerator = Σ[ observe ∈ (ℚ → ℤ) ] ((r : Frac) → observe (pack r) ≡ fst r)

noOriginalNumerator : OriginalNumerator → ⊥
noOriginalNumerator (observe , law) = differentNumerators
  (sym (law oneRep) ∙ cong observe sameRational ∙ law twoRep)

OriginalFraction : Type₀
OriginalFraction = Σ[ restore ∈ (ℚ → Frac) ] ((r : Frac) → restore (pack r) ≡ r)

noOriginalFraction : OriginalFraction → ⊥
noOriginalFraction (restore , law) = noOriginalNumerator
  ((λ q → fst (restore q)) , (λ r → cong fst (law r)))

quotientNotProp : isProp ℚ → ⊥
quotientNotProp collapse = N.znots
  (Z.injPos (Q.eq/⁻¹ zeroRep oneRep (collapse (pack zeroRep) oneQ)))

square : ℚ → ℚ
square q = R._·_ q q

addRespects : (a b c d : Frac) → a Q.∼ b → c Q.∼ d →
  R._+_ (pack a) (pack c) ≡ R._+_ (pack b) (pack d)
addRespects a b c d p q = cong₂ R._+_ (Q.eq/ a b p) (Q.eq/ c d q)

mulRespects : (a b c d : Frac) → a Q.∼ b → c Q.∼ d →
  R._·_ (pack a) (pack c) ≡ R._·_ (pack b) (pack d)
mulRespects a b c d p q = cong₂ R._·_ (Q.eq/ a b p) (Q.eq/ c d q)

lowerRespects : (a b : Frac) → a Q.∼ b → GOLD.L (pack a) ≡ GOLD.L (pack b)
lowerRespects a b p = cong GOLD.L (Q.eq/ a b p)

upperRespects : (a b : Frac) → a Q.∼ b → GOLD.U (pack a) ≡ GOLD.U (pack b)
upperRespects a b p = cong GOLD.U (Q.eq/ a b p)

Rep : ℚ → Type₀
Rep q = Σ[ r ∈ Frac ] pack r ≡ q

mereRep : (q : ℚ) → ∥ Rep q ∥₁
mereRep = SQ.[]surjective

squareRep : (q : ℚ) → Rep q → ℚ
squareRep q r = square (pack (fst r))

squareRepCorrect : (q : ℚ) (r : Rep q) → squareRep q r ≡ square q
squareRepCorrect q (r , same) = cong square same

squareRepConstant : (q : ℚ) (r s : Rep q) → squareRep q r ≡ squareRep q s
squareRepConstant q r s = squareRepCorrect q r ∙ sym (squareRepCorrect q s)

-- Actual elimination to the non-propositional set ℚ, with explicit constancy.
squareFromMere : (q : ℚ) → ∥ Rep q ∥₁ → ℚ
squareFromMere q = PT.rec→Set isSetℚ (squareRep q) (squareRepConstant q)

squareFromMereCorrect : (q : ℚ) (t : ∥ Rep q ∥₁) → squareFromMere q t ≡ square q
squareFromMereCorrect q = PT.elim
  (λ _ → isSetℚ _ _) (squareRepCorrect q)

SquareTask : ℚ → Type₀
SquareTask q = Σ[ out ∈ ℚ ] out ≡ square q

suppliedSquare : (q : ℚ) → ∥ Rep q ∥₁ → SquareTask q
suppliedSquare q t = squareFromMere q t , squareFromMereCorrect q t

generatedSquare : (q : ℚ) → SquareTask q
generatedSquare q = suppliedSquare q (mereRep q)

squareResponseCanonical : (q : ℚ) (t : ∥ Rep q ∥₁) → suppliedSquare q t ≡ (square q , refl)
squareResponseCanonical q t = Σ≡Prop (λ out → isSetℚ out (square q)) (squareFromMereCorrect q t)

repOne repTwo : Rep oneQ
repOne = oneRep , refl
repTwo = twoRep , sym sameRational

rawNumerator : Rep oneQ → ℤ
rawNumerator r = fst (fst r)

noNumeratorConstancy : ((r s : Rep oneQ) → rawNumerator r ≡ rawNumerator s) → ⊥
noNumeratorConstancy k = differentNumerators (k repOne repTwo)

RawFromMere : Type₀
RawFromMere = Σ[ observe ∈ (∥ Rep oneQ ∥₁ → ℤ) ]
  ((r : Rep oneQ) → observe ∣ r ∣₁ ≡ rawNumerator r)

noRawFromMere : RawFromMere → ⊥
noRawFromMere (observe , law) = differentNumerators
  (sym (law repOne) ∙ cong observe (squash₁ ∣ repOne ∣₁ ∣ repTwo ∣₁) ∙ law repTwo)

twoPresentationsSameSquare : squareFromMere oneQ ∣ repOne ∣₁ ≡ squareFromMere oneQ ∣ repTwo ∣₁
twoPresentationsSameSquare = squareRepConstant oneQ repOne repTwo

twoOverTwoSquared : square (pack twoRep) ≡ oneQ
twoOverTwoSquared = cong square (sym sameRational) ∙ R.·IdL oneQ

-- A chosen source is retained explicitly; it is not recovered from a bare quotient.
Rich : Type₀
Rich = Σ[ q ∈ ℚ ] Rep q

sourceNumerator : Rich → ℤ
sourceNumerator r = fst (fst (snd r))

richOne richTwo : Rich
richOne = oneQ , repOne
richTwo = oneQ , repTwo

sameBare : fst richOne ≡ fst richTwo
sameBare = refl

differentRich : richOne ≡ richTwo → ⊥
differentRich p = differentNumerators (cong sourceNumerator p)

chosenSourceLaw : (q : ℚ) (r : Rep q) → sourceNumerator (q , r) ≡ fst (fst r)
chosenSourceLaw q r = refl
