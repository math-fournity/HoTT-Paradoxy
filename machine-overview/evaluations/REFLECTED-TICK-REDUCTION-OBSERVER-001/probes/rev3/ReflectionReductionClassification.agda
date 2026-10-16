{-# OPTIONS --cubical --guarded #-}
module ReflectionReductionClassification where

open import Agda.Builtin.Bool
open import Agda.Builtin.Cubical.Path
open import Agda.Builtin.List
open import Agda.Builtin.Nat
open import Agda.Builtin.Reflection
open import Agda.Builtin.Unit
open import Clocked.Primitives

infixl 1 _>>=_
_>>=_ : ∀ {a b} {A : Set a} {B : Set b} → TC A → (A → TC B) → TC B
_>>=_ = bindTC

refl : ∀ {ℓ} {A : Set ℓ} {x : A} → x ≡ x
refl {x = x} _ = x

zeroAlg : ∀ {k} → ▹ k Nat → Nat
zeroAlg _ = zero

family : ∀ k → ▹ k Nat
family k = dfix {k = k} zeroAlg

boolTerm : Bool → Term
boolTerm false = con (quote false) []
boolTerm true  = con (quote true) []

isZeroTerm : Term → Bool
isZeroTerm (lit (nat zero)) = true
isZeroTerm (con c []) = primQNameEquality c (quote zero)
isZeroTerm _ = false

macro
  normaliseTerm : Term → Term → TC ⊤
  normaliseTerm t hole = normalise t >>= λ r → unify hole r

  normalisedIsZero : Term → Term → TC ⊤
  normalisedIsZero t hole =
    normalise t >>= λ r → unify hole (boolTerm (isZeroTerm r))

  roundTripNat : Term → Term → TC ⊤
  roundTripNat t hole =
    unquoteTC t >>= λ (x : Nat) → quoteTC x >>= λ q → unify hole q

directForceObs : ∀ k → Bool
directForceObs k = normalisedIsZero (force family k)

directForceObs-is-true : ∀ k → directForceObs k ≡ true
directForceObs-is-true k = refl

directOrdinaryObs : ∀ {k} → ▸ k \ α → Bool
directOrdinaryObs {k} α = normalisedIsZero (dfix {k = k} zeroAlg α)

directOrdinaryObs-is-false : ∀ {k} → ▸ k \ α → directOrdinaryObs α ≡ false
directOrdinaryObs-is-false α = refl

objectObserve : Nat → Bool
objectObserve x = normalisedIsZero x

objectObserve-is-constant : ∀ x → objectObserve x ≡ false
objectObserve-is-constant x = refl

objectObserve-respects-force-delay
  : ∀ {k} (f : ∀ k → ▹ k Nat) → ▸ k \ α
  → objectObserve (force f k) ≡ objectObserve (f k α)
objectObserve-respects-force-delay f α =
  λ i → objectObserve (force-delay f _ α i)

diamond-roundtrip : ∀ k → Nat
diamond-roundtrip k = roundTripNat (force family k)

ordinary-roundtrip : ∀ {k} → ▸ k \ α → Nat
ordinary-roundtrip {k} α = roundTripNat (dfix {k = k} zeroAlg α)

diamond-roundtrip-is-zero : ∀ k → diamond-roundtrip k ≡ zero
diamond-roundtrip-is-zero k = refl

ordinary-roundtrip-path : ∀ {k} → ▸ k \ α → ordinary-roundtrip α ≡ zero
ordinary-roundtrip-path α = pfix' zeroAlg α

