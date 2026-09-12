module FiberTruthInvariant where

open import Agda.Primitive using (Level)
open import Agda.Builtin.Equality using (_≡_; refl)

sym : ∀ {ℓ} {A : Set ℓ} {x y : A} → x ≡ y → y ≡ x
sym refl = refl

trans : ∀ {ℓ} {A : Set ℓ} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q

cong : ∀ {ℓ ℓ'} {A : Set ℓ} {B : Set ℓ'} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
cong f refl = refl

fiberTruthInvariant :
  ∀ {ℓw ℓm ℓy} {W : Set ℓw} {M : Set ℓm} {Y : Set ℓy}
  (α : W → M) (J : W → Y) (Ĵ : M → Y)
  → ((w : W) → J w ≡ Ĵ (α w))
  → {w₀ w₁ : W} → α w₀ ≡ α w₁ → J w₀ ≡ J w₁
fiberTruthInvariant α J Ĵ recover {w₀} {w₁} p =
  trans (recover w₀) (trans (cong Ĵ p) (sym (recover w₁)))
