{-# OPTIONS --safe --cubical --guardedness #-}
module OriginDirectedDiagram where

-- This is a minimal native Cubical Agda interface control.  It records that
-- boundary/source data, a process label, an observation label and a completion
-- label can be kept together.  It does not claim to encode the full real
-- circle/interval process or a physical notion of completion.

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.Data.Empty
open import Cubical.Data.Sigma
open import GeometricBoundaryObservation using
  ( RichDiagram ; nDiagram ; mDiagram ; forgetBoundary
  ; EndCoincidence ; nSeparate ; noRichDiagramPath
  ; swappedDiagram ; swappedDiagramPath )

OriginDirectedDiagram : Type₁
OriginDirectedDiagram = Σ[ static ∈ RichDiagram ]
  ((Bool → Bool) × Bool)

staticPart : OriginDirectedDiagram → RichDiagram
staticPart = fst

tracePart : OriginDirectedDiagram → Bool → Bool
tracePart D = fst (snd D)

doneLabel : OriginDirectedDiagram → Bool
doneLabel D = snd (snd D)

bareOrigin : OriginDirectedDiagram → Type
bareOrigin D = forgetBoundary (staticPart D)

liftStatic : RichDiagram → OriginDirectedDiagram
liftStatic static = static , (λ b → b) , true

originN originM : OriginDirectedDiagram
originN = liftStatic nDiagram
originM = liftStatic mDiagram

sameBareCarrier : bareOrigin originN ≡ bareOrigin originM
sameBareCarrier = refl

OriginEndCoincidence : OriginDirectedDiagram → Type
OriginEndCoincidence D = EndCoincidence (staticPart D)

noOriginPath : originN ≡ originM → ⊥
noOriginPath p = noRichDiagramPath (cong staticPart p)

noOneBareOriginRecovery : (recover : Type → OriginDirectedDiagram)
  → recover (bareOrigin originN) ≡ originN
  → recover (bareOrigin originM) ≡ originM
  → ⊥
noOneBareOriginRecovery recover toN toM =
  noOriginPath (sym toN ∙ toM)

-- Positive control: when all fields are retained, a transported static
-- diagram together with the unchanged trace/done labels remains an origin
-- diagram.  This refutes the stronger claim that the framework cannot carry
-- source/boundary/process/completion labels at all.
swappedOrigin : OriginDirectedDiagram
swappedOrigin = liftStatic swappedDiagram

originTransport : originN ≡ swappedOrigin
originTransport = cong liftStatic swappedDiagramPath

transportPreservesTrace : tracePart originN ≡ tracePart swappedOrigin
transportPreservesTrace = refl

transportPreservesDone : doneLabel originN ≡ doneLabel swappedOrigin
transportPreservesDone = refl
