{-# OPTIONS --safe --cubical --guardedness #-}
{-
  CG-001 follow-up: the second and third HoTT expressions of A1, and their collision.

  proof id : MP-CG001-A1-EXPRESSIONS-001
  claims   : CG001-C-10 .. CG001-C-14 (full statements in CLAIM.md)

  First expression (package motion-measurement, C-01..C-07): motion read as an
  identity path leaves every set-valued reading unchanged.

  Second expression, from other parts of HoTT:
    II-a truncations  : a step is invisible to every discrete reading iff the
                        step merely identifies its ends                (C-10)
    II-b univalence   : a reading space carried around the loop is exactly a
                        scale with one relabeling fixed in advance     (C-11)
    II-c loop space   : the lap count is not a function of position, but
                        exactly the manner of being the same            (C-12)

  Third expression, the scales themselves (helix as a bundle of origin-less
  integer scales):
    III               : no absolute origin can be chosen on all scales;
                        the shift along a trip is its winding number    (C-13)

  Collision of the expressions:                                         (C-14)
    a runner carrying a lap counter has, up to identity, one state; no
    integer-valued reading of that state varies; two readings that agree at one
    point agree along every path; the reading at the destination is computed
    from the start and the path.
-}
module A1Expressions where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (univalenceIso)
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool; true; false; not; notnot; true≢false)
open import Cubical.Data.Nat using (ℕ; zero; suc; znots; isSetℕ)
open import Cubical.Data.Int using (ℤ; pos; negsuc; sucℤ; isSetℤ)
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.HITs.S1
  using (S¹; base; loop; helix; ΩS¹; ΩS¹Isoℤ; encode; decode; decodeEncode; winding; windingℤLoop)
open import Cubical.HITs.S1.Properties using (IsoFunSpaceS¹)
open import Cubical.HITs.PropositionalTruncation as PT using (∥_∥₁; ∣_∣₁)
open import Cubical.HITs.SetTruncation as ST using (∥_∥₂; ∣_∣₂; squash₂; PathIdTrunc₀Iso)

------------------------------------------------------------------------
-- C-10 (II-a)  The attribution theorem

