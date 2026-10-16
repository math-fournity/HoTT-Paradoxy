{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda mirror of the declared L2-cofibration fragment (V2
-- calibration model) of the machine-overview engine.
--
-- Design source: Atria的方案/修订片/015 (§3 minimal design, §3.4 faithfulness
-- caveat, §5 stage-1 acceptance).  This module is the AGDA HALF of stage 1:
-- it defines the ground semantics natively and is checked against the Python
-- enumerator model on ALL ground terms (module V2GroundAgreement).
--
-- FAITHFULNESS CAVEAT (revision 015 §3.4), machine-checked in §8-9 below:
-- the face lattice here is the POINT-SET model (truth functions on the 4-point
-- boolean cube).  It validates the boolean law  f ∧ ¬f = 0, while the interval
-- I is a De Morgan algebra in which that law FAILS.  The point-set model is
-- therefore SOUND but NOT COMPLETE for De Morgan algebras (proved in §9).
-- Consequences, enforced by construction:
--   * no boolean identity is proved here as a theorem of the interval I;
--   * the model-only boolean laws live in a section named MODEL-ONLY and must
--     never justify a separation as a conclusion about the real interval;
--   * oracle verdicts for real-interval questions come only from the native
--     kernel on I (stage 2), never from this mirror (F-011).
--
-- ENGINEERING acceptance only: this module registers no mathematical claim
-- (registers_new_claim: false, revision 015 §5).

module V2Cofibration where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; foldr; map)

------------------------------------------------------------------
-- 1. Bounded enumerators
------------------------------------------------------------------

-- Bounded tower levels and bounded ground delay index: {0,1,2} (TOWER_MAX =
-- DELAY_INDEX_MAX = 2).  The bound is a GENERATOR discipline: op composition
-- on the delay axis (later / bind) uses unbounded ℕ below, exactly like the
-- L1 Delay fragment; only the ground enumeration is bounded.
data B3 : Type where b0 b1 b2 : B3

b3Toℕ : B3 → ℕ
b3Toℕ b0 = zero
b3Toℕ b1 = suc zero
b3Toℕ b2 = suc (suc zero)

b3LeqB : B3 → B3 → Bool     -- bounded tower comparison
b3LeqB b0 _ = true
b3LeqB b1 b0 = false
b3LeqB b1 _ = true
b3LeqB b2 b0 = false
b3LeqB b2 b1 = false
b3LeqB b2 b2 = true

------------------------------------------------------------------
-- 2. The point-set cube and the face lattice
------------------------------------------------------------------

-- The 4 corners of the square {0,1}², in the engine's declaration order
-- (POINT k = (i,j) for i,j ∈ (true,false)): TT, TF, FT, FF.
data Point : Type where
  ptTT : Point
  ptTF : Point
  ptFT : Point
  ptFF : Point

allPoints : List Point
allPoints = ptTT ∷ ptTF ∷ ptFT ∷ ptFF ∷ []

-- A cofibration face of the declared fragment: a truth function on the 4
-- points (bitmask 0..15 on the engine side).
Face : Type
Face = Point → Bool

faceMin faceMax : Face → Face → Face
faceMin f g p = f p and g p
faceMax f g p = f p or g p

faceNeg : Face → Face
faceNeg f p = not (f p)

fZERO fONE fI fJ : Face
fZERO p = false
fONE  p = true
fI ptTT = true;  fI ptTF = true;  fI ptFT = false; fI ptFF = false
fJ ptTT = true;  fJ ptTF = false; fJ ptFT = true;  fJ ptFF = false

-- Canonical former: the unique face whose truth table is the given 4 bits
-- (bit k ↔ point k, engine order).  faceFromBits-surjective (§5) shows every
-- face arises this way, i.e. the declared face set is finite with 16 members.
faceFromBits : Bool → Bool → Bool → Bool → Face
faceFromBits bTT bTF bFT bFF ptTT = bTT
faceFromBits bTT bTF bFT bFF ptTF = bTF
faceFromBits bTT bTF bFT bFF ptFT = bFT
faceFromBits bTT bTF bFT bFF ptFF = bFF

