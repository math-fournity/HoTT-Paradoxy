{-# OPTIONS --safe --cubical --guardedness #-}
module ReportAll where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.Unit
open import HITScan
open import NoHitGroupoidUniverse
open import AscentStallAtSets
open import UIPEscape
open import UniverseHasNoLevel
open import KSUniverseTower
r1 : ⊤
r1 = reportClosure ¬universeIsGroupoid
r2 : ⊤
r2 = reportClosure universeLoopSpaceAtSetIsSet
r3 : ⊤
r3 = reportClosure noLevel2AscentAtSets
r4 : ⊤
r4 = reportClosure typeIsNotASet
r5 : ⊤
r5 = reportClosure localGlobal
r6 : ⊤
r6 = reportClosure KS-Theorem-5-9
r7 : ⊤
r7 = reportClosure workOrderForm
r8 : ⊤
r8 = reportClosure KS-Theorem-5-10-U≤
r9 : ⊤
r9 = reportClosure KS-Theorem-5-10-Loop
