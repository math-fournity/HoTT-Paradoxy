{-# OPTIONS --safe --cubical --guardedness #-}
-- Scratch sanity check (NOT delivered evidence): KS 5.10 at n = 0 unfolds
-- definitionally to "hSet ℓ-zero is a groupoid and not a set".
module CatalogOfSetsTwoSteps where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Relation.Nullary using (¬_)
open import KSUniverseTower using (KS-Theorem-5-10-U≤)

catalogOfSetsTwoSteps : isOfHLevel 3 (hSet ℓ-zero) × (¬ isSet (hSet ℓ-zero))
catalogOfSetsTwoSteps = KS-Theorem-5-10-U≤ 0