------------------------------------------------------------------
-- 3. Values, observations, contexts
------------------------------------------------------------------

data Avail : Type where
  absent    : Avail
  pending   : Avail
  available : Avail

data Opt : Type where none : Opt; some : Bool → Opt

-- V2 ground value: ω, or a returned value carrying the computation axis
-- (rounds n : ℕ, value b : Bool) and the structural axis (face, tower level).
data V2 : Type where
  vω : V2
  vret : (n : ℕ) (b : Bool) (f : Face) (l : B3) → V2

laterV : V2 → V2
laterV vω = vω
laterV (vret n b f l) = vret (suc n) b f l

-- A supplied-face set, modelled decidably as a membership predicate.
Supplied : Type
Supplied = Face → Bool

noSupplied : Supplied
noSupplied f = false

-- Declared observations of a V2 context.
data Obs : Type where
  obsDelay    : V2 → Obs
  obsOptional : Opt → Obs
  obsAvail    : Avail → Obs
  obsTower    : Bool → Obs
  obsDensity  : Bool → Obs

-- Declared context operations (revision 015 §3.2).
data Op : Type where
  opRaceL opRaceR : V2 → Op
  opBind          : (Bool → V2) → Op
  opSupply        : Face → Op
  opDeadline      : ℕ → Op
  opFill opFillOf : Face → Op
  opTower         : B3 → Op
  opBetween       : Face → Face → Op

OpList : Type
OpList = List Op

data Mode : Type where
  mDelay       : Mode
  mOptional    : Mode
  mAvailability : Mode
  mTower       : Mode
  mDensity     : Mode

modeOfOp : Op → Mode
modeOfOp (opRaceL _)     = mDelay
modeOfOp (opRaceR _)     = mDelay
modeOfOp (opBind _)      = mDelay
modeOfOp (opSupply _)    = mDelay
modeOfOp (opDeadline _)  = mOptional
modeOfOp (opFill _)      = mAvailability
modeOfOp (opFillOf _)    = mAvailability
modeOfOp (opTower _)     = mTower
modeOfOp (opBetween _ _) = mDensity

-- The observation mode is fixed by the LAST op (as in the L1 fragment).
observationMode : OpList → Mode
observationMode [] = mDelay
observationMode (x ∷ []) = modeOfOp x
observationMode (x ∷ y ∷ xs) = observationMode (y ∷ xs)

------------------------------------------------------------------
-- 4. Decidable equality helpers + list folds
------------------------------------------------------------------

andL : List Bool → Bool
andL = foldr _and_ true

foldlL : ∀ {ℓ ℓ'} {A : Type ℓ} {B : Type ℓ'} → (B → A → B) → B → List A → B
foldlL f z [] = z
foldlL f z (x ∷ xs) = foldlL f (f z x) xs

lengthList : ∀ {ℓ} {A : Type ℓ} → List A → ℕ
lengthList [] = zero
lengthList (x ∷ xs) = suc (lengthList xs)

boolEqB : Bool → Bool → Bool
boolEqB true  true  = true
boolEqB true  false = false
boolEqB false true  = false
boolEqB false false = true

b3EqB : B3 → B3 → Bool
b3EqB b0 b0 = true
b3EqB b0 b1 = false
b3EqB b0 b2 = false
b3EqB b1 b0 = false
b3EqB b1 b1 = true
b3EqB b1 b2 = false
b3EqB b2 b0 = false
b3EqB b2 b1 = false
b3EqB b2 b2 = true

natEqB : ℕ → ℕ → Bool
natEqB zero     zero     = true
natEqB zero     (suc _)  = false
natEqB (suc _)  zero     = false
natEqB (suc m)  (suc n)  = natEqB m n

nleqB : ℕ → ℕ → Bool      -- n ≤ m
nleqB zero     _        = true
nleqB (suc _)  zero     = false
nleqB (suc m)  (suc n)  = nleqB m n

