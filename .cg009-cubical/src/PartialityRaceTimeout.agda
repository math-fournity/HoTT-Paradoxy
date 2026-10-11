{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda formalization of the R041 partiality quotient /
-- race-timeout operation-closure question, following the delay model of the
-- R041 proof note: computations are single-thread delay objects, either ω
-- (never returns) or δ^n now(a) (returns a after n rounds).
--
-- Claims formalized here (continued numbering after MP-ERCF-TRUNC-001):
--   C-71  bind respects result equivalence (positive control, R041 §2)
--   C-72  bind descends to the Cubical set quotient by result equivalence (R041 §2.1)
--   C-73  race does not respect result equivalence (explicit finite witness, R041 §3)
--   C-74  a fixed business continuation separates an already-completed run from
--         a non-terminating one although the two inputs are result-equivalent (R041 §4)
--   C-75  the bounded-observation consumer (deadline/timeout) separates the same
--         result-equivalent pair (R041 §6)
--   C-76  no function on the set quotient implements race on representatives
--         (R041 §3, using Cubical's effectiveness of the quotient)

module PartialityRaceTimeout where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isProp×; isPropΠ; isOfHLevelLift)
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Bool.Base using (Bool; false; true; if_then_else_)
open import Cubical.Data.Bool.Properties using (isSetBool; true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥; ⊥*; rec*)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Relation.Binary.Base
open import Cubical.HITs.SetQuotients.Base using (_/_; [_]; eq/; squash/)
open import Cubical.HITs.SetQuotients.Properties using (rec; effective)

------------------------------------------------------------------
-- 1. The R041 object language: single-thread deterministic delay
------------------------------------------------------------------

data Delay {ℓ : Level} (A : Type ℓ) : Type ℓ where
  ω : Delay A
  ret : (n : ℕ) (a : A) → Delay A

later : {ℓ : Level} {A : Type ℓ} → Delay A → Delay A
later ω = ω
later (ret n a) = ret (suc n) a

iterLater : {ℓ : Level} {A : Type ℓ} → ℕ → Delay A → Delay A
iterLater zero d = d
iterLater (suc k) d = later (iterLater k d)

-- R041's finite convergence evidence p ⇓ a, read as a family of types.
Conv : {ℓ : Level} {A : Type ℓ} → Delay A → A → Type ℓ
Conv ω _ = ⊥*
Conv (ret _ a) b = a ≡ b

------------------------------------------------------------------
-- 2. Result equivalence (R041 §1) and small helpers
------------------------------------------------------------------

_⇔_ : {ℓ : Level} (A B : Type ℓ) → Type ℓ
A ⇔ B = (A → B) × (B → A)
infix 5 _⇔_

mk⇔ : {ℓ : Level} {A B : Type ℓ} → (A → B) → (B → A) → A ⇔ B
mk⇔ h h' = h , h'

⇔-fwd : {ℓ : Level} {A B : Type ℓ} → A ⇔ B → A → B
⇔-fwd = fst

⇔-bwd : {ℓ : Level} {A B : Type ℓ} → A ⇔ B → B → A
⇔-bwd = snd

⇔-refl : {ℓ : Level} (A : Type ℓ) → A ⇔ A
⇔-refl A = mk⇔ (λ x → x) (λ x → x)

⇔-sym : {ℓ : Level} {A B : Type ℓ} → A ⇔ B → B ⇔ A
⇔-sym e = mk⇔ (⇔-bwd e) (⇔-fwd e)

⇔-comp : {ℓ : Level} {A B C : Type ℓ} → A ⇔ B → B ⇔ C → A ⇔ C
⇔-comp e f = mk⇔ (λ x → ⇔-fwd f (⇔-fwd e x)) (λ x → ⇔-bwd e (⇔-bwd f x))

exFalso : {ℓ ℓ' : Level} {X : Type ℓ} → ⊥* {ℓ = ℓ'} → X
exFalso e = rec* e

¬_ : {ℓ : Level} → Type ℓ → Type ℓ
¬ A = A → ⊥

-- p ≈ q iff p and q have the same finite-convergence behaviour and value.
_≈_ : {ℓ : Level} {A : Type ℓ} → Delay A → Delay A → Type ℓ
_≈_ {A = A} p q = (b : A) → Conv p b ⇔ Conv q b
infix 4 _≈_

≈-refl : {ℓ : Level} {A : Type ℓ} (p : Delay A) → p ≈ p
≈-refl p b = ⇔-refl (Conv p b)

≈-sym : {ℓ : Level} {A : Type ℓ} (p q : Delay A) → p ≈ q → q ≈ p
≈-sym p q h b = ⇔-sym (h b)

≈-trans : {ℓ : Level} {A : Type ℓ} (p q r : Delay A) → p ≈ q → q ≈ r → p ≈ r
≈-trans p q r h h' b = ⇔-comp (h b) (h' b)

