{-# OPTIONS --cubical --guarded #-}
module Rev5GuardedInfiniteNormalisation where

open import Agda.Builtin.Cubical.Path
open import Agda.Builtin.Nat
open import Agda.Builtin.Reflection
open import Agda.Builtin.Unit
open import Clocked.Primitives

infixl 1 _>>=_
_>>=_ : ∀ {a b} {A : Set a} {B : Set b} → TC A → (A → TC B) → TC B
_>>=_ = bindTC

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

data GStream : Set where
  cons : Nat → ▹ k0 GStream → GStream

repeat : GStream
repeat = fix {k = k0} λ later → cons zero later

head : GStream → Nat
head (cons n _) = n

macro
  normaliseTerm : Term → Term → TC ⊤
  normaliseTerm t hole = normalise t >>= λ r → unify hole r

normalised-repeat : GStream
normalised-repeat = normaliseTerm repeat

normalised-repeat-head : head normalised-repeat ≡ zero
normalised-repeat-head = refl

