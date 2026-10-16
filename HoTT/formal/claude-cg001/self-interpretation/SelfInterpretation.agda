{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A miniature of "HoTT eating itself" (Claude, session 7f138325, 2026-09-26;
  goal CG-002, gate G4).

  proof id : MP-CG001-SELF-INTERPRETATION-001
  claim    : CG001-C-67 (full statement in CLAIM.md)

  To interpret a type theory in itself one writes its syntax as an inductive
  type with equations, and sends each syntactic type to a type in the
  universe.  Kraus (LICS 2021) reports that in HoTT this is a long-standing
  open problem, because categories are not suitable to capture a type theory
  without uniqueness of identity proofs, and that the standard model is not a
  set-model since the universe is not a set.  This file shows the dilemma in
  a toy syntax with one equation, swap : a ⇒ (b ⇒ c) = b ⇒ (a ⇒ c), whose
  meaning in the universe is the argument-flip equivalence.

  (a) If the equations of the syntax are structure (no truncation, Syn∞),
      the faithful interpretation into the universe exists: swap goes to
      ua flipEquiv.  Then the syntax is not a set: its own equations carry
      information, so its coherence becomes a further obligation.
  (b) If the equations are facts (the syntax is truncated to a set, Syn, as
      in quotient-inductive presentations of syntax), the syntax can be
      interpreted into the universe of propositions, which is a set; but no
      function into the univalent universe sends swap to the flip.

  The toy has only function types over one base type and one equation.  It
  is a miniature of the obstruction, not a model of type theory.
-}
module SelfInterpretation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (flip)
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso ; isoToEquiv)
open import Cubical.Foundations.Univalence using (ua ; uaβ ; hPropExt)
open import Cubical.Foundations.HLevels using (hProp ; isSetHProp ; isPropΠ)
open import Cubical.Foundations.GroupoidLaws using (lUnit ; rUnit ; lCancel)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Sigma using (Σ-syntax ; _,_ ; fst ; snd)
open import Cubical.Data.Bool using (Bool ; true ; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Unit.Properties using (isPropUnit)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- The meaning of swap: flipping the order of two arguments.

flipEquiv : {A B C : Type} → (A → B → C) ≃ (B → A → C)
flipEquiv = isoToEquiv (iso flip flip (λ _ → refl) (λ _ → refl))

first : Bool → Bool → Bool
first x y = x

flipIsNotRefl : ¬ (ua (flipEquiv {Bool} {Bool} {Bool}) ≡ refl)
flipIsNotRefl e =
  false≢true (cong (λ g → g true false)
    (sym (uaβ flipEquiv first) ∙ cong (λ q → transport q first) e ∙ transportRefl first))

------------------------------------------------------------------------
-- (a) Equations as structure: faithful, but the syntax is not a set.

data Syn∞ : Type where
  base : Syn∞
  arr  : Syn∞ → Syn∞ → Syn∞
  swap : (a b c : Syn∞) → arr a (arr b c) ≡ arr b (arr a c)

⟦_⟧∞ : Syn∞ → Type
⟦ base ⟧∞ = Bool
⟦ arr a b ⟧∞ = ⟦ a ⟧∞ → ⟦ b ⟧∞
⟦ swap a b c i ⟧∞ = ua (flipEquiv {⟦ a ⟧∞} {⟦ b ⟧∞} {⟦ c ⟧∞}) i

faithful∞ : cong ⟦_⟧∞ (swap base base base) ≡ ua flipEquiv
faithful∞ = refl

syntax∞IsNotASet : ¬ isSet Syn∞
syntax∞IsNotASet setSyn =
  flipIsNotRefl (sym faithful∞ ∙ cong (cong ⟦_⟧∞) (setSyn _ _ (swap base base base) refl))

------------------------------------------------------------------------
-- (b) Equations as facts: the syntax is a set.

data Syn : Type where
  base  : Syn
  arr   : Syn → Syn → Syn
  swap  : (a b c : Syn) → arr a (arr b c) ≡ arr b (arr a c)
  trunc : isSet Syn

-- The universe of propositions is a set, and the set-level syntax maps into it.

isProp→→ : {A B C : Type} → isProp C → isProp (A → B → C)
isProp→→ pC = isPropΠ (λ _ → isPropΠ (λ _ → pC))

⟦_⟧P : Syn → hProp ℓ-zero
⟦ base ⟧P = Unit , isPropUnit
⟦ arr a b ⟧P = (fst ⟦ a ⟧P → fst ⟦ b ⟧P) , isPropΠ (λ _ → snd ⟦ b ⟧P)
⟦ swap a b c i ⟧P =
  Σ≡Prop (λ _ → isPropIsProp)
    {u = (fst ⟦ a ⟧P → fst ⟦ b ⟧P → fst ⟦ c ⟧P) , isProp→→ (snd ⟦ c ⟧P)}
    {v = (fst ⟦ b ⟧P → fst ⟦ a ⟧P → fst ⟦ c ⟧P) , isProp→→ (snd ⟦ c ⟧P)}
    (hPropExt (isProp→→ (snd ⟦ c ⟧P)) (isProp→→ (snd ⟦ c ⟧P)) flip flip) i
⟦ trunc x y p q i j ⟧P =
  isSetHProp ⟦ x ⟧P ⟦ y ⟧P (cong ⟦_⟧P p) (cong ⟦_⟧P q) i j

-- A faithful interpretation into the univalent universe would send swap at
-- (base, base, base) to the flip, up to a chosen identification e of the
-- value at base ⇒ (base ⇒ base) with Bool → Bool → Bool.

Faithful : (S : Type) (b : S) (ar : S → S → S)
  (sw : (a b c : S) → ar a (ar b c) ≡ ar b (ar a c)) → Type₁
Faithful S b ar sw =
  Σ[ f ∈ (S → Type) ]
  Σ[ e ∈ (f (ar b (ar b b)) ≡ (Bool → Bool → Bool)) ]
    (sym e ∙ cong f (sw b b b) ∙ e ≡ ua flipEquiv)

faithfulForStructure : Faithful Syn∞ base arr swap
faithfulForStructure =
  ⟦_⟧∞ , refl , sym (lUnit (ua flipEquiv ∙ refl)) ∙ sym (rUnit (ua flipEquiv))

noFaithfulForFacts : ¬ Faithful Syn base arr swap
noFaithfulForFacts (f , e , h) =
  flipIsNotRefl (sym h ∙ cong (λ q → sym e ∙ q ∙ e) swapIsRefl ∙ cancel)
  where
  swapIsRefl : cong f (swap base base base) ≡ refl
  swapIsRefl = cong (cong f) (trunc _ _ (swap base base base) refl)
  cancel : sym e ∙ refl ∙ e ≡ refl
  cancel = cong (sym e ∙_) (sym (lUnit e)) ∙ lCancel e
