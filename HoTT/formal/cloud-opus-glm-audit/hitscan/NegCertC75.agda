{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control COPUS-R1-NEG-02 for HITScan: C-75 (universeHasNoLevel)
  uses Eilenberg–MacLane spaces, so "HIT-free" must be REJECTED, with the
  HITs (EM₁, S¹, Susp, truncation HubAndSpoke, ...) named.
-}
module NegCertC75 where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import UniverseHasNoLevel using (universeHasNoLevel)

wrong : Path (List Name) (hitsOf universeHasNoLevel) []
wrong = refl
