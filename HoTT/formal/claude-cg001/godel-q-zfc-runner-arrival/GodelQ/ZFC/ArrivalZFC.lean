import GodelQ.ZFC.ArrivalArith
import GodelQ.C6Review

/-!
# CG-007 · W5（二）：跑者的到达句落到 𝗭𝗙𝗖

把 W5（一）的算术句经同一个翻译 `arithTrln` 放进 ℒₛₑₜ：

* `ΦS := arithTrln.translate haltsF`：“e 停机”的新 ℒₛₑₜ 公式；
* `arrS a := ∃z (Num_a(z) ∧ (arrF)⁺(z))`：跑者到达句。它不是 `neverS` 本身（`arrS_ne_neverS`），
  在 `Universe` 里的意思恰是 `Arrives d`（`universe_arrS_iff`）。

主定理：
* `zfc_arr_iff_never`：对每个 a，`𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a`。证明是语义的：在 𝗭𝗙𝗖 的每个模型里，ω 是 𝗣𝗔⁻ 的模型
  （C-109），到达句与永不停机句在那里同真（W5（一）的 `arr_iff_not_halts`）；再用完备性。
* `zfcEffective'`：以 ΦS 为停机公式的 𝗭𝗙𝗖 过程观察接口，四条元性质都是定理（同 C-99 的证法）；`zfcRunner`：再加上
  到达句，就是一个 `RunnerTheory`。
* `zfc_runner`：C-101 的跑者部分不再带参数 `harr`。有一个跑者确实到达；𝗭𝗙𝗖 在每一刻都确认它尚未停、位置 < 1、
  有极限，却证明不了它的到达句。
* `zfcReviewArr`：C-115 的 𝗭𝗙𝗖 审查改用到达句——“证明不充分”即证明极限判词“到了”。仍有一个标准解确实出错、
  𝗭𝗙𝗖 却既证不了充分也证不了不充分的跑者；未被批判的错误无穷且列不全。

为什么要新的停机公式：旧的 `ΦH`（`codeOfREPred`）在非标准模型里的行为无从推理，对永不停机的 d，
“`ΦH` 与 ∃k stopF 等价”在 𝗭𝗙𝗖 中证明不了（负控制 `WrongArrivalOldPhi`）。`ΦS` 由 `stopF` 写成，到达句与它的等价
在每个模型里都成立。
-/

namespace GodelQ.ArrivalZFC

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound GodelQ.Arrival

/-- “e 停机”的新 ℒₛₑₜ 公式。 -/
noncomputable def ΦS : SetTheorySemisentence 1 := arithTrln.translate haltsF

/-- 跑者到达的 ℒₛₑₜ 公式。 -/
noncomputable def ΑS : SetTheorySemisentence 1 := arithTrln.translate arrF

/-- **跑者到达句**：`∃z (Num_a(z) ∧ ΑS(z))`。 -/
noncomputable def arrS (a : ℕ) : Sentence ℒₛₑₜ := haltsS ΑS a

/-- 到达句不是永不停机句本身：一个以 ∃ 开头，一个以 ∀ 开头。 -/
theorem arrS_ne_neverS (a : ℕ) : arrS a ≠ neverS ΦS a := by
  simp [arrS, haltsS, neverS]

section model

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]

/-- ω（翻译解释）上的求值与 `W M`（标准解释）上的求值相同。 -/
lemma evalN_W_iff (φ : ArithmeticSemisentence 1) (x : N M) :
    (N M) ⊧/![x] φ ↔ φ.Evalb (M := W M) ![theta x] := by
  have h := eval_W_iff (M := M) (b := ![theta x]) (ε := (Empty.elim : Empty → W M)) (φ := φ)
  have hb : theta.symm ∘ ![theta x] = ![x] := by
    funext i; match i with | 0 => exact theta.symm_apply_apply x
  have hε : theta.symm ∘ (Empty.elim : Empty → W M) = Empty.elim := funext fun e => e.elim
  rw [hb, hε] at h
  exact h.symm

