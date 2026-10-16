{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The exit that univalence closes (Claude, session 7f138325, 2026-09-26).

  proof id : MP-CG001-UIP-ESCAPE-001
  claim    : CG001-C-63 (full statement in CLAIM.md)

  Why: every known definition of semi-simplicial types adds back some form of
  equality that is a mere fact (a strict or outer equality with uniqueness of
  identity proofs, or a display primitive); without it, each level has to
  carry the proofs used at the level below, and each such proof must cohere
  with the next level (the "infinite regress" reported by Kolomatskaia and
  Shulman).  This file isolates the premise that feeds the regress:

  (a) In the univalent universe, being the same is not a mere fact: Bool is
      identified with itself in two different ways, so Type is not a set.
  (b) Over a set, the next level cannot tell which proof of a lower equation
      it was built on: transport along any two proofs agrees.  At set level
      the regress stops after one step.
  (c) Over the universe, it can: the same boundary (Bool, Bool) carried along
      the two identifications gives different results.  So a construction
      over types must record which identification it used, and that record
      is itself subject to the same question one level up.

  Scope: (a)-(c) are standard facts (HoTT Book, Example 3.1.9 for (a)).  They
  do not prove that semi-simplicial types are undefinable in HoTT; that is an
  open problem (see CLAIM.md for the sources).
-}
module UIPEscape where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool
open import Cubical.Relation.Nullary

------------------------------------------------------------------------
-- (a) Two identifications of Bool with itself; the universe is not a set.

notPath : Bool ≡ Bool
notPath = ua notEquiv

alongNot : transport notPath true ≡ false
alongNot = uaβ notEquiv true

alongRefl : transport (refl {x = Bool}) true ≡ true
alongRefl = transportRefl true

twoIdentifications : ¬ (notPath ≡ refl)
twoIdentifications p =
  true≢false (sym alongRefl ∙ cong (λ q → transport q true) (sym p) ∙ alongNot)

typeIsNotASet : ¬ isSet Type
typeIsNotASet setType = twoIdentifications (setType Bool Bool notPath refl)

------------------------------------------------------------------------
-- (b) Over a set, higher data cannot depend on which proof was used.

overASet : {A : Type} → isSet A → (B : A → Type) {x y : A} (p q : x ≡ y)
  (b : B x) → subst B p b ≡ subst B q b
overASet setA B p q b = cong (λ r → subst B r b) (setA _ _ p q)

------------------------------------------------------------------------
-- (c) Over the universe, it does.

overTheUniverse :
  ¬ ((b : Bool) → subst (λ X → X) notPath b ≡ subst (λ X → X) refl b)
overTheUniverse sameEverywhere =
  true≢false (sym alongRefl ∙ sym (sameEverywhere true) ∙ alongNot)
