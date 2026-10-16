{-# OPTIONS --safe --cubical --guardedness #-}

-- Coordinator-templated proof for CASE-GEN001-EXISTENCE-001 / WV-0017.
-- The proof only instantiates pinned support lemmas with computable facts.

module Proof where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import PartialityRaceTimeout
open import Target
open import MVSupport

equiv : Target.p ≈ Target.q
equiv = MVSupport.≈-same-ret zero (suc zero) false

gap : ¬ (Target.left ≈ Target.right)
gap h = lower (⇔-bwd (h false) refl)
