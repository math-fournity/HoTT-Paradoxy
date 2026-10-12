import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFA
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst` 推过 `qqAlls`（Nat 归纳 + `congr 3`）。 -/
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

/-- `subst ?[^#0,^#1] (cRel R)` 是公式（供 `substs_or` 用）。 -/
lemma isUFormula_cRel_subst : IsUFormula ℒₛₑₜ
    (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel (↑cEqN : V))) :=
  (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel (↑cEqN : V))
    (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.bvar.mpr (by norm_num),
      IsSemiterm.bvar.mpr (by norm_num)⟩)).isUFormula

/-- `conjunct 2 1 i (iVE 1 ^#0)` 的 `IsUFormula`。 -/
lemma isUFormula_conjunct1 {i : V} (hi : i < 2) : IsUFormula ℒₛₑₜ
    (conjunct 2 1 i (iVE (1:V) (^#0 : V)) ^⋏ ^⊤) :=
  IsUFormula.and.mpr ⟨(isSemiformula_conjunct (b := 2) (n := (1:V)) (i := i)
    (y := iVE (1:V) (^#0 : V))
    (isSemiformula_iVE (n := (1:V)) (^#0) (IsSemiterm.bvar.mpr (by norm_num)))
    (by norm_num at hi ⊢; exact hi)).isUFormula, IsUFormula.verum⟩

/-- **原子 `iT_substs1`**：`iT 0 (subst ?[^&0] σ) = subst ?[^&0] (iT 1 σ)`，
`σ = ^rel 2 cEqN ?[^#0,^#0]`（层 1）。

两侧都展开成 `iTR` 的 `qqAlls · 2` 形状后逐项比对：
* 内层 `imp (conjunct 2 · i (iVE · ·)) C`：用 `conjunct_rename`；
* `C = subst ?[^#0,^#1] (cRel cEqN)`：引号化句子，`subst` 不动它。 -/
lemma iT_substs1_atom :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hRs : (ℒₛₑₜ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  -- 左侧内层
  have hL : subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[^&0, ^&0] : V) : V) := by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
    simp [termSubst_bvar]
  rw [hL, iT_rel (V := V) (n := (0:V)) (k := (2:V)) (R := (↑cEqN : V))
      (v := (?[^&0, ^&0] : V)) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.fvar (x := (0:V)))) (IsUTerm.fvar (x := (0:V)))))]
  rw [iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := (↑cEqN : V))
      (v := (?[^#0, ^#0] : V)) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
  rw [iTR, iTR]
  -- 消去 `.[0]`、`.[1]`
  rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl,
    show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
  simp only [nth_adjoin_zero, nth_adjoin_one]
  -- 右侧：`subst ?[^&0]` 推过 `qqAlls · 2`
  rw [show (2:V) = ((2:ℕ):V) by norm_num, substs_qqAlls 2 _ (?[^&0] : V) ?_]
  · rw [qVec_two]
    congr 1
    -- 内层：`subst ?[^#0,^#1,^&0] (imp (conjunct 2 1 i …) C) = imp (conjunct 2 0 i …) C`
    rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl,
      show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ) ?_ isUFormula_cRel_subst]
    · -- `neg` 分量：`subst W (neg A) = neg (subst W A)`，再 `conjunct_rename`
      rw [Bootstrapping.substs_neg (L := ℒₛₑₜ)
        (p := (conjunct 2 1 0 (iVE (1:V) (^#0 : V)) ^⋏
              (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤)))
        (isUFormula_conjunct1 (by norm_num) |>.1)]
      congr 1
      -- 现在：`conjunct 2 0 0 … ⋏ conjunct 2 0 1 … = subst W (conjunct 2 1 0 … ⋏ …)`
      rw [show (conjunct 2 0 0 (iVE (0:V) (^&0 : V)) : V)
          = subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (conjunct 2 1 0 (iVE (1:V) (^#0 : V))) from by
        rw [conjunct_rename (i := (0:V)) (by norm_num)]]
      rw [show (conjunct 2 0 1 (iVE (0:V) (^&0 : V)) : V)
          = subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (conjunct 2 1 1 (iVE (1:V) (^#0 : V))) from by
        rw [conjunct_rename (i := (1:V)) (by norm_num)]]
      rw [show (conjunct 2 1 0 (iVE (1:V) (^#0 : V)) : V)
          = subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) from by
        rw [conjunct]; rfl]
      rw [show (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) : V)
          = subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)) from by
        rw [conjunct]; rfl]
      rw [show (conjunct 2 0 0 (iVE (0:V) (^&0 : V)) : V)
          = subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&0 : V)) from by
        rw [conjunct]; rfl]
      rw [show (conjunct 2 0 1 (iVE (0:V) (^&0 : V)) : V)
          = subst ℒₛₑₜ (^#(0:V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&0 : V)) from by
        rw [conjunct]; rfl]
      sorry
    · exact (isUFormula_conjunct1 (i := (0:V)) (by norm_num)).1
  · -- `cRel` 分量：引号化句子，`subst W` 不动它
    congr 1
    rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0:V)) from rfl,
      show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
    simp [termSubst_bvar]

end GodelQ.ProbeFA
