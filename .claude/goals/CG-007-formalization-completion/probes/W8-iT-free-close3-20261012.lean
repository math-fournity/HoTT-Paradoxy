import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeClose3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `iT_rename`：`iT` 与「自由化」的交换律

目标（§2.5 更正后的形状）：

```
iT_rename(k) :  iT k (subst ℒₒᵣ (qVec^k ?[^&0]) p) = subst ℒₛₑₜ (qVec^k ?[^&0]) (iT k p)
```

**等等**——先确认到底该是 `k` 还是 `k+2`。`iT_all` 给
`iT k (^∀ p) = ^∀ (imp domZero (iT (k+1) p))`：`iT` **每遇到一个量词就加一层**。
而 `subst` 每推过一层 `qqAlls` 加一个 `qVec`。

所以「同一个 `k`」是自洽的：`iT k` 与 `subst` 的层数**同步增长**。
先前担心的 `+2` 是因为把 `iVE` 的 `eqAtom`（在**原子**处多一层）
与 `iT` 的量词层（在**量词**处加一层）混为一谈。

**先测最简情形**：`k = 0`，`p = ^rel 2 R ?[^#0,^#0]`（层 1）。 -/

lemma qVec_single_fvar_or : qVec ℒₒᵣ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  rw [qVec, show len (?[^&0] : V) = 1 from by simp]
  rw [show termBShiftVec ℒₒᵣ 1 (?[^&0] : V) = (?[^&0] : V) from by
    rw [show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty, termBShift_fvar,
      termBShiftVec_nil]]

lemma qVec_single_fvar_set : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  rw [qVec, show len (?[^&0] : V) = 1 from by simp]
  rw [show termBShiftVec ℒₛₑₜ 1 (?[^&0] : V) = (?[^&0] : V) from by
    rw [show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty, termBShift_fvar,
      termBShiftVec_nil]]

/-- **正确层数的原子情形**：`σ` 层 1，左 `iT 0`、右 `iT 1`。
这是 `iT_free` 的核（`free = substs1 ^&0 ∘ shift`，配合已证的 `iT_shift`）。 -/
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
  -- 右边：把 subst ?[^&0] 推过 qqAlls 2（两层），向量变 qVec² ?[^&0] = ?[^#0,^#1,^&0]
  -- 两个 `conjunct` 的公式性（层数 2+1=3）
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
  -- 目标右边外层就是 `^∀`，直接对它用 substs_all
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) (IsUFormula.all.mpr hbody)]
  congr 1
  -- 现在内层是 `qqAlls BODY_L 1 = subst (qVec ?[^&0]) (qqAlls BODY_R 1)`
  -- 内层：`qqAlls BODY_L 2 = subst (qVec ?[^&0]) (qqAlls BODY_R 2)`
  -- 直接对右边的 `qqAlls · 2` 用两次 substs_all（外层已在前面推过一层）
  conv_rhs => rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hbody]
  -- 现在右边是 `^∀ (subst (qVec ?[^&0]) (qqAlls BODY_R 1))`
  conv_rhs => rw [qqAlls_succ]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) (IsUFormula.all.mpr hbody)]
  sorry

end GodelQ.ProbeClose3
