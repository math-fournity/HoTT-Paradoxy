import GodelQ.Zeno.Attainment

/-!
# CG-007 · W2（二）：二分跑者、极限接口的碰撞、完成在稠密化的极限里丢失、时间一侧的超任务

* **稠密跑者**：第 n 步后剩余 `(1/2)ⁿ`，位置 `1 - (1/2)ⁿ`。
* **量子化跑者**（粒度 2⁻ᵐ）：每一步走剩余距离的一半，再向下取整到格点（`quantStep`）。
  `quantRem_closed`：剩余距离在第 0 至 m 步是 `(1/2)ⁿ`，此后是 0。推广 D01-C-370（m = 3：8→4→2→1→0）与
  D01-C-371（前 0–3 步余量相同），从一个粒度推广到每个粒度。
* `quant_completion_stage`：量子化跑者恰在第 m+1 步完成；稠密跑者永不完成（`densePos_lt_one`）。
* `no_limit_decoder`：两个跑者的极限都是 1，有限阶段取到与否却不同，所以没有一个只看极限值的判据能判对
  “是否取到”（T-OBS 的实例）。`grid_decoder`：接口里带上粒度，判据就存在（正控制）。
* `completion_lost_in_limit`：粒度趋于零时，量子化跑者逐步收敛到稠密跑者；每一档都在有限步完成，
  完成的步数 m+1 却趋于无穷，极限处的稠密跑者永不完成；位置的两个累次极限都是 1。
* 时间一侧：
  - `dense_supertask`：在稠密时间里，无穷多个阶段严格递增，却都在时刻 1 之前；
  - `continuous_endpoint_control`：标准解的连续运动在时刻 1 ∈ [0,1] 取到 1（正控制，同 C-361 的闭区间端点）；
  - `arrival_time_not_a_stage`：时刻 1 不是任何有限阶段；
  - `grid_no_supertask`：在量子化的时间里，严格递增的阶段时刻没有上界，无穷多个阶段挤不进一个有限时刻之前。
-/

namespace GodelQ.Zeno

open Filter Topology

/-! ## 两种跑者 -/

/-- 稠密跑者第 n 步后的剩余距离。 -/
noncomputable def denseRem (n : ℕ) : ℝ := (1 / 2 : ℝ) ^ n

/-- 稠密跑者第 n 步后的位置。 -/
noncomputable def densePos (n : ℕ) : ℝ := 1 - denseRem n

/-- 量子化半步：走剩余距离的一半，再向下取整到粒度 2⁻ᵐ 的格点。 -/
noncomputable def quantStep (m : ℕ) (r : ℝ) : ℝ := (⌊r / 2 * 2 ^ m⌋ : ℝ) / 2 ^ m

