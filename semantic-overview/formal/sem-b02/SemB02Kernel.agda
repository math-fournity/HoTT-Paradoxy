module SemB02Kernel where

open import foundation.booleans
open import foundation.decidable-types
open import foundation.universe-levels
open import foundation-core.booleans
open import foundation-core.coproduct-types
open import foundation-core.empty-types
open import foundation-core.identity-types
open import univalent-combinatorics.equality-finite-types

explicitDecision : is-decidable (true ＝ false)
explicitDecision = inr neq-true-false-bool

finiteDecision : is-decidable (true ＝ false)
finiteDecision = has-decidable-equality-is-finite is-finite-bool true false

decisionTag : {l : Level} {A : UU l} → is-decidable A → bool
decisionTag (inl _) = true
decisionTag (inr _) = false

tag-is-false-if-empty :
  {l : Level} {A : UU l} (d : is-decidable A) → (A → empty) →
  decisionTag d ＝ false
tag-is-false-if-empty (inl a) not-A = ex-falso (not-A a)
tag-is-false-if-empty (inr _) not-A = refl

explicitTag : bool
explicitTag = decisionTag explicitDecision

finiteTag : bool
finiteTag = decisionTag finiteDecision

explicitTag-eq-false : explicitTag ＝ false
explicitTag-eq-false = refl

finiteTag-eq-false : finiteTag ＝ false
finiteTag-eq-false = tag-is-false-if-empty finiteDecision neq-true-false-bool
