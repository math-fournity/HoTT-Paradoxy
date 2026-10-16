{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda first machine construction for the online-causality
-- direction (DIR-L-TIME-WORK-DIMENSION): separate complete stream functions
-- from strategies that may read only inputs already arrived.
--
--   C-106  no online strategy can output the second input at time 0 (the
--          time-0 prefix is a single value and cannot distinguish witnesses)
--   C-107  positive control: the first input is readable online at time 0
--   C-108  positive control: the second input is readable online from time 1
--   C-109  the knowledge gap: a complete stream function computes the second
--          input, but no time-0 online strategy does
--
-- Boundary result, not a HoTT paradox; no physical-time claim.

module OnlineCausality where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Base using () renaming (rec to ⊥-rec)

¬_ : {ℓ : Level} → Type ℓ → Type ℓ
¬ A = A → ⊥

------------------------------------------------------------------
-- 1. Source calculus: streams, prefixes and online strategies
------------------------------------------------------------------

Stream : Type
Stream = ℕ → Bool

-- The prefix available at time n: a nested pair of the first n+1 inputs.
Prefix : ℕ → Type
Prefix zero = Bool
Prefix (suc n) = Bool × Prefix n

prefixOf : Stream → (n : ℕ) → Prefix n
prefixOf s zero = s zero
prefixOf s (suc n) = s zero , prefixOf (λ k → s (suc k)) n

-- Reading the first (time-0) input from a prefix.
first : (n : ℕ) → Prefix n → Bool
first zero p = p
first (suc n) p = fst p

first-correct : (s : Stream) (n : ℕ) → first n (prefixOf s n) ≡ s zero
first-correct s zero = refl
first-correct s (suc n) = refl

-- An online strategy at time n may depend only on the prefix up to n.
OnlineStrategy : Type
OnlineStrategy = (n : ℕ) → Prefix n → Bool

-- A complete (omniscient) stream function.
CompleteMove : Type
CompleteMove = Stream → Bool

------------------------------------------------------------------
-- 2. C-106: no time-0 lookahead
------------------------------------------------------------------

no-zero-time-lookahead :
  ¬ (Σ[ g ∈ OnlineStrategy ] ((s : Stream) → g zero (prefixOf s zero) ≡ s (suc zero)))
no-zero-time-lookahead (g , eq) =
  false≢true (sym (eq s₁) ∙ cong (λ p → g zero p) peq ∙ eq s₂)
  where
  s₁ : Stream
  s₁ _ = false

  s₂ : Stream
  s₂ zero = false
  s₂ (suc _) = true

  -- both time-0 prefixes are the single value false
  peq : prefixOf s₁ zero ≡ prefixOf s₂ zero
  peq = refl

------------------------------------------------------------------
-- 3. C-107/C-108: positive controls
------------------------------------------------------------------

readFirst : OnlineStrategy
readFirst n p = first n p

first-input-online :
  Σ[ g ∈ OnlineStrategy ] ((s : Stream) → g zero (prefixOf s zero) ≡ s zero)
first-input-online = readFirst , (λ s → refl)

readSecond : OnlineStrategy
readSecond zero p = false
readSecond (suc n) p = first n (snd p)

second-input-online-later :
  (s : Stream) (n : ℕ) → readSecond (suc n) (prefixOf s (suc n)) ≡ s (suc zero)
second-input-online-later s n = first-correct (λ k → s (suc k)) n

------------------------------------------------------------------
-- 4. C-109: the knowledge gap
------------------------------------------------------------------

complete-second : CompleteMove
complete-second s = s (suc zero)

complete-second-correct : (s : Stream) → complete-second s ≡ s (suc zero)
complete-second-correct s = refl

knowledge-gap :
  CompleteMove
  × ¬ (Σ[ g ∈ OnlineStrategy ] ((s : Stream) → g zero (prefixOf s zero) ≡ s (suc zero)))
knowledge-gap = complete-second , no-zero-time-lookahead
