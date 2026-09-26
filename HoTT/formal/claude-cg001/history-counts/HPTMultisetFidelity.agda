{-# OPTIONS --safe --cubical --guardedness #-}
{-
  How faithful is C-54 to the multiset type MS of Homotopical Patch Theory?
  (Claude, session 91a6cdaa, 2026-09-25), in reply to Terra's audit 013
  (section 2.2, item 3).

  proof id : MP-CG001-HPT-MULTISET-001
  claim    : CG001-C-60 (full statement in CLAIM-C60.md)

  Terra 013: C-54 uses the cubical library's set-truncated FMSet; there is no
  local fidelity proof that it is the MS of Angiuli-Morehouse-Licata-Harper
  (JFP 2016, section 7).  The authors' Agda code (footnote 7 of the paper:
  dlicata335/hott-agda, branch homotopical-patch-theory-paper, file
  programming/PatchWithHistories.agda, module HistoryHIT) defines MS with
  exactly three constructors -- the empty history, prepending a boolean, and
  a path Ex x y xs : x :: (y :: xs) == y :: (x :: xs), assumed there as an
  axiom in the HoTT-Agda style of simulating higher inductives -- and an
  eliminator with cases for these three only: no set truncation and no
  higher constructors.  The data type MS below has the same three
  constructors, as a cubical higher inductive type.

  C-60 (a) MS is not a set: the loop Ex true true [] is not refl;
       (b) hence MS is not equivalent to N x N (which is a set), and the
           sentence of JFP section 7.2 that the N x N representation "is in
           fact isomorphic to MS" holds for MS's set truncation, not for MS;
       (c) the set truncation of MS is equivalent to FMSet Bool, hence to
           N x N (C-54): C-54 is a theorem about || MS ||_2;
       (d) no function MS -> Maybe Bool returns the first entry of every
           history (any function, not only set-level ones: Ex is a path);
       (e) every function from MS into a set factors through the counts;
       (f) exchanging two entries and exchanging them back is not refl in MS:
           Ex true false [] followed by Ex false true [] is a loop that some
           family transports non-trivially.  The exchange history that the
           points forget is kept, freely, in the paths between presentations.
-}
module HPTMultisetFidelity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isOfHLevelRespectEquiv; isSet×)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Sigma
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Bool using (Bool; true; false; true≢false; false≢true)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.HITs.SetTruncation as ST using (∥_∥₂; ∣_∣₂; squash₂)
open import Cubical.HITs.FiniteMultiset as FMS
  using (FMSet; comm; trunc)
  renaming ([] to []ₘ; _∷_ to _∷ₘ_)
open import Cubical.Relation.Nullary using (¬_)

open import HistoryCounts using (counts; build; buildCounts; historyIsCounts; firstOf; justInj)

private
  variable
    ℓ : Level

------------------------------------------------------------------------
-- MS of Homotopical Patch Theory, constructor for constructor

data MS : Type where
  []ms  : MS
  _∷ms_ : Bool → MS → MS
  Ex    : (x y : Bool) (xs : MS) → x ∷ms (y ∷ms xs) ≡ y ∷ms (x ∷ms xs)

------------------------------------------------------------------------
-- (a) MS is not a set, and (f) exchanging back is not refl

swap : {C : Type} → Bool × (Bool × C) → Bool × (Bool × C)
swap (a , (b , c)) = (b , (a , c))

swapEquiv : {C : Type} → (Bool × (Bool × C)) ≃ (Bool × (Bool × C))
swapEquiv = isoToEquiv (iso swap swap (λ _ → refl) (λ _ → refl))

-- an exchange whose first entry is true swaps the two front components,
-- an exchange whose first entry is false leaves them in place
stepEquiv : Bool → {C : Type} → (Bool × (Bool × C)) ≃ (Bool × (Bool × C))
stepEquiv true  = swapEquiv
stepEquiv false = idEquiv _

Code : MS → Type
Code []ms           = Unit
Code (x ∷ms xs)     = Bool × Code xs
Code (Ex x y xs i)  = ua (stepEquiv x {Code xs}) i

sample : Code (true ∷ms (false ∷ms []ms))
sample = true , (false , tt)

alongTrueFirst : (y : Bool) (xs : MS) (v : Code (true ∷ms (y ∷ms xs)))
  → subst Code (Ex true y xs) v ≡ swap v
alongTrueFirst y xs v = uaβ (stepEquiv true {Code xs}) v

alongFalseFirst : (y : Bool) (xs : MS) (v : Code (false ∷ms (y ∷ms xs)))
  → subst Code (Ex false y xs) v ≡ v
alongFalseFirst y xs v = uaβ (stepEquiv false {Code xs}) v

loopIsNotRefl : ¬ (Ex true true []ms ≡ refl)
loopIsNotRefl p = false≢true (cong fst
  (sym (alongTrueFirst true []ms (true , (false , tt)))
   ∙ cong (λ q → subst Code q (true , (false , tt))) p
   ∙ transportRefl (true , (false , tt))))

