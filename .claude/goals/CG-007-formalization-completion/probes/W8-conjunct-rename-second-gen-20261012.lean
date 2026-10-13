import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFK
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 正确目标：`conjunct_rename_second` 的**项层推广**

`conjunct_rename_second` 已对 `t = ^#0` 证过：
```
subst W (subst (^#i ∷ ?[^#2]) (iVE 1 ^#0)) = subst (^#i ∷ 0) (iVE 0 (termSubst ?[^&0] ^#0))
```
一般化到任意层 1 的项 `t`：
```
subst W (subst (^#i ∷ ?[^#2]) (iVE 1 t)) = subst (^#i ∷ 0) (iVE 0 (termSubst ?[^&0] t))
```
（`W = ?[^#0,^#1,^&0]`，`i < 2`）。**这就是 `iT_substs1` 的 `rel` 支真正需要的。** -/

/-- 一般 `t` 的 `conjunct_rename_second`。 -/
lemma conjunct_rename_second_gen {i t : V} (hi : i < 2) (ht : IsSemiterm ℒₒᵣ (1:V) t) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 1) (iVE (1:V) t))
      = subst ℒₛₑₜ ((^#i : V) ∷ ((^#0 : V) ∷ (0:V)))
          (iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V) t)) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := (1:V))
    (P := fun t ↦ subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 1) (iVE (1:V) t))
      = subst ℒₛₑₜ ((^#i : V) ∷ ((^#0 : V) ∷ (0:V)))
          (iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V) t)))
  · definability
  · -- bvar：`z < 1` 故 `z = 0`
    intro z hz
    have hz0 : z = 0 := lt_one_iff_eq_zero.mp hz
    subst hz0
    rw [show termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V) = (^&(0:V) : V) from by
      rw [termSubst_bvar, nth_adjoin_zero]]
    exact conjunct_rename_second hi
  · -- fvar：`eqAtom ^&x` 的 bvar 都在引号内，`subst` 不动它
    intro x
    rw [termSubst_fvar, iVE_fvar, iVE_fvar]
    -- 两侧都是 `subst _ (eqAtom ^&x)`；`eqAtom ^&x = ^rel 2 cEqN ?[^#0, ^&x]`
    have hE : eqAtom (^&x : V) = (^rel 2 (↑cEqN) (?[^#0, ^&x] : V) : V) := rfl
    rw [hE]
    rw [show (?[^#0, ^&x] : V) = (^#0 : V) ∷ ((^&x : V) ∷ (0:V)) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
        (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
          (IsUTerm.fvar (x := x))) (IsUTerm.bvar (z := (0:V))))),
      Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
        (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
          (IsUTerm.fvar (x := x))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    -- `termSubstVec` 在 `^&x` 上不动（fvar）
    have h1 : (^#i ∷ shiftVec (V := V) 2 1 : V) = (^#i : V) ∷ ((^#2 : V) ∷ (0:V)) := by
      rw [show shiftVec (V := V) 2 1 = (?[^#2] : V) from by
        rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero, termBShiftVec_nil]]
    rw [h1]
    rw [show (^#i ∷ shiftVec (V := V) 2 0 : V) = (^#i : V) ∷ (0:V) from by
          rw [show shiftVec (V := V) 2 0 = (0 : V) from shiftVec_zero 2]]
    rw [show (?[^#0, ^&x] : V) = (^#0 : V) ∷ ((^&x : V) ∷ (0:V)) from rfl]
    -- 右侧：`subst (^#i ∷ 0) (^rel 2 cEqN ?[^#0,^&x])`
    rw [show (^#0 ∷ (^&x : V) ∷ (0:V) : V) = (?[^#0, ^&x] : V) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
        (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
          (IsUTerm.fvar (x := x))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (?[^#0, ^&x] : V) = (^#0 : V) ∷ ((^&x : V) ∷ (0:V)) from rfl]
    rw [show (?[^#i] : V) = ((^#i : V) ∷ (0:V)) from rfl]
    -- 两侧都是 `termSubstVec 2 _ ?[^#0,^&x]`，逐分量比对
    have hWi : ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V)))).[i] = (^#i : V) := by
      rcases lt_two_cases hi with rfl | rfl <;> simp
    have hWi : ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V)))).[i] = (^#i : V) := by
      rcases lt_two_cases hi with rfl | rfl <;> simp
    have hW2 : ((^#0 : V) ∷ ((^#1 : V) ∷ (0:V))).[i] = (^#i : V) := by
      rcases lt_two_cases hi with rfl | rfl <;> simp
    have eL : termSubstVec ℒₛₑₜ (2:V) (?[^#0, ^#1, ^&0] : V)
        (termSubstVec ℒₛₑₜ (2:V) (?[^#i, ^#2] : V) (?[^#0, ^&x] : V))
        = (?[^#i, ^&x] : V) := by
      rw [show (?[^#i, ^#2] : V) = (^#i : V) ∷ ((^#2 : V) ∷ (0:V)) from rfl,
        show (?[^#0, ^&x] : V) = (^#0 : V) ∷ ((^&x : V) ∷ (0:V)) from rfl]
      rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := (1:V)))]
      rw [termSubst_bvar, termSubst_bvar]
      rw [show (?[^#i, ^&x] : V) = (^#i : V) ∷ ((^&x : V) ∷ (0:V)) from rfl]
      rw [show (?[^#0, ^#1, ^&0] : V)
            = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
      rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.fvar (x := x))]
      rw [termSubst_bvar, termSubst_fvar, hWi]
    have eR : termSubstVec ℒₛₑₜ (2:V) ((^#i : V) ∷ ((^#0 : V) ∷ (0:V))) (?[^#0, ^&x] : V)
        = (?[^#i, ^&x] : V) := by
      rw [show (?[^#0, ^&x] : V) = (^#0 : V) ∷ ((^&x : V) ∷ (0:V)) from rfl,
        show (?[^#i, ^&x] : V) = (^#i : V) ∷ ((^&x : V) ∷ (0:V)) from rfl]
      rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.fvar (x := x))]
      rw [termSubst_bvar, termSubst_fvar]
      simp
    -- 右侧先推 `subst`
    rw [show (^#0 ∷ (^&x : V) ∷ (0:V) : V) = (?[^#0, ^&x] : V) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
        (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
          (IsUTerm.fvar (x := x))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show ((^#i : V) ∷ ((^#2 : V) ∷ (0:V))) = (?[^#i, ^#2] : V) from rfl,
      show ((^#0 : V) ∷ ((^&x : V) ∷ (0:V))) = (?[^#0, ^&x] : V) from rfl,
      show ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V)))) = (?[^#0, ^#1, ^&0] : V) from rfl]
    rw [eL, eR]
  · -- func
    intro k f v hkf hv ih
    sorry
  · exact ht

end GodelQ.ProbeFK