conv-path : {ℓ : Level} {A : Type ℓ} (p q : Delay A) (b : A)
  → p ≡ q → Conv p b ⇔ Conv q b
conv-path p q b e = mk⇔ (subst (λ d → Conv d b) e) (subst (λ d → Conv d b) (sym e))

------------------------------------------------------------------
-- 3. The R041 operations: bind and fair synchronous race
------------------------------------------------------------------

leb : ℕ → ℕ → Bool
leb zero _ = true
leb (suc _) zero = false
leb (suc m) (suc n) = leb m n

-- bind(now a, f) = δ(f a);  bind(δp, f) = δ(bind(p, f))   (R041 §1)
_bind_ : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  → Delay A → (A → Delay B) → Delay B
ω bind f = ω
ret n a bind f = later (iterLater n (f a))
infixl 6 _bind_

-- race(now a, q) = now a; race(δp, now b) = now b; race(δp, δq) = δ(race(p, q))
_race_ : {ℓ : Level} {A : Type ℓ} → Delay A → Delay A → Delay A
ω race q = q
ret m a race ω = ret m a
ret m a race ret n b = if leb m n then ret m a else ret n b
infixl 6 _race_

------------------------------------------------------------------
-- 4. Bounded observation: deadline/timeout consumer (R041 §6)
------------------------------------------------------------------

data Optional {ℓ : Level} (A : Type ℓ) : Type ℓ where
  none : Optional A
  some : A → Optional A

deadline : {ℓ : Level} {A : Type ℓ} → ℕ → Delay A → Optional A
deadline k ω = none
deadline k (ret n a) = if leb n k then some a else none

------------------------------------------------------------------
-- 5. C-71: bind respects result equivalence
------------------------------------------------------------------

later-conv : {ℓ : Level} {A : Type ℓ} (d : Delay A) (b : A)
  → Conv (later d) b ⇔ Conv d b
later-conv ω b = ⇔-refl (Conv ω b)
later-conv (ret n a) b = ⇔-refl (a ≡ b)

iterLater-conv : {ℓ : Level} {A : Type ℓ} (k : ℕ) (d : Delay A) (b : A)
  → Conv (iterLater k d) b ⇔ Conv d b
iterLater-conv zero d b = ⇔-refl (Conv d b)
iterLater-conv (suc k) d b =
  ⇔-comp (later-conv (iterLater k d) b) (iterLater-conv k d b)

bind-conv-ret : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (n : ℕ) (a : A) (f : A → Delay B) (b : B)
  → Conv (ret n a bind f) b ⇔ Conv (f a) b
bind-conv-ret n a f b =
  ⇔-comp (later-conv (iterLater n (f a)) b) (iterLater-conv n (f a) b)

bind-cong : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (p q : Delay A) (f g : A → Delay B)
  → p ≈ q → ((a : A) → f a ≈ g a) → (p bind f) ≈ (q bind g)
