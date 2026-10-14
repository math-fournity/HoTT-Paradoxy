import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeSubstEqSelf1V
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ★ 核验结果：**两个可解析的 `subst_eq_self₁` 载体都不是 V 层码**
#check @Bootstrapping.subst_eq_self₁
-- open Bootstrapping.subst in
#check @subst_eq_self₁

/-- **本探针的发现（Foundation 的一处命名遮蔽）**：

`Functions.lean:790` 有 V 层的
```
lemma subst_eq_self₁ (hp : IsSemiformula L 1 p) :   -- p : V
    subst L (^#0 ∷ 0) p = p
```
但它**被遮蔽**：`Bootstrapping.subst_eq_self₁` 与 `open Bootstrapping.subst` 后的
`subst_eq_self₁` **都解析到 ℕ 层版**（`{p : ℕ}`）。

**⟹ V 层的 `subst_eq_self₁` 在本包**取不到**（除非用完整私有路径或自证）。**

这对 Master 的新桥形状是关键：RHS 的 `subst ?[^#0] (domZero ⋏ iT 1 p)`
若要靠 `subst_eq_self₁` 化成恒等，**得自证 V 层版**（或走 `subst_eq_self`
——`Functions.lean:747`，`{n w : V}`，那条可能可用）。 -/
theorem v_level_subst_eq_self1_is_shadowed : True := trivial

end ProbeSubstEqSelf1V