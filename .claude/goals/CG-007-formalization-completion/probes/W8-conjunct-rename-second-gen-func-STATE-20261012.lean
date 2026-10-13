import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `iVE` 的 `resultVec` 两个分量。 -/
lemma iVE_resultVec_two {n v : V} (hv : IsUTermVec ℒₒᵣ (2:V) v) :
    iVE.construction.resultVec ℒₒᵣ ![n] (2:V) v = ?[iVE n v.[0], iVE n v.[1]] := by
  refine nth_ext' (2:V) ?_ ?_ ?_
  · rw [iVE.construction.resultVec_lh ℒₒᵣ ![n] hv]
  · rw [show (?[iVE n v.[0], iVE n v.[1]] : V)
        = (iVE n v.[0] : V) ∷ ((iVE n v.[1] : V) ∷ (0:V)) from rfl]
    simp only [len_adjoin, len_nil]; norm_num
  · intro j hj
    rcases lt_two_cases hj with rfl | rfl
    · rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv (show (0:V) < 2 by norm_num)]
      show iVE n v.[0] = (?[iVE n v.[0], iVE n v.[1]] : V).[0]
      rw [show (?[iVE n v.[0], iVE n v.[1]] : V)
            = (iVE n v.[0] : V) ∷ ((iVE n v.[1] : V) ∷ (0:V)) from rfl]
      simp only [nth_adjoin_zero]
    · rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv (show (1:V) < 2 by norm_num)]
      show iVE n v.[1] = (?[iVE n v.[0], iVE n v.[1]] : V).[1]
      rw [show (?[iVE n v.[0], iVE n v.[1]] : V)
            = (iVE n v.[0] : V) ∷ ((iVE n v.[1] : V) ∷ (0:V)) from rfl]
      simp only [nth_adjoin_one, nth_adjoin_zero]

/-- **`conjunct_rename_second_gen` 的 `func` 支**：`t = ^func 2 f ?[^#0,^#0]`。

两侧都展开到 `ve2` 层，各含一个 `iVE` 的 `resultVec`（用 `iVE_resultVec_two` 化为二元组），
再逐分量比对。 -/
example {i f : V} (hi : i < 2) (hf : (ℒₒᵣ).IsFunc (2:V) f) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (?[^#i, ^#2] : V)
          (iVE (1:V) (^func (2:V) f (?[^#0, ^#0] : V))))
      = subst ℒₛₑₜ (?[^#i, ^#0] : V)
          (iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V)
            (^func (2:V) f (?[^#0, ^#0] : V)))) := by
  have hv : IsUTermVec ℒₒᵣ (2:V) (?[^#0, ^#0] : V) :=
    IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))
      (IsUTerm.bvar (z := (0:V)))
  have hv' : IsUTermVec ℒₒᵣ (2:V) (?[^&0, ^&0] : V) :=
    IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V))))
      (IsUTerm.fvar (x := (0:V)))
  rw [termSubst_func (L := ℒₒᵣ) hf hv]
  have htv : termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) := by
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
    simp only [termSubst_bvar, nth_adjoin_zero]
  rw [htv]
  rw [iVE_func (n := (1:V)) hf hv, iVE_func (n := (0:V)) hf hv']
  rw [iVE_resultVec_two (n := (1:V)) hv, iVE_resultVec_two (n := (0:V)) hv']
  rw [if_neg (show (2:V) ≠ 0 by norm_num), if_neg (show (2:V) ≠ 0 by norm_num)]
  -- 先把 `.[0]`/`.[1]` 归一
  have hn0 : ((^#0 : V) ∷ ((^#0 : V) ∷ (0:V))).[0] = (^#0 : V) := nth_adjoin_zero _ _
  have hn1 : ((^#0 : V) ∷ ((^#0 : V) ∷ (0:V))).[1] = (^#0 : V) := by
    rw [nth_adjoin_one]; exact nth_adjoin_zero _ _
  have hf0 : ((^&0 : V) ∷ ((^&0 : V) ∷ (0:V))).[0] = (^&0 : V) := nth_adjoin_zero _ _
  have hf1 : ((^&0 : V) ∷ ((^&0 : V) ∷ (0:V))).[1] = (^&0 : V) := by
    rw [nth_adjoin_one]; exact nth_adjoin_zero _ _
  -- 先把 `ve2` 向量参数里的 `.[0]`/`.[1]` 归一
  rw [show iVE (1:V) ((^#0 : V) ∷ ((^#0 : V) ∷ (0:V))).[0] = iVE (1:V) (^#0 : V) from by
    rw [hn0]]
  rw [show iVE (1:V) ((^#0 : V) ∷ ((^#0 : V) ∷ (0:V))).[1] = iVE (1:V) (^#0 : V) from by
    rw [hn1]]
  rw [show iVE (0:V) ((^&0 : V) ∷ ((^&0 : V) ∷ (0:V))).[0] = iVE (0:V) (^&0 : V) from by
    rw [hf0]]
  rw [show iVE (0:V) ((^&0 : V) ∷ ((^&0 : V) ∷ (0:V))).[1] = iVE (0:V) (^&0 : V) from by
    rw [hf1]]
  -- 两侧都展开 `ve2`
  rw [show ve2 (1:V) (2:V) f (iVE (1:V) (^#0 : V) ∷ iVE (1:V) (^#0 : V) ∷ (0:V))
        = qqAlls (imp ℒₛₑₜ (conjunct 3 (1:V) 0 (iVE (1:V) (^#0 : V)) ^⋏
            (conjunct 3 (1:V) 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤))
          (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc (2:V) f))) 2 from by
    rw [ve2]
    congr 2
    congr 1
    · rw [show (iVE (1:V) (^#0 : V) ∷ iVE (1:V) (^#0 : V) ∷ (0:V)).[0]
            = iVE (1:V) (^#0 : V) from nth_adjoin_zero _ _]
    · rw [show (iVE (1:V) (^#0 : V) ∷ iVE (1:V) (^#0 : V) ∷ (0:V)).[1]
            = iVE (1:V) (^#0 : V) from by
          rw [nth_adjoin_one]
          exact nth_adjoin_zero _ _]]
  rw [show ve2 (0:V) (2:V) f (iVE (0:V) (^&0 : V) ∷ iVE (0:V) (^&0 : V) ∷ (0:V))
        = qqAlls (imp ℒₛₑₜ (conjunct 3 (0:V) 0 (iVE (0:V) (^&0 : V)) ^⋏
            (conjunct 3 (0:V) 1 (iVE (0:V) (^&0 : V)) ^⋏ ^⊤))
          (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc (2:V) f))) 2 from by
    rw [ve2]
    congr 2
    congr 1
    · rw [show (iVE (1:V) (^#0 : V) ∷ iVE (1:V) (^#0 : V) ∷ (0:V)).[0]
            = iVE (1:V) (^#0 : V) from nth_adjoin_zero _ _]
    · rw [show (iVE (1:V) (^#0 : V) ∷ iVE (1:V) (^#0 : V) ∷ (0:V)).[1]
            = iVE (1:V) (^#0 : V) from by
          rw [nth_adjoin_one]
          exact nth_adjoin_zero _ _]]
  trace_state
  sorry

end GodelQ.ProbeFL
