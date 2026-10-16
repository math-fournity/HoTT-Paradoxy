{-# OPTIONS --safe --cubical --guardedness #-}

-- M4-lite Path-coherence target for MS-TASK-L3-PATH-COHERENCE-POSITIVE-001 / WV-0001.
-- This is the positive task in which cubical Path coherence is the requested output.

module Target where

open import Cubical.Foundations.Prelude

PathCarrierCoherence : Type₁
PathCarrierCoherence = {A : Type₀} → (f : I → A) → f i0 ≡ f i1
