{-# OPTIONS --safe --cubical --guardedness #-}
{-
  HITScan certificate for C-71 (Opus, hset-universe): hSetNotSet : ¬ isSet (hSet ℓ-zero)
  — the Kraus–Sattler base case (U₀^{≤0} is not a set).
  claim COPUS-R1-C06: name-level closure of 149 names contains no HIT.
-}
module CertC71 where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Unit
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import HSetNotSet using (hSetNotSet)

c71-noHIT : Path (List Name) (hitsOf hSetNotSet) []
c71-noHIT = refl
c71-size : Path Nat (sizeOf hSetNotSet) 149
c71-size = refl

report-c71 : ⊤
report-c71 = reportClosure hSetNotSet
