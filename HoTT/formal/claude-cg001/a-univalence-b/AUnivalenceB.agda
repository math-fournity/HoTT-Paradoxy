{-# OPTIONS --safe --cubical --guardedness #-}
{-
  B has two causes and one defendant: A and univalence together make the
  questioning never stop; drop either and it stops (Claude Code, desktop
  session 95a1a81b (012-Opus), 2026-10-15; goal package CG-010, handoff item
  H2; worktree claude/012-opus-w8).

  proof id : MP-CG001-A-UNIVALENCE-B-001
  claims   : CG001-C-430 (full statement in CLAIM.md)

  The research sponsor ruled on 2026-10-15 (ruling D4): "ZFC-1 causes B"
  means the same act A on both sides, plus the theorem "A and univalence
  imply B; drop either and it stops"; the defendant is A, the ready-made
  collection, and univalence is a cause but not the defendant.  The four
  parts were proved separately before (C-75/C-78 universe, C-79 gatherings,
  C-80 the fact world in Lean, C-81/C-82 product, C-83 truncation).  This
  file states the theorem once, for every collection, and checks it in one
  unit.

  A collection is a type of codes with the member each code names.

    Univalent      sameness is structure: two codes are the same in exactly
                   the ways their members are equivalent;
    SamenessIsFact sameness of codes is a fact: the codes form a set;
    AllHeights     A, every height handed over at once: for every n the
                   collection already holds a member whose (1+n)-fold
                   sameness is nontrivial, coherently at every point;
    HeightsBoundedBy k   every member is of h-level k.

  (1) both causes: Univalent and AllHeights give no finite h-level, so for
      every judge the questioning program of C-77 is `never`;
  (2) drop A, keep univalence: bounded heights give a finite h-level one
      above the bound, so the questioning halts;
  (3) drop univalence, keep A: if the sameness of codes is a fact, the
      questioning stops at the first question, whatever the members are;
  (4) read backwards: a `never` questioning on a univalent collection has
      unbounded heights, and a `never` questioning has no fact sameness;
  (5) witnesses that each clause is met: the universe (both causes; C-75 is
      re-derived through (1)); the gathering of the (1+n)-types (univalence
      without A; it stops exactly at question 1+n, C-79(b)); the numbered
      Eilenberg-MacLane collection, codes ℕ and members EM ℤ (1+n) (A
      without univalence; it stops at question 1, and through (1) it is not
      univalent);
  (6) not univalent is not enough: the paired collection, codes Type × Bool
      and members the first part, holds every height and is not univalent,
      yet its questioning never stops, because its codes still carry the
      universe's structured sameness.  So (3) needs the sameness to become a
      fact, not merely univalence to fail.

  Bridge labels (A, defendant, cause, collection, height) prove no historical
  or physical fact; which ingredient is non-real is the sponsor's ruling,
  not a theorem.
-}
module AUnivalenceB where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Pointed
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Nat.Order using (_<_)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Bool using (Bool; true; false; true≢false)
open import Cubical.Data.Unit using (Unit)
open import Cubical.Data.Sigma
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)
open import Cubical.Homotopy.Loopspace using (Ω; Ω^_; Ω^≃∙)

open import PedometerSemantics using (Delay; never; runFor)
open import UniverseHasNoLevel
  using (Ω^suc; hLevelΩ^; Πpt; ΩΠpt; Ω^Πpt; ΩEquiv≡ΩFun; K; sec; secNontrivial)
open import QuestioningDelay
  using (Judge; question; module Questioning; judgeℕ; Gathering;
         gatheringStopsAt; gatheringSilentBefore; gatheringJudge)

private
  variable
    ℓc ℓe : Level

------------------------------------------------------------------------
-- Collections and the two causes

record Collection (ℓc ℓe : Level) : Type (ℓ-max (ℓ-suc ℓc) (ℓ-suc ℓe)) where
  field
    Code : Type ℓc
    El   : Code → Type ℓe

open Collection

codeToEquiv : (C : Collection ℓc ℓe) {a b : Code C} → a ≡ b → El C a ≃ El C b
codeToEquiv C p = pathToEquiv (cong (El C) p)

-- Sameness is structure.
Univalent : Collection ℓc ℓe → Type (ℓ-max ℓc ℓe)
Univalent C = (a b : Code C) → isEquiv (codeToEquiv C {a} {b})

