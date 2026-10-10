import GodelQ.ZFC.Z0Full

/-! # 探针:D3 路线的管道验证(临时文件,不进收据) -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0Probe

open GodelQ.Z0Full GodelQ.ZFCArith GodelQ.ZFCZ0

-- 1. internalize 对 𝗭𝗙𝗖(集合论、Δ₁)可用:外部证明 → V 内部可导。
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (s : SetTheorySentence)
    (h : 𝗭𝗙𝗖 ⊢ s) : 𝗭𝗙𝗖.internalize V ⊢ (⌜s⌝ : Formula V ℒₛₜ) :=
  internal_provable_of_outer_provable (V := V) h

-- 2. 内部可导 ↔ Provable(tprovable_iff_provable,ℒₛₜ)。
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (s : SetTheorySentence)
    (h : 𝗭𝗙𝗖.internalize V ⊢ (⌜s⌝ : Formula V ℒₛₜ)) : Provable 𝗭𝗙𝗖 (⌜s⌝ : V) :=
  tprovable_iff_provable.mp h

-- 3. translate 作用在语义层公式(ξ = V)上良型,且 map_and/map_top 可用。
example {n : ℕ} (φ ψ : Semiformula ℒₒᵣ V n) :
    arithTrln.translate (φ ⋏ ψ) = arithTrln.translate φ ⋏ arithTrln.translate ψ := rfl

-- 4. 外部定理模式:SetTheory.complete + 模型事实证明(复刻 ArithInterp 的用法)。
example : 𝗭𝗙𝗖 ⊢ “∀ x, !isEmpty x → !isEmpty x” := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp [models_iff]

-- 5. blueprint 归纳原理在语义层公式上可用性检查(P 取一个简单实例)。
example {n : ℕ} (φ : ArithmeticSemisentence n)
    (hp : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ)
    (P : (n : ℕ) → ArithmeticSemisentence n → Prop)
    (hVerum : ∀ n, P n ⊤) (hFalsum : ∀ n, P n ⊥)
    (hEQ : ∀ n t₁ t₂, P n (.rel Language.Eq.eq ![t₁, t₂]))
    (hNEQ : ∀ n t₁ t₂, P n (.nrel Language.Eq.eq ![t₁, t₂]))
    (hLT : ∀ n t₁ t₂, P n (.rel Language.LT.lt ![t₁, t₂]))
    (hNLT : ∀ n t₁ t₂, P n (.nrel Language.LT.lt ![t₁, t₂]))
    (hAnd : ∀ n φ ψ, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ → ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 ψ →
      P n φ → P n ψ → P n (φ ⋏ ψ))
    (hOr : ∀ n φ ψ, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ → ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 ψ →
      P n φ → P n ψ → P n (φ ⋎ ψ))
    (hBall : ∀ n t φ, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ → P (n + 1) φ →
      P n (∀¹[“#0 < !!(Rew.bShift t)”] φ))
    (hExs : ∀ n φ, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ → P (n + 1) φ → P n (∃¹ φ)) :
    P n φ := Bounding.Hierarchy.arithmetic_sigma₁_induction' hp hVerum hFalsum hEQ hNEQ hLT hNLT hAnd hOr hBall hExs

end GodelQ.Z0Probe
