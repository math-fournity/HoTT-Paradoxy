{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The same questioning on a type that is not the universe (Claude, local
  session eadb3381, macOS, 2026-09-30).

  proof id : MP-CG001-PRODUCT-QUESTIONING-001
  claims   : CG001-C-81, CG001-C-82 (full statements in CLAIM.md)

  HoTT Book, Example 8.8.6: if every B(n) has an n-dimensional loop that is
  not n-fold reflexivity, the product of all B(n) is not an m-type for any
  m.  This file takes B from the C-75 package, K n = EM ℤ (1+n) (an
  Eilenberg-MacLane space, a higher inductive type), forms the product
  Prod = (n : ℕ) → K n, and runs on it the questioning program Q of C-77.
  C-78 showed that Q never halts on the universe; here the questioned object
  is an ordinary small type.

  C-81 (the product of members of unbounded height)
       (a) at the base point of K n, the (1+n)-fold loop sec n of C-75 is
           not trivial (C-75 states this for the whole section; its proof
           only evaluates at the base point);
       (b) for every m, Prod is not of h-level m;
       (c) for every judge, Q on Prod is never: every run returns nothing
           and Q never answers; a judge exists (it answers no at every
           stage) and every judge is equal to it; the kernel runs Q with
           that judge and fuel 1000 and gets nothing (refl);
       (d) contrast: the program that asks "is Prod settled at some h-level
           at all?" answers no at fuel 0, for every way of deciding that
           question.
  C-82 (the same product with members of bounded height)
       (a) for every b, Bounded b = (n : ℕ) → K b is of h-level 3+b and is
           not of h-level 2+b;
       (b) for every b and every judge, Q on Bounded b returns 2+b at fuel
           1+b and returns nothing at every smaller fuel: it stops at stage
           2+b; a judge exists for every b; for b = 0 the product of
           copies of K 0 stops at stage 2.

  The universe is not the questioned object here.  It appears only as the
  codomain of the family K : ℕ → Type ℓ-zero, which is defined by recursion
  on ℕ.  Higher inductive types (the Eilenberg-MacLane spaces) and
  univalence (inside the loop computations imported from C-75) are used.
  The labels (catalogue, judge, questioning) prove no philosophical fact:
  reading an existence question as this process is the interpretation
  bridge of audit paper 02, not a theorem.
-}
module ProductQuestioning where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Pointed
open import Cubical.Foundations.Transport using (transportTransport⁻)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_; snotz; discreteℕ; isSetℕ)
open import Cubical.Data.Nat.Order using (_≤_; _<_; suc-≤-suc; ≤<-trans; ≤-refl; splitℕ-≤)
open import Cubical.Data.Int using (ℤ; pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Bool using (Bool; false)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Empty as ⊥ using ()
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)
open import Cubical.Homotopy.Loopspace using (Ω^_)
open import Cubical.Algebra.AbGroup.Instances.Int using (ℤAbGroup)
open import Cubical.Homotopy.EilenbergMacLane.Base using (EM∙; 0ₖ; hLevelEM)

open import PedometerSemantics using (Delay; never; runFor)
open import UniverseHasNoLevel using (K; ΩⁿK; sec; trivSec; Πpt; Ω^Πpt; hLevelΩ^)
open import QuestioningDelay
  using (Judge; module Questioning; question; judgesAreEqual; whetherSettled; levelUp)

------------------------------------------------------------------------
-- C-81 (a) the loop of C-75 is not trivial at the base point

x₀ : (n : ℕ) → K n
x₀ n = 0ₖ {G = ℤAbGroup} (suc n)

secAtBase≢triv : (n : ℕ) → ¬ (sec n (x₀ n) ≡ trivSec n (x₀ n))
secAtBase≢triv n q = snotz (injPos one≡zero)
  where
  P : (Ω^ (suc n)) (K n , x₀ n) ≡ EM∙ ℤAbGroup 0
  P = ΩⁿK n (x₀ n)
  one≡zero : pos 1 ≡ pos 0
  one≡zero =
    sym (transportTransport⁻ (cong typ P) (pos 1))
    ∙ cong (transport (cong typ P)) q
    ∙ fromPathP (cong pt P)