-- Sameness of codes is a fact.
SamenessIsFact : Collection ℓc ℓe → Type ℓc
SamenessIsFact C = isSet (Code C)

trivialLoops : (X : Type ℓe) (n : ℕ) (x : X) → typ ((Ω^ (suc n)) (X , x))
trivialLoops X n x = pt ((Ω^ (suc n)) (X , x))

-- A: every height handed over at once.
AllHeights : Collection ℓc ℓe → Type (ℓ-max ℓc ℓe)
AllHeights C =
  (n : ℕ) → Σ[ a ∈ Code C ]
              Σ[ s ∈ ((x : El C a) → typ ((Ω^ (suc n)) (El C a , x))) ]
                ¬ (s ≡ trivialLoops (El C a) n)

HeightsBoundedBy : ℕ → Collection ℓc ℓe → Type (ℓ-max ℓc ℓe)
HeightsBoundedBy k C = (a : Code C) → isOfHLevel k (El C a)

------------------------------------------------------------------------
-- (1), (2): a univalent collection

module UnivalentCollection (C : Collection ℓc ℓe) (univ : Univalent C) where

  ΩCode≃∙ : (a : Code C) → Ω (Code C , a) ≃∙ ((El C a ≃ El C a) , idEquiv (El C a))
  ΩCode≃∙ a = (codeToEquiv C {a} {a} , univ a a) , pathToEquivRefl

  -- Univalence lifts the sameness inside a member one level up, into the
  -- sameness of the collection.
  localGlobal : (n : ℕ) (a : Code C)
    → typ ((Ω^ (suc (suc n))) (Code C , a)) ≃ ((x : El C a) → typ ((Ω^ (suc n)) (El C a , x)))
  localGlobal n a =
    compEquiv (pathToEquiv (cong typ (Ω^suc (suc n) (Code C , a))))
    (compEquiv (fst (Ω^≃∙ (suc n) (ΩCode≃∙ a)))
    (pathToEquiv (cong typ
       (Ω^suc n ((X ≃ X) , idEquiv X)
       ∙ cong (Ω^ n) (ΩEquiv≡ΩFun X ∙ ΩΠpt X (λ x → X , x))
       ∙ Ω^Πpt n X (λ x → Ω (X , x))
       ∙ cong (Πpt X) (funExt λ x → sym (Ω^suc n (X , x)))))))
    where
    X : Type ℓe
    X = El C a

  -- (1) A and univalence: no finite level.
  noFiniteLevel : AllHeights C → (m : ℕ) → ¬ isOfHLevel m (Code C)
  noFiniteLevel ah m h =
    nontriv (isContr→isProp (isOfHLevelRespectEquiv 0 (localGlobal m a) c) s (trivialLoops (El C a) m))
    where
    a : Code C
    a = fst (ah m)
    s : (x : El C a) → typ ((Ω^ (suc m)) (El C a , x))
    s = fst (snd (ah m))
    nontriv : ¬ (s ≡ trivialLoops (El C a) m)
    nontriv = snd (snd (ah m))
    c : isContr (typ ((Ω^ (suc (suc m))) (Code C , a)))
    c = hLevelΩ^ (suc (suc m)) a (isOfHLevelPlus 3 h)

  neverWithBoth : AllHeights C → (judge : Judge (Code C)) → question (Code C) judge ≡ never
  neverWithBoth ah judge = Questioning.noLevelToNever (Code C) judge (noFiniteLevel ah)

  -- (2) univalence without A: bounded heights settle one level above the bound.
  boundedSettles : (k : ℕ) → HeightsBoundedBy k C → isOfHLevel (suc k) (Code C)
  boundedSettles k hb = isOfHLevelPath'⁻ k λ a b →
    isOfHLevelRespectEquiv k (invEquiv (codeToEquiv C {a} {b} , univ a b))
      (isOfHLevel≃ k (hb a) (hb b))

  haltsWithBound : (k : ℕ) → HeightsBoundedBy k C
                 → (judge : Judge (Code C)) → Questioning.Halts (Code C) judge
  haltsWithBound k hb judge =
    Questioning.levelToHalts (Code C) judge (suc k , boundedSettles k hb)

open UnivalentCollection

------------------------------------------------------------------------
-- (3) A without univalence: fact sameness stops at the first question

