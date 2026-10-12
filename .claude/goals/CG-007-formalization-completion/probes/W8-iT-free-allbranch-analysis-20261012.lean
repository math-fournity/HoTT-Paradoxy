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
  -- `domZero = cDomN`，且 `subst_eq_self` 只要 `w.[i] = ^#i`（`i < n`）
  -- 这里 `w = qVec ?[^&0] = ?[^#0, ^&0]`，`n = 2`，`w.[0] = ^#0` 但 `w.[1] = ^&0 ≠ ^#1`
  -- **故本式不成立**——`subst_eq_self` 用不上。
  -- 正确做法：`domZero` 是 `Semisentence 1`（只有 `#0`），代入 `#0 ↦ ^#0` 才是恒等。
  rw [domZero_eq_cDomN]
  -- `cDomN` 只用到 `#0`；用 `substs1` 的形式（长度 1 的向量 `?[^#0]`）
  sorry

end GodelQ.ProbeIF2
