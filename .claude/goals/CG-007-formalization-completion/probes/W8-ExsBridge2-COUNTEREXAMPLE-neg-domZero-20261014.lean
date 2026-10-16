import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ 反例候选：`p := neg domZero`、`t := ^&0`（2026-10-14）

Master 给的候选（标身份：Master 分析，我机器核验）：

* `p := neg domZero`（层 1，表达「`x ∉ ω`」）；
* `t := ^&0`（含 fvar，**值由赋值定，可取 ∉ω 的值**）；
* **LHS** `iT 0 (substs1 ^&0 (neg domZero))` = `¬(赋值(^&0) ∈ ω)`——取该赋值 ∉ω 则**真**；
* **RHS** `^∃ (domZero ⋏ iT 1 (neg domZero))` = `∃x (x ∈ ω ∧ x ∉ ω)` = **假**。

⟹ 若成立，`ExsBridge2` 一般形状**为假**，桥必须重找。

**本探针核验三件事**：
* ① `IsSemiformula ℒₒᵣ 1 (neg domZero)` 是否成立（p 的层数）；
* ② RHS 是否真的等价于 `∃x(x ∈ ω ∧ x ∉ ω)`（即 `domZero ⋏ neg domZero` 恒假）；
* ③ 最关键：`iT 1 (neg domZero)` 是什么（`neg domZero` 是 ℒₛₑₜ 公式，但 p 要在 ℒₒᵣ！）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeCounterNegDomZero
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ⚠ ③ 先核一个**可能的致命问题**：`domZero` 是 **ℒₛₑₜ** 的公式，
--   而 `p` 必须是 **ℒₒᵣ** 的公式（`IsSemiformula ℒₒᵣ 1 p`）。
--   `neg domZero` 在 ℒₛₑₜ 里，**不在 ℒₒᵣ 里** ⟹ 这个 p 可能根本不合类型！
#check @domZero

-- 核验：`domZero` 的语言
example : IsSemiformula ℒₛₑₜ (1:V) (domZero (V := V)) := isSemiformula_domZero (V := V) (n := (0:V))

-- 核验：`neg` 是语言多态的，但 `p` 的类型要求 ℒₒᵣ
#check @IsSemiformula

end ProbeCounterNegDomZero