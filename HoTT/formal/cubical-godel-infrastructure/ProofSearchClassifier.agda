{-# OPTIONS --cubical --safe --guardedness #-}

module ProofSearchClassifier where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty as Empty
open import Agda.Builtin.Equality renaming (_≡_ to _≡b_; refl to reflb)
open import MiniProofChecker
import NatProofCode as NP
import SyntheticIncompleteness as SI

builtin→Path : {A : Type} {x y : A} → x ≡b y → x ≡ y
builtin→Path reflb = refl

------------------------------------------------------------------------
-- A Boolean semantics proving consistency of the K/S/MP calculus.

impB : Bool → Bool → Bool
impB false b = true
impB true b = b

evalF : (ℕ → Bool) → Fml → Bool
evalF valuation (atom n) = valuation n
evalF valuation bot = false
evalF valuation (φ ⇒ ψ) = impB (evalF valuation φ) (evalF valuation ψ)

impK-valid : (a b : Bool) → impB a (impB b a) ≡ true
impK-valid false false = refl
impK-valid false true = refl
impK-valid true false = refl
impK-valid true true = refl

impS-valid : (a b c : Bool)
           → impB (impB a (impB b c))
               (impB (impB a b) (impB a c))
           ≡ true
impS-valid false false false = refl
impS-valid false false true = refl
impS-valid false true false = refl
impS-valid false true true = refl
impS-valid true false false = refl
impS-valid true false true = refl
impS-valid true true false = refl
impS-valid true true true = refl

imp-mp-valid : (a b : Bool)
             → impB a b ≡ true → a ≡ true → b ≡ true
imp-mp-valid false b implication aTrue = Empty.rec (false≢true aTrue)
imp-mp-valid true false implication aTrue = Empty.rec (false≢true implication)
imp-mp-valid true true implication aTrue = refl

derivation-valid : {φ : Fml} → ⊢ φ → (valuation : ℕ → Bool)
                 → evalF valuation φ ≡ true
derivation-valid (axK φ ψ) valuation =
  impK-valid (evalF valuation φ) (evalF valuation ψ)
derivation-valid (axS φ ψ χ) valuation =
  impS-valid (evalF valuation φ) (evalF valuation ψ) (evalF valuation χ)
derivation-valid (mp {φ} {ψ} implication premise) valuation =
  imp-mp-valid (evalF valuation φ) (evalF valuation ψ)
    (derivation-valid implication valuation)
    (derivation-valid premise valuation)

no-bot : ⊢ bot → Empty.⊥
no-bot derivation = false≢true (derivation-valid derivation (λ n → true))

negF : Fml → Fml
negF φ = φ ⇒ bot

no-proof-and-refutation : {φ : Fml} → ⊢ φ → ⊢ negF φ → Empty.⊥
no-proof-and-refutation proof refutation = no-bot (mp refutation proof)

------------------------------------------------------------------------
-- Stage n checks proof code n on the positive and negative sides.

proofCore : Fml → ℕ → SI.OptionBool
proofCore φ code with NP.checkProofNat code φ | NP.checkProofNat code (negF φ)
... | true | negative = SI.some true
... | false | true = SI.some false
... | false | false = SI.none

core-true→check : (φ : Fml) (code : ℕ)
                → proofCore φ code ≡ SI.some true
                → NP.checkProofNat code φ ≡ true
core-true→check φ code with NP.checkProofNat code φ | NP.checkProofNat code (negF φ)
... | true | negative = λ equality → refl
... | false | true = λ equality →
  Empty.rec (false≢true (SI.some-injective equality))
... | false | false = λ equality → Empty.rec (SI.none≢some equality)

core-false→check-neg : (φ : Fml) (code : ℕ)
                     → proofCore φ code ≡ SI.some false
                     → NP.checkProofNat code (negF φ) ≡ true
core-false→check-neg φ code
  with NP.checkProofNat code φ | NP.checkProofNat code (negF φ)
... | true | negative = λ equality →
  Empty.rec (false≢true (sym (SI.some-injective equality)))
... | false | true = λ equality → refl
... | false | false = λ equality → Empty.rec (SI.none≢some equality)

check→core-true : (φ : Fml) (code : ℕ)
                → NP.checkProofNat code φ ≡ true
                → proofCore φ code ≡ SI.some true
check→core-true φ code with NP.checkProofNat code φ | NP.checkProofNat code (negF φ)
... | true | negative = λ equality → refl
... | false | negative = λ equality → Empty.rec (false≢true equality)

check-neg→core-false : (φ : Fml) (code : ℕ)
                     → NP.checkProofNat code (negF φ) ≡ true
                     → proofCore φ code ≡ SI.some false
check-neg→core-false φ code
  with NP.checkProofNat code φ in positive
     | NP.checkProofNat code (negF φ) in negative
... | true | true = λ equality → Empty.rec
  (no-proof-and-refutation
    (NP.natChecked-sound {φ = φ} (code , builtin→Path positive))
    (NP.natChecked-sound {φ = negF φ} (code , builtin→Path negative)))
... | true | false = λ equality → Empty.rec (false≢true equality)
... | false | true = λ equality → refl
... | false | false = λ equality → Empty.rec (false≢true equality)

proofCore-deterministic : (φ : Fml) (b₁ b₂ : Bool) (c₁ c₂ : ℕ)
                        → proofCore φ c₁ ≡ SI.some b₁
                        → proofCore φ c₂ ≡ SI.some b₂
                        → b₁ ≡ b₂
proofCore-deterministic φ false false c₁ c₂ first second = refl
proofCore-deterministic φ false true c₁ c₂ first second = Empty.rec
  (no-proof-and-refutation
    (NP.natChecked-sound {φ = φ}
      (c₂ , core-true→check φ c₂ second))
    (NP.natChecked-sound {φ = negF φ}
      (c₁ , core-false→check-neg φ c₁ first)))
proofCore-deterministic φ true false c₁ c₂ first second = Empty.rec
  (no-proof-and-refutation
    (NP.natChecked-sound {φ = φ}
      (c₁ , core-true→check φ c₁ first))
    (NP.natChecked-sound {φ = negF φ}
      (c₂ , core-false→check-neg φ c₂ second)))
proofCore-deterministic φ true true c₁ c₂ first second = refl

proofClassifier : Fml → SI.PartBool
proofClassifier φ = SI.partBool (proofCore φ) (proofCore-deterministic φ)

------------------------------------------------------------------------
-- The concrete Hilbert calculus satisfies the effective-system interface.

proof-runs-true : (φ : Fml) → ⊢ φ → proofClassifier φ SI.⇓ true
proof-runs-true φ derivation with NP.derives→natChecked derivation
... | code , checks = code , check→core-true φ code checks

true-runs-proof : (φ : Fml) → proofClassifier φ SI.⇓ true → ⊢ φ
true-runs-proof φ (code , runs) =
  NP.natChecked-sound (code , core-true→check φ code runs)

refutation-runs-false : (φ : Fml) → ⊢ negF φ
                      → proofClassifier φ SI.⇓ false
refutation-runs-false φ derivation with NP.derives→natChecked derivation
... | code , checks = code , check-neg→core-false φ code checks

false-runs-refutation : (φ : Fml) → proofClassifier φ SI.⇓ false
                      → ⊢ negF φ
false-runs-refutation φ (code , runs) =
  NP.natChecked-sound (code , core-false→check-neg φ code runs)

HilbertSystem : SI.FormalSystem Fml negF
HilbertSystem = SI.formalSystem
  (⊢_)
  proofClassifier
  proof-runs-true
  true-runs-proof
  refutation-runs-false
  false-runs-refutation

hilbert-consistent : (φ : Fml) → ⊢ φ → ⊢ negF φ → Empty.⊥
hilbert-consistent = SI.classifier-consistent HilbertSystem
