{-# OPTIONS --without-K #-}

module agda.exp-path where

open import agda.prelude
open import agda.postulates

----------------------------------------------------------------------
-- The path functor given by exponentiating by 𝕀
----------------------------------------------------------------------
℘ :
  {l : Level}
  (Γ : Set l)
  → ---------
  Set l
℘ Γ = 𝕀 → Γ

℘` :
  {l m : Level}
  {Γ : Set l}
  {Δ : Set m}
  (γ : Δ → Γ)
  → -----------
  ℘ Δ → ℘ Γ
℘` γ p i = γ (p i)

℘`comp :
  {l m n : Level}
  {Γ : Set l}
  {Δ : Set m}
  {Θ : Set n}
  (γ : Δ → Γ)
  (σ : Θ → Δ)
  (p : ℘ Θ)
  → -----------
  ℘` γ (℘` σ p) ≡ ℘` (γ ∘ σ) p
℘`comp _ _ _ = refl

