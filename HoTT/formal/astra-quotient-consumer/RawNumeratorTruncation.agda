{-# OPTIONS --safe --cubical --guardedness #-}
module RawNumeratorTruncation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ)
import Cubical.Data.Int.Properties as Z
import Cubical.HITs.PropositionalTruncation as PT
open PT using (∥_∥₁)
open import QuotientConsumer using (Rep; oneQ; rawNumerator)

-- Controlled incorrect constancy proof on the actual representative fiber.
bad : ∥ Rep oneQ ∥₁ → ℤ
bad = PT.rec→Set Z.isSetℤ rawNumerator (λ r s → refl)
