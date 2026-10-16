{-# OPTIONS --cubical --guarded #-}
module Rev4ReflectionNormalisesRecursiveTerm where

open import Agda.Builtin.Nat
open import Agda.Builtin.Reflection
open import Agda.Builtin.Unit

infixl 1 _>>=_
_>>=_ : ∀ {a b} {A : Set a} {B : Set b} → TC A → (A → TC B) → TC B
_>>=_ = bindTC

{-# TERMINATING #-}
loop : Nat
loop = loop

macro
  normaliseTerm : Term → Term → TC ⊤
  normaliseTerm t hole = normalise t >>= λ r → unify hole r

reflected-normal-form : Nat
reflected-normal-form = normaliseTerm loop

