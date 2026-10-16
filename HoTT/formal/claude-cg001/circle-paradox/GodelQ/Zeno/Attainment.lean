import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Bases
import Mathlib.Order.Filter.AtTopBot.CountablyGenerated

/-!
# CG-007 · W2（一）：取到与贴近——稠密性恰是二者分开的前提

研究发起人固定的原过程完成是“有限自然数阶段余量精确为零”（dev-01 #19）：在某个有限阶段恰好取到终点
（`AttainsAt`）。极限理论的标准解把“到达”说成极限意义的到达（`ArrivesAt`）：无限贴近终点。

* `attains_iff_isolated`（**归因定理**）：在第一可数空间里，“每个极限意义到达 x 的过程都在某个有限阶段
  取到 x”，当且仅当 x 是孤立点。也就是说，两种“到达”分开，恰好是因为终点不孤立——终点处有稠密性。
* `real_not_isolated`：ℝ 中每一点都不孤立；`zenoSeq x` 是在 x 处的芝诺式过程：贴近 x，却在每个有限阶段
  都没到 x。
* `grid`：粒度为 2⁻ᵐ 的格点（量子化的位置或时刻），放在同一条实数轴里，用同一个收敛概念。
  `grid_eventually_eq`：取值在格点上的过程若极限意义到达 L，则从某个有限阶段起一直在 L——在量子化的空间里，
  贴近就是取到。
* `discrete_attains`：任何离散空间里同样成立。

这里的定理是 Mathlib 实分析与拓扑（子理论）中的定理；“现实是量子化的”是研究发起人的物理立场
（KC-000003、KC-000004），不是这里证明的东西。
-/

namespace GodelQ.Zeno

open Filter Topology

section general

variable {X : Type*} [TopologicalSpace X]

/-- 在某个有限阶段恰好取到 x（原过程完成：有限阶段余量精确为零）。 -/
def AttainsAt (s : ℕ → X) (x : X) : Prop := ∃ n, s n = x

/-- 极限意义的到达（标准解的完成）。 -/
def ArrivesAt (s : ℕ → X) (x : X) : Prop := Tendsto s atTop (𝓝 x)

/-- x 是孤立点：x 的去心邻域滤子是空的。 -/
def Isolated (x : X) : Prop := 𝓝[≠] x = ⊥

theorem isolated_iff_isOpen (x : X) : Isolated x ↔ IsOpen ({x} : Set X) :=
  (isOpen_singleton_iff_punctured_nhds x).symm

/-- 孤立点处，极限意义的到达从某个有限阶段起一直取到。 -/
theorem eventually_eq_of_isolated {x : X} (hx : Isolated x) {s : ℕ → X} (hs : ArrivesAt s x) :
    ∀ᶠ n in atTop, s n = x :=
  hs.eventually (((isolated_iff_isOpen x).mp hx).mem_nhds rfl)

theorem attains_of_isolated {x : X} (hx : Isolated x) {s : ℕ → X} (hs : ArrivesAt s x) :
    AttainsAt s x :=
  (eventually_eq_of_isolated hx hs).exists

/-- 非孤立点处（第一可数空间），有一个极限意义到达、却在每个有限阶段都没取到的过程。 -/
theorem exists_zeno_of_not_isolated [FirstCountableTopology X] {x : X} (hx : ¬ Isolated x) :
    ∃ s : ℕ → X, ArrivesAt s x ∧ ∀ n, s n ≠ x := by
  have : NeBot (𝓝[≠] x) := ⟨hx⟩
  obtain ⟨s, hs⟩ := Filter.exists_seq_tendsto (𝓝[≠] x)
  rw [tendsto_nhdsWithin_iff] at hs
  obtain ⟨hlim, hne⟩ := hs
  obtain ⟨N, hN⟩ := eventually_atTop.mp hne
  refine ⟨fun n => s (n + N), (tendsto_add_atTop_iff_nat N).mpr hlim, fun n => ?_⟩
  have := hN (n + N) (Nat.le_add_left N n)
  simpa using this

