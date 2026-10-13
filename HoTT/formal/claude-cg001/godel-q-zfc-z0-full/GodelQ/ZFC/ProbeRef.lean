import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeRefute
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### `all` 支：两侧各展开一次

目标：证明 LHS 与 RHS 的**中间形状不同**。先各自用一条引理走一步，看 Lean 报什么。 -/

section
variable (X : V) (hX : IsUFormula ℒₒᵣ X)

-- LHS 第一步：substs1 套在 ^∀ 上
example : iT (0:V) (substs1 ℒₒᵣ (^&(0:V) : V) ((^∀ X) : V))
    = iT (0:V) (((^∀ (subst ℒₒᵣ ((qVec ℒₒᵣ ((?[^&0] : V)) : V)) X)) : V) : V) := by
  sorry

-- RHS 第一步：substs1 套在 iT 的输出 ^∀ 上
example : substs1 ℒₛₑₜ (iVE (0:V) (^&(0:V) : V)) (iT (0:V) ((^∀ X) : V))
    = ((^∀ (subst ℒₛₑₜ ((qVec ℒₛₑₜ (((?[iVE 0 ^&0] : V)) : V)) : V))
        (imp ℒₛₑₜ (domZero (V := V)) (iT (1:V) X))) : V) := by
  sorry

end

end GodelQ.ProbeRefute
