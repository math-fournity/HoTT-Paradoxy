{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The questioning process Q as a program with a judge (Claude, cloud session
  01FJANnV, 2026-09-30).

  proof id : MP-CG001-QUESTIONING-DELAY-001
  claims   : CG001-C-77, CG001-C-78, CG001-C-79 (full statements in CLAIM.md)

  C-75 proved, for every m, that Type ℓ-zero is not of h-level m.  That the
  questioning of the universe "never halts" was then a meta-level inference:
  the process Q was pseudo-code outside the theory (audit paper 02, sections
  3.1 and 5).  This file writes Q inside the theory, as a program in the
  delay monad of C-55 (the type is imported, not restated), with a judge that
  answers, at every stage k, whether the catalogue C is settled at h-level
  k+1 (isOfHLevel (k+1) C), with a proof either way:

      start at stage 1 (is C a set?); at stage k ask the judge whether C is
      settled at h-level k+1; on yes, stop and return k; on no, take one
      step and go to stage k+1.

  "Step 1", "step 2" in the audit paper are stages 1 and 2; stopping at
  stage k is the run returning k with fuel k-1 when Q starts at stage 1.

  C-77 (the program, for every catalogue C and every judge)
       (a) the fuel equations of the run, and the same equations stated with
           the fact instead of the judge (they depend only on whether C is
           settled at that h-level, not on the judge);
       (b) a returned value is sound: if a run returns j, then C is settled
           at h-level j+1;
       (c) Q halts if and only if C is settled at some finite h-level, and
           Q ≡ never if and only if C is settled at no finite h-level;
       (d) exact halting time: if C is not settled at h-levels k+1 .. k+n
           and is settled at h-level k+n+1, the run from stage k with fuel n
           returns k+n; if C is not settled at h-levels k+1 .. k+n+1, the
           run from stage k with fuel n returns nothing;
       (e) for a catalogue in the lowest universe, Q is the unbounded search
           of C-55 (StopProgram) with stop condition "settled at h-level
           k+1", started at 1.
  C-78 (the universe)
       (a) for every judge, Q on Type ℓ-zero is equal to never: every run,
           however long, returns nothing, and Q never answers;
       (b) a judge exists (judgeU answers no at every stage, each no carrying
           the proof of C-75), and every judge is equal to it (the type of
           judges is a proposition);
       (c) with judgeU the kernel itself runs Q with fuel 1000 and gets
           nothing (refl);
       (d) contrast: the program that asks the other question, "is C settled
           at some h-level at all?", stops at once, and on the universe it
           answers no, for every way of deciding that question.
  C-79 (the same program on catalogues whose members have bounded height)
       (a) ℕ and Bool: for every judge, Q stops at stage 1 and returns 1;
       (b) the catalogue of the types of h-level 1+n (TypeOfHLevel ℓ-zero
           (1+n), called Gathering n below): for every judge, the run with
           fuel n returns 1+n, and every smaller fuel returns nothing, so Q
           stops at stage 1+n; the catalogue of propositions stops at stage
           1 and the catalogue of sets at stage 2; a judge exists for every
           n.

  Bridge labels (catalogue, judge, questioning, step) prove no philosophical
  fact: "asking whether a domain element exists is this process" is the
  interpretation bridge of audit paper 02 (its question P1), not a theorem.
-}
module QuestioningDelay where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_; znots)
open import Cubical.Data.Nat.Properties using (+-zero; +-suc; +-comm; isSetℕ)
open import Cubical.Data.Nat.Order
  using (_≤_; _<_; zero-≤; suc-≤-suc; ≤-refl; ≤<-trans; splitℕ-≤)
open import Cubical.Data.Bool using (Bool; true; false; true≢false)
open import Cubical.Data.Bool.Properties using (isSetBool)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Maybe.Properties using (just-inj; ¬nothing≡just; ¬just≡nothing)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no; isPropDec)

