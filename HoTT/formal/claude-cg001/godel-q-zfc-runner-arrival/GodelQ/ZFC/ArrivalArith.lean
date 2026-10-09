import GodelQ.ZFC.PAModel

/-!
# CG-007 · W5（一）：跑者的到达句——算术层

C-101 的跑者部分以“到达句与永不停机句在 𝗭𝗙𝗖 中逐个可证等价”为显式参数 `harr`。本文件写出一个具体的到达句，
先在算术语言 ℒₒᵣ 里：

* `θ e i`：程序 e 在 i 步燃料之内已停机。它是 Foundation 给可计算二元谓词的 Σ1 代码公式（`codeOfPartrec'`）。
* `stopF e k := ∃ i ≤ k, θ e i`：到第 k 步为止已停机。外面这一层有界存在量词，使它在**每一个** 𝗣𝗔⁻ 模型里都对 k
  单调，不论 θ 在非标准元素上怎样表现。
* `haltsF e := ∃ k, stopF e k`：e 停机。它是 Σ1 的。
* `halvedF e K n := K ≤ n ∧ ∀ i < K, ¬ stopF e i`：到第 n 步，跑者至少已减半 K 次，即剩余距离 ≤ 2⁻ᴷ（`halvedF_encode`；有了单调性，它只看第 K−1 步，见 `halved_succ_iff`）。
* `arrF e := ∀ K, ∃ N, ∀ n ≥ N, halvedF e K n`：对每个精度 2⁻ᴷ，从某一步起剩余距离一直不超过它——位置趋于 1 的
  ε–N 写法，ε 取 2⁻ᴷ。

**标准模型里的读法**：`haltsF ⌜d⌝` 恰是 d 停机；`halvedF ⌜d⌝ K n` 恰是 `remaining d n ≤ (1/2)^K`；`arrF ⌜d⌝` 恰是
`Arrives d`（C-91 的跑者到达）。

**每一个 𝗣𝗔⁻ 模型里**：`arrF e ↔ ¬ haltsF e`（`arr_iff_not_halts`）。只用到两条序的事实：`N ≤ N`，`i < i + 1`。

**实数一侧**：`remaining_le_iff`（剩余距离 ≤ 2⁻ᴷ 恰是前 K 步都还没停）与 `arrives_iff_eps`（跑者到达的 ε–N 写法，
经剩余距离为正与 2⁻ᴷ → 0）。
-/

namespace GodelQ.Arrival

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic
open scoped FFL.FirstOrder.Arithmetic

open Nat.Partrec Nat.Partrec.Code

/-! ## 停机的二元代码公式 -/

/-- “代码为 n 的程序在 i 步燃料之内已停机”（布尔值）。 -/
def stopB (n i : ℕ) : Bool := (evaln i (Denumerable.ofNat Process n) 0).isSome

theorem stopB_encode (e : Process) (i : ℕ) : stopB (Encodable.encode e) i = true ↔ DoneBy e i := by
  simp [stopB, DoneBy]

theorem stopB_computable : Computable₂ stopB := by
  have hev : Computable (fun p : ℕ × ℕ => evaln p.2 (Denumerable.ofNat Process p.1) 0) :=
    (primrec_evaln.to_comp).comp
      ((Computable.pair (Computable.pair Computable.snd
        ((Primrec.ofNat Process).to_comp.comp Computable.fst)) (Computable.const 0)))
  exact (Primrec.option_isSome.to_comp).comp hev

/-- 给 `codeOfPartrec'` 的函数：停机时取 1，否则取 0。 -/
def stopFun (v : List.Vector ℕ 2) : Part ℕ := Part.some (cond (stopB (v.get 0) (v.get 1)) 1 0)

theorem stopFun_partrec' : Nat.Partrec' stopFun := by
  apply Nat.Partrec'.of_part
  have : Computable (fun v : List.Vector ℕ 2 => cond (stopB (v.get 0) (v.get 1)) 1 0) :=
    Computable.cond (stopB_computable.comp (Primrec.vector_get.to_comp.comp Computable.id (Computable.const 0))
        (Primrec.vector_get.to_comp.comp Computable.id (Computable.const 1)))
      (Computable.const 1) (Computable.const 0)
  exact this.partrec

