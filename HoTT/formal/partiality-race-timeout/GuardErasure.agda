{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda machine construction for the guard/stage-erasure
-- direction (DIR-L-GUARD-ERASURE), refining the historical conditional lemma
-- in HoTT/formal/self-contained/ZCore.agda with an explicit source calculus
-- (staged streams), an explicit forgetful translation, and its converse:
--
--   C-92  a stage-erasing translation that keeps the update law forces a
--         fixed point of the law (necessity)
--   C-93  for the negation law on Bool no such translation exists
--   C-94  conversely, any fixed point of the law yields such a translation
--         (sufficiency) — so erasure-while-keeping-the-law is equivalent to
--         fixed-point existence
--   C-95  the concrete oscillating orbit exists in the source calculus and
--         its stages are observably different

module GuardErasure where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Base using () renaming (rec to ⊥-rec)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)

¬_ : {ℓ : Level} → Type ℓ → Type ℓ
¬ A = A → ⊥

-- Source calculus: streams with explicit stages; the update law on the source
-- advances the stage, and erasing stages means demanding that the forgotten
-- value is invariant under that advance.
shift : {ℓ : Level} {X : Type ℓ} → (ℕ → X) → (ℕ → X)
shift s n = s (suc n)

-- C-92: collapse + kept update law ⇒ fixed point.
collapse-forces-fixed-point :
  {ℓ : Level} {X : Type ℓ}
  (f : X → X) (g : (ℕ → X) → X) (s₀ : ℕ → X)
  → ((s : ℕ → X) → g (shift s) ≡ g s)
  → ((s : ℕ → X) → g (shift s) ≡ f (g s))
  → Σ[ x ∈ X ] (x ≡ f x)
collapse-forces-fixed-point f g s₀ inv law = g s₀ , (sym (inv s₀) ∙ law s₀)

-- C-93: the negation law has no fixed point, so no stage erasure keeps it.
no-fixed-point-of-not : (x : Bool) → x ≡ not x → ⊥
no-fixed-point-of-not false p = false≢true p
no-fixed-point-of-not true p = true≢false p

no-collapse-for-negation :
  (g : (ℕ → Bool) → Bool)
  → ((s : ℕ → Bool) → g (shift s) ≡ g s)
  → ((s : ℕ → Bool) → g (shift s) ≡ not (g s))
  → ⊥
no-collapse-for-negation g inv law =
  no-fixed-point-of-not (g (λ _ → false))
    (collapse-forces-fixed-point not g (λ _ → false) inv law .snd)

-- C-94: conversely a fixed point yields a stage-erasing translation that
-- keeps the law.
collapse-exists-if-fixed-point :
  {ℓ : Level} {X : Type ℓ}
  (f : X → X) (x₀ : X) → x₀ ≡ f x₀
  → Σ[ g ∈ ((ℕ → X) → X) ]
      (((s : ℕ → X) → g (shift s) ≡ g s)
      × ((s : ℕ → X) → g (shift s) ≡ f (g s)))
collapse-exists-if-fixed-point f x₀ fix =
  (λ _ → x₀) , (λ s → refl) , (λ s → fix)

-- C-95: the concrete oscillation lives in the source calculus, and its stages
-- are observably different (the stage index is not erasable for free).
orbit : ℕ → Bool
orbit zero = false
orbit (suc n) = not (orbit n)

orbit-law : (n : ℕ) → orbit (suc n) ≡ not (orbit n)
orbit-law n = refl

orbit-stages-differ : ¬ (orbit zero ≡ orbit (suc zero))
orbit-stages-differ p = false≢true p

oscillating-orbit :
  ((n : ℕ) → orbit (suc n) ≡ not (orbit n))
  × (¬ (orbit zero ≡ orbit (suc zero)))
oscillating-orbit = orbit-law , orbit-stages-differ
