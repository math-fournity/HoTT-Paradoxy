{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeCurveTaskControls where

-- Full-field transport succeeds in the same ambient-step task model.
open import hott-z.NativeRealCircleQualification
open import hott-z.StereographicContinuity
open import hott-z.NativeCompletion
open import hott-z.NativeRichCurve
open import hott-z.FiniteTrace
open import hott-z.NativeCurveTask
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.transport-along-identifications
open import foundation.existential-quantification
open import foundation.propositional-truncations

planeIdentity : PointwiseHomeomorphism realPlaneMetric realPlaneMetric
PointwiseHomeomorphism.forward planeIdentity p = p
PointwiseHomeomorphism.backward planeIdentity p = p
PointwiseHomeomorphism.forwardContinuous planeIdentity p =
  intro-exists (λ ε → ε) (λ ε q near → near)
PointwiseHomeomorphism.backwardContinuous planeIdentity p =
  intro-exists (λ ε → ε) (λ ε q near → near)
PointwiseHomeomorphism.forwardBackward planeIdentity p = refl
PointwiseHomeomorphism.backwardForward planeIdentity p = refl

identityStep : (r : RichCurve) → AmbientStep r r
AmbientStep.motion (identityStep r) = planeIdentity
AmbientStep.commutes (identityStep r) u = refl

richPathStep : {r s : RichCurve} → r ＝ s → AmbientStep r s
richPathStep {r} p = tr (AmbientStep r) p (identityStep r)

fullTransportStep : AmbientStep mRich transportedRich
fullTransportStep = richPathStep fullTransportPath

fullTransportSuccess : Success (mRich , transportedRich)
fullTransportSuccess = transportedRich , step fullTransportStep stop , refl

mereFullTransportSuccess : MereSuccess (mRich , transportedRich)
mereFullTransportSuccess = unit-trunc-Prop fullTransportSuccess