/-- 在 𝗭𝗙𝗖 的每个模型里，到达句与“停机”句恰好一真一假。 -/
lemma models_arr_iff_not_halts (a : ℕ) :
    M↓[ℒₛₑₜ] ⊧ arrS a ↔ ¬ M↓[ℒₛₑₜ] ⊧ haltsS ΦS a := by
  rw [arrS, ΑS, ΦS, models_haltsS_iff, models_haltsS_iff, evalN_W_iff, evalN_W_iff]
  exact arr_iff_not_halts _

end model

/-- **𝗭𝗙𝗖 逐个证明到达句与永不停机句等价。** -/
theorem zfc_arr_iff_never (a : ℕ) : 𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  rw [Semantics.models_iff, neverS, Semantics.Not.models_not]
  exact models_arr_iff_not_halts a

/-! ## 以 ΦS 为停机公式的 𝗭𝗙𝗖 观察接口 -/

/-- Σ1 完全（一般的 Σ1 公式）：标准模型里为真的 Σ1 事实，其数字句被 𝗭𝗙𝗖 证明。 -/
theorem zfc_proves_haltsS_sigma1 {φ : ArithmeticSemisentence 1} (hφ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ)
    {a : ℕ} (h : φ.Evalb ![a]) : 𝗭𝗙𝗖 ⊢ haltsS (arithTrln.translate φ) a := by
  have hR : 𝗥₀ ⊢ φ/[↑a] := by
    apply sigma_one_completeness (T := 𝗥₀) (by simpa using hφ)
    simpa [models_iff, Semiformula.eval_substs, Matrix.constant_eq_singleton] using h
  have hZ : 𝗭𝗙𝗖 ⊢ arithTrln.translate (φ/[↑a]) := arithInterp.of_provability hR
  apply SetTheory.complete.{0}
  intro M _ _ _
  have hM : M↓[ℒₛₑₜ] ⊧ arithTrln.translate (φ/[↑a]) := models_of_provable inferInstance hZ
  have hN : (N M)↓[ℒₒᵣ] ⊧ φ/[↑a] := DirectTranslation.Model.translate_iff.mp hM
  exact (models_haltsS_iff _ a).mpr ((models_subst_numeral_iff _ a).mp hN)

/-- 数字句可靠（任一算术公式，经 `Universe`）。 -/
theorem zfc_haltsS_sound_any {φ : ArithmeticSemisentence 1} {a : ℕ}
    (h : 𝗭𝗙𝗖 ⊢ haltsS (arithTrln.translate φ) a) : φ.Evalb ![a] := by
  have hU : Universe.{0}↓[ℒₛₑₜ] ⊧ haltsS (arithTrln.translate φ) a :=
    models_of_provable inferInstance h
  have hN := (models_haltsS_iff (M := Universe.{0}) φ a).mp hU
  exact (evalN_iff φ a).mp hN

theorem haltsF_sigma1 : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 haltsF := by
  simp [haltsF, stopF, θ_sigma1]