/-- 量子化跑者（粒度 2⁻ᵐ）第 n 步后的剩余距离；起点余量为 1。 -/
noncomputable def quantRem (m : ℕ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => quantStep m (quantRem m n)

/-- 量子化跑者第 n 步后的位置。 -/
noncomputable def quantPos (m n : ℕ) : ℝ := 1 - quantRem m n

theorem quantRem_succ (m n : ℕ) : quantRem m (n + 1) = quantStep m (quantRem m n) := rfl

lemma half_pow_div_two_mul (n j : ℕ) : (1 / 2 : ℝ) ^ n / 2 * 2 ^ (n + 1 + j) = 2 ^ j := by
  have h : (2 : ℝ) ^ n ≠ 0 := by positivity
  rw [pow_add, pow_add, pow_one, one_div, inv_pow]
  field_simp

lemma half_pow_div_two_mul_self (n : ℕ) : (1 / 2 : ℝ) ^ n / 2 * 2 ^ n = 1 / 2 := by
  have h : (2 : ℝ) ^ n ≠ 0 := by positivity
  rw [one_div, inv_pow]
  field_simp

/-- **量子化跑者的闭式**：第 0 至 m 步剩余 `(1/2)ⁿ`，此后剩余 0。 -/
theorem quantRem_closed (m n : ℕ) : quantRem m n = if n ≤ m then (1 / 2 : ℝ) ^ n else 0 := by
  induction n with
  | zero => simp [quantRem]
  | succ n ih =>
    rw [quantRem_succ, ih]
    by_cases h : n + 1 ≤ m
    · rw [ite_eq_left (by omega : n ≤ m), ite_eq_left h]
      obtain ⟨j, rfl⟩ : ∃ j, m = n + 1 + j := ⟨m - (n + 1), by omega⟩
      unfold quantStep
      rw [half_pow_div_two_mul n j]
      have hf : ⌊(2 : ℝ) ^ j⌋ = (2 : ℤ) ^ j := by
        have e : (2 : ℝ) ^ j = (((2 : ℤ) ^ j : ℤ) : ℝ) := by push_cast; ring
        rw [e, Int.floor_intCast]
      rw [hf]
      have h2 : (2 : ℝ) ^ (n + 1) ≠ 0 := by positivity
      push_cast
      rw [pow_add (2 : ℝ) (n + 1) j, one_div, inv_pow]
      field_simp
    · rw [ite_eq_right h]
      by_cases hn : n ≤ m
      · obtain rfl : n = m := by omega
        rw [ite_eq_left le_rfl]
        unfold quantStep
        rw [half_pow_div_two_mul_self n]
        have hf : ⌊(1 / 2 : ℝ)⌋ = 0 := by
          rw [Int.floor_eq_zero_iff]
          constructor <;> norm_num
        rw [hf]
        simp
      · rw [ite_eq_right hn]
        simp [quantStep]

theorem quantRem_agree {m n : ℕ} (h : n ≤ m) : quantRem m n = denseRem n := by
  rw [quantRem_closed, ite_eq_left h]
  rfl

theorem quantRem_after {m n : ℕ} (h : m < n) : quantRem m n = 0 := by
  rw [quantRem_closed, ite_eq_right (by omega)]

theorem quantRem_done (m : ℕ) : quantRem m (m + 1) = 0 := quantRem_after (Nat.lt_succ_self m)

theorem denseRem_pos (n : ℕ) : 0 < denseRem n := by
  unfold denseRem
  positivity

theorem quantRem_pos {m n : ℕ} (h : n ≤ m) : 0 < quantRem m n := by
  rw [quantRem_agree h]
  exact denseRem_pos n

theorem quantRem_mem_grid (m n : ℕ) : quantRem m n ∈ grid m := by
  rw [quantRem_closed]
  split_ifs with h
  · obtain ⟨j, rfl⟩ : ∃ j, m = n + j := ⟨m - n, by omega⟩
    refine ⟨2 ^ j, ?_⟩
    push_cast
    rw [pow_add, mul_comm ((1 / 2 : ℝ) ^ n), ← mul_assoc, ← mul_pow]
    norm_num
  · exact zero_mem_grid m

/-- 量子化跑者始终走在格点上。 -/
theorem quantPos_mem_grid (m n : ℕ) : quantPos m n ∈ grid m :=
  grid_sub (one_mem_grid m) (quantRem_mem_grid m n)

/-! ## 完成与极限 -/

theorem densePos_lt_one (n : ℕ) : densePos n < 1 := by
  unfold densePos
  linarith [denseRem_pos n]

theorem densePos_arrives : ArrivesAt densePos 1 := by
  have h := (tendsto_const_nhds (x := (1 : ℝ))).sub half_pow_tendsto
  rw [sub_zero] at h
  exact h

/-- 稠密跑者永不在有限阶段取到终点。 -/
theorem densePos_not_attains : ¬ AttainsAt densePos 1 := fun ⟨n, hn⟩ => (densePos_lt_one n).ne hn

theorem quantPos_eventually_one (m : ℕ) : ∀ᶠ n in atTop, quantPos m n = 1 :=
  eventually_atTop.mpr ⟨m + 1, fun n hn => by simp [quantPos, quantRem_after (by omega : m < n)]⟩

theorem quantPos_arrives (m : ℕ) : ArrivesAt (quantPos m) 1 :=
  (tendsto_const_nhds (x := (1 : ℝ))).congr' ((quantPos_eventually_one m).mono fun _ hn => hn.symm)

/-- 量子化跑者在有限阶段取到终点。 -/
theorem quantPos_attains (m : ℕ) : AttainsAt (quantPos m) 1 :=
  ⟨m + 1, by simp [quantPos, quantRem_done]⟩

/-- 完成阶段恰是第 m+1 步：此前每一步都还没到。 -/
theorem quant_completion_stage (m : ℕ) : quantPos m (m + 1) = 1 ∧ ∀ n ≤ m, quantPos m n < 1 := by
  refine ⟨by simp [quantPos, quantRem_done], fun n hn => ?_⟩
  unfold quantPos
  linarith [quantRem_pos hn]

/-- 第 0 至 m 步，量子化跑者与稠密跑者逐步相同。 -/
theorem quant_agrees_dense {m n : ℕ} (h : n ≤ m) : quantPos m n = densePos n := by
  simp [quantPos, densePos, quantRem_agree h]

/-! ## 极限接口的碰撞（T-OBS 的实例） -/

/-- **极限接口判不了“取到”**：没有一个只看极限值的判据，能对所有极限意义到达的过程判对
“是否在某个有限阶段取到”。 -/
theorem no_limit_decoder :
    ¬ ∃ g : ℝ → Prop, ∀ (s : ℕ → ℝ) (L : ℝ), ArrivesAt s L → (g L ↔ AttainsAt s L) := by
  rintro ⟨g, hg⟩
  have h1 := hg densePos 1 densePos_arrives
  have h2 := hg (quantPos 0) 1 (quantPos_arrives 0)
  exact densePos_not_attains (h1.mp (h2.mpr (quantPos_attains 0)))

/-- 正控制：接口里带上粒度，判据就存在——格点上的过程，到达即取到。 -/
theorem grid_decoder (m : ℕ) :
    ∀ (s : ℕ → ℝ) (L : ℝ), (∀ n, s n ∈ grid m) → ArrivesAt s L → AttainsAt s L :=
  fun _ _ hs h => grid_attains hs h

/-! ## 完成在稠密化的极限里丢失 -/

/-- 粒度趋于零时，量子化跑者逐步收敛到稠密跑者（第 n 步在 m ≥ n 时已经相同）。 -/
theorem quantPos_tendsto_densePos (n : ℕ) :
    Tendsto (fun m => quantPos m n) atTop (𝓝 (densePos n)) :=
  tendsto_const_nhds.congr' (eventually_atTop.mpr ⟨n, fun _ hm => (quant_agrees_dense hm).symm⟩)

/-- 完成的阶段 m+1 随粒度变细趋于无穷。 -/
theorem completion_stage_tendsto : Tendsto (fun m : ℕ => m + 1) atTop atTop :=
  tendsto_add_atTop_nat 1

/-- **完成在稠密化的极限里丢失**：每一档量子化跑者都在有限阶段完成，它们逐步收敛到的稠密跑者却永不完成；
位置的两个累次极限都是 1（先 n 后 m：每一档的极限都是 1；先 m 后 n：逐步极限是稠密跑者，其极限是 1）。 -/
theorem completion_lost_in_limit :
    (∀ m, AttainsAt (quantPos m) 1) ∧ ¬ AttainsAt densePos 1 ∧
      (∀ n, Tendsto (fun m => quantPos m n) atTop (𝓝 (densePos n))) ∧
      (∀ m, ArrivesAt (quantPos m) 1) ∧ ArrivesAt densePos 1 :=
  ⟨quantPos_attains, densePos_not_attains, quantPos_tendsto_densePos, quantPos_arrives, densePos_arrives⟩

/-! ## 时间一侧 -/

/-- 标准解的连续时间：匀速运动，位置等于时刻；第 n 阶段在时刻 `1 - (1/2)ⁿ` 到达。 -/
noncomputable def stageTime (n : ℕ) : ℝ := densePos n

theorem stageTime_strictMono : StrictMono stageTime := by
  apply strictMono_nat_of_lt_succ
  intro n
  have h := denseRem_pos n
  simp only [stageTime, densePos, denseRem] at h ⊢
  rw [pow_succ]
  nlinarith

/-- **稠密时间里有超任务**：无穷多个阶段严格递增，却都在时刻 1 之前，并以 1 为极限。 -/
theorem dense_supertask : StrictMono stageTime ∧ (∀ n, stageTime n < 1) ∧ ArrivesAt stageTime 1 :=
  ⟨stageTime_strictMono, densePos_lt_one, densePos_arrives⟩

/-- 正控制（同 C-361 的闭区间端点）：标准解的连续运动 `x(t) = t` 在时刻 1 ∈ [0, 1] 取到位置 1，
并且在每个阶段时刻恰在该阶段的位置。 -/
theorem continuous_endpoint_control :
    (1 : ℝ) ∈ Set.Icc (0 : ℝ) 1 ∧ (fun t : ℝ => t) 1 = 1 ∧
      ∀ n, (fun t : ℝ => t) (stageTime n) = densePos n :=
  ⟨⟨zero_le_one, le_rfl⟩, rfl, fun _ => rfl⟩

/-- 但到达的时刻 1 不是任何有限阶段的时刻：它是阶段时刻的极限点。 -/
theorem arrival_time_not_a_stage : ∀ n, stageTime n ≠ 1 := fun n => (densePos_lt_one n).ne

/-- **量子化时间里没有超任务**：时刻取在格点上、严格递增的阶段序列没有上界——
无穷多个阶段挤不进一个有限时刻之前。 -/
theorem grid_no_supertask {m : ℕ} {t : ℕ → ℝ} (ht : ∀ n, t n ∈ grid m) (hmono : StrictMono t) :
    ¬ BddAbove (Set.range t) := by
  have hδ : (0 : ℝ) < (1 / 2) ^ m := by positivity
  have key : ∀ n : ℕ, t 0 + n * (1 / 2 : ℝ) ^ m ≤ t n := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      have := grid_gap (ht n) (ht (n + 1)) (hmono (Nat.lt_succ_self n))
      push_cast
      linarith
  rintro ⟨B, hB⟩
  obtain ⟨n, hn⟩ := exists_nat_gt ((B - t 0) / (1 / 2 : ℝ) ^ m)
  have h1 : t n ≤ B := hB ⟨n, rfl⟩
  have h2 := key n
  have h3 : B - t 0 < n * (1 / 2 : ℝ) ^ m := (div_lt_iff₀ hδ).mp hn
  linarith

end GodelQ.Zeno

#print axioms GodelQ.Zeno.quantRem_closed
#print axioms GodelQ.Zeno.quantPos_mem_grid
#print axioms GodelQ.Zeno.quant_completion_stage
#print axioms GodelQ.Zeno.quant_agrees_dense
#print axioms GodelQ.Zeno.densePos_not_attains
#print axioms GodelQ.Zeno.no_limit_decoder
#print axioms GodelQ.Zeno.grid_decoder
#print axioms GodelQ.Zeno.completion_lost_in_limit
#print axioms GodelQ.Zeno.dense_supertask
#print axioms GodelQ.Zeno.continuous_endpoint_control
#print axioms GodelQ.Zeno.arrival_time_not_a_stage
#print axioms GodelQ.Zeno.grid_no_supertask