/-- `θ e i`：程序 e 在 i 步燃料之内已停机（Σ1 代码公式）。 -/
noncomputable def θ : ArithmeticSemisentence 2 := (codeOfPartrec' stopFun)/[‘1’, #0, #1]

theorem θ_sigma1 : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 θ := by simp [θ, codeOfPartrec']

theorem stopFun_mem (n i : ℕ) : (1 : ℕ) ∈ stopFun (List.Vector.ofFn ![n, i]) ↔ stopB n i = true := by
  have h0 : (List.Vector.ofFn ![n, i]).get 0 = n := by simp
  have h1 : (List.Vector.ofFn ![n, i]).get 1 = i := by simp
  simp only [stopFun, Part.mem_some_iff, h0, h1]
  cases stopB n i <;> simp

theorem θ_spec (n i : ℕ) : θ.Evalb ![n, i] ↔ stopB n i = true := by
  have h := (codeOfPartrec'_spec stopFun_partrec' (y := 1) (v := ![n, i])).trans (stopFun_mem n i)
  simpa [θ, Semiformula.eval_substs, Matrix.comp_vecCons'] using h

/-! ## 到达句的算术写法 -/

/-- `stopF e k`：到第 k 步为止已停机。 -/
noncomputable def stopF : ArithmeticSemisentence 2 := “e k. ∃ i <⁺ k, !θ e i”

/-- `haltsF e`：e 停机。 -/
noncomputable def haltsF : ArithmeticSemisentence 1 := “e. ∃ k, !stopF e k”

/-- `halvedF e K n`：到第 n 步，跑者至少已减半 K 次。 -/
noncomputable def halvedF : ArithmeticSemisentence 3 := “e K n. K ≤ n ∧ ∀ i < K, ¬!stopF e i”

/-- `arrF e`：跑者到达（剩余距离趋于 0 的 ε–N 写法，ε 取 2⁻ᴷ）。 -/
noncomputable def arrF : ArithmeticSemisentence 1 := “e. ∀ K, ∃ N, ∀ n, N ≤ n → !halvedF e K n”

section model

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻]

theorem eval_stopF (e k : V) : stopF.Evalb ![e, k] ↔ ∃ i ≤ k, θ.Evalb ![e, i] := by
  simp [stopF]

omit [V↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻] in
theorem eval_haltsF (e : V) : haltsF.Evalb ![e] ↔ ∃ k, stopF.Evalb ![e, k] := by
  simp [haltsF]

theorem eval_halvedF (e K n : V) :
    halvedF.Evalb ![e, K, n] ↔ K ≤ n ∧ ∀ i < K, ¬ stopF.Evalb ![e, i] := by
  simp [halvedF]

theorem eval_arrF (e : V) : arrF.Evalb ![e] ↔ ∀ K, ∃ N, ∀ n, N ≤ n → halvedF.Evalb ![e, K, n] := by
  simp [arrF]

/-- 在每一个 𝗣𝗔⁻ 模型里，“到第 k 步为止已停机”对 k 单调（由外层的有界存在量词，不论 θ 怎样）。 -/
theorem stopF_mono {e k m : V} (h : stopF.Evalb ![e, k]) (hkm : k ≤ m) : stopF.Evalb ![e, m] := by
  rw [eval_stopF] at h ⊢
  obtain ⟨i, hi, hθ⟩ := h
  exact ⟨i, le_trans hi hkm, hθ⟩

/-- 有了单调性，“到第 n 步已减半 K+1 次”恰是“n ≥ K+1，且到第 K 步还没停”。 -/
theorem halved_succ_iff (e K n : V) :
    halvedF.Evalb ![e, K + 1, n] ↔ K + 1 ≤ n ∧ ¬ stopF.Evalb ![e, K] := by
  rw [eval_halvedF]
  constructor
  · rintro ⟨h1, h2⟩
    exact ⟨h1, h2 K (lt_succ_iff_le.mpr le_rfl)⟩
  · rintro ⟨h1, h2⟩
    exact ⟨h1, fun i hi hs => h2 (stopF_mono hs (lt_succ_iff_le.mp hi))⟩

/-- **每一个 𝗣𝗔⁻ 模型里，跑者到达恰是永不停机。** 只用到 `N ≤ N` 与 `k < k + 1`。 -/
theorem arr_iff_not_halts (e : V) : arrF.Evalb ![e] ↔ ¬ haltsF.Evalb ![e] := by
  rw [eval_arrF, eval_haltsF]
  constructor
  · rintro h ⟨k, hk⟩
    obtain ⟨N, hN⟩ := h (k + 1)
    exact ((eval_halvedF e (k + 1) N).mp (hN N le_rfl)).2 k (lt_succ_iff_le.mpr le_rfl) hk
  · intro h K
    exact ⟨K, fun n hn => (eval_halvedF e K n).mpr ⟨hn, fun i _ hi => h ⟨i, hi⟩⟩⟩

end model

/-! ## 标准模型里的读法 -/

/-- Foundation 在 ℒₒᵣ 结构上的 `≤`（`x = y ∨ x < y`）在 ℕ 上就是通常的 `≤`。 -/
theorem nat_le_iff (x y : ℕ) : @LE.le ℕ FFL.FirstOrder.Arithmetic.instLE_foundation x y ↔ x ≤ y := by
  rw [le_def]; omega

theorem stopF_nat (n k : ℕ) : stopF.Evalb ![n, k] ↔ ∃ i ≤ k, stopB n i = true := by
  rw [eval_stopF]
  refine exists_congr fun i => and_congr ?_ (θ_spec n i)
  rw [le_def]; omega

theorem stopF_encode (d : Process) (k : ℕ) : stopF.Evalb ![Encodable.encode d, k] ↔ DoneBy d k := by
  rw [stopF_nat]
  constructor
  · rintro ⟨i, hi, h⟩
    exact doneBy_mono hi ((stopB_encode d i).mp h)
  · intro h
    exact ⟨k, le_rfl, (stopB_encode d k).mpr h⟩

theorem haltsF_encode (d : Process) : haltsF.Evalb ![Encodable.encode d] ↔ Done d := by
  rw [eval_haltsF, done_iff_exists_stage]
  exact exists_congr fun k => stopF_encode d k

/-! ## 跑者的剩余距离与减半次数（实数一侧） -/

open Filter Topology

/-- **剩余距离 ≤ 2⁻ᴷ，恰是到第 n 步已减半至少 K 次**：K ≤ n，且前 K 步都还没停。 -/
theorem remaining_le_iff (d : Process) :
    ∀ n K : ℕ, remaining d n ≤ (1 / 2 : ℝ) ^ K ↔ K ≤ n ∧ ∀ i < K, ¬ DoneBy d i
  | 0, K => by
    simp only [remaining]
    constructor
    · intro h
      have hK : K = 0 := by
        by_contra hK
        have : (1 / 2 : ℝ) ^ K < 1 := pow_lt_one₀ (by norm_num) (by norm_num) hK
        linarith
      subst hK
      exact ⟨le_rfl, fun i hi => absurd hi (Nat.not_lt_zero _)⟩
    · rintro ⟨hK, -⟩
      have : K = 0 := Nat.le_zero.mp hK
      subst this
      simp
  | n + 1, K => by
    have ih := remaining_le_iff d n
    by_cases hd : DoneBy d n
    · simp only [remaining, hd, ↓reduceIte]
      rw [ih K]
      constructor
      · rintro ⟨hK, h⟩
        exact ⟨Nat.le_succ_of_le hK, h⟩
      · rintro ⟨hK, h⟩
        refine ⟨?_, h⟩
        rcases Nat.lt_or_ge n K with hlt | hge
        · exact absurd hd (h n hlt)
        · exact hge
    · simp only [remaining, hd, ↓reduceIte]
      cases K with
      | zero =>
        have h1 := remaining_le_one d n
        have h0 := remaining_pos d n
        simp only [pow_zero]
        constructor
        · intro _
          exact ⟨Nat.zero_le _, fun i hi => absurd hi (Nat.not_lt_zero _)⟩
        · intro _
          linarith
      | succ K =>
        have hhalf : remaining d n / 2 ≤ (1 / 2 : ℝ) ^ (K + 1) ↔ remaining d n ≤ (1 / 2 : ℝ) ^ K := by
          rw [pow_succ]
          constructor <;> intro h <;> linarith
        rw [hhalf, ih K]
        constructor
        · rintro ⟨hK, h⟩
          refine ⟨Nat.succ_le_succ hK, fun i hi => ?_⟩
          rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
          · exact h i hi
          · exact fun hdK => hd (doneBy_mono hK hdK)
        · rintro ⟨hK, h⟩
          exact ⟨Nat.le_of_succ_le_succ hK, fun i hi => h i (Nat.lt_succ_of_lt hi)⟩

/-- 圆环读法（间隙收拢为 0）的 ε–N 写法，ε 取 2⁻ᴷ：只用剩余距离为正与 2⁻ᴷ → 0（实分析）。 -/
theorem restores_iff_eps (d : Process) :
    Restores d ↔ ∀ K : ℕ, ∃ N, ∀ n ≥ N, remaining d n ≤ (1 / 2 : ℝ) ^ K := by
  unfold Restores
  constructor
  · intro h K
    have hpos : (0 : ℝ) < (1 / 2) ^ K := by positivity
    obtain ⟨N, hN⟩ := eventually_atTop.mp ((tendsto_order.1 h).2 _ hpos)
    exact ⟨N, fun n hn => (hN n hn).le⟩
  · intro h
    refine tendsto_order.2 ⟨fun a ha => Eventually.of_forall fun n => lt_of_lt_of_le ha (remaining_pos d n).le,
      fun a ha => ?_⟩
    obtain ⟨K, hK⟩ := exists_pow_lt_of_lt_one ha (by norm_num : (1 / 2 : ℝ) < 1)
    obtain ⟨N, hN⟩ := h K
    exact eventually_atTop.mpr ⟨N, fun n hn => lt_of_le_of_lt (hN n hn) hK⟩

/-- **跑者到达的 ε–N 写法**：位置趋于 1，恰是对每个 K，从某一步起剩余距离一直 ≤ 2⁻ᴷ。 -/
theorem arrives_iff_eps (d : Process) :
    Arrives d ↔ ∀ K : ℕ, ∃ N, ∀ n ≥ N, remaining d n ≤ (1 / 2 : ℝ) ^ K :=
  (restores_iff_arrives d).symm.trans (restores_iff_eps d)

/-! ## 到达句在标准模型里的读法 -/

/-- `halvedF ⌜d⌝ K n` 在 ℕ 里恰是“剩余距离 ≤ 2⁻ᴷ”。 -/
theorem halvedF_encode (d : Process) (K n : ℕ) :
    halvedF.Evalb ![Encodable.encode d, K, n] ↔ remaining d n ≤ (1 / 2 : ℝ) ^ K := by
  rw [eval_halvedF, remaining_le_iff]
  exact and_congr (nat_le_iff K n) (forall_congr' fun i => imp_congr_right fun _ => not_congr (stopF_encode d i))

/-- `arrF ⌜d⌝` 在 ℕ 里逐字是剩余距离趋于 0 的 ε–N 写法。 -/
theorem arrF_encode_eps (d : Process) :
    arrF.Evalb ![Encodable.encode d] ↔ ∀ K : ℕ, ∃ N, ∀ n ≥ N, remaining d n ≤ (1 / 2 : ℝ) ^ K := by
  rw [eval_arrF]
  refine forall_congr' fun K => exists_congr fun N => forall_congr' fun n => ?_
  rw [halvedF_encode]
  exact imp_congr_left (nat_le_iff N n)

/-- **`arrF ⌜d⌝` 在 ℕ 里恰是跑者到达（C-91）。** -/
theorem arrF_encode (d : Process) : arrF.Evalb ![Encodable.encode d] ↔ Arrives d :=
  (arrF_encode_eps d).trans (arrives_iff_eps d).symm

end GodelQ.Arrival

#print axioms GodelQ.Arrival.stopB_computable
#print axioms GodelQ.Arrival.θ_spec
#print axioms GodelQ.Arrival.θ_sigma1
#print axioms GodelQ.Arrival.stopF_mono
#print axioms GodelQ.Arrival.halved_succ_iff
#print axioms GodelQ.Arrival.arr_iff_not_halts
#print axioms GodelQ.Arrival.stopF_encode
#print axioms GodelQ.Arrival.haltsF_encode
#print axioms GodelQ.Arrival.remaining_le_iff
#print axioms GodelQ.Arrival.restores_iff_eps
#print axioms GodelQ.Arrival.arrives_iff_eps
#print axioms GodelQ.Arrival.halvedF_encode
#print axioms GodelQ.Arrival.arrF_encode_eps
#print axioms GodelQ.Arrival.arrF_encode
