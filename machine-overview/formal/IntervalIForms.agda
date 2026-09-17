{-# OPTIONS --safe --cubical --guardedness #-}

-- DESIGN PROBE for the interval-I branch of gap A (revision 019 left the
-- interval-I branch OPEN; revision 020 shard 008 set this probe as the next
-- unit).  Question: which forms of separation are WRITABLE on the real
-- cubical interval I?
--
-- Answer established below by ACCEPTED definitions: the writable forms are
--   (a) type families over I, with PathP as the dependent path type;
--   (b) cofibration conditions: IsOne / Partial / constraint pattern matching.
--
-- The Bool-valued observer form (separates : I -> I -> Bool) is NOT writable;
-- that refusal is recorded by the companion module IntervalIBoolDiscriminator
-- (kernel REJECTED receipt).
--
-- registers_new_claim: false (F-011).  This is a language-fragment probe, not
-- a mathematical theorem; its scope is the eliminators Cubical Agda 2.8.0 +
-- cubical v0.9 actually provides.  Falsifier: a kernel-ACCEPTED non-constant
-- function I -> Bool (see the companion module).

module IntervalIForms where

open import Cubical.Foundations.Prelude
open import Cubical.Core.Primitives
  using (I; i0; i1; _∧_; _∨_; ~_; IsOne; Partial; PartialP; 1=1; PathP; SSet)
open import Cubical.Data.Bool.Base using (Bool; true; false)

private
  variable
    ℓ : Level

------------------------------------------------------------------
-- FORM (b): cofibration conditions are writable on I
------------------------------------------------------------------

-- (b1) a TOTAL IsOne fact is writable for the constant endpoint i1.
oneIsOne : IsOne i1
oneIsOne = 1=1

-- (b2) a PARTIAL element over the cofibration (r ∨ ~ r) is writable WITHOUT
--      any decidable equality on I: the endpoint cases are supplied by
--      constraint pattern matching, and overlapping cases must agree.
--      (This is the separation-bearing form on I: it distinguishes the two
--      endpoint regimes without ever deciding r itself.)
endpointCases : (r : I) → Partial (r ∨ ~ r) Bool
endpointCases r = λ { (r = i0) → false
                    ; (r = i1) → true }

-- (b3) the same with a type-level carrier: an interval-indexed family of
--      types given piecewise on the two endpoint regimes.
endpointFamily : (r : I) → Partial (r ∨ ~ r) Type₁
endpointFamily r = λ { (r = i0) → Type₀
                     ; (r = i1) → Type₀ → Type₀ }

-- (b4) conjunction of cofibrations is writable: the meet (r ∧ s) equals i1
--      only under BOTH endpoint constraints, which is exactly what the
--      constraint pattern must state.
meetCases : (r s : I) → Partial (r ∧ s) Type₁
meetCases r s = λ { (r = i1) (s = i1) → Type₀ }

------------------------------------------------------------------
-- FORM (a): type families over I and PathP over them are writable
------------------------------------------------------------------

-- A family that genuinely depends on the interval (its carrier is the
-- cofibration-indexed partial type from b3, which mentions r).
intervalFamily : I → SSet₂
intervalFamily r = Partial (r ∨ ~ r) Type₁

-- PathP over a constant family is the ordinary path type, and its elements
-- are writable by interval abstraction.
pathOverConstant : (A : Type ℓ) (x : A) → PathP (λ _ → A) x x
pathOverConstant A x i = x

-- PathP over the genuinely interval-dependent family is a well-formed type
-- by PathP's formation rule; its inhabitance is not needed for the probe
-- claim, which concerns what is WRITABLE, not what is inhabited.  No term is
-- attempted here.
