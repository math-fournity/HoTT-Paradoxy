{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The stop-at-+2 program as a program (Claude, session 91a6cdaa, 2026-09-25),
  in reply to Terra's audit 009 (O-025 and section 5.2).

  proof id : MP-CG001-PEDOMETER-SEMANTICS-001
  claims   : CG001-C-55, CG001-C-56 (full statements in CLAIM.md)

  Terra 009 section 3: C-47 proves that no stopping time exists and that every
  fuel-bounded search returns nothing; it does not give the program an
  operational semantics, so "the program does not halt" was not yet a formal
  statement.  This file gives the program the standard semantics of general
  recursion, the delay monad (Capretta 2005): a program is a possibly infinite
  sequence of `later` steps, possibly ending in `now a`; `never` is the
  program that runs forever.

  C-55 (a) for any decidable stop condition P, the unbounded search
           searchFrom k (test P k; if it holds return k, otherwise take one
           step and continue at k + 1) is a program; if no k satisfies P, the
           program is equal to `never` (a path in the coinductive type, i.e.
           bisimilarity): it diverges;
       (b) under the P-rev transport specification of C-47 (round trips
           p . sym p, the pedometer carried by subst in any family B, any
           readout, any start value) the stop-at-+2 program is equal to
           `never`, for every type, path and family;
       (c) the same program converges to 1 (runFor 1 = just 1) under the
           escape specification of C-50 (a second, independent return path,
           Z-fibres), under the directed specification of C-51 (walks in the
           free category) and under the data specification of C-47 (c)
           (walks as lists of steps).
  C-56 the type of places of C-50 has an involutive self-equivalence that
       fixes both towns and sends go to sym back and back to sym go; carried
       through it, the counter moves go from 0 to -1 (refl).  Which paths
       count as forward walks is therefore not determined by the type and its
       towns; it is a choice of orientation (the generators go, back).

  The definitions of C-47, C-50 and C-51 are restated here (identically) so
  that the file is self-contained.  Bridge labels (walker, road, pedometer,
  stop) prove no physical fact.
-}
module PedometerSemantics where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rCancel; rUnit)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_; snotz; znots)
open import Cubical.Data.Nat.Properties using (m+n≡n→m≡0; discreteℕ)
open import Cubical.Data.Int using (ℤ; pos; negsuc; sucPathℤ; injPos; discreteℤ)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.List using (List; []; _∷_; _++_; length)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)

private
  variable
    ℓ ℓ' : Level

------------------------------------------------------------------------
-- the delay monad

mutual
  data Delay' (A : Type) : Type where
    now   : A → Delay' A
    later : Delay A → Delay' A

  record Delay (A : Type) : Type where
    coinductive
    field force : Delay' A

open Delay

never : {A : Type} → Delay A
never .force = later never

-- evaluation with a step budget, used only to state convergence
evalFor : {A : Type} → ℕ → Delay' A → Maybe A
evalFor _       (now a)   = just a
evalFor zero    (later _) = nothing
evalFor (suc n) (later d) = evalFor n (d .force)

runFor : {A : Type} → ℕ → Delay A → Maybe A
runFor n d = evalFor n (d .force)

------------------------------------------------------------------------
-- C-55 (a): the unbounded search as a program

module StopProgram (P : ℕ → Type) (dec : (k : ℕ) → Dec (P k)) where

  mutual
    searchFrom : ℕ → Delay ℕ
    searchFrom k .force = step k (dec k)

    step : (k : ℕ) → Dec (P k) → Delay' ℕ
    step k (yes _) = now k
    step k (no _)  = later (searchFrom (suc k))

  program : Delay ℕ
  program = searchFrom 0

  module Diverges (np : (k : ℕ) → ¬ P k) where

    mutual
      diverges : (k : ℕ) → searchFrom k ≡ never
      diverges k i .force = stepNever k (dec k) i

      stepNever : (k : ℕ) (d : Dec (P k)) → step k d ≡ later never
      stepNever k (yes pk) = ⊥.rec (np k pk)
      stepNever k (no _) i = later (diverges (suc k) i)

    programIsNever : program ≡ never
    programIsNever = diverges 0

  convergesAtOne : ¬ P 0 → P 1 → runFor 1 program ≡ just 1
  convergesAtOne n0 p1 = first (dec 0)
    where
    second : (d : Dec (P 1)) → evalFor 0 (step 1 d) ≡ just 1
    second (yes _)  = refl
    second (no np1) = ⊥.rec (np1 p1)
    first : (d : Dec (P 0)) → evalFor 1 (step 0 d) ≡ just 1
    first (yes p0) = ⊥.rec (n0 p0)
    first (no _)   = second (dec 1)

------------------------------------------------------------------------
-- C-55 (b): the P-rev transport specification (C-47, restated)

roundTrips : {A : Type ℓ} {a b : A} → a ≡ b → ℕ → a ≡ a
roundTrips p zero    = refl
roundTrips p (suc n) = roundTrips p n ∙ (p ∙ sym p)

roundTripsAreStaying : {A : Type ℓ} {a b : A} (p : a ≡ b) (n : ℕ) → roundTrips p n ≡ refl
roundTripsAreStaying p zero    = refl
roundTripsAreStaying p (suc n) =
  cong₂ _∙_ (roundTripsAreStaying p n) (rCancel p) ∙ sym (rUnit refl)

