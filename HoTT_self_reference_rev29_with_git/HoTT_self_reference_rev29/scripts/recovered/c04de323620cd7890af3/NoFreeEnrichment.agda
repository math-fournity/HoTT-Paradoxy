module NoFreeEnrichment where

open import Agda.Primitive using (Level)
open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where
¬_ : ∀ {ℓ} → Set ℓ → Set ℓ
¬ A = A → ⊥
_≢_ : ∀ {ℓ} {A : Set ℓ} → A → A → Set ℓ
x ≢ y = ¬ (x ≡ y)

sym : ∀ {ℓ} {A : Set ℓ} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
trans : ∀ {ℓ} {A : Set ℓ} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q
cong₂ : ∀ {ℓa ℓb ℓc} {A : Set ℓa} {B : Set ℓb} {C : Set ℓc}
      (f : A → B → C) {a a' : A} {b b' : B}
      → a ≡ a' → b ≡ b' → f a b ≡ f a' b'
cong₂ f refl refl = refl

noFreeEnrichment :
  ∀ {ℓw ℓm ℓe ℓy}
  {W : Set ℓw} {M : Set ℓm} {E : Set ℓe} {Y : Set ℓy}
  (α : W → M) (β : W → E) (F : W → Y) (recover : M → E → Y)
  → ((w : W) → F w ≡ recover (α w) (β w))
  → {w₀ w₁ : W}
  → α w₀ ≡ α w₁
  → F w₀ ≢ F w₁
  → β w₀ ≢ β w₁
noFreeEnrichment α β F recover exact {w₀} {w₁} αeq Fneq βeq =
  Fneq (trans (exact w₀)
    (trans (cong₂ recover αeq βeq) (sym (exact w₁))))
