{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control COPUS-R1-NEG-01 for HITScan: GLM-R1-C01 is about a
  syntax declared as a HIT (Tm has path constructors betaT/betaF), so the
  claim "its closure is HIT-free" must be REJECTED, with Tm named.
-}
module NegCertIota where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import RealisticIotaSyntaxSet using (realisticIotaSyntaxIsASet)

wrong : Path (List Name) (hitsOf realisticIotaSyntaxIsASet) []
wrong = refl
