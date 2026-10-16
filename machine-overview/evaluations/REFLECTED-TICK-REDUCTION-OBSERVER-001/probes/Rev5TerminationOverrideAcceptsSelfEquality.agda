{-# OPTIONS --cubical --guarded #-}
module Rev5TerminationOverrideAcceptsSelfEquality where

open import Agda.Builtin.Cubical.Path
open import Agda.Builtin.Nat

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

{-# TERMINATING #-}
loop : Nat
loop = loop

self-equality : loop ≡ loop
self-equality = refl