pointEqB : Point → Point → Bool
pointEqB ptTT ptTT = true;  pointEqB ptTT ptTF = false; pointEqB ptTT ptFT = false; pointEqB ptTT ptFF = false
pointEqB ptTF ptTT = false; pointEqB ptTF ptTF = true;  pointEqB ptTF ptFT = false; pointEqB ptTF ptFF = false
pointEqB ptFT ptTT = false; pointEqB ptFT ptTF = false; pointEqB ptFT ptFT = true;  pointEqB ptFT ptFF = false
pointEqB ptFF ptTT = false; pointEqB ptFF ptTF = false; pointEqB ptFF ptFT = false; pointEqB ptFF ptFF = true

faceEqB : Face → Face → Bool
faceEqB f g = andL (map (λ p → boolEqB (f p) (g p)) allPoints)

optEqB : Opt → Opt → Bool
optEqB none       none       = true
optEqB none       (some _)   = false
optEqB (some _)   none       = false
optEqB (some x)   (some y)   = boolEqB x y

availEqB : Avail → Avail → Bool
availEqB absent    absent    = true
availEqB absent    pending   = false
availEqB absent    available = false
availEqB pending   absent    = false
availEqB pending   pending   = true
availEqB pending   available = false
availEqB available absent    = false
availEqB available pending   = false
availEqB available available = true

v2EqB : V2 → V2 → Bool
v2EqB vω          vω              = true
v2EqB vω          (vret _ _ _ _)  = false
v2EqB (vret _ _ _ _) vω           = false
v2EqB (vret n b f l) (vret n' b' f' l') =
  natEqB n n' and (boolEqB b b' and (faceEqB f f' and b3EqB l l'))

obsEqB : Obs → Obs → Bool
obsEqB (obsDelay x)    (obsDelay y)    = v2EqB x y
obsEqB (obsDelay _)    _               = false
obsEqB (obsOptional _) (obsDelay _)    = false
obsEqB (obsOptional x) (obsOptional y) = optEqB x y
obsEqB (obsOptional _) _               = false
obsEqB (obsAvail _)    (obsDelay _)    = false
obsEqB (obsAvail _)    (obsOptional _) = false
obsEqB (obsAvail x)    (obsAvail y)    = availEqB x y
obsEqB (obsAvail _)    (obsTower _)    = false
obsEqB (obsAvail _)    (obsDensity _)  = false
obsEqB (obsTower _)    (obsDelay _)    = false
obsEqB (obsTower _)    (obsOptional _) = false
obsEqB (obsTower _)    (obsAvail _)    = false
obsEqB (obsTower x)    (obsTower y)    = boolEqB x y
obsEqB (obsTower _)    (obsDensity _)  = false
obsEqB (obsDensity _)  (obsDelay _)    = false
obsEqB (obsDensity _)  (obsOptional _) = false
obsEqB (obsDensity _)  (obsAvail _)    = false
obsEqB (obsDensity _)  (obsTower _)    = false
obsEqB (obsDensity x)  (obsDensity y)  = boolEqB x y

------------------------------------------------------------------
-- 5. Finiteness of the declared face denominator (§3.4 (ii))
------------------------------------------------------------------

-- Every face is one of the 16 bit patterns ⇒ the declared face set is finite
-- with (at most) 16 members: a surjection Bool⁴ → Face.
faceFromBits-surjective : (f : Face) → faceFromBits (f ptTT) (f ptTF) (f ptFT) (f ptFF) ≡ f
faceFromBits-surjective f = funExt λ { ptTT → refl ; ptTF → refl ; ptFT → refl ; ptFF → refl }

------------------------------------------------------------------
-- 6. Delay-axis semantics (mirrors the L1 fragment exactly)
------------------------------------------------------------------

_+ℕ_ : ℕ → ℕ → ℕ
zero  +ℕ m = m
suc n +ℕ m = suc (n +ℕ m)
infixl 6 _+ℕ_

raceV : V2 → V2 → V2
raceV vω        y           = y
raceV x         vω          = x
raceV (vret n bv1 fv1 lv1) (vret m bv2 fv2 lv2) =
  if nleqB n m then vret n bv1 fv1 lv1 else vret m bv2 fv2 lv2

bindV : V2 → (Bool → V2) → V2
bindV vω        k = vω
bindV (vret n b f l) k with k b
... | vω          = vω
... | vret m b' f' l' = vret (n +ℕ m +ℕ suc zero) b' f' l'

