{-# OPTIONS --cubical --guarded #-}
module Rev5TerminationOverrideForcedEquality where

open import Agda.Builtin.Cubical.Path
open import Agda.Builtin.Nat

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

{-# TERMINATING #-}
loop : Nat
loop = loop

distinct-normal-form : loop ≡ zero
distinct-normal-form = refl

