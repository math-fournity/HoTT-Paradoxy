{-# OPTIONS --safe #-}

-- Negative control: CCTT's all-clock force shape cannot consume one value
-- delayed at one fixed clock without additional cross-clock data.

module BadLocalFromGlobal where

module Bridge (Cl : Set) (Later : Cl → Set → Set) where
  GlobalLater : (Cl → Set) → Set
  GlobalLater A = (k : Cl) → Later k (A k)

  ForceGlobal : Set₁
  ForceGlobal = {A : Cl → Set} → GlobalLater A → (k : Cl) → A k

  badLocal : ForceGlobal → {A : Cl → Set} → (k : Cl) → Later k (A k) → A k
  badLocal force k delayed = force (λ _ → delayed) k

