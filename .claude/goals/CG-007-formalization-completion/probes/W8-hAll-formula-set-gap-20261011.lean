import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAM
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 直接看 hAll 的原始目标：
-- ih : Q d，即 Derivable (translateSeq (fstIdx d))
--      其中 fstIdx d = insert (free ℒₒᵣ p) (setShift (fstIdx dd))
-- 目标：Derivable (translateSeq s)，其中 s 满足 ^∀ p ∈ s 且 fstIdx dd = insert (free ℒₒᵣ p) (setShift (fstIdx d))

-- 展开 ih 的 sequent：
example {p dd : V} {d : V} (hd : fstIdx d = insert (free ℒₒᵣ p) (setShift ℒₒᵣ (fstIdx dd))) :
    translateSeq (fstIdx d)
      = insert (iT 0 (free ℒₒᵣ p)) (setShift ℒₛₑₜ (translateSeq (fstIdx dd))) := by
  rw [hd, translateSeq_insert]
  congr 1
  rw [translateSeq_setShift]
  · rfl
  · -- IsFormulaSet (fstIdx dd) —— 从 ih 的 Q 谓词拿不到，需要额外假设
    sorry

-- 关键：`translateSeq` 只对 **公式集** 才有 setShift 交换律。
-- 但 Q d 的定义是 Derivable (translateSeq (fstIdx d))，
-- 而 Derivable 蕴含 IsFormulaSet（Derivable.isFormulaSet）。
-- 所以 IsFormulaSet (translateSeq (fstIdx dd)) 有，但 IsFormulaSet (fstIdx dd) 没有！

-- 这是一个真实的技术障碍：translateSeq_setShift 需要**源**是公式集，
-- 而我们只有**像**是公式集。

end GodelQ.ProbeAM
