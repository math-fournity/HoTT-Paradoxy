{-# OPTIONS --safe --cubical --guardedness #-}

module NoCanonicalPoint where

-- MP-NOCANONICAL-001 / C-142–C-147: the no-canonical-point fence for
-- *unlabeled* two-element presentations in the pinned Cubical toolchain
-- (Agda 2.8.0 + Cubical v0.9).
--
-- This is the native replay, inside this repository, of the statement carried
-- by the derived development file
-- `HoTT/formal/agda-unimath/hott-z/NoCanonicalPoint.agda` (there phrased as
-- agda-unimath's `no-section-type-2-Element-Type`:
-- `¬ ((X : 2-Element-Type l) → type-2-Element-Type X)`).  The library body
-- itself is not vendored here, so the derived file stays
-- `SOURCE_REPORTED_NOT_REPLAYED`; this module replays the *statement* with the
-- pinned toolchain's own primitives.
--
-- Why a separate module: `TruncationNoRecovery.agda` (C-134–C-141) is frozen
-- byte-identically so that runs -01/-02/-03 keep passing their source pinning
-- and row-stability checks.  Claim IDs are appended (C-142+), never rewritten.
--
-- N38 -> N40 correction (recorded, not hidden).  The N38 probe file listed the
-- section-level statement
--
--   (s : (b : Bool) → carrier (boolPresentation b)) → s false ≡ s true
--
-- as "the correct constant version" of the phenomenon.  That statement is
-- *false* as literally written: the presentation family is definitionally
-- constant, so the type is just `Bool → Bool`, and `s = id` refutes it.  A
-- plain dependent function over `Bool` carries no coherence obligation, and no
-- eliminator shape can repair that.  The correct content is the no-uniform-
-- choice statement below: a choice for *every* unlabeled presentation must
-- respect that presentation's own identifications, and the swap automorphism
-- of Bool then forces the chosen point to be a fixed point of `not`.

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
  using (idEquiv; invEq; equivFun; _≃_)
open import Cubical.Data.Bool.Base
  using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties
  using (notEquiv; not≢const; false≢true)
open import Cubical.Data.Empty.Base
  using (⊥)
open import Cubical.Data.Sigma.Properties
  using (ΣPathP)
open import Cubical.Foundations.Univalence
  using (ua; uaβ)
open import Cubical.HITs.PropositionalTruncation.Base
  using (∥_∥₁; ∣_∣₁)
open import Cubical.HITs.PropositionalTruncation.Properties
  using (isPropPropTrunc)

-- C-142: an unlabeled two-element presentation is a carrier together with the
-- *mere existence* of an identification with Bool.  Unlike C-141's `isFinSet`
-- shape the label type is pinned to Bool, so no arithmetic remains.
UnlabeledTwoElement : Type₁
UnlabeledTwoElement = Σ[ A ∈ Type ] (∥ A ≃ Bool ∥₁)

unlabeledCarrier : UnlabeledTwoElement → Type
unlabeledCarrier = fst

-- The identity-labeled presentation.
identityPresentation : UnlabeledTwoElement
identityPresentation = Bool , ∣ idEquiv Bool ∣₁

-- C-142 (continued): the swap automorphism of Bool induces a nontrivial
-- *self*-identification of the unlabeled presentation.  The carrier component
-- of the path is `ua notEquiv`, whose transport computes as `not` (C-144 uses
-- that computation rule); the labeling component is filled purely by
-- propositionality of the truncation.  This is what forgetting the labeling
-- means internally: the identity and the swap presentations become one
-- element of the interface, and the only identification the choice can see is
-- the nontrivial one.
swapSelfIdentification : identityPresentation ≡ identityPresentation
swapSelfIdentification =
  ΣPathP {A = λ _ → Type} {B = λ _ A → ∥ A ≃ Bool ∥₁}
    (ua notEquiv , isProp→PathP (λ _ → isPropPropTrunc) _ _)

-- C-143: a section of the unlabeled family must respect the identifications of
-- that family.  Recorded in transport form (`subst`) so that it can be composed
-- with `ua`'s computation rule.  This is the coherence obligation that a
-- function over a discrete index would not have.
sectionRespectsSelfIdentification :
  (u : (X : UnlabeledTwoElement) → unlabeledCarrier X)
  → subst unlabeledCarrier swapSelfIdentification (u identityPresentation)
  ≡ u identityPresentation
sectionRespectsSelfIdentification u =
  J (λ (Y : UnlabeledTwoElement) (q : identityPresentation ≡ Y)
     → subst unlabeledCarrier q (u identityPresentation) ≡ u Y)
    (substRefl {B = unlabeledCarrier} {x = identityPresentation}
      (u identityPresentation))
    swapSelfIdentification

-- C-144: composing C-143 with `uaβ notEquiv` forces any hypothetical uniform
-- choice to be a fixed point of the swap: `not` of the chosen point equals the
-- chosen point.
uniformChoiceFixedPoint :
  (u : (X : UnlabeledTwoElement) → unlabeledCarrier X)
  → not (u identityPresentation) ≡ u identityPresentation
uniformChoiceFixedPoint u =
  sym (uaβ notEquiv (u identityPresentation))
  ∙ sectionRespectsSelfIdentification u

-- C-145: hence there is no uniform choice of a point for every unlabeled
-- two-element presentation.  The obstruction is the automatic heightening of
-- a choice into a transport-coherent one, not the existence of a labeling.
noUniformChoice :
  ((X : UnlabeledTwoElement) → unlabeledCarrier X) → ⊥
noUniformChoice u =
  not≢const (u identityPresentation) (uniformChoiceFixedPoint u)

-- C-146: positive control.  When the labeling is retained as data (no
-- truncation), the canonical choice exists; the fence is about the forgotten
-- labeling, not about two-element carriers.
LabeledTwoElement : Type₁
LabeledTwoElement = Σ[ A ∈ Type ] (A ≃ Bool)

labeledChoice : (X : LabeledTwoElement) → fst X
labeledChoice X = invEq (snd X) true

-- C-147: the interface identifies the two labelings as elements while the
-- labelings themselves remain different data.  Together with C-146 this fixes
-- exactly what the truncation forgets: the specific identification with Bool.
labelingsIdentified :
  (Bool , ∣ idEquiv Bool ∣₁) ≡ (Bool , ∣ notEquiv ∣₁)
labelingsIdentified =
  ΣPathP {A = λ _ → Type} {B = λ _ A → ∥ A ≃ Bool ∥₁}
    (refl , isProp→PathP (λ _ → isPropPropTrunc) _ _)

labelingsDistinct : idEquiv Bool ≡ notEquiv → ⊥
labelingsDistinct p =
  false≢true (cong (λ e → equivFun e false) p)

-- C-148: the carrier component of the self-identification is *not* the
-- identity path, i.e. the self-identification is nontrivial.  If
-- `ua notEquiv ≡ refl`, then transporting `true` along both sides gives
-- `not true ≡ true`, which contradicts `not≢const`.
uaNotEquivNotRefl : ua notEquiv ≡ refl → ⊥
uaNotEquivNotRefl p =
  not≢const true
    (sym (uaβ notEquiv true)
    ∙ cong (λ q → transport q true) p
    ∙ transportRefl true)
