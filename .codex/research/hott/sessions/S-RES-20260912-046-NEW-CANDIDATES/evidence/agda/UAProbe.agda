{-# OPTIONS --safe --cubical --guardedness #-}

-- N4 probe: is ua's regularity definitional in Cubical Agda 2.8.0 / Cubical v0.9?
-- If probe-regular fails while probe-beta succeeds, then a consumer that relies
-- on definitional reduction of transport along ua idEquiv would be upgrading a
-- propositional path to a definitional equality.
module UAProbe where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool

-- Regularity probe: the identity equivalence's ua path should transport
-- definitionally if regularity held.
probe-regular : transport (ua (idEquiv Bool)) true ≡ true
probe-regular = refl

-- Propositional version: always available through uaβ.
probe-beta : transport (ua (idEquiv Bool)) true ≡ true
probe-beta = uaβ (idEquiv Bool) true

-- Nontrivial equivalence control: transport computes through the equivalence.
probe-not : transport (ua notEquiv) true ≡ false
probe-not = refl
