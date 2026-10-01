{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A Russell-shaped questioning that must be completed: gather everything whose
  sameness has settled, and ask the gathering to be settled too (Claude,
  session 7f138325, 2026-09-26; claim CG001-C-73).

  proof id : MP-CG001-TOTALITY-ESCALATION-001
  claim    : CG001-C-73 (full statement in CLAIM.md)

  "Settled at level n" means being an n-type in the sense of h-levels
  (isOfHLevel n): for sets (level 2 in the library's counting) the question
  "in what way are x and y the same?" has at most one answer; for groupoids
  (level 3) the answers may differ but the ways between answers are unique;
  and so on.  TypeOfHLevel ℓ n gathers all types settled at level n.

  (a) Upper bound (library): the gathering of all n-types is an (n+1)-type.
  (b) Exactness at the first two rungs:
        the gathering of all sets is not a set        (setsGatherNotSet);
        the gathering of all groupoids is not a groupoid (groupoidsGatherNotGroupoid).
      So to include the gathering among the things gathered, one must go one
      level up, and the new gathering is again one level less settled:
      the demand never closes.  Univalence is what makes it escalate:
      Bool has two self-identifications (ua of not), and the circle's identity
      self-equivalence has a non-trivial loop (rotating once), which univalence
      turns into non-trivial sameness of the gatherings.
  (c) For contrast, in Lean 4 with uniqueness of identity proofs the universe
      is a set (CG001-C-72): there the gathering of settled things is settled
      at once.  (The size of the universe goes up in both worlds; that is
      Russell's own fence, not the escalation proved here.)
  (d) Forcing the gathering to be settled by truncation destroys it as a
      gathering: no map from the set-truncation back to hSet can undo the
      truncation (noDecoding), since that would make hSet a set.
-}
module TotalityEscalates where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv ; equivEq ; equivFun ; invEquiv ; compEquiv ; _≃_)
open import Cubical.Foundations.Univalence using (ua ; univalence)
open import Cubical.Foundations.HLevels
  using (hSet ; hGroupoid ; TypeOfHLevel ; isOfHLevelTypeOfHLevel ; isPropIsSet ; isPropIsGroupoid
       ; isOfHLevelRespectEquiv ; isOfHLevel)
open import Cubical.Data.Sigma using (Σ≡Prop)
open import Cubical.Data.Sigma.Properties using (Σ≡PropEquiv)
open import Cubical.Data.Bool using (Bool ; true ; false ; true≢false)
open import Cubical.Data.Bool.Properties using (notEquiv ; isSetBool)
open import Cubical.Data.Nat using (ℕ ; suc)
open import Cubical.Data.Nat.Properties using (snotz)
open import Cubical.Data.Int using (pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.HITs.S1.Base using (S¹ ; base ; loop ; rotLoop ; winding)
open import Cubical.HITs.S1.Properties using (isGroupoidS¹)
open import Cubical.HITs.SetTruncation using (∥_∥₂ ; ∣_∣₂ ; squash₂)
open import Cubical.Foundations.HLevels using (isOfHLevelRetract)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- (a) Upper bound: gathering n-types gives an (n+1)-type (library).

setsGatherIntoGroupoid : isGroupoid (hSet ℓ-zero)
setsGatherIntoGroupoid = isOfHLevelTypeOfHLevel 2

groupoidsGatherInto2Type : isOfHLevel 4 (hGroupoid ℓ-zero)
groupoidsGatherInto2Type = isOfHLevelTypeOfHLevel 3

ladderUpper : (n : ℕ) → isOfHLevel (suc n) (TypeOfHLevel ℓ-zero n)
ladderUpper = isOfHLevelTypeOfHLevel

------------------------------------------------------------------------
-- (b1) The gathering of all sets is not a set.

notPath : Bool ≡ Bool
notPath = ua notEquiv

notPath≢refl : ¬ (notPath ≡ refl)
notPath≢refl e = true≢false (sym (cong (λ q → transport q true) e))

BoolSet : hSet ℓ-zero
BoolSet = Bool , isSetBool

setsGatherNotSet : ¬ isSet (hSet ℓ-zero)
setsGatherNotSet h =
  notPath≢refl (cong (cong fst) (h BoolSet BoolSet (Σ≡Prop (λ _ → isPropIsSet) notPath) refl))

------------------------------------------------------------------------
-- (b2) The gathering of all groupoids is not a groupoid.

-- Rotating the circle once is a loop at the identity self-equivalence.
rotateOnce : idEquiv S¹ ≡ idEquiv S¹
rotateOnce = equivEq (funExt rotLoop)

rotateOnceWinds : winding (cong (λ e → equivFun e base) rotateOnce) ≡ pos 1
rotateOnceWinds = refl

selfEquivsNotSet : ¬ isSet (S¹ ≃ S¹)
selfEquivsNotSet s =
  snotz (injPos (sym rotateOnceWinds
                 ∙ cong (λ q → winding (cong (λ e → equivFun e base) q)) (s _ _ rotateOnce refl)))

CircleGroupoid : hGroupoid ℓ-zero
CircleGroupoid = S¹ , isGroupoidS¹

-- Loops of the gathering at the circle are the circle's self-equivalences.
loopsAtCircle : (CircleGroupoid ≡ CircleGroupoid) ≃ (S¹ ≃ S¹)
loopsAtCircle = compEquiv (invEquiv (Σ≡PropEquiv (λ _ → isPropIsGroupoid))) univalence

groupoidsGatherNotGroupoid : ¬ isGroupoid (hGroupoid ℓ-zero)
groupoidsGatherNotGroupoid h =
  selfEquivsNotSet (isOfHLevelRespectEquiv 2 loopsAtCircle (h CircleGroupoid CircleGroupoid))

------------------------------------------------------------------------
-- (d) Truncating the gathering settles it, but it can no longer be decoded.

noDecoding : ¬ (Σ[ s ∈ (∥ hSet ℓ-zero ∥₂ → hSet ℓ-zero) ] ((X : hSet ℓ-zero) → s ∣ X ∣₂ ≡ X))
noDecoding (s , sec) = setsGatherNotSet (isOfHLevelRetract 2 ∣_∣₂ s sec squash₂)
