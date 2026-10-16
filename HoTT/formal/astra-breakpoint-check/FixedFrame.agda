{-# OPTIONS --safe --cubical --guardedness #-}
module FixedFrame where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import Cubical.Data.Sigma
open import Cubical.Data.Bool
open import Cubical.Data.Empty

Bare : Type₁
Bare = Σ[ X ∈ Type ] X

leftBare rightBare : Bare
leftBare = Bool , true
rightBare = Bool , false

bareIdentification : leftBare ≡ rightBare
bareIdentification = ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))

noBareReadout :
  (Σ[ f ∈ (Bare → Bool) ] ((f leftBare ≡ true) × (f rightBare ≡ false))) → ⊥
noBareReadout (f , l , r) = true≢false (sym l ∙ cong f bareIdentification ∙ r)

-- A reference equivalence, not an unrelated Boolean tag.
FrameData : Type → Type
FrameData X = X × (X ≃ Bool)

Framed : Type₁
Framed = Σ[ X ∈ Type ] FrameData X

observe : Framed → Bool
observe (X , x , e) = equivFun e x

leftFixed rightFixed : Framed
leftFixed = Bool , true , idEquiv Bool
rightFixed = Bool , false , idEquiv Bool

fixedFrameSeparates : (leftFixed ≡ rightFixed) → ⊥
fixedFrameSeparates p = true≢false (cong observe p)

-- Reparameterize both point and reference map by one and the same path.
reparameterized : Framed
reparameterized = Bool , subst FrameData (ua notEquiv) (true , idEquiv Bool)

reparameterizationPath : leftFixed ≡ reparameterized
reparameterizationPath = ΣPathP (ua notEquiv , toPathP refl)

referenceObservationPreserved : observe reparameterized ≡ true
referenceObservationPreserved = sym (cong observe reparameterizationPath)

forget : Framed → Bare
forget (X , x , e) = X , x

forgottenPairIdentified : forget leftFixed ≡ forget rightFixed
forgottenPairIdentified = bareIdentification