/-- 以 ΦS 为停机公式的 𝗭𝗙𝗖 过程观察接口：四条元性质全由定理给出。 -/
noncomputable def zfcEffective' : EffectiveTheory where
  provesHalts e := 𝗭𝗙𝗖 ⊢ haltsS ΦS (Encodable.encode e)
  provesNever e := 𝗭𝗙𝗖 ⊢ neverS ΦS (Encodable.encode e)
  provesNotYet e k := 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (e, k))
  re_never := (never_re ΦS).comp Computable.encode
  sigma1_complete e h := zfc_proves_haltsS_sigma1 haltsF_sigma1 ((haltsF_encode e).mpr h)
  delta0_complete e k h := zfc_proves_haltsS notYetNat_re ((notYetNat_encode e k).mpr h)
  consistent e h1 h2 := by
    have h2' : 𝗭𝗙𝗖 ⊢ ∼ haltsS ΦS (Encodable.encode e) := h2
    apply Entailment.Consistent.not_bot (𝓢 := 𝗭𝗙𝗖)
    cl_prover [h1, h2']

/-- 𝗭𝗙𝗖 证明 `haltsS ΦS ⌜e⌝` 恰好当 e 确实停机。 -/
theorem zfc_provesHalts'_iff (e : Process) : zfcEffective'.provesHalts e ↔ Done e :=
  ⟨fun h => (haltsF_encode e).mp (zfc_haltsS_sound_any h), zfcEffective'.sigma1_complete e⟩

/-- 带到达句的 𝗭𝗙𝗖：一个 `RunnerTheory`，“到达 ⟺ 永不停”由 `zfc_arr_iff_never` 支付。 -/
noncomputable def zfcRunner : RunnerTheory where
  toEffectiveTheory := zfcEffective'
  provesArrives d := 𝗭𝗙𝗖 ⊢ arrS (Encodable.encode d)
  arrives_iff_never d := by
    have h := zfc_arr_iff_never (Encodable.encode d)
    constructor
    · intro ha
      show 𝗭𝗙𝗖 ⊢ neverS ΦS (Encodable.encode d)
      cl_prover [h, ha]
    · intro hn
      have hn' : 𝗭𝗙𝗖 ⊢ neverS ΦS (Encodable.encode d) := hn
      cl_prover [h, hn']

/-- 到达句在 `Universe` 里的意思恰是跑者到达。 -/
theorem universe_arrS_iff (d : Process) :
    Universe.{0}↓[ℒₛₑₜ] ⊧ arrS (Encodable.encode d) ↔ Arrives d := by
  rw [arrS, ΑS, models_haltsS_iff (M := Universe.{0})]
  have h := evalN_iff arrF (Encodable.encode d)
  exact h.trans (arrF_encode d)

/-! ## C-101 的跑者部分，不再带参数 -/

/-- **哥德尔–芝诺跑者，落在 𝗭𝗙𝗖 的到达句上**：有一个跑者确实到达；𝗭𝗙𝗖 在每一刻都确认它尚未停；位置每一刻都 < 1，
极限存在；𝗭𝗙𝗖 却证明不了它的到达句。 -/
theorem zfc_runner :
    ∃ d : Process, Arrives d ∧ (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d) ∧ (∀ n, position d n < 1) ∧
      (∃ L, Filter.Tendsto (position d) Filter.atTop (nhds L)) := by
  obtain ⟨d, harr, hna, hall, hlt, hlim⟩ := zfcRunner.goedel_zeno_in_theory
  exact ⟨d, harr, hall, hna, hlt, hlim⟩

/-- 𝗭𝗙𝗖 证明的到达句都不错。 -/
theorem zfc_arrS_sound (d : Process) (h : 𝗭𝗙𝗖 ⊢ arrS (Encodable.encode d)) : Arrives d :=
  zfcRunner.arrivalObserver.sound d h

/-- A_general（𝗭𝗙𝗖 确认每一个到达的跑者）恰是 Q 完备；𝗭𝗙𝗖 没有它；𝗭𝗙𝗖 不封闭于 ω 完成规则。 -/
theorem zfc_aGeneral :
    (zfcRunner.AGeneral ↔ zfcEffective'.CompleteForNever) ∧ ¬ zfcRunner.AGeneral ∧
      ¬ zfcEffective'.OmegaClosed :=
  ⟨zfcRunner.aGeneral_iff_complete, zfcRunner.not_aGeneral, zfcEffective'.devils_bargain⟩

/-- 哥德尔 I 的过程形式（含独立性），对新的接口。 -/
theorem zfc_godel_I' :
    ∃ d : Process, ¬ Done d ∧ 𝗭𝗙𝗖 ⊬ neverS ΦS (Encodable.encode d) ∧
      𝗭𝗙𝗖 ⊬ haltsS ΦS (Encodable.encode d) ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d) := by
  obtain ⟨d, hnd, hna, -, -⟩ := zfcEffective'.godel_I_process_form
  refine ⟨d, hnd, hna, fun hH => hnd ((zfc_provesHalts'_iff d).mp hH), fun hA => ?_⟩
  exact hna ((zfcRunner.arrives_iff_never d).mp hA)

/-! ## C-115 的 𝗭𝗙𝗖 审查改用到达句 -/

open GodelQ.C6

/-- 𝗭𝗙𝗖 的审查：证明 d 停机即证明标准解对 d 充分；证明 d 的到达句（极限判词“到了”）即证明不充分
——跑者在每个有限阶段都还没到 1。 -/
noncomputable def zfcReviewArr : Review where
  provesAdequate d := 𝗭𝗙𝗖 ⊢ haltsS ΦS (Encodable.encode d)
  provesInadequate d := 𝗭𝗙𝗖 ⊢ arrS (Encodable.encode d)
  sound_adequate d h := (adequate_iff d).mpr ((zfc_provesHalts'_iff d).mp h)
  sound_inadequate d h := (inadequate_iff d).mpr ((arrives_iff d).mp (zfc_arrS_sound d h))
  re_inadequate := zfcRunner.arrivalObserver.re

/-- 𝗭𝗙𝗖 审查不了标准解：有一个跑者，标准解对它确实不充分，𝗭𝗙𝗖 却既证明不了它停机，也证明不了它的到达句。 -/
theorem zfc_review_gap_arr :
    ∃ d : Process, ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ haltsS ΦS (Encodable.encode d) ∧
      𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d) := by
  obtain ⟨e, hnd, hna⟩ := zfcEffective'.misses_infinite.nonempty
  refine ⟨e, (inadequate_iff e).mpr hnd, fun hH => hnd ((zfc_provesHalts'_iff e).mp hH), fun hA => ?_⟩
  exact hna ((zfcRunner.arrives_iff_never e).mp hA)

/-- 未被批判的错误：标准解出错、𝗭𝗙𝗖 却证明不了到达句的跑者，无穷且列不全。 -/
theorem zfc_uncriticized_arr :
    {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)}.Infinite ∧
    ¬ REPred (· ∈ {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)}) := by
  have heq : {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ arrS (Encodable.encode d)} = zfcEffective'.Misses := by
    ext d
    simp only [Set.mem_ofPred_eq, inadequate_iff]
    exact and_congr_right fun _ => not_congr (zfcRunner.arrives_iff_never d)
  rw [heq]
  exact ⟨zfcEffective'.misses_infinite, zfcEffective'.misses_not_re⟩

theorem zfc_review_arr_incomplete : ¬ zfcReviewArr.Complete := no_complete_review zfcReviewArr

end GodelQ.ArrivalZFC

#print axioms GodelQ.ArrivalZFC.arrS_ne_neverS
#print axioms GodelQ.ArrivalZFC.zfc_arr_iff_never
#print axioms GodelQ.ArrivalZFC.zfc_proves_haltsS_sigma1
#print axioms GodelQ.ArrivalZFC.zfc_haltsS_sound_any
#print axioms GodelQ.ArrivalZFC.zfcEffective'
#print axioms GodelQ.ArrivalZFC.zfc_provesHalts'_iff
#print axioms GodelQ.ArrivalZFC.zfcRunner
#print axioms GodelQ.ArrivalZFC.universe_arrS_iff
#print axioms GodelQ.ArrivalZFC.zfc_runner
#print axioms GodelQ.ArrivalZFC.zfc_arrS_sound
#print axioms GodelQ.ArrivalZFC.zfc_aGeneral
#print axioms GodelQ.ArrivalZFC.zfc_godel_I'
#print axioms GodelQ.ArrivalZFC.zfcReviewArr
#print axioms GodelQ.ArrivalZFC.zfc_review_gap_arr
#print axioms GodelQ.ArrivalZFC.zfc_uncriticized_arr
#print axioms GodelQ.ArrivalZFC.zfc_review_arr_incomplete
