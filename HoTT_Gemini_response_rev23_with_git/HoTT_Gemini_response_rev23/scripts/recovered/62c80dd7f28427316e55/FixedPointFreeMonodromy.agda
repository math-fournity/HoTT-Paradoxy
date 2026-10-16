module FixedPointFreeMonodromy where

open import Agda.Primitive using (Level)
open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where

¬_ : ∀ {ℓ} → Set ℓ → Set ℓ
¬ A = A → ⊥

transport : ∀ {ℓ ℓ'} {A : Set ℓ} (P : A → Set ℓ') {x y : A} → x ≡ y → P x → P y
transport P refl u = u

apd : ∀ {ℓ ℓ'} {A : Set ℓ} {P : A → Set ℓ'} (s : (x : A) → P x)
    {x y : A} (p : x ≡ y) → transport P p (s x) ≡ s y
apd s refl = refl

noSectionFromFixedPointFreeMonodromy :
  ∀ {ℓ ℓ'} {B : Set ℓ} (P : B → Set ℓ')
  (b : B) (loop : b ≡ b)
  → ((u : P b) → ¬ (transport P loop u ≡ u))
  → ¬ ((x : B) → P x)
noSectionFromFixedPointFreeMonodromy P b loop fixedPointFree s =
  fixedPointFree (s b) (apd s loop)
