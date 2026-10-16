{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for COPUS-KS-C06 (bookkeeping near miss).

  Tries to read the first component of KS-Theorem-5-10-U≤ 0 -- which says
  that the catalog of sets is a groupoid (h-level 3) -- as the one-level
  stronger statement "the catalog of sets is a set" (h-level 2).
  Expected: kernel rejection at type checking (isOfHLevel 3 is not isSet),
  i.e. the questioning of hSet ℓ-zero really needs the second step and does
  not stop at the first.
-}
module KSNegCatalogOfSetsIsSet where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import KSUniverseTower using (KS-Theorem-5-10-U≤)

wrong : isSet (hSet ℓ-zero)
wrong = fst (KS-Theorem-5-10-U≤ 0)
