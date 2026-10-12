import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeMD
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `iT_free` 的**正确形状**：`iT_substs1`

`free X = substs1 ^&0 (shift X) = subst ?[^&0] (shift X)`。故

```
iT_free  ⟺  iT 0 (subst ?[^&0] σ) = subst ?[^&0] (iT 1 σ)      （σ 层 1）
```

（用 `iT_shift`：`iT 1 (shift p) = shift (iT 1 p)`。）

本文件在原子情形 `σ = ^rel 2 cEqN ?[^#0,^#0]` 上机器验证这条。
两侧都展开成 `iTR` 的 `qqAlls` 形状，逐项比对。 -/

/-- `subst` 推过 `qqAlls`（Nat 归纳）。 -/
lemma substs_qqAlls : ∀ (k : ℕ) (X w : V), IsUFormula ℒₛₑₜ X →
    subst ℒₛₑₜ w (qqAlls X (k : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[k] w) X) (k : V) := by
  intro k
  induction k with
  | zero => intro X w _; simp
  | succ j ih =>
    intro X w hX
    rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
    rw [qqAlls_succ]
    have hu : IsUFormula ℒₛₑₜ (qqAlls X (j : V)) := isUFormula_qqAlls.mpr hX
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hu]
    rw [ih X (qVec ℒₛₑₜ w) hX]
    rw [qqAlls_succ]
    congr 3

/-- `k = 2` 的特例（`qqAlls · 2` 的层数账用字面 `2`）。 -/
lemma substs_qqAlls_two {X w : V} (hX : IsUFormula ℒₛₑₜ X) :
    subst ℒₛₑₜ w (qqAlls X (2:V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[2] w) X) (2:V) := by
  rw [show (2:V) = ((2:ℕ):V) by norm_num]
  exact substs_qqAlls 2 X w hX

/-- `qVec² ?[^&0] = ?[^#0, ^#1, ^&0]`。 -/
lemma qVec_two : (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) := by
  rw [Function.iterate_succ_apply', Function.iterate_one]
  rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
    rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
    rw [show (1:V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]]
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^&0] : V) = (2:V) from by simp [len_adjoin, len_nil]; norm_num]
  rw [show (2:V) = 0 + 1 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
      (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
    termBShift_bvar, show (0:V) + 1 = 1 by norm_num,
    termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]

/-- `cRel R` 的 `subst` 不变（它是引号化句子，bvar 全在引号内）。 -/
lemma isSemiformula_cRel_subst : IsUFormula ℒₛₑₜ
    (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel (↑cEqN : V))) :=
  (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel (↑cEqN : V))
    (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.bvar.mpr (by norm_num),
      IsSemiterm.bvar.mpr (by norm_num)⟩)).isUFormula

/-- 原子情形的 `iT_substs1`。 -/
lemma iT_substs1_atom :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hR' : (ℒₛₑₜ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  -- 左侧：内层 subst 把 `#0 ↦ ^&0`
  have hL : subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[^&0, ^&0] : V) : V) := by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
    simp [termSubst_bvar]
  rw [hL]
  rw [iT_rel (V := V) (n := (0:V)) (k := (2:V)) (R := (↑cEqN : V))
    (v := (?[^&0, ^&0] : V)) hR
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.fvar (x := (0:V)))) (IsUTerm.fvar (x := (0:V)))))]
  -- 右侧
  rw [iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := (↑cEqN : V))
    (v := (?[^#0, ^#0] : V)) hR
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
  -- 目标：`iTR 0 2 cEqN ?[^&0,^&0] = subst ?[^&0] (iTR 1 2 cEqN ?[^#0,^#0])`
  rw [iTR, iTR]
  -- 右侧：`subst ?[^&0]` 推过 `qqAlls · 2`
  rw [substs_qqAlls_two]
  congr 1
  -- 内层：`subst (qVec² ?[^&0]) (imp (conjunct 2 1 i …) C) = imp (conjunct 2 0 i …) C`
  rw [qVec_two]
  rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
  rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
  -- 先分别算出两个 `IsUFormula`，再一次性 `rw`
  have hA0 : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V))) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_iVE (n := (1:V)) (^#0)
      (IsSemiterm.bvar.mpr (by norm_num)))
      (by rw [IsSemitermVec.cons_iff]
          exact ⟨IsSemiterm.bvar.mpr (by norm_num),
            isSemitermVec_shiftVec_V (V := V) 2 1⟩)).isUFormula
  have hA1 : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V))
      ^⋏ ^⊤) := by
    rw [IsUFormula.and]
    exact ⟨hA0, IsUFormula.verum⟩
  have hA : IsUFormula ℒₛₑₜ
      (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V))
        ^⋏ (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) ^⋏ ^⊤)) := by
    rw [IsUFormula.and]
    exact ⟨hA0, hA1⟩
  -- 先消去 `.[0]`、`.[1]`
  rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl,
    show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
  simp only [nth_adjoin_zero, nth_adjoin_one]
  rw [show (conjunct 2 1 0 (iVE (1:V) (^#0 : V)) ^⋏
        (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤) : V)
      = (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) ^⋏
        (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) ^⋏ ^⊤)) from by
    rw [conjunct, conjunct]
    rfl]
  rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hA.isUFormula.neg isSemiformula_cRel_subst]
  congr 1
  · -- `neg` 部分：两个 conjunct 的换名
    congr 1
    congr 1
    · rw [show (conjunct 2 1 0 (iVE (1:V) (^#0 : V)) : V)
          = subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) from by
        rw [conjunct]; rfl]
      rw [show (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤ : V)
          = (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) ^⋏ ^⊤) from by
        rw [conjunct]; rfl]
      rw [show (conjunct 2 0 0 (iVE (0:V) (^&0 : V)) : V)
          = subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&0 : V)) from by
        rw [conjunct]; rfl]
      rw [show (conjunct 2 0 1 (iVE (0:V) (^&0 : V)) ^⋏ ^⊤ : V)
          = (subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&0 : V)) ^⋏ ^⊤) from by
        rw [conjunct]; rfl]
      rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hA0 hA1]
      rw [Bootstrapping.substs_and (L := ℒₛₑₜ) ?_ IsUFormula.verum]
      · congr 1
        exact conjunct_rename_second (i := (0:V)) (by norm_num)
      · exact (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_iVE (n := (0:V)) (^&0)
          (IsSemiterm.fvar (V := V) (0:V) 0))
          (by rw [IsSemitermVec.cons_iff]
              exact ⟨IsSemiterm.bvar.mpr (by norm_num),
                isSemitermVec_shiftVec_V (V := V) 2 0⟩)).isUFormula
  · -- `cRel` 部分：`subst ?[^#0,^#1,^&0] (subst ?[^#0,^#1] cRel) = subst ?[^#0,^#1] cRel`
    congr 1
    rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0:V)) from rfl]
    rw [show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
    rw [show (2:V) = 0 + 1 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (1:V)))),
      termSubstVec_cons (IsUTerm.bvar (z := (1:V))) IsUTermVec.empty, termSubstVec_nil,
      termSubst_bvar, termSubst_bvar]
    rw [show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
    simp

end GodelQ.ProbeMD