convB : V2 → Bool → Bool
convB vω          _ = false
convB (vret _ b _ _) c = boolEqB b c

delayEquiv : V2 → V2 → Bool
delayEquiv l r = andL (map (λ c → boolEqB (convB l c) (convB r c)) (true ∷ false ∷ []))

------------------------------------------------------------------
-- 7. Context application (mirrors engine apply_ops, incl. the payload fix)
------------------------------------------------------------------

suppliedAt : Supplied → Face → Bool
suppliedAt s face = s face

supplyFace : Supplied → Face → Supplied
supplyFace s face f = if faceEqB face f then true else s f

fillOf : V2 → Supplied → Avail
fillOf vω          _   = absent
fillOf (vret _ _ f _) s = if suppliedAt s f then available else pending

deadlineO : ℕ → V2 → Opt
deadlineO _ vω          = none
deadlineO k (vret n b _ _) = if nleqB n k then some b else none

towerO : B3 → V2 → Bool
towerO _ vω          = false
towerO lvl (vret _ _ _ l) = b3LeqB l lvl

-- G-a density, positional form (revision 015 §3.2/§3.3): the VALUE's own face
-- is tested for lying strictly inside the declared interval (a,b).  The
-- value-dependent half is what makes density_observation reachable.
subsetB : Face → Face → Bool
subsetB x y = andL (map (λ p → (not (x p)) or (y p)) allPoints)

faceNeqB : Face → Face → Bool
faceNeqB x y = not (faceEqB x y)

faceStrictlyBetween : Face → Face → Face → Bool
faceStrictlyBetween a f b =
  (subsetB a f and subsetB f b) and (faceNeqB a f and faceNeqB f b)

-- Existence form (value-free): is there a face strictly between a and b,
-- read with a ⊆ b, i.e. does the difference carry ≥ 2 points?
pointsOf : Face → List Point
pointsOf f = foldr (λ p acc → if f p then p ∷ acc else acc) [] allPoints

faceBetween : Face → Face → Bool
faceBetween a b = 2≤length (pointsOf (λ p → a p and not (b p)))
  where
    2≤length : List Point → Bool
    2≤length [] = false
    2≤length (x ∷ []) = false
    2≤length (x ∷ y ∷ _) = true

-- One op step: (current value, supplied, accumulated terminal observation).
stepOp : Op → V2 → Supplied → Maybe Obs → V2 × Supplied × Maybe Obs
stepOp (opRaceL partner) cur s r = raceV cur partner , s , r
stepOp (opRaceR partner) cur s r = raceV partner cur , s , r
stepOp (opBind k)        cur s r = bindV cur k , s , r
stepOp (opSupply face)   cur s r = cur , supplyFace s face , r
stepOp (opDeadline k)    cur s r = cur , s , just (obsOptional (deadlineO k cur))
stepOp (opFill face)     cur s r = cur , s , just (obsAvail (fillOf cur s))
stepOp (opFillOf face)   cur s r =
  cur , s , just (obsAvail (if suppliedAt s face then available else pending))
stepOp (opTower lvl)     cur s r = cur , s , just (obsTower (towerO lvl cur))
stepOp (opBetween a b)   cur s r =
  cur , s , just (obsDensity (betweenO a cur b))
  where
    betweenO : Face → V2 → Face → Bool
    betweenO a vω b = false
    betweenO a (vret _ _ f _) b = faceStrictlyBetween a f b

applyOps : OpList → V2 → Supplied → Obs × Supplied
applyOps ops v s = finish (foldlL stepper (v , s , nothing) ops)
  where
    stepper : V2 × Supplied × Maybe Obs → Op → V2 × Supplied × Maybe Obs
    stepper (cur , sup , r) op = stepOp op cur sup r
    finish : V2 × Supplied × Maybe Obs → Obs × Supplied
    finish (cur , sup , just o)  = o , sup
    finish (cur , sup , nothing) = obsDelay cur , sup

-- The payload of an observation: the resulting value for a delay-mode context.
payload : Obs → V2
payload (obsDelay v) = v
payload _            = vω

------------------------------------------------------------------
-- 8. Separation (revision 015 §3.3) and its six kinds
------------------------------------------------------------------

