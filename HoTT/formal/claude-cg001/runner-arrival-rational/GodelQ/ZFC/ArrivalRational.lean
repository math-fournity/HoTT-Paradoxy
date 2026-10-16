import GodelQ.ZFC.ArrivalZFC

/-!
# CG-010 R7：极限的有理数 ε–N 写法落到 𝗭𝗙𝗖（CG001-C-428）

缺口表第 2 行：跑者到达句（C-117、C-118）与经典芝诺（C-423）在 𝗭𝗙𝗖 里都只用 2⁻ᴷ 这一族精度，写成“已减半至少
K 次”；通常的极限定义对**每个**正精度 ε 说话，实数一侧只在 Mathlib（Lean 元层）里。

本文件不构造实数，而是把 ε 取遍**全部正有理数** p/q（p、q 是 ω 里的正整数），用 Foundation 的算术指数
`Exp.exp`（2ᴷ）写出通常的 ε–N 句：

* `arrRatF e`：对每个正有理数 p/q，从某一步起，跑者的剩余距离都小于 p/q。剩余距离小于 p/q，写成“有 K，
  q < p·2ᴷ，并且已减半至少 K 次”。
* `arriveRatC`：经典芝诺，对每个正有理数 p/q，从某一步起 2⁻ⁿ < p/q，即 q < p·2ⁿ。

主定理：

* 在**每一个** 𝗜𝚺₁ 模型里，`arrRatF e ↔ arrF e`（`arrRat_iff_arr`）：有理精度的到达，恰是 2⁻ᴷ 精度的到达。
* 𝗭𝗙𝗖 逐个证明有理精度的到达句与 C-118 的到达句等价，因而与永不停机句等价（`zfc_arrRat_iff_never`）。
* 有一个跑者确实到达，𝗭𝗙𝗖 每一刻都确认它尚未停，却证明不了它的有理精度到达句（`zfc_runner_rat`）。
* 𝗭𝗙𝗖 证明经典芝诺的有理精度极限句（`zfc_arriveRatC`）。
* 标准模型里的读法：两句逐字是通常的 ε–N 写法，ε 取遍正有理数（`arrRat_encode_rat`、`arriveRatC_nat`）。

在实数里，取遍正有理数的 ε 与取遍正实数的 ε 等价（阿基米德性质）；这一步在 Lean 元层，本文件没有在
𝗭𝗙𝗖 内部构造实数。
-/

namespace GodelQ.ArrivalRat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound GodelQ.Arrival GodelQ.ArrivalZFC

/-! ## 算术层 -/

/-- `arrRatF e`：对每个正有理数 p/q，从某一步起，剩余距离都小于 p/q。 -/
noncomputable def arrRatF : ArithmeticSemisentence 1 :=
  “e. ∀ p, ∀ q, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → ∃ K, ∃ y, !expDef y K ∧ q < p * y ∧ !halvedF e K n”

/-- 经典芝诺的有理精度极限句：对每个正有理数 p/q，从某一步起 q < p·2ⁿ，即 2⁻ⁿ < p/q。 -/
noncomputable def arriveRatC : ArithmeticSentence :=
  “∀ p, ∀ q, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → ∃ y, !expDef y n ∧ q < p * y”

section model

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

theorem eval_arrRatF (e : V) : arrRatF.Evalb ![e] ↔
    ∀ p q : V, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n →
      ∃ K, q < p * Exp.exp K ∧ halvedF.Evalb ![e, K, n] := by
  simp [arrRatF]

