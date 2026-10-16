{-# OPTIONS --safe --cubical --guardedness #-}

module NoCanonicalFinite where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (not)
import NoCanonicalPoint as NCP

-- Bridge module for the derived-development replay of
-- `HoTT/formal/agda-unimath/hott-z/NoCanonicalPoint.agda`
-- (agda-unimath's `no-section-type-2-Element-Type` content) inside the pinned
-- Cubical toolchain.
--
-- N38 -> N40 correction: the N38 version of this file stated
-- `(s : (b : Bool) → carrier (boolPresentation b)) → s false ≡ s true` as the
-- target; that statement is false (a plain section over a definitionally
-- constant family is an arbitrary `Bool → Bool`).  The correct statement, its
-- proof, and the explanation live in `NoCanonicalPoint.agda`
-- (C-142–C-147, proof id MP-NOCANONICAL-001).  Nothing unproved is asserted
-- here; this module only re-exports the machine-checked statements.

noCanonicalPoint :
  ((X : NCP.UnlabeledTwoElement) → NCP.unlabeledCarrier X) → ⊥
noCanonicalPoint = NCP.noUniformChoice

-- The obstruction in fixed-point form: any hypothetical uniform choice would
-- be a fixed point of the nontrivial automorphism `not`.
fixedPointObligation :
  (u : (X : NCP.UnlabeledTwoElement) → NCP.unlabeledCarrier X)
  → not (u NCP.identityPresentation) ≡ u NCP.identityPresentation
fixedPointObligation = NCP.uniformChoiceFixedPoint

labeledChoice :
  (X : NCP.LabeledTwoElement) → fst X
labeledChoice = NCP.labeledChoice
