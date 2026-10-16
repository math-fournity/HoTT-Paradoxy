-- N2 audit: an LEM-based Bool classifier is a well-typed object-layer function.
-- Question: does the Agda compilation interface silently deliver an effective
-- implementation for it, or does it refuse without an explicit COMPILE pragma?
module LemClassifier where

data Bool : Set where
  true false : Bool

data ⊥ : Set where

data _⊎_ (A B : Set) : Set where
  inj₁ : A → A ⊎ B
  inj₂ : B → A ⊎ B

data ℕ : Set where
  zero : ℕ
  suc : ℕ → ℕ

postulate
  lem : (P : Set) → P ⊎ (P → ⊥)

-- Control 3: the LEM-based mathematical classifier chi.
chi : (P : Set) → Bool
chi P with lem P
... | inj₁ _ = true
... | inj₂ _ = false

-- Control 2: classical branches with equal constants.
equalConst : (P : Set) → Bool
equalConst P with lem P
... | inj₁ _ = true
... | inj₂ _ = true

-- Control 1: bounded-step halt detection (total, no LEM).
haltWithin : ℕ → Bool
haltWithin n = true
