import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeIF2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `iT_free` 的量词支（先把 `free` 展开）

`free X = subst ?[^&0] (shift X)`，即 `substs1 ^&0 (shift X)`。

`all` 支：`p = ^∀ p'`（`p'` 层 2）。
* 左：`iT 0 (free (^∀ p')) = iT 0 (subst ?[^&0] (^∀ (shift p')))`
      `= iT 0 (^∀ (subst ?[^&0] (shift p')))`（`substs_all`）
      `= ^∀ (imp domZero (iT 1 (subst ?[^&0] (shift p'))))`
* 右：`free (iT 1 (^∀ p')) = subst ?[^&0] (shift (^∀ (imp domZero (iT 2 p'))))`
      `= subst ?[^&0] (^∀ (imp domZero (iT 2 p')))`（`shift_all`，`domZero` 不动）
      `= ^∀ (imp (subst ?[^#0,^&0] domZero) (subst ?[^#0,^&0] (iT 2 p')))`

**关键**：`subst ?[^#0,^&0] domZero = domZero`（`#0 ↦ #0`）——这条要先证。 -/

lemma subst_qVec_domZero : subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (domZero (V := V))
    = domZero (V := V) := by
  rw [domZero_eq_cDomN]
  refine subst_eq_self (L := ℒₛₑₜ) (n := 1) (w := qVec ℒₛₑₜ (?[^&0] : V))
    (isSemiformula_cDomN (V := V)) ?_ ?_
  · -- `IsSemitermVec 1 1 (qVec ?[^&0])`：`qVec ?[^&0] = ?[^#0, ^&0]`
    rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
      rw [qVec, show len (?[^&0] : V) = 1 from by simp,
        termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]]
    show IsSemitermVec ℒₛₑₜ 2 1 ((^#(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V)))
    exact IsSemitermVec.adjoin
      (IsSemitermVec.adjoin (IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (1 : V))
        (IsSemiterm.bvar.mpr (show (0:V) < 1 by norm_num)))
      (IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := 1) 0)
  · intro i hi
    rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
      rw [qVec, show len (?[^&0] : V) = 1 from by simp,
        termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]]
    rw [show (?[^#0, ^&0] : V) = (^#(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V)) from rfl]
    have hz : i = 0 := by simpa using hi
    subst hz
    simp only [nth_adjoin_zero]

end GodelQ.ProbeIF2
