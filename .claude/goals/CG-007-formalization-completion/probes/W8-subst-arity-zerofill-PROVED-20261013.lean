import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **判定实验**：`subst ?[^&0] (^rel 2 cEqN ?[^#1,^#0])` 的真实值。

`IsUTermVec.adjoin h ht`：`h : IsUTermVec L n w`、`ht : IsUTerm L t`
→ `IsUTermVec L (n+1) (t ∷ w)`。**没有单独的层数参数。**

所以 `?[^#1,^#0]` 的 `IsUTermVec ℒₒᵣ 2` 是
`adjoin (adjoin empty (bvar 0)) (bvar 1)`：
内层给 `[^#0]`（长度 1），外层给 `^#1 ∷ [^#0]`（长度 2）。✅

`substs_rel` 按**元数 `k = 2`** 走 `termSubstVec 2 ?[^&0]`，
故第 0 格 `^#1`（`1 ≥ len ?[^&0] = 1`）**越界补零**。 -/
lemma subst_arity_zerofill :
    subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#1, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[0, ^&0] : V) : V) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have h1 : IsUTermVec ℒₒᵣ (1:V) ((^#0 : V) ∷ (0:V)) := by
    have := IsUTermVec.adjoin (L := ℒₒᵣ) (V := V) (n := (0:V)) (w := (0:V))
      IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))
    simpa using this
  have hv : IsUTermVec ℒₒᵣ (2:V) (?[^#1, ^#0] : V) := by
    have h2 : IsUTermVec ℒₒᵣ (2:V) ((^#1 : V) ∷ ((^#0 : V) ∷ (0:V))) := by
      have := IsUTermVec.adjoin (L := ℒₒᵣ) (V := V) (n := (1:V)) (w := (^#0 : V) ∷ (0:V))
        h1 (IsUTerm.bvar (z := (1:V)))
      simpa using this
    rw [show (?[^#1, ^#0] : V) = (^#1 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
    exact h2
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv]
  congr 1
  rw [show (?[^#1, ^#0] : V) = (^#1 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl,
    show (?[0, ^&0] : V) = (0:V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (1:V))) (IsUTerm.bvar (z := (0:V)))]
  rw [termSubst_bvar, termSubst_bvar]
  rw [show ((^&0 : V) ∷ (0:V)).[1] = (0:V) from by
    rw [nth_adjoin_one]
    rw [nth_zero]
    simp [fstIdx, pi₁_zero]]
  rw [show ((^&0 : V) ∷ (0:V)).[0] = (^&0 : V) from nth_adjoin_zero _ _]

end GodelQ.ProbeFL
