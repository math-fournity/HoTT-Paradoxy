{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A1 follow-up (Claude, session 6fd0312a, 2026-09-24):
  where order, distance and density can live in HoTT, and where motion can.

  proof id : MP-CG001-MOTION-ORDER-SPLIT-001
  claims   : CG001-C-15 .. CG001-C-18 (full statements in CLAIM.md)

  C-15  order excludes motion: two points related by any irreflexive relation
        are not (merely) connected; on a connected type every
        proposition-valued relation holds everywhere or nowhere, every
        irreflexive relation is empty, every set-valued "distance" vanishes,
        and an injective set-valued coordinate forces at most one point.
  C-16  instances: the road (interval HIT) and the circle S1 carry no strict
        order and no length; S1 carries no injective rational coordinate.
  C-17  control: the rational line carries a strict order with 0 < 1/2 < 1,
        but no motion from 0 to 1.
  C-18  one global state: clock + counter over the road form a single state
        (start , 0) = (finish , 1), every observable of the global state is
        frozen, while the clock-conditioned raw readings differ; with the clock
        as discrete data the two moments are two states.

  Bridge labels (road, clock, earlier-than, distance, coordinate) are
  interpretation; this file proves no physical fact and not HoTT inconsistency.
-}
module MotionOrderSplit where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Data.Empty using (⊥; isProp⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; znots)
open import Cubical.Data.NatPlusOne using (1+_)
open import Cubical.Data.Int using (ℤ; pos; negsuc; sucℤ; injPos; sucPathℤ)
open import Cubical.Data.Rationals.Base using (ℚ; isSetℚ; [_/_]; eq/⁻¹)
open import Cubical.Data.Rationals.Order as Q using ()
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.HITs.PropositionalTruncation as PT using (∥_∥₁; ∣_∣₁; squash₁)
open import Cubical.HITs.S1 using (S¹; base; loop; winding)
open import Cubical.HITs.S1.Properties using (isConnectedS¹)
open import Cubical.HITs.Interval using (Interval; seg; isContrInterval)
  renaming (zero to start; one to finish)

------------------------------------------------------------------------
-- CG001-C-15  Order excludes motion

-- two points related by an irreflexive relation are never merely connected
orderExcludesMotion : ∀ {ℓ ℓ'} {A : Type ℓ} (R : A → A → Type ℓ')
  → ((x : A) → ¬ R x x) → (x y : A) → R x y → ¬ ∥ x ≡ y ∥₁
orderExcludesMotion R irr x y r =
  PT.rec isProp⊥ (λ p → irr y (subst (λ z → R z y) p r))

Connected : ∀ {ℓ} → Type ℓ → Type ℓ
Connected A = (x y : A) → ∥ x ≡ y ∥₁

module OnConnected {ℓ} {A : Type ℓ} (conn : Connected A) where

  -- every proposition-valued relation holds everywhere or nowhere
  relationSpreads : ∀ {ℓ'} (R : A → A → Type ℓ') → ((x y : A) → isProp (R x y))
    → (x y x' y' : A) → R x y → R x' y'
  relationSpreads R propR x y x' y' r =
    PT.rec2 (propR x' y') (λ p q → subst2 R p q r) (conn x x') (conn y y')

  -- every irreflexive relation is empty: no strict order, no "earlier than"
  noStrictOrder : ∀ {ℓ'} (R : A → A → Type ℓ') → ((x : A) → ¬ R x x)
    → (x y : A) → ¬ R x y
  noStrictOrder R irr x y r = orderExcludesMotion R irr x y r (conn x y)

  -- every set-valued two-point function equal to o on the diagonal is o everywhere
  noDistance : ∀ {ℓ'} {P : Type ℓ'} → isSet P → (d : A → A → P) (o : P)
    → ((x : A) → d x x ≡ o) → (x y : A) → d x y ≡ o
  noDistance setP d o diag x y =
    PT.rec (setP _ _) (λ p → cong (λ z → d z y) p ∙ diag y) (conn x y)

  -- an injective set-valued coordinate forces at most one point
  coordinatedIsPoint : ∀ {ℓ'} {P : Type ℓ'} → isSet P → (f : A → P)
    → ((x y : A) → f x ≡ f y → x ≡ y) → isProp A
  coordinatedIsPoint setP f inj x y =
    inj x y (PT.rec (setP _ _) (cong f) (conn x y))

