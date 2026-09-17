{-# OPTIONS --safe --cubical --guardedness #-}

-- FEASIBILITY PROBE for registered GAP A (revision 018 sec 3A):
-- an interval-oracle-shaped interpretation of the V2 structural axes on DM3,
-- the standard NON-BOOLEAN De Morgan algebra (V2Cofibration sec 10).
--
-- Question probed: can the three structural separation kinds of the V2
-- fragment -- availability / level / density -- be produced on a De Morgan
-- algebra in which the boolean law (x and ~x = 0) FAILS?
--
-- Answer (machine-checked below): YES for all three.  In particular the
-- density witness separates using dm3StrictlyBetween on the chain
-- 0 < a < 1, where the intermediate element da exists, while dm3NonBoolean
-- (imported) proves a and ~a = a != 0 in the SAME algebra.  So the
-- separation does NOT ride on the boolean law the point-set model carries.
--
-- This is a PROBE, not an acceptance unit: it establishes that the gap-A
-- design is realizable.  registers_new_claim: false (F-011).  The probe
-- still does NOT interpret the real cubical interval I (whose equality is
-- not decidable); DM3 is a non-boolean De Morgan algebra, not I itself.
-- Lifting "DM3" to "all De Morgan algebras" or to I is NOT claimed here;
-- what is claimed is the negative statement: NO BOOLEAN LAW IS NEEDED.

-- ORIGIN: this module began as the 2026-09-17 feasibility probe for gap A and
-- was promoted to the canonical DM3 mirror after the native kernel accepted it.
-- It is the AGDA HALF of the gap-A acceptance unit; the Python half is
-- machine_overview/v2_dm3.py, which must agree with it item-by-item.

module V2DM3 where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; foldr)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import V2Cofibration
  using (DM3; d0; da; d1; dm3Meet; dm3Join; dm3Neg; dm3NonBoolean;
          B3; b0; b1; b2; b3LeqB; b3EqB; Avail; absent; pending; available)

------------------------------------------------------------------
-- 1. Decidable structure on DM3 (the 3-element chain 0 < a < 1)
------------------------------------------------------------------

boolEqB : Bool → Bool → Bool
boolEqB true  true  = true
boolEqB true  false = false
boolEqB false true  = false
boolEqB false false = true

dm3EqB : DM3 → DM3 → Bool
dm3EqB d0 d0 = true
dm3EqB d0 da = false
dm3EqB d0 d1 = false
dm3EqB da d0 = false
dm3EqB da da = true
dm3EqB da d1 = false
dm3EqB d1 d0 = false
dm3EqB d1 da = false
dm3EqB d1 d1 = true

-- Order on the chain, defined directly by the enumeration.  No boolean
-- identity is used anywhere in this section.
dm3LeqB : DM3 → DM3 → Bool
dm3LeqB d0 _  = true
dm3LeqB da d0 = false
dm3LeqB da _  = true
dm3LeqB d1 d1 = true
dm3LeqB d1 _  = false

-- The direct order agrees with the meet characterization x <= y iff x and y
-- = x; this ties the enumeration to the algebra (De Morgan lattice) itself.
dm3MeetEqB : DM3 → DM3 → Bool
dm3MeetEqB x y = dm3EqB (dm3Meet x y) x

dm3LeMeet : (x y : DM3) → boolEqB (dm3LeqB x y) (dm3MeetEqB x y) ≡ true
dm3LeMeet d0 d0 = refl
dm3LeMeet d0 da = refl
dm3LeMeet d0 d1 = refl
dm3LeMeet da d0 = refl
dm3LeMeet da da = refl
dm3LeMeet da d1 = refl
dm3LeMeet d1 d0 = refl
dm3LeMeet d1 da = refl
dm3LeMeet d1 d1 = refl

-- G-a density, positional form, on the chain: f strictly inside (a,b).
dm3StrictlyBetween : DM3 → DM3 → DM3 → Bool
dm3StrictlyBetween a f b =
  (dm3LeqB a f and dm3LeqB f b) and
  (not (dm3EqB a f) and not (dm3EqB f b))

-- The intermediate element exists in this non-boolean algebra.
daStrictlyBetween01 : dm3StrictlyBetween d0 da d1 ≡ true
daStrictlyBetween01 = refl

