import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 决定性实验：`iT_free` 的原子情形

猜想 `iT_free : iT 0 (free ℒₒᵣ q) = free ℒₛₑₜ (iT 1 q)`（`q` 层数 1）。

**先测最简原子** `q = ^rel 2 0 ?[^#0, ^#0]`（即 `#0 = #0`）。
两边都逐项展开，看是否**等式**成立（用 `decide` 不行——这是 V 层）。

先只做左、右两边的**化简**，各自独立证明，避免一次展开太多。 -/

-- (1) 左边：`free ℒₒᵣ q = ^rel 2 0 ?[^&0, ^&0]`
example : free ℒₒᵣ (^rel 2 (0 : V) (?[^#0, ^#0] : V))
    = (^rel 2 (0 : V) (?[^&0, ^&0] : V) : V) := by
  show subst ℒₒᵣ (?[^&0] : V)
      (shift ℒₒᵣ (^rel 2 (0 : V) (?[^#0, ^#0] : V))) = _
  rw [Bootstrapping.shift_rel (L := ℒₒᵣ) (by simp)
    (IsSemitermVec.adjoin (isSemitermVec_single_bvar (L := ℒₒᵣ) (n := 1) (by simp))
      (isSemitermVec_single_bvar (L := ℒₒᵣ) (n := 1) (by simp)))]
  sorry

end GodelQ.ProbeRen
