import GodelQ.ZFC.ArrivalZFC

/-!
# CG-007 · W5：命题对照（CG001-C-117、C-118）

每条命题的类型逐字写在这里，证明只引用前面文件中的定理。
-/

namespace GodelQ.ArrivalQual

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCEff GodelQ.Arrival GodelQ.ArrivalZFC GodelQ.C6

/-- **CG001-C-117（跑者到达句的算术层）**：
(1) θ 是 Σ1 的二元代码公式，在 ℕ 里恰说“程序 e 在 i 步燃料之内已停机”；
(2) 在每一个 𝗣𝗔⁻ 模型里：`stopF` 对步数单调；“已减半 K+1 次”恰是“n ≥ K+1 且到第 K 步还没停”；
    到达句 `arrF e` 恰是 `¬ haltsF e`；
(3) 剩余距离 ≤ 2⁻ᴷ，恰是 K ≤ n 且前 K 步都还没停；跑者到达恰是 ε–N 写法（ε 取 2⁻ᴷ）；
(4) 标准模型里：`haltsF ⌜d⌝` 恰是 d 停机；`halvedF ⌜d⌝ K n` 恰是剩余距离 ≤ 2⁻ᴷ；`arrF ⌜d⌝` 逐字是 ε–N 写法，
    恰是跑者到达。 -/
theorem qual_C117 :
    (ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 θ ∧ (∀ n i : ℕ, θ.Evalb ![n, i] ↔ stopB n i = true) ∧
      ∀ (e : Process) (i : ℕ), stopB (Encodable.encode e) i = true ↔ DoneBy e i) ∧
    (∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻],
      (∀ e k m : V, stopF.Evalb ![e, k] → k ≤ m → stopF.Evalb ![e, m]) ∧
      (∀ e K n : V, halvedF.Evalb ![e, K + 1, n] ↔ K + 1 ≤ n ∧ ¬ stopF.Evalb ![e, K]) ∧
      (∀ e : V, arrF.Evalb ![e] ↔ ¬ haltsF.Evalb ![e])) ∧
    ((∀ (d : Process) (n K : ℕ), remaining d n ≤ (1 / 2 : ℝ) ^ K ↔ K ≤ n ∧ ∀ i < K, ¬ DoneBy d i) ∧
      ∀ d : Process, Arrives d ↔ ∀ K : ℕ, ∃ N, ∀ n ≥ N, remaining d n ≤ (1 / 2 : ℝ) ^ K) ∧
    (∀ d : Process, (haltsF.Evalb ![Encodable.encode d] ↔ Done d) ∧
      (∀ K n : ℕ, halvedF.Evalb ![Encodable.encode d, K, n] ↔ remaining d n ≤ (1 / 2 : ℝ) ^ K) ∧
      (arrF.Evalb ![Encodable.encode d] ↔ ∀ K : ℕ, ∃ N, ∀ n ≥ N, remaining d n ≤ (1 / 2 : ℝ) ^ K) ∧
      (arrF.Evalb ![Encodable.encode d] ↔ Arrives d)) :=
  ⟨⟨θ_sigma1, θ_spec, stopB_encode⟩,
   fun _ _ _ => ⟨fun _ _ _ h hkm => stopF_mono h hkm, halved_succ_iff, arr_iff_not_halts⟩,
   ⟨remaining_le_iff, arrives_iff_eps⟩,
   fun d => ⟨haltsF_encode d, halvedF_encode d, arrF_encode_eps d, arrF_encode d⟩⟩

/-- **CG001-C-118（跑者到达句落到 𝗭𝗙𝗖）**：
(1) 对每个 a，到达句 `arrS a` 不是永不停机句 `neverS ΦS a` 本身，而 𝗭𝗙𝗖 证明二者等价；
(2) 到达句在 `Universe` 里的意思恰是跑者到达；𝗭𝗙𝗖 证明的到达句都不错；
(3) 以 ΦS 为停机公式的接口：𝗭𝗙𝗖 证明“e 停机”恰好当 e 停机；
(4) C-101 的跑者部分不再带参数：有一个跑者确实到达，𝗭𝗙𝗖 每一刻都确认它尚未停，位置每一刻 < 1、极限存在，
    𝗭𝗙𝗖 却证明不了它的到达句；
(5) A_general ⟺ Q 完备；𝗭𝗙𝗖 没有 A_general，也不封闭于 ω 完成规则；对角过程的停机句、永不停机句与到达句都不可证；
(6) C-115 改用到达句：有一个标准解确实出错的跑者，𝗭𝗙𝗖 既证不了它停机，也证不了它的到达句；未被批判的错误无穷且列不全；
    这样的审查不完备。 -/
theorem qual_C118 :
    (∀ a : ℕ, arrS a ≠ neverS ΦS a ∧ 𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a) ∧
    ((∀ d : Process, Universe.{0}↓[ℒₛₑₜ] ⊧ arrS (Encodable.encode d) ↔ Arrives d) ∧
      ∀ d : Process, 𝗭𝗙𝗖 ⊢ arrS (Encodable.encode d) → Arrives d) ∧
    (∀ e : Process, 𝗭𝗙𝗖 ⊢ haltsS ΦS (Encodable.encode e) ↔ Done e) ∧
    (∃ d : Process, Arrives d ∧ (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d) ∧ (∀ n, position d n < 1) ∧
      (∃ L, Filter.Tendsto (position d) Filter.atTop (nhds L))) ∧
    ((zfcRunner.AGeneral ↔ zfcEffective'.CompleteForNever) ∧ ¬ zfcRunner.AGeneral ∧
      ¬ zfcEffective'.OmegaClosed ∧
      ∃ d : Process, ¬ Done d ∧ 𝗭𝗙𝗖 ⊬ neverS ΦS (Encodable.encode d) ∧
        𝗭𝗙𝗖 ⊬ haltsS ΦS (Encodable.encode d) ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)) ∧
    ((∃ d : Process, ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ haltsS ΦS (Encodable.encode d) ∧
        𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)) ∧
      {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)}.Infinite ∧
      ¬ REPred (· ∈ {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)}) ∧
      ¬ zfcReviewArr.Complete) :=
  ⟨fun a => ⟨arrS_ne_neverS a, zfc_arr_iff_never a⟩,
   ⟨universe_arrS_iff, zfc_arrS_sound⟩,
   zfc_provesHalts'_iff,
   zfc_runner,
   ⟨zfc_aGeneral.1, zfc_aGeneral.2.1, zfc_aGeneral.2.2, zfc_godel_I'⟩,
   ⟨zfc_review_gap_arr, zfc_uncriticized_arr.1, zfc_uncriticized_arr.2, zfc_review_arr_incomplete⟩⟩

end GodelQ.ArrivalQual

#print axioms GodelQ.ArrivalQual.qual_C117
#print axioms GodelQ.ArrivalQual.qual_C118
