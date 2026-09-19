{-# OPTIONS --safe --cubical --guardedness --two-level #-}

-- MissileFourNecessityLEM：必要性的 LEM-条件版（2026-09-19）
-- claim id : CAND-F2-7-NECESSITY-LEM (candidate；registers_new_claim:false)
--
-- 定理：LEMProp ℓ → SingleOmega ℓ，从而 LEMProp ℓ → Necessity ℓ
-- （Necessity ℓ = ℝLayerAt ℓ → SingleOmega ℓ；前提 ℝLayerAt 在证明中未被使用）。
--
-- 数学内容（B1b′ 收官的补强件）：在 LEM 下取 Ω := Lift Bool，由 LEMProp ℓ
-- 逐点决策组装 hProp ℓ ≃ Bool。于是「ℝ 层 ⇒ 单一 Ω」在经典语境中**无条件成立**
-- （后件免费）——必要性问题的全部内容被精确定位到构造性片段（CONJECTURE 维持；
-- 030 §3 观察一的机器化）。证明形态：prop 之间的等价只需双向映射 + prop 联贯
-- （iso 的 coherence 由 isProp 吸收）；hProp 内的相等 = ΣPathP(ua, toPathP·isPropIsProp)。
--
-- 边界：不声称无条件 Necessity；不声称 HoTT 不一致；本定理 = Book 取法 3
-- 「LEM ⇒ Ω≡Bool」原文（CLAIM-PACKAGE §1.1）的机器化。

module MissileFourNecessityLEM where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (hProp; isOfHLevelLift)
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (Iso; iso; isoToEquiv)
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Data.Sigma using (Σ; fst; snd)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr; elim)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (isSetBool)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Unit.Properties using (isPropUnit)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import CutRealLayer using (LEMProp; SingleOmega; Necessity)

private
  isPropLift : {ℓ ℓ' : Level} {A : Type ℓ} → isProp A → isProp (Lift {ℓ} {ℓ'} A)
  isPropLift = isOfHLevelLift 1

  isSetLift : {ℓ ℓ' : Level} {A : Type ℓ} → isSet A → isSet (Lift {ℓ} {ℓ'} A)
  isSetLift = isOfHLevelLift 2

  absurdTo : {ℓ : Level} {A : Type ℓ} → ⊥ → A
  absurdTo ()

UnitProp : {ℓ : Level} → hProp ℓ
UnitProp {ℓ} = Lift {ℓ-zero} {ℓ} Unit , isPropLift isPropUnit

EmptyProp : {ℓ : Level} → hProp ℓ
EmptyProp {ℓ} = Lift {ℓ-zero} {ℓ} ⊥ , isPropLift isProp⊥

-- hProp 内的相等：类型路径 + prop 证明的 PathP（isPropIsProp 吸收两侧证明差）
hProp-Path : {ℓ : Level} {A B : Type ℓ} (q : A ≡ B) (pA : isProp A) (pB : isProp B)
           → (A , pA) ≡ (B , pB)
hProp-Path q pA pB =
  ΣPathP (q , toPathP (isPropIsProp (transport (λ i → isProp (q i)) pA) pB))

------------------------------------------------------------------------
-- 核心组件（LEM 参数化）：决策函数 / 回填 / 双向联贯
------------------------------------------------------------------------

module Decide {ℓ : Level} (lem : LEMProp ℓ) where

  fun : hProp ℓ → Bool
  fun P = elim (λ _ → true) (λ _ → false)
           (lem (Lift {ℓ} {ℓ-suc ℓ} (fst P)) (isPropLift (snd P)))

  back : Bool → hProp ℓ
  back true  = UnitProp
  back false = EmptyProp

  rinv : (b : Bool) → fun (back b) ≡ b
  rinv true with lem (Lift {ℓ} {ℓ-suc ℓ} (fst UnitProp)) (isPropLift (snd UnitProp))
  ... | inl _ = refl
  ... | inr ¬p = absurdTo (¬p (lift (lift tt)))
  rinv false with lem (Lift {ℓ} {ℓ-suc ℓ} (fst EmptyProp)) (isPropLift (snd EmptyProp))
  ... | inl p  = absurdTo (lower (lower p))
  ... | inr _  = refl

  linv : (P : hProp ℓ) → back (fun P) ≡ P
  linv P with lem (Lift {ℓ} {ℓ-suc ℓ} (fst P)) (isPropLift (snd P))
  ... | inl p =
    hProp-Path (sym (ua e)) (isPropLift isPropUnit) (snd P)
    where
    e : fst P ≃ Lift {ℓ-zero} {ℓ} Unit
    e = isoToEquiv (iso (λ _ → lift tt) (λ _ → lower p)
                        (λ _ → isPropLift isPropUnit _ _)
                        (λ x → snd P _ _))
  ... | inr ¬p =
    hProp-Path (sym (ua e)) (isPropLift isProp⊥) (snd P)
    where
    e : fst P ≃ Lift {ℓ-zero} {ℓ} ⊥
    e = isoToEquiv (iso (λ x → lift (¬p (lift x))) (λ y → absurdTo (lower y))
                        (λ _ → isPropLift isProp⊥ _ _)
                        (λ x → snd P _ _))

------------------------------------------------------------------------
-- 定理一：LEM 下 hProp ℓ ≃ Bool
------------------------------------------------------------------------

hProp≃Bool : {ℓ : Level} → LEMProp ℓ → hProp ℓ ≃ Bool
hProp≃Bool lem = isoToEquiv (iso (Decide.fun lem) (Decide.back lem)
                                 (Decide.rinv lem) (Decide.linv lem))

------------------------------------------------------------------------
-- 定理二（主定理）：LEM ⇒ SingleOmega（Ω := Lift Bool）
------------------------------------------------------------------------

SingleOmega-from-LEM : {ℓ : Level} → LEMProp ℓ → SingleOmega ℓ
SingleOmega-from-LEM {ℓ} lem =
  Lift {ℓ-zero} {ℓ} Bool ,
  (isSetLift isSetBool ,
   isoToEquiv (iso (λ Lb → Decide.back lem (lower Lb))
                   (λ P → lift (Decide.fun lem P))
                   (λ P → Decide.linv lem P)
                   (λ Lb → liftExt (Decide.rinv lem (lower Lb)))))

------------------------------------------------------------------------
-- 定理三：LEM ⇒ Necessity（前提 ℝLayerAt 未被使用——必要性无经典内容）
------------------------------------------------------------------------

LEM→Necessity : {ℓ : Level} → LEMProp ℓ → Necessity ℓ
LEM→Necessity lem _ = SingleOmega-from-LEM lem
