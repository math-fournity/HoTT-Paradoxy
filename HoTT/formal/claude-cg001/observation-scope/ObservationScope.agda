{-# OPTIONS --safe --cubical --guardedness #-}
{-
  How far "no change detector" reaches (Claude, session 91a6cdaa, 2026-09-25),
  in reply to Terra's audit 005 (questions O-012, O-013).

  proof id : MP-CG001-OBSERVATION-SCOPE-001
  claims   : CG001-C-44 (full statement in CLAIM.md)

  Terra 005 points out that CG001-C-26 / C-32 quantify over non-dependent
  observers only, and proposes observing a transition (before, patch,
  after), a dependent reading, or the history index instead.  This file
  states exactly which of these can and cannot see an edit.

  C-44 (a) transition observers: for any type A and any function t of a
           transition (before, after, path) into any type B,
           t a b p = t a a refl: each edit gets the answer of the no-op at
           its start.  Hence no Bool-valued transition test answers false
           on a no-op and true on an edit.  (Path induction J; contractible
           contexts are not needed.)
       (b) readings with a constant result type: for any family M over A
           and any g : (c : A) -> M c -> P, the reading of the transported
           element at the new point equals the reading of the original at
           the old point; and g agrees along any path in the total space
           (currying: these are exactly the functions on Sigma A M).
       (c) readings with a varying result type: for o : (c : A) -> D c and
           p : a = b, transporting o a along p gives o b; the only uniform
           comparison of the two values says "same".
       (d) the index layer escapes: on the history-indexed context HIT
           (hdoc : List Bool -> H, hadd b h : hdoc h = hdoc (b :: h)) every
           Bool-valued function takes the same value at hdoc [] and
           hdoc (true :: []), while the test "is the history empty" on the
           index (List Bool) separates [] from true :: [].  The negative
           control WrongContextTest.agda shows the kernel rejecting that
           test when it is defined directly on H.

  Bridge labels (edit, no-op, context, history, reading) prove no fact
  about any version control system.
-}
module ObservationScope where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool ; true ; false ; true≢false ; false≢true)
open import Cubical.Data.List using (List ; [] ; _∷_)
open import Cubical.Relation.Nullary using (¬_)

private
  variable
    ℓ ℓ' ℓ'' : Level

------------------------------------------------------------------------
-- (a) transition observers: every edit looks like the no-op at its start

transitionBlind : {A : Type ℓ} {B : Type ℓ'} (t : (a b : A) → a ≡ b → B)
  {a b : A} (p : a ≡ b) → t a b p ≡ t a a refl
transitionBlind t {a} p = J (λ b' p' → t a b' p' ≡ t a a refl) refl p

noEditDetector : {A : Type ℓ} {a b : A} (p : a ≡ b)
  → ¬ (Σ[ t ∈ ((x y : A) → x ≡ y → Bool) ] (t a a refl ≡ false) × (t a b p ≡ true))
noEditDetector p (t , noop , edit) =
  false≢true (sym noop ∙ sym (transitionBlind t p) ∙ edit)

------------------------------------------------------------------------
-- (b) readings with a constant result type (dependent in the fibre)

readingIgnoresPatch : {A : Type ℓ} (M : A → Type ℓ') {P : Type ℓ''}
  (g : (c : A) → M c → P) {a b : A} (p : a ≡ b) (x : M a)
  → g b (transport (cong M p) x) ≡ g a x
readingIgnoresPatch M g {a} p x =
  J (λ b' p' → g b' (transport (cong M p') x) ≡ g a x)
    (cong (g a) (transportRefl x)) p

totalReading : {A : Type ℓ} {M : A → Type ℓ'} {P : Type ℓ''}
  (g : (c : A) → M c → P) {s s' : Σ A M} → s ≡ s'
  → g (fst s) (snd s) ≡ g (fst s') (snd s')
totalReading g q = cong (λ s → g (fst s) (snd s)) q

------------------------------------------------------------------------
-- (c) readings with a varying result type: the uniform comparison is transport

dependentComparison : {A : Type ℓ} (D : A → Type ℓ') (o : (c : A) → D c)
  {a b : A} (p : a ≡ b) → transport (cong D p) (o a) ≡ o b
dependentComparison D o p = fromPathP (cong o p)

------------------------------------------------------------------------
-- (d) the history-indexed contexts: blind on H, sighted on the index

data HistCtx : Type where
  hdoc : List Bool → HistCtx
  hadd : (b : Bool) (h : List Bool) → hdoc h ≡ hdoc (b ∷ h)

contextBlind : (d : HistCtx → Bool) → d (hdoc []) ≡ d (hdoc (true ∷ []))
contextBlind d = cong d (hadd true [])

isEmptyHistory : List Bool → Bool
isEmptyHistory []      = true
isEmptyHistory (_ ∷ _) = false

indexSeparates : ¬ (isEmptyHistory [] ≡ isEmptyHistory (true ∷ []))
indexSeparates = true≢false

noContextLift : ¬ (Σ[ d ∈ (HistCtx → Bool) ] ((h : List Bool) → d (hdoc h) ≡ isEmptyHistory h))
noContextLift (d , agrees) =
  true≢false (sym (agrees []) ∙ contextBlind d ∙ agrees (true ∷ []))