data SeparationKind : Type where
  kValueMismatch         : SeparationKind
  kCompletionDivergence  : SeparationKind
  kDeadlineObservation   : SeparationKind
  kAvailabilityObservation : SeparationKind
  kLevelObservation      : SeparationKind
  kDensityObservation    : SeparationKind

kindEqB : SeparationKind → SeparationKind → Bool
kindEqB kValueMismatch         kValueMismatch         = true
kindEqB kValueMismatch         _                      = false
kindEqB kCompletionDivergence  kValueMismatch         = false
kindEqB kCompletionDivergence  kCompletionDivergence  = true
kindEqB kCompletionDivergence  _                      = false
kindEqB kDeadlineObservation   kDeadlineObservation   = true
kindEqB kDeadlineObservation   _                      = false
kindEqB kAvailabilityObservation kAvailabilityObservation = true
kindEqB kAvailabilityObservation _                    = false
kindEqB kLevelObservation      kLevelObservation      = true
kindEqB kLevelObservation      _                      = false
kindEqB kDensityObservation    kDensityObservation    = true
kindEqB kDensityObservation    _                      = false

isOmegaB : V2 → Bool
isOmegaB vω = true
isOmegaB _  = false

separationKind : OpList → Obs → Obs → SeparationKind
separationKind ops ol or with observationMode ops
... | mOptional      = kDeadlineObservation
... | mAvailability  = kAvailabilityObservation
... | mTower         = kLevelObservation
... | mDensity       = kDensityObservation
... | mDelay         = if _or_ (isOmegaB (payload ol)) (isOmegaB (payload or))
                         then kCompletionDivergence else kValueMismatch

equalForMode : Mode → Obs → Obs → Bool
equalForMode mDelay  ol or = delayEquiv (payload ol) (payload or)
equalForMode _       ol or = obsEqB ol or

SepResult : Type
SepResult = Bool × Obs × Obs × Maybe SeparationKind

maybeKEqB : Maybe SeparationKind → Maybe SeparationKind → Bool
maybeKEqB nothing  nothing  = true
maybeKEqB nothing  (just _) = false
maybeKEqB (just _) nothing  = false
maybeKEqB (just x) (just y) = kindEqB x y

sepEqB : SepResult → SepResult → Bool
sepEqB (q1 , o1 , p1 , k1) (q2 , o2 , p2 , k2) =
  boolEqB q1 q2 and (obsEqB o1 o2 and (obsEqB p1 p2 and maybeKEqB k1 k2))

separates : OpList → V2 → V2 → Supplied → SepResult
separates [] l r s = false , obsDelay l , obsDelay r , nothing
separates ops@(x ∷ xs) l r s =
  if equalForMode mode ol or
    then false , ol , or , nothing
    else true  , ol , or , just (separationKind ops ol or)
  where
    ol   = proj₁ (applyOps ops l s)
    or   = proj₁ (applyOps ops r s)
    mode = observationMode ops

------------------------------------------------------------------
-- 9. SOUNDNESS of the point-set model for De Morgan algebras
--    (revision 015 §3.4: the model is a De Morgan algebra)
------------------------------------------------------------------

boolAndComm : (x y : Bool) → x and y ≡ y and x
boolAndComm true  true  = refl
boolAndComm true  false = refl
boolAndComm false true  = refl
boolAndComm false false = refl

boolOrComm : (x y : Bool) → x or y ≡ y or x
boolOrComm true  true  = refl
boolOrComm true  false = refl
boolOrComm false true  = refl
boolOrComm false false = refl

boolNotNot : (x : Bool) → not (not x) ≡ x
boolNotNot true  = refl
boolNotNot false = refl

boolDeMorgan∧ : (x y : Bool) → not (x and y) ≡ not x or not y
boolDeMorgan∧ true  true  = refl
boolDeMorgan∧ true  false = refl
boolDeMorgan∧ false true  = refl
boolDeMorgan∧ false false = refl

boolDeMorgan∨ : (x y : Bool) → not (x or y) ≡ not x and not y
boolDeMorgan∨ true  true  = refl
boolDeMorgan∨ true  false = refl
boolDeMorgan∨ false true  = refl
boolDeMorgan∨ false false = refl

