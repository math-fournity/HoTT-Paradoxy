import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 测试 Master 的新桥形状：`?[^#0]` + domZero 版（2026-10-14）

Master 提议的正确桥（与 `all` 支同族，用**等式**而非蕴含）：

```
iT 0 (substs1 t p) = subst ℒₛₑₜ ?[^#0] (domZero ⋏ iT 1 p)
```

**关键**：向量是 `?[^#0]`（**绑定变量**，不是 `?[^&0]` 自由变量、不是 `iVE 0 t`）。
* 旧 `iT_substs1_term` 类型错，错在向量用 `iVE`（公式）；换 `?[^#0]`（项）类型就对了；
* `domZero` 顺带处理「值在 ω」，**不需 witness 引理**；
* `t` 只出现在 LHS，**不依赖 t 是否含 fvar**。

## ★ 核验结果（exit 0）：Master 的 RHS 里 `subst ?[^#0]` 是**恒等**

```lean
example {p : V} (hp : IsSemiformula ℒₛₑₜ (1:V) ((domZero (V := V)) ^⋏ iT (0+1:V) p)) :
    subst ℒₛₑₜ (?[^#0] : V) ((domZero (V := V)) ^⋏ iT (0+1:V) p)
      = ((domZero (V := V)) ^⋏ iT (0+1:V) p) := by
  rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
  exact Bootstrapping.subst_eq_self hp (by simp) (by simp)
```

⟹ **RHS 化简为 `domZero ⋏ iT 1 p`（`subst ?[^#0]` 消失）**，
而 `iT_exs` 给的是 `^∃ (domZero ⋏ iT 1 p)`——**两者差一个 `^∃`**。

故 Master 提议的等式
`iT 0 (substs1 t p) = subst ?[^#0] (domZero ⋏ iT 1 p)`
化简后是 `iT 0 (substs1 t p) = domZero ⋏ iT 1 p`——
**但 `iT_exs` 说 `iT 0 (^∃ p) = ^∃ (domZero ⋏ iT 1 p)`，有 `∃`**。
⟹ 该等式**形状上不成立**（差一个量词），除非 witness 项的取法另有安排。

## 附带发现：V 层 `subst_eq_self₁` 被遮蔽

`Functions.lean:790` 有 V 层的 `subst_eq_self₁`（`p : V`），
但 `Bootstrapping.subst_eq_self₁` 与 `open Bootstrapping.subst` 后**都解析到 ℕ 层版**（`{p : ℕ}`）。
**可用的是更一般的 `Bootstrapping.subst_eq_self`**（`:747`，`{n w : V}`）——上面用它证的。
见 `probes/W8-subst-eq-self1-V-check-20261014.lean`。

⚠ 但有一处我必须先核：`^∃ (domZero ⋏ iT 1 p)` 的 `∃` 引入用的 witness 是 `^#0`，
  而 `Derivable.exs` 的 witness 是**给定项 `t'`**——两者是否对得上要看 `substs1` 的展开。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeNewBridgeShape
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① RHS 的形状：`subst ?[^#0] (domZero ⋏ iT 1 p)`
--    `subst ?[^#0]` 把公式的第 0 个**自由变量**（= `^#0`）换成绑定变量 `^#0`
--    ⚠ 这看起来是个恒等变换！需核 `subst ?[^#0] X = X` 何时成立
--    ⚠ **载体陷阱**：`Typed.lean:244` 的 subst_eq_self₁ 是 Typed 层（Semiformula V L）
--    我们要的是 **V 层码**的版本：`Functions.lean:790`（p : V）
#check @Bootstrapping.subst_eq_self₁
#check @isSemiformula_domZero

-- ② LHS：`iT 0 (substs1 t p)`，`t` 是任意项
#check @IsSemiformula.substs1

-- ③ ★ 关键核验：`subst ?[^#0] X` 对层 1 的 X 是否**恒等**
--    `subst_eq_self₁ : IsSemiformula L 1 p → subst L (^#0 ∷ 0) p = p`
--    ⟹ 若 RHS 里 `subst ?[^#0]` 是恒等，则 RHS = `domZero ⋏ iT 1 p`（无 ∃ ！）
--    那与 `iT_exs` 的 `^∃ (domZero ⋏ iT 1 p)` **差一个 ∃**
example {p : V} (hp : IsSemiformula ℒₛₑₜ (1:V) ((domZero (V := V)) ^⋏ iT (0+1:V) p)) :
    subst ℒₛₑₜ (?[^#0] : V) ((domZero (V := V)) ^⋏ iT (0+1:V) p)
      = ((domZero (V := V)) ^⋏ iT (0+1:V) p) := by
  rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
  -- 用 V 层的 `subst_eq_self`（Functions.lean:747，{n w : V}），
  -- 它没被 ℕ 层版遮蔽
  exact Bootstrapping.subst_eq_self hp (by simp) (by simp)

end ProbeNewBridgeShape