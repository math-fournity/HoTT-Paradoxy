{-# OPTIONS --safe --cubical --guardedness #-}

-- N6: minimal native Cubical boundary between a strict classifier and a
-- partial classifier that is well defined only up to weak bisimilarity.
-- The source quotient identifies two representatives whose classifiers differ
-- strictly (now vs later); the strict classifier cannot descend, while the
-- weak-bisimilarity quotient of the delay fragment can receive it.
module PartialDecision where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.Data.Unit
open import Cubical.Data.Bool
open import Cubical.HITs.SetQuotients renaming (rec to SQ-rec)

¬_ : Type → Type
¬ A = A → ⊥

------------------------------------------------------------------------
-- Source states and a quotient that identifies a and b only.

data A : Type where
  a b c : A

R_A : A → A → Type
R_A a b = Unit
R_A _ _ = ⊥

Q : Type
Q = A / R_A

------------------------------------------------------------------------
-- Minimal delay/partiality fragment and its weak-bisimilarity-like relation.

data Delay (X : Type) : Type where
  now : X → Delay X
  later : Delay X → Delay X

R_D : Delay Bool → Delay Bool → Type
R_D (now x) (later (now y)) = x ≡ y
R_D _ _ = ⊥

D≈ : Type
D≈ = Delay Bool / R_D

isSet/ : ∀ {ℓ ℓ'} {X : Type ℓ} {R : X → X → Type ℓ'} → isSet (X / R)
isSet/ {X = X} {R = R} x y p q = squash/ {A = X} {R = R} x y p q

------------------------------------------------------------------------
-- The representative-level strict classifier and the strict observation.

P0 : A → Delay Bool
P0 a = now true
P0 b = later (now true)
P0 c = now false

strict : Delay Bool → Bool
strict (now _) = true
strict (later _) = false

IsNow : Delay Bool → Type
IsNow (now _) = Unit
IsNow (later _) = ⊥

now≢later : ¬ (now true ≡ later (now true))
now≢later p = subst IsNow p tt

-- C-118: the representative-level classifier exists by construction.
C-118-P0 : A → Delay Bool
C-118-P0 = P0

-- C-119: the strict observation separates now and later.
C-119-strict-separates : ¬ (strict (now true) ≡ strict (later (now true)))
C-119-strict-separates = true≢false

-- C-120: no strict Delay-valued function on the quotient extends P0.
StrictQuotient : Type
StrictQuotient =
  Σ[ g ∈ (Q → Delay Bool) ]
    (g [ a ] ≡ now true) × (g [ b ] ≡ later (now true))

C-120-no-strict-quotient : ¬ StrictQuotient
C-120-no-strict-quotient (g , pa , pb) =
  now≢later (sym pa ∙ cong g (eq/ a b tt) ∙ pb)

-- C-121: P0 is invariant up to R_D, so a partial classifier Q → D≈ exists.
inj : Delay Bool → D≈
inj = [_]

P-respect : (x y : A) → R_A x y → inj (P0 x) ≡ inj (P0 y)
P-respect a b r = eq/ {A = Delay Bool} {R = R_D} (now true) (later (now true)) refl
P-respect a a ()
P-respect a c ()
P-respect b a ()
P-respect b b ()
P-respect b c ()
P-respect c a ()
P-respect c b ()
P-respect c c ()

P : Q → D≈
P = SQ-rec (isSet/ {X = Delay Bool} {R = R_D}) (λ x → inj (P0 x)) P-respect

C-121-partial-classifier : Q → D≈
C-121-partial-classifier = P

-- C-122: no strict Bool consumer descends to the quotient.
StrictConsumer : Type
StrictConsumer =
  Σ[ h ∈ (Q → Bool) ]
    (h [ a ] ≡ true) × (h [ b ] ≡ false)

C-122-no-strict-consumer : ¬ StrictConsumer
C-122-no-strict-consumer (h , ha , hb) =
  true≢false (sym ha ∙ cong h (eq/ a b tt) ∙ hb)

-- C-123: at the representative level the strict consumer exists and
-- separates a from b; the information is lost only by the quotient.
C-123-representative-consumer : ¬ (strict (P0 a) ≡ strict (P0 b))
C-123-representative-consumer = true≢false
