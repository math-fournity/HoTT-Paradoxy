{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda continuation of MP-RACE-TIMEOUT-001: the contextual
-- equivalence hierarchy for the R041 delay fragment. Contexts are built from
-- the hole, bind, and race on either side; observations are the deadline
-- family (R041 §6). Claims (continued numbering):
--   C-77  ≡c is an equivalence relation
--   C-78  ≡c refines result equivalence ≈ (empty context)
--   C-79  deadline 0 separates "returns later" from "returns immediately"
--   C-80  race against ω separates "returns" from "diverges"
--   C-81  bind with a value-moving continuation separates equal-time,
--         different-value runs
--   C-82  a time-aligned race separates strictly later returns
--   C-83  result equivalence is strictly coarser than ≡c: p0 ≈ p2 and ¬ p0 ≡c p2

module ContextualEquivalence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Bool.Base using (Bool; false; true; if_then_else_; not)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥; rec)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import PartialityRaceTimeout

private
  variable
    ℓ : Level
    A : Type ℓ

------------------------------------------------------------------
-- 1. Contexts and the contextual equivalence
------------------------------------------------------------------

data Ctx {ℓ : Level} (A : Type ℓ) : Type ℓ where
  hole : Ctx A
  cbind : Ctx A → (A → Delay A) → Ctx A
  crace₁ : Ctx A → Delay A → Ctx A
  crace₂ : Delay A → Ctx A → Ctx A

plug : {ℓ : Level} {A : Type ℓ} → Ctx A → Delay A → Delay A
plug hole d = d
plug (cbind C f) d = plug C d bind f
plug (crace₁ C q) d = plug C d race q
plug (crace₂ q C) d = q race plug C d

-- p ≡c q: every context sends p and q to results that are result-equivalent,
-- and every context+deadline pair cannot tell them apart.
_≡c_ : {ℓ : Level} {A : Type ℓ} → Delay A → Delay A → Type ℓ
_≡c_ {A = A} p q =
    ((C : Ctx A) → plug C p ≈ plug C q)
  × ((C : Ctx A) (k : ℕ) → deadline k (plug C p) ≡ deadline k (plug C q))
infix 4 _≡c_

------------------------------------------------------------------
-- 2. C-77: ≡c is an equivalence relation
------------------------------------------------------------------

≡c-refl : (p : Delay A) → p ≡c p
≡c-refl p = (λ C → ≈-refl (plug C p)) , (λ C k → refl)

≡c-sym : (p q : Delay A) → p ≡c q → q ≡c p
≡c-sym p q h =
    (λ C → ≈-sym (plug C p) (plug C q) (fst h C))
  , (λ C k → sym (snd h C k))

≡c-trans : (p q r : Delay A) → p ≡c q → q ≡c r → p ≡c r
≡c-trans p q r h h' =
    (λ C → ≈-trans (plug C p) (plug C q) (plug C r) (fst h C) (fst h' C))
  , (λ C k → snd h C k ∙ snd h' C k)

-- C-78: contextual equivalence refines result equivalence.
≡c-to-≈ : (p q : Delay A) → p ≡c q → p ≈ q
≡c-to-≈ p q h = fst h hole

------------------------------------------------------------------
-- 3. C-79..C-82: timing and value are not forgotten
------------------------------------------------------------------

isSomeO : {ℓ : Level} {A : Type ℓ} → Optional A → Bool
isSomeO none = false
isSomeO (some _) = true

-- C-79: returning after at least one round is distinguishable from returning
-- immediately, because deadline 0 observes exactly the immediate return.
deadline-zero-separates : (n : ℕ) (a : Bool) → ¬ (ret (suc n) a ≡c ret zero a)
deadline-zero-separates n a h = false≢true (cong isSomeO (snd h hole zero))

-- C-80: a returning run is distinguishable from a divergent one by racing
-- against ω.
divergence-separates : (n : ℕ) (a : Bool) → ¬ (ret n a ≡c ω)
divergence-separates n a h = lower (⇔-fwd (fst h (crace₁ hole ω) a) refl)

not-invol : (b : Bool) → not (not b) ≡ b
not-invol false = refl
not-invol true = refl

not≢self : (a : Bool) → ¬ (not a ≡ a)
not≢self false = true≢false
not≢self true = false≢true

-- C-81: the continuation x ↦ ret 0 (not x) moves the returned value, so two
-- same-time runs with different values are separated.
value-separates : (n : ℕ) (a b : Bool) → ¬ (a ≡ b) → ¬ (ret n a ≡c ret n b)
value-separates n a b a≠b h = a≠b (sym b≡a)
  where
    f : Bool → Delay Bool
    f x = ret zero (not x)

    C : Ctx Bool
    C = cbind hole f

    h1 : (ret n a bind f) ≈ (ret n b bind f)
    h1 = fst h C

    h2 : (ret n a bind f) ≈ (f a)
    h2 = bind-conv-ret n a f

    h3 : (ret n b bind f) ≈ (f b)
    h3 = bind-conv-ret n b f

    hfa≈fb : (f a) ≈ (f b)
    hfa≈fb =
      ≈-trans (f a) (ret n b bind f) (f b)
        (≈-trans (f a) (ret n a bind f) (ret n b bind f)
          (≈-sym (ret n a bind f) (f a) h2) h1)
        h3

    got : not b ≡ not a
    got = ⇔-fwd (hfa≈fb (not a)) refl

    b≡a : b ≡ a
    b≡a = sym (not-invol b) ∙ cong not got ∙ not-invol a

------------------------------------------------------------------
-- 4. C-82: strict time differences are separated
------------------------------------------------------------------

leb-refl : (n : ℕ) → leb n n ≡ true
leb-refl zero = refl
leb-refl (suc n) = leb-refl n

lt : ℕ → ℕ → Bool
lt zero zero = false
lt zero (suc _) = true
lt (suc _) zero = false
lt (suc n) (suc m) = lt n m

lt-leb : (n m : ℕ) → lt n m ≡ true → leb m n ≡ false
lt-leb zero zero p = rec (false≢true p)
lt-leb zero (suc m) _ = refl
lt-leb (suc n) zero p = rec (false≢true p)
lt-leb (suc n) (suc m) p = lt-leb n m p

lt-timing-separates : (n m : ℕ) (a : Bool) → lt n m ≡ true → ¬ (ret n a ≡c ret m a)
lt-timing-separates n m a lt-true h = not≢self a (⇔-fwd (step2 a) refl)
  where
    C : Ctx Bool
    C = crace₁ hole (ret n (not a))

    eqv : (ret n a race ret n (not a)) ≈ (ret m a race ret n (not a))
    eqv = fst h C

    ep : (ret n a race ret n (not a)) ≡ ret n a
    ep = cong (λ b → if b then ret n a else ret n (not a)) (leb-refl n)

    eq : (ret m a race ret n (not a)) ≡ ret n (not a)
    eq = cong (λ b → if b then ret m a else ret n (not a)) (lt-leb n m lt-true)

    step1 : ret n a ≈ (ret m a race ret n (not a))
    step1 = subst (λ x → x ≈ (ret m a race ret n (not a))) ep eqv

    step2 : ret n a ≈ ret n (not a)
    step2 = subst (λ x → ret n a ≈ x) eq step1

------------------------------------------------------------------
-- 5. C-83: result equivalence is strictly coarser than contextual equivalence
------------------------------------------------------------------

result-coarser-than-contextual : (p0 ≈ p2) × ¬ (p0 ≡c p2)
result-coarser-than-contextual =
  p0≈p2 , (λ h → true≢false (cong isSomeO (snd h hole (suc zero))))
