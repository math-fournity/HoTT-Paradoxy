{-# OPTIONS --cubical --guarded #-}
module BadForceDelayRefl where

open import Agda.Builtin.Nat
open import Agda.Builtin.Cubical.Path
open import Clocked.Primitives

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

zeroAlg : ∀ {k} → ▹ k Nat → Nat
zeroAlg _ = zero

family : ∀ k → ▹ k Nat
family k = dfix {k = k} zeroAlg

bad-force-delay-judgemental : ∀ k → ▸ k \ α → force family k ≡ family k α
bad-force-delay-judgemental k α = refl
