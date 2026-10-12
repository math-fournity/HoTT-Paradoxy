import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeLvl
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 探针：`hAll` 里 `p` 的**层数**（这才是真障碍）

`hAll` 给的假设是 `^∀ p ∈ s`（`s` 层数 0），故由 `IsSemiformula.all`
得 **`IsSemiformula ℒₒᵣ 1 p`**（层数 **1**）。

而 `iT n` 要求输入与输出**同层**（`isSemiformula_iT` 的形状是
`IsSemiformula ℒₒᵣ n p → IsSemiformula ℒₛₑₜ n (iT n p)`）。

`hAll` 要构造的是 `iT 0 (^∀ p) = ^∀ (imp domZero (iT 1 p))`
（`iT_all`）——这里 **`iT 1 p` 需要 `p` 在层数 1**，正好对上！

所以 `q := imp domZero (iT 1 p)` 的层数是 **1**（`iT 1 p` 是层 1 的公式，
但外层 `^∀` 剥掉一层后是层 0）。

**结论**：`IsSemiformula ℒₛₑₜ 1 (imp domZero (iT 1 p))` 成立。 -/

example {p : V} (hp : IsSemiformula ℒₒᵣ 1 p) :
    IsSemiformula ℒₛₑₜ 1 (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p)) :=
  IsSemiformula.imp.mpr
    ⟨isSemiformula_domZero' (V := V),
     isSemiformula_iT (V := V) (n := (1 : V)) p hp⟩

end GodelQ.ProbeLvl
