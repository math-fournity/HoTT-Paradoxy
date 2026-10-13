import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性检验**：`ℒₒᵣ` 的 `+` 码是不是 `ℒₛₑₜ` 的项？

`TermRec.result` 的 graph（`Term/Basic.lean:321`）：
`!(isUTerm L).pi t → !(β.graph L) t y` —— **依赖 `IsUTerm L`**！
若 `t` 不是 `L` 的项，`result` 走另一支（返回 `0`）。

**测试**：`IsUTerm ℒₛₑₜ (^func 2 addIndex ?[^#0,^#0])` 是否可证？
（`addIndex` 是 `ℒₒᵣ` 的加法码；`ℒₛₑₜ` 是集合论语言，无 `+`。） -/
example : ¬ IsUTerm ℒₛₑₜ (^func (2:V) (⌜(Language.Add.add : (ℒₒᵣ).Func 2)⌝ : V)
    (?[^#0, ^#0] : V)) := by
  intro h
  obtain ⟨hkf, _⟩ := IsUTerm.func_iff.mp h
  -- `ℒₛₑₜ.IsFunc 2 addIndex` 应当不成立
  sorry

end GodelQ.ProbeFL
