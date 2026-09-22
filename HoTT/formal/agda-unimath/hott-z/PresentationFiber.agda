{-# OPTIONS --without-K --exact-split #-}
module hott-z.PresentationFiber where

-- The strict/dependent fiber of Bare records presentations of one fixed carrier.
-- It is a P1 object-theory control, not an assertion about a HoTT consumer.
open import hott-z.NativeRichCurve
open import hott-z.NativeRealCircleQualification
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.negation

PresentationFiber : UU (lsuc lzero) → UU (lsuc (lsuc lzero))
PresentationFiber A = Σ RichCurve (λ r → Bare r ＝ A)

transportedMInOpenFiber : PresentationFiber OpenRealInterval
transportedMInOpenFiber = transportedRich , refl

nInOpenFiber : PresentationFiber OpenRealInterval
nInOpenFiber = nRich , refl

transportedFiberClosed : EndCoincidence (pr1 transportedMInOpenFiber)
transportedFiberClosed = fullTransportKeepsEnds

nFiberNotClosed : ¬ (EndCoincidence (pr1 nInOpenFiber))
nFiberNotClosed = nSeparate

noTransportedRichPath : ¬ (transportedRich ＝ nRich)
noTransportedRichPath p = noRichPath (fullTransportPath ∙ p)

noOpenFiberPath : ¬ (transportedMInOpenFiber ＝ nInOpenFiber)
noOpenFiberPath p = noTransportedRichPath (ap pr1 p)
