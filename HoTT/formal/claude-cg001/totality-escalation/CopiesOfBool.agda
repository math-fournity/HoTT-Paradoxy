{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The finite version of the Russell-shaped questioning: gather only the
  two-element sets, identifying the same ones (Claude, session 7f138325,
  2026-09-26; claim CG001-C-74).

  proof id : MP-CG001-COPIES-OF-BOOL-001
  claim    : CG001-C-74 (full statement in CLAIM-C74.md)

  No totality of all sets is involved, so Russell's size fence plays no role.
  CopiesOfBool gathers every type that is merely equivalent to Bool.

  (a) oneUpToSameness : the set-truncation of the gathering is contractible:
      counted up to sameness there is exactly one two-element set.
  (b) gatheringNotSettled : the gathering itself is not a set: univalence
      turns the swap of Bool into a loop of the gathering that is not refl.
  So the answer to "how many two-element sets are there, identifying the
  same ones?" is one, but the gathering does not settle into one point: it
  keeps the question "in which of the two ways is Bool the same as itself?".
-}
module CopiesOfBool where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_ ; idEquiv)
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Foundations.HLevels using (isOfHLevelPath)
open import Cubical.Data.Sigma using (Σ≡Prop)
open import Cubical.Data.Bool using (Bool ; true ; false ; true≢false)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.HITs.PropositionalTruncation as PT using (∥_∥₁ ; ∣_∣₁ ; squash₁)
open import Cubical.HITs.SetTruncation as ST using (∥_∥₂ ; ∣_∣₂ ; squash₂)
open import Cubical.Relation.Nullary using (¬_)

CopiesOfBool : Type₁
CopiesOfBool = Σ[ X ∈ Type ] ∥ X ≃ Bool ∥₁

theBool : CopiesOfBool
theBool = Bool , ∣ idEquiv Bool ∣₁

------------------------------------------------------------------------
-- (a) Counted up to sameness, there is exactly one.

oneUpToSameness : isContr ∥ CopiesOfBool ∥₂
oneUpToSameness = ∣ theBool ∣₂ , ST.elim (λ _ → isOfHLevelPath 2 squash₂ _ _) toTheBool
  where
  toTheBool : (c : CopiesOfBool) → ∣ theBool ∣₂ ≡ ∣ c ∣₂
  toTheBool (X , p) =
    PT.rec (squash₂ _ _) (λ e → cong ∣_∣₂ (Σ≡Prop (λ _ → squash₁) (sym (ua e)))) p

------------------------------------------------------------------------
-- (b) The gathering itself is not settled.

swapLoop : theBool ≡ theBool
swapLoop = Σ≡Prop (λ _ → squash₁) (ua notEquiv)

swapMoves : transport (cong fst swapLoop) true ≡ false
swapMoves = refl

gatheringNotSettled : ¬ isSet CopiesOfBool
gatheringNotSettled h =
  true≢false (sym (cong (λ q → transport (cong fst q) true) (h _ _ swapLoop refl)) ∙ swapMoves)
