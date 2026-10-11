import GodelQ.ZFC.CG008CrossLanguage

/-!
# CG-008 · 解释墙：为什么 `of_provability` 填不了缺口

## `of_provability` 的证明机制（`LK/Interpretation.lean:443`）

```lean
lemma of_provability {σ : Sentence L₂} (h : U ⊢ σ) : T ⊢ π.translate σ := by
  apply Theory.Proof.complete_on_eq_models.{_, 0}
  intro M _ _ _ hT
  exact Model.translate_iff.mpr <| models_of_provable (π.model_models_theory hT) h
```

**关键**：证明走的是 `complete_on_eq_models`——**完备性定理**。
即：为了得到「`T ⊢ π.translate σ`」，它验证「`T` 的每个模型都满足 `π.translate σ`」，
然后引用完备性。

**这是语义论证**：它不构造任何证明对象。

## 为什么这对缺口是致命的

缺口（`CG008HBL3.lean`）要的是

```
∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)
```

即一个 **𝗜𝚺₁ 内部的证明**（`⊢` 是语法对象，`𝗜𝚺₁` 是算术理论）。
展开 `zfcTr`，这需要「**一个 𝗭𝗙𝗖 的证明编码**」（`provable 𝗭𝗙𝗖` 的见证 `d : V`）。

而 `of_provability` 给的是**外部**的 `T ⊢ π.translate σ`——
它有一个证明对象，但那个证明是**元层的**，**不产生 V 内部的编码**。

**这正是 `Z0Bridge.lean` 的注释已经指出的**（第 20-21 行）：
「Foundation 的 `DirectInterpretation.of_provability`（`LK/Interpretation.lean`）
只把**外部**推导经完备性变成另一条外部推导，不产生非标准模型 V 里的证明编码。」

## 本文件的价值

把这一点**机器化**并接到本轮的结构图景上：

- `of_provability` 的**类型**是可用的（本文件查实）；
- 但它的**证明机制**（完备性）意味着它无法提供缺口要的**语法编码**；
- 所以缺口不能靠「调用 `of_provability`」关闭——
  它需要**在 𝗜𝚺₁ 内部形式化解释**，即 `CrossLanguageD3` 那个位置。

**这是「解释墙」**：解释（interpretation）在元层是有的、且已机器化；
但缺口的 D3 要在**系统内**做同一件事，而 `of_provability` 的证明方式
（走完备性）恰恰说明 Foundation 没有系统内的版本。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008InterpretationWall

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`of_provability` 的类型——**元层**的解释传递。

`π : T₁ ⊳ T₂` 是直接解释，它把 `T₂` 的定理搬到 `T₁`。
**结论是元层的 `⊢`**，不是 V 内部的编码。 -/
example {L₁ L₂ : Language} [L₁.Eq] [L₂.Eq] {T₁ : Theory L₁} {T₂ : Theory L₂}
    [𝗘𝗤 _ ⪯ T₁] (π : T₁ ⊳ T₂) {σ : Sentence L₂} (h : T₂ ⊢ σ) :
    T₁ ⊢ π.trln.translate σ :=
  π.of_provability h

/-- **查实 2（对照）**：缺口要的是**系统内**的 D3——`CrossLanguageD3` 那个位置。

两者的差别：
- `of_provability`：`T₂ ⊢ σ`（元层）→ `T₁ ⊢ translate σ`（元层）；
- 缺口：`V ⊨ zfcTr σ`（V 内部）→ `V ⊨ zfcTr (zfcTr σ)`（V 内部）。

**前者是元层的定理搬运，后者是 V 内部的自指**。
`of_provability` 的证明走完备性（语义），所以它**给不出** V 内部的编码。 -/
example :
    CrossLanguageD3 (T₀ := 𝗜𝚺₁) (T := Sh) zfcTr
        (fun σ : ArithmeticSentence ↦
          (provable 𝗭𝗙𝗖).val/[⌜arithTrln.translate (zfcTr σ)⌝]) ↔
      ∀ σ : ArithmeticSentence, 𝗜𝚺₁ ⊢ zfcTr σ 🡒
        (provable 𝗭𝗙𝗖).val/[⌜arithTrln.translate (zfcTr σ)⌝] :=
  gap_is_cross_language_D3

end GodelQ.CG008InterpretationWall
