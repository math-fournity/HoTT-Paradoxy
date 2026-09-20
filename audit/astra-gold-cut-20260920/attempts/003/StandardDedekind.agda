{-# OPTIONS --safe --cubical --guardedness #-}
module StandardDedekind where

-- Standard truncated logic, with an explicit bridge to the Book's P = Q notation.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Equiv using (_≃_; propBiimpl→Equiv)
open import Cubical.Foundations.Univalence using (hPropExt)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; isPropPropTrunc)
open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.Data.Rationals.Order using (_<_)

LowerWitness UpperWitness : {ℓ : Level} → (ℚ → hProp ℓ) → ℚ → Type ℓ
LowerWitness L q = ∥ Σ[ r ∈ ℚ ] ((q < r) × fst (L r)) ∥₁
UpperWitness U r = ∥ Σ[ q ∈ ℚ ] ((q < r) × fst (U q)) ∥₁

Biimpl : {ℓ : Level} → Type ℓ → Type ℓ → Type ℓ
Biimpl A B = (A → B) × (B → A)

isPropBiimpl : {ℓ : Level} {A B : Type ℓ} → isProp A → isProp B → isProp (Biimpl A B)
isPropBiimpl pA pB = isProp× (isProp→ pB) (isProp→ pA)

dcutStd : {ℓ : Level} → (ℚ → hProp ℓ) → (ℚ → hProp ℓ) → Type ℓ
dcutStd L U =
  ∥ Σ[ q ∈ ℚ ] fst (L q) ∥₁ ×
  ∥ Σ[ r ∈ ℚ ] fst (U r) ∥₁ ×
  ((q : ℚ) → Biimpl (fst (L q)) (LowerWitness L q)) ×
  ((r : ℚ) → Biimpl (fst (U r)) (UpperWitness U r)) ×
  ((q : ℚ) → fst (L q) × fst (U q) → ⊥) ×
  ((q r : ℚ) → q < r → ∥ fst (L q) ⊎ fst (U r) ∥₁)

isPropDcutStd : {ℓ : Level} (L U : ℚ → hProp ℓ) → isProp (dcutStd L U)
isPropDcutStd L U =
  isProp× isPropPropTrunc (isProp× isPropPropTrunc
    (isProp× (isPropΠ (λ q → isPropBiimpl (snd (L q)) isPropPropTrunc))
      (isProp× (isPropΠ (λ r → isPropBiimpl (snd (U r)) isPropPropTrunc))
        (isProp× (isPropΠ (λ _ → isProp→ isProp⊥))
          (isPropΠ (λ _ → isPropΠ (λ _ → isProp→ isPropPropTrunc)))))))

StandardReals : (ℓ : Level) → Type (ℓ-suc ℓ)
StandardReals ℓ = Σ[ LU ∈ (ℚ → hProp ℓ) × (ℚ → hProp ℓ) ] dcutStd (fst LU) (snd LU)

standardRealsAreSet : (ℓ : Level) → isSet (StandardReals ℓ)
standardRealsAreSet ℓ =
  isSetΣ (isSet× (isSetΠ (λ _ → isSetHProp)) (isSetΠ (λ _ → isSetHProp)))
    (λ LU → isProp→isSet (isPropDcutStd (fst LU) (snd LU)))

lowerPredicate upperPredicate : {ℓ : Level} → StandardReals ℓ → ℚ → hProp ℓ
lowerPredicate x = fst (fst x)
upperPredicate x = snd (fst x)

-- Literal universe paths reside one level higher; no silent resizing is used.
dcutBook : {ℓ : Level} → (ℚ → hProp ℓ) → (ℚ → hProp ℓ) → Type (ℓ-suc ℓ)
dcutBook L U =
  ∥ Σ[ q ∈ ℚ ] fst (L q) ∥₁ ×
  ∥ Σ[ r ∈ ℚ ] fst (U r) ∥₁ ×
  ((q : ℚ) → fst (L q) ≡ LowerWitness L q) ×
  ((r : ℚ) → fst (U r) ≡ UpperWitness U r) ×
  ((q : ℚ) → fst (L q) × fst (U q) → ⊥) ×
  ((q r : ℚ) → q < r → ∥ fst (L q) ⊎ fst (U r) ∥₁)

isPropDcutBook : {ℓ : Level} (L U : ℚ → hProp ℓ) → isProp (dcutBook L U)
isPropDcutBook L U =
  isProp× isPropPropTrunc (isProp× isPropPropTrunc
    (isProp× (isPropΠ (λ q → isOfHLevel≡ 1 (snd (L q)) isPropPropTrunc))
      (isProp× (isPropΠ (λ r → isOfHLevel≡ 1 (snd (U r)) isPropPropTrunc))
        (isProp× (isPropΠ (λ _ → isProp→ isProp⊥))
          (isPropΠ (λ _ → isPropΠ (λ _ → isProp→ isPropPropTrunc)))))))

stdToBook : {ℓ : Level} (L U : ℚ → hProp ℓ) → dcutStd L U → dcutBook L U
stdToBook L U (a , b , rl , ru , dj , loc) = a , b ,
  (λ q → hPropExt (snd (L q)) isPropPropTrunc (fst (rl q)) (snd (rl q))) ,
  (λ r → hPropExt (snd (U r)) isPropPropTrunc (fst (ru r)) (snd (ru r))) , dj , loc

bookToStd : {ℓ : Level} (L U : ℚ → hProp ℓ) → dcutBook L U → dcutStd L U
bookToStd L U (a , b , rl , ru , dj , loc) = a , b ,
  (λ q → transport (rl q) , transport (sym (rl q))) ,
  (λ r → transport (ru r) , transport (sym (ru r))) , dj , loc

stdBookEquiv : {ℓ : Level} (L U : ℚ → hProp ℓ) → dcutStd L U ≃ dcutBook L U
stdBookEquiv L U = propBiimpl→Equiv (isPropDcutStd L U) (isPropDcutBook L U)
  (stdToBook L U) (bookToStd L U)
