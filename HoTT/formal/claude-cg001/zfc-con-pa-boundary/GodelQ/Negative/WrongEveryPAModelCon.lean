import GodelQ.ZFC.ConPABoundary

/-!
# 负控制 MP-CG001-ZFC-CON-PA-BOUNDARY-NEG-001：ℕ 上 Con(𝗣𝗔) 的证明，照搬到任意 𝗣𝗔 模型

被否定的说法：每个 𝗣𝗔 的模型都满足 Con(𝗣𝗔)。这里照搬主包 `nat_conPA`（ℕ 满足 Con(𝗣𝗔)）的证明，
把 ℕ 换成任意 𝗣𝗔 模型 V。如果这一步成立，C-109（𝗭𝗙𝗖 每个模型的 ω 都是 𝗣𝗔 的模型）加 C-429 (1) 就会直接
给出 𝗭𝗙𝗖 ⊢ Con(𝗣𝗔)。

预期：拒绝。`standard_consistent` 只说 ℕ 里“没有 ⊥ 的证明”恰是 𝗣𝗔 一致；任意 V 里可以有非标准的“证明”，
类型对不上。正面定理：`nat_conPA`、`universe_conPA`；这个说法本身是错的：`pa_model_refutes_conPA`。
-/

namespace GodelQ.ConPA.Negative

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ConPA

theorem every_pa_model_con (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔] : V↓[ℒₒᵣ] ⊧ conPA := by
  simp only [conPA, models_iff]
  exact (Bootstrapping.consistent.defined (T := 𝗣𝗔) (V := V)).mpr
    ((Bootstrapping.standard_consistent 𝗣𝗔).mpr inferInstance)

end GodelQ.ConPA.Negative