boolAbsorb₁ : (x y : Bool) → x or (x and y) ≡ x
boolAbsorb₁ true  _    = refl
boolAbsorb₁ false true = refl
boolAbsorb₁ false false = refl

boolAbsorb₂ : (x y : Bool) → x and (x or y) ≡ x
boolAbsorb₂ true  _     = refl
boolAbsorb₂ false true  = refl
boolAbsorb₂ false false = refl

faceMinComm : (f g : Face) → faceMin f g ≡ faceMin g f
faceMinComm f g = funExt λ p → boolAndComm (f p) (g p)

faceMaxComm : (f g : Face) → faceMax f g ≡ faceMax g f
faceMaxComm f g = funExt λ p → boolOrComm (f p) (g p)

faceNegInv : (f : Face) → faceNeg (faceNeg f) ≡ f
faceNegInv f = funExt λ p → boolNotNot (f p)

faceDeMorgan∧ : (f g : Face) → faceNeg (faceMin f g) ≡ faceMax (faceNeg f) (faceNeg g)
faceDeMorgan∧ f g = funExt λ p → boolDeMorgan∧ (f p) (g p)

faceDeMorgan∨ : (f g : Face) → faceNeg (faceMax f g) ≡ faceMin (faceNeg f) (faceNeg g)
faceDeMorgan∨ f g = funExt λ p → boolDeMorgan∨ (f p) (g p)

faceAbsorb₁ : (f g : Face) → faceMax f (faceMin f g) ≡ f
faceAbsorb₁ f g = funExt λ p → boolAbsorb₁ (f p) (g p)

faceAbsorb₂ : (f g : Face) → faceMin f (faceMax f g) ≡ f
faceAbsorb₂ f g = funExt λ p → boolAbsorb₂ (f p) (g p)

------------------------------------------------------------------
-- 10. MODEL-ONLY boolean laws + NON-COMPLETENESS (revision 015 §3.4)
------------------------------------------------------------------

-- MODEL-ONLY: the boolean law f ∧ ¬f = 0 holds for every face of the point-set
-- model.  This is deliberately NOT a theorem of the interval I: it holds here
-- because the model is boolean, and the interval is only a De Morgan algebra.
-- It must never be used to justify a separation as a conclusion about I.
boolComplementZero : (x : Bool) → x and not x ≡ false
boolComplementZero true  = refl
boolComplementZero false = refl

boolComplementOne : (x : Bool) → x or not x ≡ true
boolComplementOne true  = refl
boolComplementOne false = refl

modelOnly-complement-zero : (f : Face) → faceMin f (faceNeg f) ≡ fZERO
modelOnly-complement-zero f = funExt λ p → boolComplementZero (f p)

modelOnly-complement-one : (f : Face) → faceMax f (faceNeg f) ≡ fONE
modelOnly-complement-one f = funExt λ p → boolComplementOne (f p)

-- A De Morgan algebra in which the boolean law FAILS: the 3-element chain
-- 0 < a < 1 with negation 0↔1 and a fixed (¬ a = a).  This is the standard
-- non-boolean De Morgan algebra; it witnesses NON-COMPLETENESS of the
-- point-set model: the model proves an equation no De Morgan algebra theory
-- can prove, so a model-internal separation need not lift to the interval.
data DM3 : Type where   -- the 3-element chain 0 < a < 1
  d0 : DM3
  da : DM3
  d1 : DM3

dm3Meet dm3Join : DM3 → DM3 → DM3
dm3Meet d0 _  = d0
dm3Meet _  d0 = d0
dm3Meet d1 y  = y
dm3Meet da da = da
dm3Meet da d1 = da
dm3Join d1 _  = d1
dm3Join _  d1 = d1
dm3Join d0 y  = y
dm3Join da da = da
dm3Join da d0 = da

dm3Neg : DM3 → DM3
dm3Neg d0 = d1
dm3Neg d1 = d0
dm3Neg da = da