/-- **归因定理**：在第一可数空间里，“每个极限意义到达 x 的过程都在某个有限阶段取到 x”
当且仅当 x 是孤立点。 -/
theorem attains_iff_isolated [FirstCountableTopology X] (x : X) :
    (∀ s : ℕ → X, ArrivesAt s x → AttainsAt s x) ↔ Isolated x := by
  constructor
  · intro h
    by_contra hx
    obtain ⟨s, hs, hne⟩ := exists_zeno_of_not_isolated hx
    obtain ⟨n, hn⟩ := h s hs
    exact hne n hn
  · intro hx s hs
    exact attains_of_isolated hx hs

/-- 离散空间（每一点都孤立）里，极限意义的到达从某个有限阶段起一直取到。 -/
theorem discrete_attains [DiscreteTopology X] {s : ℕ → X} {x : X} (hs : ArrivesAt s x) :
    ∀ᶠ n in atTop, s n = x :=
  eventually_eq_of_isolated ((isolated_iff_isOpen x).mpr (isOpen_discrete _)) hs

end general

/-! ## ℝ：每一点都有芝诺式过程 -/

/-- 芝诺式过程：从 x 的左侧出发，每步走剩下的一半。 -/
noncomputable def zenoSeq (x : ℝ) (n : ℕ) : ℝ := x - (1 / 2 : ℝ) ^ n

theorem half_pow_tendsto : Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ n) atTop (𝓝 0) :=
  tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)

theorem zenoSeq_arrives (x : ℝ) : ArrivesAt (zenoSeq x) x := by
  have h := (tendsto_const_nhds (x := x)).sub half_pow_tendsto
  rw [sub_zero] at h
  exact h

theorem zenoSeq_ne (x : ℝ) (n : ℕ) : zenoSeq x n ≠ x := by
  have : (0 : ℝ) < (1 / 2) ^ n := by positivity
  simp only [zenoSeq, ne_eq, sub_eq_self]
  exact this.ne'

/-- ℝ 中没有孤立点：每个终点都有一个贴近它、却在每个有限阶段都没取到它的过程。 -/
theorem real_not_isolated (x : ℝ) : ¬ Isolated x := fun hx => by
  obtain ⟨n, hn⟩ := attains_of_isolated hx (zenoSeq_arrives x)
  exact zenoSeq_ne x n hn

/-! ## 量子化：粒度为 2⁻ᵐ 的格点 -/

/-- 粒度为 2⁻ᵐ 的格点（量子化的位置或时刻），放在同一条实数轴里。 -/
def grid (m : ℕ) : Set ℝ := {r | ∃ k : ℤ, r = k * (1 / 2 : ℝ) ^ m}

theorem zero_mem_grid (m : ℕ) : (0 : ℝ) ∈ grid m := ⟨0, by simp⟩

theorem one_mem_grid (m : ℕ) : (1 : ℝ) ∈ grid m :=
  ⟨2 ^ m, by push_cast; rw [← mul_pow]; norm_num⟩

theorem grid_sub {m : ℕ} {a b : ℝ} (ha : a ∈ grid m) (hb : b ∈ grid m) : a - b ∈ grid m := by
  obtain ⟨k, rfl⟩ := ha
  obtain ⟨l, rfl⟩ := hb
  exact ⟨k - l, by push_cast; ring⟩

