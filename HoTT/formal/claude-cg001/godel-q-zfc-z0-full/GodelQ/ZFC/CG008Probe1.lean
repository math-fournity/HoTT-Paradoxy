import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0Blocked
import GodelQ.ZFC.ZFCSetSigma1

/-!
# CG-008 探针 1（非收据）：判定 §4 路线的可行性

三个问题，用编译回答，不靠推理：

1. 集合语言的内部演算辅助（`eq_refl` 等）是否真的缺失？
2. `tprovable_iff_provable (T := 𝗭𝗙𝗖)` 对集合语言是否如交接单所说可用？
3. `SetTheory.complete` + `internal_provable_of_outer_provable` 对集合理论是否可用？
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe1

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1

/-- 问题 2：集合语言 quote 与 `Provable` 的双向对应（交接单说可用）。 -/
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (ψ : SetTheorySentence) :
    𝗭𝗙𝗖.internalize V ⊢ ⌜(ψ : Sentence ℒₛₑₜ)⌝ ↔ Provable 𝗭𝗙𝗖 (⌜(ψ : Sentence ℒₛₑₜ)⌝ : V) :=
  tprovable_iff_provable (T := 𝗭𝗙𝗖)

/-- 问题 3a：`SetTheory.complete` 给出外部推导。 -/
example (φ : SetTheorySentence)
    (H : ∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], M↓[ℒₛₑₜ] ⊧ φ) :
    𝗭𝗙𝗖 ⊢ φ :=
  SetTheory.complete 𝗭𝗙𝗖 φ H

/-- 问题 3b：由外部推导得到 V 内部的可证性（D1）。 -/
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (φ : SetTheorySentence)
    (h : 𝗭𝗙𝗖 ⊢ φ) : Provable 𝗭𝗙𝗖 (⌜φ⌝ : V) :=
  internalize_provability (T := 𝗭𝗙𝗖) (V := V) h

/-- 问题 1：集合语言里「t = t」是否可由内部演算给出？

这是 §4 路线的第一个硬情形。算术版是 `EquationalTheory.eq_refl`，
但它定义在 `Term V ℒₒᵣ` 上（`variable (T : ArithmeticTheory)`）。
这里测集合语言版是否存在（预期：需要自建）。 -/
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (t : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ t ≐ t := by
  -- 若这一行能编过，说明库里有现成的集合语言 eq_refl。
  exact?

end GodelQ.CG008Probe1
