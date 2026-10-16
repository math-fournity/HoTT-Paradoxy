{-# OPTIONS --cubical --guarded #-}
module OrdinaryTickPath where

open import Agda.Builtin.Nat
open import Agda.Builtin.Cubical.Path
open import Clocked.Primitives

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

zeroAlg : ∀ {k} → ▹ k Nat → Nat
zeroAlg _ = zero

ordinary-unfolds-by-path : ∀ {k} → ▸ k \ α → dfix {k = k} zeroAlg α ≡ zero
ordinary-unfolds-by-path α = pfix' zeroAlg α
