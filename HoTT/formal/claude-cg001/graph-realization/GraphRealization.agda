{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A1 follow-up (Claude, session 6fd0312a, 2026-09-24): the price of realization.

  proof id : MP-CG001-GRAPH-REALIZATION-001
  claims   : CG001-C-19 .. CG001-C-20 (full statements in CLAIM.md)

  A graph (states V, adjacency E) is the discrete skeleton of motion: distinct
  states, and a step relation between them.  HoTT's way of building a space
  from points and paths is its realization: every step becomes an
  identification.

  C-19  price theorem: set-valued readings on the realization are exactly the
        readings on states that do not change along any step; after
        realization adjacent states are separated by no irreflexive relation
        and by no set-valued "distance" that vanishes on the diagonal.
  C-20  instance: the four-place ring as a graph keeps its distinct states and
        its height profile 0,1,2,1 (which changes along a step); no reading of
        the realized ring restricts to that profile, and every edge-invariant
        reading of the ring takes one value at all four places.

  Bridge labels (state, step, height, realization as "the synthetic space")
  are interpretation; this file proves no physical fact and not HoTT
  inconsistency.
-}
module GraphRealization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; znots; snotz)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- CG001-C-19  The price of realization

module _ {ℓ ℓ'} (V : Type ℓ) (E : V → V → Type ℓ') where

  -- every step becomes an identification
  data Realize : Type (ℓ-max ℓ ℓ') where
    vtx  : V → Realize
    edge : (x y : V) → E x y → vtx x ≡ vtx y

  EdgeInvariant : ∀ {ℓ''} (P : Type ℓ'') → Type (ℓ-max (ℓ-max ℓ ℓ') ℓ'')
  EdgeInvariant P = Σ[ f ∈ (V → P) ] ((x y : V) → E x y → f x ≡ f y)

  module Readings {ℓ''} {P : Type ℓ''} (setP : isSet P) where

    restrictReading : (Realize → P) → EdgeInvariant P
    restrictReading g = (g ∘ vtx) , (λ x y e → cong g (edge x y e))

    extendReading : EdgeInvariant P → Realize → P
    extendReading (f , inv) (vtx v) = f v
    extendReading (f , inv) (edge x y e i) = inv x y e i

    back : (g : Realize → P) (z : Realize) → extendReading (restrictReading g) z ≡ g z
    back g (vtx v) = refl
    back g (edge x y e i) =
      isProp→PathP (λ j → setP (extendReading (restrictReading g) (edge x y e j)) (g (edge x y e j))) refl refl i

    -- readings on the realization = readings on states that never change along a step
    price : Iso (Realize → P) (EdgeInvariant P)
    price = iso restrictReading extendReading (λ _ → refl) (λ g → funExt (back g))

  -- after realization, no irreflexive relation separates adjacent states
  orderLostAfterRealization : ∀ {ℓr} (R : Realize → Realize → Type ℓr)
    → ((z : Realize) → ¬ R z z) → (x y : V) → E x y → ¬ R (vtx x) (vtx y)
  orderLostAfterRealization R irr x y e r =
    irr (vtx y) (subst (λ z → R z (vtx y)) (edge x y e) r)

  -- after realization, a set-valued distance vanishing on the diagonal vanishes on every step
  distanceLostAfterRealization : ∀ {ℓ''} {P : Type ℓ''} (d : Realize → Realize → P) (o : P)
    → ((z : Realize) → d z z ≡ o) → (x y : V) → E x y → d (vtx x) (vtx y) ≡ o
  distanceLostAfterRealization d o diag x y e =
    cong (λ z → d z (vtx y)) (edge x y e) ∙ diag (vtx y)

------------------------------------------------------------------------
-- CG001-C-20  Instance: the four-place ring

data Place : Type where
  p0 p1 p2 p3 : Place

next : Place → Place
next p0 = p1
next p1 = p2
next p2 = p3
next p3 = p0

Step : Place → Place → Type
Step x y = next x ≡ y

height : Place → ℕ
height p0 = 0
height p1 = 1
height p2 = 2
height p3 = 1

-- before realization: distinct states, and a reading that changes along a step
statesDistinct : ¬ (p0 ≡ p1)
statesDistinct q = znots (cong height q)

heightChangesAlongStep : Step p0 p1 × (¬ (height p0 ≡ height p1))
heightChangesAlongStep = refl , znots

heightNotEdgeInvariant : ¬ ((x y : Place) → Step x y → height x ≡ height y)
heightNotEdgeInvariant inv = znots (inv p0 p1 refl)

Ring : Type
Ring = Realize Place Step

-- after realization: no reading of the realized ring restricts to the height profile
noHeightOnRealizedRing : ¬ (Σ[ g ∈ (Ring → ℕ) ] ((v : Place) → g (vtx v) ≡ height v))
noHeightOnRealizedRing (g , agrees) =
  znots (sym (agrees p0) ∙ cong g (edge p0 p1 refl) ∙ agrees p1)

-- every edge-invariant reading of the ring takes one value at all four places
edgeInvariantIsConstant : ∀ {ℓ''} {P : Type ℓ''} → ((f , inv) : EdgeInvariant Place Step P)
  → (f p0 ≡ f p1) × (f p1 ≡ f p2) × (f p2 ≡ f p3)
edgeInvariantIsConstant (f , inv) = inv p0 p1 refl , inv p1 p2 refl , inv p2 p3 refl
