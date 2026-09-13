{-# OPTIONS --safe --cubical --guardedness #-}

-- Symbolic L3 target for MS-TASK-L3-INTERVAL-COMPLETION-001 / WV-0001.
-- I is tested as an activity-time carrier; no physical-time claim is made.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)

NoSeparatedObservable : Type₁
NoSeparatedObservable =
  {A : Type₀} → (f : I → A) → ((f i0 ≡ f i1) → ⊥) → ⊥
