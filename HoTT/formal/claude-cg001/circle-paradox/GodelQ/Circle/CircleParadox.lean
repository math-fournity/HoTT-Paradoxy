import Mathlib.Topology.Instances.AddCircle.Defs
import Mathlib.Topology.Instances.ZMultiples
import Mathlib.Topology.OpenPartialHomeomorph.Basic
import GodelQ.Zeno.Attainment

/-!
# CG-010 R2：圆环悖论本身（CG001-C-424）

研究发起人原文三（2026-09-01）：
> 一个圆，其上取一点拿走，假设现在的形态是M。然后将两端展开成线段，假设现在的形态是N。此时，问：从M到N似乎
> 没有什么障碍，那么从N复原到M我们可以做到吗？在过程中N的两端，何以，可以逼近到只剩一个点的距离？因为点没有
> 大小，无限小，无论N的两端逼近到什么接近的程度，都无法再还原到M的状态。可是，可是，我们当初确实得到了M啊！
> 为什么变成N之后就无法再回到M了呢？

模型：圆是周长为 1 的圆周 `Ring := AddCircle 1`；拿走的那一点是 0。

* **M**：`M := {0}ᶜ`，圆上取一点拿走。
* **N**：`N := (0, 1)`，两端展开成的线段。两端没有端点，因为那一点被拿走了。
* **从 M 到 N 没有障碍**：`unfold : N ≃ₜ M`，一个同胚，一步完成（`one_step`）。我们当初确实得到了 M。
* **从 N 复原到 M，逐步逼近**：把线段绕回圆上。第 n 步绕过比例 θₙ = 1 − 2⁻⁽ⁿ⁺¹⁾，一端在 0 处，另一端
  （远端）落在 ↑θₙ。
  - `farEnd_arrives`：远端极限意义地到达 0，两端越来越近；
  - `closing_never_attains`：远端在任何有限阶段都没到 0；
  - `range_bend_ne`：每个有限阶段的形态都不是 M；`range_bend_one`：只有在极限那一刻（θ = 1）才是 M；
  - `gap_infinite`：**点没有大小**。每个有限阶段两端之间的缺口都含无穷多个点，永远不是“只剩一个点的距离”；
  - `gap_length_pos`：缺口的长度 2⁻⁽ⁿ⁺¹⁾ 永远大于 0，而“一个点”的长度是 0。
* **为什么**：`zero_not_isolated`，0 在圆上不是孤立点。由 C-106 的归因定理 `attains_iff_isolated`，
  这恰好就是“逼近不等于到达”的前提（稠密）。
* **离散环对照**：点有大小（一格）的环 `Fin m`。
  - `discrete_closing_attains`：任何逼近都在有限阶段到达（C-106 的 `discrete_attains`）；
  - `discreteGap_reaches_one`：每步合拢一格，缺口在有限步内正好只剩被拿走的那一点。
  拆开、合回都在有限步完成。
-/

namespace GodelQ.Circle

open Filter Topology GodelQ.Zeno

instance : Fact ((0 : ℝ) < 1) := ⟨one_pos⟩

/-- 圆：周长为 1 的圆周。 -/
abbrev Ring := AddCircle (1 : ℝ)

/-- M：在圆上取一点（0）拿走。 -/
def M : Set Ring := {(0 : Ring)}ᶜ

/-- N：两端展开成的线段（开区间：拿走的那一点不在两端）。 -/
def N : Set ℝ := Set.Ioo 0 1

/-! ## 从 M 到 N：一步 -/

/-- Mathlib 的局部同胚：开区间 (0, 1) 与圆去掉 ↑0 之间的同胚。 -/
noncomputable def unfoldCore :
    (AddCircle.openPartialHomeomorphCoe (1 : ℝ) 0).source ≃ₜ
      (AddCircle.openPartialHomeomorphCoe (1 : ℝ) 0).target :=
  (AddCircle.openPartialHomeomorphCoe (1 : ℝ) 0).toHomeomorphSourceTarget

theorem source_eq : (AddCircle.openPartialHomeomorphCoe (1 : ℝ) 0).source = N := by
  simp [N]

theorem target_eq : (AddCircle.openPartialHomeomorphCoe (1 : ℝ) 0).target = M := by
  simp [M]

/-- 展开（反过来是复原）的同胚：`N ≃ₜ M`。 -/
noncomputable def unfold : N ≃ₜ M :=
  ((Homeomorph.setCongr source_eq.symm).trans unfoldCore).trans (Homeomorph.setCongr target_eq)

/-- **从 M 到 N 没有障碍**：M 与 N 同胚，展开一步完成；反过来，作为一个映射的复原也存在。 -/
theorem one_step : Nonempty (M ≃ₜ N) := ⟨unfold.symm⟩