bind-cong ω ω f g h hf = ≈-refl ω
bind-cong ω (ret m a') f g h hf = exFalso (⇔-bwd (h a') refl)
bind-cong (ret n a) ω f g h hf = exFalso (⇔-fwd (h a) refl)
bind-cong (ret n a) (ret m a') f g h hf b =
  ⇔-comp (bind-conv-ret n a f b)
    (⇔-comp (hf a b)
      (⇔-comp (⇔-sym (conv-path (g a') (g a) b (cong g (⇔-fwd (h a) refl))))
        (⇔-sym (bind-conv-ret m a' g b))))

------------------------------------------------------------------
-- 6. C-72: bind descends to the Cubical set quotient
------------------------------------------------------------------

Q : {ℓ : Level} (A : Type ℓ) → Type ℓ
Q A = Delay A / (_≈_ {A = A})

_≋_ : {ℓ : Level} {A : Type ℓ} → Q A → Q A → Type ℓ
x ≋ y = x ≡ y
infix 4 _≋_

bind-descends : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (f : A → Delay B) (p q : Delay A)
  → p ≈ q → [ p bind f ] ≋ [ q bind f ]
bind-descends f p q h =
  eq/ (p bind f) (q bind f) (bind-cong p q f f h (λ a → ≈-refl (f a)))

bindQ : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (f : A → Delay B) → Q A → Q B
bindQ f = rec squash/ (λ p → [ p bind f ]) (λ p q h → bind-descends f p q h)

bindQ-β : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (f : A → Delay B) (p : Delay A) → bindQ f [ p ] ≋ [ p bind f ]
bindQ-β f p = refl

------------------------------------------------------------------
-- 7. C-73..C-75: explicit finite witnesses where timing is observable
------------------------------------------------------------------

p0 : Delay Bool
p0 = ret zero true

p2 : Delay Bool
p2 = ret (suc (suc zero)) true

q1 : Delay Bool
q1 = ret (suc zero) false

p0≈p2 : p0 ≈ p2
p0≈p2 b = ⇔-refl (true ≡ b)

-- race(p0, q1) = now true, but race(p2, q1) = ret 1 false.
race-noncongruent : ¬ ((p0 race q1) ≈ (p2 race q1))
race-noncongruent h = false≢true (⇔-fwd (h true) refl)

-- The business continuation maps the losing branch value to divergence.
deliver : Bool → Delay Bool
deliver true = ret zero true
deliver false = ω

Composed : Delay Bool → Delay Bool
Composed p = (p race q1) bind deliver

-- Composed p0 returns (after one more round); Composed p2 diverges.
completion-gap : ¬ (Composed p0 ≈ Composed p2)
completion-gap h = lower (⇔-fwd (h true) refl)

fromSome : Optional Bool → Bool
fromSome none = false
fromSome (some b) = b

-- deadline 1 p0 = some true, but deadline 1 p2 = none.
deadline-separation : ¬ (deadline (suc zero) p0 ≡ deadline (suc zero) p2)
deadline-separation e = true≢false (cong fromSome e)

------------------------------------------------------------------
-- 8. C-76: no quotient-level race selector
------------------------------------------------------------------

open BinaryRelation {A = Delay Bool} (_≈_ {A = Bool})
  using (isPropValued; isEquivRel; equivRel)

conv-prop : (d : Delay Bool) (b : Bool) → isProp (Conv d b)
conv-prop ω b = isOfHLevelLift 1 isProp⊥
conv-prop (ret n a) b = isSetBool a b

≈-isProp : isPropValued
≈-isProp p q =
  isPropΠ (λ b → isProp× (isPropΠ (λ _ → conv-prop q b)) (isPropΠ (λ _ → conv-prop p b)))

≈-isEquiv : isEquivRel
≈-isEquiv = equivRel (λ p → ≈-refl p) (λ p q h → ≈-sym p q h)
  (λ p q r h h' → ≈-trans p q r h h')

-- If some r on the set quotient implemented race on representatives, then
-- effectiveness of the quotient would turn [p0] ≡ [p2] into race p0 q1 ≈ race p2 q1.
no-quotient-race :
  (r : Q Bool → Q Bool → Q Bool) →
  ((p q : Delay Bool) → r [ p ] [ q ] ≡ [ (p race q) ]) →
  ⊥
no-quotient-race r β =
  race-noncongruent
    (effective {A = Delay Bool} {R = _≈_} ≈-isProp ≈-isEquiv
      (p0 race q1) (p2 race q1) path)
  where
    e : [ p0 ] ≋ [ p2 ]
    e = eq/ p0 p2 p0≈p2

    path : [ (p0 race q1) ] ≋ [ (p2 race q1) ]
    path = sym (β p0 q1) ∙ cong (λ x → r x [ q1 ]) e ∙ β p2 q1
