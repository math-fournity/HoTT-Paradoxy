{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Repaired negative control for GLM-R3-C01 (COPUS-GLM-FIX-NEG-01).
  GLM's WrongGroupoidWitness.agda was rejected by the SCOPE CHECKER
  (`true` not in scope: it imports only Prelude and `a`), so it never
  tested the arithmetic it claims to test.  This file imports the Bool
  constructors.  Expected: kernel rejection for the claimed reason,
  a (true , true) = (false , true) ≠ (true , true)  (false != true).
-}
module GroupoidNegFixed where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (true ; false)
open import NoHitGroupoidUniverse using (a)

wrong : a (true , true) ≡ (true , true)
wrong = refl
