import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **判定 `all` 支：最小例的两侧「顶层构造子」是否相同。**

σ = `^∀ X`（层 1）。两侧（由 `iT_substs1_gen` 的 `n = 1`、`w = ?[^&0]`）：

* 左 `iT 0 (subst ?[^&0] (^∀ X))`
  = `iT 0 (^∀ (subst (qVec ?[^&0]) X))`
  = `^∀ (imp domZero (iT 1 (subst (qVec ?[^&0]) X)))`          —— 顶层 `qqAll`（标签 6）

* 右 `subst ?[^&0] (iT 1 (^∀ X))`
  = `subst ?[^&0] (^∀ (imp domZero (iT 2 X)))`
  = `^∀ (subst (qVec ?[^&0]) (imp domZero (iT 2 X)))`          —— 顶层 `qqAll`（标签 6）

**两侧顶层都是 `qqAll`** ⟹ **不是顶层构造子的分歧**。
分歧在**内层**（§12.22 已算）：
`iT 1 (subst (qVec ?[^&0]) X)` vs `subst (qVec ?[^&0]) (iT 2 X)`。

**本引理确认顶层标签相同**（否定「顶层就不同」这个更粗的判断）。 -/
lemma all_branch_toplevel_same {X : V} (hX : IsSemiformula ℒₒᵣ (2:V) X) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^∀ X))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^∀ X)) := by
  rw [Bootstrapping.substs_all (L := ℒₒᵣ) hX.isUFormula]
  rw [iT_all (n := (1:V)) hX.isUFormula]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ)
      (IsUFormula.imp.mpr ⟨isUFormula_domZero2, (isSemiformula_iT (n := (2:V)) X hX).isUFormula⟩)]
  trace_state
  sorry

end GodelQ.ProbeFL
