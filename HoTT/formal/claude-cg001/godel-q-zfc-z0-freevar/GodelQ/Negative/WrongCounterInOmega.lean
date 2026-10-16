import GodelQ.ZFC.FreeVarCounter

/-! 负控制：反例里“前件不可满足”靠的是自由变量取了 ω 以外的值。把自由变量改赋 ∅（∅ ∈ ω），
照搬 `eval_tLtZ` 的证明脚本，Lean 必须拒绝：此时前件可以满足（y₀ = ∅），推不出 `ω ∈ ω` 的矛盾，
而这个公式的值本来就是假的（∅ < 0）。 -/

namespace GodelQ.FreeVarCounterNeg

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory
open GodelQ.ZFCArith GodelQ.FreeVarCounter

/-- 把每个自由变量都赋值为 ∅。 -/
noncomputable def fEmpty : ℕ → U := fun _ ↦ (∅ : U)

lemma wrong_eval_tLtZ_in_omega : Semiformula.Evalf fEmpty (arithTrln.translate ltZ) := by
  show Semiformula.Eval ![] fEmpty (arithTrln.translateRel _ _)
  rw [eval_translateRel]
  intro w hw
  exfalso
  have h0 := hw 0
  have hd : w 0 ∈ (ω : U) := (dom_iff_mem _).mp h0.1
  have he : w 0 = (ω : U) := by
    simpa [DirectTranslation.varEqual, fEmpty] using h0.2
  exact mem_irrefl (ω : U) (he ▸ hd)

end GodelQ.FreeVarCounterNeg
