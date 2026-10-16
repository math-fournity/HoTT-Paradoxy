{-# OPTIONS --safe --cubical --guardedness #-}
{-
  HITScan certificates for the Opus pieces the GLM line leans on.
  claim COPUS-R1-C04: C-63 (typeIsNotASet: Type₀ is not a set) — 101 names, no HIT.
  claim COPUS-R6-C01: the local-global bridge `localGlobal` of the C-75 package —
                      201 names, no HIT (although its FILE imports
                      Eilenberg–MacLane spaces, which C-75's own main theorem uses).
-}
module CertOpus where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Unit
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import UIPEscape using (typeIsNotASet)
open import UniverseHasNoLevel using (localGlobal)

c63-noHIT : Path (List Name) (hitsOf typeIsNotASet) []
c63-noHIT = refl
c63-size : Path Nat (sizeOf typeIsNotASet) 101
c63-size = refl

localGlobal-noHIT : Path (List Name) (hitsOf localGlobal) []
localGlobal-noHIT = refl
localGlobal-size : Path Nat (sizeOf localGlobal) 201
localGlobal-size = refl

report-c63 : ⊤
report-c63 = reportClosure typeIsNotASet
report-localGlobal : ⊤
report-localGlobal = reportClosure localGlobal
