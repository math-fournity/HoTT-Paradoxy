import GodelQ.ZFC.Soundness
import GodelQ.GodelZenoRunner

/-!
# CG-006 · S5：哥德尔式 Q 在真实 𝗭𝗙𝗖 上的组装

* `zfc_incomplete`：𝗭𝗙𝗖 在 Foundation 的 `Entailment.Incomplete` 意义下不完全（由过程形式推出）。
* `zfcRunner`：对任意一族 ℒₛₑₜ 句 `arr`，若 𝗭𝗙𝗖 逐个证明 `arr a ↔ neverS ΦH a`，则得到跑者理论；
  于是哥德尔–芝诺跑者（C-91）、`AGeneral ↔ Q 完备`、`P ⟹ AGeneral`、`¬ AGeneral`（C-94）对 𝗭𝗙𝗖 成立。
  非空：取 `arr := neverS ΦH`。“跑者到达”的分析学句在 𝗭𝗙𝗖 内部与 `neverS` 等价，这一点本包没有在
  ℒₛₑₜ 中形式化（元层对应是 CG-005 已证的 `arrives_iff`），所以跑者部分以这一可证等价为显式参数。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCMain

open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound

/-- **𝗭𝗙𝗖 不完全**（Foundation 的 `Entailment.Incomplete`）：对角过程 d 的“永不停机”句独立于 𝗭𝗙𝗖。 -/
theorem zfc_incomplete : Entailment.Incomplete 𝗭𝗙𝗖 := by
  obtain ⟨d, -, -, hna, hnh, -⟩ := godel_I_process_form_zfc_full
  refine ⟨⟨neverS ΦH (Encodable.encode d), hna, ?_⟩⟩
  intro h
  apply hnh
  have h' : 𝗭𝗙𝗖 ⊢ ∼∼ haltsS ΦH (Encodable.encode d) := h
  cl_prover [h']

/-- 跑者理论：到达句族 `arr` 在 𝗭𝗙𝗖 中逐个与“永不停机”句可证等价。 -/
noncomputable def zfcRunner (arr : ℕ → Sentence ℒₛₑₜ)
    (harr : ∀ a, 𝗭𝗙𝗖 ⊢ arr a 🡘 neverS ΦH a) : RunnerTheory :=
  { zfcEffective with
    provesArrives := fun d ↦ 𝗭𝗙𝗖 ⊢ arr (Encodable.encode d)
    arrives_iff_never := fun d ↦ by
      have hd := harr (Encodable.encode d)
      constructor
      · intro h
        show 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d)
        cl_prover [h, hd]
      · intro h
        have h' : 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d) := h
        cl_prover [h', hd] }

/-- 非空：取到达句为“永不停机”句本身。 -/
noncomputable def zfcRunnerSelf : RunnerTheory :=
  zfcRunner (neverS ΦH) fun a ↦ by cl_prover

variable (arr : ℕ → Sentence ℒₛₑₜ) (harr : ∀ a, 𝗭𝗙𝗖 ⊢ arr a 🡘 neverS ΦH a)

include harr in
/-- **哥德尔–芝诺跑者，落在 𝗭𝗙𝗖 上**：有一个确实到达的芝诺式跑者，𝗭𝗙𝗖 每一刻都确认它尚未
停下、它的位置严格小于 1、位置有极限，却证明不了它到达。 -/
theorem goedel_zeno_zfc :
    ∃ d : Process, Arrives d ∧ 𝗭𝗙𝗖 ⊬ arr (Encodable.encode d) ∧
      (∀ n : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, n))) ∧
      (∀ n, position d n < 1) ∧ (∃ L, Filter.Tendsto (position d) Filter.atTop (nhds L)) :=
  (zfcRunner arr harr).goedel_zeno_in_theory

/-- **𝗭𝗙𝗖 + A = 𝗭𝗙𝗖 + P（落在 𝗭𝗙𝗖 上）**：A_general 恰是 Q 完备。 -/
theorem zfc_aGeneral_iff_complete :
    (zfcRunner arr harr).AGeneral ↔ zfcEffective.CompleteForNever :=
  (zfcRunner arr harr).aGeneral_iff_complete

/-- P 给出 A_general。 -/
theorem zfc_omegaClosed_imp_aGeneral (hP : zfcEffective.OmegaClosed) :
    (zfcRunner arr harr).AGeneral :=
  (zfcRunner arr harr).omegaClosed_imp_aGeneral hP

/-- 𝗭𝗙𝗖 没有 A_general：它确认不了每一个确实到达的芝诺式跑者。 -/
theorem zfc_not_aGeneral : ¬ (zfcRunner arr harr).AGeneral :=
  (zfcRunner arr harr).not_aGeneral

end GodelQ.ZFCMain

#print axioms GodelQ.ZFCMain.zfc_incomplete
#print axioms GodelQ.ZFCMain.zfcRunnerSelf
#print axioms GodelQ.ZFCMain.goedel_zeno_zfc
#print axioms GodelQ.ZFCMain.zfc_aGeneral_iff_complete
#print axioms GodelQ.ZFCMain.zfc_omegaClosed_imp_aGeneral
#print axioms GodelQ.ZFCMain.zfc_not_aGeneral
