{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda conclusion of the contextual-equivalence strand for the
-- R041 delay fragment (continuation of MP-CONTEXTUAL-EQUIV-001):
--
--   C-89  lt/leb trichotomy: for all n m, either n ≡ m, or lt n m ≡ true, or
--         lt m n ≡ true
--   C-90  general strict-time separation: for n ≢ m, ret n a and ret m a are
--         not contextually equivalent
--   C-91  full characterization on the Bool fragment: p ≡c q ↔ p ≡ q — the
--         coarsest equivalence respected by the fixed context family is
--         exactly representational equality (hence no further context
--         extension can distinguish more: identity is already the finest)

module ContextCharacterization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; if_then_else_)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Empty.Base using () renaming (rec to ⊥-rec)
open import PartialityRaceTimeout
open import ContextualEquivalence

------------------------------------------------------------------
-- 1. C-89: trichotomy for the strict comparison used by race
------------------------------------------------------------------

lt-trichotomy : (n m : ℕ) → (n ≡ m) ⊎ ((lt n m ≡ true) ⊎ (lt m n ≡ true))
lt-trichotomy zero zero = inl refl
lt-trichotomy zero (suc m) = inr (inl refl)
lt-trichotomy (suc n) zero = inr (inr refl)
lt-trichotomy (suc n) (suc m) with lt-trichotomy n m
... | inl e = inl (cong suc e)
... | inr (inl p) = inr (inl p)
... | inr (inr p) = inr (inr p)

------------------------------------------------------------------
-- 2. C-90: general strict-time separation
------------------------------------------------------------------

timing-separates : (n m : ℕ) (a : Bool) → ¬ (n ≡ m) → ¬ (ret n a ≡c ret m a)
timing-separates n m a n≠m h with lt-trichotomy n m
... | inl e = n≠m e
... | inr (inl p) = lt-timing-separates n m a p h
... | inr (inr p) = lt-timing-separates m n a p (≡c-sym (ret n a) (ret m a) h)

------------------------------------------------------------------
-- 3. C-91: full characterization of ≡c on the Bool fragment
------------------------------------------------------------------

-- deadline at the return time of a canonical immediate return
dl-refl : (k : ℕ) (c : Bool) → deadline k (ret k c) ≡ some c
dl-refl k c = cong (λ z → if z then some c else none) (leb-refl k)

dl-lt : (n m : ℕ) (b : Bool) → lt n m ≡ true → deadline n (ret m b) ≡ none
dl-lt n m b p = cong (λ z → if z then some b else none) (lt-leb n m p)

dl-gt : (n m : ℕ) (a : Bool) → lt m n ≡ true → deadline m (ret n a) ≡ none
dl-gt n m a p = cong (λ z → if z then some a else none) (lt-leb m n p)

deadline-lt-separates : (n m : ℕ) (a b : Bool)
  → lt n m ≡ true → ¬ (ret n a ≡c ret m b)
deadline-lt-separates n m a b p h =
  true≢false (cong isSomeO (sym (dl-refl n a) ∙ snd h hole n ∙ dl-lt n m b p))

deadline-gt-separates : (n m : ℕ) (a b : Bool)
  → lt m n ≡ true → ¬ (ret n a ≡c ret m b)
deadline-gt-separates n m a b p h =
  false≢true (cong isSomeO (sym (dl-gt n m a p) ∙ snd h hole m ∙ dl-refl m b))

same-time-values : (n m : ℕ) (a b : Bool)
  → (n ≡ m) → ret n a ≡c ret m b → a ≡ b
same-time-values n m a b e h =
  cong fromSome (sym (dl-refl n a) ∙ snd h' hole n ∙ dl-refl n b)
  where
  h' : ret n a ≡c ret n b
  h' = subst (λ x → ret n a ≡c x) (cong (λ k → ret k b) (sym e)) h

≡-to-≡c : (p q : Delay Bool) → p ≡ q → p ≡c q
≡-to-≡c p q e = subst (λ x → p ≡c x) e (≡c-refl p)

≡c-to-≡ : (p q : Delay Bool) → p ≡c q → p ≡ q
≡c-to-≡ ω ω h = refl
≡c-to-≡ ω (ret m b) h = ⊥-rec (divergence-separates m b (≡c-sym ω (ret m b) h))
≡c-to-≡ (ret n a) ω h = ⊥-rec (divergence-separates n a h)
≡c-to-≡ (ret n a) (ret m b) h with lt-trichotomy n m
... | inl n≡m =
      cong (λ k → ret k a) n≡m ∙ cong (ret m) (same-time-values n m a b n≡m h)
... | inr (inl p) = ⊥-rec (deadline-lt-separates n m a b p h)
... | inr (inr p) = ⊥-rec (deadline-gt-separates n m a b p h)

≡c-iff-≡ : (p q : Delay Bool) → (p ≡c q) ⇔ (p ≡ q)
≡c-iff-≡ p q = mk⇔ (≡c-to-≡ p q) (≡-to-≡c p q)