-- dm3 is a De Morgan algebra: commutativity, involution, De Morgan, absorption.
dm3MeetComm : (x y : DM3) → dm3Meet x y ≡ dm3Meet y x
dm3MeetComm d0 d0 = refl
dm3MeetComm d0 da = refl
dm3MeetComm d0 d1 = refl
dm3MeetComm da d0 = refl
dm3MeetComm da da = refl
dm3MeetComm da d1 = refl
dm3MeetComm d1 d0 = refl
dm3MeetComm d1 da = refl
dm3MeetComm d1 d1 = refl

dm3JoinComm : (x y : DM3) → dm3Join x y ≡ dm3Join y x
dm3JoinComm d0 d0 = refl
dm3JoinComm d0 da = refl
dm3JoinComm d0 d1 = refl
dm3JoinComm da d0 = refl
dm3JoinComm da da = refl
dm3JoinComm da d1 = refl
dm3JoinComm d1 d0 = refl
dm3JoinComm d1 da = refl
dm3JoinComm d1 d1 = refl

dm3NegInv : (x : DM3) → dm3Neg (dm3Neg x) ≡ x
dm3NegInv d0 = refl
dm3NegInv da = refl
dm3NegInv d1 = refl

dm3DeMorgan∧ : (x y : DM3) → dm3Neg (dm3Meet x y) ≡ dm3Join (dm3Neg x) (dm3Neg y)
dm3DeMorgan∧ d0 d0 = refl
dm3DeMorgan∧ d0 da = refl
dm3DeMorgan∧ d0 d1 = refl
dm3DeMorgan∧ da d0 = refl
dm3DeMorgan∧ da da = refl
dm3DeMorgan∧ da d1 = refl
dm3DeMorgan∧ d1 d0 = refl
dm3DeMorgan∧ d1 da = refl
dm3DeMorgan∧ d1 d1 = refl

dm3DeMorgan∨ : (x y : DM3) → dm3Neg (dm3Join x y) ≡ dm3Meet (dm3Neg x) (dm3Neg y)
dm3DeMorgan∨ d0 d0 = refl
dm3DeMorgan∨ d0 da = refl
dm3DeMorgan∨ d0 d1 = refl
dm3DeMorgan∨ da d0 = refl
dm3DeMorgan∨ da da = refl
dm3DeMorgan∨ da d1 = refl
dm3DeMorgan∨ d1 d0 = refl
dm3DeMorgan∨ d1 da = refl
dm3DeMorgan∨ d1 d1 = refl

dm3Absorb₁ : (x y : DM3) → dm3Join x (dm3Meet x y) ≡ x
dm3Absorb₁ d0 d0 = refl
dm3Absorb₁ d0 da = refl
dm3Absorb₁ d0 d1 = refl
dm3Absorb₁ da d0 = refl
dm3Absorb₁ da da = refl
dm3Absorb₁ da d1 = refl
dm3Absorb₁ d1 d0 = refl
dm3Absorb₁ d1 da = refl
dm3Absorb₁ d1 d1 = refl

dm3Absorb₂ : (x y : DM3) → dm3Meet x (dm3Join x y) ≡ x
dm3Absorb₂ d0 d0 = refl
dm3Absorb₂ d0 da = refl
dm3Absorb₂ d0 d1 = refl
dm3Absorb₂ da d0 = refl
dm3Absorb₂ da da = refl
dm3Absorb₂ da d1 = refl
dm3Absorb₂ d1 d0 = refl
dm3Absorb₂ d1 da = refl
dm3Absorb₂ d1 d1 = refl

-- The boolean law FAILS in dm3:  a ∧ ¬a = a ∧ a = a ≠ 0.
dm3MeetDaNegDa : dm3Meet da (dm3Neg da) ≡ da
dm3MeetDaNegDa = refl

isDA : DM3 → Bool
isDA da = true
isDA _  = false

da≢d0 : ¬ (da ≡ d0)
da≢d0 e = true≢false (cong isDA e)

-- The boolean law  x ∧ ¬x = 0  therefore FAILS in the De Morgan algebra dm3.
dm3NonBoolean : ¬ (dm3Meet da (dm3Neg da) ≡ d0)
dm3NonBoolean e = da≢d0 (sym dm3MeetDaNegDa ∙ e)