/-- 我们当初确实得到了 M：M 非空（例如 ↑(1/2) ∈ M）。 -/
theorem M_nonempty : M.Nonempty := by
  refine ⟨((1 / 2 : ℝ) : Ring), ?_⟩
  simp only [M, Set.mem_compl_iff, Set.mem_singleton_iff]
  rw [AddCircle.coe_eq_zero_iff_of_mem_Ico (by constructor <;> norm_num)]
  norm_num

/-! ## 从 N 复原到 M：逐步逼近 -/

/-- 第 n 步绕过的比例 θₙ = 1 − 2⁻⁽ⁿ⁺¹⁾。 -/
noncomputable def θ (n : ℕ) : ℝ := 1 - (1 / 2 : ℝ) ^ (n + 1)

theorem θ_pos (n : ℕ) : 0 < θ n := by
  have h : (1 / 2 : ℝ) ^ (n + 1) < 1 := pow_lt_one₀ (by norm_num) (by norm_num) (Nat.succ_ne_zero n)
  unfold θ; linarith

theorem θ_lt_one (n : ℕ) : θ n < 1 := by
  have h : (0 : ℝ) < (1 / 2 : ℝ) ^ (n + 1) := pow_pos (by norm_num) _
  unfold θ; linarith

theorem θ_tendsto : Tendsto θ atTop (𝓝 1) := by
  have h : Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ (n + 1)) atTop (𝓝 0) :=
    (tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)).comp (tendsto_add_atTop_nat 1)
  have h2 := (tendsto_const_nhds (x := (1 : ℝ))).sub h
  rw [sub_zero] at h2
  exact h2

/-- **圆环复活了芝诺的幽灵**：合回时远端第 n 步绕过的比例，恰是芝诺跑者（C-106 的 `zenoSeq`）
朝终点 1 跑的第 n + 1 步。 -/
theorem θ_eq_zenoSeq (n : ℕ) : θ n = zenoSeq 1 (n + 1) := rfl

/-- 远端的位置（另一端在 0 处）。 -/
noncomputable def farEnd (n : ℕ) : Ring := (θ n : Ring)

theorem coe_ne_zero_of_mem {s : ℝ} (hs : s ∈ Set.Ioo (0 : ℝ) 1) : ((s : ℝ) : Ring) ≠ 0 := by
  intro h
  rw [AddCircle.coe_eq_zero_iff_of_mem_Ico ⟨hs.1.le, hs.2⟩] at h
  exact hs.1.ne' h

/-- 远端在任何有限阶段都没到 0：两端没有在有限阶段合上。 -/
theorem farEnd_ne_zero (n : ℕ) : farEnd n ≠ 0 := coe_ne_zero_of_mem ⟨θ_pos n, θ_lt_one n⟩

