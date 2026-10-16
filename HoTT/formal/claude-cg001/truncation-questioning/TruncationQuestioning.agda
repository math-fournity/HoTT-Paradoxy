{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The textbook dissolution as a control: the same questioning on the set
  truncation (Claude, local session eadb3381, macOS, 2026-09-30).

  proof id : MP-CG001-TRUNCATION-QUESTIONING-001
  claims   : CG001-C-83 (full statement in CLAIM.md)

  C-78 and C-81 showed that the questioning program Q of C-77 never halts on
  the universe and on the product of HoTT Book Example 8.8.6.  The textbook
  answer is: ask the question about the set truncation instead, where it is
  settled at once.  This file checks that answer, and what it costs.

  C-83 (a) for every type X and every judge, Q on the set truncation of X
           returns 1 at fuel 0: it stops at stage 1, like N and Bool (C-79);
       (b) the universe: the set truncation of Type ℓ-zero is not a
           proposition (the components of Unit and of the empty type
           differ), so a judge exists (no at stage 0, yes from stage 1 on);
           every judge equals it; the kernel runs Q with it and gets 1 at
           fuel 0 (refl); side by side with C-78, where Q on Type ℓ-zero
           itself is never;
       (c) the product: for every judge, Q on the set truncation of Prod
           stops at stage 1; side by side with C-81, where Q on Prod is
           never;
       (d) what the truncation costs: transport along notEq sends true to
           false, so notEq is not refl in Type ℓ-zero; after truncation the
           two self-identifications of Bool, notEq and refl, are equal (the
           constructor squash₂ declares any two parallel paths equal); and
           no function g from the truncation back to Type ℓ-zero decodes it
           (g ∣ A ∣₂ ≡ A for every A would make the universe a set).

  Nothing here says the truncation is wrong.  It records that the question
  becomes easy only after a constructor that declares sameness to be a fact,
  and that the object asked about is then no longer the universe.  The
  labels (catalogue, judge, questioning) prove no philosophical fact.
-}
module TruncationQuestioning where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Bool using (Bool; true; false; true≢false)
open import Cubical.Data.Bool.Properties using (notEq)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Sigma
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Empty as ⊥ using (⊥; isProp⊥)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)
open import Cubical.HITs.SetTruncation as ST using (∥_∥₂; ∣_∣₂; squash₂)
open import Cubical.HITs.PropositionalTruncation as PT using (∥_∥₁; ∣_∣₁; squash₁)

open import PedometerSemantics using (Delay; never; runFor)
open import QuestioningDelay
  using (Judge; module Questioning; question; judgesAreEqual; universeQuestioningIsNever)
open import ProductQuestioning using (Prod; productQuestioningIsNever)

private
  variable
    ℓ : Level

------------------------------------------------------------------------
-- C-83 (a) on a set truncation the questioning stops at stage 1

truncStopsAtOne : (X : Type ℓ) (judge : Judge ∥ X ∥₂) → runFor 0 (question ∥ X ∥₂ judge) ≡ just 1
truncStopsAtOne X judge = Questioning.settledAt ∥ X ∥₂ judge 0 1 squash₂

------------------------------------------------------------------------
-- C-83 (b) the universe

TU : Type (ℓ-suc ℓ-zero)
TU = ∥ Type ℓ-zero ∥₂

-- reading a component as a proposition: "is some member inhabited?"
inhabited : TU → hProp ℓ-zero
inhabited = ST.rec isSetHProp (λ A → ∥ A ∥₁ , squash₁)

-- the truncated universe is not a proposition
TUNotProp : ¬ isProp TU
TUNotProp h = PT.rec isProp⊥ (λ x → x) (transport UnitToEmpty ∣ tt ∣₁)
  where
  UnitToEmpty : ∥ Unit ∥₁ ≡ ∥ ⊥ ∥₁
  UnitToEmpty = cong (λ c → fst (inhabited c)) (h ∣ Unit ∣₂ ∣ ⊥ ∣₂)

judgeTU : Judge TU
judgeTU zero    = no TUNotProp
judgeTU (suc k) = yes (isOfHLevelPlus' {n = k} 2 squash₂)

everyJudgeIsJudgeTU : (judge : Judge TU) → judge ≡ judgeTU
everyJudgeIsJudgeTU judge = judgesAreEqual TU judge judgeTU

truncUniverseStopsAtOne : (judge : Judge TU) → runFor 0 (question TU judge) ≡ just 1
truncUniverseStopsAtOne judge = truncStopsAtOne (Type ℓ-zero) judge

-- the kernel runs the program with judgeTU
truncUniverseKernel : runFor 0 (question TU judgeTU) ≡ just 1
truncUniverseKernel = refl

-- side by side: the universe itself (C-78) and its set truncation
universeSideBySide : (judge : Judge (Type ℓ-zero)) (tjudge : Judge TU)
                   → (question (Type ℓ-zero) judge ≡ never) × (runFor 0 (question TU tjudge) ≡ just 1)
universeSideBySide judge tjudge = universeQuestioningIsNever judge , truncUniverseStopsAtOne tjudge

------------------------------------------------------------------------
-- C-83 (c) the product (C-81) and its set truncation

productSideBySide : (judge : Judge Prod) (tjudge : Judge ∥ Prod ∥₂)
                  → (question Prod judge ≡ never) × (runFor 0 (question ∥ Prod ∥₂ tjudge) ≡ just 1)
productSideBySide judge tjudge = productQuestioningIsNever judge , truncStopsAtOne Prod tjudge

------------------------------------------------------------------------
-- C-83 (d) what the truncation costs

notEqActs : transport notEq true ≡ false
notEqActs = refl

notEqNotRefl : ¬ notEq ≡ refl
notEqNotRefl p = true≢false (sym (transportRefl true) ∙ cong (λ q → transport q true) (sym p) ∙ notEqActs)

-- after truncation the two self-identifications of Bool are equal
truncCollapses : cong ∣_∣₂ notEq ≡ refl
truncCollapses = squash₂ ∣ Bool ∣₂ ∣ Bool ∣₂ (cong ∣_∣₂ notEq) refl

-- and the truncation cannot be decoded back into the universe
noDecoding : ¬ (Σ[ g ∈ (TU → Type ℓ-zero) ] ((A : Type ℓ-zero) → g ∣ A ∣₂ ≡ A))
noDecoding (g , r) = notEqNotRefl (universeIsSet Bool Bool notEq refl)
  where
  universeIsSet : isSet (Type ℓ-zero)
  universeIsSet = isOfHLevelRetract 2 ∣_∣₂ g r squash₂
