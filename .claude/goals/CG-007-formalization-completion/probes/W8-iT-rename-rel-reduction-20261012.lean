import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 探针：`iT_rename` 的 `rel` 支（`k = 0`）

取 `p = ^rel 2 0 ?[^#0, ^#0]`，两边各自化简。
注意 `IsSemiterm.bvar` 是 `↔`，要 `.mpr`；`(0:V) < 1` 用 `zero_lt_one`。 -/

-- (B) 左边：`iT 0 (^rel 2 0 ?[^&0,^&0]) = iTR 0 2 0 ?[^&0,^&0]`
example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (^rel 2 R (?[^&0, ^&0] : V)) = iTR (0 : V) 2 R (?[^&0, ^&0] : V) := by
  have hb : IsSemiterm ℒₒᵣ 1 (^&(0:V) : V) := IsSemiterm.fvar (n := 1) 0
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨hb, hb⟩).isUTerm]

-- (C) 右边：`subst ?[^&0] (iT 1 (^rel 2 0 ?[^#0,^#0])) = subst ?[^&0] (iTR 1 2 0 ?[^#0,^#0])`
example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iTR (1 : V) 2 R (?[^#0, ^#0] : V)) := by
  have hb : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨hb, hb⟩).isUTerm]

end GodelQ.ProbeRen2
