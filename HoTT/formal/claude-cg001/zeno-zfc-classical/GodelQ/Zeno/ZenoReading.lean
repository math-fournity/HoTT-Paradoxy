import Mathlib.Analysis.SpecificLimits.Basic

/-!
# CG-010 R1：经典芝诺两句的实数读法（CG001-C-423 的桥）

`ZenoClassicalZFC.lean` 的算术句在标准模型 ℕ 里读作：
* `halvedC K n`（K ≤ n）恰是“第 n 步后的剩余距离 (1/2)ⁿ 不超过 2⁻ᴷ”（`zeno_halved_iff_real`）；
* `arriveC` 恰是剩余距离趋于 0 的 ε–N 写法（ε 取 2⁻ᴷ），而剩余距离确实趋于 0（`zeno_remaining_tendsto_zero`），
  即位置 1 − (1/2)ⁿ 趋于 1——这是 C-106、C-108 里的芝诺序列；
* `noFiniteC` 恰是“没有哪一步剩余距离为 0”：每一步的剩余距离都是正数（`zeno_remaining_pos`），
  而“剩余距离为 0”恰是对每个 K 都不超过 2⁻ᴷ（`zeno_remaining_zero_iff_all_halved`，在实数里不成立）。
-/

namespace GodelQ.ZenoReading

open Filter Topology

/-- 第 n 步后的剩余距离 (1/2)ⁿ 不超过 2⁻ᴷ，恰是 K ≤ n。 -/
theorem zeno_halved_iff_real (K n : ℕ) : (1 / 2 : ℝ) ^ n ≤ (1 / 2) ^ K ↔ K ≤ n :=
  pow_le_pow_iff_right_of_lt_one₀ (by norm_num) (by norm_num)

/-- 剩余距离趋于 0（位置趋于 1）。 -/
theorem zeno_remaining_tendsto_zero : Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ n) atTop (𝓝 0) :=
  tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)

/-- 每一步的剩余距离都是正数。 -/
theorem zeno_remaining_pos (n : ℕ) : (0 : ℝ) < (1 / 2) ^ n := pow_pos (by norm_num) n

/-- 在第 n 步“对每个 K 都已减半 K 次”，在实数里恰是剩余距离为 0；它不成立。 -/
theorem zeno_remaining_zero_iff_all_halved (n : ℕ) :
    (∀ K : ℕ, (1 / 2 : ℝ) ^ n ≤ (1 / 2) ^ K) ↔ False := by
  constructor
  · intro h
    exact absurd ((zeno_halved_iff_real (n + 1) n).mp (h (n + 1))) (by omega)
  · intro h; exact h.elim

end GodelQ.ZenoReading

#print axioms GodelQ.ZenoReading.zeno_halved_iff_real
#print axioms GodelQ.ZenoReading.zeno_remaining_tendsto_zero
#print axioms GodelQ.ZenoReading.zeno_remaining_pos
#print axioms GodelQ.ZenoReading.zeno_remaining_zero_iff_all_halved
