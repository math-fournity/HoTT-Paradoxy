-- CG-009: **一般开口律 `iT_subst_open`（∀m，含 0）** —— statement 与承重支。
--
--      iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)      (q : 层 m+1)
--
-- ## 分工（2026-10-13 Master 派工）
--   * rel 支：001-Flash 装配（零件 ITSubstOpen2-7 已齐，见其树）
--   * **本文件：谓词 + all/exs 支**（承重点：用归纳假设的 m+1 实例）
--
-- ## 为什么 all/exs 是承重的
-- m=0 的 all 支：`iT 0 (subst ?[^&0] (^∀ q'))` 下降一层后子目标 =
--   `iT 1 (subst (QvecVOr 1) q') = subst (QvecV 1) (iT 2 q')`
-- 即一般律在 m=1、q'（层 2）的实例（因 `qVec (QvecVOr m) = QvecVOr (m+1)`，
-- 递归在 QvecVOr 族下闭合）。公式深度无界，故连 m=0 都依赖一般律。
import GodelQ.ZFC.ITSubstOpen7
import GodelQ.ZFC.IVEOpenFull
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5 GodelQ.ITSubstOpen6
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono

namespace GodelQ.ITSubstOpenGen

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般开口律**（statement，含 m = 0）。 -/
theorem iT_subst_open (m : V) :
    ∀ (q : V), IsSemiformula ℒₒᵣ (m + 1) q →
      iT m (subst ℒₒᵣ (QvecVOr (V := V) m) q) = subst ℒₛₑₜ (QvecV (V := V) m) (iT (m + 1) q) := by
  intro q hq
  sorry

end GodelQ.ITSubstOpenGen

#print axioms GodelQ.ITSubstOpenGen.iT_subst_open
