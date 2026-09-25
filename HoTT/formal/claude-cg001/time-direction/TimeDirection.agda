{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A1 follow-up (Claude, session 6fd0312a, 2026-09-24): time order in HoTT's
  synthetic spaces, and the price of the directed exit, in a model.

  proof id : MP-CG001-TIME-DIRECTION-001
  claims   : CG001-C-23 .. CG001-C-24 (full statements in CLAIM.md)

  C-23  synthetic time has neither order nor direction: every path forward is
        equally a path back (an isomorphism of path types), going there and
        back is identified with staying put, and no irreflexive "earlier than"
        relates two moments joined by a path; when every arrow is a path, any
        reading that respects arrows into (N, <=) is frozen.
  C-24  directed model: if motion is given by arrows Arr and a reading must
        respect them into (N, <=), a round trip forces equal readings and no
        reading can go up and then come back down along one directed journey;
        control: on the time line N with arrows "<=" the clock advances, while
        the thermometer profile 0,1,0 is not a respecting reading.

  The model is order theory, not simplicial type theory; its bridge to the
  directed extension E06 is interpretation (see CLAIM.md).  Bridge labels
  (time, clock, thermometer, journey) prove no physical fact.
-}
module TimeDirection where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Path using (symIso)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; znots; snotz; +-suc)
open import Cubical.Data.Nat.Order using (_≤_; ≤-antisym)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- CG001-C-23  Synthetic time has neither order nor direction

module Synthetic {ℓ} {A : Type ℓ} where

  -- every way forward is equally a way back
  noArrowOfTime : {a b : A} → Iso (a ≡ b) (b ≡ a)
  noArrowOfTime = symIso

  -- going there and back is identified with staying put
  thereAndBackIsStaying : {a b : A} (p : a ≡ b) → p ∙ sym p ≡ refl
  thereAndBackIsStaying = rCancel

  -- no strict "earlier than" relates two moments joined by a path
  noEarlierAlongPath : ∀ {ℓ'} (R : A → A → Type ℓ') → ((x : A) → ¬ R x x)
    → {a b : A} → a ≡ b → ¬ R a b
  noEarlierAlongPath R irr {a} {b} p r = irr b (subst (λ z → R z b) p r)

  -- when every arrow is a path, a reading that respects arrows into (ℕ, ≤) is frozen
  pathsFreezeMonotone : (f : A → ℕ) → ((x y : A) → x ≡ y → f x ≤ f y)
    → (a b : A) → a ≡ b → f a ≡ f b
  pathsFreezeMonotone f mono a b p = ≤-antisym (mono a b p) (mono b a (sym p))

------------------------------------------------------------------------
-- CG001-C-24  The price of the directed exit, in a model

one≰zero : ¬ (1 ≤ 0)
one≰zero (k , p) = snotz (sym (+-suc k 0) ∙ p)

module Directed {ℓ ℓ'} {A : Type ℓ} (Arr : A → A → Type ℓ') where

  -- a reading that respects the direction of every arrow
  Monotone : (A → ℕ) → Type (ℓ-max ℓ ℓ')
  Monotone f = (x y : A) → Arr x y → f x ≤ f y

  -- a round trip forces equal readings
  roundTripFreezes : (f : A → ℕ) → Monotone f
    → (a b : A) → Arr a b → Arr b a → f a ≡ f b
  roundTripFreezes f mono a b ab ba = ≤-antisym (mono a b ab) (mono b a ba)

  -- no reading goes up and then comes back down along one directed journey
  noUpThenDown : (f : A → ℕ) → Monotone f → (a b c : A) → Arr a b → Arr b c
    → f a ≡ 0 → f b ≡ 1 → ¬ (f c ≡ 0)
  noUpThenDown f mono a b c ab bc fa0 fb1 fc0 =
    one≰zero (subst2 _≤_ fb1 fc0 (mono b c bc))

-- control: on the time line ℕ with arrows "not later than", the clock advances
clockAdvances : Σ[ f ∈ (ℕ → ℕ) ] (Directed.Monotone (λ m n → m ≤ n) f) × (¬ (f 0 ≡ f 1))
clockAdvances = (λ n → n) , (λ x y le → le) , znots

-- the thermometer profile 0, 1, 0 over times 0 ≤ 1 ≤ 2 respects no direction
thermometerNotMonotone :
  ¬ (Σ[ f ∈ (ℕ → ℕ) ] (Directed.Monotone (λ m n → m ≤ n) f)
      × (f 0 ≡ 0) × (f 1 ≡ 1) × (f 2 ≡ 0))
thermometerNotMonotone (f , mono , f0 , f1 , f2) =
  Directed.noUpThenDown (λ m n → m ≤ n) f mono 0 1 2 (1 , refl) (1 , refl) f0 f1 f2
