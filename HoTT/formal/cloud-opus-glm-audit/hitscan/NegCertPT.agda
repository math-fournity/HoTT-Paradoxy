{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control COPUS-R1-NEG-03 for HITScan: a one-line use of the
  propositional truncation (the HIT that sits in the import closure of
  every file importing Cubical.Data.Sigma).  "HIT-free" must be REJECTED,
  with ∥_∥₁ named.  (This control is what exposed the scanner's first
  defect: `_≡_` is Agda's BUILTIN PATH and stays folded under normalisation.)
-}
module NegCertPT where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Reflection using (Name)
open import Cubical.Data.Bool using (Bool ; true)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁ ; ∣_∣₁)
open import HITScan

usesPT : ∥ Bool ∥₁
usesPT = ∣ true ∣₁

wrong : Path (List Name) (hitsOf usesPT) []
wrong = refl