factStopsAtOne : (C : Collection ℓc ℓe) → SamenessIsFact C
               → (judge : Judge (Code C)) → runFor 0 (question (Code C) judge) ≡ just 1
factStopsAtOne C fact judge = Questioning.settledAt (Code C) judge 0 1 fact

------------------------------------------------------------------------
-- (4) read backwards: a questioning that never stops needs both causes

neverNeedsUnbounded : (C : Collection ℓc ℓe) → Univalent C → (judge : Judge (Code C))
  → question (Code C) judge ≡ never → (k : ℕ) → ¬ HeightsBoundedBy k C
neverNeedsUnbounded C univ judge p k hb =
  Questioning.neverToNoLevel (Code C) judge p (suc k) (boundedSettles C univ k hb)

neverNeedsStructure : (C : Collection ℓc ℓe) (judge : Judge (Code C))
  → question (Code C) judge ≡ never → ¬ SamenessIsFact C
neverNeedsStructure C judge p fact = Questioning.neverToNoLevel (Code C) judge p 2 fact

------------------------------------------------------------------------
-- (5a) the universe: both causes

universe : Collection (ℓ-suc ℓ-zero) ℓ-zero
Code universe = Type ℓ-zero
El universe X = X

universeUnivalent : Univalent universe
universeUnivalent A B = isEquivPathToEquiv

universeAllHeights : AllHeights universe
universeAllHeights n = K n , sec n , secNontrivial n

universeNoLevel : (m : ℕ) → ¬ isOfHLevel m (Type ℓ-zero)
universeNoLevel = noFiniteLevel universe universeUnivalent universeAllHeights

universeNever : (judge : Judge (Type ℓ-zero)) → question (Type ℓ-zero) judge ≡ never
universeNever = neverWithBoth universe universeUnivalent universeAllHeights

judgeViaB : Judge (Type ℓ-zero)
judgeViaB k = no (universeNoLevel (suc k))

universeKernel1000 : runFor 1000 (question (Type ℓ-zero) judgeViaB) ≡ nothing
universeKernel1000 = refl

------------------------------------------------------------------------
-- (5b) the gathering of the (1+n)-types: univalence without A

gathering : ℕ → Collection (ℓ-suc ℓ-zero) ℓ-zero
Code (gathering n) = TypeOfHLevel ℓ-zero (suc n)
El (gathering n) = fst

gatheringUnivalent : (n : ℕ) → Univalent (gathering n)
gatheringUnivalent n A B =
  snd (compEquiv ((λ p → cong fst p) ,
                  isEmbeddingFstΣProp (λ X → isPropIsOfHLevel (suc n)) {u = A} {v = B})
                 univalence)

gatheringBounded : (n : ℕ) → HeightsBoundedBy (suc n) (gathering n)
gatheringBounded n A = snd A

gatheringSettles : (n : ℕ) → isOfHLevel (suc (suc n)) (Gathering n)
gatheringSettles n = boundedSettles (gathering n) (gatheringUnivalent n) (suc n) (gatheringBounded n)

gatheringHalts : (n : ℕ) (judge : Judge (Gathering n)) → Questioning.Halts (Gathering n) judge
gatheringHalts n = haltsWithBound (gathering n) (gatheringUnivalent n) (suc n) (gatheringBounded n)

gatheringKernelSets : runFor 1 (question (Gathering 1) (gatheringJudge 1)) ≡ just 2
gatheringKernelSets = refl

------------------------------------------------------------------------
-- (5c) the numbered Eilenberg-MacLane collection: A without univalence

numbered : Collection ℓ-zero ℓ-zero
Code numbered = ℕ
El numbered = K

numberedAllHeights : AllHeights numbered
numberedAllHeights n = n , sec n , secNontrivial n

numberedFact : SamenessIsFact numbered
numberedFact = isSetℕ

numberedStopsAtOne : (judge : Judge ℕ) → runFor 0 (question ℕ judge) ≡ just 1
numberedStopsAtOne = factStopsAtOne numbered numberedFact

numberedNotUnivalent : ¬ Univalent numbered
numberedNotUnivalent univ = noFiniteLevel numbered univ numberedAllHeights 2 isSetℕ

numberedKernel : runFor 0 (question ℕ judgeℕ) ≡ just 1
numberedKernel = refl

