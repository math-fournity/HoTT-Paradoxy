{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module ApproxPellComparison where

-- Coexistence of precision-indexed success and the original exact nonzero statements.
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Empty.Base using (⊥)
open import Sqrt2CutBridge using (zeroQ)
open import Sqrt2CutQueries using (RationalRootTask; noRationalRootOutput)
open import Sqrt2Bisection
import MissileOneProcessLayer as Pell

simultaneous : (n : ℕ) → ApproxTask n ×
  ((Pell.D n ≡ pos 0) → ⊥) × (RationalRootTask → ⊥)
simultaneous n = approximate n , Pell.gap-never-zero n , noRationalRootOutput

successWithPositiveGap : (n : ℕ) → ApproxTask n × ((width (approx n) ≡ zeroQ) → ⊥)
successWithPositiveGap n = approximate n , widthNeverZero (approx n)

ExactMeetingTask : Type₀
ExactMeetingTask = Σ[ n ∈ ℕ ] Bracket.lo (approx n) ≡ Bracket.hi (approx n)

noExactMeeting : ExactMeetingTask → ⊥
noExactMeeting (n , h) = boundsNeverMeet (approx n) h
