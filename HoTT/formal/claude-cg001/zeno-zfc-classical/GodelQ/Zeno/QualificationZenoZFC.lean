import GodelQ.Zeno.ZenoClassicalZFC
import GodelQ.Zeno.ZenoReading

/-!
# 命题对照：CG001-C-423

经典芝诺的两句在 Foundation 的 𝗭𝗙𝗖 里都是定理：极限意义的到达，以及没有哪一步余量为零；𝗭𝗙𝗖 也证明不了
“有一步余量为零”。标准模型里的读法是实数上的芝诺序列（剩余距离 (1/2)ⁿ）。
-/

namespace GodelQ.ZenoZFC

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open GodelQ.ZFCArith GodelQ.ZenoReading

/-- CG001-C-423。 -/
theorem qual_C423 :
    (𝗭𝗙𝗖 ⊢ arithTrln.translate arriveC) ∧
    (𝗭𝗙𝗖 ⊢ arithTrln.translate noFiniteC) ∧
    (𝗭𝗙𝗖 ⊬ ∼ arithTrln.translate noFiniteC) ∧
    (∀ K n : ℕ, (1 / 2 : ℝ) ^ n ≤ (1 / 2) ^ K ↔ K ≤ n) ∧
    Filter.Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ n) Filter.atTop (nhds 0) ∧
    (∀ n : ℕ, (0 : ℝ) < (1 / 2) ^ n) :=
  ⟨zfc_arriveC, zfc_noFiniteC, zfc_not_finiteArrival, zeno_halved_iff_real, zeno_remaining_tendsto_zero,
    zeno_remaining_pos⟩

end GodelQ.ZenoZFC

#print axioms GodelQ.ZenoZFC.qual_C423
