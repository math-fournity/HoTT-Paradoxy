{-# OPTIONS --cubical --guarded #-}
module ForceDelayPath where

open import Agda.Builtin.Nat
open import Agda.Builtin.Cubical.Path
open import Clocked.Primitives

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

zeroAlg : ∀ {k} → ▹ k Nat → Nat
zeroAlg _ = zero

family : ∀ k → ▹ k Nat
family k = dfix {k = k} zeroAlg

force-delay-is-path : ∀ k → ▸ k \ α → force family k ≡ family k α
force-delay-is-path = force-delay family
