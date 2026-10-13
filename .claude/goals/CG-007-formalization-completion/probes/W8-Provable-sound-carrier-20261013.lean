import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## Provable.sound 的载体核验（2026-10-13）

[[probe-simp-residual-is-not-a-goal]] 的第三次教训：核验旁证要看**载体/前提**，
不是看它被成功用了几次。`provable_iff_provable` 的载体硬接线 ℕ（`ShRE.lean:28` 证实）。

本探针核验 `Provable.sound` 能否在**我们的 V**（任意 `ORingStructure V` + `V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁`）上实例化。

## ⚠ 结论：**不能**——与 `provable_iff_provable` 同一陷阱

```
error: Application type mismatch: The argument h has type
  Provable.{u_2, 0} 𝗭𝗙𝗖 ⌜φ⌝
but is expected to have type
  Provable.{0, 0} 𝗭𝗙𝗖 ⌜φ⌝
```

`Provable.sound` 的 V 参数被**硬接线在宇宙 0**（`Provable.{0,0}`），
而我们的 `V` 是任意 `Type u_2`。**这是第四次撞同一个陷阱**：
旁证的正确性判据是**载体/前提匹配**，不是使用次数。
（前三次：`provable_iff_provable` 载体硬接线 ℕ。）

**含义**：语义路线**不能**直接用 `Provable.sound` 收尾——
要么把整条路线限制在宇宙 0 的 V，要么另找桥。
`SetTheory.complete` 本身是宇宙多态的（`Type u_2`），故语义路线的**模型侧**没问题，
卡的是「V 里的可证码 → 元层 ⊢」这一步。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeProvableSoundCarrier
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 直接在我们的 V 上试：需要一个 `Sentence ℒₛₑₜ` 与 `Provable 𝗭𝗙𝗖 ⌜φ⌝`
-- ⚠ 下面这个 example **刻意失败**，它就是本探针的发现（载体不匹配）
example {φ : Sentence ℒₛₑₜ} (h : Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (⌜φ⌝ : V)) :
    (𝗭𝗙𝗖 ⊢ φ) := by
  exact Provable.sound h

end ProbeProvableSoundCarrier