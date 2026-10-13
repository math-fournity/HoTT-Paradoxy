import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeExTest
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 先做**反驳实验**，再谈形状

候选（我在探针里写下的）：
```
iT 0 (substs1 ℒᵣ ^&0 p) = substs1 ℒₜ (iVE 0 ^&0) (iT 0 p)
```

取最小原子 p = ^rel 2 cEqN ?[^#0, ^#0]，t = ^&0，n = 0。
两侧**归一化**后比较（用 iTR 的展开）。 -/

-- 左：iT 0 (substs1 ℒᵣ ^&0 p)
--   substs1 ℒᵣ ^&0 p = subst ℒᵣ ?[^&0] p
--   subst ?[^&0] (^rel 2 cEqN ?[^#0,^#0])
--     = ^rel 2 cEqN (termSubstVec 2 ?[^&0] ?[^#0,^#0])   （substs_rel）
--     = ^rel 2 cEqN (?[^&0, ^&0])                        （termSubst_bvar ×2）
-- 所以左 = iT 0 (^rel 2 cEqN ?[^&0,^&0]) = iTR 0 2 cEqN ?[^&0,^&0]

-- 右：substs1 ℒₜ (iVE 0 ^&0) (iT 0 p)
--   iT 0 p = iTR 0 2 cEqN ?[^#0,^#0] = qqAlls (...) 2   —— 形状完全不同！

-- 判定性子步：subst 推过 qqAlls · 2 会把向量**放大成 qVec²**
-- 这正是 substs_qqAlls_two 已证的形状
example (X : V) (hX : IsUFormula ℒₛₑₜ X) :
    subst ℒₛₑₜ ((?[^&0] : V)) (qqAlls X 2) = qqAlls (subst ℒₛₑₜ ((?[^#0, ^#1, ^&0] : V)) X) 2 := by
  exact substs_qqAlls_two hX

end GodelQ.ProbeExTest
