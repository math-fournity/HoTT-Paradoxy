-- CG-009: **一般开口律** `iT_subst_open`（∀m，含 0）。
--      iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)      (q : 层 m+1)
--
-- ## 为什么承重，不是包装
-- m=0 的 all 支：`iT 0 (subst ?[^&0] (∀ q'))` 下降一层后的子目标是
--     iT 1 (subst (QvecVOr 1) q') = subst (QvecV 1) (iT 2 q')
-- 即一般律在 m=1、q'（层 2）的实例（因 `qVec (QvecVOr m) = QvecVOr (m+1)`，递归在
-- QvecVOr 族下闭合）。公式深度无界，**连 m=0 都无法在没有一般律的情况下完成**。
-- 故本文件以 ∀m（含 0）陈述；m=0 桥由特化得到，不另立门户。
--
-- rel 支：逐 bvar z 分 z<m / z=m 两支，末项 ^&0 承接 z=m（分析见 OpenLawCheck5.lean）。
-- all/exs 支：用归纳假设的 m+1 实例（承重点）。

import GodelQ.ZFC.OpenLawCheck2
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat

namespace GodelQ.ITSubstOpenGen

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般开口律**（statement，含 m = 0）。 -/
theorem iT_subst_open (m : V) :
    ∀ (q : V), IsSemiformula ℒₒᵣ (m + 1) q →
      iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m + 1) q) := by
  intro q hq
  sorry

end GodelQ.ITSubstOpenGen

#print axioms GodelQ.ITSubstOpenGen.iT_subst_open
