{-# OPTIONS --safe --cubical --guardedness #-}
{-
  HITScan certificates for GLM's HIT-free claims (audit item R1).
  claim COPUS-R1-C01: GLM-R3-C01 (¬universeIsGroupoid) — name-level closure
                      of 251 names contains no HIT.
  claim COPUS-R1-C02: GLM-R2-C01 (universeLoopSpaceAtSetIsSet) — 189 names, no HIT.
  claim COPUS-R1-C03: GLM-R2-C02 (noLevel2AscentAtSets) — 190 names, no HIT.
  With -v hitscan:10 the full closures are printed into stdout.
  Reading: see HITScan.agda header (what the closure is, and its boundary).
-}
module CertGLM where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Unit
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import NoHitGroupoidUniverse using (¬universeIsGroupoid)
open import AscentStallAtSets using (universeLoopSpaceAtSetIsSet ; noLevel2AscentAtSets)

glm-r3-c01-noHIT : Path (List Name) (hitsOf ¬universeIsGroupoid) []
glm-r3-c01-noHIT = refl
glm-r3-c01-size : Path Nat (sizeOf ¬universeIsGroupoid) 251
glm-r3-c01-size = refl

glm-r2-c01-noHIT : Path (List Name) (hitsOf universeLoopSpaceAtSetIsSet) []
glm-r2-c01-noHIT = refl
glm-r2-c01-size : Path Nat (sizeOf universeLoopSpaceAtSetIsSet) 189
glm-r2-c01-size = refl

glm-r2-c02-noHIT : Path (List Name) (hitsOf noLevel2AscentAtSets) []
glm-r2-c02-noHIT = refl
glm-r2-c02-size : Path Nat (sizeOf noLevel2AscentAtSets) 190
glm-r2-c02-size = refl

report-r3-c01 : ⊤
report-r3-c01 = reportClosure ¬universeIsGroupoid
report-r2-c01 : ⊤
report-r2-c01 = reportClosure universeLoopSpaceAtSetIsSet
report-r2-c02 : ⊤
report-r2-c02 = reportClosure noLevel2AscentAtSets
