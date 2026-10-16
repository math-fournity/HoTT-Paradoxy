import GodelQ.Zeno.Runners

/-!
# CG-007 · W2：命题对照（CG001-C-106、C-107、C-108）

每条命题的类型逐字写在这里，证明只引用前面文件中的定理。
-/

namespace GodelQ.Zeno.Qual

open Filter Topology GodelQ.Zeno

/-- **CG001-C-106（归因：稠密性恰是“贴近”与“取到”分开的前提）**：
(1) 第一可数空间中，“每个极限意义到达 x 的过程都在某个有限阶段取到 x” ⟺ x 孤立；
(2) ℝ 中每一点都不孤立，`zenoSeq x` 贴近 x、却在每个有限阶段都没取到 x；
(3) 取值在粒度 2⁻ᵐ 格点上的过程，极限意义到达 L 则从某个有限阶段起一直在 L；
(4) 任何离散空间里同样如此。 -/
theorem qual_C106 :
    (∀ (X : Type) [TopologicalSpace X] [FirstCountableTopology X] (x : X),
      (∀ s : ℕ → X, ArrivesAt s x → AttainsAt s x) ↔ Isolated x) ∧
    (∀ x : ℝ, ¬ Isolated x ∧ ArrivesAt (zenoSeq x) x ∧ ∀ n, zenoSeq x n ≠ x) ∧
    (∀ (m : ℕ) (s : ℕ → ℝ) (L : ℝ), (∀ n, s n ∈ grid m) → ArrivesAt s L →
      ∀ᶠ n in atTop, s n = L) ∧
    (∀ (X : Type) [TopologicalSpace X] [DiscreteTopology X] (s : ℕ → X) (x : X),
      ArrivesAt s x → ∀ᶠ n in atTop, s n = x) :=
  ⟨fun _ _ _ x => attains_iff_isolated x,
   fun x => ⟨real_not_isolated x, zenoSeq_arrives x, zenoSeq_ne x⟩,
   fun _ _ _ hs h => grid_eventually_eq hs h,
   fun _ _ _ _ _ h => discrete_attains h⟩

/-- **CG001-C-107（二分跑者、极限接口的碰撞、完成在稠密化的极限里丢失）**：
(1) 量子化跑者由“走一半再向下取整到格点”逐步定义，闭式为：第 0 至 m 步剩余 `(1/2)ⁿ`，此后为 0；它走在格点上；
(2) 它恰在第 m+1 步完成，第 0 至 m 步与稠密跑者相同；稠密跑者永不完成；
(3) 没有只看极限值的判据能判对“是否取到”；接口带上粒度则有；
(4) 每一档都在有限步完成，逐步收敛到的稠密跑者却永不完成，位置的累次极限都是 1。 -/
theorem qual_C107 :
    (∀ m n, quantRem m (n + 1) = quantStep m (quantRem m n)) ∧
    (∀ m n, quantRem m n = if n ≤ m then (1 / 2 : ℝ) ^ n else 0) ∧
    (∀ m n, quantPos m n ∈ grid m) ∧
    (∀ m, quantPos m (m + 1) = 1 ∧ ∀ n ≤ m, quantPos m n < 1) ∧
    (∀ m n, n ≤ m → quantPos m n = densePos n) ∧
    (∀ n, densePos n < 1) ∧
    (¬ ∃ g : ℝ → Prop, ∀ (s : ℕ → ℝ) (L : ℝ), ArrivesAt s L → (g L ↔ AttainsAt s L)) ∧
    (∀ m (s : ℕ → ℝ) (L : ℝ), (∀ n, s n ∈ grid m) → ArrivesAt s L → AttainsAt s L) ∧
    ((∀ m, AttainsAt (quantPos m) 1) ∧ ¬ AttainsAt densePos 1 ∧
      (∀ n, Tendsto (fun m => quantPos m n) atTop (𝓝 (densePos n))) ∧
      (∀ m, ArrivesAt (quantPos m) 1) ∧ ArrivesAt densePos 1) ∧
    Tendsto (fun m : ℕ => m + 1) atTop atTop :=
  ⟨quantRem_succ, quantRem_closed, quantPos_mem_grid, quant_completion_stage,
   fun _ _ h => quant_agrees_dense h, densePos_lt_one, no_limit_decoder, grid_decoder,
   completion_lost_in_limit, completion_stage_tendsto⟩

/-- **CG001-C-108（时间一侧：超任务要靠稠密的时间）**：
(1) 稠密时间里，无穷多个阶段严格递增、都在时刻 1 之前，并以 1 为极限；
(2) 正控制：标准解的连续运动在时刻 1 ∈ [0,1] 取到 1，在每个阶段时刻恰在该阶段的位置；
(3) 时刻 1 不是任何有限阶段；
(4) 量子化时间里，严格递增的阶段时刻没有上界。 -/
theorem qual_C108 :
    (StrictMono stageTime ∧ (∀ n, stageTime n < 1) ∧ ArrivesAt stageTime 1) ∧
    ((1 : ℝ) ∈ Set.Icc (0 : ℝ) 1 ∧ (fun t : ℝ => t) 1 = 1 ∧
      ∀ n, (fun t : ℝ => t) (stageTime n) = densePos n) ∧
    (∀ n, stageTime n ≠ 1) ∧
    (∀ (m : ℕ) (t : ℕ → ℝ), (∀ n, t n ∈ grid m) → StrictMono t → ¬ BddAbove (Set.range t)) :=
  ⟨dense_supertask, continuous_endpoint_control, arrival_time_not_a_stage,
   fun _ _ ht hmono => grid_no_supertask ht hmono⟩

end GodelQ.Zeno.Qual

#print axioms GodelQ.Zeno.Qual.qual_C106
#print axioms GodelQ.Zeno.Qual.qual_C107
#print axioms GodelQ.Zeno.Qual.qual_C108
