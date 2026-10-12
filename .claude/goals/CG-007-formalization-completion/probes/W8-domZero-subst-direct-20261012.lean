import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeIF3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **直接测**：`subst (qVec ?[^&0]) domZero = domZero` 到底成不成立？
example : subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN]
  -- `cDomN = ⌜domain⌝`，`domain : Semisentence ℒₛₑₜ 1`——只有 `#0` 是自由的
  -- 故 `subst w cDomN` 只看 `w.[0] = ^#0`，对 `#0 ↦ ^#0` 是恒等
  -- 试 `subst_eq_self` 的变体：先 `show` 成 `?[^#0]` 向量
  have hw : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
    rw [qVec, show len (?[^&0] : V) = 1 from by simp,
      termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]
  rw [hw]
  -- `cDomN = ⌜domain⌝`，`domain : Semisentence ℒₛₑₜ 1`。
  -- 用 `quote_substs`：`subst w ⌜φ⌝ = ⌜φ ⇜ w'⌝`，其中 `w'` 是 `w` 的项向量形式。
  -- 关键：`?[^#0, ^&0]` 的前 1 个分量是 `^#0`，正是 `domain` 需要的。
  show subst ℒₛₑₜ (?[^#0, ^&0] : V) ((cDomN : ℕ) : V) = ((cDomN : ℕ) : V)
  -- 用 `subst_eq_self` 的**放宽版**：只需前 `bv p` 个分量对
  -- 这里 `bv cDomN = 1`，而 `?[^#0, ^&0]` 的 `.[0] = ^#0` ✓
  sorry

end GodelQ.ProbeIF3