open import PedometerSemantics
  using (Delay; Delay'; now; later; never; evalFor; runFor; module StopProgram)
open import DelayMonad using (return; divergesRunsNothing)
open import UniverseHasNoLevel using (universeHasNoLevel; gatheringNeverSettled)

open Delay

private
  variable
    ℓ : Level

------------------------------------------------------------------------
-- the judge and the program

-- A judge answers, at every stage k, whether C is settled at h-level k+1,
-- with a proof either way.
Judge : Type ℓ → Type ℓ
Judge C = (k : ℕ) → Dec (isOfHLevel (suc k) C)

module Questioning {ℓ : Level} (C : Type ℓ) (judge : Judge C) where

  mutual
    askFrom : ℕ → Delay ℕ
    askFrom k .force = answer k (judge k)

    answer : (k : ℕ) → Dec (isOfHLevel (suc k) C) → Delay' ℕ
    answer k (yes _) = now k
    answer k (no _)  = later (askFrom (suc k))

  Q : Delay ℕ
  Q = askFrom 1

  ----------------------------------------------------------------------
  -- C-77 (a) the fuel equations

  runYes : (n k : ℕ) (h : isOfHLevel (suc k) C) → evalFor n (answer k (yes h)) ≡ just k
  runYes n k h = refl

  runNoZero : (k : ℕ) (nh : ¬ isOfHLevel (suc k) C) → evalFor zero (answer k (no nh)) ≡ nothing
  runNoZero k nh = refl

  runNoSuc : (n k : ℕ) (nh : ¬ isOfHLevel (suc k) C)
           → evalFor (suc n) (answer k (no nh)) ≡ runFor n (askFrom (suc k))
  runNoSuc n k nh = refl

  -- the same equations with the fact in place of the judge's answer

  settledAt : (n k : ℕ) → isOfHLevel (suc k) C → runFor n (askFrom k) ≡ just k
  settledAt n k h = go (judge k)
    where
    go : (d : Dec (isOfHLevel (suc k) C)) → evalFor n (answer k d) ≡ just k
    go (yes _) = refl
    go (no nh) = ⊥.rec (nh h)

  notSettledAtZero : (k : ℕ) → ¬ isOfHLevel (suc k) C → runFor zero (askFrom k) ≡ nothing
  notSettledAtZero k nh = go (judge k)
    where
    go : (d : Dec (isOfHLevel (suc k) C)) → evalFor zero (answer k d) ≡ nothing
    go (yes h) = ⊥.rec (nh h)
    go (no _)  = refl

  notSettledAt : (n k : ℕ) → ¬ isOfHLevel (suc k) C
               → runFor (suc n) (askFrom k) ≡ runFor n (askFrom (suc k))
  notSettledAt n k nh = go (judge k)
    where
    go : (d : Dec (isOfHLevel (suc k) C)) → evalFor (suc n) (answer k d) ≡ runFor n (askFrom (suc k))
    go (yes h) = ⊥.rec (nh h)
    go (no _)  = refl

  ----------------------------------------------------------------------
  -- C-77 (b) a returned value is sound

  mutual
    sound : (n k j : ℕ) → runFor n (askFrom k) ≡ just j → isOfHLevel (suc j) C
    sound n k j p = soundAnswer n k j (judge k) p

    soundAnswer : (n k j : ℕ) (d : Dec (isOfHLevel (suc k) C))
                → evalFor n (answer k d) ≡ just j → isOfHLevel (suc j) C
    soundAnswer n       k j (yes h) p = subst (λ m → isOfHLevel (suc m) C) (just-inj k j p) h
    soundAnswer zero    k j (no _)  p = ⊥.rec (¬nothing≡just p)
    soundAnswer (suc n) k j (no _)  p = sound n (suc k) j p

  ----------------------------------------------------------------------
  -- C-77 (c) halting is exactly "settled at some finite h-level"

  Halts : Type
  Halts = Σ[ n ∈ ℕ ] Σ[ j ∈ ℕ ] runFor n Q ≡ just j

  HasLevel : Type ℓ
  HasLevel = Σ[ m ∈ ℕ ] isOfHLevel m C

  mutual
    haltsWithin : (n k : ℕ) → isOfHLevel (suc (n + k)) C
                → Σ[ j ∈ ℕ ] runFor n (askFrom k) ≡ just j
    haltsWithin n k h = haltsAnswer n k h (judge k)

    haltsAnswer : (n k : ℕ) → isOfHLevel (suc (n + k)) C → (d : Dec (isOfHLevel (suc k) C))
                → Σ[ j ∈ ℕ ] evalFor n (answer k d) ≡ just j
    haltsAnswer n       k h (yes _) = k , refl
    haltsAnswer zero    k h (no nh) = ⊥.rec (nh h)
    haltsAnswer (suc n) k h (no _)  =
      haltsWithin n (suc k) (subst (λ m → isOfHLevel (suc m) C) (sym (+-suc n k)) h)

  haltsToLevel : Halts → HasLevel
  haltsToLevel (n , j , p) = suc j , sound n 1 j p

  levelToHalts : HasLevel → Halts
  levelToHalts (m , h) =
    m , haltsWithin m 1 (subst (λ l → isOfHLevel (suc l) C) (+-comm 1 m) (isOfHLevelPlus 2 h))

  module NoLevel (noLevel : (m : ℕ) → ¬ isOfHLevel m C) where

    mutual
      askFromIsNever : (k : ℕ) → askFrom k ≡ never
      askFromIsNever k i .force = answerIsNever k (judge k) i

      answerIsNever : (k : ℕ) (d : Dec (isOfHLevel (suc k) C)) → answer k d ≡ later never
      answerIsNever k (yes h)  = ⊥.rec (noLevel (suc k) h)
      answerIsNever k (no _) i = later (askFromIsNever (suc k) i)

    QIsNever : Q ≡ never
    QIsNever = askFromIsNever 1

    QRunsNothing : (n : ℕ) → runFor n Q ≡ nothing
    QRunsNothing = divergesRunsNothing Q QIsNever

    QNeverAnswers : ¬ Halts
    QNeverAnswers (n , j , p) = ¬just≡nothing (sym p ∙ QRunsNothing n)

  noLevelToNever : ((m : ℕ) → ¬ isOfHLevel m C) → Q ≡ never
  noLevelToNever noLevel = NoLevel.QIsNever noLevel

  neverToNoLevel : Q ≡ never → (m : ℕ) → ¬ isOfHLevel m C
  neverToNoLevel p m h = ¬just≡nothing (sym (snd (snd w)) ∙ divergesRunsNothing Q p (fst w))
    where
    w : Halts
    w = levelToHalts (m , h)

  ----------------------------------------------------------------------
  -- C-77 (d) exact halting time

  exactHalt : (n k : ℕ)
            → ((i : ℕ) → i < n → ¬ isOfHLevel (suc (k + i)) C)
            → isOfHLevel (suc (k + n)) C
            → runFor n (askFrom k) ≡ just (k + n)
  exactHalt zero k below h =
    settledAt zero k (subst (λ m → isOfHLevel (suc m) C) (+-zero k) h)
    ∙ cong just (sym (+-zero k))
  exactHalt (suc n) k below h =
    notSettledAt n k
      (λ hk → below 0 (suc-≤-suc zero-≤) (subst (λ m → isOfHLevel (suc m) C) (sym (+-zero k)) hk))
    ∙ exactHalt n (suc k)
        (λ i i<n hi → below (suc i) (suc-≤-suc i<n)
                        (subst (λ m → isOfHLevel (suc m) C) (sym (+-suc k i)) hi))
        (subst (λ m → isOfHLevel (suc m) C) (+-suc k n) h)
    ∙ cong just (sym (+-suc k n))

  silentUpTo : (n k : ℕ)
             → ((i : ℕ) → i ≤ n → ¬ isOfHLevel (suc (k + i)) C)
             → runFor n (askFrom k) ≡ nothing
  silentUpTo zero k below =
    notSettledAtZero k
      (λ hk → below 0 ≤-refl (subst (λ m → isOfHLevel (suc m) C) (sym (+-zero k)) hk))
  silentUpTo (suc n) k below =
    notSettledAt n k
      (λ hk → below 0 zero-≤ (subst (λ m → isOfHLevel (suc m) C) (sym (+-zero k)) hk))
    ∙ silentUpTo n (suc k)
        (λ i i≤n hi → below (suc i) (suc-≤-suc i≤n)
                        (subst (λ m → isOfHLevel (suc m) C) (sym (+-suc k i)) hi))

question : (C : Type ℓ) → Judge C → Delay ℕ
question C judge = Questioning.Q C judge

------------------------------------------------------------------------
-- C-77 (e) for a catalogue in the lowest universe, Q is the search of C-55

module SameAsC55 (C : Type) (judge : Judge C) where

  open Questioning C judge using (askFrom; answer; Q)
  open StopProgram (λ k → isOfHLevel (suc k) C) judge using (searchFrom; step)

  mutual
    askIsSearch : (k : ℕ) → askFrom k ≡ searchFrom k
    askIsSearch k i .force = answerIsStep k (judge k) i

    answerIsStep : (k : ℕ) (d : Dec (isOfHLevel (suc k) C)) → answer k d ≡ step k d
    answerIsStep k (yes _)  = refl
    answerIsStep k (no _) i = later (askIsSearch (suc k) i)

  QIsSearchFromOne : Q ≡ searchFrom 1
  QIsSearchFromOne = askIsSearch 1

------------------------------------------------------------------------
-- C-78 the universe

judgeU : Judge (Type ℓ-zero)
judgeU k = no (universeHasNoLevel (suc k))

judgesAreEqual : (C : Type ℓ) → isProp (Judge C)
judgesAreEqual C = isPropΠ (λ k → isPropDec (isPropIsOfHLevel (suc k)))

everyJudgeIsJudgeU : (judge : Judge (Type ℓ-zero)) → judge ≡ judgeU
everyJudgeIsJudgeU judge = judgesAreEqual (Type ℓ-zero) judge judgeU

universeQuestioningIsNever : (judge : Judge (Type ℓ-zero)) → question (Type ℓ-zero) judge ≡ never
universeQuestioningIsNever judge = Questioning.noLevelToNever (Type ℓ-zero) judge universeHasNoLevel

universeQuestioningRunsNothing : (judge : Judge (Type ℓ-zero)) (n : ℕ)
                               → runFor n (question (Type ℓ-zero) judge) ≡ nothing
universeQuestioningRunsNothing judge =
  Questioning.NoLevel.QRunsNothing (Type ℓ-zero) judge universeHasNoLevel

universeQuestioningNeverAnswers : (judge : Judge (Type ℓ-zero))
                                → ¬ Questioning.Halts (Type ℓ-zero) judge
universeQuestioningNeverAnswers judge =
  Questioning.NoLevel.QNeverAnswers (Type ℓ-zero) judge universeHasNoLevel

-- the kernel runs the program with judgeU and fuel 1000
kernelRuns1000 : runFor 1000 (question (Type ℓ-zero) judgeU) ≡ nothing
kernelRuns1000 = refl

-- contrast: the other question, "is C settled at some h-level at all?"
whetherSettled : (C : Type ℓ) → Dec (Σ[ m ∈ ℕ ] isOfHLevel m C) → Delay Bool
whetherSettled C (yes _) = return true
whetherSettled C (no _)  = return false

universeWhetherAnswersNo : (d : Dec (Σ[ m ∈ ℕ ] isOfHLevel m (Type ℓ-zero)))
                         → runFor 0 (whetherSettled (Type ℓ-zero) d) ≡ just false
universeWhetherAnswersNo (yes w) = ⊥.rec (universeHasNoLevel (fst w) (snd w))
universeWhetherAnswersNo (no _)  = refl

------------------------------------------------------------------------
-- C-79 catalogues whose members have bounded height

judgeℕ : Judge ℕ
judgeℕ zero    = no (λ h → znots (h 0 1))
judgeℕ (suc k) = yes (isOfHLevelPlus' {n = k} 2 isSetℕ)

naturalsStopAtOne : (judge : Judge ℕ) → runFor 0 (question ℕ judge) ≡ just 1
naturalsStopAtOne judge = Questioning.settledAt ℕ judge 0 1 isSetℕ

judgeBool : Judge Bool
judgeBool zero    = no (λ h → true≢false (h true false))
judgeBool (suc k) = yes (isOfHLevelPlus' {n = k} 2 isSetBool)

boolsStopAtOne : (judge : Judge Bool) → runFor 0 (question Bool judge) ≡ just 1
boolsStopAtOne judge = Questioning.settledAt Bool judge 0 1 isSetBool

-- the catalogue of the types of h-level 1+n
Gathering : ℕ → Type (ℓ-suc ℓ-zero)
Gathering n = TypeOfHLevel ℓ-zero (suc n)

levelUp : {A : Type ℓ} {m l : ℕ} → m ≤ l → isOfHLevel m A → isOfHLevel l A
levelUp {A = A} (d , p) h = subst (λ l → isOfHLevel l A) p (isOfHLevelPlus d h)

gatheringNotBelow : (n i : ℕ) → i < n → ¬ isOfHLevel (suc (1 + i)) (Gathering n)
gatheringNotBelow n i (d , p) h =
  gatheringNeverSettled n (levelUp (d , +-suc d (suc i) ∙ cong suc p) h)

gatheringStopsAt : (n : ℕ) (judge : Judge (Gathering n))
                 → runFor n (question (Gathering n) judge) ≡ just (suc n)
gatheringStopsAt n judge =
  Questioning.exactHalt (Gathering n) judge n 1 (gatheringNotBelow n) (isOfHLevelTypeOfHLevel (suc n))

gatheringSilentBefore : (n : ℕ) (judge : Judge (Gathering n)) (i : ℕ) → i < n
                      → runFor i (question (Gathering n) judge) ≡ nothing
gatheringSilentBefore n judge i i<n =
  Questioning.silentUpTo (Gathering n) judge i 1 (λ j j≤i → gatheringNotBelow n j (≤<-trans j≤i i<n))

gatheringJudge : (n : ℕ) → Judge (Gathering n)
gatheringJudge n k = decide (splitℕ-≤ k n)
  where
  decide : (k ≤ n) ⊎ (n < k) → Dec (isOfHLevel (suc k) (Gathering n))
  decide (inl k≤n) = no (λ h → gatheringNeverSettled n (levelUp (suc-≤-suc k≤n) h))
  decide (inr n<k) = yes (levelUp (suc-≤-suc n<k) (isOfHLevelTypeOfHLevel (suc n)))

propsStopAtOne : (judge : Judge (hProp ℓ-zero)) → runFor 0 (question (hProp ℓ-zero) judge) ≡ just 1
propsStopAtOne = gatheringStopsAt 0

setsStopAtTwo : (judge : Judge (hSet ℓ-zero))
              → (runFor 0 (question (hSet ℓ-zero) judge) ≡ nothing)
              × (runFor 1 (question (hSet ℓ-zero) judge) ≡ just 2)
setsStopAtTwo judge = gatheringSilentBefore 1 judge 0 ≤-refl , gatheringStopsAt 1 judge
