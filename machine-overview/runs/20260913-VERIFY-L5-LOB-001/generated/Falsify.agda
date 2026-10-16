{-# OPTIONS --safe #-}

module Falsify where

open import L5ConsumerSupport using (⊥)

-- Negative control: reflection plus a Löb rule is missing the boxed
-- reflection premise; omitting internal certification must be rejected.
bad : {Box : Set → Set}
    → ((A : Set) → Box A → A)
    → ((A : Set) → Box (Box A → A) → Box A)
    → ⊥
bad reflect lob = reflect ⊥ (lob ⊥)
