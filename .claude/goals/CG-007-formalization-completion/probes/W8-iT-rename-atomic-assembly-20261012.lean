import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen4
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 探针：`iT_rename` 的 `rel` 支 —— 逐项核对

仿 `shift_iTR`（`TranslateShiftCompat.lean:482`）。目标（`k = 0`）：
`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`，`p = ^rel 2 R ?[^#0,^#0]`。

先测最关键的**内层换名**：`subst (qVec ?[^&0]) (eqAtom ^#1) = eqAtom ^&0`。 -/

lemma qVec_single_fvar : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  rw [qVec, show len (?[^&0] : V) = 1 from by simp]
  rw [show termBShiftVec ℒₛₑₜ 1 (?[^&0] : V) = (?[^&0] : V) from by
    rw [show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty, termBShift_fvar,
      termBShiftVec_nil]]

lemma subst_vec_two : termSubstVec ℒₛₑₜ 2 (?[^#0, ^&0] : V) (?[^#0, ^#1] : V)
    = (?[^#0, ^&0] : V) := by
  rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl,
    show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
    termSubst_bvar, termSubst_bvar]
  simp

-- 内层换名：`subst (qVec ?[^&0]) (eqAtom ^#1) = eqAtom ^&0`
lemma subst_qVec_eqAtom : subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (eqAtom (^#(1:V) : V))
    = eqAtom (^&(0:V) : V) := by
  have hv2 : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (z := (1:V))))
      (IsUTerm.bvar (z := (0:V)))
  rw [qVec_single_fvar, eqAtom, eqAtom]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (by simpa using hv2)]
  congr 1
  exact subst_vec_two


/-! ## 决定性一步：完整的原子 `iT_rename`

`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`，`p = ^rel 2 R ?[^#0,^#0]`。

左边 = `iTR 0 2 R ?[^&0,^&0]`；右边 = `subst ?[^&0] (iTR 1 2 R ?[^#0,^#0])`。
展开 `iTR` 后，右边要把 `subst ?[^&0]` 推过 `qqAlls 2`（`substs_all` 用 `qVec`），
再与左边逐项比对。 -/

example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  have hbF : IsSemiterm ℒₒᵣ 1 (^&(0:V) : V) := IsSemiterm.fvar (n := 1) 0
  have hbB : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  have hvB : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) := IsSemitermVec.doubleton.mpr ⟨hbB, hbB⟩
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hvB.isUTerm]
  rw [show termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) from by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0 : V)) from rfl,
      show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
    simp [termSubst_bvar]]
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨hbF, hbF⟩).isUTerm]
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR hvB.isUTerm]
  simp only [iTR]
  -- 右边：把 subst ?[^&0] 推过 qqAlls 2（substs_all 用 qVec）
  have hconj0 : IsSemiformula ℒₛₑₜ (1 + 1 + 1) (conjunct (1 + 1) 1 0 (iVE (1:V) (^#(0:V) : V))) :=
    isSemiformula_conjunct (b := 1 + 1) (n := 1) (i := 0)
      (isSemiformula_iVE (n := 1) (^#(0:V) : V)
        (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)))
      (by rw [show (1:V) + 1 = 2 by norm_num]; norm_num)
  have hconj1 : IsSemiformula ℒₛₑₜ (1 + 1 + 1) (conjunct (1 + 1) 1 1 (iVE (1:V) (^#(0:V) : V))) :=
    isSemiformula_conjunct (b := 1 + 1) (n := 1) (i := 1)
      (isSemiformula_iVE (n := 1) (^#(0:V) : V)
        (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)))
      (by rw [show (1:V) + 1 = 2 by norm_num]; norm_num)
  have hsub1 : IsSemiformula ℒₛₑₜ (1 + 1 + 1) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel R)
      (by simpa using isSemitermVec_two_bvars (n := 1))
  have hbodyU : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct (1 + 1) 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct (1 + 1) 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) :=
    IsUFormula.or.mpr
      ⟨(IsSemiformula.and.mpr ⟨hconj0, IsSemiformula.and.mpr ⟨hconj1, IsSemiformula.verum⟩⟩).isUFormula.neg,
       hsub1.isUFormula⟩
  -- 目标此刻是：左体 = subst ?[^&0] (右体)，两边都形如 `^∀ (qqAlls · 1)`。
  -- 用 `congr` 剥掉两层 `^∀`/`qqAlls`，再比内层。
  simp only [qqAlls_succ]
  sorry

end GodelQ.ProbeRen4
