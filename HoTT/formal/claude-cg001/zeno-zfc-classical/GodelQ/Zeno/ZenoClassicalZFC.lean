import GodelQ.ZFC.PAModel

/-!
# CG-010 R1：经典芝诺的两句落到 Foundation 的 𝗭𝗙𝗖（CG001-C-423）

缺口表第 9 行、CN-076 §6 第 1 条：经典芝诺（每次走剩下的一半，没有别的花样）上，
“极限是 1”与“哪一步都到不了 1”这两句，𝗭𝗙𝗖 都证得出——此前只是数学上显然，没有在真实的 𝗭𝗙𝗖 上
机器核对。研究发起人 2026-10-14 确认 Q 是 ASK（判断一句表述的计算可不可停机）之后，这两句的作用是：
𝗭𝗙𝗖 看得见过程的两面，缺的是门口那一问（ASK），不是眼睛。

算术写法沿用 W5（C-117）的跑者，只是去掉驱动过程：

* `halvedC K n := K ≤ n`：到第 n 步，跑者至少已减半 K 次，即剩余距离 ≤ 2⁻ᴷ（经典芝诺每一步都减半）；
* `arriveC := ∀K ∃N ∀n (N ≤ n → halvedC K n)`：极限意义的到达，剩余距离趋于 0 的 ε–N 写法，ε 取 2⁻ᴷ；
* `noFiniteC := ¬∃n ∀K halvedC K n`：没有哪一步余量为零（余量为零即对每个 K 都已减半 K 次）。

主定理：
* `models_arriveC`、`models_noFiniteC`：在每一个 𝗣𝗔⁻ 模型里两句都成立（只用 `K ≤ K` 与 `n < n + 1`）；
* `zfc_arriveC`、`zfc_noFiniteC`：𝗭𝗙𝗖 证明两句的翻译（经 C-109：每个 𝗭𝗙𝗖 模型的 ω 满足 𝗣𝗔，再用完备性）；
* `zfc_not_finiteArrival`：𝗭𝗙𝗖 证明不了“有一步余量为零”的翻译（由 𝗭𝗙𝗖 的一致性，Lean 元层 `Universe` 模型）。
-/

namespace GodelQ.ZenoZFC

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCArith

/-- 经典芝诺：到第 n 步已减半 K 次，恰是 K ≤ n。 -/
noncomputable def halvedC : ArithmeticSemisentence 2 := “K n. K ≤ n”

/-- 极限意义的到达：对每个精度 2⁻ᴷ，从某一步起剩余距离都不超过它。 -/
noncomputable def arriveC : ArithmeticSentence := “∀ K, ∃ N, ∀ n, N ≤ n → !halvedC K n”

/-- 没有哪一步余量为零。 -/
noncomputable def noFiniteC : ArithmeticSentence := “¬∃ n, ∀ K, !halvedC K n”

section model

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻]

theorem eval_halvedC (K n : V) : halvedC.Evalb ![K, n] ↔ K ≤ n := by
  simp [halvedC]

/-- 每一个 𝗣𝗔⁻ 模型里，极限意义的到达成立（取 N = K）。 -/
theorem models_arriveC : V↓[ℒₒᵣ] ⊧ arriveC := by
  simp only [arriveC, models_iff]
  simp [halvedC]
  intro K
  exact ⟨K, fun n hn => hn⟩

/-- 每一个 𝗣𝗔⁻ 模型里，没有哪一步余量为零（取 K = n + 1）。 -/
theorem models_noFiniteC : V↓[ℒₒᵣ] ⊧ noFiniteC := by
  simp only [noFiniteC, models_iff]
  simp [halvedC]
  intro n
  exact ⟨n + 1, lt_add_one n⟩

end model

/-- **𝗭𝗙𝗖 证明经典芝诺的极限意义到达。** -/
theorem zfc_arriveC : 𝗭𝗙𝗖 ⊢ arithTrln.translate arriveC := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  apply DirectTranslation.Model.translate_iff.mpr
  exact (models_N_iff (M := M) arriveC).mpr models_arriveC

/-- **𝗭𝗙𝗖 证明经典芝诺没有哪一步余量为零。** -/
theorem zfc_noFiniteC : 𝗭𝗙𝗖 ⊢ arithTrln.translate noFiniteC := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  apply DirectTranslation.Model.translate_iff.mpr
  exact (models_N_iff (M := M) noFiniteC).mpr models_noFiniteC

/-- **𝗭𝗙𝗖 证明不了“有一步余量为零”**（`noFiniteC` 的否定的翻译）。用到 𝗭𝗙𝗖 的一致性
（Foundation 的 `zfc_consistent`，Lean 元层 `Universe` 模型）。 -/
theorem zfc_not_finiteArrival : 𝗭𝗙𝗖 ⊬ ∼ arithTrln.translate noFiniteC := by
  intro h
  have h1 : 𝗭𝗙𝗖 ⊢ arithTrln.translate noFiniteC := zfc_noFiniteC
  apply Entailment.Consistent.not_bot (𝓢 := 𝗭𝗙𝗖)
  cl_prover [h, h1]

end GodelQ.ZenoZFC

#print axioms GodelQ.ZenoZFC.models_arriveC
#print axioms GodelQ.ZenoZFC.models_noFiniteC
#print axioms GodelQ.ZenoZFC.zfc_arriveC
#print axioms GodelQ.ZenoZFC.zfc_noFiniteC
#print axioms GodelQ.ZenoZFC.zfc_not_finiteArrival
