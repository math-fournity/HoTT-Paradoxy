import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeStep
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### `subst` 推过 `n` 层量词（从 `W8-subst-qqAlls-20261012` 抄来） -/

lemma subst_qqAlls {X : V} (hX : IsUFormula ℒₛₑₜ X) :
    ∀ (n : ℕ) (w : V), subst ℒₛₑₜ w (qqAlls X (n : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[n] w) X) (n : V) := by
  intro n w
  induction n generalizing w with
  | zero => simp [qqAlls_zero]
  | succ k ih =>
    have hXk : IsUFormula ℒₛₑₜ (qqAlls X (k : V)) := isUFormula_qqAlls.mpr hX
    have hit : ((qVec ℒₛₑₜ)^[k + 1] w) = ((qVec ℒₛₑₜ)^[k] (qVec ℒₛₑₜ w)) := by
      rw [Function.iterate_succ_apply]
    rw [Nat.cast_succ, qqAlls_succ, Bootstrapping.substs_all hXk, hit,
      ih (qVec ℒₛₑₜ w), qqAlls_succ]

/-! ## 原子 `iT_free`：`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)` -/

example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  have hbB : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  have hvB : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) := IsSemitermVec.doubleton.mpr ⟨hbB, hbB⟩
  have htv : termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) := by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0 : V)) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
    simp only [termSubst_bvar, nth_adjoin_zero]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hvB.isUTerm, htv]
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.fvar (n := 1) 0, IsSemiterm.fvar (n := 1) 0⟩).isUTerm]
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR hvB.isUTerm]
  simp only [iTR]
  have hc0 : IsSemiformula ℒₛₑₜ 3 (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V))) :=
    isSemiformula_conjunct (b := 2) (n := 1) (i := 0)
      (isSemiformula_iVE (n := 1) (^#(0:V) : V)
        (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)))
      (by norm_num)
  have hc1 : IsSemiformula ℒₛₑₜ 3 (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V))) :=
    isSemiformula_conjunct (b := 2) (n := 1) (i := 1)
      (isSemiformula_iVE (n := 1) (^#(0:V) : V)
        (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)))
      (by norm_num)
  have hsub : IsSemiformula ℒₛₑₜ 3 (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel R)
      (by simpa using isSemitermVec_two_bvars (n := 1))
  have hbody : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) :=
    IsUFormula.or.mpr
      ⟨(IsSemiformula.and.mpr ⟨hc0, IsSemiformula.and.mpr ⟨hc1, IsSemiformula.verum⟩⟩).isUFormula.neg,
       hsub.isUFormula⟩
  -- `qVec w = ^#0 ∷ termBShiftVec (len w) w`，逐步算
  have e1 : qVec ℒₛₑₜ (?[^&0] : V) = ((^#0 : V) ∷ ((^&0 : V) ∷ (0 : V))) := by
    rw [qVec, show len (?[^&0] : V) = 1 from by simp]
    rw [show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]
  have hq2 : (qVec ℒₛₑₜ)^[(2:ℕ)] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) := by
    rw [Function.iterate_succ_apply, e1]
    show qVec ℒₛₑₜ ((^#0 : V) ∷ ((^&0 : V) ∷ (0 : V))) = ?[^#0, ^#1, ^&0]
    rw [qVec, show len ((^#0 : V) ∷ ((^&0 : V) ∷ (0 : V))) = 2 from by norm_num]
    rw [show (2 : V) = 0 + 1 + 1 by norm_num]
    rw [termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
      (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V))))]
    simp
  -- RHS: subst ?[^&0] (qqAlls BODY_R 2) = qqAlls (subst (qVec² ?[^&0]) BODY_R) 2
  have hR : subst ℒₛₑₜ (?[^&0] : V)
      (qqAlls (imp ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) (2 : V))
    = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[(2:ℕ)] (?[^&0] : V))
        (imp ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
          (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)))) (2 : V) :=
    subst_qqAlls hbody 2 (?[^&0] : V)
  have hAR : IsSemiformula ℒₛₑₜ 3
      (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
        (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hc0, IsSemiformula.and.mpr ⟨hc1, IsSemiformula.verum⟩⟩
  -- 先化简 `.[0]`/`.[1]`，让 `hR` 能匹配
  simp only [nth_adjoin_zero, nth_adjoin_one]
  rw [hR, hq2]
  congr 1
  -- `imp p q = neg p ^⋎ q`（definitional）：用 `show` 把目标写成 ⋎ 形式
  show neg ℒₛₑₜ (conjunct 2 0 0 (iVE (0:V) (^&(0:V) : V)) ^⋏
        (conjunct 2 0 1 (iVE (0:V) (^&(0:V) : V)) ^⋏ ^⊤))
      ^⋎ subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)
    = subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (neg ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
          ^⋎ subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))
  -- 右侧 `subst W (neg A_R ⋎ C)`：
  -- `substs_neg` 先剥掉 `neg`，再 `substs_and`/`substs_or` 分配。
  -- 必须**先在 RHS 定位**（LHS 无 `subst`，rw 会失败）。
  have hStep : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
      (neg ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))
    = neg ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤)))
      ^⋎ subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))
    := by
      -- `IsSemitermVec L k n w`：k = 长度、n = 层数。
      -- `adjoin` 用**元素的层数**作 k，所以逐层 adjoin 保持层数 3。
      have hf : IsSemiterm (V := V) ℒₛₑₜ 3 (^&(0:V) : V) := IsSemiterm.fvar (V := V) (n := 3) 0
      have hb1 : IsSemiterm (V := V) ℒₛₑₜ 3 (^#(1:V) : V) := IsSemiterm.bvar.mpr (by norm_num)
      have hb0 : IsSemiterm (V := V) ℒₛₑₜ 3 (^#(0:V) : V) := IsSemiterm.bvar.mpr (by norm_num)
      have hvec : IsSemitermVec (V := V) ℒₛₑₜ 3 3
          ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V)))) := by
        have h1 : IsSemitermVec (V := V) ℒₛₑₜ (0 + 1) 3 ((^&(0:V) : V) ∷ (0 : V)) :=
          IsSemitermVec.adjoin (IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (3 : V)) hf
        have h2 : IsSemitermVec (V := V) ℒₛₑₜ 2 3
            ((^#(1:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V))) :=
          IsSemitermVec.adjoin h1 hb1
        have h3 : IsSemitermVec (V := V) ℒₛₑₜ 3 3
            ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V)))) :=
          IsSemitermVec.adjoin h2 hb0
        exact h3
      -- 先 `substs_or` 分配 ⋎（顶层），`neg` 才暴露在顶层
      rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hAR.neg.isUFormula hsub.isUFormula,
        Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 3) hAR hvec]
  -- 目标：`neg A_L ⋎ C = subst W (neg A_R ⋎ C)`。
  -- `hStep.symm : neg (subst W A_R) ⋎ subst W C = subst W (neg A_R ⋎ C)`。
  -- 所以只要证 `neg A_L ⋎ C = neg (subst W A_R) ⋎ subst W C`。
  refine Eq.trans ?_ hStep.symm
  -- `neg X ⋎ C` 形式；两侧都是 `neg _ ⋎ C`
  congr 1
  -- `conjunct b n i y = subst ?[^#i] cDomN ⋏ subst (^#i ∷ shiftVec b n) y`
  rw [show conjunct (V := V) 2 0 0 (iVE (0:V) (^&(0:V) : V))
      = (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
        ^⋏ subst ℒₛₑₜ ((^#0 : V) ∷ (shiftVec (V := V) 2 0)) (iVE (0:V) (^&(0:V) : V)) from rfl,
    show conjunct (V := V) 2 1 0 (iVE (1:V) (^#(0:V) : V))
      = (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
        ^⋏ subst ℒₛₑₜ ((^#0 : V) ∷ (shiftVec (V := V) 2 1)) (iVE (1:V) (^#(0:V) : V)) from rfl]
  sorry

end GodelQ.ProbeStep
