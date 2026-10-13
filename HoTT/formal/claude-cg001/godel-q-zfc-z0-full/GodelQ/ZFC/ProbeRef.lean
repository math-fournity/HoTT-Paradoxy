import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeRefute
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 第一步：**先试反驳**，再谈形状

候选（我在 hExs 探针里写下但未验证的）：

```
iT 0 (substs1 ℒᵣ ^&0 p) = substs1 ℒₜ (iVE 0 ^&0) (iT 0 p)
```

取**最小反例候选** `p = ⊤`（verum）——如果连 verum 都对不上，候选立刻死。 -/

-- 先算左：iT 0 (substs1 ℒᵣ ^&0 ^⊤)
-- substs1 对 verum 应无影响（verum 无 bvar）
example : iT (0:V) (substs1 ℒₒᵣ (^&(0:V) : V) (^⊤ : V)) = ((^⊤ : V) : V) := by
  sorry

-- 右：substs1 ℒₜ (iVE 0 ^&0) (iT 0 ^⊤) = iVE 0 ^&0 = eqAtom ^&0
example : iT (0:V) (^⊤ : V) = ((^⊤ : V) : V) := iT_verum 0

-- 若左 = ⊤ 而右 = eqAtom ^&0，则候选被 verum 反驳
example : substs1 ℒₛₑₜ (iVE (0:V) (^&(0:V) : V)) ((^⊤ : V) : V)
    = eqAtom (^&(0:V) : V) := by
  sorry

end GodelQ.ProbeRefute
