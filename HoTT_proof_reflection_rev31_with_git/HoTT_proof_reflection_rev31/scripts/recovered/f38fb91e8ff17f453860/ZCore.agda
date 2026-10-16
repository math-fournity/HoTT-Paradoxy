module ZCore where

open import Agda.Primitive using (Level)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Nat using (Nat; zero; suc)

data Empty : Set where

¬_ : ∀ {ℓ} → Set ℓ → Set ℓ
¬ A = A → Empty

_≢_ : ∀ {ℓ} {A : Set ℓ} → A → A → Set ℓ
x ≢ y = ¬ (x ≡ y)

sym : ∀ {ℓ} {A : Set ℓ} {x y : A} → x ≡ y → y ≡ x
sym refl = refl

trans : ∀ {ℓ} {A : Set ℓ} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q

cong : ∀ {ℓ ℓ'} {A : Set ℓ} {B : Set ℓ'}
  → (f : A → B) → {x y : A} → x ≡ y → f x ≡ f y
cong f refl = refl

cong₂ : ∀ {ℓa ℓb ℓc} {A : Set ℓa} {B : Set ℓb} {C : Set ℓc}
  → (f : A → B → C) → {a a' : A} {b b' : B}
  → a ≡ a' → b ≡ b' → f a b ≡ f a' b'
cong₂ f refl refl = refl

------------------------------------------------------------------------
-- Representation-loss core
------------------------------------------------------------------------

-- Necessary condition for exact recovery through a representation α:
-- the target observation J must be constant on every α-fiber.
fiber-truth-invariant :
  ∀ {ℓw ℓm ℓy} {W : Set ℓw} {M : Set ℓm} {Y : Set ℓy}
  → (α : W → M) → (J : W → Y) → (decode : M → Y)
  → ((w : W) → J w ≡ decode (α w))
  → {w₀ w₁ : W} → α w₀ ≡ α w₁ → J w₀ ≡ J w₁
fiber-truth-invariant α J decode exact {w₀} {w₁} same =
  trans (exact w₀) (trans (cong decode same) (sym (exact w₁)))

-- If an enriched representation (α, β) recovers an observation that α alone
-- collapses, then β must distinguish the collapsed worlds.  This is a
-- no-free-enrichment statement, not an inconsistency theorem.
no-free-enrichment :
  ∀ {ℓw ℓm ℓe ℓy}
  {W : Set ℓw} {M : Set ℓm} {E : Set ℓe} {Y : Set ℓy}
  → (α : W → M) → (β : W → E) → (J : W → Y)
  → (decode : M → E → Y)
  → ((w : W) → J w ≡ decode (α w) (β w))
  → {w₀ w₁ : W}
  → α w₀ ≡ α w₁
  → J w₀ ≢ J w₁
  → β w₀ ≢ β w₁
no-free-enrichment α β J decode exact {w₀} {w₁} α-same J-different β-same =
  J-different
    (trans (exact w₀)
      (trans (cong₂ decode α-same β-same) (sym (exact w₁))))

------------------------------------------------------------------------
-- Finite countermodels: provenance and direction are not recoverable from
-- a reduct that maps the two relevant worlds to the same value.
------------------------------------------------------------------------

data Bit : Set where
  b0 b1 : Bit

b0≢b1 : b0 ≢ b1
b0≢b1 ()

data Unit : Set where
  unit : Unit

data History : Set where
  history₀ history₁ : History

snapshot : History → Unit
snapshot _ = unit

provenance : History → Bit
provenance history₀ = b0
provenance history₁ = b1

snapshot-cannot-recover-provenance :
  (recover : Unit → Bit)
  → ¬ ((h : History) → recover (snapshot h) ≡ provenance h)
snapshot-cannot-recover-provenance recover exact =
  b0≢b1 (trans (sym (exact history₀)) (exact history₁))

data ProcessWorld : Set where
  forward backward : ProcessWorld

core : ProcessWorld → Unit
core _ = unit

direction : ProcessWorld → Bit
direction forward = b0
direction backward = b1

core-cannot-recover-direction :
  (recover : Unit → Bit)
  → ¬ ((w : ProcessWorld) → recover (core w) ≡ direction w)
core-cannot-recover-direction recover exact =
  b0≢b1 (trans (sym (exact forward)) (exact backward))

------------------------------------------------------------------------
-- Context underdetermination: identical surface data cannot determine two
-- incompatible context-sensitive targets without receiving the context.
------------------------------------------------------------------------

surface : Unit
surface = unit

context-target : Bit → Bit
context-target context = context

no-context-free-perfect-formalizer :
  (translate : Unit → Bit)
  → ¬ ((context : Bit) → translate surface ≡ context-target context)
no-context-free-perfect-formalizer translate exact =
  b0≢b1 (trans (sym (exact b0)) (exact b1))

------------------------------------------------------------------------
-- Two conditional fixed-point lemmas used to delimit, not exaggerate, the
-- temporal interpretation.
------------------------------------------------------------------------

transport : ∀ {ℓ ℓ'} {A : Set ℓ} (P : A → Set ℓ')
  → {x y : A} → x ≡ y → P x → P y
transport P refl u = u

apd : ∀ {ℓ ℓ'} {A : Set ℓ} {P : A → Set ℓ'}
  → (section : (x : A) → P x)
  → {x y : A} → (p : x ≡ y)
  → transport P p (section x) ≡ section y
apd section refl = refl

no-section-from-fixed-point-free-monodromy :
  ∀ {ℓ ℓ'} {B : Set ℓ} (P : B → Set ℓ')
  → (b : B) → (loop : b ≡ b)
  → ((u : P b) → transport P loop u ≢ u)
  → ¬ ((x : B) → P x)
no-section-from-fixed-point-free-monodromy P b loop fixed-point-free section =
  fixed-point-free (section b) (apd section loop)

guard-erasure-implies-fixed-point :
  ∀ {ℓ} {X : Set ℓ}
  → (F : X → X) → (trajectory : Nat → X) → (collapsed : X)
  → ((n : Nat) → trajectory (suc n) ≡ F (trajectory n))
  → ((n : Nat) → trajectory n ≡ collapsed)
  → collapsed ≡ F collapsed
guard-erasure-implies-fixed-point F trajectory collapsed step collapse =
  trans (sym (collapse (suc zero)))
    (trans (step zero) (cong F (collapse zero)))
