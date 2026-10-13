import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1_samelevel` 的 `rel` 支**（路线 2：直接用 `iTR` 显式形式）。

目标：`iT n (subst ?[^#0,^&0] (^rel k R v)) = subst ?[^&0] (iT n (^rel k R v))`（`n = 1`）。

* 左端：`subst` 先动 → `iT n (^rel k R (termSubstVec k ?[^#0,^&0] v))`
  = `iTR n k R (termSubstVec k ?[^#0,^&0] v)`（用 `iT_rel`）。
* 右端：`iT n (^rel k R v) = iTR n k R v`，再 `subst ?[^&0]` 推过 `qqAlls 2`
  （`substs_qqAlls_two`）→ `qqAlls (subst ?[^#0,^#1,^&0] (imp …)) 2`。

`iTR` 是 `def`，故 `iTR n k R (termSubstVec …)` 与 `iTR n k R v` 的
**内部 `conjunct` 链**要用 `conjunct_rename_second_gen` 逐分量换名。
本探针先把**左侧**推到 `iTR` 的显式形式，确认形状。 -/
example {k R v : V} (hR : (ℒₒᵣ).IsRel k R)
    (hv : IsSemitermVec ℒₒᵣ k (1:V) v) :
    iT (1:V) (subst ℒₒᵣ (?[^#0, ^&0] : V) (^rel k R v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel k R v)) := by
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^#0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.bvar.mpr (by norm_num),
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  rw [iT_rel (V := V) (n := (1:V)) (k := k) (R := R) hR
      (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (V := V) hv hw).isUTerm]
  rw [iT_rel (V := V) (n := (1:V)) (k := k) (R := R) hR hv.isUTerm]
  -- 两侧都是 `iTR 1 k R _`；展开 `iTR` 看 `conjunct` 链
  rw [iTR, iTR]
  rw [substs_qqAlls_two (L := ℒₛₑₜ) (X := _) ?_]
  trace_state
  sorry

end GodelQ.ProbeFL
