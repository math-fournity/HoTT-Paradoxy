import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1_gen` 的 `and` 支**（层数 `m`、向量 `w` 一般，`len w = m`）。

两侧同 §12.26，只是把 `0`/`1` 换成 `m-1`/`m`、`?[^&0]` 换成 `w`。
**`and` 支不涉及 `qVec`，故对任意 `w` 都成立。** -/
example {m : V} {X Y w : V} (hX : IsSemiformula ℒₒᵣ m X) (hY : IsSemiformula ℒₒᵣ m Y)
    (hw : IsSemitermVec ℒₒᵣ m m w)
    (ihX : iT (m - 1) (subst ℒₒᵣ w X) = subst ℒₛₑₜ w (iT m X))
    (ihY : iT (m - 1) (subst ℒₒᵣ w Y) = subst ℒₛₑₜ w (iT m Y)) :
    iT (m - 1) (subst ℒₒᵣ w (X ^⋏ Y))
      = subst ℒₛₑₜ w (iT m (X ^⋏ Y)) := by
  rw [Bootstrapping.substs_and (L := ℒₒᵣ) hX.isUFormula hY.isUFormula]
  rw [iT_and (V := V) (n := m - 1) ?_ ?_]
  · rw [iT_and (V := V) (n := m) hX.isUFormula hY.isUFormula]
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ)
        (isSemiformula_iT (n := m) X hX).isUFormula
        (isSemiformula_iT (n := m) Y hY).isUFormula]
    rw [ihX, ihY]
  · exact (IsSemiformula.subst (L := ℒₒᵣ) (n := m) (m := m) hX hw).isUFormula
  · exact (IsSemiformula.subst (L := ℒₒᵣ) (n := m) (m := m) hY hw).isUFormula

end GodelQ.ProbeFL
