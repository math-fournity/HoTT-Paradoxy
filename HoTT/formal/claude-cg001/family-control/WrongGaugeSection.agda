{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-25 (MP-CG001-FAMILY-CONTROL-NEG-001).
  Expected result: KERNEL_REJECTED.

  Claim tested: the section of the glued family is forced by the gluing.
  Declaring the raw value 5 at the second place while the first step shifts
  0 by +1 must fail at the boundary of the first path.
-}
module WrongGaugeSection where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (ℤ; pos; sucPathℤ)

data Step : Type where
  a b : Step
  e : a ≡ b

Gauge : Step → Type
Gauge a = ℤ
Gauge b = ℤ
Gauge (e i) = sucPathℤ i

wrongSection : (x : Step) → Gauge x
wrongSection a = pos 0
wrongSection b = pos 5
wrongSection (e i) = toPathP {A = λ j → sucPathℤ j} {x = pos 0} {y = pos 5} refl i
