import GodelQ.Zeno.ZenoClassicalZFC

/-!
# 负控制 MP-CG001-ZENO-ZFC-CLASSICAL-NEG-001：经典芝诺在某一步余量为零

被否定的说法：在每一个 𝗣𝗔⁻ 模型里，都有一步 n，到那一步对每个 K 都已减半 K 次（余量为零）。
这里取“第 0 步”作候选。

预期：拒绝。要证每个 K 都满足 K ≤ 0，证不出。主包的正面定理 `models_noFiniteC`（C-423）证明
这个说法本来就不成立。
-/

namespace GodelQ.ZenoZFC.Negative

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic
open GodelQ.ZenoZFC

theorem finite_arrival {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻] :
    ∃ n : V, ∀ K : V, halvedC.Evalb ![K, n] :=
  ⟨0, fun K => (eval_halvedC K 0).mpr (by simp)⟩

end GodelQ.ZenoZFC.Negative
