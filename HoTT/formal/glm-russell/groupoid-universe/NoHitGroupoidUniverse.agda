{-# OPTIONS --safe --cubical --guardedness #-}

-- M1c: HIT-free proof that Type l1 is NOT a groupoid (KS n=1 instance),
-- simplified route (design doc: GLM-5.3-Flash/M1c设计书).  SCAFFOLD:
-- this file currently delivers the definitions and the computational
-- fact (two involutions of Bool*Bool do not commute); the hard kernel
-- lemma (transport-in-path-family = conjugation) and the final assembly
-- are marked TODO and NOT claimed.  No claim IDs issued yet.

module NoHitGroupoidUniverse where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (isEquiv)
open import Cubical.Foundations.Isomorphism using (iso ; isoToIsEquiv)
open import Cubical.Foundations.Univalence using (ua ; pathToEquiv)
open import Cubical.Foundations.HLevels using (isSet×)
open import Cubical.Data.Bool using (Bool ; true ; false ; not ; notnot ;
  true≢false)
open import Cubical.Data.Bool.Properties using (isSetBool)
open import Cubical.Data.Sigma using (_×_ ; fst ; snd)
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

-- TODO (kernel, unit 2) — SHAPE RESOLVED (2026-09-26 session-end note):
-- the ABSTRACT conjugation lemma below is ILL-TYPED: for abstract rho,
-- neither `PathP (λ i → rho i ≡ rho i) tau sigma` nor
-- `transport (λ i → rho i ≡ rho i) tau` accept tau : c ≡ c, because
-- rho i0 does not reduce for an abstract path.  With the CONCRETE
-- rho := Σ-path (ua ea, isProp→PathP part) everything changes: ua has
-- definitional boundary, so rho i0 ≡ c0 definitionally and all
-- PathP/transport statements typecheck with computable endpoints.
-- Unit 2 therefore works with concrete rho/tau at c0 := (X , X-isSet):
--   q := cong (λ c → c ≡ c) rho : (c0 ≡ c0) ≡ (c0 ≡ c0)
--   h : q ≡ refl (from isOfHLevel 3 (Type (ℓ-suc ℓ)))
--   cong (transport-at-tau) h gives transport q tau ≡ tau
-- refute by computing transport q tau's first Σ-component as the
-- conjugated equivalence (ua-normalisation + a/b facts), landing on
-- a∘b≠b∘a.  Tools: fromPathP/toPathP/PathPIsoPath (Foundations.Path),
-- ua-beta lemmas, doubleCompPath-filler (faces now reducible).
-- No claim IDs issued yet.