module Attribution {ℓ ℓ' : Level} {Pos : Type ℓ} (Step : Pos → Pos → Type ℓ') where

  -- no discrete (set-valued) reading tells the two ends of any step apart
  Invisible : Type (ℓ-max (ℓ-suc ℓ) ℓ')
  Invisible = (P : Type ℓ) → isSet P → (f : Pos → P) → (x y : Pos) → Step x y → f x ≡ f y

  -- every step merely identifies its two ends
  Identified : Type (ℓ-max ℓ ℓ')
  Identified = (x y : Pos) → Step x y → ∥ x ≡ y ∥₁

  identified→invisible : Identified → Invisible
  identified→invisible idf P setP f x y s = PT.rec (setP _ _) (cong f) (idf x y s)

  invisible→identified : Invisible → Identified
  invisible→identified inv x y s = Iso.fun PathIdTrunc₀Iso (inv ∥ Pos ∥₂ squash₂ ∣_∣₂ x y s)

  visibleStep→notIdentified : (P : Type ℓ) → isSet P → (f : Pos → P) → (x y : Pos)
    → Step x y → ¬ (f x ≡ f y) → ¬ Identified
  visibleStep→notIdentified P setP f x y s differ idf =
    differ (identified→invisible idf P setP f x y s)

-- motion read as identity: identified, hence invisible
module MotionAsIdentity where
  open Attribution {Pos = S¹} (λ x y → x ≡ y)

  pathsAreIdentified : Identified
  pathsAreIdentified x y p = ∣ p ∣₁

  motionIsInvisible : Invisible
  motionIsInvisible = identified→invisible pathsAreIdentified

-- motion as discrete steps between four places: visible, hence not identified
data Place : Type where
  p0 p1 p2 p3 : Place

next : Place → Place
next p0 = p1
next p1 = p2
next p2 = p3
next p3 = p0

height : Place → ℕ
height p0 = 0
height p1 = 1
height p2 = 2
height p3 = 1

module MotionAsSteps where
  open Attribution {Pos = Place} (λ x y → next x ≡ y)

  stepsAreNotIdentified : ¬ Identified
  stepsAreNotIdentified = visibleStep→notIdentified ℕ isSetℕ height p0 p1 refl znots

------------------------------------------------------------------------
-- C-11 (II-b)  Change only as a relabeling fixed in advance

readingSpacesOverLoop : ∀ {ℓ} → Iso (S¹ → Type ℓ) (Σ[ A ∈ Type ℓ ] (A ≃ A))
readingSpacesOverLoop = compIso IsoFunSpaceS¹ (Σ-cong-iso-snd (λ A → univalenceIso))

lapCounterIsRelabeling : (z : ℤ) → equivFun (snd (Iso.fun readingSpacesOverLoop helix)) z ≡ sucℤ z
lapCounterIsRelabeling z = transportRefl (sucℤ z)

------------------------------------------------------------------------
-- C-12 (II-c)  Where the laps went

circleReadingConstant : ∀ {ℓ} {P : Type ℓ} → isSet P → (h : S¹ → P) (x : S¹) → h x ≡ h base
circleReadingConstant setP h base = refl
circleReadingConstant setP h (loop i) = isProp→PathP (λ j → setP (h (loop j)) (h base)) refl refl i

noLapCountFromPosition : (h : S¹ → ℤ) (x : S¹) → h x ≡ h base
noLapCountFromPosition = circleReadingConstant isSetℤ

lapsAreTheMannerOfSameness : Iso ΩS¹ ℤ
lapsAreTheMannerOfSameness = ΩS¹Isoℤ

contrast : ((h : S¹ → ℤ) (x : S¹) → h x ≡ h base) × Iso ΩS¹ ℤ
contrast = noLapCountFromPosition , lapsAreTheMannerOfSameness

------------------------------------------------------------------------
-- C-13 (III)  Scales without an origin

evenℕ : ℕ → Bool
evenℕ zero = true
evenℕ (suc n) = not (evenℕ n)

parity : ℤ → Bool
parity (pos n) = evenℕ n
parity (negsuc n) = not (evenℕ n)

parityFlips : (z : ℤ) → parity (sucℤ z) ≡ not (parity z)
parityFlips (pos n) = refl
parityFlips (negsuc zero) = refl
parityFlips (negsuc (suc n)) = sym (notnot (not (evenℕ n)))

noFixedNot : (b : Bool) → ¬ (not b ≡ b)
noFixedNot true p = true≢false (sym p)
noFixedNot false p = true≢false p

sucℤ≢ : (z : ℤ) → ¬ (sucℤ z ≡ z)
sucℤ≢ z p = noFixedNot (parity z) (sym (parityFlips z) ∙ cong parity p)

-- no reading on every scale around the loop can be chosen consistently
noAbsoluteOrigin : ¬ ((x : S¹) → helix x)
noAbsoluteOrigin s = sucℤ≢ (s base) (sym (transportRefl (sucℤ (s base))) ∙ fromPathP (cong s loop))

-- the shift a trip induces on the scale is its winding number
shiftIsWinding : (p : ΩS¹) → transport (λ i → helix (p i)) (pos 0) ≡ winding p
shiftIsWinding p = refl

------------------------------------------------------------------------
-- C-14  Collision

isSetHelix : (x : S¹) → isSet (helix x)
isSetHelix base = isSetℤ
isSetHelix (loop i) = isProp→PathP (λ j → isPropIsSet {A = helix (loop j)}) isSetℤ isSetℤ i

encodeDecode : (x : S¹) (c : helix x) → encode x (decode x c) ≡ c
encodeDecode base c = windingℤLoop c
encodeDecode (loop i) =
  isProp→PathP
    (λ j → isPropΠ (λ c → isSetHelix (loop j) (encode (loop j) (decode (loop j) c)) c))
    windingℤLoop windingℤLoop i

pathsToCounter : (x : S¹) → Iso (base ≡ x) (helix x)
pathsToCounter x = iso (encode x) (decode x) (encodeDecode x) (decodeEncode x)

-- a runner carrying a lap counter has, up to identity, exactly one state
runnerHasOneState : isContr (Σ S¹ helix)
runnerHasOneState =
  isOfHLevelRespectEquiv 0 (Σ-cong-equiv-snd (λ x → isoToEquiv (pathsToCounter x))) (isContrSingl base)

zeroLapsIsOneLap : Path (Σ S¹ helix) (base , pos 0) (base , pos 1)
zeroLapsIsOneLap = isContr→isProp runnerHasOneState _ _

-- no integer-valued reading of the runner's state can vary
counterUnreadable : (g : Σ S¹ helix → ℤ) (w w' : Σ S¹ helix) → g w ≡ g w'
counterUnreadable g w w' = cong g (isContr→isProp runnerHasOneState w w')

-- along an identification no new information arises
module NoNewInformation {ℓ ℓ' : Level} {A : Type ℓ} (P : A → Type ℓ') where

  destinationPredicted : (s : (x : A) → P x) {a b : A} (p : a ≡ b)
    → s b ≡ transport (λ i → P (p i)) (s a)
  destinationPredicted s p = sym (fromPathP (cong s p))

  agreeOnceAgreeAlong : (s t : (x : A) → P x) {a b : A} (p : a ≡ b) → s a ≡ t a → s b ≡ t b
  agreeOnceAgreeAlong s t p q =
    destinationPredicted s p ∙ cong (transport (λ i → P (p i))) q ∙ fromPathP (cong t p)
