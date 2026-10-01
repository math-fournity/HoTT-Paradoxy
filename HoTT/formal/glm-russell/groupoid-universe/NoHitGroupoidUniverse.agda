{-# OPTIONS --safe --cubical --guardedness #-}

-- M1c COMPLETE (units 1-3, GLM-R3-C01): HIT-free proof that the
-- universe Type (ℓ-suc ℓ-zero) is NOT a groupoid (KS n=1 instance).
-- Kernel: the self-sliding square D via compPathL→PathP + path
-- algebra; the KS xi-family FAM via ΣPathP (q , D q); nontriviality at
-- (c₀ , τ) with τ the a-loop; assembly via univalence transfer and
-- equivEq.  See REVISIONS.md for the full attempt history.

module NoHitGroupoidUniverse where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_ ; isEquiv ; idEquiv ;
  equivEq)
open import Cubical.Foundations.Isomorphism using (iso ; isoToIsEquiv)
open import Cubical.Foundations.Univalence using (ua ; uaβ ; univalence)
open import Cubical.Foundations.GroupoidLaws using (assoc ; lCancel ; lUnit)
open import Cubical.Foundations.Path using (compPathL→PathP)
open import Cubical.Foundations.HLevels using (isOfHLevel ; isSet× ;
  isPropIsSet ; isOfHLevelRespectEquiv)
open import Cubical.Data.Bool using (Bool ; true ; false ; not ; notnot ;
  true≢false)
open import Cubical.Data.Bool.Properties using (isSetBool)
open import Cubical.Data.Sigma using (_×_ ; fst ; snd)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Relation.Nullary using (¬_)

-- The subuniverse of sets (KS: U^{<=0}), a member of Type l1.
B : (ℓ : Level) → Type (ℓ-suc ℓ)
B ℓ = Σ (Type ℓ) (λ X → isSet X)

-- The self-referential member (KS: Loop_0 shape, restricted use):
-- points of B together with their own loop data.
Loop : (ℓ : Level) → Type (ℓ-suc ℓ)
Loop ℓ = Σ (B ℓ) (λ b → b ≡ b)

-- The base set: Bool * Bool with its two involutions.
X : Type
X = Bool × Bool

a : X → X
a (x , y) = (not x , y)

flip2 : Bool → Bool → Bool
flip2 true y = not y
flip2 false y = y

b : X → X
b (x , y) = (x , flip2 x y)

-- Machine-checkable computational fact: a and b do NOT commute,
-- witnessed at (true,true):  a (b tt,tt) = (false,false) but
-- b (a tt,tt) = (false,true).
a∘b≠b∘a : ¬ ((p : X) → a (b p) ≡ b (a p))
a∘b≠b∘a h = true≢false (sym (cong snd (h (true , true))))

a-invol : (p : X) → a (a p) ≡ p
a-invol (x , y) i = (notnot x i , y)

b-invol : (p : X) → b (b p) ≡ p
b-invol (true , y) i = (true , notnot y i)
b-invol (false , y) i = (false , y)

a-isEquiv : isEquiv a
a-isEquiv = isoToIsEquiv (iso a a a-invol a-invol)

b-isEquiv : isEquiv b
b-isEquiv = isoToIsEquiv (iso b b b-invol b-invol)

X-isSet : isSet X
X-isSet = isSet× isSetBool isSetBool

----------------------------------------------------------------------
-- The kernel (M1c unit 2): the self-sliding square, landed.
-- For any loop q : b ≡ b, D q : PathP (λ i → q i ≡ q i) q q — the square
-- underlying "a loop is a loop at each of its own points".  Route:
-- compPathL→PathP applied to pure path algebra
-- (sym q ∙ q ∙ q ≡ (sym q ∙ q) ∙ q ≡ refl ∙ q ≡ q).  All propositional;
-- no definitional walls (session-end obstruction resolved).
----------------------------------------------------------------------

D : ∀ {ℓ} {C : Type ℓ} {b : C} (q : b ≡ b) → PathP (λ i → q i ≡ q i) q q
D q = compPathL→PathP
  ( (sym q ∙ q ∙ q) ≡⟨ assoc (sym q) q q ⟩
    ((sym q ∙ q) ∙ q) ≡⟨ cong (λ s → s ∙ q) (lCancel q) ⟩
    (refl ∙ q) ≡⟨ sym (lUnit q) ⟩ q ∎ )

-- The KS xi-family: every point of Loop carries its own loop data as a
-- loop AT itself.
FAM : {ℓ : Level} (x : Loop ℓ) → x ≡ x
FAM (b , q) = ΣPathP (q , D q)

----------------------------------------------------------------------
-- Nontriviality witness at the concrete point.
----------------------------------------------------------------------

ea : X ≃ X
ea = (a , a-isEquiv)

c₀ : B ℓ-zero
c₀ = (X , X-isSet)

-- The a-loop at c₀ (a Σ-path over ua of the a-equivalence).
τ : c₀ ≡ c₀
τ = ΣPathP (ua ea ,
            isProp→PathP (λ i → isPropIsSet {A = ua ea i}) X-isSet X-isSet)

τ≠refl : ¬ (τ ≡ refl)
τ≠refl h = true≢false (cong fst chain)
  where
  t1 = uaβ ea (true , true)
  t2 = cong (λ e → transport e (true , true)) (cong (cong fst) h)
  t3 = transportRefl (true , true)
  chain = sym t3 ∙ sym t2 ∙ t1

-- Standalone forcing lemma (pattern validated in isolation).
forceEquivLoop : {ℓ : Level} (G : isOfHLevel 3 (Type (ℓ-suc ℓ)))
                 (L : Type (ℓ-suc ℓ)) (e : L ≃ L) (p : e ≡ e) → p ≡ refl
forceEquivLoop G L e p =
  isOfHLevelRespectEquiv 2 univalence (G L L) e e p refl

-- GLM-R3-C01: the universe Type (ℓ-suc ℓ-zero) is NOT a groupoid,
-- HIT-free (KS n=1 instance).  Suppose G.  Then Loop ≃ Loop is a set
-- (univalence transfer of G Loop Loop).  The FAM-family gives a loop
-- at idEquiv; set-ness forces it to refl; evaluating at the concrete
-- point (c₀ , τ) and projecting the first component forces τ ≡ refl
-- — refuted above.
¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))
¬universeIsGroupoid G = τ≠refl τIsRefl
  where
  L : Type (ℓ-suc ℓ-zero)
  L = Loop ℓ-zero

  theId : L ≃ L
  theId = idEquiv L

  FAML : (x : L) → x ≡ x
  FAML x = FAM x

  loopE : theId ≡ theId
  loopE = equivEq (funExt FAML)

  forced : loopE ≡ refl
  forced = forceEquivLoop G L theId loopE

  atPt : FAML (c₀ , τ) ≡ refl
  atPt = cong (cong (λ e → e .fst (c₀ , τ))) forced

  τIsRefl : τ ≡ refl
  τIsRefl = cong (cong fst) atPt
