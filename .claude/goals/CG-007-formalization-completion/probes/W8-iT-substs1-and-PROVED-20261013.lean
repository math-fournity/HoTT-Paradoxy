import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1` 的 `and` 支：两侧都推到 `qqAnd` 层。**

σ = `X ^⋏ Y`（层 1）。

* 左 `iT 0 (subst ?[^&0] (X ⋏ Y))`
  = `iT 0 (subst ?[^&0] X ⋏ subst ?[^&0] Y)`（`substs_and`）
  = `iT 0 (subst ?[^&0] X) ⋏ iT 0 (subst ?[^&0] Y)`（`iT_and`）

* 右 `subst ?[^&0] (iT 1 (X ⋏ Y))`
  = `subst ?[^&0] (iT 1 X ⋏ iT 1 Y)`（`iT_and`）
  = `subst ?[^&0] (iT 1 X) ⋏ subst ?[^&0] (iT 1 Y)`（`substs_and`）

**两侧逐分量同形** ⟹ `and` 支**由两条 `ih` 直接拼**（层数不偏移！）。

**这是好消息**：`and`/`or` 支**不需要** `qVec`（`subst` 与 `iT` 在二元连接词上**同步**）。
只有 `all`/`exs`（一元绑定）才错开。 -/
example {X Y : V} (hX : IsSemiformula ℒₒᵣ (1:V) X) (hY : IsSemiformula ℒₒᵣ (1:V) Y)
    (ihX : iT (0:V) (subst ℒₒᵣ (?[^&0] : V) X) = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) X))
    (ihY : iT (0:V) (subst ℒₒᵣ (?[^&0] : V) Y) = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) Y)) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (X ^⋏ Y))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (X ^⋏ Y)) := by
  rw [Bootstrapping.substs_and (L := ℒₒᵣ) hX.isUFormula hY.isUFormula]
  have hsX : IsUFormula ℒₒᵣ (subst ℒₒᵣ (?[^&0] : V) X) :=
    (IsSemiformula.subst (L := ℒₒᵣ) hX
      (IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0))).isUFormula
  have hsY : IsUFormula ℒₒᵣ (subst ℒₒᵣ (?[^&0] : V) Y) :=
    (IsSemiformula.subst (L := ℒₒᵣ) hY
      (IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0))).isUFormula
  rw [iT_and (V := V) (n := (0:V)) hsX hsY]
  rw [iT_and (V := V) (n := (1:V)) hX.isUFormula hY.isUFormula]
  rw [Bootstrapping.substs_and (L := ℒₛₑₜ)
      (isSemiformula_iT (n := (1:V)) X hX).isUFormula
      (isSemiformula_iT (n := (1:V)) Y hY).isUFormula]
  rw [ihX, ihY]

end GodelQ.ProbeFL