msIsNotASet : ¬ isSet MS
msIsNotASet s = loopIsNotRefl (s _ _ (Ex true true []ms) refl)

exchangeBackIsNotRefl : ¬ (Ex true false []ms ∙ Ex false true []ms ≡ refl)
exchangeBackIsNotRefl p = false≢true (cong fst
  (sym (substComposite Code (Ex true false []ms) (Ex false true []ms) sample
        ∙ alongFalseFirst true []ms (subst Code (Ex true false []ms) sample)
        ∙ alongTrueFirst false []ms sample)
   ∙ cong (λ q → subst Code q sample) p
   ∙ transportRefl sample))

------------------------------------------------------------------------
-- (b) MS is not N x N

msIsNotCounts : ¬ (MS ≃ (ℕ × ℕ))
msIsNotCounts e = msIsNotASet (isOfHLevelRespectEquiv 2 (invEquiv e) (isSet× isSetℕ isSetℕ))

------------------------------------------------------------------------
-- (c) the set truncation of MS is FMSet Bool, hence N x N

toFMS : MS → FMSet Bool
toFMS []ms          = []ₘ
toFMS (x ∷ms xs)    = x ∷ₘ toFMS xs
toFMS (Ex x y xs i) = comm x y (toFMS xs) i

toFMS₂ : ∥ MS ∥₂ → FMSet Bool
toFMS₂ = ST.rec trunc toFMS

cons₂ : Bool → ∥ MS ∥₂ → ∥ MS ∥₂
cons₂ x = ST.map (x ∷ms_)

cons₂Comm : (x y : Bool) (b : ∥ MS ∥₂) → cons₂ x (cons₂ y b) ≡ cons₂ y (cons₂ x b)
cons₂Comm x y = ST.elim (λ _ → isProp→isSet (squash₂ _ _)) (λ m → cong ∣_∣₂ (Ex x y m))

fromFMS : FMSet Bool → ∥ MS ∥₂
fromFMS = FMS.Rec.f squash₂ ∣ []ms ∣₂ cons₂ cons₂Comm

toFMS₂Cons : (x : Bool) (b : ∥ MS ∥₂) → toFMS₂ (cons₂ x b) ≡ x ∷ₘ toFMS₂ b
toFMS₂Cons x = ST.elim (λ _ → isProp→isSet (trunc _ _)) (λ m → refl)

toFrom : (xs : FMSet Bool) → toFMS₂ (fromFMS xs) ≡ xs
toFrom = FMS.ElimProp.f (trunc _ _) refl
  (λ x {xs} ih → toFMS₂Cons x (fromFMS xs) ∙ cong (x ∷ₘ_) ih)

fromTo' : (m : MS) → fromFMS (toFMS m) ≡ ∣ m ∣₂
fromTo' []ms          = refl
fromTo' (x ∷ms m)     = cong (cons₂ x) (fromTo' m)
fromTo' (Ex x y m i)  =
  isProp→PathP (λ j → squash₂ (fromFMS (toFMS (Ex x y m j))) ∣ Ex x y m j ∣₂)
    (cong (cons₂ x) (cong (cons₂ y) (fromTo' m)))
    (cong (cons₂ y) (cong (cons₂ x) (fromTo' m))) i

fromTo : (b : ∥ MS ∥₂) → fromFMS (toFMS₂ b) ≡ b
fromTo = ST.elim (λ _ → isProp→isSet (squash₂ _ _)) fromTo'

msTruncIsFMSet : ∥ MS ∥₂ ≃ FMSet Bool
msTruncIsFMSet = isoToEquiv (iso toFMS₂ fromFMS toFrom fromTo)

msTruncIsCounts : ∥ MS ∥₂ ≃ (ℕ × ℕ)
msTruncIsCounts = compEquiv msTruncIsFMSet historyIsCounts

------------------------------------------------------------------------
-- (d) no first entry, for any function out of MS

fromListMS : List Bool → MS
fromListMS []       = []ms
fromListMS (x ∷ xs) = x ∷ms fromListMS xs

noFirstEntryMS : ¬ (Σ[ f ∈ (MS → Maybe Bool) ] ((xs : List Bool) → f (fromListMS xs) ≡ firstOf xs))
noFirstEntryMS (f , agrees) =
  true≢false (justInj (sym (agrees (true ∷ false ∷ []))
                       ∙ cong f (Ex true false []ms)
                       ∙ agrees (false ∷ true ∷ [])))

------------------------------------------------------------------------
-- (e) functions into sets factor through the counts

factorsThroughCountsMS : {X : Type ℓ} (isSetX : isSet X) (g : MS → X)
  → (m : MS) → g m ≡ ST.rec isSetX g (fromFMS (build (counts (toFMS m))))
factorsThroughCountsMS isSetX g m =
  sym (cong (ST.rec isSetX g) (cong fromFMS (buildCounts (toFMS m)) ∙ fromTo' m))
