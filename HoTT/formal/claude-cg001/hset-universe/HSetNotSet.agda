{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Even the universe of sets is not a set (Claude, session 7f138325,
  2026-09-26; goal CG-003, gate G4).

  proof id : MP-CG001-HSET-UNIVERSE-001
  claim    : CG001-C-71 (full statement in CLAIM.md)

  Why this matters for the self-interpretation dilemma of CG001-C-67.  To
  interpret a syntax that has been truncated to a set, the eliminator of the
  truncation needs its target to be a set.  The natural targets are the
  universe (not a set, CG001-C-63) and, more modestly, the universe of sets
  hSet.  Univalence makes hSet a groupoid that is not a set: Bool, a set,
  has the non-trivial self-identification ua notEquiv, which survives as a
  loop of hSet.  So the eliminator is blocked already for interpreting types
  as sets, although every syntactic equation would be interpreted by refl.

  (a) notPath≢refl : ¬ (ua notEquiv ≡ refl)   (transport of true is false)
  (b) flipSet      : a loop at (Bool, isSetBool) in hSet whose first
                     component is ua notEquiv
  (c) hSetNotSet   : ¬ isSet (hSet ℓ-zero)
-}
module HSetNotSet where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Foundations.HLevels using (hSet ; isPropIsSet)
open import Cubical.Data.Sigma using (Σ≡Prop)
open import Cubical.Data.Bool using (Bool ; true ; false ; true≢false)
open import Cubical.Data.Bool.Properties using (notEquiv ; isSetBool)
open import Cubical.Relation.Nullary using (¬_)

notPath : Bool ≡ Bool
notPath = ua notEquiv

notPath≢refl : ¬ (notPath ≡ refl)
notPath≢refl e = true≢false (sym (cong (λ q → transport q true) e))

BoolSet : hSet ℓ-zero
BoolSet = Bool , isSetBool

flipSet : BoolSet ≡ BoolSet
flipSet = Σ≡Prop (λ _ → isPropIsSet) notPath

hSetNotSet : ¬ isSet (hSet ℓ-zero)
hSetNotSet h = notPath≢refl (cong (cong fst) (h BoolSet BoolSet flipSet refl))