/-- 远端极限意义地到达 0：两端越来越近。 -/
theorem farEnd_arrives : ArrivesAt farEnd (0 : Ring) := by
  have h := ((AddCircle.continuous_mk' (1 : ℝ)).tendsto 1).comp θ_tendsto
  have h1 : ((QuotientAddGroup.mk' (AddSubgroup.zmultiples (1 : ℝ))) 1 : Ring) = 0 :=
    AddCircle.coe_period 1
  rw [h1] at h
  exact h

/-- **无论两端逼近到什么程度，都没有在有限阶段合上。** -/
theorem closing_never_attains : ¬ AttainsAt farEnd (0 : Ring) := by
  rintro ⟨n, hn⟩
  exact farEnd_ne_zero n hn

/-- 0 在圆上不是孤立点（这正是逼近不等于到达的前提）。 -/
theorem zero_not_isolated : ¬ Isolated (0 : Ring) := fun hx =>
  closing_never_attains (attains_of_isolated hx farEnd_arrives)

/-- 第 s 阶段的形态：线段上的点 t 放到圆上 ↑(s·t)。 -/
noncomputable def bend (s : ℝ) (t : N) : Ring := ((s * (t : ℝ) : ℝ) : Ring)

/-- 在极限那一刻（s = 1），形态恰是 M。 -/
theorem range_bend_one : Set.range (bend 1) = M := by
  ext x
  constructor
  · rintro ⟨t, rfl⟩
    simp only [bend, one_mul]
    exact coe_ne_zero_of_mem t.2
  · intro hx
    obtain ⟨b, hb, rfl⟩ := AddCircle.eq_coe_Ico (p := (1 : ℝ)) x
    have hb0 : b ≠ 0 := by
      rintro rfl
      exact hx (by simp)
    refine ⟨⟨b, lt_of_le_of_ne hb.1 (Ne.symm hb0), hb.2⟩, ?_⟩
    simp [bend]

/-- 第 n 阶段的形态里，取不到 ↑θₙ（[0, θₙ) 之外的点都取不到）。 -/
theorem not_mem_range_bend {n : ℕ} {s : ℝ} (hs : s ∈ Set.Ico (θ n) 1) :
    ((s : ℝ) : Ring) ∉ Set.range (bend (θ n)) := by
  rintro ⟨t, ht⟩
  have ht' : θ n * (t : ℝ) ∈ Set.Ico (0 : ℝ) (0 + 1) := by
    have h1 := t.2.1
    have h2 := t.2.2
    have hθ := θ_pos n
    have hθ1 := θ_lt_one n
    constructor
    · positivity
    · nlinarith
  have hs' : s ∈ Set.Ico (0 : ℝ) (0 + 1) := by
    have hθ := θ_pos n
    exact ⟨by linarith [hs.1], by simpa using hs.2⟩
  have heq := (AddCircle.coe_eq_coe_iff_of_mem_Ico ht' hs').mp ht
  have h2 := t.2.2
  have hθ := θ_pos n
  have : θ n * (t : ℝ) < θ n := by nlinarith
  linarith [hs.1]

/-- **每个有限阶段的形态都不是 M。** -/
theorem range_bend_ne (n : ℕ) : Set.range (bend (θ n)) ≠ M := by
  intro h
  have hmem : farEnd n ∈ M := farEnd_ne_zero n
  rw [← h] at hmem
  exact not_mem_range_bend ⟨le_rfl, θ_lt_one n⟩ hmem

/-- 第 n 阶段两端之间的缺口：属于 M、却还没被绕上的点。 -/
def gap (n : ℕ) : Set Ring := M \ Set.range (bend (θ n))

/-- **点没有大小**：每个有限阶段的缺口都含无穷多个点，永远不是“只剩一个点”。 -/
theorem gap_infinite (n : ℕ) : (gap n).Infinite := by
  have hI : (Set.Ioo (θ n) 1).Infinite := Set.Ioo_infinite (θ_lt_one n)
  have hinj : Set.InjOn (fun s : ℝ => ((s : ℝ) : Ring)) (Set.Ioo (θ n) 1) := by
    intro a ha b hb hab
    have hθ := θ_pos n
    exact (AddCircle.coe_eq_coe_iff_of_mem_Ico (a := (0 : ℝ))
      ⟨by linarith [ha.1], by simpa using ha.2⟩ ⟨by linarith [hb.1], by simpa using hb.2⟩).mp hab
  refine Set.Infinite.mono ?_ (hI.image hinj)
  rintro x ⟨s, hs, rfl⟩
  have hθ := θ_pos n
  refine ⟨coe_ne_zero_of_mem ⟨by linarith [hs.1], hs.2⟩, ?_⟩
  exact not_mem_range_bend ⟨hs.1.le, hs.2⟩

/-- 缺口的长度：远端到 0 还差 2⁻⁽ⁿ⁺¹⁾，永远大于 0；“一个点”的长度是 0。 -/
theorem gap_length_pos (n : ℕ) : 0 < 1 - θ n := by
  have := θ_lt_one n; linarith

/-! ## 离散环对照：点有大小 -/

/-- 离散环（`Fin m`，每一点都孤立）里，任何逼近都在有限阶段到达（C-106 的 `discrete_attains`）。 -/
theorem discrete_closing_attains {m : ℕ} {s : ℕ → Fin m} {x : Fin m} (hs : ArrivesAt s x) :
    AttainsAt s x :=
  (discrete_attains hs).exists

/-- 离散环里，两端之间的缺口（按格数计，含被拿走的那一点）从 g₀ 起每步合拢一格，至少剩 1 格。 -/
def discreteGap (g₀ k : ℕ) : ℕ := max 1 (g₀ - k)

/-- **离散环里，缺口在有限步内正好只剩被拿走的那一点**：第 g₀ − 1 步起缺口为 1 格，环复原。 -/
theorem discreteGap_reaches_one (g₀ : ℕ) : ∀ k, g₀ - 1 ≤ k → discreteGap g₀ k = 1 := by
  intro k hk
  unfold discreteGap
  omega

end GodelQ.Circle

#print axioms GodelQ.Circle.one_step
#print axioms GodelQ.Circle.θ_eq_zenoSeq
#print axioms GodelQ.Circle.M_nonempty
#print axioms GodelQ.Circle.farEnd_arrives
#print axioms GodelQ.Circle.closing_never_attains
#print axioms GodelQ.Circle.zero_not_isolated
#print axioms GodelQ.Circle.range_bend_one
#print axioms GodelQ.Circle.range_bend_ne
#print axioms GodelQ.Circle.gap_infinite
#print axioms GodelQ.Circle.gap_length_pos
#print axioms GodelQ.Circle.discrete_closing_attains
#print axioms GodelQ.Circle.discreteGap_reaches_one
