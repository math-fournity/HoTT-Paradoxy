{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The same ω-question in one univalent kernel (Claude Code, desktop session
  d58e0c0d, 2026-10-09; goal package CG-007, unit W6).

  proof id : MP-CG001-SAME-Q-UNIVALENT-001
  claims   : CG001-C-112 (the schema), CG001-C-113 (the instances);
             full statements in CLAIM.md

  C-93 (Lean, CG-005) put Zeno, H0 and Z0 under one ω-question schema, but
  H0 entered Lean only as a parameter ("every question is answered no"): the
  never-halting of the universe's questioning is a Cubical Agda theorem (C-78)
  and needs a univalent universe (C-80: in a UIP world it stops at the first
  question).  This file states the schema and all three instances in one
  univalent kernel, with H0 native.

  C-112 (the schema)
    * an ω-question is a stream of answers, `OmegaQ = ℕ → Bool` ("settled at
      stage k?"); `askQ q s` asks from stage s on and stops at the first yes;
    * the search never answers iff the question is never settled
      (`neverIff`); a stage that is settled makes the search answer within
      that much fuel (`settledHalts`);
    * P_fin is refuted: not every ω-question, although all its answers are
      given at once as a completed whole, is completed at some finite stage
      (`¬PFin`);
    * the runner: at every stage that is not settled it halves its remaining
      distance (the remaining distance after n stages is 2^-(halvings q n));
      it arrives in the limit (`Arrives`: for every precision 2^-K the
      remaining distance eventually drops below it) iff the question is never
      settled, provided a settled stage stays settled (`arrivesOfNever`,
      `neverOfArrives`); the proviso is needed (`monotoneNeeded`);
    * a judge-driven questioning in the sense of C-77 is exactly the search
      over its decided answers (`FromJudge.sameQuestion`, a path of programs).
  C-113 (the instances, all in this kernel)
    * Zeno: the stream that is never settled; the search never completes at
      a finite stage, the runner halves at every stage (1 - 2^-n) and arrives;
    * H0: the questioning of the univalent universe `Type ℓ-zero` is the
      search over its decided answers, it is never settled from stage 1 on
      (C-78, imported), and the runner driven by it arrives;
    * contrast: on the set-truncated universe the same program stops at
      stage 1 (C-83, imported), every later stage is settled, and the runner
      stands still and does not arrive;
    * Z0, as a parameter: for any monotone stream (a theory's stage-by-stage
      search for a contradiction) the same equivalences hold.  That ZFC
      cannot prove its own stream never settled is the Lean side (C-103,
      C-109 to C-111), not this file.

  Bridge labels (runner, distance, settled, Zeno, H0, Z0) prove no physical
  or historical fact.
-}
module SameQ where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties using (+-suc; +-zero; +-comm)
open import Cubical.Data.Nat.Order
  using (_≤_; _<_; suc-≤-suc; ≤-refl; ≤-suc; ≤-trans; splitℕ-≤; ¬m<m; ¬-<-zero)
open import Cubical.Data.Bool using (Bool; true; false; if_then_else_; not; true≢false)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Maybe.Properties using (¬nothing≡just)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)
open import Cubical.HITs.SetTruncation using (squash₂)

