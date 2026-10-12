import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeFreeJ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 更正探针：`free` 在 `hAll` 的真实层级上**不越界**

上一探针测的是 `subst ?[^&0] (^rel 2 cEqN ?[^#0,^#1])`——**层级不对**。
`hAll` 里 `free` 作用在 `iT 1 p` 上，而 `iT 1 p` 的外层是 `qqAlls · 2`。
`subst` 推过 `qqAlls` 时向量变成 `qVec² ?[^&0] = ?[^#0, ^#1, ^&0]`（长度 3），
**足以覆盖 `#1`**。所以内层代入是良构的。

本探针测**正确的组合**：`subst` 推过两层 `qqAlls` 后向量变成什么。 -/

-- 内层代入在长度 3 的向量下**不越界**：`?[^#0,^#1]` 两个下标都 < 3
example : termSubstVec ℒₛₑₜ 2 (?[^#0, ^#1, ^&0] : V) (?[^#0, ^#1] : V)
    = (?[^#0, ^#1] : V) := by
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V)))]
  simp [termSubst_bvar]

end GodelQ.ProbeFreeJ
