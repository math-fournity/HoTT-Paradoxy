import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst` 推过 `qqAlls`（`substs_qqAlls` 的本地副本）。 -/
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

lemma shiftVec_2_1 : shiftVec (V := V) 2 1 = (?[^#2] : V) := by
  rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero, termBShiftVec_nil]

lemma shiftVec_2_0 : shiftVec (V := V) 2 0 = (0 : V) := shiftVec_zero 2

lemma keyL : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^#2] : V) : V) := by
  rw [iVE_bvar, eqAtom, shiftVec_2_1]
  rw [show ((^#(0:V) : V) ∷ (?[^#2] : V)) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) from rfl]
  rw [show (0 : V) + 1 = 1 by norm_num]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  have hR1 : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]; exact codeIn_rel_quote _
  have hv1 : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (L := ℒₛₑₜ) (z := (1:V))))
      (IsUTerm.bvar (L := ℒₛₑₜ) (z := (0:V)))
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (k := (0 + 1 + 1 : V))
    (v := ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V)))) hR1 hv1]
  congr 1
  rw [termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (1:V)))),
      termSubstVec_cons (IsUTerm.bvar (z := (1:V))) IsUTermVec.empty,
      termSubstVec_nil, termSubst_bvar, termSubst_bvar]
  simp only [nth_adjoin_zero, nth_adjoin_one]

lemma keyR : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  rw [iVE_fvar, eqAtom, shiftVec_2_0]
  rw [show ((^#(0:V) : V) ∷ (0 : V)) = (?[^#0] : V) from rfl]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  have hR2 : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]; exact codeIn_rel_quote _
  have hv2 : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.fvar (L := ℒₛₑₜ) (x := (0:V))))
      (IsUTerm.bvar (L := ℒₛₑₜ) (z := (0:V)))
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (k := (0 + 1 + 1 : V))
    (v := ((^#(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V)))) hR2 hv2]
  congr 1
  rw [termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
      termSubstVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termSubstVec_nil, termSubst_bvar, termSubst_fvar]
  simp only [nth_adjoin_zero, nth_adjoin_one]

/-- **原子情形的 `iT_free`**：`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`。 -/
theorem iT_free_atom {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  have hbB : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  have hvB : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) := IsSemitermVec.doubleton.mpr ⟨hbB, hbB⟩
  -- 左侧：`subst ?[^&0] p = ^rel 2 R ?[^&0,^&0]`，再 `iT 0`
  have htv : termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) := by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0 : V)) from rfl]
    rw [show (2 : V) = 0 + 1 + 1 by norm_num]
    rw [termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
          (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))),
        termSubstVec_cons (IsUTerm.bvar (z := (0:V))) IsUTermVec.empty,
        termSubstVec_nil, termSubst_bvar, termSubst_bvar]
    simp only [nth_adjoin_zero]
  have hvB' : IsUTermVec ℒₒᵣ 2 (?[^#0, ^#0] : V) := hvB.isUTerm
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) (k := (2:V)) (v := (?[^#0, ^#0] : V)) hR hvB']
  rw [htv]
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.fvar (n := 1) 0, IsSemiterm.fvar (n := 1) 0⟩).isUTerm]
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR hvB.isUTerm]
  simp only [iTR]
  -- 右侧：把 `subst ?[^&0]` 推过 `qqAlls · 2`
  have hA : IsUFormula ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
      (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤)) :=
    (IsSemiformula.and.mpr
      ⟨isSemiformula_conjunct (b := 2) (n := 1) (i := 0)
        (isSemiformula_iVE (n := 1) (^#(0:V) : V)
          (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1))) (by norm_num),
       IsSemiformula.and.mpr
        ⟨isSemiformula_conjunct (b := 2) (n := 1) (i := 1)
          (isSemiformula_iVE (n := 1) (^#(0:V) : V)
            (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1))) (by norm_num),
         IsSemiformula.verum⟩⟩).isUFormula
  have hC₀ : IsSemiformula ℒₛₑₜ (1 + 1) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel R)
      (IsSemitermVec.doubleton.mpr
        ⟨IsSemiterm.bvar.mpr (by norm_num), IsSemiterm.bvar.mpr (by norm_num)⟩)
  have hC : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) := hC₀.isUFormula
  have hbody : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) :=
    IsUFormula.or.mpr ⟨hA.neg, hC⟩
  -- 先化简两侧的 `.[i]`（`?[^&0,^&0]` 与 `?[^#0,^#0]` 都是 `∷` 形式）
  rw [show (?[^&0, ^&0] : V) = (^&(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V)) from rfl,
    show (?[^#0, ^#0] : V) = (^#(0:V) : V) ∷ ((^#(0:V) : V) ∷ (0 : V)) from rfl]
  simp only [nth_adjoin_zero, nth_adjoin_one]
  -- 把整个目标 `show` 成 `((2:ℕ):V)` 形式（`substs_qqAlls` 的 `k` 是 `ℕ`）
  show qqAlls
      (imp ℒₛₑₜ (conjunct 2 0 0 (iVE 0 ^&0) ^⋏ conjunct 2 0 1 (iVE 0 ^&0) ^⋏ ^⊤)
        (subst ℒₛₑₜ (^#0 ∷ ^#1 ∷ 0) (cRel R))) ((2 : ℕ) : V)
    = subst ℒₛₑₜ (^&0 ∷ 0)
      (qqAlls
        (imp ℒₛₑₜ (conjunct 2 1 0 (iVE 1 ^#0) ^⋏ conjunct 2 1 1 (iVE 1 ^#0) ^⋏ ^⊤)
          (subst ℒₛₑₜ (^#0 ∷ ^#1 ∷ 0) (cRel R))) ((2 : ℕ) : V))
  rw [substs_qqAlls 2 _ (?[^&0] : V) hbody]
  congr 1
  -- 内层：`imp (conjunct 2 0 i …) C = subst (qVec² ?[^&0]) (imp (conjunct 2 1 i …) C)`
  rw [show (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) from by
    rw [Function.iterate_succ_apply', Function.iterate_one]
    rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
      rw [qVec, show len (?[^&0] : V) = 1 from by simp,
        termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]]
    rw [qVec, show len (?[^#0, ^&0] : V) = 2 from by rw [len_adjoin, len_adjoin, len_nil]; rfl,
      show (2 : V) = 0 + 1 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
      termBShift_bvar, show (0 : V) + 1 = 1 by norm_num,
      termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]]
  rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
  rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
  rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hA.neg hC,
    Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 1) hA]
  congr 1
  · -- 第一条：`neg (conjunct 2 0 0 (iVE 0 ^&0) ⋏ …) = subst ?[^#0,^#1,^&0] (neg (conjunct 2 1 0 …))`
    rw [Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 1) hA]
    congr 1
    -- 展开两侧的 `conjunct`
    simp only [conjunct]
    -- 现在两侧都是 `(subst ?[^#i] cDomN) ⋏ (subst (^#i ∷ shiftVec 2 n) (iVE n ·))`
    rw [keyL, keyR]
    -- 左：`(subst ?[^#0] cDomN) ⋏ ^rel 2 cEqN ?[^#0, ^&0]`；右：同样
    rw [show (subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&(0:V) : V)) : V)
        = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) from keyR]
    rfl
  · -- 第二条：`C = subst ?[^#0,^#1,^&0] C`（`cRel R` 闭式）
    rw [show (subst ℒₛₑₜ ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V))))
        (subst ℒₛₑₜ ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))) (cRel R)) : V)
        = subst ℒₛₑₜ ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))) (cRel R) from by
      rw [show ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V))))
          = (?[^#0, ^#1, ^&0] : V) from rfl]
      rw [show ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))) = (?[^#0, ^#1] : V) from rfl]
      -- `subst w (subst v p) = subst (termSubstVec w v) p`（`substs_substs`）
      sorry]

end GodelQ.ProbeL
