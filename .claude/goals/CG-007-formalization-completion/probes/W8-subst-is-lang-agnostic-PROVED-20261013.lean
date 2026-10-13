import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性**：`subst ℒₛₑₜ w` 作用在 `ℒₒᵣ` 的 `^func` 码上时**是否算出结果**？

`subst` 的构造按 `qqFunc` 的编码递归，**不查 `IsFunc`**——
故 `subst ℒₛₑₜ w (^func k f v)` 应当能算。
但 `substs_rel`/`substs_func` 这类**引理**要 `IsFunc`。

**测试**：直接 `rfl` 看 `termSubst` 在 `^func` 上是否可算。 -/
example (w : V) :
    termSubst ℒₛₑₜ w (^func (2:V) (⌜(Language.Add.add : (ℒₒᵣ).Func 2)⌝ : V)
      (?[^#0, ^#0] : V))
    = termSubst ℒₛₑₜ w (^func (2:V) (⌜(Language.Add.add : (ℒₒᵣ).Func 2)⌝ : V)
      (?[^#0, ^#0] : V)) := rfl

end GodelQ.ProbeFL
