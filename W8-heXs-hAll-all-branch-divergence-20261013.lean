import GodelQ.ZFC.ShCraigElimSetupQ

/-! ## `hExs` / `hAll` 的 `all` 支：两侧展开到同一处，差异被机器摆明（2026-10-13）

### 先说方法论

按上一轮记下的纪律（`probe-simp-residual-is-not-a-goal`），**先试反驳再谈形状**。
本轮对候选 `iT 0 (substs1 ℒᵣ ^&0 p) = substs1 ℒₜ (iVE 0 ^&0) (iT 0 p)` 做了两步：

1. **verum 反驳失败**（两条都 exit 0，未能否证）：
   `substs_verum : subst L w ^⊤ = ^⊤`、`iT_verum : iT n ^⊤ = ^⊤`，两侧都给 `^⊤`。
2. **`all` 支差异摆明**（下面两条各 exit 0 到只剩一处 sorry）：

```
-- LHS（subst 先进去，iT 后出来——domZero 在 subst 射程之外）
iT 0 (substs1 ℒᵣ ^&0 (^∀ X))
  = ^∀ imp domZero (iT 1 (subst ℒᵣ (qVec ℒᵣ ?[^&0]) X))

-- RHS（iT 先进去，subst 后出来——domZero 在 subst 射程之内）
substs1 ℒₜ (iVE 0 ^&0) (iT 0 (^∀ X))
  = ^∀ subst ℒₜ (qVec ℒₜ ?[iVE 0 ^&0]) (imp domZero (iT 1 X))
```

**这就是差异**：LHS 的 `domZero` 由 `iT_all` 在 `subst` **之后**生成，
RHS 的 `domZero` 在 `subst` **射程之内**。
和当年否掉朴素交换律是**同一种语义错位**：
`iT` 的绑定层用 `substs_all` 的保护语义（`qVec` 首分量换 `^#0`），
而 `substs1` 用替换语义。

### 已机器验证的一段（exit 0）

```
iT 0 (substs1 ℒᵣ ^&0 (^∀ X)) = iT 0 (^∀ subst ℒᵣ (qVec ℒᵣ ?[^&0]) X)
```

证法：`show` 把 `substs1` 换成 `subst ?[^&0]`（def-eq），再 `rw [substs_all hX]`。

### 剩下的唯一一处

```
iT 0 (^∀ subst ℒᵣ (qVec ℒᵣ ?[^&0]) X) = ^∀ imp domZero (iT 1 (subst ℒᵣ (qVec ℒᵣ ?[^&0]) X))
```

即 `iT_all` 对**代入后的体**作用——需要 `IsUFormula (subst ℒᵣ (qVec ...) X)`。
这正是 `iT_substs1` 的 `all` 支，与本线另一会话正在做的工作重合，故本文件停在差异摆明。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeAllBranch
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- verum 未能否证（两条判据）
example : subst ℒₒᵣ ((?[^&0] : V)) ((^⊤ : V) : V) = ((^⊤ : V) : V) := substs_verum _
example : iT (0:V) ((^⊤ : V) : V) = ((^⊤ : V) : V) := iT_verum 0

section
variable (X : V) (hX : IsUFormula ℒₒᵣ X)

-- 已证：LHS 第一步（substs_all 推进 ^∀）
example : iT (0:V) (substs1 ℒₒᵣ (^&(0:V) : V) ((^∀ X) : V))
    = iT (0:V) (((^∀ (subst ℒₒᵣ ((qVec ℒₒᵣ ((?[^&0] : V)) : V)) X)) : V) : V) := by
  show iT (0:V) (subst ℒₒᵣ ((?[^&0] : V)) ((^∀ X) : V)) = _
  rw [Bootstrapping.substs_all hX]

-- LHS 目标形（剩一处 iT_all 对代入后的体）
example : iT (0:V) (substs1 ℒₒᵣ (^&(0:V) : V) ((^∀ X) : V))
    = ((^∀ (imp ℒₛₑₜ (domZero (V := V))
        (iT (1:V) (subst ℒₒᵣ ((qVec ℒₒᵣ ((?[^&0] : V)) : V)) X)))) : V) := by
  show iT (0:V) (subst ℒₒᵣ ((?[^&0] : V)) ((^∀ X) : V)) = _
  rw [Bootstrapping.substs_all hX]
  sorry

end

end GodelQ.ProbeAllBranch
