{-# OPTIONS --safe --cubical --guardedness #-}
{-
  How deep the coherence goes is how deep sameness goes: machine-checked
  instances (Claude, session 7f138325, 2026-09-26; goal CG-003, gate G3).

  proof id : MP-CG001-WILD-SST-LEVELS-001
  claim    : CG001-C-70 (full statement in CLAIM-C70.md)

  Uses the irrelevant-order definition WildSSTᵢ, its hexagon Coh₂ᵢ and the
  generated second coherence Coh₃ of WildSSTP4.agda (CG001-C-68).

  (a) setsCohereᵢ : every level a set  ⇒ Coh₂ᵢ holds (nothing to add).
  (b) coh₂IsProp  : every level a groupoid ⇒ Coh₂ᵢ is a proposition (the
      hexagon data, if it exists, is unique);
      groupoidsCohere₃ : every level a groupoid ⇒ Coh₃ holds for every
      choice of hexagon data (the regress stops after the hexagon).
  (c) The flat shape over the circle (points of S¹ in dimension 0, Unit
      above): any two hexagon data are equal, and every one satisfies Coh₃.
      Over the 2-sphere the same shape has two different hexagon data
      (CG001-C-66) and one of them violates Coh₃ (CG001-C-68).

  Read together with CG001-C-64 (sets: Coh₂ automatic; spin on S¹: Coh₂ can
  fail) and C-66/C-68 (S²: Coh₂ data not unique; Coh₃ can fail): each extra
  level of sameness adds exactly one level of coherence to be supplied.
  The general statement for every truncation level t (supply up to the
  (t+1)-st coherence, the rest is automatic) is a meta-level argument about
  h-levels; it is not stated here, because the n-th coherence for variable n
  cannot itself be written uniformly -- that is the open problem.
-}
module WildSSTP4Levels where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Unit.Properties using (isOfHLevelUnit)
open import Cubical.HITs.S1.Base using (S¹ ; base)
open import Cubical.HITs.S1.Properties using (isGroupoidS¹)

open import WildSST using (Fin ; _≤F_)
open import WildSSTP4

------------------------------------------------------------------------
-- (a) Sets.

setsCohereᵢ : (S : WildSSTᵢ) → ((n : ℕ) → isSet (WildSSTᵢ.X S n)) → Coh₂ᵢ S
setsCohereᵢ S st m i j k p q x = st m _ _ _ _

------------------------------------------------------------------------
-- (b) Groupoids.

coh₂IsProp : (S : WildSSTᵢ) → ((n : ℕ) → isGroupoid (WildSSTᵢ.X S n)) → isProp (Coh₂ᵢ S)
coh₂IsProp S g h h' t m a b c p q x =
  g m _ _ _ _ (h m a b c p q x) (h' m a b c p q x) t

groupoidsCohere₃ : (S : WildSSTᵢ₂)
  → ((n : ℕ) → isGroupoid (WildSSTᵢ.X (WildSSTᵢ₂.underlying S) n)) → Coh₃ S
groupoidsCohere₃ S g m i j k l p q s x =
  g m _ _ _ _ (P4.hem₁ S m i j k l p q s x) (P4.hem₂ S m i j k l p q s x)

------------------------------------------------------------------------
-- (c) The flat shape over the circle.

flatS¹ : WildSSTᵢ
WildSSTᵢ.X flatS¹ zero = S¹
WildSSTᵢ.X flatS¹ (suc n) = Unit
WildSSTᵢ.d flatS¹ zero _ _ = base
WildSSTᵢ.d flatS¹ (suc n) _ _ = tt
WildSSTᵢ.sid flatS¹ zero _ _ _ _ = refl
WildSSTᵢ.sid flatS¹ (suc n) _ _ _ _ = refl

flatS¹-groupoid : (n : ℕ) → isGroupoid (WildSSTᵢ.X flatS¹ n)
flatS¹-groupoid zero = isGroupoidS¹
flatS¹-groupoid (suc n) = isOfHLevelUnit 3

flatS¹-hexagon : Coh₂ᵢ flatS¹
flatS¹-hexagon zero i j k _ _ x = refl
flatS¹-hexagon (suc m) i j k _ _ x = refl

flatS¹-unique : (C C' : Coh₂ᵢ flatS¹) → C ≡ C'
flatS¹-unique = coh₂IsProp flatS¹ flatS¹-groupoid

flatS¹-coh₃ : (C : Coh₂ᵢ flatS¹) → Coh₃ (record { underlying = flatS¹ ; hexagon = C })
flatS¹-coh₃ C = groupoidsCohere₃ (record { underlying = flatS¹ ; hexagon = C }) flatS¹-groupoid