/-- 两个格点之差的绝对值若小于一个粒度，它们就相等。 -/
theorem grid_eq_of_abs_lt {m : ℕ} {a b : ℝ} (ha : a ∈ grid m) (hb : b ∈ grid m)
    (h : |a - b| < (1 / 2 : ℝ) ^ m) : a = b := by
  obtain ⟨k, rfl⟩ := ha
  obtain ⟨l, rfl⟩ := hb
  have hδ : (0 : ℝ) < (1 / 2) ^ m := by positivity
  have h' : |((k - l : ℤ) : ℝ)| * (1 / 2) ^ m < 1 * (1 / 2) ^ m := by
    have e : (k : ℝ) * (1 / 2) ^ m - l * (1 / 2) ^ m = ((k - l : ℤ) : ℝ) * (1 / 2) ^ m := by
      push_cast; ring
    rw [e, abs_mul, abs_of_pos hδ] at h
    simpa using h
  have h1 : |((k - l : ℤ) : ℝ)| < 1 := lt_of_mul_lt_mul_right h' hδ.le
  have h2 : |k - l| < 1 := by exact_mod_cast h1
  have h3 : k - l = 0 := Int.abs_lt_one_iff.mp h2
  have : k = l := by omega
  rw [this]

/-- 两个格点若 a < b，则 b - a 至少是一个粒度。 -/
theorem grid_gap {m : ℕ} {a b : ℝ} (ha : a ∈ grid m) (hb : b ∈ grid m) (h : a < b) :
    (1 / 2 : ℝ) ^ m ≤ b - a := by
  rcases le_or_gt ((1 / 2 : ℝ) ^ m) (b - a) with hle | hlt
  · exact hle
  exfalso
  have hab : |a - b| < (1 / 2 : ℝ) ^ m := by
    rw [abs_sub_comm, abs_of_pos (by linarith)]
    exact hlt
  exact h.ne (grid_eq_of_abs_lt ha hb hab)

/-- **量子化空间里，贴近就是取到**：取值在格点上、极限意义到达 L 的过程，从某个有限阶段起一直在 L。 -/
theorem grid_eventually_eq {m : ℕ} {s : ℕ → ℝ} (hs : ∀ n, s n ∈ grid m) {L : ℝ}
    (h : ArrivesAt s L) : ∀ᶠ n in atTop, s n = L := by
  have hδ : (0 : ℝ) < (1 / 2) ^ m := by positivity
  obtain ⟨N, hN⟩ := Metric.tendsto_atTop.mp h ((1 / 2) ^ m / 2) (by positivity)
  have hconst : ∀ n ≥ N, s n = s N := fun n hn => by
    apply grid_eq_of_abs_lt (hs n) (hs N)
    have h1 := hN n hn
    have h2 := hN N le_rfl
    rw [Real.dist_eq] at h1 h2
    calc |s n - s N| ≤ |s n - L| + |L - s N| := abs_sub_le _ _ _
      _ = |s n - L| + |s N - L| := by rw [abs_sub_comm L]
      _ < (1 / 2) ^ m / 2 + (1 / 2) ^ m / 2 := add_lt_add h1 h2
      _ = (1 / 2) ^ m := by ring
  have hL : s N = L := by
    have h' : Tendsto s atTop (𝓝 (s N)) :=
      tendsto_const_nhds.congr' (eventually_atTop.mpr ⟨N, fun n hn => (hconst n hn).symm⟩)
    exact tendsto_nhds_unique h' h
  exact eventually_atTop.mpr ⟨N, fun n hn => (hconst n hn).trans hL⟩

theorem grid_attains {m : ℕ} {s : ℕ → ℝ} (hs : ∀ n, s n ∈ grid m) {L : ℝ} (h : ArrivesAt s L) :
    AttainsAt s L :=
  (grid_eventually_eq hs h).exists

end GodelQ.Zeno

#print axioms GodelQ.Zeno.attains_iff_isolated
#print axioms GodelQ.Zeno.discrete_attains
#print axioms GodelQ.Zeno.real_not_isolated
#print axioms GodelQ.Zeno.grid_eq_of_abs_lt
#print axioms GodelQ.Zeno.grid_gap
#print axioms GodelQ.Zeno.grid_eventually_eq
#print axioms GodelQ.Zeno.grid_attains
