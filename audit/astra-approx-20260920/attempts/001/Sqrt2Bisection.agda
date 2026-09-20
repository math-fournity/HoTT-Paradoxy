{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module Sqrt2Bisection where

-- Binary-precision brackets in the unchanged GOLD rational type.
-- No use of the library's different QuoQ commutative-ring carrier.
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.NatPlusOne.Base using (1+_)
open import Cubical.Data.Rationals.Base using (ℚ; [_/_]; eq/)
open import Cubical.Data.Rationals.Properties
  using (+Assoc; +Comm; +IdR; +InvR; +InvL; +CancelR; ·DistL+; ·IdR; ·AnnihilR)
  renaming (_+_ to _+ℚ_; _·_ to _·ℚ_; -_ to -ℚ_)
open import Cubical.Data.Rationals.Order
  using (_<_; _≤_; <-+o; <-o+; <-+o-cancel; isIrrefl<; isRefl≤; <Weaken≤)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Empty.Base using (⊥)
open import CutInfra using (·-mono-<-nn)
import CutGoldForm as G
open import Sqrt2CutQueries using (classify)
open import Sqrt2CutBridge using (zeroQ; oneQ; twoQ; goldReal)
open import StandardDedekind using (lowerPredicate; upperPredicate)

halfQ : ℚ
halfQ = [ pos 1 / (1+ (suc zero)) ]

halfPositive : zeroQ < halfQ
halfPositive = 0 , refl

halfLessOne : halfQ < oneQ
halfLessOne = 0 , refl

halfPlusHalf : halfQ +ℚ halfQ ≡ oneQ
halfPlusHalf = eq/ (pos 4 , 1+ 3) (pos 1 , 1+ zero) refl

gap middle : ℚ → ℚ → ℚ
gap a b = b +ℚ (-ℚ a)
middle a b = a +ℚ (gap a b ·ℚ halfQ)

cancelAround : (a v : ℚ) → (a +ℚ v) +ℚ (-ℚ a) ≡ v
cancelAround a v = cong (_+ℚ (-ℚ a)) (+Comm a v) ∙
  sym (+Assoc v a (-ℚ a)) ∙ cong (v +ℚ_) (+InvR a) ∙ +IdR v

restoreGap : (a b : ℚ) → a +ℚ gap a b ≡ b
restoreGap a b = +Assoc a b (-ℚ a) ∙ cancelAround a b

gapThenBase : (a b : ℚ) → gap a b +ℚ a ≡ b
gapThenBase a b = sym (+Assoc b (-ℚ a) a) ∙ cong (b +ℚ_) (+InvL a) ∙ +IdR b

doubleHalf : (w : ℚ) → (w ·ℚ halfQ) +ℚ (w ·ℚ halfQ) ≡ w
doubleHalf w = sym (·DistL+ w halfQ halfQ) ∙ cong (w ·ℚ_) halfPlusHalf ∙ ·IdR w

leftHalf : (a b : ℚ) → gap a (middle a b) ≡ gap a b ·ℚ halfQ
leftHalf a b = cancelAround a (gap a b ·ℚ halfQ)

halfPlusMiddle : (a b : ℚ) → (gap a b ·ℚ halfQ) +ℚ middle a b ≡ b
halfPlusMiddle a b = +Assoc v a v ∙ cong (_+ℚ v) (+Comm v a) ∙
  sym (+Assoc a v v) ∙ cong (a +ℚ_) (doubleHalf (gap a b)) ∙ restoreGap a b
  where v = gap a b ·ℚ halfQ

rightHalf : (a b : ℚ) → gap (middle a b) b ≡ gap a b ·ℚ halfQ
rightHalf a b = +CancelR (gap (middle a b) b) (middle a b) (gap a b ·ℚ halfQ)
  (gapThenBase (middle a b) b ∙ sym (halfPlusMiddle a b))

gapPositive : (a b : ℚ) → a < b → zeroQ < gap a b
gapPositive a b h = subst (λ x → x < gap a b) (+InvR a) (<-+o a b (-ℚ a) h)

halfProductPositive : (w : ℚ) → zeroQ < w → zeroQ < w ·ℚ halfQ
halfProductPositive w h = subst (λ x → x < w ·ℚ halfQ) (·AnnihilR w)
  (·-mono-<-nn w zeroQ halfQ h halfPositive)

fromPositiveGap : (a b : ℚ) → zeroQ < gap a b → a < b
fromPositiveGap a b h = <-+o-cancel a b (-ℚ a)
  (subst (λ x → x < gap a b) (sym (+InvR a)) h)

middleAbove : (a b : ℚ) → a < b → a < middle a b
middleAbove a b h = subst (λ x → x < middle a b) (+IdR a)
  (<-o+ zeroQ (gap a b ·ℚ halfQ) a (halfProductPositive (gap a b) (gapPositive a b h)))

middleBelow : (a b : ℚ) → a < b → middle a b < b
middleBelow a b h = fromPositiveGap (middle a b) b
  (subst (zeroQ <_) (sym (rightHalf a b)) (halfProductPositive (gap a b) (gapPositive a b h)))

record Bracket : Type₀ where
  constructor bracket
  field
    lo hi : ℚ
    memberL : G.L lo
    memberU : G.U hi
open Bracket

width : Bracket → ℚ
width s = gap (lo s) (hi s)

bracketOrdered : (s : Bracket) → lo s < hi s
bracketOrdered s = G.disjoint (lo s) (hi s) (memberL s) (memberU s)

initialBracket : Bracket
initialBracket = bracket oneQ twoQ G.inhabL G.inhabU

refine : Bracket → Bracket
refine s with classify (middle (lo s) (hi s))
... | inl l = bracket (middle (lo s) (hi s)) (hi s) l (memberU s)
... | inr u = bracket (lo s) (middle (lo s) (hi s)) (memberL s) u

refineWidth : (s : Bracket) → width (refine s) ≡ width s ·ℚ halfQ
refineWidth s with classify (middle (lo s) (hi s))
... | inl _ = rightHalf (lo s) (hi s)
... | inr _ = leftHalf (lo s) (hi s)

lowerNested : (s : Bracket) → lo s ≤ lo (refine s)
lowerNested s with classify (middle (lo s) (hi s))
... | inl _ = <Weaken≤ (lo s) (middle (lo s) (hi s)) (middleAbove (lo s) (hi s) (bracketOrdered s))
... | inr _ = isRefl≤ (lo s)

upperNested : (s : Bracket) → hi (refine s) ≤ hi s
upperNested s with classify (middle (lo s) (hi s))
... | inl _ = isRefl≤ (hi s)
... | inr _ = <Weaken≤ (middle (lo s) (hi s)) (hi s) (middleBelow (lo s) (hi s) (bracketOrdered s))

approx : ℕ → Bracket
approx zero = initialBracket
approx (suc n) = refine (approx n)

dyadicWidth : ℕ → ℚ
dyadicWidth zero = oneQ
dyadicWidth (suc n) = dyadicWidth n ·ℚ halfQ

approxWidth : (n : ℕ) → width (approx n) ≡ dyadicWidth n
approxWidth zero = refl
approxWidth (suc n) = refineWidth (approx n) ∙ cong (_·ℚ halfQ) (approxWidth n)

ApproxTask : ℕ → Type₀
ApproxTask n = Σ[ s ∈ Bracket ] width s ≡ dyadicWidth n

approximate : (n : ℕ) → ApproxTask n
approximate n = approx n , approxWidth n

packedBounds : (n : ℕ) →
  fst (lowerPredicate goldReal (lo (approx n))) × fst (upperPredicate goldReal (hi (approx n)))
packedBounds n = memberL (approx n) , memberU (approx n)

-- Count refinement calls, not CPU instructions or physical time.
data RefinementTrace : ℕ → Bracket → Bracket → Type₀ where
  idle : {s : Bracket} → RefinementTrace zero s s
  next : {n : ℕ} {s t : Bracket} → RefinementTrace n s t → RefinementTrace (suc n) s (refine t)

approxTrace : (n : ℕ) → RefinementTrace n initialBracket (approx n)
approxTrace zero = idle
approxTrace (suc n) = next (approxTrace n)

widthPositive : (s : Bracket) → zeroQ < width s
widthPositive s = gapPositive (lo s) (hi s) (bracketOrdered s)

widthNeverZero : (s : Bracket) → width s ≡ zeroQ → ⊥
widthNeverZero s h = isIrrefl< zeroQ (subst (zeroQ <_) h (widthPositive s))

boundsNeverMeet : (s : Bracket) → lo s ≡ hi s → ⊥
boundsNeverMeet s h = isIrrefl< (hi s) (subst (_< hi s) h (bracketOrdered s))

widthStrictlyDecreases : (s : Bracket) → width (refine s) < width s
widthStrictlyDecreases s = subst2 _<_ (sym (refineWidth s)) (·IdR (width s))
  (·-mono-<-nn (width s) halfQ oneQ (widthPositive s) halfLessOne)

twoStepLower : lo (approx 2) ≡ [ pos 5 / (1+ 3) ]
twoStepLower = refl

twoStepUpper : hi (approx 2) ≡ [ pos 3 / (1+ 1) ]
twoStepUpper = refl
