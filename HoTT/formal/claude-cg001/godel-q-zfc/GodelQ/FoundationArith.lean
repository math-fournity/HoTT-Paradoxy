import GodelQ.GodelZenoRunner
import Foundation.FirstOrder.Incompleteness.Halting

/-!
# CG-006 · S1：哥德尔式 Q 落到真实的形式算术理论

对 Foundation 中任意 Δ1、扩张 𝗥₀、Σ1 可靠的算术理论 `T`（例如 PA），`EffectiveTheory` 的三类
陈述取作 `T` 中真实的可证性：

* `provesHalts e  := T ⊢ φH/[⌜e⌝]`，其中 `φH := codeOfREPred haltsNat` 是“e 停机”的 Σ1 公式；
* `provesNever e  := T ⊢ ∼φH/[⌜e⌝]`；
* `provesNotYet e k := T ⊢ ψN/[⌜(e,k)⌝]`，`ψN` 是“e 在 k 步内尚未停机”的 Σ1 公式。

四条前提由 Foundation 的定理推出（不是假设）：可证性可枚举（`rePred_iff_sigma1` 与内部可证性的
可靠、完全），Σ1/Δ0 完全（`rePred_weak_representation`），一致（Σ1 可靠蕴涵一致）。于是 CG-005 的
哥德尔 I 过程形式、魔鬼交易、跑者对 `T` 成立；另证对角过程在 `T` 中独立。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ

/-- “停机”作为 ℕ 上的谓词（经解码）。 -/
def haltsNat (n : ℕ) : Prop := (Encodable.decode (α := Process) n).elim False Done

theorem haltsNat_re : REPred haltsNat :=
  REPred.iff_decoded_pred.mp (ComputablePred.halting_problem_re 0)

theorem haltsNat_encode (e : Process) : haltsNat (Encodable.encode e) ↔ Done e := by
  simp [haltsNat]

/-- “在 k 步内尚未停机”作为 ℕ 上的谓词（对 `(e, k)` 的编码）。 -/
def notYetNat (n : ℕ) : Prop :=
  (Encodable.decode (α := Process × ℕ) n).elim False (fun p => ¬ DoneBy p.1 p.2)

theorem notYetNat_re : REPred notYetNat :=
  REPred.iff_decoded_pred.mp (ComputablePred.to_re (ComputablePred.not doneBy_computable))

theorem notYetNat_encode (e : Process) (k : ℕ) :
    notYetNat (Encodable.encode (e, k)) ↔ ¬ DoneBy e k := by
  simp [notYetNat]

/-- “e 停机”的 Σ1 公式。 -/
noncomputable def φH : ArithmeticSemisentence 1 := codeOfREPred haltsNat

/-- “e 在 k 步内尚未停机”的 Σ1 公式。 -/
noncomputable def ψN : ArithmeticSemisentence 1 := codeOfREPred notYetNat

variable (T : ArithmeticTheory) [T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]

omit [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1] in
/-- `T` 证明的“永不停机”句（按数字）构成可枚举集合。 -/
theorem never_re_nat : REPred (fun a : ℕ => T ⊢ ∼φH/[↑a]) := by
  have : 𝚺ᴬ₁-Predicate fun b : ℕ ↦ Bootstrapping.Provable T
      (Bootstrapping.neg ℒₒᵣ
        <| Bootstrapping.subst ℒₒᵣ ?[Bootstrapping.Arithmetic.numeral b] ⌜φH⌝) := by
    definability
  apply REPred.of_eq (rePred_iff_sigma1.mpr this)
  intro a
  constructor
  · rintro hP
    apply Bootstrapping.Provable.sound
    simpa [Sentence.quote_def, Semiformula.quote_def, Rewriting.emb_subst_eq_subst_coe₁] using hP
  · rintro hφ
    simpa [Sentence.quote_def, Semiformula.quote_def, Rewriting.emb_subst_eq_subst_coe₁] using
      Bootstrapping.internalize_provability (V := ℕ) hφ

/-- S1：Foundation 算术理论 `T` 的过程观察接口，四条前提全部由定理给出。 -/
noncomputable def arithEffective : EffectiveTheory where
  provesHalts e := T ⊢ φH/[↑(Encodable.encode e)]
  provesNever e := T ⊢ ∼φH/[↑(Encodable.encode e)]
  provesNotYet e k := T ⊢ ψN/[↑(Encodable.encode (e, k))]
  re_never := (never_re_nat T).comp Computable.encode
  sigma1_complete e h :=
    (rePred_weak_representation (T := T) haltsNat_re).mp ((haltsNat_encode e).mpr h)
  delta0_complete e k h :=
    (rePred_weak_representation (T := T) notYetNat_re).mp ((notYetNat_encode e k).mpr h)
  consistent e h1 h2 := by
    apply Entailment.Consistent.not_bot (𝓢 := T)
    cl_prover [h1, h2]

/-- 在 Σ1 可靠之下，`T` 证明“e 停机”恰好当 e 确实停机。 -/
theorem provesHalts_iff (e : Process) : (arithEffective T).provesHalts e ↔ Done e :=
  ((rePred_weak_representation (T := T) haltsNat_re).symm).trans (haltsNat_encode e)

/-- S1 主定理（哥德尔 I 过程形式，落在真实理论上）：存在过程 `d`，它确实永不停机；`T` 对每个 k
证明“d 在 k 步内尚未停机”，却既证明不了“d 永不停机”，也证明不了“d 停机”（独立）；并且
d 停机恰好当 `T` 证明它永不停机。 -/
theorem godel_I_process_form_arith :
    ∃ d : Process, ¬ Done d ∧
      (∀ k : ℕ, T ⊢ ψN/[↑(Encodable.encode (d, k))]) ∧
      T ⊬ ∼φH/[↑(Encodable.encode d)] ∧
      T ⊬ φH/[↑(Encodable.encode d)] ∧
      (Done d ↔ T ⊢ ∼φH/[↑(Encodable.encode d)]) := by
  obtain ⟨d, hnd, hna, hall, hiff⟩ := (arithEffective T).godel_I_process_form
  refine ⟨d, hnd, hall, hna, ?_, hiff⟩
  intro hH
  exact hnd ((provesHalts_iff T d).mp hH)

/-- 魔鬼交易落在真实理论上：`T` 不封闭于 ω 完成规则。 -/
theorem devils_bargain_arith : ¬ (arithEffective T).OmegaClosed :=
  (arithEffective T).devils_bargain

omit [𝗥₀ ⪯ T] in
/-- 交叉核对：Foundation 自己的哥德尔第一不完备（经停机问题）对同一 `T` 成立。 -/
theorem foundation_crosscheck [𝗜𝚺₁ ⪯ T] : Entailment.Incomplete T :=
  incomplete_of_halting_problem T

end GodelQ

#print axioms GodelQ.never_re_nat
#print axioms GodelQ.arithEffective
#print axioms GodelQ.provesHalts_iff
#print axioms GodelQ.godel_I_process_form_arith
#print axioms GodelQ.devils_bargain_arith
#print axioms GodelQ.foundation_crosscheck