open import PedometerSemantics using (Delay; Delay'; now; later; never; evalFor; runFor)
open import DelayMonad using (divergesRunsNothing)
open import QuestioningDelay
  using (Judge; question; module Questioning; universeQuestioningIsNever; judgeU)
open import TruncationQuestioning using (TU; truncUniverseStopsAtOne)

open Delay

private
  variable
    ℓ : Level

------------------------------------------------------------------------
-- 1. the ω-question and its search program

-- the answer, at every stage k, to "is it settled at stage k?"
OmegaQ : Type
OmegaQ = ℕ → Bool

mutual
  askQ : OmegaQ → ℕ → Delay ℕ
  askQ q k .force = stepQ q k (q k)

  stepQ : OmegaQ → ℕ → Bool → Delay' ℕ
  stepQ q k true  = now k
  stepQ q k false = later (askQ q (suc k))

-- never settled from stage s on
NeverFrom : OmegaQ → ℕ → Type
NeverFrom q s = (k : ℕ) → q (k + s) ≡ false

-- never settled
Never : OmegaQ → Type
Never q = (k : ℕ) → q k ≡ false

Halts : Delay ℕ → Type
Halts d = Σ[ n ∈ ℕ ] Σ[ j ∈ ℕ ] runFor n d ≡ just j

neverStep : (q : OmegaQ) (s : ℕ) → NeverFrom q s → NeverFrom q (suc s)
neverStep q s h k = subst (λ m → q m ≡ false) (sym (+-suc k s)) (h (suc k))

never→from0 : (q : OmegaQ) → Never q → NeverFrom q 0
never→from0 q h k = subst (λ m → q m ≡ false) (sym (+-zero k)) (h k)

from0→never : (q : OmegaQ) → NeverFrom q 0 → Never q
from0→never q h k = subst (λ m → q m ≡ false) (+-zero k) (h k)

-- C-112 (a) never settled ⟹ the search is the program that runs forever
mutual
  askNever : (q : OmegaQ) (s : ℕ) → NeverFrom q s → askQ q s ≡ never
  askNever q s h i .force = stepNever q s h (q s) (h 0) i

  stepNever : (q : OmegaQ) (s : ℕ) → NeverFrom q s → (b : Bool) → b ≡ false
            → stepQ q s b ≡ later never
  stepNever q s h true  p = ⊥.rec (true≢false p)
  stepNever q s h false p i = later (askNever q (suc s) (neverStep q s h) i)

neverRunsNothing : (q : OmegaQ) (s : ℕ) → NeverFrom q s → (n : ℕ) → runFor n (askQ q s) ≡ nothing
neverRunsNothing q s h = divergesRunsNothing (askQ q s) (askNever q s h)

-- C-112 (b) a settled stage makes the search answer within that much fuel
settledHalts : (q : OmegaQ) (s k : ℕ) → q (k + s) ≡ true
             → Σ[ j ∈ ℕ ] runFor k (askQ q s) ≡ just j
settledHalts q s zero p = s , cong (λ b → evalFor 0 (stepQ q s b)) p
settledHalts q s (suc k) p = go (q s) refl
  where
  go : (b : Bool) → q s ≡ b → Σ[ j ∈ ℕ ] runFor (suc k) (askQ q s) ≡ just j
  go true  e = s , cong (λ b → evalFor (suc k) (stepQ q s b)) e
  go false e =
    let (j , r) = settledHalts q (suc s) k (subst (λ m → q m ≡ true) (sym (+-suc k s)) p)
    in j , cong (λ b → evalFor (suc k) (stepQ q s b)) e ∙ r

nothingNever : (q : OmegaQ) (s : ℕ) → ((n : ℕ) → runFor n (askQ q s) ≡ nothing) → NeverFrom q s
nothingNever q s h k = go (q (k + s)) refl
  where
  go : (b : Bool) → q (k + s) ≡ b → q (k + s) ≡ false
  go false e = e
  go true  e = ⊥.rec (¬nothing≡just (sym (h k) ∙ snd (settledHalts q s k e)))

-- C-112 (a) the search never answers iff the question is never settled
neverIff : (q : OmegaQ) (s : ℕ)
         → (NeverFrom q s → askQ q s ≡ never) × (askQ q s ≡ never → NeverFrom q s)
neverIff q s = askNever q s , λ p → nothingNever q s (divergesRunsNothing (askQ q s) p)

-- C-112 (c) P_fin: every ω-question, all of whose answers are given at once,
-- is completed at some finite stage.  It is false.
PFin : Type
PFin = (q : OmegaQ) → Halts (askQ q 0)

constFalse : OmegaQ
constFalse _ = false

¬PFin : ¬ PFin
¬PFin pf =
  ¬nothing≡just (sym (neverRunsNothing constFalse 0 (λ _ → refl) (fst (pf constFalse)))
                 ∙ snd (snd (pf constFalse)))

------------------------------------------------------------------------
-- 2. the runner

-- at every stage that is not settled the runner halves its remaining
-- distance; after n stages the remaining distance is 2^-(halvings q n)
halvings : OmegaQ → ℕ → ℕ
halvings q zero    = zero
halvings q (suc n) = if q n then halvings q n else suc (halvings q n)

-- arrival in the limit: for every precision 2^-K the remaining distance
-- eventually drops to 2^-K or below (and stays there, by `halvingsMono`)
Arrives : OmegaQ → Type
Arrives q = (K : ℕ) → Σ[ n ∈ ℕ ] K ≤ halvings q n

-- a settled stage stays settled
Monotone : OmegaQ → Type
Monotone q = (k : ℕ) → q k ≡ true → q (suc k) ≡ true

halvingsStep : (q : OmegaQ) (n : ℕ) (b : Bool) → q n ≡ b
             → halvings q (suc n) ≡ (if b then halvings q n else suc (halvings q n))
halvingsStep q n b e = cong (λ c → if c then halvings q n else suc (halvings q n)) e

halvingsMono : (q : OmegaQ) (n : ℕ) → halvings q n ≤ halvings q (suc n)
halvingsMono q n = go (q n) refl
  where
  go : (b : Bool) → q n ≡ b → halvings q n ≤ halvings q (suc n)
  go true  e = subst (halvings q n ≤_) (sym (halvingsStep q n true e)) ≤-refl
  go false e = subst (halvings q n ≤_) (sym (halvingsStep q n false e)) (≤-suc ≤-refl)

halvings≤ : (q : OmegaQ) (n : ℕ) → halvings q n ≤ n
halvings≤ q zero = ≤-refl
halvings≤ q (suc n) = go (q n) refl
  where
  go : (b : Bool) → q n ≡ b → halvings q (suc n) ≤ suc n
  go true  e = subst (_≤ suc n) (sym (halvingsStep q n true e)) (≤-suc (halvings≤ q n))
  go false e = subst (_≤ suc n) (sym (halvingsStep q n false e)) (suc-≤-suc (halvings≤ q n))

halvingsNever : (q : OmegaQ) → Never q → (n : ℕ) → halvings q n ≡ n
halvingsNever q h zero = refl
halvingsNever q h (suc n) = halvingsStep q n false (h n) ∙ cong suc (halvingsNever q h n)

halvingsAllSettled : (q : OmegaQ) → ((k : ℕ) → q k ≡ true) → (n : ℕ) → halvings q n ≡ 0
halvingsAllSettled q h zero = refl
halvingsAllSettled q h (suc n) = halvingsStep q n true (h n) ∙ halvingsAllSettled q h n

-- C-112 (d) never settled ⟹ the runner arrives
arrivesOfNever : (q : OmegaQ) → Never q → Arrives q
arrivesOfNever q h K = K , subst (K ≤_) (sym (halvingsNever q h K)) ≤-refl

settledFrom : (q : OmegaQ) → Monotone q → (k : ℕ) → q k ≡ true → (d : ℕ) → q (d + k) ≡ true
settledFrom q mono k p zero = p
settledFrom q mono k p (suc d) = mono (d + k) (settledFrom q mono k p d)

frozen : (q : OmegaQ) → Monotone q → (k : ℕ) → q k ≡ true
       → (d : ℕ) → halvings q (d + k) ≡ halvings q k
frozen q mono k p zero = refl
frozen q mono k p (suc d) =
  halvingsStep q (d + k) true (settledFrom q mono k p d) ∙ frozen q mono k p d

boundedOfSettled : (q : OmegaQ) → Monotone q → (k : ℕ) → q k ≡ true
                 → (n : ℕ) → halvings q n ≤ k
boundedOfSettled q mono k p n with splitℕ-≤ n k
... | inl n≤k = ≤-trans (halvings≤ q n) n≤k
... | inr (i , e) = subst (_≤ k) (sym fz) (halvings≤ q k)
  where
  fz : halvings q n ≡ halvings q k
  fz = cong (halvings q) (sym e ∙ +-suc i k) ∙ frozen q mono k p (suc i)

-- C-112 (d) for a monotone question: the runner arrives ⟹ never settled
neverOfArrives : (q : OmegaQ) → Monotone q → Arrives q → Never q
neverOfArrives q mono arr k = go (q k) refl
  where
  go : (b : Bool) → q k ≡ b → q k ≡ false
  go false e = e
  go true  e =
    ⊥.rec (¬m<m (≤-trans (snd (arr (suc k)))
                         (boundedOfSettled q mono k e (fst (arr (suc k))))))

-- the monotone proviso is needed: an alternating question halves at every
-- other stage, so the runner arrives, yet it is settled at every other stage
alt : OmegaQ
alt zero    = true
alt (suc n) = not (alt n)

twice : ℕ → ℕ
twice zero    = zero
twice (suc n) = suc (suc (twice n))

halvingsAltTwoSteps : (n : ℕ) → halvings alt (suc (suc n)) ≡ suc (halvings alt n)
halvingsAltTwoSteps n = go (alt n) refl
  where
  go : (b : Bool) → alt n ≡ b → halvings alt (suc (suc n)) ≡ suc (halvings alt n)
  go true  e = halvingsStep alt (suc n) false (cong not e) ∙ cong suc (halvingsStep alt n true e)
  go false e = halvingsStep alt (suc n) true (cong not e) ∙ halvingsStep alt n false e

halvingsAltTwice : (K : ℕ) → halvings alt (twice K) ≡ K
halvingsAltTwice zero    = refl
halvingsAltTwice (suc K) = halvingsAltTwoSteps (twice K) ∙ cong suc (halvingsAltTwice K)

monotoneNeeded : Σ[ q ∈ OmegaQ ] Arrives q × (¬ Never q)
monotoneNeeded =
  alt , (λ K → twice K , subst (K ≤_) (sym (halvingsAltTwice K)) ≤-refl) , λ h → true≢false (h 0)

------------------------------------------------------------------------
-- 3. a judge-driven questioning (C-77) is the search over its decided answers

decBool : {P : Type ℓ} → Dec P → Bool
decBool (yes _) = true
decBool (no _)  = false

decBoolYes : {P : Type ℓ} (d : Dec P) → P → decBool d ≡ true
decBoolYes (yes _) _ = refl
decBoolYes (no np) p = ⊥.rec (np p)

module FromJudge {ℓ : Level} (C : Type ℓ) (judge : Judge C) where
  open Questioning C judge using (askFrom; answer)

  answers : OmegaQ
  answers k = decBool (judge k)

  mutual
    sameAsk : (k : ℕ) → askFrom k ≡ askQ answers k
    sameAsk k i .force = sameAnswer k (judge k) i

    sameAnswer : (k : ℕ) (d : Dec (isOfHLevel (suc k) C))
               → answer k d ≡ stepQ answers k (decBool d)
    sameAnswer k (yes _) = refl
    sameAnswer k (no _) i = later (sameAsk (suc k) i)

  -- C-112 (e) the questioning program is the search, as a path of programs
  sameQuestion : question C judge ≡ askQ answers 1
  sameQuestion = sameAsk 1

------------------------------------------------------------------------
-- 4. the instances, all in this univalent kernel

-- (a) Zeno: every stage still has distance left
zenoQ : OmegaQ
zenoQ = constFalse

zenoNeverCompletes : askQ zenoQ 0 ≡ never
zenoNeverCompletes = askNever zenoQ 0 (λ _ → refl)

zenoHalvings : (n : ℕ) → halvings zenoQ n ≡ n
zenoHalvings = halvingsNever zenoQ (λ _ → refl)

zenoArrives : Arrives zenoQ
zenoArrives = arrivesOfNever zenoQ (λ _ → refl)

-- (b) H0: the questioning of the univalent universe
module H0 (judge : Judge (Type ℓ-zero)) where
  open FromJudge (Type ℓ-zero) judge

  h0IsSearch : question (Type ℓ-zero) judge ≡ askQ answers 1
  h0IsSearch = sameQuestion

  h0SearchNever : askQ answers 1 ≡ never
  h0SearchNever = sym h0IsSearch ∙ universeQuestioningIsNever judge

  h0NeverSettled : NeverFrom answers 1
  h0NeverSettled = snd (neverIff answers 1) h0SearchNever

  -- the runner driven by the universe's answers, from stage 1 on
  h0Stream : OmegaQ
  h0Stream k = answers (k + 1)

  h0RunnerArrives : Arrives h0Stream
  h0RunnerArrives = arrivesOfNever h0Stream h0NeverSettled

-- the kernel runs the H0 search with the judge of C-78
h0Kernel100 : runFor 100 (askQ (FromJudge.answers (Type ℓ-zero) judgeU) 1) ≡ nothing
h0Kernel100 = refl

-- (c) contrast: the set-truncated universe
module Truncated (tjudge : Judge TU) where
  open FromJudge TU tjudge

  truncIsSearch : question TU tjudge ≡ askQ answers 1
  truncIsSearch = sameQuestion

  truncStopsAtStageOne : runFor 0 (askQ answers 1) ≡ just 1
  truncStopsAtStageOne = cong (runFor 0) (sym truncIsSearch) ∙ truncUniverseStopsAtOne tjudge

  truncSettled : (k : ℕ) → answers (k + 1) ≡ true
  truncSettled k = decBoolYes (tjudge (k + 1))
    (subst (λ m → isOfHLevel m TU) (cong suc (sym (+-comm k 1)))
      (isOfHLevelPlus' {n = k} 2 squash₂))

  truncStream : OmegaQ
  truncStream k = answers (k + 1)

  truncRunnerStands : (n : ℕ) → halvings truncStream n ≡ 0
  truncRunnerStands = halvingsAllSettled truncStream truncSettled

  truncRunnerDoesNotArrive : ¬ Arrives truncStream
  truncRunnerDoesNotArrive arr =
    ¬-<-zero (subst (1 ≤_) (truncRunnerStands (fst (arr 1))) (snd (arr 1)))

-- (d) Z0, as a parameter: any monotone stream, e.g. a theory's stage-by-stage
-- search for a contradiction ("a contradiction found by stage k")
module Z0 (z : OmegaQ) (zMono : Monotone z) where

  z0SearchNeverIff : (Never z → askQ z 0 ≡ never) × (askQ z 0 ≡ never → Never z)
  z0SearchNeverIff =
    (λ h → askNever z 0 (never→from0 z h)) , (λ p → from0→never z (snd (neverIff z 0) p))

  z0RunnerIff : (Arrives z → Never z) × (Never z → Arrives z)
  z0RunnerIff = neverOfArrives z zMono , arrivesOfNever z

------------------------------------------------------------------------
-- 5. the claims, as single statements

qual-C112 :
  ((q : OmegaQ) (s : ℕ) → (NeverFrom q s → askQ q s ≡ never) × (askQ q s ≡ never → NeverFrom q s)) ×
  ((q : OmegaQ) (s k : ℕ) → q (k + s) ≡ true → Σ[ j ∈ ℕ ] runFor k (askQ q s) ≡ just j) ×
  (¬ PFin) ×
  ((q : OmegaQ) → Never q → Arrives q) ×
  ((q : OmegaQ) → Monotone q → Arrives q → Never q) ×
  (Σ[ q ∈ OmegaQ ] Arrives q × (¬ Never q)) ×
  ((C : Type) (judge : Judge C) → question C judge ≡ askQ (FromJudge.answers C judge) 1)
qual-C112 =
  neverIff , settledHalts , ¬PFin , arrivesOfNever , neverOfArrives , monotoneNeeded ,
  (λ C judge → FromJudge.sameQuestion C judge)

qual-C113 :
  ((askQ zenoQ 0 ≡ never) × ((n : ℕ) → halvings zenoQ n ≡ n) × Arrives zenoQ) ×
  ((judge : Judge (Type ℓ-zero)) →
     (question (Type ℓ-zero) judge ≡ askQ (FromJudge.answers (Type ℓ-zero) judge) 1) ×
     NeverFrom (FromJudge.answers (Type ℓ-zero) judge) 1 ×
     Arrives (H0.h0Stream judge)) ×
  ((tjudge : Judge TU) →
     (runFor 0 (askQ (FromJudge.answers TU tjudge) 1) ≡ just 1) ×
     ((n : ℕ) → halvings (Truncated.truncStream tjudge) n ≡ 0) ×
     (¬ Arrives (Truncated.truncStream tjudge))) ×
  ((z : OmegaQ) → Monotone z →
     ((Never z → askQ z 0 ≡ never) × (askQ z 0 ≡ never → Never z)) ×
     ((Arrives z → Never z) × (Never z → Arrives z)))
qual-C113 =
  (zenoNeverCompletes , zenoHalvings , zenoArrives) ,
  (λ judge → H0.h0IsSearch judge , H0.h0NeverSettled judge , H0.h0RunnerArrives judge) ,
  (λ tjudge → Truncated.truncStopsAtStageOne tjudge , Truncated.truncRunnerStands tjudge ,
              Truncated.truncRunnerDoesNotArrive tjudge) ,
  (λ z zMono → Z0.z0SearchNeverIff z zMono , Z0.z0RunnerIff z zMono)
