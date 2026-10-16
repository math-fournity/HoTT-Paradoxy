{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The user's ring story on a quantized ring (Claude, session 91a6cdaa,
  2026-09-25): a positive control for the density premise.

  proof id : MP-CG001-DISCRETE-RING-001
  claims   : CG001-C-42 (full statement in CLAIM.md)

  Story (user's original text, paraphrased): take a point away from a ring
  (M), unfold the two ends into a segment (N), and ask whether N can be
  restored to M.  With points of zero size, the ends seem never to close.

  C-42  on a ring of n+1 discrete points with the point fzero removed, the
        unfolded segment of n points restores onto every remaining point,
        by finite case analysis and with no extra principle: the restoring
        map is injective and covers M, so the segment and M are equivalent.

  Contrast (not proved here; see CLAIM.md): on the Dedekind-real circle, the
  analogous coverage of the weakly punctured circle by a fixed restoring map
  implies Markov's principle, and is equivalent to it given countable choice
  (Astra, C-319, C-322, C-324 in the shared matrix).

  Bridge labels (ring, point, segment, restore) prove no physical fact.
-}
module DiscreteRing where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; snotz)
open import Cubical.Data.Nat.Order using (pred-≤-pred)
open import Cubical.Data.Empty using () renaming (rec to ⊥-rec)
open import Cubical.Data.Fin using (Fin; fzero; fsuc)
open import Cubical.Data.Fin.Properties using (Fin-fst-≡; fsuc-inj)
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Relation.Nullary.Properties using (isProp¬)

-- the ring with the point fzero taken away
M : ℕ → Type
M n = Σ[ w ∈ Fin (suc n) ] ¬ (w ≡ fzero)

-- the unfolded segment
N : ℕ → Type
N n = Fin n

-- restoring: the i-th point of the segment goes back next to the gap
restore : (n : ℕ) → N n → M n
restore n j = fsuc j , λ p → snotz (cong fst p)

-- every remaining point of the ring is reached, by finite case analysis
covers : (n : ℕ) (m : M n) → Σ[ j ∈ N n ] restore n j ≡ m
covers n ((zero , lt) , away) = ⊥-rec (away (Fin-fst-≡ refl))
covers n ((suc k , lt) , away) =
  (k , pred-≤-pred lt) , Σ≡Prop (λ w → isProp¬ (w ≡ fzero)) (Fin-fst-≡ refl)

restoreInjective : (n : ℕ) (i j : N n) → restore n i ≡ restore n j → i ≡ j
restoreInjective n i j p = fsuc-inj (cong fst p)

-- the segment and the punctured ring are equivalent: the ring is restored exactly
restoreIso : (n : ℕ) → Iso (N n) (M n)
Iso.fun (restoreIso n) = restore n
Iso.inv (restoreIso n) m = fst (covers n m)
Iso.rightInv (restoreIso n) m = snd (covers n m)
Iso.leftInv (restoreIso n) j = restoreInjective n _ _ (snd (covers n (restore n j)))

restoreEquiv : (n : ℕ) → N n ≃ M n
restoreEquiv n = isoToEquiv (restoreIso n)