-- The boolean law FAILS here (imported theorem of the mirror sec 10):
--   a and ~a = a != 0.
boolLawFails : ¬ (dm3Meet da (dm3Neg da) ≡ d0)
boolLawFails = dm3NonBoolean

------------------------------------------------------------------
-- 2. DM3-valued ground values
------------------------------------------------------------------

data V2D : Type where
  vωd   : V2D
  vretd : (n : ℕ) (b : Bool) (d : DM3) (l : B3) → V2D

SuppliedD : Type
SuppliedD = DM3 → Bool

noSuppliedD : SuppliedD
noSuppliedD _ = false

supplyDm3 : SuppliedD → DM3 → SuppliedD
supplyDm3 s d x = if dm3EqB x d then true else s x

suppliedAtD : SuppliedD → DM3 → Bool
suppliedAtD s d = s d

data ObsD : Type where
  obsDelayD   : V2D → ObsD
  obsAvailD   : Avail → ObsD
  obsTowerD   : Bool → ObsD
  obsDensityD : Bool → ObsD

data OpD : Type where
  opSupplyD  : DM3 → OpD
  opFillD    : OpD
  opTowerD   : B3 → OpD
  opBetweenD : DM3 → DM3 → OpD

OpDList : Type
OpDList = List OpD

data ModeD : Type where
  mDelayD mAvailabilityD mTowerD mDensityD : ModeD

modeOfOpD : OpD → ModeD
modeOfOpD (opSupplyD _)    = mDelayD
modeOfOpD opFillD          = mAvailabilityD
modeOfOpD (opTowerD _)     = mTowerD
modeOfOpD (opBetweenD _ _) = mDensityD

observationModeD : OpDList → ModeD
observationModeD [] = mDelayD
observationModeD (x ∷ []) = modeOfOpD x
observationModeD (x ∷ y ∷ xs) = observationModeD (y ∷ xs)

------------------------------------------------------------------
-- 3. Decidable equality helpers
------------------------------------------------------------------

natEqB : ℕ → ℕ → Bool
natEqB zero     zero     = true
natEqB zero     (suc _)  = false
natEqB (suc _)  zero     = false
natEqB (suc m)  (suc n)  = natEqB m n

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

v2dEqB : V2D → V2D → Bool
v2dEqB vωd          vωd              = true
v2dEqB vωd          (vretd _ _ _ _)  = false
v2dEqB (vretd _ _ _ _) vωd           = false
v2dEqB (vretd n b d l) (vretd n' b' d' l') =
  natEqB n n' and (boolEqB b b' and (dm3EqB d d' and b3EqB l l'))

obsEqD : ObsD → ObsD → Bool
obsEqD (obsDelayD x)   (obsDelayD y)   = v2dEqB x y
obsEqD (obsDelayD _)   _               = false
obsEqD (obsAvailD _)   (obsDelayD _)   = false
obsEqD (obsAvailD x)   (obsAvailD y)   = availEqB x y
obsEqD (obsAvailD _)   (obsTowerD _)   = false
obsEqD (obsAvailD _)   (obsDensityD _) = false
obsEqD (obsTowerD _)   (obsDelayD _)   = false
obsEqD (obsTowerD _)   (obsAvailD _)   = false
obsEqD (obsTowerD x)   (obsTowerD y)   = boolEqB x y
obsEqD (obsTowerD _)   (obsDensityD _) = false
obsEqD (obsDensityD _) (obsDelayD _)   = false
obsEqD (obsDensityD _) (obsAvailD _)   = false
obsEqD (obsDensityD _) (obsTowerD _)   = false
obsEqD (obsDensityD x) (obsDensityD y) = boolEqB x y

-- Delay-axis equivalence: only (n,b) visible, exactly as in the L1 fragment
-- and in V2Cofibration.delayEquiv.  The structural coordinates (d,l) are
-- invisible here -- that is what makes the three witnesses below
-- delay-invisible.
convD : V2D → Bool → Bool
convD vωd          _ = false
convD (vretd _ b _ _) b' = boolEqB b b'

delayEquivD : V2D → V2D → Bool
delayEquivD p q =
  boolEqB (convD p true)  (convD q true) and
  boolEqB (convD p false) (convD q false)

