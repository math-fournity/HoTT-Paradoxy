{-# OPTIONS --safe --cubical --guardedness #-}

-- M1 first batch (GLM-R2): the ascent engine of the universe's
-- non-settling STALLS at set members.  HIT-free: only Prelude-level
-- univalence machinery, Bool not needed.  Together with C-63 (already
-- HIT-free: univalence alone makes the universe not a set), this
-- sharpens the P-HIT ablation: HITs are NOT needed for the first level
-- of non-settling, and level >= 2 non-triviality provably requires
-- NON-SET members (in HIT-free Type l-zero none are known; the full
-- ascent is supplied by HITs per C-75, or by the universe tower per
-- Kraus-Sattler 2015, source only).

module AscentStallAtSets where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_ ; invEquiv)
open import Cubical.Foundations.Univalence using (univalence)
open import Cubical.Foundations.HLevels
  using (isOfHLevelRespectEquiv ; isOfHLevel≃)

-- GLM-R2-C01: the universe's loop space at a SET member is itself a set
-- (the loop space is equivalent to the member's auto-equivalences, and
-- equivalences between sets form a set).
universeLoopSpaceAtSetIsSet :
  ∀ {ℓ} (X : Type ℓ) (pX : isSet X) → isSet (Path (Type ℓ) X X)
universeLoopSpaceAtSetIsSet X pX =
  isOfHLevelRespectEquiv 2 (invEquiv univalence) (isOfHLevel≃ 2 pX pX)

-- GLM-R2-C02: consequently the SECOND level of the ascent is trivial at
-- set members: the double loop space at a set member is contractible.
-- The local-global engine (Omega^2(U,X) ≃ Pi x, Omega^1(X,x)) has
-- nothing to lift at a set.
noLevel2AscentAtSets :
  ∀ {ℓ} (X : Type ℓ) (pX : isSet X)
  → isContr (Path (Path (Type ℓ) X X) refl refl)
noLevel2AscentAtSets X pX =
  refl ,
  (λ p → sym (universeLoopSpaceAtSetIsSet X pX refl refl p refl))
