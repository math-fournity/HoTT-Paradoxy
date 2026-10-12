import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen5
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

/-! ## 更干净的目标：项层的 `iVE` 换名律

公式层的装配太依赖 `rw` 的模式匹配。先做**项层**的对应物：

```
iVE_subst : iVE k (termSubst w t) = subst w (iVE (k+1) t)
```

取最简的 `w = ?[^&0]`、`t = ^#0` 测（`iVE 1 ^#0 = eqAtom ^#1`，
`subst ?[^&0] (eqAtom ^#1) = eqAtom ^&0 = iVE 0 ^&0`）。
这正是 `iT_rename` 的 `rel` 支需要的**项层零件**，且形状干净得多。 -/

-- 项层换名律（最简情形）：`subst ?[^&0] (iVE 1 ^#0) = iVE 0 ^&0`。
-- 展开后即 `subst_qVec_eqAtom`——本行确认两条引理接得上。
-- `subst ?[^&0] (eqAtom ^#1)`：向量是 `?[^&0]`（长度 1），不是 `qVec`
lemma iVE_subst_bvar_zero :
    subst ℒₛₑₜ (?[^&0] : V) (eqAtom (^#(0 + 1) : V)) = eqAtom (^&(0:V) : V) := by
  rw [eqAtom, eqAtom]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (1:V))))]
  congr 1
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V)))]
  simp [termSubst_bvar]

end GodelQ.ProbeRen5
