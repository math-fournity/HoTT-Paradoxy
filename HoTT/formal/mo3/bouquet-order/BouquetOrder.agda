{-# OPTIONS --safe --cubical --guardedness #-}
module BouquetOrder where

-- MO3 C04: a fixed native Bouquet family with two reversible actions.
-- The task observes the fiber label, not merely the common base point.

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.Transport
open import Cubical.Data.Bool.Base
open import Cubical.Data.Unit
open import Cubical.Data.Empty as Empty
open import Cubical.HITs.Bouquet.Base

data Mark : Type where
  a b c : Mark

swapAB : Mark → Mark
swapAB a = b
swapAB b = a
swapAB c = c

swapBC : Mark → Mark
swapBC a = a
swapBC b = c
swapBC c = b

swapAB² : (x : Mark) → swapAB (swapAB x) ≡ x
swapAB² a = refl
swapAB² b = refl
swapAB² c = refl

swapBC² : (x : Mark) → swapBC (swapBC x) ≡ x
swapBC² a = refl
swapBC² b = refl
swapBC² c = refl

abIso bcIso : Iso Mark Mark
abIso = iso swapAB swapAB swapAB² swapAB²
bcIso = iso swapBC swapBC swapBC² swapBC²

Space : Type
Space = Bouquet Bool

State : Space → Type
State base = Mark
State (loop false i) = ua (isoToEquiv abIso) i
State (loop true i) = ua (isoToEquiv bcIso) i

α β : base {A = Bool} ≡ base
α = loop false
β = loop true

act : (base {A = Bool} ≡ base) → Mark → Mark
act p = subst State p

actα : (x : Mark) → act α x ≡ swapAB x
actα x = uaβ (isoToEquiv abIso) x

actβ : (x : Mark) → act β x ≡ swapBC x
actβ x = uaβ (isoToEquiv bcIso) x

-- C-331 proposed: same initial label, two different operation orders.
αβ-a : act (α ∙ β) a ≡ c
αβ-a = substComposite State α β a ∙ cong (act β) (actα a) ∙ actβ b

βα-a : act (β ∙ α) a ≡ b
βα-a = substComposite State β α a ∙ cong (act α) (actβ a) ∙ actα a

distinguishC : Mark → Type
distinguishC a = Unit
distinguishC b = ⊥
distinguishC c = Unit

c≢b : c ≡ b → ⊥
c≢b p = subst distinguishC p tt

-- C-332 proposed: both the observed labels and the composite paths differ.
outputsDifferent : act (α ∙ β) a ≡ act (β ∙ α) a → ⊥
outputsDifferent p = c≢b (sym αβ-a ∙ p ∙ βα-a)

pathsDifferent : (α ∙ β) ≡ (β ∙ α) → ⊥
pathsDifferent p = outputsDifferent (cong (λ q → act q a) p)

-- C-333 proposed: invert the actual path; reverse both operations in order.
restore : (p : base {A = Bool} ≡ base) (x : Mark) →
  act (sym p) (act p x) ≡ x
restore p x = subst⁻Subst State p x

restoreTwo : (p q : base {A = Bool} ≡ base) (x : Mark) →
  act (sym p) (act (sym q) (act q (act p x))) ≡ x
restoreTwo p q x = cong (act (sym p)) (restore q (act p x)) ∙ restore p x

restoreComposite : (p q : base {A = Bool} ≡ base) (x : Mark) →
  act (sym q ∙ sym p) (act (p ∙ q) x) ≡ x
restoreComposite p q x =
  cong (act (sym q ∙ sym p)) (substComposite State p q x) ∙
  substComposite State (sym q) (sym p) (act q (act p x)) ∙
  restoreTwo p q x

-- C-334 proposed: removing dependence on the path changes the task family.
constantControl : (p : base {A = Bool} ≡ base) (x : Mark) →
  subst (λ (_ : Space) → Mark) p x ≡ x
constantControl p x = transportRefl x
