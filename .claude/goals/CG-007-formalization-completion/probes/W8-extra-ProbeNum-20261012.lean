import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeNum
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `V` 层 numeral 归一：把 `0 + 1 + 1` 与 `2` 统一

反复的失败都源于此。这里试几种写法，找出**稳定**的那一个。 -/

-- 候选 1：`norm_num` 直接作用于 `V` 层
example : (0 : V) + 1 + 1 = 2 := by norm_num

-- 候选 2：`simp` + `Nat.cast`
example : ((0 + 1 + 1 : ℕ) : V) = 2 := by norm_num

-- 候选 3：`push_cast` + `ring`
example : ((2 : ℕ) : V) = 2 := by norm_num

-- 候选 4：把 `2` 写成 `(2:ℕ)` 形式后与 `0+1+1` 互通
example : (2 : V) = ((2 : ℕ) : V) := by norm_num

-- 候选 5：`(2:V)` 展开成 `1 + 1`
example : (2 : V) = 1 + 1 := by norm_num

-- 候选 6：`(2:V)` 展开成 `0 + 1 + 1`
example : (2 : V) = 0 + 1 + 1 := by norm_num

end GodelQ.ProbeNum
