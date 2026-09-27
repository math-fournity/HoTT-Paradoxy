{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Q7 (work order §3): independent line-by-line check of GLM's
  NoHitGroupoidUniverse.agda.  Every intermediate step of GLM's proof is
  restated here WITH ITS TYPE WRITTEN OUT, so that the kernel confirms the
  auditor's reading of each step (direction of the τ≠refl chain, the
  definitional unfoldings the proof relies on, the h-level bookkeeping, and
  that isOfHLevel 3 is literally isGroupoid).  Claim COPUS-Q7-C01.
-}
module Q7AnnotatedReplay where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_ ; idEquiv ; equivEq)
open import Cubical.Foundations.Univalence using (ua ; uaβ ; univalence)
open import Cubical.Foundations.HLevels using (isOfHLevel ; isOfHLevelRespectEquiv)
open import Cubical.Data.Bool using (Bool ; true ; false ; true≢false)
open import Cubical.Data.Sigma using (_×_ ; fst ; snd)
open import Cubical.Relation.Nullary using (¬_)
open import NoHitGroupoidUniverse
  using (B ; Loop ; X ; a ; ea ; c₀ ; τ ; D ; FAM ; ¬universeIsGroupoid)

-- (Q7-1) The declared statement is the groupoid statement, verbatim:
--        isOfHLevel 3 is definitionally isGroupoid.
hlevel3≡isGroupoid : (A : Type (ℓ-suc ℓ-zero)) → isOfHLevel 3 A ≡ isGroupoid A
hlevel3≡isGroupoid A = refl

-- (Q7-2) The concrete computation behind non-triviality.
a-moves : a (true , true) ≡ (false , true)
a-moves = refl

-- (Q7-3) τ's first component is definitionally ua ea.
fst-τ : cong fst τ ≡ ua ea
fst-τ = refl

-- (Q7-4) GLM's τ≠refl with every intermediate type written out.
--        Direction: (tt,tt) ≡ transport refl (tt,tt) ≡ transport (ua ea) (tt,tt) ≡ (ff,tt).
τ≠refl-annotated : ¬ (τ ≡ refl)
τ≠refl-annotated h = true≢false (cong fst chain)
  where
  t1 : transport (ua ea) (true , true) ≡ (false , true)
  t1 = uaβ ea (true , true)
  t2 : transport (ua ea) (true , true) ≡ transport refl (true , true)
  t2 = cong (λ e → transport e (true , true)) (cong (cong fst) h)
  t3 : transport refl (true , true) ≡ (true , true)
  t3 = transportRefl (true , true)
  chain : (true , true) ≡ (false , true)
  chain = sym t3 ∙ sym t2 ∙ t1

-- (Q7-5) FAM's first projection returns the point's own loop, definitionally
--        (so D's filler content is never inspected by the contradiction).
fst-FAM : (x : Loop ℓ-zero) → cong fst (FAM x) ≡ snd x
fst-FAM x = refl

-- (Q7-6) Evaluating the equivalence-loop at a point is definitionally FAM there.
eval-loopE : cong (λ e → e .fst (c₀ , τ))
               (equivEq {e = idEquiv (Loop ℓ-zero)} {f = idEquiv (Loop ℓ-zero)} (funExt FAM))
             ≡ FAM (c₀ , τ)
eval-loopE = refl

-- (Q7-7) The h-level bookkeeping of forceEquivLoop: a groupoid universe makes
--        the self-equivalences of Loop a set (univalence transfer).
setOfSelfEquivs : isOfHLevel 3 (Type (ℓ-suc ℓ-zero)) → isSet (Loop ℓ-zero ≃ Loop ℓ-zero)
setOfSelfEquivs G = isOfHLevelRespectEquiv 2 univalence (G (Loop ℓ-zero) (Loop ℓ-zero))

-- (Q7-8) The theorem, re-exported with its declared type (no weakening).
Q7-theorem : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))
Q7-theorem = ¬universeIsGroupoid
