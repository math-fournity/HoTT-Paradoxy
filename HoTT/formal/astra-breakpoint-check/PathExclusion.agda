{-# OPTIONS --safe --cubical --guardedness #-}
module PathExclusion where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma
open import Cubical.Data.Bool
open import Cubical.Data.Empty as Empty
open import Cubical.HITs.S1.Base
open import Cubical.HITs.S1.Properties using (isConnectedS¹)
import Cubical.HITs.PropositionalTruncation as PT

PathComplement : {ℓ : Level} (A : Type ℓ) → A → Type ℓ
PathComplement A a = Σ[ x ∈ A ] ((x ≡ a) → ⊥)

-- This excludes identity paths, not a point of an underlying topological set.
connectedExclusion : {ℓ : Level} {A : Type ℓ} (a : A)
  → ((x : A) → PT.∥ a ≡ x ∥₁) → PathComplement A a → ⊥
connectedExclusion a conn (x , absent) =
  PT.rec isProp⊥ (λ p → absent (sym p)) (conn x)

circleExclusion : PathComplement S¹ base → ⊥
circleExclusion = connectedExclusion base isConnectedS¹

circleExclusionEquiv : PathComplement S¹ base ≃ ⊥
circleExclusionEquiv = isoToEquiv
  (iso circleExclusion Empty.rec
       (λ ()) (λ x → Empty.rec (circleExclusion x)))

-- Set-level positive control: deleting one Boolean leaves another inhabitant.
setExclusionPositive : PathComplement Bool true
setExclusionPositive = false , false≢true

setComplementIsNotEmpty : (PathComplement Bool true → ⊥) → ⊥
setComplementIsNotEmpty f = f setExclusionPositive

-- The same expression is not uniformly empty on all pointed types.
noUniversalEmptyComplement :
  ((A : Type) (a : A) → PathComplement A a → ⊥) → ⊥
noUniversalEmptyComplement f = f Bool true setExclusionPositive
