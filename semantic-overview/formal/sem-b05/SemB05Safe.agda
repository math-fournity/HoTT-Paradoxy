{-# OPTIONS --safe #-}

module SemB05Safe where

open import Agda.Builtin.Bool
open import Agda.Builtin.Equality
open import Agda.Builtin.List
open import Agda.Builtin.Reflection
open import Agda.Builtin.Unit

visible-name : Name → Arg Name
visible-name q =
  arg (arg-info visible (modality relevant quantity-ω)) q

-- Same controlled macro as SemB05Unsafe, checked under Agda's safe mode.
macro
  postulate-goal! : Term → TC ⊤
  postulate-goal! hole =
    bindTC (inferType hole) λ goal →
    bindTC (freshName "sem-b05-declared-axiom") λ axiom-name →
    bindTC (declarePostulate (visible-name axiom-name) goal) λ _ →
    unify hole (def axiom-name [])

controlled-false-equality : true ≡ false
controlled-false-equality = postulate-goal!
