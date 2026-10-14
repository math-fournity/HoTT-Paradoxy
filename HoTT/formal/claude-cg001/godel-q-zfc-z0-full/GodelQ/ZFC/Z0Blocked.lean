import GodelQ.ZFC.Z0Full

/-!
# CG-007 · W8：唯一的阻塞引理（未证，不作为收据源）

`Z0Full.lean` 证明了：除了 Hilbert–Bernays 可导性条件 D3 之外，Z0 的完整形式
`𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗼.consistent)ᵗ` 的全部前提都已具备。本文件把 D3 逐字写成一条 Lean 命题。

它带 `sorry`，因此**不是**任何运行收据的编译源（`zfc_lean_check.py` 会拒绝 `sorry`）；
它存在的目的是把“还差什么”固定成一条可以交给下一个工作单元、也可以交给外部复核的精确命题。

内容见命题的 docstring。`Z0Full.zfc_z0_full_of_D3_internalize` 表明：这条引理一旦成立，
完整形式立即随之成立。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.Z0Blocked

/-- **阻塞引理（D3 的唯一实质内容）**：在 𝗜𝚺₁ 的每个模型 V 中，
`𝗭𝗙𝗖 ⊢ ⌜σᵗ⌝ → 𝗭𝗙𝗖 ⊢ ⌜(zfcTr σ)ᵗ⌝`，即“𝗭𝗙𝗖 证明了 σ 的翻译，就也能证明
‘𝗭𝗙𝗖 证明 σ 的翻译’这句话的翻译”。

Foundation 的 `of_provability`（`LK/Interpretation.lean:443`）用完备性定理**语义地**证明
`U ⊢ σ → T ⊢ π.translate σ`；它不经过一条可搬进 𝗜𝚺₁ 的语法证明翻译。本文件没有证明这条引理。
它是 `zfcTr.HBL3`（D3）的唯一实质内容；`zfc_z0_full_of_D3_internalize` 表明它一旦成立，
Z0 的完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 立即随之成立。

## ⚠ 2026-10-14 路线判定：**没有捷径，三条候选路都已机器核验**

本会话（9276-W8-D3）把 D3 的三条候选路都走到底并机核验，**结论是没有捷径**：

| 候选路 | 关键件 | 判定 |
|---|---|---|
| 语义/完备性 | `SetTheory.complete` + `models_iff_provable_of_Sigma0_param` | ❌ **循环**：后者要 `[T.SoundOnHierarchy 𝚺 1]`，而该 instance 蕴含 `Consistent T`（`FirstOrder/Arithmetic/Basic/Hierarchy.lean:189`）——用「𝗭𝗙𝗂 一致」证「𝗭𝗙𝗂 一致」的反命题。机核验 exit 0：`sound_on_hierarchy_implies_consistent` |
| Foundation 现成 D3 | `provable_internalize`（`DerivabilityCondition/D3.lean:175`） | ❌ **对 `T := Sh` 用不了**：要 `[Theory.Δ₁ T]`，而 `#synth Theory.Δ₁ Sh` **失败**（本线与 012-Flash 双方独立机核验一致）。改 `T := 𝗜𝚺₁` 也不行：`provabilityPred 𝗜𝚺₁ σ` 与 `zfcTr σ` **是不同的谓词**（前者「σ 在 𝗜𝚺₁ 可证」，后者「σ 的翻译在 𝗭𝗙𝗂 可证」） |
| 反向引理（码 → 引号） | `IsSemiformula → ∃ φ, p = ⌜φ⌝` | ❌ **为假**：`IsUFormula` 是 `Fixpoint`，非标准模型里含非标准元素。Foundation 的 `IsSemiformula.sound`（`Formula/Coding.lean:478`）载体是 `ℕ`——「限定在 ℕ」是**本质的**，不是待推广 |

### 为什么 `Theory.Δ₁ Sh` 建不起来（= 显式义务）

`Theory.Δ₁`（`Syntax/Theory.lean:16`）要 `ch : 𝚫ᴬ₁.Semisentence 1`，即 **Σ₁ 且 Π₁**：

* **Σ₁ 侧（已有）**：`trProv`（`Z0Full.lean:40`）= `∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗂 y`；
* **Π₁ 侧（义务，未证）**：`¬∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗂 y` 的 Π₁ 定义。

**Π₁ 侧的数学内容** = 「`x` 的翻译在 𝗭𝗙𝗂 中**不可证**」要在 𝗜𝚺₁ 内有 Π₁ 表示。
而 D3 说的正是「**可证性**能被内部表示」——故 **Π₁ 侧与 D3 是同一件难事**
（012-Flash 独立判断一致）。**⟹ Foundation 的 D3 路线对 `T := Sh` 是循环的。**

### 两个已澄清的误区（别再重复）

1. **`Sh.RE` 是白送的**：`#synth Theory.RE Sh` ✅（`Sh_RE`）。
   本文档旧版与 `Z0Shadow.lean:14-17` 把 `Sh.RE` 记为「未证条件」**已过时**
   （W4b 证了 `translate_computable` 之后它就是现成件）。**卡点不是 `Sh.RE`。**
2. **Foundation 没有 `Theory.Δ₁_of_RE`**：全库 grep 过，全部 Δ₁ 构造子里
   没有一个从 `T.RE` 出发。`T.craig` 那条虽假设 `[T.RE]`，但产出的是
   `(T.craig).Δ₁` 而非 `T.Δ₁`——它换了个理论，绕过去而非建出来。

## 剩下的唯一方向

**直接在 ℒₛₑₜ 里构造该蕴含的 𝗭𝗙𝗖 推导**（即语法路线的 `iT_substs1` 型一般律，
与 `AllBlocker`/`ExsBridge2` 同族），或把
「`Theory.Δ₁ Sh` 的 Π₁ 侧」作为**独立的显式义务**交还。 -/
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  sorry

end GodelQ.Z0Blocked
