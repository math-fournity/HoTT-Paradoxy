module GuardErasure where

open import Agda.Primitive using (Level)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Nat using (Nat; zero; suc)

sym : ∀ {ℓ} {A : Set ℓ} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
trans : ∀ {ℓ} {A : Set ℓ} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q
cong : ∀ {ℓ ℓ'} {A : Set ℓ} {B : Set ℓ'} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
cong f refl = refl

guardErasureImpliesFixedPoint :
  ∀ {ℓ} {X : Set ℓ} (F : X → X) (trajectory : Nat → X) (collapsed : X)
  → ((n : Nat) → trajectory (suc n) ≡ F (trajectory n))
  → ((n : Nat) → trajectory n ≡ collapsed)
  → collapsed ≡ F collapsed
guardErasureImpliesFixedPoint F trajectory collapsed step collapse =
  trans (sym (collapse (suc zero)))
    (trans (step zero) (cong F (collapse zero)))
