import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 L1：translate 的语法 API 清单（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCArith

namespace ProbeL1

-- A. translate 作为 LogicalConnective.Hom 已有的交换律
example {ξ : Type*} {n : ℕ} (φ ψ : Semiformula ℒₒᵣ ξ n) :
    arithTrln.translate (φ ⋏ ψ) = arithTrln.translate φ ⋏ arithTrln.translate ψ := rfl
example {ξ : Type*} {n : ℕ} (φ ψ : Semiformula ℒₒᵣ ξ n) :
    arithTrln.translate (φ ⋎ ψ) = arithTrln.translate φ ⋎ arithTrln.translate ψ := rfl
example {ξ : Type*} {n : ℕ} (φ : Semiformula ℒₒᵣ ξ n) :
    arithTrln.translate (∼φ) = ∼arithTrln.translate φ := by simp

-- B. 代入 / 移位 / free / setShift 的 API 名称
#check @Semiformula.subst
#check @Semiformula.shift
#check @Semiformula.substs
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.free
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.setShift
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.vecToSet
#check @Rew.emb

-- C. translate 与 subst 的关系（关键未知）
#check @FFL.FirstOrder.DirectTranslation.translate
#check @LogicalConnective.Hom.map_subst

end ProbeL1
