import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen6
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


/-! ## 决定性实验：`qVec²` 形状的原子情形

按更正后的猜想：`iT 0 (subst w p) = subst (qVec² w) (iT 2 p)`（`w = ?[^&0]`，`p` 层数 1）。

**注意层数**：左边 `iT 0`，右边 `iT 2`——差 2，因为 `eqAtom` 自带一层绑定变量。
`qVec² ?[^&0] = ?[^#0, ^#1, ^&0]`。

先测最简的**内层换名**：`subst ?[^#0,^#1,^&0] (conjunct 2 1 0 (iVE 1 ^#0))`
`= conjunct 2 0 0 (iVE 0 ^&0)`。 -/

/-! **更正**：`conjunct b n i y` 已经做了换名 `subst (^#i ∷ shiftVec b n) y`，
所以内层不是裸的 `iVE 1 ^#0`。逐项手算：

* 左 `conjunct 2 0 0 (iVE 0 ^&0)` = `subst ?[^#0] (^rel 2 cEqN ?[^#0, ^&0])`
  = `(subst ?[^#0] cDomN) ⋏ ^rel 2 cEqN ?[^#0, ^&0]`
* 右内层 `conjunct 2 1 0 (iVE 1 ^#0)` = `subst ?[^#0, ^#2, ^#3] (^rel 2 cEqN ?[^#0, ^#1])`
  = `(subst ?[^#0] cDomN) ⋏ ^rel 2 cEqN ?[^#0, ^#2]`（`#1 ↦ ^#2`）
* 再经外层 `subst (qVec² ?[^&0]) = subst ?[^#0, ^#1, ^&0]`：`#2 ↦ ^&0`

**故要测的是**：`subst ?[^#0,^#1,^&0] (^rel 2 cEqN ?[^#0, ^#2]) = ^rel 2 cEqN ?[^#0, ^&0]`。 -/

example : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (^rel (0 + 1 + 1) (↑cEqN) (?[^#0, ^#2] : V))
    = (^rel (0 + 1 + 1) (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  have hv : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (z := (2:V))))
      (IsUTerm.bvar (z := (0:V)))
  have hR : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]
    exact codeIn_rel_quote _
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR (by simpa using hv)]
  congr 1
  rw [show (?[^#0, ^#2] : V) = (^#0 : V) ∷ ((^#2 : V) ∷ (0 : V)) from rfl,
    show (0 : V) + 1 + 1 = 2 by norm_num,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (2:V))),
    termSubst_bvar, termSubst_bvar]
  simp

end GodelQ.ProbeRen6
