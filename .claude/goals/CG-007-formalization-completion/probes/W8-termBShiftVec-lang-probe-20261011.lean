import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeZ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 关键：termBShiftVec 与语言无关（ℒₒᵣ 与 ℒₛₑₜ 上相同）
lemma termBShiftVec_lang_eq {k v : V} (hv : IsUTermVec ℒₒᵣ k v) :
    termBShiftVec ℒₒᵣ k v = termBShiftVec ℒₛₑₜ k v := by
  sorry

-- 若成立，则 qVec 也语言无关
example {w : V} : qVec ℒₒᵣ w = qVec ℒₛₑₜ w := by
  rw [qVec, qVec]

end GodelQ.ProbeZ
