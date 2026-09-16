{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda first machine construction for the same-function /
-- different-time (cost) direction (DIR-L-SAME-FUNCTION-DIFFERENT-TIME),
-- the first candidate of the HoTT research三问:
--
--   C-96  a concrete pair: fast and slow k have the same extensional function
--         but different step costs
--   C-97  no predicate on the bare function type can distinguish two
--         extensionally equal programs (funext path + transport)
--   C-98  hence no consumer r : (ℕ → ℕ) → ℕ can recover the cost value from
--         the bare function
--   C-99  positive control: the cost-refined representation separates the two
--         programs and recovers the cost

module CostFactorization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (znots; snotz; injSuc)

¬_ : {ℓ : Level} → Type ℓ → Type ℓ
¬ A = A → ⊥

------------------------------------------------------------------
-- 1. Source calculus: programs with a syntax-directed step cost
------------------------------------------------------------------

data Prog : Type where
  fast : Prog              -- returns 0 in one step
  slow : (k : ℕ) → Prog    -- returns 0 in 2 + k steps

run : Prog → ℕ → ℕ
run fast _ = zero
run (slow k) _ = zero

cost : Prog → ℕ → ℕ
cost fast _ = suc zero
cost (slow k) _ = suc (suc k)

fun : Prog → (ℕ → ℕ)
fun p x = run p x

------------------------------------------------------------------
-- 2. C-96: same function, different cost
------------------------------------------------------------------

same-function-different-cost : (k : ℕ)
  → (fun fast ≡ fun (slow k)) × (¬ (cost fast zero ≡ cost (slow k) zero))
same-function-different-cost k =
  funExt (λ x → refl) , (λ h → znots (injSuc h))

------------------------------------------------------------------
-- 3. C-97/C-98: the bare function cannot carry the cost
------------------------------------------------------------------

-- No predicate on the bare function type can hold of one program's function
-- and fail of the other's.
no-distinguishing-predicate :
  ¬ (Σ[ P ∈ ((ℕ → ℕ) → Type) ] (P (fun fast) × (¬ P (fun (slow zero)))))
no-distinguishing-predicate (P , pfast , ¬pslow) =
  ¬pslow (subst P (funExt (λ x → refl)) pfast)

-- Hence no consumer recovers the cost value from the bare function.
no-cost-value-recovery :
  ¬ (Σ[ r ∈ ((ℕ → ℕ) → ℕ) ] ((p : Prog) → r (fun p) ≡ cost p zero))
no-cost-value-recovery (r , eq) =
  no-distinguishing-predicate
    ( (λ g → r g ≡ suc zero)
    , eq fast
    , (λ h → snotz (injSuc (sym (eq (slow zero)) ∙ h))) )

------------------------------------------------------------------
-- 4. C-99: positive control — the cost-refined representation works
------------------------------------------------------------------

refine : Prog → ((ℕ → ℕ) × ℕ)
refine p = fun p , cost p zero

refined-cost-recovery : (p : Prog) → snd (refine p) ≡ cost p zero
refined-cost-recovery p = refl

refined-separates : (k : ℕ) → ¬ (refine fast ≡ refine (slow k))
refined-separates k h = znots (injSuc (cong snd h))
