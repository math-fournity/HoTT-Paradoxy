import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFG
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hAll` 需要的那条等式（原子情形）**：

`iT 0 (free p) = free (imp domZero (iT 1 p))`

右端用 `free_imp_domZero` 展开成 `imp (subst ?[^&0] domZero) (free (iT 1 p))`，
再用 `iT_substs1_atom`（左侧 `free p = subst ?[^&0] (shift p)`）。

**注意**：这不是「等式」，`free p` 与 `subst ?[^&0] p` 在 `p` 有 bvar 时不同——
`free` 先 `shift`（bvar 不动）。原子情形下 `shift` 不动 `^rel 2 cEqN ?[^#0,^#0]`
（其 bvar 都在引号内），故两者相同。 -/
lemma hAll_atom_eq :
    iT (0:V) (free ℒₒᵣ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))
      = free ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) (iT (1:V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))) := by
  have hsh : shift ℒₒᵣ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[^#0, ^#0] : V) : V) := by
    rw [Bootstrapping.shift_rel (by rw [cEqN]; exact codeIn_rel_quote _)
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl,
      show (2:V) = 0 + 1 + 1 by norm_num,
      termShiftVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))),
      termShiftVec_cons (IsUTerm.bvar (z := (0:V))) IsUTermVec.empty, termShiftVec_nil]
    simp only [termShift_bvar]
  -- 左：`free p = subst ?[^&0] (shift p) = subst ?[^&0] p`
  rw [free, substs1, hsh]
  -- 右：`free_imp_domZero` 展开
  rw [free_imp_domZero (V := V) (isSemiformula_iT (V := V) (n := (1:V))
    (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
    (IsSemiformula.rel.mpr ⟨by rw [cEqN]; exact codeIn_rel_quote _,
      by simpa using (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.bvar.mpr (by norm_num),
        IsSemiterm.bvar.mpr (by norm_num)⟩)⟩))]
  sorry

end GodelQ.ProbeFG