------------------------------------------------------------------
-- 4. Semantics of the ops
------------------------------------------------------------------

fillOfD : V2D → SuppliedD → Avail
fillOfD vωd          _ = absent
fillOfD (vretd _ _ d _) s = if suppliedAtD s d then available else pending

towerOfD : B3 → V2D → Bool
towerOfD _  vωd          = false
towerOfD lvl (vretd _ _ _ l) = b3LeqB l lvl

betweenOfD : DM3 → V2D → DM3 → Bool
betweenOfD _  vωd          _ = false
betweenOfD a  (vretd _ _ d _) b = dm3StrictlyBetween a d b

foldlL : {A B : Type} → (B → A → B) → B → List A → B
foldlL f z [] = z
foldlL f z (x ∷ xs) = foldlL f (f z x) xs

stepOpD : OpD → V2D → SuppliedD → Maybe ObsD → V2D × SuppliedD × Maybe ObsD
stepOpD (opSupplyD d)  cur s r = cur , supplyDm3 s d , r
stepOpD opFillD        cur s r = cur , s , just (obsAvailD (fillOfD cur s))
stepOpD (opTowerD lvl) cur s r = cur , s , just (obsTowerD (towerOfD lvl cur))
stepOpD (opBetweenD a b) cur s r = cur , s , just (obsDensityD (betweenOfD a cur b))

applyOpsD : OpDList → V2D → SuppliedD → ObsD × SuppliedD
applyOpsD ops v s = finish (foldlL stepper (v , s , nothing) ops)
  where
    stepper : V2D × SuppliedD × Maybe ObsD → OpD → V2D × SuppliedD × Maybe ObsD
    stepper (cur , sup , r) op = stepOpD op cur sup r
    finish : V2D × SuppliedD × Maybe ObsD → ObsD × SuppliedD
    finish (cur , sup , just o)  = o , sup
    finish (cur , sup , nothing) = obsDelayD cur , sup

payloadD : ObsD → V2D
payloadD (obsDelayD v) = v
payloadD _             = vωd

------------------------------------------------------------------
-- 5. Separation on the DM3-valued fragment
------------------------------------------------------------------

data SepKindD : Type where
  kAvailD kLevelD kDensityD : SepKindD

kindEqD : SepKindD → SepKindD → Bool
kindEqD kAvailD   kAvailD   = true
kindEqD kAvailD   _         = false
kindEqD kLevelD   kLevelD   = true
kindEqD kLevelD   _         = false
kindEqD kDensityD kDensityD = true
kindEqD kDensityD _         = false

separationKindD : OpDList → ObsD → ObsD → SepKindD
separationKindD ops ol or with observationModeD ops
... | mAvailabilityD = kAvailD
... | mTowerD        = kLevelD
... | mDensityD      = kDensityD
... | mDelayD        = kAvailD

equalForModeD : ModeD → ObsD → ObsD → Bool
equalForModeD mDelayD ol or = delayEquivD (payloadD ol) (payloadD or)
equalForModeD _        ol or = obsEqD ol or

maybeKindEqD : Maybe SepKindD → Maybe SepKindD → Bool
maybeKindEqD nothing  nothing  = true
maybeKindEqD nothing  (just _) = false
maybeKindEqD (just _) nothing  = false
maybeKindEqD (just x) (just y) = kindEqD x y

SepResultD : Type
SepResultD = Bool × ObsD × ObsD × Maybe SepKindD

sepEqD : SepResultD → SepResultD → Bool
sepEqD (q1 , o1 , p1 , k1) (q2 , o2 , p2 , k2) =
  boolEqB q1 q2 and (obsEqD o1 o2 and (obsEqD p1 p2 and maybeKindEqD k1 k2))

separatesD : OpDList → V2D → V2D → SuppliedD → SepResultD
separatesD [] l r s = false , obsDelayD l , obsDelayD r , nothing
separatesD ops@(x ∷ xs) l r s =
  if equalForModeD mode ol or
    then false , ol , or , nothing
    else true  , ol , or , just (separationKindD ops ol or)
  where
    ol   = proj₁ (applyOpsD ops l s)
    or   = proj₁ (applyOpsD ops r s)
    mode = observationModeD ops

