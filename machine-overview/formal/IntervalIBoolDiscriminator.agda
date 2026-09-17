{-# OPTIONS --safe --cubical --guardedness #-}

-- REFUSAL HALF of the interval-I design probe (companion of IntervalIForms).
-- Attempted form (c): a Bool-valued observer on the interval, i.e. the shape
-- the point-set / DM3 separation oracle had:  separates : A -> A -> Bool.
-- On the real interval the analogous signature is  I -> I -> Bool  (or the
-- endpoint observer  I -> Bool).
--
-- Every route to such a function needs either
--   (c1) an eliminator for I into a non-interval universe (does not exist:
--        I : IUniv, and IUniv is not an inductive type with an eliminator),
--   or (c2) pattern matching on an interval variable into Bool.
--
-- Below the natural attempts are written out.  The kernel is EXPECTED to
-- refuse them.  The refusal is the probe's positive information: the
-- separation oracle layer that the DM3 branch used (a Bool-valued decidable
-- observer) is NOT transferable to the real interval I, which is exactly why
-- revision 019 left interval_i_confirmed = false and why separation on I
-- must live in the type-family / cofibration layer of IntervalIForms.
--
-- Falsifier of the negative claim: a kernel-ACCEPTED non-constant function of
-- type I -> Bool (or a kernel-ACCEPTED decidable equality on I).

module IntervalIBoolDiscriminator where

open import Cubical.Foundations.Prelude
open import Cubical.Core.Primitives using (I; i0; i1)
open import Cubical.Data.Bool.Base using (Bool; true; false)

-- ATTEMPT 1 (route c2): pattern match on the interval endpoints into Bool.
endpointObserver : I → Bool
endpointObserver i0 = true
endpointObserver i1 = false
endpointObserver r  = true
