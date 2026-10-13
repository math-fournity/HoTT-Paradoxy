import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★★ 反向引理**已存在于 Foundation**：`IsSemiformula.sound`（2026-10-13）

我在 `W8-reverse-quote-20261013.lean` 里花力气自建反向引理——**白费**。
Foundation 在 `Formula/Coding.lean:478` 已有：

```
lemma IsSemiformula.sound {n φ : ℕ} (h : IsSemiformula L n φ) :
    ∃ F : FirstOrder.Semiproposition L n, ⌜F⌝ = φ
```

**⚠ 但载体是 `ℕ`**（`{n φ : ℕ}`），不是任意 `V`。
这是 [[probe-simp-residual-is-not-a-goal]] 那个陷阱的**第五次**：
「存在」与「可用」是两回事——载体不匹配就用不上。

本探针核验（**exit 0**）：确认 `IsSemiformula.sound` 的载体是 `ℕ`，任意 V 上**用不了**：

```
@IsSemiformula.sound : ∀ {L} [L.Encodable] [L.LORDefinable] {n φ : ℕ},
    IsSemiformula L n φ → ∃ F, ⌜F⌝ = φ
```

在任意 V 上引用报 `φ has type V … but is expected to have type ℕ`。

## ★ 但这**不阻塞**语义路线——因为语义路线不需要它

回到 001-Step 的问题：`¬A ⋎ B` 是否已是引号形？
我的回答是「**条件**是 A、B 是引号形，唯一缺口是基例 `p = ⌜φ⌝`」。

**现在补一个关键观察**：`ExsBlockerQ` 里的 `p` **不是**任意的 V 元素——
它来自 `^∃ p ∈ s` 且 `s` 是 `IsFormulaSet`，即 `IsFormula (^∃ p)`。
而 `IsFormula` 在 **V 层**给出（`IsSemiformula ℒₛₑₜ 0 (^∃ p)`）。

**要把它变成 `∃ φ, p = ⌜φ⌝` 需要 V 层的 `IsSemiformula.sound`，
而 Foundation 只有 ℕ 层版。** 故：

**语义路线的组装**（对 `ExsBlockerQ`）**确实需要一条 V 层的反向引理**，
它比 ℕ 层版强，且**不在 Foundation 里**。

**但注意**：ℕ 层版的存在说明**数学内容是真**的（在标准模型里每支都构造得出），
故 V 层版**应当可证**——只是需要把 `IsSemiformula.sound` 的证明
（`Nat.strongRec` + `case_iff` + `choose`）搬到 V 层。
**V 层没有 `Nat.strongRec`**（`p : V` 不是归纳类型），
这正是 `W8-reverse-quote-20261013.lean` 撞到的墙。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeReverseFound

#check @IsSemiformula.sound

-- ⚠ 下面这个 example **刻意失败**：它就是本探针的发现（载体不匹配）
-- example {n : ℕ} {φ : V} (h : IsSemiformula ℒₛₑₜ n φ) :
--     ∃ F : Semiproposition ℒₛₑₜ n, (⌜F⌝ : V) = φ := by sorry

end ProbeReverseFound