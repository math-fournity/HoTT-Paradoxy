{-# OPTIONS --safe --cubical --guardedness #-}

-- Pinned support lemmas for the machine-overview L1 calibration proofs.
--
-- The lemmas are generic over ground terms of the pinned R041 delay model in
-- HoTT/formal/partiality-race-timeout/.  A generated candidate proof only
-- instantiates them with facts that reduce by computation (refl).  This module
-- is part of the trusted base of the calibration chain; it is not generated and
-- not writable by a candidate process.

module MVSupport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Empty.Base using (⊥; ⊥*; rec*)
open import PartialityRaceTimeout

-- Result equivalence for two equal-value ground delays.
≈-same-ret : (n m : ℕ) (a : Bool) → ret n a ≈ ret m a
≈-same-ret n m a b = ⇔-refl (a ≡ b)

≈-same-omega : ω {A = Bool} ≈ ω {A = Bool}
≈-same-omega = ≈-refl (ω {A = Bool})

-- Constructor discrimination for the declared Optional Bool observation.
noneB : Optional Bool
noneB = none

someB : Bool → Optional Bool
someB b = some b

isSome : Optional Bool → Bool
isSome none = false
isSome (some _) = true

some-neq-none : (b : Bool) → ¬ (someB b ≡ noneB)
some-neq-none b e = true≢false (cong isSome e)

none-neq-some : (b : Bool) → ¬ (noneB ≡ someB b)
none-neq-some b e = false≢true (cong isSome e)

some-neq-some : (a c : Bool) → ¬ (a ≡ c) → ¬ (someB a ≡ someB c)
some-neq-some a c neq e = neq (cong fromSome e)
