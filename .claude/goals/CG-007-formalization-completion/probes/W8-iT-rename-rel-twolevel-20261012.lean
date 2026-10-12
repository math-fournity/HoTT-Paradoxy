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

/-! ## 决定性一步：完整的 `iT_rename`（`k = 0`，原子）

`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`，`p = ^rel 2 R ?[^#0,^#0]`。

左边 = `iTR 0 2 R ?[^&0,^&0]`；右边 = `subst ?[^&0] (iTR 1 2 R ?[^#0,^#0])`。
把 `iTR` 展开，看两者是否**相等**。 -/

example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  -- 左边：subst 先作用，得 ^rel 2 R ?[^&0,^&0]，再 iT 0
  have hbF : IsSemiterm ℒₒᵣ 1 (^&(0:V) : V) := IsSemiterm.fvar (n := 1) 0
  have hbB : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  have hvB : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) := IsSemitermVec.doubleton.mpr ⟨hbB, hbB⟩
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hvB.isUTerm]
  rw [show termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) from by
    rw [termSubstVec_cons₂ hbB.isUTerm hbB.isUTerm, termSubst_bvar, termSubst_bvar]
    simp only [Matrix.cons_val_zero]]
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨hbF, hbF⟩).isUTerm]
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR hvB.isUTerm]
  simp only [iTR]
  -- 右边：把 subst 推进 qqAlls（`substs_all` 用 `qVec`）
  rw [show subst ℒₛₑₜ (?[^&0] : V)
        (qqAlls (imp ℒₛₑₜ (conjunct 2 1 0 (iVE 1 (?[^#0, ^#0] : V).[0]) ^⋏
          (conjunct 2 1 1 (iVE 1 (?[^#0, ^#0] : V).[1]) ^⋏ ^⊤))
          (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) 2)
      = qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V))
          (imp ℒₛₑₜ (conjunct 2 1 0 (iVE 1 (?[^#0, ^#0] : V).[0]) ^⋏
            (conjunct 2 1 1 (iVE 1 (?[^#0, ^#0] : V).[1]) ^⋏ ^⊤))
            (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)))) 2 from by
    rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ, qqAlls_succ]
    simp only [substs_all]
    rfl]

end GodelQ.ProbeRen2
