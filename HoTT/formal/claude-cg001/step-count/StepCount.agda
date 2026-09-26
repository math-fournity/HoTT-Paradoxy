{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Counting steps when a step is a path (Claude, session 91a6cdaa, 2026-09-25).

  proof id : MP-CG001-STEP-COUNT-001
  claims   : CG001-C-39 .. CG001-C-41 (full statements in CLAIM.md)

  Source (paraphrased; locator in CLAIM.md): Angiuli, Morehouse, Licata,
  Harper, "Homotopical patch theory", J. Funct. Program. 26 (2016), section
  3.2: a function counting the primitive patches in a composite patch is not
  definable, because a patch followed by its inverse equals the identity
  patch, while the count would be 2 for the one and 0 for the other.

  C-39  for any type, any path p : x = y and any function c on loops: c sends
        "there and back" (p . sym p) and "undo, then redo" (sym p . p) to
        c refl; for any family B, transport along p . sym p is the identity;
        so no counter gives 0 for staying put and 2 for there and back, and
        no counter carried along by transport in any family rises by 2 over
        there and back.
  C-40  on the circle (the one-context patch theory of the paper), no
        additive N-valued counter of loops counts loop as one step, while the
        additive Z-valued winding number counts net displacement and gives 0
        for loop . sym loop.
  C-41  journeys as data (lists of forward and back steps) carry both a step
        count and a net displacement; realizing a journey as a loop keeps the
        net displacement (winding . realize = net) and loses the step count:
        no function on loops agrees with the step count on realized journeys.

  Bridge labels (step, journey, patch, undo, pedometer) prove no physical or
  version-control fact.
-}
module StepCount where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (rCancel; lCancel; rUnit)
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_; snotz)
open import Cubical.Data.Nat.Properties using (m+n≡n→m≡0)
open import Cubical.Data.Int using (ℤ; pos; negsuc) renaming (_+_ to _+ℤ_)
open import Cubical.Data.List using (List; []; _∷_; length)
open import Cubical.HITs.S1 using (S¹; base; loop; ΩS¹; winding; winding-hom)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- CG001-C-39  Going and coming back is invisible to every reading of the path

module _ {ℓ} {A : Type ℓ} {x y : A} where

  roundTripInvisible : ∀ {ℓ'} {P : Type ℓ'} (c : x ≡ x → P) (p : x ≡ y)
    → c (p ∙ sym p) ≡ c refl
  roundTripInvisible c p = cong c (rCancel p)

  undoRedoInvisible : ∀ {ℓ'} {P : Type ℓ'} (c : y ≡ y → P) (p : x ≡ y)
    → c (sym p ∙ p) ≡ c refl
  undoRedoInvisible c p = cong c (lCancel p)

  roundTripTransportTrivial : ∀ {ℓ'} (B : A → Type ℓ') (p : x ≡ y) (b : B x)
    → subst B (p ∙ sym p) b ≡ b
  roundTripTransportTrivial B p b =
    cong (λ q → subst B q b) (rCancel p) ∙ substRefl {B = B} b

  noPedometer : (p : x ≡ y) → ¬ (Σ[ c ∈ (x ≡ x → ℕ) ] (c refl ≡ 0) × (c (p ∙ sym p) ≡ 2))
  noPedometer p (c , c0 , c2) = snotz (sym c2 ∙ roundTripInvisible c p ∙ c0)

  -- a counter carried along the journey by any family cannot rise over there and back
  noCarriedPedometer : ∀ {ℓ'} (B : A → Type ℓ') (p : x ≡ y)
    → ¬ (Σ[ r ∈ (B x → ℕ) ] Σ[ b ∈ B x ] r (subst B (p ∙ sym p) b) ≡ suc (suc (r b)))
  noCarriedPedometer B p (r , b , up2) =
    snotz (m+n≡n→m≡0 {m = 2} (sym up2 ∙ cong r (roundTripTransportTrivial B p b)))

------------------------------------------------------------------------
-- CG001-C-40  On the circle, additive counters count net displacement, not steps

noAdditiveStepCounter :
  ¬ (Σ[ c ∈ (ΩS¹ → ℕ) ] ((p q : ΩS¹) → c (p ∙ q) ≡ c p + c q) × (c loop ≡ 1))
noAdditiveStepCounter (c , add , c1) = snotz roundTripSteps
  where
  staying : c refl ≡ 0
  staying = m+n≡n→m≡0 (sym (add refl refl) ∙ cong c (sym (rUnit refl)))

  roundTripSteps : suc (c (sym loop)) ≡ 0
  roundTripSteps =
    cong (_+ c (sym loop)) (sym c1)
    ∙ sym (add loop (sym loop))
    ∙ cong c (rCancel loop)
    ∙ staying

netRoundTrip : winding (loop ∙ sym loop) ≡ pos 0
netRoundTrip = refl

------------------------------------------------------------------------
-- CG001-C-41  Journeys as data keep both counts; realized as loops, only the net

data Step : Type where
  fwd back : Step

Journey : Type
Journey = List Step

steps : Journey → ℕ
steps = length

stepLoop : Step → ΩS¹
stepLoop fwd = loop
stepLoop back = sym loop

realize : Journey → ΩS¹
realize [] = refl
realize (s ∷ j) = stepLoop s ∙ realize j

stepNet : Step → ℤ
stepNet fwd = pos 1
stepNet back = negsuc 0

net : Journey → ℤ
net [] = pos 0
net (s ∷ j) = stepNet s +ℤ net j

windingStep : (s : Step) → winding (stepLoop s) ≡ stepNet s
windingStep fwd = refl
windingStep back = refl

realizeKeepsNet : (j : Journey) → winding (realize j) ≡ net j
realizeKeepsNet [] = refl
realizeKeepsNet (s ∷ j) =
  winding-hom (stepLoop s) (realize j) ∙ cong₂ _+ℤ_ (windingStep s) (realizeKeepsNet j)

thereAndBack : Journey
thereAndBack = fwd ∷ back ∷ []

stepsDiffer : (steps thereAndBack ≡ 2) × (steps [] ≡ 0)
stepsDiffer = refl , refl

netAgrees : net thereAndBack ≡ net []
netAgrees = refl

realizedAgree : realize thereAndBack ≡ realize []
realizedAgree = cong (loop ∙_) (sym (rUnit (sym loop))) ∙ rCancel loop

stepCountLost : ¬ (Σ[ c ∈ (ΩS¹ → ℕ) ] ((j : Journey) → c (realize j) ≡ steps j))
stepCountLost (c , agrees) =
  snotz (sym (agrees thereAndBack) ∙ cong c realizedAgree ∙ agrees [])
