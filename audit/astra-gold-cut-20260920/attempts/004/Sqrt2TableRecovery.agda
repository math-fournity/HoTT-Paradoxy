{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module Sqrt2TableRecovery where

-- Recovery from the actual old square-table specification plus rational sign.
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.Relation.Nullary.Properties using (isPropDec)
open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.Data.Rationals.Order using (_<_; _≟_; lt; eq; gt; isAsym<)
open import CutInfra using (<-≤)
open import MissileThreeVerdictCollision using (Spec_A)
import MissileThreeUnconditional as Old
import CutGoldForm as G
open import Sqrt2CutBridge
open import Sqrt2CutQueries

squareFromTable : Spec_A → (q : ℚ) → Dec (q ·ℚ q < twoQ)
squareFromTable (f , table) q with f q | table q
... | true  | (to , from) = yes (to refl)
... | false | (to , from) = no (λ sq → true≢false (sym (from sq)))

lowerViaTable : Spec_A → (q : ℚ) → Dec (G.L q)
lowerViaTable a q with q ≟ zeroQ
... | lt q<0 = yes (inl q<0)
... | eq q=0 = yes (subst G.L (sym q=0) zeroLower)
... | gt 0<q with squareFromTable a q
...   | yes sq<2 = yes (inr (<-≤ zeroQ q 0<q , sq<2))
...   | no notSq = no (λ { (inl q<0) → isAsym< zeroQ q 0<q q<0 ; (inr (_ , sq<2)) → notSq sq<2 })

recoveryAgrees : (a : Spec_A) (q : ℚ) → lowerViaTable a q ≡ lowerQuery q
recoveryAgrees a q = isPropDec (snd (G.Lₚ q)) (lowerViaTable a q) (lowerQuery q)

recoveredMinusThree : decisionTag (lowerViaTable Old.specA-inhabited-unc minusThreeQ) ≡ true
recoveredMinusThree = refl
