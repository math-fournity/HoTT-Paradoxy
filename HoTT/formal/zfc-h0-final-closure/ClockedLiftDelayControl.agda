{-# OPTIONS --cubical --guarded #-}
{-
  Candidate M1 operational target, to be checked only with the frozen
  forcing-ticks Agda compiler and agda/guarded source named in F1-E.

  This does *not* translate fixed Cubical Agda H0.  It isolates the exact
  operational shape that an eventual translation would have to preserve:
  a coinductive Delay-like carrier, one-step force, a silent object, and
  finite observation.  The target's separate `in∀/out-in-∀` postulates and
  missing H0 universe/HIT map remain outside this file's proposed scope.
-}
module ClockedLiftDelayControl where

open import Agda.Primitive using (Level; _⊔_)
open import Clocked.Lift

private
  variable
    ℓ : Level
    A : Set ℓ

data _⊎_ {ℓ} (A B : Set ℓ) : Set ℓ where
  inl : A → A ⊎ B
  inr : B → A ⊎ B

data Nat : Set where
  zero : Nat
  suc  : Nat → Nat

data Maybe {ℓ} (A : Set ℓ) : Set ℓ where
  nothing : Maybe A
  just    : A → Maybe A

data ⊥ : Set where

¬_ : Set ℓ → Set ℓ
¬ P = P → ⊥

-- `∀Lift` is the source library's clock-quantified coinductive carrier.
force : ∀ {ℓ} {A : Set ℓ} → ∀Lift A → A ⊎ ∀Lift A
force (∀Lift.now a) = inl a
force (∀Lift.step d) = inr (∀Lift'.uncon d)

-- The recursive occurrence sits underneath the source library's coinductive
-- record constructor.  Acceptance/rejection by the matching target compiler
-- is a real discriminant for this candidate operational target.
never : ∀ {ℓ} {A : Set ℓ} → ∀Lift A
never = ∀Lift.step (∀Lift'.con never)

runFor : ∀ {ℓ} {A : Set ℓ} → Nat → ∀Lift A → Maybe A
runFor zero    d             = nothing
runFor (suc n) (∀Lift.now a) = just a
runFor (suc n) (∀Lift.step d) = runFor n (∀Lift'.uncon d)

never-silent : ∀ {ℓ} {A : Set ℓ} (n : Nat) → runFor n (never {A = A}) ≡ nothing
never-silent zero    = refl
never-silent (suc n) = never-silent n

now-visible : ∀ {ℓ} {A : Set ℓ} (n : Nat) (a : A) → runFor (suc n) (∀Lift.now a) ≡ just a
now-visible n a = refl

nothing≢just : ∀ {ℓ} {A : Set ℓ} (a : A) → ¬ (nothing ≡ just a)
nothing≢just a ()

never-has-no-finite-answer : ∀ {ℓ} {A : Set ℓ} (n : Nat) (a : A) →
  ¬ (runFor n (never {A = A}) ≡ just a)
never-has-no-finite-answer zero a p = nothing≢just a p
never-has-no-finite-answer (suc n) a p = never-has-no-finite-answer n a p
