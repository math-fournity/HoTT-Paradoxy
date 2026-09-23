{-# OPTIONS --safe --cubical --guardedness #-}

-- REFUSAL HALF (route c1) of the interval-I design probe.
-- Attempt: state an identity type between interval elements, which is what a
-- decidable equality / Bool-valued separates on I would have to quantify over.
-- PathP requires a family  A : I -> Type ℓ, but the interval itself is not in
-- a universe of that sort (I : IUniv), so the identity type on I is not even
-- FORMABLE at the level the DM3 oracle needed.

module IntervalIEqualityAttempt where

open import Cubical.Foundations.Prelude
open import Cubical.Core.Primitives using (I; i0; i1; PathP)

identityOnI : (r s : I) → Type₀
identityOnI r s = PathP (λ i → I) r s
