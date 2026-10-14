import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFF
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 决定性问题：`hAll` 需要哪条等式？

`hAll` 手里是 `iT 0 (free p)`，`all_m` 要的是
`free (imp domZero (iT 1 p)) = imp (subst ?[^&0] domZero) (free (iT 1 p))`。

先测「带护罩版」是否成立（原子 p）： -/

example :
    iT (0:V) (free ℒₒᵣ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))
      = free ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) (iT (1:V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))) := by
  -- 左侧：`free p = subst ?[^&0] p`（p 无 fvar），再 `iT 0`
  rw [free, substs1]
  rw [show shift ℒₒᵣ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
        = (^rel 2 (↑cEqN) (?[^#0, ^#0] : V) : V) from by
    rw [Bootstrapping.shift_rel (by rw [cEqN]; exact codeIn_rel_quote _)
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl,
      show (2:V) = 0 + 1 + 1 by norm_num,
      termShiftVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))),
      termShiftVec_cons (IsUTerm.bvar (z := (0:V))) IsUTermVec.empty, termShiftVec_nil,
      termShift_bvar, termShift_bvar]
  rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
  congr 1
  simp [termSubst_bvar]
  sorry

end GodelQ.ProbeFF
