import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1` 的 `all` 支：两侧都推到 `imp domZero` 层，确认第二分量的形状。**

σ = `^∀ X`（层 1，`X` 层 2）。

* 左 `iT 0 (subst ?[^&0] (^∀ X))`
  = `iT 0 (^∀ (subst (qVec ?[^&0]) X))`              -- substs_all
  = `^∀ (imp domZero (iT 1 (subst (qVec ?[^&0]) X)))`  -- iT_all
  记 `A := iT 1 (subst (qVec ?[^&0]) X)`

* 右 `subst ?[^&0] (iT 1 (^∀ X))`
  = `subst ?[^&0] (^∀ (imp domZero (iT 2 X)))`        -- iT_all
  = `^∀ (subst (qVec ?[^&0]) (imp domZero (iT 2 X)))`  -- substs_all
  = `^∀ (imp (subst (qVec ?[^&0]) domZero) (subst (qVec ?[^&0]) (iT 2 X)))`  -- substs_and/or
  记 `B := subst (qVec ?[^&0]) (iT 2 X)`

**第一分量**：`domZero` vs `subst (qVec ?[^&0]) domZero`——
**`subst_qVec_domZero'` 已证两者相等**（exit 0）✅

**第二分量**：`A = iT 1 (subst (qVec ?[^&0]) X)` vs `B = subst (qVec ?[^&0]) (iT 2 X)`。

**这正是 `iT_substs1_qVec` 的形状**（层数 1 vs 2、向量 `qVec ?[^&0]`），
但它**就是 `iT_substs1` 本身在 `X` 上、层数 +1**——
所以 `all` 支**可以用「`iT_substs1` 的归纳假设」在 `X` 上、层数 1** 关掉，
**前提是 `iT_substs1` 的归纳是「对层数也归纳」的**。

**本探针只把两侧推到 `imp`/`subst` 层，确认第一分量已消。** -/
example {X : V} (hX : IsSemiformula ℒₒᵣ (2:V) X) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^∀ X))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^∀ X)) := by
  rw [Bootstrapping.substs_all (L := ℒₒᵣ) hX.isUFormula]
  rw [show iT (0:V) (^∀ (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) X))
        = (^∀ (imp ℒₛₑₜ domZero
            (iT (0 + 1 : V) (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) X))) : V)
      from iT_all (n := (0:V))
        ((IsSemiformula.subst (L := ℒₒᵣ) hX ?_).isUFormula)]
  rw [iT_all (n := (1:V)) hX.isUFormula]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ)
      (IsUFormula.imp.mpr ⟨isUFormula_domZero2, (isSemiformula_iT (n := (2:V)) _ hX).isUFormula⟩)]
  trace_state
  sorry

end GodelQ.ProbeFL
