{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Homotopical patch theory's own addendum, reconstructed natively
  (Claude, session 91a6cdaa, 2026-09-25), in reply to Terra's audit 003
  (questions O-007 .. O-009).

  proof id : MP-CG001-PATCH-CONTRACTIBLE-001
  claims   : CG001-C-30 .. CG001-C-33 (full statements in CLAIM.md)

  Source (paraphrased; locators in CLAIM.md): Angiuli, Morehouse, Licata,
  Harper, "Homotopical Patch Theory (Expanded Version)".  Addendum A.2, A.3
  and A.5 prove that the line-count context type and the history-indexed
  context types are contractible, and that paths out of the empty context
  carry no information beyond their endpoint histories.  Section 5.3 says
  that two elements joined by a path cannot be told apart inside the
  theory, while running a program can tell them apart.

  C-30  the line-count context HIT (the R of CG001-C-28/C-29: doc : N -> R,
        add n : doc n = doc (suc n)) is contractible; so every family over
        it has all fibres equal to its fibre at doc 0.
  C-31  the history-indexed context HIT (hdoc : List Bool -> H,
        hadd b h : hdoc h = hdoc (b :: h)) is contractible; paths out of the
        empty context are classified by histories; parallel patches are equal.
  C-32  with the singleton model (a context denotes the one repository its
        history determines), the total state space is contractible: the state
        before an edit and the state after it are identified, every
        non-dependent observable agrees on them, and no Bool-valued test on
        contexts tells them apart; the histories themselves differ, and the
        content is read off the fibre over each named context.
  C-33  two levels: two optimizers into singleton types are equal inside the
        theory, yet running the normalizing one on a detour patch yields the
        no-op patch by computation; the one-context interpreter runs.

  Bridge labels (context, patch, edit, repository, optimizer, run) prove no
  fact about any version control system.
-}
module PatchContractible where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Bool using (Bool; true; false)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.Data.List.Properties using (¬nil≡cons)
open import Cubical.Data.Int using (ℤ; pos)
open import Cubical.HITs.S1 using (S¹; base; loop; ΩS¹; winding; intLoop; decodeEncode)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- CG001-C-30  The line-count context HIT is contractible (addendum A.2)

data LineCtx : Type where
  doc : ℕ → LineCtx
  add : (n : ℕ) → doc n ≡ doc (suc n)

lineToPath : (n : ℕ) → doc 0 ≡ doc n
lineToPath zero = refl
lineToPath (suc n) = lineToPath n ∙ add n

lineContraction : (x : LineCtx) → doc 0 ≡ x
lineContraction (doc n) = lineToPath n
lineContraction (add n i) = compPath-filler (lineToPath n) (add n) i

isContrLineCtx : isContr LineCtx
isContrLineCtx = doc 0 , lineContraction

allFibresEqual : ∀ {ℓ} (F : LineCtx → Type ℓ) (n : ℕ) → F (doc 0) ≡ F (doc n)
allFibresEqual F n = cong F (lineToPath n)

------------------------------------------------------------------------
-- CG001-C-31  History-indexed contexts are contractible (addendum A.3, A.5)

data HistCtx : Type where
  hdoc : List Bool → HistCtx
  hadd : (b : Bool) (h : List Bool) → hdoc h ≡ hdoc (b ∷ h)

histToPath : (h : List Bool) → hdoc [] ≡ hdoc h
histToPath [] = refl
histToPath (b ∷ h) = histToPath h ∙ hadd b h

histContraction : (x : HistCtx) → hdoc [] ≡ x
histContraction (hdoc h) = histToPath h
histContraction (hadd b h i) = compPath-filler (histToPath h) (hadd b h) i

isContrHistCtx : isContr HistCtx
isContrHistCtx = hdoc [] , histContraction

-- paths out of the empty context are classified by histories ("log")
logEquiv : (Σ[ h ∈ List Bool ] hdoc [] ≡ hdoc h) ≃ List Bool
logEquiv = Σ-contractSnd λ h → isContr→isContrPath isContrHistCtx (hdoc []) (hdoc h)

-- a patch is determined by its endpoints: parallel patches are equal
parallelPatchesEqual : (x y : HistCtx) (p q : x ≡ y) → p ≡ q
parallelPatchesEqual x y p q = isContr→isProp (isContr→isContrPath isContrHistCtx x y) p q

------------------------------------------------------------------------
-- CG001-C-32  The singleton model: the total state space is one point

Model : HistCtx → Type
Model (hdoc h) = singl h
Model (hadd b h i) = ua (isContr→Equiv (isContrSingl h) (isContrSingl (b ∷ h))) i

isContrModel : (x : HistCtx) → isContr (Model x)
isContrModel (hdoc h) = isContrSingl h
isContrModel (hadd b h i) =
  isProp→PathP (λ j → isPropIsContr {A = Model (hadd b h j)})
    (isContrSingl h) (isContrSingl (b ∷ h)) i

State : Type
State = Σ HistCtx Model

isContrState : isContr State
isContrState = isContrΣ isContrHistCtx isContrModel

before after : State
before = hdoc [] , ([] , refl)
after = hdoc (true ∷ []) , (true ∷ [] , refl)

editIdentifiesStates : before ≡ after
editIdentifiesStates = isContr→isProp isContrState before after

observablesAgree : ∀ {ℓ} {P : Type ℓ} (g : State → P) → g before ≡ g after
observablesAgree g = cong g editIdentifiesStates

noChangeDetector : ¬ (Σ[ d ∈ (HistCtx → Bool) ] ¬ (d (hdoc []) ≡ d (hdoc (true ∷ []))))
noChangeDetector (d , differs) = differs (cong d (isContr→isProp isContrHistCtx _ _))

historiesDiffer : ¬ (Path (List Bool) [] (true ∷ []))
historiesDiffer = ¬nil≡cons

-- the content is read off the fibre over a named context
readAt : (h : List Bool) → Model (hdoc h) → List Bool
readAt h (c , _) = c

readBefore : readAt [] (snd before) ≡ []
readBefore = refl

readAfter : readAt (true ∷ []) (snd after) ≡ true ∷ []
readAfter = refl

------------------------------------------------------------------------
-- CG001-C-33  Two levels: equal inside the theory, different when run (section 5.3)

-- keep the patch as given
optimizeKeep : (p : ΩS¹) → singl p
optimizeKeep p = p , refl

-- replace the patch by its normal form (repeat (encode p) in the paper)
optimizeNormal : (p : ΩS¹) → singl p
optimizeNormal p = intLoop (winding p) , sym (decodeEncode base p)

optimizersEqual : optimizeKeep ≡ optimizeNormal
optimizersEqual = funExt λ p →
  isContr→isProp (isContrSingl p) (optimizeKeep p) (optimizeNormal p)

-- run on the detour "add one, then undo it": the normalizing optimizer returns
-- the no-op patch by computation (the other one returns the detour itself;
-- see the negative control WrongDetourRefl.agda)
normalRemovesDetour : fst (optimizeNormal (loop ∙ sym loop)) ≡ refl
normalRemovesDetour = refl

-- the one-context interpreter runs: two add1 patches applied to 0 give 2
interpreterRuns : winding (loop ∙ loop) ≡ pos 2
interpreterRuns = refl
