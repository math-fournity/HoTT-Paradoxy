{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The two choices in HoTT's own kernel, next to B (Claude Code, desktop
  session 95a1a81b (012-Opus), 2026-10-15; goal package CG-010, unit R4;
  worktree claude/012-opus-w8).

  proof id : MP-CG001-TWO-CHOICES-CUBICAL-001
  claims   : CG001-C-426 (full statement in CLAIM.md)

  The research sponsor (2026-10-14): giving up the observation Q is the first
  choice, A is the second; A treats a result that only an infinite number of
  steps reaches as an already existing result and computes with it.  C-418
  (Lean, two-choices-lpo) showed that at the Sigma-1 level the two are one
  principle: LimBit (the final value of a monotone switch sequence is at hand)
  is equivalent to LPO without excluded middle.  This file

    (1) re-proves LimBit <-> LPO in Cubical Agda (--safe, nothing assumed), on
        the same omega-question type `OmegaQ` and the same `Monotone` as the
        same-Q package (C-112, C-113);
    (2) shows that settling needs monotonicity (the alternating question);
    (3) puts B into the same check unit: for every judge the questioning of
        the univalent universe is `never` (C-78, imported), and its answer
        stream is "no" at every stage, settled from stage 0 on, by proof and
        not by LPO;
    (4) the universe is at no finite h-level (C-75, imported);
    (5) every finite stage answers: the gathering of the (m+1)-types answers
        exactly at stage m+1 (C-76's two facts, imported, turned into the run
        of the same questioning program);
    (6) every finite stage has a judge, so (5) is not vacuous; the kernel runs
        the sets' gathering (stage 2) and the 4-types' gathering (stage 4),
        and the universe with fuel 100 (nothing).

  The check unit assumes no LPO: every source runs under --safe, and the
  replay verifier refuses any source that assumes an axiom.  That LPO is also
  not provable here is a metatheorem (canonicity), not proved in this file.

  Bridge labels (choice, A, B, stage, gathering) prove no historical or
  physical fact.
-}
module TwoChoicesCubical where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties using (+-comm; +-suc)
open import Cubical.Data.Nat.Order using (_≤_; _<_; zero-≤; suc-≤-suc; splitℕ-≤)
open import Cubical.Data.Bool using (Bool; true; false; _or_; true≢false; not≢const; or-zeroʳ)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)

open import PedometerSemantics using (Delay; never; evalFor; runFor)
open import QuestioningDelay using (Judge; question; universeQuestioningIsNever; judgeU)
open import UniverseHasNoLevel using (universeHasNoLevel; gatheringNeverSettled; gatheringOneUp)
open import SameQ
  using (OmegaQ; Monotone; settledFrom; alt; askQ; stepQ; decBool; decBoolYes; module FromJudge)

private
  variable
    ℓ : Level

------------------------------------------------------------------------
-- 1. the two choices: LimBit <-> LPO, without excluded middle

-- LPO: every omega-question answers "no" forever, or "yes" at some stage
LPO : Type
LPO = (q : OmegaQ) → ((k : ℕ) → q k ≡ false) ⊎ (Σ[ k ∈ ℕ ] q k ≡ true)

-- the sequence has settled at stage N: every later stage has the value of N
SettlesAt : OmegaQ → ℕ → Type
SettlesAt s N = (d : ℕ) → s (d + N) ≡ s N

-- A (switch form): every monotone switch sequence has a settling stage
LimBit : Type
LimBit = (s : OmegaQ) → Monotone s → Σ[ N ∈ ℕ ] SettlesAt s N

-- "has a yes been seen up to stage n?"
seen : OmegaQ → ℕ → Bool
seen q zero    = q zero
seen q (suc n) = seen q n or q (suc n)

seenOfTrue : (q : OmegaQ) (k : ℕ) → q k ≡ true → seen q k ≡ true
seenOfTrue q zero    p = p
seenOfTrue q (suc k) p = cong (seen q k or_) p ∙ or-zeroʳ (seen q k)

seenMono : (q : OmegaQ) → Monotone (seen q)
seenMono q n p = cong (_or q (suc n)) p

