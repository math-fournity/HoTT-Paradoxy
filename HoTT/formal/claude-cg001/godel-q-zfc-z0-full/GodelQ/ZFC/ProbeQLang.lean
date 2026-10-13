import GodelQ.ZFC.ITSubsts1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
set_option maxHeartbeats 8000000

namespace GodelQ.ProbeQLang
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 直接算：bvar 与 fvar 的单点情形（这两支 construction 的体显然与 L 无关）
example (z : V) : termBShift ℒₛₑₜ (^#z) = termBShift ℒₒᵣ (^#z) := by
  rw [Bootstrapping.termBShift_bvar, Bootstrapping.termBShift_bvar]

example (x : V) : termBShift ℒₛₑₜ (^&x) = termBShift ℒₒᵣ (^&x) := by
  rw [Bootstrapping.termBShift_fvar, Bootstrapping.termBShift_fvar]

-- func 支需要 IsFunc 前提，两边语言不同 ⇒ 这一步是真正的障碍
example (k f v : V) (hfS : (ℒₛₑₜ).IsFunc k f) (hvS : IsUTermVec ℒₛₑₜ k v)
    (hfR : (ℒₒᵣ).IsFunc k f) (hvR : IsUTermVec ℒₒᵣ k v) :
    termBShift ℒₛₑₜ (^func k f v) = termBShift ℒₒᵣ (^func k f v) := by
  rw [Bootstrapping.termBShift_func hfS hvS, Bootstrapping.termBShift_func hfR hvR]
  congr 1
  -- 两边都是 `termBShiftVec L k v`
  sorry

end GodelQ.ProbeQLang
