{-# OPTIONS --safe --cubical --guardedness #-}

-- Positive controls: a completion-preserving consumer does not separate
-- the same result-equivalent pair, while the declared consumer does.

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import PartialityRaceTimeout
open import Target
open import Proof

keeping : Bool → Delay Bool
keeping _ = ret zero true

preserved : (Target.p bind keeping) ≈ (Target.q bind keeping)
preserved = bind-cong Target.p Target.q keeping keeping Proof.equiv (λ a → ≈-refl (keeping a))

not-preserved : ¬ (Target.left ≈ Target.right)
not-preserved = Proof.gap