existsOfSeen : (q : OmegaQ) (n : ℕ) → seen q n ≡ true → Σ[ k ∈ ℕ ] q k ≡ true
existsOfSeen q zero    p = zero , p
existsOfSeen q (suc n) p = go (seen q n) refl
  where
  go : (b : Bool) → seen q n ≡ b → Σ[ k ∈ ℕ ] q k ≡ true
  go true  e = existsOfSeen q n e
  go false e = suc n , sym (cong (_or q (suc n)) e) ∙ p

-- A ⟹ LPO: once final values are at hand, every infinite search is decided
lpoOfLimBit : LimBit → LPO
lpoOfLimBit h q = go (seen q N) refl
  where
  N : ℕ
  N = fst (h (seen q) (seenMono q))
  settle : SettlesAt (seen q) N
  settle = snd (h (seen q) (seenMono q))
  go : (b : Bool) → seen q N ≡ b → ((k : ℕ) → q k ≡ false) ⊎ (Σ[ k ∈ ℕ ] q k ≡ true)
  go true  e = inr (existsOfSeen q N e)
  go false e = inl allNo
    where
    allNo : (k : ℕ) → q k ≡ false
    allNo k = check (q k) refl
      where
      check : (b : Bool) → q k ≡ b → q k ≡ false
      check false e' = e'
      check true  e' = ⊥.rec (true≢false (sym late ∙ settle k ∙ e))
        where
        late : seen q (k + N) ≡ true
        late = subst (λ m → seen q m ≡ true) (+-comm N k)
                     (settledFrom (seen q) (seenMono q) k (seenOfTrue q k e') N)

-- LPO ⟹ A
limBitOfLPO : LPO → LimBit
limBitOfLPO h s mono = go (h s)
  where
  go : ((k : ℕ) → s k ≡ false) ⊎ (Σ[ k ∈ ℕ ] s k ≡ true) → Σ[ N ∈ ℕ ] SettlesAt s N
  go (inl allNo)   = zero , λ d → allNo (d + zero) ∙ sym (allNo zero)
  go (inr (k , p)) = k , λ d → settledFrom s mono k p d ∙ sym p

limBit↔LPO : (LimBit → LPO) × (LPO → LimBit)
limBit↔LPO = lpoOfLimBit , limBitOfLPO

------------------------------------------------------------------------
-- 2. settling needs monotonicity: the alternating question never settles

noSettlingWithoutMonotone : ¬ ((s : OmegaQ) → Σ[ N ∈ ℕ ] SettlesAt s N)
noSettlingWithoutMonotone h = not≢const (alt (fst (h alt))) (snd (h alt) 1)

------------------------------------------------------------------------
-- 3. B without LPO: the universe's questioning never stops, and its answer
--    stream is settled ("no" at every stage) by proof

decBoolNo : {P : Type ℓ} (d : Dec P) → ¬ P → decBool d ≡ false
decBoolNo (yes p) np = ⊥.rec (np p)
decBoolNo (no _)  _  = refl

module UniverseAnswers (judge : Judge (Type ℓ-zero)) where
  open FromJudge (Type ℓ-zero) judge using (answers)

  allNo : (k : ℕ) → answers k ≡ false
  allNo k = decBoolNo (judge k) (universeHasNoLevel (suc k))

  settlesAtZero : SettlesAt answers 0
  settlesAtZero d = allNo (d + 0) ∙ sym (allNo 0)

------------------------------------------------------------------------
-- 4. each finite stage answers exactly at its stage

-- h-levels are cumulative
levelUp : {A : Type ℓ} {a b : ℕ} → a ≤ b → isOfHLevel a A → isOfHLevel b A
levelUp {A = A} (d , e) h = subst (λ m → isOfHLevel m A) e (isOfHLevelPlus d h)

-- the search answers exactly at stage k + s when the stages s .. k + s - 1
-- are "no" and stage k + s is "yes"
exactRun : (q : OmegaQ) (s k : ℕ) → ((i : ℕ) → i < k → q (i + s) ≡ false)
         → q (k + s) ≡ true → runFor k (askQ q s) ≡ just (k + s)
exactRun q s zero    below p = cong (λ b → evalFor 0 (stepQ q s b)) p
exactRun q s (suc k) below p =
  cong (λ b → evalFor (suc k) (stepQ q s b)) (below 0 (suc-≤-suc zero-≤))
  ∙ exactRun q (suc s) k below' p'
  ∙ cong just (+-suc k s)
  where
  below' : (i : ℕ) → i < k → q (i + suc s) ≡ false
  below' i lt = subst (λ t → q t ≡ false) (sym (+-suc i s)) (below (suc i) (suc-≤-suc lt))
  p' : q (k + suc s) ≡ true
  p' = subst (λ t → q t ≡ true) (sym (+-suc k s)) p

module Stage (m : ℕ) (judge : Judge (TypeOfHLevel ℓ-zero (suc m))) where
  open FromJudge (TypeOfHLevel ℓ-zero (suc m)) judge using (answers; sameQuestion)

  -- stages 1 .. m answer "no": the gathering of (m+1)-types is not an
  -- (m+1)-type (C-76), so it is at no lower level either
  silentBelow : (i : ℕ) → i < m → answers (i + 1) ≡ false
  silentBelow i lt = decBoolNo (judge (i + 1)) (λ h → gatheringNeverSettled m (levelUp le h))
    where
    le : suc (i + 1) ≤ suc m
    le = subst (λ t → suc t ≤ suc m) (sym (+-comm i 1)) (suc-≤-suc lt)

  -- stage m + 1 answers "yes": the gathering sits one level above (C-76)
  yesAtStage : answers (m + 1) ≡ true
  yesAtStage = decBoolYes (judge (m + 1))
    (subst (λ t → isOfHLevel (suc t) (TypeOfHLevel ℓ-zero (suc m))) (sym (+-comm m 1))
           (gatheringOneUp (suc m)))

  stopsAtStage : runFor m (question (TypeOfHLevel ℓ-zero (suc m)) judge) ≡ just (suc m)
  stopsAtStage =
    cong (runFor m) sameQuestion
    ∙ exactRun answers 1 m silentBelow yesAtStage
    ∙ cong just (+-comm m 1)

-- every finite stage has a judge
stageJudge : (m : ℕ) → Judge (TypeOfHLevel ℓ-zero (suc m))
stageJudge m j with splitℕ-≤ (suc m) j
... | inl sm≤j = yes (levelUp (suc-≤-suc sm≤j) (gatheringOneUp (suc m)))
... | inr j<sm = no (λ h → gatheringNeverSettled m (levelUp j<sm h))

------------------------------------------------------------------------
-- 5. kernel runs in this check unit

universeRun100 : runFor 100 (question (Type ℓ-zero) judgeU) ≡ nothing
universeRun100 = refl

setsGatheringRun : runFor 1 (question (TypeOfHLevel ℓ-zero 2) (stageJudge 1)) ≡ just 2
setsGatheringRun = refl

fourTypesGatheringRun : runFor 3 (question (TypeOfHLevel ℓ-zero 4) (stageJudge 3)) ≡ just 4
fourTypesGatheringRun = refl

------------------------------------------------------------------------
-- 6. the claim, as a single statement

qual-C426 :
  ((LimBit → LPO) × (LPO → LimBit)) ×
  (¬ ((s : OmegaQ) → Σ[ N ∈ ℕ ] SettlesAt s N)) ×
  ((judge : Judge (Type ℓ-zero)) →
     (question (Type ℓ-zero) judge ≡ never) ×
     ((k : ℕ) → FromJudge.answers (Type ℓ-zero) judge k ≡ false) ×
     SettlesAt (FromJudge.answers (Type ℓ-zero) judge) 0) ×
  ((n : ℕ) → ¬ isOfHLevel n (Type ℓ-zero)) ×
  ((m : ℕ) (judge : Judge (TypeOfHLevel ℓ-zero (suc m))) →
     runFor m (question (TypeOfHLevel ℓ-zero (suc m)) judge) ≡ just (suc m)) ×
  ((m : ℕ) → Judge (TypeOfHLevel ℓ-zero (suc m)))
qual-C426 =
  limBit↔LPO ,
  noSettlingWithoutMonotone ,
  (λ judge → universeQuestioningIsNever judge ,
             UniverseAnswers.allNo judge ,
             UniverseAnswers.settlesAtZero judge) ,
  universeHasNoLevel ,
  (λ m judge → Stage.stopsAtStage m judge) ,
  stageJudge
