import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeNorm
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `V` 层 numeral 的**命名 simp 集**（不登记全局 `[simp]`，避免递归） -/

theorem V_two : (2 : V) = 1 + 1 := by norm_num
theorem V_three : (3 : V) = 2 + 1 := by norm_num
theorem V_natCast_two : (2 : V) = ((2 : ℕ) : V) := by norm_num
theorem V_natCast_three : (3 : V) = ((3 : ℕ) : V) := by norm_num

-- 测试：用 `simp only [...]` 显式列出
example : (0 : V) + 1 + 1 = ((2 : ℕ) : V) := by
  rw [show (0 : V) + 1 + 1 = 2 by norm_num, V_natCast_two]

example : (2 : V) + 1 = ((3 : ℕ) : V) := by
  rw [show (2 : V) + 1 = 3 by norm_num, V_natCast_three]

end GodelQ.ProbeNorm
