import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 10（**不是收据**）：`Theory.Δ₁ Sh` 的建法——Σ1 → 𝚫 的一步到底缺什么。

探针 9 已定：`trProv : {Γ := 𝚺, rank := 1}.Semisentence 1`（`𝚺ᴬ₁-Predicate TrProvable`）、
`iT` 是 `{Γ := 𝚺, rank := 1}-Function₂`。所以"`x` 的翻译可证"整体是 **Σ1**。

`Theory.Δ₁` 要 `ch : 𝚫ᴬ₁.Semisentence 1`，即同时有 Σ 与 Π 两侧。**Π 侧缺。**

## 有没有现成的 Σ → 𝚫 提升件？

本探针在 Foundation 里找"(X → Σᴬ₁) ⟹ X → 𝚫ᴬ₁"这形状的引理。已知候选方向：
1. `Hierarchy.le_succ` 之类（层级单调）——那只给 Σ₁ ⊆ Σ₂，不给 𝚫。
2. **`Hierarchy.le_zero_succ_of_neg`** 之类：若 `p` 是 Σ0 且 `¬p` 是 Σ1，则 `p` 是 𝚫1。
   `¬(TrProvable x)` 是不是 Σ1？那是"不存在 𝗭𝗙𝗖 推导"，**Σ1 不可**（要 Π1 才行）。
3. `Arithmetic.sigmaOne_delta1_iff` 之类：Σ1 谓词若是"绝对"的则可能 𝚫1。

## 诚实的结论方向

若 `TrProvable` 的否定不是 Σ1，则 `Theory.Δ₁ Sh` **原则性建不出**（不是技术困难）。
但这不影响：我们的目标只是 **D3**（`zfcTr σ → zfcTr (zfcTr σ)`），
而 Foundation 的 `provable_internalize` 只是 D3 的一条**现成捷径**，不是唯一路径
——`Z0Full.lean:121-133` 的 `zfc_z0_full_of_D3_internalize` 显式接受 D3 为假设。

本探针逐条 `#check` 上面三个候选，看有没有能用的。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeD1Sh3

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 候选 1：Σ → 𝚫 的一般提升件
#check @Hierarchy.le_succ
#check @Hierarchy.le_zero_succ_of_neg
#check @Hierarchy.le_of_le_of_lt

-- 候选 2：(𝚺ᴬ₁-Predicate p) → (𝚫ᴬ₁-Predicate p)？
#check @HierarchySymbol.Predicate.arithmetic

-- 候选 3：Σ1 谓词的否定仍是 Σ1 吗（这决定 𝚫1 可行性）
#check @Negation.delta1

-- 现成参照：Foundation 自己的 provability 谓词是 𝚺 还是 𝚫？
#check @provabilityPred
#check @tprovable

end GodelQ.ProbeD1Sh3
