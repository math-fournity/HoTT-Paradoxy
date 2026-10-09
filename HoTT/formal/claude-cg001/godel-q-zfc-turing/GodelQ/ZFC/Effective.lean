import GodelQ.ZFC.NeverRE
import GodelQ.ZFC.NumeralSemantics
import GodelQ.ZFC.R0Model
import GodelQ.FoundationArith
import Foundation.FirstOrder.SetTheory.Universe

/-!
# CG-006 · S5（一）：真实的 𝗭𝗙𝗖 是满足四条元性质的有效理论

三类陈述（`a := encode e`，`Num_a` 是 Rayo 数字公式）：
* `provesHalts e  := 𝗭𝗙𝗖 ⊢ ∃z (Num_a(z) ∧ Φ⁺(z))`，`Φ⁺ := arithTrln.translate φH`；
* `provesNever e  := 𝗭𝗙𝗖 ⊢ ¬∃z (Num_a(z) ∧ Φ⁺(z))`；
* `provesNotYet e k := 𝗭𝗙𝗖 ⊢ ∃z (Num_b(z) ∧ Ψ⁺(z))`，`b := encode (e,k)`，`Ψ⁺ := arithTrln.translate ψN`。

四条元性质全部是定理：
* 可枚举：S2d `never_re`（经 `𝗭𝗙𝗖.Δ₁` 与内部可证性）；
* Σ1、Δ0 完全：𝗥₀ 的 Σ1 完全性（`sigma_one_completeness`，不需要可靠性）→ S3 的解释
  `arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀` → 在每个 𝗭𝗙𝗖 模型里，翻译句与数字句同真（`eval_numeralF_iff`）；
* 一致：Foundation 的 `zfc_consistent`（Lean 元层的 `Universe` 模型）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCEff

open GodelQ.ZFCNum GodelQ.ZFCArith

/-- 𝗥₀ 证明每一个真实的 r.e. 事实（只用 Σ1 完全性）。 -/
lemma R0_proves {p : ℕ → Prop} (hp : REPred p) {x : ℕ} (h : p x) :
    𝗥₀ ⊢ (codeOfREPred p)/[↑x] := by
  apply sigma_one_completeness (T := 𝗥₀) (by simp [codeOfREPred, codeOfPartrec'])
  simpa [models_iff, Semiformula.eval_substs, Matrix.constant_eq_singleton]
    using (codeOfREPred_spec hp (x := x)).mpr h

section bridge

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]

/-- 数字代入：在 ω 上的算术结构中，`φ/[↑a]` 为真，恰好当 `φ` 在 `ofNat a` 处为真。 -/
lemma models_subst_numeral_iff (φ : ArithmeticSemisentence 1) (a : ℕ) :
    (N M)↓[ℒₒᵣ] ⊧ φ/[↑a] ↔ (N M) ⊧/![toN (ofNat a) (ofNat_mem_ω' a)] φ := by
  simp [models_iff, Semiformula.eval_substs, Semiterm.val_operator, ZFCArith.val_numeral]

/-- 数字句：`M ⊧ ∃z (Num_a(z) ∧ Φ⁺(z))` 恰好当 `φ` 在 ω 的结构中于 `ofNat a` 处为真。 -/
lemma models_haltsS_iff (φ : ArithmeticSemisentence 1) (a : ℕ) :
    M↓[ℒₛₑₜ] ⊧ haltsS (arithTrln.translate φ) a ↔
      (N M) ⊧/![toN (ofNat a) (ofNat_mem_ω' a)] φ := by
  have h1 : M↓[ℒₛₑₜ] ⊧ haltsS (arithTrln.translate φ) a ↔
      M ⊧/![(ofNat a : M)] (arithTrln.translate φ) := by
    simp [haltsS, models_iff, eval_numeralF_iff]
  rw [h1]
  exact DirectTranslation.Model.evalb_singleton_translate_iff (x := toN (ofNat a) (ofNat_mem_ω' a))

end bridge

/-- **Σ1 完全（落到 𝗭𝗙𝗖）**：真实的 r.e. 事实，其数字句被 𝗭𝗙𝗖 证明。 -/
theorem zfc_proves_haltsS {p : ℕ → Prop} (hp : REPred p) {a : ℕ} (h : p a) :
    𝗭𝗙𝗖 ⊢ haltsS (arithTrln.translate (codeOfREPred p)) a := by
  have hZ : 𝗭𝗙𝗖 ⊢ arithTrln.translate ((codeOfREPred p)/[↑a]) :=
    arithInterp.of_provability (R0_proves hp h)
  apply SetTheory.complete.{0}
  intro M _ _ _
  have hM : M↓[ℒₛₑₜ] ⊧ arithTrln.translate ((codeOfREPred p)/[↑a]) :=
    models_of_provable inferInstance hZ
  have hN : (N M)↓[ℒₒᵣ] ⊧ (codeOfREPred p)/[↑a] := DirectTranslation.Model.translate_iff.mp hM
  exact (models_haltsS_iff _ a).mpr ((models_subst_numeral_iff _ a).mp hN)

/-- “e 停机”的 ℒₛₑₜ 公式。 -/
noncomputable def ΦH : SetTheorySemisentence 1 := arithTrln.translate GodelQ.φH
/-- “e 在 k 步内尚未停机”的 ℒₛₑₜ 公式。 -/
noncomputable def ΨN : SetTheorySemisentence 1 := arithTrln.translate GodelQ.ψN

/-- **真实 𝗭𝗙𝗖 的过程观察接口**：四条元性质全部由定理给出。 -/
noncomputable def zfcEffective : EffectiveTheory where
  provesHalts e := 𝗭𝗙𝗖 ⊢ haltsS ΦH (Encodable.encode e)
  provesNever e := 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode e)
  provesNotYet e k := 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (e, k))
  re_never := (never_re ΦH).comp Computable.encode
  sigma1_complete e h := zfc_proves_haltsS haltsNat_re ((haltsNat_encode e).mpr h)
  delta0_complete e k h := zfc_proves_haltsS notYetNat_re ((notYetNat_encode e k).mpr h)
  consistent e h1 h2 := by
    have h2' : 𝗭𝗙𝗖 ⊢ ∼ haltsS ΦH (Encodable.encode e) := h2
    apply Entailment.Consistent.not_bot (𝓢 := 𝗭𝗙𝗖)
    cl_prover [h1, h2']

/-- **哥德尔 I 的过程形式，落在真实的 𝗭𝗙𝗖 上**：存在过程 `d`，它确实永不停机；𝗭𝗙𝗖 对每个 k
证明“d 在 k 步内尚未停机”，却证明不了“d 永不停机”；并且 d 停机恰好当 𝗭𝗙𝗖 证明它永不停机。 -/
theorem godel_I_process_form_zfc :
    ∃ d : Process, ¬ Done d ∧
      (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode d) ∧
      (Done d ↔ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d)) := by
  obtain ⟨d, hnd, hna, hall, hiff⟩ := zfcEffective.godel_I_process_form
  exact ⟨d, hnd, hall, hna, hiff⟩

/-- **魔鬼交易，落在真实的 𝗭𝗙𝗖 上**：𝗭𝗙𝗖 不封闭于 ω 完成规则 P。 -/
theorem devils_bargain_zfc : ¬ zfcEffective.OmegaClosed := zfcEffective.devils_bargain

end GodelQ.ZFCEff

#print axioms GodelQ.ZFCEff.zfcEffective
#print axioms GodelQ.ZFCEff.godel_I_process_form_zfc
#print axioms GodelQ.ZFCEff.devils_bargain_zfc