module PRevProgram {A : Type ℓ} {a b : A} (p : a ≡ b)
                   (B : A → Type ℓ') (read : B a → ℕ) (start : B a) where

  after : ℕ → B a
  after n = subst B (roundTrips p n) start

  Advanced : ℕ → Type
  Advanced n = read (after n) ≡ 2 + read start

  neverAdvanced : (n : ℕ) → ¬ Advanced n
  neverAdvanced n adv =
    snotz (m+n≡n→m≡0 {m = 2}
      (sym adv ∙ cong read (cong (λ q → subst B q start) (roundTripsAreStaying p n)
                            ∙ substRefl {B = B} start)))

  open StopProgram Advanced (λ n → discreteℕ (read (after n)) (2 + read start))

  stopProgram : Delay ℕ
  stopProgram = program

  stopProgramIsNever : stopProgram ≡ never
  stopProgramIsNever = Diverges.programIsNever neverAdvanced

------------------------------------------------------------------------
-- C-55 (c), first: the escape specification (C-50, restated)

module Escape where

  data Places : Type where
    west east : Places
    go   : west ≡ east
    back : east ≡ west

  Ped : Places → Type
  Ped west     = ℤ
  Ped east     = ℤ
  Ped (go i)   = sucPathℤ i
  Ped (back i) = sucPathℤ i

  roundTrip : west ≡ west
  roundTrip = go ∙ back

  rounds : ℕ → west ≡ west
  rounds zero    = refl
  rounds (suc n) = rounds n ∙ roundTrip

  after : ℕ → ℤ
  after n = subst Ped (rounds n) (pos 0)

  Advanced : ℕ → Type
  Advanced n = after n ≡ pos 2

  open StopProgram Advanced (λ n → discreteℤ (after n) (pos 2))

  notAtStart : ¬ Advanced 0
  notAtStart adv = znots (injPos (sym (substRefl {B = Ped} {x = west} (pos 0)) ∙ adv))

  afterOne : Advanced 1
  afterOne = substComposite Ped refl roundTrip (pos 0)
           ∙ cong (subst Ped roundTrip) (substRefl {B = Ped} {x = west} (pos 0))

  stopProgram : Delay ℕ
  stopProgram = program

  stopProgramConverges : runFor 1 stopProgram ≡ just 1
  stopProgramConverges = convergesAtOne notAtStart afterOne

  ----------------------------------------------------------------------
  -- C-56: the orientation is a choice

  reverse : Places → Places
  reverse west     = west
  reverse east     = east
  reverse (go i)   = back (~ i)
  reverse (back i) = go (~ i)

  reverseInvolutive : (x : Places) → reverse (reverse x) ≡ x
  reverseInvolutive west     = refl
  reverseInvolutive east     = refl
  reverseInvolutive (go i)   = refl
  reverseInvolutive (back i) = refl

  reverseEquiv : Places ≃ Places
  reverseEquiv = isoToEquiv (iso reverse reverse reverseInvolutive reverseInvolutive)

  reverseFixesWest : reverse west ≡ west
  reverseFixesWest = refl

  reverseFixesEast : reverse east ≡ east
  reverseFixesEast = refl

  reverseSendsGoToTheReverseOfBack : cong reverse go ≡ sym back
  reverseSendsGoToTheReverseOfBack = refl

  reverseSendsBackToTheReverseOfGo : cong reverse back ≡ sym go
  reverseSendsBackToTheReverseOfGo = refl

  -- carried through the symmetry, the counted walk go counts -1
  reversedCounterRetreatsAlongGo : subst (λ x → Ped (reverse x)) go (pos 0) ≡ negsuc 0
  reversedCounterRetreatsAlongGo = refl

  -- and the anti-walk sym go counts +1
  reversedCounterAdvancesAlongSymGo : subst (λ x → Ped (reverse x)) (sym go) (pos 0) ≡ pos 1
  reversedCounterAdvancesAlongSymGo = refl

------------------------------------------------------------------------
-- C-55 (c), second: the directed specification (C-51, restated)

module Directed where

  data Town : Type where
    west east : Town

  data Step : Town → Town → Type where
    go   : Step west east
    back : Step east west

  infixr 5 _then_ _+++_

  data Walk : Town → Town → Type where
    stay   : {x : Town} → Walk x x
    _then_ : {x y z : Town} → Step x y → Walk y z → Walk x z

  _+++_ : {x y z : Town} → Walk x y → Walk y z → Walk x z
  stay       +++ v = v
  (s then w) +++ v = s then (w +++ v)

  carry : {x y : Town} → Walk x y → ℕ → ℕ
  carry stay       n = n
  carry (s then w) n = carry w (suc n)

  roundTrip : Walk west west
  roundTrip = go then back then stay

  rounds : ℕ → Walk west west
  rounds zero    = stay
  rounds (suc k) = rounds k +++ roundTrip

  after : ℕ → ℕ
  after k = carry (rounds k) 0

  open StopProgram (λ k → after k ≡ 2) (λ k → discreteℕ (after k) 2)

  stopProgram : Delay ℕ
  stopProgram = program

  stopProgramConverges : runFor 1 stopProgram ≡ just 1
  stopProgramConverges = refl

------------------------------------------------------------------------
-- C-55 (c), third: the data specification (C-47 (c), restated)

module AsData where

  data Move : Type where
    fwd bwd : Move

  oscillation : ℕ → List Move
  oscillation zero    = []
  oscillation (suc n) = oscillation n ++ (fwd ∷ bwd ∷ [])

  stepsAfter : ℕ → ℕ
  stepsAfter n = length (oscillation n)

  open StopProgram (λ n → stepsAfter n ≡ 2) (λ n → discreteℕ (stepsAfter n) 2)

  stopProgram : Delay ℕ
  stopProgram = program

  stopProgramConverges : runFor 1 stopProgram ≡ just 1
  stopProgramConverges = refl