/-- 已减半至少 K' 次，就已减半至少 K 次（K ≤ K'）。 -/
theorem halved_mono_K {e K K' n : V} (hK : K ≤ K') (h : halvedF.Evalb ![e, K', n]) :
    halvedF.Evalb ![e, K, n] := by
  rw [eval_halvedF] at h ⊢
  exact ⟨le_trans hK h.1, fun i hi => h.2 i (lt_of_lt_of_le hi hK)⟩

/-- **每一个 𝗜𝚺₁ 模型里，有理精度的到达恰是 2⁻ᴷ 精度的到达。** -/
theorem arrRat_iff_arr (e : V) : arrRatF.Evalb ![e] ↔ arrF.Evalb ![e] := by
  rw [eval_arrRatF, eval_arrF]
  constructor
  · intro h K
    obtain ⟨N, hN⟩ := h 1 (Exp.exp K) one_pos (exp_pos K)
    refine ⟨N, fun n hn => ?_⟩
    obtain ⟨K', hlt, hhalf⟩ := hN n hn
    have hlt' : Exp.exp K < Exp.exp K' := by simpa using hlt
    exact halved_mono_K (le_of_lt (exp_monotone.mp hlt')) hhalf
  · intro h p q hp _
    obtain ⟨N, hN⟩ := h q
    refine ⟨N, fun n hn => ⟨q, ?_, hN n hn⟩⟩
    have h1 : q < Exp.exp q := lt_exp q
    have h2 : Exp.exp q ≤ p * Exp.exp q := le_mul_of_one_le_left zero_le (pos_iff_one_le.mp hp)
    exact lt_of_lt_of_le h1 h2

theorem models_arriveRatC_iff : V↓[ℒₒᵣ] ⊧ arriveRatC ↔
    ∀ p q : V, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → q < p * Exp.exp n := by
  simp [arriveRatC, models_iff]

/-- 每一个 𝗜𝚺₁ 模型里，经典芝诺的有理精度极限句成立（取 N = q）。 -/
theorem models_arriveRatC : V↓[ℒₒᵣ] ⊧ arriveRatC := by
  rw [models_arriveRatC_iff]
  intro p q hp _
  refine ⟨q, fun n hn => ?_⟩
  have h1 : q < Exp.exp q := lt_exp q
  have h2 : Exp.exp q ≤ Exp.exp n := exp_monotone_le.mpr hn
  have h3 : Exp.exp n ≤ p * Exp.exp n := le_mul_of_one_le_left zero_le (pos_iff_one_le.mp hp)
  exact lt_of_lt_of_le h1 (le_trans h2 h3)

end model

/-! ## 𝗭𝗙𝗖 层 -/

/-- 有理精度到达的 ℒₛₑₜ 公式。 -/
noncomputable def ΑRatS : SetTheorySemisentence 1 := arithTrln.translate arrRatF

/-- **有理精度的跑者到达句**：`∃z (Num_a(z) ∧ ΑRatS(z))`。 -/
noncomputable def arrRatS (a : ℕ) : Sentence ℒₛₑₜ := haltsS ΑRatS a

section modelZ

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]

lemma models_arrRat_iff_arr (a : ℕ) : M↓[ℒₛₑₜ] ⊧ arrRatS a ↔ M↓[ℒₛₑₜ] ⊧ arrS a := by
  rw [arrRatS, ΑRatS, arrS, ΑS, models_haltsS_iff, models_haltsS_iff, evalN_W_iff, evalN_W_iff]
  exact arrRat_iff_arr _

end modelZ

/-- **𝗭𝗙𝗖 逐个证明有理精度的到达句与 C-118 的到达句等价。** -/
theorem zfc_arrRat_iff_arr (a : ℕ) : 𝗭𝗙𝗖 ⊢ arrRatS a 🡘 arrS a := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  rw [Semantics.models_iff]
  exact models_arrRat_iff_arr a

/-- **𝗭𝗙𝗖 逐个证明有理精度的到达句与永不停机句等价。** -/
theorem zfc_arrRat_iff_never (a : ℕ) : 𝗭𝗙𝗖 ⊢ arrRatS a 🡘 neverS ΦS a := by
  have h1 := zfc_arrRat_iff_arr a
  have h2 := zfc_arr_iff_never a
  cl_prover [h1, h2]

/-- 有理精度的到达句在 `Universe` 里的意思恰是跑者到达。 -/
theorem universe_arrRatS_iff (d : Process) :
    Universe.{0}↓[ℒₛₑₜ] ⊧ arrRatS (Encodable.encode d) ↔ Arrives d :=
  (models_arrRat_iff_arr (M := Universe.{0}) _).trans (universe_arrS_iff d)

/-- **有一个跑者确实到达，𝗭𝗙𝗖 每一刻都确认它尚未停，却证明不了它的有理精度到达句。** -/
theorem zfc_runner_rat :
    ∃ d : Process, Arrives d ∧ (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ arrRatS (Encodable.encode d) := by
  obtain ⟨d, harr, hall, hna, -, -⟩ := zfc_runner
  refine ⟨d, harr, hall, fun hR => hna ?_⟩
  have h := zfc_arrRat_iff_arr (Encodable.encode d)
  cl_prover [h, hR]

/-- **𝗭𝗙𝗖 证明经典芝诺的有理精度极限句。** -/
theorem zfc_arriveRatC : 𝗭𝗙𝗖 ⊢ arithTrln.translate arriveRatC := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  apply DirectTranslation.Model.translate_iff.mpr
  exact (models_N_iff (M := M) arriveRatC).mpr models_arriveRatC

/-! ## 标准模型里的读法：通常的 ε–N 写法，ε 取遍正有理数 -/

/-- 正整数 p、q：q < p·2ⁿ 恰是 2⁻ⁿ < p/q。 -/
theorem lt_mul_two_pow_iff {p q : ℕ} (_hp : 0 < p) (hq : 0 < q) (n : ℕ) :
    q < p * 2 ^ n ↔ (1 / 2 : ℝ) ^ n < (p : ℝ) / q := by
  have hq' : (0 : ℝ) < q := by exact_mod_cast hq
  have h2 : (0 : ℝ) < 2 ^ n := by positivity
  rw [one_div_pow, div_lt_div_iff₀ h2 hq', one_mul]
  constructor
  · intro h; exact_mod_cast h
  · intro h; exact_mod_cast h

/-- 跑者的剩余距离总是 2 的负幂。 -/
theorem remaining_eq_pow (d : Process) : ∀ n, ∃ h : ℕ, remaining d n = (1 / 2 : ℝ) ^ h
  | 0 => ⟨0, by simp [remaining]⟩
  | n + 1 => by
    obtain ⟨h, hh⟩ := remaining_eq_pow d n
    by_cases hd : DoneBy d n
    · exact ⟨h, by simp [remaining, hd, hh]⟩
    · refine ⟨h + 1, ?_⟩
      simp only [remaining, hd, ↓reduceIte, hh, pow_succ]
      ring

/-- 正整数 p、q：剩余距离 < p/q，恰是有 K 使 q < p·2ᴷ 且剩余距离 ≤ 2⁻ᴷ。 -/
theorem remaining_lt_iff (d : Process) {p q : ℕ} (hp : 0 < p) (hq : 0 < q) (n : ℕ) :
    (∃ K : ℕ, q < p * 2 ^ K ∧ remaining d n ≤ (1 / 2 : ℝ) ^ K) ↔ remaining d n < (p : ℝ) / q := by
  constructor
  · rintro ⟨K, hK, hle⟩
    exact lt_of_le_of_lt hle ((lt_mul_two_pow_iff hp hq K).mp hK)
  · intro h
    obtain ⟨k, hk⟩ := remaining_eq_pow d n
    refine ⟨k, (lt_mul_two_pow_iff hp hq k).mpr (hk ▸ h), le_of_eq hk⟩

/-- **`arrRatF ⌜d⌝` 在 ℕ 里逐字是剩余距离趋于 0 的 ε–N 写法，ε 取遍正有理数。** -/
theorem arrRat_encode_rat (d : Process) :
    arrRatF.Evalb ![Encodable.encode d] ↔
      ∀ p q : ℕ, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → remaining d n < (p : ℝ) / q := by
  rw [eval_arrRatF]
  refine forall_congr' fun p => forall_congr' fun q => ?_
  constructor
  · intro h hp hq
    obtain ⟨N, hN⟩ := h hp hq
    refine ⟨N, fun n hn => ?_⟩
    obtain ⟨K, hK, hhalf⟩ := hN n ((nat_le_iff N n).mpr hn)
    rw [exp_nat_eq_two_pow] at hK
    exact (remaining_lt_iff d hp hq n).mp ⟨K, hK, (halvedF_encode d K n).mp hhalf⟩
  · intro h hp hq
    obtain ⟨N, hN⟩ := h hp hq
    refine ⟨N, fun n hn => ?_⟩
    obtain ⟨K, hK, hle⟩ := (remaining_lt_iff d hp hq n).mpr (hN n ((nat_le_iff N n).mp hn))
    exact ⟨K, by rw [exp_nat_eq_two_pow]; exact hK, (halvedF_encode d K n).mpr hle⟩

/-- **`arriveRatC` 在 ℕ 里逐字是“2⁻ⁿ → 0”的 ε–N 写法，ε 取遍正有理数。** -/
theorem arriveRatC_nat :
    ℕ↓[ℒₒᵣ] ⊧ arriveRatC ↔
      ∀ p q : ℕ, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → (1 / 2 : ℝ) ^ n < (p : ℝ) / q := by
  rw [models_arriveRatC_iff]
  refine forall_congr' fun p => forall_congr' fun q => ?_
  constructor
  · intro h hp hq
    obtain ⟨N, hN⟩ := h hp hq
    refine ⟨N, fun n hn => ?_⟩
    have hK := hN n ((nat_le_iff N n).mpr hn)
    rw [exp_nat_eq_two_pow] at hK
    exact (lt_mul_two_pow_iff hp hq n).mp hK
  · intro h hp hq
    obtain ⟨N, hN⟩ := h hp hq
    refine ⟨N, fun n hn => ?_⟩
    rw [exp_nat_eq_two_pow]
    exact (lt_mul_two_pow_iff hp hq n).mpr (hN n ((nat_le_iff N n).mp hn))

end GodelQ.ArrivalRat