------------------------------------------------------------------------
-- C-81 (b) the product of all K n has no h-level (HoTT Book Example 8.8.6)

Prod : Type ℓ-zero
Prod = (n : ℕ) → K n

Prod∙ : Pointed ℓ-zero
Prod∙ = Πpt ℕ (λ n → K n , x₀ n)

-- the loop space of dimension 1+m at the base point, one factor per n
LoopFactor : (m n : ℕ) → Type ℓ-zero
LoopFactor m n = typ ((Ω^ (suc m)) (K n , x₀ n))

-- in dimension 1+m: the loop sec m at factor m, the trivial loop elsewhere
pick : (m n : ℕ) → Dec (m ≡ n) → LoopFactor m n
pick m n (yes p) = subst (LoopFactor m) p (sec m (x₀ m))
pick m n (no _)  = pt ((Ω^ (suc m)) (K n , x₀ n))

bump : (m : ℕ) → (n : ℕ) → LoopFactor m n
bump m n = pick m n (discreteℕ m n)

bumpAtItself : (m : ℕ) → bump m m ≡ sec m (x₀ m)
bumpAtItself m = go (discreteℕ m m)
  where
  go : (d : Dec (m ≡ m)) → pick m m d ≡ sec m (x₀ m)
  go (yes p) = cong (λ r → subst (LoopFactor m) r (sec m (x₀ m))) (isSetℕ m m p refl)
               ∙ substRefl {B = LoopFactor m} {x = m} (sec m (x₀ m))
  go (no ¬p) = ⊥.rec (¬p refl)

productNot2+ : (m : ℕ) → ¬ isOfHLevel (2 + m) Prod
productNot2+ m h = secAtBase≢triv m (sym (bumpAtItself m) ∙ funExt⁻ bumpIsTrivial m)
  where
  contrLoops : isContr (typ ((Ω^ (suc m)) Prod∙))
  contrLoops = hLevelΩ^ (suc m) (pt Prod∙) h
  contrFactors : isContr ((n : ℕ) → LoopFactor m n)
  contrFactors = subst (λ A → isContr (typ A)) (Ω^Πpt (suc m) ℕ (λ n → K n , x₀ n)) contrLoops
  bumpIsTrivial : bump m ≡ (λ n → pt ((Ω^ (suc m)) (K n , x₀ n)))
  bumpIsTrivial = isContr→isProp contrFactors (bump m) (λ n → pt ((Ω^ (suc m)) (K n , x₀ n)))

productHasNoLevel : (m : ℕ) → ¬ isOfHLevel m Prod
productHasNoLevel m h = productNot2+ m (isOfHLevelPlus 2 h)

------------------------------------------------------------------------
-- C-81 (c) the questioning of the product never halts

judgeProd : Judge Prod
judgeProd k = no (productHasNoLevel (suc k))

everyJudgeIsJudgeProd : (judge : Judge Prod) → judge ≡ judgeProd
everyJudgeIsJudgeProd judge = judgesAreEqual Prod judge judgeProd

productQuestioningIsNever : (judge : Judge Prod) → question Prod judge ≡ never
productQuestioningIsNever judge = Questioning.noLevelToNever Prod judge productHasNoLevel

productQuestioningRunsNothing : (judge : Judge Prod) (n : ℕ) → runFor n (question Prod judge) ≡ nothing
productQuestioningRunsNothing judge = Questioning.NoLevel.QRunsNothing Prod judge productHasNoLevel

productQuestioningNeverAnswers : (judge : Judge Prod) → ¬ Questioning.Halts Prod judge
productQuestioningNeverAnswers judge = Questioning.NoLevel.QNeverAnswers Prod judge productHasNoLevel