------------------------------------------------------------------------
-- CG001-C-16  Instances: the road and the circle

q0 q½ q1 : ℚ
q0 = [ pos 0 / 1+ 0 ]
q½ = [ pos 1 / 1+ 1 ]
q1 = [ pos 1 / 1+ 0 ]

connectedRoad : Connected Interval
connectedRoad x y = ∣ isContr→isProp isContrInterval x y ∣₁

connectedCircle : Connected S¹
connectedCircle x y =
  PT.rec2 squash₁ (λ p q → ∣ sym p ∙ q ∣₁) (isConnectedS¹ x) (isConnectedS¹ y)

-- start is not "earlier than" finish, for any strict relation whatever
noEarlierOnRoad : ∀ {ℓ'} (R : Interval → Interval → Type ℓ')
  → ((x : Interval) → ¬ R x x) → ¬ R start finish
noEarlierOnRoad R irr = OnConnected.noStrictOrder connectedRoad R irr start finish

-- any rational-valued "length" that vanishes on the diagonal gives the road length 0
roadHasNoLength : (d : Interval → Interval → ℚ)
  → ((x : Interval) → d x x ≡ q0) → d start finish ≡ q0
roadHasNoLength d diag = OnConnected.noDistance connectedRoad isSetℚ d q0 diag start finish

noEarlierOnCircle : ∀ {ℓ'} (R : S¹ → S¹ → Type ℓ')
  → ((x : S¹) → ¬ R x x) → (x y : S¹) → ¬ R x y
noEarlierOnCircle = OnConnected.noStrictOrder connectedCircle

circleNotAPoint : ¬ isProp S¹
circleNotAPoint propS = znots (injPos (sym (cong winding loopTrivial)))
  where
  loopTrivial : loop ≡ refl
  loopTrivial = isProp→isSet propS base base loop refl

noCoordinateOnCircle : ¬ (Σ[ f ∈ (S¹ → ℚ) ] ((x y : S¹) → f x ≡ f y → x ≡ y))
noCoordinateOnCircle (f , inj) =
  circleNotAPoint (OnConnected.coordinatedIsPoint connectedCircle isSetℚ f inj)

------------------------------------------------------------------------
-- CG001-C-17  Control: the number line has order (and a point between) but no motion

orderOnNumberLine : (q0 Q.< q½) × (q½ Q.< q1)
orderOnNumberLine = (0 , refl) , (0 , refl)

irreflexiveOnNumberLine : (x : ℚ) → ¬ (x Q.< x)
irreflexiveOnNumberLine = Q.isIrrefl<

noMotionOnNumberLine : ¬ (q0 ≡ q1)
noMotionOnNumberLine p = znots (injPos (eq/⁻¹ _ _ p))

-- the same fact read through C-15: ordered points are not connected
orderedHenceUnconnected : ¬ ∥ q0 ≡ q1 ∥₁
orderedHenceUnconnected =
  orderExcludesMotion Q._<_ irreflexiveOnNumberLine q0 q1 (0 , refl)

------------------------------------------------------------------------
-- CG001-C-18  One global state: clock and counter over the road

Counter : Interval → Type
Counter start = ℤ
Counter finish = ℤ
Counter (seg i) = sucPathℤ i

oneGlobalState : Path (Σ Interval Counter) (start , pos 0) (finish , pos 1)
oneGlobalState = ΣPathP (seg , toPathP {A = λ j → sucPathℤ j} {x = pos 0} {y = pos 1} refl)

globalObservablesFrozen : ∀ {ℓ} {P : Type ℓ} (g : Σ Interval Counter → P)
  → g (start , pos 0) ≡ g (finish , pos 1)
globalObservablesFrozen g = cong g oneGlobalState

conditionedReadingsDiffer : ¬ (pos 0 ≡ pos 1)
conditionedReadingsDiffer p = znots (injPos p)

-- contrast: the clock kept as discrete data, the two moments are two states
discreteMomentsDistinct : ¬ (Path (ℕ × ℤ) (0 , pos 0) (1 , pos 1))
discreteMomentsDistinct p = znots (cong fst p)
