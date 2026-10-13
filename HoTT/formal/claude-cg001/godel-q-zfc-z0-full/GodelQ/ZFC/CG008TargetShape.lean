import GodelQ.ZFC.CG008SingleInstance
import GodelQ.ZFC.CG008MinimalGapSuffices

/-!
# CG-008 · 靶心的最终形状（与 002-Step 的收窄合成）

两条收窄来自两个方向，本文件把它们**合成一条陈述**并机器核对
「哪一条更强」。

## 两条收窄

| # | 收窄 | 出处 | 状态 |
|---|---|---|---|
| A | `AxStep_induction` 的墙**全在非标准码**（标准码支已付清） | `CG008InductionBody.axStep_standard_code` / `axStep_induction_reduces` | 已证 |
| B | Z0 只需**一条** D3 实例（在 Gödel 句 `𝐆` 上），不需整族 `∀σ` | `CG008SingleInstance.zfc_z0_full_of_single` | 已证（002-Step） |

## 合成的关键核对：`𝐆` 是**标准**码

`gödel`（`ProvabilityAbstraction/Basic.lean:188`）是**元层定义**：

```lean
def gödel (𝔅 : Provability T₀ T) : Sentence L :=
  fixedpoint T₀ “x. ¬!𝔅.prov x”
```

所以 `𝐆` 是一个**元层句子**，`⌜𝐆⌝` 是**标准**码。

**于是 A 与 B 合成后，靶心并不是「非标准码」**：
B 要的那条实例的 `σ` 是 `𝐆`——**标准**的。
而 A 说的是「`AxStep` 的标准码支已付清」。

## 但两者不冲突：`AxStep` 与 D3 是**不同形状**

- `AxStep` 说的是「**`p ∈ 𝗜𝚺₁.Δ₁Class` 的码**在 `iT 0` 下可证」——
  `p` 遍历的是**公理码**，可以是**非标准**的；
- B 说的是「`𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)`」——这是一个**𝗜𝚺₁ 定理**，
  其证明可以（且必须）用到 `𝐆` 的**非标准**公理码吗？

**关键问题**：`AxStep` 是 `HBL3` 的**证明手段**（经 `Fixpoint.induction` 的归纳步），
而 B 是 `HBL3` 的**使用方式**（只需一句）。两者在**不同的位置**：
- B 减少的是「**需要多少 D3**」；
- A 减少的是「**证一条 D3 需要什么**」。

**所以合起来是**：要证**一条** D3 实例（B），而证它（经 `Fixpoint.induction`）
时**只有非标准公理码那一支**是障碍（A）。**两个收窄正交，可以叠加。**

## 本文件机器化的内容

把「B 的 `σ` 是标准码」这件事**明确固定**（`godel_is_standard`），
以免后续工作单元误以为「B 的收窄已经绕开了非标准码」。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含未证标记，可进入收据。
- **不声称缺口已证**；`Z0Blocked.lean:65` 的未证标记仍在。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008TargetShape

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate

variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`𝐆` 是标准码**：`gödel` 是元层定义（`Basic.lean:188`），
所以 `⌜𝐆⌝` 是 V 里的标准元素——`AxStep_induction` 的「非标准」不指它。

**这条的作用**：标明 B 的收窄（只需一句）**没有**绕开 A 的墙（非标准公理码）；
两者在不同的位置。 -/
theorem godel_is_standard :
    ∃ σ : Sentence ℒₒᵣ, (⌜gödel (T₀ := 𝗜𝚺₁) zfcTr⌝ : V) = ⌜σ⌝ :=
  ⟨gödel (T₀ := 𝗜𝚺₁) zfcTr, rfl⟩

/-- **合成的靶心（本文件的主陈述）**：Z0 完整形式 ⟸
「`𝐆` 上的 D3 实例」——**一条**，且**经 `Fixpoint.induction` 证它时只剩非标准公理码支**。

本定义只是把 A 与 B 的合取写清楚，**不声称它已证**。 -/
def FinalTarget : Prop :=
  ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
    𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr))

/-- **B 的方向已机器化**（引用 002-Step 的定理，不重复证明）：
`FinalTarget` 一旦成立，Z0 完整形式立即成立。

注意这里用的是 `CG008SingleInstance` 的单实例定理，
所以**不需要整族 `MinimalGap`**。 -/
theorem z0_of_finalTarget (h : FinalTarget) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  GodelQ.CG008SingleInstance.zfc_z0_full_of_single (h ℕ)

/-- **A 与 B 的关系（本文件的核对结论）**：`MinimalGap` ⟹ `FinalTarget`。

**单向**：整族 D3（`MinimalGap`）给出单实例（`FinalTarget`），
因为 `FinalTarget` 就是 `MinimalGap` 在 `V` 与 `σ := 𝐆` 处的实例
（经 `models_zfcTr_iff` 的语义读法）。**反向不成立**——这是 B 的收窄内容。 -/
theorem finalTarget_of_minimalGap (h : GodelQ.CG008FleetGap.MinimalGap) :
    FinalTarget :=
  fun _ _ _ ↦ GodelQ.CG008MinimalGapSuffices.hD3G_of_minimalGap h

end GodelQ.CG008TargetShape

#print axioms GodelQ.CG008TargetShape.godel_is_standard
#print axioms GodelQ.CG008TargetShape.z0_of_finalTarget
#print axioms GodelQ.CG008TargetShape.finalTarget_of_minimalGap