-- the kernel runs the program with judgeProd and fuel 1000
productKernelRuns1000 : runFor 1000 (question Prod judgeProd) ≡ nothing
productKernelRuns1000 = refl

------------------------------------------------------------------------
-- C-81 (d) contrast: "is it settled at some h-level at all?" answers at once

productWhetherAnswersNo : (d : Dec (Σ[ m ∈ ℕ ] isOfHLevel m Prod))
                        → runFor 0 (whetherSettled Prod d) ≡ just false
productWhetherAnswersNo (yes w) = ⊥.rec (productHasNoLevel (fst w) (snd w))
productWhetherAnswersNo (no _)  = refl

------------------------------------------------------------------------
-- C-82 the same product with members of bounded height

Bounded : ℕ → Type ℓ-zero
Bounded b = (n : ℕ) → K b

Bounded∙ : ℕ → Pointed ℓ-zero
Bounded∙ b = Πpt ℕ (λ _ → K b , x₀ b)

boundedLevel : (b : ℕ) → isOfHLevel (3 + b) (Bounded b)
boundedLevel b = isOfHLevelΠ (3 + b) (λ _ → hLevelEM ℤAbGroup (suc b))

boundedNot2+ : (b : ℕ) → ¬ isOfHLevel (2 + b) (Bounded b)
boundedNot2+ b h = secAtBase≢triv b (funExt⁻ constIsTrivial 0)
  where
  contrLoops : isContr (typ ((Ω^ (suc b)) (Bounded∙ b)))
  contrLoops = hLevelΩ^ (suc b) (pt (Bounded∙ b)) h
  contrFactors : isContr ((n : ℕ) → LoopFactor b b)
  contrFactors = subst (λ A → isContr (typ A)) (Ω^Πpt (suc b) ℕ (λ _ → K b , x₀ b)) contrLoops
  constIsTrivial : (λ (_ : ℕ) → sec b (x₀ b)) ≡ (λ _ → pt ((Ω^ (suc b)) (K b , x₀ b)))
  constIsTrivial = isContr→isProp contrFactors _ _

boundedNotBelow : (b i : ℕ) → i < suc b → ¬ isOfHLevel (suc (1 + i)) (Bounded b)
boundedNotBelow b i i<sb hi = boundedNot2+ b (levelUp (suc-≤-suc i<sb) hi)

boundedStopsAt : (b : ℕ) (judge : Judge (Bounded b))
               → runFor (suc b) (question (Bounded b) judge) ≡ just (suc (suc b))
boundedStopsAt b judge =
  Questioning.exactHalt (Bounded b) judge (suc b) 1 (boundedNotBelow b) (boundedLevel b)

boundedSilentBefore : (b : ℕ) (judge : Judge (Bounded b)) (i : ℕ) → i < suc b
                    → runFor i (question (Bounded b) judge) ≡ nothing
boundedSilentBefore b judge i i<sb =
  Questioning.silentUpTo (Bounded b) judge i 1 (λ j j≤i → boundedNotBelow b j (≤<-trans j≤i i<sb))

judgeBounded : (b : ℕ) → Judge (Bounded b)
judgeBounded b k = decide (splitℕ-≤ k (suc b))
  where
  decide : (k ≤ suc b) ⊎ (suc b < k) → Dec (isOfHLevel (suc k) (Bounded b))
  decide (inl k≤sb) = no (λ h → boundedNot2+ b (levelUp (suc-≤-suc k≤sb) h))
  decide (inr sb<k) = yes (levelUp (suc-≤-suc sb<k) (boundedLevel b))

-- b = 0: the product of copies of K 0 is silent at stage 1 and stops at stage 2
boundedZeroStopsAtTwo : (judge : Judge (Bounded 0))
                      → (runFor 0 (question (Bounded 0) judge) ≡ nothing)
                      × (runFor 1 (question (Bounded 0) judge) ≡ just 2)
boundedZeroStopsAtTwo judge = boundedSilentBefore 0 judge 0 ≤-refl , boundedStopsAt 0 judge
