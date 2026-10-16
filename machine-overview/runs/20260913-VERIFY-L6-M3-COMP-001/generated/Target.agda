{-# OPTIONS --safe --cubical --guardedness #-}

-- M3/L6 compensation-composition target for MS-TASK-L6-COMPENSATION-COHERENCE-001 / WV-0001.
-- Path coherence and exact endpoint apartness are tested on the same endpoints.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)

NoJointPathAndApart : Type₁
NoJointPathAndApart =
  {A : Type₀} {x y : A} → x ≡ y → ((x ≡ y) → ⊥) → ⊥
