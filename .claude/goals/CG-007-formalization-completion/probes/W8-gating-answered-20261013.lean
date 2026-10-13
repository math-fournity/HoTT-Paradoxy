import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **判定（项层）：`termSubst ?[^&0]` 与 `termSubst (qVec ?[^&0])` 在 `^#0` 上不同。**

这是 §12 的论断，也是 `all` 支真假的关键。

* `termSubst ?[^&0] ^#0 = (?[^&0]).[0] = ^&0`   （向量 1 格，`#0` 在界内）
* `termSubst (qVec ?[^&0]) ^#0 = (qVec ?[^&0]).[0] = ^#0`   （首格是保护层）

**`^&0 ≠ ^#0`** ⟹ 两者不同。 -/
lemma termSubst_vs_qVec_bvar0 :
    termSubst ℒₒᵣ (?[^&0] : V) (^#0 : V) = (^&0 : V) ∧
    termSubst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) (^#0 : V) = (^#0 : V) := by
  constructor
  · rw [termSubst_bvar]
    rw [show (?[^&0] : V).[0] = (^&0 : V) from by
      rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero]]
  · rw [termSubst_bvar]
    rw [show (qVec ℒₒᵣ (?[^&0] : V)) = ((^#0 : V) ∷ ((^&0 : V) ∷ (0:V))) from by
      rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
      rw [show (1:V) = 0 + 1 by norm_num,
        termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
        termBShift_fvar, termBShiftVec_nil]]
    rw [nth_adjoin_zero]

/-- **决定性**：`^&0 ≠ ^#0`（编码不同：`⟪1,0⟫+1` vs `⟪0,0⟫+1`）。 -/
lemma fvar0_ne_bvar0 : (^&(0:V) : V) ≠ (^#(0:V) : V) := by
  intro h
  have h1 : (⟪(1:V), (0:V)⟫ : V) + 1 = ⟪(0:V), (0:V)⟫ + 1 := by
    simpa only [qqFvar, qqBvar] using h
  have h2 : (⟪(1:V), (0:V)⟫ : V) = ⟪(0:V), (0:V)⟫ := add_right_cancel h1
  have h3 : (1:V) = (0:V) := (pair_ext_iff.mp h2).1
  exact absurd h3 (by norm_num)

end GodelQ.ProbeFL
