{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module Sqrt2TaskComparison where

-- A closed family of requests about the fixed GOLD specification, not all HoTT tasks.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Empty as Empty
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.Data.Rationals.Order using (_<_)
open import StandardDedekind
open import Sqrt2CutBridge using (zeroQ; twoQ; minusThreeQ; goldReal)
open import Sqrt2CutQueries using (lowerQuery; upperQuery; minusThreeIsLower; oldSquareTableRejectsMinusThree)
open import Sqrt2TableRecovery using (lowerViaTable; recoveryAgrees)
open import Sqrt2Bisection
open import ApproxPellComparison using (noExactMeeting)
open import MissileThreeVerdictCollision using (Spec_A; Spec_B)
import MissileThreeUnconditional as Old
import MissileTwoUniversalIrrationality as M2
import MissileOneProcessLayer as Pell
import CutGoldForm as G
import CutRealLayer as Legacy

-- Explicit upward universe packaging, not propositional resizing or a downcast.
Up : Type₀ → Type₁
Up A = Lift {j = ℓ-suc ℓ-zero} A

TruthSpec : Type₀ → Bool → Type₀
TruthSpec P b = (b ≡ true → P) × (P → b ≡ true)

data Request : Type₀ where
  representation : Request
  queryL queryU : ℚ → Request
  approximation : ℕ → Request
  oldTable : Request
  suppliedLower : Spec_A → ℚ → Request
  rationalRoot bisectionMeeting pellZero : Request

Output : Request → Type₁
Output representation = StandardReals ℓ-zero
Output (queryL q) = Up Bool
Output (queryU q) = Up Bool
Output (approximation n) = Up Bracket
Output oldTable = Up (ℚ → Bool)
Output (suppliedLower a q) = Up Bool
Output rationalRoot = Up ℚ
Output bisectionMeeting = Up ℕ
Output pellZero = Up ℕ

Done : (r : Request) → Output r → Type₁
Done representation x = (lowerPredicate x ≡ G.Lₚ) × (upperPredicate x ≡ G.Uₚ)
Done (queryL q) b = Up (TruthSpec (G.L q) (lower b))
Done (queryU q) b = Up (TruthSpec (G.U q) (lower b))
Done (approximation n) s = Up (width (lower s) ≡ dyadicWidth n)
Done oldTable f = Up ((q : ℚ) → TruthSpec (q ·ℚ q < twoQ) (lower f q))
Done (suppliedLower a q) b = Up (TruthSpec (G.L q) (lower b))
Done rationalRoot q = Up (lower q ·ℚ lower q ≡ twoQ)
Done bisectionMeeting n = Up (Bracket.lo (approx (lower n)) ≡ Bracket.hi (approx (lower n)))
Done pellZero n = Up (Pell.D (lower n) ≡ pos 0)

Response : Request → Type₁
Response r = Σ[ o ∈ Output r ] Done r o

truthFromDecision : {P : Type₀} → Dec P → Σ[ b ∈ Bool ] TruthSpec P b
truthFromDecision (yes p) = true , (λ _ → p) , (λ _ → refl)
truthFromDecision (no np) = false ,
  (λ h → Empty.rec (true≢false (sym h))) , (λ p → Empty.rec (np p))

lowerFromDecision : (q : ℚ) → Dec (G.L q) → Response (queryL q)
lowerFromDecision q d = lift (fst t) , lift (snd t)
  where t = truthFromDecision d

upperFromDecision : (q : ℚ) → Dec (G.U q) → Response (queryU q)
upperFromDecision q d = lift (fst t) , lift (snd t)
  where t = truthFromDecision d

representationReply : Response representation
representationReply = goldReal , refl , refl

representationCanonical : (r : Response representation) → fst r ≡ goldReal
representationCanonical (x , l , u) =
  Σ≡Prop (λ LU → isPropDcutStd (fst LU) (snd LU)) (cong₂ (λ L U → L , U) l u)

lowerReply : (q : ℚ) → Response (queryL q)
lowerReply q = lowerFromDecision q (lowerQuery q)

upperReply : (q : ℚ) → Response (queryU q)
upperReply q = upperFromDecision q (upperQuery q)

approximationReply : (n : ℕ) → Response (approximation n)
approximationReply n = lift (approx n) , lift (approxWidth n)

approximationReplyTrace : (n : ℕ) →
  RefinementTrace n initialBracket (lower (fst (approximationReply n)))
approximationReplyTrace = approxTrace

oldTableReply : Response oldTable
oldTableReply = lift (fst Old.specA-inhabited-unc) , lift (snd Old.specA-inhabited-unc)

tableToOriginal : Response oldTable → Spec_A
tableToOriginal (f , p) = lower f , lower p

originalToTable : Spec_A → Response oldTable
originalToTable (f , p) = lift f , lift p

tableResponseEquivOriginal : Response oldTable ≃ Spec_A
tableResponseEquivOriginal = isoToEquiv (iso tableToOriginal originalToTable (λ _ → refl) (λ _ → refl))

suppliedReply : (a : Spec_A) (q : ℚ) → Response (suppliedLower a q)
suppliedReply a q = lowerFromDecision q (lowerViaTable a q)

suppliedGeneratedAgreement : (a : Spec_A) (q : ℚ) → suppliedReply a q ≡ lowerReply q
suppliedGeneratedAgreement a q = cong (lowerFromDecision q) (recoveryAgrees a q)

rootToOriginal : Response rationalRoot → Spec_B
rootToOriginal (q , p) = lower q , lower p

originalToRoot : Spec_B → Response rationalRoot
originalToRoot (q , p) = lift q , lift p

rootResponseEquivOriginal : Response rationalRoot ≃ Spec_B
rootResponseEquivOriginal = isoToEquiv (iso rootToOriginal originalToRoot (λ _ → refl) (λ _ → refl))

noRootResponse : Response rationalRoot → ⊥
noRootResponse r = M2.spec-B-empty (rootToOriginal r)

PositiveRootResponse : Type₁
PositiveRootResponse = Σ[ r ∈ Response rationalRoot ] Up (zeroQ < lower (fst r))

noPositiveRootResponse : PositiveRootResponse → ⊥
noPositiveRootResponse (r , _) = noRootResponse r

noMeetingResponse : Response bisectionMeeting → ⊥
noMeetingResponse (n , p) = noExactMeeting (lower n , lower p)

noPellZeroResponse : Response pellZero → ⊥
noPellZeroResponse (n , p) = Pell.gap-never-zero (lower n) (lower p)

-- Complete for these nine request families only; not a verifier for arbitrary candidates.
dispatch : (r : Request) → Dec (Response r)
dispatch representation = yes representationReply
dispatch (queryL q) = yes (lowerReply q)
dispatch (queryU q) = yes (upperReply q)
dispatch (approximation n) = yes (approximationReply n)
dispatch oldTable = yes oldTableReply
dispatch (suppliedLower a q) = yes (suppliedReply a q)
dispatch rationalRoot = no noRootResponse
dispatch bisectionMeeting = no noMeetingResponse
dispatch pellZero = no noPellZeroResponse

noUniversalSuccessfulResponder : ((r : Request) → Response r) → ⊥
noUniversalSuccessfulResponder f = noRootResponse (f rationalRoot)

oldAnswerFailsLowerDone :
  Done (queryL minusThreeQ) (lift (fst Old.specA-inhabited-unc minusThreeQ)) → ⊥
oldAnswerFailsLowerDone p = true≢false
  (sym (snd (lower p) minusThreeIsLower) ∙ oldSquareTableRejectsMinusThree)

originalM3Refusal : (Spec_A ≃ Spec_B) → ⊥
originalM3Refusal = Old.M3-L1-unc

noOldTableToRoot : (Spec_A → Spec_B) → ⊥
noOldTableToRoot f = M2.spec-B-empty (f Old.specA-inhabited-unc)

-- The fourth-layer implication retains its explicit input; necessity is not filled in.
smallnessIfProvided : (ℓ : Level) → Legacy.SingleOmega ℓ → Legacy.ℝLayerAt ℓ
smallnessIfProvided = Legacy.sufficiency
