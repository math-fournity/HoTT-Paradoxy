{-# OPTIONS --safe #-}

module SemB05SafeReflectionPositive where

open import Agda.Builtin.Bool
open import Agda.Builtin.Equality
open import Agda.Builtin.List
open import Agda.Builtin.Reflection
open import Agda.Builtin.Unit

-- Positive control: safe mode permits reflection that supplies an ordinary
-- proof term and does not declare a postulate.
macro
  refl-goal! : Term → TC ⊤
  refl-goal! hole = unify hole (con (quote refl) [])

safe-reflection-equality : true ≡ true
safe-reflection-equality = refl-goal!
