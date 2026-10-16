{-# OPTIONS --safe --cubical --guardedness #-}
{-
  CG-001 / seed C1 "measurement record of a real": positive controls.

  proof id : MP-CG001-MEASUREMENT-LOG-001
  claim    : CG001-C-08 (full statement in CLAIM.md)

  A quantity u of an arbitrary type U comes with a reading relation
  Reads n u q, read "q is an acceptable reading of u at precision level n".
  For the Book's HIIT Cauchy reals one would take Reads n u q to be
  u ~_{2^-n} rat(q); that instance is source-reported (Book Thm
  RC-archimedean) and is NOT replayed here, because cubical 0.9 has no
  HIIT Cauchy reals.  Everything below is generic in U and Reads.

  What is checked:
    (i)   every finite record of readings merely exists (finite choice);
    (ii)  an infinite record restricts to every finite record;
    (iii) with countable choice given as an explicit hypothesis (never
          assumed as an axiom), the infinite record merely exists;
    (iv)  a quantity that carries a rational approximation as data
          (setoid style) has an infinite record outright.
  Not checked: that the infinite record is unobtainable without countable
  choice.  That would need a countermodel and is outside this package.
-}
module MeasurementLog where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.FinData.Base using (Fin; toℕ)
open import Cubical.Data.FinData.FiniteChoice using (choice)
open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁)

-- countable choice, stated as a type so that it can only enter as a hypothesis
ACω : (ℓ : Level) → Type (ℓ-suc ℓ)
ACω ℓ = (P : ℕ → Type ℓ) → ((n : ℕ) → ∥ P n ∥₁) → ∥ ((n : ℕ) → P n) ∥₁

module _ {ℓ ℓ' : Level} {U : Type ℓ} (Reads : ℕ → U → ℚ → Type ℓ') (u : U) where

  -- what a measuring procedure provides: at each precision some reading exists
  EachPrecision : Type ℓ'
  EachPrecision = (n : ℕ) → ∥ Σ ℚ (Reads n u) ∥₁

  -- a record of readings for precision levels 0 … N-1
  FiniteLog : ℕ → Type ℓ'
  FiniteLog N = (i : Fin N) → Σ ℚ (Reads (toℕ i) u)

  -- a record of readings for every precision level
  InfiniteLog : Type ℓ'
  InfiniteLog = (n : ℕ) → Σ ℚ (Reads n u)

  -- C-08 (i): any finite record the experimenter asks for merely exists
  finiteLogAvailable : EachPrecision → (N : ℕ) → ∥ FiniteLog N ∥₁
  finiteLogAvailable each N =
    choice (λ i → Σ ℚ (Reads (toℕ i) u)) (λ i → each (toℕ i))

  -- C-08 (ii): an infinite record gives every finite record by restriction
  restrict : InfiniteLog → (N : ℕ) → FiniteLog N
  restrict log N i = log (toℕ i)

  -- C-08 (iii): the premise switch; with countable choice the infinite record merely exists
  infiniteLogFromChoice : ACω ℓ' → EachPrecision → ∥ InfiniteLog ∥₁
  infiniteLogFromChoice ac each = ac (λ n → Σ ℚ (Reads n u)) each

  -- C-08 (iv): a quantity carried together with a rational approximation has an infinite record
  carriedApproximationGivesLog : (s : ℕ → ℚ) → ((n : ℕ) → Reads n u (s n)) → InfiniteLog
  carriedApproximationGivesLog s r n = s n , r n

  carriedApproximationGivesEachPrecision :
    (s : ℕ → ℚ) → ((n : ℕ) → Reads n u (s n)) → EachPrecision
  carriedApproximationGivesEachPrecision s r n = ∣ s n , r n ∣₁
