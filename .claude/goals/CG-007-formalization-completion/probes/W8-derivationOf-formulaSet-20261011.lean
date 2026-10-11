import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAO
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 关键发现：Derivation 携带 IsFormulaSet（它的第一个分量）。
-- 所以对 **推导 d** 本身，IsFormulaSet L (fstIdx d) 总是有的！
-- 缺的只是 **dd**（子推导）的 IsFormulaSet —— 但 dd 也是推导！
--
-- 问题在于 Q d 只说了 Derivable (translateSeq (fstIdx d))，
-- 没有说 d 本身是 Derivation。而 induction1 的 ih 只给 Q dp。
--
-- 但 induction1 的支里**有** DerivationOf 的假设吗？
-- 看 hAll 的签名：
--   hAll : ∀ s, IsFormulaSet L s → ∀ p d, ^∀ p ∈ s →
--     DerivationOf T d (insert (free L p) (setShift L s)) → P d → P (allIntro s p d)
-- 是的！有 DerivationOf T d (...)。所以 d 的 IsFormulaSet 有。

-- 验证：从 DerivationOf 拿 IsFormulaSet
example {d s : V} (h : DerivationOf (V := V) (L := ℒₒᵣ) Sh.craig d s) :
    IsFormulaSet ℒₒᵣ s := h.isFormulaSet

-- 而 translateSeq_setShift 需要 IsFormulaSet ℒₒᵣ s'（源集合）。
-- 在 hAll 里，源集合是 fstIdx d（子推导的结论）。
-- DerivationOf T d (insert (free L p) (setShift L s)) 给
--   IsFormulaSet L (insert (free L p) (setShift L s))
-- 要从中抽出 IsFormulaSet L (setShift L s)，再用 setShift_iff 得 IsFormulaSet L s。

example {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) (setShift ℒₒᵣ s)) :
    IsFormulaSet (L := ℒₒᵣ) s := by
  simpa using (IsFormulaSet.setShift_iff (L := ℒₒᵣ) (s := s)).mp hs

example {p s : V} (hs : IsFormulaSet (L := ℒₒᵣ) (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s))) :
    IsFormulaSet (L := ℒₒᵣ) (setShift ℒₒᵣ s) := by
  intro q hq
  exact hs q (by simp [hq])

end GodelQ.ProbeAO
