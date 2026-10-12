import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeDF
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **verum 支：`ProbeDef2` 的形状在此支为假**。

左端 `iT n (free ^⊤) = ^⊤`（`free`/`iT` 都不动 `⊤`），
右端 `imp D (free (iT (n+1) ^⊤)) = imp D ^⊤`——**两者不等**：
`^⊤ = ⟪2,0⟫+1` 而 `imp D ^⊤ = ⟪5,·,·⟫+1`，顶层 pair 标签不同。

故 `iT_free_shape` 的普适形状**不成立**，`ProbeDef2` 那条路线在此支终结。 -/
example (n : V) : ¬ (iT n (free ℒₒᵣ (^⊤ : V))
      = imp ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V)))
          (free ℒₛₑₜ (iT (n + 1) (^⊤ : V)))) := by
  intro h
  rw [free, Bootstrapping.shift_verum,
    show substs1 ℒₒᵣ (^&0) (^⊤ : V) = ^⊤ from Bootstrapping.substs_verum _,
    iT_verum] at h
  rw [iT_verum, free, Bootstrapping.shift_verum,
    show substs1 ℒₛₑₜ (^&0) (^⊤ : V) = ^⊤ from Bootstrapping.substs_verum _] at h
  -- `h : ^⊤ = imp D ^⊤`，即 `⟪2,0⟫+1 = ⟪5,⟪neg D, ^⊤⟫⟫+1`
  rw [show (imp ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V))) (^⊤ : V))
      = ⟪5, ⟪neg ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V))), ^⊤⟫⟫ + 1 from rfl,
    show (^⊤ : V) = ⟪2, 0⟫ + 1 from rfl] at h
  -- 两边都是 `x + 1`：消去
  have h' : (⟪2, 0⟫ : V) = ⟪5, ⟪neg ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V))), ^⊤⟫⟫ := by
    exact add_right_cancel h
  -- `pair_ext_iff`：两边的首分量必须相等
  have := (pair_ext_iff.mp h').1
  norm_num at this

end GodelQ.ProbeDF
