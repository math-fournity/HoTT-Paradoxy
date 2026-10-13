import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`conjunct_rename_second_gen` 的 `func` 支（一般 `f`）**。

`t = ^func 2 f ?[^#0,^#0]`，两侧都归一到 `qqAlls (imp …) 2`。
用 `substs_qqAlls` 各推一次 + `hqL` 对齐向量。 -/
example {i f : V} (hi : i < 2) (hf : (ℒₒᵣ).IsFunc (2:V) f) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (?[^#i, ^#2] : V)
          (iVE (1:V) (^func (2:V) f (?[^#0, ^#0] : V))))
      = subst ℒₛₑₜ (?[^#i, ^#0] : V)
          (iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V)
            (^func (2:V) f (?[^#0, ^#0] : V)))) := by
  -- 内层：把 `iVE` 归一到 `qqAlls`（ve2 展开）
  have hv : IsUTermVec ℒₒᵣ (2:V) (?[^#0, ^#0] : V) := by
    simpa using isUTermVec_two_bvars (V := V) (L := ℒₒᵣ)
  have hv' : IsUTermVec ℒₒᵣ (2:V) (?[^&0, ^&0] : V) := by
    refine IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty ?_) ?_
    · exact IsUTerm.fvar (L := ℒₒᵣ) (V := V) 0
    · exact IsUTerm.fvar (L := ℒₒᵣ) (V := V) 0
  rw [termSubst_func (L := ℒₒᵣ) hf hv]
  have htv : termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) := by
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
    simp only [termSubst_bvar, nth_adjoin_zero]
  rw [htv]
  rw [iVE_func (n := (1:V)) hf hv, iVE_func (n := (0:V)) hf hv']
  rw [if_neg (show (2:V) ≠ 0 by norm_num), if_neg (show (2:V) ≠ 0 by norm_num)]
  rw [iVE_resultVec_two (n := (1:V)) hv, iVE_resultVec_two (n := (0:V)) hv']
  -- 归一 `.[0]`/`.[1]`
  simp only [nth_adjoin_zero, nth_adjoin_one]
  -- 两侧都是 `subst _ (ve2 _ _ f ?[iVE _ _, iVE _ _])`
  -- 展开 `ve2` 成 `qqAlls (imp …) 2`
  have eA : ve2 (1:V) (2:V) f (iVE (1:V) (^#0 : V) ∷ iVE (1:V) (^#0 : V) ∷ (0:V))
      = qqAlls (imp ℒₛₑₜ (conjunct 3 (1:V) 0 (iVE (1:V) (^#0 : V)) ^⋏
          (conjunct 3 (1:V) 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc (2:V) f))) 2 := by
    rw [ve2]
    simp only [nth_adjoin_zero, nth_adjoin_one]
  have eB : ve2 (0:V) (2:V) f (iVE (0:V) (^&0 : V) ∷ iVE (0:V) (^&0 : V) ∷ (0:V))
      = qqAlls (imp ℒₛₑₜ (conjunct 3 (0:V) 0 (iVE (0:V) (^&0 : V)) ^⋏
          (conjunct 3 (0:V) 1 (iVE (0:V) (^&0 : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc (2:V) f))) 2 := by
    rw [ve2]
    simp only [nth_adjoin_zero, nth_adjoin_one]
  rw [eA, eB]
  -- 两侧各推一次 `subst` 过 `qqAlls`
  -- 两侧各推一次 `subst` 过 `qqAlls`（k = 2，用 `substs_qqAlls_two`）
  have hA : IsUFormula ℒₛₑₜ (imp ℒₛₑₜ
      (conjunct 3 (1:V) 0 (iVE (1:V) (^#0 : V)) ^⋏
        (conjunct 3 (1:V) 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤))
      (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc (2:V) f))) := by sorry
  have hB : IsUFormula ℒₛₑₜ (imp ℒₛₑₜ
      (conjunct 3 (0:V) 0 (iVE (0:V) (^&0 : V)) ^⋏
        (conjunct 3 (0:V) 1 (iVE (0:V) (^&0 : V)) ^⋏ ^⊤))
      (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc (2:V) f))) := by sorry
  trace_state
  sorry

end GodelQ.ProbeFL