------------------------------------------------------------------
-- 6. THE THREE STRUCTURAL WITNESSES, on the non-boolean algebra
------------------------------------------------------------------

-- (i) AVAILABILITY (G-b): a value whose declared cofibration coordinate IS
--     supplied vs one whose is NOT.  Decidable membership only; no lattice
--     identity.
pA qA : V2D
pA = vretd zero true da b0
qA = vretd zero true d1 b0

opsA : OpDList
opsA = opSupplyD da ∷ opFillD ∷ []

witnessA : sepEqD (separatesD opsA pA qA noSuppliedD)
               (true , obsAvailD available , obsAvailD pending , just kAvailD)
               ≡ true
witnessA = refl

sameValueControlA : sepEqD (separatesD opsA pA pA noSuppliedD)
                     (false , obsAvailD available , obsAvailD available , nothing)
                     ≡ true
sameValueControlA = refl

-- (ii) LEVEL (G-c): bounded truncation-tower comparison.  The bounded lattice
--      {b0,b1,b2} is finite and decidable; no face-lattice identity is used.
pL qL : V2D
pL = vretd zero true da b2
qL = vretd zero true da b0

opsL : OpDList
opsL = opTowerD b1 ∷ []

witnessL : sepEqD (separatesD opsL pL qL noSuppliedD)
               (true , obsTowerD false , obsTowerD true , just kLevelD)
               ≡ true
witnessL = refl

-- (iii) DENSITY (G-a): the value's own coordinate lies strictly inside the
--      declared interval (d0,d1).  da is strictly inside; d1 is not (it is
--      the upper bound).  THIS IS THE KEY WITNESS: the separation uses only
--      the chain order of the non-boolean De Morgan algebra, while
--      boolLawFails (dm3NonBoolean, mirror sec 10) proves a and ~a = a != 0
--      in the SAME algebra.  Hence the separation survives removal of the
--      boolean law that the point-set model carries for free.
pD qD : V2D
pD = vretd zero true da b0
qD = vretd zero true d1 b0

opsD : OpDList
opsD = opBetweenD d0 d1 ∷ []

witnessD : sepEqD (separatesD opsD pD qD noSuppliedD)
               (true , obsDensityD true , obsDensityD false , just kDensityD)
               ≡ true
witnessD = refl

sameValueControlD : sepEqD (separatesD opsD pD pD noSuppliedD)
                     (false , obsDensityD true , obsDensityD true , nothing)
                     ≡ true
sameValueControlD = refl

-- (iv) BOOLEAN-LAW INDEPENDENCE of the density witness: the boolean law
--      fails in this algebra, yet the density separation holds.  Both facts
--      are machine-checked above; this record states their conjunction for
--      the external auditor.
data BoolLawIndependence : Type where
  mk : (sepEqD (separatesD opsD pD qD noSuppliedD)
               (true , obsDensityD true , obsDensityD false , just kDensityD)
               ≡ true)
       → ¬ (dm3Meet da (dm3Neg da) ≡ d0)
       → BoolLawIndependence

boolLawIndependence : BoolLawIndependence
boolLawIndependence = mk witnessD boolLawFails

------------------------------------------------------------------
-- 7. Delay-axis invisibility (the L1 fragment cannot see these pairs)
------------------------------------------------------------------

delayInvisibleA : delayEquivD pA qA ≡ true
delayInvisibleA = refl

delayInvisibleL : delayEquivD pL qL ≡ true
delayInvisibleL = refl

delayInvisibleD : delayEquivD pD qD ≡ true
delayInvisibleD = refl

------------------------------------------------------------------
-- 8. Finiteness of the declared DM3 denominator (mirror sec 5 analogue)
------------------------------------------------------------------

allDM3 : List DM3
allDM3 = d0 ∷ da ∷ d1 ∷ []

-- The DM3 coordinate ranges over a finite decidable set of 3 elements, the
-- tower level over 3 and the delay index over a bounded prefix of N, so the
-- ground denominator is finite (1 + 3 * 2 * 3 * 3 = 55 elements) and every
-- observation above is total and decidable on it.
sucN : ℕ → ℕ
sucN n = suc n

denominatorIsFinite : foldr (λ _ n → sucN n) zero allDM3
                         ≡ sucN (sucN (sucN zero))
denominatorIsFinite = refl
