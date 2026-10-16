{-# OPTIONS --safe --cubical --guardedness #-}
module GeometricBoundaryObservation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Data.Sigma
open import Cubical.Data.Bool
open import Cubical.Data.Empty
open import Cubical.Data.Int.Base using (ℤ; pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Nat.Properties using (znots)
open import BoundaryIncidence using (noBoundaryPreservingEquivalence)

-- Exact integral boundary coordinates, separately related to actual real curves
-- by StructuredCurve.lean. This module does not encode the whole real curves.
Coord : Type
Coord = ℤ × ℤ

nBoundary mBoundary : Bool → Coord
nBoundary false = pos 0 , pos 0
nBoundary true  = pos 1 , pos 0
mBoundary _    = pos 1 , pos 0

nSeparate : nBoundary false ≡ nBoundary true → ⊥
nSeparate p = znots (injPos (cong fst p))

mCoincident : (u v : Bool) → mBoundary u ≡ mBoundary v
mCoincident _ _ = refl

noCommutingBoundaryEquivalence : (e : Coord ≃ Coord) (labels : Bool ≃ Bool)
  → ((b : Bool) → equivFun e (nBoundary b) ≡ mBoundary (equivFun labels b)) → ⊥
noCommutingBoundaryEquivalence = noBoundaryPreservingEquivalence
  nBoundary mBoundary nSeparate mCoincident

RichDiagram : Type₁
RichDiagram = Σ[ A ∈ Type ] (Bool → A)

nDiagram mDiagram : RichDiagram
nDiagram = Coord , nBoundary
mDiagram = Coord , mBoundary

forgetBoundary : RichDiagram → Type
forgetBoundary = fst

bareCarrierPath : forgetBoundary nDiagram ≡ forgetBoundary mDiagram
bareCarrierPath = refl

EndCoincidence : RichDiagram → Type
EndCoincidence (A , boundary) = boundary false ≡ boundary true

noRichDiagramPath : nDiagram ≡ mDiagram → ⊥
noRichDiagramPath p = nSeparate (subst EndCoincidence (sym p) refl)

noOneBareRecovery : (recover : Type → RichDiagram)
  → recover Coord ≡ nDiagram → recover Coord ≡ mDiagram → ⊥
noOneBareRecovery recover toN toM = noRichDiagramPath (sym toN ∙ toM)

-- Positive control: transport the actual map together with its ambient carrier.
transportDiagram : (e : Coord ≃ Coord)
  → nDiagram ≡ (Coord , λ b → equivFun e (nBoundary b))
transportDiagram e = ΣPathP (ua e , λ i b → ua-gluePathExt e i (nBoundary b))

swapIso : Iso Coord Coord
swapIso = iso (λ p → snd p , fst p) (λ p → snd p , fst p)
  (λ _ → refl) (λ _ → refl)

swappedDiagram : RichDiagram
swappedDiagram = Coord , λ b → equivFun (isoToEquiv swapIso) (nBoundary b)

swappedDiagramPath : nDiagram ≡ swappedDiagram
swappedDiagramPath = transportDiagram (isoToEquiv swapIso)

swappedRightCoordinate : snd swappedDiagram true ≡ (pos 0 , pos 1)
swappedRightCoordinate = refl

swappedStillSeparate : EndCoincidence swappedDiagram → ⊥
swappedStillSeparate = subst (λ D → EndCoincidence D → ⊥) swappedDiagramPath nSeparate
