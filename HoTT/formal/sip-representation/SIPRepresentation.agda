{-# OPTIONS --safe --cubical --guardedness #-}

-- N8: minimal native Cubical boundary for the structure-identity principle
-- (SIP) as a substitutivity license.  Two pointed structures are identified by
-- ua (the pointed-structure instance of SIP), but an observable outside the
-- signature differs on them; no function out of the structure type can recover
-- it.  Adding the observable to the signature prevents the identification and
-- recovers it (positive control).
module SIPRepresentation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.Data.Bool
open import Cubical.Data.Bool.Properties

¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
¬ A = A → ⊥

------------------------------------------------------------------------
-- Signature: pointed types.  s and t are isomorphic pointed structures.

Str : Type₁
Str = Σ[ X ∈ Type₀ ] X

s : Str
s = Bool , true

t : Str
t = Bool , false

-- The outside-signature observable values: the raw point components of s and t.
-- There is no total function Str -> Bool returning them, because the carrier of
-- a pointed structure is abstract; the values are only available with the extra
-- representation data "carrier is Bool".
observable-s : Bool
observable-s = true

observable-t : Bool
observable-t = false

------------------------------------------------------------------------
-- C-124: native SIP/UA identification of the two pointed structures.

C-124-ua-transport : transport (ua notEquiv) true ≡ false
C-124-ua-transport = uaβ notEquiv true

C-124-identification : s ≡ t
C-124-identification = ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))

-- C-125: the outside-signature observable differs on s and t.
C-125-obs-differs : ¬ (observable-s ≡ observable-t)
C-125-obs-differs = true≢false

-- C-126: every Bool-valued function on Str is constant on the identified pair.
C-126-any-function-constant : (f : Str → Bool) → f s ≡ f t
C-126-any-function-constant f = cong f C-124-identification

-- C-127: no uniform recovery of the outside-signature observable.
C-127-no-recovery :
  ¬ (Σ[ f ∈ (Str → Bool) ] (f s ≡ true) × (f t ≡ false))
C-127-no-recovery (f , hs , ht) =
  true≢false (sym hs ∙ cong f C-124-identification ∙ ht)

------------------------------------------------------------------------
-- Refinement positive control: put the observable into the signature.

Str' : Type₁
Str' = Σ[ X ∈ Type₀ ] Σ[ x ∈ X ] Bool

s' : Str'
s' = Bool , true , true

t' : Str'
t' = Bool , false , false

obs' : Str' → Bool
obs' (_ , _ , b) = b

-- C-128: in the refined structure the observable is part of identity: the
-- projection recovers it and the two structures are not identified.
C-128-obs'-differs : ¬ (obs' s' ≡ obs' t')
C-128-obs'-differs = true≢false

C-128-no-identification : ¬ (s' ≡ t')
C-128-no-identification q = true≢false (cong (λ z → snd (snd z)) q)
