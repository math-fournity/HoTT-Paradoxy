{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda verification of the R034 path-certificate boundary
-- (continuation of the DIR-W-PATH-CERTIFICATE direction):
--
--   C-100  the univalence path of the Bool negation moves booleans by not
--   C-101  ∥Bool ≡ Y∥₁ is a proposition and is inhabited at Y = Bool
--   C-102  the fixed-pair weak interface ∥Bool ≡ Bool∥₁ → Bool → Bool exists
--   C-103  the fixed-source variant (Y : Type) → ∥Bool ≡ Y∥₁ → Bool → Y is
--          empty (Σ-loop + dependent transport, real Cubical Path)
--   C-104  the general unified interface
--          (X Y : Type) → ∥X ≡ Y∥₁ → X → Y is empty
--   C-105  the path-indexed interface (X ≡ Y) → X → Y exists (transport)
--
-- This replaces "ordinary Lean Eq" by native Cubical Path/truncation/
-- univalence; it is a boundary result, not a HoTT paradox.

module PathCertificate where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Base using () renaming (rec to ⊥-rec)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)

¬_ : {ℓ : Level} → Type ℓ → Type ℓ
¬ A = A → ⊥

------------------------------------------------------------------
-- 1. C-100: a real univalence path moves points by the equivalence
------------------------------------------------------------------

ua-move-computes : (b : Bool) → transport (ua notEquiv) b ≡ not b
ua-move-computes b = uaβ notEquiv b

ua-move-is-not : transport (ua notEquiv) ≡ not
ua-move-is-not = funExt ua-move-computes

------------------------------------------------------------------
-- 2. C-101/C-102: truncation and the fixed-pair interface
------------------------------------------------------------------

H : Type → Type₁
H Y = ∥ Bool ≡ Y ∥₁

H-is-prop : (Y : Type) → isProp (H Y)
H-is-prop Y = squash₁

H-inhabited : H Bool
H-inhabited = ∣ refl ∣₁

-- The fixed-pair weak interface is inhabited (identity is an example).
fixed-pair-interface : H Bool → Bool → Bool
fixed-pair-interface _ x = x

------------------------------------------------------------------
-- 3. C-103: the fixed-source unified variant is empty
------------------------------------------------------------------

C : Type₁
C = Σ[ Y ∈ Type ] H Y

z₀ : C
z₀ = Bool , ∣ refl ∣₁

loop : Bool ≡ Bool
loop = ua notEquiv

loop-fiber : PathP (λ i → H (loop i)) (snd z₀) (snd z₀)
loop-fiber = isProp→PathP (λ i → squash₁) (snd z₀) (snd z₀)

loop-point : z₀ ≡ z₀
loop-point = ΣPathP (loop , loop-fiber)

left-end : loop-point i0 ≡ z₀
left-end = ΣPathP (refl , squash₁ (snd (loop-point i0)) (snd z₀))

right-end : loop-point i1 ≡ z₀
right-end = ΣPathP (refl , squash₁ (snd (loop-point i1)) (snd z₀))

no-fixed-point-of-not : (x : Bool) → x ≡ not x → ⊥
no-fixed-point-of-not false p = false≢true p
no-fixed-point-of-not true p = true≢false p

no-fixed-source-mere-move : ¬ ((Y : Type) → H Y → Bool → Y)
no-fixed-source-mere-move m = no-fixed-point-of-not (s z₀) final
  where
  s : (z : C) → fst z
  s (Y , h) = m Y h false

  ω : PathP (λ i → fst (loop-point i)) (s (loop-point i0)) (s (loop-point i1))
  ω i = s (loop-point i)

  tA : transport (λ i → fst (loop-point i)) (s (loop-point i0)) ≡ s (loop-point i1)
  tA = fromPathP ω

  tB : transport (λ i → fst (loop-point i)) (s (loop-point i0))
       ≡ transport loop (s (loop-point i0))
  tB = refl

  tC : transport loop (s (loop-point i0)) ≡ not (s (loop-point i0))
  tC = uaβ notEquiv (s (loop-point i0))

  tE : s (loop-point i1) ≡ s z₀
  tE = cong s right-end

  chain : not (s (loop-point i0)) ≡ s z₀
  chain = sym tC ∙ sym tB ∙ tA ∙ tE

  final : s z₀ ≡ not (s z₀)
  final = sym (subst (λ w → not w ≡ s z₀) (cong s left-end) chain)

------------------------------------------------------------------
-- 4. C-104/C-105: the unified interface versus the path interface
------------------------------------------------------------------

MereMove : Type₁
MereMove = (X Y : Type) → ∥ X ≡ Y ∥₁ → X → Y

no-mere-move : ¬ MereMove
no-mere-move mm = no-fixed-source-mere-move (λ Y h b → mm Bool Y h b)

path-move : {X Y : Type} → X ≡ Y → X → Y
path-move p x = transport p x
