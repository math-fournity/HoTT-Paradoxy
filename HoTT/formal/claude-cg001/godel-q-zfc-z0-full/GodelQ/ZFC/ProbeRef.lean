import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeRefute
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### `all` 支判据：`qVec` 在这里长层数

取 `p = ^∀ X`（X 是层 1 公式）。候选：

```
iT 0 (substs1 ℒᵣ ^&0 (^∀ X)) = substs1 ℒₜ (iVE 0 ^&0) (iT 0 (^∀ X))
```

**LHS**：`substs1 ℒᵣ ^&0 p = subst ℒᵣ ?[^&0] p`，
  用 `substs_all` 推过 `^∀`：`subst ?[^&0] (^∀ X) = ^∀ subst (qVec ℒᵣ ?[^&0]) X`
  → `iT 0 (^∀ subst (qVec ?[^&0]) X)` → `iT_all` → `^∀ imp domZero (iT 1 ...)`

**RHS**：`iT 0 (^∀ X) = ^∀ imp domZero (iT 1 X)`（iT_all），
  再 `substs1 ℒₜ X (^∀ ...)` → `substs_all` → `^∀ subst (qVec ℒₜ ?[X]) (imp domZero (iT 1 X))`

**两侧都有一个 `^∀`，但里面不同**：LHS 是 `imp domZero (iT 1 (subst (qVec ℒᵣ ?[^&0]) X))`，
RHS 是 `subst (qVec ℒₜ ?[iVE 0 ^&0]) (imp domZero (iT 1 X))`。

**关键差别**：RHS 的 `subst (qVec ?[X])` 会作用到 `imp domZero (...)` 上——
包括 `domZero`！而 LHS 的 `imp domZero` 是 `iT_all` **之后**才引入的，
`subst` 在 `iT` **之前**就已经做完、够不到它。

**这正是当年否掉朴素交换律的同一种语义错位**（`iT` 在绑定层下用保护语义，
`substs1` 用替换语义）。`hExs` 的 `all` 支很可能**也要卡在这里**。 -/

#check @iT_all
#check @Bootstrapping.substs_all
#check @iT_exs
end GodelQ.ProbeRefute
