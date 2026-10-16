{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The wall met by homotopical patch theory, reconstructed natively
  (Claude, session 6fd0312a, 2026-09-25).

  proof id : MP-CG001-PATCH-WALL-001
  claims   : CG001-C-28 .. CG001-C-29 (full statements in CLAIM.md)

  Source (paraphrased, see CLAIM.md): Angiuli, Morehouse, Licata, Harper,
  "Homotopical Patch Theory", section "A Patch Theory With Richer Contexts":
  when contexts are classified by line count and adding a line is a path,
  the natural interpretation of a context as the type of files of that length
  fails, and if every context is reachable from the empty one, every context
  must be interpreted by a contractible type.

  C-28  on the context HIT with doc : N -> R and add n : doc n = doc (suc n),
        no family F : R -> Type has F (doc 0) = File 0 and
        F (doc 1) = File 1, where File n is the type of n-line files over a
        two-letter alphabet.
  C-29  for every family F : R -> Type, if F (doc 0) is contractible then
        F (doc n) is contractible for every n.

  File n = Bool x ... x Bool x Unit (n factors) stands in for n-line files;
  bridge labels (context, file, line) prove no fact about any version
  control system.
-}
module PatchWall where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Bool using (Bool; true; false; true≢false)
open import Cubical.Data.Unit using (Unit; tt; isPropUnit)
open import Cubical.Relation.Nullary using (¬_)

-- n-line files over a two-letter alphabet
File : ℕ → Type
File zero = Unit
File (suc n) = Bool × File n

-- contexts classified by line count; adding a line is a path
data R : Type where
  doc : ℕ → R
  add : (n : ℕ) → doc n ≡ doc (suc n)

------------------------------------------------------------------------
-- CG001-C-28  The natural interpretation fails

-- the empty file is the only 0-line file
isPropFile0 : isProp (File 0)
isPropFile0 = isPropUnit

oneLineFilesDiffer : ¬ (Path (File 1) (true , tt) (false , tt))
oneLineFilesDiffer p = true≢false (cong fst p)

noLengthInterpretation :
  ¬ (Σ[ F ∈ (R → Type) ] (F (doc 0) ≡ File 0) × (F (doc 1) ≡ File 1))
noLengthInterpretation (F , p0 , p1) =
  oneLineFilesDiffer (isPropFile1 (true , tt) (false , tt))
  where
  file0≡file1 : File 0 ≡ File 1
  file0≡file1 = sym p0 ∙ cong F (add 0) ∙ p1

  isPropFile1 : isProp (File 1)
  isPropFile1 = subst isProp file0≡file1 isPropFile0

------------------------------------------------------------------------
-- CG001-C-29  Every context reachable from the empty one is forced to be contractible

allContextsContractible : (F : R → Type) → isContr (F (doc 0)) → (n : ℕ) → isContr (F (doc n))
allContextsContractible F c zero = c
allContextsContractible F c (suc n) =
  subst isContr (cong F (add n)) (allContextsContractible F c n)
