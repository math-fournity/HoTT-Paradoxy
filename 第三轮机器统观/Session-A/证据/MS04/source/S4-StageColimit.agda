{-# OPTIONS --safe --cubical --guardedness #-}
module StageColimit where

-- MO3 C01: finite countdown graphs and their native sequential colimit.
-- The aggregate edge is the mere image of an actual edge at one stage.
-- No operational/physical completion or preservation promise is assumed.

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat
open import Cubical.Data.Sigma
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Fin.Inductive.Base
open import Cubical.Data.Sequence.Base
open import Cubical.Induction.WellFounded
open import Cubical.HITs.SequentialColimit.Base
open import Cubical.HITs.PropositionalTruncation.Base
import Cubical.HITs.PropositionalTruncation as PT

Stage : ℕ → Type
Stage n = Fin (suc n)

-- Step y x means that the recursive call from x may move to y.
NatStep : ℕ → ℕ → Type
NatStep y x = suc y ≡ x

StageStep : (n : ℕ) → Stage n → Stage n → Type
StageStep n y x = NatStep (fst y) (fst x)

natAccessible : (x : ℕ) → Acc NatStep x
natAccessible zero = acc (λ y p → Empty.rec (snotz p))
natAccessible (suc x) = acc (λ y p →
  subst (Acc NatStep) (sym (injSuc p)) (natAccessible x))

liftAccessible : {n : ℕ} (x : Stage n) →
  Acc NatStep (fst x) → Acc (StageStep n) x
liftAccessible x (acc next) =
  acc (λ y edge → liftAccessible y (next (fst y) edge))

-- Proposed C-327: every point of every finite stage is accessible.
stageWellFounded : (n : ℕ) → WellFounded (StageStep n)
stageWellFounded n x = liftAccessible x (natAccessible (fst x))

Stages : Sequence ℓ-zero
Sequence.obj Stages n = Stage n
Sequence.map Stages x = fsuc x

-- Proposed C-328: the inclusions preserve every stage edge.
stepPreserved : {n : ℕ} (y x : Stage n) → StageStep n y x →
  StageStep (suc n) (fsuc y) (fsuc x)
stepPreserved y x edge = cong suc edge

Total : Type
Total = SeqColim Stages

TotalStep : Total → Total → Type
TotalStep y x = ∥ (Σ[ n ∈ ℕ ]
  Σ[ a ∈ Stage n ] Σ[ b ∈ Stage n ]
  (StageStep n a b × ((incl {n = n} a ≡ y) ×
                     (incl {n = n} b ≡ x)))) ∥₁

-- The terminal vertex born at stage k.  At the next stage it acquires
-- an outgoing edge to the newly introduced terminal vertex.
terminal : ℕ → Total
terminal k = incl {n = k} fzero

terminalStep : (k : ℕ) → TotalStep (terminal (suc k)) (terminal k)
terminalStep k = ∣ (suc k , fzero , fsuc (fzero {m = k}) ,
  refl , refl , sym (push {n = k} (fzero {m = k}))) ∣₁

-- Proposed C-329: accessibility at any point of this explicit chain
-- would recursively supply accessibility at its successor, giving Empty.
terminalNotAccessible : (k : ℕ) → Acc TotalStep (terminal k) → ⊥
terminalNotAccessible k (acc next) =
  terminalNotAccessible (suc k) (next (terminal (suc k)) (terminalStep k))

totalNotWellFounded : WellFounded TotalStep → ⊥
totalNotWellFounded wf = terminalNotAccessible zero (wf (terminal zero))

-- Positive control: keep one stage fixed while using the same native
-- colimit and the same definition by stage-induced relation image.
module Frozen (bound : ℕ) where
  Constant : Sequence ℓ-zero
  Sequence.obj Constant k = Stage bound
  Sequence.map Constant x = x

  FrozenTotal : Type
  FrozenTotal = SeqColim Constant

  rank : FrozenTotal → ℕ
  rank (incl x) = fst x
  rank (push x i) = fst x

  FrozenStep : FrozenTotal → FrozenTotal → Type
  FrozenStep y x = ∥ (Σ[ k ∈ ℕ ]
    Σ[ a ∈ Stage bound ] Σ[ b ∈ Stage bound ]
    (StageStep bound a b × ((incl {n = k} a ≡ y) ×
                           (incl {n = k} b ≡ x)))) ∥₁

  rankStep : (y x : FrozenTotal) → FrozenStep y x → NatStep (rank y) (rank x)
  rankStep y x = PT.rec (isSetℕ _ _) λ where
    (k , a , b , edge , pa , pb) →
      cong suc (sym (cong rank pa)) ∙ edge ∙ cong rank pb

  frozenAccessible : (x : FrozenTotal) → Acc NatStep (rank x) → Acc FrozenStep x
  frozenAccessible x (acc next) = acc λ y edge →
    frozenAccessible y (next (rank y) (rankStep y x edge))

  -- Proposed C-330: the unchanged-stage aggregate retains the qualification.
  frozenWellFounded : WellFounded FrozenStep
  frozenWellFounded x = frozenAccessible x (natAccessible (rank x))
