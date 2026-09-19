{-# OPTIONS --safe --cubical --guardedness #-}
module EliminationControls where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Univalence
open import Cubical.Data.Sigma
open import Cubical.Data.Bool
open import Cubical.Data.Unit
open import Cubical.Data.Empty
import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ

-- Original-witness recovery is stronger than merely choosing some Boolean.
noOriginalWitness :
  (Σ[ f ∈ (PT.∥ Bool ∥₁ → Bool) ] ((b : Bool) → f PT.∣ b ∣₁ ≡ b)) → ⊥
noOriginalWitness (f , law) = true≢false
  (sym (law true) ∙ cong f (PT.squash₁ PT.∣ true ∣₁ PT.∣ false ∣₁) ∙ law false)

uniqueRecovery : {ℓ : Level} {A : Type ℓ} → isProp A → PT.∥ A ∥₁ → A
uniqueRecovery prop = PT.rec prop (λ x → x)

unitRecovery : uniqueRecovery isPropUnit PT.∣ tt ∣₁ ≡ tt
unitRecovery = refl

Q : Type
Q = Bool SQ./ (λ _ _ → Unit)

noRepresentativeRecovery :
  (Σ[ f ∈ (Q → Bool) ] ((b : Bool) → f SQ.[ b ] ≡ b)) → ⊥
noRepresentativeRecovery (f , law) = true≢false
  (sym (law true) ∙ cong f (SQ.eq/ true false tt) ∙ law false)

lawfulObservation : Q → Bool
lawfulObservation = SQ.rec isSetBool (λ _ → true) (λ _ _ _ → refl)

-- BP-C11: genuine composition of native transport, quotient and consumer.
combined : Bool → Bool
combined b = lawfulObservation SQ.[ transport (ua notEquiv) b ]

combinedPreservesDeclaredObservation : (b : Bool) → combined b ≡ true
combinedPreservesDeclaredObservation b = refl

-- A legal data-valued truncated consumer with the additional constancy law.
chosenConstant : PT.∥ Bool ∥₁ → Bool
chosenConstant _ = true
