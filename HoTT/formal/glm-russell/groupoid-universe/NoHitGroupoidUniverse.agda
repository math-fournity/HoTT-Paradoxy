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

-- TODO (kernel, next session): conjugation lemma
--   transport (λ i → ρ i ≡ ρ i) τ ≡ sym ρ ∙ τ ∙ ρ (orientation TBD);
-- then: q := cong (λ c → c ≡ c) ρ at c0 := (X , X-isSet) is a loop in
-- Type l1 at the member (c0 ≡ c0); q = refl would force the conjugated
-- b-loop to equal the b-loop, refuted by a∘b≠b∘a after pathToEquiv/ua
-- normalisation; assemble
--   ¬ isOfHLevel 3 (Type (ℓ-suc ℓ)).
