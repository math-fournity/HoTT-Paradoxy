import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeAsm
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- `shiftVec 2 1 = ?[^#2]`
lemma shiftVec_2_1 : shiftVec (V := V) 2 1 = (?[^#2] : V) := by
  rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero]
  rfl

-- `shiftVec 2 0 = 0`
lemma shiftVec_2_0 : shiftVec (V := V) 2 0 = (0 : V) := shiftVec_zero 2

-- 关键：`subst (^#0 ∷ shiftVec 2 1) (iVE 1 ^#0) = ^rel 2 cEqN ?[^#0, ^#2]`
lemma keyL : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^#2] : V) : V) := by
  rw [iVE_bvar, eqAtom, shiftVec_2_1]
  rw [show ((^#(0:V) : V) ∷ (?[^#2] : V)) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) from rfl]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (2:V))))
      (IsUTerm.bvar (z := (0:V))))]
  congr 1
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
    termSubst_bvar, termSubst_bvar]
  rw [show (0 : V) + 1 = 1 by norm_num]
  rfl

-- 关键：`subst (^#0 ∷ shiftVec 2 0) (iVE 0 ^&0) = ^rel 2 cEqN ?[^#0, ^&0]`
lemma keyR : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  rw [iVE_fvar, eqAtom, shiftVec_2_0]
  rw [show ((^#(0:V) : V) ∷ (0 : V)) = (?[^#0] : V) from rfl]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))]
  congr 1
  rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.fvar (x := (0:V))),
    termSubst_bvar, termSubst_fvar]
  rfl


/-! ## 最终装配：`subst W (conjunct 2 1 0 (iVE 1 ^#0)) = conjunct 2 0 0 (iVE 0 ^&0)`

已知：
* `keyL : subst (^#0 ∷ shiftVec 2 1) (iVE 1 ^#0) = ^rel 2 cEqN ?[^#0,^#2]`
* `keyR : subst (^#0 ∷ shiftVec 2 0) (iVE 0 ^&0) = ^rel 2 cEqN ?[^#0,^&0]`

要证：`subst W A_R = A_L`，即
`subst W ((subst ?[^#0] cDomN) ⋏ subst (^#0 ∷ shiftVec 2 1) (iVE 1 ^#0)) = (subst ?[^#0] cDomN) ⋏ subst (^#0 ∷ shiftVec 2 0) (iVE 0 ^&0)`

两侧都是 `X ⋏ Y`。左侧 `X` 分量：`subst W (subst ?[^#0] cDomN)`；右侧 `subst ?[^#0] cDomN`。
需要 `subst W (subst ?[^#0] cDomN) = subst ?[^#0] cDomN`——`cDomN` 是 `Semisentence 1`
（只用 `#0`），而 `W.[0] = ^#0`，故内层 `?[^#0]` 把 `#0 ↦ #0`，外层 `W` 又把
`#0 ↦ ^#0`；而 `?[^#0]` 本身也是 `#0 ↦ ^#0`。两者一致。
Y 分量：`subst W (^rel 2 cEqN ?[^#0,^#2]) = ^rel 2 cEqN ?[^#0,^&0]`
——`W` 把 `#2 ↦ ^&0`。 -/

-- W 把 `#2` 映到 `^&0`。`^#z` 作为**项**；`subst w ^#z = w.[z]` 是
-- `subst` 在 atom 层的定义，故先用 `substs_rel` 剥到 rel，再算项向量。
-- 但 `^#z` 本身不是公式。改用：把它嵌入 `^rel 2 cEqN ?[^#z, ^#z]` 里。
-- 直接测最终需要的形状：`subst W (^rel 2 cEqN ?[^#0,^#2]) = ^rel 2 cEqN ?[^#0,^&0]`
lemma Wrel2 : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
    (^rel 2 (↑cEqN) (?[^#0, ^#2] : V)) = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (by
      rw [show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V))) from rfl]
      exact IsSemitermVec.adjoin
        (IsSemitermVec.adjoin
          (IsSemitermVec.adjoin (IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (3:V))
            (IsSemiterm.fvar (V := V) (n := 3) 0))
          (IsSemiterm.bvar (V := V) (z := (0:V))))
        (IsSemiterm.bvar (V := V) (z := (1:V))))]
  congr 1
  rw [show (?[^#0, ^#2] : V) = (^#0 : V) ∷ ((^#2 : V) ∷ (0 : V)) from rfl,
    show (2 : V) = 0 + 1 + 1 by norm_num,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (2:V))),
    termSubst_bvar, termSubst_bvar,
    show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V))) from rfl]
  rw [show (3 : V) = 0 + 1 + 1 + 1 by norm_num]
  rw [termSubst_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V)))]
  rw [show (0 : V) + 1 = 1 by norm_num,
    termSubst_cons₂ (IsUTerm.fvar (x := (0:V))) (IsUTerm.bvar (z := (2:V)))]
  rw [show (0 : V) + 1 = 1 by norm_num, termSubst_cons₁ (IsUTerm.bvar (z := (2:V)))]
  rfl

end GodelQ.ProbeAsm

