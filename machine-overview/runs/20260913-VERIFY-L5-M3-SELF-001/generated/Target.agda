{-# OPTIONS --safe --cubical --guardedness #-}

-- M3/L5 exact self-coding target for MS-TASK-L5-SELF-GUARANTEE-001 / WV-0001.
-- The rejected strengthening is a section for every Bool predicate, not checking one proof.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Empty.Base using (⊥)

NoExactSelfCoding : Type₁
NoExactSelfCoding =
  {A : Type₀} → (encode : A → A → Bool) → (decode : (A → Bool) → A)
  → ((p : A → Bool) → encode (decode p) ≡ p) → ⊥
