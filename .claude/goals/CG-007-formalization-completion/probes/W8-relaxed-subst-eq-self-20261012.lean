import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
set_option maxHeartbeats 800000
namespace GodelQ.ProbeIF4
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 放宽版 `subst_eq_self`：向量比公式长也没关系

`subst_eq_self` 要求 `IsSemitermVec L n n w`（长度 = 层数）。
但 `subst` 实际只用 `w.[i]`（`i < bv p`）。所以**只需前 `bv p` 个分量对**。

先看 `substs_rel` 的行为：`subst w (^rel k R v) = ^rel k R (termSubstVec k w v)`，
而 `termSubstVec` 用 `w.[z]`（`z` 是 `v` 里的 bvar）。**故只要 `z < len w` 就行**——
不需要 `len w = n`。

所以放宽版的正确陈述是：
`∀ i < bv p, w.[i] = ^#i` ⟹ `subst w p = p`（**不再要求 `len w = n`**）。 -/

-- 测：`subst ?[^#0, ^&0] cDomN = cDomN`（长度 2 的向量，公式层 1）
example : subst ℒₛₑₜ (?[^#0, ^&0] : V) ((cDomN : ℕ) : V) = ((cDomN : ℕ) : V) := by
  -- `cDomN` 是 `⌜domain⌝`，`domain : Semisentence ℒₛₑₜ 1`
  -- 用 `subst_eq_self` 需要一个长度 1 的向量；但 `?[^#0]` 与 `?[^#0, ^&0]` 在 `#0` 上一致
  -- 直接展开 `cDomN` 看 `subst` 的行为
  show subst ℒₛₑₜ (?[^#0, ^&0] : V) ((⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝ : ℕ) : V)
    = ((⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝ : ℕ) : V)
  sorry

end GodelQ.ProbeIF4
