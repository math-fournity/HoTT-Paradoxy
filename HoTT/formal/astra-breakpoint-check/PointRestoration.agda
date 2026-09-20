{-# OPTIONS --safe --cubical --guardedness #-}
module PointRestoration where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Empty as Empty using (⊥)
open import Cubical.Relation.Nullary using (Dec; yes; no; isProp¬)

-- No topology, physical-operation permission, resizing or excluded middle
-- is silently built into this interface. All universes are explicit.
module Restoration {ℓ : Level} (C : Type ℓ) (p : C) where
  Puncture : Type ℓ
  Puncture = Σ[ x ∈ C ] ((x ≡ p) → ⊥)

  Completed : Type ℓ
  Completed = Puncture ⊎ Unit

  extend : Completed → C
  extend (inl (x , absent)) = x
  extend (inr tt) = p

  SplitRestore : Type ℓ
  SplitRestore = Σ[ decode ∈ (C → Completed) ] ((x : C) → extend (decode x) ≡ x)

  PointDecidable : Type ℓ
  PointDecidable = (x : C) → Dec (x ≡ p)

  splitToDecision : SplitRestore → PointDecidable
  splitToDecision (decode , law) x = classify (decode x) (law x)
    where
    classify : (r : Completed) → extend r ≡ x → Dec (x ≡ p)
    classify (inl (y , absent)) q = no (λ xp → absent (q ∙ xp))
    classify (inr tt) q = yes (sym q)

  decode : PointDecidable → C → Completed
  decode decision x with decision x
  ... | yes xp = inr tt
  ... | no absent = inl (x , absent)

  decodeRight : (decision : PointDecidable) (x : C)
    → extend (decode decision x) ≡ x
  decodeRight decision x with decision x
  ... | yes xp = sym xp
  ... | no absent = refl

  decisionToSplit : PointDecidable → SplitRestore
  decisionToSplit decision = decode decision , decodeRight decision

  -- The two implications are explicit; no extra equivalence of evidence
  -- types, uniqueness of choices or judgmental inverse law is asserted.
  restorationCriterion : (SplitRestore → PointDecidable) × (PointDecidable → SplitRestore)
  restorationCriterion = splitToDecision , decisionToSplit

  decodeLeft : (decision : PointDecidable) (r : Completed)
    → decode decision (extend r) ≡ r
  decodeLeft decision (inl (x , absent)) with decision x
  ... | yes xp = Empty.rec (absent xp)
  ... | no absent' = cong inl (Σ≡Prop (λ y → isProp¬ (y ≡ p)) refl)
  decodeLeft decision (inr tt) with decision p
  ... | yes pp = refl
  ... | no absent = Empty.rec (absent refl)

  restorationIso : PointDecidable → Iso Completed C
  Iso.fun (restorationIso decision) = extend
  Iso.inv (restorationIso decision) = decode decision
  Iso.rightInv (restorationIso decision) = decodeRight decision
  Iso.leftInv (restorationIso decision) = decodeLeft decision

  restorationEquiv : PointDecidable → Completed ≃ C
  restorationEquiv decision = isoToEquiv (restorationIso decision)
