{-# OPTIONS --safe --cubical --guardedness #-}

-- N3: native Cubical Agda upgrade of the R036/R038 transition-abstraction
-- boundary.  The finite quotient/lift core (R036) and the truncation-limit
-- non-commutation core (R038-D) are formalised with native Path/HIT semantics.
module TransitionLift where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Transport
open import Cubical.Data.Nat
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.Data.Unit
open import Cubical.Data.Maybe
open import Cubical.HITs.PropositionalTruncation renaming (rec to PT-rec)

¬_ : Type → Type
¬ A = A → ⊥

------------------------------------------------------------------------
-- Part 1. The finite R036 model: a -> b -> d, abstraction {a,b} = w.

data S : Type where
  a b d : S

data Q : Type where
  w W : Q

α : S → Q
α a = w
α b = w
α d = W

-- The transition is a total step function into Maybe; R is its graph.
step : S → Maybe S
step a = just b
step b = just d
step d = nothing

R : S → S → Type
R x y = step x ≡ just y

data R* : S → S → Type where
  r* : ∀ s → R* s s
  s* : ∀ {x y z} → R x y → R* y z → R* x z

-- C-110: the concrete process terminates at d in two steps, and d is terminal.
C-110-terminates : R* a d
C-110-terminates = s* refl (s* refl (r* d))

NotJust : Maybe S → Type
NotJust nothing = Unit
NotJust (just _) = ⊥

nothing≢just : ∀ {s} → ¬ (nothing ≡ just s)
nothing≢just p = subst NotJust p tt

C-110-d-terminal : ¬ (Σ[ s ∈ S ] R d s)
C-110-d-terminal (s , p) = nothing≢just p

-- Discriminator for the two abstract states.
Bot : Q → Type
Bot w = ⊥
Bot W = Unit

W≢w : ¬ (W ≡ w)
W≢w p = subst Bot p tt

-- C : the successor of the *current* concrete state s, seen at abstract v.
C : S → Q → Type
C s v = ∥ Σ[ t ∈ S ] (R s t) × (α t ≡ v) ∥₁

-- E : the existential relation image; it only fixes the abstract endpoints.
E : Q → Q → Type
E u v = ∥ Σ[ x ∈ S ] Σ[ y ∈ S ] (α x ≡ u) × (R x y) × (α y ≡ v) ∥₁

-- C-111: the abstract graph has a self-loop at w (from a -> b) and a w -> W
-- edge (from b -> d); hence the constant-w path is an abstract infinite run.
C-111-e-ww : E w w
C-111-e-ww = ∣ a , b , refl , refl , refl ∣₁

C-111-e-wW : E w W
C-111-e-wW = ∣ b , d , refl , refl , refl ∣₁

β : ℕ → Q
β n = w

C-111-beta-path : ∀ n → E (β n) (β (suc n))
C-111-beta-path n = C-111-e-ww

AbstractTwo : Q → Q → Type
AbstractTwo u v = ∥ Σ[ m ∈ Q ] E u m × E m v ∥₁

C-112-abstract-two-www : AbstractTwo w w
C-112-abstract-two-www = ∣ w , C-111-e-ww , C-111-e-ww ∣₁

-- C-112: the abstract two-step prefix w,w,w has no concrete lift starting at a.
Lift2FromA : Type
Lift2FromA =
  Σ[ s₁ ∈ S ] Σ[ s₂ ∈ S ]
    (R a s₁) × (α s₁ ≡ w) × (R s₁ s₂) × (α s₂ ≡ w)

C-112-no-lift-two : ¬ Lift2FromA
C-112-no-lift-two (s₁ , s₂ , r₁ , p₁ , r₂ , p₂) =
  W≢w (subst (λ z → α z ≡ w)
             (sym (just-inj d s₂
                     (subst (λ z → step z ≡ just s₂) (sym (just-inj b s₁ r₁)) r₂)))
             p₂)

-- C-113: the exact current-state successor descent L fails: there is no
-- function that turns every E(α s, v) into C(s, v).  The witness is (b, w).
CurrentLift : Type
CurrentLift = ∀ s v → E (α s) v → C s v

C-113-no-current-lift : ¬ CurrentLift
C-113-no-current-lift l =
  PT-rec isProp⊥
    (λ { (t , r , p) → W≢w (subst (λ z → α z ≡ w) (sym (just-inj d t r)) p) })
    (l b w C-111-e-ww)

-- C-117: no rank can be simultaneously strictly descending on R and constant
-- on α-fibres; the merge of a and b therefore cannot descend the concrete rank.
_≤_ : ℕ → ℕ → Type
zero ≤ n = Unit
suc m ≤ zero = ⊥
suc m ≤ suc n = m ≤ n

_<_ : ℕ → ℕ → Type
m < n = suc m ≤ n

¬suc≤ : ∀ n → ¬ (suc n ≤ n)
¬suc≤ zero p = p
¬suc≤ (suc n) p = ¬suc≤ n p

rank-descends : (S → ℕ) → Type
rank-descends r = ∀ {x y} → R x y → r y < r x

fiber-constant : (S → ℕ) → Type
fiber-constant r = ∀ {x y} → α x ≡ α y → r x ≡ r y

C-117-no-descending-fiber-constant-rank :
  ¬ (Σ[ r ∈ (S → ℕ) ] rank-descends r × fiber-constant r)
C-117-no-descending-fiber-constant-rank (r , desc , fib) =
  ¬suc≤ (r a) (subst (λ z → suc z ≤ r a) (sym (fib refl)) (desc refl))

------------------------------------------------------------------------
-- Part 2. R038-D: truncating each stage and then taking the limit is not the
-- same as taking the limit and then truncating.  Here A k = Σ m, k ≤ m.

≤-refl : ∀ n → n ≤ n
≤-refl zero = tt
≤-refl (suc n) = ≤-refl n

≤-suc : ∀ {m n} → m ≤ n → m ≤ suc n
≤-suc {m = zero} p = tt
≤-suc {m = suc zero} {n = zero} ()
≤-suc {m = suc (suc m)} {n = zero} p = p
≤-suc {m = suc m} {n = suc n} p = ≤-suc {m = m} {n = n} p

≤-drop-suc : ∀ {k m} → suc k ≤ m → k ≤ m
≤-drop-suc {k = zero} {m = zero} ()
≤-drop-suc {k = suc k} {m = zero} p = p
≤-drop-suc {k = k} {m = suc m} p = ≤-suc {m = k} {n = m} p

A : ℕ → Type
A k = Σ[ m ∈ ℕ ] (k ≤ m)

j : ∀ k → A (suc k) → A k
j k (m , p) = m , ≤-drop-suc {k = k} {m = m} p

-- The exact compatible limit of the tower.
LimA : Type
LimA = Σ[ f ∈ (∀ k → A k) ] (∀ k → fst (f (suc k)) ≡ fst (f k))

first-constant :
  (f : ∀ k → A k)
  (h : ∀ k → fst (f (suc k)) ≡ fst (f k))
  → ∀ k → fst (f k) ≡ fst (f 0)
first-constant f h zero = refl
first-constant f h (suc k) = h k ∙ first-constant f h k

-- C-114: the exact limit is empty.
C-114-LimA-empty : ¬ LimA
C-114-LimA-empty (f , h) =
  ¬suc≤ (fst (f 0))
    (subst (λ z → suc (fst (f 0)) ≤ z)
           (first-constant f h (suc (fst (f 0))))
           (snd (f (suc (fst (f 0))))))

-- The same tower after truncating each stage.
LimTruncA : Type
LimTruncA =
  Σ[ f ∈ (∀ k → ∥ A k ∥₁) ]
    (∀ k → map (j k) (f (suc k)) ≡ f k)

-- C-115: the truncated limit is inhabited: each stage supplies its own bound.
C-115-limTrunc : LimTruncA
C-115-limTrunc = (λ k → ∣ k , ≤-refl k ∣₁) , λ k → squash₁ _ _

-- C-116: there is no inverse: a function from the truncated limit back to the
-- exact limit would inhabit the empty exact limit.
C-116-no-inverse : ¬ (LimTruncA → LimA)
C-116-no-inverse f = C-114-LimA-empty (f C-115-limTrunc)
