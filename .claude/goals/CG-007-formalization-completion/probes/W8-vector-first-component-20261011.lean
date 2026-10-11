import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 换个方式：用「截断」函数把两个向量合并成一个。
-- trunc w n := ?[w.[0], ..., w.[n-1]]（长度 n 的向量）
-- 若两个向量在 < n 上一致，则 trunc 相等。

-- 更简单：直接对 w₁ 做「替换成 w₂ 的前缀」——定义
--   w' := fun i => if i < n then w₂.[i] else w₁.[i]
-- 但 V 里没有函数，只有向量。

-- 实用做法：用 nth_ext' 造一个向量，其前 n 位来自 w₂、其余来自 w₁。
-- 这需要「向量拼接」，Foundation 里是 adjoin。

-- 最简：直接说「存在 w'，其前 n 位与 w₂ 一致且 termSubst w' t = termSubst w₁ t」
-- 这是存在量化，definability 应该能处理（但要 Σ1）

-- 或者：换个角度——**用具体的向量**。我们的用例里 w₁ = ?[^&0]、w₂ = ^#0 ∷ ^&0 ∷ 0。
-- 直接证这两个具体向量的情形，不做一般化。

-- 具体情形：termSubst ?[^&0] t = termSubst (^#0 ∷ ^&0 ∷ 0) t（当 t 层数 ≤ 1）
lemma termSubst_singleton_eq_cons {t : V} (ht : IsSemiterm ℒₛₑₜ 1 t) :
    termSubst ℒₛₑₜ (?[^&0] : V) t
      = termSubst ℒₛₑₜ ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V)) t := by
  revert t
  apply IsSemiterm.sigma1_induction (L := ℒₛₑₜ) (n := (1 : V))
    (P := fun t ↦ termSubst ℒₛₑₜ (?[^&0] : V) t
      = termSubst ℒₛₑₜ ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V)) t)
  · definability
  · intro z hz
    rw [termSubst_bvar, termSubst_bvar]
    -- z < 1 故 z = 0
    have hz0 : z = 0 := by simpa using lt_one_iff_eq_zero.mp hz
    subst hz0
    rw [nth_adjoin_zero, nth_adjoin_zero]
  · intro x
    rw [termSubst_fvar, termSubst_fvar]
  · intro k f v hf hv ih
    rw [termSubst_func hf hv.isUTerm, termSubst_func hf hv.isUTerm]
    congr 1
    sorry

end GodelQ.ProbeAL
