import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeQ

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 试：`iVE` 与 `termSubst` 在 fvar 代入下。

`substs1 L ^&0 σ = subst L ?[^&0] σ`，即把 **fvar 0** 塞进去（不是 bvar）。
`termSubst L ?[^&0] t` 对 fvar 不动（`termSubst_fvar`），对 bvar 换 `w.[z]`。

但 `iT 0 (subst ℒₒᵣ ?[^&0] σ)` 里的 `subst` 是**公式层**的代入（`Bootstrapping.subst`），
它同时处理 bvar（换 `w.[z]`）与 fvar（不动）。而 `iT 1 σ` 的 fvar 编码是 `eqAtom ^&x`，
`subst ℒₛₑₜ ?[^&0]` 对它是……要看 `subst` 对 fvar 的处理。

结论：需要先弄清 `Bootstrapping.subst` 对 `^&x` 的行为。 -/
#check @Bootstrapping.subst_bvar
#check @Bootstrapping.subst_fvar
#check @Bootstrapping.subst_rel
#check @Bootstrapping.subst_func
#check @Bootstrapping.substs1
#check @Bootstrapping.IsSemiformula.substs1

end GodelQ.ProbeQ