------------------------------------------------------------------------
-- (6) not univalent is not enough: the sameness must become a fact

paired : Collection (ℓ-suc ℓ-zero) ℓ-zero
Code paired = Type ℓ-zero × Bool
El paired = fst

pairedAllHeights : AllHeights paired
pairedAllHeights n = (K n , true) , sec n , secNontrivial n

pairedNotUnivalent : ¬ Univalent paired
pairedNotUnivalent univ =
  true≢false (cong snd (invEq (codeToEquiv paired {Unit , true} {Unit , false} ,
                               univ (Unit , true) (Unit , false))
                              (idEquiv Unit)))

pairedNoLevel : (m : ℕ) → ¬ isOfHLevel m (Code paired)
pairedNoLevel m h = universeNoLevel m (isOfHLevelRetract m (λ X → X , true) fst (λ X → refl) h)

pairedNever : (judge : Judge (Code paired)) → question (Code paired) judge ≡ never
pairedNever judge = Questioning.noLevelToNever (Code paired) judge pairedNoLevel

------------------------------------------------------------------------
-- The claim in one type

qual-C430 :
  -- (1) both causes: never
  ((C : Collection (ℓ-suc ℓ-zero) ℓ-zero) → Univalent C → AllHeights C →
     ((m : ℕ) → ¬ isOfHLevel m (Code C)) ×
     ((judge : Judge (Code C)) → question (Code C) judge ≡ never)) ×
  -- (2) drop A: halts
  ((C : Collection (ℓ-suc ℓ-zero) ℓ-zero) (k : ℕ) → Univalent C → HeightsBoundedBy k C →
     isOfHLevel (suc k) (Code C) ×
     ((judge : Judge (Code C)) → Questioning.Halts (Code C) judge)) ×
  -- (3) drop univalence: first question
  ((C : Collection ℓ-zero ℓ-zero) → SamenessIsFact C →
     (judge : Judge (Code C)) → runFor 0 (question (Code C) judge) ≡ just 1) ×
  -- (4) read backwards
  ((C : Collection (ℓ-suc ℓ-zero) ℓ-zero) → Univalent C → (judge : Judge (Code C)) →
     question (Code C) judge ≡ never →
     ((k : ℕ) → ¬ HeightsBoundedBy k C) × (¬ SamenessIsFact C)) ×
  -- (5a) the universe meets both causes and never stops
  (Univalent universe × AllHeights universe ×
     ((judge : Judge (Type ℓ-zero)) → question (Type ℓ-zero) judge ≡ never)) ×
  -- (5b) the gathering of the (1+n)-types: univalent, bounded, stops exactly at question 1+n
  ((n : ℕ) → Univalent (gathering n) × HeightsBoundedBy (suc n) (gathering n) ×
     ((judge : Judge (Gathering n)) →
        (runFor n (question (Gathering n) judge) ≡ just (suc n)) ×
        ((i : ℕ) → i < n → runFor i (question (Gathering n) judge) ≡ nothing))) ×
  -- (5c) the numbered collection: all heights, fact sameness, stops at question 1, not univalent
  (AllHeights numbered × SamenessIsFact numbered ×
     ((judge : Judge ℕ) → runFor 0 (question ℕ judge) ≡ just 1) × (¬ Univalent numbered)) ×
  -- (6) the paired collection: all heights, not univalent, yet never
  (AllHeights paired × (¬ Univalent paired) ×
     ((judge : Judge (Code paired)) → question (Code paired) judge ≡ never))
qual-C430 =
  (λ C univ ah → noFiniteLevel C univ ah , neverWithBoth C univ ah) ,
  (λ C k univ hb → boundedSettles C univ k hb , haltsWithBound C univ k hb) ,
  factStopsAtOne ,
  (λ C univ judge p → neverNeedsUnbounded C univ judge p , neverNeedsStructure C judge p) ,
  (universeUnivalent , universeAllHeights , universeNever) ,
  (λ n → gatheringUnivalent n , gatheringBounded n ,
         λ judge → gatheringStopsAt n judge , gatheringSilentBefore n judge) ,
  (numberedAllHeights , numberedFact , numberedStopsAtOne , numberedNotUnivalent) ,
  (pairedAllHeights , pairedNotUnivalent , pairedNever)
