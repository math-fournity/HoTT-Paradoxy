{-# OPTIONS --safe --cubical --guardedness #-}
module RationalPointSet where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
import Cubical.Data.Int as Z
import Cubical.Data.Nat as N
open import Cubical.Data.NatPlusOne using (1+_)
open import Cubical.Data.Rationals.Base using (ℚ; [_/_]; eq/⁻¹; isSetℚ)
open import Cubical.Data.Rationals.Properties using (_+_; _·_)

zeroQ oneQ : ℚ
zeroQ = [ Z.pos 0 / 1+ 0 ]
oneQ = [ Z.pos 1 / 1+ 0 ]

zeroNotOne : (zeroQ ≡ oneQ) → ⊥
zeroNotOne p = N.znots (Z.injPos (eq/⁻¹ (Z.pos 0 , 1+ 0) (Z.pos 1 , 1+ 0) p))

-- A genuine algebraic point set. No real completion/topology is asserted.
QCircle : Type
QCircle = Σ[ x ∈ ℚ ] Σ[ y ∈ ℚ ] ((x · x) + (y · y) ≡ oneQ)

north east : QCircle
north = zeroQ , oneQ , refl
east = oneQ , zeroQ , refl

northNotEast : (north ≡ east) → ⊥
northNotEast p = zeroNotOne (cong fst p)

PuncturedQCircle : Type
PuncturedQCircle = Σ[ x ∈ QCircle ] ((x ≡ east) → ⊥)

nonemptyPointSetPuncture : PuncturedQCircle
nonemptyPointSetPuncture = north , northNotEast

isSetQCircle : isSet QCircle
isSetQCircle = isSetΣ isSetℚ (λ x → isSetΣ isSetℚ (λ y → isProp→isSet (isSetℚ _ _)))
