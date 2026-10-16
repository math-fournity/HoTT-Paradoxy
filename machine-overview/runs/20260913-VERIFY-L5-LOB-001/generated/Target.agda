{-# OPTIONS --safe #-}

-- L5 Löb/self-certification target for MS-TASK-L5-LOB-SELF-CERTIFICATION-001 / WV-0001.
-- This is a generic joint-interface boundary, not a claim about a qualified HoTT consumer.

module Target where

open import L5ConsumerSupport using (⊥)

NoLobSelfCertification : Set₁
NoLobSelfCertification =
  {Box : Set → Set}
  → ((A : Set) → Box A → A)
  → ((A : Set) → Box (Box A → A) → Box A)
  → ((A : Set) → Box (Box A → A))
  → ⊥
