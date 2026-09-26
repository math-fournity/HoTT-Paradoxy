{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The decisive restoration step on the rational circle (Claude, session
  91a6cdaa, 2026-09-25): a second positive control for the ring story,
  separating "dense" from "equality undecidable".

  proof id : MP-CG001-RATIONAL-LIFT-001
  claims   : CG001-C-43 (full statement in CLAIM.md)

  On the unit circle with the point (-1, 0) removed, the stereographic
  parameter of a remaining point (x, y) is the t with (1 + x) t = y.  To
  compute it one must invert 1 + x knowing only that x is not -1.

  C-43  for rationals (dense, with decidable equality), knowing x /= -1 is
        enough: 1 + x /= 0, and a parameter t with (1 + x) t = y exists, by
        the library's inverse of nonzero rationals and no extra principle.

  Contrast (not proved here): for Dedekind reals, "x /= 0 implies x is
  apart from 0" is the principle RealNonzeroApartness, which Astra's C-319 /
  C-322 tie to the lift of the fixed restoration and to Markov's principle.

  Bridge labels (circle, gap, parameter, restore) prove no physical fact.
-}
module RationalLift where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Algebra.CommRing
open import Cubical.Algebra.CommRing.Instances.Rationals using (ℚCommRing)
open import Cubical.Algebra.Field.Instances.Rationals using (hasInverseℚ)
open import Cubical.Data.Rationals.MoreRationals.QuoQ using (ℚ)

open CommRingStr (ℚCommRing .snd)

-- if 1 + x were 0, x would be the gap point -1
awayFromGap : (x : ℚ) → ¬ (x ≡ - 1r) → ¬ (1r + x ≡ 0r)
awayFromGap x ne p = ne path
  where
  path : x ≡ - 1r
  path = sym (+IdL x)
       ∙ cong (_+ x) (sym (+InvL 1r))
       ∙ sym (+Assoc (- 1r) 1r x)
       ∙ cong ((- 1r) +_) p
       ∙ +IdR (- 1r)

-- the restoring parameter of any point other than the gap, with no extra principle
restoreParameter : (x y : ℚ) → ¬ (x ≡ - 1r) → Σ[ t ∈ ℚ ] (1r + x) · t ≡ y
restoreParameter x y ne = (u · y) , computes
  where
  inverse : Σ[ u ∈ ℚ ] (1r + x) · u ≡ 1r
  inverse = hasInverseℚ (1r + x) (awayFromGap x ne)

  u : ℚ
  u = fst inverse

  computes : (1r + x) · (u · y) ≡ y
  computes = ·Assoc (1r + x) u y ∙ cong (_· y) (snd inverse) ∙ ·IdL y
